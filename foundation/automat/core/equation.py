from copy import deepcopy
from importlib import import_module

from foundation.automat.common.backtracker import Backtracker
from foundation.automat.arithmetic.function import Function
from foundation.automat.parser.parser import Parser

class Equation:
    """
    This is the entry point for automat, it is supposed to parse a string, that is the equation, into internal
    memory, which, for now, is a dictionary of list of nodes (node=tuple(label, id)). We call it Abstract
    Syntax Tree (ast for short).

    TODO ast should also be displayable in 2D/3D, and glow/shine and shift and rotate and all that
    TODO 2d/3d will help in debugging
    TODO PICKLE too? https://docs.python.org/3/library/pickle.html

    :param equationStr: the equation str to be parsed
    :type equationStr: str
    :param parserName: the name of the parser to be used
    :type parserName: str
    """
    FUNCNAME__MODULENAME = Function.FUNCNAME__MODULENAME()
    FUNCNAME__CLASSNAME = Function.FUNCNAME__CLASSNAME()


    def __init__(self, equationStr, parserName, verbose=False):
        """
        loads the parser with that name, throws a tantrum if parserName was not found. Also the constructor

        :param equationStr: the equation str to be parsed
        :type equationStr: str
        :param parserName: the name of the parser to be used
        :type parserName: str
        """
        self.verbose = verbose
        self._eqs = equationStr
        self._parserName = parserName
        (self.ast, self.functions, self.variables, self.primitives,
         self.totalNodeCount) = Parser(parserName).parse(self._eqs)
        self.availableStrsFormats = {
            self._parserName: self._eqs
        }
        #############
        if self.verbose:
            print('~~~~~~~~~~~~~~~~~~~~INIT')
            print(self.ast)
            print('self.functions', self.functions)
            print('self.variables', self.variables)
            print('self.primitives', self.primitives)
            print('self.totalNodeCount', self.totalNodeCount)
        #############


    def getFunctionClass(self, funcName):
        moduleName = Equation.FUNCNAME__MODULENAME[funcName]
        className = Equation.FUNCNAME__CLASSNAME[funcName]
        import importlib, inspect
        module_obj = importlib.import_module(f'.{moduleName}', package='foundation.automat.arithmetic.standard')
        klassName, functionClass = list(filter(lambda tup: tup[0]==className,inspect.getmembers(module_obj, predicate=inspect.isclass)))[0]
        globals()[className] = functionClass
        return functionClass

    def makeSubject(self, variable):
        """
        make variable the subject of this equation

        :param variable:
        :type variable: str
        :return: a new AST that has variable as the subject of the formula
        :rtype: dict[tuple[str, int], list[tuple[str, int]]]
        """
        #error checking
        if variable not in self.variables:
            raise Exception("Variable Not Available")
        if self.variables[variable] > 1: 
            #TODO, unable to further handle without more patterns like quadratic, cubic, quartic, 
            #TODO partial-fractions
            #TODO can put factorisation here
            #TODO put manipulate here
            #TODO manipulate: AST-equivalence-for-special-substitution-to-make-polynomials-techniques
            raise Exception("Cannot handle")

        if self.verbose:
            print('working on AST:', self.ast)

        #find path from subRoot to variable
        stack = [Backtracker(
            '=', #label
            None, #neighbours
            None, # argumentIdx
            None, #prev
            0, #id
        )]
        found = None
        while len(stack) != 0:
            current = stack.pop()
            if current.label == variable:
                found = current
                break
            currentNode = (current.label, current.id)
            for argumentIdx, (label, idx) in enumerate(self.ast.get(currentNode, [])):
                backtracker = Backtracker(
                    label, #label
                    None, #neighbours
                    argumentIdx, #argumentIdx
                    current, #prev=parent
                    idx
                )
                stack.append(backtracker)
        if found is None:
            raise Exception("No path to variable") # this shouldn't happen, most probably a parser error
        #find out which side of the equation found is on, need to backtrack all the way back to =, and see its argumentIdx
        if self.verbose:
            print('found.label:', found.label)
        foundBackUp = Backtracker(
            found.label,
            None,
            found.argumentIdx,
            found.prev,
            found.id
        )
        ops = [{
                    'functionName':found.label,
                    'argumentIdx':found.argumentIdx, # this is the argumentIdx of self in its parent
                    'id':found.id,
                    'lastId':found.prev.id if found.prev is not None else None
                }] # chain of inverses to apply,
        while found.prev is not None:
            found = found.prev
            if found.label != '=':#cannot apply reverse(=)
                ops.append({
                    'functionName':found.label,
                    'argumentIdx':found.argumentIdx, # this is the argumentIdx of self in its parent
                    'id':found.id,
                    # 'lastId':found.prev.id if found.prev is not None else None
                })
            # print('oplabel', found.label, ops)
        # originalAst = deepcopy(self.ast)
        #
        found = foundBackUp #reset found
        while found.prev is not None:
            if found.prev.label == '=':
                firstAncestorOfFound = (found.label, found.id)
                if self.verbose:
                    print(firstAncestorOfFound)
                childrenOfEquals = self.ast[('=', 0)]
                firstAncestorOfFoundChildIdx = childrenOfEquals.index(firstAncestorOfFound)
                if firstAncestorOfFoundChildIdx == 0:#left side
                    equationSide = 'L'
                elif firstAncestorOfFoundChildIdx == 1:#right side
                    equationSide = 'R'
                else:
                    raise Exception(f'firstAncestorOfFoundChildIdx: {firstAncestorOfFoundChildIdx}')
            found = found.prev
        if equationSide != 'L' and equationSide != 'R':
            raise Exception(f'equationSide must be L or R, equationSide:{equationSide}')

        operationOrderWithIdx = []
        for opIdx in range(1, len(ops)):
            hinOp = ops[opIdx-1]
            vorOp = ops[opIdx]
            operationOrderWithIdx.append({
                'functionName':vorOp['functionName'],
                'argumentIdx':hinOp['argumentIdx'], # take the child's argumentIdx
                'id':vorOp['id'],
                'lastId':0 # always going to be equals, after then prevOp....
            })
        ops = operationOrderWithIdx
        if self.verbose:
            print('ops', ops)
        #apply the reverses
        while len(ops) != 0:
            op = ops.pop(-1) # apply in reverse order (start with the one nearest to =)
            if self.verbose:
                print('applying op', op)
            functionClass = self.getFunctionClass(op['functionName'])
            (invertedAst, functionCountChange, primitiveCountChange, totalNodeCountChange) = functionClass(self, op['id'], verbose=self.verbose).reverse(
                equationSide, op['argumentIdx'], [op['id'], op['lastId']]
            )
            #update the `stat` of self
            self.ast = invertedAst #TODO since equation is changed after each op, we have to recalculate the next op again, after the reversal... and so, we only need to calculate one op at a time... => might it go into an infinity loop?
            for funcName, countChange in functionCountChange.items():
                self.functions[funcName] = self.functions.get(funcName, 0) + countChange
                if self.functions[funcName] == 0:
                    del self.functions[funcName]
            self.primitives += primitiveCountChange
            self.totalNodeCount += totalNodeCountChange
        return self.ast



    def substituteValue(self, substitutionDictionary):
        """

        substituteDictionary is mapping from variable to primitives (numbers), 

        TODO
        test substitute value for many multilevel-AST, after you get infinite precision & symbolic, like ChatGPT suggested.
        ChatGPT suggests that, to get infinity precision:
        1. use "from decimal import Decimal" (but this does not support trigonometric functions)
        2. implement your own trigo function: Taylor/Maclaurin series, ...
        3. get ideas from https://mpmath.org/ (although there are forum complains https://stackoverflow.com/questions/25714830/python-mpmath-not-arbitrary-precision)
        4. symbolic-irrationals-calculation. like give answers in log, sqrt, exponentials, pi, e, ....
            (ChatGPT ni yotte) other irrationals can come from:
            1. explicitly constructed irrational&transcendental numbers, Liouville Numbers, Chaitin Constant
            2. Infinite series, zeta(3)
            3. Continued fractions, golden ratio
            4. Integrals, Hypergeometric function
            5. Iterative processes, Newton's Method

        self.equation.ast, and then substitute each variable under each sub-AST using substituteDictionary

        :param substitutionDictionary: mapping from variable (str) to numbers
        :type substitutionDictionary: dict[str, float]
        """
        #error-checking
        if len(substitutionDictionary) == 0:
            raise Exception("Did not input substitution")
        for variableStr, value in substitutionDictionary.items():
            if variableStr not in self.variables:
                raise Exception("Function not in equation")
        from foundation.automat.common import isNum
        def _recursiveSubsituteValue(bt): # put in BackTracker for Storage, then DFS BackTracker to put in AST format
            ##########
            # print(bt)
            ##########
            node = (bt.label, bt.id)
            nodeName, nodeId = bt.label, bt.id
            children = self.ast.get(node, [])
            if len(children) == 0: # is leaf
                nodeName = substitutionDictionary.get(nodeName, nodeName)
                ############
                # print('return0')
                ############
                return Backtracker(
                    nodeName,
                    [],
                    None,
                    None,
                    nodeId
                )
            else:
                childBts = []
                substitutedChildren = []
                allPrimitives = True # number-like
                for child in children:
                    childName, childId = child
                    childBt = _recursiveSubsituteValue(Backtracker(
                        childName,
                        [],#filled by recursion if possible
                        None,
                        None, 
                        childId
                    ))
                    childBts.append(childBt)
                    substitutedChildName = childBt.label
                    substitutedChildId = childBt.id
                    substitutedChildren.append(substitutedChildName)
                    if not isNum(str(substitutedChildName)):
                        allPrimitives = False
                if allPrimitives:
                    functionClass = self.getFunctionClass(nodeName)
                    floatifiedChildren = list(map(lambda primitiveStr: float(primitiveStr), substitutedChildren))
                    # import pdb;pdb.set_trace()
                    num = functionClass(self, nodeId, verbose=self.verbose)._calculate(*floatifiedChildren)
                    ############
                    # print('return1')
                    ############
                    return Backtracker(
                        str(num),
                        [],
                        None,
                        None,
                        nodeId
                    )
                else:
                    ############
                    # print('return2')
                    ############
                    return Backtracker(
                        str(nodeName),
                        childBts,
                        None,
                        None,
                        nodeId
                    )
        rootBt = _recursiveSubsituteValue(Backtracker(
            '=',
            self.ast.get(('=', 0)),
            None,
            None,
            0
        ))
        newNodeId = 0
        oldId__newId = {}
        ast = {}
        stack = [rootBt]
        while len(stack) > 0:
            currentBt = stack.pop()
            stack += currentBt.neighbours
            if len(currentBt.neighbours) > 0:
                def childG(newId, neighbours):
                    for neighbour in neighbours:
                        yield (neighbour.label, newId) # yield because parents will always have the smaller id (they born first)
                        oldId__newId[newId] = neighbour.id
                        newId += 1

                # children = []
                # for childBt in currentBt.neighbours:
                #     children.append((childBt.label, childBt.id))
                newId = oldId__newId.get(currentBt.id, newNodeId)
                if newId == newNodeId:
                    newNodeId+=1
                ast[(currentBt.label, currentBt.id)] = [child for child in childG(newNodeId,  currentBt.neighbours)]
        return ast # substituted ast



    def linearEliminationBySubstitution(self, eq, variable):
        """
        Make variable the subject of the Equation:self and Equation:eq
        Find which side, variable is on each equation
        Take the side_variable_node of self = side_not_variable_node of eq
        Take every other node of eq and put into self.ast
        relabel the ids on the newly formed equation

        update the 
        functionCountChange
        primitiveCountChange
        totalNodeCountChange


        :param variable: variable to eliminate
        :type variable: str
        :param eq: another Equation containing the variable
        :type format: :class:`Equation`
        """
        if self.verbose:
            import pprint
            pp = pprint.PrettyPrinter(indent=4)
            print('before makeSubject self.ast totalNodeCount', self.totalNodeCount)
            print('before makeSubject eq.ast totalNodeCount', eq.totalNodeCount)

        self.makeSubject(variable)
        eq.makeSubject(variable)
        if self.verbose:
            print('after makeSubject self.ast: ', self.ast)
            print('after makeSubject self.ast totalNodeCount: ', self.totalNodeCount)
            print('after makeSubject self.ast functions: ', self.functions)
            print('after makeSubject self.ast variables: ', self.variables)
            print('after makeSubject self.ast primitives', self.primitives)
            print('after makeSubject eq.ast:', eq.ast)
            print('after makeSubject eq.ast totalNodeCount: ', eq.totalNodeCount)
            print('after makeSubject eq.ast functions: ', eq.functions)
            print('after makeSubject eq.ast variables: ', eq.variables)
            print('after makeSubject eq.ast primitives', eq.primitives)

        #find which side of the = does variable be on
        sideOfVariableOfSelf = None
        if self.ast[('=', 0)][0][0] == variable:
            sideOfVariableOfSelf = 0
            variableIdInSelf = self.ast[('=', 0)][0][1]
        elif self.ast[('=', 0)][1][0] == variable:
            sideOfVariableOfSelf = 1
            variableIdInSelf = self.ast[('=', 0)][1][1]
        else:
            raise Exception(f'{variable} not the subject of self') # something wrong with makeSubject
        sideOfNonVariableOfEq = None
        if eq.ast[('=', 0)][0][0] == variable:
            sideOfNonVariableOfEq = 1
            variableIdInEq = eq.ast[('=', 0)][0][1]
        elif eq.ast[('=', 0)][1][0] == variable:
            sideOfNonVariableOfEq = 0
            variableIdInEq = eq.ast[('=', 0)][1][1]
        else:
            raise Exception(f'{variable} not the subject of eq') # something wrong with makeSubject

        #move nodeId in self.ast that are > variableIdInEq, for consecutiveness
        newAst = {}
        stack = [('=', 0)]
        while len(stack) > 0:
            nodeName, nodeId = stack.pop()
            children = self.ast.get((nodeName, nodeId), [])
            stack += children
            if len(children) > 0: # only keeping those with children
                newChildren = []
                for child in children:
                    childName, childId = child
                    if childId > variableIdInSelf:
                        childId -= 1 # removing 1 variable
                    newChildren.append((childName, childId))
                if nodeId > variableIdInSelf:
                    nodeId -= 1 # removing 1 variable
                newAst[(nodeName, nodeId)] = newChildren
        self.ast = newAst

        from copy import deepcopy
        eqAst = deepcopy(eq.ast)
        #rename the ids of eqAst by adding self.totalNodeCount - 1 to all of eqAst
        amountToIncreaseId = self.totalNodeCount - 2 # we will be removing 2 id from eq.ast, = and variable
        newEqAst = {}
        stack = [('=', 0)]
        while len(stack) > 0:
            nodeName, nodeId = stack.pop()
            children = eqAst.get((nodeName, nodeId), [])
            stack += children
            if len(children) > 0: # we only put in nonLeaves
                newChildren = []
                for child in children:
                    childName, childId = child
                    if childId > variableIdInEq:
                        childId -= 1 # removing 1 variable
                    # import pdb;pdb.set_trace()
                    newChildren.append((childName, childId+amountToIncreaseId))
                if nodeId > variableIdInEq:
                    nodeId -= 1
                # import pdb;pdb.set_trace()
                newEqAst[(nodeName, nodeId+amountToIncreaseId)] = newChildren
        if self.verbose:
            print('new self.ast:')
            pp.pprint(self.ast)
            print(f'after increasing nodeId by amountToIncreaseId ({amountToIncreaseId}) :')
            pp.pprint(newEqAst)

        self.ast[('=', 0)][sideOfVariableOfSelf] = newEqAst[('=', amountToIncreaseId)][sideOfNonVariableOfEq]
        del newEqAst[('=', amountToIncreaseId)]
        if self.verbose:
            print('updating self.ast: ')
            pp.pprint(self.ast)
            print('with')
            pp.pprint(newEqAst)
        self.ast.update(newEqAst)
        if self.verbose:
            print('updated ast: ')
            pp.pprint(self.ast)
        #substitution complete

        #update functionCountChange, should have no functionCountChange
        def mergeCountDictionaries(d0, d1):
            commonKeys = set(d0.keys()).intersection(set(d1.keys()))
            cd0 = deepcopy(d0)
            cd1 = deepcopy(d1)
            for commonKey in commonKeys:
                cd0[commonKey] += cd1[commonKey]
            for key in (set(d1.keys()) - commonKeys):
                cd0[key] = cd1[key]
            return cd0
        eqFunctions = deepcopy(eq.functions)
        self.functions = mergeCountDictionaries(self.functions, eqFunctions)

        #remove 1 count of variable from a both
        eqVariable = deepcopy(eq.variables)
        eqVariable[variable] -= 1
        if eqVariable[variable] == 0:
            del eqVariable[variable]
        self.variables[variable] -= 1
        if self.variables[variable] == 0:
            del self.variables[variable]
        self.variables = mergeCountDictionaries(self.variables, eqVariable)

        #should have no change in primitives
        # import pdb;pdb.set_trace()
        self.primitives += eq.primitives#mergeCountDictionaries(self.primitives, eqPrimitives)
        # import pdb;pdb.set_trace()
        self.totalNodeCount += eq.totalNodeCount - 3 #the equalNode was removed, 2 variables from each AST, total 3 nodes
        return self.ast, self.functions, self.variables, self.primitives, self.totalNodeCount






    def toString(self, format):
        """
        write the equation to string

        :param format: states the format to be used, to write to a string
        :type format: str
        """
        if format not in self.availableStrsFormats:
            unparsedStr = Parser(format).unparse(self.ast)
            self.availableStrsFormats[format] = unparsedStr
        return self.availableStrsFormats[format]


    def _findCommonFactorOfDistributivePath(self, distributivePath):
        """

        #~ DRAFT ~#
        TODO test
        current target usage for one-term factorisation

        ~SKETCH~
        1. cut out the subAST of each termNode
            a. convert to SchemeStr
            b. Find ALL longestCommonSubStrings SL between this_SchemeStr and prev_SchemeStr
                ~a. find possibleCommonFactors = set(this_SL).intersection(set(prev_SL))
                    !a. if len(possibleCommonFactors) == 0, return [] # no common factor
            c. for each possibleCommonFactorStr in possibleCommonFactors, cfAST = Schemeparser._unparse(possibleCommonFactor)
                ~a. store cfAST in cfASTL
        2. return cfSATL # list of common factors in AST format

        :param distributivePath: list of nodes, where the names of all the nodes in distributivePath is distributiveOpStr (see _findAllDistributivePaths)
        :type distributivePath: list
        """
        subAST = self._cutSubASTAtRoot(distributivePath[0])
        subASTschemeStr = Schemeparser._unparse(ast=subAST) # TODO write test for _unparse
        #TODO need to find ALL commonsubstrings....
        possibleCommonFactors = set()
        for nextIdx in range(1, len(distributivePath)):
            subAST = self._cutSubASTAtRoot(termNode)
            subASTschemeStr = Schemeparser._unparse(ast=subAST) # TODO write test for _unparse
            #TODO need to find ALL commonsubstrings....



    def _findAllDistributivePaths(self, distributiveOpStr, baseOpStr):
        """

        #~ DRAFT ~#
        TODO test
        current target usage for one-term factorisation

        For Example: 
        distributionOpStr is '*' (Multiplication)
        baseOpStr is '+' (Addition)

        We assume COMMUTATIVITY since we do not order the returnList nor terms, and the FACTORISABLE can be a tree.

        ~SKETCH~
        1. Find a node with (distributionOpStr as name)
            a. if there are no such node,
                ~1. iterate through each node H of distributivePath,
                    !1. if name(H) != baseOpStr, break it into a new distributive path if more than 1 node, else discard (distributivePath with only 1 node, is not factorisable)
                ~2. return new distributivePaths
            b. if there is such a node GOTO STEP2
        2. Find its parent to find the HEAD of distribution
        3. DFS the HEAD of distribution, until children have not distributionOpStr as name
            a. save that as a distributivePath
            b. remove all the nodes in the distributivePath from ASTcopy
            c. GOTO STEP1
        
        :param distributionOpStr: the name of the node to find factor
        :type distributionOpStr: str
        :param baseOpStr: the name of the node to find factor
        :type baseOpStr: str
        """
        distributionPaths = []
        astCopy = copy.deepcopy(self.ast)
        foundDistributiveOp = True # so that it goes through the first pass
        while foundDistributiveOp:
            #~~~~~~~~~~~~~STEP1
            foundDistributiveOp = False
            #try to find a distributiveOp, must have children, so no need to look into values()
            distributiveOpNode = None
            for branchNode in astCopy:
                if branchNode[0] == distributiveOpStr:
                    foundDistributiveOp = True
                    distributiveOpNode = branchNode
                    break
            if distributiveOpNode is not None:
                #~~~~~~~~~~~~~STEP2
                #TODO refactor, this is similiar(PREDICATE:[if rootId in childenPos]: difference) algorithm as EnclosureTree.makeEnclosureTreeWithRoots
                #go all the way to Rome(non-distributiveOpStr), then DFS down..., collect all the (non-distributiveOpNode)
                distributiveRoot = distributiveOpNode
                checkAgain = True
                while checkAgain: # keep going up
                    checkAgain = False
                    for parent, children in astCopy.items():
                        if distributiveRoot in children and \
                            parent[0] == distributiveOpStr: #extra PREDICATE different from EnclosureTree.makeEnclosureTreeWithRoots
                            distributiveOpNode = parent
                            checkAgain = True
                            break # this is better than EnclosureTree.makeEnclosureTreeWithRoots (because tree so only 1 parent)
                #here we have root, DFS down
                #~~~~~~~~~~~~~STEP3 : TODO refer to unionfindbyrankwithcompressiontest.py
                # terms = []#Here we flatten the FACTORIZABLE to a path.... 
                # stack = [distributiveRoot]
                # while len(stack) > 0:
                #     current = stack.pop()
                #     children = astCopy[current]
                #     for child in children:
                #         if child[0] != distributiveOpStr:# a term, since childname!=distributiveOpStr #handle baseOp later
                #             terms.append(child) # communtative 

                #~~~~~~~~~~~~~STEP3a
                # distributivePaths.append(terms)
                distributivePaths = TermsOfBaseOp.findTermsOfBaseOp(self.ast, baseOpStr) #TODO test on equationtest.py 

                #~~~~~~~~~~~~~STEP3b
                for node in terms:
                    try:
                        del astCopy[node]
                    except:# will throw if node has no children
                        pass

        #~~~~~~~~~~~~~STEP~1
        newDistributivePaths = []
        for distributivePath in distributivePaths:
            newDistributivePath = []
            #
            for termNode in distributivePath:
                if termNode[0] != baseOpStr:
                    #break this distributivePath into another distributivePath
                    if len(newDistributivePath) > 1: # need at least 2 nodes to do factorisation
                        newDistributivePaths.append(newDistributivePath)
                    newDistributivePath = []
                else:
                    newDistributivePath.append(termNode)

        #~~~~~~~~~~~~~STEP~2
        return newDistributivePaths










    def _cutSubASTAtRoot(self, rootNode):
        """

        #~ DRAFT ~#
        TODO test
        current target usage for one-term factorisation

        ~SKETCH~
        Find the rootNode in self.ast, then DFS from there to get subAST
        
        TODO test
        """

        if rootNode not in self.ast: # rootNode might be a leaf(variables/primitives)
            if rootNode not in self.variables and rootNode not in self.primitives:
                raise Exception(f'rootNode is not a valid node of AST')
            else:
                return {rootNode: []} # since rootNode is a leaf, TODO thats not the format that we agreed to
        else: # rootNode is a non-leaf in self.ast, nous DFSons
            subAST = {}
            stack = [rootNode]
            while len(stack) > 0:
                current = stack.pop()
                children = self.ast[current]
                subAST[current] = children
                stack += children
            return subAST
