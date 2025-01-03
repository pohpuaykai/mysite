import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.pythagoreanangle import Pythagoreanangle
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (+ (^ (sin b) 2) (^ (cos b) 2)))' # fill it in
    eqsType = 'scheme'
    #filename = 'pythagoreanangle'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Pythagoreanangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (^ (sin $0) 2) (^ (cos $0) 2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '1' # 1
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a 1)' # fill it in
    eqsType = 'scheme'
    #filename = 'pythagoreanangle'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Pythagoreanangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # 1
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (+ (^ (sin v_{0}) 2) (^ (cos v_{0}) 2)))' # (+ (^ (sin $0) 2) (^ (cos $0) 2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    


if __name__=='__main__':
    test__vor0__configTest()
    test__hin0__configTest()
    