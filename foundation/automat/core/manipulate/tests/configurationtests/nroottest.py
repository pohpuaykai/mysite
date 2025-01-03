import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.nroot import Nroot
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (nroot b (^ c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (nroot $0 (^ $1 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (^ c (/ d b)))' # (^ $1 (/ $2 $0))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (^ b (/ c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ $1 (/ $2 $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (nroot d (^ b c)))' # (nroot $0 (^ $1 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (^ (nroot b c) d))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ (nroot $0 $1) $2)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (nroot b (^ c d)))' # (nroot $0 (^ $1 $2))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a (nroot b (^ c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (nroot $0 (^ $1 $2))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (^ (nroot b c) d))' # (^ (nroot $0 $1) $2)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a (^ (nroot b c) d))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ (nroot $0 $1) $2)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (^ c (/ d b)))' # (^ $1 (/ $2 $0))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= a (^ b (/ c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ $1 (/ $2 $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (^ (nroot d b) c))' # (^ (nroot $0 $1) $2)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= a (nroot b (* c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (nroot $2 (* $0 $1))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (* (nroot b c) (nroot b d)))' # (* (nroot $2 $0) (nroot $2 $1))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= a (* (nroot b c) (nroot b d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (nroot $2 $0) (nroot $2 $1))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (nroot b (* c d)))' # (nroot $2 (* $0 $1))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= a (nroot b (/ c d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (nroot $2 (/ $0 $1))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ (nroot b c) (nroot b d)))' # (/ (nroot $2 $0) (nroot $2 $1))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= a (/ (nroot b c) (nroot b d)))' # fill it in
    eqsType = 'scheme'
    #filename = 'nroot'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Nroot(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (nroot $2 $0) (nroot $2 $1))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (nroot b (/ c d)))' # (nroot $2 (/ $0 $1))
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
    