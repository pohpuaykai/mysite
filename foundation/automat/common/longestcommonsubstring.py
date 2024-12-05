class LongestCommonSubString:
    """
    Courtesy of https://www.geeksforgeeks.org/longest-common-substring-dp-29/

    We will put in all the algorithm here for now, but only use and test the COOLEST sounding-one, 
    "Space Optimized DP"

    Other might be useful later, if for small cases or special processors or multithreading, 
    their performance outstrips the COOLEST sounding-one

    And also because i am a greedy ass

    """
    @classmethod
    def alcs(cls, s1, s2):
        m = len(s1)
        n = len(s2)
        swapped = False
        #because of how we do the 1D, the longer string has to be s2...
        if m > n: # swap s1 and s2....
            s1, s2, = s2, s1
            m, n = n, m
            swapped = True


        matches = []
        #helper
        def putInMatch(harvestableIndiceHolder, matchesE, swappedE):
            if harvestableIndiceHolder[3] - harvestableIndiceHolder[1] > 1 and harvestableIndiceHolder[2] - harvestableIndiceHolder[0] > 1:
                if swappedE:#TODO refactor
                    matchesE.append([
                    {
                        'startPos':harvestableIndiceHolder[1],
                        'endPos':harvestableIndiceHolder[3],
                        's':s2[harvestableIndiceHolder[1]:harvestableIndiceHolder[3]]
                    },
                    {
                        'startPos':harvestableIndiceHolder[0],
                        'endPos':harvestableIndiceHolder[2],
                        's':s1[harvestableIndiceHolder[0]:harvestableIndiceHolder[2]]
                    }])
                else:
                    matchesE.append([
                    {
                        'startPos':harvestableIndiceHolder[0],
                        'endPos':harvestableIndiceHolder[2],
                        's':s1[harvestableIndiceHolder[0]:harvestableIndiceHolder[2]]
                    }, 
                    {
                        'startPos':harvestableIndiceHolder[1],
                        'endPos':harvestableIndiceHolder[3],
                        's':s2[harvestableIndiceHolder[1]:harvestableIndiceHolder[3]]
                    }])
            return matchesE

        temparrayCount = (max(n, m) + 1)
        indiceHolderIniter = [-1, -1, -1, -1]
        #Create a 1D array to store the previous row's results
        import copy
        prevCoord = [indiceHolderIniter] * temparrayCount # s1_start, s2_start, s1_end, s2_end
        cs = []
        c = ''
        tlcs = ''
        res = 0
        for i in range(1, m + 1):
            take = None
            clear = False
            # Create a temporary array to store the current row
            # print('**', i, '*****************************')
            currCoord = [indiceHolderIniter] * temparrayCount # s1_start, s2_start=-1(no match), s1_end, s2_end
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    currCoord[j] = copy.deepcopy(prevCoord[j - 1])
                    if currCoord[j] == [-1, -1, -1, -1]:
                        currCoord[j][0] = i - 1
                        currCoord[j][1] = j - 1
                    currCoord[j][2] = i
                    currCoord[j][3] = j
            # print(prevCoord)
            # print(currCoord)
            #get our answers :)
            harvestableIdx = None
            for k in range(0, temparrayCount):
                if prevCoord[k] != indiceHolderIniter and currCoord[k] == indiceHolderIniter: #there is something to harvest
                    if harvestableIdx == None: # we also want the longest to be at least length 2
                        harvestableIdx = k
                    harvestableIdx = max(harvestableIdx, k)#we want the last in the consecutive harvestables
            # import pdb;pdb.set_trace()
            if harvestableIdx is not None:
                matches = putInMatch(prevCoord[harvestableIdx], matches, swapped)

            prevCoord = currCoord
        
        #at last get our straggler
        matches = putInMatch(prevCoord[-1], matches, swapped)

        return cls._mergeShardsFromALCS(matches)


    @classmethod
    def _mergeShardsFromALCS(cls, matches):
        """
        matches can only come from alcs
        and an example looks like this:

        matches = [   
        [   {'endPos': 2, 's': '(*', 'startPos': 0},
            {'endPos': 5, 's': '(*', 'startPos': 3}],
        [   {'endPos': 4, 's': ' (', 'startPos': 2},
            {'endPos': 24, 's': ' (', 'startPos': 22}],
        [   {'endPos': 5, 's': ' (+', 'startPos': 2},
            {'endPos': 25, 's': ' (+', 'startPos': 22}],
        [   {'endPos': 7, 's': ' (+ x', 'startPos': 2},
            {'endPos': 27, 's': ' (+ x', 'startPos': 22}],
        [   {'endPos': 8, 's': ' (+ x ', 'startPos': 2},
            {'endPos': 28, 's': ' (+ x ', 'startPos': 22}],
        [   {'endPos': 9, 's': ' x 1', 'startPos': 5},
            {'endPos': 20, 's': ' x 1', 'startPos': 16}],
        [   {'endPos': 12, 's': ') (', 'startPos': 9},
            {'endPos': 24, 's': ') (', 'startPos': 21}],
        [   {'endPos': 13, 's': ') (+', 'startPos': 9},
            {'endPos': 25, 's': ') (+', 'startPos': 21}],
        [   {'endPos': 15, 's': ') (+ x', 'startPos': 9},
            {'endPos': 27, 's': ') (+ x', 'startPos': 21}],
        [   {'endPos': 16, 's': ') (+ x ', 'startPos': 9},
            {'endPos': 28, 's': ') (+ x ', 'startPos': 21}],
        [   {'endPos': 17, 's': ') (+ x 2', 'startPos': 9},
            {'endPos': 29, 's': ') (+ x 2', 'startPos': 21}],
        [   {'endPos': 19, 's': ') (+ x 2))', 'startPos': 9},
            {'endPos': 31, 's': ') (+ x 2))', 'startPos': 21}]]
        """
        from foundation.automat.common.bubblemerge import BubbleMerge

        def mergeGrupp(gruppp):
            ranges0 = list(gruppp.keys())
            def prependable0(range0, range1):
                overlap = range1[0] <= range0[1] and range0[0] <= range1[1] and range0[0] <= range1[0]
                return overlap
                ###touching not allowed, bespiel:
                ###(2, 8): ' (+ x '
                ###(9, 12): ') ('
                # touching = range0[1]+1==range1[0] and range0[0] <= range1[1]
                # return overlap or touching
            def appendable0(range0, range1): 
                overlap = range1[0] <= range0[1] and range0[0] <= range1[1] and range0[0] <= range1[0]
                return overlap
                ###touching not allowed, bespiel:
                ###(2, 8): ' (+ x '
                ###(9, 12): ') ('
                # touching = range0[1]+1==range1[0] and range0[0] <= range1[1]
                # return overlap or touching
            def handlePrepend0(allRanges, range0, range1):
                #first modify allRanges,
                newRange = (min(range0[0], range1[0]), max(range0[1],  range1[1]))
                if range0 in allRanges:
                    del allRanges[allRanges.index(range0)]
                if range1 in allRanges:
                    del allRanges[allRanges.index(range1)]
                allRanges.append(newRange)
                #then modify gruppp
                str0 = gruppp[range0]
                str1 = gruppp[range1]
                if range0[0] <= range1[0] and range1[1] <= range0[1]:
                    newString = str0
                elif range1[0] <= range0[0] and range0[1] <= range1[1]:
                    newString = str1
                elif range0[1]>range1[0]:
                    str0Start = 0
                    str0End = range0[1] - range0[0]
                    str1Start = range1[0] - range0[0]
                    str1End = range1[1] - range0[0]
                    intersectingStr = str0[str1Start:str0End]
                    newString = str0[str0Start:str1Start] + intersectingStr + str1[str0End-str1Start:]
                    # import pdb;pdb.set_trace()
                elif range0[1]==range1[0] or range0[1]+1==range1[0]:#touching
                    newString = str0+str1
                if range0 in gruppp:
                    del gruppp[range0]
                if range1 in gruppp:
                    del gruppp[range1]
                gruppp[newRange] = newString
                # import pdb;pdb.set_trace()
                return allRanges
            def handleAppend0(allRanges, range0, range1):
                #first modify allRanges,
                newRange = (min(range0[0], range1[0]), max(range0[1],  range1[1]))
                if range0 in allRanges:
                    del allRanges[allRanges.index(range0)]
                if range1 in allRanges:
                    del allRanges[allRanges.index(range1)]
                allRanges.append(newRange)
                #then modify gruppp
                str0 = gruppp[range0]
                str1 = gruppp[range1]
                if range0[0] <= range1[0] and range1[1] <= range0[1]:
                    newString = str0
                elif range1[0] <= range0[0] and range0[1] <= range1[1]:
                    newString = str1
                elif range0[1]>range1[0]:
                    str0Start = 0
                    str0End = range0[1] - range0[0]
                    str1Start = range1[0] - range0[0]
                    str1End = range1[1] - range0[0]
                    intersectingStr = str0[str1Start:str0End]
                    newString = str0[str0Start:str1Start] + intersectingStr + str1[str0End-str1Start:]
                    # import pdb;pdb.set_trace()
                elif range0[1]==range1[0] or range0[1]+1==range1[0]:#touching
                    newString = str0+str1
                if range0 in gruppp:
                    del gruppp[range0]
                if range1 in gruppp:
                    del gruppp[range1]
                gruppp[newRange] = newString
                return allRanges
            BubbleMerge.bubbleMerge(ranges0, prependable0, appendable0, handlePrepend0, handleAppend0)

        grupp0 = {}
        grupp1 = {}
        for rangeRaw in matches:
            infoDict0, infoDict1 = rangeRaw
            grupp0[(infoDict0['startPos'], infoDict0['endPos'])] = infoDict0['s']
            grupp1[(infoDict1['startPos'], infoDict1['endPos'])] = infoDict1['s']

        mergeGrupp(grupp0)
        mergeGrupp(grupp1)
        return grupp0, grupp1




    @classmethod
    def lcs(cls, s1, s2):
        m = len(s1)
        n = len(s2)
        #because of how we do the 1D, the longer string has to be s2...
        if m > n: # swap s1 and s2....
            s1, s2, = s2, s1
            m, n = n, m

        #Create a 1D array to store the previous row's results
        prev = [0] * (max(n, m) + 1)# * range(1, m + 1)
        prevStr = [''] * (max(n, m) + 1)
        cs = []
        c = ''
        tlcs = ''
        res = 0
        for i in range(1, m + 1):
            take = None
            clear = False
            # Create a temporary array to store the current row
            curr = [0] * (max(n, m) + 1)
            currStr = [''] * (max(n, m) + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                    res = max(res, curr[j])
                    #logic for which side to take
                    currStr[j] = prevStr[j - 1] + s2[j - 1]
                else:
                    curr[j] = 0
                    currStr[j] = ''

            # Move the current row's data to the previous row
            prev = curr
            prevStr = currStr
        #find the longest to return
        longestCommonSubString = ''
        for s in prevStr:
            if len(s) > len(longestCommonSubString):
                longestCommonSubString = s
        return longestCommonSubString



    #Other less COOL algorithms~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @classmethod
    def __allpairs__lcs(cls, s1, s2): # TODO untested
        m = len(s1)
        n = len(s2)

        res = 0

        # Consider every pair of index and find the length
        # of the longest common substring beginning with
        # every pair. Finally return max of all maximums
        for i in range(m):
            for j in range(n):
                curr = 0
                while (i + curr) < m and (j + curr) < n and s1[i + curr] == s2[j + curr]:
                    curr += 1
                res = max(res, curr)
        return res

    @classmethod
    def __recursive__lcs(cls, s1, s2): #TODO untested
        m = len(s1)
        n = len(s2)

        res = 0

        def commonSuffix(s1, s2, sl1, sl2):
            if sl1 == 0 or sl2 == 0 or s1[sl1 - 1] != s2[sl2 - 1]:
                return 0
            return 1 + commonSuffix(s1, s2, sl1 - 1, sl2 - 1)

        # Find the longest common substring ending
        # at every pair of characters and take the 
        # maximum of all.
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                res = max(res, commonSuffix(s1, s2, i, j))
        return res


    @classmethod
    def __dynamicProgramming__lcs(cls, s1, s2):
        m = len(s1)
        n = len(s2)

        # Create a table to store lengths of longest
        # common suffixes of substrings.
        LCSuf = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0

        # Build LCSuf[m+1][n+1] in bottom-up fashion.
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    LCSuf[i][j] = LCSuf[i - 1][j - 1] + 1
                    res = max(res, LCSuf[i][j])
                else:
                    LCSuf[i][j] = 0

        return res