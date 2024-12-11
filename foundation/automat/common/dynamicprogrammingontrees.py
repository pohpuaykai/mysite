class DynamicProgrammingOnTrees:

    @classmethod
    def dpOnTree(cls, ast, startNode, baseCases, modifiers, recursionLogic):
        """
        Courtsey of https://www.geeksforgeeks.org/introduction-to-dynamic-programming-on-trees/
        """

        def _recursionFunction(node, memo, states):
            signalFromBaseCases = baseCases(node, memo, states)
            if 'return' signalFromBasesCases:
                return signalFromBasesCases['return']
            node, memo, states = modifiers(node, memo, states)
            node, memo, states = recursionLogic(node, memo, states, _recursionFunction)


        memo = {}
        states = {}
        _recursionFunction(startNode, memo, states)

        return memo, states