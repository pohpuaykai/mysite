import inspect
import pprint

from foundation.automat.common.intervaltouches import IntervalTouches

pp = pprint.PrettyPrinter(indent=4)


def test__1dTouchingIntervals__sameIntervals(verbose=False):
    intervalList = [
        ((0, 3), 0), #e
        ((0, 3), 1) # e
    ]
    touchesInfoDicts = IntervalTouches.interval1DTouchesEachOtherAt(intervalList)
    expected = [   {   'idxInInputList': 0,
        'interval': ((0, 3), 0),
        'toucherInfoDict': {'c': [], 'e': [((0, 3), 1)], 'l': [], 'r': []}},
    {   'idxInInputList': 1,
        'interval': ((0, 3), 1),
        'toucherInfoDict': {'c': [], 'e': [((0, 3), 0)], 'l': [], 'r': []}}]
    print('PASSED? ', expected==touchesInfoDicts)
    if verbose:
        pp.pprint(touchesInfoDicts)


def test__1dTouchingIntervals__leftRightIntervalsFrom2DCase(verbose=False):
    intervalList = [
        ((0, 3), 0), #left
        ((2, 5), 1) # right
    ]
    touchesInfoDicts = IntervalTouches.interval1DTouchesEachOtherAt(intervalList)
    expected = [   {   'idxInInputList': 0,
        'interval': ((0, 3), 0),
        'toucherInfoDict': {'c': [], 'e': [], 'l': [], 'r': [((2, 5), 1)]}},
    {   'idxInInputList': 1,
        'interval': ((2, 5), 1),
        'toucherInfoDict': {'c': [], 'e': [], 'l': [((0, 3), 0)], 'r': []}}]
    print('PASSED? ', expected==touchesInfoDicts)
    if verbose:
        pp.pprint(touchesInfoDicts)


def test__1dTouchingIntervals__smallerCaseFrom2DAllPairsDimension0(verbose=False):
    intervalList = [
        ((0, 3), 0), 
        ((0, 3), 1), 
        ((0, 3), 2), 
        ((0, 3), 3), 
        ((2, 5), 4), 
        ((2, 5), 5), 
        ((2, 5), 6)
    ]
    touchesInfoDicts = IntervalTouches.interval1DTouchesEachOtherAt(intervalList)
    expected = [   {   'idxInInputList': 0,
        'interval': ((0, 3), 0),
        'toucherInfoDict': {   'c': [],
                               'e': [((0, 3), 1), ((0, 3), 2), ((0, 3), 3)],
                               'l': [],
                               'r': [((2, 5), 4), ((2, 5), 5), ((2, 5), 6)]}},
    {   'idxInInputList': 1,
        'interval': ((0, 3), 1),
        'toucherInfoDict': {   'c': [],
                               'e': [((0, 3), 0), ((0, 3), 2), ((0, 3), 3)],
                               'l': [],
                               'r': [((2, 5), 4), ((2, 5), 5), ((2, 5), 6)]}},
    {   'idxInInputList': 2,
        'interval': ((0, 3), 2),
        'toucherInfoDict': {   'c': [],
                               'e': [((0, 3), 0), ((0, 3), 1), ((0, 3), 3)],
                               'l': [],
                               'r': [((2, 5), 4), ((2, 5), 5), ((2, 5), 6)]}},
    {   'idxInInputList': 3,
        'interval': ((0, 3), 3),
        'toucherInfoDict': {   'c': [],
                               'e': [((0, 3), 0), ((0, 3), 1), ((0, 3), 2)],
                               'l': [],
                               'r': [((2, 5), 4), ((2, 5), 5), ((2, 5), 6)]}},
    {   'idxInInputList': 4,
        'interval': ((2, 5), 4),
        'toucherInfoDict': {   'c': [],
                               'e': [((2, 5), 5), ((2, 5), 6)],
                               'l': [   ((0, 3), 0),
                                        ((0, 3), 1),
                                        ((0, 3), 2),
                                        ((0, 3), 3)],
                               'r': []}},
    {   'idxInInputList': 5,
        'interval': ((2, 5), 5),
        'toucherInfoDict': {   'c': [],
                               'e': [((2, 5), 4), ((2, 5), 6)],
                               'l': [   ((0, 3), 0),
                                        ((0, 3), 1),
                                        ((0, 3), 2),
                                        ((0, 3), 3)],
                               'r': []}},
    {   'idxInInputList': 6,
        'interval': ((2, 5), 6),
        'toucherInfoDict': {   'c': [],
                               'e': [((2, 5), 4), ((2, 5), 5)],
                               'l': [   ((0, 3), 0),
                                        ((0, 3), 1),
                                        ((0, 3), 2),
                                        ((0, 3), 3)],
                               'r': []}}]
    print('PASSED? ', expected==touchesInfoDicts)
    if verbose:
        pp.pprint(touchesInfoDicts)


