import inspect
import pprint

from foundation.automat.core.equation import Equation
# from foundation.automat.core.manipulate.recommend.recommend import Recommend
from foundation.automat.core.manipulate.recommend.searchers.solvesearcher import SolveSearcher


pp = pprint.PrettyPrinter(indent=4)

def solve__factoriseAndCancel__2terms(verbose):
    eq = Equation('(= (+ (* 2 x) (* 2 y)) (* 2 z))', parserName='scheme', verbose=verbose)
    # r = Recommend()
    solvedSchemeStrs = (SolveSearcher(eq, 7)).search()
    # solvedSchemeStrs = Recommend.combingSearch(eq) # maybe rename this to solve
    expected_solvedSchemeStrs = [{'schemeStr': '(= (+ x y) z)', 'solvingStep': [('distributivity', 'vor', 0), ('equalitycancellation', 'vor', 0)]}]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', solvedSchemeStrs == expected_solvedSchemeStrs)
    if verbose:
        print('solvedSchemeStrs: ')
        print(solvedSchemeStrs)


def solve__factoriseAndCancel__3terms(verbose):
    eq = Equation('(= (+ (+ (* 2 x) (* 2 y)) (* 2 z)) (* 2 a))', parserName='scheme', verbose=verbose)
    # r = Recommend()
    solvedSchemeStrs = (SolveSearcher(eq, 7)).search()
    # solvedSchemeStrs = Recommend.combingSearch(eq) # maybe rename this to solve
    expected_solvedSchemeStrs = [{'schemeStr': '(= (+ z (+ y x)) a)', 'solvingStep': [('distributivity', 'vor', 0), ('communtativity', 'vor', 0), ('distributivity', 'vor', 0), ('equalitycancellation', 'vor', 0)]}, {'schemeStr': '(= a (+ (+ x y) z))', 'solvingStep': [('distributivity', 'vor', 0), ('communtativity', 'vor', 2), ('distributivity', 'vor', 0), ('equalitycancellation', 'vor', 0)]}]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', solvedSchemeStrs == expected_solvedSchemeStrs)
    if verbose:
        print('solvedSchemeStrs: ')
        print(solvedSchemeStrs)

def solve__factoriseAndCancel__2termsHarmonic(verbose):
    eq = Equation('(= (+ (/ 2 x) (/ 2 y)) (/ 2 z))', parserName='scheme', verbose=verbose)
    # r = Recommend(verbose=verbose)
    solvedSchemeStrs = (SolveSearcher(eq, 7)).search()
    # solvedSchemeStrs = Recommend.combingSearch(eq) # maybe rename this to solve
    expected_solvedSchemeStrs = [
    {'schemeStr': '(= (+ (/ 1 x) (/ 1 y)) (/ 1 z))', 'solvingStep': [('multiplydividecancel', 'vor', 2), ('distributivity', 'vor', 0), ('equalitycancellation', 'vor', 0)]}
    ]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', solvedSchemeStrs == expected_solvedSchemeStrs)
    if verbose:
        print('solvedSchemeStrs: ')
        print(solvedSchemeStrs)


def solve__factoriseAndCancel__twoResistorParallelCircuit(verbose):
    eq = Equation('(= (* (- (/ V_{DC_{8}} R_{DC_{8}}) (/ V_{DC_{8}} R_{R_{3}})) R_{R_{0}}) V_{DC_{8}})', parserName='scheme', verbose=verbose)
    solvedSchemeStrs = (SolveSearcher(eq, 7)).search()
    # solvedSchemeStrs = Recommend.combingSearch(eq) # maybe rename this to solve
    expected_solvedSchemeStrs = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', solvedSchemeStrs == expected_solvedSchemeStrs)
    if verbose:
        print('solvedSchemeStrs: ')
        print(solvedSchemeStrs)


if __name__=='__main__':#use this to shrink the search space of bipartiteSearch? so we get test cases from bipartitesearchtest? then we need to translate the path to actual equations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    solve__factoriseAndCancel__2terms(True)
    # solve__factoriseAndCancel__3terms()
    # solve__factoriseAndCancel__2termsHarmonic()
    # solve__factoriseAndCancel__twoResistorParallelCircuit(True)