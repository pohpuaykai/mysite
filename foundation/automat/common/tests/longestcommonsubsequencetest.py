import pprint
import inspect

from foundation.automat.common.longestcommonsubsequence import LongestCommonSubsequence

pp = pprint.PrettyPrinter(indent=4)


def test__schemeGrammarUpgrade__communtativity1vor(verbose=False):
    """
    """
    iPattern = '(+ $0 $1)'
    oPattern = '(+ $1 $0)'
    iMatchedFrags, oMatchedFrags = LongestCommonSubsequence.lcss(iPattern, oPattern)
    iExpected = [   
        {'e': 4, 's': 0, 'w': '(+ $'},
        {'e': 7, 's': 5, 'w': ' $'},
        {'e': 9, 's': 8, 'w': ')'}
    ]
    oExpected = [   
        {'e': 4, 's': 0, 'w': '(+ $'},
        {'e': 7, 's': 5, 'w': ' $'},
        {'e': 9, 's': 8, 'w': ')'}
    ]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


def test__schemeGrammarUpgrade__pythagoreanangle1vor(verbose=False):
    """
    """
    iPattern = '(+ (^ (sin $0) 2) (^ (cos $0) 2))'
    oPattern = '1'
    iMatchedFrags, oMatchedFrags = LongestCommonSubsequence.lcss(iPattern, oPattern)
    iExpected = []
    oExpected = []
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


def test__schemeGrammarUpgrade__subtractzero1vor(verbose=False):
    """
    """
    iPattern = '(- 0 $0)'
    oPattern = '$0'
    iMatchedFrags, oMatchedFrags = LongestCommonSubsequence.lcss(iPattern, oPattern)
    iExpected = [{'e': 7, 's': 5, 'w': '$0'}]
    oExpected = [{'e': 2, 's': 0, 'w': '$0'}]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


def test__schemeGrammarUpgrade__doubleinverse1vor(verbose=False):
    """
    """
    iPattern = '(/ (/ $2 $0) $1)'
    oPattern = '(/ $2 (* $0 $1))'
    iMatchedFrags, oMatchedFrags = LongestCommonSubsequence.lcss(iPattern, oPattern)
    iExpected = [{'e': 11, 's': 3, 'w': '(/ $2 $0'}, {'e': 16, 's': 12, 'w': ' $1)'}]
    oExpected = [   
        {'e': 5, 's': 0, 'w': '(/ $2'},
        {'e': 14, 's': 8, 'w': ' $0 $1'},
        {'e': 16, 's': 15, 'w': ')'}
    ]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)



def test__manipulateTest__subtractZero(verbose=False):
    """
    """
    iPattern = '(- (* I_{R_{C}} R_{C}) V^{Q1}_{BE})'
    oPattern = '(- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0)'
    iMatchedFrags, oMatchedFrags, iUnmatchedFrags, oUnmatchedFrags = LongestCommonSubsequence.lcssWithUnmatched(iPattern, oPattern)
    iExpected = [{'e': 35, 's': 0, 'w': '(- (* I_{R_{C}} R_{C}) V^{Q1}_{BE})'}]
    oExpected = [   {'e': 37, 's': 3, 'w': '(- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}'},
    {'e': 41, 's': 40, 'w': ')'}]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
        print('iUnmatchedFrags')
        pp.pprint(iUnmatchedFrags)
        print('oUnmatchedFrags')
        pp.pprint(oUnmatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)



def test__schemegrammar__substractzeroAtback(verbose=False):
    """
    """
    iPattern = '(- $ 0)'
    oPattern = '$'
    iMatchedFrags, oMatchedFrags, iUnmatchedFrags, oUnmatchedFrags = LongestCommonSubsequence.lcssWithUnmatched(iPattern, oPattern)
    iExpected = [{'e': 4, 's': 3, 'w': '$'}]
    oExpected = [{'e': 1, 's': 0, 'w': '$'}]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
        print('iUnmatchedFrags')
        pp.pprint(iUnmatchedFrags)
        print('oUnmatchedFrags')
        pp.pprint(oUnmatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


def test__schemeGrammarUpgrade__doubleinverse1vorNoArgNumMoreThan1Dollar(verbose=False):
    """
    """
    iPattern = '(/ (/ $ $) $)'
    oPattern = '(/ $ (* $ $))'
    iMatchedFrags, oMatchedFrags, iUnmatchedFrags, oUnmatchedFrags = LongestCommonSubsequence.lcssWithUnmatched(iPattern, oPattern)
    iExpected = [   
    {'e': 4, 's': 0, 'w': '(/ ('},
    {'e': 10, 's': 5, 'w': ' $ $)'},
    {'e': 13, 's': 12, 'w': ')'}]
    oExpected = [   
    {'e': 2, 's': 0, 'w': '(/'},
    {'e': 6, 's': 4, 'w': ' ('},
    {'e': 13, 's': 7, 'w': ' $ $))'}]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
        print('iUnmatchedFrags')
        pp.pprint(iUnmatchedFrags)
        print('oUnmatchedFrags')
        pp.pprint(oUnmatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


if __name__=='__main__':
    # test__schemeGrammarUpgrade__communtativity1vor()
    # test__schemeGrammarUpgrade__pythagoreanangle1vor()
    # test__schemeGrammarUpgrade__subtractzero1vor()
    # test__schemeGrammarUpgrade__doubleinverse1vor()
    test__manipulateTest__subtractZero(True)
    # test__schemegrammar__substractzeroAtback()
    # test__schemeGrammarUpgrade__doubleinverse1vorNoArgNumMoreThan1Dollar()