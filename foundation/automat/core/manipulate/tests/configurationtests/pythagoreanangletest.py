import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.pythagoreanangle import Pythagoreanangle


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (+ (^ (sin b) 2) (^ (cos b) 2)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Pythagoreanangle(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # (+ (^ (sin $0) 2) (^ (cos $0) 2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '1' # 1
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a 1)' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Pythagoreanangle(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # 1
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (+ (^ (sin v_{0}) 2) (^ (cos v_{0}) 2)))' # (+ (^ (sin $0) 2) (^ (cos $0) 2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    


if __name__=='__main__':
    test__vor0__configTest()
    test__hin0__configTest()
    