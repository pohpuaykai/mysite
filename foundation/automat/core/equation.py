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
        #############
        if self.verbose:
            print('self.functions', self.functions)
            print('self.variables', self.variables)
            print('self.primitives', self.primitives)
            print('self.totalNodeCount', self.totalNodeCount)
        #############

    def makeSubject(self, variable):
        """
        #~ DRAFT ~#
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
            #TODO, unable to further handle without more patterns like quadratic, cubic, quartic, AST-equivalence-for-special-substitution-to-make-polynomials-techniques
            #TODO partial-fractions
            #TODO can put factorisation here
            raise Exception("Cannot handle")

        if self.verbose:
            print('working on AST:', self.ast)

        #correct but inefficient.... keep it somewhere else? or remove?
        # op = {}
        # while len(op) ==0 or op['functionName'] != '=':

        #     #find path from subRoot to variable
        #     stack = [Backtracker(
        #         '=', #label
        #         None, #neighbours
        #         None, # argumentIdx
        #         None, #prev
        #         0, #id
        #     )]
        #     found = None
        #     while len(stack) != 0:
        #         current = stack.pop()
        #         if current.label == variable:
        #             found = current
        #             break
        #         currentNode = (current.label, current.id)
        #         for argumentIdx, (label, idx) in enumerate(self.ast.get(currentNode, [])):
        #             backtracker = Backtracker(
        #                 label, #label
        #                 None, #neighbours
        #                 argumentIdx, #argumentIdx
        #                 current, #prev=parent
        #                 idx
        #             )
        #             stack.append(backtracker)
        #     if found is None:
        #         raise Exception("No path to variable") # this shouldn't happen, most probably a parser error

        #     #create found backup
        #     foundBackUp = Backtracker(
        #         found.label,
        #         None,
        #         found.argumentIdx,
        #         found.prev,
        #         found.id
        #     )

        #     # import pdb;pdb.set_trace()
        #     #backtrack until found.prev is '=', then take found as op
        #     thePrev = None
        #     while found.prev.label != '=':
        #         thePrev = found
        #         found = found.prev
        #     if thePrev is None:
        #         break
        #     # import pdb;pdb.set_trace()
        #     op = {
        #         'functionName':found.label,
        #         'argumentIdx':thePrev.argumentIdx,#found.argumentIdx,#found.prev.argumentIdx,
        #         'id':found.id,
        #         'lastId':found.prev.id
        #     }
        #     #find which side subject is on :
        #     found = foundBackUp
        #     while found.prev is not None:
        #         if found.prev.label == '=':
        #             firstAncestorOfFound = (found.label, found.id)
        #             if self.verbose:
        #                 print(firstAncestorOfFound)
        #             childrenOfEquals = self.ast[('=', 0)]
        #             firstAncestorOfFoundChildIdx = childrenOfEquals.index(firstAncestorOfFound)
        #             if firstAncestorOfFoundChildIdx == 0:#left side
        #                 equationSide = 'L'
        #             elif firstAncestorOfFoundChildIdx == 1:#right side
        #                 equationSide = 'R'
        #             else:
        #                 raise Exception(f'firstAncestorOfFoundChildIdx: {firstAncestorOfFoundChildIdx}')
        #         found = found.prev
        #     if equationSide != 'L' and equationSide != 'R':
        #         raise Exception(f'equationSide must be L or R, equationSide:{equationSide}')
        #     #perform the op
        #     #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~HELPER_START
        #     def getFunctionClass(funcName):
        #         moduleName = Equation.FUNCNAME__MODULENAME[funcName] # TODO implement
        #         className = Equation.FUNCNAME__CLASSNAME[funcName] # TODO implement
        #         import importlib, inspect
        #         module_obj = importlib.import_module(f'.{moduleName}', package='foundation.automat.arithmetic.standard')
        #         klassName, functionClass = list(filter(lambda tup: tup[0]==className,inspect.getmembers(module_obj, predicate=inspect.isclass)))[0]
        #         globals()[className] = functionClass
        #         return functionClass
        #     #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~HELPER_END
        #     if self.verbose:
        #         print('applying op', op, 'equationSide', equationSide)
        #     functionClass = getFunctionClass(op['functionName'])
        #     (invertedAst, functionCountChange, primitiveCountChange, totalNodeCountChange) = functionClass(self, verbose=self.verbose).reverse(
        #         equationSide, op['argumentIdx'], [op['id'], op['lastId']]
        #     )
        #     #update the `stat` of self
        #     self.ast = invertedAst #TODO since equation is changed after each op, we have to recalculate the next op again, after the reversal... and so, we only need to calculate one op at a time... => might it go into an infinity loop?
        #     for funcName, countChange in functionCountChange.items():
        #         originalSum = self.functions.get(funcName, 0) + countChange
        #         self.functions[funcName] = originalSum
        #     self.primitives = primitiveCountChange
        #     self.totalNodeCount += totalNodeCountChange
        #     if self.verbose:
        #         print('reversed AST: ', self.ast)
        # return self.ast









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
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~HELPER_START
        def getFunctionClass(funcName):
            moduleName = Equation.FUNCNAME__MODULENAME[funcName] # TODO implement
            className = Equation.FUNCNAME__CLASSNAME[funcName] # TODO implement
            import importlib, inspect
            module_obj = importlib.import_module(f'.{moduleName}', package='foundation.automat.arithmetic.standard')
            klassName, functionClass = list(filter(lambda tup: tup[0]==className,inspect.getmembers(module_obj, predicate=inspect.isclass)))[0]
            globals()[className] = functionClass
            return functionClass
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~HELPER_END
        #apply the reverses
        while len(ops) != 0:
            op = ops.pop(-1) # apply in reverse order (start with the one nearest to =)
            if self.verbose:
                print('applying op', op)
            functionClass = getFunctionClass(op['functionName'])
            (invertedAst, functionCountChange, primitiveCountChange, totalNodeCountChange) = functionClass(self, verbose=self.verbose).reverse(
                equationSide, op['argumentIdx'], [op['id'], op['lastId']]
            )
            #update the `stat` of self
            self.ast = invertedAst #TODO since equation is changed after each op, we have to recalculate the next op again, after the reversal... and so, we only need to calculate one op at a time... => might it go into an infinity loop?
            for funcName, countChange in functionCountChange.items():
                originalSum = self.functions.get(funcName, 0) + countChange
                self.functions[funcName] = originalSum
            self.primitives = primitiveCountChange
            self.totalNodeCount += totalNodeCountChange
        return self.ast


    def toString(self, format):
        """
        #~ DRAFT ~#
        write the equation to string

        :param format: states the format to be used, to write to a string
        :type format: str
        """
        return Parser(format).unparse(self.ast)


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
