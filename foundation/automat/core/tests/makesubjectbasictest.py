import inspect
import pprint

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


def test__makeSubject2Input__addition0(verbose=False):
    eq0 = Equation('(= a (+ b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=a-c' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__addition1(verbose=False):
    eq0 = Equation('(= a (+ b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'c=a-b' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__subtraction0(verbose=False):
    eq0 = Equation('(= a (- b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=a+c' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__subtraction1(verbose=False):
    eq0 = Equation('(= a (- b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'c=b-a' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__multiply0(verbose=False):
    eq0 = Equation('(= a (* b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\frac{a}{c}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__multiply1(verbose=False):
    eq0 = Equation('(= a (* b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'c=\\frac{a}{b}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__divide0(verbose=False):
    eq0 = Equation('(= a (/ b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=ac' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__divide1(verbose=False):
    eq0 = Equation('(= a (/ b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'c=\\frac{b}{a}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__exponent0(verbose=False):
    eq0 = Equation('(= a (^ b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\sqrt[c]{a}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__exponent1(verbose=False):
    eq0 = Equation('(= a (^ b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'c=\\log_b(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__nroot0(verbose=False):
    eq0 = Equation('(= a (nroot b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\log_a(c)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__nroot1(verbose=False):
    eq0 = Equation('(= a (nroot b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'c=a^b' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__log0(verbose=False):
    eq0 = Equation('(= a (log b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\sqrt[a]{c}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject2Input__log1(verbose=False):
    eq0 = Equation('(= a (log b c))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'c=b^a' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arccosec(verbose=False):
    eq0 = Equation('(= a (arccosec b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\cosec(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arccosech(verbose=False):
    eq0 = Equation('(= a (arccosech b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\cosech(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arccos(verbose=False):
    eq0 = Equation('(= a (arccos b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\cos(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arccosh(verbose=False):
    eq0 = Equation('(= a (arccosh b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\cosh(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arccot(verbose=False):
    eq0 = Equation('(= a (arccot b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\cot(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arccoth(verbose=False):
    eq0 = Equation('(= a (arccoth b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\coth(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arcsec(verbose=False):
    eq0 = Equation('(= a (arcsec b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\sec(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arcsech(verbose=False):
    eq0 = Equation('(= a (arcsech b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\sech(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arcsin(verbose=False):
    eq0 = Equation('(= a (arcsin b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\sin(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arcsinh(verbose=False):
    eq0 = Equation('(= a (arcsinh b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\sinh(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arctan(verbose=False):
    eq0 = Equation('(= a (arctan b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\tan(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__arctanh(verbose=False):
    eq0 = Equation('(= a (arctanh b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\tanh(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__cosec(verbose=False):
    eq0 = Equation('(= a (cosec b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arccosec(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__cosech(verbose=False):
    eq0 = Equation('(= a (cosech b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arccosech(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__cos(verbose=False):
    eq0 = Equation('(= a (cos b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arccos(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__cosh(verbose=False):
    eq0 = Equation('(= a (cosh b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arccosh(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__cot(verbose=False):
    eq0 = Equation('(= a (cot b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arccot(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__coth(verbose=False):
    eq0 = Equation('(= a (coth b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arccoth(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__sec(verbose=False):
    eq0 = Equation('(= a (sec b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arcsec(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__sech(verbose=False):
    eq0 = Equation('(= a (sech b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arcsech(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__sin(verbose=False):
    eq0 = Equation('(= a (sin b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arcsin(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__sinh(verbose=False):
    eq0 = Equation('(= a (sinh b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arcsinh(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__tan(verbose=False):
    eq0 = Equation('(= a (tan b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arctan(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__makeSubject1Input__tanh(verbose=False):
    eq0 = Equation('(= a (tanh b))', 'scheme', verbose=verbose)
    modifiedAST = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'b=\\arctanh(a)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



if __name__=='__main__':
    test__makeSubject2Input__addition0()
    test__makeSubject2Input__addition1()
    test__makeSubject2Input__subtraction0()
    test__makeSubject2Input__subtraction1()
    test__makeSubject2Input__multiply0()
    test__makeSubject2Input__multiply1()
    test__makeSubject2Input__divide0()
    test__makeSubject2Input__divide1()
    test__makeSubject2Input__exponent0()
    test__makeSubject2Input__exponent1()
    test__makeSubject2Input__nroot0()
    test__makeSubject2Input__nroot1()
    test__makeSubject2Input__log0()
    test__makeSubject2Input__log1()
    test__makeSubject1Input__arccosec()
    test__makeSubject1Input__arccosech()
    test__makeSubject1Input__arccos()
    test__makeSubject1Input__arccosh()
    test__makeSubject1Input__arccot()
    test__makeSubject1Input__arccoth()
    test__makeSubject1Input__arcsec()
    test__makeSubject1Input__arcsech()
    test__makeSubject1Input__arcsin()
    test__makeSubject1Input__arcsinh()
    test__makeSubject1Input__arctan()
    test__makeSubject1Input__arctanh()
    test__makeSubject1Input__cosec()
    test__makeSubject1Input__cosech()
    test__makeSubject1Input__cos()
    test__makeSubject1Input__cosh()
    test__makeSubject1Input__cot()
    test__makeSubject1Input__coth()
    test__makeSubject1Input__sec()
    test__makeSubject1Input__sech()
    test__makeSubject1Input__sin()
    test__makeSubject1Input__sinh()
    test__makeSubject1Input__tan()
    test__makeSubject1Input__tanh()
