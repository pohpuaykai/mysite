class LongestCommonSubsequence:
    """
    What if in backtracking_step to get the LONGEST_COMMON subsequence, we find ALL_COMMON subsequence, then SCHEMEGRAMMARPARSER will not miss any matches? <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    """
    @classmethod
    def lcssWithEntities(cls, s1, s2, s1Entities, s2Entities):
        """
        
        s1Entities are positions in s1 that should be treated as 1 character
        s2Entities are positions in s2 that should be treated as 1 character

        entities are a list of 2_tuples, where (s, e), s is the startPosition[inclusive], and e is the endPosition[exclusive]
        """
        # print('s1', s1); print('s2', s2)
        s1Entities = sorted(s1Entities, key=lambda d: d[0]) # sort by startPos
        s2Entities = sorted(s2Entities, key=lambda d: d[0]) # sort by startPos
        # m = { s1:s1Entities, s2:s2Entities}; memoLen = {}
        # def leng(st):
        #     if st in memoLen:
        #         return memoLen[st]
        #     entities = m[st]
        #     reducedSum = 0
        #     for s, e in entities:
        #         reducedSum += (e-s - 1) # originally (e-s) length, becomes 1
        #     memoLen[st] = len(st) - reducedSum
        #     return memoLen[st]

        # print('leng(s1)', leng(s1), 'leng(s2)', leng(s2))

        #fill up the gaps of the entities
        def fillGaps(s, entities):
            sAll = []; prevEnd = None
            if entities[0][0] == 0:
                sAll.append(entities[0]); prevEnd = entities[0][1]; idx = 1;
            else:
                sAll.append((0, entities[0][0])); prevEnd = entities[0][0]; idx = 0
            while idx < len(entities):
                entity = entities[idx]
                if prevEnd != entity[0]: # there is gap, but each character must be an entity, and not be grouped together by this
                    for i in range(prevEnd, entity[0]):
                        sAll.append((i, i+1))
                    # sAll.append((prevEnd, entity[0])); 
                    prevEnd = entity[0]
                else: # there is no gap
                    sAll.append(entity); prevEnd = entity[1]
                    idx += 1
            if sAll[-1][1] != len(s):
                for i in range(sAll[-1][1], len(s)):
                    sAll.append((i, i+1))
                # sAll.append((sAll[-1][1], len(s)))
            return sAll
        s1All = fillGaps(s1, s1Entities); s2All = fillGaps(s2, s2Entities)
        # print('s1All', s1All); print('s2All', s2All); import pdb;pdb.set_trace()
        o = { s1:s1All, s2:s2All} # will break if s1 == s2
        def get(st, idx):
            sAll = o[st]
            s, e = sAll[idx]
            return st[s:e]
        def leng(st):
            return len(o[st])
        #normal lcss
        c = [ [0]*(leng(s2)+1) for i in range(leng(s1)+1)]
        b = [ [0]*leng(s2) for i in range(leng(s1))]
        # b = [ [0]*(leng(s2)+1) for i in range(leng(s1)+1)]
        for i in range(1, leng(s1)+1):
            for j in range(1, leng(s2)+1):
                # print('i-1', i-1, 'j-1', j-1)
                # print('comparing: |'+get(s1, i-1)+'| V |'+get(s2, j-1)+'| equals: ', get(s1, i-1) == get(s2, j-1)); import pdb;pdb.set_trace()
                if get(s1, i-1) == get(s2, j-1):
                    c[i][j] = c[i-1][j-1] + 1
                    b[i-1][j-1] = 'd' # took the diagonal
                elif c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i-1][j-1] = 'u'
                else:
                    c[i][j] = c[i][j-1]
                    b[i-1][j-1] = 'l'
        #backtrack
        # print('b', b); import pdb;pdb.set_trace()
        matchedCharPosList = []
        i = leng(s1) - 1
        j = leng(s2) - 1
        while i>=0 and j>=0:
            if b[i][j] == 'd':
                # matchedCharPosList.append((get(s1, i), i, j)) #need to convert i and j to absolutePosition
                a1, e1 = s1All[i]; a2, e2 = s2All[j]
                matchedCharPosList.append((s1[a1:e1], a1, a2)) # absolutePosition
                i -= 1
                j -= 1
            elif b[i][j] == 'u':
                i -= 1
            elif b[i][j] == 'l':
                j -= 1
            else:
                raise Exception('should not happen')

        # print('matchedCharPosList', matchedCharPosList); import pdb;pdb.set_trace()
        #reconstruct the matchStrings
        #
        s1pos__str = {}; s2pos__str = {}; s1pos__s2pos = {}; s2pos__s1pos = {}
        for s, s1pos, s2pos in matchedCharPosList:
            s1pos__str[s1pos] = s
            s2pos__str[s2pos] = s
            s1pos__s2pos[s1pos] = s2pos
            s2pos__s1pos[s2pos] = s1pos
        #
        def groupByConsecutive(theS, theDict, theAll): # theDict are matches
            matchedFrags = []
            word = ''
            wordStartPos = None
            wordEndPos = None

            for entitySPos, entityEPos in theAll:
                if entitySPos in theDict: #entityMatched
                    if len(word) == 0:
                        wordStartPos = entitySPos
                        wordEndPos = entitySPos
                    wordEndPos += len(theDict[entitySPos])
                    word+=theDict[entitySPos]
                else: #entityNOTMatched
                    matchedFrags.append({
                        'w':word,
                        's':wordStartPos,
                        'e':wordEndPos
                    })
                    word = ''
            if len(word) != 0:
                matchedFrags.append({
                    'w':word,
                    's':wordStartPos,
                    'e':wordEndPos
                })
            return matchedFrags

        #
        s1matchedFrags = list(filter(lambda d: len(d['w'])>0, groupByConsecutive(s1, s1pos__str, s1All)))
        s2matchedFrags = list(filter(lambda d: len(d['w'])>0, groupByConsecutive(s2, s2pos__str, s2All)))


        # print('s1matchedFrags', s1matchedFrags); print('s2matchedFrags', s2matchedFrags); import pdb;pdb.set_trace()
        return s1matchedFrags, s2matchedFrags, s1pos__s2pos, s2pos__s1pos

    @classmethod
    def lcssWithEntitiesUnmatched(cls, s1, s2, s1Entities, s2Entities):
        # s1matchedFrags, s2matchedFrags, s1All, s2All = cls.lcssWithEntities(s1, s2, s1Entities, s2Entities)
        s1matchedFrags, s2matchedFrags, s1pos__s2pos, s2pos__s1pos = cls.lcssWithEntities(s1, s2, s1Entities, s2Entities)
        # o = { s1:s1All, s2:s2All} # will break if s1 == s2
        # def leng(st):
        #     return len(o[st])

        iMatchedPos = []
        for m in s1matchedFrags:
            for i in range(m['s'], m['e']): # 
                iMatchedPos.append(i)
        iMatchedPos = sorted(iMatchedPos)
        iUnmatchedPos = sorted(list(set(range(0, len(s1))) - set(iMatchedPos)))#ipattern(unmatched) = removed, len not leng because absolutePosition
        # print('iMatchedPos: ', iMatchedPos); print('iUnmatchedPos: ', iUnmatchedPos); import pdb;pdb.set_trace()

        def collateIntoFrags(rawPattern, unmatchedPos):
            unmatchedFrags = []
            if len(unmatchedPos) == 0:
                return unmatchedFrags
            startPos = unmatchedPos[0]
            endPos = startPos + 1
            word = rawPattern[startPos]#get
            for idx in range(1, len(unmatchedPos)):
                vorpos = unmatchedPos[idx-1]
                hinpos = unmatchedPos[idx]
                if hinpos - 1 == vorpos: #consecutive
                    word += rawPattern[hinpos]
                    endPos = hinpos + 1
                else: #not consecutive
                    unmatchedFrags.append({
                        's':startPos,
                        'e':endPos,
                        'w':word
                    })
                    startPos = hinpos
                    endPos = startPos + 1
                    word = rawPattern[startPos]
            if len(word) > 0:
                unmatchedFrags.append({
                    's':startPos,
                    'e':endPos,
                    'w':word
                })
            return unmatchedFrags

        iUnmatchedFrags = collateIntoFrags(s1, iUnmatchedPos)
        iUnmatchedFrags = sorted(iUnmatchedFrags, key=lambda d: d['s'])

        oMatchedPos = []
        for m in s2matchedFrags:
            for i in range(m['s'], m['e']):
                oMatchedPos.append(i)
        oMatchedPos = sorted(oMatchedPos)
        #matched = unchanged
        oUnmatchedPos = sorted(list(set(range(0, len(s2))) - set(oMatchedPos)))#opattern(unmatched) = added

        oUnmatchedFrags = collateIntoFrags(s2, oUnmatchedPos)
        oUnmatchedFrags = sorted(oUnmatchedFrags, key=lambda d: d['s'])

        s1matchedFrags = sorted(s1matchedFrags, key=lambda d: d['s'])
        s2matchedFrags = sorted(s2matchedFrags, key=lambda d: d['s'])
        return s1matchedFrags, s2matchedFrags, iUnmatchedFrags, oUnmatchedFrags, s1pos__s2pos, s2pos__s1pos


    @classmethod
    def lcssWithEntitiesUnmatchedRejoined(cls, s1, s2, s1Entities, s2Entities):
        s1matchedFrags, s2matchedFrags, iUnmatchedFrags, oUnmatchedFrags, s1pos__s2pos, s2pos__s1pos = cls.lcssWithEntitiesUnmatched(s1, s2, s1Entities, s2Entities)
        import copy
        def interleavingJoin(matched, unmatched):
            matchedCopy = copy.deepcopy(matched)
            unmatchedCopy = copy.deepcopy(unmatched)
            sequence = []
            while len(matchedCopy) > 0 or len(unmatchedCopy) > 0:
                if len(matchedCopy) > 0 and len(unmatchedCopy) > 0:#compare top(matched)['s'] and top(unmatched)['s']
                    if matchedCopy[0]['s'] > unmatchedCopy[0]['s']:
                        d = unmatchedCopy.pop(0)
                        d['matched'] = False
                        sequence.append(d)
                    else:
                        d = matchedCopy.pop(0)
                        d['matched'] = True
                        sequence.append(d)

                elif len(matchedCopy) == 0:
                    for d in unmatchedCopy:
                        d['matched'] = False
                        sequence.append(d)
                    return sequence
                elif len(unmatchedCopy) == 0:
                    for d in matchedCopy:
                        d['matched'] = True
                        sequence.append(d)
                    return sequence
                else:
                    raise Exception('no supposed to happen')
            return sequence
        return s1matchedFrags, s2matchedFrags, iUnmatchedFrags, oUnmatchedFrags, interleavingJoin(s1matchedFrags, iUnmatchedFrags), interleavingJoin(s2matchedFrags, oUnmatchedFrags), s1pos__s2pos, s2pos__s1pos


    @classmethod
    def lcss(cls, s1, s2):
        """
        Courtesy of Cormens' Introduction to Algorithms 4ed
        """
        #DPMemo
        c = [ [0]*(len(s2)+1) for i in range(len(s1)+1)]
        b = [ [0]*len(s2) for i in range(len(s1))]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    c[i][j] = c[i-1][j-1] + 1
                    b[i-1][j-1] = 'd' #took the diagonal
                elif c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i-1][j-1] = 'u'
                else:
                    c[i][j] = c[i][j-1]
                    b[i-1][j-1] = 'l'
        #backtrack
        matchedCharPosList = []
        i = len(s1) - 1
        j = len(s2) - 1
        while i>=0 and j>=0:
            if b[i][j] == 'd':
                matchedCharPosList.append((s1[i], i, j))
                i -= 1
                j -= 1
            elif b[i][j] == 'u':
                i-=1
            elif b[i][j] == 'l':
                j -= 1
            else:
                raise Exception('should not happen')


        #reconstruct the matchStrings
        #
        s1pos__str = {}
        s2pos__str = {}
        for s, s1pos, s2pos in matchedCharPosList:
            s1pos__str[s1pos] = s
            s2pos__str[s2pos] = s
        #
        def groupByConsecutive(theS, theDict):
            matchedFrags = []
            word = ''
            wordStartPos = None
            wordEndPos = None
            for i, c in enumerate(theS):
                if i in theDict:
                    if len(word) == 0:
                        # import pdb;pdb.set_trace()
                        wordStartPos = i
                        wordEndPos = i
                    wordEndPos += 1
                    word += theDict[i]
                else:
                    matchedFrags.append({
                        'w':word,
                        's':wordStartPos,
                        'e':wordEndPos
                    })
                    word = ''
            if len(word) != 0:
                matchedFrags.append({
                    'w':word,
                    's':wordStartPos,
                    'e':wordEndPos
                })

            return matchedFrags
        #
        s1matchedFrags = list(filter(lambda d: len(d['w'])>0, groupByConsecutive(s1, s1pos__str)))
        s2matchedFrags = list(filter(lambda d: len(d['w'])>0, groupByConsecutive(s2, s2pos__str)))


        return s1matchedFrags, s2matchedFrags


    @classmethod
    def lcssWithUnmatched(cls, s1, s2):
        s1matchedFrags, s2matchedFrags = cls.lcss(s1, s2)

        iMatchedPos = []
        for m in s1matchedFrags:
            for i in range(m['s'], m['e']):
                iMatchedPos.append(i)
        iMatchedPos = sorted(iMatchedPos)
        iUnmatchedPos = sorted(list(set(range(0, len(s1))) - set(iMatchedPos)))#ipattern(unmatched) = removed

        def collateIntoFrags(rawPattern, unmatchedPos):
            unmatchedFrags = []
            if len(unmatchedPos) == 0:
                return unmatchedFrags
            startPos = unmatchedPos[0]
            endPos = startPos + 1
            word = rawPattern[startPos]
            for idx in range(1, len(unmatchedPos)):
                vorpos = unmatchedPos[idx-1]
                hinpos = unmatchedPos[idx]
                if hinpos - 1 == vorpos: #consecutive
                    word += rawPattern[hinpos]
                    endPos = hinpos + 1
                else: #not consecutive
                    unmatchedFrags.append({
                        's':startPos,
                        'e':endPos,
                        'w':word
                    })
                    startPos = hinpos
                    endPos = startPos + 1
                    word = rawPattern[startPos]
            if len(word) > 0:
                unmatchedFrags.append({
                        's':startPos,
                        'e':endPos,
                        'w':word
                    })
            return unmatchedFrags

        iUnmatchedFrags = collateIntoFrags(s1, iUnmatchedPos)
        # print('********************************************************')
        iUnmatchedFrags = sorted(iUnmatchedFrags, key=lambda d: d['s'])

        oMatchedPos = []
        for m in s2matchedFrags:
            for i in range(m['s'], m['e']):
                oMatchedPos.append(i)
        oMatchedPos = sorted(oMatchedPos)
        #matched = unchanged
        oUnmatchedPos = sorted(list(set(range(0, len(s2))) - set(oMatchedPos)))#opattern(unmatched) = added

        ####
        # print(iUnmatchedPos)
        # print(oUnmatchedPos)
        ####


        oUnmatchedFrags = collateIntoFrags(s2, oUnmatchedPos)
        oUnmatchedFrags = sorted(oUnmatchedFrags, key=lambda d: d['s'])

        s1matchedFrags = sorted(s1matchedFrags, key=lambda d: d['s'])
        s2matchedFrags = sorted(s2matchedFrags, key=lambda d: d['s'])
        return s1matchedFrags, s2matchedFrags, iUnmatchedFrags, oUnmatchedFrags


    @classmethod
    def lcssWithUnmatchedRejoined(cls, s1, s2):
        s1matchedFrags, s2matchedFrags, iUnmatchedFrags, oUnmatchedFrags = cls.lcssWithUnmatched(s1, s2)
        import copy
        def interleavingJoin(matched, unmatched):
            matchedCopy = copy.deepcopy(matched)
            unmatchedCopy = copy.deepcopy(unmatched)
            sequence = []
            while len(matchedCopy) > 0 or len(unmatchedCopy) > 0:
                if len(matchedCopy) > 0 and len(unmatchedCopy) > 0:#compare top(matched)['s'] and top(unmatched)['s']
                    if matchedCopy[0]['s'] > unmatchedCopy[0]['s']:
                        d = unmatchedCopy.pop(0)
                        d['matched'] = False
                        sequence.append(d)
                    else:
                        d = matchedCopy.pop(0)
                        d['matched'] = True
                        sequence.append(d)

                elif len(matchedCopy) == 0:
                    for d in unmatchedCopy:
                        d['matched'] = False
                        sequence.append(d)
                    return sequence
                elif len(unmatchedCopy) == 0:
                    for d in matchedCopy:
                        d['matched'] = True
                        sequence.append(d)
                    return sequence
                else:
                    raise Exception('no supposed to happen')
            return sequence
        return s1matchedFrags, s2matchedFrags, iUnmatchedFrags, oUnmatchedFrags, interleavingJoin(s1matchedFrags, iUnmatchedFrags), interleavingJoin(s2matchedFrags, oUnmatchedFrags)