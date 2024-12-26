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
        self.inputPattern, self.variables, self.inVariablesAndPos = self.prepareRawPattern(self.rawInputPattern)
        self.outputPattern, self.outVariables, self.outVariablesAndPos = self.prepareRawPattern(self.rawOutputPattern)
        self.calledBuildEnclosure = False
        self.subsitutedOutputGrammar = self.outputPattern
        self.additionalReplacementStrForVariablesDict = {}

        import pprint
        self.pp = pprint.PrettyPrinter(indent=4)


    def buildEnclosureTree(self, schemeword):
        self.schemeword = schemeword
        self.id__data, self.enclosureTree = self.findAll(self.inputPattern, self.schemeword)
        self.calledBuildEnclosure = True
        # this inputPattern is not applicable to this schemeword. Note that, if there are no variables in inputPattern, it might still be a match
        # import pdb;pdb.set_trace()
        self.noMatches = (len(self.id__data) == 2) and (self.id__data[0]['w']==self.id__data[1]['w'])


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
            # import pdb;pdb.set_trace()
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
        import bisect
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
        #variablesPosList = []
        # for m in re.finditer('(\$)', pattern):
        #     variablesPosList.append((m.start(), m.end(), m.group()))
        #rawVariables__variables = dict(zip(rawVariablesPosList, variablesPosList)) # attach to self, if we need this
        #variables__rawVariables = dict(zip(variablesPosList, rawVariablesPosList)) # attach to self, if we need this
        
        return pattern, variables, variablesAndPos


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
            if id__data[nodeId]['pid'] is None:#it was not matched to any variables, or inputPattern has no variables :)
                rWord = copy.deepcopy(oWord)
                if len(variables) == 0: #no variables, then we need to replace with outputPattern instead of replaceStr
                    #but first we need to replace the variables in outputPattern first... with variable/s that in not in equation.
                    #and that is handled by Manipulate :)
                    replaceStrs = [self.subsitutedOutputGrammar] * len(replaceStrs)

                # print('no match')
                # import pdb;pdb.set_trace()
                childId__replacedStr = dict(zip(childIds, replaceStrs))
                for childId in reversed(childIds): #have to replace from the back, else, the frontPositions might shift.
                    childData = id__data[childId]
                    rWord = rs.replaceAtPos(rWord, childData['s'], childData['e'], childId__replacedStr[childId])
                return rWord
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
                    multiple = len(childIds)//len(variables)
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
                    for childId in reversed(childIds):
                        data = id__data[childId]
                        # import pdb;pdb.set_trace()
                        template = rs.replaceAtPos(template, data['s']- parentStartOffset, data['e']- parentStartOffset, op)
                    return template
                else:
                    ##################check if there is a match to all variables
                    variables__valuesPos = {} # dict to check if variable has more than 1 value mapped
                    #check if same variable has been mapped to more than 1 value <<< this is not well-defined
                    for varIdx in range(0, len(self.variables)):
                        #very convienent that replaceStrs(values) and self.variables are already aligned in list order :)
                        variable, pos = self.inVariablesAndPos[varIdx]
                        value = replaceStrs[varIdx]
                        existingValuePos = variables__valuesPos.get(variable, (None, None))
                        existingValue, existingPos = existingValuePos
                        if existingValue is not None and existingValue != value: 
                            #more than one value was assigned to variable and those values are different
                            raise Exception(f'{existingValue} was assigned to {variable} at position {existingPos}, and now {value} is being assigned to the same {variable} again. Not well-defined')
                        variables__valuesPos[variable] = (value, pos)
                    ##################
                    if nodeId in nodeIdsToSkip:
                        op = copy.deepcopy(inputPattern)
                    else:
                        op = copy.deepcopy(outputPattern)
                    # import pdb;pdb.set_trace()
                    #there might be more unique variables in outputPattern than variables in inputPattern, see #logarithmtest.test__hin4__configTest
                    # if len(set(self.outVariables)) > len(set(self.variables)):
                    #     #then we need to create variables, which should be handled by manipulate.py?
                    #     missingVariables = list(set(self.outVariables) - set(self.variables))
                    #     varList = self.variables
                    #match&not_just_variable_and_space&less_variable_available
                    currentVariablesToReplacement = dict(zip(variables, replaceStrs))
                    currentVariablesToReplacement.update(self.additionalReplacementStrForVariablesDict)
                    for variable, replaceStr in currentVariablesToReplacement.items(): # childId are in the order of the variables in inputPattern
                        op = op.replace(variable, replaceStr)
                    # print('match')
                    # import pdb;pdb.set_trace()
                    return op
        ##############
        # print('*******')
        # import pdb;pdb.set_trace()
        ##############
        manipulatedSchemeEquationStr = _recursiveManipulate(0) # root__nodeId is always 0
        return manipulatedSchemeEquationStr


