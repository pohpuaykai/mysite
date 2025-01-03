import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.logarithm import Logarithm
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (log a (* b c)))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (log $0 (* $1 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (+ (log a b) (log a c)))' # (+ (log $0 $1) (log $0 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (+ (log b c) (log b d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (log $0 $1) (log $0 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (log b (* c d)))' # (log $0 (* $1 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (log b (/ c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (log $0 (/ $1 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (- (log b c) (log b d)))' # (- (log $0 $1) (log $0 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a (- (log b c) (log b d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (log $0 $1) (log $0 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (log b (/ c d)))' # (log $0 (/ $1 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a (log b (^ c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (log $0 (^ $1 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (* d (log b c)))' # (* $2 (log $0 $1))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= a (* b (log c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* $2 (log $0 $1))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (log c (^ d b)))' # (log $0 (^ $1 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= a (log b (nroot c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (log $0 (nroot $1 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ (log b d) c))' # (/ (log $0 $2) $1)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= a (/ (log b c) d))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (log $0 $2) $1)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (log b (nroot d c)))' # (log $0 (nroot $1 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= a (/ (log b c) (log b d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (log $2 $1) (log $2 $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (log d c))' # (log $0 $1)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= a (log b c))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (log $0 $1)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ (log v_{0} c) (log v_{0} b)))' # (/ (log $2 $1) (log $2 $0))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= a (log b b))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (log $0 $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '1' # 1
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= a 1)' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # 1
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (log v_{0} v_{0}))' # (log $0 $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= a (log b 1))' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'vor'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (log $0 1)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '0' # 0
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= a 0)' # fill it in
    eqsType = 'scheme'
    #filename = 'logarithm'
    direction = 'hin'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Logarithm(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # 0
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (log v_{0} 1))' # (log $0 1)
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
    