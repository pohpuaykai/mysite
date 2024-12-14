import inspect
import pprint

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


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
    test__onetermFactorisation__cutSubtreeAtRoot() # not yet pass
    # test__onetermFactorisation__cutSubtreeAtRoot0() # not yet pass
    # test__onetermFactorisation__findDistributivePath() # not yet pass
    # test__onetermFactorisation__findDistributivePath0() # not yet pass