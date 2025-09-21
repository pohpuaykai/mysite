from foundation.automat.arithmetic.function import Function
from foundation.automat.common import findAllMatches, isNum, lenOrZero
from foundation.automat.parser.parser import Parser

class Schemeparser(Parser):
    """
    Naive Parser for Scheme Strings. More details about 'Scheme' format, check
    https://groups.csail.mit.edu/mac/ftpdir/scheme-7.4/doc-html/scheme_2.html
    """
    FUNC_NAMES = Function.FUNC_NAMES()

    def __init__(self, equationStr=None, verbose=False, veryVerbose=False, ast=None, rootOfTree=None):
        self.parserName = 'scheme'
        #this attribute is unique to schemeparsers for now
        self.nodeId__len = {} # TODO have a go on the equationStr, to remove all the excess spaces..., this will give problems to startPos__nodeId and nodeId__len
        if ast is None:
            self._eqs = equationStr
            self.verbose = verbose
            self.veryVerbose = veryVerbose
            self.rootOfTree = None
            # self.ast, self.functions, self.variables, self.primitives, self.totalNodeCount, self.startPos__nodeId = self._parse()
        else:
            self.rootOfTree = rootOfTree
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
        self.rootOfTree = (backtrackerRoot.label, currentId)
        startPos__nodeId[backtrackerRoot.prev] = currentId
        while len(stack) != 0:
            currentBt = stack.pop(0)
            tid = currentBt['tid']
            current = currentBt['bt']
            if self.verbose:
                print(f'label: {current.label}, argumentIdx: {current.argumentIdx}, id: {current.id}, tid:{tid}')
            #do the tabulating
            totalNodeCount += 1
            #
            # if isNum(current.label):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<does your isNum at least contain e and i?
            #     primitives[current.label] = primitives.get(current.label, 0) + 1
            # elif current.label in Schemeparser.FUNC_NAMES: # is a function
            #     functionsD[current.label] = functionsD.get(current.label, 0) + 1
            # elif current.label != '=': # is a variable
            #     variablesD[current.label] = variablesD.get(current.label, 0) + 1
            #
            #
            if len(current.neighbours) > 0: # it is a function
                functionsD[current.label] = functionsD.get(current.label, 0) + 1
            elif isNum(current.label): # is a primitive
                primitives[current.label] = primitives.get(current.label, 0) + 1
            else:
                variablesD[current.label] = variablesD.get(current.label, 0) + 1

            #
            #end of tabulating
            #node = (current.label, id)
            #ast[node] = ast.get(node, []) + current.neighbours
            #id += 1
            self.nodeId__len[tid] = current.length
            thisNodeId = currentId
            neighbourNodes = []
            for neighbour in sorted(current.neighbours, key=lambda neigh: neigh.argumentIdx, reverse=False):
                currentId += 1
                neighbourNodes.append((neighbour.label, currentId))
                startPos__nodeId[neighbour.prev] = currentId # neighbour.prev is actually the startPos of neighbour.label. (SORRY FOR THE CONFUSION! refactor if you want, future-me)
                stack.append({'bt':neighbour, 'tid':currentId})
            currentNode = (current.label, (current.argumentIdx, current.id))
            if self.verbose:
                print(f'ast: {ast}, currentNode: {currentNode}, thisNodeId: {thisNodeId}, nodeId__len: {self.nodeId__len}')
            if len(neighbourNodes) > 0: # avoid putting leaves as keys
                ast[(current.label, tid)] = neighbourNodes
        self.ast=ast
        self.startPos__nodeId = startPos__nodeId
        self.functions = functionsD
        self.variables = variablesD
        self.primitives = primitives
        self.totalNodeCount = totalNodeCount
        return ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId

    def getASTDepth(self):
        """"""
        if getattr(self, 'depth', None) is None:
            self.depth = len(self.ast) + 1 if len(self.startPos__nodeId) > 0 else 0# +1 is for the leaves
        return self.depth

    def getASTWidth(self):
        """
        Use leveling information to get the width
        all the nodes on the same level is the width of the level
        so if leveling information is not available it needs to be calculated
        #there is code overlap with _getLevelingInformation, so refactor?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        if getattr(self, 'width', None) is None:
            self.width = max(map(lambda list_nodeId: len(list_nodeId), self.getLevelToNodeIds().values()))
        return self.width

    def getLevelToNodeIds(self):
        if getattr(self, 'level__list_nodeIds', None) is None:
            self.level__list_nodeIds = {}
            stack = [(self.rootOfTree, 0)]
            while len(stack) > 0:
                currentNode, currentLevel = stack.pop()
                #collect
                existingList = self.level__list_nodeIds.get(currentLevel, [])
                existingList.append(currentNode)
                self.level__list_nodeIds[currentLevel] = existingList
                #
                childNodes = self.ast.get(currentNode, [])
                childNodesTaggedWithLevel = list(zip(childNodes, [currentLevel+1]*len(childNodes)))
                stack += childNodesTaggedWithLevel
        return self.level__list_nodeIds


    def getLabelsInOrderOfStartPos(self):
        if getattr(self, 'labelsInOrderOfStartPos', None) is None:
            #the schemeparser might have been initiated from ast
            if getattr(self, '_eqs', None) is None:
                self._eqs = self._unparse()
            self.labelsInOrderOfStartPos = []; nodeId__labelLen = self._getLabelLength()
            for startPos, nodeId in sorted(self.startPos__nodeId.items(), key=lambda t: t[0]):
                self.labelsInOrderOfStartPos.append(self._eqs[startPos:startPos+nodeId__labelLen[nodeId]])
        return self.labelsInOrderOfStartPos

    def getListWithoutLabels(self):
        if getattr(self, 'listWithoutLabels', None) is None:
            delimiterThatCannotBeUsedInSchemeStr = ')(' # because any )(, must have a space in between
            from copy import copy
            stringWithoutLabels = copy(self._eqs)
            for label, _ in self.functions.items():
                stringWithoutLabels = stringWithoutLabels.replace(label, delimiterThatCannotBeUsedInSchemeStr)
            for label, _ in self.variables.items():
                stringWithoutLabels = stringWithoutLabels.replace(label, delimiterThatCannotBeUsedInSchemeStr)
            for label, _ in self.primitives.items():
                stringWithoutLabels = stringWithoutLabels.replace(label, delimiterThatCannotBeUsedInSchemeStr)
            self.listWithoutLabels = stringWithoutLabels.split(delimiterThatCannotBeUsedInSchemeStr)
            # print('self.listWithoutLabels', self.listWithoutLabels); import pdb;pdb.set_trace()
        return self.listWithoutLabels


    def _getLabelLength(self):
        """
        #some parts of schemegrammarparser duplicates this implementation, please remove from schemegrammarparser<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        """
        if getattr(self, 'nodeId__labelLen', None) is None:
            self.nodeId__labelLen = {}
            if len(self.ast) == 0 and len(self._eqs) != 0: # this is a single leaf, and the single leaf will not appear on self.ast.
                self.nodeId__labelLen[self.rootOfTree[1]] = len(self._eqs)
            else:
                for (pLabel, pNodeId), childNodes in self.ast.items():
                    self.nodeId__labelLen[pNodeId] = len(pLabel)
                    for (cLabel, cNodeId) in childNodes:
                        self.nodeId__labelLen[cNodeId] = len(cLabel)
            # print('_getLabelLength: ', nodeId__labelLen)
        return self.nodeId__labelLen



    def _getLevelingInformation(self):
        """This requires ast, startPos__nodeId, nodeId__len to have been calculated"""
        #difference between entity and label, entity is the whole openBracket, while label is the name of the schemeFunction
        #all the nodeStartPos are entityStartPos, not labelStartPos
        nodeStartPos__nodeEndPos = {}; level__nodeStartPos = {}; nodeStartPos__level = {} # for quick jumping to nodeEndPos, when matching segments
        #fill up nodeStartPos__nodeEndPos
        nodeId__entityStartPos = {}
        for startPos, nodeId in self.startPos__nodeId.items():
            if self._eqs[startPos-1] == '(':
                nodeStartPos__nodeEndPos[startPos-1] = startPos-1 + self.nodeId__len[nodeId]
                nodeId__entityStartPos[nodeId] = startPos - 1
            else:
                nodeStartPos__nodeEndPos[startPos] = startPos + self.nodeId__len[nodeId]
                nodeId__entityStartPos[nodeId] = startPos
        #fill up level__nodeStartPos & nodeStartPos__level, by using ast
        rootId = self.rootOfTree[1]; level__nodeStartPos[0] = [nodeId__entityStartPos[rootId]]; nodeStartPos__level[nodeId__entityStartPos[rootId]] = 0
        stack = [(self.rootOfTree, 0)]; 
        while len(stack) > 0:
            currentNode, currentLevel = stack.pop()
            childNodes = self.ast.get(currentNode, [])
            childNodesTaggedWithLevel = list(zip(childNodes, [currentLevel+1]*len(childNodes)))
            stack += childNodesTaggedWithLevel
            #
            for childNode, childLevel in childNodesTaggedWithLevel:
                childId = childNode[1]
                #
                existing = level__nodeStartPos.get(childLevel, [])
                existing.append(nodeId__entityStartPos[childId]); 
                level__nodeStartPos[childLevel] = existing
                #
                nodeStartPos__level[nodeId__entityStartPos[childId]] = childLevel
        self.nodeStartPos__nodeEndPos = nodeStartPos__nodeEndPos
        level__nodeStartPos___sorted = {}
        for level, list_nodeStartPos in level__nodeStartPos.items():
            level__nodeStartPos___sorted[level] = sorted(list_nodeStartPos)
        self.level__nodeStartPos = level__nodeStartPos___sorted
        self.nodeStartPos__level = nodeStartPos__level
        self.nodeId__entityStartPos = nodeId__entityStartPos
        return nodeStartPos__nodeEndPos, level__nodeStartPos___sorted, nodeStartPos__level, nodeId__entityStartPos

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
            openBra__count___others = {'{':0, '[':0}; closeBra__openBra = {'}':'{', ']':'['} # this is for test__latexParserUnparse__bipartiteSearch_dc_twoResistor_parallel_STEP1, where there are compound variables
            for idx, c in enumerate(strippedEqs):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<do bracket_accounting here
                #
                if c in openBra__count___others.keys():
                    openBra__count___others[c] += 1
                elif c in closeBra__openBra.keys():
                    openBra__count___others[closeBra__openBra[c]] -= 1
                #
                if not any(map(lambda count: count!=0, openBra__count___others.values())) and \
                (c == ' '): #first part is to allow anything within {} and [] to be counted as 1 entity is a space...
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
            openBra__count___others = {'{':0, '[':0}; closeBra__openBra = {'}':'{', ']':'['} # this is for test__latexParserUnparse__bipartiteSearch_dc_twoResistor_parallel_STEP1, where there are compound variables
            
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
                #bracket_accounting here:
                if c in openBra__count___others.keys():
                    openBra__count___others[c] += 1
                elif c in closeBra__openBra.keys():
                    openBra__count___others[closeBra__openBra[c]] -= 1
                #
                if not any(map(lambda count: count!=0, openBra__count___others.values())) and \
                 (c == ' ' and bracketCounter == 0): # (brackets are balanced) and this character c is a space
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
                level, #id,   (depthId),
                len(eqs)
            )
            #for backtrackNeighbour in neighbours:
            #    backtrackNeighbour.prev = rootNode

        else:#primitive or variable
            rootNode = Backtracker(
                eqs, # label
                [], # neighbours
                0, # not used, argumentIdx
                parentStartPosOffset, #used as the startPos of eqs , (SORRY FOR THE CONFUSION! refactor if you want, future-me)
                level, # not used, id
                len(eqs)
            )
        return rootNode

    def _findEqualTuple(self):
        for keyTuple in self.ast.keys():
            if keyTuple[0] == '=':
                self.rootOfTree = keyTuple


    def _unparse(self):
        """

        :param abstractSyntaxTree:
        :type abstractSyntaxTree:
        """
        self.startPos__nodeId = {}
        self.functions = {}
        self.variables = {}
        self.primitives = {}
        #find the (=, id)
        if self.rootOfTree is None:
            self._findEqualTuple()#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<brauchst du noch diese?
        if self.rootOfTree is None:#noch rootOfTree kann nicht finden
            raise Exception('No equal, Invalid Equation String')
        # print(self.ast); import pdb;pdb.set_trace()
        returnTup = self._recursiveUnparse(self.ast, self.rootOfTree, 0)
        # if '=' in self.functions:
        #     del self.functions['=']
        return returnTup

    def _recursiveUnparse(self, subAST, keyTuple, startPos):
        if keyTuple not in subAST: # is Leaf
            self.startPos__nodeId[startPos] = keyTuple[1]
            self.nodeId__len[keyTuple[1]] = len(keyTuple[0])
            if isNum(keyTuple[0]):
                self.primitives[keyTuple[0]] = self.primitives.get(keyTuple[0], 0) + 1
            else: # a variable
                self.variables[keyTuple[0]] = self.variables.get(keyTuple[0], 0) + 1
            return keyTuple[0] # return the key, discard the ID
        else:
            startPos += len('(')
            self.startPos__nodeId[startPos] = keyTuple[1]
            self.functions[keyTuple[0]] = self.functions.get(keyTuple[0], 0) + 1
        # argumentStr = ' '.join([self._recursiveUnparse(subAST, argumentTuple) for argumentTuple in subAST[keyTuple]])

        startPos += len(keyTuple[0]) + len(' ')
        argStrs = []
        for i, argumentTuple in enumerate(subAST[keyTuple]):
            argStr = self._recursiveUnparse(subAST, argumentTuple, startPos)
            # print('startPos', startPos, 'argStr', argStr)
            startPos += len(argStr)
            if i < len(subAST[keyTuple]) -1: #not the last argument in subAST[keyTuple]
                startPos +=len(' ')
            argStrs.append(argStr)
        # print('~~~~~~~~~~~')
        argumentStr = ' '.join(argStrs)
        subSchemeStr = f"({keyTuple[0]} {argumentStr})"
        self.nodeId__len[keyTuple[1]] = len(subSchemeStr)
        # print(subSchemeStr+'|')
        return subSchemeStr


    def _toLatex(self):
        """
        #~ DRAFT ~#

        Then we call the _unparse function of Latex to get the NICESWEETSTRING
        """
        from foundation.automat.parser.sorte.latexparser import Latexparser
        # print(self.ast); import pdb;pdb.set_trace()
        if getattr(self, 'ast', None) is None:
            self._parse()
        if self.verbose:
            import pprint
            pp = pprint.PrettyPrinter(indent=4)
            print('self.ast***********')
            pp.pprint(self.ast)
            print('*******************')
        return Latexparser(ast=self.ast, rootOfTree=self.rootOfTree)._unparse()


