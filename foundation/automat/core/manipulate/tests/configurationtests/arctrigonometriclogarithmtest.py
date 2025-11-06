import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.arctrigonometriclogarithm import Arctrigonometriclogarithm
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (arcsin x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arcsin $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (* "i" (log "e" (+ (* "i" x) (nroot "2" (- "1" (^ x "2"))))))))' # (- 0 (* i (log e (+ (* i $0) (nroot 2 (- 1 (^ $0 2)))))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (- "0" (* "i" (log "e" (+ (* "i" x) (nroot "2" (- "1" (^ x "2"))))))))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (* i (log e (+ (* i $0) (nroot 2 (- 1 (^ $0 2)))))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arcsin x))' # (arcsin $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (arccos x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arccos $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (* "i" (log "e" (+ x (nroot "2" (- (^ x "2") "1")))))))' # (- 0 (* i (log e (+ $0 (nroot 2 (- (^ $0 2) 1))))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (- "0" (* "i" (log "e" (+ x (nroot "2" (- (^ x "2") "1")))))))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (* i (log e (+ $0 (nroot 2 (- (^ $0 2) 1))))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccos x))' # (arccos $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (arctan x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arctan $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (/ "i" "2") (log "e" (/ (+ "i" x) (- "i" x)))))' # (* (/ i 2) (log e (/ (+ i $0) (- i $0))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (* (/ "i" "2") (log "e" (/ (+ "i" x) (- "i" x)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (/ i 2) (log e (/ (+ i $0) (- i $0))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arctan x))' # (arctan $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (arccosec x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arccosec $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (* "i" (log "e" (+ (/ "i" x) (nroot "2" (- "1" (/ "1" (^ x "2")))))))))' # (- 0 (* i (log e (+ (/ i $0) (nroot 2 (- 1 (/ 1 (^ $0 2))))))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (- "0" (* "i" (log "e" (+ (/ "i" x) (nroot "2" (- "1" (/ "1" (^ x "2")))))))))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (* i (log e (+ (/ i $0) (nroot 2 (- 1 (/ 1 (^ $0 2))))))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccosec x))' # (arccosec $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (arcsec x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arcsec $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- "0" (* "i" (log "e" (+ (/ "1" x) (* "i" (nroot "2" (- "1" (/ "1" (^ x "2"))))))))))' # (- 0 (* i (log e (+ (/ 1 $0) (* i (nroot 2 (- 1 (/ 1 (^ $0 2)))))))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (- "0" (* "i" (log "e" (+ (/ "1" x) (* "i" (nroot "2" (- "1" (/ "1" (^ x "2"))))))))))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- 0 (* i (log e (+ (/ 1 $0) (* i (nroot 2 (- 1 (/ 1 (^ $0 2)))))))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arcsec x))' # (arcsec $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (arccot x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (arccot $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (/ "i" "2") (log "e" (/ (- x "i") (+ x "i")))))' # (* (/ i 2) (log e (/ (- $0 i) (+ $0 i))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (* (/ "i" "2") (log "e" (/ (- x "i") (+ x "i")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometriclogarithm'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometriclogarithm(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (* (/ i 2) (log e (/ (- $0 i) (+ $0 i))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccot x))' # (arccot $0)
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
    