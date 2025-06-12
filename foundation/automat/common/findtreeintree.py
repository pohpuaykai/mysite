class FindTreeInTree:

    @classmethod
    def findAllTreeInTree(gesuchteTree, gesuchteTreeRoot, targetTree, _nodeMatch): # assume gesuchteTree & targetTree are both connected_trees
        """
        another way is topological_sort, then subsequence matching(longestcommonsubsequence) TODO both, parallelise, see which finish first

        USE THIS IN PARSETEST to AVOID nodeId differences<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        list_of_matches = []
        for children in targetTree.values():
            for child in children:
                # if child[0] == gesuchteTreeRoot[0]: #<<<<<<<<<<<<<<<<<<<<<<<<<<<funcmatching
                if _nodeMatch(gesuchteTreeRoot, child):
                    list_of_matches.append(child)
        if len(list_of_matches) > 0:#some found => list_of_matches (different nodeId)
            allMatchedTrees = []
            for targetTreeRoot in list_of_matches:
                gesuchteTreeStack, targetTreeStack = [gesuchteTreeRoot], [targetTreeRoot]
                matchedTargetTree, lastLeafMatched = None, None # for getting nodeId
                while len(gesuchteTreeStack) > 0 and len(targetTreeStack) > 0:
                    gesuchteCurrent, targetCurrent = gesuchteTreeStack.pop(), targetTreeStack.pop()
                    # if gesuchteCurrent[0] != targetCurrent[0]: #no_match #<<<<<<<<<<<<<<<<<<<<<<<<<<<funcmatching
                    if not _nodeMatch(gesuchteCurrent, targetCurrent):
                        break
                    else:
                        #record the matchedTargetTree, but format of matchedTargetTree does not take leaf as key
                        lastLeafMatched = targetCurrent
                        if matchedTargetTree is None:#initialise
                            matchedTargetTree = {}
                        targetCurrentChildren=sorted(targetTree.get(gesuchteCurrent, []), key=lambda child: child[0])
                        if len(targetCurrentChildren) > 0:
                            matchedTargetTree[gesuchteCurrent] = targetCurrentChildren
                        #put back to the stacks
                        gesuchteTreeStack+=sorted(gesuchteTree.get(gesuchteCurrent, []), key=lambda child: child[0])
                        targetTreeStack+=targetCurrentChildren
                if matchedTargetTree is not None:
                    if len(matchedTargetTree) > 0: 
                        allMatchedTrees.append(matchedTargetTree)
                    else:
                        allMatchedTrees.append({lastLeafMatched:[]})
            return allMatchedTrees