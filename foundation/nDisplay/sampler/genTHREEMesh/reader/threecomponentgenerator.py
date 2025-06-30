import os

from jinja2 import Environment, FileSystemLoader

from foundation.nDisplay.common.flattener import Flattener
from foundation.nDisplay import NDISPLAY_MODULE_DIR, info

class THREEComponentGenerator:
    
    def __init__(self, verbose=False):
        self.verbose=verbose
        #read the configuration file for standard functions
        self.templateFolder = os.path.join(NDISPLAY_MODULE_DIR, 'sampler', 'genTHREEMesh', 'template')
        # self.outputFolder = os.path.join(NDISPLAY_MODULE_DIR, 'sampler', 'genTHREEMesh', 'THREEMesh')
        self.outputFolder = os.path.join(NDISPLAY_MODULE_DIR, 'three', 'public', 'static', 'meshes')
        if not os.path.isdir(self.outputFolder):
            os.makedirs(self.outputFolder)

    def generateMeshFile(self, meshName, type, listOfCoordinates, listOfIndices, listOfColors, solderableLeads):
        templateName = "Component~.js.jinja2"
        environment = Environment(loader=FileSystemLoader(self.templateFolder))
        meshJSTemplate = environment.get_template(templateName)
        #flatten coordinates
        listOfCoordinates___new = []
        for coordinates in listOfCoordinates:
            listOfCoordinates___new.append(Flattener.flatten(coordinates))
        listOfCoordinates = listOfCoordinates___new
        #flatten indices
        listOfIndices___new = []
        for indices in listOfIndices:
            listOfIndices___new.append(Flattener.flatten(indices))# these are indices of coordinates, grouped to form triangles
        listOfIndices = listOfIndices___new
        #flatten colors
        listOfColors___new = []
        for colors in listOfColors:
            listOfColors___new.append(Flattener.flatten(colors))#these are RGB_colors for each vertices|indices
        listOfColors = listOfColors___new
        meshJSContent = meshJSTemplate.render({
            'type':type,
            'listOfCoordinates':listOfCoordinates,
            'listOfIndices':listOfIndices,
            'listOfColors':listOfColors,
            'className':meshName,
            'solderableLeads':solderableLeads,
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

