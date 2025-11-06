import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.hyperbolictrigonometricintegration import Hyperbolictrigonometricintegration
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (int (* (cosh x) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (cosh $0) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (sinh x) v_{0}))' # (+ (sinh $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (+ (sinh x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (sinh $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (cosh x) (D x v_{0})) v_{0}))' # (int (* (cosh $0) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (int (* (sinh x) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (sinh $0) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (cosh x) v_{0}))' # (+ (cosh $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (+ (cosh x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (cosh $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (sinh x) (D x v_{0})) v_{0}))' # (int (* (sinh $0) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (int (* (/ "2" (+ (cosh (* "2" x) "1"))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (/ 2 (+ (cosh (* 2 $0) 1))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (tanh x) v_{0}))' # (+ (tanh $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (+ (tanh x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (tanh $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (/ "2" (+ (cosh (* "2" x) "1"))) (D x v_{0})) v_{0}))' # (int (* (/ 2 (+ (cosh (* 2 $0) 1))) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (int (* (- "0" (* (tanh x) (sech x))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (- 0 (* (tanh $0) (sech $0))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (sech x) v_{0}))' # (+ (sech $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (+ (sech x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (sech $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (- "0" (* (tanh x) (sech x))) (D x v_{0})) v_{0}))' # (int (* (- 0 (* (tanh $0) (sech $0))) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (int (* (- "0" (* (coth x) (cosech x))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (- 0 (* (coth $0) (cosech $0))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (cosech x) v_{0}))' # (+ (cosech $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (+ (cosech x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (cosech $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (- "0" (* (coth x) (cosech x))) (D x v_{0})) v_{0}))' # (int (* (- 0 (* (coth $0) (cosech $0))) (D $0 $1)) $1)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (int (* (/ "2" (- "1" (sinh (* "2" x)))) (D x x)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (int (* (/ 2 (- 1 (sinh (* 2 $0)))) (D $0 $1)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (coth x) v_{0}))' # (+ (coth $0) $2)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (+ (coth x) v_{0}))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricintegration'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricintegration(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (coth $0) $2)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (int (* (/ "2" (- "1" (sinh (* "2" x)))) (D x v_{0})) v_{0}))' # (int (* (/ 2 (- 1 (sinh (* 2 $0)))) (D $0 $1)) $1)
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
    