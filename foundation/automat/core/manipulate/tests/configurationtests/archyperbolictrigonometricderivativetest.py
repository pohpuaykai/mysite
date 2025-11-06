import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.archyperbolictrigonometricderivative import Archyperbolictrigonometricderivative
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (D (arcsinh x) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (D (arcsinh $0) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (sech (arcsinh x)) (D x x)))' # (* (sech (arcsinh $0)) (D $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (* (sech (arcsinh x)) (D x x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (sech (arcsinh $0)) (D $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D (arcsinh x) x))' # (D (arcsinh $0) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (D (arccosh x) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (D (arccosh $0) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (cosech (arccosh x)) (D x x)))' # (* (cosech (arccosh $0)) (D $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (* (cosech (arccosh x)) (D x x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (cosech (arccosh $0)) (D $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D (arccosh x) x))' # (D (arccosh $0) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (D (arctanh x) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (D (arctanh $0) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (/ (+ "1" (cosh (* "2" (arctanh x)))) "2") (D x x)))' # (* (/ (+ 1 (cosh (* 2 (arctanh $0)))) 2) (D $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (* (/ (+ "1" (cosh (* "2" (arctanh x)))) "2") (D x x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (/ (+ 1 (cosh (* 2 (arctanh $0)))) 2) (D $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D (arctanh x) x))' # (D (arctanh $0) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (D (arcsech x) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (D (arcsech $0) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (* (- "0" (cosh (arcsech x))) (coth (arcsech x))) (D x x)))' # (* (* (- 0 (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (* (* (- "0" (cosh (arcsech x))) (coth (arcsech x))) (D x x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (* (- 0 (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D (arcsech x) x))' # (D (arcsech $0) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (D (arccosech x) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (D (arccosech $0) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (* (- "0" (sinh (arccosech x)))) (D x x)))' # (* (* (- 0 (sinh (arccosech $0)))) (D $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (* (* (- "0" (sinh (arccosech x)))) (D x x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (* (- 0 (sinh (arccosech $0)))) (D $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D (arccosech x) x))' # (D (arccosech $0) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (D (arccoth x) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (D (arccoth $0) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (/ (- "1" (sinh (arccoth x))) "2") (D x x)))' # (* (/ (- 1 (sinh (arccoth $0))) 2) (D $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (* (/ (- "1" (sinh (arccoth x))) "2") (D x x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricderivative'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricderivative(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (/ (- 1 (sinh (arccoth $0))) 2) (D $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D (arccoth x) x))' # (D (arccoth $0) $1)
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
    