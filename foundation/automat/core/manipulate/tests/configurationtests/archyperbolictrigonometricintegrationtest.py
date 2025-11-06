import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.archyperbolictrigonometricintegration import Archyperbolictrigonometricintegration
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (int (* (sech (arcsinh x)) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (sech (arcsinh $0)) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arcsinh x) v_{0}))' # (+ (arcsinh $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (+ (arcsinh x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arcsinh $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (sech (arcsinh x)) (D x v_{0})) v_{0}))' # (int (* (sech (arcsinh $0)) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (int (* (cosech (arccosh x)) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (cosech (arccosh $0)) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arccosh x) v_{0}))' # (+ (arccosh $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (+ (arccosh x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arccosh $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (cosech (arccosh x)) (D x v_{0})) v_{0}))' # (int (* (cosech (arccosh $0)) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (int (* (/ (+ "1" (cosh (* "2" (arctanh x)))) "2") (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (/ (+ 1 (cosh (* 2 (arctanh $0)))) 2) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arctanh x) v_{0}))' # (+ (arctanh $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (+ (arctanh x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arctanh $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (/ (+ "1" (cosh (* "2" (arctanh x)))) "2") (D x v_{0})) v_{0}))' # (int (* (/ (+ 1 (cosh (* 2 (arctanh $0)))) 2) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (int (* (* (- "0" (cosh (arcsech x))) (coth (arcsech x))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (* (- 0 (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arcsech x) v_{0}))' # (+ (arcsech $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (+ (arcsech x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arcsech $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (* (- "0" (cosh (arcsech x))) (coth (arcsech x))) (D x v_{0})) v_{0}))' # (int (* (* (- 0 (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (int (* (* (- "0" (sinh (arccosech x)))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (* (- 0 (sinh (arccosech $0)))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arccosech x) v_{0}))' # (+ (arccosech $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (+ (arccosech x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arccosech $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (* (- "0" (sinh (arccosech x)))) (D x v_{0})) v_{0}))' # (int (* (* (- 0 (sinh (arccosech $0)))) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (int (* (/ (- "1" (sinh (arccoth x))) "2") (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (/ (- 1 (sinh (arccoth $0))) 2) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arccoth x) v_{0}))' # (+ (arccoth $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (+ (arccoth x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arccoth $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (/ (- "1" (sinh (arccoth x))) "2") (D x v_{0})) v_{0}))' # (int (* (/ (- 1 (sinh (arccoth $0))) 2) (D $0 $1)) $1)
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
    