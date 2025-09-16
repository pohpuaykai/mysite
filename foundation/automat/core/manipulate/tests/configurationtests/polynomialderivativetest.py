import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.polynomialderivative import Polynomialderivative
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (D x x))' # fill it in
    eqsType = 'scheme'
    #filename = 'polynomialderivative'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Polynomialderivative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (D $0 $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y "1")' # 1
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y "1")' # fill it in
    eqsType = 'scheme'
    #filename = 'polynomialderivative'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Polynomialderivative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # 1
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D v_{0} v_{0}))' # (D $0 $0)
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (D (* a (^ x n)) x))' # fill it in
    eqsType = 'scheme'
    #filename = 'polynomialderivative'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Polynomialderivative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (D (* $0 (^ $1 $2)) $1)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (* a (* n (^ x (- n "1")))))' # (* $0 (* $2 (^ $1 (- $2 1))))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y (* a (* n (^ x (- n "1")))))' # fill it in
    eqsType = 'scheme'
    #filename = 'polynomialderivative'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Polynomialderivative(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* $0 (* $2 (^ $1 (- $2 1))))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (D (* a (^ x n)) x))' # (D (* $0 (^ $1 $2)) $1)
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
    