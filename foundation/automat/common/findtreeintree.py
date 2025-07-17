class FindTreeInTree:

    @classmethod
    def findAllTreeInTree(cls, gesuchteTree, gesuchteTreeRoot, targetTree, targetTreeRoot, _nodeMatch, callbackForMatchCompletion=lambda x: x, callbackForTreeTreeMatchingStart=lambda x: x): # assume gesuchteTree & targetTree are both connected_trees
        """
        MUST be BFS to match the whole TREE?

        another way is topological_sort, then subsequence matching(longestcommonsubsequence) TODO both, parallelise, see which finish first

        USE THIS IN PARSETEST to AVOID nodeId differences<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        #
        # import pprint;pp = pprint.PrettyPrinter(indent=4)
        # print('gesuchteTree')
        # pp.pprint(gesuchteTree)
        
        #
        list_of_matches = []
        queue = [targetTreeRoot]
        while len(queue) > 0:
            jetzt = queue.pop(0)#INORDER for (top->bottom, left->right), use BFS
            children = targetTree.get(jetzt, [])
            queue += targetTree.get(jetzt, [])
            for child in children:
                if _nodeMatch(gesuchteTreeRoot, child):
                    list_of_matches.append(child)
        #
        # print('list_of_matches<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        # print(list_of_matches)


        if len(list_of_matches) > 0:#some found => list_of_matches (different nodeId)
            allMatchedTrees = []
            for targetTreeRoot in list_of_matches:
                gesuchteTreeStack, targetTreeStack = [gesuchteTreeRoot], [targetTreeRoot]
                matchedTargetTree, lastLeafMatched = None, None # for getting nodeId
                callbackForTreeTreeMatchingStart(targetTreeRoot)
                # print('rooting at ', targetTreeRoot)
                # print('___________________________________________________________________')
                while len(gesuchteTreeStack) > 0 and len(targetTreeStack) > 0:
                    gesuchteCurrent, targetCurrent = gesuchteTreeStack.pop(0), targetTreeStack.pop(0) # BFS
                    gesuchteCurrentChildren = gesuchteTree.get(gesuchteCurrent, [])
                    gesuchteTreeStack+=gesuchteCurrentChildren
                    # print('popped:', gesuchteCurrent, targetCurrent); import pdb;pdb.set_trace()
                    # print('gesuchteTreeStack', gesuchteTreeStack)
                    # print('targetTreeStack', targetTreeStack)
                    # if gesuchteCurrent[0] != targetCurrent[0]: #no_match #<<<<<<<<<<<<<<<<<<<<<<<<<<<funcmatching
                    if not _nodeMatch(gesuchteCurrent, targetCurrent):
                        break
                    else:
                        #record the matchedTargetTree, but format of matchedTargetTree does not take leaf as key
                        lastLeafMatched = targetCurrent
                        if matchedTargetTree is None:#initialise
                            matchedTargetTree = {}
                        # targetCurrentChildren=sorted(targetTree.get(targetCurrent, []), key=lambda child: child[0])#target cannot be sorted
                        targetCurrentChildren = targetTree.get(targetCurrent, []) # assume the_user gives it in the right order
                        if len(targetCurrentChildren) > 0 and len(gesuchteCurrentChildren) > 0:
                            matchedTargetTree[targetCurrent] = targetCurrentChildren
                        #put back to the stacks
                        # gesuchteTreeStack+=sorted(gesuchteTree.get(gesuchteCurrent, []), key=lambda child: child[0])
                        targetTreeStack+=targetCurrentChildren
                    # print(gesuchteTreeStack, 'gesuchteTreeStack')
                    # print(targetTreeStack, 'targetTreeStack')
                if matchedTargetTree is not None and len(gesuchteTreeStack)==0 and len(targetTreeStack) == 0: # (len(gesuchteTreeStack)==0)~need to check if it matched the_whole_gesuchteTree
                    callbackForMatchCompletion(targetTreeRoot)
                    if len(matchedTargetTree) > 0: 
                        allMatchedTrees.append((targetTreeRoot, matchedTargetTree))
                    else:
                        allMatchedTrees.append((targetTreeRoot, {lastLeafMatched:[]}))
                # print('allMatchedTrees', allMatchedTrees, '0000000000000000000000000000000000000000000000000000000000000000');import pdb;pdb.set_trace()
            # print('~~~~~')
            # print(allMatchedTrees)
            # print('~~~~~')
            return allMatchedTrees
        return []