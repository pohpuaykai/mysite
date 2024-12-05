import inspect
import pprint

from foundation.automat.common.longestcommonsubstring import LongestCommonSubString

pp = pprint.PrettyPrinter(indent=4)

def test__oneTermFactorization__formulaContainedInAnotherFormula(verbose=False):
    schemeFormula0 = '(+ x 1)'
    schemeFormula1 = '(* (+ x 1) (- x 1))'
    commonSubstring = LongestCommonSubString.lcs(schemeFormula0, schemeFormula1)
    expected = '(+ x 1)'
    print('PASSED? ', commonSubstring == expected)
    if verbose:
        print(commonSubstring)


def test__oneTermFactorization__otherDirectionContainment(verbose=False):
    schemeFormula0 = '(* (+ x 1) (- x 1))'
    schemeFormula1 = '(+ x 1)'
    commonSubstring = LongestCommonSubString.lcs(schemeFormula0, schemeFormula1)
    expected = '(+ x 1)'
    print('PASSED? ', commonSubstring == expected)
    if verbose:
        print(commonSubstring)



def test__longCommonString__bloteBespiel(verbose=False):
    schemeFormula0 = 'abbbbbcddd'
    schemeFormula1 = 'bbbbbddd'
    commonSubstring = LongestCommonSubString.alcs(schemeFormula0, schemeFormula1)

    expected = [   [   {'endPos': 6, 's': 'bbbbb', 'startPos': 1},
        {'endPos': 5, 's': 'bbbbb', 'startPos': 0}],
    [   {'endPos': 10, 's': 'ddd', 'startPos': 7},
        {'endPos': 8, 's': 'ddd', 'startPos': 5}]]
    print('PASSED? ', commonSubstring == expected)
    if verbose:
        pp.pprint(commonSubstring)




def test__oneTermFactorization__moreThanOneCommonString(verbose=False): # TODO wrong , please refer to common.tests.bubblemergetest.py test__overlappingIntervalsTwoSetsOfIntervals__AllLongestCommonSubString
    schemeFormula0 = '(* (+ x 1) (+ x 2))'
    schemeFormula1 = '(* (* (+ x 1) (- x 1)) (+ x 2))'
    commonSubstring = LongestCommonSubString.alcs(schemeFormula0, schemeFormula1)
    expected = [   [   {'endPos': 2, 's': '(*', 'startPos': 0},
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
    print('PASSED? ', commonSubstring == expected) # ok, maybe can pass this to bubble merge :)
    if verbose:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(commonSubstring)



if __name__=='__main__':
    # test__oneTermFactorization__formulaContainedInAnotherFormula()
    # test__oneTermFactorization__otherDirectionContainment()
    # test__longCommonString__bloteBespiel()
    test__oneTermFactorization__moreThanOneCommonString()