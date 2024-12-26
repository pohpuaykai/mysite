import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.distributivity import Distributivity


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (+ (* b c) (* b d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Distributivity(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # (+ (* $0 $1) (* $0 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (* b (+ c d)))' # (* $0 (+ $1 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (* b (+ c d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Distributivity(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # (* $0 (+ $1 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (+ (* b c) (* b d)))' # (+ (* $0 $1) (* $0 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (- (* b c) (* b d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Distributivity(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[1] # (- (* $0 $1) (* $0 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (* b (- c d)))' # (* $0 (- $1 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a (* b (- c d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Distributivity(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[1] # (* $0 (- $1 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (- (* b c) (* b d)))' # (- (* $0 $1) (* $0 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a (+ (/ b c) (/ d c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Distributivity(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[2] # (+ (/ $1 $0) (/ $2 $0))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (/ (+ b d) c))' # (/ (+ $1 $2) $0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= a (/ (+ b c) d))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Distributivity(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[2] # (/ (+ $1 $2) $0)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (+ (/ b d) (/ c d)))' # (+ (/ $1 $0) (/ $2 $0))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= a (- (/ b c) (/ d c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Distributivity(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[3] # (- (/ $1 $0) (/ $2 $0))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (/ (- b d) c))' # (/ (- $1 $2) $0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= a (/ (- b c) d))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Distributivity(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[3] # (/ (- $1 $2) $0)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (- (/ b d) (/ c d)))' # (- (/ $1 $0) (/ $2 $0))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    


if __name__=='__main__':
    test__vor0__configTest()
    test__hin0__configTest()
    test__vor1__configTest()
    test__hin1__configTest()
    test__vor2__configTest()
    test__hin2__configTest()
    test__vor3__configTest()
    test__hin3__configTest()
    