def test__1dTouchingIntervals__smallerCaseFrom2DAllPairsDimension1(verbose=False):
    intervalList = [
        ((6, 9), 2),
        ((8, 11), 3),
        ((4, 7), 5),
        ((8, 11), 6),
        ((6, 9), 8),
        ((4, 7), 10),
        ((8, 11), 11),
        ((6, 9), 14),
        ((8, 11), 15)
    ]
    touchesInfoDicts = IntervalTouches.interval1DTouchesEachOtherAt(intervalList)
    expected = [   {   'idxInInputList': 0,
        'interval': ((6, 9), 2),
        'toucherInfoDict': {   'c': [],
                               'e': [((6, 9), 8), ((6, 9), 14)],
                               'l': [((4, 7), 5), ((4, 7), 10)],
                               'r': [   ((8, 11), 3),
                                        ((8, 11), 6),
                                        ((8, 11), 11),
                                        ((8, 11), 15)]}},
    {   'idxInInputList': 1,
        'interval': ((8, 11), 3),
        'toucherInfoDict': {   'c': [],
                               'e': [   ((8, 11), 6),
                                        ((8, 11), 11),
                                        ((8, 11), 15)],
                               'l': [((6, 9), 2), ((6, 9), 8), ((6, 9), 14)],
                               'r': []}},
    {   'idxInInputList': 2,
        'interval': ((4, 7), 5),
        'toucherInfoDict': {   'c': [],
                               'e': [((4, 7), 10)],
                               'l': [],
                               'r': [((6, 9), 2), ((6, 9), 8), ((6, 9), 14)]}},
    {   'idxInInputList': 3,
        'interval': ((8, 11), 6),
        'toucherInfoDict': {   'c': [],
                               'e': [   ((8, 11), 3),
                                        ((8, 11), 11),
                                        ((8, 11), 15)],
                               'l': [((6, 9), 2), ((6, 9), 8), ((6, 9), 14)],
                               'r': []}},
    {   'idxInInputList': 4,
        'interval': ((6, 9), 8),
        'toucherInfoDict': {   'c': [],
                               'e': [((6, 9), 2), ((6, 9), 14)],
                               'l': [((4, 7), 5), ((4, 7), 10)],
                               'r': [   ((8, 11), 3),
                                        ((8, 11), 6),
                                        ((8, 11), 11),
                                        ((8, 11), 15)]}},
    {   'idxInInputList': 5,
        'interval': ((4, 7), 10),
        'toucherInfoDict': {   'c': [],
                               'e': [((4, 7), 5)],
                               'l': [],
                               'r': [((6, 9), 2), ((6, 9), 8), ((6, 9), 14)]}},
    {   'idxInInputList': 6,
        'interval': ((8, 11), 11),
        'toucherInfoDict': {   'c': [],
                               'e': [((8, 11), 3), ((8, 11), 6), ((8, 11), 15)],
                               'l': [((6, 9), 2), ((6, 9), 8), ((6, 9), 14)],
                               'r': []}},
    {   'idxInInputList': 7,
        'interval': ((6, 9), 14),
        'toucherInfoDict': {   'c': [],
                               'e': [((6, 9), 2), ((6, 9), 8)],
                               'l': [((4, 7), 5), ((4, 7), 10)],
                               'r': [   ((8, 11), 3),
                                        ((8, 11), 6),
                                        ((8, 11), 11),
                                        ((8, 11), 15)]}},
    {   'idxInInputList': 8,
        'interval': ((8, 11), 15),
        'toucherInfoDict': {   'c': [],
                               'e': [((8, 11), 3), ((8, 11), 6), ((8, 11), 11)],
                               'l': [((6, 9), 2), ((6, 9), 8), ((6, 9), 14)],
                               'r': []}}]
    print('PASSED? ', expected==touchesInfoDicts)
    if verbose:
        pp.pprint(touchesInfoDicts)


def test__1dTouchingIntervals__leftRightIntervals(verbose=False):
    intervalList = [
        ((4, 7), 0), #left
        ((5, 8), 1) # right
    ]
    touchesInfoDicts = IntervalTouches.interval1DTouchesEachOtherAt(intervalList)
    expected = [   
    {   'idxInInputList': 0,
        'interval': ((4, 7), 0),
        'toucherInfoDict': {'c': [], 'e': [], 'l': [], 'r': [((5, 8), 1)]}},
    {   'idxInInputList': 1,
        'interval': ((5, 8), 1),
        'toucherInfoDict': {'c': [], 'e': [], 'l': [((4, 7), 0)], 'r': []}}]
    print('PASSED? ', expected==touchesInfoDicts)
    if verbose:
        pp.pprint(touchesInfoDicts)


