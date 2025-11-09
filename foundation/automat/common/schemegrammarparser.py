import sys


class SchemeGrammarParser:
    variableStartMarker = '$'#'"Why did you choose $ as mark?", asked Winnie_the_Pooh. "Because this will never have anything to do with money, so, i will never have any variable collision"'
    """There are 3 MODEs
    MODE0: iPattern has no variables

    MODE1: iPattern has no statics, only variables and spaces. there must be no space before and after iPattern, each variable must be delimited from the next variable by exactly 1 space

    MODE2: iPattern has both statics and variables

    """


    def __init__(self, iPattern, oPattern, calculateSchemeNodeChanges=True, verbose=False):
        """
        This method is supposed to 
        0. get information about iPattern (what MODE is it?)
        1. get information about iPattern, and oPattern (how many variables, positions of the variables in pattern)
        2. get information about iPattern, and oPattern (static positions in pattern)
        3. match iPattern and oPattern (variables, for generating oStr)
        4. match iPattern and oPattern (statics = LCSS)


        :param iPattern:
        :type iPattern:
        :param oPattern:
        :type oPattern:
        """
        self.verbose = verbose; self.calculateSchemeNodeChanges = calculateSchemeNodeChanges
        import pprint
        self.pp = pprint.PrettyPrinter(indent=4)
        
        self.newEnclosureNodeCounter = -1
        self.allTakenNums = None # for when output has less variables than input, and we need to create

        self.iPattern = iPattern
        self.oPattern = oPattern
        #0
        # self.getMode()
        self.mode = SchemeGrammarParser.getMode(self.iPattern)
        #1
        self.oPatternSansNum, self.oUniqueVariables, self.oSortedVariablesAndPosition, self.oSortedVariablesAndPositionSansNum = self.getVariablesAndPosition(self.oPattern)
        self.iPatternSansNum, self.iUniqueVariables, self.iSortedVariablesAndPosition, self.iSortedVariablesAndPositionSansNum = self.getVariablesAndPosition(self.iPattern) #need for prepValsForExtraOVarsForEachMatch
        self.oStaticPatternStartEndPositionSansNum = self.getStatics(self.oSortedVariablesAndPositionSansNum, self.oPatternSansNum) # can you check if this is correct for MODE 1?
        self.iStaticPatternStartEndPositionSansNum = self.getStatics(self.iSortedVariablesAndPositionSansNum, self.iPatternSansNum)

        from foundation.automat.parser.sorte.schemeparser import Schemeparser# prevent circular_import
        # self.iSchemeparser = Schemeparser(equationStr=self.iPattern)
        self.iSchemeparser = Schemeparser(equationStr=self.iPatternSansNum)
        self.ast___ip, self.functionsD___ip, self.variablesD___ip, self.primitives___ip, self.totalNodeCount___ip, self.startPos__nodeId___ip = self.iSchemeparser._parse() # if this raises, then it is not a valid MODE2
        
        # self.oSchemeparser = Schemeparser(equationStr=self.oPattern)
        self.oSchemeparser = Schemeparser(equationStr=self.oPatternSansNum)
        self.ast___op, self.functionsD___op, self.variablesD___op, self.primitives___op, self.totalNodeCount___op, self.startPos__nodeId___op = self.oSchemeparser._parse()
        
        # if self.mode in [1, 2]:
            #2
            #3
        if self.mode in [2]:
            self.nodeStartPos__nodeEndPos___ip, self.level__nodeStartPos___sorted___ip, self.nodeStartPos__level___ip, self.nodeId__entityStartPos___ip = self.iSchemeparser._getLevelingInformation()
            # print('self.nodeStartPos__level___ip'); print(self.nodeStartPos__level___ip)
            #4
        self.matchIOPatterns()


    @classmethod
    def getMode(cls, iPattern):
        mode = None
        if SchemeGrammarParser.variableStartMarker not in iPattern:
            mode = 0
        else:#check for MODE1
            #after splitting by $ should only contain space and numbers
            MODE1 = True
            from foundation.automat.common.checker import Booler
            for part in iPattern.split(SchemeGrammarParser.variableStartMarker):
                if len(part) > 0 and not Booler.isNum(part):
                    MODE1 = False
                    break
            if MODE1:
                #check for bad MODE1,
                #no space before or after iPattern
                if iPattern.startswith(' '):
                    raise Exception('There must be no space at the start of iPattern')
                if iPattern.endswith(' '):
                    raise Exception('There must be no space at the end of iPattern')
                #exactly 1 space between each variable
                partsBySpace = iPattern.split(' ') #hardcoding?
                numberOfSpaces = len(list(filter(lambda part: len(part)==0, partsBySpace)))
                numberOfVariables = len(list(filter(lambda part: len(part)>0, partsBySpace)))
                if numberOfVariables-1!=numberOfSpaces:
                    raise Exception("There must be 1 space between eaceh variable")
                mode = 1
            else:#check for mode2, must be able to be passed by schemeParser... TODO
                mode = 2
        return mode

    def getVariablesAndPosition(self, rawPattern):
        """
        patternSansNum

        :returns:
            - patternSansNum -
            - uniqueVariables -
            - sortedVariablesAndPosition -
            - sortedVariablesAndPositionSansNum - 
        :rtype:
        """
        import re
        import bisect # TODO repeated imports REFACTOR?
        variables = []
        variablesAndPos = []
        for m in re.finditer('(\$\d+)', rawPattern):
            t = (m.group(), m.start())
            posToInsert = bisect.bisect_left(variablesAndPos, t[1], key=lambda x: x[1]) # to insert in order of startPosition
            variablesAndPos.insert(posToInsert, t)
        variables = list(map(lambda t: t[0], variablesAndPos))
        # import pdb;pdb.set_trace()
        pattern = re.sub(r'\$\d+', '$', rawPattern) # remove the numbers
        variablesPosSansVarnumList = []
        for m in re.finditer('(\$)', pattern):
            variablesPosSansVarnumList.append(m.start())
        variablesPosSansVarnumList = list(zip(variables, variablesPosSansVarnumList))

        return pattern, sorted(list(set(variables))), variablesAndPos, variablesPosSansVarnumList

    def getStatics(self, variablesPosSansVarnumList, pattern):
        startPos = 0; staticsStartEnd = []; #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        for _, pos in variablesPosSansVarnumList:
            staticsStartEnd.append((startPos, pos))
            startPos = pos + len('$')
        staticsStartEnd.append((startPos, len(pattern)))
        return staticsStartEnd

    def mapIOVariables(self):
        """
        Gets iVarPos__oVarPos [used for schemeNodeChangeLog, for checking if there are variables from iPattern that are being removed] & 
        oVarPos__iVarPos, used for generateOStr
        """
        from copy import deepcopy

        ioUniqueVariables = set(self.iUniqueVariables).intersection(set(self.oUniqueVariables)) #intersection because if there are variables either not in iVars or not in oVars, then they cannot be mapped across IO
        iVar__list_iVarPos = {}
        for (iVar, iPos) in self.iSortedVariablesAndPositionSansNum:
            existing = iVar__list_iVarPos.get(iVar, [])
            existing.append((iVar, iPos))
            iVar__list_iVarPos[iVar] = existing
        oVar__list_oVarPos = {}
        for (oVar, oPos) in self.oSortedVariablesAndPositionSansNum:
            existing = oVar__list_oVarPos.get(oVar, [])
            existing.append((oVar, oPos))
            oVar__list_oVarPos[oVar] = existing
        for variable in ioUniqueVariables:
            list_iVarPos = sorted(iVar__list_iVarPos.get(variable), key=lambda t: t[1])#sort by position
            list_oVarPos = sorted(oVar__list_oVarPos.get(variable), key=lambda t: t[1])#sort by position
            list_oVarPos_noRepeats = deepcopy(list_oVarPos)
            if list_iVarPos is not None and list_oVarPos is not None:
                if len(list_iVarPos) > len(list_oVarPos):
                    repetitions = (len(list_iVarPos)+len(list_oVarPos)-1)//len(list_oVarPos)
                    list_oVarPos = (list_oVarPos * repetitions)[:len(list_iVarPos)]
                elif len(list_iVarPos) < len(list_oVarPos):
                    repetitions = (len(list_oVarPos)+len(list_iVarPos)-1)//len(list_iVarPos)
                    list_iVarPos = (list_iVarPos * repetitions)[:len(list_oVarPos)]
                # print('zip(list(list_iVarPos), list(list_oVarPos))', list(zip(list(list_iVarPos), list(list_oVarPos)))); import pdb;pdb.set_trace()

                for iVarPos, oVarPos in zip(list(list_iVarPos), list(list_oVarPos)):
                    if oVarPos not in self.oVarPos__iVarPos:
                        self.oVarPos__iVarPos[oVarPos] = iVarPos
                for iVarPos, oVarPos in zip(list(list_iVarPos), list(list_oVarPos_noRepeats)):
                    if iVarPos not in self.iVarPos__oVarPos:
                        self.iVarPos__oVarPos[iVarPos] = oVarPos
                # print('self.oVarPos__iVarPos', self.oVarPos__iVarPos); print('self.iVarPos__oVarPos', self.iVarPos__oVarPos); import pdb;pdb.set_trace()

    def matchIOPatterns(self): # this is patternChanges in old norse
        # from foundation.automat.common.longestcommonsubsequence import LongestCommonSubsequence
        from foundation.automat.parser.sorte.schemeparser import Schemeparser# prevent circular_import
        """
        This is to track static changes between iPattern and oPattern

        it should output
        staticRanges__list_startPosInioPattern for addition, removal, edition
        this only use the counts for each schemeLabel
        if there is more schemeLabel in iPattern than in oPattern, match the nearest of the same schemeLabel (edition), then those that are left in iPattern, are removed
        if there is more schemeLabel in oPattern than in iPattern, match the nearest of the same schemeLabel (edition), then those that are left in oPattern, are 

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
        # self.iStaticIdx__sortedList_tuple_labelStartPos_labelEndPos_type = dict(map(lambda staticIdx: (staticIdx, []), range(0, len(self.iSortedVariablesAndPositionSansNum))))
        # self.oStaticIdx__sortedList_tuple_labelStartPos_labelEndPos_type = dict(map(lambda staticIdx: (staticIdx, []), range(0, len(self.oSortedVariablesAndPositionSansNum))))

        # self.iStaticIdx__sortedList_tuple_labelStartPos_labelEndPos_type = {}#used by the defeckted verPosWord, remove and change to iTuple_patternLabelStartEndPos__oTuple_patternLabelStartEndPos
        # self.oStaticIdx__sortedList_tuple_labelStartPos_labelEndPos_type = {}#used by the defeckted verPosWord, remove and change to oTuple_patternLabelStartEndPos__iTuple_patternLabelStartEndPos
        #those with no matches in iPattern or oPattern, not needed here, ...
        self.iTuple_patternLabelStartEndPos__oTuple_patternLabelStartEndPos_oStaticIdx = {}#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
        self.oTuple_patternLabelStartEndPos__iTuple_patternLabelStartEndPos_iStaticIdx = {}#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO

        def compareCountDict(iLabel__count, oLabel__count, iLabel__sortedList_tuple_startPos_endPos_nodeId, oLabel__sortedList_tuple_startPos_endPos_nodeId):
            """
            also need the startEndPos of each segment of static of iPattern and oPattern
            iLabel__count is the number
            """
            iLabels___set = set(iLabel__count.keys()); oLabels___set = set(oLabel__count.keys())
            commonLabels___set = iLabels___set.intersection(oLabels___set)
            commonLabel__oMinusICount = dict(map(lambda commonLabel: (commonLabel, oLabel__count[commonLabel]-iLabel__count[commonLabel]), commonLabels___set))

            for commonLabel, oMinusICount in commonLabel__oMinusICount.items():
                oZipList = oLabel__sortedList_tuple_startPos_endPos_nodeId[commonLabel]
                iZipList = iLabel__sortedList_tuple_startPos_endPos_nodeId[commonLabel]
                if oMinusICount > 0:#more O than I
                    oZipList = oZipList[:oMinusICount]
                elif oMinusICount < 0: #more I than O
                    iZipList = iZipList[:-oMinusICount]


                def zipStaticRegionsAndCommonLabels(commonLabels, staticRegions):
                    result = []
                    commonLabelsIdx = 0; staticRegionsIdx = 0
                    while commonLabelsIdx < len(commonLabels) and staticRegionsIdx < len(staticRegions):
                        labelStartPos, labelEndPos, nodeId = commonLabels[min(commonLabelsIdx, len(commonLabels)-1)]
                        staticIdx = min(staticRegionsIdx, len(staticRegions)-1)
                        staticPatternStartPos, staticPatternEndPos = staticRegions[staticIdx]
                        if staticPatternStartPos <= labelStartPos and labelEndPos <= staticPatternEndPos:
                            # result.append((labelStartPos, labelEndPos, nodeId, staticIdx))
                            result.append((labelStartPos, labelEndPos, staticIdx))
                            commonLabelsIdx += 1
                        elif staticPatternEndPos <= labelEndPos:
                            staticRegionsIdx += 1
                        elif labelEndPos <= staticPatternEndPos:
                            commonLabelsIdx += 1
                        else:#this should not happend
                            raise Exception("")
                    return result

                oZipListWithOStaticIdx = zipStaticRegionsAndCommonLabels(oZipList, self.oStaticPatternStartEndPositionSansNum)
                iZipListWithIStaticIdx = zipStaticRegionsAndCommonLabels(iZipList, self.iStaticPatternStartEndPositionSansNum)

                self.iTuple_patternLabelStartEndPos__oTuple_patternLabelStartEndPos_oStaticIdx.update(dict(zip(
                    list(map(lambda t: (t[0], t[1]), iZipList)), 
                    oZipListWithOStaticIdx
                )))
                self.oTuple_patternLabelStartEndPos__iTuple_patternLabelStartEndPos_iStaticIdx.update(dict(zip(
                    list(map(lambda t: (t[0], t[1]), oZipList)), 
                    iZipListWithIStaticIdx
                )))
                
                


        def getLabel__sortedList_tuple_startPos_endPos_nodeId(startPos__nodeId, nodeId__len, theStr):
            label__list_tuple_startPos_endPos_nodeId = {}
            for startPos, nodeId in startPos__nodeId.items():
                leng = nodeId__len[nodeId]
                label = theStr[startPos: startPos+leng]
                existing = label__list_tuple_startPos_endPos_nodeId.get(label, [])
                existing.append((startPos, startPos+leng, nodeId))
                label__list_tuple_startPos_endPos_nodeId[label] = existing
                # print('label__list_tuple_startPos_endPos_nodeId', label__list_tuple_startPos_endPos_nodeId); import pdb;pdb.set_trace()
            label__sortedList_tuple_startPos_endPos_nodeId = dict(map(lambda s: (s, []), label__list_tuple_startPos_endPos_nodeId.keys()))
            for label, list_tuple_startPos_endPos_nodeId in label__list_tuple_startPos_endPos_nodeId.items():
                label__sortedList_tuple_startPos_endPos_nodeId[label] = sorted(list_tuple_startPos_endPos_nodeId, key=lambda t: t[0])
            return label__sortedList_tuple_startPos_endPos_nodeId


        allLabel__count___ip = {}
        allLabel__count___ip.update(self.functionsD___ip);
        allLabel__count___ip.update(self.variablesD___ip);
        allLabel__count___ip.update(self.primitives___ip)#are these all the labels?

        allLabel__count___op = {}
        allLabel__count___op.update(self.functionsD___op);
        allLabel__count___op.update(self.variablesD___op);
        allLabel__count___op.update(self.primitives___op)#are these all the labels?

        iNodeId__labelLen = self.iSchemeparser._getLabelLength()
        oNodeId__labelLen = self.oSchemeparser._getLabelLength()
        # print('self.startPos__nodeId___ip', self.startPos__nodeId___ip)
        # print('iNodeId__labelLen', iNodeId__labelLen)
        # print('self.iPatternSansNum', self.iPatternSansNum); import pdb;pdb.set_trace()
        iLabel__sortedList_tuple_startPos_endPos_nodeId = getLabel__sortedList_tuple_startPos_endPos_nodeId(self.startPos__nodeId___ip, iNodeId__labelLen, self.iPatternSansNum)
        
        # print('self.startPos__nodeId___op', self.startPos__nodeId___op)
        # print('oNodeId__labelLen', oNodeId__labelLen)
        # print('self.oPatternSansNum', self.oPatternSansNum); import pdb;pdb.set_trace()
        oLabel__sortedList_tuple_startPos_endPos_nodeId = getLabel__sortedList_tuple_startPos_endPos_nodeId(self.startPos__nodeId___op, oNodeId__labelLen, self.oPatternSansNum)
        # print('iLabel__sortedList_tuple_startPos_endPos_nodeId')
        # print(iLabel__sortedList_tuple_startPos_endPos_nodeId)
        # print('oLabel__sortedList_tuple_startPos_endPos_nodeId')
        # print(oLabel__sortedList_tuple_startPos_endPos_nodeId)
        compareCountDict(
            allLabel__count___ip, 
            allLabel__count___op, 
            iLabel__sortedList_tuple_startPos_endPos_nodeId, 
            oLabel__sortedList_tuple_startPos_endPos_nodeId
        )




    #make a "buildEnclosureTree" wrapper for this<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< also need to change Recommend.py & Manipulate.py
    def matchIPattern(self, iStr, startPos__nodeId={}):#this is equivalent to buildEnclosureTree, iStr is equivalent to schemeword
        """
        gets all the schemeInformation about iStr. Mainly for skipNode because skipNode needs it, and all 3 MODEs use skipNode
        MODE0 does not use anymore information from schemeInformation
        MODE1 uses 0.ast___iStr 1.nodeId__len___iStr 2. startPos portion of startPos__nodeId
        MODE2 uses 0.nodeId__len___iStr 1.getLevelingInformation

        generate vals for variables in oPattern but not in iPattern (for generating oStr)

        :param iStr: string to do the matching with iPattern
        :type iStr:

        :param startPos__nodeId: user_given_mapping_of_startPos_to_nodeId
        :type startPos__nodeId:

        :param nodeIdsToSkip: list of nodeIds (according to the user_given_mapping_of_startPos_to_nodeId, so if there is no user_given_mapping_of_startPos_to_nodeId), then this does not work.
        Usecase for this is, when some parts of the Equation matches iPattern, but we do not want to apply the oPattern, because it does not help with solving
        :type nodeIdsToSkip:

        :param variableMinArgs: variable_to_minNumberOfArgs matching
        matched variable must have minNumberOfArgs, in order for the replacement with outputPattern to happen
        constants - without brackets, are 0NumberOfArgs
        any variables with brackets (a schemeFunction) - just count the number of arguments
        :type variableMinArgs: dict

        :param variableMaxArgs: variable_to_maxNumberOfArgs matching
        matched variable must have maxNumberOfArgs, in order for the replacement with outputPattern to happen
        :type variableMaxArgs: dict
        """
        from foundation.automat.parser.sorte.schemeparser import Schemeparser# prevent circular_import
        self.iStr = iStr;
        self.schemeparser___iStr = Schemeparser(equationStr=self.iStr)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<refactor the others so we do not call schemeparser on iStr again
        self.ast___iStr, functionsD___iStr, variablesD___iStr, primitives___iStr, totalNodeCount___iStr, self.startPos__nodeId___iStr = self.schemeparser___iStr._parse()
        self.nodeId__len___iStr = self.schemeparser___iStr.nodeId__len
        self.nodeStartPos__nodeEndPos___iStr, self.level__nodeStartPos___iStr, self.nodeStartPos__level___iStr, self.nodeId__entityStartPos___iStr = self.schemeparser___iStr._getLevelingInformation()
        self.userProvided_startPos__nodeId = False
        if startPos__nodeId: # user provided startPos__nodeId, will be named startPos__nodeId__iStr to reduce confusion and we do not need our own startPos__nodeId if user already provided it
            self.startPos__nodeId___iStr___OLD = self.startPos__nodeId___iStr
            self.startPos__nodeId___iStr = startPos__nodeId; 
            #needs to remap the : to userNodeIds in startPos__nodeId
            #0. ast___iStr
            #1. nodeId__len___iStr
            #BUT for now non of the functions need it so we just keep the old startPos__nodeIde___iStr for future use here
            self.nodeId__entityStartPos___iStr = self.renameUserGivenSchemeNodeId(self.nodeId__entityStartPos___iStr)
            #
            self.userProvided_startPos__nodeId = True#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<this flag was never used????
        self.newNodeCounter = max(map(lambda t: t[1], self.startPos__nodeId___iStr.items())) # iSchemeparser is the iPattern, not iStr


        if self.mode == 0:
            self.matchIPattern___MODE0()
        elif self.mode == 1:
            self.matchIPattern___MODE1()
        elif self.mode == 2:
            self.matchIPattern___MODE2()
        else:
            raise Exception('undefined mode: '+str(self.mode))

        # print('self.iEnclosureTree', self.iEnclosureTree); import pdb;pdb.set_trace()
        # if len(self.iEnclosureTree) == 0: # there are no matches#<<<<<<<<<<<<<<<<<<<<<<<<<this criteria is bad for detecting no match. perhaps each MODE should have its own noMatch<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        noOfMatches = 0
        if 'noOfMatches' in self.iId__data[0]:
            noOfMatches = self.iId__data[0]['noOfMatches'] # we assume rootId is always 0
        # print('are there matches?', noOfMatches); import pdb;pdb.set_trace()
        if noOfMatches == 0:
            self.oStr = self.iStr
            self.startPos__nodeId___oStr = self.startPos__nodeId___iStr
            self.schemeNodeChangeLog = []
            self.noMatches = True
        else:
            # print('noOfMatches', noOfMatches, '')
            self.mapBetweenEnclosureAndScheme()#should map between enclosureId and schemeId, so that user can use both mapping happily, also give make_startPos__argsCount : self.entityStartPos__schemeEntityNodeId
            self.make_startPos__argsCount() # this make data for self.skipNode, the data is startPos__argsCount, where we map each iVar to the number of args it contains
            
            self.noMatches = False

    def matchIPattern___MODE0(self):
        """
        take the rawInputPattern, and search for positions using REGEX,
        replace the rawOutputPattern's variables with newly created variables, call it filledOutputPattern
        replace with positions with rawInputPattern with filledOutputPattern

        iStatics are the iPattern matches -  for verWordPos easy calculation
        there are no iVars...
        iVors and iHins are those unmatched parts. Mental image:

        vor|iPattern|hin=vor|iPattern|hin=vor|iPattern|hin
            ~match~~         ~match~~         ~match~~    

        since there are no variables in iPattern, the enclosureTree will only have 2 levels, the first match, and then its regex children (which are considered the iVars for later calculations)

        This method should only produce enclosureTree and id__data [should only contain iVars iStatics(empty) iVors iHins for root. 's', 'e', 'w']

        """
        # self.iEnclosureTree = {0:[]};
        self.iEnclosureTree = {}
        iStatics = []; iVors = []; iHins = []
        import re
        escapedInputPattern = re.escape(self.iPattern)
        #list_tuple_startPos_endPos___sorted are all the matches|iStatics|enclosureChildren, and will be stored and used later as such
        list_tuple_startPos_endPos___sorted = sorted(list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(escapedInputPattern, self.iStr))), key=lambda t: t[0])
        
        self.iId__data = {0:{'noOfMatches':len(list_tuple_startPos_endPos___sorted), 'matchIdx':0, 's':0, 'e':len(self.iStr), 'vars':[]}}
        # iVors.append([(0, list_tuple_startPos_endPos___sorted[0][0])]); prevHinVorStart = list_tuple_startPos_endPos___sorted[0][1]
        if len(list_tuple_startPos_endPos___sorted) > 0:
            self.iEnclosureTree = {0:[]};
        # else:#<<<<<<<<noMatch<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        for idx, (startPos, endPos, group) in enumerate(list_tuple_startPos_endPos___sorted):
            nodeId = idx+1
            self.iEnclosureTree[0].append(nodeId)
            iStatics.append([(startPos, endPos)]) # each match is 1 static
            if idx == 0:
                iVors.append((0, startPos))
            else:
                prevIdx = idx-1; prevEndPos = list_tuple_startPos_endPos___sorted[prevIdx][1]
                iVors.append((prevEndPos, startPos))
                iHins.append((prevEndPos, startPos))
            self.iId__data[nodeId] = {'noOfMatches':0, 's':startPos, 'e':endPos, 'w':self.iPattern, 'id':nodeId, 'matchIdx':idx}
        #capture the straggler
        iHins.append((list_tuple_startPos_endPos___sorted[-1][1], len(self.iStr)))
        self.iId__data[0]['statics'] = iStatics
        self.iId__data[0]['vors'] = iVors
        self.iId__data[0]['hins'] = iHins


    def matchIPattern___MODE1(self):
        # print('MODE1********************************')
        """ mental image:
        There should be no static except for the space between variables, because static is defined as nonvariables in the inputPattern and outputPattern
        This is for 1 enclosureId:
        vor|$0 $0 $1 $2 $0 $0 $1 $2 $0 $0 $1 $2|hin=vor
            ~~~match~~~ ~~~match~~~ ~~~match~~~
        The vor and hin are delimited by s___parent and e___parent, meaning that there can be a lot of schemeNodes in the vor and hin, but there is at least one schemeNode
        validNonOverlappingMatches are sorted (by schemeStartPosition children), 


        HOW?
        traverse the iEnclosureTree(each node is a match), with queue
        make sliding window of children, in order to get validMatchesWithPos (matches that do not contradict in $variables)
        then out_of validMatchesWithPos, we choose those nonOverlapping
        then, we use nonOverlapping to find hin & vor. (iStatic are spaces only)


        ####
        ##########put all these thoughts into comments????????
        iPattern $0 $1 $2
        (igrpg (uhdrf 1 3 5) (uhdfg 1 3 5) (udrfg 1 3 5))

        what does this match?
        are [(uhdrf 1 3 5),(uhdfg 1 3 5),(udrfg 1 3 5)] also matches? if so what is hin and vor?
        are [(1 3 5),(1 3 5),(1 3 5)] also matches? if so what is hin and vor?







        So0,
        schemeWord: (= a b)
        iPattern: $0
        oPattern: (^ $0 1)
        ((^ = 1) (^ a 1) (^ b 1))

        so1
        (^ (= a b) 1) # this makes sense in subscripts of summation|production|indiction? but it seems like only in subscripts? and sometimes we do make swaps in index of summation|production|indication?
        #when does this not make sense?
        #for non_function, when does this make sense? always makes sense? only for this (iPattern, oPattern)?
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        FOR NOW
        0. always fit a non_function(no brackets) [any (iPattern, oPattern)]
        1. else fits the most number of consistent arguments? of any schemeFunction
        -0. what is hin_vor? should include function_name because we are putting them back
        -1. because, we are just putting hin_vor back, the original schemeword does not matter, when extracting hin_vor
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        any other STRANGE cases?

        more than 1 variable? (more general)


        also, do you want to match the function? What use_case? or would that be more general? but the function should be different than its arguments?
        so, to be more general, do you want a function swapper? seperate_or_getrannt?
        ####


        calls schemeparser.parse on schemeword to get ast, map startEndPos and substrings from schemeword to the nodeId of ast
        then make slidingWindow of length=len(#_of_variables_of_pattern), on ast, to produce enclosureTree (matches), if there are not enough args on ast, then its no match
        
        after matching, we should check_for_consistency_of_variables, so in the match all $0 should be equals, ...
        inputPattern: '$0 $0 $1 $1', so in the sliding window the first2 matches must be equals, and the last2 matches must be equals

        after check_for_consistency_of_variables

        regarding inVars:
        because there is only 1 variable in inputPattern, so each match in this nodeId, should only have 1 tuple in each list, and each match is in a list.
        so, if there are 2 variables in inputPattern, there will be 2 tuples in each match|list
        in general, if there are n variables in inputPattern, there will be n tuples in each match|list

        regarding inStatics:
        if inputPattern has only 1 variable, then there should only have 2Statics, in general if there are n variables in inputPattern, then there should be (n+1)Statics for each match in this nodeId
        """
        #make the enclosureTree from schemeTree first, so that it is easier to reason with
        #some schemeTree arguments might not fit the inputPattern, or has less arguments than there are variables in inputPattern
        #so we need to do those 2 filters on the schemeTree to get the enclosureTree.
        #
        noOfVariables = self.iPattern.count('$')
        if not self.iStr.startswith('(') and noOfVariables == 1: # this is a non_function and only 1 variable in self.iPattern, then we have a match
            self.iId__data = {}
            self.iId__data[0] = {
                'noOfMatches':1,
                'statics':[], # iPattern having only 1 var does not have spaces, and so does not have static
                'vars':[[(0, len(self.iStr))]],
                'hins':[(len(self.iStr), len(self.iStr))],#whole self.iStr is a match, so there are no hins
                'vors':[(0, 0)],#whole self.iStr is a match, so there are no vors
                's':0,
                'e':len(self.iStr),
                'w':self.iStr,
                'matchIdx':0,
                'pid':None
            }
            self.iId__data[1] = {
                # 'id':enclosureTreeId,
                'noOfMatches':0,
                's':0,
                'e':len(self.iStr),
                'w':self.iStr,
                'matchIdx':1,
                'pid':0
            }
            self.iEnclosureTree = {0:[1]}
        else:
        #

            def makeSlidingWindowMatches(childNodes, windowLen):
                matches = []
                for offset in range(0, len(childNodes)-windowLen+1):
                    matches.append(childNodes[offset:offset+windowLen])
                return matches
            nodeId__startPos = dict(map(lambda t: (t[1], t[0]), self.startPos__nodeId___iStr.items()))
            def getStartPosition(nodeId):
                sp = nodeId__startPos[nodeId]
                if sp>0 and self.iStr[sp-1]=='(':
                    return sp-len('(')
                return sp
            # nodeId__len = self.schemeparser___iStr.nodeId__len # is len the entire length? for schemeFunctions, is it inclusive of brackets
            enclosureTreeId = self.getEnclosureNodeId(); self.iEnclosureTree = {enclosureTreeId:[]}; self.iId__data = {enclosureTreeId:{}}
            queue = [{'schemeNode':self.schemeparser___iStr.rootOfTree, 'enclosureId':enclosureTreeId}]; enclosureTreeId += 1
            while len(queue) > 0:
                cN = queue.pop(0)
                (parentSchemeLabel, parentSchemeId) = cN['schemeNode']; parentEnclosureId = cN['enclosureId']
                children = self.ast___iStr.get((parentSchemeLabel, parentSchemeId), [])
                children = sorted(children, key=lambda child: getStartPosition(child[1]))
                if len(children) >= noOfVariables:# we can do a match#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    matches = makeSlidingWindowMatches(children, noOfVariables)
                    #need to do var__val matching, to check for inconsistency before we can declare this as a enclosureTreeNodeId?
                    validMatchesWithPos = []
                    for matchIdx, match in enumerate(matches):
                        firstSchemeNodeId = match[0][1];
                        schemeStartPos = getStartPosition(firstSchemeNodeId);
                        var__val = {}; consistent = True
                        zipped = list(zip(self.iSortedVariablesAndPosition, match)); zipped__len = len(zipped)
                        matchWithPos = []
                        for idx, (inVarPos, (schemeLabel, schemeNodeId)) in enumerate(zipped):#match is a list of schemeNodeId
                            var_i, patternInVarStartPos = inVarPos; 
                            schemeStartPos = getStartPosition(schemeNodeId); schemeEndPos = schemeStartPos+self.nodeId__len___iStr[schemeNodeId]# if nodeId__startPos maps schemeFunction like () to the position_of_openRoundBracket, then it is right, if nodeId__startPos maps schemeFunction like () to the position_of_openRoundBracket+1, then it is wrong
                            matchWithPos.append({'inVarPos':inVarPos, 'schemeStartPos':schemeStartPos, 'schemeEndPos':schemeEndPos, 'schemeLabel':schemeLabel, 'schemeNodeId':schemeNodeId})
                            #for consistency matching
                            if var_i in var__val:
                                matchedVal = schemeword[schemeStartPos:schemeEndPos]
                                if matchedVal != var__val[var_i]:
                                    consistent = False
                                    break
                                var__val[var_i] = matchedVal
                            #
                            # for capturing statics
                            if idx != zipped__len-1:#we add a static after each variable (which is just a space), except for the last variable, after which there is no space
                                (_, patternInVarStartPos___next), (_, schemeNodeId___next) = zipped[idx+1]
                        if consistent: #then we keep this match, its inStatic and inVar in validMatches
                            validMatchesWithPos.append(matchWithPos)
                    # if len(validMatches) > 0:
                    if len(validMatchesWithPos) > 0:#this method is just a filter
                        #only get the most number of validMatches that are nonOverlapping
                        lastEndPos = -1#for checking overlap, since we are doing GreedyParadigm, we will always take the first validMatches
                        validNonOverlappingMatchesWithPos = [];
                        # for matchIdx, match in enumerate(validMatches):
                        for matchIdx, match in enumerate(validMatchesWithPos):#each match is a dict with 'inVarPos':inVarPos, 'schemeStartPos':schemeStartPos, 'schemeEndPos':schemeEndPos, 'schemeLabel':schemeLabel, 'schemeNodeId':schemeNodeId
                            schemeStartPos = match[0]['schemeStartPos']
                            if lastEndPos <= schemeStartPos:
                                #capture
                                validNonOverlappingMatchesWithPos.append(match)
                                #update lastEndPos
                                schemeEndPos = match[-1]['schemeEndPos']
                                lastEndPos = schemeEndPos
                        #
                        if len(validNonOverlappingMatchesWithPos) > 0:
                            """ mental image:
                            There should be no static except for the space between variables, because static is defined as nonvariables in the inputPattern and outputPattern
                            This is for 1 enclosureId:
                            vor|$0 $0 $1 $2 $0 $0 $1 $2 $0 $0 $1 $2|hin=vor
                                ~~~match~~~ ~~~match~~~ ~~~match~~~
                            The vor and hin are delimited by s___parent and e___parent, meaning that there can be a lot of schemeNodes in the vor and hin, but there is at least one schemeNode
                            validNonOverlappingMatches are sorted (by schemeStartPosition children), 
                            """
                            #here each match is a new enclosureTreeId
                            s___parent = getStartPosition(parentSchemeId); e___parent = s___parent+self.nodeId__len___iStr[parentSchemeId]; # also used to get vorhin 
                            list_existingChild = self.iEnclosureTree.get(parentEnclosureId, []); 
                            #getting the vor
                            vorStartPos = s___parent; vorEndPos = validNonOverlappingMatchesWithPos[0][0]['schemeStartPos']
                            hinStartPos = validNonOverlappingMatchesWithPos[-1][-1]['schemeEndPos'];hinEndPos = e___parent
                            iVars = []; iStatics = []; iVors = []; iHins = [];
                            iVors.append((vorStartPos, vorEndPos))
                            for matchIdx, match in enumerate(validNonOverlappingMatchesWithPos):#each match is a dict with 'inVarPos':inVarPos, 'schemeStartPos':schemeStartPos, 'schemeEndPos':schemeEndPos, 'schemeLabel':schemeLabel, 'schemeNodeId':schemeNodeId
                                enclosureTreeId = self.getEnclosureNodeId()
                                list_existingChild.append(enclosureTreeId)
                                #also capture the iVar & iStatic
                                iVar = []; iStatic = []; staticStartPos = vorEndPos
                                #need to put children_attached_with_enclosureTreeId back into the queue
                                for varIdx, d in enumerate(match): # each d is a variable in the iPattern
                                    queue.append({'schemeNode':(d['schemeLabel'], d['schemeNodeId']), 'enclosureId':enclosureTreeId}) # there will not be a childSchemeId with 2 different enclosureTreeId, because matches are nonOverlapping.
                                    iVar.append((d['schemeStartPos'], d['schemeEndPos']))
                                    if varIdx != len(match)-1:#static are not at the start&end of iPattern, so we take the end of each var to the start of each var as the static, which should be a single space
                                        nextD = match[varIdx-1]
                                        iStatic.append((d['schemeEndPos'], nextD['schemeStartPos']))
                                #if iVars is not consistent, iStatic cannot be appended also<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                # if self.variablesConsistent(iVar):
                                iVars.append(iVar); iStatics.append(iStatic)
                                s = iVars[matchIdx][0][0]; #s is the start of inVars
                                e = iVars[matchIdx][-1][-1]; # e is the end of inVars
                                if enclosureTreeId in self.iId__data:# might be a parent too so has some answers
                                    self.iId__data[enclosureTreeId].update({
                                        # 'id':enclosureTreeId,
                                        's':s,
                                        'e':e,
                                        'w':self.iStr[s:e],
                                        'matchIdx':matchIdx,
                                        'pid':parentEnclosureId
                                    })
                                else:#this is totally new
                                    self.iId__data[enclosureTreeId] = {
                                        # 'id':enclosureTreeId,
                                        'noOfMatches':0,
                                        's':s,
                                        'e':e,
                                        'w':self.iStr[s:e],
                                        'matchIdx':matchIdx,
                                        'pid':parentEnclosureId
                                    }
                            iHins.append((hinStartPos, hinEndPos))
                            self.iEnclosureTree[parentEnclosureId] = list_existingChild

                            self.iId__data[parentEnclosureId] = {
                                # 'id':parentEnclosureId,
                                'noOfMatches':len(iVars),
                                'statics':iStatics, # this should contain all the spaces between each variable in the inputPattern
                                'vars':iVars,
                                'hins':iHins,
                                'vors':iVors,
                                's':s___parent,
                                'e':e___parent,
                                'w':self.iStr[s:e],
                            }
                            #
                            #update self.iId__data too
                        else:# all valid matches, overlap, i am not sure how this can happen?
                            for (childSchemeLabel, childSchemeId) in children:
                                queue.append({'schemeNode':(childSchemeLabel, childSchemeId), 'enclosureId':parentEnclosureId})

                    else:# only have inconsistent matches, all matches have some variables that disagree on values matched
                        for (childSchemeLabel, childSchemeId) in children:
                            queue.append({'schemeNode':(childSchemeLabel, childSchemeId), 'enclosureId':parentEnclosureId})

                else:#not enough schemeArgs to match inputPatternVariables
                    for (childSchemeLabel, childSchemeId) in children:
                        queue.append({'schemeNode':(childSchemeLabel, childSchemeId), 'enclosureId':parentEnclosureId})
            #calculate__startPos__nodeId can be done here<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        return self.iId__data, self.iEnclosureTree # TODO do not have to return here

    def matchIPattern___MODE2(self):
        """
        The mental image is like this:

        #vor inStatic $0 inStatic $1...inStatic hin=vor inStatic $0 inStatic $1...inStatic hin=vor... inStatic $0 inStatic $1... inStatic hin
             ~~~~~~~~~~~~~~MATCH~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~MATCH~~~~~~~~~~~~~~            ~~~~~~~~~~~~~~~~MATCH~~~~~~~~~~~~~~
        
        0. parse the iStr with SchemeParser

        1. segment the iPattern by variables.
        2. use index to find each segment, in order, and according to schemeStartPositions
        3. between each matched_segment is the variable (so that each variable is schemeCompliant)
        4. for each variable, goto 0
        """
        # self.schemeparser___iStr = Schemeparser(equationStr=self.iStr)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<check skipNode for code_duplication, it seems that nodeStartPos__nodeEndPos is also needed for skipNode
        # ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = self.schemeparser___iStr._parse()
        # nodeId__len = self.schemeparser___iStr.nodeId__len
        # nodeStartPos__nodeEndPos, level__nodeStartPos, nodeStartPos__level, _ = self.schemeparser___iStr._getLevelingInformation()
        #
        # def getAllSchemeLevelCompliantPositionAfter(currentPosition, currentLevel):#currentPosition should be after a scheme_compliant_variable
        #     print('currentLevel', currentLevel)
        #     print('self.level__nodeStartPos___iStr', self.level__nodeStartPos___iStr)
        #     return list(filter(lambda startPos: startPos>=currentPosition, self.level__nodeStartPos___iStr[currentLevel]))


        def getiPatternLevelCompliantPositionAt(currentPosition, currentLevel):
            return list(filter(lambda startPos: startPos>=currentPosition, self.level__nodeStartPos___iStr[currentLevel]))[0]


        # self.noMatches = True #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<then if found any valid matches, then set to false
        self.iId__data = {}; self.iEnclosureTree = {}
        def recursiveMatch(absoluteStartPos, absoluteEndPos, parentNodeId): # recursiveMatch is called on each matchedVariable and also the initial_string
            noMatch = False
            iPatternSegments = self.iPatternSansNum.split(SchemeGrammarParser.variableStartMarker); currentPointerPosition = absoluteStartPos;
            # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            # print('iPatternSegments', iPatternSegments)

            iVars = []; iStatics = []; iHins = []; iVors = []; noOfMatches = 0; vorStartPointer = absoluteStartPos
            while not noMatch and currentPointerPosition < len(self.iStr):#there might be more than 1 matches on s
                iVar = []; iStatic = [];
                matchedSchemeLevel = None; #all matches on this enclosureNode, might not be on the same schemeLevel, so we have to None matchedSchemeLevel on every match
                segmentIdx = 0
                while segmentIdx < len(iPatternSegments):
                # for segmentIdx, ips in enumerate(iPatternSegments):
                    ips = iPatternSegments[segmentIdx]
                    if segmentIdx == 0:
                        try:
                            # print('looking for ips', ' in ', '|'+self.iStr[currentPointerPosition:absoluteEndPos]+'|')
                            staticStartPos = currentPointerPosition+self.iStr[currentPointerPosition:absoluteEndPos].index(ips)#s already chopped, no need to chop again
                            #here there is match
                            segmentIdx+=1
                        except:
                            noMatch = True
                            # import pdb; pdb.set_trace()
                            break
                        #vorHin Capture#if match was reseted, vorHin should also be reseted<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        # vorHin = (currentPointerPosition, staticStartPos)
                        vorHin = (vorStartPointer, staticStartPos)
                        if len(iVors) == 0:
                            iVors.append(vorHin)
                        else: # middle vorHin, add to both
                            iVors.append(vorHin); iHins.append(vorHin)
                        iStatic.append((staticStartPos, staticStartPos+len(ips))) #capture
                        currentPointerPosition = staticStartPos + len(ips) # also =startOfIVar
                        vorStartPointer = currentPointerPosition
                        matchedSchemeLevel = self.nodeStartPos__level___iStr[staticStartPos]#this is schemeLevel=0 in iPattern
                    else: # we have to find the next scheme_level_compliant position, that also matches ips, because ONLY variables must be scheme_level_compliant, and in this MODE2, segments do not have to be scheme_level_compliant

                        iVarIdxInISortedVariablesAndPosition = len(iVar)
                        # var___i, iPos = self.iSortedVariablesAndPosition[iVarIdxInISortedVariablesAndPosition]
                        var___i, iPos = self.iSortedVariablesAndPositionSansNum[iVarIdxInISortedVariablesAndPosition]
                        # print('self.iSortedVariablesAndPositionSansNum', self.iSortedVariablesAndPositionSansNum); import pdb;pdb.set_trace()
                        iVarLevel = self.nodeStartPos__level___ip[iPos] # level in iPattern, need to convert iPatternSchemeLevel to iStrSchemeLevel
                        
                        schemeEndPos = currentPointerPosition
                        #
                        # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        # print('ips: ', '|'+ips+'|')
                        # print('iPos', iPos)
                        # print("self.nodeStartPos__level___ip", self.nodeStartPos__level___ip)
                        # print('currentPointerPosition', currentPointerPosition)#IS currentPointerPosition always before a schemeCompliantVariableOfIPattern?
                        # print('matchedSchemeLevel', matchedSchemeLevel)
                        # print('iVarLevel', iVarLevel)
                        # print('schemeEndPos', schemeEndPos)
                        #
                        schemeStartPos = getiPatternLevelCompliantPositionAt(currentPointerPosition, matchedSchemeLevel+iVarLevel)# matchedSchemeLevel=schemeLevel_in_iStr=schemeLevel0_in_iPattern, iVarLevel=schemeLevel_in_iPattern_of_iVar, so to get the schemeLevel_of_iVar_in_iStr=matchedSchemeLevel+(iVarLevel-0)
                        schemeEndPos = self.nodeStartPos__nodeEndPos___iStr[schemeStartPos]
                        if self.iStr[schemeEndPos:schemeEndPos+len(ips)] == ips:
                            staticStartPos = schemeStartPos
                            iVar.append((schemeStartPos, schemeEndPos)) # capture
                            iStatic.append((schemeEndPos, schemeEndPos+len(ips))) # capture
                            currentPointerPosition = schemeEndPos + len(ips)
                            vorStartPointer = currentPointerPosition
                            # print('ips match found =) at currentPointerPosition', currentPointerPosition, 'schemeStartPos: ', schemeStartPos, 'schemeEndPos: ', schemeEndPos); 
                            # import pdb;pdb.set_trace()
                            segmentIdx += 1
                        else:
                            #did not match the whole of list_schemeLevelCompliantStartPos ?
                            #so we should currentPointer should move to the end of list_schemeLevelCompliantStartPos?
                            # print('restarting............ currentPointerPosition: ', currentPointerPosition, 'schemeStartPos: ', schemeStartPos)
                            currentPointerPosition = schemeStartPos#+len(ips) # +len(ips) is to keep the currentPointerPosition always at the start of schemeCompliantVariableOfIPattern
                            segmentIdx = 0 # if all the list_schemeLevelCompliantStartPos (which are all the valid are no match), then we cannot continue with this matching anymore
                            noMatch = True
                            iVors.pop(); 
                            if len(iHins) > 0:
                                iHins.pop()
                            iVar = []; iStatic = []; 
                            if len(iStatics) == 0:
                                vorStartPointer = absoluteStartPos
                            else:
                                vorStartPointer = iStatics[-1][-1][-1]

                # if len(iVar) > 0:#, but might not be a complete match... has to be a complete match<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                if len(iVar) == len(self.iSortedVariablesAndPositionSansNum) and self.variablesConsistent(iVar):
                    iVars.append(iVar); iStatics.append(iStatic)
                    noOfMatches += 1


            if len(iVars) > 0: # something was captured
                #capture the stragglering Hin
                lastMatchedStaticEndPos = iStatics[-1][-1][-1]
                iHins.append((lastMatchedStaticEndPos, absoluteEndPos))
                #
                #store the parent in id__data
                self.iId__data[parentNodeId] = {
                    's': absoluteStartPos, 'e': absoluteEndPos, 'w': self.iStr[absoluteStartPos:absoluteEndPos],
                    'vars':iVars, 'statics':iStatics, 'vors':iVors, 'hins':iHins, 'noOfMatches':noOfMatches
                }


                #recurse on each variable, no matter if the variablesConsistent or NOT
                self.iEnclosureTree[parentNodeId] = []
                # print('iVars: ', iVars, '<<<<<<<<<<<<<<<<<<<<<<<<<'); 
                # import pdb;pdb.set_trace()
                for matchIdx, iVar in enumerate(iVars):
                    for iVarIdx, (varStartPos, varEndPos) in enumerate(iVar):
                        varNodeId = self.getEnclosureNodeId()
                        self.iEnclosureTree[parentNodeId].append(varNodeId)
                        recursiveMatch(varStartPos, varEndPos, varNodeId)
                #
            else:
                self.iId__data[parentNodeId] = {
                    'w':self.iStr[absoluteStartPos:absoluteEndPos],
                    's':absoluteStartPos,
                    'e':absoluteEndPos, 'noOfMatches':noOfMatches
                }

        recursiveMatch(0, len(self.iStr), self.getEnclosureNodeId())# 0:absoluteStartPos
        # print('id__data:')
        # self.pp.pprint(self.iId__data)
        # print('enclosureTree:')
        # self.pp.pprint(self.iEnclosureTree)
        # import pdb;pdb.set_trace()



    def mapBetweenEnclosureAndScheme(self):#This is only for iId__data... do it for oId__data too please<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
        """
        map from (enclosureId,MatchId)->root_of_iPattern
        mainly used for checking user provided skip node in scheme
        If it is MODE1, then the root_of_iPattern will be the schemeNodeId of the first $ that was matched

        SO user must only provide the schemeId of the root_of_iPattern that they wish to skip, we will not DFS for them... for now


        """
        self.tuple_enclosureId_matchId__schemeIdRootOfIPattern = {}
        if self.mode == 0 or self.mode == 2:
            rootOfIPatternSchemeId = self.iSchemeparser.rootOfTree[1]
            startPos_rootOfIPatternSchemeId = list(filter(lambda t: t[1]==rootOfIPatternSchemeId, self.startPos__nodeId___ip.items()))[0][0]
            for matchedEnclosureId in self.iEnclosureTree.keys():#only the keys of iEnclosureTree are matches
                for matchId, staticMatch in enumerate(self.iId__data[matchedEnclosureId]['statics']):
                    absoluteStartPosOfMatch = staticMatch[0][0]
                    absoluteStartPosRootOfIPattern = absoluteStartPosOfMatch + startPos_rootOfIPatternSchemeId
                    schemeIdRootOfIPattern = self.startPos__nodeId___iStr[absoluteStartPosRootOfIPattern]
                    self.tuple_enclosureId_matchId__schemeIdRootOfIPattern[(matchedEnclosureId, matchId)] = schemeIdRootOfIPattern
                    # print('check'); import pdb;pdb.set_trace()
        else: # self.mode == 1

            for matchedEnclosureId in self.iEnclosureTree.keys():
                for matchId, variableMatch in enumerate(self.iId__data[matchedEnclosureId]['vars']):
                    absoluteStartPosOfMatch = variableMatch[0][0]
                    #for scheme, the start of any scheme_str is always ( or a single schemeNode
                    #if it is (, then the startPos of its root is always after (
                    #else, it is the startPos of the single schemeNode
                    if self.iStr[absoluteStartPosOfMatch] == '(':
                        absoluteStartPosMatchRoot = absoluteStartPosOfMatch+len('(')
                    else: # single schemeNode
                        absoluteStartPosMatchRoot = absoluteStartPosOfMatch
                    #
                    schemeIdRootOfIPattern = self.startPos__nodeId___iStr[absoluteStartPosMatchRoot]
                    self.tuple_enclosureId_matchId__schemeIdRootOfIPattern[(matchedEnclosureId, matchId)] = schemeIdRootOfIPattern




        self.tuple_enclosureId_matchId__iVarPos__schemeIdRoot = {} # this only applies to MODE1 or MODE2
        if self.mode == 1 or self.mode == 2:
            for matchedEnclosureId in self.iEnclosureTree.keys():
                for matchId, variableMatch in enumerate(self.iId__data[matchedEnclosureId]['vars']):
                    iVarPos__schemeIdRoot = {}
                    for iVarPos, (absoluteVarStartPos, absoluteVarEndPos) in zip(self.iSortedVariablesAndPosition, variableMatch):
                        if self.iStr[absoluteVarStartPos] == '(':
                            absoluteStartPosMatchRoot = absoluteVarStartPos+len('(')
                        else:
                            absoluteStartPosMatchRoot = absoluteVarStartPos
                        schemeIdRootOfIPattern = self.startPos__nodeId___iStr[absoluteStartPosMatchRoot]
                        iVarPos__schemeIdRoot[iVarPos] = schemeIdRootOfIPattern
                    self.tuple_enclosureId_matchId__iVarPos__schemeIdRoot[(matchedEnclosureId, matchId)] = iVarPos__schemeIdRoot



    def parse(self, nodeIdsToSkip=[], variableMinArgs={}, variableMaxArgs={}):
        """

        after the startPos__nodeId done in buildEnclosureTree, the user can choose, what nodeIdsToSkip, or they can use the enclosureTree to choose (but not user friendly because need extra mapping from user)

        :
        """
        if getattr(self, 'iEnclosureTree', None) is None or self.iEnclosureTree is None: # make the user call it, so that they can plan what nodeIdsToSkip to use
            raise Exception('please call buildEnclosureTree first')

        # if len(self.iEnclosureTree) == 0: # there are no matches
        
        #
        # print('iId__data', self.iId__data)
        #
        if self.noMatches:
            return self.oStr

        self.newOEnclosureNodeCounter = -1

        self.nodeIdsToSkip = nodeIdsToSkip; self.variableMinArgs = variableMinArgs; self.variableMaxArgs = variableMaxArgs

        self.OLDSchemeNodeId__NEWSchemeNodeId___oStr = {} # map old to new first for future uses
        self.iEnclosureTreeId__oEnclosureTreeId = {}
        self.oEnclosureTreeId__iEnclosureTreeId = {}

        self.oVarPos__iVarPos = {}; self.iVarPos__oVarPos = {}

        self.list_oEnclosureIdSkipped = []
        self.list_iEnclosureIdSkipped = []

        if self.mode == 0:
            # self.mapIOVariables()#no iVar, not needed
            self.prepValsForExtraOVarsForEachMatch()
            self.generateOStr___MODE0()
            self.oEnclosureTreeId__iEnclosureTreeId = dict(map(lambda t: (t[1], t[0]), self.iEnclosureTreeId__oEnclosureTreeId.items()))
            if self.calculateSchemeNodeChanges:
                self.changesBetweenIStrVOStrForAllSchemeNodes()# self.calculateVerPosWord()
                if self.userProvided_startPos__nodeId:
                    self.calculate__startPos__nodeId()
        elif self.mode == 1:
            self.mapIOVariables()
            self.prepValsForExtraOVarsForEachMatch()
            self.generateOStr___MODE1()
            self.oEnclosureTreeId__iEnclosureTreeId = dict(map(lambda t: (t[1], t[0]), self.iEnclosureTreeId__oEnclosureTreeId.items()))
            if self.calculateSchemeNodeChanges:
                self.changesBetweenIStrVOStrForAllSchemeNodes()# self.calculateVerPosWord()
                if self.userProvided_startPos__nodeId:
                    self.calculate__startPos__nodeId()
        elif self.mode == 2:
            self.mapIOVariables()
            self.prepValsForExtraOVarsForEachMatch()
            self.generateOStr___MODE2()
            self.oEnclosureTreeId__iEnclosureTreeId = dict(map(lambda t: (t[1], t[0]), self.iEnclosureTreeId__oEnclosureTreeId.items()))
            if self.calculateSchemeNodeChanges:
                self.changesBetweenIStrVOStrForAllSchemeNodes()# self.calculateVerPosWord()
                if self.userProvided_startPos__nodeId:
                    self.calculate__startPos__nodeId()

        return self.oStr

    def prepValsForExtraOVarsForEachMatch(self):
        self.list_extraVars = list(set(self.oUniqueVariables) - set(self.iUniqueVariables))
        self.nodeId__matchIdx__outVarPos__outVal = {}; usedVariables = []
        # print('self.iId__data: '); self.pp.pprint(self.iId__data)
        for nodeId, data in self.iId__data.items():
            if 'statics' in data: #this node is a match
                self.nodeId__matchIdx__outVarPos__outVal[nodeId] = {}
                for matchIdx, match in enumerate(data.get('statics', [])): # not using inVars as a matchIdx, because MODE0 does not have inVars, but has inStatics
                    self.nodeId__matchIdx__outVarPos__outVal[nodeId][matchIdx] = {}
                    # print('self.list_extraVars', self.list_extraVars); import pdb;pdb.set_trace()
                    #generate extra outVarPos
                    if len(self.list_extraVars) > 0:
                        for oVarExtra in self.list_extraVars:
                            val = self.giveMeNVariableNotInThisList(1, usedVariables)
                            usedVariables += val
                            for outVarPos in filter(lambda outVarPos: outVarPos[0] == oVarExtra, self.oSortedVariablesAndPositionSansNum):
                                self.nodeId__matchIdx__outVarPos__outVal[nodeId][matchIdx].update({outVarPos:val[0]})

    def generateOStr___MODE0(self):
        """Mental Image (there will only be 1 match node which is nodeId=0, because this is just regex match:

        vor|iPattern|hin=vor|iPattern|hin=vor|iPattern|hin
            ~match~~         ~match~~         ~match~~    


        Any variables in oPattern are filled with giveMeNVariableNotInThisList, and then each match|iPattern in iStr are replaced with the filled_oPattern

        vor|outStatic oVarVal outStatic oVarVal outStatic|hin=vor|outStatic oVarVal outStatic oVarVal outStatic|hin=vor|outStatic oVarVal outStatic oVarVal outStatic|hin
            ~~~~~~~~~~~~~~~~~~~~~~match~~~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~~~match~~~~~~~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~~~match~~~~~~~~~~~~~~~~~~~~~~
        
        +vor
        for matchIdx in self.iId__data[0]['inStatics']:
            +filled_oPattern
            +hin

        """

        # print('self.iId__data')
        # self.pp.pprint(self.iId__data); 
        # import pdb;pdb.set_trace()

        oEnclosureTreeId = self.getOEnclosureNodeId()
        self.iEnclosureTreeId__oEnclosureTreeId[0]=oEnclosureTreeId
        self.oId__data = {}; self.oEnclosureTree = {oEnclosureTreeId:[]};#should each oVar have its oEnclosureId, just like the other 2 MODEs?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        oStr = ''
        oVors = []; oHins = []; oStatics = []; oVars = []
        parentId = 0
        matchIdx__outVarPos__outVal = self.nodeId__matchIdx__outVarPos__outVal[parentId]
        # print("self.iId__data[parentId]['iVors']"); self.pp.pprint(self.iId__data[parentId]['iVors']); import pdb;pdb.set_trace()
        iVorStartPos, iVorEndPos = self.iId__data[parentId]['vors'][0]
        oVorStartPos = len(oStr)
        oStr = self.iStr[iVorStartPos:iVorEndPos]
        # print('0 oStr: ', '|'+oStr+'|'); import pdb;pdb.set_trace()
        oVorEndPos = len(oStr)
        oVors.append((oVorStartPos, oVorEndPos))
        
        for matchIdx, enclosureChildId in enumerate(self.iEnclosureTree[parentId]):
            oStatic = [];oVar = []; 
            skipThisNodeMatch = self.skipNode(parentId, matchIdx)
            # print('skipThisNodeMatch', skipThisNodeMatch, 'enclosureChildId', enclosureChildId, 'matchIdx', matchIdx)
            if skipThisNodeMatch:
                oStaticStartPos = len(oStr)
                oStr += self.iPatternSansNum # putting it back
                oStaticEndPos = len(oStr)
                oStatic.append((oStaticStartPos, oStaticEndPos))
                #
                oEnclosureId = self.getOEnclosureNodeId()
                self.oEnclosureTree[oEnclosureTreeId].append(oEnclosureId)
                self.iEnclosureTreeId__oEnclosureTreeId[enclosureChildId]=oEnclosureTreeId
                self.oId__data[oEnclosureId] = {'s':oStaticStartPos, 'e':oStaticEndPos, 'w':val, 'noOfMatches':0}
                #
                self.list_oEnclosureIdSkipped.append(oEnclosureId)
                self.list_iEnclosureIdSkipped.append(enclosureChildId)
            else: # put in the oPattern
                
                for staticIdx, oVarPos in enumerate(self.oSortedVariablesAndPositionSansNum):
                    oPatternStaticStartPos, oPatternStaticEndPos = self.oStaticPatternStartEndPositionSansNum[staticIdx]
                    static = self.oPatternSansNum[oPatternStaticStartPos:oPatternStaticEndPos]
                    oStaticStartPos = len(oStr)
                    oStr += static
                    oStaticEndPos = len(oStr)
                    oStatic.append((oStaticStartPos, oStaticEndPos))
                    #
                    oVarStartPos = len(oStr)
                    val = matchIdx__outVarPos__outVal[matchIdx][oVarPos]
                    oStr += val
                    oVarEndPos = len(oStr)
                    #
                    oEnclosureId = self.getOEnclosureNodeId()
                    self.oEnclosureTree[oEnclosureTreeId].append(oEnclosureId)
                    self.iEnclosureTreeId__oEnclosureTreeId[enclosureChildId]=oEnclosureTreeId
                    self.oId__data[oEnclosureId] = {'s':oVarStartPos, 'e':oVarEndPos, 'w':val, 'noOfMatches':0}
                    #
                    oVar.append((oVarStartPos, oVarEndPos))
                oPatternStaticStartPos, oPatternStaticEndPos = self.oStaticPatternStartEndPositionSansNum[-1]
                static = self.oPatternSansNum[oPatternStaticStartPos:oPatternStaticEndPos]
                oStaticStartPos = len(oStr)
                oStr += static
                oStaticEndPos = len(oStr)
                oStatic.append((oStaticStartPos, oStaticEndPos))
                
            #
            oVars.append(oVar)
            oStatics.append(oStatic); 
            #
            iHinStartPos, iHinEndPos = self.iId__data[parentId]['hins'][matchIdx]
            # print('iHinStartPos: ', iHinStartPos, 'iHinEndPos:', iHinEndPos)
            hin = self.iStr[iHinStartPos:iHinEndPos]
            oVorHinStartPos = len(oStr)
            oStr += hin
            # print('2 oStr: ', '|'+oStr+'|'); import pdb;pdb.set_trace()
            oVorHinEndPos = len(oStr)
            oHins.append((oVorHinStartPos, oVorHinEndPos))
            if matchIdx != len(self.iEnclosureTree[parentId])-1: # not the last
                oVors.append((oVorHinStartPos, oVorHinEndPos))
        self.oId__data[oEnclosureTreeId] = {
            's':0, 'e':len(oStr), 'w':oStr,
            'vors':oVors, 'hins':oHins, 'statics':oStatics, 'vars':oVars, 'noOfMatches':len(self.iEnclosureTree[parentId])
        }
        self.oStr = oStr
        # print('oStr:', self.oStr)
        ####
        # print('self.iId__data')
        # self.pp.pprint(self.iId__data); 
        # print('self.oId__data')
        # self.pp.pprint(self.oId__data); 
        # import pdb;pdb.set_trace()

        return self.oStr

    def generateOStr___MODE1(self):
        """

        mental image:
        There should be no static except for the space between variables, because static is defined as nonvariables in the inputPattern and outputPattern
        This is for 1 enclosureId:
        vor|$0 $0 $1 $2 $0 $0 $1 $2 $0 $0 $1 $2|hin
            ~~~match~~~ ~~~match~~~ ~~~match~~~
        The vor and hin are delimited by s___parent and e___parent, meaning that there can be a lot of schemeNodes in the vor and hin, but there is at least one schemeNode
        validNonOverlappingMatches are sorted (by schemeStartPosition children), 


        need to find outputStr [mental image]:

        This is for 1 enclosureId:
        vor|outStatic$0outStatic$2outStatic outStatic$0outStatic$2outStatic outStatic$0outStatic$2outStatic|hin
            ~~~~~~~~~~~~~match~~~~~~~~~~~~~ ~~~~~~~~~~~~~match~~~~~~~~~~~~~ ~~~~~~~~~~~~~match~~~~~~~~~~~~~


        vor + [from parentNodeData]
        for each match
          for childId|var in match
            + static [from parentNodeData]
            + base_case_will_get_the_variable_match
          + static [from parentNodeData]
          +[space_between_matches_that_is_not_captured_in_id__data]
        + hin [from parentNodeData]

        

        """
        oRootEnclosureId = self.getOEnclosureNodeId()
        self.oId__data = {}; self.oEnclosureTree = {}
        # parent = {}; # this is the inverted self.iEnclosureTree
        def recursiveGenerate(nodeId, oNodeId):#change nodeId to iNodeId<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # print('nodeId: ', nodeId, nodeId not in self.iEnclosureTree); import pdb;pdb.set_trace()
            self.iEnclosureTreeId__oEnclosureTreeId[nodeId] = oNodeId
            if 'vars' not in self.iId__data[nodeId]: # is not a Match node
                # print('nodeId: ', nodeId, 'returning', self.iId__data[nodeId]['w'])
                # print('returned! nodeId:', nodeId)
                return self.iId__data[nodeId]['w']
            # print('did not return: ', nodeId)
            matchIdx__outVarPosExtra__outVal = self.nodeId__matchIdx__outVarPos__outVal[nodeId]
            list_replacement = []; 
            oVars = []; oStatics = []; oVors = []; oHins = []
            # outVorRelativeStartPos = 
            # print('self.iId__data["nodeId"]["iVors"]', self.iId__data[nodeId]['iVors']); import pdb;pdb.set_trace()
            vorStartPos, vorEndPos = self.iId__data[nodeId]['vors'][0]
            matchRelativeStartPos = vorEndPos - vorStartPos; 

            self.oEnclosureTree[oNodeId] = []
            # skipThisNode = self.skipNode(nodeId)
            oStr = ''
            oVorStartPos = len(oStr)
            oStr += self.iStr[vorStartPos:vorEndPos];
            oVorEndPos = len(oStr)
            oVors.append((oVorStartPos, oVorEndPos))
            relativeStaticStartPos = 0
            matches = self.iId__data[nodeId].get('vars', [])
            for matchIdx, match in enumerate(matches):
                skipThisNodeMatch = self.skipNode(nodeId, matchIdx)
                if skipThisNodeMatch:
                    sortedVariablesAndPosition = self.iSortedVariablesAndPositionSansNum
                    staticPatternStartEndPosition = self.iStaticPatternStartEndPositionSansNum#iMatch is done SanPosition, so here with have to use SanPosition
                    pattern = self.iPatternSansNum
                else:
                    sortedVariablesAndPosition = self.oSortedVariablesAndPositionSansNum
                    staticPatternStartEndPosition = self.oStaticPatternStartEndPositionSansNum
                    pattern = self.oPatternSansNum
                # print('staticPatternStartEndPosition: ', staticPatternStartEndPosition); import pdb;pdb.set_trace()
                oStatic = []; oVar = [];
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<after this please also correct MODE1
                for varIdx, varPos in enumerate(sortedVariablesAndPosition):
                    #static # in MODE1, this will be outside the varForLoop
                    patternStaticStartPos, patternStaticEndPos = staticPatternStartEndPosition[varIdx] # the static at the front of varPos
                    staticFrag = pattern[patternStaticStartPos:patternStaticEndPos]
                    staticRelativeStartPos = len(oStr)
                    oStr += staticFrag
                    staticRelativeEndPos = len(oStr)
                    oStatic.append((staticRelativeStartPos, staticRelativeEndPos))
                    #
                    #variable
                    oChildEnclosureId = self.getOEnclosureNodeId()
                    self.oEnclosureTree[oNodeId].append(oChildEnclosureId)
                    if skipThisNodeMatch:#use iVarPos
                        childIdxInEnclosureTree = matchIdx * len(self.iSortedVariablesAndPositionSansNum) + varIdx
                        childNodeId = self.iEnclosureTree[nodeId][childIdxInEnclosureTree]
                        val = recursiveGenerate(childNodeId, oChildEnclosureId)
                        self.list_oEnclosureIdSkipped.append(oNodeId)
                        self.list_iEnclosureIdSkipped.append(nodeId)
                    else:#use oVarPos, need to map back to iVarPos to get childNodeId, 
                        if varPos in self.oVarPos__iVarPos:
                            iVarPos = self.oVarPos__iVarPos[varPos]
                            iVarIdx = self.iSortedVariablesAndPositionSansNum.index(iVarPos)
                            childIdxInEnclosureTree = matchIdx * len(self.iSortedVariablesAndPositionSansNum) + iVarIdx
                            childNodeId = self.iEnclosureTree[nodeId][childIdxInEnclosureTree]
                            val = recursiveGenerate(childNodeId, oChildEnclosureId)
                        else:#if unable to map back, then get from generatedExtraVals
                            # print('varPos:', varPos)
                            # print('matchIdx__outVarPosExtra__outVal[matchIdx]', matchIdx__outVarPosExtra__outVal[matchIdx]); import pdb;pdb.set_trace()
                            val = matchIdx__outVarPosExtra__outVal[matchIdx][varPos]
                    staticVariableStartPos = len(oStr)
                    oStr += val
                    staticVariableEndPos = len(oStr)
                    if oChildEnclosureId in self.oId__data:
                        self.oId__data[oChildEnclosureId].update({
                            's':0, 'e': len(val), 'w':val
                        })
                    else:
                        self.oId__data[oChildEnclosureId] = {
                            's':0, 'e': len(val), 'w':val, 'noOfMatches':0
                        }
                    oVar.append((staticVariableStartPos, staticVariableEndPos))
                    #
                oPatternStaticStartPos, oPatternStaticEndPos = self.oStaticPatternStartEndPositionSansNum[-1]
                staticFrag = pattern[oPatternStaticStartPos:oPatternStaticEndPos]
                staticRelativeStartPos = len(oStr)
                oStr += staticFrag
                staticRelativeEndPos = len(oStr)
                oStatic.append((staticRelativeStartPos, staticRelativeEndPos))
                oStatics.append(oStatic); oVars.append(oVar)
                #the space that was not captured, between non_overlapping_matches
                if matchIdx != len(matches) - 1:# do not add a space to the last match
                    oStr += ' '

                #
            iHinStartPos, iHinEndPos = self.iId__data[nodeId]['hins'][-1]
            hin = self.iStr[iHinStartPos:iHinEndPos] # hin String
            oHinStartPos = len(oStr)
            oStr += hin
            oHinEndPos = len(oStr)
            oHins.append((oHinStartPos, oHinEndPos))
            self.oId__data[oNodeId] = {
                'vors':oVors, 'statics':oStatics, 'vars':oVars, 'hins':oHins,
                's':0,# currently in relative position
                'e':len(oStr),# currently in relative position
                'w':oStr, 'noOfMatches':len(matches)
            }

            return oStr
            #calculatePositionsOfChange relative to this nodeId

            #

        self.oStr = recursiveGenerate(0, oRootEnclosureId)# assume the enclosureTreeId is always 1
        # print('****************************')
        # print('self.oStr: ', self.oStr)
        # self.pp.pprint(self.oEnclosureTree); self.pp.pprint(self.oId__data)
        """

        vor|outStatic$0outStatic$2outStatic outStatic$0outStatic$2outStatic outStatic$0outStatic$2outStatic|hin
            ~~~~~~~~~~~~~match~~~~~~~~~~~~~ ~~~~~~~~~~~~~match~~~~~~~~~~~~~ ~~~~~~~~~~~~~match~~~~~~~~~~~~~

        
        if a child is it's parent's matchIdx and variableIdx
        for each [vor|static|variable|hin] THING, we only have to add the THING immediately before it in its parent's match

        each match come from the parent's variable, and in MODE1, the THING before the parent's variable is always static
        so we just have to add static to everyTHING in the child


        to all the child's oDatum
        """
        queue = [0]
        while len(queue) > 0:
            parentEnclosureId = queue.pop(0)
            childEnclosureIds = self.oEnclosureTree.get(parentEnclosureId, [])
            queue += childEnclosureIds
            #pointer
            parentDatum = self.oId__data[parentEnclosureId]
            #
            for oMatchIdxTimesVarIdx, childEnclosureId in enumerate(childEnclosureIds):
                #
                oMatchIdxInParent = oMatchIdxTimesVarIdx // len(self.oSortedVariablesAndPosition);
                oVarIdxInParent = oMatchIdxTimesVarIdx % len(self.oSortedVariablesAndPosition)
                #
                # print('parentEnclosureId', parentEnclosureId, 'parentDatum', parentDatum)
                # import pdb;pdb.set_trace()
                offset__byParentStatic = parentDatum['statics'][oMatchIdxInParent][oVarIdxInParent][-1]#endPos of static in the parent, just before the variable=thisChild, this is inclusive of the offset__vor
                self.oId__data[childEnclosureId]['s'] += offset__byParentStatic#child is a variableInParent, the immediateTHINGbeforeChildInParent is the static
                #offset children oVors
                oVors___new = []
                for oVorStartPos, oVorEndPos in self.oId__data[childEnclosureId].get('vors', []):
                    oVors___new.append((oVorStartPos+offset__byParentStatic, oVorEndPos+offset__byParentStatic))
                if len(oVors___new) > 0:
                    self.oId__data[childEnclosureId]['vors'] = oVors___new
                #offset children oStatic
                oStatics___new = []
                for oStatic in self.oId__data[childEnclosureId].get('statics', []):
                    oStatic___new = []
                    for oStaticStartPos, oStaticEndPos in oStatic:
                        oStatic___new.append((oStaticStartPos+offset__byParentStatic, oStaticEndPos+offset__byParentStatic))
                    oStatics___new.append(oStatic___new)
                if len(oStatics___new) > 0:
                    self.oId__data[childEnclosureId]['statics'] = oStatics___new
                #offset children oVars
                oVars___new = []
                for oVar in self.oId__data[childEnclosureId].get('vars', []):
                    oVar___new = []
                    for oVarStartPos, oVarEndPos in oVar:
                        oVar___new.append((oVarStartPos+offset__byParentStatic, oVarEndPos+offset__byParentStatic))
                    oVars___new.append(oVar___new)
                if len(oVars___new) > 0:
                    self.oId__data[childEnclosureId]['vars'] = oVars___new
                #offset children oHins
                oHins___new = []
                for oHinStartPos, oHinEndPos in self.oId__data[childEnclosureId].get('hins', []):
                    oHins___new.append((oHinStartPos+offset__byParentStatic, oHinEndPos+offset__byParentStatic))
                if len(oHins___new) > 0:
                    self.oId__data[childEnclosureId]['hins'] = oHins___new
                #
                self.oId__data[childEnclosureId]['e'] += offset__byParentStatic

        # self.pp.pprint(self.oId__data); import pdb;pdb.set_trace()
        # print('****************************')
        # print('self.oStr: ', self.oStr)
        # self.pp.pprint(self.oEnclosureTree); self.pp.pprint(self.oId__data); import pdb;pdb.set_trace()
        return self.oStr

    def generateOStr___MODE2(self):
        """
        Mental image for each matched enclosureId (in this example there are 2 matches of the inputPattern):
        vor|inStatic$0inStatic$1inStatic$2inStatic|hin=vor|inStatic$0inStatic$1inStatic$2inStatic|hin
            ~~~~~~~~~~~~~match~~~~~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~match~~~~~~~~~~~~~~~~~    


        There are the same number of matches for outputStr, and everything in the match can change including the outStatic. But, the vor|hin must remain the same as the schemeword
        vor|outStatic$0outStatic|hin=vor|outStatic$0outStatic|hin
            ~~~~~~match~~~~~~~~~         ~~~~~~~~match~~~~~~~

        for each match
          vor + [from parentNodeData]
          for childId|var in match
            + static [from parentNodeData]
            + base_case_will_get_the_variable_match
          + static [from parentNodeData]
          + hin [from parentNodeData]

        """
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<should there be a map from iEnclosureId__oEnclosureId & oEnclosureId__iEnclosureId?
        self.oEnclosureTree = {}; self.oId__data = {}#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<rename to avoid confusion iId__data
        def recursiveGenerate(nodeId, oNodeId):
            # print('start: generateOStr___MODE2'); import pdb; pdb.set_trace()
            self.iEnclosureTreeId__oEnclosureTreeId[nodeId] = oNodeId
            if 'vars' not in self.iId__data[nodeId]: # is not a Match node
                # print('nodeId: ', nodeId, 'returning', self.iId__data[nodeId]['w'])
                return self.iId__data[nodeId]['w']
            # print('nodeId: ', nodeId)
            #take out the extraVals
            matchIdx__outVarPosExtra__outVal = self.nodeId__matchIdx__outVarPos__outVal[nodeId]
            #is a match node
            oStr = ''; oVars = []; oStatics = []; oVors= []; oHins = []
            # skipThisNode = self.skipNode(nodeId)
            # print('nodeId: ', nodeId, 'skipThisNode? ', skipThisNode); import pdb;pdb.set_trace()
            #for each match
            self.oEnclosureTree[oNodeId] = []
            matches = self.iId__data[nodeId]['vars']
            for matchIdx, _ in enumerate(matches):
                #take out the extraVals
                vorStartPos, vorEndPos = self.iId__data[nodeId]['vors'][matchIdx]
                vor = self.iStr[vorStartPos:vorEndPos]#vor String
                vorRelativeStartPos = len(oStr)
                oStr += vor
                vorRelativeEndPos = len(oStr)
                oVors.append((vorRelativeStartPos, vorRelativeEndPos))

                if matchIdx != 0: # not the first match
                    oHins.append((vorRelativeStartPos, vorRelativeEndPos))
                skipThisNodeMatch = self.skipNode(nodeId, matchIdx)
                # skipThisNodeMatch = False#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<cange this back for testing
                if skipThisNodeMatch:
                    sortedVariablesAndPosition = self.iSortedVariablesAndPositionSansNum
                    staticPatternStartEndPosition = self.iStaticPatternStartEndPositionSansNum#iMatch is done SanPosition, so here with have to use SanPosition
                    pattern = self.iPatternSansNum
                    self.list_oEnclosureIdSkipped.append(oNodeId)
                    self.list_iEnclosureIdSkipped.append(nodeId)
                else:
                    sortedVariablesAndPosition = self.oSortedVariablesAndPositionSansNum
                    staticPatternStartEndPosition = self.oStaticPatternStartEndPositionSansNum
                    pattern = self.oPatternSansNum
                # print('skipThisNodeMatch', skipThisNodeMatch)
                # print('sortedVariablesAndPosition: ', sortedVariablesAndPosition)
                # print('staticPatternStartEndPosition: ', staticPatternStartEndPosition); 
                # print('pattern', pattern)
                # import pdb;pdb.set_trace()
                oStatic = []; oVar = [];
                for varIdx, varPos in enumerate(sortedVariablesAndPosition):
                    oPatternStaticStartPos, oPatternStaticEndPos = staticPatternStartEndPosition[varIdx]
                    staticFrag = pattern[oPatternStaticStartPos:oPatternStaticEndPos]
                    staticRelativeStartPos = len(oStr)
                    oStr += staticFrag
                    staticRelativeEndPos = len(oStr)
                    # print('staticRelativeStartPos: ', staticRelativeStartPos, 'staticRelativeEndPos:', staticRelativeEndPos)
                    # print('oPatternStaticStartPos: ', oPatternStaticStartPos, 'oPatternStaticEndPos:', oPatternStaticEndPos, 'staticFrag:', staticFrag); import pdb;pdb.set_trace()
                    oStatic.append((staticRelativeStartPos, staticRelativeEndPos))

                    #variable
                    oChildEnclosureId = self.getOEnclosureNodeId()
                    self.oEnclosureTree[oNodeId].append(oChildEnclosureId)
                    if skipThisNodeMatch:#use iVarPos
                        childIdxInEnclosureTree = matchIdx * len(self.iSortedVariablesAndPositionSansNum) + varIdx
                        childNodeId = self.iEnclosureTree[nodeId][childIdxInEnclosureTree]
                        val = recursiveGenerate(childNodeId, oChildEnclosureId)
                    else:#use oVarPos, need to map back to iVarPos to get childNodeId
                        if varPos in self.oVarPos__iVarPos:
                            iVarPos = self.oVarPos__iVarPos[varPos]
                            iVarIdx = self.iSortedVariablesAndPositionSansNum.index(iVarPos)
                            childIdxInEnclosureTree = matchIdx * len(self.iSortedVariablesAndPositionSansNum) + iVarIdx
                            childNodeId = self.iEnclosureTree[nodeId][childIdxInEnclosureTree]
                            val = recursiveGenerate(childNodeId, oChildEnclosureId)
                        else:#if unable to map back, then get from generatedExtraVals
                            val = matchIdx__outVarPosExtra__outVal[matchIdx][varPos]
                    #
                    varRelativeStartPos = len(oStr)
                    oStr += val 
                    varRelativeEndPos = len(oStr)
                    if oChildEnclosureId in self.oId__data:
                        self.oId__data[oChildEnclosureId].update({
                            's':0, 'e': len(val), 'w':val
                        })
                    else:
                        self.oId__data[oChildEnclosureId] = {
                            's':0, 'e': len(val), 'w':val, 'noOfMatches':0
                        }
                    oVar.append((varRelativeStartPos, varRelativeEndPos))
                oPatternStaticStartPos, oPatternStaticEndPos = staticPatternStartEndPosition[-1]
                staticFrag = pattern[oPatternStaticStartPos:oPatternStaticEndPos]
                # print('staticFrag: ', staticFrag); import pdb;pdb.set_trace()
                staticRelativeStartPos = len(oStr)
                oStr += staticFrag
                staticRelativeEndPos = len(oStr)
                oStatic.append((staticRelativeStartPos, staticRelativeEndPos))
                oStatics.append(oStatic); oVars.append(oVar)
                #
            iHinStartPos, iHinEndPos = self.iId__data[nodeId]['hins'][-1]
            hin = self.iStr[iHinStartPos:iHinEndPos] # hin String
            oHinStartPos = len(oStr)
            oStr += hin
            oHinEndPos = len(oStr)
            oHins.append((oHinStartPos, oHinEndPos))
            self.oId__data[oNodeId] = {
                'vors':oVors, 'statics':oStatics, 'vars':oVars, 'hins':oHins,
                's':0,# currently in relative position
                'e':len(oStr),# currently in relative position
                'w':oStr, 'noOfMatches':len(matches)
            }
            # print('oStr: ', oStr); import pdb;pdb.set_trace()
            return oStr
        #
        # print('iId__data', self.iId__data)
        #
        self.oStr = recursiveGenerate(0, self.getOEnclosureNodeId())# 0 is the iEnclosureRootId

        # print('****************************')
        # print('self.oStr: ', self.oStr)
        # self.pp.pprint(self.oEnclosureTree); self.pp.pprint(self.oId__data)
        # self.pp.pprint(self.iId__data); import pdb;pdb.set_trace()
        """
        vor|outStatic$0outStatic|hin=vor|outStatic$0outStatic|hin
            ~~~~~~match~~~~~~~~~         ~~~~~~~~match~~~~~~~


        DFS so we convert each oDatum using the absolute position of its parents' oDatum. The root of enclosureTree is always already in absolutePosition
        if a child is it's parent's matchIdx and variableIdx
        for each [vor|static|variable|hin] THING, we only have to add the THING immediately before it in its parent's match

        each match come from the parent's variable, and in MODE2, the THING before the parent's variable is always static
        so we just have to add static to everyTHING in the child

        to all the child's oDatum
        """
        # print('self.oEnclosureTree')
        # self.pp.pprint(self.oEnclosureTree)

        queue = [0]
        while len(queue) > 0:
            parentEnclosureId = queue.pop(0)
            childEnclosureIds = self.oEnclosureTree.get(parentEnclosureId, [])
            queue += childEnclosureIds
            #pointer
            parentDatum = self.oId__data[parentEnclosureId]
            #
            for oMatchIdxTimesVarIdx, childEnclosureId in enumerate(childEnclosureIds):
                #
                oMatchIdxInParent = oMatchIdxTimesVarIdx // len(self.oSortedVariablesAndPosition);
                oVarIdxInParent = oMatchIdxTimesVarIdx % len(self.oSortedVariablesAndPosition)
                #
                offset__byParentStatic = parentDatum['statics'][oMatchIdxInParent][oVarIdxInParent][-1]#endPos of static in the parent, just before the variable=thisChild, this is inclusive of the offset__vor
                # print('childEnclosureId', childEnclosureId)
                # print('oMatchIdxInParent', oMatchIdxInParent); print('oVarIdxInParent', oVarIdxInParent)
                # print('offset__byParentStatic', offset__byParentStatic)
                # import pdb;pdb.set_trace()
                self.oId__data[childEnclosureId]['s'] += offset__byParentStatic#child is a variableInParent, the immediateTHINGbeforeChildInParent is the static
                #offset children oVors
                oVors___new = []
                for oVorStartPos, oVorEndPos in self.oId__data[childEnclosureId].get('vors', []):
                    oVors___new.append((oVorStartPos+offset__byParentStatic, oVorEndPos+offset__byParentStatic))
                if len(oVors___new) > 0:
                    self.oId__data[childEnclosureId]['vors'] = oVors___new
                #offset children oStatic
                oStatics___new = []
                for oStatic in self.oId__data[childEnclosureId].get('statics', []):
                    oStatic___new = []
                    for oStaticStartPos, oStaticEndPos in oStatic:
                        oStatic___new.append((oStaticStartPos+offset__byParentStatic, oStaticEndPos+offset__byParentStatic))
                    oStatics___new.append(oStatic___new)
                if len(oStatics___new) > 0:
                    self.oId__data[childEnclosureId]['statics'] = oStatics___new
                #offset children oVars
                oVars___new = []
                for oVar in self.oId__data[childEnclosureId].get('vars', []):
                    oVar___new = []
                    for oVarStartPos, oVarEndPos in oVar:
                        oVar___new.append((oVarStartPos+offset__byParentStatic, oVarEndPos+offset__byParentStatic))
                    oVars___new.append(oVar___new)
                if len(oVars___new) > 0:
                    self.oId__data[childEnclosureId]['vars'] = oVars___new
                #offset children oHins
                oHins___new = []
                for oHinStartPos, oHinEndPos in self.oId__data[childEnclosureId].get('hins', []):
                    oHins___new.append((oHinStartPos+offset__byParentStatic, oHinEndPos+offset__byParentStatic))
                if len(oHins___new) > 0:
                    self.oId__data[childEnclosureId]['hins'] = oHins___new
                #
                self.oId__data[childEnclosureId]['e'] += offset__byParentStatic

        # print('self.oStr: ', self.oStr)
        # self.pp.pprint(self.oEnclosureTree); self.pp.pprint(self.oId__data)
        # print('self.iId__data')
        # self.pp.pprint(self.iId__data); 
        # print('self.oId__data')
        # self.pp.pprint(self.oId__data); 
        # import pdb;pdb.set_trace()
        return self.oStr



    def changesBetweenIStrVOStrForAllSchemeNodes(self):
        """
        we can use iId__data and oId__data to match Between startPos__nodeId___iStr & startPos__nodeId___oStr
        for each (startPos, nodeId), we have a list of
        0. enclosureIdx
        1. matchIdx
        2. Type
          0. vorhin - if the schemeNode is here, there will only be 1 tuple
          1. static - position in the matchedPattern(IO) - if the schemeNode is here, there will only be 1 tuple
            0. {patternPosition} - {self.oStaticIdx__sortedList_tuple_labelStartPos_labelEndPos_type} -  for getting idxInStr
            1. {absolutePosition} - {self.oId__data[oNodeId]['statics'][matchIdx][staticIdx]}
          2. var - position in the matchedPattern(IO) - if the schemeNode is here, there might be a long list
            0. {patternPosition} - {self.oSortedVariablesAndPositionSansNum}
            1. {absolutePosition} - {self.oId__data[oNodeId]['vars'][matchIdx][varIdx]} -  for getting idxInStr
        This is also an identifier for the (startPos, nodeId) = @

        for (startPos, nodeId) in startPos__nodeId___iStr 
            we try to find the corresponding @ in startPos__nodeId___oStr
            if we can find the corresponding @, 
                we do not process that (startPos, nodeId) again for startPos__nodeId___oStr later_loop <>
                keep it as an {edit[this is also a mapping between startPos__nodeId___iStr and startPos__nodeId___oStr, that we can use later to get the real startPos__nodeId___oStr]}
            else
                keep it as a {remove}

        for (startPos, nodeId) in startPos__nodeId___oStr
            if (startPos, nodeId) in <> {already processed as edit}: continue
                
            keep it as an {addition[we can use later to get the real startPos__nodeId___oStr]}
        """
        # print('iStr: ')
        # print(self.iStr)
        # print('oStr: ')
        # print(self.oStr)
        # print('self.iEnclosureTree:')
        # print(self.iEnclosureTree)
        # print('self.oEnclosureTree:')
        # print(self.oEnclosureTree)
        #
        # import pprint; pp = pprint.PrettyPrinter(indent=4)
        # print('self.iId__data')
        # pp.pprint(self.iId__data);
        # print('self.oId__data')
        # pp.pprint(self.oId__data)
        # import pdb;pdb.set_trace()

        #


        from copy import copy
        from foundation.automat.parser.sorte.schemeparser import Schemeparser# prevent circular_import
        # print('self.iId__data', self.iId__data)
        # print('self.oStr: ', self.oStr)
        self.schemeparser___oStr = Schemeparser(equationStr=self.oStr)#, verbose=self.verbose)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<refactor the others so we do not call schemeparser on iStr again
        self.ast___oStr, functionsD___oStr, variablesD___oStr, primitives___oStr, totalNodeCount___oStr, self.startPos__nodeId___oStr = self.schemeparser___oStr._parse()
        self.nodeId__labelLen___oStr = self.schemeparser___oStr._getLabelLength()
        self.nodeId__labelLen___iStr = self.schemeparser___iStr._getLabelLength()
        #remapping nodeId__labelLen___iStr to user given nodeIds
        if self.userProvided_startPos__nodeId:
            self.nodeId__labelLen___iStr = self.renameUserGivenSchemeNodeId(self.nodeId__labelLen___iStr)
            self.ast___oStr = None # will need to be recalculated
        #
        #if user has given startPos__nodeId___iStr, then we must remap nodeId__labelLen___iStr<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #get the startPos__nodeId___iStr_NEW, zip with startPos__nodeId___iStr<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


        startPos__nodeId___iStr = copy(self.startPos__nodeId___iStr) # for getting the leftover, after removing the positions of static and variable, so that we can compute vorhin more easily
        startPos__nodeId___oStr = copy(self.startPos__nodeId___oStr) # for getting the leftover, after removing the positions of static and variable, so that we can compute vorhin more easily


        #
        # print('self.oEnclosureTreeId__iEnclosureTreeId', self.oEnclosureTreeId__iEnclosureTreeId)
        # print('self.oEnclosureTree', self.oEnclosureTree)
        # print('self.iEnclosureTree', self.iEnclosureTree)
        #



        def constructNonOverlappingRangesTOid(id__data, enclosureTree, noOfVariables, typ):
            from copy import deepcopy
            sortedList_tuple_startEndPosRange_id = []
            def recursive(enclosureId, accumulatedCallerIds):
                """Go by per match, and go in order of all the types of each match"""
                if id__data[enclosureId]['noOfMatches'] == 0:
                    data = id__data[enclosureId]; startPos = data['s']; endPos = data['e']
                    # import pdb;pdb.set_trace()
                    sortedList_tuple_startEndPosRange_id.append((startPos, endPos, accumulatedCallerIds))

                #     accumulatedCallerIds___copy = deepcopy(accumulatedCallerIds)
                #     accumulatedCallerIds___copy.append(('var', enclosureId, matchIdx, staticVarIdx))
                
                data = id__data[enclosureId]#what if len(iVar)==0? like for MODE0? use static, so far, for these modes, they are never 0
                for matchIdx in range(0, id__data[enclosureId]['noOfMatches']): # is it ok to keep the number of matches, so you don't have to recount, are there any other places that use this information?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    #vor if any
                    if 'vors' in id__data[enclosureId] and len(id__data[enclosureId]['vors']) > matchIdx: # matchIdx-1 because MODE1 only has 1 vor in front of all the matches for 1 enclosureId
                        # print("len(id__data[enclosureId]['vors'])", len(id__data[enclosureId]['vors']), 'matchIdx-1', matchIdx)
                        accumulatedCallerIds___copy = deepcopy(accumulatedCallerIds)
                        accumulatedCallerIds___copy.append(('vor', enclosureId, matchIdx))
                        startPos, endPos = id__data[enclosureId]['vors'][matchIdx]
                        sortedList_tuple_startEndPosRange_id.append((startPos, endPos, accumulatedCallerIds___copy))

                    #MODE1, there are only empty space (static) between variables
                    if self.mode == 1 and typ == 'i':
                        childEnclosureIds = enclosureTree[enclosureId][matchIdx*noOfVariables:(matchIdx+1)*noOfVariables]
                        for staticVarIdx, childEnclosureId in enumerate(childEnclosureIds):
                            #var
                            accumulatedCallerIds___copy = deepcopy(accumulatedCallerIds)
                            accumulatedCallerIds___copy.append(('var', enclosureId, matchIdx, staticVarIdx))
                            recursive(childEnclosureId, accumulatedCallerIds___copy) # this will write to sortedList_tuple_startEndPosRange_id
                            # startPos, endPos = id__data[enclosureId]['vars'][matchIdx][staticVarIdx]
                            # sortedList_tuple_startEndPosRange_id.append((startPos, endPos, accumulatedCallerIds___copy))

                            if staticVarIdx != len(childEnclosureIds) - 1: # if not last variable, then there is a blank that is the static.
                                accumulatedCallerIds___copy = deepcopy(accumulatedCallerIds)
                                accumulatedCallerIds___copy.append(('static', enclosureId, matchIdx, staticVarIdx))
                                startPos, endPos = id__data[enclosureId]['statics'][matchIdx][staticVarIdx]
                                sortedList_tuple_startEndPosRange_id.append((startPos, endPos, accumulatedCallerIds___copy))


                    else:#MODE2, there is always a static, in front of the variable. If MODE0, where there is no variables, there is exactly 1 static only
                        childEnclosureIds = enclosureTree[enclosureId][matchIdx*noOfVariables:(matchIdx+1)*noOfVariables]
                        for staticVarIdx, childEnclosureId in enumerate(childEnclosureIds):
                            accumulatedCallerIds___copy = deepcopy(accumulatedCallerIds)
                            accumulatedCallerIds___copy.append(('static', enclosureId, matchIdx, staticVarIdx))
                            #static, the front of every childEnclosureId, is a static... except iMODE1
                            # print('enclosureId', enclosureId, "id__data[enclosureId]['statics']", id__data[enclosureId]['statics'], 'matchIdx', matchIdx, 'typ: ', typ); import pdb;pdb.set_trace()
                            startPos, endPos = id__data[enclosureId]['statics'][matchIdx][staticVarIdx]
                            if startPos != endPos: #for MODE1 o
                                sortedList_tuple_startEndPosRange_id.append((startPos, endPos, accumulatedCallerIds___copy))

                            #var (with recursive_call) if any
                            if len(id__data[enclosureId]['vars'])>0 and len(id__data[enclosureId]['vars'][matchIdx]) > 0:
                                accumulatedCallerIds___copy = deepcopy(accumulatedCallerIds)
                                accumulatedCallerIds___copy.append(('var', enclosureId, matchIdx, staticVarIdx))
                                recursive(childEnclosureId, accumulatedCallerIds___copy) # this will write to sortedList_tuple_startEndPosRange_id
                                # startPos, endPos = id__data[enclosureId]['vars'][matchIdx][staticVarIdx]
                                # sortedList_tuple_startEndPosRange_id.append((startPos, endPos, accumulatedCallerIds___copy))

                        #static if any [the ending of the match] # not available for MODE0SKIP {len(id__data[enclosureId]['statics']) > matchIdx and}
                        # print("matchIdx", matchIdx, "id__data[enclosureId]['statics']", id__data[enclosureId]['statics']); import pdb;pdb.set_trace()
                        if len(id__data[enclosureId]['statics']) > matchIdx and len(id__data[enclosureId]['statics'][matchIdx]) > 1:
                            accumulatedCallerIds___copy = deepcopy(accumulatedCallerIds)
                            accumulatedCallerIds___copy.append(('static', enclosureId, matchIdx, staticVarIdx)) 
                            startPos, endPos = id__data[enclosureId]['statics'][matchIdx][-1]
                            # print(startPos, endPos, 'static')
                            if startPos != endPos:#for MODE1 o
                                sortedList_tuple_startEndPosRange_id.append((startPos, endPos, accumulatedCallerIds___copy))
                                # print('added'); import pdb;pdb.set_trace()

                #hin if any
                if 'hins' in id__data[enclosureId] and len(id__data[enclosureId]['hins']) > 0:#we only want the last one to prevent overlap with middle vors
                    accumulatedCallerIds___copy = deepcopy(accumulatedCallerIds)
                    # accumulatedCallerIds___copy.append(('hin', enclosureId, matchIdx))
                    accumulatedCallerIds___copy.append(('hin', enclosureId, len(id__data[enclosureId]['hins'])))
                    # startPos, endPos = id__data[enclosureId]['hins'][matchIdx]
                    startPos, endPos = id__data[enclosureId]['hins'][-1]
                    sortedList_tuple_startEndPosRange_id.append((startPos, endPos, accumulatedCallerIds___copy))

            recursive(0, [])
            return sortedList_tuple_startEndPosRange_id

        if self.mode == 0:
            numberOfVariables = 1
        else:
            numberOfVariables = len(self.iSortedVariablesAndPositionSansNum)

        # print('self.iId__data:')
        # self.pp.pprint(self.iId__data)
        # print('self.oId__data:')
        # self.pp.pprint(self.oId__data); import pdb;pdb.set_trace()


        iSortedList_tuple_startEndPosRange_id = constructNonOverlappingRangesTOid(self.iId__data, self.iEnclosureTree, numberOfVariables, 'i') # this did not consider that the nodeId might be skipped<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # print('done with iSortedList_tuple_startEndPosRange_id'); 
        # print(iSortedList_tuple_startEndPosRange_id)
        # import pdb;pdb.set_trace()
        oSortedList_tuple_startEndPosRange_id = constructNonOverlappingRangesTOid(self.oId__data, self.oEnclosureTree, len(self.oSortedVariablesAndPositionSansNum), 'o')

        # print('iSortedList_tuple_startEndPosRange_id', iSortedList_tuple_startEndPosRange_id)
        # print('oSortedList_tuple_startEndPosRange_id', oSortedList_tuple_startEndPosRange_id); import pdb;pdb.set_trace()

        def zipTogether(sortedList_tuple_startEndPosRange_id, sortedList_tuple_startPos_endPos_nodeId):
            #
            # print('zipTogether')
            # print(sortedList_tuple_startEndPosRange_id)
            # print(sortedList_tuple_startPos_endPos_nodeId)
            #
            madeUpIdIdx = 0; schemeIdIdx = 0; results = []
            while madeUpIdIdx < len(sortedList_tuple_startEndPosRange_id) and schemeIdIdx < len(sortedList_tuple_startPos_endPos_nodeId):
                (segmentStartPos, segmentEndPos, theIds) = sortedList_tuple_startEndPosRange_id[min(madeUpIdIdx, len(sortedList_tuple_startEndPosRange_id)-1)]
                (labelStartPos, labelEndPos, schemeNodeId) = sortedList_tuple_startPos_endPos_nodeId[min(schemeIdIdx, len(sortedList_tuple_startPos_endPos_nodeId)-1)]
                # print('segmentStartPos: ', segmentStartPos)
                # print('labelStartPos: ', labelStartPos)
                # print('labelEndPos: ', labelEndPos)
                # print('segmentEndPos', segmentEndPos)
                if segmentStartPos <= labelStartPos and labelEndPos <= segmentEndPos:
                    results.append((labelStartPos, labelEndPos, schemeNodeId, theIds))
                    schemeIdIdx+=1
                elif labelStartPos <= segmentStartPos and (segmentEndPos > labelEndPos):
                    schemeIdIdx+=1
                elif segmentEndPos <= labelEndPos:
                    madeUpIdIdx+=1
            return results

        # print('self.nodeId__labelLen___iStr', self.nodeId__labelLen___iStr); import pdb;pdb.set_trace()
        iSortedList_tuple_labelPosRangeSchemeIdTheIds = zipTogether(iSortedList_tuple_startEndPosRange_id, 
            list(map(lambda t: (t[0], t[0]+self.nodeId__labelLen___iStr[t[1]], t[1]), sorted(self.startPos__nodeId___iStr.items(), key=lambda t: t[0])))
        )
        oSortedList_tuple_labelPosRangeSchemeIdTheIds = zipTogether(oSortedList_tuple_startEndPosRange_id, 
            list(map(lambda t: (t[0], t[0]+self.nodeId__labelLen___oStr[t[1]], t[1]), sorted(self.startPos__nodeId___oStr.items(), key=lambda t: t[0])))
        )

        # print('end of zip together')
        # print('iSortedList_tuple_labelPosRangeSchemeIdTheIds', iSortedList_tuple_labelPosRangeSchemeIdTheIds)
        # print('oSortedList_tuple_labelPosRangeSchemeIdTheIds', oSortedList_tuple_labelPosRangeSchemeIdTheIds); import pdb;pdb.set_trace()


        schemeNodeChangeLog = []; 
        #
        mappedINodeId = set() # for the same theIds{bucket_for_vorhin_var_static}, there might be many iNodeId{for that oNodeId},  and it should not be repeated
        currentVorHinId = None # the mappedISchemeNodeIdInVorHin will be cleared for every currentVorHinId#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<not used yet
        #
        iTuple_type_enclosureId_matchId__sortedList_tuple_startPos_endPos_nodeId = {}
        for iStartPos, iEndPos, iNodeId, theIds in iSortedList_tuple_labelPosRangeSchemeIdTheIds:
            theId = theIds[-1] # the last one is the leaf, most specific
            #
            tuple_type_enclosureId_matchId = theId
            existing = iTuple_type_enclosureId_matchId__sortedList_tuple_startPos_endPos_nodeId.get(tuple_type_enclosureId_matchId, [])
            existing.append((iStartPos, iEndPos, iNodeId))
            iTuple_type_enclosureId_matchId__sortedList_tuple_startPos_endPos_nodeId[tuple_type_enclosureId_matchId] = existing
            #
        # print('iTuple_type_enclosureId_matchId__sortedList_tuple_startPos_endPos_nodeId')
        # print(iTuple_type_enclosureId_matchId__sortedList_tuple_startPos_endPos_nodeId); import pdb;pdb.set_trace()

        oTuple_type_enclosureId_matchId__sortedList_tuple_startPos_endPos_nodeId = {} # this is used to find removed on the second pass of startPos__nodeId___oStr
        for oStartPos, oEndPos, oNodeId, theIds in oSortedList_tuple_labelPosRangeSchemeIdTheIds:
            # theId = theIds[-1] # the last one is the leaf, most specific
            ow = self.oStr[oStartPos:oEndPos]
            theId = theIds[-1] # the last one is the leaf, most specific
            oEnclosureParentId = theId[1]; matchIdx = theId[2]; iEnclosureParentId = self.oEnclosureTreeId__iEnclosureTreeId[oEnclosureParentId]

            iTuple_type_enclosureId_matchId = None; var = None
            # print(oStartPos, oEndPos, oNodeId, theIds); import pdb;pdb.set_trace()
            if theId[0] == 'var':
                oVarIdx = theId[3] % len(self.oSortedVariablesAndPositionSansNum)
                oVarPos = self.oSortedVariablesAndPositionSansNum[oVarIdx]
                oEnclosureId = self.oEnclosureTree[oEnclosureParentId][theId[3]]
                tuple_type_enclosureId_matchId = theId#weird<<<<<<<<<
                #
                # print(oStartPos, oEndPos, oNodeId, 'oEnclosureId: ', oEnclosureId, oEnclosureId in self.oEnclosureTreeId__iEnclosureTreeId)
                # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<check'); import pdb;pdb.set_trace()
                if oEnclosureId in self.oEnclosureTreeId__iEnclosureTreeId:# only to check if oVarPos was an extra
                    iEnclosureId = self.oEnclosureTreeId__iEnclosureTreeId[oEnclosureId]
                    iParentEnclosureId = self.oEnclosureTreeId__iEnclosureTreeId[oEnclosureParentId]
                    iVarIdx = self.iEnclosureTree[iParentEnclosureId].index(iEnclosureId)
                    # iTuple_type_enclosureId_matchId = (theId[0], iEnclosureId, matchIdx, iVarPos)
                    iTuple_type_enclosureId_matchId = (theId[0], iEnclosureParentId, matchIdx, iVarIdx)
                    iVarPos = self.iSortedVariablesAndPositionSansNum[iVarIdx%len(self.iSortedVariablesAndPositionSansNum)]
                    var = iVarPos[0]
                else:#added
                    var = oVarPos[0] #  since it is added, it will not be in iVar, and can only be found in oVar

            elif theId[0] == 'static':
                #
                tuple_type_enclosureId_matchId = (theId[0], theId[1], theId[2], theId[3])
                #
                #convert to patternLabelStartEndPos
                oStaticIdx = theId[3]
                oPatternStaticStartPos, _ = self.oStaticPatternStartEndPositionSansNum[oStaticIdx]

                # oEnclosureId = self.oEnclosureTree[oEnclosureParentId][theId[3]] # this method to check for skipped will not work for MODE1i <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<keep a list of skipped Nodes? [takes up more space, but simplifies logic... not cannot be used for vars]

                # oAbsoluteStaticStartPos, _ = self.oId__data[oEnclosureId]['statics'][matchIdx][oStaticIdx]
                oAbsoluteStaticStartPos, _ = self.oId__data[oEnclosureParentId]['statics'][matchIdx][oStaticIdx]
                oPatternLabelStartPos = oPatternStaticStartPos + oStartPos - oAbsoluteStaticStartPos 
                oSchemeLabelLen = self.nodeId__labelLen___oStr[oNodeId]
                key = (oPatternLabelStartPos, oPatternLabelStartPos+oSchemeLabelLen)# schemeLabelLen might not be the same in oStr?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # print('key: ', key, 'in', self.oTuple_patternLabelStartEndPos__iTuple_patternLabelStartEndPos_iStaticIdx)
                #if this is skipped, then this criterion is wrong<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # if key in self.oTuple_patternLabelStartEndPos__iTuple_patternLabelStartEndPos_iStaticIdx:#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<this should also handle skipNodes
                
                if self.mode == 0:
                    skipCriterion = self.oEnclosureTree[oEnclosureParentId][matchIdx] in self.list_oEnclosureIdSkipped or (key in self.oTuple_patternLabelStartEndPos__iTuple_patternLabelStartEndPos_iStaticIdx)
                elif self.mode == 1:
                    skipCriterion = False #for MODE1, static is always added (never edit), because we don't care about blankspace and iPattern does not have static
                else:
                    skipCriterion = oEnclosureParentId in self.list_oEnclosureIdSkipped or (key in self.oTuple_patternLabelStartEndPos__iTuple_patternLabelStartEndPos_iStaticIdx)
                # print('oEnclosureParentId: ', oEnclosureParentId, 'in', self.list_oEnclosureIdSkipped, skipCriterion); import pdb;pdb.set_trace()

                #seems like this is for MODE2 only?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                
                if skipCriterion: #its edit, 
                    if key in self.oTuple_patternLabelStartEndPos__iTuple_patternLabelStartEndPos_iStaticIdx:
                        _, _, iStaticIdx = self.oTuple_patternLabelStartEndPos__iTuple_patternLabelStartEndPos_iStaticIdx[key]
                    else: #oEnclosureParentId in self.list_oEnclosureIdSkipped
                        iStaticIdx = oStaticIdx # if skipped static was also not changed
                    # iTuple_type_enclosureId_matchId = (theId[0], iEnclosureId, matchIdx, iStaticIdx)
                    if self.mode == 0:
                        iEnclosureParentId = 0#in MODE0 there is only 1 parent.
                    iTuple_type_enclosureId_matchId = (theId[0], iEnclosureParentId, matchIdx, iStaticIdx)

                # else:# added...
            else:#vor hin
                #
                tuple_type_enclosureId_matchId = (theId[0], theId[1], matchIdx)
                #
                if self.mode == 0:
                    iEnclosureParentId = 0#in MODE0 there is only 1 parent.
                iTuple_type_enclosureId_matchId = (theId[0], iEnclosureParentId, matchIdx)#should not use parent, but its own id<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            #
            existing = oTuple_type_enclosureId_matchId__sortedList_tuple_startPos_endPos_nodeId.get(tuple_type_enclosureId_matchId, [])
            existing.append((oStartPos, oEndPos, oNodeId))
            oTuple_type_enclosureId_matchId__sortedList_tuple_startPos_endPos_nodeId[tuple_type_enclosureId_matchId] = existing
            #
            if iTuple_type_enclosureId_matchId is not None: # edited

                sortedList_tuple_startPos_endPos_nodeId = iTuple_type_enclosureId_matchId__sortedList_tuple_startPos_endPos_nodeId[iTuple_type_enclosureId_matchId]

#sortedList_tuple_startPos_endPos_nodeId contains the absolutePos, but we should also have the patternPos...
                for iStartPos, iEndPos, iNodeId in sortedList_tuple_startPos_endPos_nodeId:
                    iw = self.iStr[iStartPos:iEndPos]
                    if ow == iw and iNodeId not in mappedINodeId: #mappedINodeId, should also be cleared for every change in nodeId
                        mappedINodeId.add(iNodeId)

                        schemeNodeChangeLog.append({'d':'e', 't':theId[0], 'in':iNodeId, 'on':oNodeId, 'm':theId[2], 'v':var, 's':iStartPos, 'e':oStartPos, 'iw':iw, 'ow':ow})# now the nodeId 'n' is in scheme

                        break#there is only supposed to be one iSchemeNode for 1 oSchemeNode
                        #for testing please remove
                        # if theId[0] == 'vor' and oStartPos == 17:
                        #     print('please check'); import pdb;pdb.set_trace()
                        #

                #for testing please remove
                # if theId[0] == 'vor' and oStartPos == 17:
                #     print('please check'); import pdb;pdb.set_trace()
                #

            else:
                schemeNodeChangeLog.append({'d':'a', 't':theId[0], 'in':None, 'on':oNodeId, 'm':theId[2], 'v':var, 's':oStartPos, 'e':oEndPos, 'iw':None, 'ow':ow})# now the nodeId 'n' is in scheme

        #for finding removed
        for iStartPos, iEndPos, iNodeId, theIds in iSortedList_tuple_labelPosRangeSchemeIdTheIds:
            theId = theIds[-1] # the last one is the leaf, most specific
            iEnclosureId = theId[1]; matchIdx = theId[2]; oEnclosureId = self.iEnclosureTreeId__oEnclosureTreeId[iEnclosureId];
            oTuple_type_enclosureId_matchId = None#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<this is not used?
            iw = self.iStr[iStartPos:iEndPos]
            if theId[0] == 'var':
                iVarPos = self.iSortedVariablesAndPositionSansNum[theId[3]%len(self.iSortedVariablesAndPositionSansNum)]
                # print('look for b12 ($0, 14)', iVarPos); import pdb;pdb.set_trace()
                # print('iEnclosureId', iEnclosureId, self.list_iEnclosureIdSkipped); import pdb;pdb.set_trace()
                if iEnclosureId not in self.list_iEnclosureIdSkipped and iVarPos not in self.iVarPos__oVarPos: # removed<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<wrong way to check, assume no skipNode
                    #
                    var = iVarPos[0]
                    schemeNodeChangeLog.append({'d':'r', 't':theId[0], 'in':iNodeId, 'on':None, 'm':theId[2], 'v':var, 's':iStartPos, 'e':iEndPos, 'iw':iw, 'ow':None})# now the nodeId 'n' is in scheme

            elif theId[0] == 'static':
                #convert to patternLabelStartEndPos
                iStaticIdx = theId[3]
                iPatternStaticStartPos, _ = self.iStaticPatternStartEndPositionSansNum[iStaticIdx]
                iAbsoluteStaticStartPos, _ = self.iId__data[iEnclosureId]['statics'][matchIdx][iStaticIdx]
                iPatternLabelStartPos = iPatternStaticStartPos + iStartPos - iAbsoluteStaticStartPos 
                # iSchemeLabelLen = self.nodeId__labelLen___iStr[oNodeId]
                iSchemeLabelLen = self.nodeId__labelLen___iStr[iNodeId]
                key = (iPatternLabelStartPos, iPatternLabelStartPos+iSchemeLabelLen)


                if self.mode == 0:
                    skipCriterion = self.oEnclosureTree[iEnclosureId][matchIdx] not in self.list_iEnclosureIdSkipped and key not in self.iTuple_patternLabelStartEndPos__oTuple_patternLabelStartEndPos_oStaticIdx
                elif self.mode == 1: #in mode1, static cannot be removed, because there is not static in iPattern
                    skipCriterion = False
                else:
                    skipCriterion = iEnclosureId not in self.list_iEnclosureIdSkipped and key not in self.iTuple_patternLabelStartEndPos__oTuple_patternLabelStartEndPos_oStaticIdx
                # print('iw', iw)
                # print('iStartPos', iStartPos)
                # print('iPatternStaticStartPos', iPatternStaticStartPos);
                # print('iAbsoluteStaticStartPos', iAbsoluteStaticStartPos)
                # print('iPatternLabelStartPos', iPatternLabelStartPos);
                # print('iSchemeLabelLen', iSchemeLabelLen)
                # # if key not in self.iTuple_patternLabelStartEndPos__oTuple_patternLabelStartEndPos_oStaticIdx:# removed
                # print('iEnclosureId', iEnclosureId, 'not in ', self.list_iEnclosureIdSkipped, ' ', iEnclosureId not in self.list_iEnclosureIdSkipped); import pdb;pdb.set_trace()
                # if self.mode==0:#change to childEnclosureId
                #     iEnclosureId = self.iEnclosureTree[iEnclosureId][matchIdx]
                if skipCriterion:
                    #
                    s = iStartPos; e = iStartPos+ iSchemeLabelLen
                    schemeNodeChangeLog.append({'d':'r', 't':theId[0], 'in':iNodeId, 'on':None, 'm':theId[2], 'v':None, 's':s, 'e':e, 'iw':iw, 'ow':None})# now the nodeId 'n' is in scheme
                    # print(schemeNodeChangeLog); import pdb;pdb.set_trace()

                # print('check<<<<<<<<<<<', iEnclosureId in self.list_iEnclosureIdSkipped); import pdb;pdb.set_trace()
                # elif self.mode == 0 and iEnclosureId in self.list_iEnclosureIdSkipped: # for skipped MODE0
                #     s = iStartPos
                #     e = oStartPos
                #     on = 
                #     ow = 
                #     schemeNodeChangeLog.append({'d':'e', 't':theId[0], 'in':iNodeId, 'on':on, 'm':theId[2], 'v':None, 's':s, 'e':e, 'iw':iw, 'ow':ow})# now the nodeId 'n' is in scheme


        self.schemeNodeChangeLog = schemeNodeChangeLog
        #
        # print('self.iStr')
        # print(self.iStr)
        # print('self.oStr')
        # print(self.oStr)
        # import pprint; pp = pprint.PrettyPrinter(indent=4)
        # print('schemeNodeChangeLog')
        # pp.pprint(self.schemeNodeChangeLog)
        #
            #
            #



    def calculate__startPos__nodeId(self):
        """
        go through each row of schemeNodeChangeLog
        include all the 
        0. d:'e' ~ e
        1. d:'a' ~ s
        """
        maxId = -1
        for _, iNodeId in self.startPos__nodeId___iStr.items():
            # print(iNodeId)
            maxId = max(maxId, iNodeId)
        # print('maxId', maxId); import pdb;pdb.set_trace()
        startPos__nodeId___oStr_new = {}
        for data in self.schemeNodeChangeLog:
            if data['d'] == 'e':
                startPos__nodeId___oStr_new[data['e']] = data['in']
                # maxId = max(maxId, data['in'])
        for data in self.schemeNodeChangeLog:
            if data['d'] == 'a':#need to change data['on'] to a new ID
                maxId += 1
                startPos__nodeId___oStr_new[data['s']] = maxId
        #
        for startPos, nodeId___OLD in self.schemeparser___oStr.startPos__nodeId.items():
            nodeId___NEW = startPos__nodeId___oStr_new[startPos]
            self.OLDSchemeNodeId__NEWSchemeNodeId___oStr[nodeId___OLD] = nodeId___NEW
        #
        self.startPos__nodeId___oStr = startPos__nodeId___oStr_new

    def getNodeId__len___oStr(self):
        if getattr(self, 'nodeId__len___oStr', None) is None:
            #renaming nodeId because recommend.py needs it.
            nodeId__SCHMCK = self.schemeparser___oStr.nodeId__len
            nodeId__SCHMCK___NEW = {}
            for nodeId___OLD, SCHMCK in nodeId__SCHMCK.items():
                nodeId___NEW = self.OLDSchemeNodeId__NEWSchemeNodeId___oStr[nodeId___OLD]
                nodeId__SCHMCK___NEW[nodeId___NEW] = SCHMCK
            self.nodeId__len___oStr = nodeId__SCHMCK___NEW
        return self.nodeId__len___oStr

    def getAST___oStr(self):
        if getattr(self, 'ast___oStr', None) is None:
            #renaming nodeId because recommend.py needs it.
            self.ast___oStr = {}
            stack = [self.schemeparser___oStr.rootOfTree]
            while len(stack) > 0:
                cLabel, cNodeId = stack.pop()
                childNodes = self.schemeparser___oStr.ast.get((cLabel, cNodeId), [])
                stack += childNodes
                childNodes___NEW = []
                for childLabel, childNodeId in childNodes:
                    childNodes___NEW.append((childLabel, self.OLDSchemeNodeId__NEWSchemeNodeId___oStr[childNodeId]))
                if len(childNodes___NEW) > 0:
                    self.ast___oStr[(cLabel, self.OLDSchemeNodeId__NEWSchemeNodeId___oStr[cNodeId])] = childNodes___NEW
                # print('sTEPPTPEPT: ', self.ast___oStr); import pdb;pdb.set_trace()
        # print('self.ast___oStr', self.ast___oStr); import pdb;pdb.set_trace()
        return self.ast___oStr

    def getRootOfTree___oStr(self):
        if getattr(self, 'rootOfTree___oStr', None) is None:
            #renaming nodeId because recommend.py needs it.
            rLabel, rNodeId = self.schemeparser___oStr.rootOfTree
            self.rootOfTree___oStr = (rLabel, self.OLDSchemeNodeId__NEWSchemeNodeId___oStr[rNodeId])

        return self.rootOfTree___oStr



    def make_startPos__argsCount(self): 
        from foundation.automat.common import isNum
        #going to do a simple bracket_accounting, because there is no need to call Schemeparser for this simple task... TODO also done in a lot of places... REFACTOR?
        def countArgsOfSchemeFunction(schemefunctionStr):
            #also takes care of compound_variables like V_{ R_{ 1 } }
            argumentCount = 0
            openBracket__count = {'(':0, '{':0, '[':0}; closeBracket__openBracket = {')':'(', ']':'[', '}':'{'}
            for c in schemefunctionStr:
                if c in openBracket__count:
                    openBracket__count[c] +=1
                elif c in closeBracket__openBracket:
                    openBracket__count[closeBracket__openBracket[c]] -= 1
                if c == ' ' and (not any(map(lambda t: t[1]!=0, openBracket__count.items()))):#NOT(any count not equals 0?)==(all counts are 0)
                    argumentCount += 1
            return argumentCount

        self.schemeId__argCount = {}
        for schemeNodeId, schemeNodeStartPos in self.nodeId__entityStartPos___iStr.items():
            schemeNodeEndPos = self.nodeStartPos__nodeEndPos___iStr[schemeNodeStartPos]
            w = self.iStr[schemeNodeStartPos:schemeNodeEndPos]
            if w[0] == '(':#a function argLen is at least 2? inclusive of it self? the function name?
                #the [1:-1] takes out the startOpenBracket and the endOpenBracket
                self.schemeId__argCount[schemeNodeId] = countArgsOfSchemeFunction(w[1:-1]) + 1 # +1 is the name of the function itself? also differentiates this from variables
            else: #might be a number or variable
                if isNum(w): # argLen is 0 (constant)
                    self.schemeId__argCount[schemeNodeId] = 0
                else: # argLen is 1 (variable)
                    self.schemeId__argCount[schemeNodeId] = 1


    ######################################
    #HELPER FUNCTION
    ######################################
    def variablesConsistent(self, iVar): # there is no need to check for variableConsistency in oVar
        iVar__val = {}
        for iVarPos, (absoluteStartPos, absoluteEndPos) in zip(self.iSortedVariablesAndPosition, iVar):
            iVar = iVarPos[0]
            existingVal = iVar__val.get(iVar, None)
            actualWord = self.iStr[absoluteStartPos:absoluteEndPos]
            if existingVal is not None and actualWord != existingVal:
                return False
            if existingVal is None:
                iVar__val[iVar] = actualWord
        return True



    def renameUserGivenSchemeNodeId(self, nodeId__SCHMCK):
        if getattr(self, 'nodeId__startPos___iStr___OLD', None) is None: # caching
            self.nodeId__startPos___iStr___OLD = dict(map(lambda t: (t[1], t[0]) ,self.startPos__nodeId___iStr___OLD.items()))
        nodeId__SCHMCK___NEW = {}
        for nodeId___OLD, SCHMCK in nodeId__SCHMCK.items():
            startPos___NEW = self.nodeId__startPos___iStr___OLD[nodeId___OLD]
            nodeId__SCHMCK___NEW[self.startPos__nodeId___iStr[startPos___NEW]] = SCHMCK
        return nodeId__SCHMCK___NEW


    def skipNode(self, nodeIdToCheck, matchIdx):
        """


        MODE0 has no iVar, so var will also be None
        for MODE1 and MODE2, the nodeIdToCheck is also some enclosureTreeId, which we need to convert to schemeNodeId first


        Check if nodeIdToCheck [this is in schemeNodeId]
        0. nodeIdToCheck are in the nodeIdsToSkip [user_provided, as in self.startPos__nodeId, if user did not provide self.startPos__nodeId, there should have been a schemeparser.parse and startPos__nodeId should be stored in self]
        1. statisfy minVarArgs [user_provided]
        2. statisfy maxVarArgs [user_provided]
        """
        schemeIdRootOfIPattern = self.tuple_enclosureId_matchId__schemeIdRootOfIPattern.get((nodeIdToCheck, matchIdx))
        userWishToSkip = schemeIdRootOfIPattern in self.nodeIdsToSkip
        # print('checking enclosureId: ', nodeIdToCheck, 'matchIdx', matchIdx, 'schemeIdRootOfIPattern', schemeIdRootOfIPattern, self.nodeIdsToSkip, 'userWishToSkip: ', userWishToSkip)
        if userWishToSkip:
            return userWishToSkip


        if self.mode == 0:
            didNotStatisfyMaxVarArgs = False; didNotStatisfyMinVarArgs = False; #since there are no variables, there is no MaxMinVarArgs to check....
        else:
            numberOfArgs = len(self.iSortedVariablesAndPosition)
            for matchIdx in range(0, len(self.iId__data[nodeIdToCheck]['vars'])):#check every childId of nodeIdToCheck, nodeIdToCheck is the parent
                enclosureChildIds = self.iEnclosureTree[nodeIdToCheck][matchIdx*numberOfArgs: (matchIdx+1)*numberOfArgs]
                for (iVar, iPos), enclosureChildId in zip(self.iSortedVariablesAndPosition, enclosureChildIds):
                    schemeIdRootOfIPattern = self.tuple_enclosureId_matchId__iVarPos__schemeIdRoot[(nodeIdToCheck, matchIdx)][(iVar, iPos)]
                    numberOfArgs = self.schemeId__argCount[schemeIdRootOfIPattern]

                    didNotStatisfyMinVarArgs = self.variableMinArgs.get(iVar, -sys.maxsize -1) > numberOfArgs # get numberOfArgs sys.maxsize because user might not define it, in which case, we take it as user allows it, also neater for the user's configuration.
                    didNotStatisfyMaxVarArgs = self.variableMaxArgs.get(iVar, sys.maxsize) < numberOfArgs # get numberOfArgs
                    if didNotStatisfyMinVarArgs or didNotStatisfyMaxVarArgs:
                        break
                if didNotStatisfyMinVarArgs or didNotStatisfyMaxVarArgs:
                    break


        return didNotStatisfyMinVarArgs or didNotStatisfyMaxVarArgs # then you skip this node

    def getEnclosureNodeId(self):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<rename to getIEnclosureNodeId
        self.newEnclosureNodeCounter += 1
        return self.newEnclosureNodeCounter#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<rename self.newIEnclosureNodeCounter

    def getOEnclosureNodeId(self):
        self.newOEnclosureNodeCounter += 1
        return self.newOEnclosureNodeCounter


    def getNewNodeId(self):# this is schemeNodeId, not EnclosureID
        self.newNodeCounter += 1
        return self.newNodeCounter


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
