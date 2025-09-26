class StringCompare:
    """TODO please put LongestCommonSubsequence, LongestCommonSubstring here too :D"""

    @classmethod
    def damerauLevenshtein(cls, a, b):
        """Courtesy of https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance

        the Original Flavour

        allow custom_scores, seperate the score info #(done in general, extendedDamerauLevenschstein is flexible enough to handle this.)
        0. deletion
        1. insertion
        2. substitution
        3. transposition
        """
        d = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]# a is the first index, b is the second index
        # import pdb;pdb.set_trace()

        for i in range(0, len(a)+1):
            d[i][0] = i
        for j in range(0, len(b)+1):
            d[0][j] = j

        for i in range(1, len(a)+1):
            for j in range(1, len(b)+1):
                if a[i-1] == b[j-1]: #this is only substitution_cost... 
                    cost = 0
                else:
                    cost = 1
                d[i][j] = min(
                    d[i-1][j]+1, #deletion, cost fixed as +1
                    d[i][j-1]+1, #insertion, cost fixed as +1
                    d[i-1][j-1]+cost #substitution, we consider the prevCost, no matter if the test_pass_or_fail
                )
                if i >1 and j >1 and a[i-1]==b[j-2] and a[i-2]==b[j-1]:#the 'so_called_transposition' only compares 2_characters_before_after
                    d[i][j] = min(d[i][j], d[i-2][j-2]+1)#transposition, cost is fixed as +1, but we don't even consider prev_cost, if the test does not pass.........
        #
        import pprint; pp = pprint.PrettyPrinter(indent=4);
        pp.pprint(d)
        #
        return d[len(a)][len(b)]

    @classmethod
    def extendedDamerauLevenschstein(cls, s0, s1, comparisonDictionaries, costAggregator=min, initialiser=None):
        """
        Each comparisonDictionary, so that we may have 'different_algorithms' for different pairs of strings...?

        {
            leftCharOffset: how much offset to add to index of s0 at that point in iteration
            rightCharOffset: how much offset to add to index of s1 at that point in iteration
            nonEqualityLeft: True or False or None only, if True, then we add the cost if s0[i-s0Offset]!=s1[j-s1Offset]. If False, then we add the cost if s0[i-s0Offset]==s1[j-s1Offset]. If None, then we add the cost without checking anything
            nonEqualityRight: same as nonEqualityLeft, but sides are swapped. in NonEqualityLeft:
                    s0[i-leftCharOffset]==s1[j-rightCharOffset]
                in NonEqualityRight:
                    s0[i-rightCharOffset]==s1[j-leftCharOffset]
            prevCostOffset0: from which previous do we carry over the cost from?
            prevCostOffset1: from which previous do we carry over the cost from?
            cost: The cost to add for comparison

        }

        costAggregator takes a list of object, and return a object. Depends on how we want to count cost

        """
        #INIT
        if initialiser is None: # then we do the default initialisation
            d = [[0 for _ in range(len(s1)+1)] for _ in range(len(s0)+1)]# a is the first index, b is the second index
            for i in range(0, len(s0)+1):
                d[i][0] = i
            for j in range(0, len(s1)+1):
                d[0][j] = j
        else:
            d = initialiser()

        #
        for i in range(1, len(s0)+1):
            for j in range(1, len(s1)+1):
                #
                costs = []
                for compare in comparisonDictionaries:
                    if (compare['nonEqualityLeft'] is not None and compare['nonEqualityRight'] is not None) and\
                        (i>=max(compare['leftCharOffset'], compare['rightCharOffset']) and j>=max(compare['leftCharOffset'], compare['rightCharOffset'])) and\
                        (i>=compare['prevCostOffset0'] and j>=compare['prevCostOffset1']):
                        if compare['nonEqualityLeft'] is True:
                            conditionLeft = s0[i-compare['leftCharOffset']]!=s1[j-compare['rightCharOffset']]
                        else: #has to be false
                            conditionLeft = s0[i-compare['leftCharOffset']]==s1[j-compare['rightCharOffset']]

                        if compare['nonEqualityRight'] is True:
                            conditionRight = s0[i-compare['rightCharOffset']]!=s1[j-compare['leftCharOffset']]
                        else: #has to be false
                            conditionRight = s0[i-compare['rightCharOffset']]==s1[j-compare['leftCharOffset']]



                        if conditionLeft and conditionRight: # here we fix the 'and'
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']]+compare['cost'])
                        elif not compare['considerPrevOnlyIfPassCheck']:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']])


                    elif (compare['nonEqualityLeft'] is not None) and\
                        (i>=compare['leftCharOffset'] and j>=compare['rightCharOffset']) and\
                        (i>=compare['prevCostOffset0'] and j>=compare['prevCostOffset1']): #ignore the nonEqualityRight is None
                        if compare['nonEqualityLeft'] is True:
                            conditionLeft = s0[i-compare['leftCharOffset']]!=s1[j-compare['rightCharOffset']]
                        else: #has to be false
                            conditionLeft = s0[i-compare['leftCharOffset']]==s1[j-compare['rightCharOffset']]

                        if conditionLeft:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']]+compare['cost'])
                        elif not compare['considerPrevOnlyIfPassCheck']:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']])
                    elif (compare['nonEqualityRight'] is not None) and\
                        (i>=compare['rightCharOffset'] and j>=compare['leftCharOffset']) and\
                        (i>=compare['prevCostOffset0'] and j>=compare['prevCostOffset1']): #ignore the nonEqualityLeft is None

                        if compare['nonEqualityRight'] is True:
                            conditionRight = s0[i-compare['rightCharOffset']]!=s1[j-compare['leftCharOffset']]
                        else: #has to be false
                            conditionRight = s0[i-compare['rightCharOffset']]==s1[j-compare['leftCharOffset']]

                        if conditionRight:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']]+compare['cost'])
                        elif not compare['considerPrevOnlyIfPassCheck']:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']])
                    elif (compare['nonEqualityLeft'] is None and compare['nonEqualityRight'] is None) and\
                        (i>=compare['prevCostOffset0'] and j>=compare['prevCostOffset1']): # just append

                        if not compare['considerPrevOnlyIfPassCheck']:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']]+compare['cost'])

                    # else: #unhandled case, reflect to user
                    #     raise Exception(f'comparisonDictionaries has a dictionary: {compare}, whose nonEquality is not handled')
                

                print(costs)
                #
                d[i][j] = costAggregator(costs)
        #
        #
        import pprint; pp = pprint.PrettyPrinter(indent=4);
        pp.pprint(d)
        #
        return d[-1][-1]

    @classmethod
    def extendedDamerauLevenschsteinWithEntities(cls, s0, s1, s0Entities, s1Entities, comparisonDictionaries, costAggregator=min, initialiser=None):
        """
        schemeLabelCompliant

        s1Entities are positions in s1 that should be treated as 1 character
        s2Entities are positions in s2 that should be treated as 1 character

        entities are a list of 2_tuples, where (s, e), s is the startPosition[inclusive], and e is the endPosition[exclusive]

        
        Each comparisonDictionary, so that we may have 'different_algorithms' for different pairs of strings...?

        {
            leftCharOffset: how much offset to add to index of s0 at that point in iteration
            rightCharOffset: how much offset to add to index of s1 at that point in iteration
            nonEqualityLeft: True or False or None only, if True, then we add the cost if s0[i-s0Offset]!=s1[j-s1Offset]. If False, then we add the cost if s0[i-s0Offset]==s1[j-s1Offset]. If None, then we add the cost without checking anything
            nonEqualityRight: same as nonEqualityLeft, but sides are swapped. in NonEqualityLeft:
                    s0[i-leftCharOffset]==s1[j-rightCharOffset]
                in NonEqualityRight:
                    s0[i-rightCharOffset]==s1[j-leftCharOffset]
            prevCostOffset0: from which previous do we carry over the cost from?
            prevCostOffset1: from which previous do we carry over the cost from?
            cost: The cost to add for comparison

        }

        costAggregator takes a list of object, and return a object. Depends on how we want to count cost

        """

        s0Entities = sorted(s0Entities, key=lambda d: d[0]) # sort by startPos
        s1Entities = sorted(s1Entities, key=lambda d: d[0]) # sort by startPos
        #fill up the gaps of the entities
        def fillGaps(s, entities):
            sAll = []; prevEnd = None
            if entities[0][0] == 0:
                sAll.append(entities[0]); prevEnd = entities[0][1]; idx = 1;
            else:
                sAll.append((0, entities[0][0])); prevEnd = entities[0][0]; idx = 0
            while idx < len(entities):
                entity = entities[idx]
                if prevEnd != entity[0]: # there is gap, but each character must be an entity, and not be grouped together by this
                    for i in range(prevEnd, entity[0]):
                        sAll.append((i, i+1))
                    # sAll.append((prevEnd, entity[0])); 
                    prevEnd = entity[0]
                else: # there is no gap
                    sAll.append(entity); prevEnd = entity[1]
                    idx += 1
            if sAll[-1][1] != len(s):
                for i in range(sAll[-1][1], len(s)):
                    sAll.append((i, i+1))
                # sAll.append((sAll[-1][1], len(s)))
            return sAll
        s0All = fillGaps(s0, s0Entities); s1All = fillGaps(s1, s1Entities)
        # print('s0All', s0All); print('s1All', s1All); import pdb;pdb.set_trace()
        o = { s0:s0All, s1:s1All} # will break if s0 == s1
        def get(st, idx):
            sAll = o[st]
            s, e = sAll[idx]
            return st[s:e]
        def leng(st):
            return len(o[st])


        if initialiser is None: # then we do the default initialisation
            d = [[0 for _ in range(leng(s1)+1)] for _ in range(leng(s0)+1)]# a is the first index, b is the second index
            for i in range(0, leng(s0)+1):
                d[i][0] = i
            for j in range(0, leng(s1)+1):
                d[0][j] = j
        else:
            d = initialiser(get, leng)

        #
        for i in range(1, leng(s0)+1):
            for j in range(1, leng(s1)+1):
                #
                costs = []
                for compare in comparisonDictionaries:
                    if (compare['nonEqualityLeft'] is not None and compare['nonEqualityRight'] is not None) and\
                        (i>=max(compare['leftCharOffset'], compare['rightCharOffset']) and j>=max(compare['leftCharOffset'], compare['rightCharOffset'])) and\
                        (i>=compare['prevCostOffset0'] and j>=compare['prevCostOffset1']):
                        if compare['nonEqualityLeft'] is True:
                            # conditionLeft = s0[i-compare['leftCharOffset']]!=s1[j-compare['rightCharOffset']]
                            conditionLeft = get(s0, i-compare['leftCharOffset']) != get(s1, j-compare['rightCharOffset'])
                        else: #has to be false
                            # conditionLeft = s0[i-compare['leftCharOffset']]==s1[j-compare['rightCharOffset']]
                            conditionLeft = get(s0, i-compare['leftCharOffset']) == get(s1, j-compare['rightCharOffset'])

                        if compare['nonEqualityRight'] is True:
                            # conditionRight = s0[i-compare['rightCharOffset']]!=s1[j-compare['leftCharOffset']]
                            conditionRight = get(s0, i-compare['rightCharOffset']) != get(s1, j-compare['leftCharOffset'])
                        else: #has to be false
                            # conditionRight = s0[i-compare['rightCharOffset']]==s1[j-compare['leftCharOffset']]
                            conditionRight = get(s0, i-compare['rightCharOffset'])==get(s1, j-compare['leftCharOffset'])



                        if conditionLeft and conditionRight: # here we fix the 'and'
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']]+compare['cost'])
                        elif not compare['considerPrevOnlyIfPassCheck']:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']])


                    elif (compare['nonEqualityLeft'] is not None) and\
                        (i>=compare['leftCharOffset'] and j>=compare['rightCharOffset']) and\
                        (i>=compare['prevCostOffset0'] and j>=compare['prevCostOffset1']): #ignore the nonEqualityRight is None
                        if compare['nonEqualityLeft'] is True:
                            # conditionLeft = s0[i-compare['leftCharOffset']]!=s1[j-compare['rightCharOffset']]
                            conditionLeft = get(s0, i-compare['leftCharOffset'])!=get(s1, j-compare['rightCharOffset'])
                        else: #has to be false
                            # conditionLeft = s0[i-compare['leftCharOffset']]==s1[j-compare['rightCharOffset']]
                            conditionLeft = get(s0, i-compare['leftCharOffset'])==get(s1, j-compare['rightCharOffset'])

                        if conditionLeft:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']]+compare['cost'])
                        elif not compare['considerPrevOnlyIfPassCheck']:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']])
                    elif (compare['nonEqualityRight'] is not None) and\
                        (i>=compare['rightCharOffset'] and j>=compare['leftCharOffset']) and\
                        (i>=compare['prevCostOffset0'] and j>=compare['prevCostOffset1']): #ignore the nonEqualityLeft is None

                        if compare['nonEqualityRight'] is True:
                            # conditionRight = s0[i-compare['rightCharOffset']]!=s1[j-compare['leftCharOffset']]
                            conditionRight = get(s0, i-compare['rightCharOffset'])!=get(s1, j-compare['leftCharOffset'])
                        else: #has to be false
                            # conditionRight = s0[i-compare['rightCharOffset']]==s1[j-compare['leftCharOffset']]
                            conditionRight = get(s0, i-compare['rightCharOffset'])==get(s1, j-compare['leftCharOffset'])

                        if conditionRight:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']]+compare['cost'])
                        elif not compare['considerPrevOnlyIfPassCheck']:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']])
                    elif (compare['nonEqualityLeft'] is None and compare['nonEqualityRight'] is None) and\
                        (i>=compare['prevCostOffset0'] and j>=compare['prevCostOffset1']): # just append

                        if not compare['considerPrevOnlyIfPassCheck']:
                            costs.append(d[i-compare['prevCostOffset0']][j-compare['prevCostOffset1']]+compare['cost'])

                    # else: #unhandled case, reflect to user
                    #     raise Exception(f'comparisonDictionaries has a dictionary: {compare}, whose nonEquality is not handled')
                

                print(costs)
                #
                d[i][j] = costAggregator(costs)
        #
        #
        import pprint; pp = pprint.PrettyPrinter(indent=4);
        pp.pprint(d)
        #
        return d[-1][-1]


    @classmethod
    def damerauLevenschsteinMimickWithEntities(cls, s0, s1, s0Entities, s1Entities):
        """
        Here we mimick the OG damerauLevenschstein, with our extended version

        this is also an example of how we can create different types of stringcomparison

        maybe try to mimick LCSS too?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        comparisonDictionaries = [
            {#deletion
                'leftCharOffset':1,
                'rightCharOffset':0,
                'nonEqualityLeft':None,
                'nonEqualityRight':None,
                'cost':1,
                'prevCostOffset0':1,
                'prevCostOffset1':0,
                'considerPrevOnlyIfPassCheck':False
            },
            {#insertion
                'leftCharOffset':0,
                'rightCharOffset':1,
                'nonEqualityLeft':None,
                'nonEqualityRight':None,
                'cost':1,
                'prevCostOffset0':0,
                'prevCostOffset1':1,
                'considerPrevOnlyIfPassCheck':False
            },
            {#substitution
                'leftCharOffset':1,
                'rightCharOffset':1,
                'nonEqualityLeft':False,
                'nonEqualityRight':None,
                'cost':1,
                'prevCostOffset0':1,
                'prevCostOffset1':1,
                'considerPrevOnlyIfPassCheck':False
            },
            {#transposition
                'leftCharOffset':1,
                'rightCharOffset':2,
                'nonEqualityLeft':False,
                'nonEqualityRight':False,
                'cost':1,
                'prevCostOffset0':2,
                'prevCostOffset1':2,
                'considerPrevOnlyIfPassCheck':True
            },
        ]
        return cls.extendedDamerauLevenschsteinWithEntities(s0, s1, s0Entities, s1Entities, comparisonDictionaries=comparisonDictionaries)

    @classmethod
    def damerauLevenschsteinMimick(cls, s0, s1):
        """
        Here we mimick the OG damerauLevenschstein, with our extended version

        this is also an example of how we can create different types of stringcomparison

        maybe try to mimick LCSS too?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        comparisonDictionaries = [
            {#deletion
                'leftCharOffset':1,
                'rightCharOffset':0,
                'nonEqualityLeft':None,
                'nonEqualityRight':None,
                'cost':1,
                'prevCostOffset0':1,
                'prevCostOffset1':0,
                'considerPrevOnlyIfPassCheck':False
            },
            {#insertion
                'leftCharOffset':0,
                'rightCharOffset':1,
                'nonEqualityLeft':None,
                'nonEqualityRight':None,
                'cost':1,
                'prevCostOffset0':0,
                'prevCostOffset1':1,
                'considerPrevOnlyIfPassCheck':False
            },
            {#substitution
                'leftCharOffset':1,
                'rightCharOffset':1,
                'nonEqualityLeft':False,
                'nonEqualityRight':None,
                'cost':1,
                'prevCostOffset0':1,
                'prevCostOffset1':1,
                'considerPrevOnlyIfPassCheck':False
            },
            {#transposition
                'leftCharOffset':1,
                'rightCharOffset':2,
                'nonEqualityLeft':False,
                'nonEqualityRight':False,
                'cost':1,
                'prevCostOffset0':2,
                'prevCostOffset1':2,
                'considerPrevOnlyIfPassCheck':True
            },
        ]
        return cls.extendedDamerauLevenschstein(s0, s1, comparisonDictionaries=comparisonDictionaries)