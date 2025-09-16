import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.trigonometricplusminus import Trigonometricplusminus
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (sin (+ x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (+ $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (* (sin x) (cos z)) (* (cos x) (sin z))))' # (+ (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (+ (* (sin x) (cos z)) (* (cos x) (sin z))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (+ x z)))' # (sin (+ $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (sin (- x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (sin (- $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (* (sin x) (cos z)) (* (cos x) (sin z))))' # (- (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (- (* (sin x) (cos z)) (* (cos x) (sin z))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (- x z)))' # (sin (- $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (cos (+ x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (+ $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (* (cos x) (cos z)) (* (sin x) (sin z))))' # (- (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (- (* (cos x) (cos z)) (* (sin x) (sin z))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (+ x z)))' # (cos (+ $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (cos (- x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cos (- $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (* (cos x) (cos z)) (* (sin x) (sin z))))' # (+ (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (+ (* (cos x) (cos z)) (* (sin x) (sin z))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (- x z)))' # (cos (- $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (tan (+ x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (+ $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (tan x) (tan z)) (- "1" (* (tan x) (tan z)))))' # (/ (+ (tan $0) (tan $1)) (- 1 (* (tan $0) (tan $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (/ (+ (tan x) (tan z)) (- "1" (* (tan x) (tan z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ (tan $0) (tan $1)) (- 1 (* (tan $0) (tan $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan (+ x z)))' # (tan (+ $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (tan (- x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (tan (- $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (tan x) (tan z)) (+ "1" (* (tan x) (tan z)))))' # (/ (- (tan $0) (tan $1)) (+ 1 (* (tan $0) (tan $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (/ (- (tan x) (tan z)) (+ "1" (* (tan x) (tan z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (- (tan $0) (tan $1)) (+ 1 (* (tan $0) (tan $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan (- x z)))' # (tan (- $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= y (cosec (+ x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cosec (+ $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (+ (* (sec x) (cosec z)) (* (cosec x) (sec z)))))' # (/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (+ (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (+ (* (sec x) (cosec z)) (* (cosec x) (sec z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (+ (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosec (+ x z)))' # (cosec (+ $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor7__configTest(verbose=False):
    eqs = '(= y (cosec (- x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cosec (- $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (- (* (sec x) (cosec z)) (* (cosec x) (sec z)))))' # (/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (- (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin7__configTest(verbose=False):
    eqs = '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (- (* (sec x) (cosec z)) (* (cosec x) (sec z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (- (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosec (- x z)))' # (cosec (- $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor8__configTest(verbose=False):
    eqs = '(= y (cosec (+ x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cosec (+ $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (- (* (sec x) (cosec z)) (* (cosec x) (sec z)))))' # (/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (- (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin8__configTest(verbose=False):
    eqs = '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (- (* (sec x) (cosec z)) (* (cosec x) (sec z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (- (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosec (+ x z)))' # (cosec (+ $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor9__configTest(verbose=False):
    eqs = '(= y (cosec (- x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cosec (- $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (+ (* (sec x) (cosec z)) (* (cosec x) (sec z)))))' # (/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (+ (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin9__configTest(verbose=False):
    eqs = '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (+ (* (sec x) (cosec z)) (* (cosec x) (sec z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (+ (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosec (- x z)))' # (cosec (- $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor10__configTest(verbose=False):
    eqs = '(= y (cot (+ x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cot (+ $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (* (cot x) (cot z)) "1") (+ (cot z) (cot x))))' # (/ (- (* (cot $0) (cot $1)) 1) (+ (cot $1) (cot $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin10__configTest(verbose=False):
    eqs = '(= y (/ (- (* (cot x) (cot z)) "1") (+ (cot z) (cot x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (- (* (cot $0) (cot $1)) 1) (+ (cot $1) (cot $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cot (+ x z)))' # (cot (+ $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor11__configTest(verbose=False):
    eqs = '(= y (cot (- x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (cot (- $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (* (cot x) (cot z)) "1") (- (cot z) (cot x))))' # (/ (+ (* (cot $0) (cot $1)) 1) (- (cot $1) (cot $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin11__configTest(verbose=False):
    eqs = '(= y (/ (+ (* (cot x) (cot z)) "1") (- (cot z) (cot x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ (* (cot $0) (cot $1)) 1) (- (cot $1) (cot $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cot (- x z)))' # (cot (- $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor12__configTest(verbose=False):
    eqs = '(= y (+ (arcsin x) (arcsin z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 12
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (arcsin $0) (arcsin $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arcsin (+ (* x (nroot "2" (- "1" (^ z "2")))) (* z (nroot "2" (- "1" (^ x "2")))))))' # (arcsin (+ (* $0 (nroot 2 (- 1 (^ $1 2)))) (* $1 (nroot 2 (- 1 (^ $0 2))))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin12__configTest(verbose=False):
    eqs = '(= y (arcsin (+ (* x (nroot "2" (- "1" (^ z "2")))) (* z (nroot "2" (- "1" (^ x "2")))))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 12
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arcsin (+ (* $0 (nroot 2 (- 1 (^ $1 2)))) (* $1 (nroot 2 (- 1 (^ $0 2))))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arcsin x) (arcsin z)))' # (+ (arcsin $0) (arcsin $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor13__configTest(verbose=False):
    eqs = '(= y (- (arcsin x) (arcsin z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 13
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (arcsin $0) (arcsin $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arcsin (- (* x (nroot "2" (- "1" (^ z "2")))) (* z (nroot "2" (- "1" (^ x "2")))))))' # (arcsin (- (* $0 (nroot 2 (- 1 (^ $1 2)))) (* $1 (nroot 2 (- 1 (^ $0 2))))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin13__configTest(verbose=False):
    eqs = '(= y (arcsin (- (* x (nroot "2" (- "1" (^ z "2")))) (* z (nroot "2" (- "1" (^ x "2")))))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 13
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arcsin (- (* $0 (nroot 2 (- 1 (^ $1 2)))) (* $1 (nroot 2 (- 1 (^ $0 2))))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (arcsin x) (arcsin z)))' # (- (arcsin $0) (arcsin $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor14__configTest(verbose=False):
    eqs = '(= y (+ (arccos x) (arccos z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 14
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (arccos $0) (arccos $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccos (- (* x z) (nroot "2" (* (- "1" (^ x "2")) (- "1" (^ z "2")))))))' # (arccos (- (* $0 $1) (nroot 2 (* (- 1 (^ $0 2)) (- 1 (^ $1 2))))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin14__configTest(verbose=False):
    eqs = '(= y (arccos (- (* x z) (nroot "2" (* (- "1" (^ x "2")) (- "1" (^ z "2")))))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 14
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccos (- (* $0 $1) (nroot 2 (* (- 1 (^ $0 2)) (- 1 (^ $1 2))))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arccos x) (arccos z)))' # (+ (arccos $0) (arccos $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor15__configTest(verbose=False):
    eqs = '(= y (- (arccos x) (arccos z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 15
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (arccos $0) (arccos $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccos (+ (* x z) (nroot "2" (* (- "1" (^ x "2")) (- "1" (^ z "2")))))))' # (arccos (+ (* $0 $1) (nroot 2 (* (- 1 (^ $0 2)) (- 1 (^ $1 2))))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin15__configTest(verbose=False):
    eqs = '(= y (arccos (+ (* x z) (nroot "2" (* (- "1" (^ x "2")) (- "1" (^ z "2")))))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 15
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccos (+ (* $0 $1) (nroot 2 (* (- 1 (^ $0 2)) (- 1 (^ $1 2))))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (arccos x) (arccos z)))' # (- (arccos $0) (arccos $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor16__configTest(verbose=False):
    eqs = '(= y (+ (arctan x) (arctan z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 16
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (arctan $0) (arctan $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arctan (/ (+ x z) (- "1" (* x z)))))' # (arctan (/ (+ $0 $1) (- 1 (* $0 $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin16__configTest(verbose=False):
    eqs = '(= y (arctan (/ (+ x z) (- "1" (* x z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 16
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arctan (/ (+ $0 $1) (- 1 (* $0 $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arctan x) (arctan z)))' # (+ (arctan $0) (arctan $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor17__configTest(verbose=False):
    eqs = '(= y (- (arctan x) (arctan z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 17
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (arctan $0) (arctan $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arctan (/ (- x z) (+ "1" (* x z)))))' # (arctan (/ (- $0 $1) (+ 1 (* $0 $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin17__configTest(verbose=False):
    eqs = '(= y (arctan (/ (- x z) (+ "1" (* x z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 17
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arctan (/ (- $0 $1) (+ 1 (* $0 $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (arctan x) (arctan z)))' # (- (arctan $0) (arctan $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor18__configTest(verbose=False):
    eqs = '(= y (+ (arccot x) (arccot z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 18
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (arccot $0) (arccot $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccot (/ (- (* x z) "1") (+ z x))))' # (arccot (/ (- (* $0 $1) 1) (+ $1 $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin18__configTest(verbose=False):
    eqs = '(= y (arccot (/ (- (* x z) "1") (+ z x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 18
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccot (/ (- (* $0 $1) 1) (+ $1 $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arccot x) (arccot z)))' # (+ (arccot $0) (arccot $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor19__configTest(verbose=False):
    eqs = '(= y (- (arccot x) (arccot z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'vor'
    idx = 19
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (arccot $0) (arccot $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccot (/ (+ (* x z) "1") (- z x))))' # (arccot (/ (+ (* $0 $1) 1) (- $1 $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin19__configTest(verbose=False):
    eqs = '(= y (arccot (/ (+ (* x z) "1") (- z x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'trigonometricplusminus'
    direction = 'hin'
    idx = 19
    eq0 = Equation(eqs, eqsType)
    ma0 = Trigonometricplusminus(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccot (/ (+ (* $0 $1) 1) (- $1 $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (arccot x) (arccot z)))' # (- (arccot $0) (arccot $1))
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
    test__vor18__configTest(True) # Not tested yet
    test__hin18__configTest(True) # Not tested yet
    test__vor19__configTest(True) # Not tested yet
    test__hin19__configTest(True) # Not tested yet
    