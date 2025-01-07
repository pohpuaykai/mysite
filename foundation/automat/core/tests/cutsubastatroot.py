import inspect
import pprint

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


def test__onetermFactorisation__cutSubtreeAtRoot(verbose=False):


    eq0 = Equation('(= z (+ (* 2 a) (+ (* 2 b) (+ (* 2 c) (+ (* 2 d) (+ (* 2 e) (+ (* 2 f) (+ (* 2 g) (+ (* 2 h) (+ (* 2 i) (+ (* 2 j) (* 2 k))))))))))))', 'scheme')
    rootNode = ('*', 3)
    if verbose:
        print(eq0.ast)
    subTree = eq0._cutSubASTAtRoot(rootNode)
    expected = {('*', 3): [('2', 5), ('a', 6)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == subTree)
    if verbose:
        pp.pprint(subTree)


def test__onetermFactorisation__cutSubtreeAtRoot0(verbose=False):


    eq0 = Equation('(= z (+ (* (sin (* (+ x 1) (- x 1))) a) (+ (* (sin (* (+ x 1) (- x 1))) b) (+ (* (sin (* (+ x 1) (- x 1))) c) (+ (* (sin (* (+ x 1) (- x 1))) d) (+ (* (sin (* (+ x 1) (- x 1))) e) (+ (* (sin (* (+ x 1) (- x 1))) f) (+ (* (sin (* (+ x 1) (- x 1))) g) (+ (* (sin (* (+ x 1) (- x 1))) h) (+ (* (sin (* (+ x 1) (- x 1))) i) (+ (* (sin (* (+ x 1) (- x 1))) j) (* (sin (* (+ x 1) (- x 1))) k))))))))))))', 'scheme')
    rootNode = ('*', 3)
    if verbose:
        print(eq0.ast)
    subTree = eq0._cutSubASTAtRoot(rootNode) # need to find a rootNode (with the rightID)
    expected = {   
    ('*', 3): [('sin', 5), ('a', 6)],
    ('*', 9): [('+', 14), ('-', 15)],
    ('+', 14): [('x', 21), ('1', 22)],
    ('-', 15): [('x', 23), ('1', 24)],
    ('sin', 5): [('*', 9)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == subTree)
    if verbose:
        pp.pprint(subTree) # we are expecting the AST of (sin (* (+ x 1) (- x 1)))




if __name__=='__main__':
    test__onetermFactorisation__cutSubtreeAtRoot()
    test__onetermFactorisation__cutSubtreeAtRoot0()
