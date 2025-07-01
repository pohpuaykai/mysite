import inspect
import pprint

from foundation.automat.common.spanningtree import SpanningTree
from foundation.automat.common.flattener import Flattener


def mst__dc_twoResistor_parallel(verbose=True):
    g = {
        0: [2, 3],
        1: [2, 3],
        2: [0, 1, 6],
        3: [0, 1, 5],
        4: [5, 6],
        5: [4, 3],
        6: [4, 2]}
    w = {(0, 2): 5, (2, 0): 5, (0, 3): 5, (3, 0): 5, (1, 2): 5, (2, 1): 5, (1, 3): 5, (3, 1): 5, 
    (2, 6): 5, (6, 2): 5, (3, 5): 5, (5, 3): 5, (4, 5): 4, (5, 4): 4, (4, 6): 4, (6, 4): 4}

    expected = None
    stg = SpanningTree.minimumSpanningTreeKruskal(list((set(Flattener.flatten(list(w.keys()))))), list(w.keys()), w)


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == stg)
    if verbose:
        print(stg)

if __name__=='__main__':
    mst__dc_twoResistor_parallel(True)