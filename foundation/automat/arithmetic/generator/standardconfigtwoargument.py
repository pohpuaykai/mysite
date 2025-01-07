import os

from jinja2 import Environment, FileSystemLoader
from yaml import safe_load, dump

from foundation.automat import AUTOMAT_MODULE_DIR
from foundation.automat.log import info
from foundation.automat.arithmetic.configuration.twoargumentconfiguration import FUNC_NAMES



class Standardconfigtwoargument:


    @classmethod
    def generateConfigurations(cls, verbose=False, toRun=None):
        # #copied from https://realpython.com/primer-on-jinja-templating/
        environment = Environment(loader=FileSystemLoader(os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'generator', 'template', 'configuration')))
        template = environment.get_template("standardtwoargument.yaml.jinja2")

        template__reverse = environment.get_template("standardtwoargument_reverse.yaml.jinja2")

        for function_name, mapping in FUNC_NAMES.items():
            print(function_name, toRun, function_name!=toRun)
            if toRun is not None and function_name != toRun:
                continue # skip
            #default_style=None: Ensures PyYAML quotes the string only when necessary
            #explicit_end=False: Prevents the ellipsis (...) from being added to the output
            fname = cls.escapeYAMLSpecialCha(mapping['funcName']) # to escape the - (minus)
            cname = mapping['className']
            importList = ["from foundation.automat.arithmetic.function import Function"]
            reversedAsts = []
            for rd in mapping['reversedAsts']:
                #rd['permutation'] is only good for shifting of nodeIds around
                transformed_className = list(rd['function'].values())[0]
                if transformed_className.lower() == function_name:
                    convertedClassName = None
                    importStrs = []
                else:
                    convertedClassName = transformed_className
                    importStrs = [f"from foundation.automat.arithmetic.standard.{convertedClassName.lower()} import {convertedClassName}"]
                reverse__content = template__reverse.render(
                    transformed_className=transformed_className,
                    equationSide=rd['equationSide'],
                    t00=(lambda tup: f'{tup[0]}_{tup[1]}')(rd['permutation'][(0, 0)]),
                    t01=(lambda tup: f'{tup[0]}_{tup[1]}')(rd['permutation'][(0, 1)]),
                    t10=(lambda tup: f'{tup[0]}_{tup[1]}')(rd['permutation'][(1, 0)]),
                    t11=(lambda tup: f'{tup[0]}_{tup[1]}')(rd['permutation'][(1, 1)]),
                    argumentIdx=rd['argumentIdx'],
                    functionCountAdd__toString=cls._template__reverseAsts__functionCountAdded(convertedClassName),
                    imports__toString=cls._template__reverseAsts__imports(importStrs),
                    #for startPos__nodeId
                    # needs special care when you deserialise
                    permutation=cls.addSpacesBeforeEveryLine(
                        dump({'permutation':list(map(lambda item: [list(item[0]), list(item[1])], rd['permutation'].items()))}),
                        spacesCount=4
                    )
                )
                reversedAsts.append(reverse__content)
            content = template.render(
                function_name=fname,
                class_name=cname,
                imports__toString=dump(importList),
                return_calculations=dump(mapping['return_calculations']),
                reversedAsts=reversedAsts
            )
            cls.writeToFile(f'{function_name}.yaml', content, verbose=verbose)


    @classmethod
    def upperFirstLetter(cls, word):
        word = str(word).lower()
        upperedWord = word[0].upper() + word[1:].lower()
        return upperedWord

    @classmethod
    def writeToFile(cls, filename, content, verbose=False):
        #we fix the filepath here:
        directory = os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'configuration', 'standard')
        with open(os.path.join(directory, filename), mode='w', encoding='utf-8') as file:
            file.write(content)
            if verbose:
                info(f"written {content} {os.linesep} {filename} to {directory}")


    @classmethod
    def _loadYAMLFromFilePath(cls, filepath):
        with open(filepath, 'r') as f:
            data = safe_load(f)
            return data


    @classmethod
    def _template__reverseAsts__functionCountAdded(cls, convertedClassName):
        tFunctionCountAdded = lambda s: f"""    functionCountAdded: {s}"""
        if convertedClassName is None: # there was no change in functionCount
            return tFunctionCountAdded(str({}))
        else:#somehow functionCount only transformed into convertedFuncName
            s = f"""
      '@cN@.@vfN@': -1
      '@cN_{convertedClassName}@.@vfN@': 1"""
            return tFunctionCountAdded(s)


    @classmethod
    def _template__reverseAsts__imports(cls, importStrs):
        tImports = lambda s: f"""    imports: {s}"""
        if len(importStrs) > 0:
            s = ''.join(list(map(lambda importStr: f"{os.linesep}    - {importStr}", importStrs)))
            return tImports(s)
        return tImports(importStrs)


    @classmethod
    def addSpacesBeforeEveryLine(cls, dumpStr, spacesCount):
        prefixSpaces = ' ' * spacesCount
        return os.linesep.join([prefixSpaces + line for line in dumpStr.splitlines()])


    @classmethod
    def escapeYAMLSpecialCha(cls, s):
        s = dump(s, default_style=None, explicit_end=False).strip()
        if s.endswith('...'):#what if s originally had ...? TODO
            return s[:-4]
        return s