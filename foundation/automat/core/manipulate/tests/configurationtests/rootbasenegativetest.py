import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.rootbasenegative import Rootbasenegative


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (nroot (- 0 b) c))' # fill it in
    eqsType = 'scheme'
    #filename = 'rootbasenegative'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Rootbasenegative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (nroot (- 0 $0) $1)
    expected = '(= a (nroot b (/ 1 c)))' # (nroot $0 (/ 1 $1))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (nroot b (/ 1 c)))' # fill it in
    eqsType = 'scheme'
    #filename = 'rootbasenegative'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Rootbasenegative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (nroot $0 (/ 1 $1))
    expected = '(= a (nroot (- 0 b) c))' # (nroot (- 0 $0) $1)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    


if __name__=='__main__':
    test__vor0__configTest()
    test__hin0__configTest()
    