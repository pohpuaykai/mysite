from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class KVLEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def findEquations(self):
        #requires the polarity of each edge
        list_equationVars = []
        # print('KVL directedCycles:', EquationFinder.directedCycles)
        for directedCycle___OG in EquationFinder.directedCycles:
            # print(directedCycle)
            #skip wires by filtering them out
            directedCycle = list(filter(lambda nodeId: self.id__type[nodeId] != 'wire', directedCycle___OG))
            # print('filteredDirectedCycle', directedCycle)
            startNode = directedCycle[0]
            list_vars = []
            for idx in range(1, len(directedCycle)):
                endNode = directedCycle[idx]
                # directedEdge = (startNode, endNode); 
                componentType = self.id__type[startNode]
                variable = EquationFinder.getVariable('voltage', componentType, startNode)
                #get the original directedEdge in directedCycle___OG, to be used in self.componentDirectionPositive
                startIdxOnOGCycle = directedCycle___OG.index(startNode); endIdxOnOGCycle = directedCycle___OG.index(endNode);
                if startIdxOnOGCycle < endIdxOnOGCycle:
                    directedEdge = (startNode, directedCycle___OG[startIdxOnOGCycle+1])
                else: #startIdxOnOGCycle > endIdxOnOGCycle
                    directedEdge = (directedCycle___OG[startIdxOnOGCycle-1], startNode)
                list_vars.append({'varStr':variable, 'positive':self.componentDirectionPositive(directedEdge)})#add positive Voltage variable
                self.addVariableToComponentIdx(startNode, variable)

                # if directedEdge in self.id__positiveLeadsDirections[startNode]:
                #     list_vars.append({'varStr':variable, 'positive':True})#add positive Voltage variable
                #     self.addVariableToComponentIdx(startNode, variable)
                # else:
                #     list_vars.append({'varStr':variable, 'positive':False})#add negative Voltage variable
                #     self.addVariableToComponentIdx(startNode, variable)
                startNode = endNode
            list_equationVars.append(list_vars)
        #convert equationVars to list_equations and store in parent
        for list_vars in list_equationVars:
            self.sumOfPositiveNegativeToLatexAndScheme(list_vars, {'varStr':'0', 'positive':True})
        return self.list_equations