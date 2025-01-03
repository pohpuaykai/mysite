import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.pattern.communtativity import Communtativity
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


    

def test__vor0__configTest(verbose=False):
    eqs = '(= a (+ b c))' # fill it in
    eqsType = 'scheme'
    #filename = 'communtativity'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Communtativity(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ $0 $1)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (+ c b))' # (+ $1 $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin0__configTest(verbose=False):
    eqs = '(= a (+ b c))' # fill it in
    eqsType = 'scheme'
    #filename = 'communtativity'
    direction = 'hin'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    ma0 = Communtativity(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (+ $1 $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (+ c b))' # (+ $0 $1)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor1__configTest(verbose=False):
    eqs = '(= a (* b c))' # fill it in
    eqsType = 'scheme'
    #filename = 'communtativity'
    direction = 'vor'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Communtativity(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* $0 $1)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (* c b))' # (* $1 $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin1__configTest(verbose=False):
    eqs = '(= a (* b c))' # fill it in
    eqsType = 'scheme'
    #filename = 'communtativity'
    direction = 'hin'
    idx = 1
    eq0 = Equation(eqs, eqsType)
    ma0 = Communtativity(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (* $1 $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= a (* c b))' # (* $0 $1)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__vor2__configTest(verbose=False):
    eqs = '(= a b)' # fill it in
    eqsType = 'scheme'
    #filename = 'communtativity'
    direction = 'vor'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Communtativity(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (= $0 $1)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= b a)' # (= $1 $0)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    

def test__hin2__configTest(verbose=False):
    eqs = '(= a b)' # fill it in
    eqsType = 'scheme'
    #filename = 'communtativity'
    direction = 'hin'
    idx = 2
    eq0 = Equation(eqs, eqsType)
    ma0 = Communtativity(eq0, direction, idx, verbose=verbose)
    manipulatedSchemeEquation = ma0.apply() # (= $1 $0)
    manipulatedAst = Schemeparser(equationStr=manipulatedSchemeEquation).ast
    expected = '(= b a)' # (= $0 $1)
    expectedAst = Schemeparser(equationStr=expected).ast
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected == manipulatedSchemeEquation and manipulatedAst == expectedAst
    )
    if verbose:
        print(manipulatedSchemeEquation)
        print(manipulatedAst)

    


if __name__=='__main__':
    test__vor0__configTest()
    test__hin0__configTest()
    test__vor1__configTest()
    test__hin1__configTest()
    test__vor2__configTest()
    test__hin2__configTest()
    