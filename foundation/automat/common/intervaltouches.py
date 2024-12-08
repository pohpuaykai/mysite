class IntervalTouches:

    TOUCHES_ENUM = [
    'e', #things that Enclose interval
    'l', #things that touch Left of interval 
    'r', #things that touch Right of interval
    'c'  #things that interval Cover
    ]

    @classmethod
    def intervalnDTouchesEachOtherAt(cls, intervalList):
        """
        TODO test

        TODO AddOn to longestcommonsubstring.py:LongestCommonSubString.alcs(cls)

        listTemplateKey is a key for list of other intervals, describing how other intervals TOUCH it
        listTemplateKey example:
        cerelle
          ^
        touch interval at the Right at 3rd dimension (because r is the 3rd character of listTemplateKey)

        interval2D = rectangle

        :param intervalList: list of list L of 2-tuples tup. 
        each index of L is a dimension
        tup[0]=StartPos_of_tup, tup[1]=EndPos_of_tup
        :type intervalList: list[list[tuple[float]]]
        """
        #generate listTemplateKey s
        dim = len(intervalList[0]) # what dimensional world is this?
        listTemplateKeys = []
        numberToTOUCHESENUM__replacementDict = dict(zip(['0', '1', '2', '3'], IntervalTouches.TOUCHES_ENUM))
        for n in range(0, pow(len(IntervalTouches.TOUCHES_ENUM), dim)):
            unflavouredKey = cls.toFilledStr(n, len(IntervalTouches.TOUCHES_ENUM), dim)
            for num, TENum in numberToTOUCHESENUM__replacementDict.items():
                unflavouredKey = unflavouredKey.replace(num, TENum)
            listTemplateKeys.append(unflavouredKey)


        #put intervalIdx in each interval
        newIntervalList = []
        for intervalIdx, interval in enumerate(intervalList):
            newIntervalList.append((tuple(interval), intervalIdx))
        oldIntervalList, intervalList = intervalList, newIntervalList

        #basically a tranpose of the intervalList (before adding tags)
        intervalsByDimension = []
        dimension__intervalFragments = dict(map(lambda dimension: (dimension, []), range(0, dim)))
        for intervalWithIdx in intervalList:
            interval, intervalIdx = intervalWithIdx
            for dimensionNum, intervalFragment in enumerate(interval):
                dimension__intervalFragments[dimensionNum].append((intervalFragment, intervalIdx))
        for dimension, dimensionalSlice in sorted(dimension__intervalFragments.items(), key=lambda t: t[0]): # sort by dimension
            intervalsByDimension.append(dimensionalSlice)

        # import pdb;pdb.set_trace()
        #init the template for cls.interval1DTouchesEachOtherAt
        interval__touchersFragments = {}
        for listIdx in range(0, len(intervalList)):
            dimensionDict = {}
            for dimensionIdx in range(0, dim):
                dimensionDict[dimensionIdx] = {}
            interval__touchersFragments[listIdx] = dimensionDict


        for intervalDimensionNum, dimensionList in enumerate(intervalsByDimension):#dimension
            #################
            # print('*********************************', intervalDimensionNum)
            # print(dimensionList)
            # import pdb;pdb.set_trace()
            #################
            intervalInfoDicts = cls.interval1DTouchesEachOtherAt(dimensionList)
            ###################
            # print('***********************', intervalDimensionNum)
            # print('dimensionList:', dimensionList)
            # import pprint
            # pp = pprint.PrettyPrinter(indent=4)
            # SintervalInfoDicts = dict(map(lambda d: (d['interval'], d['toucherInfoDict']), intervalInfoDicts))
            # print('SintervalInfoDicts')
            # pp.pprint(SintervalInfoDicts)
            
            ###################
            for intervalInfoDict in intervalInfoDicts:
                toucherFragmentInfoDict = {}
                # import pdb;pdb.set_trace()
                for touchEnum, toucherFragments in intervalInfoDict['toucherInfoDict'].items():
                    for toucherFragment in toucherFragments:
                        (startPos, endPos), userIdx = toucherFragment
                        toucherFragmentInfoDict[userIdx] = (startPos, endPos, touchEnum) # if use dict with userIdx as key
                interval__touchersFragments[intervalInfoDict['idxInInputList']][intervalDimensionNum] = toucherFragmentInfoDict

        # import pdb;pdb.set_trace()


        #prepare return format
        intervalTouchers = {}
        for intervalWithIdx in intervalList:
            interval, intervalIdx = intervalWithIdx
            touchTypes__touchers = {}
            for touchType in listTemplateKeys:
                touchTypes__touchers[touchType] = []
            intervalTouchers[tuple(intervalWithIdx)] = touchTypes__touchers


        for intervalIdx, interval in enumerate(intervalList):
            touchers = []#each interval has templatekey: a bunch of touchers
            toucherFragments = interval__touchersFragments[intervalIdx][0] # start at dimension 0
            for userIdx, toucherFragment in toucherFragments.items():
                cannotReconstructToucher = False
                startPos, endPos, touchEnum = toucherFragment
                toucher = [(startPos, endPos)]
                how = touchEnum
                currentDimension = 1
                while dim - currentDimension > 0:
                    toucherFragmentsOfCurrentDimensions = interval__touchersFragments[intervalIdx][currentDimension]
                    nextToucherFragment = toucherFragmentsOfCurrentDimensions.get(userIdx)
                    if nextToucherFragment is None:
                        cannotReconstructToucher = True
                        break
                    else:
                        startPos, endPos, touchEnum = nextToucherFragment
                        toucher.append((startPos, endPos))
                        how += touchEnum
                    currentDimension += 1
                if not cannotReconstructToucher:
                    touchers.append((how, toucher))
            ###########
            # print(intervalIdx, interval, '******')
            # print(touchers, how)
            ###########
            for how, toucher in touchers:
                intervalTouchers[tuple(interval)][how].append(toucher)

        return intervalTouchers


    @classmethod
    def interval1DTouchesEachOtherAt(cls, intervalList):
        """

        TODO use this to refactor EnclosureTree
        TODO use this to refactor BubbleMerge?
        TODO use this to refactor Latexparser (enclosing bracket finding)

        intervalList = [((1, 3), 0), ((5, 7), 1), ((8, 9), 2)] # ((startPos, endPos), tag)

        :param intervalList: list of 2-tuples tup. tup[0]=StartPos_of_tup, tup[1]=EndPos_of_tup
        :type intervalList: list[tuple[float]]
        """
        from foundation.automat.common.binarysearch import BinarySearch

        #Courtesey of ChatGPT
        # def appComparator(a, b):
        #     if a < b:
        #         return -1
        #     else:
        #         return 1
        # def preComparator(a, b):
        #     if a <= b:
        #         return -1
        #     else:
        #         return 1

        sortedByStaAsc = sorted(intervalList, key=lambda interval: interval[0][0])
        sortedByEndDes = sorted(intervalList, key=lambda interval: interval[0][1])#, reverse=True)
        # from functools import cmp_to_key
        # sortedByStaApp = sorted(intervalList, key=cmp_to_key(lambda i0, i1: appComparator(i0[0][0], i1[0][0])))
        # sortedByStaPre = sorted(intervalList, key=cmp_to_key(lambda i0, i1: preComparator(i0[0][0], i1[0][0])))
        # sortedByEndApp = sorted(intervalList, key=cmp_to_key(lambda i0, i1: appComparator(i0[0][1], i1[0][1])))
        # sortedByEndPre = sorted(intervalList, key=cmp_to_key(lambda i0, i1: preComparator(i0[0][1], i1[0][1])))
        # sortedByStaAscNoId = list(map(lambda t: t[0], sortedByStaAsc))
        # sortedByEndDesNoId = list(map(lambda t: t[0], sortedByEndDes))


        startPosSorted = sorted(list(map(lambda interval: interval[0][0], intervalList)))
        endPosSorted = sorted(list(map(lambda interval: interval[0][1], intervalList)))

        intervalInfoDicts = []
        for idx, interval in enumerate(intervalList):
            isl = BinarySearch.binarySearchPre(startPosSorted, interval[0][0], breakTie='l')# 1234|55555, TODO PreMustBeWith'l', write a wrapper to simplify this
            isr = BinarySearch.binarySearchApp(startPosSorted, interval[0][0], breakTie='r')# 123455555|, TODO AppMustBeWith'r', write a wrapper to simplify this
            iel = BinarySearch.binarySearchPre(endPosSorted, interval[0][1], breakTie='l')# 1234|55555, TODO PreMustBeWith'l', write a wrapper to simplify this
            ier = BinarySearch.binarySearchApp(endPosSorted, interval[0][1], breakTie='r') # 123455555|, TODO AppMustBeWith'r', write a wrapper to simplify this

            # ilsp = sortedByStaPre.index(interval)#sortedList[i][0] <= numToInsert[0] < sortedList[i+1][0]
            # ilsa = sortedByStaApp.index(interval)#sortedList[i][0] < numToInsert[0] <= sortedList[i+1][0]
            # ilep = sortedByEndPre.index(interval)#sortedList[i][1] <= numToInsert[1] < sortedList[i+1][1]
            # ilea = sortedByEndApp.index(interval)#sortedList[i][1] < numToInsert[1] <= sortedList[i+1][1]
            ##################correct
            # print('interval', interval[0])
            # print('startPosSorted', startPosSorted)
            # print('endPosSorted', endPosSorted)
            # print('isl 1234|55555', isl)
            # print('isr 123455555|', isr)
            # print('iel 1234|55555', iel)
            # print('ier 123455555|', ier)
            ##################
            llsl = sortedByStaAsc[:isr]#t[0]<=interval[0]
            llst = sortedByStaAsc[:isl]#t[0] < interval[0]
            lrst = sortedByStaAsc[isr:]#interval[0]<t[0]
            lrsl = sortedByStaAsc[isl:]#interval[0] <= t[0]
            llel = sortedByEndDes[:ier]#t[1]<=interval[1]
            llet = sortedByEndDes[:iel]#t[1] < interval[1]
            lret = sortedByEndDes[ier:]#interval[1]<t[1]
            lrel = sortedByEndDes[iel:]#interval[1] <= t[1]
            
            ################
            # print('*******************')
            # print('interval', interval[0])
            # print('startPosSorted', startPosSorted)
            # print('endPosSorted', endPosSorted)
            # print('t[0]<=interval[0] llsl', llsl)
            # print('t[0] < interval[0] llst', llst)
            # print('interval[0]<t[0] lrst', lrst)
            # print('interval[0] <= t[0] lrsl', lrsl)
            # print('t[1]<=interval[1] llel', llel)
            # print('t[1] < interval[1] llet', llet)
            # print('interval[1]<t[1] lret', lret)
            # print('interval[1] <= t[1] lrel', lrel)
            # print('*******************')
            ################

            #enclosing: we want t[0]<=interval[0] & interval[1]<=t[1]
            s00 = list(set(llsl).intersection(set(lrel)) - set([interval]))
            #s00 = list(set(lls).intersection(set(lre)) - set([interval]))#t[0]<=interval[0] & interval[1]<t[1]

            #touches left of interval: we want t[0]<interval[0] & t[1]<interval[1] 
            s01 = list(set(llst).intersection(set(llet)) - set([interval]))
            # s01 = list(set(lls).intersection(set(lle)) - set([interval]))#t[0]<=interval[0] & t[1]<=interval[1] 
            if len(s01) > 0:
                #(for intersecting, we also need interval[0] <= t[1])
                s01 = sorted(s01, key=lambda t: t[0][1]) # assume always have an ID tagged to it
                s01NoId = list(map(lambda t: t[0], s01))
                cutIdx = BinarySearch.binarySearchPre(s01NoId, interval[0][0], key=lambda t: t[1], breakTie='l')
                # import pdb;pdb.set_trace()
                s01 = s01[cutIdx:]

            #touches right of interval: we want interval[0]<t[0] & interval[1]<t[1] 
            s10 = list(set(lrst).intersection(set(lret)) - set([interval]))
            # s10 = list(set(lrs).intersection(set(lre)) - set([interval]))#interval[0]<t[0] & interval[1]<t[1] 
            if len(s10) > 0:
                #(for intersecting, we also need t[0] <= interval[1])
                s10 = sorted(s10, key=lambda t: t[0][0]) # assume always have an ID tagged to it
                s10NoId = list(map(lambda t: t[0], s10))
                cutIdx = BinarySearch.binarySearchPre(s10NoId, interval[0][1], key=lambda t: t[0], breakTie='l')
                s10 = s10[:cutIdx]

            #covering: we want interval[0]<t[0] & t[1]<interval[1]
            s11 = list(set(lrst).intersection(set(llet)) - set([interval]))
            # s11 = list(set(lrs).intersection(set(lle)) - set([interval]))#interval[0]<t[0] & t[1]<=interval[1]

            #sort by listID before inserting...
            s00 = sorted(s00, key=lambda t: intervalList.index(t))
            s01 = sorted(s01, key=lambda t: intervalList.index(t))
            s10 = sorted(s10, key=lambda t: intervalList.index(t))
            s11 = sorted(s11, key=lambda t: intervalList.index(t))
            # intervalToIntersects[interval] = {
            #     'e':s00,
            #     'l':s01,
            #     'r':s10,
            #     'c':s11 
            # }
            intervalInfoDicts.append({
                'idxInInputList':idx,
                'interval':interval,
                'toucherInfoDict':dict(zip(IntervalTouches.TOUCHES_ENUM, [s00, s01, s10, s11]))

            })
        return intervalInfoDicts





    @classmethod
    def toFilledStr(cls, n, base, fillWithZeroTil):
        """
        Courtesey of ChatGPT
        """
        if n == 0:
            unfilledStr = "0"
        symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        if base > len(symbols):
            raise ValueError("Base too large")
        result = []
        while n:
            result.append(symbols[n % base])
            n //= base
        unfilledStr = ''.join(result)
        zerosToAdd = fillWithZeroTil - len(unfilledStr)
        if zerosToAdd > 0:
            unfilledStr += symbols[0] * zerosToAdd
        return unfilledStr