class Backtracker:
    """
    Used in some tree traversal algorithms, allow selected path to be reconstructed.
    Holds the name of nodes, the neighbours of nodes, prev is the parent of this, id is this id in the whole tree
    Also used to hold the traversal itself in the memory of this process/thread, so that it can be re-made to a
    pythonic format (or not).

    TODO should it be a "container" class?... Mixin?

    :param label: name of this Node
    :type label: str
    :param neighbours: connections to this Backtracker
    :type neighbours: list[:class:`Backtracker`]
    :param argumentIdx: the position of this Node on its parent,which also denotes its position as an argument on
    its parent as a function
    :param prev: a BackTracker, denoting the previous link
    :type prev: :class: `BackTracer`
    :param id: id of this BackTracker, in the tree
    :type id: int
    """
    def __init__(self, label, neighbours, argumentIdx, prev, id, length):
        """
        Just getters and setter. Also the constructor.

        :param label: name of this Node
        :type label: str
        :param neighbours: connections to this Node, elements are tuples
            -item.0 : label
            -item.1 : id of the node in the tree
        :type neighbours: list[tuple[str, int]]
        :param argumentIdx: the position of this Node on its parent,which also denotes its position as an argument on
        its parent as a function
        :param prev: a BackTracker, denoting the previous link
        :type prev: :class: `BackTracer`
        :param id: id of this Node, in the tree
        :type id: int
        """
        self.label = label
        self.neighbours = neighbours
        self.argumentIdx = argumentIdx
        self.prev = prev
        self.id = id
        self.length = length