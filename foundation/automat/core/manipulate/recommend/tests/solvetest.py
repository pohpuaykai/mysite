import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend


pp = pprint.PrettyPrinter(indent=4)

def solve__factoriseAndCancel__2terms(verbose):
    eq = Equation('(= (+ (* 2 x) (* 2 y)) (* 2 z))', parserName='scheme', verbose=verbose)
    r = Recommend()
    solvedSchemeStrs = r.combingSearch(eq) # maybe rename this to solve
    expected_solvedSchemeStrs = ['(= (+ x y) z)', '(= (+ y x) z)', '(= z (+ x y))', '(= z (+ y x))']

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', solvedSchemeStrs == expected_solvedSchemeStrs)
    if verbose:
        print('solvedSchemeStrs: ')
        print(solvedSchemeStrs)


def solve__factoriseAndCancel__3terms(verbose):
    eq = Equation('(= (+ (+ (* 2 x) (* 2 y)) (* 2 z)) (* 2 a))', parserName='scheme', verbose=verbose)
    r = Recommend()
    solvedSchemeStrs = r.combingSearch(eq) # maybe rename this to solve
    expected_solvedSchemeStrs = ['(= (+ (+ x y) z) a)', '(= (+ z (+ y x)) a)', '(= a (+ (+ x y) z))', '(= a (+ z (+ y x)))']

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', solvedSchemeStrs == expected_solvedSchemeStrs)
    if verbose:
        print('solvedSchemeStrs: ')
        print(solvedSchemeStrs)

def solve__factoriseAndCancel__2termsHarmonic(verbose):
    eq = Equation('(= (+ (/ 2 x) (/ 2 y)) (/ 2 z))', parserName='scheme', verbose=verbose)
    r = Recommend()
    solvedSchemeStrs = r.combingSearch(eq) # maybe rename this to solve
    expected_solvedSchemeStrs = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', solvedSchemeStrs == expected_solvedSchemeStrs)
    if verbose:
        print('solvedSchemeStrs: ')
        print(solvedSchemeStrs)


if __name__=='__main__':#use this to shrink the search space of bipartiteSearch? so we get test cases from bipartitesearchtest? then we need to translate the path to actual equations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # solve__factoriseAndCancel__2terms()
    # solve__factoriseAndCancel__3terms()
    solve__factoriseAndCancel__2termsHarmonic(True)