import inspect
import pprint

from foundation.automat.common.mstprim import MstPrim

def mst__test1(verbose=True):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<move to spanningtreetest.py
    g = {
    0:[1,3],
    1:[0,2,4],
    2:[1,5],
    3:[0,4,6],
    4:[1,3,5,7],
    5:[2,4,8],
    6:[3,7],
    7:[4,6,8],
    8:[5,7]
    }#no directed, edges point both ways
    w = {
    (1,4):0,
    (3,4):1,
    (4,5):2
    (4,7):3,
    (0,1):4,
    (1,2):5,
    (6,7):6,
    (7,8):7,
    (0,3):100,
    (2,5):100,
    (3,6):100,
    (5,8):100
    }
    expected = {
    0:[1],
    1:[0,2,4],
    3:[4],
    5:[4],
    4:[1,3,5,7],
    6:[7],
    7:[6,8],
    8:[7]
    } # forms a wang chinese character
    #need to convert to nodeList, and edgeEdge
    nodeList = list(set(list(g.keys()) + [b for a in g.values() for b in a]))
    edgeList = list(w.keys())
    def childrenOfVertex(input):
        return g[input]
    startVertex = 4
    mst = MstPrim.minimumSpanningTreePrim(nodeList, edgeList, w, childrenOfVertex, startVertex)

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedPath == path)
    if verbose:
        print(path)

if __name__=='__main__':
    mst__test1(True)