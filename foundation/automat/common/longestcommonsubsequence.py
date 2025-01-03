class LongestCommonSubsequence:
    """

    """
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