import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.exponential import Exponential


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (^ b 0))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # (^ $0 0)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '1' # 1
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (+ 1 (+ 1 1)))' # 
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # 1
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (+ (^ v_{0} 0) (+ (^ v_{0} 0) (^ v_{0} 0))))' # (^ $0 0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (^ b 1))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[1] # (^ $0 1)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a b)' # $0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a a)' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[1] # $0
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= (^ a 1) (^ a 1))' # (^ $0 1)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a (^ b (+ c d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[2] # (^ $0 (+ $1 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (* (^ b c) (^ b d)))' # (* (^ $0 $1) (^ $0 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= a (* (^ b c) (^ b d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[2] # (* (^ $0 $1) (^ $0 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (^ b (+ c d)))' # (^ $0 (+ $1 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= a (^ (^ b c) d))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[3] # (^ (^ $0 $1) $2)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (^ b (* c d)))' # (^ $0 (* $1 $2))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= a (^ b (* c d)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[3] # (^ $0 (* $1 $2))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (^ (^ b c) d))' # (^ (^ $0 $1) $2)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= a (* (^ b c) (^ d c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[4] # (* (^ $1 $0) (^ $2 $0))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (^ (* b d) c))' # (^ (* $1 $2) $0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= a (^ (* b c) d))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[4] # (^ (* $1 $2) $0)
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (* (^ b d) (^ c d)))' # (* (^ $1 $0) (^ $2 $0))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= a (^ b (- "0" c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[5] # (^ $0 (- "0" $1))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['scheme'], patternDict['vor']['return'])
    expected = '(= a (/ "1" (^ b c)))' # (/ "1" (^ $0 $1))
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= a (/ "1" (^ b c)))' # fill it in
    eqsType = 'scheme'
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[5] # (/ "1" (^ $0 $1))
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['hin']['scheme'], patternDict['hin']['return'])
    expected = '(= a (^ b (- "0" c)))' # (^ $0 (- "0" $1))
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
    