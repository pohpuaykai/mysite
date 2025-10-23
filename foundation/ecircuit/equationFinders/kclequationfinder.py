from copy import copy

from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class KCLEquationFinder(EquationFinder):
    equationFinderDisplayName = "Kirchhoff Current Law"
    usageTags = ['all']

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def findEquations(self):
        """

        """
        nonWireNodeIdsDeg2 = list(filter(lambda nodeId: self.id__type[nodeId] not in ['wire'], self.list_nodeIds___deg2))
        # print('nonWireNodeIdsDeg2', nonWireNodeIdsDeg2)
        visitedSubgraph = {}#this a subgraph of visiteddeg2NodeId, so that we can make sure that it does not form a cycle, so that we can get linearly independent formulas<<<<<<<
        visitedUndirectedEdges = set() # undirected because = is bidirectional
        for deg2NodeId in nonWireNodeIdsDeg2:
            # print('deg2NodeId: ', deg2NodeId, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            #find immediateNeighbours that are not wireNodes...BFS?
            queue = [deg2NodeId]; immediateNeighboursNonWires = set(); immediateVisited = set()
            while len(queue) > 0:
                nodeId = queue.pop(0) # please use append to make a queue
                immediateVisited.add(nodeId)
                for cNodeId in self.networkGraph[nodeId]:
                    if self.id__type[cNodeId] in ['wire']:
                        if cNodeId not in immediateVisited:
                            queue.append(cNodeId)
                    elif deg2NodeId != cNodeId:
                        immediateNeighboursNonWires.add(cNodeId)
                        # print(immediateNeighboursNonWires)
                        # import pdb;pdb.set_trace()
            #
            #form the current_edge_equations
            for neighbour in immediateNeighboursNonWires:
                if (deg2NodeId, neighbour) in visitedUndirectedEdges or (neighbour, deg2NodeId) in visitedUndirectedEdges:
                    continue
                visitedUndirectedEdges.add((deg2NodeId, neighbour))
                #to make sure that we are not forming a cycle, so that we can get linearly independent formulas
                # print('making sure we will not formCycle')
                visitedNodes = set()
                stack = [deg2NodeId]; willFormCycle = False; subVisited = set()
                while len(stack) > 0:
                    nodeId = stack.pop() # please use append to make it a stack
                    subVisited.add(nodeId)
                    for cNodeId in visitedSubgraph.get(nodeId, []):
                        if cNodeId == neighbour: #this means we will form a cycle
                            willFormCycle = True
                            break
                    for cNodeId in set(visitedSubgraph.get(nodeId, [])) - subVisited:  #this will mess up DFS order... does order really matter here?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        stack.append(cNodeId)
                # print('checking if ', (deg2NodeId, neighbour), 'will form a cycle... in visitedSubgraph')
                # print('visitedSubgraph: ', visitedSubgraph)
                # print('willFormCycle: ', willFormCycle)
                # import pdb;pdb.set_trace()
                if not willFormCycle:
                    neighbours = visitedSubgraph.get(deg2NodeId, []); neighbours.append(neighbour); visitedSubgraph[deg2NodeId] = neighbours
                    neighbours = visitedSubgraph.get(neighbour, []); neighbours.append(deg2NodeId); visitedSubgraph[neighbour] = neighbours
                    #add the equations
                    componentType = self.id__type[deg2NodeId]
                    variable0___nc0 = EquationFinder.getVariable('current', componentType, deg2NodeId)
                    self.addVariableToComponentIdx(deg2NodeId, variable0___nc0)

                    componentType = self.id__type[neighbour]
                    variable1___nc0 = EquationFinder.getVariable('current', componentType, neighbour)
                    self.addVariableToComponentIdx(neighbour, variable1___nc0)

                    latexStr = f'{variable0___nc0}={variable1___nc0}'
                    # print('0latexStr: ', latexStr)
                    associatedComponentIdList = [[deg2NodeId, neighbour]]
                    self.addLatexStrAsEquation(latexStr, associatedComponentIdList)
                # import pdb;pdb.set_trace()
                #



        list_equationVars = []; 
        # visitedUndirected = set()
        visitedUndirectedSuperNodes = set()
        #kirchoff_current_law components on directedEdges going into the startSuperNodeId are positive_variable, components on directedEdges that are going out of the startSuperNodeId are negative_variable
        for startSuperNodeId in self.superNodeIds:
            #find components
            #
            associatedComponentIdList = []
            list_vars = []
            # print('self.superNodeUndirectedGraph: ', self.superNodeUndirectedGraph); import pdb;pdb.set_trace()
            for endSuperNodeId in self.superNodeUndirectedGraph[startSuperNodeId]:
                if (startSuperNodeId, endSuperNodeId) in visitedUndirectedSuperNodes:
                    continue
                else:
                    visitedUndirectedSuperNodes.add((startSuperNodeId, endSuperNodeId))
                    visitedUndirectedSuperNodes.add((endSuperNodeId, startSuperNodeId))
                list_directedPath = self.tuple_startSuperNodeId_endSuperNodeId__list_path.get((startSuperNodeId, endSuperNodeId), self.tuple_startSuperNodeId_endSuperNodeId__list_path.get((endSuperNodeId, startSuperNodeId)))
                for directedPath in list_directedPath: #all the components on this directedPath are ALL_positive or ALL_negative
                    # import pdb;pdb.set_trace()
                    # associatedComponentIdList.append([startSuperNodeId]+list(directedPath)+[endSuperNodeId])
                    # print('startSuperNodeId: ', startSuperNodeId)
                    # print('directedPath: ', directedPath)
                    # print('endSuperNodeId: ', endSuperNodeId)

                    # import pdb;pdb.set_trace()
                    directedEdge = (startSuperNodeId, directedPath[0])
                    isPositive = directedEdge in self.directedEdges
                    # print('directedEdge', directedEdge); import pdb;pdb.set_trace()
                    #find all nonwire components
                    alreadyAddedThisPath = False
                    visited = set()
                    for componentId in filter(lambda nodeId: self.id__type[nodeId] not in ['wire'], directedPath):
                        if componentId in visited:
                            continue
                        if not alreadyAddedThisPath: # this is placed here so that we get the componentId duplicate check
                            alreadyAddedThisPath = True
                            #check if the last node of the directedPath is a wireNode, if so remove the last node from directedPath, because wire is not calculated in Lumped Matter Discipline
                            # pathToAdd = list(copy(directedPath))
                            pathToAdd = []
                            #remove all the wireNode starting from the end of the pathToAdd
                            for nodeId in reversed(directedPath):
                                if self.id__type[nodeId] not in ['wire']:
                                    pathToAdd.insert(0, nodeId)
                            # if self.id__type[directedPath[-1]] in ['wire']:
                            #     pathToAdd = list(directedPath[:-1])
                            associatedComponentIdList.append([startSuperNodeId]+pathToAdd)
                            #the startSuperNodeId must be a wireNode, and that is where KCL acted on, so we must add it to the associatedComponentIdList, we do not add endSuperNodeId
                        visited.add(componentId)
                        variable = EquationFinder.getVariable('current', self.id__type[componentId], componentId)
                        list_vars.append({'varStr':variable, 'positive':isPositive})#add positive Voltage variable
                        self.addVariableToComponentIdx(componentId, variable)
            if len(list_vars) > 0:
                self.sumOfPositiveNegativeToLatexAndScheme(list_vars, {'varStr':'0', 'positive':True}, associatedComponentIdList)
        return self.list_equations