import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.hyperbolictrigonometricsumtoproduct import Hyperbolictrigonometricsumtoproduct
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (+ (sinh x) (sinh z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricsumtoproduct'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricsumtoproduct(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (sinh $0) (sinh $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (* "2" (sinh (/ (+ x z) "2"))) (cosh (/ (- x z) "2"))))' # (* (* 2 (sinh (/ (+ $0 $1) 2))) (cosh (/ (- $0 $1) 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (* (* "2" (sinh (/ (+ x z) "2"))) (cosh (/ (- x z) "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricsumtoproduct'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricsumtoproduct(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (* 2 (sinh (/ (+ $0 $1) 2))) (cosh (/ (- $0 $1) 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (sinh x) (sinh z)))' # (+ (sinh $0) (sinh $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (+ (cosh x) (cosh z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricsumtoproduct'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricsumtoproduct(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (cosh $0) (cosh $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (* "2" (cosh (/ (+ x z) "2"))) (cosh (/ (- x z) "2"))))' # (* (* 2 (cosh (/ (+ $0 $1) 2))) (cosh (/ (- $0 $1) 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (* (* "2" (cosh (/ (+ x z) "2"))) (cosh (/ (- x z) "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricsumtoproduct'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricsumtoproduct(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (* 2 (cosh (/ (+ $0 $1) 2))) (cosh (/ (- $0 $1) 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (cosh x) (cosh z)))' # (+ (cosh $0) (cosh $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (- (sinh x) (sinh z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricsumtoproduct'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricsumtoproduct(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (sinh $0) (sinh $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (* "2" (cosh (/ (+ x z) "2"))) (sinh (/ (- x z) "2"))))' # (* (* 2 (cosh (/ (+ $0 $1) 2))) (sinh (/ (- $0 $1) 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (* (* "2" (cosh (/ (+ x z) "2"))) (sinh (/ (- x z) "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricsumtoproduct'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricsumtoproduct(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (* 2 (cosh (/ (+ $0 $1) 2))) (sinh (/ (- $0 $1) 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (sinh x) (sinh z)))' # (- (sinh $0) (sinh $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (- (cosh x) (cosh z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricsumtoproduct'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricsumtoproduct(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (- (cosh $0) (cosh $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (* "2" (sinh (/ (+ x z) "2"))) (sinh (/ (- x z) "2"))))' # (* (* 2 (sinh (/ (+ $0 $1) 2))) (sinh (/ (- $0 $1) 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (* (* "2" (sinh (/ (+ x z) "2"))) (sinh (/ (- x z) "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricsumtoproduct'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricsumtoproduct(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (* 2 (sinh (/ (+ $0 $1) 2))) (sinh (/ (- $0 $1) 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (cosh x) (cosh z)))' # (- (cosh $0) (cosh $1))
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
    