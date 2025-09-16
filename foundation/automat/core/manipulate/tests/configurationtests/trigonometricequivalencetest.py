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
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (tan b))' # (tan $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
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
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (/ (sin b) (cos b)))' # (/ (sin $0) (cos $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
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
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (cot b))' # (cot $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
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
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (/ (cos b) (sin b)))' # (/ (cos $0) (sin $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a (/ "1" (sin b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (sin $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (cosec b))' # (cosec $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
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
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (/ "1" (sin b)))' # (/ 1 (sin $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= a (/ "1" (cos b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (cos $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (sec b))' # (sec $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
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
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (/ "1" (cos b)))' # (/ 1 (cos $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= a (/ "1" (tan b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (tan $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (cot b))' # (cot $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
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
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (/ "1" (tan b)))' # (/ 1 (tan $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= a (/ "1" (cot b)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (cot $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (tan b))' # (tan $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
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
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= a (/ "1" (cot b)))' # (/ 1 (cot $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= y (sin (- "0" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (- 0 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (sin x)))' # (- 0 (sin $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= y (- "0" (sin x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- 0 (sin $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (- "0" x)))' # (sin (- 0 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor7__configTest(verbose=False):
    eqs = '(= y (cos (- "0" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (- 0 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos x))' # (cos $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin7__configTest(verbose=False):
    eqs = '(= y (cos x))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (- "0" x)))' # (cos (- 0 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor8__configTest(verbose=False):
    eqs = '(= y (sin x))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) (* "2" "i")))' # (/ (- (^ e (* i $0)) (^ e (- 0 (* i $0)))) (* 2 i))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin8__configTest(verbose=False):
    eqs = '(= y (/ (- (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) (* "2" "i")))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (- (^ e (* i $0)) (^ e (- 0 (* i $0)))) (* 2 i))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin x))' # (sin $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor9__configTest(verbose=False):
    eqs = '(= y (cos x))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) "2"))' # (/ (+ (^ e (* i $0)) (^ e (- 0 (* i $0)))) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin9__configTest(verbose=False):
    eqs = '(= y (/ (+ (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ (^ e (* i $0)) (^ e (- 0 (* i $0)))) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos x))' # (cos $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor10__configTest(verbose=False):
    eqs = '(= y (^ "e" (* "i" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'vor'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (^ e (* i $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (cos x) (* "i" (sin x))))' # (+ (cos $0) (* i (sin $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin10__configTest(verbose=False):
    eqs = '(= y (+ (cos x) (* "i" (sin x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricequivalence'
    direction = 'hin'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricequivalence(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (cos $0) (* i (sin $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (^ "e" (* "i" x)))' # (^ e (* i $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    


if __name__=='__main__':
    test__vor0__configTest(True) # Not tested yet
    test__hin0__configTest(True) # Not tested yet
    test__vor1__configTest(True) # Not tested yet
    test__hin1__configTest(True) # Not tested yet
    test__vor2__configTest(True) # Not tested yet
    test__hin2__configTest(True) # Not tested yet
    test__vor3__configTest(True) # Not tested yet
    test__hin3__configTest(True) # Not tested yet
    test__vor4__configTest(True) # Not tested yet
    test__hin4__configTest(True) # Not tested yet
    test__vor5__configTest(True) # Not tested yet
    test__hin5__configTest(True) # Not tested yet
    test__vor6__configTest(True) # Not tested yet
    test__hin6__configTest(True) # Not tested yet
    test__vor7__configTest(True) # Not tested yet
    test__hin7__configTest(True) # Not tested yet
    test__vor8__configTest(True) # Not tested yet
    test__hin8__configTest(True) # Not tested yet
    test__vor9__configTest(True) # Not tested yet
    test__hin9__configTest(True) # Not tested yet
    test__vor10__configTest(True) # Not tested yet
    test__hin10__configTest(True) # Not tested yet
    