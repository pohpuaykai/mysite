class PathFinderInTree:

    @classmethod
    def getPath(cls, ast, startNode, endNode):
        """
        We assume that startNode is not a leaf

        This method returns the a path from startNode(inclusive) to endNode(inclusive)
        """
        from foundation.automat.common.backtracker import Backtracker
        stack = [Backtracker(
            label=startNode[0], 
            neighbours=None, 
            argumentIdx=None, 
            prev=None, 
            id=startNode[1]
        )]
        foundBacktracker = None
        while len(stack) > 0:
            currentBacktracker = stack.pop()
            nodeName = currentBacktracker.label
            nodeId = currentBacktracker.id
            currentNode = (nodeName, nodeId)
            if currentNode == endNode:
                foundBacktracker = currentBacktracker
                break
            children = ast.get(currentNode, [])
            for childNode in children:
                childBacktracker = Backtracker(
                    label=childNode[0],
                    neighbours=None,
                    argumentIdx=None,
                    prev=currentBacktracker,
                    id=childNode[1]
                )
                stack.append(childBacktracker)
        if foundBacktracker is None:
            raise Exception('Cannot Find EndNode')
        path = [(foundBacktracker.label, foundBacktracker.id)]
        currentBacktracker = foundBacktracker
        while currentBacktracker.prev is not None:
            currentBacktracker = currentBacktracker.prev
            path.insert(0, (currentBacktracker.label, currentBacktracker.id))
        return path


    @classmethod
    def findNodeNameWhoseChildrenAreLeaves(cls, ast, nodeName, startNode):
        stack = [startNode]
        allSuchNodes = []
        while len(stack) > 0:
            currentNode = stack.pop()
            children = ast.get(currentNode)
            if currentNode[0] == nodeName:
                #check if currentNode's children are all leaves
                if children is None:
                    continue # currentNode itself is a leaf
                else:
                    allLeaves = True
                    for child in children:
                        if child in ast:
                            allLeaves = False
                            break
                    if allLeaves:
                        allSuchNodes.append(currentNode)
            if children is not None:
                stack += children
        return allSuchNodes