def test__1dTouchingIntervals__allCasesHas1(verbose=False):
    intervalList = [
        ((4, 7), 0), #inner
        ((2, 9), 1), #outer
        ((3, 6), 2), #left
        ((5, 8), 3), #right
    ]
    touchesInfoDicts = IntervalTouches.interval1DTouchesEachOtherAt(intervalList)
    expected = [   
    {   'idxInInputList': 0,
        'interval': ((4, 7), 0),
        'toucherInfoDict': {   'c': [],
                               'e': [((2, 9), 1)],
                               'l': [((3, 6), 2)],
                               'r': [((5, 8), 3)]}},
    {   'idxInInputList': 1,
        'interval': ((2, 9), 1),
        'toucherInfoDict': {   'c': [((4, 7), 0), ((3, 6), 2), ((5, 8), 3)],
                               'e': [],
                               'l': [],
                               'r': []}},
    {   'idxInInputList': 2,
        'interval': ((3, 6), 2),
        'toucherInfoDict': {   'c': [],
                               'e': [((2, 9), 1)],
                               'l': [],
                               'r': [((4, 7), 0), ((5, 8), 3)]}},
    {   'idxInInputList': 3,
        'interval': ((5, 8), 3),
        'toucherInfoDict': {   'c': [],
                               'e': [((2, 9), 1)],
                               'l': [((4, 7), 0), ((3, 6), 2)],
                               'r': []}}]
    print('PASSED? ', expected==touchesInfoDicts)
    if verbose:
        pp.pprint(touchesInfoDicts)


def test__1dTouchingIntervals__nonTouching(verbose=False):
    intervalList = [
        ((0, 3), 0),
        ((8, 11), 1)
    ]
    touchesInfoDict = IntervalTouches.interval1DTouchesEachOtherAt(intervalList)
    expected = [   
    {   'idxInInputList': 0,
        'interval': ((0, 3), 0),
        'toucherInfoDict': {'c': [], 'e': [], 'l': [], 'r': []}},
    {   'idxInInputList': 1,
        'interval': ((8, 11), 1),
        'toucherInfoDict': {'c': [], 'e': [], 'l': [], 'r': []}}]
    print('PASSED? ', expected==touchesInfoDict)
    if verbose:
        pp.pprint(touchesInfoDict)



