import copy

class LookAheadSearcher:
    """
    TODO test
    courtesy of Charissa Tan weiyi(1990 nov 12) and lim wei zhong (???)

    copy.deepcopy(queue) is like a savepoint for the queue, ready to jump back to the savepoint if something goes wrong.
    Can also be adapted for mixing search-type DFS/BFS/AFS, depending on the weights of the graph

    TODO adapt for Recommend.combingSearch?

    """
    
    @classmethod
    def bfsbt(cls, g, queue, exitNow, lookAhead, unvisitable):#bfs with backtrack
        #queue = [0] #assume start
        child__parent = {}
        while len(queue):
            cid, level, parent = queue.pop(0)#BFS
            child__parent[cid] = parent
            #exit if level is too high
            exitCondMet = exitNow(cid, level, parent, child__parent)   #implement
            #use to track nodes that were already visited, to make small cycle
            if exitCondMet:
                break
            #look ahead
            lqueue = copy.deepcopy(queue)
            while len(lqueue):
                lcid, llevel, lparent = lqueue.pop(0)
                # checking criterion
                child__parent[lcid] = lparent
        
                for childid in g[lcid]:
                    skipChild = lookAhead(cid, level, parent, lcid, llevel, lparent, childid, child__parent) #implement
                #check if a basic cycle is formed
                    if not skipChild:
                        lqueue.append((childid, llevel+1, lcid))
            #exit if checking criterion is met
            #end of look ahead
            for childid in g[lcid]:
                if not unvisitable(childid):
                    queue.append((childid, level+1, cid))