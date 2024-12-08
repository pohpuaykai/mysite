class BinarySearch:

    @classmethod
    def binarySearchPre(cls, sortedList, numToInsert, key=None, breakTie='l'):
        if len(sortedList) == 0:
            raise Exception('sortedList cannot be empty')
        if key == None:
            key = lambda x: x
        tookSortedList = list(map(key, sortedList))
        s, e = cls.binarySearchPreK(tookSortedList, numToInsert)
        # print(s, e, '')
        if breakTie == 'l': # take the smallest to break tie
            return cls.smallestBreakTie(tookSortedList, e, numToInsert, s)
        elif breakTie == 'r': # take the largest to break tie
            return cls.largestBreakTie(tookSortedList, e, numToInsert, s)# + 1
        raise Exception('breakTie Enum only l or r')


    @classmethod
    def binarySearchPreK(cls, sortedList, numToInsert):
        """
        assumes that sortedList is sorted ascending

        finds the smallest position i, (there can be repeats in sortedList)
        where
        sortedList[i] < numToInsert <= sortedList[i+1]
        """
        from math import ceil
        s, e = -1, len(sortedList)
        while s+1!=e:
            # print(s, e)
            m = int(ceil((s+e)/2.0))
            if sortedList[m] < numToInsert:# go Right
                s, e = m, e
            else: # go Left
                s, e = s, m
        # print(s, e)
        return s, e
        # if s==0 and sortedList[s] >= numToInsert:
        #     return 0
        # #check for consecutive same numbers in sortedList, that is smaller than s
        # smallerIdx = e
        # for i in range(smallerIdx, -1, -1):
        #     if smallerIdx < len(sortedList) and i < len(sortedList) and sortedList[smallerIdx] == sortedList[i]:
        #         smallerIdx = i
        # return smallerIdx


    @classmethod
    def binarySearchApp(cls, sortedList, numToInsert, key=None, breakTie='l'):
        if len(sortedList) == 0:
            raise Exception('sortedList cannot be empty')
        if key == None:
            key = lambda x: x
        tookSortedList = list(map(key, sortedList))
        s, e = cls.binarySearchAppK(tookSortedList, numToInsert)
        if breakTie == 'l': # take the smallest to break tie
            return cls.smallestBreakTie(tookSortedList, s, numToInsert, s)+1 # tookSortedList[s]==numToInsert
        elif breakTie == 'r': # take the largest to break tie
            return cls.largestBreakTie(tookSortedList, s, numToInsert, s)+1 # tookSortedList[s]==numToInsert
        raise Exception('breakTie Enum only l or r')


    @classmethod
    def binarySearchAppK(cls, sortedList, numToInsert):
        """
        assumes that sortedList is sorted ascending

        finds the smallest position i, (there can be repeats in sortedList)
        where
        sortedList[i] <= numToInsert < sortedList[i+1]
        """
        from math import ceil
        s, e = -1, len(sortedList)
        while s+1!=e:
            # print(s, e)
            m = int(ceil(s+e)/2.0)
            if sortedList[m] <= numToInsert:# go Right
                s, e = m, e
            else: # go Left
                s, e = s, m
        # print(s, e, '<<<<')
        return s, e
        # if s==0 and sortedList[s] >= numToInsert:
        #     return 0
        # #check for consecutive same numbers in sortedList, that is smaller than s
        # smallerIdx = s
        # for i in range(smallerIdx, -1, -1):
        #     if smallerIdx < len(sortedList) and i < len(sortedList) and sortedList[smallerIdx] == sortedList[i]:
        #         smallerIdx = i
        # return smallerIdx + 1



    @classmethod
    def smallestBreakTie(cls, sortedList, smallerIdx, numToInsert, checkZero):
        """
        return the leftmost position if there is a tie
        """
        # if checkZero==0 and sortedList[checkZero] >= numToInsert:
        #     return 0
        # import pdb;pdb.set_trace()
        for i in range(smallerIdx, -1, -1):
            if smallerIdx < len(sortedList) and i < len(sortedList) and sortedList[smallerIdx] == sortedList[i]:
                smallerIdx = i
            # import pdb;pdb.set_trace()
        return smallerIdx

    @classmethod
    def largestBreakTie(cls, sortedList, largerIdx, numToInsert, checkZero):
        """
        return the rightmost position if there is a tie
        """
        # if checkZero==0 and sortedList[checkZero] >= numToInsert:
        #     return 0
        # import pdb;pdb.set_trace()
        for i in range(largerIdx, len(sortedList), 1):
            # print(i, '<<<')
            if largerIdx < len(sortedList) and i < len(sortedList) and sortedList[largerIdx] == sortedList[i]:
                largerIdx = i
        return largerIdx

