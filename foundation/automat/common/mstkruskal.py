class MstKruskal:

    @classmethod
    def minimumSpanningTreeKruskal(cls, vertexIterable, edgeIterableSortable, edgeWeight):
        """ TODO test
        Courtesy of Chapter 21 of "Introduction to Algorithms (4Ed)" by Thomas Cormens

        vertexIterable is a iterable of integers
        edgeIterableSortable is a iterable of 2-tuples of integers in vertexIterable, must also be sortable
        edgeWeight is a function, from an element in edgeIterableSortable to a number
        """
        from automat.common.unionfindbyrankwithpathcompression import UnionFindByRankWithPathCompression
        A = set()
        uf = UnionFindByRankWithPathCompression(len(vertexIterable))
        edgeIterableSortable__sorted = sorted(edgeIterableSortable, key=lambda edge: edgeWeight[edge])
        for edge in edgeIterableSortable__sorted:
            if uf.find(edge[0]) != uf.find(edge[1]):
                A = A.add(edge)
                uf.union(edge[0], edge[1])
        return A