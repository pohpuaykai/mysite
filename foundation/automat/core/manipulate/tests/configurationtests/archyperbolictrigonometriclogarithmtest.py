import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.archyperbolictrigonometriclogarithm import Archyperbolictrigonometriclogarithm
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (arcsinh x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arcsinh $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (log "e" (+ x (nroot "2" (+ (^ x "2") "1")))))' # (log e (+ $0 (nroot 2 (+ (^ $0 2) 1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (log "e" (+ x (nroot "2" (+ (^ x "2") "1")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (log e (+ $0 (nroot 2 (+ (^ $0 2) 1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arcsinh x))' # (arcsinh $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (arccosh x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arccosh $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (log "e" (+ x (nroot "2" (- (^ x "2") "1")))))' # (log e (+ $0 (nroot 2 (- (^ $0 2) 1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (log "e" (+ x (nroot "2" (- (^ x "2") "1")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (log e (+ $0 (nroot 2 (- (^ $0 2) 1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccosh x))' # (arccosh $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (arctanh x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arctanh $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (log "e" (/ (+ "1" x) (- "1" x))) "2"))' # (/ (log e (/ (+ 1 $0) (- 1 $0))) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (/ (log "e" (/ (+ "1" x) (- "1" x))) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (log e (/ (+ 1 $0) (- 1 $0))) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arctanh x))' # (arctanh $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (arccoth x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arccoth $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (log "e" (/ (+ x "1") (- x "1"))) "2"))' # (/ (log e (/ (+ $0 1) (- $0 1))) 2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (/ (log "e" (/ (+ x "1") (- x "1"))) "2"))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (log e (/ (+ $0 1) (- $0 1))) 2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccoth x))' # (arccoth $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (arcsech x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arcsech $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (log "e" (+ (/ "1" x) (nroot "2" (- (/ "1" (^ x "2")) "1")))))' # (log e (+ (/ 1 $0) (nroot 2 (- (/ 1 (^ $0 2)) 1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (log "e" (+ (/ "1" x) (nroot "2" (- (/ "1" (^ x "2")) "1")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (log e (+ (/ 1 $0) (nroot 2 (- (/ 1 (^ $0 2)) 1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arcsech x))' # (arcsech $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (arcsech x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arcsech $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (log "e" (/ (+ "1" (nroot "2" (- "1" (^ x "2")))) x)))' # (log e (/ (+ 1 (nroot 2 (- 1 (^ $0 2)))) $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (log "e" (/ (+ "1" (nroot "2" (- "1" (^ x "2")))) x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (log e (/ (+ 1 (nroot 2 (- 1 (^ $0 2)))) $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arcsech x))' # (arcsech $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= y (arccosech x))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'vor'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arccosech $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (log "e" (+ (/ "1" x) (nroot "2" (+ (/ "1" (^ x "2")) "1")))))' # (log e (+ (/ 1 $0) (nroot 2 (+ (/ 1 (^ $0 2)) 1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= y (log "e" (+ (/ "1" x) (nroot "2" (+ (/ "1" (^ x "2")) "1")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'archyperbolictrigonometriclogarithm'
    direction = 'hin'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Archyperbolictrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (log e (+ (/ 1 $0) (nroot 2 (+ (/ 1 (^ $0 2)) 1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccosech x))' # (arccosech $0)
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
    