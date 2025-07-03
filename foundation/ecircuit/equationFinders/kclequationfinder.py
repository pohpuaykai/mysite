from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class KCLEquationFinder(EquationFinder):
    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections):
        super().__init__(networkGraph, id__type)
        self.id__positiveLeadsDirections = id__positiveLeadsDirections

    def findEquations(self):
        """

        """
        added2DegEdges = set()
        for deg2NodeId in self.list_nodeIds___deg2: # need both directions.... the edge not just the node.#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            [neighbour0, neighbour1] = self.networkGraph[deg2NodeId]
            if neighbour0 in self.list_nodeIds___deg2 and (deg2NodeId, neighbour0) not in added2DegEdges:
                #
                added2DegEdges.add((deg2NodeId, neighbour0)); added2DegEdges.add((neighbour0, deg2NodeId))
                #
                componentType = self.id__type[deg2NodeId]
                variable0 = self.getVariable('current', componentType, deg2NodeId)
                self.addVariableToComponentIdx(deg2NodeId, variable0)
                #
                componentType = self.id__type[neighbour0]
                variable1 = self.getVariable('current', componentType, neighbour0)
                self.addVariableToComponentIdx(neighbour0, variable1)
                #add equation
                latexStr = f'{variable0}={variable1}'
                print('latexStr: ', latexStr)
                self.addLatexStrAsEquation(latexStr)
            #
            if neighbour1 in self.list_nodeIds___deg2 and (deg2NodeId, neighbour1) not in added2DegEdges:
                #
                added2DegEdges.add((deg2NodeId, neighbour1)); added2DegEdges.add((neighbour1, deg2NodeId))
                #
                componentType = self.id__type[deg2NodeId]
                variable0 = self.getVariable('current', componentType, deg2NodeId)
                self.addVariableToComponentIdx(deg2NodeId, variable0)
                #
                componentType = self.id__type[neighbour1]
                variable1 = self.getVariable('current', componentType, neighbour1)
                self.addVariableToComponentIdx(neighbour1, variable1)
                #add equation
                latexStr = f'{variable0}={variable1}'
                print('latexStr: ', latexStr)
                self.addLatexStrAsEquation(latexStr)


        list_equationVars = []
        for startSuperNodeId in self.superNodeIds:
            startComponentType = self.id__type[startSuperNodeId]
            list_vars = []
            for endSuperNodeId in self.superNodeUndirectedGraph[startSuperNodeId]:
                endComponentType = self.id__type[endSuperNodeId]
                list_directedPath = self.tuple_startSuperNodeId_endSuperNodeId__list_path[(startSuperNodeId, endSuperNodeId)]
                for directedPath in list_directedPath:
                    #find first non_wire_component
                    selectedComponentId = None; selectedComponentType = None; prevSelectedComponentId = startSuperNodeId
                    for componentId in directedPath:
                        componentType = self.id__type[componentId]
                        if componentType not in ['wire']:
                            selectedComponentId = componentId; selectedComponentType = componentType
                            break
                        prevSelectedComponentId = componentId # this is to find the direction for positiveLeadsDirection
                    if selectedComponentId is not None:
                        directedEdge = (prevSelectedComponentId, selectedComponentId)
                        variable = self.getVariable('current', selectedComponentType, selectedComponentId)
                        if directedEdge in self.id__positiveLeadsDirections[prevSelectedComponentId]:
                            list_vars.append({'varStr':variable, 'positive':True})#add positive Voltage variable
                            self.addVariableToComponentIdx(selectedComponentId, variable)
                        else:
                            list_vars.append({'varStr':variable, 'positive':False})#add negative Voltage variable
                            self.addVariableToComponentIdx(selectedComponentId, variable)
            list_equationVars.append(list_vars)
        #convert equationVars to list_equations and store in parent
        for list_vars in list_equationVars:
            self.sumOfPositiveNegativeToLatexAndScheme(list_vars)


            #find path in this: tuple_startSuperNodeId_endSuperNodeId__list_path
            #take first non-wire component in path, check its +ve direction and add to equation