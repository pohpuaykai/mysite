import inspect
import pprint

from foundation.automat.common.dynamicprogrammingontress import DynamicProgrammingOnTrees

pp = pprint.PrettyPrinter(indent=4)

def test__latexUnparser__findImplicitMultiplyIds(verbose=False):

    ast = None # to be filled in
    def predicate(node, memo, _recursiveFindPredicateIds):
        pass # to be filled in 
    startNode = #to be filled in 
    idsWithPredicate = DynamicProgrammingOnTrees.findAllNodeIdsWithPredicate(ast, predicate, startNode)
    expected = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == idsWithPredicate)
    if verbose:
        pp.pprint(idsWithPredicate)


def test__equationOneTermFactorizable__findAllDistributivePaths(verbose=False):

    ast = None # to be filled in
    def predicate(node, memo, _recursiveFindPredicateIds):
        pass # to be filled in 
    startNode = #to be filled in 
    idsWithPredicate = DynamicProgrammingOnTrees.findAllNodeIdsWithPredicate(ast, predicate, startNode)
    expected = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == idsWithPredicate)
    if verbose:
        pp.pprint(idsWithPredicate)


if __name__=='__main__':
    test__latexUnparser__findImplicitMultiplyIds(True)
    test__equationOneTermFactorizable__findAllDistributivePaths(True)