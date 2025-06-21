import os

from jinja2 import Environment, FileSystemLoader

from foundation.nDisplay.common.flattener import Flattener
from foundation.nDisplay import NDISPLAY_MODULE_DIR, info


class THREEMeshClassGenerator:

    def __init__(self, verbose=False):
        self.verbose=verbose
        #read the configuration file for standard functions
        self.templateFolder = os.path.join(NDISPLAY_MODULE_DIR, 'sampler', 'genTHREEMesh', 'template')
        # self.outputFolder = os.path.join(NDISPLAY_MODULE_DIR, 'sampler', 'genTHREEMesh', 'THREEMesh')
        self.outputFolder = os.path.join(NDISPLAY_MODULE_DIR, 'three', 'public', 'static', 'meshes')
        if not os.path.isdir(self.outputFolder):
            os.makedirs(self.outputFolder)

    def generateMeshFile(self, meshName, coordinates, indices, colors):
        templateName = "Mesh~.js.jinja2"
        environment = Environment(loader=FileSystemLoader(self.templateFolder))
        meshJSTemplate = environment.get_template(templateName)
        #flatten coordinates
        coordindates = Flattener.flatten(coordinates)
        #flatten indices
        indices = Flattener.flatten(indices)# these are indices of coordinates, grouped to form triangles
        #flatten colors
        colors = Flattener.flatten(colors)#these are RGB_colors for each triangle in indices
        meshJSContent = meshJSTemplate.render({
            'coordinates':coordindates,
            'indices':indices,
            'colors':colors,
            'className':meshName
        })
        fileName = templateName.replace('~', meshName).replace('.jinja2', '')
        self.writeToFile(fileName, meshJSContent, verbose=self.verbose)


    def writeToFile(self, filename, content, verbose=False):
        #we fix the filepath here:
        filepath = os.path.join(self.outputFolder, filename)#
        with open(filepath, mode='w', encoding='utf-8') as file:
            file.write(content)
            if verbose:
                info(f"written {directory}  {filename}")

