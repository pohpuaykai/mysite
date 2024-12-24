import os

from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

from foundation.automat import AUTOMAT_MODULE_DIR, info


class Patternate:
    """
    generate class files in folder `pattern` from the configuration file

    """

    def __init__(self, verbose):
        self.verbose = verbose
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        self.pformat = pp.pformat
        self.manipulateConfigFileFolder = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate','configuration')

    def generateClass(self, toRun=None):

        #copied from https://realpython.com/primer-on-jinja-templating/
        environment = Environment(loader=FileSystemLoader(os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate', 'generator', 'template')))# put in the full directory
        for filename in os.listdir(self.manipulateConfigFileFolder):
            if filename.endswith('.yaml'): # then its good! sei vorsichtung um nicht zu non-configuration-files zu beitragen
                if toRun is not None and filename != toRun+'.yaml':
                    continue # skip this file
                if self.verbose:
                    info(f'processing {filename}')
                config = self._loadYAMLFromFilePath(os.path.join(self.manipulateConfigFileFolder, filename))
                if self.verbose:
                    info(config)

                #fill template for pattern
                mainFTemplate = environment.get_template("manipulate.py.jinja2")

                renderedMainFTemplate = mainFTemplate.render({
                    'type':config['type'],
                    'className':config['className'],
                    'manipulations':config['manipulations'],
                    'imports':['from foundation.automat.core.manipulate.manipulate import Manipulate']
                })
                fileName = f"{config['className'].lower()}.py"
                self.writeToFile(fileName, renderedMainFTemplate)



    def writeToFile(self, filename, content):
        #we fix the filepath here:
        directory = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate', 'pattern')
        with open(os.path.join(directory, filename), mode='w', encoding='utf-8') as file:
            file.write(content)
            if self.verbose:
                info(f"written {directory}  {filename}")


    def _loadYAMLFromFilePath(self, filepath):
        with open(filepath, 'r') as f:
            data = safe_load(f)
            return data