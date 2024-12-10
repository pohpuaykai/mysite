class DynamicProgrammingOnTrees:

    @classmethod
    def findAllNodeIdsWithPredicate(cls, ast, predicate, startNode):
        """
        Courtsey of https://www.geeksforgeeks.org/introduction-to-dynamic-programming-on-trees/
        """

        def _recursiveFindPredicateIds(node, memo):
            nodeName = node[0]
            nodeId = node[1]
            memo[nodeId] = predicate(node, memo, _recursiveFindPredicateIds)
            return memo[nodeId]

        idsWithPredicate = []
        memo = {}
        _recursiveFindPredicateIds(startNode, memo)
        for nodeId, predicateValue in memo.items():
            if predicateValue == True:
                idsWithPredicate.append(nodeId)

        return idsWithPredicate