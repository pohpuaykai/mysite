import os
import re

from jinja2 import Environment, FileSystemLoader
import numpy as np
from yaml import safe_load

from foundation.automat import AUTOMAT_MODULE_DIR, info
# from foundation.automat.common.longestcommonsubsequence import LongestCommonSubsequence
# from foundation.automat.common.regexshorts import Regexshorts as rs
from foundation.automat.core.manipulate.manipulate import Manipulate

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
    PATTERN_FILENAMES__CLASSNAMES = Manipulate.PATTERN_FILENAMES__CLASSNAMES()

    def __init__(self, equation, verbose=False):
        self.verbose=verbose
        # self.verbose = False
        self.eq = equation
        self.manipulateConfigFileFolder = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate','configuration')
        self.metaFolder = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate', 'recommend', 'meta')
        self.metaFilename = 'manipulations_patterns.npy'
        self.metaData = None
        self._retrieveMetaInformation()
        # print(type(self.metaData))
        # import pdb;pdb.set_trace()


    def getManipulateClass(self, filename):
        className = Recommend.PATTERN_FILENAMES__CLASSNAMES[filename]
        import importlib, inspect
        module_obj = importlib.import_module(f'.{filename}', package='foundation.automat.core.manipulate.pattern')
        klassName, manipulateClass = list(filter(lambda tup: tup[0]==className,inspect.getmembers(module_obj, predicate=inspect.isclass)))[0]
        globals()[className] = manipulateClass
        return manipulateClass


    def _generateMetaInformation(self):
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
                            if direction in ['type', 'minArgs', 'maxArgs', 'preCond']:
                                continue
                            # print(d); print('config'); print(config)
                            # import pdb;pdb.set_trace()
                            iAst, iFunctions, iVariables, iPrimitives, iTotalNodeCount, iStartPos__nodeId = Schemeparser(equationStr=d['scheme'])._parse()
                            oAst, oFunctions, oVariables, oPrimitives, oTotalNodeCount, oStartPos__nodeId = Schemeparser(equationStr=d['return'])._parse()
                            # if filename == 'subtractzero.yaml':
                            #     print(filename, direction, idx)
                            #     print(iFunctions)
                            #     import pdb;pdb.set_trace()
                            metaData.append({#TODO sqlite database? lol OR implement your own BTree, werde settle for numpy for now
                                'identity':{
                                    'idx':idx,
                                    'direction':direction,
                                    'filename':filename[:filename.index('.')]
                                },
                                # 'i': {
                                #     'ast':iAst,
                                #     'functions':iFunctions,
                                #     'variables':iVariables,
                                #     'primitive':iPrimitives,
                                #     'totalNodeCount':iTotalNodeCount
                                # },
                                # 'o': {
                                #     'ast':oAst,
                                #     'functions':oFunctions,
                                #     'variables':oVariables,
                                #     'primitive':oPrimitives,
                                #     'totalNodeCount':oTotalNodeCount
                                # },
                                #i
                                'iAst':iAst,
                                'iFunctions':iFunctions,
                                'iVariables':iVariables,
                                'iPrimitives':iPrimitives,
                                'iTotalNodeCount':iTotalNodeCount,
                                'iStartPos__nodeId':iStartPos__nodeId,
                                #o
                                'oAst':oAst,
                                'oFunctions':oFunctions,
                                'oVariables':oVariables,
                                'oPrimitives':oPrimitives,
                                'oTotalNodeCount':oTotalNodeCount,
                                'oStartPos__nodeId':oStartPos__nodeId,
                                #differences
                                'type':typey,
                                'functionsIO':set(iFunctions.keys()) - set(oFunctions.keys()),
                                'functionsOI':set(oFunctions.keys()) - set(iFunctions.keys()),
                                'variablesIO':set(iVariables.keys()) - set(oVariables.keys()),
                                'variablesOI':set(oVariables.keys()) - set(iVariables.keys()),
                                'primitiveIO':set(iPrimitives.keys()) - set(oPrimitives.keys()),
                                'primitiveOI':set(oPrimitives.keys()) - set(iPrimitives.keys()),
                                'totalNodeCountIO':iTotalNodeCount - oTotalNodeCount
                            })
        np.save(file=os.path.join(self.metaFolder, self.metaFilename), arr=metaData)#, allow_pickle=False) # ValueError: Object arrays cannot be saved when allow_pickle=False
        #then https://numpy.org/doc/stable/reference/generated/numpy.save.html says its a security issue.... WHAT TO DO?
        self.metaData = np.array(metaData)

    def _retrieveMetaInformation(self, rederive=False):
        """
        TODO change to SINGLETON, um this function load faster, so that the loading only done on application load once.
#maybe have tags for each manipulation, for what equation it is suitable for???? should be done in the experience file.<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        #~ DRAFT ~#


        read from folder meta (if available)
        if not available OR rederive=True, 
            read all the YAML from manipulate/configuration
            calculate meta-information and store it in folder meta

        :param rederive:
        :type rederive:
        """
        if self.metaData is None or rederive:
            self._generateMetaInformation()
        else:
            try:
                self.metaData = np.array(np.load(file=os.path.join(self.metaFolder, self.metaFilename)))
            except:
                if self.verbose:
                    import traceback
                    info('loading of metaData Failed, generating metaData')
                    traceback.print_exc()
                #regenerate
                self._generateMetaInformation()


    def filterMetaList(self, metaList, searchCol, searchTerms):
        # print('metaList', metaList); print('searchCol', searchCol); print('searchTerms', searchTerms);
        # import pdb;pdb.set_trace()
        if isinstance(searchTerms, list): # we assume that searchCol's values are list of str
            def hasOneOfThese(row, terms):
                return len(terms.intersection(row[searchCol])) > 0
            mask = np.vectorize(lambda row: hasOneOfThese(row, set(searchTerms)))(metaList)
            return metaList[mask]
        # a range string '>5', '<=10.0'
        m = re.match('([><=]+)([-]*\\d+(?:\\.{1}\\d+)*)$', searchTerms)
        if m is not None:
            gle, numS = m.groups()
            num = float(numS)
            def findRange(row, gle, num):
                if gle == '>':
                    return row[searchCol] > num
                elif gle == '>=':
                    return row[searchCol] >= num
                elif gle == '<':
                    return row[searchCol] < num
                elif gle == '<=':
                    return row[searchCol] <= num
                elif gle == '==':
                    return row[searchCol] == num
                else:
                    raise Exception(f'We only take <, >, <=, >=, ==, but we got {gle}')
            mask = np.vectorize(lambda row: findRange(row, gle, num))(metaList)
            # import pdb;pdb.set_trace()
            return metaList[mask]

    def getRowsInMeta(self, searchCol, searchTerms):
        return self.filterMetaList(self.metaData, searchCol, searchTerms)


    def simplify(self, hint=None):
        """
The smaller the self.equation.astScheme the more simple???<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO




###
Cannot be applied to Differentiation|Integration
Please see:
hi Sir, i just found something irritating in a computer algebra system(CAS)... i will write in latex
Suppose we are to solve $\frac{d}{dx} \log_a(B(x))$, where a is any number
If the CAS took the wrong route and went:
$\frac{d}{dx} \ln(e^{\log_a(B(x))})$
it would have gotten:
$\frac{(\log_a(B(x)))(e^{\log_a(B(x)))}}{e^{\log_a(B(x))}}$
and after simplifying it would have gotten:
$\log_a(B(x))$
Which is wrong, but all the rules applied are valid... is there some kind of hiearchy_of_rules or some rules that are omitted?
###

        #~ DRAFT ~#


        ~UNHINTED SEARCH~



        ~HINTED SEARCH~



        :param hint:
        a dictionary, containing the last op performed...
        (TODO: give the whole series of op that was performed on the equation. -> maybe store this on `Equation`?)
        (TODO: give characteristics of the equation, like the number of +, -, ..., primitives used, )
        :type hint:
        """

        self.simplifyingManipulations = self.getRowsInMeta('totalNodeCountIO', '>0') #maybe if the number of node count is reduced then it is a simplying step.. but what if we need the number of nodes to increase before we can reduce it?
        # TODO HEURIS: differentiation/integration/functors related configurations should be ignore and filtered out
        
        if self.verbose:
            #should this be under self.verbose? seems like a pretty decent HEURES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
            relevantManipulations = sorted(self.simplifyingManipulations, key=lambda row: row['oTotalNodeCount']) #TODO refactor to self function. 
            # import pprint; pp = pprint.PrettyPrinter(indent=4)
            # print('***************************************')
            # pp.pprint(relevantManipulations[0])
            # pp.pprint(list(map(lambda d: d['identity']['filename'], relevantManipulations)))

            # import pdb;pdb.set_trace()

        if hint is None:
            self.combingSearch()
        elif 'invertedResults' in hint:
        # elif 'op' in hint: # is this check necessary? break into parts?
            """
            hint['invertedResults'] = {   
            ('-', 6): {'newKey': ('-', 6), 'newValue': (('-', 4), ('0', 10))},
            ('=', 0): {'newKey': ('=', 0), 'newValue': (('*', 8), ('-', 6))}
            }

            tupleKey with higher id, is the one being swapped, and we take the funcName of the newKey
            """
            #also if there is - 0, we should try subtractzero first.... but the logic... should not be here. TODO
            # print('hint: ', hint)
            # import pdb;pdb.set_trace()
            # largestNodeId = -1 # the nodeId is now not according to rootOfTree being first.... so we cannot do it this way
            # funcAdded = None
            # for oldFuncName, nodeId in hint['invertedResults'].keys():
            #     if largestNodeId < nodeId:
            #         largestNodeId = nodeId
            #         funcAdded = oldFuncName

            # functionNamesJustAdded = [funcAdded]
            # functionNamesJustAdded = list(map(lambda d: d[0], hint['invertedResults'].keys()))
            #functionNamesJustAdded should take the newKey from invertedResults
            functionNamesJustAdded = list(map(lambda d: d['newKey'][0], hint['invertedResults'].values()))
            if len(functionNamesJustAdded) == 0:
                if self.verbose:
                    print(f'Could not identify functions just added, hint: {hint}')
            else:
                #TODO HEURIS: if no trigo in the formula, can just ignore all the trigoPatterns
                #TODO HEURIS: if no log/sqrt/expo, not need those patterns .... not sure about that
                if self.verbose:
                    print('hint: ', hint)
                    print(functionNamesJustAdded, '<<functionNamesJustAdded')
                    import pdb;pdb.set_trace()#<<<< some thing wrong with 
                relevantManipulations = self.filterMetaList(self.simplifyingManipulations, 'iFunctions', functionNamesJustAdded)# should use: self.simplifyingManipulations AS a base
                if self.verbose:
                    import pprint; pp = pprint.PrettyPrinter(indent=4)
                    print('***************************************')
                    # pp.pprint(relevantManipulations[0])
                    pp.pprint(list(map(lambda d: d['identity']['filename'], relevantManipulations)))
                # TODO HEURIS: those with least number of output nodes, should be tried first :)
                # TODO HEURIS: alot of LCSS matches (prefix/suffix/middlefixes) with pattern and target, should be tried first: https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
                # NOTE that np.array mess up the sorting_order
                relevantManipulations = sorted(relevantManipulations, key=lambda row: row['oTotalNodeCount']) #TODO refactor to self function. 
                # print('TYPEEEEE; ', type(self.simplifyingManipulations))
                if self.verbose:
                    print('** total number of metaData: ', len(self.metaData))
                    print('**there are ', len(relevantManipulations), ' manipulations that we trying out')
                    print('** here are the top 10: ')
                    printables = list(map(lambda row: f"{row['oTotalNodeCount']} {row['identity']}", relevantManipulations))
                    for printable in printables:
                        print(printable)

                rmIdentities = list(map(lambda row: row['identity'], relevantManipulations))
                for idd in rmIdentities:
                    manipulateClass = self.getManipulateClass(idd['filename'])
                    # import pdb;pdb.set_trace()
                    manipulate = manipulateClass(self.eq, idd['direction'], idd['idx'], verbose=self.verbose)
                    if self.verbose:
                        print(f"SIMPLIFYING trying applying {idd['filename']}, {idd['idx']}, {idd['direction']} to {self.eq.ast}", "|", manipulate.inputGrammar, "|", manipulate.outputGrammar)
                    returnTup = manipulate.apply(startPos__nodeId=hint['startPos__nodeId'], toAst=True)
                    if self.verbose:
                        print(f"SIMPLIFYING tried applying {idd['filename']}, {idd['idx']}, {idd['direction']}, hasResult?: {returnTup is not None}")

                    if returnTup is not None: # successfully applied manipulation


                        #
                        #use sgp.schemeId__argCount, and sgp.schemeNodeChangeLog to get function/variable/primitive count? for variable, schemeId__argCount=1, for function, schemeId__argCount>1, for primitive, schemeId__argCount=0
                        #but the downstream equation.simplify does not need countsOfFunctionVariablePrimitivesRemoved anymore!
                        #equation.simplify needs, can be reparsed by schemeparser, but those with nodeId, need to be changed to the OLD nodeIds provided by sgp
                        #or should they be provided by sgp? but it is weird to put latexParser in sgp...?
                        sgp, manipulateType, manipulateClassName = returnTup
                        rootOfTree___simplified = sgp.getRootOfTree___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        ast___simplified = sgp.getAST___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        startPos__nodeId___simplified = sgp.startPos__nodeId___oStr
                        nodeId__len___simplified = sgp.getNodeId__len___oStr()# this is schemeNodeLen, not schemeLabelLen, nodeId needs to be recalculated
                        schemeStr___simplified = sgp.oStr

                        functions___simplified = sgp.schemeparser___oStr.functions
                        variables___simplified = sgp.schemeparser___oStr.variables
                        primitives___simplified = sgp.schemeparser___oStr.primitives
                        totalNodeCount___simplified = sgp.schemeparser___oStr.totalNodeCount
                        latexStr___simplified = sgp.schemeparser___oStr._toLatex()

                        iPattern = sgp.iPattern
                        oPattern = sgp.oPattern
                        return rootOfTree___simplified, ast___simplified, startPos__nodeId___simplified, nodeId__len___simplified, schemeStr___simplified, functions___simplified, variables___simplified, primitives___simplified, totalNodeCount___simplified, latexStr___simplified, manipulateType, manipulateClassName, iPattern, oPattern

            #if we reach here this means non of the prioritised-simplifyingManipulations worked.
            if self.verbose:
                info(f'we cannot find a suitable manipulation based on the hint lastOp: {hint["invertedResults"]}, will combingSearch')
            #for now we return None #self.combingSearch() # then we comb :)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO




    def reduceVariablesCount(self, variable):
        """
        #~ DRAFT ~#
        try to reduce the variablesCount(variable) -> 1


        variable should appear 2 or more times in self.eq
        ==
        self.eq.variables[variable] > 1

        look for the lowest-common-ancestor in AST of variable <<<TODO in `Equation`
        ON EACH SIDE OF THE EQUATION
        cut-out the subTree
        (or hinted simplify, where hint = {lastOp: root of the subTree})
        then run UNHINTED SEARCH??? << no need, will comb in simplify

        :param variable:
        :type variable:
        """
        self.eq._cutSubASTAtRoot(rootNode)


    @classmethod
    def bipartiteSearch(
        self, 
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds
        ):
        """THIS method seem ill suited to be in this class............. change file? >< Maybe create a new class called Eliminator take always takes a system of equations, also contains symbolicGaussian

        This was the original planned search. Implemented for ecircuit

        equations are nodes on 1 side of the bipartite, the other side are variables. variables connect to equations, if they appear in the equation. The connection is undirected

        There are 
        0. controllable_variables(manufacturers, variable_resistance, variable_capacitance, variable_inductance, amplification_of_transistor),
        1. fixed_variables(more like constants coming from specifications|after_choosing_manufacturers, like V_{cc}, load_max_current, transistor_threshold_voltage, collector_emitter_breakdown_voltage)
        2. intermediate_variables(not 0|1), we want to substitute these away...

        form a path P, going through all the intermediate_variables, path will alternate between equation & variable.
        In P, between 2 equations E0, E1 there is a variable V.
        Make V the subject of E0, and substitute V away in E1.
        Repeat for the whole P. We will get an equation without all the intermediate_variables.

        Then either plop in the values(simple calculation), or plot a graph with the equation(understand effects of circuit), or use equation for optimization(what to buy)

        :param dependentVariableId: is a vertexId, (not from list_equations nor list_variables)
        :param list_independentVariableIds: are vertexIds (not from list_equations nor list_variables)
        :param type__list_vertexIds: type is either (0)equationKey or (1)variableKey (the partite of each vertexId), values are a list of vertexIds of its key's partite
        """
        #[TODO optimization possible, if the bipartite graph equationVariables_bg is disconnected, only take the connected part that is related to dependent|indepedentVariables]
        # from foundation.automat.common.spanningtree import SpanningTree
        # vertexIterable = sorted(list(equationVariables_bg))
        # def isEquation(parentId):
        #     return parentId < len(list_equations)
        # edgeIterableSortable = []; edgeWeight = {}#assign edges incident to variables that we want to get rid of, lower weights
        # HIGH_WEIGHTS = 3000; LOW_WEIGHTS = 0; #[TODO many optimizations possible here]
        # for parentId, neighbours in equationVariables_bg.items():
        #     parentKeep = isEquation(parentId) or (parentId in [dependentVariableId]+list_independentVariableIds) # equation=KEEP, dependent|independentVariable=KEEP
        #     for neighbourId in neighbours:
        #         neighbourKeep = isEquation(neighbourId) or (neighbourId in [dependentVariableId]+list_independentVariableIds)
        #         directedEdge = (parentId, neighbourId)
        #         edgeIterableSortable.append(directedEdge)
        #         if parentKeep and neighbourKeep:# both nodes of directedEdge are either (0)Equation OR (1)dependent|independentVariables, assign HIGH_WEIGHTS to keep
        #             edgeWeight[directedEdge] = HIGH_WEIGHTS
        #         else: # either nodes of directedEdge is NOT Equation NOR dependent|independentVariables, assign LOW_WEIGHTS to form subsitutionPath to be eliminated
        #             edgeWeight[directedEdge] = LOW_WEIGHTS
        # T, R = SpanningTree.minimumSpanningTreeKruskal(vertexIterable, edgeIterableSortable, edgeWeight)
        # print('T:', T); print('R: ', R, '<<<<<<<<<<')
        #find equationNode in T, that has dependentVariableId as start of DFS#[TODO many optimizations possible here, to get a Path that substitutes away all the unwanted variables]
        #since T is spanning, we can just look in list_equations, for ANY equation that has_most_number_of_dependentVariableId_and_list_independentVariableIds[heuristic][TODO many optimizations possible here, on which starting point to pick] Ou est vers origin, ja?
        print(dependentVariableId, 'dependentVariableId'); print('list_independentVariableIds', list_independentVariableIds)
        from foundation.automat.common.priorityqueue import PriorityQueue
        wantedVariables = []
        for wantedVariableId in [dependentVariableId]+list_independentVariableIds:
            wantedVariables.append(list_variables[wantedVariableId])
        maxTotalCount = -1; maxEquationVertexId = None;
        for equationId, equation in enumerate(list_equations):
            variables__count = equation.variablesScheme; totalWantedVariableCount = 0
            for wantedVariable in set(variables__count.keys()).intersection(set(wantedVariables)):
                totalWantedVariableCount += variables__count[wantedVariable]
            if totalWantedVariableCount > maxTotalCount:
                maxTotalCount = totalWantedVariableCount; maxEquationVertexId = equationId__vertexId[equationId]
        #check if all the variables to be substituted away are in our path
        #or we can start from a variable, then add the appropriate equation to the beginning of the resulting path
        unwantedVariableIds = list(set(type__list_vertexIds[variableKey])-set([dependentVariableId]+list_independentVariableIds)) # any variable that is not dependent|independentVariable
        # dependentVariable = list_variables[dependentVariableId]
        # stack = [{'current':dependentVariableId, 'path':[dependentVariableId]}]; visited = [dependentVariableId]; 
        #maxEquationVertexId might be None... then for now just get a random one...
        if maxEquationVertexId is None:#[TODO many optimizations possible here]
            maxEquationVertexId = list(equationId__vertexId.values())[0]
        # stack = [{'current':maxEquationVertexId, 'path':[maxEquationVertexId]}]; 
        print('unwantedVariableIds', unwantedVariableIds); print('wantedVariables', wantedVariables)
        priorityQueue = PriorityQueue(); priorityQueue.insert({'current':maxEquationVertexId, 'path':[maxEquationVertexId]}, -1)
        visited = [maxEquationVertexId];
        maxLength=0; maxLengthChildDict = None
        HIGH_WEIGHTS = 3000; LOW_WEIGHTS = 0; #[TODO many optimizations possible here]
        # while len(stack)>0:
        while len(priorityQueue)>0:
            # current___dict = stack.pop()#lastOut,  what if we choose the neighbour, that is in the unwanted_variable set ? will that be a better path? PRIORITY_QUEUE, use your binarySearch to implement priority_queue on []<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
            current___dict = priorityQueue.popMax()
            for neighbour in equationVariables_bg[current___dict['current']]:
            # for neighbour in T[current___dict['current']]: # this is the correct one, but does not perform as well
                if neighbour not in visited:
                    visited.append(neighbour)
                    childDict = {'current':neighbour, 'path':current___dict['path']+[neighbour]}
                    if len(childDict['path']) > maxLength:
                        maxLength = len(childDict['path']); maxLengthChildDict = childDict
                    # stack.append(childDict)
                    #
                    childDictPriority = HIGH_WEIGHTS if neighbour in unwantedVariableIds else LOW_WEIGHTS
                    priorityQueue.insert(childDict, childDictPriority)
                    #
        #             print('******')
        #             print('current: ', current___dict['current'], ' child: ', childDict['current'], ' path: ', childDict['path'])
        #             print('******')
        # print('returning substitutionPath:', maxLengthChildDict['path'])
        return maxLengthChildDict['path']


    def combingSearch(self):
        """
        #~ DRAFT ~#

        use Dijkstra : (courtesy of ChatGPT)

        TODO implement Dijkstra with heurestic in common
        nodes are equations, nodes are connected if we can apply a manipulation from a node to another node.
        there are some end nodes, where if our search hits, then it terminates (Take me Ohm)



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