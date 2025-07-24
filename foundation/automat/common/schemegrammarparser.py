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
        self.inputPattern, self.variables, self.inVariablesAndPos, self.inVariablesPosSansVarnumList, self.inStaticsStartEnd = self.prepareRawPattern(self.rawInputPattern)
        self.outputPattern, self.outVariables, self.outVariablesAndPos, self.outVariablesPosSansVarnumList, self.outStaticsStartEnd = self.prepareRawPattern(self.rawOutputPattern)
        self.calledBuildEnclosure = False
        # self.subsitutedOutputGrammar = self.outputPattern
        self.additionalReplacementStrForVariablesDict = {}

        self.allTakenNums = None # for when output has less variables than input, and we need to create

        # self.recordMaking = recordMaking
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
        self.matches = [] # all the not0 and notLeaves(if not variables==0)
        if not self.noMatches:
            if len(self.variables) == 0: # children_of_0(leaves) are matches
                for parentId, data in filter(lambda t: t[0]!=0, self.id__data.items()):
                    self.matches.append({'s':data['s'], 'e':data['e'], 'w':data['w']})
            else: #leaves are not matches
                for parentId, data in filter(lambda t: t[0]!=0 and t[0] in self.enclosureTree, self.id__data.items()):
                    self.matches.append({'s':data['s'], 'e':data['e'], 'w':data['w']})


    def patternChanges(self):
        """

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
        #TODO try out StringCompare.damerauLevenshtein, for an upgrade? static that swap place, are current detected as an addition and a deletion, not very effective.<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
            #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<change this after findAllEntity
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
                return matchingBrackets[beginPos]#returns the next balanced_close_brackets after beginPos
        patternSegmentedByDollar = pattern.split('$')
        # if len(patternSegmentedByDollar) == 1: # there are no $ in pattern <==> no variables in pattern
        # is this pattern possible: '$0 $1'?
        # if so, then it can only match scheme strings with 2-variables?
        firstPre = patternSegmentedByDollar[0]
        ###########
        # print(schemeword, 'schemeword<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< chopped: ', chopped)
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
                # print('pre|', pre, '|suf|', suf, '|start+len(pre)|', start+len(pre), '|schemeword[start+len(pre)]|', schemeword[start+len(pre)])
                # print('(start+len(pre)) < len(schemeword)', (start+len(pre)) < len(schemeword))
                # print("schemeword[start+len(pre)] == '('", schemeword[start+len(pre)] == '(')
                # import pdb;pdb.set_trace()
                #########
                if (start+len(pre)) < len(schemeword) and schemeword[start+len(pre)] == '(':
                    ##########
                    # info('0!', i, start, pre)
                    ##########
                    #
                    nextPos = getNextBalancedPos(start+len(pre)) + 1 # return None if cannot find
                    ##########
                    # print('0!nextPos', nextPos, i, start, pre)
                    ##########
                    # if 
                else:#variable, find next place(ENTITY) that starts with suf<<<<<<<<<<<<<<<<<<find nexy Entity instead of place(position)
                    #if suf==' ', do you get all the space, and then next?
                    ##########
                    # info('1!', i, start, pre)

                    ##########
                    try:
                        subStart = start+len(pre)
                        # subEnd = schemeword[start+len(pre):].index(suf) + (start+len(pre))
                        subEnd = len(schemeword)
                        openBra__count___others = {'{':0, '[':0}; closeBra__openBra = {'}':'{', ']':'['} # this is for test__latexParserUnparse__bipartiteSearch_dc_twoResistor_parallel_STEP1, where there are compound variables
                        for j in range(subStart, subEnd+1):
                            if schemeword[j] in openBra__count___others:
                                openBra__count___others[schemeword[j]] += 1
                            elif schemeword[j] in closeBra__openBra:
                                openBra__count___others[closeBra__openBra[schemeword[j]]] -= 1
                            # print(j);import pdb; pdb.set_trace()
                            if not any(map(lambda count: count!=0, openBra__count___others.values())) and ((schemeword[j].isspace()) or (schemeword[j] in ['(', ')'])): # do bracket accounting here for {} and []
                            # if (schemeword[j].isspace()) or (schemeword[j] in ['(', ')']): # do bracket accounting here for {} and []
                            
                                nextPos = j
                                break
                        if nextPos == subStart:
                            nextPos = None # empty string

                    ##########
                        # print('1!nextPos', nextPos, i, start, pre)

                    ##########
                    except:
                        nextPos = None
                if nextPos is None: # cannot continue with this sPos
                    break # try the next sPos
                else:
                    dollarPoss.append((start+len(pre)+chopped, nextPos+chopped))
                    start = nextPos
                # print('********************************************************************')
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
            if schemeword.startswith('('):#can include the inVarPos in dollarPoss<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                dollarPoss = [] # position of arguments of this level (might be enclosed by brackets or not), also the $ variables
                #do bracket-matching
                openBracketPosStack = [0]
                for i in range(1, len(schemeword)):
                    c = schemeword[i]
                    if c == '(':
                        openBracketPosStack.append(i)
                    elif c == ')':
                        matchingOpenBracketPos = openBracketPosStack.pop()
                        if len(openBracketPosStack) == 1: #we are on direct child level of root bracket
                            vIdx = len(dollarPoss)
                            dollarPoss.append((matchingOpenBracketPos, i+1)) # inclusive of closeBracket
                if len(dollarPoss) == 0: # schemeword has no inner brackets (arguments has no inner brackets)
                    #variables are delimited by space only.
                    #but we have to take care to remove the opening/closing brackets
                    variables = list(filter(lambda x: len(x)>0, schemeword[1:-1].split(' ')))[1:] # [1:] to remove the functionName
                    vIdx = 0
                    sPos = 0
                    ts = copy.deepcopy(schemeword)#its a string, copy will do.......TODO
                    chopped = 0
                    while vIdx < len(variables): # getting the positions of arguments(variables) in schemeword (IS schemeword INPUT or OUTPUT)
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
                if numberOfVariables == 1: #there is a match, depends on whether $ is a function or a argument(variable|number?)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<typing REQUIRED
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
        # print('***************findAllSameLevel:')
        # print(schemeword)
        # print(answers)
        # for s, e, seMatches in answers:
        #     print('matched: ', schemeword[s:e], list(map(lambda t: (t[0], t[1], schemeword[t[0]:t[1]]), seMatches)))
        # print('********************************')
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


        w: string that matched inputPattern
        s: start position of matched on OUTPUT string
        e: end position of matched on OUTPUT string
        ms: start position of matched relative to parent_matched_str on (OUTPUT?INPUT?) string
        me: end position of matched relative to parent_matched_str on (OUTPUT?INPUT?) string

        :param pattern: inputPattern
        :type pattern:
        :param schemeword: original schemeword (input)
        :type schemeword:

        :return:
        :rtype:
        """

        id__data = {}
        nodeId = 0
        current = {
            'w':schemeword, 'id':nodeId, 'pid':None, 'cms':0, 'cme':len(schemeword), 'ms':0, 'me':len(schemeword), 
            'matchIdx':None,
            #'inVar':{}, 'inStatic':{}, 
            'outVars':[], #'outStatic':{}
            #default
            'hin':'', 'vor':''
        }
        stack = [current]
        id__data[nodeId] = current; child__parent = {}
        while len(stack) > 0:
            current = stack.pop()
            word = current['w']
            parentStart = id__data.get(current['id'], {'cms':0})['cms']
            matches = self.findAllSameLevel(pattern, word)
            if current['id'] == 0:
                current['matchIdx'] = 0 if len(matches) > 0 else None
            self.extraGeneratedInputValueForMissingVariables = []; matchIdx=0
            # print('current', current, 'matches', matches, 'parentStart', parentStart); import pdb;pdb.set_trace()
            # print('id: ', current['id'], '#ofMatches:', len(matches))
            if matches: # with leaves
                inVars = []; inputStatics = []
                for matchIdx, (mStart, mEnd, argPoss) in enumerate(matches):
                    # if matchIdx == 0:
                    #     print('nodeId', nodeId, '<<<<<')
                    #     matchedId = nodeId
                    inVarPosition = []
                    # nodeId += 1
                    inVariables = {}; startOfInputStatic = parentStart+current['ms']+mStart; inputStatic = [] # startEndTuples of absolutePosition of inputTemplate excluding substitutedVariables
                    for argIdx, ((inVariable, templatePos), argPos) in enumerate(zip(self.inVariablesAndPos, argPoss)): # this is the inputVariables, we assume argPoss was sorted by argPos[0]
                        #also get the static parts of the inputTemplate
                        # print(mStart, mEnd, '~~~~', inVariable, argPos); import pdb;pdb.set_trace()
                        nodeId += 1;
                        # print('matchIdx:', matchIdx, 'argIdx', argIdx, 'nodeId: ', nodeId)
                        # print('pid: ', current['id'], 'cid: ', nodeId, ' w: ', word[argPos[0]:argPos[1]], ' <<<<<<<<MATCH')
                        if matchIdx == 0 and argIdx == 0:
                            matchedId = nodeId;# mmStart=parentStart+current['ms']+matches[0][0];mmEnd=parentStart+current['ms']+matches[-1][1]
                        dat = {
                            'w':word[argPos[0]:argPos[1]],
                            'id':nodeId,
                            'pid':current['id'],
                            'ms':argPos[0],
                            'me':argPos[1],
                        }
                        stack.append(dat)
                        dat.update({
                            'cms':parentStart+current['ms']+argPos[0], # this is the matched startposition
                            'cme':parentStart+current['ms']+argPos[1]  # this is the matched endposition
                        })
                        inVarPosition.append(((inVariable, templatePos), dat['cms'], dat['cme'], nodeId))
                        inVariables[(inVariable, templatePos)] = dat #==nodeId__rootNonMatches_childId__listOfTupStartPosOffset_i <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO remove
                        inputStatic.append((startOfInputStatic, parentStart+current['ms']+argPos[0]))
                        startOfInputStatic = parentStart+current['ms']+argPos[1]
                        id__data[nodeId] = {
                            # 'w':word[mStart:mEnd],
                            'w':word[argPos[0]:argPos[1]],
                            'ms':mStart, 
                            'me':mEnd, 
                            'id':nodeId, 
                            'pid':current['id'],
                            'cms':parentStart+current['ms'],
                            'cme':parentStart+current['me'],
                            'matchIdx':matchIdx,
                            'inVar':(inVariable, templatePos),
                            'positionInParent':{'matchIdx':matchIdx, 'inVariable':inVariable, 'templatePos':templatePos},
                            #
                            # 'inVar':inVariables,

                            # 'inStatic':dict(zip(self.inStaticsStartEnd, inputStatic)), # tuples from mStart to mEnd, excluding argPoss
                            'outVars':[],
                            # 'outStatic':{}
                        }
                        # child__parent[nodeId] = current['id']
                    if len(argPoss) == 0:# there was a match, but no argument matches => there are no arguments in the inputPattern
                        nodeId += 1
                        if matchIdx == 0:
                            matchedId = nodeId;
                        outValues = self.giveMeNVariableNotInThisList(len(self.outVariables), varList=self.extraGeneratedInputValueForMissingVariables)
                        op = self.outputPattern
                        for outValue, (outVariable, outPos) in reversed(list(zip(outValues, sorted(self.outVariablesAndPos, key=lambda outVarPos: outVarPos[1])))):
                            op = rs.replaceAtPos(op, outPos, outPos+len(outVariable)-1, outValue)
                        id__data[nodeId] = {
                            'w':op,
                            'ms':mStart,
                            'me':mEnd,
                            'id': nodeId,
                            'pid':current['id'],
                            'cms':mStart,
                            'cme':mEnd,
                            'matchIdx':0,# all same template
                            'inVar':(self.schemeword[mStart:mEnd], mStart),
                            # 'inStatic':{},
                            'outVars':[],
                            # 'outStatic':{}
                        }
                        inVarPosition.append(((self.schemeword[mStart:mEnd], mStart), mStart, mEnd, nodeId))
                        inVars.append(inVarPosition)
                        startOfInputStatic = 0 if matchIdx == 0 else matches[matchIdx-1][1]
                        inputStatic.append((startOfInputStatic, mStart))
                        # startOfInputStatic = mEnd
                        inputStatics.append(inputStatic)
                        #if last match, then add it in
                        if matchIdx == len(matches)-1:
                            inputStatics.append([(mEnd, len(self.schemeword))])
                    else:
                        inputStatic.append((startOfInputStatic, parentStart+current['ms']+mEnd))
                        inputStatics.append(dict(zip(self.inStaticsStartEnd, inputStatic)))
                        inVars.append(inVarPosition)
                #for calculatePositions
                id__data[id__data[matchedId]['pid']]['inVars'] = inVars
                # inStatics = []; start = mmStart#id__data[id__data[matchedId]['pid']]['cms']
                # print(inVars)
                # for group in inVars:
                #     for inVar, absoluteVarStart, absoluteVarEnd in group:
                #         inStatics.append((start, absoluteVarStart))
                #         start = absoluteVarEnd
                # inStatics.append((start, mmEnd))#id__data[id__data[matchedId]['pid']]['cme']))
                # id__data[id__data[matchedId]['pid']]['inStatics'] = inStatics
                id__data[id__data[matchedId]['pid']]['inStatics'] = inputStatics
                #for calculatePositions
            else:
                nodeId += 1
                # print('pid: ', current['id'], 'cid: ', nodeId, ' w: ', word, ' <<<<<<<<NOMATCH')
                id__data[nodeId] = {
                    'w':word, 
                    'ms':current['ms'], 
                    'me':current['me'], 
                    'id':nodeId, 
                    'pid':current['id'],
                    'cms':parentStart+current['ms'],
                    'cme':parentStart+current['me'],
                    'matchIdx':None,
                    'inVar':(),
                    # 'inStatic':{},
                    'outVars':[],
                    # 'outStatic':{}
                }
            # print('******')
            # print(matchedId)
            # print('******')
            #####put in the inVars and inStatics
            # id__data[id__data[matchedId]['pid']]['inVars'] = inVars
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
            ##########
            # print('##########')
            # print('parentId: ', v['pid'])
            # print(v['cms'], v['cme'], v['ms'], v['me'], (v['cme']-v['cms']), (v['me']-v['ms']))
            # print('id: ', k, ' s: ', v['s'], ' e: ', v['e'], self.schemeword[v['s']:v['e']], '||| w: ', v['w'], ' same length? ', len(self.schemeword[v['s']:v['e']])==len(v['w']), ' another same length: ', (v['cme']-v['cms'])==(v['me']-v['ms'])); 
            # import pdb;pdb.set_trace()
            # print('##########')
            ##########

        ########################################################
        enclosureTree = {0:[]}
        import bisect
        sortKey = 's'
        for nodeId, data in id__data.items():
            if data['pid'] is not None:
                childIds = enclosureTree.get(data['pid'], [])
                sortList = list(map(lambda idd: id__data[idd][sortKey], childIds))
                sortValue = data[sortKey]
                positionToInsert = bisect.bisect_right(sortList, sortValue)
                childIds.insert(positionToInsert, nodeId)
                enclosureTree[data['pid']] = childIds
                child__parent[nodeId] = data['pid']

        if len(self.variables) == 0:
            # self.pp.pprint(id__data); import pdb;pdb.set_trace()
            for nodeIdx, (nodeId, data) in enumerate(sorted(filter(lambda t: t[0] in child__parent, id__data.items()), key=lambda t: t[0])):
                if nodeId in child__parent:
                    parentId = child__parent[nodeId]
                    vorTuple = id__data[parentId]['inStatics'][nodeIdx][0]
                    id__data[nodeId]['vor'] = self.schemeword[vorTuple[0]:vorTuple[1]]
                    hinTuple = id__data[parentId]['inStatics'][nodeIdx+1][0]
                    id__data[nodeId]['hin'] = self.schemeword[hinTuple[0]:hinTuple[1]]
                    # print('nodeIdx', nodeIdx, 'vorTuple', vorTuple, 'hinTuple', hinTuple);import pdb;pdb.set_trace()
        else:
            for nodeId, data in id__data.items():

                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # if ((data['cme']-data['cms'])!=(data['me']-data['ms'])): # for pid==0, there will always be vor:"(=";  hin:")"
                if data['matchIdx'] is not None:
                    allSiblings = enclosureTree[child__parent[nodeId]] if nodeId in child__parent else [nodeId]
                    #capture the before_match and after_match here, in manipulate, attach it back
                    #if there is more than 1 match?, need to take into account the other matches(allSiblings) on the same level<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    #vor: 
                    positionInSiblingList = allSiblings.index(nodeId)
                    vorNodeId = allSiblings[positionInSiblingList - 1] if positionInSiblingList > 0 else None
                    hinNodeId = allSiblings[positionInSiblingList + 1] if positionInSiblingList < len(allSiblings)-1 else None
                    
                    wholeChildStr = self.schemeword[data['cms']:data['cme']]#including unmatched parts, only vor and hin
                    vorNodeData = id__data.get(vorNodeId, {'me':0}); hinNodeData = id__data.get(hinNodeId, {'ms':len(wholeChildStr)})
                    # print('|', wholeChildStr[vorNodeData['me']:data['ms']], '|'); print('|', wholeChildStr[data['me']:hinNodeData['ms']], '|')
                    data.update({
                        'vor':wholeChildStr[vorNodeData['me']:data['ms']], 
                        'hin':wholeChildStr[data['me']:hinNodeData['ms']]
                    })
                    # v.update({
                    #     'vor':wholeChildStr[:data['ms']], 'hin':wholeChildStr[data['me']:]
                    # })
                else:
                    data.update({
                        'vor':'', 'hin':''
                    })
        ########################################################

        # info(id__data)
        # info(enclosureTree)
        # import pdb;pdb.set_trace()
        # print('findAll*****************************************************************')
        # print(enclosureTree)
        # self.pp.pprint(id__data); import pdb;pdb.set_trace()
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

        # print(variablesPosSansVarnumList)
        #get the (start, end) of pattern(without numbers) without variables, 
        startPos = 0; staticsStartEnd = []; #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        for pos in variablesPosSansVarnumList:
            staticsStartEnd.append((startPos, pos))
            startPos = pos + len('$')
        staticsStartEnd.append((startPos, len(pattern)))
        # print('*******************************')#TODO use this map to actual positions
        # print(staticsStartEnd)
        # print('*******************************')

        return pattern, variables, variablesAndPos, variablesPosSansVarnumList, staticsStartEnd


    def _manipulationPrep(self):
        """

        1. count each variable in inputPattern and outputPattern
        2. if there are variables in outputPattern but not inputPattern, generate values for them

        3. match inVarPos to outVarPos
        """
        #actually these only appears in patterns not(self.patternOnlyVariablesAndSpaces), so might be a bit inefficient... but for readability?
        self.iVars__count = {}
        for var, pos in self.inVariablesAndPos:
            self.iVars__count[var] = self.iVars__count.get(var, 0) + 1
        self.oVars__count = {}
        for var, pos in self.outVariablesAndPos:
            self.oVars__count[var] = self.oVars__count.get(var, 0) + 1
        self.allUniqueVars = set(map(lambda t: t[0], self.inVariablesAndPos)).union(map(lambda t: t[0], self.outVariablesAndPos))

        #0.2 generate variableValues for variables in outPattern but not in inPattern#<<<<<this seems like the only prep needed for manipulate. later parts are for calculating position of changes
        allValuesThatMatched = list(map(lambda data: data['w'], self.id__data.values()))
        # print(allValuesThatMatched)
        if len(self.variables) > 0:
            variableValues = self.giveMeNVariableNotInThisList(len(set(self.outVariables) - set(self.variables)), varList=allValuesThatMatched)
            variableDiffList = list(set(self.outVariables) - set(self.variables))
            outVariables__variableValues = dict(zip(variableDiffList, variableValues))
            allValuesThatMatched += variableValues
            outVariablesPos__variableValues = {}
            # print('outVariables__variableValues', outVariables__variableValues)
            variablePosDiffList = list(filter(lambda t: t[0] in variableDiffList, self.outVariablesAndPos))
            for outVarPos in variablePosDiffList:
                outVariablesPos__variableValues[outVarPos] = {
                    'w':outVariables__variableValues[outVarPos[0]],#<<<<<<<<<<<<fill up the cms, cme for verPosWord
                    # 'cms':,
                    # 'cme':
                }
            #attach that to id__data[inVar] for ids that are matches
            # for nodeId, data in filter(lambda t: t[0] in self.enclosureTree, self.id__data.items()):# does not work for self.patternOnlyVariablesAndSpaces
            # for nodeId, data in filter(lambda t: t[0] != 0, self.id__data.items()):
            #     # print(data)
            #     outVariablesPos__variableValues___new = {}
            #     for outVarPos, variableValues in outVariablesPos__variableValues.items():
            #         variableValues.update({
            #             'cms':data['s'],
            #             'cme':data['e']
            #         })
            #         outVariablesPos__variableValues___new[outVarPos]
            #     data['inVar'].update(outVariablesPos__variableValues)

            # self.inVariablesAndPos += variablePosDiffList


        else:#TODO doesn't give the right variable subscript....<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # variableValues = self.giveMeNVariableNotInThisList(len(set(self.outVariables) - set(self.variables)), varList=allValuesThatMatched)
            # for nodeId, data in filter(lambda t: t[0] in self.enclosureTree, self.id__data.items()):# does not work for self.patternOnlyVariablesAndSpaces
            for nodeId, data in filter(lambda t: t[0] != 0, self.id__data.items()):
                generatedVariableValues = self.giveMeNVariableNotInThisList(len(self.outVariables), varList=allValuesThatMatched)
                generatedVariableValues = list(map(lambda val: {
                    'w':val, #<<<<<<<<<<<<fill up the  ms, me for verPosWord
                    # 'cms':,
                    # 'cme':
                }, generatedVariableValues))
                # print(generatedVariableValues)
                # data['inVar'].update(dict(zip(self.outVariablesAndPos, generatedVariableValues)))
                allValuesThatMatched += generatedVariableValues

            # self.inVariablesAndPos += self.outVariablesAndPos

        #3
        if len(self.variables) == 0:
            # self.inVarPos__outVarPos = dict(zip(sorted(self.inVariablesAndPos, key=lambda t: (t[0], t[1])), sorted(self.outVariablesAndPos, key=lambda t: (t[0], t[1]))))
            self.outVarPos__inVarPos = {}; self.inVarPos__outVarPos = {}
        #match same variables to same variables, sorted by position. If less, repeat the original list of variables
        else:
            inVar__list_inVarPos = {}
            for (inVar, inPos) in self.inVariablesAndPos:
                existing = inVar__list_inVarPos.get(inVar, [])
                existing.append((inVar, inPos))
                inVar__list_inVarPos[inVar] = existing
            outVar__list_outVarPos = {}
            for (outVar, outPos) in self.outVariablesAndPos:
                existing = outVar__list_outVarPos.get(outVar, [])
                existing.append((outVar, outPos))
                outVar__list_outVarPos[outVar] = existing
            # print('inVar__list_inVarPos', inVar__list_inVarPos)
            # print('outVar__list_outVarPos', outVar__list_outVarPos)
            self.outVarPos__inVarPos = {}; self.inVarPos__outVarPos = {}
            for variable in self.allUniqueVars:
                list_inVarPos = inVar__list_inVarPos[variable]
                list_outVarPos = outVar__list_outVarPos[variable]
                if len(list_inVarPos) > len(list_outVarPos):#
                    repetitions = (len(list_inVarPos)+len(list_outVarPos)-1)//len(list_outVarPos)
                    list_outVarPos = (list_outVarPos * repetitions)[:len(list_inVarPos)]
                elif len(list_inVarPos) < len(list_outVarPos):#
                    repetitions = (len(list_outVarPos)+len(list_inVarPos)-1)//len(list_inVarPos)
                    list_inVarPos = (list_inVarPos * repetitions)[:len(list_outVarPos)]
                for inVarPos, outVarPos in zip(list(list_inVarPos), list(list_outVarPos)):
                    if outVarPos not in self.outVarPos__inVarPos: # these matched means that are not removed nor added, only swapped. And we want to swap those that are nearer to the start of the patterns, and remove|add those excess that are further from the patterns
                        self.outVarPos__inVarPos[outVarPos] = inVarPos
                        self.inVarPos__outVarPos[inVarPos] = outVarPos


    def _getGroupIndices(self, nodeId):
        return sorted(list(set(map(lambda childId: self.id__data[childId]['matchIdx'], self.enclosureTree[nodeId]))))

    def _nodeIsMatchedNode(self, nodeId):
        return self._getGroupIndices(nodeId) != [None]

    def manipulate(self, oWord, variables, outputPattern, inputPattern, id__data, enclosureTree, nodeIdsToSkip, existingVariables=None):
        """
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<summarise this in a few words please
        BaseCase: 
            if id__data[nodeId]['matchIdx'] is None:
                return id__data[nodeId]['w']
        RecursiveCase:
            group childIds(nodeId) by id__data[childId]['matchIdx'] -> groups
            totalStr = '''
            for each groupIdx, group in groups
                if childIdx == 0
                    totalStr = vor+match(replaceStrs(childIds), outputTemplate)+hin
                else
                    totalStr += match(replaceStrs(childIds), outputTemplate)+hin
            return totalStr
        """
        # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        self._manipulationPrep();#positionalParent = {}; #relationship where we skip the intermediate_match(variable_node), linking the non-match to match directly
        parent = {};
        def _manipulateRecursive(nodeId):#, parentId):
            #
            # id__data[nodeId]['es'] = 0; id__data[nodeId]['ee'] = None
            #
            #BaseCase # (0) or (1), (0) is normal_case, (1) is inputPattern has no variables
            if id__data[nodeId]['matchIdx'] is None or nodeId not in enclosureTree:
                # print(nodeId, 'BC: ', id__data[nodeId]['w'])
                return id__data[nodeId]['w']
            #RecursiveCase:
            groupIndices = self._getGroupIndices(nodeId)
            # print(groupIndices, '<<<<<<groupIndices')
            #for calculatePositionsOfChanges
            # if parentId is not None:
            #     positionalParent[enclosureTree[nodeId][0]] = parentId

            #for calculatePositionsOfChanges
            if groupIndices == [None]: #_nodeIsMatchedNode
                
                return _manipulateRecursive(enclosureTree[nodeId][0])#, nodeId)#we cannot have more than 1 children with noMatch????
            totalStr = ''; groupOffset = 0; substitutedPatternTotalLen = 0; outVarPositions = []; outputStatics = []
            for groupIdx, groupId in enumerate(groupIndices):#matches in this level
                # print('~~~~~~~~~~~~~~~~~~~~groupId: ', groupId)
                sortedGroupChildIds = sorted(filter(lambda childId: id__data[childId]['matchIdx']==groupId, enclosureTree[nodeId]), key=lambda childId: id__data[childId]['s'])
                inVarPos__replaceStr = {}
                # groupOffset += len(id__data[sortedGroupChildIds[0]]['vor']) if groupIdx == 0 else 0;tempGroupOffset = groupOffset;
                #groupOutVarPositions = []
                for inVarPosIdx, childId in enumerate(sortedGroupChildIds):
                    parent[childId] = nodeId
                    replaceStr = _manipulateRecursive(childId)#, nodeId)
                    # print('pid: ', nodeId, 'cid: ', childId, 'inVar: ', id__data[childId]['inVar'], ' replaceStr: ', replaceStr)
                    inVarPos = id__data[childId]['inVar']
                    inVarPos__replaceStr[inVarPos] = replaceStr
                    #for calculatePositionsOfChanges
                    # outVarPos = self.inVarPos__outVarPos[inVarPos]
                    # # id__data[childId]['outVar'] = outVarPos
                    # print('before, adding es ee to ', enclosureTree[childId][0], ' @ ', nodeId);# import pdb;pdb.set_trace()
                    # startPos = tempGroupOffset+outVarPos[1]; endPos = startPos+len(replaceStr)#needs to be stored in the child of childId<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    # id__data[enclosureTree[childId][0]]['es'] = startPos; id__data[enclosureTree[childId][0]]['ee'] = endPos#PLEASE REMOVE NOT NEEDED<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    # #groupOutVarPositions.append((childId, startPos, endPos))
                    # print('adding es ee to ', enclosureTree[childId][0])
                    # tempGroupOffset += len(replaceStr) - len(outVarPos[0])
                    #for calculatePositionsOfChanges
                #outVarPositions.append(groupOutVarPositions)
                replacement = outputPattern if len(self.inVariablesAndPos) > 0 else self.schemeword
                replacementListVariableAndPos = list(reversed(self.outVariablesAndPos)) if len(self.inVariablesAndPos) > 0 else list(reversed(sorted(map(lambda childId: id__data[childId]['inVar'], enclosureTree[nodeId]), key=lambda t: t[1])))
                if nodeId in nodeIdsToSkip:
                    replacement = inputPattern; replacementListVariableAndPos = list(reversed(self.inVariablesAndPos))

                # print('replacement: ', replacement)
                # print('inVarPos__replaceStr', inVarPos__replaceStr)
                # print('replacementListVariableAndPos', list(replacementListVariableAndPos))
                # import pdb;pdb.set_trace()
                for outVarPos in replacementListVariableAndPos:#outVar can only be calculated here.<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    replaceStr = inVarPos__replaceStr[self.outVarPos__inVarPos.get(outVarPos, outVarPos)]# the default case is when the inputPattern has no variables
                    # print('replacing at: ', outVarPos[1], outVarPos[1]+len(outVarPos[0]), ' with ', replaceStr);
                    replacement = rs.replaceAtPos(replacement, outVarPos[1], outVarPos[1]+len(outVarPos[0]), replaceStr)

                    #for calculatePositionsOfChanges
                    # startPos = tempGroupOffset+outVarPos[1]; endPos = startPos+len(replaceStr)#needs to be stored in the child of childId<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    # groupOutVarPositions.append((outVarPos, startPos, endPos))
                    # tempGroupOffset += len(replaceStr) - len(outVarPos[0])

                    #for calculatePositionsOfChanges
                    #need to capture the new position of the variables in outputPattern
                    # print('replaced String: ', '|'+replacement+'|')
                #for calculatePositionsOfChanges
                # print('list(reversed(replacementListVariableAndPos))', list(reversed(replacementListVariableAndPos)))
                groupOffset += len(id__data[sortedGroupChildIds[0]]['vor']) if groupIdx == 0 else 0;tempGroupOffset = groupOffset;
                # if groupIdx == 0:
                #     id__data[nodeId]['es'] = groupOffset # relativeStart
                groupOutVarPositions = []; outputStatic = []; staticStart = tempGroupOffset if len(variables) > 0 else 0
                # print('init~~~~ staticStart:', staticStart)
                for sortedGroupChildId, outVarPos in enumerate(reversed(replacementListVariableAndPos), 1):
                    replaceStr = inVarPos__replaceStr[self.outVarPos__inVarPos.get(outVarPos, outVarPos)]# the default case is when the inputPattern has no variables
                    
                    startPos = tempGroupOffset+outVarPos[1] if len(variables) >0 else tempGroupOffset
                    endPos = startPos+len(replaceStr)
                    outputStatic.append((staticStart, startPos)); staticStart = endPos
                    groupOutVarPositions.append((outVarPos, startPos, endPos))
                    # print('***');import pdb;pdb.set_trace()
                    tempGroupOffset += len(replaceStr) - len(outVarPos[0]) if len(variables) >0 else len(replaceStr) + len(id__data[sortedGroupChildId]['hin'])
                outVarPositions.append(groupOutVarPositions)
                # outputStatic.append((staticStart, tempGroupOffset))
                # outputStatics.append(outputStatic)
                # id__data[nodeId]['ee'] = tempGroupOffset
                ####
                # substitutedPatternTotalLen += len(replacement)
                # groupOffset += substitutedPatternTotalLen;#substitutedPatternTotalLen = 0

                groupOffset += len(replacement)
                ####
                if len(variables) > 0:
                    outputStatic.append((staticStart, groupOffset))
                    outputStatics.append(dict(zip(self.outStaticsStartEnd, outputStatic)))
                else:
                    pass
                # print('matchId:', groupIdx, outputStatic); import pdb;pdb.set_trace()
                #for calculatePositionsOfChanges
                if groupIdx == 0:
                    replacement = id__data[sortedGroupChildIds[0]]['vor']+replacement+id__data[sortedGroupChildIds[-1]]['hin'] if len(self.inVariablesAndPos) > 0 else replacement
                    # id__data[nodeId]['ee'] = groupOffset
                else:
                    replacement = replacement+id__data[sortedGroupChildIds[-1]]['hin'] if len(self.inVariablesAndPos) > 0 else replacement
                #for calculatePositionsOfChanges
                groupOffset += len(id__data[sortedGroupChildIds[-1]]['hin'])
                #for calculatePositionsOfChanges
                totalStr += replacement
                if len(variables) == 0:
                    outputStatic.append((staticStart, len(totalStr)))
                    outputStatics.append(outputStatic)
                # print('resulting outoutStatics: ', outputStatic); import pdb;pdb.set_trace()
            id__data[nodeId]['outVars'] = outVarPositions
            id__data[nodeId]['outStatics'] = outputStatics
            return totalStr
        outputStr = _manipulateRecursive(0)#, None)
        
        #outVars already in relativePosition, even wrt to group(matches)
        #adding whatever is infront of it in the parent as outVars+self.vor
        for nodeId, data in sorted(filter(lambda t: len(t[1]['outVars']) > 0, id__data.items()), key=lambda t: t[0]):# we assume the bigger the nodeId, the higher in the enclosureTree, a pseudo-DFS
            parentId = parent.get(nodeId)
            if parentId is not None:
                thisOutVarPos = self.inVarPos__outVarPos[data['inVar']]; thePOutVarIdx = None;# thisMatchIdx = data['matchIdx'];
                for pOutVarIdx, ((outVar, outPos), _, _) in enumerate(id__data[parentId]['outVars'][data['matchIdx']]):
                    if thisOutVarPos == (outVar, outPos):
                        thePOutVarIdx = pOutVarIdx
                        break
                #add up everything before id__data[parentId]['outVars'][:data['matchIdx']] and id__data[parentId]['outVars'][data['matchIdx']][:thePOutVarIdx]#this excludes thePOutVarIdx
                offset = id__data[parentId]['outVars'][data['matchIdx']][thePOutVarIdx][1]
                outVar___new = []
                for matchId, group in enumerate(data['outVars']):
                    newGroup = []
                    for (var, outPatternPos), relativeStartPos, relativeEndPos in group:
                        #################################################################
                        # print('adding offset: ', offset, ' shiftOffset: ', shiftOffset, ' totalOffset: ', (offset+shiftOffset), 'to nodeId ', nodeId, ' outVar: ', (var, outPatternPos), 'relativeStartPos', relativeStartPos, 'relativeEndPos', relativeEndPos, '=========')
                        # newGroup.append(((var, outPatternPos), shiftOffset+offset+relativeStartPos, shiftOffset+offset+relativeEndPos))
                        newGroup.append(((var, outPatternPos), offset+relativeStartPos, offset+relativeEndPos))
                        # newGroup.append(((var, outPatternPos), shiftOffset+relativeStartPos, shiftOffset+relativeEndPos))
                    outVar___new.append(newGroup)
                id__data[nodeId]['outVars'] = outVar___new
                #outStatics
                outStatics___new = []
                for matchId, group in enumerate(data['outStatics']):
                    newGroup = []
                    for sStart, sEnd in group.values():
                        newGroup.append((offset+sStart, offset+sEnd))
                    outStatics___new.append(dict(zip(self.outStaticsStartEnd, newGroup)))
                id__data[nodeId]['outStatics'] = outStatics___new

        #special case for len(variables) == 0
        if len(variables) == 0:
            """
            flatten inVars
            """
            new___inVars = []
            for inVarDataList in self.id__data[0]['inVars']:
                new___inVars.append(inVarDataList[0])
            self.id__data[0]['inVars'] = [new___inVars]
            #
            # self.outVarPos__inVarPos = dict(zip(
            #     list(map(lambda l: (l[1], l[2]), self.id__data[0]['outVars'][0])),
            #     list(map(lambda l: (l[1], l[2]), self.id__data[0]['inVars'][0]))
            # ))
            # self.pp.pprint(self.id__data)
            # self.pp.pprint(self.outVarPos__inVarPos)
            # import pdb;pdb.set_trace()

        # #verPosWord calculation: self.outVarPos__inVarPos, need self.inVarPos__outVarPos, then we just have to keep the absolute_position for each match_node?
        # #Variable_matches are in the children of enclosureTree
        # #convert the relativePosition of the new position of the variables in outputPattern
        # #variable change position with match
        # childId__tuple_inVar_inPatternPos_matchId = {}
        # for nodeId, data in sorted(filter(lambda t: len(t[1]['outVars']) > 0, id__data.items()), key=lambda t: t[0]):
        #     #make map
        #     inVarPos__relativePos = {}
        #     for matchId, group in enumerate(data['inVars']):
        #         for (inVar, inPatternPos), inRelativeStartPos, inRelativeEndPos, childId in data['inVars'][matchId]:#_ is the nodeId
        #             inVarPos__relativePos[(inVar, inPatternPos)] = (inRelativeStartPos, inRelativeEndPos)
        #             childId__tuple_inVar_inPatternPos_matchId[childId] = (inVar, inPatternPos, matchId)
        #     id__data[nodeId]['outVarShifts'] = {}
        #     for matchId, group in enumerate(data['outVars']):
        #         for varId, ((var, outPatternPos), outRelativeStartPos, outRelativeEndPos) in enumerate(group):
        #             # inVarPos = self.outVarPos__inVarPos[(var, outPatternPos)]
        #             # (inRelativeStartPos, inRelativeEndPos) = inVarPos__relativePos[inVarPos]
        #             inVar, inPatternPos = self.outVarPos__inVarPos[(var, outPatternPos)]
        #             pid = id__data[nodeId]['pid']
        #             if pid is not None:
        #                 print('pid', pid, 'outVarShifts: ', id__data[pid]['outVarShifts'])
        #                 (pInVar, pInPatternPos, pMatchId) = childId__tuple_inVar_inPatternPos_matchId[nodeId]
        #                 (pOutVar, pOutPatternPos) = self.inVarPos__outVarPos[(pInVar, pInPatternPos)]
        #                 offset = id__data[pid]['outVarShifts'][(pOutVar, pOutPatternPos, pMatchId)]
        #             else:
        #                 offset = 0
        #             #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<should ignore static changes?
        #             #ignore static changes
        #             print('(nodeId, var, outPatternPos, matchId)', (nodeId, var, outPatternPos, matchId),'outPatternPos: ', outPatternPos, ' inPatternPos', inPatternPos, 'diff', outPatternPos - inPatternPos, '???????????????', 'offset: ', offset, 'total:', offset+outPatternPos - inPatternPos)
        #             id__data[nodeId]['outVarShifts'][(var, outPatternPos, matchId)] = offset + outPatternPos - inPatternPos # should only be templateShift, 
        #             # id__data[nodeId]['outVarShifts'][(var, outPatternPos, matchId)] = outPatternPos - inPatternPos
        #             #find corresponding relativeStartPos, relativeEndPos of inputVar,matchId
        # #DFS one more time to get the absolute position of outVar and outStatic, by adding matchParent's offset<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # id__data[0]['outStatics'] = list(map(lambda lis: dict(zip(self.outStaticsStartEnd, lis)), id__data[0]['outStatics']))
        # for nodeId, data in sorted(filter(lambda t: len(t[1]['outVars']) > 0, id__data.items()), key=lambda t: t[0]):# we assume the bigger the nodeId, the higher in the enclosureTree, a pseudo-DFS
        #     parentId = parent.get(nodeId)
        #     # shiftOffset = id__data[parentId]['outVarShifts'][(var, outPatternPos, matchId)]#should add parent's ()
        #     if parentId is not None:
        #         print('parentId: ', parentId, ' outVarShifts: ', id__data[parentId]['outVarShifts'])
        #         (pInVar, pInPatternPos, pMatchId) = childId__tuple_inVar_inPatternPos_matchId[nodeId]
        #         (pOutVar, pOutPatternPos) = self.inVarPos__outVarPos[(pInVar, pInPatternPos)]
        #         shiftOffset = id__data[parentId]['outVarShifts'][(pOutVar, pOutPatternPos, pMatchId)]#THIS is just a recalculation<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<please remove
        #         print('shiftOffset: ', shiftOffset)
        #         offset = id__data[parentId]['outVars'][0][0][1]#these are relativeOutvariablePositions by level<<<<< do we still need the shiftOffset for test__idealNested__addition?, 
        #         #or we can just take id__data[parentId]['outVars'][0][0][1] - id__data[parentId]['inVars'][0][0][1]
        #         outVar___new = []
        #         for matchId, group in enumerate(data['outVars']):
        #             newGroup = []
        #             for (var, outPatternPos), relativeStartPos, relativeEndPos in group:
        #                 #################################################################
        #                 print('adding offset: ', offset, ' shiftOffset: ', shiftOffset, ' totalOffset: ', (offset+shiftOffset), 'to nodeId ', nodeId, ' outVar: ', (var, outPatternPos), 'relativeStartPos', relativeStartPos, 'relativeEndPos', relativeEndPos, '=========')
        #                 newGroup.append(((var, outPatternPos), shiftOffset+offset+relativeStartPos, shiftOffset+offset+relativeEndPos))
        #                 # newGroup.append(((var, outPatternPos), offset+relativeStartPos, offset+relativeEndPos))
        #                 # newGroup.append(((var, outPatternPos), shiftOffset+relativeStartPos, shiftOffset+relativeEndPos))
        #             outVar___new.append(newGroup)
        #         id__data[nodeId]['outVars'] = outVar___new
        #         #outStatics
        #         outStatics___new = []
        #         for matchId, group in enumerate(data['outStatics']):
        #             newGroup = []
        #             for sStart, sEnd in group:
        #                 newGroup.append((offset+sStart, offset+sEnd))
        #             outStatics___new.append(dict(zip(self.outStaticsStartEnd, newGroup)))
        #         id__data[nodeId]['outStatics'] = outStatics___new





        # positionalEnclosureTree = {}
        # for child, parent in positionalParent.items():
        #     existing = positionalEnclosureTree.get(parent, [])
        #     existing.append(child)
        #     positionalEnclosureTree[parent] = existing
        #####
        # import pprint; pp = pprint.PrettyPrinter(indent=4)
        # print('positionalParent*****')
        # pp.pprint(positionalParent)
        # pp.pprint(positionalEnclosureTree)
        # print('positionalParent*****')
        #####

        # for parent, children in sorted(positionalEnclosureTree.items(), key=lambda t: t[0]):# we assume the bigger the nodeId, the higher in the enclosureTree, a pseudo-DFS
        #     for childId in children:
        #         id__data[childId]['es'] += id__data[enclosureTree[parent][0]]['es']
        #         id__data[childId]['ee'] += id__data[enclosureTree[parent][0]]['es']
        #         print('adding ', id__data[enclosureTree[parent][0]]['es'], ' to nodeId: ', childId, id__data[childId]['es'], id__data[childId]['ee'], '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        self.getPositionsOfChanges()

        return outputStr


    def getPositionsOfChanges(self):
        """
# a nodeId is matched only if all its children have matchId, children_of_enclosureTree are inputVariables, we can get a corresponding set of outputVariables


        1. if the inputTemplate has no variables, then the whole inputTemplate will be removed, and replaced by the whole outputTemplate


        2. VARIABLE CHANGES
            0. more|less of a variable when comparing inputPattern to outputPattern
                for each match_node
            1. positional shifts of a variable when comparing inputPattern to outputPattern

        3. NON_VARIABLE CHANGES # could be done in prepareRawPattern?
        """
        self.verPosWord = []
        #1
        # if len(self.variables) == 0:
        #     self.pp.pprint(self.id__data)
        #     import pdb;pdb.set_trace()


        #2
        allVariablePossRemoved = []; allVariablePossAdded = []
        for variable in self.allUniqueVars:
            inxCount = self.iVars__count.get(variable, 0); outCount = self.oVars__count.get(variable, 0)
            # print('~~~~~~~~~~~~~~~~~~~~~ inxCount: ', inxCount, ' outCount: ', outCount)
            if inxCount > outCount: #0.0.1|0.1, we assume that the last variable were removed
                variablesRemoved = sorted(filter(lambda t: t[0]==variable, self.inVariablesAndPos), key=lambda t: t[1])[outCount-inxCount:]
                allVariablePossRemoved+=variablesRemoved
                #need the relative_position_of_id_data; lengths of its previousArguments_of_inputPattern, to get its actual position 
            elif outCount > inxCount: #0.0.0|0.2, we assume that the last variable was added
                variablesAdded = sorted(filter(lambda t: t[0]==variable, self.outVariablesAndPos), key=lambda t: t[1])[inxCount-outCount:]
                allVariablePossAdded+=variablesAdded
        matchedNodeIds = sorted(list(filter(lambda nodeId: self._nodeIsMatchedNode(nodeId), self.enclosureTree.keys())))#we assume that larger the nodeId the larger
        # print('allVariablePossRemoved', allVariablePossRemoved); print('self.inVariablesAndPos', self.inVariablesAndPos)
        # print('allVariablePossAdded', allVariablePossAdded); print('self.outVariablesAndPos', self.outVariablesAndPos)
        # print('matchedNodeIds', matchedNodeIds)

        #2.0
        for nodeId, data in filter(lambda t: t[0] in matchedNodeIds, self.id__data.items()):
            # print(nodeId)
            #
            for group in data['inVars']:
                for inVarPos, absStart, absEnd, cNodeId in group:
                    if inVarPos in allVariablePossRemoved and cNodeId not in self.nodeIdsToSkip:
                        self.verPosWord.append({#could have included information on which variable of the outputTemplate
                        'd': 'r', 'e': absEnd, 'n': cNodeId, 's': absStart, 't': 'n', 'v': inVarPos[0], 'w': self.id__data[self.enclosureTree[nodeId][0]]['w']
                        })
            #
            for group in data['outVars']:
                for outVarPos, absStart, absEnd in group:
                    if outVarPos in allVariablePossAdded and nodeId not in self.nodeIdsToSkip:
                        self.verPosWord.append({#could have included information on which variable of the inputTemplate
                        'd': 'a', 'e': absEnd, 'n': nodeId, #added nodeId is from the outputString, which is not directly on the enclosureTree
                        's': absStart, 't': 'n', 'v': outVarPos[0], 'w': infoData['w']
                        })


        #2.1
        #
        # import pprint; pp = pprint.PrettyPrinter(indent=4)
        # print('self.outVarPos__inVarPos')
        # pp.pprint(self.outVarPos__inVarPos)
        #

        for nodeId, data in filter(lambda t: t[0] in matchedNodeIds, self.id__data.items()):
            #
            tuple_inVarPos_groupIdx__absIn = {}
            for groupIdx, group in enumerate(data['inVars']):
                # print('')
                for inVarPos, absInStart, absInEnd, cNodeId in group:
                    # if cNodeId in self.nodeIdsToSkip:# this part is just to calculate the tuple_inVarPos_groupIdx__absIn, SO CANNOT SKIP!
                    #     continue
                    # print('$$$ cNodeId ', cNodeId)
                    tuple_inVarPos_groupIdx__absIn[(inVarPos, groupIdx)] = {'absInStart':absInStart, 'absInEnd':absInEnd, 'cNodeId':cNodeId, 'w':self.id__data[cNodeId]['w']}
            #
            #
            # pp.pprint(tuple_inVarPos_groupIdx__absIn); 


            #
            for groupIdx, group in enumerate(data['outVars']):
                for outVarPos, absOutStart, absOutEnd in group:
                    if nodeId in self.nodeIdsToSkip:
                        continue
                    inVarPos = self.outVarPos__inVarPos.get(outVarPos, outVarPos)
                    absIn = tuple_inVarPos_groupIdx__absIn[(inVarPos, groupIdx)]
                    #
                    # print('in: ', (inVarPos, groupIdx))
                    # print('out: ', (outVarPos, groupIdx))
                    # print('getting ', (inVarPos, groupIdx), ' from map, got: ', absIn)

                    # import pdb;pdb.set_trace()
                    #
                    self.verPosWord.append({
                        'd': 'e', 'e': absOutStart, 'n': absIn['cNodeId'], 's': absIn['absInStart'], 't': 'p', 'v': inVarPos[0], 
                        'w': absIn['w'] # should be the same as outDatum['w']
                        })

        #3
        # print('self.iUnmatchedFrags', self.iUnmatchedFrags)
        # print('self.oUnmatchedFrags', self.oUnmatchedFrags)
        def findOffsetInRangeDictionary(point, rangeDictionary):
            for (oStart, oEnd), (eStart, eEnd) in rangeDictionary.items():
                if oStart <= point and point < oEnd:
                    return eStart - oStart
        if len(self.variables) > 0:
            for nodeId, data in filter(lambda t: t[0] in matchedNodeIds and t[0] not in self.nodeIdsToSkip, self.id__data.items()):
                for unmatchedInfo in self.iUnmatchedFrags:
                    if unmatchedInfo['w'].strip() == '$':
                        continue
                    for rangeDictionary in data['inStatics']:
                        # print(rangeDictionary)
                        offset = findOffsetInRangeDictionary(unmatchedInfo['s'], rangeDictionary)
                        self.verPosWord.append({
                            'd': 'r', 'e': offset+unmatchedInfo['e'], 'n': nodeId, 's': offset+unmatchedInfo['s'], 't': 's', 'v': None, 'w': unmatchedInfo['w']
                        })

                for unmatchedInfo in self.oUnmatchedFrags:
                    if unmatchedInfo['w'].strip() == '$':
                        continue
                    for rangeDictionary in data['outStatics']:
                        # print(rangeDictionary)
                        offset = findOffsetInRangeDictionary(unmatchedInfo['s'], rangeDictionary)
                        self.verPosWord.append({
                            'd': 'a', 'e': offset+unmatchedInfo['e'], 'n': nodeId, 's': offset+unmatchedInfo['s'], 't': 's', 'v': None, 'w': unmatchedInfo['w']
                        })






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