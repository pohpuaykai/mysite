import inspect
import pprint

from foundation.automat.common.dynamicprogrammingontress import DynamicProgrammingOnTrees

pp = pprint.PrettyPrinter(indent=4)

def test__latexUnparser__findImplicitMultiplyIds(verbose=False):
    """
                              +
            *                                  t    <<<<<3
   *                 *                         a    <<<<<5, 6
   3                 y                         n    
   s                 *                         5    <<<<<6
   i                 c                         *    <<<<<7
   n                 o                         z    
   2                 s                              
   *                 2                              <<<<<14
   x                 *                              <<<<<15
                     x
    """
    ast = {
    ('=',0):[('+',1),('F',2)],
    ('+',1):[('*',3),('tan',4)],
    ('*',3):[('*',5),('*',6)],
    ('tan',4):[('*',7)],
    ('*',5):[('3',8),('sin',9)],
    ('*',6):[('y',10),('cos',11)],
    ('*',7):[('5',12),('z',13)],
    ('sin',9):[('*',14)],
    ('cos',11):[('*',15)],
    ('*',14):[('2',16),('x',17)],
    ('*',15):[('2',18),('x',19)]}
    startNode = ('=', 0)#to be filled in 
    def baseCases(node, memo, states):

        return signalFromBaseCases

    def modifiers(node, memo, states):

        return node, memo, states

    def recursionLogic(node, memo, states, _recursionFunction):

        return node, memo, states

    memo, states = DynamicProgrammingOnTrees.findAllNodeIdsWithPredicate(ast, startNode, baseCases, modifiers, recursionLogic)
    expected = [3, 5, 6, 7, 14, 15] # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == idsWithPredicate)
    if verbose:
        pp.pprint(idsWithPredicate)


def test__equationOneTermFactorizable__findAllDistributivePaths(verbose=False):
    """
    NOTICE that the root of termSubtree are not always *
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
    def baseCases(node, memo, states):

        return signalFromBaseCases

    def modifiers(node, memo, states):

        return node, memo, states

    def recursionLogic(node, memo, states, _recursionFunction):

        return node, memo, states


    childToParent = {}
    stack = [('=', 0)]
    while len(stack) > 0:
        parent = stack.pop()
        children = ast.get(parent, [])
        for child in children:
            childToParent[child] = parent
        stack += children
    
    memo, states = DynamicProgrammingOnTrees.findAllNodeIdsWithPredicate(ast, predicate, startNode)
    expected = [[1, 2, 3], [9]] # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == idsWithPredicate)
    if verbose:
        pp.pprint(idsWithPredicate)


if __name__=='__main__':
    test__latexUnparser__findImplicitMultiplyIds(True)
    # test__equationOneTermFactorizable__findAllDistributivePaths(True)