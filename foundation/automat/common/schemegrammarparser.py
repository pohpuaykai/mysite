from foundation.automat.common.regexshorts import Regexshorts as rs
from foundation.automat.common.longestcommonsubsequence import LongestCommonSubsequence
from foundation.automat.log import info

class SchemeGrammarParser:


    def __init__(self, inputPattern, outputPattern, verbose=False, recordMaking=False):
        """
        A parser, that will try to match inputPattern with (variables that begin with $ and end with a number).
        and then places the values of those matched variables, into the outputPattern, that also has
        the same variables.
        `Equation` class ignorant
        
        #TODO would it have been also good, if it was done with a dict__list (tree) structure, instead of string-based?

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
        # self.subsitutedOutputGrammar = self.outputPattern
        self.additionalReplacementStrForVariablesDict = {}

        self.allTakenNums = None # for when output has less variables than input, and we need to create

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




    def parse(self, schemeword, nodeIdsToSkip=None, existingVariables=None):
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
            info('you may skip these ids, and not change it to outputPattern: ')
            self.pp.pprint(id__data)
        self.manipulatedSchemeWord = self.manipulate(
            self.schemeword,
            self.variables,
            self.rawOutputPattern,
            self.rawInputPattern,
            self.id__data,
            self.enclosureTree,
            self.nodeIdsToSkip,
            existingVariables
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
        ###########
        # info('schemeword', schemeword)
        # info('pattern', pattern)
        # info('firstPre', firstPre)
        ###########
        for sPos in rs.lazyPrefixFinder(firstPre, schemeword):
            dollarPoss = []
            start = sPos
            suf = pattern # for the case when there are no variables in pattern
            for i in range(0, len(patternSegmentedByDollar) -1):
                pre = patternSegmentedByDollar[i]
                suf = patternSegmentedByDollar[i+1]
                #########
                # info('pre|', pre, '|suf|', suf, '|start+len(pre)|', start+len(pre), '|schemeword[start+len(pre)]|', schemeword[start+len(pre)])
                # info('len(schemeword) < (start+len(pre))', len(schemeword) < (start+len(pre)))
                # import pdb;pdb.set_trace()
                # info("schemeword[start+len(pre)] == '('", schemeword[start+len(pre)] == '(')
                #########
                if (start+len(pre)) < len(schemeword) and schemeword[start+len(pre)] == '(':
                    ##########
                    # info('0!', i, start, pre)
                    ##########
                    #
                    nextPos = getNextBalancedPos(start+len(pre)) + 1 # return None if cannot find
                    ##########
                    # info('0!nextPos', nextPos, i, start, pre)
                    ##########
                    # if 
                else:#variable, find next place that starts with suf
                    ##########
                    # info('1!', i, start, pre)

                    ##########
                    try:
                        subStart = start+len(pre)
                        subEnd = schemeword[start+len(pre):].index(suf) + (start+len(pre))
                        for j in range(subStart, subEnd+1):
                            if (schemeword[j].isspace()) or (schemeword[j] in ['(', ')']):
                                nextPos = j
                                break
                        if nextPos == subStart:
                            nextPos = None # empty string

                    ##########
                        # info('1!nextPos', nextPos, i, start, pre)

                    ##########
                    except:
                        nextPos = None
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
                # info('!0!', schemewordSuf, schemewordSufStart, schemewordSufEnd)
                # info('!0!', dollarPoss)
                # import pdb;pdb.set_trace()
                schemewordSufToMatch = schemewordSuf[:len(suf)]
            else:
                schemewordSufToMatch = suf
            # info(schemewordSufToMatch, '<<schemewordSufToMatch', suf)
            if schemewordSufToMatch == suf and len(dollarPoss) == len(patternSegmentedByDollar) - 1: # we got all the dollarPoss
                ######
                # info('returning: ', (sPos+chopped, start+len(suf)+chopped, dollarPoss), '*****')
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

        # info(schemeword)
        # info(answers)
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
            # info(stack, '<<<stack')
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
        enclosureTree = {} # TODO refactor with EnclosureTree? Also increases coupling though...
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
                    #     info('~~~~')
                    #     info('mycms', mycms)
                    #     info(startPoss)
                    #     info('~~~~')
                    #
                    positionToInsert = bisect.bisect_left(startPoss, mycms)
                    childIds.insert(positionToInsert, data['id'])
                enclosureTree[data['pid']] = childIds
        # info(id__data)
        # info(enclosureTree)
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


    def _manipulationPrep__helperDatum(self,enclosureTree, id__data):
        if self.verbose:
            info(self.variables)
            info(self.inVariablesAndPos)
            info(self.inVariablesPosSansVarnumList)
            info(self.outVariablesPosSansVarnumList)
            info(id__data)
        if self.recordMaking:

            allValuesThatMatched = list(map(lambda data: data['w'], id__data.values()))

            #actually these only appears in patterns not(self.patternOnlyVariablesAndSpaces), so might be a bit inefficient... but for readability?
            self.iVars__count = {}
            for var, pos in self.inVariablesAndPos:
                self.iVars__count[var] = self.iVars__count.get(var, 0) + 1
            self.oVars__count = {}
            for var, pos in self.outVariablesAndPos:
                self.oVars__count[var] = self.oVars__count.get(var, 0) + 1
            self.allUniqueVars = set(map(lambda t: t[0], self.inVariablesAndPos)).union(map(lambda t: t[0], self.outVariablesAndPos))

            #neccesitat?
            self.iVarPosIdxInOGSansVarNumList = list(zip(self.variables, self.inVariablesPosSansVarnumList, range(len(self.variables))))
            self.oVarPosIdxInOGSansVarNumList = list(zip(self.outVariables, self.outVariablesPosSansVarnumList, range(len(self.outVariables))))
            self.iVar__posIdxInOGList = {}
            for var0, pos, idx in self.iVarPosIdxInOGSansVarNumList:
                self.iVar__posIdxInOGList[var0] = (pos, idx)
            self.oVar__posIdxInOGList = {}
            for var0, pos, idx in self.oVarPosIdxInOGSansVarNumList:
                self.oVar__posIdxInOGList[var0] = (pos, idx)
            var__oPositionMinusIPosition = {}

            if self.verbose:
                info('iVarPosIdxInOGSansVarNumList')
                info(self.iVarPosIdxInOGSansVarNumList) # inVariablesPosSansVarnumList SAME? just different format
                info('oVarPosIdxInOGSansVarNumList')
                info(self.oVarPosIdxInOGSansVarNumList) # outVariablesPosSansVarnumList SAME? just different format

            #match variables[enclosureTree] to replaceStrs[matchedSchemewords(id__data)]
            self.nodeId__rootNonMatches_childId__listOfTupStartPosOffset_i = {}
            self.nodeId__rootNonMatches_childId__listOfTupStartPosOffset = {}
            if self.verbose:
                info(enclosureTree) 
            self.nodeId__var__oPositionMinusIPosition = {}
            self.nodeId__variables__valuesPos = {} # BUT THIS IS ONLY FOR inputPattern?
            import copy # TODO refactor
            #TODO is it better to abandon the recursion, and just do everything iterative?
            #we don't do the nodeId=0, because it is not a variable matching, just YES/NO match to inputPattern.
            # number of children is the number of matches in the id__data[0]['w'], only after nodeId=0, then the number of children match the number of variables in the inputPattern
            #This is why are start from the children of nodeId=0, because heran, we do var to replaceStr matching
            stack = copy.deepcopy(enclosureTree[0]) # traverse the enclosureTree, we will also do this in manipulate (but recursive.) is this a bit inefficient... but for readability?
            while len(stack) > 0:
                cid = stack.pop()
                children = enclosureTree.get(cid, [])
                stack += reversed(children) # reversed so that child pops out in argumentOrder
                #
                rStrs = dict(zip(range(len(children)), map(lambda childId: id__data[childId]['w'], children)))
                variables__valuesPos = {} # dict to check if variable has more than 1 value mapped
                variables__valuesPosNoVarnum = {}
                #
                #Here is where we fill up the variables__valuesPosNoVarnum
                #check if same variable has been mapped to more than 1 value <<< this is not well-defined
                # for varIdx in range(0, len(self.variables)):
                # we are relying on the fact that there was match, so implying that the children line up with the input variables.
                # if there was no match... then this assumption is not valid
                # for varIdx in range(0, len(self.inVariablesAndPos)):
                #only pattern and 
                if self.patternOnlyVariablesAndSpaces: #input pattern only variables and spaces, then we are just matching variables/primitives
                    for childId in children:
                        variables__valuesPosNoVarnum = {}
                        for var, vPos in self.inVariablesAndPos:
                            variables__valuesPosNoVarnum[var] = (id__data[childId]['w'], vPos)
                            if self.variables < self.outVariables:# and cid != 0: # the root does not need a extraVar, because not substitutable? 
                                # need to add values to fill the gap, since we are using self.nodeId__variables__valuesPos for both input & output
                                missingAmount = len(set(self.outVariables) - set(self.variables))
                                nVarList = self.giveMeNVariableNotInThisList(missingAmount, varList=allValuesThatMatched) # all the values matched, no matter whether variable/primitive
                                for var, val in zip(sorted(list(set(self.outVariables) - set(self.variables))), sorted(nVarList)):
                                    variables__valuesPosNoVarnum[var] = (val, -1) # no posNum, cause autogenerated
                        self.nodeId__variables__valuesPos[childId] = variables__valuesPosNoVarnum
                else:
                    for varIdx in range(0, len(children)):
                        #very convienent that rStrs(values) and self.variables are already aligned in list order :) #Courtesey of {positionToInsert = bisect.bisect_left(startPoss, mycms)}
                        
                        variable, pos = self.inVariablesAndPos[varIdx] #TODO can be refactored to self.inVariablesPosSansVarnumList
                        value = rStrs[varIdx] # rStrs are children's w...
                        posSansVarnum = self.inVariablesPosSansVarnumList[varIdx]
                        variables__valuesPosNoVarnum[variable] = (value, posSansVarnum)
                        #
                        existingValuePos = variables__valuesPos.get(variable, (None, None))
                        existingValue, existingPos = existingValuePos
                        if existingValue is not None and existingValue != value: 
                            #more than one value was assigned to variable and those values are different
                            raise Exception(f'{existingValue} was assigned to {variable} at position {existingPos}, and now {value} is being assigned to the same {variable} again. Not well-defined')
                        variables__valuesPos[variable] = (value, pos)
                    if len(self.variables) == 0 or (self.variables < self.outVariables and len(children) > 0):# and cid != 0: # the root does not need a extraVar, because not substitutable? 
                        # need to add values to fill the gap, since we are using self.nodeId__variables__valuesPos for both input & output
                        missingAmount = len(set(self.outVariables) - set(self.variables))
                        nVarList = self.giveMeNVariableNotInThisList(missingAmount, varList=allValuesThatMatched) # all the values matched, no matter whether variable/primitive
                        for var, val in zip(sorted(list(set(self.outVariables) - set(self.variables))), sorted(nVarList)):
                            variables__valuesPosNoVarnum[var] = (val, -1) # no posNum, cause autogenerated
                    self.nodeId__variables__valuesPos[cid] = variables__valuesPosNoVarnum #TODO refactor, this is not just for recordMaking!

                variables__valuesPos = self.nodeId__variables__valuesPos.get(cid, {})
                # for patterns like distributivity, this is not true: len(self.outVariables) == len(variables__valuesPos)
                if len(variables__valuesPos) > 0:# for outPattern
                    var__oPositionMinusIPosition = {} # KEY should be (var, listIdx) or just listIdx.
                    # for var0 in self.allUniqueVars:
                    for oIdx in range(len(self.outVariables)):
                        var0 = self.outVariables[oIdx]
                        if self.iVars__count.get(var0, 0) == self.oVars__count.get(var0, 0):
                            iPatternPos, iOGListIdx = self.iVar__posIdxInOGList[var0]
                            oPatternPos, oOGListIdx = self.oVar__posIdxInOGList[var0]
                            #also need to add the 1.preNonVariables, 2. at each var
                            totalLenBeforeVar0InRIPattern = 0 
                            if len(self.iVarPosIdxInOGSansVarNumList) > 0 and len(self.iVarPosIdxInOGSansVarNumList[:iOGListIdx]) == 0: # we still need to add preNonVariable
                                totalLenBeforeVar0InRIPattern = len(self.inputPattern[0:self.iVarPosIdxInOGSansVarNumList[0][1]])
                            prevIPatternStartPos = 0
                            for iVar, iPrevPos, iidx in self.iVarPosIdxInOGSansVarNumList[:iOGListIdx]: # vars before var0 in iPattern
                                iNextPos = iPrevPos
                                if iidx + 1 <= len(self.iVarPosIdxInOGSansVarNumList[:iOGListIdx]):
                                    _, iNextPos, _ = self.iVarPosIdxInOGSansVarNumList[iidx+1]
                                replacedStr, _ = variables__valuesPos[iVar]
                                if iidx > 0:
                                    preNonVariable = self.inputPattern[prevIPatternStartPos+1:iPrevPos] # get rid of the $
                                else:
                                    preNonVariable = self.inputPattern[prevIPatternStartPos:iPrevPos]
                                prevIPatternStartPos = iPrevPos
                                # -1 for the $ on the prev # amount of space, from nextStart to prevEnd in pattern(not realised pattern!)
                                totalLenBeforeVar0InRIPattern +=  len(preNonVariable) + len(replacedStr)# len(currentVariablesToReplacement[iVar]) + (iNextPos - iPrevPos -1) 
                            #need to add current preNonVariable
                            if len(self.iVarPosIdxInOGSansVarNumList[:iOGListIdx]) > 0: #last preNonVariable
                                iPrevPos = self.iVarPosIdxInOGSansVarNumList[iOGListIdx][1]
                                totalLenBeforeVar0InRIPattern += len(self.inputPattern[prevIPatternStartPos+1:iPrevPos])
                            
                            totalLenBeforeVar0InROPattern = 0
                            if len(self.oVarPosIdxInOGSansVarNumList) > 0 and len(self.oVarPosIdxInOGSansVarNumList[:oOGListIdx]) == 0: # we still need to add preNonVariable
                                totalLenBeforeVar0InROPattern = len(self.outputPattern[0:self.oVarPosIdxInOGSansVarNumList[0][1]])
                            prevOPatternStartPos = 0
                            for oVar, oPrevPos, oidx in self.oVarPosIdxInOGSansVarNumList[:oOGListIdx]: # vars before var0 in oPattern
                                oNextPos = oPrevPos
                                if oidx + 1 <= len(self.oVarPosIdxInOGSansVarNumList[:oOGListIdx]):
                                    _, oNextPos, _ = self.oVarPosIdxInOGSansVarNumList[oidx+1]
                                replacedStr, _ = variables__valuesPos[oVar]
                                if oidx > 0:
                                    preNonVariable = self.outputPattern[prevOPatternStartPos+1:oPrevPos]
                                else:
                                    preNonVariable = self.outputPattern[prevOPatternStartPos:oPrevPos]
                                prevOPatternStartPos = oPrevPos
                                #
                                # -1 for the $ on the prev # amount of space, from nextStart to prevEnd in pattern(not realised pattern!)
                                totalLenBeforeVar0InROPattern +=  len(preNonVariable) + len(replacedStr)# len(currentVariablesToReplacement[oVar]) + (oNextPos - oPrevPos -1) 
                            #need to add current preNonVariable
                            if len(self.oVarPosIdxInOGSansVarNumList[:oOGListIdx]) > 0: #last preNonVariable
                                oPrevPos = self.oVarPosIdxInOGSansVarNumList[oOGListIdx][1]
                                # info(prevOPatternStartPos,oPrevPos, 'adding at last to output: ', self.outputPattern[prevOPatternStartPos+1:oPrevPos], len(self.outputPattern[prevOPatternStartPos+1:oPrevPos]))
                                totalLenBeforeVar0InROPattern += len(self.outputPattern[prevOPatternStartPos+1:oPrevPos])
                            # var__oPositionMinusIPosition[var0] = totalLenBeforeVar0InROPattern - totalLenBeforeVar0InRIPattern
                            var__oPositionMinusIPosition[oIdx] = totalLenBeforeVar0InROPattern - totalLenBeforeVar0InRIPattern
                        self.nodeId__var__oPositionMinusIPosition[cid] = var__oPositionMinusIPosition
                ######


    def manipulate(self, oWord, variables, outputPattern, inputPattern, id__data, enclosureTree, nodeIdsToSkip, existingVariables=None):
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
        self._manipulationPrep__helperDatum(enclosureTree, id__data)

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
        # nodeId__variables__valuesPos = {} # dict of dict, for computation of rootNonMatches_childId__listOfTupStartPosOffset, actually we only need this info, whose direct_parent is a direct_child of the root. TODO further, SPACE-OPTIMISATION
        verPosWord = []
        import copy
        def _recursiveManipulate(nodeId):
            # BaseCase
            if nodeId not in enclosureTree: # its a leaf
                # if len(set(self.outVariables)) > len(set(self.variables)): not this, see case test__hin4__configTest
                if len(self.variables) == 0:
                    #but first we need to replace the variables in outputPattern first... with variable/s that in not in equation.
                    #may be generate the need extra values here
                    substitutedOutputPattern = copy.deepcopy(self.rawOutputPattern)
                    for oVar, (oVal, oPos) in self.nodeId__variables__valuesPos[nodeId].items():
                        substitutedOutputPattern = substitutedOutputPattern.replace(oVar, oVal)
                    return substitutedOutputPattern, id__data[nodeId]['s']
                else:

                    return id__data[nodeId]['w'], id__data[nodeId]['s']
            # RecursiveCase
            replaceStrsPos = [] # _recursiveManipulate need to return the startPos of replaceStr too.
            replaceStrs = []
            childIds = enclosureTree[nodeId]
            for childId in childIds: 
                data = id__data[childId]
                replaceStr, startPos = _recursiveManipulate(data['id'])
                replaceStrs.append(replaceStr)
                replaceStrsPos.append((replaceStr, startPos)) # TODO we don't need this, we already got: self.nodeId__variables__valuesPos
            
            # number of children is the number of matches in the id__data[0]['w'], only after nodeId=0, then the number of children match the number of variables in the inputPattern
            #This is why are start from the children of nodeId=0, because heran, we do var to replaceStr matching
            if id__data[nodeId]['pid'] is None:#it was not matched to any variables, or inputPattern has no variables :), according to def findAll, this is the root, starting Node
                rWord = copy.deepcopy(oWord)
                #

                if self.recordMaking and len(self.nodeId__variables__valuesPos.get(1, {})) > 0: # for totally no matches: len(self.nodeId__variables__valuesPos.get(1, {})) > 0
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
                            var__valuesPosSansVarnum = self.nodeId__variables__valuesPos.get(childId, {})
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
                            rootNonMatches_childId__listOfTupStartPosOffset_i[childId].append((id__data[childId]['s'], accumulatedOffset))
                            accumulatedOffset += len(id__data[childId]['w'])
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
                            var__valuesPosSansVarnum = self.nodeId__variables__valuesPos.get(childId, {}) # should be available since we do bottoms up (recursion)
                            for listIdx, (var, pos) in enumerate(self.outVariablesAndPos):
                                # import pdb;pdb.set_trace()
                                replaceStr, _ = var__valuesPosSansVarnum[self.outVariablesAndPos[listIdx][0]]

                                #add the pre-non-variable(outputPattern) of this outVariable. -> accumulatedOffset
                                posSansVarnum = self.outVariablesPosSansVarnumList[listIdx]
                                if listIdx > 0:
                                    startPosOnPattern = self.outVariablesPosSansVarnumList[listIdx - 1]
                                else:
                                    startPosOnPattern = 0
                                
                                preNonVariableOfOutputPattern = self.outputPattern[startPosOnPattern:posSansVarnum]
                                #appendedTup[0] is the startPos on the self.outputPattern
                                rootNonMatches_childId__listOfTupStartPosOffset[childId].append((startPosOnPattern,accumulatedOffset - max(0, listIdx - 1))) # seems like the offset positions always over by 1... WHY?
                                #remember to subtract the total number of $ = listIdx

                                accumulatedOffset += len(replaceStr) + len(preNonVariableOfOutputPattern) # - minusVarLen # need to add previous replaceStr
                                #
                        else: # outputPattern has no variables, there should be only 1 match for each childId, and its replaceStr=id__data['childId']['w']
                            rootNonMatches_childId__listOfTupStartPosOffset[childId].append((id__data[childId]['s'], accumulatedOffset))
                            accumulatedOffset += len(id__data[childId]['w'])
                            # #NOTE THAT BELOW IS ALSO POSSIBLE (and totally independent of accumulatedOffset):
                            # rootNonMatches_childId__listOfTupStartPosOffset[childId].append((id__data['childId']['s'], id__data['childId']['s']))

                    #
                    if len(self.outVariablesPosSansVarnumList) > 0:
                        startPosOnPattern = self.outVariablesPosSansVarnumList[listIdx]
                        replaceStr, _ = var__valuesPosSansVarnum[self.outVariablesAndPos[listIdx-1][0]] # value == replaceStr
                        rootNonMatches_childId__listOfTupStartPosOffset[childId].append((startPosOnPattern, accumulatedOffset - max(0, listIdx)))
                    # else: # what about for no variables

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
                    template = copy.deepcopy(id__data[nodeId]['w'])
                    for listIdx, childId in enumerate(reversed(childIds)):
                        variables__valuesPos = self.nodeId__variables__valuesPos[childId]
                        currentVariablesToReplacement = dict(map(lambda t: (t[0], t[1][0]), variables__valuesPos.items())) # extract variables__replacementStr from variables__valuesPos
                        # print("currentVariablesToReplacement", currentVariablesToReplacement)
                        op = copy.deepcopy(self.rawOutputPattern)
                        for variable, replaceStr in currentVariablesToReplacement.items():
                            op = op.replace(variable, replaceStr)
                        #replace the child in template with op (in reverse, since might affect the earlier character positions)
                        #then the 'w' becomes the template, and the variables are the replaceStr, and replaceStr are (outputPattern with 'ogVariable' replaced)
                        parentStartOffset = id__data[nodeId]['s']
                        data = id__data[childId]
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

                        template = rs.replaceAtPos(template, data['s']- parentStartOffset, data['e']- parentStartOffset, op)
                    return template, parentStartOffset # = id__data[nodeId]['s']
                else:
                    currentVariablesToReplacement = dict(zip(variables, replaceStrs))
                    if len(self.outVariables) > len(self.variables):
                        missingVariables = set(self.outVariables) - set(self.variables)
                        for mVar in missingVariables:
                            mVal, mPos = self.nodeId__variables__valuesPos[nodeId][mVar]
                            currentVariablesToReplacement[mVar] = mVal

                    # nodeId__variables__valuesPos[nodeId] = variables__valuesPosNoVarnum
                    if nodeId in nodeIdsToSkip:
                        op = copy.deepcopy(inputPattern)
                        #actually no change here... no need to replace, can just return... lol you waste computation
                        #TODO optimise
                    else:
                        op = copy.deepcopy(outputPattern)
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
                            #for iCount == oCount
                            #precalculate the mapping for amount of change in position for each var that was only transposed
                            #amount of character shifted
                            currentVariablesToChildIds = dict(zip(variables, childIds)) # TODO to the preamble?
                            ###

                            # info(self.nodeId__var__oPositionMinusIPosition)
                            var__oPositionMinusIPosition = self.nodeId__var__oPositionMinusIPosition[nodeId]
                            ###


                            # for iCount <> oCount.
                            variables__valuesPos = self.nodeId__variables__valuesPos[nodeId]
                            iVarPosIdxInOGList = [(t[0], t[1], idx) for idx, t in enumerate(self.inVariablesAndPos)] # t[0] is $102, t[1] is pos
                            oVarPosIdxInOGList = [(t[0], t[1], idx) for idx, t in enumerate(self.outVariablesAndPos)]
                            for var in self.allUniqueVars:
                                iCount = self.iVars__count.get(var, 0)
                                oCount = self.oVars__count.get(var, 0)

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
                                    #match and find positional differences
                                    varWithPosAndIdx = list(filter(lambda t: t[0]==var, oVarPosIdxInOGList))
                                    #need to subtract sum of len of numberId(v) of all the v before var (to get absolute position)
                                    for oVar, oPos, oIdx in varWithPosAndIdx:
                                        iPos, iIdx = self.iVar__posIdxInOGList[oVar]
                                        # if oIdx != iIdx: # position was shifted..., TODO but this is only in the variablelist. if position of variable was shifted in the actual, but not in variable list, this will not be detected.
                                        if oPos != iPos:
                                            replacedStr, _ = variables__valuesPos[oVar]
                                            associatedChildId = currentVariablesToChildIds[var]
                                            relativeShifts[associatedChildId] = {
                                                'change': var__oPositionMinusIPosition[oIdx],
                                                'replaceStr':replacedStr,
                                                'var':var
                                            }

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
                            ipos__varNumReplaceStr = {}
                            for var, patternPos, listPos in self.iVarPosIdxInOGSansVarNumList:
                                ipos__varNumReplaceStr[patternPos], _ = variables__valuesPos[var]
                            opos__varNumReplaceStr = {}
                            for var, patternPos, listPos in self.oVarPosIdxInOGSansVarNumList:
                                opos__varNumReplaceStr[patternPos], _ = variables__valuesPos[var]
                            import bisect#TODO refactor
                            for frag in self.rejoinedIFrags:
                                if not frag['matched']: #input and not(matched) => deletion
                                    #
                                    idx = bisect.bisect_right(self.inVariablesPosSansVarnumList, frag['s']) - 1 # idx of the variable to start the preNonVariable
                                    if idx < 0:
                                        varEndPos = 0
                                    else:
                                        varEndPos = self.inVariablesPosSansVarnumList[idx] + 1
                                    preNonVariable = self.inputPattern[varEndPos:frag['s']]
                                    if '$' in frag['w']:
                                        replaceStr = ipos__varNumReplaceStr[frag['s']+frag['w'].index('$')]
                                        w = frag['w'].replace('$', replaceStr)
                                        ne = frag['e'] -1 + len(replaceStr)
                                        # import pdb;pdb.set_trace() # what should the preNonVariable be? TODD
                                    else:
                                        w = frag['w']
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
                                    #
                                    if '$' in frag['w']:
                                        replaceStr = opos__varNumReplaceStr[frag['s']+frag['w'].index('$')]
                                        w = frag['w'].replace('$', replaceStr)
                                        ne = frag['e'] -1 + len(replaceStr)
                                    else:
                                        w = frag['w']
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

                    #there might be more unique variables in outputPattern than variables in inputPattern, see #logarithmtest.test__hin4__configTest
                    for variable, replaceStr in currentVariablesToReplacement.items(): # childId are in the order of the variables in inputPattern
                        op = op.replace(variable, replaceStr)
                    return op, id__data[nodeId]['s'] 
        manipulatedSchemeEquationStr, replaceStartPos = _recursiveManipulate(0) # root__nodeId is always 0

        if self.recordMaking:
            if self.verbose:
                info('self.nodeId__var__oPositionMinusIPosition', self.nodeId__var__oPositionMinusIPosition)
                info('rootNonMatches_childId__listOfTupStartPosOffset_i', rootNonMatches_childId__listOfTupStartPosOffset_i)
                info('rootNonMatches_childId__listOfTupStartPosOffset', rootNonMatches_childId__listOfTupStartPosOffset)

            import bisect #TODO refactor
            stack = [(0, 0)] # TODO nodeId=0 contains non-matched frags too and must be added as offset...
            while len(stack) > 0:
                parentNodeId, parentChange = stack.pop()
                #do the non-variable changes
                for frag in nonVariableChanges.get(parentNodeId, []):
                    if frag['d'] == 'a': # its take from outputPattern
                        patternStartPos_offsetTupList = rootNonMatches_childId__listOfTupStartPosOffset[parentNodeId]
                        offsetIdx = bisect.bisect_right(patternStartPos_offsetTupList, frag['s'], key=lambda tup: tup[0]) - 1 #somehow need to minus 1...
                        s = len(frag['p']) + patternStartPos_offsetTupList[offsetIdx][1]
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
                        offsetIdx = bisect.bisect_right(patternStartPos_offsetTupList, frag['s'], key=lambda tup: tup[0]) - 1 #somehow need to minus 1...
                        s = len(frag['p']) + patternStartPos_offsetTupList[offsetIdx][1]
                        verPosWord.append({
                            't':'p', #nomatch(n)/varonly(v)/patrepl(p)
                            'd':frag['d'], #addition(a)/removal(r)/positional_shift[edit](e)
                            'n':parentNodeId, #nodeId where this was done
                            's':s, #relative( to outPattern) start position in new string processed, where this change was done
                            'e':s+len(frag['w']), #relative( to outPattern) end position in new string processed, where this change was done
                            'w':frag['w'], #string involved in the change
                            'v':None, #associated variable
                        })
                children = enclosureTree.get(parentNodeId, [])
                for childNodeId in children:
                    rsd = relativeShifts.get(childNodeId)
                    # for var in shiftVariables: # var corresponed to a childNodeId, need to get it from id__data....
                    #     #d = relativeShifts.get((parentNodeId, var))
                    change = parentChange
                    if rsd is not None:
                        change += rsd['change']
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


    def giveMeNVariableNotInThisList(self, n, varList=None): # how do you know which is var, which is primitive?
        """
        look for variables that start with v_
        if None, then return v_{0}
        else:
            look for the number after v_ or v_{
            if no number after v_
                then return v_{0}
            else
                return v_{num+1}
        """
        if self.allTakenNums is None:
            variablePrefix = 'v_'
            variableStartingWithPrefix = None
            self.allTakenNums = []
            for variable in varList:
                if variable.startswith(variablePrefix+'{'): # we expect the variable to close with '}', following LatexSyntax
                    startPosOfCurlyBracket = variable.index(variablePrefix+'{') + len(variablePrefix+'{')
                    #since we expect this to be the first openbracket, then the close bracket must be the last '}' == no need bracket-matching
                    endPosOfCurlyBracket = variable.rindex('}')
                    try:
                        num = int(variable[startPosOfCurlyBracket:endPosOfCurlyBracket])
                        allTakenNums.append(num)
                    except:
                        pass
                        # num = 0
                elif variable.startswith(variablePrefix): # we expect the next position to be a number, following LatexSyntax
                    posOfEndOfVariablePrefix = variable.index(variablePrefix) + len(variablePrefix)
                    try:
                        num = int(variable[posOfEndOfVariablePrefix:posOfEndOfVariablePrefix+1]) # we only expect a 1 character number, following LatexSyntax
                        allTakenNums.append(num)
                        #then we add 1 to get the next
                    except:
                        pass
                        # num = 0 #next character after variablePrefix is not a num
                # else:
                #     num = 0
        rList = []
        nmax = max(self.allTakenNums) if len(self.allTakenNums) > 0 else n
        for num in range(0, nmax):
            if len(rList) >= n:
                break
            if len(rList) < n and num not in self.allTakenNums:
                self.allTakenNums.append(num)
                rList.append(f'v_{{{num}}}')
        if len(rList) < n: # continue adding from max(allTakeNums)
            startNum = max(self.allTakenNums) + 1
            for num in range(startNum, startNum+(n - len(rList))):
                self.allTakenNums.append(num)
                rList.append(f'v_{{{num}}}')

        return rList