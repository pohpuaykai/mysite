class UnionFindByRankWithPathCompression:
    """
    Courtesy of https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
    """
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    #Finds set of given item x
    def find(self, x):

        # Finds the representative of the set
        # that x is an element of 
        if (self.parent[x] != x):

            # if x is not the parent of itself
            # Then x is not the representative of
            # its set, 
            self.parent[x] = self.find(self.parent[x])

            # so we recursively call Find on its parent
            # and move i's node directly under the
            # representative of this set
        return self.parent[x]

    # Do union of two sets represented
    # by x and y
    def union(self, x, y):
        #Actually a 'path', rank=path_height, parent is a nodeset, containing items that are grouped together

        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset ==  yset:
            return

        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree

        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1 # (first insert) iff self.rank[xset]==self.rank[yset] (TODO PROOF)

    def grouping(self):
        groups = dict(map(lambda groupNum: (groupNum, []), set(self.parent)))
        for itemIdx, groupNum in enumerate(self.parent):
            groups[groupNum].append(itemIdx)
        # print(groups)
        listOfList = []
        for groupNum, group in sorted(groups.items(), key=lambda t:t[0]):# sort by groupNum
            listOfList.append(group)
        return listOfList

    def groupingWithFirstInserted(self): #TODO test_case
        from operator import itemgetter
        listOfList = self.grouping()
        listOfInfoDict = []
        for grouping in listOfList:
            # import pdb;pdb.set_trace()
            def itemRankGetter():
                itemRanksOrSingle = itemgetter(*grouping)(self.rank)
                return list(itemRanksOrSingle) if isinstance(itemRanksOrSingle, tuple) else [itemRanksOrSingle]
            itemRanks = itemRankGetter() # earliest-joiners-highest-rank
            earliestJoinerIdxOfGrouping = max(range(len(itemRanks)), key=itemRanks.__getitem__)
            earliestJoiner = grouping[earliestJoinerIdxOfGrouping]
            listOfInfoDict.append({
                'grouping':grouping,
                'earliestJoiner':earliestJoiner#in the context of a tree, the earliestJoiner is the root of the subtree(grouping)
            })
        return listOfList, listOfInfoDict
