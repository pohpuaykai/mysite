import copy

class AllPairShortestPath:

    @classmethod
    def apspTree(cls, undirectedTree, startNode):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<not used REMOVE?
        """
        
        first DFS to get branchNodes (like compressPaths)
        combinatorially, example:
        branchNode+superPath+branchNode = [0, 1, 2, 3, 4]
        then all pair of shortest paths:
        [0]
        [1]
        [2]
        [3]
        [4]
        [0, 1]
        [1, 2]
        [2, 3]
        [3, 4]
        [0, 1, 2]
        [1, 2, 3]
        [2, 3, 4]
        [0, 1, 2, 3]
        [1, 2, 3, 4]
        [0, 1, 2, 3, 4]

        [4]<<< repeated.
        [3, 4]
        [2, 3]
        [1, 2]
        [0, 1]
        [2, 3, 4]
        [1, 2, 3]
        [0, 1, 2]
        [1, 2, 3, 4]
        [0, 1, 2, 3]
        [0, 1, 2, 3, 4]

        TODO put together with MST?

        TODO cover with testcases
        
        :params undirectedTree: undirectedTree is a tree whose edges are not directed AND unweighted

        :type mst: dict[int,list[int]]
        """
        #since its a tree any path will be the shortest path
        #find a path in tree, enumerate all paths of length < original path
        #for node in path, remove node from children_list of OG_graph
        #repeat until empty OG_graph
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<implement this instead..... its like the smallcyclefinder middle part, but for all edges, but i don't need it now
        pass




        # #start from list_of_edges, expand the list of edges
        # #get list_of_edges
        # startNode__endNode = {} # this is a path
        # tuple_startNode_endNode__list_shortestPaths = {}
        # for parentNode, neighbours in undirectedTree.items():
        #     for neighbour in neighbours:
        #         if (parentNode, neighbour) not in tuple_startNode_endNode__list_shortestPaths:
        #             tuple_startNode_endNode__list_shortestPaths[(parentNode, neighbour)] = [parentNode, neighbour]
        #             if parentNode in startNode__endNode:

        #             else:

        #             if neighbour in startNode__endNode:

        #             else:



        # #since its a tree any path will be the shortestpath


        # #go through every pair of node in undirectedTree
        # #since this is a connected_undirected_tree, the keys of undirectedTree must be exactly all the nodes
        # nodes = list(undirectedTree.keys())

        # for node0 in nodes:
        #     for node1 in nodes:
        #         #find a path from node0 to node1



        #         if (node0, node1) not in tuple_startNode_endNode__list_shortestPaths:
        #             #find a path from node0 to node1, with DFS (since unweighted), combinatorally 


        #             #not very efficient here... a lot of duplicates
        #             for node2 in nodes:

        #         if (node1, node0) not in tuple_startNode_endNode__list_shortestPaths:




