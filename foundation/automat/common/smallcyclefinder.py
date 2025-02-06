from foundation.automat.common.lookaheadsearcher import LookAheadSearcher

class SmallCycleFinder:#KVL
    """
    Courtesy of Charissa Tan weiyi(1990 nov 12) and lim wei zhong (???)

    TODO use test cases from MST, and create test cases for this and MST
    """
    
    @classmethod
    def findCycles(cls, g):
        """
        g is dict of nodeId to list of nodeId
        """
        nodesVisited = set() #to check for cycle formation
        cycles = []
        def exitNow(cid, level, parent, child__parent):
            nodesVisited.add(cid)
            return False
        def lookAhead(cid, level, parent, lcid, llevel, lparent, childid, child__parent):
            if childid in nodesVisited:# cycle is formed
                #need to backtrack to get all the nodeId in cycle
                cycle = []
                cNode = lparent
                while cNode in child__parent:
                    cycle.insert(0, cNode)
                    cNode = child__parent[cNode]
                #also need to backtrack on the other side
                #the other side, would have started with childid
                
                cNode = childid
                while cNode in child__parent:
                    if cNode not in cycle:# find the earliest common node
                        #previous cNode was the end of the cycle.
                        cycle.append(cNode)
                        cNode = child__parent[cNode]
                    else:#we reached the end of cycle, and we need to snip off the handle of the innoculation loop
                        snipLoc = cycle.index(cNode)
                        cycle = cycle[snipLoc:]# conviently located on my left hand 
                        
                        
                #then meet at the nearest common point
                
                cycles.add(cycle)
            return abs(level - llevel) > 2#we only want to look ahead 1 level
        def unvisitable(childid):
            return childid not in nodesVisited # but we should allow look ahead
        queue = [(0,0,None)]
        LookAheadSearcher.bfsbt(g, queue, exitNow, lookAhead)
        return cycles