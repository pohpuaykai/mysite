import os

from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

from foundation.automat import AUTOMAT_MODULE_DIR, info

class Recommend:
    """
    recommends what to do to an equation to make it 'better'
    better is 
    1. simplification
    2. transforming to make it suit another purpose, like integration

    also reads manipulation/configuration to derive meta
    information about manipulations, for heuristic searching

    #~ DRAFT ~#
    input:
    1. Equation


    """

    def __init__(self, equation, verbose=False):
        self.eq = equation
        self.manipulateConfigFileFolder = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate','configuration')


    def _deriveMetaInformation(self, rederive=False):
        """
        #~ DRAFT ~#


        read from folder meta (if available)
        if not available OR rederive=True, 
            read all the YAML from manipulate/configuration
            calculate meta-information and store it in folder meta

        :param rederive:
        :type rederive:
        """
        from foundation.automat.parser.sorte.schemeparser import Schemeparser
        metaData = []
        for filename in os.listdir(self.manipulateConfigFileFolder):
            if filename.endswith('.yaml'): # then its good! sei vorsichtung um nicht zu non-configuration-files zu beitragen
                config = self._loadYAMLFromFilePath(os.path.join(self.manipulateConfigFileFolder, filename))
                if 'manipulations' not in config or config['manipulations'] is None:
                    continue
                for idx, manipulations in enumerate(config['manipulations']):
                    if manipulations['type'] == 'regex':
                        typey = manipulations['type']
                        for direction, d in manipulations.items():
                            if direction in ['type']:
                                continue
                            iAst, iFunctions, iVariables, iPrimitives, iTotalNodeCount = Schemeparser(equationStr=d['scheme'])

                            oAst, oFunctions, oVariables, oPrimitives, oTotalNodeCount = Schemeparser(equationStr=d['return'])
                            metaData.append({#TODO sqlite database? lol OR implement your own BTree
                                'identity':{
                                    'idx':idx,
                                    'direction':direction
                                },
                                'i': {
                                    'ast':iAst,
                                    'functions':iFunctions,
                                    'variables':iVariables,
                                    'primitive':iPrimitives,
                                    'totalNodeCount':iTotalNodeCount
                                },
                                'o': {
                                    'ast':oAst,
                                    'functions':oFunctions,
                                    'variables':oVariables,
                                    'primitive':oPrimitives,
                                    'totalNodeCount':oTotalNodeCount
                                },
                                'type':typey,
                                'filename':filename[:filename.index('.')],
                                'functionsIO':set(iFunctions) - set(oFunctions), #TODO
                                'functionsOI':set(oFunctions) - set(iFunctions),
                                'variablesIO':set() - set(),
                                'variablesOI':set() - set(),
                                'primitiveIO':set() - set(),
                                'primitiveOI':set() - set()
                            })

    def getRelatedManipulateWithMetaInformation(self, searchField, searchTerm):
        """
        #~ DRAFT ~#

        :return:
        list of `Manipulate`, order by the most likely on the top of the list
        :rtype:list[`Manipulate`]
        """
        raise Exception('unimplemented')


    def simplify(self, hint=None):
        """
        #~ DRAFT ~#


        ~UNHINTED SEARCH~



        ~HINTED SEARCH~



        :param hint:
        a dictionary, containing the last op performed...
        (TODO: give the whole series of op that was performed on the equation. -> maybe store this on `Equation`?)
        (TODO: give characteristics of the equation, like the number of +, -, ..., primitives used, )
        :type hint:
        """
        if hint is None:
            self.combingSearch()
        elif 'lastOp' in hint:
            searchTerm = hint['lastOp']
            searchField = None #TODO
            for manipulate in self.getRelatedManipulateWithMetaInformation(searchField, searchTerm):
                if manipulate.applicable():
                    manipulatedSchemeEquationStr = manipulate.apply() # just apply one - and be an ass about it
                    return Equation(manipulatedSchemeEquationStr, 'scheme')
            if self.verbose:
                info(f'we cannot find a suitable manipulation based on the hint lastOp: {hint["lastOp"]}, will combingSearch')
            self.combingSearch()




    def reduceVariablesCount(self, variable):
        """
        #~ DRAFT ~#
        try to reduce the variablesCount(variable) -> 1


        variable should appear 2 or more times in self.eq
        ==
        self.eq.variables[variable] > 1

        look for the lowest-common-ancestor in AST of variable
        ON EACH SIDE OF THE EQUATION
        cut-out the subTree
        then run UNHINTED SEARCH???

        :param variable:
        :type variable:
        """
        pass


    def combingSearch(self):
        """
        #~ DRAFT ~#

        use Dijkstra : (courtesy of ChatGPT)

        TODO implement Dijkstra with heurestic in common



        import heapq

        # Create an empty priority queue
        priority_queue = []

        # Push elements with priorities
        heapq.heappush(priority_queue, (2, "Task A"))  # Priority 2
        heapq.heappush(priority_queue, (1, "Task B"))  # Priority 1
        heapq.heappush(priority_queue, (3, "Task C"))  # Priority 3

        # Pop elements (smallest priority first)
        print(heapq.heappop(priority_queue))  # Output: (1, 'Task B')
        print(heapq.heappop(priority_queue))  # Output: (2, 'Task A')
        print(heapq.heappop(priority_queue))  # Output: (3, 'Task C')
        """
        raise Exception("unimplemented")


    def _loadYAMLFromFilePath(self, filepath):
        with open(filepath, 'r') as f:
            data = safe_load(f)
            return data