from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class KVLEquationFinder(EquationFinder):
    usageTags = ['all']

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def componentIsPositive(self, componentId):
        return self.id__type[componentId] in ['AC_signal_generator', 'battery']

    def findEquations(self):
        #requires the polarity of each edge
        list_equationVars = []
        print('KVL directedCycles:', EquationFinder.directedCycles)
        for directedCycle___OG in EquationFinder.directedCycles:
            # print(directedCycle)
            #skip wires by filtering them out
            directedCycle = list(filter(lambda nodeId: self.id__type[nodeId] != 'wire', directedCycle___OG))
            visited = set(); list_vars = []
            for componentId in directedCycle:
                if componentId in visited:
                    continue
                visited.add(componentId)
                idxOnOGCycle = directedCycle___OG.index(componentId)
                if idxOnOGCycle == len(directedCycle):
                    directedEdge = (directedCycle___OG[idxOnOGCycle-1], componentId)
                else:
                    directedEdge = (componentId, directedCycle___OG[idxOnOGCycle+1])
                variable = EquationFinder.getVariable('voltage', self.id__type[componentId], componentId)
                #kirchoff_voltage_law: if component gives voltage, then variable is positive, else variable is negative
                list_vars.append({'varStr':variable, 'positive':self.componentIsPositive(componentId)})#add positive Voltage variable
                self.addVariableToComponentIdx(componentId, variable)


            #can have repeated, nodeId if 
            # startNode = nonRepeatingDirectedCycle[0]
            # list_vars = []
            # for idx in range(0, len(nonRepeatingDirectedCycle)): # we assume there always going to be wire between non-wire-components
            #     endNode = directedCycle[idx]
            #     # directedEdge = (startNode, endNode); 
            #     componentType = self.id__type[startNode]
            #     variable = EquationFinder.getVariable('voltage', componentType, startNode)
            #     #get the original directedEdge in directedCycle___OG, to be used in self.componentDirectionPositive
            #     startIdxOnOGCycle = directedCycle___OG.index(startNode); endIdxOnOGCycle = directedCycle___OG.index(endNode);
            #     if startIdxOnOGCycle < endIdxOnOGCycle:
            #         directedEdge = (startNode, directedCycle___OG[startIdxOnOGCycle+1])
            #     else: #startIdxOnOGCycle > endIdxOnOGCycle
            #         startIdxOnOGCycle = startIdxOnOGCycle-2 if startIdxOnOGCycle ==0 else startIdxOnOGCycle-1 # if (startIdxOnOGCycle-1) == the_end_of_directedCycle, startNode==the_end_of_directedCycle, because we repeat the startNode at the endNode of the directedCycle
            #         directedEdge = (directedCycle___OG[startIdxOnOGCycle], startNode)
            #     import pdb;pdb.set_trace()
            #     list_vars.append({'varStr':variable, 'positive':self.componentDirectionPositive(directedEdge)})#add positive Voltage variable
            #     self.addVariableToComponentIdx(startNode, variable)

            #     print('KVL: checking directedEdge: ', directedEdge, ' ?????????????????????????????????')
            #     # if directedEdge in self.id__positiveLeadsDirections[startNode]:
            #     #     list_vars.append({'varStr':variable, 'positive':True})#add positive Voltage variable
            #     #     self.addVariableToComponentIdx(startNode, variable)
            #     # else:
            #     #     list_vars.append({'varStr':variable, 'positive':False})#add negative Voltage variable
            #     #     self.addVariableToComponentIdx(startNode, variable)
            #     startNode = endNode




            list_equationVars.append(list_vars)
            print('list_equationVars: ', list_equationVars)
            # print('filteredDirectedCycle', directedCycle); import pdb;pdb.set_trace()
        #convert equationVars to list_equations and store in parent
        for list_vars in list_equationVars:
            self.sumOfPositiveNegativeToLatexAndScheme(list_vars, {'varStr':'0', 'positive':True})
        return self.list_equations