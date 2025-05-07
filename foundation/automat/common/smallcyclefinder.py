from foundation.automat.common.lookaheadsearcher import LookAheadSearcher

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
    @classmethod
    def compressPath(cls, g):
        """
        
        courtesy of Charissa Tan Weiyi (12 11 1990) & shaw the french tutor

        :params g: 
        connection graph g, nodeId to its list of children nodeId
        nodeId with no children are not included.
        :types g: dict[int, list[int]]
        """
        compressedG = {}
        edges__superPaths = {}#edge is between 2 branchPoints
        superPath = []
        branchPoints = []
        branchPointStart = None
        stack = [0]#assume 0 is always in g
        while len(stack):
            c = stack.pop(0)
            children = g[c]
            queue += children
            if len(children) > 1:#branch point
                branchPoints.append(c)#this is in DFS order
                if branchPointStart is None:#c is startPoint
                      branchPointStart = c
                else:#c is endPoint
                      edges__superPaths[(branchPointStart, c)] = copy.copy(superPath)
                      branchPointStart = None
                      #make connection in newNode
                      children = compressedG.get(branchPointStart, [])
                      
                      children.append(c)
                      branchPointStart = None
                #collect the superPath, but has to be connected to branchPoints
                superPath = []
                
            else:
                superPath.append(c)
                
        return compressedG

    @classmethod
    def findCycles(cls, g):
        """
        
        courtesy of Charissa Tan Weiyi (12 11 1990)

        compressPath
        apsp on compressedGraph
        between each pair, choose every 2 paths to make a face/hole/

        TODO implement
        TODO cover with test cases

        """
        pass #TODO implement all-pairs-shortest-path