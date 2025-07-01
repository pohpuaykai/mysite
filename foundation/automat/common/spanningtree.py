from foundation.automat.common.unionfindbyrankwithpathcompression import UnionFindByRankWithPathCompression

class SpanningTree:



    @classmethod
    def minimumSpanningTreeKruskal(cls, vertexIterable, edgeIterableSortable, edgeWeight):
        """ TODO test
        Courtesy of Chapter 21 of "Introduction to Algorithms (4Ed)" by Thomas Cormens

        vertexIterable is a iterable of integers
        edgeIterableSortable is a iterable of 2-tuples of integers in vertexIterable, must also be sortable
        edgeWeight is a function, from an element in edgeIterableSortable to a number
        """
        A = set()
        uf = UnionFindByRankWithPathCompression(len(vertexIterable))
        edgeIterableSortable__sorted = sorted(edgeIterableSortable, key=lambda edge: edgeWeight[edge])
        for edge in edgeIterableSortable__sorted:#Add commentMore actions
            if uf.find(edge[0]) != uf.find(edge[1]):
                A.add(edge)
                uf.union(edge[0], edge[1])

        #not part of original algorithm, reconstruct the tree
        stg = {} # node to list_of_neighbours
        for node0, node1 in list(A):
            oldChildren = stg.get(node0, [])
            oldChildren.append(node1)
            stg[node0] = oldChildren
            #
            oldChildren = stg.get(node1, [])
            oldChildren.append(node0)
            stg[node1] = oldChildren
            #
        #find subtracted edges
        return stg, list(set(edgeIterableSortable) - A)


    @classmethod
    def undirectedSpanningTreeDBFSSearchUndirectedGraph(cls, g, breadthFirst=False):
        """
        g is undirected_connected_graph

        if breadthFirst is false, then its depthFirst
        """
        if breadthFirst:
            popOrder = 0 # first out -> queue
        else: 
            popOrder = -1 # last out -> stack

        edgesSelected = set()
        undirectedSpanningTree = {} # undirected
        startNode = list(g.keys())[0];#any random one... is there a better way?
        stack = [startNode]; visited = set([startNode])
        while len(stack) > 0:
            current = stack.pop(popOrder); 
            for neighbour in g[current]:
                if neighbour not in visited:
                    visited.add(neighbour);
                    stack.append(neighbour) # last in
                    #add to undirected_spanning_tree
                    existingNeighbours = undirectedSpanningTree.get(current, [])
                    existingNeighbours.append(neighbour)
                    undirectedSpanningTree[current] = existingNeighbours
                    edgesSelected.add((current, neighbour))
                    #if undirected then we only add one side
                    existingNeighbours = undirectedSpanningTree.get(neighbour, [])
                    existingNeighbours.append(current)
                    undirectedSpanningTree[neighbour] = existingNeighbours
                    edgesSelected.add((neighbour, current))
        #
        subtracted_edges = []
        for parentNode, neighbours in g.items(): #since g is undirected_connected_graph, every edge is on g
            for neighbour in neighbours:
                if (parentNode, neighbour) not in edgesSelected:
                    subtracted_edges.append((parentNode, neighbour))
        return undirectedSpanningTree, subtracted_edges