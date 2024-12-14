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


#################################################################################################################

def test__onetermFactorisation__cutSubtreeAtRoot(verbose=False):


    eq0 = Equation('(= z (+ (* 2 a) (+ (* 2 b) (+ (* 2 c) (+ (* 2 d) (+ (* 2 e) (+ (* 2 f) (+ (* 2 g) (+ (* 2 h) (+ (* 2 i) (+ (* 2 j) (* 2 k))))))))))))', 'scheme')
    rootNode = None
    for nonLeaf in eq0.ast.keys():
        if str(nonLeaf[0]) == '2':
            rootNode = nonLeaf
            break
    subTree = eq0._cutSubASTAtRoot(rootNode) # need to find a rootNode (with the rightID)
    expected = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == subTree)
    if verbose:
        pp.pprint(subTree)


def test__onetermFactorisation__cutSubtreeAtRoot0(verbose=False):


    eq0 = Equation('(= z (+ (* (sin (* (+ x 1) (- x 1))) a) (+ (* (sin (* (+ x 1) (- x 1))) b) (+ (* (sin (* (+ x 1) (- x 1))) c) (+ (* (sin (* (+ x 1) (- x 1))) d) (+ (* (sin (* (+ x 1) (- x 1))) e) (+ (* (sin (* (+ x 1) (- x 1))) f) (+ (* (sin (* (+ x 1) (- x 1))) g) (+ (* (sin (* (+ x 1) (- x 1))) h) (+ (* (sin (* (+ x 1) (- x 1))) i) (+ (* (sin (* (+ x 1) (- x 1))) j) (* (sin (* (+ x 1) (- x 1))) k))))))))))))', 'scheme')
    rootNode = None
    for nonLeaf in eq0.ast.keys():
        if str(nonLeaf[0]) == 'sin':
            rootNode = nonLeaf
            break
    subTree = eq0._cutSubASTAtRoot(rootNode) # need to find a rootNode (with the rightID)
    expected = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == subTree)
    if verbose:
        pp.pprint(subTree) # we are expecting the AST of (sin (* (+ x 1) (- x 1)))


def test__onetermFactorisation__findDistributivePath(verbose=False):
    """
                              +
            +                                  t    <<<<<3
   +                 +                         a    <<<<<5, 6
   3                 y                         n    
   s                 +                         5    <<<<<6
   i                 c                         +    <<<<<7
   n                 o                         z    
   2                 s                              
   +                 2                              <<<<<14
   x                 +                              <<<<<15
                     x
    """
    ast = {
    ('=',0):[('+',1),('F',2)],
    ('+',1):[('+',3),('tan',4)],
    ('+',3):[('+',5),('+',6)],
    ('tan',4):[('+',7)],
    ('+',5):[('3',8),('sin',9)],
    ('+',6):[('y',10),('cos',11)],
    ('+',7):[('5',12),('z',13)],
    ('sin',9):[('+',14)],
    ('cos',11):[('+',15)],
    ('+',14):[('2',16),('x',17)],
    ('+',15):[('2',18),('x',19)]}
    startNode = ('=', 0)
    expected_terms = [[4, 3, 8, 10, 11], [12, 13], [16, 17], [18, 19]]
    #use the algo from _findAllDistributivePaths TODO
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_terms == distributivePaths)
    if verbose:
        pp.pprint(distributivePaths)


def test__onetermFactorisation__findDistributivePath0(verbose=False):
    """
    
    2+sin(x)+2(x+1)+1/2
               +          <<<<this is what we want
          +         +     <<<<this is what we want
       2     s    *    /  
             i    2    1
             n    (    2
             (    x    
             x    +       <<<<this is what we what
             )    1
                  )
    """

    ast = {
    ('=',0):[('+',1),('F',2)],
    ('+',1):[('+',2),('+',3)],
    ('+',2):[('2',4),('sin',5)],
    ('+',3):[('*',6),('/',7)],
    ('*',6):[('2',8),('+',9)],
    ('/',7):[('1',10),('2',11)],
    ('sin',5):[('x',12)],
    ('+',9):[('x',13),('1',14)]} # to be filled in
    startNode = ('=', 0)#to be filled in 
    expected_terms = [[4, 5, 6, 7], [13, 14]]
    #use the algo from _findAllDistributivePaths TODO
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_terms == distributivePaths)
    if verbose:
        pp.pprint(distributivePaths)




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

    # test__onetermFactorisation__cutSubtreeAtRoot() # not yet pass
    # test__onetermFactorisation__cutSubtreeAtRoot0() # not yet pass
    # test__onetermFactorisation__findDistributivePath() # not yet pass
    # test__onetermFactorisation__findDistributivePath0() # not yet pass