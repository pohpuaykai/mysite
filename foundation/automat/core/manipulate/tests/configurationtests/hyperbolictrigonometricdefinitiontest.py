import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.hyperbolictrigonometricdefinition import Hyperbolictrigonometricdefinition
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (cosh x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cosh $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (^ "e" x) (^ "e" (- "0" x))) "2"))' # (/ (+ (^ e $0) (^ e (- 0 $0))) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (/ (+ (^ "e" x) (^ "e" (- "0" x))) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (^ e $0) (^ e (- 0 $0))) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosh x))' # (cosh $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (sinh x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sinh $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (^ "e" x) (^ "e" (- "0" x))) "2"))' # (/ (- (^ e $0) (^ e (- 0 $0))) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (/ (- (^ "e" x) (^ "e" (- "0" x))) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (- (^ e $0) (^ e (- 0 $0))) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sinh x))' # (sinh $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (cosh (- "0" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cosh (- 0 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosh x))' # (cosh $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (cosh x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cosh $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosh (- "0" x)))' # (cosh (- 0 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (sin x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sin $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (* "i" (sinh (* "i" x)))))' # (- 0 (* i (sinh (* i $0))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (- "0" (* "i" (sinh (* "i" x)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (* i (sinh (* i $0))))
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

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (cos x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cos $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosh (* "i" x)))' # (cosh (* i $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (cosh (* "i" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cosh (* i $0))
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

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (sin (* "i" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sin (* i $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* "i" (sinh x)))' # (* i (sinh $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (* "i" (sinh x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* i (sinh $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sin (* "i" x)))' # (sin (* i $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= y (cos (* "i" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cos (* i $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosh x))' # (cosh $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= y (cosh x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cosh $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cos (* "i" x)))' # (cos (* i $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor7__configTest(verbose=False):
    eqs = '(= y (sinh (- "0" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sinh (- 0 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (sinh x)))' # (- 0 (sinh $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin7__configTest(verbose=False):
    eqs = '(= y (- "0" (sinh x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (sinh $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sinh (- "0" x)))' # (sinh (- 0 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor8__configTest(verbose=False):
    eqs = '(= y (tan x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (tan $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (* "i" (tanh (* "i" x)))))' # (- 0 (* i (tanh (* i $0))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin8__configTest(verbose=False):
    eqs = '(= y (- "0" (* "i" (tanh (* "i" x)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (* i (tanh (* i $0))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tan x))' # (tan $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor9__configTest(verbose=False):
    eqs = '(= y (cot x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cot $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* "i" (coth (* "i" x))))' # (* i (coth (* i $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin9__configTest(verbose=False):
    eqs = '(= y (* "i" (coth (* "i" x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 9
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* i (coth (* i $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cot x))' # (cot $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor10__configTest(verbose=False):
    eqs = '(= y (sec x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sec $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sech (* "i" x)))' # (sech (* i $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin10__configTest(verbose=False):
    eqs = '(= y (sech (* "i" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 10
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sech (* i $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sec x))' # (sec $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor11__configTest(verbose=False):
    eqs = '(= y (cosec x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cosec $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* "i" (cosech (* "i" x))))' # (* i (cosech (* i $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin11__configTest(verbose=False):
    eqs = '(= y (* "i" (cosech (* "i" x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 11
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* i (cosech (* i $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosec x))' # (cosec $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor12__configTest(verbose=False):
    eqs = '(= y (tanh (- "0" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 12
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (tanh (- 0 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (tanh x)))' # (- 0 (tanh $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin12__configTest(verbose=False):
    eqs = '(= y (- "0" (tanh x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 12
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (tanh $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tanh (- "0" x)))' # (tanh (- 0 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor13__configTest(verbose=False):
    eqs = '(= y (coth (- "0" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 13
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (coth (- 0 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (coth x)))' # (- 0 (coth $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin13__configTest(verbose=False):
    eqs = '(= y (- "0" (coth x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 13
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (coth $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (coth (- "0" x)))' # (coth (- 0 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor14__configTest(verbose=False):
    eqs = '(= y (sech (- "0" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 14
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sech (- 0 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sech x))' # (sech $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin14__configTest(verbose=False):
    eqs = '(= y (sech x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 14
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sech $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sech (- "0" x)))' # (sech (- 0 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor15__configTest(verbose=False):
    eqs = '(= y (cosech (- "0" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'vor'
    idx = 15
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cosech (- 0 $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (cosech x)))' # (- 0 (cosech $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin15__configTest(verbose=False):
    eqs = '(= y (- "0" (cosech x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricdefinition'
    direction = 'hin'
    idx = 15
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricdefinition(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (cosech $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosech (- "0" x)))' # (cosech (- 0 $0))
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
    