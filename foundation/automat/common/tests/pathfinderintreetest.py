import inspect
import pprint

from foundation.automat.common.pathfinderintree import PathFinderInTree

def test__smallAST__findPath(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {
    ('=', 0):[('+', 1), ('F', 2)],
    ('+', 1):[('1', 3), ('*', 4)],
    ('*', 4):[('2', 5), ('^', 6)],
    ('^', 6):[('x', 7), ('3', 8)]
    }

    startNode = ('+', 1)
    endNode = ('^', 6)
    path = PathFinderInTree.getPath(ast, startNode, endNode)
    expectedPath = [('+', 1), ('*', 4), ('^', 6)]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedPath == path)
    if verbose:
        print(path)


def test__smallAST__findNodeNameWhoseChildrenAreLeaves(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {
    ('=', 0):[('+', 1), ('F', 2)],
    ('+', 1):[('1', 3), ('*', 4)],
    ('*', 4):[('2', 5), ('^', 6)],
    ('^', 6):[('x', 7), ('3', 8)]
    }

    startNode = ('+', 1)
    nodeName = '^'
    weirdNode = PathFinderInTree.findNodeNameWhoseChildrenAreLeaves(ast, nodeName, startNode)
    expectedWeirdNode = [('^', 6)]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedWeirdNode == weirdNode)
    if verbose:
        print(weirdNode)


if __name__=='__main__':
    # test__smallAST__findPath(True)
    test__smallAST__findNodeNameWhoseChildrenAreLeaves(True)