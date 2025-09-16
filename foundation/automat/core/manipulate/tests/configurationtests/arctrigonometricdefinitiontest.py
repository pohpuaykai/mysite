import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.arctrigonometricdefinition import Arctrigonometricdefinition
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= y (arcsin (sin x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arcsin (sin $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y x)' # $0
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= y x)' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (arcsin (sin y)) (arcsin (sin x)))' # (arcsin (sin $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= y (arccos (cos x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccos (cos $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y x)' # $0
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= y x)' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (arccos (cos y)) (arccos (cos x)))' # (arccos (cos $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= y (arctan (tan x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arctan (tan $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y x)' # $0
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= y x)' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (arctan (tan y)) (arctan (tan x)))' # (arctan (tan $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor3__configTest(verbose=False):
    eqs = '(= y (arcsec (sec x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'vor'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arcsec (sec $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y x)' # $0
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin3__configTest(verbose=False):
    eqs = '(= y x)' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'hin'
    idx = 3
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (arcsec (sec y)) (arcsec (sec x)))' # (arcsec (sec $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor4__configTest(verbose=False):
    eqs = '(= y (arccosec (cosec x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'vor'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccosec (cosec $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y x)' # $0
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin4__configTest(verbose=False):
    eqs = '(= y x)' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'hin'
    idx = 4
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (arccosec (cosec y)) (arccosec (cosec x)))' # (arccosec (cosec $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor5__configTest(verbose=False):
    eqs = '(= y (arccot (cot x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'vor'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccot (cot $0))
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y x)' # $0
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin5__configTest(verbose=False):
    eqs = '(= y x)' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'hin'
    idx = 5
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # $0
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= (arccot (cot y)) (arccot (cot x)))' # (arccot (cot $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor6__configTest(verbose=False):
    eqs = '(= y (arcsech x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'vor'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arcsech $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arccosh (/ "1" x)))' # (arccosh (/ 1 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin6__configTest(verbose=False):
    eqs = '(= y (arccosh (/ "1" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'hin'
    idx = 6
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccosh (/ 1 $0))
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

    

def test__vor7__configTest(verbose=False):
    eqs = '(= y (arccosech x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'vor'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccosech $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arcsinh (/ "1" x)))' # (arcsinh (/ 1 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin7__configTest(verbose=False):
    eqs = '(= y (arcsinh (/ "1" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'hin'
    idx = 7
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arcsinh (/ 1 $0))
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

    

def test__vor8__configTest(verbose=False):
    eqs = '(= y (arccoth x))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'vor'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arccoth $0)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=manipulatedSchemeEquation)._parse()
    manipulatedAst = ast
    expected = '(= y (arctanh (/ "1" x)))' # (arctanh (/ 1 $0))
    ast0, functionsD0, variablesD0, primitives0, totalNodeCount0, startPos__nodeId0 = Schemeparser(equationStr=expected)._parse()
    expectedAst = ast0
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin8__configTest(verbose=False):
    eqs = '(= y (arctanh (/ "1" x)))' # fill it in
    eqsType = 'scheme'
    #filename = 'arctrigonometricdefinition'
    direction = 'hin'
    idx = 8
    eq0 = Equation(eqs, eqsType)
    ma0 = Arctrigonometricdefinition(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (arctanh (/ 1 $0))
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
    test__vor7__configTest(True) # Not tested yet
    test__hin7__configTest(True) # Not tested yet
    test__vor8__configTest(True) # Not tested yet
    test__hin8__configTest(True) # Not tested yet
    