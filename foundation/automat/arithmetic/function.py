from abc import ABC
from copy import deepcopy
import importlib
import inspect
import os

from foundation.automat import AUTOMAT_MODULE_DIR
from foundation.automat.common.backtracker import Backtracker


class Function:#(metaclass=FunctionHook):
    """
    Should be able to take an AST (dictionary, key: node (tuple[label, id]), value: list of neighbours (list[tuple[label, id]])
    and do:
    (1) each of its inputs (one at a time) the 'root of the sub-AST' (sub-subject of the equation) through inverses primitive
    (2) substitute primitives in variables, evaluate the sub-AST and replace sub-AST with primitve node
    (3) form a bunch of displayable
        (a) "Scheme - styled_string" (with pretty option)
        (b) "Latex - styled_string"
        (c) MathML (html)


    """
    _FUNC_NAMES = []
    _FUNCNAME__MODULENAME = {}
    _FUNCNAME__CLASSNAME = {}
    _TRIGNOMETRIC_NAMES = []

    def __init__subclass(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # import pdb;pdb.set_trace()
        # if kwargs.get('type') == 'trigonometric' and kwargs.get('funcName') is not None: # somehow, this is nie gerennt, wenn TRIGONOMETRIC_NAMES hiess
        #     cls._TRIGONOMETRIC_NAMES.append(kwargs.get('funcName'))
        # if type == 'trigonometric':
        #     cls.TRIGONOMETRIC_NAMES.append(funcName)
        # import pdb;pdb.set_trace()

    # @property # for now it wll return a property-object, and the expected list... , TODO so we will use it as a cls_method FOR NOW
    @classmethod
    def TRIGONOMETRIC_NAMES(cls): #TODO refactor0
        if len(cls._TRIGNOMETRIC_NAMES) == 0:
            #gather all the trigonometric function names
            module_dir = os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'standard')
            for module in os.listdir(module_dir):
                # print('***', module)
                if module.endswith('.py') and module != '__init__.py':
                    module_name = module[:-3] # remove .py
                    module_obj = importlib.import_module(f'.{module_name}', package='foundation.automat.arithmetic.standard')
                    for name, ocls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                        if name in ['Function']:
                            continue
                        # print('name***', name, '***ocls***', ocls)
                        # import pdb;pdb.set_trace()
                        if ocls.TYPE == 'trigonometric':
                            # import pdb;pdb.set_trace()
                            cls._TRIGNOMETRIC_NAMES.append(ocls.FUNC_NAME)

        return cls._TRIGNOMETRIC_NAMES


    @classmethod
    def FUNC_NAMES(cls): #TODO refactor0
        if len(cls._FUNC_NAMES) == 0:
            #gather all the function names
            module_dir = os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'standard')
            for module in os.listdir(module_dir):
                if module.endswith('.py') and module != '__init__.py':
                    module_name = module[:-3] # remove .py
                    module_obj = importlib.import_module(f'.{module_name}', package='foundation.automat.arithmetic.standard')
                    for name, ocls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                        if name in ['Function']: #skip the parent of all function
                            continue
                        cls._FUNC_NAMES.append(ocls.FUNC_NAME)
        return cls._FUNC_NAMES


    @classmethod
    def FUNCNAME__MODULENAME(cls): #TODO refactor0
        if len(cls._FUNCNAME__MODULENAME) == 0:
            #gather all the function names
            module_dir = os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'standard')
            for module in os.listdir(module_dir):
                if module.endswith('.py') and module != '__init__.py':
                    module_name = module[:-3] # remove .py
                    module_obj = importlib.import_module(f'.{module_name}', package='foundation.automat.arithmetic.standard')
                    for klassName, ocls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                        if klassName in ['Function']: #skip the parent of all function
                            continue
                        cls._FUNCNAME__MODULENAME[ocls.FUNC_NAME] = module_name
        return cls._FUNCNAME__MODULENAME


    @classmethod
    def FUNCNAME__CLASSNAME(cls): # TODO refactor0
        if len(cls._FUNCNAME__CLASSNAME) == 0:
            #gather all the function names
            module_dir = os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'standard')
            for module in os.listdir(module_dir):
                if module.endswith('.py') and module != '__init__.py':
                    module_name = module[:-3] # remove.py
                    module_obj = importlib.import_module(f'.{module_name}', package='foundation.automat.arithmetic.standard')
                    for klassName, ocls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                        if klassName in ['Function']: # skip the parent of all function
                            continue
                        cls._FUNCNAME__CLASSNAME[ocls.FUNC_NAME] = klassName
        return cls._FUNCNAME__CLASSNAME



    def __init__(self, equation, idInAst, verbose=False):
        self.eq = equation
        self.inverses = None
        self.verbose = verbose
        self.idInAst = idInAst


    def preReverse(self, equationSide, argumentIdx, nodeIds, startPos__nodeId): # TODO refactor, startPos__nodeId does not need to be passed here, get from self.eq.startPos__nodeIdScheme
        """"""
        ast = deepcopy(self.eq.astScheme)
        replacementDictionary = {}
        for key, value in ast.items():
            if key[1] in nodeIds:
                replacementDictionary[key] = value

        if self.verbose:
            print('replacementDictionary')
            print(replacementDictionary)
            print('len(replacementDictionary):', len(replacementDictionary))
            print('reverses key: ', (equationSide, str(argumentIdx)))


        #will raise error if function of the node with `nodeId` is not equals to self.FUNC_NAME, handle in child.inverse
        (invertedResults, functionCountChange, primitiveCountChange, totalNodeCountChange, permutation, key0, key1) = self.reverses[(equationSide, str(argumentIdx))](
            replacementDictionary, self.eq.totalNodeCountScheme)

        return invertedResults, functionCountChange, primitiveCountChange, totalNodeCountChange, ast, permutation, key0, key1, replacementDictionary


    def reverse(self, equationSide, argumentIdx, nodeIds, startPos__nodeId, nodeId__len, rootOfTree): # TODO refactor, startPos__nodeId&nodeId__len, get from self.eq.
        """
        make argumentIdx the subject of the subAST

        :param argumentIdx: the index of the argument of self(this function) to make into the subject of the formula
        :type argumentIdx: int
        :param nodeIds: node ids (of the AST) to do the inversion on
        :type nodeIds: list[int]
        :return: multiple returns
            - Modified Abstract Syntax Tree
            - mapping from FUNC_NAME to (number of increase in FUNC_NAME in new tree, will be negative if it decrease)
            - mapping from variable_str to (number of increase in variable_str in new tree, will be negative it decrease)
            - how many primitives were added?
            - how many total nodes were added to the AST?
        :rtype: tuple[
            dict[tuple[str, int], list[tuple[str, int]]],
            dict[str, int],
            dict[str, int],
            int,
            int]
        """
        invertedResults, functionCountChange, primitiveCountChange, totalNodeCountChange, ast, permutation, key0, key1, replacementDictionary = self.preReverse(equationSide, argumentIdx, nodeIds, startPos__nodeId)
        if self.verbose:
            print('invertedResults')
            print(invertedResults)

        newRootOfTree = rootOfTree
        for oldKey, oldValue in invertedResults.items():
            if oldKey in ast: # due to addition of operations, `oldKey` might not exist in ast
                del ast[oldKey]
            ast[oldValue['newKey']] = list(oldValue['newValue'])
            #replace rootOfTree
            if oldKey == rootOfTree:
                newRootOfTree = oldValue['newKey']

        altered__startPos__nodeId, altered__nodeId__len = self._reverse__startPosRecalculation(permutation, replacementDictionary, ast, key0, key1, startPos__nodeId, invertedResults, nodeId__len)


        return ast, newRootOfTree, functionCountChange, primitiveCountChange, totalNodeCountChange, invertedResults, altered__startPos__nodeId, altered__nodeId__len


    def _reverse__startPosRecalculation(self, permutation, replacementDictionary, ast, key0, key1, startPos__nodeId, invertedResults, nodeId__len):
        #all these inputs need not be passed...? get from self? but inconvienent for reuse/testing?
        from copy import deepcopy # TODO refactor..., imported multiple times
        #TODO nodeId__len might also be changed, if another node is removed from it.
        #it seems that only key1's length is changed
        #actually key0's length is also changed, but key0 is always the =. which contains everything. And in reversal, everything does not change.
        key1ChildrenIdBefore = set(map(lambda t: t[1], replacementDictionary[key1]))
        key1ChildrenIdAfter = set(map(lambda t: t[1], invertedResults[key1]['newValue']))
        idsAdded = key1ChildrenIdAfter - key1ChildrenIdBefore
        idsRemoved = key1ChildrenIdBefore - key1ChildrenIdAfter
        lenChanged = 0
        for nodeId in idsRemoved:
            lenChanged -= nodeId__len[nodeId]
        for nodeId in idsAdded:
            lenChanged += nodeId__len[nodeId]
        nodeId__len__after = deepcopy(nodeId__len)
        nodeId__len__after[key1[1]] += lenChanged

        updated__nodeId__len = nodeId__len__after
        #changing the label(key1), might change the len
        newKey1Label = invertedResults[key1]['newKey'][0]
        oldKey1Label = key1[0]
        updated__nodeId__len[key1[1]] += (len(newKey1Label) - len(oldKey1Label))
        # print(updated__nodeId__len[key1[1]])
        # import pdb;pdb.set_trace()

        if self.verbose:
            print('id: ', key1[1], 'lenChanged', lenChanged)


        # print('permutation')
        # print(permutation)

        rowCol__nodeId = {
            (0, 0):replacementDictionary[key0][0][1], # [1], um die ausWeisungen zu bekommen
            (0, 1):replacementDictionary[key0][1][1],
            (1, 0):replacementDictionary[key1][0][1],
            # (1, 1):replacementDictionary[key1][1][1] # does not exist for 1arg functions
        }
        if len(replacementDictionary[key1]) > 1: # there might be 2arg functions
            rowCol__nodeId[(1, 1)] = replacementDictionary[key1][1][1]

        oRowCol__nodeId = {
            (0, 0):invertedResults[key0]['newValue'][0][1], # [1], um die ausWeisungen zu bekommen
            (0, 1):invertedResults[key0]['newValue'][1][1],
            (1, 0):invertedResults[key1]['newValue'][0][1],
            # (1, 1):invertedResults[key1]['newValue'][1][1] # does not exist for 1arg functions

        }
        if len(invertedResults[key1]['newValue']) > 1: # there might be 2arg functions
            oRowCol__nodeId[(1, 1)] = invertedResults[key1]['newValue'][1][1]


        # print("rowCol__nodeId")
        # print(rowCol__nodeId)
        nodeId__nodeId = {}
        for iRowCol, oRowCol in permutation.items():
            iNodeId = rowCol__nodeId[iRowCol]
            # oNodeId = rowCol__nodeId[oRowCol] # for 2 arg?
            oNodeId = oRowCol__nodeId[iRowCol]
            # #this does not work 
            # if len(replacementDictionary[key1]) > 1: 
            #     oNodeId = oRowCol__nodeId[iRowCol] # for 2 arg?
            # else:
            #     oNodeId = oRowCol__nodeId[iRowCol] # for 1 arg?
            nodeId__nodeId[iNodeId] = oNodeId
        #DFS to get the order, TODO technically its ALWAYS going to be 2 rows and 2 items in each row
        #i.e. a SMALL CONSTANT, do we need to invoke DFS? TODO
        stack = [self.eq.rootOfTree]#stack = [('=', 0)]#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        orderList__after = []
        #
        # print('nodeId__nodeId')
        # print(nodeId__nodeId)
        # print('replacementDictionary')
        # print(replacementDictionary)
        #
        while len(stack) > 0:
            current = stack.pop()
            children = replacementDictionary.get(current, [])
            stack += children
            if len(children) > 0:
                try:
                    idxInOrderList = orderList__after.index(current[1]) + 1
                except:
                    idxInOrderList = len(orderList__after)
                # print('current', current, 'children: ', children)
                for i, child in enumerate(children): # i so that we will insert in order of children after idxInOrderList
                    # print('putting in ', child[1], 'afmap', nodeId__nodeId[child[1]], 'at', idxInOrderList+i, ' of ', orderList__after)
                    orderList__after.insert(idxInOrderList+i, nodeId__nodeId[child[1]])
                    # print(orderList__after)
                    # import pdb;pdb.set_trace()

        #all the below calculation, can be done at PARENT LEVEL?
        #get the orderLists before and after permutation OF only the affected 4 nodeIds
        flattenedChildrenOfReplacementDictionary = sum(replacementDictionary.values(), [])
        relevantNodeIds = list(map(lambda t: t[1], flattenedChildrenOfReplacementDictionary))
        # sorted__newStartPos__nodeId__items = sorted(newStartPos__nodeId.items(), key=lambda t:t[0])
        sorted__startPos__nodeId__items = sorted(startPos__nodeId.items(), key=lambda t:t[0])
        # orderList__after = list(map(lambda t: t[1], filter(lambda t: t[1] in relevantNodeIds, sorted__newStartPos__nodeId__items)))
        orderList__before = list(map(lambda t: t[1], filter(lambda t: t[1] in relevantNodeIds, sorted__startPos__nodeId__items)))
        
        
        nodeIdContaining = key1[1]
        #
        # print(self.eq)
        # import pdb;pdb.set_trace()
        if self.verbose:
            print('startPos__nodeId', startPos__nodeId)
            print('sorted__startPos__nodeId__items', sorted__startPos__nodeId__items)
            print('~~~')

            print('replacementDictionary.values()', replacementDictionary)
            print('relevantNodeIds', relevantNodeIds)
            print('orderList__after', orderList__after)
            print('orderList__before', orderList__before)
            print('nodeIdContaining', nodeIdContaining)
        #
        #nodeIdsContainedBy(nodeIdContaining)
        nodeIdsContainedBy = list(map(lambda t: t[1], replacementDictionary[key1]))
        indexOfNodeIdContaining = orderList__before.index(nodeIdContaining)
        labelContaining = key1[0]
        nodeId__beforeLengths = {} # we are not taking absoluteLenght, just length relative to the start of the item being swapped
        #
        # print('orderList__before')
        # print(orderList__before)
        #
        for i, nodeId in enumerate(orderList__before):
            totalLen = 0
            skipAddingLengthOfNodeContainingId = False
            if nodeId in nodeIdsContainedBy and i > indexOfNodeIdContaining:
                #skip addition of len(nodeIdContaining) and only add the length of the label and openbracket and one-space
                skipAddingLengthOfNodeContainingId = True
                totalLen += len('(') + len(labelContaining) + len(' ') # labelContaining is the funcName of the nodeIdContaining
            for j, preNodeId in enumerate(orderList__before[:i]):
                if preNodeId == nodeIdContaining and skipAddingLengthOfNodeContainingId:
                    # print('***!',nodeId, 'skipping preNodeId', preNodeId, 'which is the containing')
                    continue
                #if then next two args (including nodeId) is contained in preNodeId, then we should only take the length of 
                #usually only happen on the key that is not =, which is key1 #actually always, so hardcode
                if j> indexOfNodeIdContaining and preNodeId in nodeIdsContainedBy and nodeId not in nodeIdsContainedBy: 
                    # print('***@',nodeId, 'skipping preNodeId', preNodeId, 'which is the containedBy and nodeId is NOT containedBy', )
                    continue
                totalLen += nodeId__len[preNodeId] + len(' ')
                #
                # print('****', nodeId, 'examining:', preNodeId, 'totalLen:', totalLen, 'justadded:', nodeId__len[preNodeId]+len(' '), 'of preNodeId', preNodeId)
                #
            nodeId__beforeLengths[nodeId] = totalLen
            # print('!***', nodeId__beforeLengths)
        
        
        #also need containment information, that is in the reversedDict..., and also done in the parent like this:
        # invertedResults = invertedResults
        #we assume that nodeIdContaining does not change
        nodeIdsContainedBy = list(map(lambda t: t[1], invertedResults[key1]['newValue']))
        indexOfNodeIdContaining = orderList__after.index(nodeIdContaining)
        nodeId__afterLengths = {}

        #
        # print('orderList__after')
        # print(orderList__after)
        #
        #labelContaining should be the label of the transformed
        # print(invertedResults)
        # import pdb;pdb.set_trace()
        labelContaining = invertedResults[key1]['newKey'][0]
        # import pdb;pdb.set_trace()
        for i, nodeId in enumerate(orderList__after):
            totalLen = 0
            skipAddingLengthOfNodeContainingId = False
            if nodeId in nodeIdsContainedBy and i > indexOfNodeIdContaining:
                #skip addition of len(nodeIdContaining) and only add the length of the label and openbracket and one-space
                skipAddingLengthOfNodeContainingId = True
                totalLen += len('(') + len(labelContaining) + len(' ') # labelContaining is the funcName of the nodeIdContaining
            for j, preNodeId in enumerate(orderList__after[:i]):
                if preNodeId == nodeIdContaining and skipAddingLengthOfNodeContainingId:
                    # print('***!',nodeId, 'skipping preNodeId', preNodeId, 'which is the containing')
                    continue
                #if then next two args (including nodeId) is contained in preNodeId, then we should only take the length of 
                #usually only happen on the key that is not =, which is key1 # actually always, so hardcode
                if j> indexOfNodeIdContaining and preNodeId in nodeIdsContainedBy and nodeId not in nodeIdsContainedBy:
                    # print('***@',nodeId, 'skipping preNodeId', preNodeId, 'which is the containedBy and nodeId is NOT containedBy', )
                    continue
                totalLen += updated__nodeId__len[preNodeId] + len(' ')
                #
                # print('****', nodeId, 'examining:', preNodeId, 'totalLen:', totalLen, 'justadded:', updated__nodeId__len[preNodeId]+len(' '), 'of preNodeId', preNodeId)
                # import pdb;pdb.set_trace()
                #
            nodeId__afterLengths[nodeId] = totalLen
            
        #
        if self.verbose:
            print('~~~~~~')
            print('nodeId__beforeLengths:')
            print(nodeId__beforeLengths)
            print('nodeId__afterLengths:')
            print(nodeId__afterLengths)
            print('changes:')
            for nodeId in nodeId__beforeLengths.keys():
                print(nodeId, ':', nodeId__afterLengths[nodeId],  '-',  nodeId__beforeLengths[nodeId], '=', nodeId__afterLengths[nodeId] - nodeId__beforeLengths[nodeId])
            print('~~~~~')
        #

        #but every other node that is contained in A, B, and C are shifted by that amount... and 
        #need to cut out subtree, rooted at A, B, C
        newStartPos__nodeId = {}#deepcopy(startPos__nodeId)
        # nodeId__startPos = dict(map(lambda t: (t[1],t[0]), startPos__nodeId.items()))
        # for iRowCol, oRowCol in permutation.items():
        #     iNodeId = rowCol__nodeId[iRowCol]
        #     oNodeId = rowCol__nodeId[oRowCol]
        #     startPos = nodeId__startPos[iNodeId]
        #     newStartPos__nodeId[startPos] = oNodeId #rough position...
        nodeId__startPos = dict(map(lambda t: (t[1], t[0]), startPos__nodeId.items()))
        # for row in replacementDictionary.values(): # 
        #     for node in row:
        #
        # print("flattenedChildrenOfReplacementDictionary")
        # print(flattenedChildrenOfReplacementDictionary)
        #
        for node in flattenedChildrenOfReplacementDictionary:
            startPosChange = nodeId__afterLengths[node[1]] - nodeId__beforeLengths[node[1]]
            #
            # print('startPosChange')
            # print(startPosChange)
            # print('node', node)
            #
            if node == key1: # key1 is the function Node , and it contains the other two , we don't want this change to propagate to children of key1
                newStartPos = nodeId__startPos[node[1]] + startPosChange
                newStartPos__nodeId[newStartPos] = node[1]
                continue
            #all the shifts below node should be = startPosChange
            subAST = self.eq._cutSubASTAtRoot(node)
            listOfChildren = list(subAST.values()) + [[node]] # children will not include root, so we need to use +[node] to add back the node
            if len(sum(listOfChildren, [])) == 0:
                listOfChildren = [list(subAST.keys())]
            # print('listOfChildren')
            # print(listOfChildren)
            #just take out all the node, which are at the values in subAST as lists
            for children in listOfChildren:
                for childNode in children:
                    newStartPos = nodeId__startPos[childNode[1]] + startPosChange
                    newStartPos__nodeId[newStartPos] = childNode[1]
                    #
                    # print('!!!!')
                    # print(newStartPos, childNode[1])
                    #

        #add back everything that was not touched.
        touchedNodeIds = newStartPos__nodeId.values()
        for startPos, nodeId in startPos__nodeId.items():
            if nodeId not in touchedNodeIds:
                newStartPos__nodeId[startPos] = nodeId
        return newStartPos__nodeId, updated__nodeId__len # need to add back the equals.



    def evalFunctor(self):
        """

        #~ DRAFT ~#
        
        evaluates the AST for functors like Differentiation and Integration


        TODO this is a sketch... please test&correct
        """
        #prevent circular import
        from foundation.automat.arithmetic.sfunctor import FUNCTOR_NAMES_TO_CLASS
        queue = [self.astScheme] # TODO need to insert the root.... of the AST.... which i did not put in...
        while len(queue) != 0:
            current = queue.pop()
            if current.label in FUNCTOR_NAMES_TO_CLASS: 
                neighbours = self.astScheme[current.label]
                subroot = neighbours[0]
                withrespectto = neighbours[1]
                self.astScheme = FUNCTOR_NAMES_TO_CLASS[current.label]._calculate(subroot, withrespectto)
                # put which neighbours in queue again?
