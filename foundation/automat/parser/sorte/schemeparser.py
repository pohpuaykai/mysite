from foundation.automat.arithmetic.function import Function
from foundation.automat.common import Backtracker, findAllMatches, isNum, lenOrZero
from foundation.automat.parser.parser import Parser

class Schemeparser(Parser):
    """
    Naive Parser for Scheme Strings. More details about 'Scheme' format, check
    https://groups.csail.mit.edu/mac/ftpdir/scheme-7.4/doc-html/scheme_2.html
    """
    FUNC_NAMES = Function.FUNC_NAMES()

    def __init__(self, equationStr=None, verbose=False, veryVerbose=False, ast=None):
        if ast is None:
            self._eqs = equationStr
            self.verbose = verbose
            self.veryVerbose = veryVerbose
            self.equalTuple = None
            # self.ast, self.functions, self.variables, self.primitives, self.totalNodeCount, self.startPos__nodeId = self._parse()
        else:
            self.equalTuple = None
            self.ast = ast
            self.verbose = verbose
            self.veryVerbose = veryVerbose

    def _parse(self):
        """
        parses Scheme Strings into AST. eqs must be in 'Scheme' format.
        Each term starts with '(' and ends with ')'.
        After the first '(', is the procedure name, than a space
        Then followed by arguments, which can be a term or primitive, delimited by space.

        :param equationStr: the equation string to be parsed
        :type equationStr: str
        :return: tuple of
            - ast (Abstract Syntax Tree), map, key:tuple(label, id), value:list[tuple[label, id]]
            - functionsD (map from function_label_str to number of such functions there are in the equation)
            - variablesD (map from variable_label_str to number of such variables there are in the equation)
            - primitives (map from primitive_label_str to number of such primitives there are in the equation)
            - totalNodeCount (total number of nodes in the ast)
        :rtype: tuple[
            dict[tuple[str, int], list[tuple[str, int]]],
            dict[str, int],
            dict[str, int],
            int,
            int]
        """
        startPos__nodeId = {} # TODO do the same for LatexParser...
        functionsD = {}# function(str) to no_of_such_functions in the ast(int)
        variablesD = {}# variable(str) to no_of_such_variables in the ast(int)
        primitives = {}# primitives(str) to no_of_such_primities in the ast(int)
        totalNodeCount = 0# total number of nodes in the ast
        backtrackerRoot = self._recursiveParse(self._eqs, 0, 0) # return pointer to the root ( in process/thread memory)
        if self.verbose:
            print('return from _recursiveParse*************')
        ast = {}
        if self.verbose:
            print(f'return from _recursiveParse************* initialised ast: {ast}')
        currentId = 0
        stack = [{'bt':backtrackerRoot, 'tid':currentId}]
        startPos__nodeId[backtrackerRoot.prev] = currentId
        while len(stack) != 0:
            currentBt = stack.pop(0)
            tid = currentBt['tid']
            current = currentBt['bt']
            if self.verbose:
                print(f'label: {current.label}, argumentIdx: {current.argumentIdx}, id: {current.id}, tid:{tid}')
            #do the tabulating
            totalNodeCount += 1
            if isNum(current.label):
                primitives[current.label] = primitives.get(current.label, 0) + 1
            elif current.label in Schemeparser.FUNC_NAMES: # is a function
                functionsD[current.label] = functionsD.get(current.label, 0) + 1
            elif current.label != '=': # is a variable
                variablesD[current.label] = variablesD.get(current.label, 0) + 1
            #end of tabulating
            #node = (current.label, id)
            #ast[node] = ast.get(node, []) + current.neighbours
            #id += 1
            thisNodeId = currentId
            neighbourNodes = []
            for neighbour in sorted(current.neighbours, key=lambda neigh: neigh.argumentIdx, reverse=False):
                currentId += 1
                neighbourNodes.append((neighbour.label, currentId))
                startPos__nodeId[neighbour.prev] = currentId # neighbour.prev is actually the startPos of neighbour.label. (SORRY FOR THE CONFUSION! refactor if you want, future-me)
                stack.append({'bt':neighbour, 'tid':currentId})
            currentNode = (current.label, (current.argumentIdx, current.id))
            if self.verbose:
                print(f'ast: {ast}, currentNode: {currentNode}')
            if len(neighbourNodes) > 0: # avoid putting leaves as keys
                ast[(current.label, tid)] = neighbourNodes

        return ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId

    def _recursiveParse(self, eqs, level, parentStartPosOffset):
        """
        Handles the syntex of 'Scheme', but just stores the tree in the memory stack of the process/thread

        :param eqs: the equation string to be parsed
        :type eqs: str
        :param level: tree level
        :type level: int
        :return: root of the AST
        :rtype: :class:`Backtracker`
        """
        if self.verbose:
            print(f'recursive level: {level}, eqs: {eqs}, parentOffset: {parentStartPosOffset}')
        if (eqs.startswith('(') and not eqs.endswith(')')) or \
                (not eqs.startswith('(') and eqs.endswith(')')):
            raise Exception('Closing Brackets Mismatch')

        if eqs.startswith('('): # then it is a procedure
            strippedEqs = eqs[1:-1] # remove start and end brackets
            #find procedure label and end position of procedure label
            procedureLabel = ''
            realProcedureStartPos = parentStartPosOffset + 1 # because we stripped the (
            procedureEndPosition = None
            for idx, c in enumerate(strippedEqs):
                if c == ' ': # is a space...
                    procedureEndPosition = idx
                    break
                procedureLabel += c
            realProcedureEndPos = procedureEndPosition + parentStartPosOffset + 1 # because we stripped the (
            argumentsStr = strippedEqs[procedureEndPosition:].strip()
            #for original_string position calculation
            amountStrippedOnLeft = len(strippedEqs[procedureEndPosition:]) - len(strippedEqs[procedureEndPosition:].lstrip())
            argStrStartPos = realProcedureEndPos + amountStrippedOnLeft # absolute beginning of argStr
            #
            if self.verbose:
                print(f'argumentsStr: {argumentsStr}', 'procedureEndPosition', procedureEndPosition)
            #find individual arguments START
            bracketCounter = 0 #+1 for '(', -1 for ')'
            currentArgumentStr = ''
            arguments = []
            argStartPos = argStrStartPos # absolute beginning of each individual argstr
            argAmountStrippedOnLeft = 0
            for jc, c in enumerate(argumentsStr):
                if self.veryVerbose:
                    print(c, currentArgumentStr, c == ' ', bracketCounter == 0, '<<<<<<<<<<<<<<12<<<<<<<<<', jc)  
                currentArgumentStr += c
                if c == '(':
                    if bracketCounter == 0:
                        argStartPos = argStrStartPos + jc
                    bracketCounter += 1
                elif c == ')':
                    bracketCounter -= 1
                if c == ' ' and bracketCounter == 0: # (brackets are balanced) and this character c is a space
                    if self.veryVerbose:
                        print(c, currentArgumentStr, c == ' ', bracketCounter == 0, '<<<<<<<<<<<<<<<<<<<<<<<', jc)
                    #for original_string position calculation
                    argAmountStrippedOnLeft = len(currentArgumentStr) - len(currentArgumentStr.lstrip())
                    currentArgumentStr = currentArgumentStr.strip()
                    if len(currentArgumentStr) > 0:
                        arguments.append((currentArgumentStr, argStartPos + argAmountStrippedOnLeft))
                        argStartPos = argStrStartPos + jc + 1 # +1 for the space
                        currentArgumentStr = ''
            if len(currentArgumentStr) > 0: # left-overs, please eat!
                arguments.append((currentArgumentStr, argStartPos))
            #find individual argumets END
            if self.verbose:
                print(f'level: {level}, arguments: {arguments}')
            neighbours = []
            # for argumentIdx, backtrackNeighbour in enumerate(map(lambda argu: self._recursiveParse(argu, level+1), arguments)):
            for argumentIdx, backtrackNeighbour in enumerate(map(lambda tup: self._recursiveParse(tup[0], level+1, tup[1]), arguments)):
                if self.verbose:
                    print(f'recursive level: {level}, eqs: {eqs}, argumentIdx: {argumentIdx}, id: {backtrackNeighbour.id}, label: {backtrackNeighbour.label}')
                backtrackNeighbour.argumentIdx = argumentIdx
                neighbours.append(backtrackNeighbour)
            rootNode = Backtracker(
                procedureLabel, # label
                neighbours, # neighbours
                0,#  argumentIdx, will be set by calling process (self._recursiveParse)
                #+1 for the openBracket (
                realProcedureStartPos, #used as the startPos of procedureLabel, (SORRY FOR THE CONFUSION! refactor if you want, future-me)
                level, #id,   (depthId)
            )
            #for backtrackNeighbour in neighbours:
            #    backtrackNeighbour.prev = rootNode

        else:#primitive or variable
            rootNode = Backtracker(
                eqs, # label
                [], # neighbours
                0, # not used, argumentIdx
                parentStartPosOffset, #used as the startPos of eqs , (SORRY FOR THE CONFUSION! refactor if you want, future-me)
                level # not used, id
            )
        return rootNode

    def _findEqualTuple(self):
        for keyTuple in self.ast.keys():
            if keyTuple[0] == '=':
                self.equalTuple = keyTuple


    def _unparse(self):
        """

        :param abstractSyntaxTree:
        :type abstractSyntaxTree:
        """
        #find the (=, id)
        if self.equalTuple is None:
            self._findEqualTuple()
        if self.equalTuple is None:#noch equalTuple kann nicht finden
            raise Exception('No equal, Invalid Equation String')
        return self._recursiveUnparse(self.ast, self.equalTuple)

    def _recursiveUnparse(self, subAST, keyTuple):
        if keyTuple not in subAST: # is Leaf
            return keyTuple[0] # return the key, discard the ID
        argumentStr = ' '.join([self._recursiveUnparse(subAST, argumentTuple) for argumentTuple in subAST[keyTuple]])
        return f"({keyTuple[0]} {argumentStr})"


    def _toLatex(self):
        """
        #~ DRAFT ~#

        Then we call the _unparse function of Latex to get the NICESWEETSTRING
        """
        from foundation.automat.parser.sorte.latexparser import Latexparser
        if self.verbose:
            import pprint
            pp = pprint.PrettyPrinter(indent=4)
            print('self.ast***********')
            pp.pprint(self.ast)
            print('*******************')
        return Latexparser(ast=self.ast)._unparse()