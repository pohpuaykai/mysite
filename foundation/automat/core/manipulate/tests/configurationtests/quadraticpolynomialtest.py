import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.quadraticpolynomial import Quadraticpolynomial
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= (+ (+ (* a (^ x 2)) (* b x)) c) "0")' # fill it in
    eqsType = 'scheme'
    #filename = 'quadraticpolynomial'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Quadraticpolynomial(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= x (/ (+ (- "0" b) (nroot "2" (- (^ b "2") (* (* "4" a) c)))) (* "2" a)))' # (= $3 (/ (+ (- 0 $1) (nroot 2 (- (^ $1 2) (* (* 4 $0) $2)))) (* 2 $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= x (/ (+ (- "0" b) (nroot "2" (- (^ b "2") (* (* "4" a) c)))) (* "2" a)))' # fill it in
    eqsType = 'scheme'
    #filename = 'quadraticpolynomial'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Quadraticpolynomial(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (= $3 (/ (+ (- 0 $1) (nroot 2 (- (^ $1 2) (* (* 4 $0) $2)))) (* 2 $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (+ (+ (* a (^ x 2)) (* b x)) c) "0")' # (= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= (+ (+ (* a (^ x 2)) (* b x)) c) "0")' # fill it in
    eqsType = 'scheme'
    #filename = 'quadraticpolynomial'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Quadraticpolynomial(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= x (/ (- (- "0" b) (nroot "2" (- (^ b "2") (* (* "4" a) c)))) (* "2" a)))' # (= $3 (/ (- (- 0 $1) (nroot 2 (- (^ $1 2) (* (* 4 $0) $2)))) (* 2 $0)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= x (/ (- (- "0" b) (nroot "2" (- (^ b "2") (* (* "4" a) c)))) (* "2" a)))' # fill it in
    eqsType = 'scheme'
    #filename = 'quadraticpolynomial'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Quadraticpolynomial(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (= $3 (/ (- (- 0 $1) (nroot 2 (- (^ $1 2) (* (* 4 $0) $2)))) (* 2 $0)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (+ (+ (* a (^ x 2)) (* b x)) c) "0")' # (= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= (+ (+ (* a (^ x 2)) (* b x)) c) "0")' # fill it in
    eqsType = 'scheme'
    #filename = 'quadraticpolynomial'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Quadraticpolynomial(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (+ (* a (^ (+ x (/ b (* "2" a))) "2")) (- c (/ (^ b "2") (* "4" a)))) "0")' # (= (+ (* $0 (^ (+ $3 (/ $1 (* 2 $0))) 2)) (- $2 (/ (^ $1 2) (* 4 $0)))) 0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= (+ (* a (^ (+ x (/ b (* "2" a))) "2")) (- c (/ (^ b "2") (* "4" a)))) "0")' # fill it in
    eqsType = 'scheme'
    #filename = 'quadraticpolynomial'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Quadraticpolynomial(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (= (+ (* $0 (^ (+ $3 (/ $1 (* 2 $0))) 2)) (- $2 (/ (^ $1 2) (* 4 $0)))) 0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (+ (+ (* a (^ x 2)) (* b x)) c) "0")' # (= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)
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
    