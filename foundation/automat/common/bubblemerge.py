class BubbleMerge:


    @classmethod
    def bubbleMerge(cls, ranges, prependable, appendable, handlePrepend, handleAppend):#Does this work like UnionFind YES? construct graph of connectedness between each interval (nlogn - (sort, then linear) comparison if connected?) , then run UnionFind TODO refactor
        from foundation.automat.common.binarysearch import BinarySearch

        import copy
        changed = True
        
        rangesC = copy.deepcopy(ranges)
        while changed:
            changed = False
            originalCopy = copy.deepcopy(rangesC) # for bisectionChecking which need to ignore self
            
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
                prependableIdx = BinarySearch.binarySearchPre(lsByEnd, range0[-1], key=lambda t: t[0])
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
                appendableIdx = BinarySearch.binarySearchApp(lsByStart, range0[0], key=lambda t: t[-1])
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
