import inspect
import pprint

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


def test__removeMinusZero__removeNodeIds0(verbose=False):
    ast = {
        ('=', 0): [('a', 1), ('-', 2)],
        ('-', 2): [('b', 3), ('-', 4)],
        ('-', 4): [('c', 5), ('0', 6)]
    }
    nodeIdsToRemove = [4, 6]
    expected__modifiedAst = {
        ('=', 0): [('a', 1), ('-', 2)],
        ('-', 2): [('b', 3), ('c', 5)],
    }
    eq = Equation(ast=ast)
    modifiedAst = eq._removeNodeIds(nodeIdsToRemove)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected__modifiedAst == modifiedAst)
    if verbose:
        pp.pprint(modifiedAst)





if __name__=='__main__':
    test__removeMinusZero__removeNodeIds0(True)