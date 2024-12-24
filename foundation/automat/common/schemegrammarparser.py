from foundation.automat.common.regexshorts import Regexshorts as rs

class SchemeGrammarParser:


    def __init__(self, inputPattern, outputPattern, verbose=False):
        """
        A parser, that will try to match inputPattern with (variables that begin with $ and end with a number).
        and then places the values of those matched variables, into the outputPattern, that also has
        the same variables.
        
        :param inputPattern:
        :type inputPattern: str
        :param outputPattern:
        :type outputPattern: str
        :param verbose:
        :type verbose: bool
        """
        self.verbose=False
        self.rawOutputPattern = outputPattern
        self.rawInputPattern = inputPattern
        self.inputPattern, self.variables = self.prepareRawPattern(self.rawInputPattern)
        self.outputPattern, self.outVariables = self.prepareRawPattern(self.rawOutputPattern)
        self.calledBuildEnclosure = False

        import pprint
        self.pp = pprint.PrettyPrinter(indent=4)


    def buildEnclosureTree(self, schemeword):
        self.schemeword = schemeword
        self.id__data, self.enclosureTree = self.findAll(self.inputPattern, self.schemeword)
        self.calledBuildEnclosure = True
        self.noMatches = len(self.enclosureTree) == 1


    def parse(self, schemeword, nodeIdsToSkip=None):
        """
        parse the schemeword (Scheme-styled string), with the inputPattern, and try to find the variables
        in the inputPattern. 
        Then it wil fit the values of the variables in found from schemeword, into the variables of the
        outputPattern.

        :param schemeword:
        :type schemeword:
        :param nodeIdsToSkip:
        :type nodeIdsToSkip:
        """
        if nodeIdsToSkip is None:
            nodeIdsToSkip = []
        self.schemeword = schemeword
        self.nodeIdsToSkip = nodeIdsToSkip
        if not self.calledBuildEnclosure:
            self.buildEnclosureTree(self.schemeword)
        # import pdb;pdb.set_trace()
        if self.verbose:
            print('you may skip these ids, and not change it to outputPattern: ')
            self.pp.pprint(id__data)
        self.manipulatedSchemeWord = self.manipulate(
            self.schemeword,
            self.variables,
            self.rawOutputPattern,
            self.rawInputPattern,
            self.id__data,
            self.enclosureTree,
            self.nodeIdsToSkip
        )
        return self.manipulatedSchemeWord


    def findFirstSameLevel(self, pattern, schemeword, chopped=0):
        """
        
        :param pattern: SchemeGrammar-styled pattern
        all variables, start with $, and then have a integer that does not
        start with 0, (except 0 itself, so we can have $0)

        only returns FIRST sub-schemeword, that match pattern, on the TOP-level (i.e. widest)
        example, schemeword: '(= (+ a b) (+ c d))'
        will return: 
        1. (+ a b)
        ONLY

        example, schemeword: '(= (+ a b) (+ (+ c d) e))'
        will return:
        1. (+ a b)
        ONLY

        :type pattern: str
        :param schemeword:
        :type schemeword: str
        :param chopped:
        for the iterator(findAllSameLevel) to correct the position, of matched-string-that-was-chopped

        :type chopped: int

        :return:
        :rtype:
        """
        matchingBrackets = {}
        def getNextBalancedPos(beginPos): # innerClass, for memoisation of matchingBrackets
            if beginPos in matchingBrackets:
                return matchingBrackets[beginPos]
            else: # compute matchingBrackets
                #we assume that schemeword[beginPos] is a (
                stack = [beginPos]
                for i, c in enumerate(schemeword[beginPos+1:]):
                    if len(stack) == 0: # we balanced the brackets
                        return beginPos + i
                    if c == '(':
                        stack.append(beginPos + i)
                    elif c == ')':
                        openPos = stack.pop()
                        matchingBrackets[openPos] = beginPos + i # memoize
                        
        patternSegmentedByDollar = pattern.split('$')
        firstPre = patternSegmentedByDollar[0]
        firstSuf = patternSegmentedByDollar[1]
        for sPos in rs.lazyPrefixFinder(firstPre, schemeword):
            dollarPoss = []
            start = sPos
            for i in range(0, len(patternSegmentedByDollar) -1):
                pre = patternSegmentedByDollar[i]
                suf = patternSegmentedByDollar[i+1]
                if schemeword[start+len(pre)] == '(':
                    nextPos = getNextBalancedPos(start+len(pre)) + 1 # return None if cannot find
                else:#variable, find next place that starts with suf
                    try:
                        nextPos = schemeword[start+len(pre):].index(suf) + (start+len(pre))
                    except:
                        nextPos = None
                if nextPos is None: # cannot continue with this sPos
                    break # try the next sPos
                else:
                    #import pdb;pdb.set_trace()
                    dollarPoss.append((start+len(pre)+chopped, nextPos+chopped))
                    start = nextPos
            if len(dollarPoss) == len(patternSegmentedByDollar) - 1: # we got all the dollarPoss
                return sPos+chopped, start+len(suf)+chopped, dollarPoss


    def findAllSameLevel(self, pattern, schemeword):
        """
        1.calls findFirstSameLevel, gets match
        2.if there is a match, 
        3.  chops match from schemeword
        4.  repeat Step 1 with new-chopped-schemeword
        5.else
        6.  return all the matches


        :param pattern: SchemeGrammar-styled pattern
        all variables, start with $, and then have a integer that does not
        start with 0, (except 0 itself, so we can have $0)

        only returns all sub-schemeword, that match pattern, on the TOP-level (i.e. widest)
        example, schemeword: '(= (+ a b) (+ c d))'
        will return: 
        1. (+ a b)
        2. (+ c d)
        ONLY

        example, schemeword: '(= (+ a b) (+ (+ c d) e))'
        will return:
        1. (+ a b)
        2. (+ (+ c d) e)
        ONLY

        :type pattern: str
        :param schemeword:
        :type schemeword: str

        :return:
        :rtype:
        """
        answers = []
        tup = self.findFirstSameLevel(pattern, schemeword)
        chopped = 0
        while tup is not None:
            answers.append(tup)
            chopped += tup[1]
            tup = self.findFirstSameLevel(pattern, schemeword[tup[1]:], chopped)
        return answers


    def findAll(self, pattern, schemeword):
        """
        calls findAllSameLevel in a Depth-First-Search Fashion

        1.calls findAllSameLevel, to get all TOP-level-matches
        2.puts all TOP-level-matches into stack for DFS
        3.if no more matches from findAllSameLevel for all things remaining in stack, then return collected-matches

        Also, has a #DATA-MASSAGING portion
        calculates an EnclosureTree, a dict, where
        key: parentId
        value: list of childId, belong to parentId, and in the order of appearance of variables in pattern


        :param pattern:
        :type pattern:
        :param schemeword:
        :type schemeword:

        :return:
        :rtype:
        """
        id__data = {}
        matchedId = 0
        current = {'w':schemeword, 'id':matchedId, 'pid':None, 'cms':0, 'cme':len(schemeword), 'ms':0, 'me':len(schemeword)}
        stack = [current]
        id__data[matchedId] = current
        while len(stack) > 0:
            current = stack.pop()
            word = current['w']
            parentStart = id__data.get(current['id'], {'cms':0})['cms']
            matches = self.findAllSameLevel(pattern, word)
            if matches: # with leaves
                for mStart, mEnd, argPoss in matches:
                    matchedId += 1
                    id__data[matchedId] = {
                        'w':word[mStart:mEnd], 
                        'ms':mStart, 
                        'me':mEnd, 
                        'id':matchedId, 
                        'pid':current['id'],
                        'cms':parentStart+current['ms'],
                        'cme':parentStart+current['me']
                    }
                    for argPos in argPoss:
                        #matchedId += 1
                        dat = {
                            'w':word[argPos[0]:argPos[1]],
                            'id':matchedId,
                            'pid':current['id'],
                            'ms':argPos[0],
                            'me':argPos[1],
                        }
                        stack.append(dat)
            else:
                matchedId += 1
                id__data[matchedId] = {
                    'w':word, 
                    'ms':current['ms'], 
                    'me':current['me'], 
                    'id':matchedId, 
                    'pid':current['id'],
                    'cms':parentStart+current['ms'],
                    'cme':parentStart+current['me'],
                }
                
        #TODO i jumbled the ms and cms..., please fix, future-me
        #but quick-fix for now. we know that the absolute-position, will always be the s!=0
        #DATA-MASSAGING
        for k, v in id__data.items():
            takes = 'cms'
            takee = 'cme'
            if v[takes] == 0:
                takes = 'ms'
                takee = 'me'
            v.update({
                's':v[takes],
                'e':v[takee]
            })
        enclosureTree = {} # TODO refactor with EnclosureTree?
        import bisect
        sortKey = 'ms' # 'cms'
        for idx, data in id__data.items():
            if data['pid'] is not None:
                childIds = enclosureTree.get(data['pid'], [])
                if len(childIds) == 0:
                    childIds.append(data['id'])
                else:
                    startPoss = list(map(lambda idd: id__data[idd][sortKey], childIds))
                    mycms = id__data[data['id']][sortKey]
                    positionToInsert = bisect.bisect_left(startPoss, mycms)
                    childIds.insert(positionToInsert, data['id'])
                enclosureTree[data['pid']] = childIds
        return id__data, enclosureTree


    def prepareRawPattern(self, rawPattern):
        """
        We expect users to input scheme-styled rawPattern, with $\d+ as variables.
        But our program expects only $ as variables. so...
        Here, we convert $\d+ to $ in the rawPattern, and make a record.


        :param rawPattern:
        :type rawPattern:

        :return:
        :rtype:
        """
        import re
        variables = []
        #rawVariablesPosList = []
        for m in re.finditer('(\$\d+)', rawPattern):
            #rawVariablesPosList.append((m.start(), m.end(), m.group()))
            variables.append(m.group())
        pattern = re.sub(r'\$\d+', '$', rawPattern) # remove the numbers
        #variablesPosList = []
        # for m in re.finditer('(\$)', pattern):
        #     variablesPosList.append((m.start(), m.end(), m.group()))
        #rawVariables__variables = dict(zip(rawVariablesPosList, variablesPosList)) # attach to self, if we need this
        #variables__rawVariables = dict(zip(variablesPosList, rawVariablesPosList)) # attach to self, if we need this
        
        return pattern, variables


    def manipulate(self, oWord, variables, outputPattern, inputPattern, id__data, enclosureTree, nodeIdsToSkip):
        """
        recursively traverse the whole enclosureTree

        BaseCase:
            if leaf, return the matched string. (NO CHANGES)
        RecursiveCase:
            Map childIds(nodeId) -> replacementStr (recursive call)
            If nodeId was not matched (usually the original schemeword only)
                Place each replacementStr back, in reverseOrder
            Else
                If skiping nodeId
                    Use inputPattern
                Else
                    Use outputPattern
                Replace all variables in selectedPattern with replacementStr


        :return:
        :rtype: str
        """
        import copy
        def _recursiveManipulate(nodeId):
            # BaseCase
            if nodeId not in enclosureTree: # its a leaf
                return id__data[nodeId]['w']
            # RecursiveCase
            replaceStrs = []
            childIds = enclosureTree[nodeId]
            for childId in childIds: 
                data = id__data[childId]
                replaceStr = _recursiveManipulate(data['id'])
                replaceStrs.append(replaceStr)
            if id__data[nodeId]['pid'] is None:#it was not matched...
                rWord = copy.deepcopy(oWord)
                childId__replacedStr = dict(zip(childIds, replaceStrs))
                for childId in reversed(childIds): #have to replace from the back, else, the frontPositions might shift.
                    childData = id__data[childId]
                    rWord = rs.replaceAtPos(rWord, childData['s'], childData['e'], childId__replacedStr[childId])
                return rWord
            else:
                if nodeId in nodeIdsToSkip:
                    op = copy.deepcopy(inputPattern)
                else:
                    op = copy.deepcopy(outputPattern)
                for variable, replaceStr in zip(variables, replaceStrs): # childId are in the order of the variables in inputPattern
                    op = op.replace(variable, replaceStr)
            return op
        manipulatedSchemeEquationStr = _recursiveManipulate(0) # root__nodeId is always 0
        return manipulatedSchemeEquationStr