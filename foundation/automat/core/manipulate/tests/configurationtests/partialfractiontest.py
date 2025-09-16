import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.partialfraction import Partialfraction
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (/ (+ (* p x) q) (* (- x a) (- x b))))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ (* $1 $0) $2) (* (- $0 $3) (- $0 $4)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (/ (- p (/ (* (- q (* p b)) b) (- a b))) (- x a)) (/ (/ (* (- q (* b p)) b) (- a b)) (- x b))))' # (+ (/ (- $1 (/ (* (- $2 (* $1 $4)) $4) (- $3 $4))) (- $0 $3)) (/ (/ (* (- $2 (* $4 $1)) $4) (- $3 $4)) (- $0 $4)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (+ (/ (- p (/ (* (- q (* p b)) b) (- a b))) (- x a)) (/ (/ (* (- q (* b p)) b) (- a b)) (- x b))))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (/ (- $1 (/ (* (- $2 (* $1 $4)) $4) (- $3 $4))) (- $0 $3)) (/ (/ (* (- $2 (* $4 $1)) $4) (- $3 $4)) (- $0 $4)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (* p x) q) (* (- x a) (- x b))))' # (/ (+ (* $1 $0) $2) (* (- $0 $3) (- $0 $4)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (/ (+ (* p x) q) (^ (- x a) "2")))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ (* $1 $0) $2) (^ (- $0 $3) 2))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (/ p (- x a)) (/ (+ (* a p) q) (^ (- x a) "2"))))' # (+ (/ $1 (- $0 $3)) (/ (+ (* $3 $1) $2) (^ (- $0 $3) 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (+ (/ p (- x a)) (/ (+ (* a p) q) (^ (- x a) "2"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (/ $1 (- $0 $3)) (/ (+ (* $3 $1) $2) (^ (- $0 $3) 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (* p x) q) (^ (- x a) "2")))' # (/ (+ (* $1 $0) $2) (^ (- $0 $3) 2))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (/ (+ (+ (* p (^ x "2")) (* q x)) r) (* (* (- x a) (- x b)) (- x c))))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ (+ (* $1 (^ $0 2)) (* $2 $0)) $3) (* (* (- $0 $4) (- $0 $5)) (- $0 $6)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (+ (/ (/ (+ (- (* (^ a "2") p) (* a q)) r) (* (- a b) (- a c))) (- x a)) (/ (/ (- (- (* b q) r) (* (^ b "2") p)) (* (- a b) (- b c))) (- x b))) (/ (/ (+ (- r (* c q)) (* (^ c "2") p)) (* (- a c) (- b c))) (- x c))))' # (+ (+ (/ (/ (+ (- (* (^ $4 2) $1) (* $4 $2)) $3) (* (- $4 $5) (- $4 $6))) (- $0 $4)) (/ (/ (- (- (* $5 $2) $3) (* (^ $5 2) $1)) (* (- $4 $5) (- $5 $6))) (- $0 $5))) (/ (/ (+ (- $3 (* $6 $2)) (* (^ $6 2) $1)) (* (- $4 $6) (- $5 $6))) (- $0 $6)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (+ (+ (/ (/ (+ (- (* (^ a "2") p) (* a q)) r) (* (- a b) (- a c))) (- x a)) (/ (/ (- (- (* b q) r) (* (^ b "2") p)) (* (- a b) (- b c))) (- x b))) (/ (/ (+ (- r (* c q)) (* (^ c "2") p)) (* (- a c) (- b c))) (- x c))))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (+ (/ (/ (+ (- (* (^ $4 2) $1) (* $4 $2)) $3) (* (- $4 $5) (- $4 $6))) (- $0 $4)) (/ (/ (- (- (* $5 $2) $3) (* (^ $5 2) $1)) (* (- $4 $5) (- $5 $6))) (- $0 $5))) (/ (/ (+ (- $3 (* $6 $2)) (* (^ $6 2) $1)) (* (- $4 $6) (- $5 $6))) (- $0 $6)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (+ (* p (^ x "2")) (* q x)) r) (* (* (- x a) (- x b)) (- x c))))' # (/ (+ (+ (* $1 (^ $0 2)) (* $2 $0)) $3) (* (* (- $0 $4) (- $0 $5)) (- $0 $6)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (/ (+ (+ (* p (^ x "2")) (* q x)) r) (* (^ (- x a) "2") (- x b))))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ (+ (* $1 (^ $0 2)) (* $2 $0)) $3) (* (^ (- $0 $4) 2) (- $0 $5)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (+ (/ (/ (- (- (- (* (^ a "2") p) (* (* (* "2" a) b) p)) (* q b)) r) (^ (- b a) "2")) (- x a)) (/ (/ (+ (+ (^ a "2") a) r) (- a b)) (^ (- x a) "2"))) (/ (/ (+ (+ (* (^ b "2") p) (* b q)) r) (^ (- b a) "2")) (- x b))))' # (+ (+ (/ (/ (- (- (- (* (^ $4 2) $1) (* (* (* 2 $4) $5) $1)) (* $2 $5)) $3) (^ (- $5 $4) 2)) (- $0 $4)) (/ (/ (+ (+ (^ $4 2) $4) $3) (- $4 $5)) (^ (- $0 $4) 2))) (/ (/ (+ (+ (* (^ $5 2) $1) (* $5 $2)) $3) (^ (- $5 $4) 2)) (- $0 $5)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (+ (+ (/ (/ (- (- (- (* (^ a "2") p) (* (* (* "2" a) b) p)) (* q b)) r) (^ (- b a) "2")) (- x a)) (/ (/ (+ (+ (^ a "2") a) r) (- a b)) (^ (- x a) "2"))) (/ (/ (+ (+ (* (^ b "2") p) (* b q)) r) (^ (- b a) "2")) (- x b))))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (+ (/ (/ (- (- (- (* (^ $4 2) $1) (* (* (* 2 $4) $5) $1)) (* $2 $5)) $3) (^ (- $5 $4) 2)) (- $0 $4)) (/ (/ (+ (+ (^ $4 2) $4) $3) (- $4 $5)) (^ (- $0 $4) 2))) (/ (/ (+ (+ (* (^ $5 2) $1) (* $5 $2)) $3) (^ (- $5 $4) 2)) (- $0 $5)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (+ (* p (^ x "2")) (* q x)) r) (* (^ (- x a) "2") (- x b))))' # (/ (+ (+ (* $1 (^ $0 2)) (* $2 $0)) $3) (* (^ (- $0 $4) 2) (- $0 $5)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (/ (+ (+ (* p (^ x "2")) (* q x)) r) (* (- x a) (+ (+ (^ x "2") (* b x)) c))))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (+ (+ (* $1 (^ $0 2)) (* $2 $0)) $3) (* (- $0 $4) (+ (+ (^ $0 2) (* $5 $0)) $6)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (/ (/ (+ (+ (* (^ a "2") p) (* a q)) r) (+ (+ (^ a "2") (* a b)) c)) (- x a)) (/ (+ (* (/ (+ (- (* (* a b) p) (* a q)) (- (* p c) r)) (+ (+ (^ a "2") (* a b)) c)) x) (/ (+ (+ (* (* a p) c) (* a r)) (- (* b r) (* c q))) (+ (+ (^ a "2") (* a b)) c))) (+ (+ (^ x "2") (* b x)) c))))' # (+ (/ (/ (+ (+ (* (^ $4 2) $1) (* $4 $2)) $3) (+ (+ (^ $4 2) (* $4 $5)) $6)) (- $0 $4)) (/ (+ (* (/ (+ (- (* (* $4 $5) $1) (* $4 $2)) (- (* $1 $6) $3)) (+ (+ (^ $4 2) (* $4 $5)) $6)) $0) (/ (+ (+ (* (* $4 $1) $6) (* $4 $3)) (- (* $5 $3) (* $6 $2))) (+ (+ (^ $4 2) (* $4 $5)) $6))) (+ (+ (^ $0 2) (* $5 $0)) $6)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (+ (/ (/ (+ (+ (* (^ a "2") p) (* a q)) r) (+ (+ (^ a "2") (* a b)) c)) (- x a)) (/ (+ (* (/ (+ (- (* (* a b) p) (* a q)) (- (* p c) r)) (+ (+ (^ a "2") (* a b)) c)) x) (/ (+ (+ (* (* a p) c) (* a r)) (- (* b r) (* c q))) (+ (+ (^ a "2") (* a b)) c))) (+ (+ (^ x "2") (* b x)) c))))' # fill it in
    eqsType = 'scheme'
    #filename = 'partialfraction'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Partialfraction(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ (/ (/ (+ (+ (* (^ $4 2) $1) (* $4 $2)) $3) (+ (+ (^ $4 2) (* $4 $5)) $6)) (- $0 $4)) (/ (+ (* (/ (+ (- (* (* $4 $5) $1) (* $4 $2)) (- (* $1 $6) $3)) (+ (+ (^ $4 2) (* $4 $5)) $6)) $0) (/ (+ (+ (* (* $4 $1) $6) (* $4 $3)) (- (* $5 $3) (* $6 $2))) (+ (+ (^ $4 2) (* $4 $5)) $6))) (+ (+ (^ $0 2) (* $5 $0)) $6)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (+ (* p (^ x "2")) (* q x)) r) (* (- x a) (+ (+ (^ x "2") (* b x)) c))))' # (/ (+ (+ (* $1 (^ $0 2)) (* $2 $0)) $3) (* (- $0 $4) (+ (+ (^ $0 2) (* $5 $0)) $6)))
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
    