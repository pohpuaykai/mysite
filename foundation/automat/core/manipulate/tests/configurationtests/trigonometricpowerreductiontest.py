import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.trigonometricpowerreduction import Trigonometricpowerreduction
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (^ (sin x) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (^ (sin $0) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- "1" (cos (* "2" x))) "2"))' # (/ (- 1 (cos (* 2 $0))) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (/ (- "1" (cos (* "2" x))) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (- 1 (cos (* 2 $0))) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (^ (sin x) "2"))' # (^ (sin $0) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (^ (sin x) "3"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (^ (sin $0) 3)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (* "3" (sin x)) (sin (* "3" x))) "4"))' # (/ (- (* 3 (sin $0)) (sin (* 3 $0))) 4)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (/ (- (* "3" (sin x)) (sin (* "3" x))) "4"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (- (* 3 (sin $0)) (sin (* 3 $0))) 4)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (^ (sin x) "3"))' # (^ (sin $0) 3)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (^ (sin x) "4"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (^ (sin $0) 4)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (- "3" (* "4" (cos (* "2" x)))) (cos (* "4" x))) "8"))' # (/ (+ (- 3 (* 4 (cos (* 2 $0)))) (cos (* 4 $0))) 8)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (/ (+ (- "3" (* "4" (cos (* "2" x)))) (cos (* "4" x))) "8"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (- 3 (* 4 (cos (* 2 $0)))) (cos (* 4 $0))) 8)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (^ (sin x) "4"))' # (^ (sin $0) 4)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (^ (sin x) "5"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (^ (sin $0) 5)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (- (* "10" (sin x)) (* "5" (sin (* "3" x)))) (sin (* "5" x))) "16"))' # (/ (+ (- (* 10 (sin $0)) (* 5 (sin (* 3 $0)))) (sin (* 5 $0))) 16)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (/ (+ (- (* "10" (sin x)) (* "5" (sin (* "3" x)))) (sin (* "5" x))) "16"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (- (* 10 (sin $0)) (* 5 (sin (* 3 $0)))) (sin (* 5 $0))) 16)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (^ (sin x) "5"))' # (^ (sin $0) 5)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (^ (cos x) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (^ (cos $0) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ "1" (cos (* "2" x))) "2"))' # (/ (+ 1 (cos (* 2 $0))) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (/ (+ "1" (cos (* "2" x))) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ 1 (cos (* 2 $0))) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (^ (cos x) "2"))' # (^ (cos $0) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (^ (cos x) "3"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (^ (cos $0) 3)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (* "3" (cos x)) (cos (* "3" x))) "4"))' # (/ (+ (* 3 (cos $0)) (cos (* 3 $0))) 4)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (/ (+ (* "3" (cos x)) (cos (* "3" x))) "4"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (* 3 (cos $0)) (cos (* 3 $0))) 4)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (^ (cos x) "3"))' # (^ (cos $0) 3)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= y (^ (cos x) "4"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (^ (cos $0) 4)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (+ "3" (* "4" (cos (* "2" x)))) (cos (* "4" x))) "8"))' # (/ (+ (+ 3 (* 4 (cos (* 2 $0)))) (cos (* 4 $0))) 8)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= y (/ (+ (+ "3" (* "4" (cos (* "2" x)))) (cos (* "4" x))) "8"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (+ 3 (* 4 (cos (* 2 $0)))) (cos (* 4 $0))) 8)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (^ (cos x) "4"))' # (^ (cos $0) 4)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor7__configTest(verbose=False):
    eqs = '(= y (^ (cos x) "5"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (^ (cos $0) 5)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (+ (* "10" (cos x)) (* "5" (cos x))) (cos (* "5" x))) "16"))' # (/ (+ (+ (* 10 (cos $0)) (* 5 (cos $0))) (cos (* 5 $0))) 16)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin7__configTest(verbose=False):
    eqs = '(= y (/ (+ (+ (* "10" (cos x)) (* "5" (cos x))) (cos (* "5" x))) "16"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (+ (* 10 (cos $0)) (* 5 (cos $0))) (cos (* 5 $0))) 16)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (^ (cos x) "5"))' # (^ (cos $0) 5)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor8__configTest(verbose=False):
    eqs = '(= y (* (^ (sin x) "2") (^ (cos x) "2")))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (^ (sin $0) 2) (^ (cos $0) 2))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- "1" (cos (* "4" x))) "8"))' # (/ (- 1 (cos (* 4 $0))) 8)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin8__configTest(verbose=False):
    eqs = '(= y (/ (- "1" (cos (* "4" x))) "8"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (- 1 (cos (* 4 $0))) 8)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (^ (sin x) "2") (^ (cos x) "2")))' # (* (^ (sin $0) 2) (^ (cos $0) 2))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor9__configTest(verbose=False):
    eqs = '(= y (* (^ (sin x) "3") (^ (cos x) "3")))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (^ (sin $0) 3) (^ (cos $0) 3))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (* "3" (sin (* "2" x))) (sin (* "6" x))) "32"))' # (/ (- (* 3 (sin (* 2 $0))) (sin (* 6 $0))) 32)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin9__configTest(verbose=False):
    eqs = '(= y (/ (- (* "3" (sin (* "2" x))) (sin (* "6" x))) "32"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (- (* 3 (sin (* 2 $0))) (sin (* 6 $0))) 32)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (^ (sin x) "3") (^ (cos x) "3")))' # (* (^ (sin $0) 3) (^ (cos $0) 3))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor10__configTest(verbose=False):
    eqs = '(= y (* (^ (sin x) "4") (^ (cos x) "4")))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (^ (sin $0) 4) (^ (cos $0) 4))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (- "3" (* "4" (cos (* "4" x)))) (cos (* "8" x))) "128"))' # (/ (+ (- 3 (* 4 (cos (* 4 $0)))) (cos (* 8 $0))) 128)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin10__configTest(verbose=False):
    eqs = '(= y (/ (+ (- "3" (* "4" (cos (* "4" x)))) (cos (* "8" x))) "128"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (- 3 (* 4 (cos (* 4 $0)))) (cos (* 8 $0))) 128)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (^ (sin x) "4") (^ (cos x) "4")))' # (* (^ (sin $0) 4) (^ (cos $0) 4))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor11__configTest(verbose=False):
    eqs = '(= y (* (^ (sin x) "5") (^ (cos x) "5")))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'vor'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (^ (sin $0) 5) (^ (cos $0) 5))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (- (* "10" (sin (* "2" x))) (* "5" (sin (* "6" x)))) (sin (* "10" x))) "512"))' # (/ (+ (- (* 10 (sin (* 2 $0))) (* 5 (sin (* 6 $0)))) (sin (* 10 $0))) 512)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin11__configTest(verbose=False):
    eqs = '(= y (/ (+ (- (* "10" (sin (* "2" x))) (* "5" (sin (* "6" x)))) (sin (* "10" x))) "512"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricpowerreduction'
    direction = 'hin'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricpowerreduction(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (- (* 10 (sin (* 2 $0))) (* 5 (sin (* 6 $0)))) (sin (* 10 $0))) 512)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (^ (sin x) "5") (^ (cos x) "5")))' # (* (^ (sin $0) 5) (^ (cos $0) 5))
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
    test__vor11__configTest(True) # Not tested yet
    test__hin11__configTest(True) # Not tested yet
    