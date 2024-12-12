class TermsOfBaseOp:

    @classmethod
    def nodeOfBaseOpByGroup(cls, ast, baseOp):
        """TODO test
        TODO documentation
        """
        #TODO totalNumberOfNodes
        allNodes = set(ast.keys())
        for parent, children in ast.items():
            for child in children:
                allNodes.add(child)

        totalNumberOfNodes = len(allNodes)
        consecutiveNodeId__latexASTNodeId = dict(map(lambda c: (c, c), range(0, totalNumberOfNodes)))
        #####################IMPLEMENTATIONs
        #
        reverseIdMapping = dict(map(lambda t: (t[1], t[0]), consecutiveNodeId__latexASTNodeId.items()))
        uf = UnionFindByRankWithPathCompression(totalNumberOfNodes)
        idToGroup = {}
        allIdsWithBaseOp = []
        baseOpStr = '+'
        stack = [('=', 0)]
        while len(stack) > 0:
            currentNode = stack.pop()
            idToGroup[currentNode[1]] = currentNode
            children = ast.get(currentNode, [])
            stack += children
            #
            nodeName, nodeId = currentNode
            if nodeName == baseOpStr:
                allIdsWithBaseOp.append(nodeId)
            tNodeId = consecutiveNodeId__latexASTNodeId[nodeId]
            for childNode in children:
                childNodeName, childNodeId = childNode
                tChildNodeId = consecutiveNodeId__latexASTNodeId[childNodeId]
                if nodeName == baseOpStr and childNodeName == baseOpStr:
                    uf.union(tNodeId, tChildNodeId)
        grouping = uf.grouping()
        groupingByRightId = []
        for group in grouping:
            groupByRightId = []
            for idx in group:
                groupByRightId.append(reverseIdMapping[idx])
            groupingByRightId.append(groupByRightId)
        ###
        groupsWithBaseOp = []
        for group in groupingByRightId:
            if group[0] in allIdsWithBaseOp:
                nodeGroup = []
                for idx in group:
                    nodeGroup.append(idToGroup[idx])
                groupsWithBaseOp.append(nodeGroup)
        return groupingByRightId, groupsWithBaseOp


    @classmethod
    def findTermsOfBaseOp(cls, ast, baseOp): # this for factorisation
        """TODO test
        
        gets the children of groupsWithBaseOp, and then put them together :)
        """
        groupingByRightId, groupsWithBaseOp = cls.idsOfBaseOpByGroup(ast, baseOp)
        termsByGroup = []
        for group in groupsWithBaseOp:
            childrenOfGroup = []
            for node in group:
                children = ast.get(node, [])
                childrenOfGroup += children
            termsByGroup.append(childrenOfGroup)
        return termsByGroup
