from foundation.automat.common.stringcompare import StringCompare
from foundation.automat.parser.sorte.schemeparser import Schemeparser

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
        self.list_equations = list_equations
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
        self.init()

    def init(self):#init should be a class?<<<
        self.init__groupEquationsBySimilarity()
        self.init__countNoOfTimesVarAppear()
        if self.bipartiteTreeExpand:
            self.init__idIssuer()

    def init__groupEquationsBySimilarity(self):
        """
        #group the equations by similarity (this was working well when we wanted to find the resistorSumFormulas for series2Resistor & parallel2Resistor)
        # we might want to put heuristics in classes, and then turn them on and off as per experience(neuralnetwork?), since this might be a special case(over_trained_heuristic)?

        """
        list_equationStrs = list(map(lambda equation: equation.schemeStr, list_equations))

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
        tuple_comparisonIdx__score = {}
        for idx0, schemeStr0 in enumerate(list_equationStrs):
            for idx1, schemeStr1 in enumerate(list_equationStrs[idx0+1:]):
                idx1 += idx0+1
                tuple_comparisonIdx__score[(idx0, idx1)] = StringCompare.damerauLevenschsteinMimickWithEntities( # this could be altered to give scores more suitable for the set of equations
                    schemeStr0, schemeStr1, idx__entities[idx0], idx__entities[idx1]) / (idx__divisorOfCutOff[idx0]+idx__divisorOfCutOff[idx1])
        cutoffScore = 0.34#hardcode for now... there must be someway to parametrise this? neuralnetwork? BTW, this is a score, of how equation look alike
        from foundation.automat.common.unionfindbyrankwithpathcompression import UnionFindByRankWithPathCompression
        uf = UnionFindByRankWithPathCompression(len(list_equationStrs))
        for (idx0, idx1), score in tuple_comparisonIdx__score.items():
            if score < cutoffScore:
                uf.union(idx0, idx1)
        #use uf to give high priority if adjacent equations are in the same union.
        #convert groupings to vertexId
        verticesIdGroupings = []
        for group in uf.grouping():
            verticesIdGroupings.append(list(map(lambda equationId: equationId__vertexId[equationId], group)))

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
                equation = list_equations[equationIdx]
                groupTotalVariableCount = updateCountDict(groupTotalVariableCount, equation.variables)
            groupTotalVariableCount = dict(map(lambda t: (list_variables.index(t[0]), t[1]), groupTotalVariableCount.items()))
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

        currentMaxEquationId = len(list_equations)-1; currentMaxEquationVertexId = max(list(equationId__vertexId.values())+list(variableId__vertexId.values()))
        # import pdb;pdb.set_trace()
        # print('currentMaxEquationVertexId', currentMaxEquationVertexId)
        self.equationVertexIdIssuer = EquationVertexIdIssuer(currentMaxEquationId, currentMaxEquationVertexId)

        self.tuple_variableVertexIdContaining__equationVertexId = {}#for checking duplicates
        self.equationVertexId__tuple_variableVertexIdContaining = {}
        for equationVertexId in equationId__vertexId.values():
            tuple_variableVertexIdContaining = tuple(sorted(equationVariables_bg[equationVertexId]))
            self.tuple_variableVertexIdContaining__equationVertexId[tuple_variableVertexIdContaining] = equationVertexId
            self.equationVertexId__tuple_variableVertexIdContaining[equationVertexId] = tuple_variableVertexIdContaining
        # if bipartiteTreeExpand:
        #     equationVertexId__tuple_variableVertexIdContaining___NEW = {} # for user easy returns