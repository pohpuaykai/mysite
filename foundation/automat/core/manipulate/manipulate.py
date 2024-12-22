import re

class Manipulate:
    """
    parent class of all patterns

    #~ DRAFT ~#
    input:
    1. Equation


    """

    def __init__(self, equation, verbose):
        self.eq = equation
        self.verbose = verbose
        #make and store the scheme string
        self.schemeStr = equation.toString('scheme')
        #process each rawRegex from child
        # self.manipulationDict = {}
        for d in self.rawRegexes: # should i process everything at once, i might not need everything
            if d['type'] == 'regex':
                for direction, infoDict in d.items():
                    print(infoDict)

                    if direction in ['type']: # ignore
                        continue
                    inputRegexStr = infoDict['scheme']
                    outputRegexStr = infoDict['return']
                    outputVariables = self._getVariablesFromRegexStr(outputRegexStr)
                    if len(outputVariables) == 0: # output totally does not depend on input
                        inputVariables = None
                        inputTransformedRegexStr = None
                    else:
                        inputVariables = self._getVariablesFromRegexStr(inputRegexStr)
                        inputTransformedRegexStr = self._processRawRegexFromChildClass(inputRegexStr)
                    infoDict.update({
                        'inputVariables':inputVariables,
                        'propreRegex':inputTransformedRegexStr,
                        'outputVariables':outputVariables
                    })

    def _getVariablesFromRegexStr(self, regexStr):
        #count the number of variables in regexStr, variables must be consecutive
        self.startPosAndvariableStr = [{'start':match.start(), 'vastr':match.group()} for match in re.finditer('\\$\d+', regexStr)]
        self.startPosAndvariableStr = sorted(self.startPosAndvariableStr, key=lambda d: d['start'])
        self.variables = list(set([d['vastr'] for d in self.startPosAndvariableStr]))
        if self.verbose:
            print(self.variables)
        return self.variables

    def _processRawRegexFromChildClass(self, regexStr):
        transformedRegexStr = self._custom_escape(regexStr)
        for variableStr in self.variables: # depends on _getVariablesFromRegexStr for self.variables
            transformedRegexStr = transformedRegexStr.replace(variableStr, '(.+)')
        if self.verbose:
            print(transformedRegexStr)
            return transformedRegexStr

    def _custom_escape(self, s, ignore_char="$"): #TODO refactor to common?
        # Temporarily replace the character to ignore with a unique placeholder
        placeholder = "__PLACEHOLDER__"
        s = s.replace(ignore_char, placeholder)
        
        # Escape the string using re.escape
        escaped = re.escape(s)
        
        # Restore the ignored character
        return escaped.replace(re.escape(placeholder), ignore_char)

    def _extract_matches(self, pattern, string):
        """
        TODO refactor to common?


        """
        self.matches = []
        matchId = 0
        stack = [{'s':string, 'p':0, 'id':matchId, 'parentId':None}]
        while len(stack) > 0:
            currentObj = stack.pop()
            currentStr = currentObj['s']
            currentId = currentObj['id']
            matchings = list(re.finditer(pattern, currentStr))
            if len(matchings) > 0:
                for m in matchings:
                    matchedStr = m.group()
                    for variable in m.groups():
                        matchId += 1
                        startPos__ofSubstring = matchedStr.index(variable)
                        startPos__ofEntire = startPos__ofSubstring+currentObj['p']
                        self.matches.append({
                            'v':variable,
                            'se':startPos__ofEntire,
                            'ss':startPos__ofSubstring,
                            'id':matchId,
                            'parentId': currentId
                        })
                        stack.append({'s':variable, 'p':startPos__ofEntire, 'id':matchId, 'parentId':currentId})
        return self.matches


    # def returnHasVariables(self):
    #     self.rawRegexes

    def applicable(self, propreRegex):
        """
        #~ DRAFT ~#
        check if equation is manipulatable with this pattern
        """
        self._extract_matches(propreRegex, self.schemeStr)
        return len(self.matches) > 0 # no matches cannot apply manipulation

    def apply(self, propreRegex, outputRegexStr):
        """
        #~ DRAFT ~#
        return manipulated equation
        """
        if propreRegex is None:
            return outputRegexStr # output does not depend on input variables, no manipulation needed.
        if self.applicable(propreRegex): # here we have matches
            if self.verbose:
                import pprint
                pp = pprint.PrettyPrinter(indent=4)
                pp.pprint(self.matches)
            
            #parentId=0 is the original str. need id, to argumentNumber and parentId
            parentId__idStartPoss = {}
            id__infoDict = {}
            for d in self.matches:
                selfId = d['id']
                infoDict={} # clone d myself...
                for k, v in d.items():
                    infoDict[k] = v
                id__infoDict[selfId] = infoDict
                #####
                childIds = parentId__idStartPoss.get(d['parentId'], [])
                childIds.append({'id':d['id'], 'relStartPos':d['ss']}) # binaryInsert TODO will be more efficient
                parentId__idStartPoss[d['parentId']] = childIds
            #sort relStartPos, to match back to $0, $1, .... (TODO if binaryInsert, then no need to sort)
            sorted__parentId__idStartPoss = {}
            for parentId, childDicts in parentId__idStartPoss.items():
                sortedChildDicts = sorted(childDicts, key=lambda d: d['relStartPos'])
                sorted__parentId__idStartPoss[parentId] = sortedChildDicts
            parentId__idStartPoss = sorted__parentId__idStartPoss
            if self.verbose:
                pp.pprint(parentId__idStartPoss)
            #TODO this is actually EnclosureTree... refactor?
            enclosureTree = {}
            newChildId__infoDict = {}
            for parentId, childDicts in parentId__idStartPoss.items():#now we just zip, the parentId__idStartPoss and self.startPosAndvariableStr
                childIds = []
                for idx, patternVarDict in enumerate(self.startPosAndvariableStr):
                    childId = childDicts[idx]['id'] # idx is position on childDicts
                    childInfoDict = id__infoDict[childId]
                    childInfoDict.update(patternVarDict)
                    childIds.append(childId)
                    newChildId__infoDict[childId] = childInfoDict
                enclosureTree[parentId] = childIds
            
            if self.verbose:
                pp.pprint(enclosureTree)
            
            import copy
            #replace the strings from leaves, by-recursion
            def _recursiveReplaceVariables(nodeId):
                if nodeId not in enclosureTree: # it is a leaf
                    infoDict = newChildId__infoDict[nodeId]
                    return infoDict['v']
                childIds = enclosureTree[nodeId]
                variableToReplacementStr = {}
                for childId in childIds:
                    child = newChildId__infoDict[childId]
                    variableToReplacementStr[child['vastr']]=_recursiveReplaceVariables(child['id'])
                returnSchemeRegexCopy = copy.deepcopy(outputRegexStr)
                for variable, replaceStr in variableToReplacementStr.items():
                    returnSchemeRegexCopy = returnSchemeRegexCopy.replace(variable, replaceStr)
                return returnSchemeRegexCopy
            manipulatedSchemeEquation = _recursiveReplaceVariables(0) # the original formula, always have id=0
            if self.verbose:
                print(manipulatedSchemeEquation)
            return manipulatedSchemeEquation