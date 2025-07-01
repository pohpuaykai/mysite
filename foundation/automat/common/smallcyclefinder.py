# from foundation.automat.common.lookaheadsearcher import LookAheadSearcher

class SmallCycleFinder:#KVL
    """
    Courtesy of Charissa Tan weiyi(1990 nov 12) and lim wei zhong (???)

    TODO use test cases from MST, and create test cases for this and MST

    #not sure if this is good, trying to use APSP
    """
    
    # @classmethod
    # def findCycles(cls, g):
    #     """
    #     g is dict of nodeId to list of nodeId
    #     """
    #     nodesVisited = set() #to check for cycle formation
    #     cycles = []
    #     def exitNow(cid, level, parent, child__parent):
    #         nodesVisited.add(cid)
    #         return False
    #     def lookAhead(cid, level, parent, lcid, llevel, lparent, childid, child__parent):
    #         if childid in nodesVisited:# cycle is formed
    #             #need to backtrack to get all the nodeId in cycle
    #             cycle = []
    #             cNode = lparent
    #             while cNode in child__parent:
    #                 cycle.insert(0, cNode)
    #                 cNode = child__parent[cNode]
    #             #also need to backtrack on the other side
    #             #the other side, would have started with childid
                
    #             cNode = childid
    #             while cNode in child__parent: # TODO what if cNode has more than 1 parent??, then we will form more than 1 cycle...
    #                 #TODO those paths that contain nodes, that does not have any other neighbours (isolated), should not be considered again...
    #                 if cNode not in cycle:# find the earliest common node
    #                     #previous cNode was the end of the cycle.
    #                     cycle.append(cNode)
    #                     cNode = child__parent[cNode]
    #                 else:#we reached the end of cycle, and we need to snip off the handle of the innoculation loop
    #                     snipLoc = cycle.index(cNode)
    #                     cycle = cycle[snipLoc:]# conviently located on my left hand 
                        
                        
    #             #then meet at the nearest common point
                
    #             cycles.add(cycle)
    #         return abs(level - llevel) > 2#we only want to look ahead 1 level
    #     def unvisitable(childid):
    #         return childid not in nodesVisited # but we should allow look ahead
    #     queue = [(0,0,None)]
    #     LookAheadSearcher.bfsbt(g, queue, exitNow, lookAhead)
    #     return cycles


    ########################below is a new beginning
    # @classmethod
    # def compressPath(cls, g):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<not needed, remove?
    #     """
        
    #     courtesy of Charissa Tan Weiyi (12 11 1990) & shaw the french tutor

    #     :params g: 
    #     connection graph g, nodeId to its list of children nodeId
    #     nodeId with no children are not included.
    #     :types g: dict[int, list[int]]
    #     """
    #     compressedG = {}
    #     edges__superPaths = {}#edge is between 2 branchPoints
    #     superPath = []
    #     branchPoints = []
    #     branchPointStart = None
    #     stack = [0]#assume 0 is always in g<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #     while len(stack):
    #         c = stack.pop(0)
    #         children = g[c]
    #         queue += children
    #         if len(children) > 1:#branch point
    #             branchPoints.append(c)#this is in DFS order
    #             if branchPointStart is None:#c is startPoint
    #                   branchPointStart = c
    #             else:#c is endPoint
    #                   edges__superPaths[(branchPointStart, c)] = copy.copy(superPath)
    #                   branchPointStart = None
    #                   #make connection in newNode
    #                   children = compressedG.get(branchPointStart, [])
                      
    #                   children.append(c)
    #                   branchPointStart = None
    #             #collect the superPath, but has to be connected to branchPoints
    #             superPath = []
                
    #         else:
    #             superPath.append(c)
                
    #     return compressedG


    ########################below is a new beginning
    @classmethod
    def findCycles(cls, g):
        """
        
        courtesy of Charissa Tan Weiyi (12 11 1990)

        g is undirected_connected_graph

        we find spanningTree (DFSTree),
        take subtracted_edges
        for subtracted_edge in subtracted_edges:
            $0:find path in spanning_tree between the subtracted_edge, connect them with subtracted_edge and that is a cycle in the original graph
            memoise all the intermediate paths in path

        we may use all-pairs-shortest-path in the connection step, but very inefficient for small number of subtracted_edges????? not very sure, have not calculated
        instead for $0



        TODO implement
        TODO cover with test cases

        """
        pass #TODO implement all-pairs-shortest-path
        #constructing undirected_spanning_tree
        from foundation.automat.common.spanningtree import SpanningTree
        cycles = []
        undirectedSpanningTree, subtracted_edges = SpanningTree.undirectedSpanningTreeDBFSSearchUndirectedGraph(g, breadthFirst=True)
        print(undirectedSpanningTree)
        doubleSidedEdges = set() # this is a little wasted, could be checked in undirectedSpanningTreeDBFSSearchUndirectedGraph
        tuple_startNode_endNode__list_stPath = {}#memoise spanningTreePaths for each startNode, endNode
        for subtracted_edge in subtracted_edges:
            if subtracted_edge not in doubleSidedEdges:
                doubleSidedEdges.add(subtracted_edge); doubleSidedEdges.add((subtracted_edge[1], subtracted_edge[0])) # prevent adding the same edge twice for different directions
                #find a path between subtracted_edge[0] and subtracted_edge[1] in undirectedSpanningTree
                #check memoised first
                stPath = tuple_startNode_endNode__list_stPath.get(subtracted_edge, None)
                if stPath is None:
                    stack = [(subtracted_edge[0], [subtracted_edge[0]])]; visited_node = set()#keep the wholepath? any other way?
                    while len(stack) > 0:
                        current, path = stack.pop(); visited_node.add(current); #pop-order is depthfirst
                        if current == subtracted_edge[1]: # check target
                            stPath = path; break
                        for neighbour in undirectedSpanningTree[current]:
                            if neighbour not in visited_node:
                                stack.append((neighbour, path+[neighbour]))
                                #memoise, this is an edge in the undirectedSpanningTree
                                tuple_startNode_endNode__list_stPath[(current, neighbour)] = [current, neighbour]
                                tuple_startNode_endNode__list_stPath[(neighbour, current)] = [neighbour, current]
                                #

                    #enumerate stPath for each length<stPath and memoise
                    for length in range(2, len(stPath)-1):#enumeration like a sliding window of varying length, start from length 2, because we are only considering edges
                        for startNodeIdx in range(0, len(stPath)-length+1):
                            tuple_startNode_endNode__list_stPath[(stPath[startNodeIdx], stPath[startNodeIdx+length-1])] = stPath[startNodeIdx:startNodeIdx+length]
                            tuple_startNode_endNode__list_stPath[(stPath[startNodeIdx+length-1], stPath[startNodeIdx])] = reversed(stPath[startNodeIdx:startNodeIdx+length])
                    #
                cycles.append(stPath+[subtracted_edge[0]]) # go back to first node to form a cycle
        return cycles