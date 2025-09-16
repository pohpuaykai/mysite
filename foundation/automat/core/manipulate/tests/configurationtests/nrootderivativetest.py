import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.nrootderivative import Nrootderivative
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (D (nroot f g) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'nrootderivative'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Nrootderivative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (D (nroot $0 $1) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (nroot f g) (/ (- (/ (* (D g x) f) g) (* (D f x) (log "e" g))) (^ f 2))))' # (* (nroot $0 $1) (/ (- (/ (* (D $1 $2) $0) $1) (* (D $0 $2) (log e $1))) (^ $0 2)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (* (nroot f g) (/ (- (/ (* (D g x) f) g) (* (D f x) (log "e" g))) (^ f 2))))' # fill it in
    eqsType = 'scheme'
    #filename = 'nrootderivative'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Nrootderivative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (nroot $0 $1) (/ (- (/ (* (D $1 $2) $0) $1) (* (D $0 $2) (log e $1))) (^ $0 2)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D (nroot f g) x))' # (D (nroot $0 $1) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (D (nroot a f) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'nrootderivative'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Nrootderivative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (D (nroot $0 $1) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* (* (D f x) (/ "1" a)) (^ f (- (/ "1" a) "1"))))' # (* (* (D $1 $2) (/ 1 $0)) (^ $1 (- (/ 1 $0) 1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (* (* (D f x) (/ "1" a)) (^ f (- (/ "1" a) "1"))))' # fill it in
    eqsType = 'scheme'
    #filename = 'nrootderivative'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Nrootderivative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (* (D $1 $2) (/ 1 $0)) (^ $1 (- (/ 1 $0) 1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D (nroot a f) x))' # (D (nroot $0 $1) $2)
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
    