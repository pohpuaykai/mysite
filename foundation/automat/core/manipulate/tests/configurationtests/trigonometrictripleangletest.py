import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.trigonometrictripleangle import Trigonometrictripleangle
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (sin (* "3" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (* 3 x))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (* "3" (sin x)) (* "4" (^ (sin x) "3"))))' # (- (* 3 (sin x)) (* 4 (^ (sin x) 3)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (- (* "3" (sin x)) (* "4" (^ (sin x) "3"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (* 3 (sin x)) (* 4 (^ (sin x) 3)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (* "3" x)))' # (sin (* 3 x))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (cos (* "3" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (* 3 x))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (* "4" (^ (cos x) "3")) (* "3" (cos x))))' # (- (* 4 (^ (cos x) 3)) (* 3 (cos x)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (- (* "4" (^ (cos x) "3")) (* "3" (cos x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (* 4 (^ (cos x) 3)) (* 3 (cos x)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (* "3" x)))' # (cos (* 3 x))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (tan (* "3" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (* 3 x))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (* "3" (tan x)) (^ (tan x) "3")) (- "1" (* "3" (^ (tan x) "2")))))' # (/ (- (* 3 (tan x)) (^ (tan x) 3)) (- 1 (* 3 (^ (tan x) 2))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (/ (- (* "3" (tan x)) (^ (tan x) "3")) (- "1" (* "3" (^ (tan x) "2")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (- (* 3 (tan x)) (^ (tan x) 3)) (- 1 (* 3 (^ (tan x) 2))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan (* "3" x)))' # (tan (* 3 x))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (cot (* "3" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cot (* 3 x))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (* "3" (cot x)) (^ (cot x) "3")) (- "1" (* "3" (^ (cot x) "2")))))' # (/ (- (* 3 (cot x)) (^ (cot x) 3)) (- 1 (* 3 (^ (cot x) 2))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (/ (- (* "3" (cot x)) (^ (cot x) "3")) (- "1" (* "3" (^ (cot x) "2")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (- (* 3 (cot x)) (^ (cot x) 3)) (- 1 (* 3 (^ (cot x) 2))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cot (* "3" x)))' # (cot (* 3 x))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (sec (* "3" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sec (* 3 x))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (^ (sec x) "3") (- "4" (* "3" (^ (sec x) "2")))))' # (/ (^ (sec x) 3) (- 4 (* 3 (^ (sec x) 2))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (/ (^ (sec x) "3") (- "4" (* "3" (^ (sec x) "2")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (^ (sec x) 3) (- 4 (* 3 (^ (sec x) 2))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sec (* "3" x)))' # (sec (* 3 x))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (cosec (* "3" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cosec (* 3 x))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (^ (cosec x) "3") (- (* "3" (^ (cosec x) "3")) "4")))' # (/ (^ (cosec x) 3) (- (* 3 (^ (cosec x) 3)) 4))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (/ (^ (cosec x) "3") (- (* "3" (^ (cosec x) "3")) "4")))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometrictripleangle'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometrictripleangle(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (^ (cosec x) 3) (- (* 3 (^ (cosec x) 3)) 4))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosec (* "3" x)))' # (cosec (* 3 x))
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
    