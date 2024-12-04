class BubbleMerge:


    @classmethod
    def bubbleMerge(cls, ranges, prependable, appendable, handlePrepend, handleAppend):
        import bisect
        import copy
        changed = True
        
        rangesC = copy.deepcopy(ranges)
        while changed:
            changed = False
            originalCopy = copy.deepcopy(rangesC)
            
            for selfIdx, range0 in enumerate(rangesC):
                del originalCopy[selfIdx]
                #sort range1 by start for bisectingPrepend
                lsByEnd = sorted(originalCopy, key=lambda ranget: ranget[-1], reverse=True)
                prependableIdx = bisect.bisect(lsByEnd, range0[0], key=lambda t: t[-1])
                #check for intersection of range0 and range1
                if prependable(range0, lsByEnd[prependableIdx]):
                    rangesC = handlePrepend(rangesC, range0, lsByEnd[prependableIdx])
                    changed = True
            if changed:
                originalCopy = copy.deepcopy(rangesC)
            #sort range1 by end for bisectingAppend
            #check for append
            for selfIdx, range0 in enumerate(rangesC):
                del originalCopy[selfIdx]
                #sort range1 by start for bisectingAppend
                lsByStart = sorted(originalCopy, key=lambda ranget: ranget[0], reverse=True)
                appendableIdx = bisect.bisect(lsByStart, range0[-1], key=lambda t: t[0])
                lsByStart[appendableIdx]
                if appendable(lsByStart[appendableIdx], range0):
                    rangesC = handleAppend(rangesC, lsByStart[appendableIdx], range0)
                    changed = True
            if changed:
                originalCopy = copy.deepcopy(rangesC)




    # @classmethod
    # def bubbleMerge(cls):
    #     """
    #     input is a list of 1D ranges
    #     a callback for the user to edit the THING associated with those 1D ranges. TODO

    #     # maybe this can be a general algorithm.... grouping by consecutiveness.... even in 3D space... like how bubbles come together to make bigger bubbles (or atoms => molecules :))
        
    #     we do this with bubble-merge, comes with a debugging tool <<ppprint>>
    #     so that we can see whats going on
    #     """
    #     changed = True
    #     while changed:
    #         #sortedConsecutiveGroupsItems = sorted(self.consecutiveGroups.items(), key=lambda item: item[0][0])
    #         changed = False
    #         ###################
    #         if self.showError():
    #             print('@@@@@@@@@@@@@@@@@@@@@@@, reset sortedConsecutiveGroupsItems')
    #             self.ppprint(self.consecutiveGroups, sortedConsecutiveGroupsItems)
    #             print('@@@@@@@@@@@@@@@@@@@@@@@, reset sortedConsecutiveGroupsItems')
    #         ###################
    #         for grenzeRange0, existingDings0 in sortedConsecutiveGroupsItems: # TODO refactor to more dimensions

    #             if changed:
    #                 if self.showError():
    #                     print('BREAKKKKKKKKKKKKKKKKKKKKKKKKKKKK2')
    #                 break
    #             for grenzeRange1, existingDings1 in sortedConsecutiveGroupsItems:
    #                 if grenzeRange0 == grenzeRange1:
    #                     continue
    #                 #########
    #                 if self.showError():
    #                     def slst(existingD):
    #                         nD = []
    #                         for din in existingD:
    #                             if din['type'] == 'infix':
    #                                 dingTup = lambda ding : (ding['name'], ding['position'], ding['position']+len(ding['name']))
    #                             else:
    #                                 dingTup = lambda ding : (ding['name'], ding['ganzStartPos'], ding['ganzEndPos'])
    #                             nD.append(dingTup(din))
    #                         return nD
    #                     print('w', grenzeRange0, slst(existingDings0),'||||||', grenzeRange1, slst(existingDings1))
    #                 #########
    #                 action = rangesConsecutiveInEqsIgnoringSpace(grenzeRange0, grenzeRange1)
    #                 if action is not None:
    #                     if action == 'append':
    #                         newGrenzeRange = (grenzeRange0[0], grenzeRange1[1])
    #                         newExistingDings = existingDings0 + existingDings1
    #                     else: #action == 'prepend'
    #                         newGrenzeRange = (grenzeRange1[0], grenzeRange0[1])
    #                         newExistingDings = existingDings1 + existingDings0
    #                     if grenzeRange0 in self.consecutiveGroups:
    #                         del self.consecutiveGroups[grenzeRange0]
    #                     if grenzeRange1 in self.consecutiveGroups:
    #                         del self.consecutiveGroups[grenzeRange1]
    #                     self.consecutiveGroups[newGrenzeRange] = newExistingDings
    #                     sortedConsecutiveGroupsItems = sorted(self.consecutiveGroups.items(), key=lambda item: item[0][0])
    #                     changed = True
    #                     #############
    #                     if self.showError():
    #                         print('====================', action)
    #                         if action == 'append':
    #                             if ding['type'] == 'infix':
    #                                 dingTup = lambda ding : (ding['name'], ding['position'], ding['position']+len(ding['name']))
    #                             else:
    #                                 dingTup = lambda ding : (ding['name'], ding['ganzStartPos'], ding['ganzEndPos'])
    #                             print(grenzeRange0, list(map(lambda ding: dingTup(ding), existingDings0)))
    #                             print('++++++++++++++++++++')
    #                             print(grenzeRange1, list(map(lambda ding: dingTup(ding), existingDings1)))
    #                         else:
    #                             print(grenzeRange1, list(map(lambda ding: dingTup(ding), existingDings1)))
    #                             print('++++++++++++++++++++')
    #                             print(grenzeRange0, list(map(lambda ding: dingTup(ding), existingDings0)))
    #                         self.ppprint(self.consecutiveGroups, sortedConsecutiveGroupsItems)
    #                         print('====================')
    #                     #############
    #                     if self.showError():
    #                         print('BREAKKKKKKKKKKKKKKKKKKKKKKKKKKKK1')
    #                     break
    #                 if self.showError():
    #                     print('AFTER BREAK1, changed: ', changed)

