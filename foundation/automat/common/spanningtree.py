class SpanningTree:
    @classmethod
    def minimumSpanningTree(cls, g, w):
    """
    g must be a connected graph
    
    spanning tree
    1. contain all nodes from g
    2. edges from g, so that g remains connected
    
    minimum spanning tree.
    1.a spanning tree
    2. the sum of all the edges in output is the lowest amongst all the possible spanning trees that can be derived from g
    
    Courtesy of Charissa Tan Weiyi and her pilates friends

    TODO cover it with testcases
    """
    visited__edges = set()
    node__minEdgeWeight = {}#todo init to inf?
    node__edge = {}
    stack = [0]
    while len(stack) > 0:
        p = stack.pop()
        children = g[p]
        stack += children
        for c in children:
            edge = set([p,c])#the direction does not matter
            if edge not in visited__edges:
                visited__edges.add(edge)
                weight = w[edge]
                if p not in node_minEdgeWeight or node_minEdgeWeight[p] > weight:
                    #update node p
                    node__minEdgeWeight[p] = weight
                    node__edge[p] = edge
                if c not in node_minEdgeWeight or node_minEdgeWeight[c] > weight:
                    #update node c
                    node__minEdgeWeight[c] = weight
                    node__minEdgeWeight[c] = edge
    #reconstruct spanningTree
    stg = {}
    for node, edge in node__edge.items():
        edge = tuple(edge)
        oldChildren = g.get(node, [])
        if node == edge[0]:# then edge[1] is neighbour
            oldChildren.append(edge[1])
        else: # then edge[0] is neighbour
            oldChildren.append(edge[0])
        stg[node] = oldChildren
    return stg