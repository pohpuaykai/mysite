import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.logarithm import Logarithm


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (log a (* b c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # (log $0 (* $1 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (+ (log a b) (log a c)))' # (+ (log $0 $1) (log $0 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (+ (log b c) (log b d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # (+ (log $0 $1) (log $0 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (log b (* c d)))' # (log $0 (* $1 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (log b (/ c d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[1] # (log $0 (/ $1 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (- (log b c) (log b d)))' # (- (log $0 $1) (log $0 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a (- (log b c) (log b d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[1] # (- (log $0 $1) (log $0 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (log b (/ c d)))' # (log $0 (/ $1 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a (log b (^ c d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[2] # (log $0 (^ $1 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (* d (log b c)))' # (* $2 (log $0 $1))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= a (* b (log c d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[2] # (* $2 (log $0 $1))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (log c (^ d b)))' # (log $0 (^ $1 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= a (log b (nroot c d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[3] # (log $0 (nroot $1 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (/ (log b d) c))' # (/ (log $0 $2) $1)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= a (/ (log b c) d))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[3] # (/ (log $0 $2) $1)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (log b (nroot d c)))' # (log $0 (nroot $1 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= a (/ (log b c) (log b d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[4] # (/ (log $2 $1) (log $2 $0))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (log d c))' # (log $0 $1)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= a (log b c))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[4] # (log $0 $1)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (/ (log v_{0} c) (log v_{0} b)))' # (/ (log $2 $1) (log $2 $0))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= a (log b b))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[5] # (log $0 $0)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '1' # 1
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= a 1)' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[5] # 1
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (log v_{0} v_{0}))' # (log $0 $0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= a (log b 1))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[6] # (log $0 1)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '0' # 0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= a 0)' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[6] # 0
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (log v_{0} 1))' # (log $0 1)
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
    test__vor4__configTest()
    test__hin4__configTest()
    test__vor5__configTest()
    test__hin5__configTest()
    test__vor6__configTest()
    test__hin6__configTest()
    