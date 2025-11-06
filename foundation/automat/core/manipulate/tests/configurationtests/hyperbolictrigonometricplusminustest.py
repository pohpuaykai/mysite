import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.hyperbolictrigonometricplusminus import Hyperbolictrigonometricplusminus
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (sinh (+ x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sinh (+ $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (* (sinh x) (cosh z)) (* (cosh x) (sinh z))))' # (+ (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y (+ (* (sinh x) (cosh z)) (* (cosh x) (sinh z))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sinh (+ x z)))' # (sinh (+ $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (cosh (+ x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cosh (+ $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (+ (* (cosh x) (cosh z)) (* (sinh x) (sinh z))))' # (+ (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (+ (* (cosh x) (cosh z)) (* (sinh x) (sinh z))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (+ (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosh (+ x z)))' # (cosh (+ $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (tanh (+ x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (tanh (+ $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (+ (tanh x) (tanh z)) (+ "1" (* (tanh x) (tanh z)))))' # (/ (+ (tanh $0) (tanh $1)) (+ 1 (* (tanh $0) (tanh $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y (/ (+ (tanh x) (tanh z)) (+ "1" (* (tanh x) (tanh z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (+ (tanh $0) (tanh $1)) (+ 1 (* (tanh $0) (tanh $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tanh (+ x z)))' # (tanh (+ $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (sinh (- x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (sinh (- $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (* (sinh x) (cosh z)) (* (cosh x) (sinh z))))' # (- (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y (- (* (sinh x) (cosh z)) (* (cosh x) (sinh z))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (sinh (- x z)))' # (sinh (- $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (cosh (- x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (cosh (- $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (- (* (cosh x) (cosh z)) (* (sinh x) (sinh z))))' # (- (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y (- (* (cosh x) (cosh z)) (* (sinh x) (sinh z))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (- (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (cosh (- x z)))' # (cosh (- $0 $1))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (tanh (- x z)))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (tanh (- $0 $1))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (/ (- (tanh x) (tanh z)) (- "1" (* (tanh x) (tanh z)))))' # (/ (- (tanh $0) (tanh $1)) (- 1 (* (tanh $0) (tanh $1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y (/ (- (tanh x) (tanh z)) (- "1" (* (tanh x) (tanh z)))))' # fill it in
    eqsType = 'scheme'
    #filename = 'hyperbolictrigonometricplusminus'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Hyperbolictrigonometricplusminus(direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply(eq0) # (/ (- (tanh $0) (tanh $1)) (- 1 (* (tanh $0) (tanh $1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (tanh (- x z)))' # (tanh (- $0 $1))
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
    