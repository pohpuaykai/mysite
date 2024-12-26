import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.crossmultiply import Crossmultiply


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (+ (/ b c) (/ d e)))' # fill it in
    eqsType = 'scheme'
    #filename = 'crossmultiply'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Crossmultiply(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (/ $0 $1) (/ $2 $3))
    expected = '(= a (/ (+ (* b e) (* c d)) (* c e)))' # (/ (+ (* $0 $3) (* $1 $2)) (* $1 $3))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (/ (+ (* b e) (* c d)) (* c e)))' # fill it in
    eqsType = 'scheme'
    #filename = 'crossmultiply'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Crossmultiply(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ (* $0 $3) (* $1 $2)) (* $1 $3))
    expected = '(= a (+ (/ b c) (/ d e)))' # (+ (/ $0 $1) (/ $2 $3))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    


if __name__=='__main__':
    test__vor0__configTest()
    test__hin0__configTest()
    