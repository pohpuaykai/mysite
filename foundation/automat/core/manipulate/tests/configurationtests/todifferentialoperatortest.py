import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.todifferentialoperator import ToDifferentialOperator
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'todifferentialoperator'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = ToDifferentialOperator(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (/ d (* d $1)) $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (D (* u v) x) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))' # (D $0 $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= (D (* u v) x) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'todifferentialoperator'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = ToDifferentialOperator(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (D $0 $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))' # (* (/ d (* d $1)) $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'todifferentialoperator'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = ToDifferentialOperator(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* d $0) (* d $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (* (/ d (* d x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))' # (D $0 $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= (* (/ d (* d x)) (* u v)) (+ (* u (D v x)) (* v (D u x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'todifferentialoperator'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = ToDifferentialOperator(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (D $0 $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))' # (/ (* d $0) (* d $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'todifferentialoperator'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = ToDifferentialOperator(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* (/ partial (* partial $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (D (* u v) x) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x))))' # (D $0 $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= (D (* u v) x) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'todifferentialoperator'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = ToDifferentialOperator(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (D $0 $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))' # (* (/ partial (* partial $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'todifferentialoperator'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = ToDifferentialOperator(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (/ (* partial $0) (* partial $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (* (/ partial (* partial x)) (* u v))(+ (* u (D v x)) (* v (D u x))))' # (D $0 $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= (* (/ partial (* partial x)) (* u v))(+ (* u (D v x)) (* v (D u x))))' # fill it in
    eqsType = 'scheme'
    #filename = 'todifferentialoperator'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = ToDifferentialOperator(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (D $0 $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (* (/ partial (* partial x)) (* u v)) (+ (* u (/ (* partial v) (* partial x))) (* v (/ (* partial u) (* partial x)))))' # (/ (* partial $0) (* partial $1))
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
    