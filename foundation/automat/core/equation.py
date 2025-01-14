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


    def __init__(self, equationStr=None, parserName=None, ast=None, verbose=False):
        """
        loads the parser with that name, throws a tantrum if parserName was not found. Also the constructor

        SchemeString is a staple representation of this class.
        If parserName is not 'scheme', we need to unparse the self.ast to scheme and then store all the statistics, 
        including startPos__nodeId

        In this `Equation`, for all calculations, we will use the *Scheme version. Like if we want to use 
        ast, we will use the self.astScheme, instead of self.ast (which might be derived from other parsers, and 
        have different ids, ....)

        :param equationStr: the equation str to be parsed
        :type equationStr: str
        :param parserName: the name of the parser to be used
        :type parserName: str
        """
        self.verbose = verbose
        if ast is not None: # from ast to str
            from foundation.automat.parser.sorte.schemeparser import Schemeparser # not elegant, please refactor
            self.ast = ast
            self.astScheme = ast
            self.schemeparser = Schemeparser(ast=self.ast)
            self.schemeStr = self.schemeparser._unparse()
            self.functionsScheme = self.schemeparser.functions
            self.variablesScheme = self.schemeparser.variables
            self.primitivesScheme = self.schemeparser.primitives
            self.nodeId__lenScheme = self.schemeparser.nodeId__len
            self.startPos__nodeIdScheme = self.schemeparser.startPos__nodeId
            self._eqs = self.schemeStr
            self._parserName = 'scheme'
            self._parser = self.schemeparser

        else:
            self._eqs = equationStr
            self._parserName = parserName
            self._parser = Parser(parserName)
            (self.ast, self.functions, self.variables, self.primitives,
             self.totalNodeCount, self.startPos__nodeId) = self._parser.parse(self._eqs)
            if parserName.lower() == 'scheme':
                self.schemeStr = equationStr
                self.startPos__nodeId = self._parser.startPos__nodeId
                self.nodeId__len = self._parser.nodeId__len
                self.schemeparser = self._parser
                self.astScheme = self.ast
                self.functionsScheme = self.functions
                self.variablesScheme = self.variables
                self.primitivesScheme = self.primitives
                self.totalNodeCountScheme = self.totalNodeCount
                self.startPos__nodeIdScheme = self._parser.startPos__nodeId
                self.nodeId__lenScheme = self._parser.nodeId__len
            else: # unparse to schemeStr, because schemeStr and startPos__nodeId are essential data to equation now.
                from foundation.automat.parser.sorte.schemeparser import Schemeparser # not elegant, please refactor
                self.schemeparser = Schemeparser(ast=self.ast)
                self.schemeStr = self.schemeparser._unparse()
                self.astScheme = self.ast
                #TODO test, untested please future-me
                self.functionsScheme = self.schemeparser.functions
                self.variablesScheme = self.schemeparser.variables
                self.primitivesScheme = self.schemeparser.primitives
                self.totalNodeCountScheme = self.totalNodeCount
                self.nodeId__lenScheme = self.schemeparser.nodeId__len
                self.startPos__nodeIdScheme = self.schemeparser.startPos__nodeId

            #TODO this can be removed, once we calculate self.functionsScheme, self.variablesScheme, self.primitivesScheme, self.totalNodeCountScheme, self.startPos__nodeIdScheme
            #in _unparse :)
            # self.schemeparser._eqs=self.schemeStr # TODO future me please refactor, ugly
            # (self.astScheme, self.functionsScheme, self.variablesScheme, self.primitivesScheme,
            # self.totalNodeCountScheme, self.startPos__nodeIdScheme) = self.schemeparser._parse()
            # self.startPos__nodeId = self.schemeparser.startPos__nodeId
            # self.nodeId__lenScheme = self.schemeparser.nodeId__len
            #
            #
            
        self.availableStrsFormats = {
            self._parserName: self._eqs
        }
        #############
        if self.verbose:
            print('~~~~~~~~~~~~~~~~~~~~INIT')
            print(self.astScheme)
            print('self.functionsScheme', self.functionsScheme)
            print('self.variablesScheme', self.variablesScheme)
            print('self.primitivesScheme', self.primitivesScheme)
            print('self.totalNodeCountScheme', self.totalNodeCountScheme)
            print('self.startPos__nodeIdScheme', self.startPos__nodeIdScheme)
            print('self.nodeId__lenScheme', self.nodeId__lenScheme)
        #############


    def getFunctionClass(self, funcName):
        moduleName = Equation.FUNCNAME__MODULENAME[funcName]
        className = Equation.FUNCNAME__CLASSNAME[funcName]
        import importlib, inspect
        module_obj = importlib.import_module(f'.{moduleName}', package='foundation.automat.arithmetic.standard')
        klassName, functionClass = list(filter(lambda tup: tup[0]==className,inspect.getmembers(module_obj, predicate=inspect.isclass)))[0]
        globals()[className] = functionClass
        return functionClass

    def makeSubject(self, variable, simplify=False):
        """
        make variable the subject of this equation


        :param variable:
        :type variable: str
        :return: a new AST that has variable as the subject of the formula
        :rtype: dict[tuple[str, int], list[tuple[str, int]]]
        """
        #error checking
        if variable not in self.variablesScheme:
            raise Exception("Variable Not Available")
        if self.variablesScheme[variable] > 1: 
            #TODO, unable to further handle without more patterns like quadratic, cubic, quartic, 
            #TODO partial-fractions
            #TODO can put factorisation here
            #TODO put manipulate here
            #TODO manipulate: AST-equivalence-for-special-substitution-to-make-polynomials-techniques
            raise Exception("Cannot handle")

        if self.verbose:
            print('working on AST:', self.astScheme)

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
            for argumentIdx, (label, idx) in enumerate(self.astScheme.get(currentNode, [])):
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
                childrenOfEquals = self.astScheme[('=', 0)]
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
                'id':vorOp['id'], #this is the function nodeId
                'lastId':0 # always going to be equals, after then prevOp....
            })
        ops = operationOrderWithIdx
        if self.verbose:
            print('ops', ops)
        if simplify:
            from foundation.automat.core.manipulate.recommend.recommend import Recommend
            recommend = Recommend(self, verbose=self.verbose)
        #apply the reverses
        from foundation.automat.parser.sorte.schemeparser import Schemeparser # not elegant, please refactor
        while len(ops) != 0:
            op = ops.pop(-1) # apply in reverse order (start with the one nearest to =)
            if self.verbose:
                print('*****applying op', op)
            functionClass = self.getFunctionClass(op['functionName'])
            #TODO (optional)since equation is changed after each op, we have to recalculate the next op again, after the reversal... and so, we only need to calculate one op at a time... => might it go into an infinity loop?
            
            # (invertedAst, functionCountChange, primitiveCountChange, totalNodeCountChange, invertedResults) = functionClass(self, op['id'], verbose=self.verbose).reverse(
            #     equationSide, op['argumentIdx'], [op['id'], op['lastId']]
            # )
            # self.ast = invertedAst 
            #give hint to Recommend in order to do 'simplification' TODO
            if self.verbose:
                print('BEFORE nodeId__lenScheme', self.nodeId__lenScheme)
                print('BEFORE astScheme', self.astScheme)
                print('BEFORE startPos__nodeIdScheme', self.startPos__nodeIdScheme)
            (invertedAst, functionCountChange, primitiveCountChange, totalNodeCountChange, invertedResults, startPos__nodeId, nodeId__len) = functionClass(self, op['id'], verbose=self.verbose).reverse(
                equationSide, op['argumentIdx'], [op['id'], op['lastId']], self.startPos__nodeIdScheme, self.nodeId__lenScheme
            ) #TODO functionClass to make change to SchemeStr & startPos__nodeId too?
            self.nodeId__lenScheme = nodeId__len
            self.startPos__nodeIdScheme = startPos__nodeId
            self.astScheme = invertedAst
            self.schemeStr = Schemeparser(ast=self.astScheme)._unparse()
            if self.verbose:
                print('AFTER nodeId__lenScheme', self.nodeId__lenScheme)
                print('AFTER astScheme:', self.astScheme)
                print('AFTER startPos__nodeIdScheme', self.startPos__nodeIdScheme)
            if simplify:
                returnTup = recommend.simplify(hint={'invertedResults':invertedResults})#, 'lastOp':op})
                if returnTup is not None:
                    simplifiedAst, nodeIdOfPrimitivesRemoved, nodeIdOfVariablesRemoved, nodeIdOfFuncsRemoved = returnTup
                    ######
                    if self.verbose:
                        print('before simplifying:')
                        print(invertedAst)
                        print('after simplifying:')
                        print(simplifiedAst)
                        print('ops:')
                        print(ops)
                        print('simplifiedAst:')
                        print(simplifiedAst)
                        print('nodeIdOfPrimitivesRemoved:')
                        print(nodeIdOfPrimitivesRemoved)
                        print('nodeIdOfVariablesRemoved:')
                        print(nodeIdOfVariablesRemoved)
                        print('nodeIdOfFuncsRemoved:')
                        print(nodeIdOfFuncsRemoved)
                    """
                        SO, i need to look at the nodeIdOfFuncsRemoved & invertedAst (before simplification.)
                        And then manually, remove from invertedAst, what is in nodeIdOfFuncsRemoved? Wow, do that in general? How should the invertedAst be changed?
                        In this way, the ops, will not be disturbed.... and the original will not be disturbed.
                        This also means we do not need the simplifiedAst.....?
                    """
                    self._removeNodeIds(nodeIdOfPrimitivesRemoved+nodeIdOfVariablesRemoved+nodeIdOfFuncsRemoved) # this function will auto-update the astScheme, without changing the existing nodeIds on astScheme
                    ######
                    #need to recalculate path to variable again... because ast changed...
                    # we can also get `Recommend` to give us the changes made, then we can maybe just alter the ops a bit?
                    #TODO we do not do this calculation for now...
                    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # newOps = []
                    # for op0 in ops:
                    #     #TODO refactor the blanks underscores, 
                    #     (preInvertedAst, preFunctionCountChange, prePrimitiveCountChange, preTotalNodeCountChange,  _, _, _, _, _) = functionClass(self, op0['id'], verbose=self.verbose).preReverse(
                    #         equationSide, op0['argumentIdx'], [op0['id'], op0['lastId']], self.startPos__nodeIdScheme
                    #     )
                    #     #################
                    #     print('nodeIdOfFuncsRemoved')
                    #     print(nodeIdOfFuncsRemoved)
                    #     print(op0) # if changes in primitives/variables, op should be modified, instead of removed?
                    #     #TODO we need to match the OP's nodeId to nodeIdOfFuncsRemoved
                    #     print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                    #     import pdb;pdb.set_trace()
                    #     #################
                    #     # then we also remove this nodeId of function from ops...
                    #     # those removed might also be primitives or variables
                    #     if op0['id'] in nodeIdOfFuncsRemoved: 
                    #         # another way to do it, is if op fails... then just skip this op, and go to the next op? -> any situation where this might fail?
                    #         #if variable/primitive is removed. the reversal of that function containing it, still need to do correct reversal.
                    #         #skipping the reversal of that function , will result in incorrect answer. SO WRONG WAY
                    #         #TODO another way to do it, is invertedResults then we calculate from the changes...., but it seems, that first way is more efficient?
                    #         #preReverse is reading from a dictionary in a class... and then passing it up 2 classes (2 pieces in the tracestack.)
                    #         if self.verbose:
                    #             print(f"removed {op0['functionName']}, {op0['id']} from ops")
                    #         continue
                    #     newOps.append(op0)
                    # ops = newOps
                    # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    # self.astScheme = simplifiedAst

            # else: #no step-by-step simplification needed, should not raise exception...
            #     (invertedAst, functionCountChange, primitiveCountChange, totalNodeCountChange, invertedResults, startPos__nodeId) = functionClass(self, op['id'], verbose=self.verbose).reverse(
            #         equationSide, op['argumentIdx'], [op['id'], op['lastId']], self.startPos__nodeId, self.nodeId__len
            #     )
            #     self.startPos__nodeId = startPos__nodeId
            #     self.ast = invertedAst 

            #update the `stat` of self
            for funcName, countChange in functionCountChange.items():
                self.functionsScheme[funcName] = self.functionsScheme.get(funcName, 0) + countChange
                if self.functionsScheme[funcName] == 0:
                    del self.functionsScheme[funcName]
            for primitiveName, countChange in primitiveCountChange.items():
                self.primitivesScheme[primitiveName] = self.primitivesScheme.get(primitiveName, 0) + countChange
                if self.primitivesScheme[primitiveName] == 0:
                    del self.primitivesScheme[primitiveName]
            # self.primitivesScheme += primitiveCountChange
            self.totalNodeCountScheme += totalNodeCountChange

        #need to put the scheme string back
        self.schemeStr = self.schemeparser.unparse(ast=self.astScheme)
        return self.astScheme



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
            if variableStr not in self.variablesScheme:
                raise Exception("Function not in equation")
        from foundation.automat.common import isNum
        def _recursiveSubsituteValue(bt): # put in BackTracker for Storage, then DFS BackTracker to put in AST format
            ##########
            # print(bt)
            ##########
            node = (bt.label, bt.id)
            nodeName, nodeId = bt.label, bt.id
            children = self.astScheme.get(node, [])
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
            print('before makeSubject self.astScheme totalNodeCountScheme', self.totalNodeCountScheme)
            print('before makeSubject self.astScheme functionsScheme: ', self.functionsScheme)
            print('before makeSubject self.astScheme variablesScheme: ', self.variablesScheme)
            print('before makeSubject self.astScheme primitivesScheme', self.primitivesScheme)
            print('before makeSubject eq.astScheme totalNodeCountScheme', eq.totalNodeCountScheme)
            print('before makeSubject eq.astScheme functionsScheme: ', eq.functionsScheme)
            print('before makeSubject eq.astScheme variablesScheme: ', eq.variablesScheme)
            print('before makeSubject eq.astScheme primitivesScheme', eq.primitivesScheme)

        self.makeSubject(variable)
        eq.makeSubject(variable)
        if self.verbose:
            print('after makeSubject self.astScheme: ', self.astScheme)
            print('after makeSubject self.astScheme totalNodeCountScheme: ', self.totalNodeCountScheme)
            print('after makeSubject self.astScheme functionsScheme: ', self.functionsScheme)
            print('after makeSubject self.astScheme variablesScheme: ', self.variablesScheme)
            print('after makeSubject self.astScheme primitivesScheme', self.primitivesScheme)
            print('after makeSubject eq.astScheme:', eq.astScheme)
            print('after makeSubject eq.astScheme totalNodeCountScheme: ', eq.totalNodeCountScheme)
            print('after makeSubject eq.astScheme functionsScheme: ', eq.functionsScheme)
            print('after makeSubject eq.astScheme variablesScheme: ', eq.variablesScheme)
            print('after makeSubject eq.astScheme primitivesScheme', eq.primitivesScheme)

        #find which side of the = does variable be on
        sideOfVariableOfSelf = None
        if self.astScheme[('=', 0)][0][0] == variable:
            sideOfVariableOfSelf = 0
            variableIdInSelf = self.astScheme[('=', 0)][0][1]
        elif self.astScheme[('=', 0)][1][0] == variable:
            sideOfVariableOfSelf = 1
            variableIdInSelf = self.astScheme[('=', 0)][1][1]
        else:
            raise Exception(f'{variable} not the subject of self') # something wrong with makeSubject
        sideOfNonVariableOfEq = None
        if eq.astScheme[('=', 0)][0][0] == variable:
            sideOfNonVariableOfEq = 1
            variableIdInEq = eq.astScheme[('=', 0)][0][1]
        elif eq.astScheme[('=', 0)][1][0] == variable:
            sideOfNonVariableOfEq = 0
            variableIdInEq = eq.astScheme[('=', 0)][1][1]
        else:
            raise Exception(f'{variable} not the subject of eq') # something wrong with makeSubject

        #move nodeId in self.ast that are > variableIdInEq, for consecutiveness
        newAst = {}
        stack = [('=', 0)]
        while len(stack) > 0:
            nodeName, nodeId = stack.pop()
            children = self.astScheme.get((nodeName, nodeId), [])
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
        self.astScheme = newAst

        from copy import deepcopy
        eqAst = deepcopy(eq.astScheme)
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
            print('new self.astScheme:')
            pp.pprint(self.astScheme)
            print(f'after increasing nodeId by amountToIncreaseId ({amountToIncreaseId}) :')
            pp.pprint(newEqAst)

        self.astScheme[('=', 0)][sideOfVariableOfSelf] = newEqAst[('=', amountToIncreaseId)][sideOfNonVariableOfEq]
        del newEqAst[('=', amountToIncreaseId)]
        if self.verbose:
            print('updating self.astScheme: ')
            pp.pprint(self.astScheme)
            print('with')
            pp.pprint(newEqAst)
        self.astScheme.update(newEqAst)
        if self.verbose:
            print('updated astScheme: ')
            pp.pprint(self.astScheme)
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
        eqFunctions = deepcopy(eq.functionsScheme)
        self.functionsScheme = mergeCountDictionaries(self.functionsScheme, eqFunctions)

        #remove 1 count of variable from a both
        eqVariable = deepcopy(eq.variablesScheme)
        eqVariable[variable] -= 1
        if eqVariable[variable] == 0:
            del eqVariable[variable]
        self.variablesScheme[variable] -= 1
        if self.variablesScheme[variable] == 0:
            del self.variablesScheme[variable]
        self.variablesScheme = mergeCountDictionaries(self.variablesScheme, eqVariable)

        #should have no change in primitives
        # import pdb;pdb.set_trace()
        eqPrimitives = deepcopy(eq.primitivesScheme)
        self.primitivesScheme = mergeCountDictionaries(self.primitivesScheme, eqPrimitives)#self.primitivesScheme += eq.primitivesScheme#
        # import pdb;pdb.set_trace()
        self.totalNodeCountScheme += eq.totalNodeCountScheme - 3 #the equalNode was removed, 2 variables from each AST, total 3 nodes


        #TODO recalculate for startPos__nodeIdScheme
        #TODO recalculate for nodeId__lenScheme


        return self.astScheme, self.functionsScheme, self.variablesScheme, self.primitivesScheme, self.totalNodeCountScheme




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
        current target usage for one-term factorisation: seems to be done by `Manipulate` TODO do something about this...

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
        astCopy = copy.deepcopy(self.astScheme)
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
                distributivePaths = TermsOfBaseOp.findTermsOfBaseOp(self.astScheme, baseOpStr) #TODO test on equationtest.py 

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
        current target usage for one-term factorisation

        Find the rootNode in self.ast, then DFS from there to get subAST
        
        """

        if rootNode not in self.astScheme: # rootNode might be a leaf(variables/primitives)
            if rootNode[0] not in self.variablesScheme and rootNode[0] not in self.primitivesScheme:
                raise Exception(f'rootNode is not a valid node of AST')
            else:
                return {rootNode: []} # since rootNode is a leaf, TODO thats not the format that we agreed to
        else: # rootNode is a non-leaf in self.ast, nous DFSons
            subAST = {}
            stack = [rootNode]
            #
            # print('***', 'in _cutSubASTAtRoot')
            # print(self.ast)
            # print(rootNode)
            #
            while len(stack) > 0:
                current = stack.pop()
                children = self.astScheme.get(current, [])
                stack += children
                if len(children) > 0:
                    subAST[current] = children
            return subAST



    def _removeNodeIds(self, nodeIdsToRemove):
        """ TODO this might be repeated in Latexparser.... and alot of others, refactor AST into its own class (careful of the Python's internal ast.)
        nodeId can be a leaf (primitive/variable) or a func (branch having children)
        
        generally it does not make sense to remove a single leaf, since the resulting formula will become NOT well-formed.
        Usually the whole function is removed with some of its associated arguments.
        And the arguments that remain, are reattached to the removed-function's parent.


        ~SKETCH~
        0. check for noBranchNode => raise Exception
        1. get a map from childToParent.
        2. DFS down the astScheme, if both parent and child in nodeIds, then union
        3. UF.groupingWithFirstInserted will give subtrees with their respective roots
        4. for each root, 
            a. find parent, and what idx the root is in the parent
            b. find all children (not connected in UF)/(not in nodeIds)
            c. attach b to c
        5. DFS down, checking for 
            a. rootId (from 4a), then we start skipping
            b. childId (from 4b), then we stop skipping
                i.attach childId to parent(rootId)
        """
        branchNodeIds = list(map(lambda t: t[1], self.astScheme.keys()))
        branchNodes = []
        leafNodes = []
        for nodeId in nodeIdsToRemove:  
            if nodeId in branchNodeIds: # has children
                branchNodes.append(nodeId)
            else:
                leafNodes.append(nodeId)
        if len(branchNodes) == 0:
            raise Exception('Trying to only remove primitive/variables, will lead to NOT well-formed formula')

        #Step 1
        child__parent = {}
        nodeId__label = {}
        stack = [('=', 0)]
        while len(stack) > 0:
            parent = stack.pop()
            children = self.astScheme.get(parent, [])
            stack += children
            nodeId__label[parent[1]] = parent[0]
            for child in children:
                child__parent[child] = parent

        from foundation.automat.common.flattener import Flattener
        from foundation.automat.common.unionfindbyrankwithpathcompression import UnionFindByRankWithPathCompression
        childrenNodeIds = []
        for children in self.astScheme.values():
            for child in children:
                childrenNodeIds.append(child[1])
        allNodeIds = set(branchNodeIds).union(set(childrenNodeIds))
        #Union all the nodeIds together and get their subRoots
        uf = UnionFindByRankWithPathCompression(len(allNodeIds))
        #might need to map to a new Id that is consecutive, and also need the un-map to get the values back
        #since UF need consecutive IDs, but self.astScheme does not guarantee consecutive IDs
        allNodeIds = sorted(list(allNodeIds))
        nodeIds__consec = dict(zip(range(0, len(allNodeIds)), allNodeIds))
        consec__nodeIds = dict(zip(allNodeIds, range(0, len(allNodeIds))))
        #
        # print("nodeIdsToRemove")
        # print(nodeIdsToRemove)
        #
        #Step 2
        stack = [('=', 0)]
        while len(stack) > 0:
            parentNode = stack.pop()
            children = self.astScheme.get(parentNode, [])
            stack += children
            for child in children:
                # print('parentId:', parentNode[1], 'childId:', child[1])
                if parentNode[1] in nodeIdsToRemove and child[1] in nodeIdsToRemove:
                    uf.union(nodeIds__consec[parentNode[1]], nodeIds__consec[child[1]])
        #Step 3
        listOfList, listOfInfoDict = uf.groupingWithFirstInserted() # note that listOfList is contained in listOfInfoDict and is not used here
        listOfInfoDict = list(filter(lambda d: d['earliestJoiner'] in nodeIdsToRemove, listOfInfoDict))
        #
        # print("listOfInfoDict")
        # print(listOfInfoDict)
        #
        #Step 4
        subRootNodeId__leafChildNodeIdsArgIdx = {}
        for d in listOfInfoDict:
            subRootNodeId = consec__nodeIds[d['earliestJoiner']]
            subRootNode = (nodeId__label[subRootNodeId], subRootNodeId)
            #Step 4a
            argIdx = None
            if subRootNode in child__parent: # the =, has no parent
                parentNode = child__parent[subRootNode] # TODO deal with it
                childrenOfParentNode = self.astScheme[parentNode]
                for argIdx, childOfParentNode in enumerate(childrenOfParentNode):
                    if childOfParentNode[1] == subRootNodeId:
                        break # we have the argIdx
            #Step 4b
            neglectedChildrenNodes = []
            #get children of d['grouping'] 
            stack = [(nodeId__label[subRootNodeId], subRootNodeId)]
            while len(stack) > 0:
                node = stack.pop()
                children = self.astScheme.get(node, [])
                # import pdb;pdb.set_trace()
                for child in children:
                    if nodeIds__consec[child[1]] in d['grouping']:
                        stack.append(child)
                    else: # not part of the group, the 'neglected-children' of this grouping
                        neglectedChildrenNodes.append(child)
            #Step 4c
            if len(neglectedChildrenNodes) > 1: # i am not sure how to deal with this...yet
                raise Exception(f'root: {subRootNodeId} has more than 1 children: {neglectedChildrenNodes}')
            subRootNodeId__leafChildNodeIdsArgIdx[subRootNodeId] = {
                'argIdx':argIdx, 
                'leafChildren':neglectedChildrenNodes, 
                'parentNode':parentNode,
                'done':False
            }
        #Step 5
        #
        # print("subRootNodeId__leafChildNodeIdsArgIdx")
        # print(subRootNodeId__leafChildNodeIdsArgIdx)
        #
        choppedAndRegraftedAST = {}
        stack = [('=', 0, None)] # the None is which subRoot is this under, if not, then None
        while len(stack) > 0:
            currentNodeAndMain = stack.pop()
            currentNode = (currentNodeAndMain[0], currentNodeAndMain[1])
            children = self.astScheme.get(currentNode, [])
            for child in children:
                stack.append((child[0], child[1], None))
            if currentNodeAndMain[2] is None: # first check...
                #
                # print('****')
                # print('currentNodeAndMain[1]', currentNodeAndMain[1])
                # print(subRootNodeId__leafChildNodeIdsArgIdx)
                # print('in?', currentNodeAndMain[1] in subRootNodeId__leafChildNodeIdsArgIdx)
                #
                if currentNodeAndMain[1] in subRootNodeId__leafChildNodeIdsArgIdx:
                    currentNodeAndMain = list(currentNodeAndMain)
                    currentNodeAndMain[2] = currentNodeAndMain[1]
                    currentNodeAndMain = tuple(currentNodeAndMain)

            #
            # print('****')
            # print('subRootNodeId')
            # print(currentNodeAndMain[2])
            # print('choppedAndRegraftedAST')
            # print(choppedAndRegraftedAST)
            # import pdb;pdb.set_trace()
            #
            if currentNodeAndMain[2] is not None: # these are the nodes to be skipped(removed)
                #if we reached the leafChildOf this subtree, we should remove the Main(currentNodeAndMain[2])
                leafChildNodeIdsArgIdx = subRootNodeId__leafChildNodeIdsArgIdx[currentNodeAndMain[2]]
                subTreeRootNodeId = currentNodeAndMain[2]
                # if currentNodeAndMain[1] in leafChildNodeIdsArgIdx['leafChildren']:
                #     subTreeRootNodeId = None
                    #attach currentNode to parent of subRootNodeId
                    #need to remove the child in that argIdx
                if currentNode[1] not in nodeIdsToRemove and not leafChildNodeIdsArgIdx['done']: # only want the top of the children not in nodeIdsRemove, not everything.
                    #the first out of the stack, will be the top of the children not in nodeIdsRemove, since we DFS? -TODO proof
                    #if so, then once we made a attachment(here) for this leafChildNodeIdsArgIdx, we do not do it anymore :)
                    #
                    # print('children: ', choppedAndRegraftedAST[leafChildNodeIdsArgIdx['parentNode']])
                    # print('argIdx: ', leafChildNodeIdsArgIdx['argIdx'])
                    # print('currentNode: ', currentNode)
                    #
                    choppedAndRegraftedAST[leafChildNodeIdsArgIdx['parentNode']][leafChildNodeIdsArgIdx['argIdx']] = currentNode
                    leafChildNodeIdsArgIdx['done'] = True # to get the top of the children not in nodeIdsRemove
                for child in children:
                    stack.append((child[0], child[1], subTreeRootNodeId))
            else: # these are the nodes that should be kept
                #this:
                #choppedAndRegraftedAST[leafChildNodeIdsArgIdx['parentNode']][leafChildNodeIdsArgIdx['argIdx']] = currentNode
                #should be done here
                if len(children) > 0 and currentNode[1] not in nodeIdsToRemove:
                    choppedAndRegraftedAST[currentNode] = children
        return choppedAndRegraftedAST