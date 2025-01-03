import os

from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

from foundation.automat import AUTOMAT_MODULE_DIR
from foundation.automat.log import info
from foundation.automat.arithmetic.configuration.oneargumentconfiguration import FUNC_NAMES



class Standardconfigoneargument:


    @classmethod
    def generateConfigurations(cls, verbose=False, toRun=None):
        #copied from https://realpython.com/primer-on-jinja-templating/
        environment = Environment(loader=FileSystemLoader(os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'generator', 'template', 'configuration')))
        template = environment.get_template("standardoneargument.yaml.jinja2")

        for function_name, mapping in FUNC_NAMES.items():
            if toRun is not None and function_name != toRun:
                continue # skip
            vorfname = function_name
            vorcname = mapping['class_name']
            hinfname = mapping['reverse_prefix']+function_name
            hincname = cls.upperFirstLetter(mapping['reverse_prefix']+vorcname.lower())
            importList = ["from foundation.automat.arithmetic.function import Function"]
            vorcontent = template.render(
                function_name=vorfname,
                class_name=vorcname,
                reverse_class_name=hincname,
                # imports=str(["from foundation.automat.arithmetic.function import Function"]).replace("'", '"'),
                imports__toString=str(os.linesep.join(map(lambda importStr: cls._template__imports(importStr), importList))),
                # reverse_imports=str([f"from foundation.automat.arithmetic.standard.{hincname.lower()} import {hincname}"]).replace("'", '"'),
                reverse_imports__toString=str(os.linesep.join(map(lambda reverseImportStr: cls._template__reverse_imports(reverseImportStr), [f"from foundation.automat.arithmetic.standard.{hincname.lower()} import {hincname}"]))),
                # imports_as_str=str(mapping['import']).replace("'", '"'),
                imports_as_str__toString=str(os.linesep.join(map(lambda imports_as_str: cls._template__imports_as_str(imports_as_str), mapping['import']))),
                code_as_str=str(mapping['code']).replace("'", '"'),
            )
            cls.writeToFile(f'{vorfname}.yaml', vorcontent, verbose=verbose)
            hincontent = template.render(
                function_name=hinfname,
                class_name=hincname,
                reverse_class_name=vorcname,
                # imports=str(["from foundation.automat.arithmetic.function import Function"]).replace("'", '"'),
                imports__toString=str(os.linesep.join(map(lambda importStr: cls._template__imports(importStr), importList))),
                # reverse_imports=str([f"from foundation.automat.arithmetic.standard.{vorcname.lower()} import {vorcname}"]).replace("'", '"'),
                reverse_imports__toString=str(os.linesep.join(map(lambda reverseImportStr: cls._template__reverse_imports(reverseImportStr), [f"from foundation.automat.arithmetic.standard.{vorcname.lower()} import {vorcname}"]))),
                # imports_as_str=str(mapping['reverse_import']).replace("'", '"'),
                imports_as_str__toString=str(os.linesep.join(map(lambda imports_as_str: cls._template__imports_as_str(imports_as_str), mapping['reverse_import']))),
                code_as_str=str(mapping['reverse_code']).replace("'", '"'),
            )
            cls.writeToFile(f'{hinfname}.yaml', hincontent, verbose=verbose)

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
    def _template__imports(cls, importStr):
        return f'- {importStr}'

    @classmethod
    def _template__imports_as_str(cls, imports_as_str):
        return f'  - {imports_as_str}'

    @classmethod
    def _template__reverse_imports(cls, reverseImportStr):
        return f'    - {reverseImportStr}'
