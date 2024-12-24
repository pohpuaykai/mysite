import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.trigonometricplusminusmultiply import Trigonometricplusminusmultiply


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (sin (+ b c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminusmultiply(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # (sin (+ $0 $1))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '' # (+ (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (+ (* (sin b) (cos c)) (* (cos b) (sin c))))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminusmultiply(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # (+ (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '' # (sin (+ $0 $1))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (sin (- b c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminusmultiply(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[1] # (sin (- $0 $1))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '' # (- (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a (- (* (sin b) (cos c)) (* (cos b) (sin c))))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminusmultiply(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[1] # (- (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '' # (sin (- $0 $1))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a (cos (+ b c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminusmultiply(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[2] # (cos (+ $0 $1))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '' # (- (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= a (- (* (cos b) (cos c)) (* (sin b) (sin c))))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminusmultiply(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[2] # (- (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '' # (cos (+ $0 $1))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= a (cos (- b c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminusmultiply(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[3] # (cos (- $0 $1))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '' # (+ (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= a (+ (* (cos b) (cos c)) (* (sin b) (sin c))))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminusmultiply(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[3] # (+ (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '' # (cos (- $0 $1))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    


if __name__=='__main__':
    test__vor0__configTest(True) # Not tested yet
    test__hin0__configTest(True) # Not tested yet
    test__vor1__configTest(True) # Not tested yet
    test__hin1__configTest(True) # Not tested yet
    test__vor2__configTest(True) # Not tested yet
    test__hin2__configTest(True) # Not tested yet
    test__vor3__configTest(True) # Not tested yet
    test__hin3__configTest(True) # Not tested yet
    