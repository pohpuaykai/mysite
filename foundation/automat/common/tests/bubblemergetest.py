from foundation.automat.common.bubblemerge import BubbleMerge


def test__overlappingIntervalsTwoSetsOfIntervals__AllLongestCommonSubString(verbose=False):
    """
    #write test case, use shit from LCS test__oneTermFactorization__moreThanOneCommonString
    """
    rangesRaw = [   
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

    grupp0 = {}
    grupp1 = {}
    for rangeRaw in rangesRaw:
        infoDict0, infoDict1 = rangeRaw
        grupp0[(infoDict0['startPos'], infoDict0['endPos'])] = infoDict0['s']
        grupp1[(infoDict1['startPos'], infoDict1['endPos'])] = infoDict1['s']

    ranges0 = list(grupp0.keys())
    def prependable0(range0, range1):
        return range1[0] <= range0[1] # there is overlap
    def appendable0(range0, range1):
        return range1[0] <= range0[1] # there is overlap
    def handlePrepend0(allRanges, range0, range1):
        #first modify allRanges,
        newRange = (range0[0], range1[1])
        if range0 in allRanges:
            del allRanges[allRanges.index(range0)]
        if range1 in allRanges:
            del allRanges[allRanges.index(range1)]
        allRanges.append(allRanges)
        #then modify grupp0
        str0 = grupp0[range0]
        str1 = grupp0[range1]
        intersectingStr = str0[range1[0]:range0[1]]
        newString = str0[range0[0]:range1[0]] + intersectingStr + str1[range0[1]:range1[1]]
        grupp0[newRange] = newString
        return allRanges
    def handleAppend0(allRanges, range0, range1):
        #first modify allRanges,
        newRange = (range0[0], range1[1])
        if range0 in allRanges:
            del allRanges[allRanges.index(range0)]
        if range1 in allRanges:
            del allRanges[allRanges.index(range1)]
        allRanges.append(allRanges)
        #then modify grupp0
        str0 = grupp0[range0]
        str1 = grupp0[range1]
        intersectingStr = str0[range1[0]:range0[1]]
        newString = str0[range0[0]:range1[0]] + intersectingStr + str1[range0[1]:range1[1]]
        grupp0[newRange] = newString
        return allRanges
    BubbleMerge.bubbleMerge(ranges0, prependable0, appendable0, handlePrepend0, handleAppend0)


    ranges1 = list(grupp1.keys())
    def prependable1(range0, range1):
        return range1[0] <= range0[1] # there is overlap
    def appendable1(range0, range1):
        return range1[0] <= range0[1] # there is overlap
    def handlePrepend1(allRanges, range0, range1):
        #first modify allRanges,
        newRange = (range0[0], range1[1])
        if range0 in allRanges:
            del allRanges[allRanges.index(range0)]
        if range1 in allRanges:
            del allRanges[allRanges.index(range1)]
        allRanges.append(allRanges)
        #then modify grupp1
        str0 = grupp1[range0]
        str1 = grupp1[range1]
        intersectingStr = str0[range1[0]:range0[1]]
        newString = str0[range0[0]:range1[0]] + intersectingStr + str1[range0[1]:range1[1]]
        grupp0[newRange] = newString
        return allRanges
    def handleAppend1(allRanges, range0, range1):
        #first modify allRanges,
        newRange = (range0[0], range1[1])
        if range0 in allRanges:
            del allRanges[allRanges.index(range0)]
        if range1 in allRanges:
            del allRanges[allRanges.index(range1)]
        allRanges.append(allRanges)
        #then modify grupp1
        str0 = grupp1[range0]
        str1 = grupp1[range1]
        intersectingStr = str0[range1[0]:range0[1]]
        newString = str0[range0[0]:range1[0]] + intersectingStr + str1[range0[1]:range1[1]]
        grupp0[newRange] = newString
        return allRanges
    BubbleMerge.bubbleMerge(ranges1, prependable1, appendable1, handlePrepend1, handleAppend1)

    if verbose:
        pp = pprint.PrettyPrinter(indent=4)
        print('grupp0')
        pp.pprint(grupp0)
        print('grupp1')
        pp.pprint(grupp1)


def test__consecutivenessBasedOnAnotherStr__LatexParser_collateBackslashInfixLeftOversToContiguous0(verbose):
    """
    #test case 2 from latexparser # test__findingBackSlashAndInfixOperations__Trig1
    """
    _eqs = '\\sin^2(x) + \\cos^2(x)=1' # TODO change this to self._eqs
    occupiedBrackets = []#TODO

    rangesRaw = {   
    (0, 9): [('sin', 0, 9)],
    (5, 6): [('2', 5, 6)],
    (7, 8): [('x', 7, 8)],
    (10, 11): [('+', 10, 11)],
    (12, 21): [('cos', 12, 21)],
    (17, 18): [('2', 17, 18)],
    (19, 20): [('x', 19, 20)],
    (22, 23): [('1', 22, 23)]}

    expectedRaw = {   
    (0, 21): [('sin', 0, 9), ('+', 10, 11), ('cos', 12, 21)],
    (5, 6): [('2', 5, 6)],
    (7, 8): [('x', 7, 8)],
    (17, 18): [('2', 17, 18)],
    (19, 20): [('x', 19, 20)],
    (22, 23): [('1', 22, 23)]}

    ranges0 = list(rangesRaw.keys())
    def prependable0(range0, range1):
        hikinoko = []
        for hiki in range(range0[1], range1[0]):
            if hiki not in occupiedBrackets:
                hikinoko.append(_eqs[hiki])
        if range0[1]<=range1[0] and len(''.join(hikinoko).strip()) == 0:
            return True
        return False
    def appendable0(range0, range1):
        hikinoko = []
        for hiki in range(range0[1], range1[0]):
            if hiki not in occupiedBrackets:
                hikinoko.append(_eqs[hiki])
        if range0[1]<=range1[0] and len(''.join(hikinoko).strip()) == 0:
            return True
        return False
    def handlePrepend0(allRanges, range0, range1):
        #first modify allRanges,
        newRange = (range0[0], range1[1])
        if range0 in allRanges:
            del allRanges[allRanges.index(range0)]
        if range1 in allRanges:
            del allRanges[allRanges.index(range1)]
        allRanges.append(allRanges)
        #then modify rangesRaw
        list0 = rangesRaw[range0]
        list1 = rangesRaw[range1]
        newList = list0 + list1
        if range0 in rangesRaw:
            del rangesRaw[range0]
        if range1 in rangesRaw:
            del rangesRaw[range1]
        rangesRaw[newRange] = newList
        return allRanges
    def handleAppend0(allRanges, range0, range1):
        #first modify allRanges,
        newRange = (range0[0], range1[1])
        if range0 in allRanges:
            del allRanges[allRanges.index(range0)]
        if range1 in allRanges:
            del allRanges[allRanges.index(range1)]
        allRanges.append(allRanges)
        #then modify rangesRaw
        list0 = rangesRaw[range0]
        list1 = rangesRaw[range1]
        newList = list0 + list1
        if range0 in rangesRaw:
            del rangesRaw[range0]
        if range1 in rangesRaw:
            del rangesRaw[range1]
        rangesRaw[newRange] = newList
        return allRanges
    BubbleMerge.bubbleMerge(ranges0, prependable0, appendable0, handlePrepend0, handleAppend0)
    if verbose:
        pp.pprint('rangesRaw: ', rangesRaw)
        pp.pprint('expectedRaw: ', expectedRaw)
        print('PASSED? ', rangesRaw == expectedRaw)


def test__consecutivenessBasedOnAnotherStr__LatexParser_collateBackslashInfixLeftOversToContiguous1(verbose):
    """
    #test case 3 from latexparser # test__BODMAS__enclosingBracketInBackslashArg
    """
    _eqs = '\\frac{2}{(x-1)(x+1)} = \\frac{1}{x-1} - \\frac{1}{x+1}' # TODO change this to self._eqs
    occupiedBrackets = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 9, 13, 14, 18]#TODO

    rangesRaw = {   
    (0, 20): [('frac', 0, 20)],
    (6, 7): [('2', 6, 7)],
    (10, 11): [('x', 10, 11)],
    (11, 12): [('-', 11, 12)],
    (12, 13): [('1', 12, 13)],
    (15, 16): [('x', 15, 16)],
    (16, 17): [('+', 16, 17)],
    (17, 18): [('1', 17, 18)],
    (23, 36): [('frac', 23, 36)],
    (29, 30): [('1', 29, 30)],
    (32, 33): [('x', 32, 33)],
    (33, 34): [('-', 33, 34)],
    (34, 35): [('1', 34, 35)],
    (37, 38): [('-', 37, 38)],
    (39, 52): [('frac', 39, 52)],
    (45, 46): [('1', 45, 46)],
    (48, 49): [('x', 48, 49)],
    (49, 50): [('+', 49, 50)],
    (50, 51): [('1', 50, 51)]}

    expectedRaw = {   
    (0, 20): [('frac', 0, 20)],
    (6, 7): [('2', 6, 7)],
    (10, 18): [   ('x', 10, 11),
                  ('-', 11, 12),
                  ('1', 12, 13),
                  ('x', 15, 16),
                  ('+', 16, 17),
                  ('1', 17, 18)],
    (23, 52): [('frac', 23, 36), ('-', 37, 38), ('frac', 39, 52)],
    (29, 30): [('1', 29, 30)],
    (32, 35): [('x', 32, 33), ('-', 33, 34), ('1', 34, 35)],
    (45, 46): [('1', 45, 46)],
    (48, 51): [('x', 48, 49), ('+', 49, 50), ('1', 50, 51)]}

    ranges0 = list(rangesRaw.keys())
    def prependable0(range0, range1):
        hikinoko = []
        for hiki in range(range0[1], range1[0]):
            if hiki not in occupiedBrackets:
                hikinoko.append(_eqs[hiki])
        if range0[1]<=range1[0] and len(''.join(hikinoko).strip()) == 0:
            return True
        return False
    def appendable0(range0, range1):
        hikinoko = []
        for hiki in range(range0[1], range1[0]):
            if hiki not in occupiedBrackets:
                hikinoko.append(_eqs[hiki])
        if range0[1]<=range1[0] and len(''.join(hikinoko).strip()) == 0:
            return True
        return False
    def handlePrepend0(allRanges, range0, range1):
        #first modify allRanges,
        newRange = (range0[0], range1[1])
        if range0 in allRanges:
            del allRanges[allRanges.index(range0)]
        if range1 in allRanges:
            del allRanges[allRanges.index(range1)]
        allRanges.append(allRanges)
        #then modify rangesRaw
        list0 = rangesRaw[range0]
        list1 = rangesRaw[range1]
        newList = list0 + list1
        if range0 in rangesRaw:
            del rangesRaw[range0]
        if range1 in rangesRaw:
            del rangesRaw[range1]
        rangesRaw[newRange] = newList
        return allRanges
    def handleAppend0(allRanges, range0, range1):
        #first modify allRanges,
        newRange = (range0[0], range1[1])
        if range0 in allRanges:
            del allRanges[allRanges.index(range0)]
        if range1 in allRanges:
            del allRanges[allRanges.index(range1)]
        allRanges.append(allRanges)
        #then modify rangesRaw
        list0 = rangesRaw[range0]
        list1 = rangesRaw[range1]
        newList = list0 + list1
        if range0 in rangesRaw:
            del rangesRaw[range0]
        if range1 in rangesRaw:
            del rangesRaw[range1]
        rangesRaw[newRange] = newList
        return allRanges
    BubbleMerge.bubbleMerge(ranges0, prependable0, appendable0, handlePrepend0, handleAppend0)
    if verbose:
        pp.pprint('rangesRaw: ', rangesRaw)
        pp.pprint('expectedRaw: ', expectedRaw)
        print('PASSED? ', rangesRaw == expectedRaw)



if __name__=='__main__':
    test__overlappingIntervalsTwoSetsOfIntervals__AllLongestCommonSubString(True) # not tested
    # test__consecutivenessBasedOnAnotherStr__LatexParser_collateBackslashInfixLeftOversToContiguous0(True) # not tested
    # test__consecutivenessBasedOnAnotherStr__LatexParser_collateBackslashInfixLeftOversToContiguous1(True) # not tested