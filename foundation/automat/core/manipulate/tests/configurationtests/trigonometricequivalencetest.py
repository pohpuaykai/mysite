import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.trigonometricequivalence import Trigonometricequivalence
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (/ (sin b) (cos b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (sin $0) (cos $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (tan b))' # (tan $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (tan b))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ (sin b) (cos b)))' # (/ (sin $0) (cos $0))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (/ (cos b) (sin b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (cos $0) (sin $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (cot b))' # (cot $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a (cot b))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cot $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ (cos b) (sin b)))' # (/ (cos $0) (sin $0))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a (/ 1 (sin b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (sin $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (cosec b))' # (cosec $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= a (cosec b))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cosec $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ 1 (sin b)))' # (/ 1 (sin $0))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= a (/ 1 (cos b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (cos $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (sec b))' # (sec $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= a (sec b))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sec $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ 1 (sec b)))' # (/ 1 (sec $0))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= a (/ 1 (tan b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (tan $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (cot b))' # (cot $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= a (cot b))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cot $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ 1 (tan b)))' # (/ 1 (tan $0))
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= a (/ 1 (cot b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (cot $0))
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (tan b))' # (tan $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= a (tan b))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (/ 1 (cot b)))' # (/ 1 (cot $0))
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
    