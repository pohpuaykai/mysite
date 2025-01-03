import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.exponential import Exponential
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (^ b 0))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ $0 0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '1' # 1
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (+ 1 (+ 1 1)))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # 1
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (+ (^ v_{0} 0) (+ (^ v_{0} 0) (^ v_{0} 0))))' # (^ $0 0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (^ b 1))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ $0 1)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a b)' # $0
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a a)' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= (^ a 1) (^ a 1))' # (^ $0 1)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a (^ b (+ c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ $0 (+ $1 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (* (^ b c) (^ b d)))' # (* (^ $0 $1) (^ $0 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= a (* (^ b c) (^ b d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (^ $0 $1) (^ $0 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (^ b (+ c d)))' # (^ $0 (+ $1 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= a (^ (^ b c) d))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ (^ $0 $1) $2)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (^ b (* c d)))' # (^ $0 (* $1 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= a (^ b (* c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ $0 (* $1 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (^ (^ b c) d))' # (^ (^ $0 $1) $2)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= a (* (^ b c) (^ d c)))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (^ $1 $0) (^ $2 $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (^ (* b d) c))' # (^ (* $1 $2) $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= a (^ (* b c) d))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ (* $1 $2) $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (* (^ b d) (^ c d)))' # (* (^ $1 $0) (^ $2 $0))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= a (^ b (- "0" c)))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ $0 (- "0" $1))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ "1" (^ b c)))' # (/ "1" (^ $0 $1))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= a (/ "1" (^ b c)))' # fill it in
    eqsType = 'scheme'
    #filename = 'exponential'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Exponential(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ "1" (^ $0 $1))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (^ b (- "0" c)))' # (^ $0 (- "0" $1))
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
    