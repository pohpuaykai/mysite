import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.trigonometricarctrigonometric import Trigonometricarctrigonometric
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (sin (arcsin x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (arcsin $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y x)' # $0
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y x)' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (sin (arcsin y)) (sin (arcsin x)))' # (sin (arcsin $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (sin (arccos x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (arccos $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (nroot "2" (- "1" (^ x "2"))))' # (nroot 2 (- 1 (^ $0 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (nroot "2" (- "1" (^ x "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (nroot 2 (- 1 (^ $0 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (arccos x)))' # (sin (arccos $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (sin (arctan x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (arctan $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ x (nroot "2" (+ "1" (^ x "2")))))' # (/ $0 (nroot 2 (+ 1 (^ $0 2))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (/ x (nroot "2" (+ "1" (^ x "2")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ $0 (nroot 2 (+ 1 (^ $0 2))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (arctan x)))' # (sin (arctan $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (sin (arccosec x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (arccosec $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ "1" x))' # (/ 1 $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (/ "1" x))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (arccosec x)))' # (sin (arccosec $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (sin (arcsec x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (arcsec $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (nroot "2" (- (^ x "2") "1")) x))' # (/ (nroot 2 (- (^ $0 2) 1)) $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (/ (nroot "2" (- (^ x "2") "1")) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (nroot 2 (- (^ $0 2) 1)) $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (arcsec x)))' # (sin (arcsec $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (sin (arccot x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (arccot $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ "1" (nroot "2" (+ "1" (^ x "2")))))' # (/ 1 (nroot 2 (+ 1 (^ $0 2))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (/ "1" (nroot "2" (+ "1" (^ x "2")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (nroot 2 (+ 1 (^ $0 2))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (arccot x)))' # (sin (arccot $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= y (cos (arcsin x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (arcsin $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (nroot "2" (- "1" (^ x "2"))))' # (nroot 2 (- 1 (^ $0 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= y (nroot "2" (- "1" (^ x "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (nroot 2 (- 1 (^ $0 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (arcsin x)))' # (cos (arcsin $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor7__configTest(verbose=False):
    eqs = '(= y (cos (arccos x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (arccos $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y x)' # $0
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin7__configTest(verbose=False):
    eqs = '(= y x)' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (cos (arccos y)) (cos (arccos x)))' # (cos (arccos $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor8__configTest(verbose=False):
    eqs = '(= y (cos (arctan x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (arctan $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ "1" (nroot "2" (+ "1" (^ x "2")))))' # (/ 1 (nroot 2 (+ 1 (^ $0 2))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin8__configTest(verbose=False):
    eqs = '(= y (/ "1" (nroot "2" (+ "1" (^ x "2")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (nroot 2 (+ 1 (^ $0 2))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (arctan x)))' # (cos (arctan $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor9__configTest(verbose=False):
    eqs = '(= y (cos (arccosec x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (arccosec $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (nroot "2" (- (^ x "2") "1")) x))' # (/ (nroot 2 (- (^ $0 2) 1)) $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin9__configTest(verbose=False):
    eqs = '(= y (/ (nroot "2" (- (^ x "2") "1")) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (nroot 2 (- (^ $0 2) 1)) $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (arccosec x)))' # (cos (arccosec $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor10__configTest(verbose=False):
    eqs = '(= y (cos (arcsec x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (arcsec $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ "1" x))' # (/ 1 $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin10__configTest(verbose=False):
    eqs = '(= y (/ "1" x))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (arcsec x)))' # (cos (arcsec $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor11__configTest(verbose=False):
    eqs = '(= y (cos (arccot x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (arccot $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ x (nroot "2" (+ "1" (^ x "2")))))' # (/ $0 (nroot 2 (+ 1 (^ $0 2))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin11__configTest(verbose=False):
    eqs = '(= y (/ x (nroot "2" (+ "1" (^ x "2")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ $0 (nroot 2 (+ 1 (^ $0 2))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (arccot x)))' # (cos (arccot $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor12__configTest(verbose=False):
    eqs = '(= y (tan (arcsin x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 12
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (arcsin $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ x (nroot "2" (- "1" (^ x "2")))))' # (/ $0 (nroot 2 (- 1 (^ $0 2))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin12__configTest(verbose=False):
    eqs = '(= y (/ x (nroot "2" (- "1" (^ x "2")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 12
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ $0 (nroot 2 (- 1 (^ $0 2))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan (arcsin x)))' # (tan (arcsin $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor13__configTest(verbose=False):
    eqs = '(= y (tan (arccos x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 13
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (arccos $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (nroot "2" (- "1" (^ x "2"))) x))' # (/ (nroot 2 (- 1 (^ $0 2))) $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin13__configTest(verbose=False):
    eqs = '(= y (/ (nroot "2" (- "1" (^ x "2"))) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 13
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (nroot 2 (- 1 (^ $0 2))) $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan (arccos x)))' # (tan (arccos $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor14__configTest(verbose=False):
    eqs = '(= y (tan (arctan x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 14
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (arctan $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y x)' # $0
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin14__configTest(verbose=False):
    eqs = '(= y x)' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 14
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (tan (arctan y)) (tan (arctan x)))' # (tan (arctan $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor15__configTest(verbose=False):
    eqs = '(= y (tan (arccosec x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 15
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (arccosec $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ "1" (nroot "2" (- (^ x "2") "1"))))' # (/ 1 (nroot 2 (- (^ $0 2) 1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin15__configTest(verbose=False):
    eqs = '(= y (/ "1" (nroot "2" (- (^ x "2") "1"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 15
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 (nroot 2 (- (^ $0 2) 1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan (arccosec x)))' # (tan (arccosec $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor16__configTest(verbose=False):
    eqs = '(= y (tan (arcsec x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 16
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (arcsec $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (nroot "2" (- (^ x "2") "1")))' # (nroot 2 (- (^ $0 2) 1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin16__configTest(verbose=False):
    eqs = '(= y (nroot "2" (- (^ x "2") "1")))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 16
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (nroot 2 (- (^ $0 2) 1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan (arcsec x)))' # (tan (arcsec $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor17__configTest(verbose=False):
    eqs = '(= y (tan (arccot $0)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'vor'
    idx = 17
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (arccot $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ "1" $0))' # (/ 1 $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin17__configTest(verbose=False):
    eqs = '(= y (/ "1" $0))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricarctrigonometric'
    direction = 'hin'
    idx = 17
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricarctrigonometric(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ 1 $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan (arccot $0)))' # (tan (arccot $0))
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
    test__vor13__configTest(True) # Not tested yet
    test__hin13__configTest(True) # Not tested yet
    test__vor14__configTest(True) # Not tested yet
    test__hin14__configTest(True) # Not tested yet
    test__vor15__configTest(True) # Not tested yet
    test__hin15__configTest(True) # Not tested yet
    test__vor16__configTest(True) # Not tested yet
    test__hin16__configTest(True) # Not tested yet
    test__vor17__configTest(True) # Not tested yet
    test__hin17__configTest(True) # Not tested yet
    