def test__2dTouchingIntervals__allCasesHas1(verbose=False):
    intervalList = [
        [(0,3), (0,3)], #0  0
        [(0,3), (2,5)], #1  1
        [(0,3), (6,9)], #2  2
        [(0,3), (8,11)], #d  3
        [(2,5), (0,3)], #3  4
        [(2,5), (4,7)], #4  5
        [(2,5), (8,11)], #5  6
        [(4,7), (2,5)], #6  7
        [(4,7), (6,9)], #7  8
        [(6,9), (0,3)], #8  9
        [(6,9), (4,7)], #9  10
        [(6,9), (8,11)], #a  11
        [(8,11), (0,3)], #e  12
        [(8,11), (2,5)], #b  13
        [(8,11), (6,9)], #c  14
        [(8,11), (8,11)], #f  15
    ]
    intervalToIntersects = IntervalTouches.intervalnDTouchesEachOtherAt(intervalList)
    expected = {   (((0, 3), (0, 3)), 0): {   'cc': [],
                               'ce': [],
                               'cl': [],
                               'cr': [],
                               'ec': [],
                               'ee': [],
                               'el': [],
                               'er': [[(0, 3), (2, 5)]],
                               'lc': [],
                               'le': [],
                               'll': [],
                               'lr': [],
                               'rc': [],
                               're': [[(2, 5), (0, 3)]],
                               'rl': [],
                               'rr': []},
    (((0, 3), (2, 5)), 1): {   'cc': [],
                               'ce': [],
                               'cl': [],
                               'cr': [],
                               'ec': [],
                               'ee': [],
                               'el': [[(0, 3), (0, 3)]],
                               'er': [],
                               'lc': [],
                               'le': [],
                               'll': [],
                               'lr': [],
                               'rc': [],
                               're': [],
                               'rl': [[(2, 5), (0, 3)]],
                               'rr': [[(2, 5), (4, 7)]]},
    (((0, 3), (6, 9)), 2): {   'cc': [],
                               'ce': [],
                               'cl': [],
                               'cr': [],
                               'ec': [],
                               'ee': [],
                               'el': [],
                               'er': [[(0, 3), (8, 11)]],
                               'lc': [],
                               'le': [],
                               'll': [],
                               'lr': [],
                               'rc': [],
                               're': [],
                               'rl': [[(2, 5), (4, 7)]],
                               'rr': [[(2, 5), (8, 11)]]},
    (((0, 3), (8, 11)), 3): {   'cc': [],
                                'ce': [],
                                'cl': [],
                                'cr': [],
                                'ec': [],
                                'ee': [],
                                'el': [[(0, 3), (6, 9)]],
                                'er': [],
                                'lc': [],
                                'le': [],
                                'll': [],
                                'lr': [],
                                'rc': [],
                                're': [[(2, 5), (8, 11)]],
                                'rl': [],
                                'rr': []},
    (((2, 5), (0, 3)), 4): {   'cc': [],
                               'ce': [],
                               'cl': [],
                               'cr': [],
                               'ec': [],
                               'ee': [],
                               'el': [],
                               'er': [],
                               'lc': [],
                               'le': [[(0, 3), (0, 3)]],
                               'll': [],
                               'lr': [[(0, 3), (2, 5)]],
                               'rc': [],
                               're': [],
                               'rl': [],
                               'rr': [[(4, 7), (2, 5)]]},
    (((2, 5), (4, 7)), 5): {   'cc': [],
                               'ce': [],
                               'cl': [],
                               'cr': [],
                               'ec': [],
                               'ee': [],
                               'el': [],
                               'er': [],
                               'lc': [],
                               'le': [],
                               'll': [[(0, 3), (2, 5)]],
                               'lr': [[(0, 3), (6, 9)]],
                               'rc': [],
                               're': [],
                               'rl': [[(4, 7), (2, 5)]],
                               'rr': [[(4, 7), (6, 9)]]},
    (((2, 5), (8, 11)), 6): {   'cc': [],
                                'ce': [],
                                'cl': [],
                                'cr': [],
                                'ec': [],
                                'ee': [],
                                'el': [],
                                'er': [],
                                'lc': [],
                                'le': [[(0, 3), (8, 11)]],
                                'll': [[(0, 3), (6, 9)]],
                                'lr': [],
                                'rc': [],
                                're': [],
                                'rl': [[(4, 7), (6, 9)]],
                                'rr': []},
    (((4, 7), (2, 5)), 7): {   'cc': [],
                               'ce': [],
                               'cl': [],
                               'cr': [],
                               'ec': [],
                               'ee': [],
                               'el': [],
                               'er': [],
                               'lc': [],
                               'le': [],
                               'll': [[(2, 5), (0, 3)]],
                               'lr': [[(2, 5), (4, 7)]],
                               'rc': [],
                               're': [],
                               'rl': [[(6, 9), (0, 3)]],
                               'rr': [[(6, 9), (4, 7)]]},
    (((4, 7), (6, 9)), 8): {   'cc': [],
                               'ce': [],
                               'cl': [],
                               'cr': [],
                               'ec': [],
                               'ee': [],
                               'el': [],
                               'er': [],
                               'lc': [],
                               'le': [],
                               'll': [[(2, 5), (4, 7)]],
                               'lr': [[(2, 5), (8, 11)]],
                               'rc': [],
                               're': [],
                               'rl': [[(6, 9), (4, 7)]],
                               'rr': [[(6, 9), (8, 11)]]},
    (((6, 9), (0, 3)), 9): {   'cc': [],
                               'ce': [],
                               'cl': [],
                               'cr': [],
                               'ec': [],
                               'ee': [],
                               'el': [],
                               'er': [],
                               'lc': [],
                               'le': [],
                               'll': [],
                               'lr': [[(4, 7), (2, 5)]],
                               'rc': [],
                               're': [[(8, 11), (0, 3)]],
                               'rl': [],
                               'rr': [[(8, 11), (2, 5)]]},
    (((6, 9), (4, 7)), 10): {   'cc': [],
                                'ce': [],
                                'cl': [],
                                'cr': [],
                                'ec': [],
                                'ee': [],
                                'el': [],
                                'er': [],
                                'lc': [],
                                'le': [],
                                'll': [[(4, 7), (2, 5)]],
                                'lr': [[(4, 7), (6, 9)]],
                                'rc': [],
                                're': [],
                                'rl': [[(8, 11), (2, 5)]],
                                'rr': [[(8, 11), (6, 9)]]},
    (((6, 9), (8, 11)), 11): {   'cc': [],
                                 'ce': [],
                                 'cl': [],
                                 'cr': [],
                                 'ec': [],
                                 'ee': [],
                                 'el': [],
                                 'er': [],
                                 'lc': [],
                                 'le': [],
                                 'll': [[(4, 7), (6, 9)]],
                                 'lr': [],
                                 'rc': [],
                                 're': [[(8, 11), (8, 11)]],
                                 'rl': [[(8, 11), (6, 9)]],
                                 'rr': []},
    (((8, 11), (0, 3)), 12): {   'cc': [],
                                 'ce': [],
                                 'cl': [],
                                 'cr': [],
                                 'ec': [],
                                 'ee': [],
                                 'el': [],
                                 'er': [[(8, 11), (2, 5)]],
                                 'lc': [],
                                 'le': [[(6, 9), (0, 3)]],
                                 'll': [],
                                 'lr': [],
                                 'rc': [],
                                 're': [],
                                 'rl': [],
                                 'rr': []},
    (((8, 11), (2, 5)), 13): {   'cc': [],
                                 'ce': [],
                                 'cl': [],
                                 'cr': [],
                                 'ec': [],
                                 'ee': [],
                                 'el': [[(8, 11), (0, 3)]],
                                 'er': [],
                                 'lc': [],
                                 'le': [],
                                 'll': [[(6, 9), (0, 3)]],
                                 'lr': [[(6, 9), (4, 7)]],
                                 'rc': [],
                                 're': [],
                                 'rl': [],
                                 'rr': []},
    (((8, 11), (6, 9)), 14): {   'cc': [],
                                 'ce': [],
                                 'cl': [],
                                 'cr': [],
                                 'ec': [],
                                 'ee': [],
                                 'el': [],
                                 'er': [[(8, 11), (8, 11)]],
                                 'lc': [],
                                 'le': [],
                                 'll': [[(6, 9), (4, 7)]],
                                 'lr': [[(6, 9), (8, 11)]],
                                 'rc': [],
                                 're': [],
                                 'rl': [],
                                 'rr': []},
    (((8, 11), (8, 11)), 15): {   'cc': [],
                                  'ce': [],
                                  'cl': [],
                                  'cr': [],
                                  'ec': [],
                                  'ee': [],
                                  'el': [[(8, 11), (6, 9)]],
                                  'er': [],
                                  'lc': [],
                                  'le': [[(6, 9), (8, 11)]],
                                  'll': [],
                                  'lr': [],
                                  'rc': [],
                                  're': [],
                                  'rl': [],
                                  'rr': []}}
    print('PASSED? ', expected==intervalToIntersects)
    if verbose:
        pp.pprint(intervalToIntersects)



