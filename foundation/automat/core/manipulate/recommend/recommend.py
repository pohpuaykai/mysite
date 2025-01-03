import os
import re

from jinja2 import Environment, FileSystemLoader
import numpy as np
from yaml import safe_load

from foundation.automat import AUTOMAT_MODULE_DIR, info
from foundation.automat.common.longestcommonsubsequence import LongestCommonSubsequence
from foundation.automat.common.regexshorts import Regexshorts as rs
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
                            if direction in ['type']:
                                continue
                            iAst, iFunctions, iVariables, iPrimitives, iTotalNodeCount = Schemeparser(equationStr=d['scheme'])._parse()
                            oAst, oFunctions, oVariables, oPrimitives, oTotalNodeCount = Schemeparser(equationStr=d['return'])._parse()
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
                                #o
                                'oAst':oAst,
                                'oFunctions':oFunctions,
                                'oVariables':oVariables,
                                'oPrimitives':oPrimitives,
                                'oTotalNodeCount':oTotalNodeCount,
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
        #~ DRAFT ~#


        ~UNHINTED SEARCH~



        ~HINTED SEARCH~



        :param hint:
        a dictionary, containing the last op performed...
        (TODO: give the whole series of op that was performed on the equation. -> maybe store this on `Equation`?)
        (TODO: give characteristics of the equation, like the number of +, -, ..., primitives used, )
        :type hint:
        """

        self.simplifyingManipulations = self.getRowsInMeta('totalNodeCountIO', '>0')
        # TODO HEURIS: differentiation/integration/functors related configurations should be ignore and filtered out
        
        if self.verbose:
            relevantManipulations = sorted(self.simplifyingManipulations, key=lambda row: row['oTotalNodeCount']) #TODO refactor to self function. 
            # import pdb;pdb.set_trace()

        if hint is None:
            self.combingSearch()
        elif 'invertedResults' in hint:
            """
            hint['invertedResults'] = {   
            ('-', 6): {'newKey': ('-', 6), 'newValue': (('-', 4), ('0', 10))},
            ('=', 0): {'newKey': ('=', 0), 'newValue': (('*', 8), ('-', 6))}
            }

            tupleKey with higher id, is the one being swapped, and we take the funcName of the newKey
            """
            #also if there is - 0, we should try subtractzero first.... but the logic... should not be here. TODO
            # import pdb;pdb.set_trace()
            largestNodeId = -1
            funcAdded = None
            for oldFuncName, nodeId in hint['invertedResults'].keys():
                if largestNodeId < nodeId:
                    largestNodeId = nodeId
                    funcAdded = oldFuncName

            functionNamesJustAdded = [funcAdded]
            if len(functionNamesJustAdded) == 0:
                if self.verbose:
                    print(f'Could not identify functions just added, hint: {hint}')
            else:
                #TODO HEURIS: if no trigo in the formula, can just ignore all the trigoPatterns
                #TODO HEURIS: if no log/sqrt/expo, not need those patterns .... not sure about that
                if self.verbose:
                    print(functionNamesJustAdded, '<<functionNamesJustAdded')
                relevantManipulations = self.filterMetaList(self.simplifyingManipulations, 'iFunctions', functionNamesJustAdded)# should use: self.simplifyingManipulations AS a base
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
                        print(f"SIMPLIFYING trying applying {idd['filename']}, {idd['idx']}, {idd['direction']} to {self.eq.ast}")
                    returnTup = manipulate.apply(toAst=True)
                    if self.verbose:
                        print(f"SIMPLIFYING tried applying {idd['filename']}, {idd['idx']}, {idd['direction']}, hasResult?: {returnTup is not None}")

                    if returnTup is not None: # successfully applied manipulation
                        manipulatedSchemeWordSchemeParser, verPosWord, iManipulateSchemeParser, oManipulateSchemeParser  = returnTup
                        if self.verbose:
                            info('successful application')

                        # we must know all the things(function/variable/primitive) in the IOpatterns, so that we can iterate through them to look for change in verPosWord

                        #sometimes the remove and addition NET OUT, and we are only interested in the resulting net.
                        additionRemovalTrackingKeys = ['f', 'v', 'p'] # f=function, v=variable, p=primitive
                        type__removalNames__nodeIdList = dict(map(lambda k: (k, {}), additionRemovalTrackingKeys))#{'f':{}, 'v':{}, 'p':{}}
                        type__additioNames__nodeIdList = dict(map(lambda k: (k, {}), additionRemovalTrackingKeys))#{'f':{}, 'v':{}, 'p':{}}
                        for changeDict in filter(lambda changeDict: changeDict['d'] in ['r', 'a'] and changeDict['t'] in ['p'], verPosWord): # TODO make use of the other changeDict
                            if changeDict['d'] == 'r': # something was removed from input

                                #
                                print(self.eq.startPos__nodeId) # this is not updated...., or we just return the positions to equation, then if equations got something, it will recalculate? startPos__nodeId?
                                #

                                for function in iManipulateSchemeParser.functions:
                                    if function in changeDict['w']:
                                        #find all occurences of function and its startPos, match to nodeId in self.eq.startPos__nodeId
                                        for relativeStartPos in rs.lazyPrefixFinder(function, changeDict['w']):
                                            absoluteStartPos = changeDict['s'] + relativeStartPos
                                            print(changeDict)
                                            print(manipulate.schemeStr)#Wrong one this is the OG...
                                            nodeId = self.eq.startPos__nodeId[absoluteStartPos]
                                            existingList = type__removalNames__nodeIdList['f'].get(function, [])
                                            existingList.append(nodeId)
                                            type__removalNames__nodeIdList['f'][function] = existingList

                                for variable in iManipulateSchemeParser.variables:
                                    if variable in changeDict['w']:
                                        #find all occurences of variable and its startPos, match to nodeId in self.eq.startPos__nodeId
                                        for relativeStartPos in rs.lazyPrefixFinder(variable, changeDict['w']):
                                            absoluteStartPos = changeDict['s'] + relativeStartPos
                                            nodeId = self.eq.startPos__nodeId[absoluteStartPos]
                                            existingList = type__removalNames__nodeIdList['v'].get(variable, [])
                                            existingList.append(nodeId)
                                            type__removalNames__nodeIdList['v'][variable] = existingList


                                for primitive in iManipulateSchemeParser.primitives:
                                    if primitive in changeDict['w']:
                                        #find all occurences of primitive and its startPos, match to nodeId in self.eq.startPos__nodeId
                                        for relativeStartPos in rs.lazyPrefixFinder(primitive, changeDict['w']):
                                            absoluteStartPos = changeDict['s'] + relativeStartPos
                                            nodeId = self.eq.startPos__nodeId[absoluteStartPos]
                                            existingList = type__removalNames__nodeIdList['p'].get(primitive, [])
                                            existingList.append(nodeId)
                                            type__removalNames__nodeIdList['p'][primitive] = existingList


                            elif changeDict['a'] == 'a': #something was added to output

                                for function in oManipulateSchemeParser.functions:
                                    if function in changeDict['w']:
                                        #find all occurences of function and its startPos, match to nodeId in manipulatedSchemeWordSchemeParser.startPos__nodeId
                                        for relativeStartPos in rs.lazyPrefixFinder(function, changeDict['w']):
                                            absoluteStartPos = changeDict['s'] + relativeStartPos
                                            nodeId = manipulatedSchemeWordSchemeParser.startPos__nodeId[absoluteStartPos]
                                            existingList = type__additioNames__nodeIdList['f'].get(function, [])
                                            existingList.append(nodeId)
                                            type__additioNames__nodeIdList['f'][function] = existingList

                                for variable in oManipulateSchemeParser.variables:
                                    if variable in changeDict['w']:
                                        #find all occurences of variable and its startPos, match to nodeId in manipulatedSchemeWordSchemeParser.startPos__nodeId
                                        for relativeStartPos in rs.lazyPrefixFinder(variable, changeDict['w']):
                                            absoluteStartPos = changeDict['s'] + relativeStartPos
                                            nodeId = manipulatedSchemeWordSchemeParser.startPos__nodeId[absoluteStartPos]
                                            existingList = type__additioNames__nodeIdList['v'].get(variable, [])
                                            existingList.append(nodeId)
                                            type__additioNames__nodeIdList['v'][variable] = existingList


                                for primitive in oManipulateSchemeParser.primitives:
                                    if primitive in changeDict['w']:
                                        #find all occurences of primitive and its startPos, match to nodeId in manipulatedSchemeWordSchemeParser.startPos__nodeId
                                        for relativeStartPos in rs.lazyPrefixFinder(primitive, changeDict['w']):
                                            absoluteStartPos = changeDict['s'] + relativeStartPos
                                            nodeId = manipulatedSchemeWordSchemeParser.startPos__nodeId[absoluteStartPos]
                                            existingList = type__additioNames__nodeIdList['p'].get(primitive, [])
                                            existingList.append(nodeId)
                                            type__additioNames__nodeIdList['p'][primitive] = existingList

                        nonNettedaddRem__type__nodeIdList = {'a':dict(map(lambda k: (k, []), additionRemovalTrackingKeys)), 'r':dict(map(lambda k: (k, []), additionRemovalTrackingKeys))}
                        for gk in additionRemovalTrackingKeys:
                            removalNames__nodeIdList = type__removalNames__nodeIdList[gk]
                            additioNames__nodeIdList = type__additioNames__nodeIdList[gk]
                            #find things that NOT NET OUT
                            nettedOutNodeNames = []
                            for commonNodeName in set(removalNames__nodeIdList.keys()).intesection(set(additioNames__nodeIdList.keys())):
                                if len(removalNames__nodeIdList[commonNodeName]) != len(additioNames__nodeIdList[commonNodeName]):
                                    nettedOutNodeNames.append(commonNodeName)

                            for nodeName, nodeIdList in removalNames__nodeIdList.items():
                                if nodeName not in nettedOutNodeNames:
                                    nonNettedaddRem__type__nodeIdList['r'][gk] += nodeIdList
                            for nodeName, nodeIdList in additioNames__nodeIdList.items():
                                if nodeName not in nettedOutNodeNames:
                                    nonNettedaddRem__type__nodeIdList['a'][gk] += nodeIdList
                        # import pdb;pdb.set_trace()
                        return manipulatedSchemeWordSchemeParser.ast, nonNettedaddRem__type__nodeIdList['r']['p'], nonNettedaddRem__type__nodeIdList['r']['v'], nonNettedaddRem__type__nodeIdList['r']['f']

            #if we reach here this means non of the prioritised-simplifyingManipulations worked.
            if self.verbose:
                info(f'we cannot find a suitable manipulation based on the hint lastOp: {hint["lastOp"]}, will combingSearch')
            #for now we return None #self.combingSearch() # then we comb :)




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