import inspect
import pprint

from foundation.automat.common.allpairshortestpath import AllPairShortestPath
# from foundation.automat.common.flattener import Flattener


def mst__dc_twoResistor_parallel(verbose=True):
    stg = {
    1: [2], #
    2: [1, 0, 6], #
    4: [6, 5], 
    6: [4, 2], 
    0: [3, 2], 
    3: [0], 
    5: [4]
    }
    startNode = 2

    expected = None

    shortestPaths = AllPairShortestPath.apsp(stg, startNode)

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == shortestPaths)
    if verbose:
        print(shortestPaths)

if __name__=='__main__':
    mst__dc_twoResistor_parallel(True)