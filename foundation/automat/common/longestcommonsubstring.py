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
        return matches


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