def test__1dTouchingIntervals__withIntervalnDTouchesEachOtherAt(verbose=False):
    intervalList = [
        [(4, 7)], #inner
        [(2, 9)], #outer
        [(3, 6)], #left
        [(5, 8)], #right
    ]
    intervalToIntersects = IntervalTouches.intervalnDTouchesEachOtherAt(intervalList)
    expected = {
    (((2, 9),), 1): {   'c': [[(4, 7)], [(3, 6)], [(5, 8)]],
                        'e': [],
                        'l': [],
                        'r': []},
    (((3, 6),), 2): {   'c': [],
                        'e': [[(2, 9)]],
                        'l': [],
                        'r': [[(4, 7)], [(5, 8)]]},
    (((4, 7),), 0): {   'c': [],
                        'e': [[(2, 9)]],
                        'l': [[(3, 6)]],
                        'r': [[(5, 8)]]},
    (((5, 8),), 3): {   'c': [],
                        'e': [[(2, 9)]],
                        'l': [[(4, 7)], [(3, 6)]],
                        'r': []}}
    print('PASSED? ', expected==intervalToIntersects)
    if verbose:
        pp.pprint(intervalToIntersects)
    


if __name__=='__main__':
    test__1dTouchingIntervals__sameIntervals()
    test__1dTouchingIntervals__leftRightIntervalsFrom2DCase()
    test__1dTouchingIntervals__smallerCaseFrom2DAllPairsDimension0()
    test__1dTouchingIntervals__smallerCaseFrom2DAllPairsDimension1()
    test__1dTouchingIntervals__leftRightIntervals()
    test__1dTouchingIntervals__allCasesHas1()

    test__1dTouchingIntervals__nonTouching()
    test__2dTouchingIntervals__allCasesHas1()
    test__1dTouchingIntervals__withIntervalnDTouchesEachOtherAt()