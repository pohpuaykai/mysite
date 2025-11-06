import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.arctrigonometricintegration import Arctrigonometricintegration
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (int (* (/ "1" (nroot "2" (- "1" (* x x)))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (/ 1 (nroot 2 (- 1 (* $0 $0)))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arcsin x) v_{0}))' # (+ (arcsin $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (+ (arcsin x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arcsin $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (/ "1" (nroot "2" (- "1" (* x x)))) (D x v_{0})) v_{0}))' # (int (* (/ 1 (nroot 2 (- 1 (* $0 $0)))) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (int (* (- "0" (/ "1" (nroot "2" (- "1" (* x x))))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (- 0 (/ 1 (nroot 2 (- 1 (* $0 $0))))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arccos x) v_{0}))' # (+ (arccos $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (+ (arccos x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arccos $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (- "0" (/ "1" (nroot "2" (- "1" (* x x))))) (D x v_{0})) v_{0}))' # (int (* (- 0 (/ 1 (nroot 2 (- 1 (* $0 $0))))) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (int (* (/ "1" (+ "1" (* x x))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (/ 1 (+ 1 (* $0 $0))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arctan x) v_{0}))' # (+ (arctan $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (+ (arctan x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arctan $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (/ "1" (+ "1" (* x x))) (D x v_{0})) v_{0}))' # (int (* (/ 1 (+ 1 (* $0 $0))) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (int (* (/ "1" (* x (nroot "2" (- (* x x) "1")))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (/ 1 (* $0 (nroot 2 (- (* $0 $0) 1)))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arcsec x) v_{0}))' # (+ (arcsec $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (+ (arcsec x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arcsec $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (/ "1" (* x (nroot "2" (- (* x x) "1")))) (D x v_{0})) v_{0}))' # (int (* (/ 1 (* $0 (nroot 2 (- (* $0 $0) 1)))) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (int (* (nroot "2" (- (* x x) "1")) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (nroot 2 (- (* $0 $0) 1)) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arccosec x) v_{0}))' # (+ (arccosec $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (+ (arccosec x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arccosec $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (nroot "2" (- (* x x) "1")) (D x v_{0})) v_{0}))' # (int (* (nroot 2 (- (* $0 $0) 1)) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (int (* (- "0" (/ "1" (+ "1" (* x x)))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (- 0 (/ 1 (+ 1 (* $0 $0)))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (arccot x) v_{0}))' # (+ (arccot $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (+ (arccot x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricintegration'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (arccot $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (- "0" (/ "1" (+ "1" (* x x)))) (D x v_{0})) v_{0}))' # (int (* (- 0 (/ 1 (+ 1 (* $0 $0)))) (D $0 $1)) $1)
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
    