from foundation.automat.common.regexshorts import Regexshorts as rs
from foundation.automat.common.longestcommonsubsequence import LongestCommonSubsequence

class SchemeGrammarParser:


    def __init__(self, inputPattern, outputPattern, verbose=False, recordMaking=False):
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
        self.inputPattern, self.variables, self.inVariablesAndPos, self.inVariablesPosSansVarnumList = self.prepareRawPattern(self.rawInputPattern)
        self.outputPattern, self.outVariables, self.outVariablesAndPos, self.outVariablesPosSansVarnumList = self.prepareRawPattern(self.rawOutputPattern)
        self.calledBuildEnclosure = False
        self.subsitutedOutputGrammar = self.outputPattern
        self.additionalReplacementStrForVariablesDict = {}


        self.recordMaking = recordMaking
        self.patternChanges()
        import pprint
        self.pp = pprint.PrettyPrinter(indent=4)


    def buildEnclosureTree(self, schemeword):
        self.schemeword = schemeword
        self.id__data, self.enclosureTree = self.findAll(self.inputPattern, self.schemeword)
        self.calledBuildEnclosure = True
        # this inputPattern is not applicable to this schemeword. Note that, if there are no variables in inputPattern, it might still be a match
        # import pdb;pdb.set_trace()
        self.noMatches = (len(self.id__data) == 2) and (self.id__data[0]['w']==self.id__data[1]['w'])


    def patternChanges(self):
        """
        ~This is never used~

        calculates 
        self.iUnmatchedFrags and self.oUnmatchedFrags
        which are string fragments of 
        rawInputPattern (self.iUnmatched) that are not matched with rawOutputPattern
        rawOutputPattern (self.oUnmatched) that are not matched with rawInputPattern

        self.iUnmatched and self.oUnmatched are list of dictionary with 
        1. w = the unmatched string fragment
        2. s = start position of the unmatched string
        3. e = end position of the unmatched string

        Both lists are sorted by start position
        """
        # self.iMatchedFrags, self.oMatchedFrags = LongestCommonSubsequence.lcss(self.rawInputPattern, self.rawOutputPattern) # if put raw pattern, the $ number might confuse lcss, when there is same number as a pattern like (- $0 0)
        self.iMatchedFrags, self.oMatchedFrags, self.iUnmatchedFrags, self.oUnmatchedFrags, self.rejoinedIFrags, self.rejoinedOFrags = LongestCommonSubsequence.lcssWithUnmatchedRejoined(self.inputPattern, self.outputPattern)




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
            #beginPos = (   ALWAYS
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
                return matchingBrackets[beginPos]
        patternSegmentedByDollar = pattern.split('$')
        # if len(patternSegmentedByDollar) == 1: # there are no $ in pattern <==> no variables in pattern
        # is this pattern possible: '$0 $1'?
        # if so, then it can only match scheme strings with 2-variables?
        firstPre = patternSegmentedByDollar[0]
        # if len(firstPre) == 0: # before $, the pattern has nothing
        #     #scheme-styled-str either begins with a ( or it is a variable/number
        #     if schemeword.startswith('('): # prefix is everything up to and include the space
        #         firstPre = schemeword[:schemeword.index(' ')+1]
        #     else: # scheme-string is a variable/number ONLY, scheme-string cannot have 2 or more variables ONLY (without open-brackets)
        #         firstPre = schemeword
        # firstSuf = patternSegmentedByDollar[1]
        # import pdb;pdb.set_trace()
        ###########
        # print('schemeword', schemeword)
        # print('pattern', pattern)
        # print('firstPre', firstPre)
        ###########
        for sPos in rs.lazyPrefixFinder(firstPre, schemeword):
            dollarPoss = []
            start = sPos
            suf = pattern # for the case when there are no variables in pattern
            for i in range(0, len(patternSegmentedByDollar) -1):
                pre = patternSegmentedByDollar[i]
                # if len(pre) == 0: # before $, the pattern has nothing
                #     #scheme-styled-str either begins with a ( or it is a variable/number
                #     if schemeword.startswith('('): # has some function
                #         if i == 0:
                #             # prefix is everything up to and include the space
                #             pre = schemeword[:schemeword.index(' ')+1]
                #         else:
                #             pre = ' '
                #     else: # scheme-string is a variable/number ONLY, scheme-string cannot have 2 or more variables ONLY (without open-brackets)
                #         pre = schemeword
                suf = patternSegmentedByDollar[i+1]
                # if len(suf) == 0: # after $ there was nothing
                #     #either pattern='....$' (before $, there are any other chars) or pattern='$$$$' (many $ all packed together, no space.)
                #     #if pattern='$$$$', then originalPattern='$0$1$2$3', all packed together
                #     #this means that user expect no space between variables
                #     #this is against the definition of scheme-styled variables.
                #     #thus the only possible pattern here is '....$'
                #     #
                #     if schemeword.startswith('('): # has some function
                #         if i == len(patternSegmentedByDollar) - 1:
                #             suf = ')' # last char of the schemeword, we expect )
                #         else:
                #             suf = ' ' # there are other variables after this, we expect ' '
                #     else: # has no function
                #         suf = ''
                # import pdb;pdb.set_trace()
                #########
                # print('pre|', pre, '|suf|', suf, '|start+len(pre)|', start+len(pre), '|schemeword[start+len(pre)]|', schemeword[start+len(pre)])
                # print('len(schemeword) < (start+len(pre))', len(schemeword) < (start+len(pre)))
                # import pdb;pdb.set_trace()
                # print("schemeword[start+len(pre)] == '('", schemeword[start+len(pre)] == '(')
                #########
                if (start+len(pre)) < len(schemeword) and schemeword[start+len(pre)] == '(':
                    ##########
                    # print('0!', i, start, pre)
                    ##########
                    #
                    nextPos = getNextBalancedPos(start+len(pre)) + 1 # return None if cannot find
                    ##########
                    # print('0!nextPos', nextPos, i, start, pre)
                    ##########
                    #next nextPos must match suf TODO
                    # if 
                else:#variable, find next place that starts with suf
                    ##########
                    # print('1!', i, start, pre)

                    ##########
                    #get longest string from (start+len(pre)), that does not contain round_brackets nor spaces...
                    try:
                        subStart = start+len(pre)
                        subEnd = schemeword[start+len(pre):].index(suf) + (start+len(pre))
                        for j in range(subStart, subEnd+1):
                            if (schemeword[j].isspace()) or (schemeword[j] in ['(', ')']):
                                nextPos = j
                                break
                        if nextPos == subStart:
                            nextPos = None # empty string
                        # else:#next nextPos must match suf TODO

                    ##########
                        # print('1!nextPos', nextPos, i, start, pre)

                    ##########
                    except:
                        nextPos = None
                    # try:
                    #     nextPos = schemeword[start+len(pre):].index(suf) + (start+len(pre))
                    # except:
                    #     nextPos = None
                if nextPos is None: # cannot continue with this sPos
                    break # try the next sPos
                else:
                    dollarPoss.append((start+len(pre)+chopped, nextPos+chopped))
                    start = nextPos
            #here we need to match the suf, the last thing
            if len(dollarPoss) > 0:
                schemewordSufStart = dollarPoss[-1][1]-chopped # -chopped because we don't have the complete schemeword
                schemewordSufEnd = len(schemeword) # otherwise we could have +chopped here
                schemewordSuf = schemeword[schemewordSufStart:schemewordSufEnd]
                # print('!0!', schemewordSuf, schemewordSufStart, schemewordSufEnd)
                # print('!0!', dollarPoss)
                # import pdb;pdb.set_trace()
                schemewordSufToMatch = schemewordSuf[:len(suf)]
            else:
                schemewordSufToMatch = suf
            # print(schemewordSufToMatch, '<<schemewordSufToMatch', suf)
            if schemewordSufToMatch == suf and len(dollarPoss) == len(patternSegmentedByDollar) - 1: # we got all the dollarPoss
                # import pdb;pdb.set_trace()
                ######
                # print('returning: ', (sPos+chopped, start+len(suf)+chopped, dollarPoss), '*****')
                ######
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
        import copy
        # if pattern contains only variables and spaces
        if not any(map(lambda p: len(p.strip())>0, pattern.split('$'))):
            #TODO refactor to its own function, but must be called here, because there is still going to be bracket-leveling, which is handled by findAll
            self.patternOnlyVariablesAndSpaces = True
            numberOfVariables = pattern.count('$')
            answers = [] # tuples (startPos, endPos, listOfDollarPoss)
            if schemeword.startswith('('):
                dollarPoss = []
                #do bracket-matching
                openBracketPosStack = [0]
                for i in range(1, len(schemeword)):
                    c = schemeword[i]
                    if c == '(':
                        openBracketPosStack.append(i)
                    elif c == ')':
                        matchingOpenBracketPos = openBracketPosStack.pop()
                        if len(openBracketPosStack) == 1: #we are on direct child level of root bracket
                            dollarPoss.append((matchingOpenBracketPos, i+1)) # inclusive of closeBracket
                if len(dollarPoss) == 0: # schemeword has no inner brackets
                    #variables are delimited by space only.
                    #but we have to take care to remove the opening/closing brackets
                    variables = list(filter(lambda x: len(x)>0, schemeword[1:-1].split(' ')))[1:] # [1:] to remove the functionName
                    vIdx = 0
                    sPos = 0
                    ts = copy.deepcopy(schemeword)
                    chopped = 0
                    while vIdx < len(variables):
                        sPos = ts.index(variables[vIdx])
                        ePos = sPos + len(variables[vIdx])
                        vIdx += 1
                        dollarPoss.append((sPos+chopped, ePos+chopped))
                        ts = ts[ePos:]
                        chopped += ePos

                startPos = len(schemeword)
                endPos = 0
                #find startPos and endPos
                for s, e in dollarPoss:
                    startPos = min(startPos, s)
                    endPos = max(endPos, e)

                answers = [(startPos, endPos, dollarPoss)]
            else: #the whole schemeword is a variable/number
                if numberOfVariables == 1: #there is a match
                    answers = [(0, len(schemeword), [])] # should not consider itself as an argument
        else:# a pattern with other characters than variables and spaces
            self.patternOnlyVariablesAndSpaces = False
            answers = []
            tup = self.findFirstSameLevel(pattern, schemeword)
            chopped = 0
            while tup is not None:
                # import pdb;pdb.set_trace()
                answers.append(tup)
                chopped = tup[1]
                tup = self.findFirstSameLevel(pattern, schemeword[tup[1]:], chopped)

        # print(schemeword)
        # print(answers)
        # import pdb;pdb.set_trace()
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
            # print(stack, '<<<stack')
            # import pdb;pdb.set_trace()
                
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
        sortKey = 's' # 'cms'
        for idx, data in id__data.items():
            if data['pid'] is not None:
                childIds = enclosureTree.get(data['pid'], [])
                if len(childIds) == 0:
                    childIds.append(data['id'])
                else:
                    startPoss = list(map(lambda idd: id__data[idd][sortKey], childIds))
                    mycms = id__data[data['id']][sortKey]
                    #
                    # if data['pid'] == 1:
                    #     print('~~~~')
                    #     print('mycms', mycms)
                    #     print(startPoss)
                    #     print('~~~~')
                    #
                    positionToInsert = bisect.bisect_left(startPoss, mycms)
                    childIds.insert(positionToInsert, data['id'])
                enclosureTree[data['pid']] = childIds
        # print(id__data)
        # print(enclosureTree)
        # import pdb;pdb.set_trace()
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
        import bisect # TODO repeated imports REFACTOR?
        variables = []
        # rawVariablesPosList = []
        variablesAndPos = []
        for m in re.finditer('(\$\d+)', rawPattern):
            #rawVariablesPosList.append((m.start(), m.end(), m.group()))
            # variables.append(m.group())
            t = (m.group(), m.start())
            posToInsert = bisect.bisect_left(variablesAndPos, t[1], key=lambda x: x[1])
            variablesAndPos.insert(posToInsert, t)
        variables = list(map(lambda t: t[0], variablesAndPos))
        # import pdb;pdb.set_trace()
        pattern = re.sub(r'\$\d+', '$', rawPattern) # remove the numbers
        variablesPosSansVarnumList = []
        for m in re.finditer('(\$)', pattern):
            variablesPosSansVarnumList.append(m.start())
        #rawVariables__variables = dict(zip(rawVariablesPosList, variablesPosList)) # attach to self, if we need this
        #variables__rawVariables = dict(zip(variablesPosList, rawVariablesPosList)) # attach to self, if we need this
        
        return pattern, variables, variablesAndPos, variablesPosSansVarnumList


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
        relativeShifts = {}
        nonVariableChanges = {}
        #key: nodeId
        #contains list(tuple):(after_this_pos, how_much_offset_to_ad), NOTE: ONLY works for INPUT PATTERN!
        rootNonMatches_childId__listOfTupStartPosOffset_i = {}
        # rootNonMatches_startPos__offset = [] #contains tuple:(after_this_pos, how_much_offset_to_add), NOTE: ONLY works for INPUT PATTERN!
        #key: nodeId
        #contains list(tuple):(after_this_pos, how_much_offset_to_ad), NOTE: ONLY works for OUTPUT PATTERN!
        rootNonMatches_childId__listOfTupStartPosOffset = {} 
        #
        nodeId__variables__valuesPos = {} # dict of dict, for computation of rootNonMatches_childId__listOfTupStartPosOffset, actually we only need this info, whose direct_parent is a direct_child of the root. TODO further, SPACE-OPTIMISATION
        verPosWord = []
        import copy
        def _recursiveManipulate(nodeId):
            # BaseCase
            if nodeId not in enclosureTree: # its a leaf
                return id__data[nodeId]['w'], id__data[nodeId]['s']
            # RecursiveCase
            replaceStrsPos = [] # _recursiveManipulate need to return the startPos of replaceStr too.
            replaceStrs = []
            childIds = enclosureTree[nodeId]
            for childId in childIds: 
                data = id__data[childId]
                replaceStr, startPos = _recursiveManipulate(data['id'])
                replaceStrs.append(replaceStr)
                replaceStrsPos.append((replaceStr, startPos))
            if id__data[nodeId]['pid'] is None:#it was not matched to any variables, or inputPattern has no variables :), according to def findAll, this is the root, starting Node
                rWord = copy.deepcopy(oWord)
                if self.recordMaking and len(nodeId__variables__valuesPos) > 0: # for totally no matches: len(nodeId__variables__valuesPos) > 0
                    #find the nonVariable changes FOR INPUT PATTERN
                    accumulatedOffset = 0 #this is the end of the first unmatched frag from pos:0
                    for childId in childIds:
                        #
                        rootNonMatches_childId__listOfTupStartPosOffset_i[childId] = []
                        #
                        accumulatedOffset += id__data[childId]['s'] # this is the pre-unmatched(inputPattern)
                        if len(self.inVariablesPosSansVarnumList) > 0: #inputPattern has variables... need the variableToReplaceStr mapping... from grandChild
                            #add the pre-non-variable(inputPattern) of the first inVariable. -> accumulatedOffset
                            # if we store every $varToReplacementStr, at everyNode, in a MAP, then this will not be such a big problem.
                            # import pdb;pdb.set_trace()
                            var__valuesPosSansVarnum = nodeId__variables__valuesPos[childId] # should be available since we do bottoms up (recursion)
                            for listIdx, (var, pos) in enumerate(self.inVariablesAndPos):

                                replaceStr, _ = var__valuesPosSansVarnum[self.inVariablesAndPos[listIdx][0]]

                                #add te pre-non-variable(inputPattern) of this inVariable. -> accumulatedOffset
                                posSansVarnum = self.inVariablesPosSansVarnumList[listIdx]
                                if listIdx > 0:
                                    startPosOnPattern = self.inVariablesPosSansVarnumList[listIdx - 1]
                                else:
                                    startPosOnPattern = 0

                                preNonVariableOfInputPattern = self.inputPattern[startPosOnPattern:posSansVarnum]
                                # - max(0, listIdx - 1) number of variables before this 
                                rootNonMatches_childId__listOfTupStartPosOffset_i[childId].append((startPosOnPattern, accumulatedOffset - max(0, listIdx - 1))) # seems like the offset positions always over by 1... WHY?
                                #remember to subtract the total number of $ = listIdx
                                accumulatedOffset += len(replaceStr) + len(preNonVariableOfInputPattern)
                        else: # inputPattern has no variables, there should be only 1 match for each childId, and its replaceStr=id__data['childId']['w']
                            rootNonMatches_childId__listOfTupStartPosOffset_i[childId].append((id__data['childId']['s'], accumulatedOffset))
                            accumulatedOffset += len(id__data['childId']['w'])
                    #
                    if len(self.inVariablesPosSansVarnumList) > 0:
                        startPosOnPattern = self.inVariablesPosSansVarnumList[listIdx]
                        replaceStr, _ = var__valuesPosSansVarnum[self.inVariablesAndPos[listIdx-1][0]] # value == replaceStr
                        rootNonMatches_childId__listOfTupStartPosOffset_i[childId].append((startPosOnPattern, accumulatedOffset - max(0, listIdx)))
                    # else: # what about for no variables

                    #find the nonVariable changes FOR OUTPUT PATTERN
                    accumulatedOffset = 0# this is the end of the first unmatched frag from pos:0
                    for childId in childIds:
                        #
                        rootNonMatches_childId__listOfTupStartPosOffset[childId] = []
                        #
                        accumulatedOffset += id__data[childId]['s'] # this is the pre-unmatched(outputPattern)
                        if len(self.outVariablesPosSansVarnumList) > 0: #outputPattern has variables... need the variableToReplaceStr mapping... from grandChild
                            #add the pre-non-variable(outputPattern) of the first outVariable. -> accumulatedOffset
                            # if we store every $varToReplacementStr, at everyNode, in a MAP, then this will not be such a big problem.
                            var__valuesPosSansVarnum = nodeId__variables__valuesPos[childId] # should be available since we do bottoms up (recursion)
                            #
                            # print(nodeId__variables__valuesPos)
                            # import pdb;pdb.set_trace()
                            #
                            for listIdx, (var, pos) in enumerate(self.outVariablesAndPos):
                                replaceStr, _ = var__valuesPosSansVarnum[self.outVariablesAndPos[listIdx][0]]
                                #minusVarLen = 1


                                #add the pre-non-variable(outputPattern) of this outVariable. -> accumulatedOffset
                                posSansVarnum = self.outVariablesPosSansVarnumList[listIdx]
                                if listIdx > 0:
                                    startPosOnPattern = self.outVariablesPosSansVarnumList[listIdx - 1]
                                else:
                                    startPosOnPattern = 0
                                
                                preNonVariableOfOutputPattern = self.outputPattern[startPosOnPattern:posSansVarnum]
                                # replaceStr, _ = var__valuesPosSansVarnum[var] # value == replaceStr
                                #appendedTup[0] is the startPos on the self.outputPattern
                                rootNonMatches_childId__listOfTupStartPosOffset[childId].append((startPosOnPattern,accumulatedOffset - max(0, listIdx - 1))) # seems like the offset positions always over by 1... WHY?
                                #remember to subtract the total number of $ = listIdx
                                #
                                # print('len(preNonVariableOfOutputPattern)', len(preNonVariableOfOutputPattern), preNonVariableOfOutputPattern)
                                # print('len(replaceStr)', len(replaceStr), replaceStr)
                                # print('accumulatedOffset', accumulatedOffset)
                                # print('going to add: ', len(preNonVariableOfOutputPattern), '+', len(replaceStr), '=', len(preNonVariableOfOutputPattern) + len(replaceStr) - 1)
                                # print('^^^')
                                #
                                accumulatedOffset += len(replaceStr) + len(preNonVariableOfOutputPattern) # - minusVarLen # need to add previous replaceStr
                                #
                        else: # outputPattern has no variables, there should be only 1 match for each childId, and its replaceStr=id__data['childId']['w']
                            rootNonMatches_childId__listOfTupStartPosOffset[childId].append((id__data['childId']['s'], accumulatedOffset))
                            accumulatedOffset += len(id__data['childId']['w'])
                            # #NOTE THAT BELOW IS ALSO POSSIBLE (and totally independent of accumulatedOffset):
                            # rootNonMatches_childId__listOfTupStartPosOffset[childId].append((id__data['childId']['s'], id__data['childId']['s']))

                    #
                    if len(self.outVariablesPosSansVarnumList) > 0:
                        startPosOnPattern = self.outVariablesPosSansVarnumList[listIdx]
                        replaceStr, _ = var__valuesPosSansVarnum[self.outVariablesAndPos[listIdx-1][0]] # value == replaceStr
                        rootNonMatches_childId__listOfTupStartPosOffset[childId].append((startPosOnPattern, accumulatedOffset - max(0, listIdx)))
                    # else: # what about for no variables

                # print('listIdx', listIdx, self.outVariablesAndPos)
                # print(self.outVariablesPosSansVarnumList)
                # print(startPosOnPattern)
                # print(accumulatedOffset)
                # print(rootNonMatches_childId__listOfTupStartPosOffset)
                # import pdb;pdb.set_trace()
                #

                # id__data[childIds[0]]['s'] # this is the end of the first unmatched from pos:0
                # #subsequent unmatches will be the strings between the $ in the outputPattern, plus sum(lens(replaceStr_before_this_unmatched))
                # accumulatedOffset = id__data[childIds[0]]['s']
                # for listIdx, (var, patternPos) in enumerate(self.outVariablesAndPos): # note that var, is like childId but for OUTPUTPATTERN
                #     #map var to childId to val?
                #     val, _ = variables__valuesPos[var] # val is replaceStr
                #     startPosOnOutputPattern = self.oVariablesPosSansVarnumList[listIdx]
                #     rootNonMatches_startPosOnOutputPattern__offset.append((startPosOnOutputPattern, accumulatedOffset))

                #     #
                #     endPos = self.outVariablesPosSansVarnumList[listIdx] # this gives the startPos of var(listIdx) in the outputPattern
                #     if listIdx > 0:
                #         startPos = self.outVariablesPosSansVarnumList[listIdx - 1]
                #     else:
                #         startPos = 0
                #     accumulatedOffset += len(val) + (endPos - startPos + 1) - 1#remember to subtract 1 for the $
                # rootNonMatches_startPosOnOutputPattern__offset.append((accumulatedOffset+len(val), accumulatedOffset+len(val)))
                #


                if len(variables) == 0: #no variables, then we need to replace with outputPattern instead of replaceStr
                    #but first we need to replace the variables in outputPattern first... with variable/s that in not in equation.
                    #and that is handled by Manipulate :)
                    replaceStrs = [self.subsitutedOutputGrammar] * len(replaceStrs)

                # print('no match')
                # import pdb;pdb.set_trace()
                childId__replacedStr = dict(zip(childIds, replaceStrs))
                for listIdx, childId in enumerate(reversed(childIds)): #have to replace from the back, else, the frontPositions might shift.
                    childData = id__data[childId]

                    if self.recordMaking and len(self.variables) > 0:
                        var = self.variables[len(self.variables) - listIdx -1]
                        #also need to find unmatched parts and do offseting later TODO
                        verPosWord.append({
                            't':'n', #nomatch(n)/varonly(v)/patrepl(p)
                            'd':'a', #addition(a)/removal(r)/positional_shift[edit](e)
                            'n':nodeId, #nodeId where this was done
                            's':childData['s'], #start position in original string processed, where this change was done
                            'e':childData['e'], #end position in original string processed, where this change was done
                            'w':childId__replacedStr[childId], #string involved in the change
                            'v':var, #associated variable
                        })
                        verPosWord.append({
                            't':'n', #nomatch(n)/varonly(v)/patrepl(p)
                            'd':'r', #addition(a)/removal(r)/positional_shift[edit](e)
                            'n':nodeId, #nodeId where this was done
                            's':childData['s'], #start position in original string processed, where this change was done
                            'e':childData['e'], #end position in original string processed, where this change was done
                            'w':rWord[childData['s']:childData['e']], #string involved in the change
                            'v':var, #associated variable
                        })
                    rWord = rs.replaceAtPos(rWord, childData['s'], childData['e'], childId__replacedStr[childId])
                return rWord, 0 # since the whole oWord was replaced
            else:

                #len(variables) == 1 and len(replaceStrs) == 2
                #TODO what if len(variables) == 3 and len(replaceStrs) == 4?, then findAllSameLevel found more replaceStrs, then there are unique variables
                if self.patternOnlyVariablesAndSpaces: 
                    
                    #the childId must be in multiples of len(variables)
                    #zum bespiel, variables = ['$0'], then len(childIds) must be of multiples of 1
                    #wieder bespiel, variables = ['$0', '$1', '$2'], then len(childIds) must be of multiples of 3
                    #if inputPattern='$0 $1', then only multiples of 2 will match:
                    #(= a b)
                    #with $0=a, $1=b
                    #if inputPattern='$0 $1 $2', then only multiples of 3 will match:
                    #(int a b f)   #definiteIntegral with bounds (a, b) and function continuous f
                    #with $0=a, $1=b, $2=f

                    #check that remainder is zero
                    if len(childIds)%len(variables) != 0:
                        raise Exception('number of matches(childIds) must be a multiple of number of variables')
                    # multiple = len(childIds)//len(variables)
                    #check well-defined
                    variables__valuesPos = {} # dict to check if variable has more than 1 value mapped
                    for i, childId in enumerate(childIds):
                        variableId = i % len(variables)
                        variable, pos = self.inVariablesAndPos[variableId]
                        value = replaceStrs[i]
                        existingValuePos = variables__valuesPos.get(variable, (None, None))
                        existingValue, existingPos = existingValuePos
                        if existingValue is not None and existingValue != value:
                            #more than one value was assigned to variable and those values are different
                            raise Exception(f'{existingValue} was assigned to {variable} at position {existingPos}, and now {value} is being assigned to the same {variable} again. Not well-defined')
                        variables__valuesPos[variable] = (value, pos)
                    #replace outputPattern's variables with replaceStr, using variables__valuesPos
                    ############
                    # import pdb;pdb.set_trace()
                    ############
                    currentVariablesToReplacement = dict(map(lambda t: (t[0], t[1][0]), variables__valuesPos.items())) # extract variables__replacementStr from variables__valuesPos
                    currentVariablesToReplacement.update(self.additionalReplacementStrForVariablesDict)
                    op = copy.deepcopy(outputPattern)
                    # for variable in variables:
                    #     # op = op.replace(variable, variables__valuesPos[variable][0])
                    for variable, replaceStr in currentVariablesToReplacement.items():
                        op = op.replace(variable, replaceStr)
                    #replace the child in template with op (in reverse, since might affect the earlier character positions)
                    #then the 'w' becomes the template, and the variables are the replaceStr, and replaceStr are (outputPattern with 'ogVariable' replaced)
                    template = copy.deepcopy(id__data[nodeId]['w'])
                    parentStartOffset = id__data[nodeId]['s']
                    nodeId__variables__valuesPos[nodeId] = {}
                    for listIdx, childId in enumerate(reversed(childIds)):
                        data = id__data[childId]
                        # import pdb;pdb.set_trace()
                        #make a record to return
                        # verPosWord.append({
                        #     's':data['s']- parentStartOffset, # start position of the removed word
                        #     'e':data['e']- parentStartOffset, # 
                        #     'o':template[data['s']- parentStartOffset: data['e']- parentStartOffset], # removed word
                        #     'i':op,
                        #     'nodeId':nodeId
                        # })
                        # print(self.inVariablesPosSansVarnumList)
                        # print()
                        # import pdb;pdb.set_trace()
                        posOnInputPattern = self.inVariablesPosSansVarnumList[len(self.variables) - listIdx -1]
                        var = self.variables[len(self.variables) - listIdx -1]
                        if self.recordMaking:
                            verPosWord.append({
                                't':'v', #nomatch(n)/varonly(v)/patrepl(p)
                                'd':'a', #addition(a)/removal(r)/positional_shift[edit](e)
                                'n':nodeId, #nodeId where this was done
                                's':data['s'] - parentStartOffset, #start position in original string processed, where this change was done
                                'e':data['e'] - parentStartOffset, #end position in original string processed, where this change was done
                                'w':op, #string involved in the change
                                'v':var, #associated variable
                            })
                            verPosWord.append({
                                't':'v', #nomatch(n)/varonly(v)/patrepl(p)
                                'd':'r', #addition(a)/removal(r)/positional_shift[edit](e)
                                'n':nodeId, #nodeId where this was done
                                's':data['s'] - parentStartOffset, #start position in original string processed, where this change was done
                                'e':data['e'] - parentStartOffset, #end position in original string processed, where this change was done
                                'w':template[data['s']- parentStartOffset: data['e']- parentStartOffset], #string involved in the change
                                'v':var, #associated variable
                            })
                        nodeId__variables__valuesPos[nodeId][var] = (op, posOnInputPattern)
                        #
                        # print(nodeId__variables__valuesPos)
                        # import pdb;pdb.set_trace()
                        #
                        template = rs.replaceAtPos(template, data['s']- parentStartOffset, data['e']- parentStartOffset, op)
                    return template, parentStartOffset # = id__data[nodeId]['s']
                else:
                    ##################check if there is a match to all variables TODO REFACTOR_SAME(1)
                    variables__valuesPos = {} # dict to check if variable has more than 1 value mapped
                    variables__valuesPosNoVarnum = {}
                    #check if same variable has been mapped to more than 1 value <<< this is not well-defined
                    for varIdx in range(0, len(self.variables)):
                        #very convienent that replaceStrs(values) and self.variables are already aligned in list order :)
                        variable, pos = self.inVariablesAndPos[varIdx] #TODO can be refactored to self.inVariablesPosSansVarnumList
                        value = replaceStrs[varIdx]
                        #
                        posSansVarnum = self.inVariablesPosSansVarnumList[varIdx]
                        variables__valuesPosNoVarnum[variable] = (value, posSansVarnum)
                        #
                        existingValuePos = variables__valuesPos.get(variable, (None, None))
                        existingValue, existingPos = existingValuePos
                        if existingValue is not None and existingValue != value: 
                            #more than one value was assigned to variable and those values are different
                            raise Exception(f'{existingValue} was assigned to {variable} at position {existingPos}, and now {value} is being assigned to the same {variable} again. Not well-defined')
                        variables__valuesPos[variable] = (value, pos)
                    ##################

                    nodeId__variables__valuesPos[nodeId] = variables__valuesPosNoVarnum
                    #
                    # print(nodeId__variables__valuesPos)
                    # import pdb;pdb.set_trace()
                    #
                    if nodeId in nodeIdsToSkip:
                        op = copy.deepcopy(inputPattern)
                        currentVariablesToReplacement = dict(zip(variables, replaceStrs))
                        currentVariablesToReplacement.update(self.additionalReplacementStrForVariablesDict)
                        # print('skippp', nodeId, op)
                        #actually no change here... no need to replace, can just return... lol you waste computation
                        #TODO optimise
                    else:
                        op = copy.deepcopy(outputPattern)
                        currentVariablesToReplacement = dict(zip(variables, replaceStrs))
                        currentVariablesToReplacement.update(self.additionalReplacementStrForVariablesDict)
                        # print('NO skippp', nodeId, op)

                        if self.recordMaking:
                            #changes in variables from input to output, TODO
                            # self.inVariablesAndPos
                            # self.outVariablesAndPos
                            #1. variables from output might appear more than it appear in output than input
                            #2. variables from output might appear less than it appear in output than input
                            #3. variables from input might appear more than it appear in input than output
                            #4. variables from input might appear less than it appear in input than output
                            #5. self.oUnmatchedFrags - added (static)
                            #6. self.iUnmatchedFrags - removed (static)
                            iVars__count = {}
                            for var, pos in self.inVariablesAndPos:
                                iVars__count[var] = iVars__count.get(var, 0) + 1
                            oVars__count = {}
                            for var, pos in self.outVariablesAndPos:
                                oVars__count[var] = oVars__count.get(var, 0) + 1
                            allUniqueVars = set(map(lambda t: t[0], self.inVariablesAndPos)).union(map(lambda t: t[0], self.outVariablesAndPos))

                            #for iCount == oCount
                            #precalculate the mapping for amount of change in position for each var that was only transposed
                            #amount of character shifted
                            subtractVarIdxLenAccumulator = 0
                            iVarPosIdxInOGSansVarNumList = []
                            for idx, (varStr, patternPos) in enumerate(self.inVariablesAndPos):
                                iVarPosIdxInOGSansVarNumList.append((varStr, patternPos - subtractVarIdxLenAccumulator, idx))
                                varIdStr = rs.getMatchesOrNone('\$(\d+)', varStr)[0]
                                subtractVarIdxLenAccumulator += len(varIdStr)
                            subtractVarIdxLenAccumulator = 0
                            oVarPosIdxInOGSansVarNumList = []
                            for idx, (varStr, patternPos) in enumerate(self.outVariablesAndPos):
                                oVarPosIdxInOGSansVarNumList.append((varStr, patternPos - subtractVarIdxLenAccumulator, idx))
                                varIdStr = rs.getMatchesOrNone('\$(\d+)', varStr)[0]
                                subtractVarIdxLenAccumulator += len(varIdStr)
                            iVar__posIdxInOGList = {}
                            for var0, pos, idx in iVarPosIdxInOGSansVarNumList:
                                iVar__posIdxInOGList[var0] = (pos, idx)
                            oVar__posIdxInOGList = {}
                            for var0, pos, idx in oVarPosIdxInOGSansVarNumList:
                                oVar__posIdxInOGList[var0] = (pos, idx)
                            var__oPositionMinusIPosition = {}
                            for var0 in allUniqueVars:
                                if iVars__count.get(var0, 0) == oVars__count.get(var0, 0):
                                    #
                                    # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                                    # print(var0, currentVariablesToReplacement[var0])
                                    # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                                    #
                                    iPatternPos, iOGListIdx = iVar__posIdxInOGList[var0]
                                    oPatternPos, oOGListIdx = oVar__posIdxInOGList[var0]
                                    #also need to add the 1.preNonVariables, 2. at each var
                                    totalLenBeforeVar0InRIPattern = 0 
                                    if len(iVarPosIdxInOGSansVarNumList) > 0 and len(iVarPosIdxInOGSansVarNumList[:iOGListIdx]) == 0: # we still need to add preNonVariable
                                        totalLenBeforeVar0InRIPattern = len(self.inputPattern[0:iVarPosIdxInOGSansVarNumList[0][1]])
                                    prevIPatternStartPos = 0
                                    # print('iTotal before loop', totalLenBeforeVar0InRIPattern)
                                    for iVar, iPrevPos, iidx in iVarPosIdxInOGSansVarNumList[:iOGListIdx]: # vars before var0 in iPattern
                                        iNextPos = iPrevPos
                                        if iidx + 1 <= len(iVarPosIdxInOGSansVarNumList[:iOGListIdx]):
                                            _, iNextPos, _ = iVarPosIdxInOGSansVarNumList[iidx+1]
                                        # import pdb;pdb.set_trace()
                                        # if iidx > 0:
                                        #     prevVar = iVarPosIdxInOGSansVarNumList[iidx-1][0]
                                        #     replacedStr = currentVariablesToReplacement[prevVar]
                                        # else:
                                        #     replacedStr = ''
                                        replacedStr = currentVariablesToReplacement[iVar]
                                        if iidx > 0:
                                            preNonVariable = self.inputPattern[prevIPatternStartPos+1:iPrevPos] # get rid of the $
                                        else:
                                            preNonVariable = self.inputPattern[prevIPatternStartPos:iPrevPos]
                                        prevIPatternStartPos = iPrevPos
                                        # if iidx > 0: # for the second var onwards
                                        #     prevIPatternStartPos += 1 # we need to add 1 to pos to get rid of the $ from the prev Var

                                        # -1 for the $ on the prev # amount of space, from nextStart to prevEnd in pattern(not realised pattern!)
                                        # print('iTotal before', totalLenBeforeVar0InRIPattern)
                                        totalLenBeforeVar0InRIPattern +=  len(preNonVariable) + len(replacedStr)# len(currentVariablesToReplacement[iVar]) + (iNextPos - iPrevPos -1) 
                                        #
                                        # print('in iloop')
                                        # print(iVar)
                                        # print('replacedStr', replacedStr, 'len', len(replacedStr))
                                        # print('preNonVariable', preNonVariable, 'len', len(preNonVariable))
                                        # print('iTotal', totalLenBeforeVar0InRIPattern)
                                        # import pdb;pdb.set_trace()
                                    #need to add current preNonVariable
                                    if len(iVarPosIdxInOGSansVarNumList[:iOGListIdx]) > 0: #last preNonVariable
                                        iPrevPos = iVarPosIdxInOGSansVarNumList[iOGListIdx][1]
                                        # print(prevIPatternStartPos, iPrevPos, 'adding at last to input: ', self.inputPattern[prevIPatternStartPos+1:iPrevPos], len(self.inputPattern[prevIPatternStartPos+1:iPrevPos]))
                                        totalLenBeforeVar0InRIPattern += len(self.inputPattern[prevIPatternStartPos+1:iPrevPos])
                                    
                                    totalLenBeforeVar0InROPattern = 0
                                    if len(oVarPosIdxInOGSansVarNumList) > 0 and len(oVarPosIdxInOGSansVarNumList[:oOGListIdx]) == 0: # we still need to add preNonVariable
                                        totalLenBeforeVar0InROPattern = len(self.outputPattern[0:oVarPosIdxInOGSansVarNumList[0][1]])
                                    prevOPatternStartPos = 0
                                    # print('oTotal before', totalLenBeforeVar0InROPattern)
                                    for oVar, oPrevPos, oidx in oVarPosIdxInOGSansVarNumList[:oOGListIdx]: # vars before var0 in oPattern
                                        oNextPos = oPrevPos
                                        if oidx + 1 <= len(oVarPosIdxInOGSansVarNumList[:oOGListIdx]):
                                            _, oNextPos, _ = oVarPosIdxInOGSansVarNumList[oidx+1]

                                        # if oidx > 0:
                                        #     prevVar = oVarPosIdxInOGSansVarNumList[iidx-1][0]
                                        #     replacedStr = currentVariablesToReplacement[prevVar]
                                        # else:
                                        #     replacedStr = ''
                                        replacedStr = currentVariablesToReplacement[oVar]
                                        if oidx > 0:
                                            preNonVariable = self.outputPattern[prevOPatternStartPos+1:oPrevPos]
                                        else:
                                            preNonVariable = self.outputPattern[prevOPatternStartPos:oPrevPos]
                                        # preNonVariable = self.outputPattern[prevOPatternStartPos+1:oPrevPos]
                                        prevOPatternStartPos = oPrevPos
                                        # if oidx > 0: # for the second var onwards
                                        #     prevOPatternStartPos += 1 # we need to add 1 to pos to get rid of the $ from the prev Var

                                        #
                                        # -1 for the $ on the prev # amount of space, from nextStart to prevEnd in pattern(not realised pattern!)
                                        totalLenBeforeVar0InROPattern +=  len(preNonVariable) + len(replacedStr)# len(currentVariablesToReplacement[oVar]) + (oNextPos - oPrevPos -1) 
                                        # print('in oloop')
                                        # print(oVar)
                                        # print('replacedStr', replacedStr, 'len', len(replacedStr))
                                        # print('preNonVariable', preNonVariable, 'len', len(preNonVariable))
                                        # print('oTotal', totalLenBeforeVar0InROPattern)
                                        # import pdb;pdb.set_trace()
                                    #need to add current preNonVariable
                                    if len(oVarPosIdxInOGSansVarNumList[:oOGListIdx]) > 0: #last preNonVariable
                                        oPrevPos = oVarPosIdxInOGSansVarNumList[oOGListIdx][1]
                                        # print(prevOPatternStartPos,oPrevPos, 'adding at last to output: ', self.outputPattern[prevOPatternStartPos+1:oPrevPos], len(self.outputPattern[prevOPatternStartPos+1:oPrevPos]))
                                        totalLenBeforeVar0InROPattern += len(self.outputPattern[prevOPatternStartPos+1:oPrevPos])

                                    var__oPositionMinusIPosition[var0] = totalLenBeforeVar0InROPattern - totalLenBeforeVar0InRIPattern
                                    ###
                                    # print('^^^')
                                    # print(var0)
                                    # print(currentVariablesToReplacement[var0])
                                    # print(totalLenBeforeVar0InRIPattern)
                                    # print(totalLenBeforeVar0InROPattern)
                                    # print('change:', var__oPositionMinusIPosition[var0])
                                    # print('^^^')
                                    # print('variables', variables)
                                    # print('self.outVariables', self.outVariables)
                                    # print('childIds', childIds)
                                    ###
                                    # var__oPositionMinusIPosition[var0] = totalLenBeforeVar0InRIPattern - totalLenBeforeVar0InROPattern
                                    # import pdb;pdb.set_trace()
                            currentVariablesToChildIds = dict(zip(variables, childIds))
                            # currentVariablesToChildIds = dict(zip(self.outVariables, childIds))
                            ###
                            # print('currentVariablesToChildIds', currentVariablesToChildIds)
                            # print('var__oPositionMinusIPosition')
                            # print(var__oPositionMinusIPosition)
                            ###


                            # for iCount <> oCount.
                            iVarPosIdxInOGList = [(t[0], t[1], idx) for idx, t in enumerate(self.inVariablesAndPos)] # t[0] is $102, t[1] is pos
                            oVarPosIdxInOGList = [(t[0], t[1], idx) for idx, t in enumerate(self.outVariablesAndPos)]



                            for var in allUniqueVars:
                                iCount = iVars__count.get(var, 0)
                                oCount = oVars__count.get(var, 0)
                                if iCount > oCount: # removed
                                    #need to add a row in verPosWord for each (iCount - oCount)
                                    #take out the first (iCount - oCount) of var from self.inVariablesAndPos, we just take in ascending order of Pos
                                    varWithPosAndIdx = list(filter(lambda t: t[0]==var, iVarPosIdxInOGList))[:(iCount - oCount)]
                                    # replaceStrsPos
                                    for v, pos, idxInOGList in varWithPosAndIdx: #note that v==var (since we filtered for var)
                                        #replaceStrsPos is aligned with inVariablesAndPos 
                                        replaceStr, startPosInOriginalWord = replaceStrsPos[idxInOGList]
                                        verPosWord.append({
                                            't':'p', #nomatch(n)/varonly(v)/patrepl(p)
                                            'd':'r', #addition(a)/removal(r)/positional_shift[edit](e)
                                            'n':nodeId, #nodeId where this was done
                                            #removed from old String
                                            's':startPosInOriginalWord, #start position in original string processed, where this change was done
                                            'e':startPosInOriginalWord+len(replaceStr), #end position in original string processed, where this change was done
                                            'w':replaceStr, #string involved in the change
                                            'v':var, #associated variable
                                        })
                                elif iCount < oCount: # added
                                    #additions positions only make sense in the outputStr, since additions might not even inputPattern...
                                    #need to add a row in verPosWord for each (oCount - iCount)
                                    #take out the first (oCount - iCount) of var from self.outVariablesAndPos, we just take in ascending order of Pos
                                    varWithPosAndIdx = list(filter(lambda t: t[0]==var, oVarPosIdxInOGList))[:(oCount - iCount)]
                                    for v, pos, idxInOGList in varWithPosAndIdx: #note that v==var (since we filtered for var)
                                        #replaceStrsPos is not aligned with outVariables...
                                        value, _ = variables__valuesPos[v]
                                        verPosWord.append({
                                            't':'p', #nomatch(n)/varonly(v)/patrepl(p)
                                            'd':'a', #addition(a)/removal(r)/positional_shift[edit](e)
                                            'n':nodeId, #nodeId where this was done
                                            #added to new String TODO can we make this to absolute position
                                            's':pos, #relative( to outPattern) start position in new string processed, where this change was done
                                            'e':pos+len(replaceStr), #relative( to outPattern) end position in new string processed, where this change was done
                                            'w':value, #string involved in the change
                                            'v':var, #associated variable
                                        })
                                else: # what if there is only a positional shift, but no change in number of variables between inVariables and outVariables

                                    # print('IIIIIII AMMMMMMM HEREEREREREEEE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', iCount, oCount)
                                    #then there will be difference in order between iVarPosIdxInOGList and [('$1', 3, 0), ('$0', 6, 1)]
                                    # oVarPos__idxInOGList = {}
                                    # for var, pos, idx in self.oVarPosIdxInOGList:
                                    #     oVarPos__idxInOGList[(var, pos)] = idx
                                    #match and find positional differences
                                    varWithPosAndIdx = list(filter(lambda t: t[0]==var, oVarPosIdxInOGList))
                                    #need to subtract sum of len of numberId(v) of all the v before var (to get absolute position)
                                    for oVar, oPos, oIdx in varWithPosAndIdx:
                                        # print('~0')
                                        iPos, iIdx = iVar__posIdxInOGList[oVar]
                                        # print('~1', 'posDiff:', oPos, iPos, 'idxDiff:', oIdx, iIdx)
                                        # if oIdx != iIdx: # position was shifted..., TODO but this is only in the variablelist. if position of variable was shifted in the actual, but not in variable list, this will not be detected.
                                        if oPos != iPos:
                                            # print('~2')
                                            #replaceStrsPos is aligned with inVariablesAndPos 
                                            # replaceStr, startPosInOriginalWord = replaceStrsPos[oIdx] # comes from input
                                            # print('~3')
                                            # replacedStr, _ = replaceStrsPos[iidx]
                                            replacedStr = currentVariablesToReplacement[oVar] # should be the same as currentVariablesToReplacement[iVar]

                                            # import pdb;pdb.set_trace()
                                            # verPosWord.append({
                                            #     't':'p', #nomatch(n)/varonly(v)/patrepl(p)
                                            #     'd':'e', #addition(a)/removal(r)/positional_shift[edit](e)
                                            #     'n':nodeId, #nodeId where this was done
                                            #     #NOT THE RIGHT LABELs....TODO do something about it?
                                            #     's':startPosInOriginalWord, #start position in original string processed, where this change was done
                                            #     #'e' need to subtract sum of len(arg) before this in the outPattern
                                            #     #original + positionalChangeWithinSubString + (sumOfParentsChangesInPosition)
                                            #     #TODO cannot be done in recursion... because the parent's changes are not computed yet, have to DFS enclosureTree, after recursion
                                            #     'e':startPosInOriginalWord + var__oPositionMinusIPosition[oVar], #end position in original string processed, where this change was done

                                            #     'w':replaceStr, #string involved in the change
                                            #     'v':var, #associated variable
                                            # })
                                            # import pdb;pdb.set_trace()
                                            associatedChildId = currentVariablesToChildIds[var]
                                            # print('~4')
                                            relativeShifts[associatedChildId] = {
                                            #relativeShifts[(nodeId, var)] = { # nodeId is parentId, 
                                                'change': var__oPositionMinusIPosition[oVar],
                                                'replaceStr':replacedStr,
                                                'var':var
                                            }
                                            # print('~5')
                                            # print(currentVariablesToChildIds)
                                            # print(var)
                                            # print(oVar)
                                            # print(var, associatedChildId, replaceStr, var__oPositionMinusIPosition[oVar])
                                            # print('associatedChildId')
                                            # print(associatedChildId)
                                            # print('replaceStr')
                                            # print(replaceStr)
                                            # print('replaceStrsPos')
                                            # print(replaceStrsPos)
                                            # print('appended:')
                                            # print({
                                            # #relativeShifts[(nodeId, var)] = { # nodeId is parentId, 
                                            #     'change': var__oPositionMinusIPosition[oVar],
                                            #     'replaceStr':replaceStr,
                                            #     'var':var
                                            # })
                                            # print(relativeShifts)
                                            # # import pdb;pdb.set_trace()
                                            # print('*******')


                                    # import pdb;pdb.set_trace()





                        
                            #join all the oUnmatchedFrags and matchedFrags and oVariables of same nodeId -> combinedFrag will be schemeparsable
                            #join all the iUnmatchedFrags and matchedFrags and iVariables of same nodeId -> combinedFrag will be schemeparsable
                            #Schemeparsable since 
                            #1. what remaining (after all these replacements), is schemeparsable
                            #2. before processing by this, it was schemeparsable
                            #3. each pattern is schemeparsable
                            #but is has to correspond to the actual inputoutput (cannot be relative) and also exclude variable changes TODO
                            #and again, the parent's changes are not calculated at this point in the code.
                            # we have to use relativeShifts' method, and then DFS after the recursiveParse.
                            #relatveShifts dictionary keys does not fit this...

                            ###

                            # print(self.rejoinedIFrags)
                            # print(self.rejoinedOFrags)
                            # iVarPosIdxInOGSansVarNumList
                            # ipos__varNumReplaceStr = {}
                            # for var, patternPos, listPos in iVarPosIdxInOGSansVarNumList:
                            #     ipos__varNumReplaceStr[patternPos] = currentVariablesToReplacement[var]
                            # opos__varNumReplaceStr = {}
                            # for var, patternPos, listPos in oVarPosIdxInOGSansVarNumList:
                            #     opos__varNumReplaceStr[patternPos] = currentVariablesToReplacement[var]
                            # def replaceFragVarAndCalculateStartPos(rejoinedFrags, pos__varNumReplaceStr):
                            #     replacedFrags = []
                            #     accumulatedPosIncrements = 0
                            #     accumulatedDollar = 0
                            #     for frag in rejoinedFrags:
                            #         newFrag = copy.deepcopy(frag)
                            #         if '$' in frag['w']:
                            #             replaceStr = pos__varNumReplaceStr[frag['s']+frag['w'].index('$')]
                            #             newFrag['os'] = copy.copy(newFrag['s']) # for outputPattern rootNonMatches_startPosOnOutputPattern__offset
                            #             newFrag['s'] += accumulatedPosIncrements - accumulatedDollar
                            #             accumulatedPosIncrements += len(replaceStr)
                            #             newFrag['e'] += accumulatedPosIncrements - accumulatedDollar
                            #             newFrag['fw'] = newFrag['w'].replace('$', replaceStr)
                            #             accumulatedDollar += 1
                            #         else:
                            #             newFrag['os'] = copy.copy(newFrag['s']) # for outputPattern rootNonMatches_startPosOnOutputPattern__offset
                            #             newFrag['s'] += accumulatedPosIncrements - accumulatedDollar
                            #             newFrag['e'] += accumulatedPosIncrements - accumulatedDollar
                            #             newFrag['fw'] = newFrag['w']
                            #         # import pdb;pdb.set_trace()
                            #         replacedFrags.append(newFrag)
                            #     return replacedFrags
                            # ###
                            # print('self.rejoinedIFrags:')
                            # print(self.rejoinedIFrags)
                            # print('self.rejoinedOFrags')
                            # print(self.rejoinedOFrags)
                            # ###
                            # for replacedFrag in replaceFragVarAndCalculateStartPos(self.rejoinedIFrags, ipos__varNumReplaceStr):
                            #     if not replacedFrag['matched']: #input and not(matched) => deletion
                            #         existingList = nonVariableChanges.get(nodeId, [])
                            #         existingList.append({#need to subtract the number of $ before this frag from s and e... TODO
                            #             'd':'r', # actually 'r' is always only from input... 
                            #             's':replacedFrag['s'],
                            #             'e':replacedFrag['e'],
                            #             'w':replacedFrag['w'],
                            #             'fw':replacedFrag['fw'],
                            #             # 'f':'i' # from inputPattern
                            #         })
                            #         nonVariableChanges[nodeId] = existingList
                            # for replacedFrag in replaceFragVarAndCalculateStartPos(self.rejoinedOFrags, opos__varNumReplaceStr):
                            #     if not replacedFrag['matched']: #output and not(matched) => addition
                            #         existingList =  nonVariableChanges.get(nodeId, [])
                            #         existingList.append({#need to subtract the number of $ before this frag from s and e... TODO
                            #             'd':'a', # also 'a' is always only from output...
                            #             's':replacedFrag['s'],
                            #             'e':replacedFrag['e'],
                            #             'w':replacedFrag['w'],
                            #             'fw':replacedFrag['fw'],
                            #             'os':replacedFrag['os']
                            #         })
                            #         nonVariableChanges[nodeId] = existingList
                            #         # import pdb;pdb.set_trace()


                            ipos__varNumReplaceStr = {}
                            for var, patternPos, listPos in iVarPosIdxInOGSansVarNumList:
                                ipos__varNumReplaceStr[patternPos] = currentVariablesToReplacement[var]
                            opos__varNumReplaceStr = {}
                            for var, patternPos, listPos in oVarPosIdxInOGSansVarNumList:
                                opos__varNumReplaceStr[patternPos] = currentVariablesToReplacement[var]
                            import bisect#TODO refactor
                            # print('self.rejoinedIFrags', self.rejoinedIFrags)
                            for frag in self.rejoinedIFrags:
                                if not frag['matched']: #input and not(matched) => deletion
                                    #
                                    idx = bisect.bisect_right(self.inVariablesPosSansVarnumList, frag['s']) - 1 # idx of the variable to start the preNonVariable
                                    if idx < 0:
                                        varEndPos = 0
                                    else:
                                        varEndPos = self.inVariablesPosSansVarnumList[idx] + 1
                                    preNonVariable = self.inputPattern[varEndPos:frag['s']]
                                    # print('frag', frag)
                                    # print('idx', idx)
                                    # print('self.inVariablesPosSansVarnumList', self.inVariablesPosSansVarnumList)
                                    # print('varEndPos', varEndPos)
                                    # print('preNonVariable|', preNonVariable)
                                    # import pdb;pdb.set_trace()
                                    #
                                    if '$' in frag['w']:
                                        replaceStr = ipos__varNumReplaceStr[frag['s']+frag['w'].index('$')]
                                        w = frag['w'].replace('$', replaceStr)
                                        # ns = frag['s'] -1 + len(replaceStr)
                                        ne = frag['e'] -1 + len(replaceStr)
                                        # import pdb;pdb.set_trace() # what should the preNonVariable be? TODD
                                    else:
                                        w = frag['w']
                                        # ns = frag['s']
                                        ne = frag['e']
                                    existingList = nonVariableChanges.get(nodeId, [])
                                    existingList.append({
                                        'd':'r', # actually 'r' is always only from input...
                                        's':frag['s'],
                                        'e':ne,#frag['e'],
                                        'w':w,#frag['w'],
                                        'p':preNonVariable # in pattern
                                    })
                                    nonVariableChanges[nodeId] = existingList
                            for frag in self.rejoinedOFrags:
                                if not frag['matched']: #output and not(matched) => addition
                                    #
                                    idx = bisect.bisect_right(self.outVariablesPosSansVarnumList, frag['s']) - 1
                                    if idx < 0:
                                        varEndPos = 0
                                    else:
                                        varEndPos = self.outVariablesPosSansVarnumList[idx] + 1
                                    preNonVariable = self.outputPattern[varEndPos:frag['s']]
                                    # print('self.outVariablesPosSansVarnumList', self.outVariablesPosSansVarnumList)
                                    # print('varEndPos', varEndPos)
                                    # print('preNonVariable|', preNonVariable)
                                    # import pdb;pdb.set_trace()
                                    #
                                    if '$' in frag['w']:
                                        replaceStr = opos__varNumReplaceStr[frag['s']+frag['w'].index('$')]
                                        w = frag['w'].replace('$', replaceStr)
                                        # ns = frag['s'] -1 + len(replaceStr)
                                        ne = frag['e'] -1 + len(replaceStr)
                                    else:
                                        w = frag['w']
                                        # ns = frag['s']
                                        ne = frag['e']
                                    existingList = nonVariableChanges.get(nodeId, [])
                                    existingList.append({
                                        'd':'a',
                                        's':frag['s'],
                                        'e':ne,#frag['e'],
                                        'w':w,#frag['w']
                                        'p':preNonVariable # in pattern
                                    })
                                    nonVariableChanges[nodeId] = existingList


                            # print(nonVariableChanges)
                            # import pdb;pdb.set_trace()
                    #there might be more unique variables in outputPattern than variables in inputPattern, see #logarithmtest.test__hin4__configTest
                    # if len(set(self.outVariables)) > len(set(self.variables)):
                    #     #then we need to create variables, which should be handled by manipulate.py?
                    #     missingVariables = list(set(self.outVariables) - set(self.variables))
                    #     varList = self.variables
                    #match&not_just_variable_and_space&less_variable_available


                    # currentVariablesToReplacement = dict(zip(variables, replaceStrs))
                    # currentVariablesToReplacement.update(self.additionalReplacementStrForVariablesDict)
                    for variable, replaceStr in currentVariablesToReplacement.items(): # childId are in the order of the variables in inputPattern
                        op = op.replace(variable, replaceStr)
                    # print('match', op)
                    # import pdb;pdb.set_trace()
                    return op, id__data[nodeId]['s'] 
        ##############
        # print('*******')
        # import pdb;pdb.set_trace()
        ##############
        manipulatedSchemeEquationStr, replaceStartPos = _recursiveManipulate(0) # root__nodeId is always 0

        ####
        # import pprint
        # pp = pprint.PrettyPrinter(indent=4)
        # print('relativeShifts')
        # pp.pprint(relativeShifts)
        # print('enclosureTree')
        # pp.pprint(enclosureTree)
        # print('id__data')
        # pp.pprint(id__data)
        ####
        if self.recordMaking:
            import bisect #TODO refactor
            stack = [(0, 0)] # TODO nodeId=0 contains non-matched frags too and must be added as offset...
            while len(stack) > 0:
                parentNodeId, parentChange = stack.pop()
                #

                # print(rootNonMatches_startPos__offset)
                # print('looking for', id__data[parentNodeId]['s'])
                # print('index in rootNonMatches_startPos__offset:', bisect.bisect_left(
                    # rootNonMatches_startPos__offset, id__data[parentNodeId]['s'], key=lambda tup: tup[0]))
                # parentOffsetByNonMatchesOfRoot = rootNonMatches_startPos__offset[bisect.bisect_left(
                #     rootNonMatches_startPos__offset, id__data[parentNodeId]['s'], key=lambda tup: tup[0])][1]
                # print("parentOffsetByNonMatchesOfRoot", parentOffsetByNonMatchesOfRoot)

                # print('rootNonMatches_startPos__offset')
                # print(rootNonMatches_startPos__offset)
                #
                #do the non-variable changes
                for frag in nonVariableChanges.get(parentNodeId, []):
                    if frag['d'] == 'a': # its take from outputPattern
                        # print('rootNonMatches_childId__listOfTupStartPosOffset', rootNonMatches_childId__listOfTupStartPosOffset)

                        patternStartPos_offsetTupList = rootNonMatches_childId__listOfTupStartPosOffset[parentNodeId]
                        # print('patternStartPos_offsetTupList', patternStartPos_offsetTupList)
                        offsetIdx = bisect.bisect_right(patternStartPos_offsetTupList, frag['s'], key=lambda tup: tup[0]) - 1 #somehow need to minus 1...
                        # print('offsetIdx', offsetIdx)
                        s = len(frag['p']) + patternStartPos_offsetTupList[offsetIdx][1]
                        # print('patternStartPos_offsetTupList', patternStartPos_offsetTupList)
                        # print('offsetIdx: ', offsetIdx, 'startPos_offsetTup:', patternStartPos_offsetTupList[offsetIdx])
                        # print('frag s', frag['s'])
                        # print('frag e', frag['e'])
                        # print('frag p', len(frag['p']))
                        # print('offsetted s:', len(frag['p']), '+', patternStartPos_offsetTupList[offsetIdx][1], '=', s)
                        # print('frag', frag)
                        # print('~~~~~~~~~~~~~~~~~~~~~~')
                        verPosWord.append({
                            't':'p', #nomatch(n)/varonly(v)/patrepl(p)
                            'd':frag['d'], #addition(a)/removal(r)/positional_shift[edit](e)
                            'n':parentNodeId, #nodeId where this was done
                            's':s, #relative( to outPattern) start position in new string processed, where this change was done
                            'e':s+len(frag['w']), #relative( to outPattern) end position in new string processed, where this change was done
                            'w':frag['w'], #string involved in the change
                            'v':None, #associated variable
                        })
                        # import pdb;pdb.set_trace()
                    else:# its take from inputPattern

                        patternStartPos_offsetTupList = rootNonMatches_childId__listOfTupStartPosOffset_i[parentNodeId]
                        # print(frag['s'], 'in', 'patternStartPos_offsetTupList', patternStartPos_offsetTupList)
                        offsetIdx = bisect.bisect_right(patternStartPos_offsetTupList, frag['s'], key=lambda tup: tup[0]) - 1 #somehow need to minus 1...
                        # print('offsetIdx', offsetIdx)
                        s = len(frag['p']) + patternStartPos_offsetTupList[offsetIdx][1]
                        # print('patternStartPos_offsetTupList', patternStartPos_offsetTupList)
                        # print('offsetIdx: ', offsetIdx, 'startPos_offsetTup:', patternStartPos_offsetTupList[offsetIdx])
                        # print('frag s', frag['s'])
                        # print('frag e', frag['e'])
                        # print('frag p', len(frag['p']))
                        # print('offsetted s:', len(frag['p']), '+', patternStartPos_offsetTupList[offsetIdx][1], '=', s)
                        # print('frag', frag)
                        # print('~~~~~~~~~~~~~~~~~~~~~~')
                        # import pdb;pdb.set_trace()
                        verPosWord.append({
                            't':'p', #nomatch(n)/varonly(v)/patrepl(p)
                            'd':frag['d'], #addition(a)/removal(r)/positional_shift[edit](e)
                            'n':parentNodeId, #nodeId where this was done
                            's':s, #relative( to outPattern) start position in new string processed, where this change was done
                            'e':s+len(frag['w']), #relative( to outPattern) end position in new string processed, where this change was done
                            'w':frag['w'], #string involved in the change
                            'v':None, #associated variable
                        })


                        # offset = parentOffsetByNonMatchesOfRoot
                        # verPosWord.append({
                        #     't':'p', #nomatch(n)/varonly(v)/patrepl(p)
                        #     'd':frag['d'], #addition(a)/removal(r)/positional_shift[edit](e)
                        #     'n':parentNodeId, #nodeId where this was done
                        #     's':offset+frag['s'], #relative( to outPattern) start position in new string processed, where this change was done
                        #     'e':offset+frag['e'], #relative( to outPattern) end position in new string processed, where this change was done
                        #     'w':frag['w'], #string involved in the change
                        #     'v':None, #associated variable
                        # })
                #####
                # print('####')
                # print(parentNodeId)
                # print(parentChange)
                # print('relativeShifts', relativeShifts)
                # print('####')
                #####
                children = enclosureTree.get(parentNodeId, [])
                for childNodeId in children:
                    rsd = relativeShifts.get(childNodeId)
                    # for var in shiftVariables: # var corresponed to a childNodeId, need to get it from id__data....
                    #     #d = relativeShifts.get((parentNodeId, var))
                    change = parentChange
                    if rsd is not None:
                        change += rsd['change']
                        ####
                        # print('####')
                        # print('childNodeId', childNodeId)
                        # print('replaceStr', rsd['replaceStr'])
                        # print('change', rsd['change'])
                        # print('parentChange:', parentChange)
                        # print('s', id__data[childNodeId]['s'])
                        # print(change)
                        # print('####')
                        ####

                        verPosWord.append({
                            't':'p', #nomatch(n)/varonly(v)/patrepl(p)
                            'd':'e', #addition(a)/removal(r)/positional_shift[edit](e)
                            'n':childNodeId, #nodeId where this was done
                            #NOT THE RIGHT LABELs....TODO do something about it?
                            's':id__data[childNodeId]['s'], #start position in original string processed, where this change was done
                            #'e' need to subtract sum of len(arg) before this in the outPattern
                            #original + positionalChangeWithinSubString + (sumOfParentsChangesInPosition)
                            #TODO cannot be done in recursion... because the parent's changes are not computed yet, have to DFS enclosureTree, after recursion
                            'e':id__data[childNodeId]['s'] + change, #end position in original string processed, where this change was done

                            'w':rsd['replaceStr'], #string involved in the change
                            'v':rsd['var'], #associated variable
                        })
                    stack.append((childNodeId, change))

        self.verPosWord = verPosWord
        return manipulatedSchemeEquationStr


