import inspect
import pprint

from math import pi

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


def test__substituteValue__addition(verbose=False):
    eqStr = 'a=b+c'
    subDict = {'b':1, 'c':2}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('3.0', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)


def test__substituteValue__minus(verbose=False):
    eqStr = 'a=b-c'
    subDict = {'b':1, 'c':2}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('-1.0', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)


def test__substituteValue__multiply(verbose=False):
    eqStr = 'a=b c'
    subDict = {'b':2, 'c':3}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('6.0', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)


def test__substituteValue__divide(verbose=False):
    eqStr = 'a=\\frac{b}{c}'
    subDict = {'b':1, 'c':2}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.5', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)


def test__substituteValue__exponential(verbose=False):
    eqStr = 'a=b^c'
    subDict = {'b':2, 'c':2}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('4.0', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)



def test__substituteValue__logarithm(verbose=False):
    eqStr = 'a=\\log_{b}(c)'
    subDict = {'b':2, 'c':4}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('2.0', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)



def test__substituteValue__nroot(verbose=False):
    eqStr = 'a=\\sqrt[b]{c}'
    subDict = {'b':3, 'c':27}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('3.0', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)



def test__substituteValue__arccosecant(verbose=False):
    eqStr = 'a=\\arccosec(b)'
    subDict = {'b':1}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.5707963267948966', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)


def test__substituteValue__arccosecanth(verbose=False):
    eqStr = 'a=\\arccosech(b)'
    subDict = {'b':1}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.881373587019543', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)



def test__substituteValue__arccosine(verbose=False):
    eqStr = 'a=\\arccos(b)'
    subDict = {'b':0.5}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.0471975511965979', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__arccosineh(verbose=False):
    eqStr = 'a=\\arccosh(b)'
    subDict = {'b':1}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.0', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)





def test__substituteValue__arccotangent(verbose=False):
    eqStr = 'a=\\arccot(b)'
    subDict = {'b':0.5}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.1071487177940904', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__arccotangenth(verbose=False):
    eqStr = 'a=\\arccoth(b)'
    subDict = {'b':2}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.5493061443340549', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__arcsecant(verbose=False):
    eqStr = 'a=\\arcsec(b)'
    subDict = {'b':2}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.0471975511965979', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)


def test__substituteValue__arcsecanth(verbose=False):
    eqStr = 'a=\\arcsech(b)'
    subDict = {'b':0.5}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.3169578969248166', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__arcsine(verbose=False):
    eqStr = 'a=\\arcsin(b)'
    subDict = {'b':0.5}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.5235987755982989', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__arcsineh(verbose=False):
    eqStr = 'a=\\arcsinh(b)'
    subDict = {'b':1}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.881373587019543', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__arctangent(verbose=False):
    eqStr = 'a=\\arctan(b)'
    subDict = {'b':0.5}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.4636476090008061', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__arctangenth(verbose=False):
    eqStr = 'a=\\arctanh(b)'
    subDict = {'b':0}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.0', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)





def test__substituteValue__cosecant(verbose=False):
    eqStr = 'a=\\cosec(b)'
    subDict = {'b':pi/4}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.414213562373095', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__cosecanth(verbose=False):
    eqStr = 'a=\\cosech(b)'
    subDict = {'b':1}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.6480542736638855', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)





def test__substituteValue__cosine(verbose=False):
    eqStr = 'a=\\cos(b)'
    subDict = {'b':pi/4}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.7071067811865476', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__cosineh(verbose=False):
    eqStr = 'a=\\cosh(b)'
    subDict = {'b':1}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.5430806348152437', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__cotangent(verbose=False):
    eqStr = 'a=\\cot(b)'
    subDict = {'b':pi/4}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.0000000000000002', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__cotangenth(verbose=False):
    eqStr = 'a=\\coth(b)'
    subDict = {'b':2}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.0373147207275482', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__secant(verbose=False):
    eqStr = 'a=\\sec(b)'
    subDict = {'b':pi/4}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.414213562373095', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__secanth(verbose=False):
    eqStr = 'a=\\sech(b)'
    subDict = {'b':1}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.8509181282393216', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__sine(verbose=False):
    eqStr = 'a=\\sin(b)'
    subDict = {'b':pi/4}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.7071067811865476', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__sineh(verbose=False):
    eqStr = 'a=\\sinh(b)'
    subDict = {'b':1}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('1.1752011936438014', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__tangent(verbose=False):
    eqStr = 'a=\\tan(b)'
    subDict = {'b':pi/4}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.9999999999999999', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)




def test__substituteValue__tangenth(verbose=False):
    eqStr = 'a=\\tanh(b)'
    subDict = {'b':2}
    eq0 = Equation(eqStr, 'latex', verbose=verbose)
    ast = eq0.substituteValue(subDict)
    expectedAst = {('=', 0): [('a', 1), ('0.9640275800758169', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', ast == expectedAst)
    if verbose:
        print(eqStr)
        pp.pprint(subDict)
        pp.pprint(ast)



if __name__=='__main__':
    test__substituteValue__addition()
    test__substituteValue__minus()
    test__substituteValue__multiply()
    test__substituteValue__divide()
    test__substituteValue__exponential()
    test__substituteValue__logarithm()
    test__substituteValue__nroot()
    test__substituteValue__arccosecant()
    test__substituteValue__arccosecanth()
    test__substituteValue__arccosine()
    test__substituteValue__arccosineh()
    test__substituteValue__arccotangent()
    test__substituteValue__arccotangenth()
    test__substituteValue__arcsecant()
    test__substituteValue__arcsecanth()
    test__substituteValue__arcsine()
    test__substituteValue__arcsineh()
    test__substituteValue__arctangent()
    test__substituteValue__arctangenth()
    test__substituteValue__cosecant()
    test__substituteValue__cosecanth()
    test__substituteValue__cosine()
    test__substituteValue__cosineh()
    test__substituteValue__cotangent()
    test__substituteValue__cotangenth()
    test__substituteValue__secant()
    test__substituteValue__secanth()
    test__substituteValue__sine()
    test__substituteValue__sineh()
    test__substituteValue__tangent()
    test__substituteValue__tangenth()