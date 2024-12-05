class BubbleMerge:


    @classmethod
    def bubbleMerge(cls, ranges, prependable, appendable, handlePrepend, handleAppend):
        import copy
        changed = True
        
        rangesC = copy.deepcopy(ranges)
        while changed:
            changed = False
            originalCopy = copy.deepcopy(rangesC) # for bisectionChecking which need to ignore self
            
            ###THIS IS ACTUALLY APPEND
            for selfIdx, range0 in enumerate(rangesC):
                # import pdb;pdb.set_trace()
                if range0 in originalCopy:
                    del originalCopy[selfIdx]
                #sort range1 by start for bisectingPrepend, bisect expects ranget[-1] to be in ascending order
                lsByEnd = copy.deepcopy(sorted(originalCopy, key=lambda ranget: ranget[0]))#, reverse=True))
                originalCopy = copy.deepcopy(rangesC) # for bisectionChecking which need to ignore self, get it back
                if len(rangesC) == 1:
                    changed = False
                    break
                prependableIdx = cls.binarySearchPre(lsByEnd, range0[-1], key=lambda t: t[0])
                #############
                # print('P*******************lsByEnd')
                # print(range0, 'in ', lsByEnd, 'len:', len(lsByEnd), 'prependAT:', prependableIdx)
                # print('changed', changed)
                # print('rangesC', rangesC)
                #############
                #check for intersection of range0 and range1
                if (prependableIdx>-1 and prependableIdx<len(lsByEnd)) and prependable(range0, lsByEnd[prependableIdx]):
                    rangesC = handlePrepend(rangesC, range0, lsByEnd[prependableIdx])
                    changed = True
                    originalCopy = copy.deepcopy(rangesC) # for bisectionChecking which need to ignore self
                    # import pdb;pdb.set_trace()

            for selfIdx, range0 in enumerate(rangesC):
                if range0 in originalCopy:
                    del originalCopy[selfIdx]
                #sort range1 by start for bisectingAppend, bisect expects ranget[0] to be in ascending order
                lsByStart = copy.deepcopy(sorted(originalCopy, key=lambda ranget: ranget[-1]))#, reverse=True))
                originalCopy = copy.deepcopy(rangesC) # for bisectionChecking which need to ignore self, get it back
                if len(rangesC) == 1:
                    changed = False
                    break
                appendableIdx = cls.binarySearchApp(lsByStart, range0[0], key=lambda t: t[-1])
                #############
                # print('A*******************lsByStart')
                # print(range0, 'in ', lsByStart, 'len:', len(lsByStart), 'appendAT: ', appendableIdx)
                # print('changed', changed)
                # print('rangesC', rangesC)
                #############
                if (appendableIdx>-1 and appendableIdx<len(lsByStart)) and appendable(lsByStart[appendableIdx], range0):
                    rangesC = handleAppend(rangesC, lsByStart[appendableIdx], range0)
                    changed = True
                    originalCopy = copy.deepcopy(rangesC) # for bisectionChecking which need to ignore self
            ###############
            # print('changed', changed)
            # print('rangesC', rangesC)
            ###############


    @classmethod
    def binarySearchPre(cls, sortedList, numToInsert, key=None):
        if len(sortedList) == 0:
            raise Exception('sortedList cannot be empty')
        if key == None:
            key = lambda x: x
        tookSortedList = list(map(key, sortedList))
        return cls.binarySearchPreK(tookSortedList, numToInsert)


    @classmethod
    def binarySearchPreK(cls, sortedList, numToInsert):
        """
        assumes that sortedList is sorted ascending

        finds the smallest position i, (there can be repeats in sortedList)
        where
        sortedList[i] < numToInsert <= sortedList[i+1]
        """
        from math import ceil
        s, e = 0, len(sortedList)
        while s+1!=e:
            m = int(ceil((s+e)/2.0))
            if sortedList[m] < numToInsert:# go Right
                s, e = m, e
            else: # go Left
                s, e = s, m
        #check for consecutive same numbers in sortedList, that is smaller than s
        smallerIdx = s
        for i in range(s, -1, -1):
            if sortedList[s] == sortedList[i] and i < smallerIdx:
                smallerIdx = i
        return smallerIdx


    @classmethod
    def binarySearchApp(cls, sortedList, numToInsert, key=None):
        if len(sortedList) == 0:
            raise Exception('sortedList cannot be empty')
        if key == None:
            key = lambda x: x
        tookSortedList = list(map(key, sortedList))
        return cls.binarySearchAppK(tookSortedList, numToInsert)


    @classmethod
    def binarySearchAppK(cls, sortedList, numToInsert):
        """
        assumes that sortedList is sorted ascending

        finds the smallest position i, (there can be repeats in sortedList)
        where
        sortedList[i] <= numToInsert < sortedList[i+1]
        """
        from math import ceil
        s, e = 0, len(sortedList)
        while s+1!=e:
            m = int(ceil(s+e)/2.0)
            if sortedList[m] <= numToInsert:# go Right
                s, e = m, e
            else: # go Left
                s, e = s, m
        #check for consecutive same numbers in sortedList, that is smaller than s
        smallerIdx = s
        for i in range(s, -1, -1):
            if sortedList[s] == sortedList[i] and i < smallerIdx:
                smallerIdx = i
        return smallerIdx