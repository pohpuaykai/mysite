import pprint
import inspect

from foundation.automat.common.unionfindbyrankwithpathcompression import UnionFindByRankWithPathCompression


def test__simpletest__numbersOnly(verbose=False):
    uf = UnionFindByRankWithPathCompression(5)
    uf.union(0, 2)
    uf.union(4, 2)
    uf.union(3, 1)
    grouping = uf.grouping()
    expected_grouping = [[0, 2, 4], [1, 3]]
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', grouping == expected_grouping)
    if verbose:
        print(grouping)


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
    expected_grouping = [[0], [1, 3, 5, 6], [2], [4], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19]]

    totalNumberOfNodes = 20
    consecutiveNodeId__latexASTNodeId = dict(map(lambda c: (c, c), range(0, totalNumberOfNodes)))
    #####################IMPLEMENTATIONs
    #
    reverseIdMapping = dict(map(lambda t: (t[1], t[0]), consecutiveNodeId__latexASTNodeId.items()))
    uf = UnionFindByRankWithPathCompression(totalNumberOfNodes)
    baseOpStr = '+'
    stack = [('=', 0)]
    while len(stack) > 0:
        currentNode = stack.pop()
        children = ast.get(currentNode, [])
        stack += children
        #
        nodeName, nodeId = currentNode
        tNodeId = consecutiveNodeId__latexASTNodeId[nodeId]
        for childNode in children:
            childNodeName, childNodeId = childNode
            tChildNodeId = consecutiveNodeId__latexASTNodeId[childNodeId]
            if nodeName == baseOpStr and childNodeName == baseOpStr:
                uf.union(tNodeId, tChildNodeId)
    grouping = uf.grouping()
    groupingByRightId = []
    for group in grouping:
        groupByRightId = []
        for idx in group:
            groupByRightId.append(reverseIdMapping[idx])
        groupingByRightId.append(groupByRightId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', groupingByRightId == expected_grouping)
    if verbose:
        print(groupingByRightId)




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
    expected_grouping = [[0], [1, 2, 3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14]]

    totalNumberOfNodes = 15
    consecutiveNodeId__latexASTNodeId = dict(map(lambda c: (c, c), range(0, totalNumberOfNodes)))
    #####################IMPLEMENTATIONs
    #
    reverseIdMapping = dict(map(lambda t: (t[1], t[0]), consecutiveNodeId__latexASTNodeId.items()))
    uf = UnionFindByRankWithPathCompression(totalNumberOfNodes)
    baseOpStr = '+'
    stack = [('=', 0)]
    while len(stack) > 0:
        currentNode = stack.pop()
        children = ast.get(currentNode, [])
        stack += children
        #
        nodeName, nodeId = currentNode
        tNodeId = consecutiveNodeId__latexASTNodeId[nodeId]
        for childNode in children:
            childNodeName, childNodeId = childNode
            tChildNodeId = consecutiveNodeId__latexASTNodeId[childNodeId]
            if nodeName == baseOpStr and childNodeName == baseOpStr:
                uf.union(tNodeId, tChildNodeId)
    import pdb;pdb.set_trace()
    grouping = uf.grouping()
    groupingByRightId = []
    for group in grouping:
        groupByRightId = []
        for idx in group:
            groupByRightId.append(reverseIdMapping[idx])
        groupingByRightId.append(groupByRightId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', groupingByRightId == expected_grouping)
    if verbose:
        print(groupingByRightId)


if __name__=='__main__':
    # test__simpletest__numbersOnly(True)
    # test__onetermFactorisation__findDistributivePath(True)
    test__onetermFactorisation__findDistributivePath0(True)