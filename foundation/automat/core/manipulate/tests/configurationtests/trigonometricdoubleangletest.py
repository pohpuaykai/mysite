import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.trigonometricdoubleangle import Trigonometricdoubleangle
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (sin (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (* "2" (sin x)) (cos x)))' # (* (* 2 (sin $0)) (cos $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (* (* "2" (sin x)) (cos x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (* 2 (sin $0)) (cos $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (* "2" x)))' # (sin (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (sin (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (* "2" (tan x)) (+ "1" (^ (tan x) "2"))))' # (/ (* 2 (tan $0)) (+ 1 (^ (tan $0) 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (/ (* "2" (tan x)) (+ "1" (^ (tan x) "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* 2 (tan $0)) (+ 1 (^ (tan $0) 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (* "2" x)))' # (sin (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (cos (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (^ (cos x) "2") (^ (sin x) "2")))' # (- (^ (cos $0) 2) (^ (sin $0) 2))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (- (^ (cos x) "2") (^ (sin x) "2")))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (^ (cos $0) 2) (^ (sin $0) 2))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (* "2" x)))' # (cos (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (cos (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (* "2" (^ (cos x) "2")) "1"))' # (- (* 2 (^ (cos $0) 2)) 1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (- (* "2" (^ (cos x) "2")) "1"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (* 2 (^ (cos $0) 2)) 1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (* "2" x)))' # (cos (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (cos (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "1" (* "2" (^ (sin x) "2"))))' # (- 1 (* 2 (^ (sin $0) 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (- "1" (* "2" (^ (sin x) "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- 1 (* 2 (^ (sin $0) 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (* "2" x)))' # (cos (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (cos (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- "1" (^ (tan x) "2")) (+ "1" (^ (tan x) "2"))))' # (/ (- 1 (^ (tan $0) 2)) (+ 1 (^ (tan $0) 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (/ (- "1" (^ (tan x) "2")) (+ "1" (^ (tan x) "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (- 1 (^ (tan $0) 2)) (+ 1 (^ (tan $0) 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (* "2" x)))' # (cos (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= y (tan (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (* "2" (tan x)) (- "1" (^ (tan x) "2"))))' # (/ (* 2 (tan $0)) (- 1 (^ (tan $0) 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= y (/ (* "2" (tan x)) (- "1" (^ (tan x) "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* 2 (tan $0)) (- 1 (^ (tan $0) 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan (* "2" x)))' # (tan (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor7__configTest(verbose=False):
    eqs = '(= y (cot (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cot (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (* (^ cot "2") x) "1") (* "2" (cot x))))' # (/ (- (* (^ cot 2) $0) 1) (* 2 (cot $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin7__configTest(verbose=False):
    eqs = '(= y (/ (- (* (^ cot "2") x) "1") (* "2" (cot x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (- (* (^ cot 2) $0) 1) (* 2 (cot $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cot (* "2" x)))' # (cot (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor8__configTest(verbose=False):
    eqs = '(= y (cot (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cot (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- "1" (* (^ tan "2") x)) (* "2" (tan x))))' # (/ (- 1 (* (^ tan 2) $0)) (* 2 (tan $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin8__configTest(verbose=False):
    eqs = '(= y (/ (- "1" (* (^ tan "2") x)) (* "2" (tan x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (- 1 (* (^ tan 2) $0)) (* 2 (tan $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cot (* "2" x)))' # (cot (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor9__configTest(verbose=False):
    eqs = '(= y (sec (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sec (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (^ (sec x) "2") (- "2" (* (^ sec "2") x))))' # (/ (^ (sec $0) 2) (- 2 (* (^ sec 2) $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin9__configTest(verbose=False):
    eqs = '(= y (/ (^ (sec x) "2") (- "2" (* (^ sec "2") x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (^ (sec $0) 2) (- 2 (* (^ sec 2) $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sec (* "2" x)))' # (sec (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor10__configTest(verbose=False):
    eqs = '(= y (sec (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sec (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ "1" (* (^ tan "2") x)) (- "1" (* (^ tan "2") x))))' # (/ (+ 1 (* (^ tan 2) $0)) (- 1 (* (^ tan 2) $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin10__configTest(verbose=False):
    eqs = '(= y (/ (+ "1" (* (^ tan "2") x)) (- "1" (* (^ tan "2") x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ 1 (* (^ tan 2) $0)) (- 1 (* (^ tan 2) $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sec (* "2" x)))' # (sec (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor11__configTest(verbose=False):
    eqs = '(= y (cosec (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cosec (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (* (sec x) (cosec x)) "2"))' # (/ (* (sec $0) (cosec $0)) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin11__configTest(verbose=False):
    eqs = '(= y (/ (* (sec x) (cosec x)) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* (sec $0) (cosec $0)) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosec (* "2" x)))' # (cosec (* 2 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor12__configTest(verbose=False):
    eqs = '(= y (cosec (* "2" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'vor'
    idx = 12
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cosec (* 2 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ "1" (* (^ tan "2") x)) (* "2" (tan x))))' # (/ (+ 1 (* (^ tan 2) $0)) (* 2 (tan $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin12__configTest(verbose=False):
    eqs = '(= y (/ (+ "1" (* (^ tan "2") x)) (* "2" (tan x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricdoubleangle'
    direction = 'hin'
    idx = 12
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricdoubleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ 1 (* (^ tan 2) $0)) (* 2 (tan $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosec (* "2" x)))' # (cosec (* 2 $0))
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
    test__vor12__configTest(True) # Not tested yet
    test__hin12__configTest(True) # Not tested yet
    