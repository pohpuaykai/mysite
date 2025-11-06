import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__makesubjecttest0__linearEliminationBySubstitution_eq1_noMatch(verbose=False):
    from foundation.automat.core.manipulate.pattern.distributivity import Distributivity
    eqs = '(= (* I_{R} R) (- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0))' # fill it in
    eqsType = 'scheme'
    #filename = 'distributivity'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Distributivity(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (* $0 $1) (* $0 $2))

    #manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast

    #we expect no-match...
    expected = None # (* $0 (+ $1 $2))
    #expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation# and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        #print(manipulatedAst)


def test__makesubjecttest0__linearEliminationBySubstitution_eq1_match(verbose=False):
    from foundation.automat.core.manipulate.pattern.subtractzero import Subtractzero
    eqs = '(= (* I_{R} R) (- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0))' # fill it in
    eqsType = 'scheme'
    #filename = 'distributivity'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Subtractzero(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (* $0 $1) (* $0 $2))

    #manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast

    #we expect no-match...
    expected = None # when no-match, it returns None
    # expected = '(= (* I_{R} R) (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}))' # (* $0 (+ $1 $2))
    #expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation# and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        #print(manipulatedAst)


if __name__=='__main__':
    test__makesubjecttest0__linearEliminationBySubstitution_eq1_noMatch()
    test__makesubjecttest0__linearEliminationBySubstitution_eq1_match()