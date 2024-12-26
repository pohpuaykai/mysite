import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.multiplydividecancel import Multiplydividecancel


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (* (/ b c) c))' # fill it in
    eqsType = 'scheme'
    #filename = 'multiplydividecancel'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Multiplydividecancel(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (/ $1 $0) $0)
    expected = '(= a b)' # $1
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a a)' # fill it in
    eqsType = 'scheme'
    #filename = 'multiplydividecancel'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Multiplydividecancel(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $1
    expected = '(= (* (/ a v_{0}) v_{0}) (* (/ a v_{0}) v_{0}))' # (* (/ $1 $0) $0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (/ (* b c) c))' # fill it in
    eqsType = 'scheme'
    #filename = 'multiplydividecancel'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Multiplydividecancel(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* $1 $0) $0)
    expected = '(= a b)' # $1
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a a)' # fill it in
    eqsType = 'scheme'
    #filename = 'multiplydividecancel'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Multiplydividecancel(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $1
    expected = '(= (/ (* a v_{0}) v_{0}) (/ (* a v_{0}) v_{0}))' # (/ (* $1 $0) $0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    


if __name__=='__main__':
    test__vor0__configTest()
    test__hin0__configTest()
    test__vor1__configTest()
    test__hin1__configTest()
    