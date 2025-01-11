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


def test__linearEliminationBySubstitution_eq1__removeNodeIds0(verbose=False):
    ast = {   
    ('*', 2): [('I_{R_{C}}', 1), ('R_{C}', 3)],
    ('*', 8): [('I_{R}', 7), ('R', 9)],
    ('-', 4): [('*', 2), ('V^{Q1}_{BE}', 5)],
    ('-', 6): [('-', 4), ('0', 10)],
    ('=', 0): [('*', 8), ('-', 6)]}
    nodeIdsToRemove = [6, 10]
    expected__modifiedAst = {
    ('*', 2): [('I_{R_{C}}', 1), ('R_{C}', 3)],
    ('*', 8): [('I_{R}', 7), ('R', 9)],
    ('-', 4): [('*', 2), ('V^{Q1}_{BE}', 5)],
    ('=', 0): [('*', 8), ('-', 4)]
    }
    eq = Equation(ast=ast)
    modifiedAst = eq._removeNodeIds(nodeIdsToRemove)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected__modifiedAst == modifiedAst)
    if verbose:
        print('OG:')
        pp.pprint(ast)
        print('modifiedAst')
        pp.pprint(modifiedAst)
        print('expected__modifiedAst')
        pp.pprint(expected__modifiedAst)



if __name__=='__main__':
    test__removeMinusZero__removeNodeIds0()
    test__linearEliminationBySubstitution_eq1__removeNodeIds0()