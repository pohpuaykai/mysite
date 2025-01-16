class MstPrim:

    @classmethod
    def minimumSpanningTreePrim(cls, vertexIterable, edgeIterableSortable, edgeWeight, childrenOfVertex, startVertex=None):
        """ TODO test
        Courtesy of Chapter 21 of "Introduction to Algorithms (4Ed)" by Thomas Cormens
        
        vertexIterable is a iterable of integers
        edgeIterableSortable is a iterable of 2-tuples of integers in vertexIterable, must also be sortable
        edgeWeight is a function, from an element in edgeIterableSortable to a number
        childrenOfVertex is a function from input to a list of vertices that are adjacent to input
        """
        from foundation.automat.common.fibonacciheap import FibonacciHeap, FibonacciHeapNode
        def node(vertex):
            return FibonacciHeapNode(vertex)
        key = dict(map(lambda vertex: (vertex, float('inf')), vertexIterable))
        pi = dict(map(lambda vertex: (vertex, None), vertexIterable))
        if startVertex is None:
            startVertex = list(vertexIterable)[0]
        key[startVertex] = 0
        priorityQueue = FibonacciHeap() # untested, TODO use for Recommend.combingSearch
        for vertex in vertexIterable:
            priorityQueue.insert(vertex)
        """
        Chapter 21 of "Introduction to Algorithms (4Ed)" by Thomas Cormens
        A = {(child, pi[child]): child in (vertexIterable - set(startVertex) - set(priorityQueue))}
        This means every time take out an element from PQ, we put into A
        Everything pi is changed, we have to update A
        """
        A = {}
        while not priorityQueue.isEmpty():
            cVertex = priorityQueue.extractMin().child # add cVertex to the tree
            A[pi[cVertex]] = cVertex # edge in reversed direction... BEWARE
            for child in childrenOfVertex(cVertex): # update keys of cVertex's non-tree neighbours
                if priorityQueue.contain(child) and edgeWeight((cVertex, child)) < key[child]: # TODO undirected Graph
                    #
                    if pi[child] in A:
                        A[pi[child]] = cVertex
                    #
                    pi[child] = cVertex
                    key[child] = edgeWeight((cVertex, child))
                    priorityQueue.decreaseKey(node(child), edgeWeight(cVertex, child)) # refactor node TODO
        return A