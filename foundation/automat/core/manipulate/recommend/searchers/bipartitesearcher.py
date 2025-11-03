from copy import copy

from foundation.automat.parser.sorte.schemeparser import Schemeparser
from foundation.automat.common.priorityqueue import PriorityQueue

class BipartiteSearcher:
    """

        #another heuristic might be crammer_method|GE? that will tell us which equation to choose and eliminate first? I think this will work very well...... a way into this heuristic is that  we do the <<2.3.5AmoreComplexCircuit>> bipartiteSolverWay manually, and then match bipartiteSolverWay to the CramerMethod<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    """


    def __init__(self,
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        variableId__vertexId,
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds):
        self.list_equations = list_equations#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO prepend self. to these variables
        self.list_variables = list_variables
        self.equationVariables_bg = equationVariables_bg
        self.vertexId__equationVariableId = vertexId__equationVariableId
        self.equationId__vertexId = equationId__vertexId
        self.variableId__vertexId = variableId__vertexId
        self.type__list_vertexIds = type__list_vertexIds
        self.equationKey = equationKey
        self.variableKey = variableKey
        self.dependentVariableId = dependentVariableId
        self.list_independentVariableIds = list_independentVariableIds
        
        self.bipartiteTreeExpand = True #some equations cannot be reached without increasing the number of equations, so we have to add equationNodes, while we combine them
        self.HIGH_WEIGHTS = 100
        self.LOW_WEIGHTS = 0
        self.init()

    def init(self):#init should be a class?<<<
        self.init__groupEquationsBySimilarity()
        self.init__countNoOfTimesVarAppear()
        if self.bipartiteTreeExpand:
            self.init__idIssuer()
        self.init__valuesForHeuristics()
        self.init__findStartingNodes()

    def search(self): #this should be standardised across different types of searchAlgos
        priorityQueue = PriorityQueue(); 
        priorityQueue.insert({
            'current':maxEquationVertexId, 
            'path':[maxEquationVertexId],
            'visited':[],
            #we assume that this equation only has 1 of each variable
            'variableCount':variableCount
        }, -1)
        while len(priorityQueue) > 0:
            priority, current___dict = priorityQueue.popMaxWithPriority()
            current = current___dict['current']
            #############early termination, what if you waited for a few possible solutions first? how many to wait for?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if set(originalEquationVertexIds).issubset(set(current___dict['path'])): #we used all the original equations
                # print('used up all the ORIGINAL equations')
                # print('p: ', priority)
                # pp.pprint(current___dict)
                # import pdb;pdb.set_trace()
                return current___dict['path'], equationVertexId__tuple_variableVertexIdContaining___NEW
            #############

            visited = copy(current___dict['visited'])
            visited.append(current)
                    
            if current in allEquationVertexIds:#neighbours will be variables
                def sortKey(vertexIdx, path):
                    amt = 0
                    amt += self.sortingEquationHeuristics__similarNeighboursExploredFirst(vertexIdx, path)
                    return amt
                neighbours = sorted(self.equationVariables_bg[current], key=lambda vertexId: sortKey(vertexId, current___dict['path']))#<<<<<<<<<<<<<<<<<fillin sort key
            else:
                def sortKey(vertexIdx, path):
                    amt = 0
                    amt += self.sortingVariableHeuristics__similarNeighboursExploredFirst(vertexIdx, path)
                    return amt
                neighbours = sorted(self.equationVariables_bg[current], key=lambda vertexId: sortKey(vertexId, current___dict['path']))#<<<<<<<<<<<<<<<<<fillin sort key

            for orderOfExploration, neighbour in enumerate(neighbours):#[TODO optimisation possibility] self.equationVariables_bg[current] can be sorted, because you are depending on the orderOfExploration
                if neighbour not in visited:
                    newPath = current___dict['path']+[neighbour]

                    childDict = {
                        'current':neighbour, 
                        'path':newPath, 
                        'visited':visited+[neighbour],
                        'variableCount':current___dict['variableCount']
                        # we assume that this equation only has 1 of each variable
                    }
                    if self.bipartiteTreeExpand:
                        self.treeExpander__equationJoins()

                    if childDict['path'] not in visitedPaths:#global check for no repeat paths
                        visitedPaths.append(childDict['path'])

                        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<les(heuristics)-Mettrez
                        childDictPriority = self.stateRankingHeuristics__originalEquationsPriority(childDictPriority)
                        childDictPriority = self.stateRankingHeuristics__followSortedHeuristics(childDictPriority)
                        childDictPriority = self.stateRankingHeuristics__longerPathPriority(childDictPriority)
                        childDictPriority = self.stateRankingHeuristics__preventIncreaseInUnwantedVariables(childDictPriority)
                        childDictPriority = self.stateRankingHeuristics__preventUsingEquationWithManyUnwantedVariables(childDictPriority)
                        childDictPriority = self.stateRankingHeuristics__linearityCondition(childDictPriority)
                        childDictPriority = self.stateRankingHeuristics__chooseLeastAppearedVariableOfEquationGroup(childDictPriority)
                        childDictPriority = self.stateRankingHeuristics__chooseEquationsFromEquationGroup(childDictPriority)
                        childDictPriority = self.stateRankingHeuristics__penaliseUseOfNewEquation(childDictPriority)
                        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                    if childDictPriority > float('-inf'):#we discard everything that is -infinity
                        priorityQueue.insert(childDict, childDictPriority)#-orderOfExploration try to ensure that those inserted later, have lower priority

        maxLen = min(map(lambda s: len(s), visitedPaths))
        maxLengthPaths = list(filter(lambda s: len(s)==maxLen, visitedPaths))
        # print('maxLengthPaths')
        # print(maxLengthPaths)
        # import pdb; pdb.set_trace()
        favouritePath = maxLengthPaths[0] # [TODO many optimisations possible here]
        if bipartiteTreeExpand:
            return favouritePath, equationVertexId__tuple_variableVertexIdContaining___NEW
        else:
            return favouritePath, {}



    def treeExpander__equationJoins(self):
        #
        # if set(wantedVariableVertexIds).intersection(set(newPath)) == set(wantedVariableVertexIds): # we already hit all the wanted Variables
        #     print('found!'); import pdb;pdb.set_trace()
        #     favouritePath = newPath; break
        #

        #on the second equationVertexId, union all the variables of both equationsTogether to form a NEW equationVertexId{track this}
        #add the NEW equationVertexId to self.equationVariables_bg
        #childDict['current'] need to jump to the NEW equationVertexId
        #{neighbour in equationVertexId__tuple_variableVertexIdContaining} is to check if neighbour is an equation
        if len(newPath) > 2 and neighbour in allEquationVertexIds:#equationVertexId__tuple_variableVertexIdContaining: #this means we have 1equation, 1variable ending the path and neighbour is the next equation
            


            # print('newPath: ', newPath)
            equationVertexId0, variableVertexIdToEliminate, equationVertexId1 = newPath[-3:]
            # print('equationVertexId0', equationVertexId0)
            # equation0VariableIds = equationVertexId__tuple_variableVertexIdContaining[equationVertexId0]
            # equation1VariableIds = equationVertexId__tuple_variableVertexIdContaining[equationVertexId1]
            # newEquationVariableIds = set(equation0VariableIds).union(set(equation1VariableIds)) - set([variableVertexIdToEliminate])
            



            #we need to update the variableCount
            variableCount = copy(current___dict['variableCount'])
            tuple_variableVertexIdContaining = equationVertexId__tuple_variableVertexIdContaining[neighbour]
            for variableVertexId, count in current___dict['variableCount'].items():
                if variableVertexId != variableVertexIdToEliminate:
                    if variableVertexId in tuple_variableVertexIdContaining:
                        variableCount[variableVertexId] += 1
                    # else:
                    #     variableCount[variableVertexId] = 1
                else:
                    variableCount[variableVertexId] -= 1
                    if variableCount[variableVertexId] == 0:
                        del variableCount[variableVertexId]
            for newVariableVertexId in set(tuple_variableVertexIdContaining) - set(current___dict['variableCount'].keys()):
                if newVariableVertexId != variableVertexIdToEliminate:
                    variableCount[newVariableVertexId] = 1
            childDict['variableCount'] = variableCount


            tuple_variableVertexIdContaining = tuple(sorted(variableCount.keys()))
            #add newEquationVariableIds into the 
            # print('tuple_variableVertexIdContaining__equationVertexId')
            # print(tuple_variableVertexIdContaining__equationVertexId); import pdb;pdb.set_trace()
            # print('tuple_variableVertexIdContaining', tuple_variableVertexIdContaining)
            # print('tuple_variableVertexIdContaining__equationVertexId', tuple_variableVertexIdContaining__equationVertexId)
            # import pdb;pdb.set_trace()
            if tuple_variableVertexIdContaining not in tuple_variableVertexIdContaining__equationVertexId: # this prevents infiniteLoop, but it is not working<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                newEquationId, newEquationVertexId = equationVertexIdIssuer.getNewEquationIdAndEquationVertexId()
                allEquationVertexIds.append(newEquationVertexId)
                tuple_variableVertexIdContaining__equationVertexId[tuple_variableVertexIdContaining] = newEquationVertexId
                equationVertexId__tuple_variableVertexIdContaining[newEquationVertexId] = tuple_variableVertexIdContaining
                #graph update. update the new equation, also update its neighbours
                equationNeighbourIds = list(set(tuple_variableVertexIdContaining)-set(wantedVariableVertexIds))
                self.equationVariables_bg[newEquationVertexId] = equationNeighbourIds
                for variableId in equationNeighbourIds:
                    self.equationVariables_bg[variableId].append(newEquationVertexId)
                #
                self.vertexId__equationVariableId[newEquationVertexId] = newEquationId
                self.equationId__vertexId[newEquationId] = newEquationVertexId
                self.type__list_vertexIds[self.equationKey].append(newEquationVertexId)
                equationVertexId__tuple_variableVertexIdContaining___NEW[newEquationVertexId] = tuple_variableVertexIdContaining
            else:
                newEquationVertexId = tuple_variableVertexIdContaining__equationVertexId[tuple_variableVertexIdContaining]
            childDict['current'] = newEquationVertexId

            # print('self.equationVariables_bg', self.equationVariables_bg)
            #



    def init__groupEquationsBySimilarity(self):
        """
        #group the equations by similarity (this was working well when we wanted to find the resistorSumFormulas for series2Resistor & parallel2Resistor)
        # we might want to put heuristics in classes, and then turn them on and off as per experience(neuralnetwork?), since this might be a special case(over_trained_heuristic)?

        """
        list_equationStrs = list(map(lambda equation: equation.schemeStr, self.list_equations))

        def getEntitiesOfPattern(patternStr):
            parser = Schemeparser(equationStr=patternStr)
            ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
            stack = [parser.rootOfTree]; nodeId__label = {}
            while len(stack) > 0:
                current = stack.pop()
                nodeId__label[current[1]] = current[0]
                children = ast.get(current, [])
                stack += children
            entities = []
            for startPos, nodeId in startPos__nodeId.items():
                l = len(nodeId__label[nodeId])
                entities.append((startPos, startPos+l))
            return entities, functionsD, variablesD, primitives, totalNodeCount
        #
        idx__entities = {}; 
        # idx__functions = {}; idx__variables = {}; idx__primitives = {} # more complex divisors of cutoff, can be devised...later<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        idx__divisorOfCutOff = {} # for now, we use a simple divisorOfCutOff
        for idx, schemeStr in enumerate(list_equationStrs):
            entities, functions, variables, primitives, totalNodeCount = getEntitiesOfPattern(schemeStr)
            idx__entities[idx] = entities
            # idx__functions[idx] = functions
            # idx__primitives[idx] = primitives
            # idx__variables[idx] = variables
            idx__divisorOfCutOff[idx] = totalNodeCount + 0.0 # to make it float
        #
        from foundation.automat.common.stringcompare import StringCompare
        tuple_comparisonIdx__score = {}
        for idx0, schemeStr0 in enumerate(list_equationStrs):
            for idx1, schemeStr1 in enumerate(list_equationStrs[idx0+1:]):
                idx1 += idx0+1
                tuple_comparisonIdx__score[(idx0, idx1)] = StringCompare.damerauLevenschsteinMimickWithEntities( # this could be altered to give scores more suitable for the set of equations
                    schemeStr0, schemeStr1, idx__entities[idx0], idx__entities[idx1]) / (idx__divisorOfCutOff[idx0]+idx__divisorOfCutOff[idx1])
        cutoffScore = 0.34#hardcode for now... there must be someway to parametrise this? neuralnetwork? BTW, this is a score, of how equation look alike
        from foundation.automat.common.unionfindbyrankwithpathcompression import UnionFindByRankWithPathCompression
        self.uf = UnionFindByRankWithPathCompression(len(list_equationStrs))
        for (idx0, idx1), score in tuple_comparisonIdx__score.items():
            if score < cutoffScore:
                self.uf.union(idx0, idx1)
        #use uf to give high priority if adjacent equations are in the same union.
        #convert groupings to vertexId
        verticesIdGroupings = []
        for group in self.uf.grouping():
            verticesIdGroupings.append(list(map(lambda equationId: self.equationId__vertexId[equationId], group)))

    def init__countNoOfTimesVarAppear(self):
        """
        dependsOn@init__groupEquationsBySimilarity
        #within the same group of equations, there are same variables between all the equations, give each variable a count of the number of times they appear. when choosing a variable to subtitute away, choose the one that appears the least... #this heuristic was (this was working well when we wanted to find the resistorSumFormulas for series2Resistor & parallel2Resistor)
        """
        def updateCountDict(d0, d1):
            """d0&d1 are dictionaries from string to integer"""
            commonKeys = set(d0.keys()).intersection(set(d1.keys()))
            d0UniqueKeys = set(d0.keys()) - commonKeys
            d1UniqueKeys = set(d1.keys()) - commonKeys
            allUniqueKeys = d0UniqueKeys.union(d1UniqueKeys)
            d2 = copy(d0)
            d2.update(d1)
            groupTotalVariableCount = dict(filter(lambda t: t[0] in allUniqueKeys, d2.items()))
            for commonKey in commonKeys:
                groupTotalVariableCount[commonKey] = d0[commonKey] + d1[commonKey]
            return groupTotalVariableCount

        ufGroupIdx__groupTotalVariableCount = {}
        for group in uf.grouping():
            groupTotalVariableCount = {}
            for equationIdx in group:
                equation = self.list_equations[equationIdx]
                groupTotalVariableCount = updateCountDict(groupTotalVariableCount, equation.variables)
            groupTotalVariableCount = dict(map(lambda t: (self.list_variables.index(t[0]), t[1]), groupTotalVariableCount.items()))
            ufGroupIdx = uf.find(equationIdx)
            ufGroupIdx__groupTotalVariableCount[ufGroupIdx] = groupTotalVariableCount
            # import pdb;pdb.set_trace()
        #

    def init__idIssuer(self):
        """"""

        class EquationVertexIdIssuer:
            def __init__(self, currentMaxEquationId, currentMaxEquationVertexId):
                self.currentMaxEquationId = currentMaxEquationId
                self.currentMaxEquationVertexId = currentMaxEquationVertexId
            def getNewEquationIdAndEquationVertexId(self):
                self.currentMaxEquationId += 1; self.currentMaxEquationVertexId += 1
                return self.currentMaxEquationId, self.currentMaxEquationVertexId

        currentMaxEquationId = len(self.list_equations)-1; currentMaxEquationVertexId = max(list(self.equationId__vertexId.values())+list(self.variableId__vertexId.values()))
        # import pdb;pdb.set_trace()
        # print('currentMaxEquationVertexId', currentMaxEquationVertexId)
        self.equationVertexIdIssuer = EquationVertexIdIssuer(currentMaxEquationId, currentMaxEquationVertexId)

        self.tuple_variableVertexIdContaining__equationVertexId = {}#for checking duplicates
        self.equationVertexId__tuple_variableVertexIdContaining = {}
        for equationVertexId in self.equationId__vertexId.values():
            tuple_variableVertexIdContaining = tuple(sorted(self.equationVariables_bg[equationVertexId]))
            self.tuple_variableVertexIdContaining__equationVertexId[tuple_variableVertexIdContaining] = equationVertexId
            self.equationVertexId__tuple_variableVertexIdContaining[equationVertexId] = tuple_variableVertexIdContaining
        # if bipartiteTreeExpand:
        #     equationVertexId__tuple_variableVertexIdContaining___NEW = {} # for user easy returns

    def init__valuesForHeuristics(self):
        self.allVariableVertexIds = list(map(lambda variableId: self.variableId__vertexId[variableId], range(0, len(self.list_variables))))
        self.wantedVariableVertexIds = list(map(lambda variableId: self.variableId__vertexId[variableId], [self.dependentVariableId]+self.list_independentVariableIds))
        self.unwantedVariableVertexIds = list(set(self.allVariableVertexIds) - set(self.wantedVariableVertexIds))
        self.allEquationVertexIds = list(map(lambda equationId: self.equationId__vertexId[equationId], range(0, len(self.list_equations))))
        self.originalEquationVertexIds = copy(self.allEquationVertexIds)
        #remove wantedVariableVertexIds
        equationVariables_bg___noWantedVariableVertexIds = {}
        for parentVertexId, childVertexIds in self.equationVariables_bg.items():
            if parentVertexId not in wantedVariableVertexIds:
                filteredChildVertexIds = []
                for childVertexId in childVertexIds:
                    if childVertexId not in wantedVariableVertexIds:
                        filteredChildVertexIds.append(childVertexId)
                equationVariables_bg___noWantedVariableVertexIds[parentVertexId] = filteredChildVertexIds
        self.equationVariables_bg = equationVariables_bg___noWantedVariableVertexIds


    def init__findStartingNodes(self): #if multiprocessing was possible, then we can have multiple startingPoints<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
 #finding a startNode, maybe start with the most number of unwanted variable...
        """
        maxEquationVertexId = None;maxTotalCount = -1
        wantedVariables = list(map(lambda variableId: self.variableId__vertexId[variableId], [self.dependentVariableId]+self.list_independentVariableIds))
        unwantedVariables = list(map(lambda variableId: self.variableId__vertexId[variableId], set(range(0, len(self.list_variables))) - set(wantedVariables)))
        # print('unwantedVariables: ', unwantedVariables)
        for equationId, equation in enumerate(self.list_equations):
            # variables__count = equation.variablesScheme; 
            variables__count = dict(map(lambda n: (n, 1), self.equationVariables_bg[self.equationId__vertexId[equationId]]))#it has to have only 1 count, otherwise it will not work?
            totalWantedVariableCount = 0
            # print('variables__count: ', variables__count)
            # for wantedVariable in set(variables__count.keys()).intersection(set(wantedVariables)):
            # for unwantedVariable in set(variables__count.keys()).intersection(unwantedVariables):
            #     # totalWantedVariableCount += variables__count[wantedVariable]
            #     totalWantedVariableCount += variables__count[unwantedVariable]
            totalWantedVariableCount = len(set(variables__count.keys()).intersection(unwantedVariables))
            # print('equationId: ', equationId, 'variables__count', variables__count, 'totalWantedVariableCount', totalWantedVariableCount, 'maxTotalCount: ', maxTotalCount)
            if totalWantedVariableCount > maxTotalCount:
                maxTotalCount = totalWantedVariableCount; maxEquationVertexId = self.equationId__vertexId[equationId]

    def sortingEquationHeuristics__similarNeighboursExploredFirst(self, vertexIdx, path):
        key = 0
        if vertexIdx in unwantedVariableVertexIds:
            key += 10*self.LOW_WEIGHTS # we want this to be higher than 
            eq0VertexId = path[-1]
            if eq0VertexId in originalEquationVertexIds:
                groupTotalVariableCount = ufGroupIdx__groupTotalVariableCount[uf.find(self.vertexId__equationVariableId[eq0VertexId])]
                if self.vertexId__equationVariableId[vertexIdx] in groupTotalVariableCount:
                    variableCountInGroup = groupTotalVariableCount[self.vertexId__equationVariableId[vertexIdx]]
                    key += (variableCountInGroup/sum(groupTotalVariableCount.values())) * self.LOW_WEIGHTS
        else:
            key += 10*self.HIGH_WEIGHTS
        #find previous group of equation in uf, rank by group_variable_occurence#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        return key

    def sortingVariableHeuristics__similarNeighboursExploredFirst(self, vertexIdx, path):
        key = 0
        if vertexIdx in originalEquationVertexIds:
            key += 10*self.LOW_WEIGHTS
            # print('checking: ', path[-2], vertexIdx, 'same group?: ', path[-2] != vertexIdx and uf.together(self.vertexId__equationVariableId[path[-2]], self.vertexId__equationVariableId[vertexIdx]))
            # print(path[-2], vertexIdx, '<<<<<these should be vertexIdx')
            if path[-2] in originalEquationVertexIds:
                if path[-2] != vertexIdx and uf.together(self.vertexId__equationVariableId[path[-2]], self.vertexId__equationVariableId[vertexIdx]):
                    key+= self.LOW_WEIGHTS
                else:
                    key+= self.HIGH_WEIGHTS
        else:
            key += 10*self.HIGH_WEIGHTS
        #find previous group of equation in uf, if neighbour in the group, give higher priority#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        return key

    def stateRankingHeuristics__originalEquationsPriority(self, childDictPriority):
        """
        Higher points for using original Equations, instead of expanded ones.

        This was good for 2 element circuits...
        """

        childDictPriority += self.HIGH_WEIGHTS if neighbour in unwantedVariableVertexIds or neighbour in allEquationVertexIds else self.LOW_WEIGHTS
                        
        return childDictPriority

    def stateRankingHeuristics__followSortedHeuristics(self, childDictPriority):
        """
        We should try to make the states follow the sorted order

        This was good for 2 element circuits...
        """

        childDictPriority += childDictPriority - orderOfExploration if neighbour in unwantedVariableVertexIds else childDictPriority # do not subtract orderofExploration if it is a equation
        #
        return childDictPriority

    def stateRankingHeuristics__longerPathPriority(self, childDictPriority):
        """
        Higher points for states with longerPaths

        This was good for 2 elements circuits...
        """
        childDictPriority += PATHLENGTH_FACTOR * len(childDict['path']) # should continue on the longest path, and not jump other timeframe of shorter path,  and then at some point in the history go for the shorter path first, when most of the original equations are exhausted?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        return childDictPriority

    def stateRankingHeuristics__preventIncreaseInUnwantedVariables(self, childDictPriority):
        """
        If we have to add unwantedVariables, we deduct points....

        This was good for 2 elements circuits...
        """
        childDictPriority += WANTEDVARIABLE_PENALTY if neighbour in wantedVariableVertexIds else 0 # because this means we will substitute the wanted variable away
        return childDictPriority


    def stateRankingHeuristics__preventUsingEquationWithManyUnwantedVariables(self, childDictPriority):
        """
        Less points for states that use equations with many unwanted variables
        """
        if neighbour in allEquationVertexIds: #if it is an equation
            variableVertexIds = list(equationVertexId__tuple_variableVertexIdContaining[neighbour]) # this is not a good way to get the containing_variables, because, we removed the variables from self.equationVariables_bg
            eliminatedVariableVertexId = childDict['path'][-2]
            # print('neighbour', neighbour)
            # print('variableVertexIds: ', variableVertexIds)
            for variableVertexId in variableVertexIds:
                if variableVertexId != eliminatedVariableVertexId: #ignore the variable that will be eliminated
                    if variableVertexId in wantedVariableVertexIds:
                        # print('wanted added: ', INCREASE_IN_WANTED_VARIABLE_PENALTY, 'to', childDictPriority, '=', childDictPriority+INCREASE_IN_WANTED_VARIABLE_PENALTY)
                        childDictPriority += INCREASE_IN_WANTED_VARIABLE_PENALTY
                    else: # it is unwanted
                        # print('unwanted added: ', INCREASE_IN_UNWANTED_VARIABLE_PENALTY, 'to', childDictPriority, '=', childDictPriority+INCREASE_IN_UNWANTED_VARIABLE_PENALTY)
                        childDictPriority += INCREASE_IN_UNWANTED_VARIABLE_PENALTY
        return childDictPriority

    def stateRankingHeuristics__linearityCondition(self, childDictPriority):
        """
        If we try to substitute away a variable, that appears more than once, then heavy penalty
        this is because we are not able to do simplify, for variables that appears more than once

        Actually this condition would mean that Cramers|GaussianElimination will give good heuristics
        """

        if neighbour in allVariableVertexIds and childDict['variableCount'].get(neighbour, 0) > 1:
            childDictPriority += TRYING_TO_ELIMINATE_VARIABLE_WITH_MORE_THAN_ONE_COUNT_PENALTY
        return childDictPriority

    def stateRankingHeuristics__chooseLeastAppearedVariableOfEquationGroup(self, childDictPriority):
        """
        #within the same group of equations, there are same variables between all the equations, 
        give each variable a count of the number of times they appear. when choosing a variable to subtitute away, 
        choose the one that appears the least... 
        
        #this heuristic was (this was working well when we wanted to find the resistorSumFormulas for series2Resistor & parallel2Resistor)
        """
        if len(newPath) > 2 and neighbour in allEquationVertexIds and (set(originalEquationVertexIds) >= set(newPath[::2])):#does not contain any equationVertexId, that nonoriginal<<<<<<
            #within the same group of equations, there are same variables between all the equations, give each variable a count of the number of times they appear. when choosing a variable to subtitute away, choose the one that appears the least... #this heuristic was (this was working well when we wanted to find the resistorSumFormulas for series2Resistor & parallel2Resistor)
            variableIdx = self.vertexId__equationVariableId[newPath[-2]] # you want all the previous equations
            previousEquationIdx = self.vertexId__equationVariableId[newPath[-1]]
            ufGroupIdx = uf.find(previousEquationIdx)
            # variableIdx = self.vertexId__equationVariableId[newPath[-2]]
            # print("ufGroupIdx__groupTotalVariableCount", ufGroupIdx__groupTotalVariableCount); import pdb;pdb.set_trace()
            if variableIdx in ufGroupIdx__groupTotalVariableCount[ufGroupIdx]:
                groupTotalVariableCount = ufGroupIdx__groupTotalVariableCount[ufGroupIdx]
                variableCount = groupTotalVariableCount[variableIdx]
                totalVariableCountInGroup = sum(map(lambda t: t[1], groupTotalVariableCount.items()))
                penaltyAmt = SAME_EQUATION_GROUP_VARIABLE_COUNT_REWARD * ((totalVariableCountInGroup - variableCount)/(totalVariableCountInGroup*len(newPath))) # the more of the same variable in the same equation_group, the higher the penalty...
                childDictPriority += penaltyAmt
        return childDictPriority

    def stateRankingHeuristics__chooseEquationsFromEquationGroup(self, childDictPriority):
        """
        #SAME_EQUATION_GROUP_REWARDS, we want similiar equations(odd_index on path) to be processed together...

        """

        def is_contiguous_sublist(sublist, mainlist):
            n = len(mainlist)
            m = len(sublist)
            if m > n:
                return False
            for i in range(n - m + 1):
                if mainlist[i:i+m] == sublist:
                    return True
            return False
        #
        equationVertexIdList = newPath[::2]
        for equationVertexIdGroupList in verticesIdGroupings:
            # if equationVertexIdGroupList <= equationVertexIdList: # <= means subList, so both the order and content has to match before this is true
            if is_contiguous_sublist(equationVertexIdGroupList, equationVertexIdList):
                rewardAmt = SAME_EQUATION_GROUP_REWARDS * len(equationVertexIdGroupList)
                childDictPriority += rewardAmt # please note that we might repeat this reward more than once for the same criteria<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        return childDictPriority

    def stateRankingHeuristics__penaliseUseOfNewEquation(self, childDictPriority):
        """
        """

        if bipartiteTreeExpand:
            childDictPriority += NEWEQUATION_PENALTY if neighbour in equationVertexId__tuple_variableVertexIdContaining___NEW else 0
        return childDictPriority