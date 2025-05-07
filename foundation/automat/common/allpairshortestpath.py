class AllPairShortestPath:

    @classmethod
    def apsp(cls, mst, startNode):
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
        
        :params mst: mst is a minimum spanning tree
        :type mst: dict[int,list[int]]
        """
        #dfs graph while keeping the whole path in the stack
        #recursion graph while passing the whole path as argument?
        
        #dfs front-to-back
        ftb_shortestPaths = []
        stack = [[startNode]]
        while len(stack) > 0:
            path = stack.pop()
            ftb_shortestPaths.append(path)
            lastNode = copy.copy(path[-1])
            children = mst.get(lastNode, [])
            for child in children:
                newPath = copy.copy(path)
                newPath.append(child)
                stack.append(newPath)
                
        #recursion back-to-front
        btf_shortestPaths = []
        def recurse(cNode, path):
            if cNode not in g:#it is a leaf
                path = path.insert(0, cNode)
                btf_shortestPaths.append(path)
                return #not sure what to return
            for child in g[cNode]:
                newPath = copy.copy(path)
                newPath.insert(0, cNode)
                btf_shortestPaths.append(newPath)
                recurse(child, newPath)
        recurse(startNode, [])
        return ftb_shortestPaths+btf_shortestPaths # there is going to be repeats. TODO please fix