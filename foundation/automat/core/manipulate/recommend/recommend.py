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
Suppose we are to solve $\frac{d}{dx} \\log_a(B(x))$, where a is any number
If the CAS took the wrong route and went:
$\frac{d}{dx} \\ln(e^{\\log_a(B(x))})$
it would have gotten:
$\frac{(\\log_a(B(x)))(e^{\\log_a(B(x)))}}{e^{\\log_a(B(x))}}$
and after simplifying it would have gotten:
$\\log_a(B(x))$
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
        variableId__vertexId,
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

        Count_Tree_まま
        When we try to derive parallelSumOfResistors of 2_resistor_in_parallel_circuit, the bipartite_path_is_blocked on V_{DC}-V_{R_3}=0, because the next required step of elimination requires a equation that is not on the bipartiteGraph
        as we do linearEliminationBySubstitution, new Equations (set of variables) are produced, and some of them might have extra_variables_that_can_be_cancelled_out.
        If we could simplify equations, so that they do not have extra_variables_that_can_be_cancelled_out, the_set_of_variables_ignoring_position_in_equation, can be used as id for the equation
        If we have the_set_of_variables_ignoring_position_in_equation as id for equation, we can add newly created variables to the bipartite_graph {the underlying graph changes as we traverse it}
        And then that path becomes explorable_and_obtainable.
        This means:
        - WE HAVE TO WORK ON SIMPLIFY(finding the shortest_possible_standard_representation_of_an_equation) for id_of_equation
        - and then the update the bipartite_graph as we traverse it

        Also our current_method_of_substitution does not allow SchemeFunctions to be substituted away, if this was possible other paths to derive the parallel_sum_of_resistance might be possible... {ELEGANCE}



        :param dependentVariableId: is a vertexId, (not from list_equations nor list_variables)
        :param list_independentVariableIds: are vertexIds (not from list_equations nor list_variables)
        :param type__list_vertexIds: type is either (0)equationKey or (1)variableKey (the partite of each vertexId), values are a list of vertexIds of its key's partite
        """
        #[TODO optimization possible, if the bipartite graph equationVariables_bg is disconnected, only take the connected part that is related to dependent|indepedentVariables]

        from foundation.automat.common.priorityqueue import PriorityQueue
        #since we are finding all possible paths, what about save_points? (each save_point is [priority_queue, list_of_next_explored, index_of_visited_to_back_track]), everytime, we finish the PQ, but we cannot find an answer that gets all the unwantedVariables, we popOff a savePoint, but if we popOff more than 1 savePoint, savePoint0 and then savePoint1, we have to make sure we do not go back to the same savePoint0 again when we explore savePoint1... not sure how to do that
        allVariableVertexIds = list(map(lambda variableId: variableId__vertexId[variableId], range(0, len(list_variables))))
        wantedVariableVertexIds = list(map(lambda variableId: variableId__vertexId[variableId], [dependentVariableId]+list_independentVariableIds))
        unwantedVariableVertexIds = list(set(allVariableVertexIds) - set(wantedVariableVertexIds))
        allEquationVertexIds = list(map(lambda equationId: equationId__vertexId[equationId], range(0, len(list_equations))))
        #remove wantedVariableVertexIds
        equationVariables_bg___noWantedVariableVertexIds = {}
        for parentVertexId, childVertexIds in equationVariables_bg.items():
            if parentVertexId not in wantedVariableVertexIds:
                filteredChildVertexIds = []
                for childVertexId in childVertexIds:
                    if childVertexId not in wantedVariableVertexIds:
                        filteredChildVertexIds.append(childVertexId)
                equationVariables_bg___noWantedVariableVertexIds[parentVertexId] = filteredChildVertexIds
        equationVariables_bg = equationVariables_bg___noWantedVariableVertexIds

        #finding a startNode
        maxEquationVertexId = None;maxTotalCount = -1
        wantedVariables = []
        for wantedVariableId in [dependentVariableId]+list_independentVariableIds:
            wantedVariables.append(list_variables[wantedVariableId])
        for equationId, equation in enumerate(list_equations):
            variables__count = equation.variablesScheme; totalWantedVariableCount = 0
            for wantedVariable in set(variables__count.keys()).intersection(set(wantedVariables)):
                totalWantedVariableCount += variables__count[wantedVariable]
            if totalWantedVariableCount > maxTotalCount:
                maxTotalCount = totalWantedVariableCount; maxEquationVertexId = equationId__vertexId[equationId]



        #check if all the variables to be substituted away are in our path
        #or we can start from a variable, then add the appropriate equation to the beginning of the resulting path
        #maxEquationVertexId might be None... then for now just get a random one...
        if maxEquationVertexId is None:#[TODO many optimizations possible here] Ou est vers origin, ja?
            maxEquationVertexId = allEquationVertexIds[0] # startNode
        # print('unwantedVariableVertexIds', unwantedVariableVertexIds); print('wantedVariableVertexIds', wantedVariableVertexIds)
        # print('startNode: ', maxEquationVertexId)
        priorityQueue = PriorityQueue(); 
        priorityQueue.insert({
            'current':maxEquationVertexId, 
            'path':[maxEquationVertexId],
            'visited':[]
        }, -1)
        maxLength=0; maxLengthPaths = []
        HIGH_WEIGHTS = 3000; LOW_WEIGHTS = 0; WANTEDVARIABLE_PENALTY = -2* HIGH_WEIGHTS#[TODO many optimizations possible here]
        PATHLENGTH_FACTOR = 10
        visitedPaths = [] # paths that have been explored before
        # while len(stack)>0:
        while len(priorityQueue)>0:
            current___dict = priorityQueue.popMax()
            current = current___dict['current']

            current___dict['visited'].append(current)
                    
            for orderOfExploration, neighbour in enumerate(sorted(equationVariables_bg[current], key=lambda vertexId: LOW_WEIGHTS if vertexId in unwantedVariableVertexIds or vertexId in allEquationVertexIds else HIGH_WEIGHTS)):#[TODO optimisation possibility] equationVariables_bg[current] can be sorted, because you are depending on the orderOfExploration
                if neighbour not in current___dict['visited']:
                    childDict = {'current':neighbour, 'path':current___dict['path']+[neighbour], 'visited':current___dict['visited']+[neighbour]}
                    if len(childDict['path']) > maxLength:
                        maxLength = len(childDict['path'])
                        maxLengthPaths = [] # only store longest path, this will not work if the #OfNodes(equationVariables_bg) increases as we process equationVariables_bg <Heuristic>
                    if len(childDict['path']) == maxLength:#there might be many paths with same maxLength, if we have a choice, HOW TO CHOOSE<<<<<<<<<<<<<<<<<<<<<<<TODO?
                        maxLengthPaths.append(childDict['path'])
                    #Priority Heuristic
                    childDictPriority = HIGH_WEIGHTS if neighbour in unwantedVariableVertexIds or neighbour in allEquationVertexIds else LOW_WEIGHTS
                    childDictPriority = childDictPriority - orderOfExploration if neighbour in unwantedVariableVertexIds else childDictPriority # do not subtract orderofExploration if it is a equation
                    childDictPriority += PATHLENGTH_FACTOR * len(childDict['path']) # should continue on the longest path, and not jump other timeframe of shorter path
                    childDictPriority += WANTEDVARIABLE_PENALTY if neighbour in wantedVariableVertexIds else 0
                    priorityQueue.insert(childDict, childDictPriority)#-orderOfExploration try to ensure that those inserted later, have lower priority
                    #
                    # print('******')
                    # print('neighbour', neighbour, 'priority: ', childDictPriority-orderOfExploration)
                    # print('current: ', current, ' child: ', childDict['current'], 'currentPath: ', current___dict['path'], ' childPath: ', childDict['path'])
                    # print('priorityQueue')
                    # print(priorityQueue)
                    # print('visited:', current___dict['visited'])
                    # print('******')
        # print('returning substitutionPath:', maxLengthChildDict['path'])
        #pick your favourite path from maxLengthPaths?
        # print('maxLengthPaths:')
        # print(maxLengthPaths)
        # print('********')
        favouritePath = maxLengthPaths[0] # [TODO many optimisations possible here]
        return favouritePath


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