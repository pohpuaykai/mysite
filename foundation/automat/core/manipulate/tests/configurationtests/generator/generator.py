import os

from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

from foundation.automat import AUTOMAT_MODULE_DIR, info

class Generator:
    """
    generate test definitions in folder `pattern` from the configuration file
    """

    def __init__(self, verbose):
        self.verbose = verbose
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        self.pformat = pp.pformat
        self.manipulateConfigFileFolder = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate','configuration')

    def generateClass(self, toRun=None):
        from foundation.automat.core.manipulate.tests.configurationtests.generator.testdatum import TEST_DATUM


        #copied from https://realpython.com/primer-on-jinja-templating/
        environment = Environment(loader=FileSystemLoader(os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate', 'tests', 'configurationtests', 'generator', 'template')))# put in the full directory
        for filename in os.listdir(self.manipulateConfigFileFolder):
            if filename.endswith('.yaml'): # then its good! sei vorsichtung um nicht zu non-configuration-files zu beitragen
                if toRun is not None and filename != toRun+'.yaml':
                    continue # skip this file
                if self.verbose:
                    info(f'processing {filename}')
                config = self._loadYAMLFromFilePath(os.path.join(self.manipulateConfigFileFolder, filename))
                # if self.verbose:
                #     info(config)
                # import pdb;pdb.set_trace()
                if 'manipulations' not in config or config['manipulations'] is None:
                    continue
                # if self.verbose:
                #     info(config)

                testDatumFirstTag = filename[:filename.index('.yaml')]

                defNameTemplate = lambda infix: f"test__{infix}__configTest"
                defTemplate = environment.get_template("test_definition.py.jinja2")
                testDefinitionStrs = []
                testCallStrs = []
                for idx, manipulations in enumerate(config['manipulations']):
                    if manipulations['type'] == 'regex':
                        for direction, d in manipulations.items():
                            if direction in ['type', 'minArgs']:
                                continue
                            #import pdb;pdb.set_trace()
                            infix = f'{direction}{idx}'
                            defName = defNameTemplate(infix)
                            callStr = f'{defName}(True) # Not tested yet'
                            testCallStrs.append(callStr)
                            print(TEST_DATUM[testDatumFirstTag])
                            testDatum = TEST_DATUM[testDatumFirstTag][(direction, str(idx))]
                            inputDatum = testDatum['input']
                            renderedDefNameTemplate = defTemplate.render({
                                'defName':defName,
                                'eqs':f"'{inputDatum}' # fill it in",
                                'eqsType':'scheme',
                                'regexNum':idx,
                                'direction':direction,
                                'filename':f"{config['className'].lower()}",#filename,
                                'idx':idx,
                                'regexUsedComment':d['scheme'],
                                'returnRegexUsedComment':d['return'],
                                'className':config['className'],
                                'expected':testDatum['expected'],
                            })
                            testDefinitionStrs.append(renderedDefNameTemplate)


                #fill template for pattern
                mainFTemplate = environment.get_template("test.py.jinja2")

                renderedMainFTemplate = mainFTemplate.render({
                    'testDefinitionStrs':testDefinitionStrs,
                    'testCallStrs':testCallStrs,
                    'filename':config['className'].lower(),
                    'classname':config['className']
                })
                fileName = f"{config['className'].lower()}test.py"
                self.writeToFile(fileName, renderedMainFTemplate)



    def writeToFile(self, filename, content):
        #we fix the filepath here:
        directory = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate', 'tests', 'configurationtests')
        with open(os.path.join(directory, filename), mode='w', encoding='utf-8') as file:
            file.write(content)
            if self.verbose:
                info(f"written {directory}  {filename}")


    def _loadYAMLFromFilePath(self, filepath):
        with open(filepath, 'r') as f:
            data = safe_load(f)
            return data