import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.crossmultiply import Crossmultiply
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (+ (/ b c) (/ d e)))' # fill it in
    eqsType = 'scheme'
    #filename = 'crossmultiply'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Crossmultiply(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (/ $0 $1) (/ $2 $3))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (/ (+ (* b e) (* c d)) (* c e)))' # (/ (+ (* $0 $3) (* $1 $2)) (* $1 $3))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (/ (+ (* b e) (* c d)) (* c e)))' # fill it in
    eqsType = 'scheme'
    #filename = 'crossmultiply'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Crossmultiply(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (* $0 $3) (* $1 $2)) (* $1 $3))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (+ (/ b c) (/ d e)))' # (+ (/ $0 $1) (/ $2 $3))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    


if __name__=='__main__':
    test__vor0__configTest(True) # Not tested yet
    test__hin0__configTest(True) # Not tested yet
    