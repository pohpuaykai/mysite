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
        from foundation.automat.common.unionfindbyrankwithpathcompression import UnionFindByRankWithPathCompression
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
            # print(currentNode, children)
            if nodeName == baseOpStr:
                allIdsWithBaseOp.append(nodeId)
            tNodeId = consecutiveNodeId__latexASTNodeId[nodeId]
            for childNode in children:
                childNodeName, childNodeId = childNode
                tChildNodeId = consecutiveNodeId__latexASTNodeId[childNodeId]
                if nodeName == baseOpStr and childNodeName == baseOpStr:
                    uf.union(tNodeId, tChildNodeId)
        # grouping = uf.grouping()
        grouping, groupingWithFirstInserted = uf.groupingWithFirstInserted()
        groupingByRightIdWithEarliestJoiner = []
        # import pdb;pdb.set_trace()
        # for group in grouping:
        for infoDict in groupingWithFirstInserted:
            group = infoDict['grouping']
            earliestJoiner = infoDict['earliestJoiner']
            groupByRightId = []
            for idx in group:
                groupByRightId.append(reverseIdMapping[idx])
            # groupingByRightId.append(groupByRightId)
            if group[0] in allIdsWithBaseOp:
                groupingByRightIdWithEarliestJoiner.append({
                    'group':group,
                    'earliestJoiner':earliestJoiner
                })
        ###
        groupsWithBaseOp = []
        for infoDict in groupingByRightIdWithEarliestJoiner:
            group = infoDict['group']
            # earliestJoiner = infoDict['earliestJoiner']
            if group[0] in allIdsWithBaseOp: # already check earlier, TODO remove, this is redundant
                nodeGroup = []
                for idx in group:
                    nodeGroup.append(idToGroup[idx])
                groupsWithBaseOp.append(nodeGroup)

        return groupingByRightIdWithEarliestJoiner, groupsWithBaseOp


    @classmethod
    def findTermsOfBaseOp(cls, ast, baseOp): # this for factorisation
        """TODO test
        
        gets the children of groupsWithBaseOp, and then put them together :)
        """
        groupingByRightIdWithEarliestJoiner, groupsWithBaseOp = cls.idsOfBaseOpByGroup(ast, baseOp)
        termsByGroup = []
        for group in groupsWithBaseOp:
            childrenOfGroup = []
            for node in group:
                children = ast.get(node, [])
                childrenOfGroup += children
            termsByGroup.append(childrenOfGroup)
        #TODO also return the first element of each group to be placed into unionFind (that will correspond to the root of the subTree, because we DFS)
        return termsByGroup 
