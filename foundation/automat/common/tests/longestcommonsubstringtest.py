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



def test__manipulate__simple(verbose=False):
    schemeFormula0 = '(= a (+ b c))'
    schemeFormula1 = '(+ $0 $1)'
    commonSubstring = LongestCommonSubString.lcs(schemeFormula0, schemeFormula1)
    expected = ['(+ b c)']
    print('PASSED? ', commonSubstring == expected)
    if verbose:
        print(commonSubstring)



def test__manipulate__sameLevel(verbose=False):
    schemeFormula0 = '(= (+ a b) (+ c d))'
    schemeFormula1 = '(+ $0 $1)'
    commonSubstring = LongestCommonSubString.lcs(schemeFormula0, schemeFormula1)
    expected = ['(+ a b)', '(+ c d)']
    print('PASSED? ', commonSubstring == expected)
    if verbose:
        print(commonSubstring)


def test__manipulate__nested(verbose=False):
    schemeFormula0 = '(= a (+ (+ b c) d))'
    schemeFormula1 = '(+ $0 $1)'
    commonSubstring = LongestCommonSubString.lcs(schemeFormula0, schemeFormula1)
    expected = ['(+ (+ b c) d)']#, '(+ b c)'] # we only want to return same levels first..., then use a stack to recursively find same pattern within results
    print('PASSED? ', commonSubstring == expected)
    if verbose:
        print(commonSubstring)


def test__manipulate__nestedEtSameLevel(verbose=False): # TODO also test for weird variables
    schemeFormula0 = '(= (+ (+ a b) (+ c d)) (+ (+ e f) (+ g h)))'
    schemeFormula1 = '(+ $0 $1)'
    commonSubstring = LongestCommonSubString.lcs(schemeFormula0, schemeFormula1)
    expected = ['(+ (+ a b) (+ c d))', '(+ (+ e f) (+ g h))'] # we only want to return same levels first..., then use a stack to recursively find same pattern within results
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
    # schemeFormula1 = '(* (+ x 1) (+ x 2))'
    # schemeFormula0 = '(* (* (+ x 1) (- x 1)) (+ x 2))'
    grupp0, grupp1 = LongestCommonSubString.alcs(schemeFormula0, schemeFormula1)
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
    print('PASSED? ')
    expectedGrupp0 = {(0, 19): '(* (+ x 1) (+ x 2))'}
    expectedGrupp1 = {(3, 15): '(* (+ x 1) (', (21, 31): ') (+ x 2))'}
    if verbose:
        pp.pprint(grupp0)
        print(expectedGrupp0, '<<<<<<<<<<<<<<<<<<<<expected')
        pp.pprint(grupp1)
        print(expectedGrupp1, '<<<<<<<<<<<<<<<<<<<<expected')



if __name__=='__main__':
    # test__oneTermFactorization__formulaContainedInAnotherFormula()
    # test__oneTermFactorization__otherDirectionContainment()
    # test__longCommonString__bloteBespiel()
    test__oneTermFactorization__moreThanOneCommonString(True)