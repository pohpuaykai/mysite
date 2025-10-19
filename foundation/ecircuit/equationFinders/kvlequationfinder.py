from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class KVLEquationFinder(EquationFinder):
    equationFinderDisplayName = "Kirchhoff Voltage Law"
    usageTags = ['all']

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def componentIsPositive(self, componentId):
        return self.id__type[componentId] in ['AC_signal_generator', 'battery']

    def findEquations(self):
        #requires the polarity of each edge
        list_equationVars = []
        # print('KVL directedCycles:', EquationFinder.directedCycles)
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
            associatedComponentIdList = directedCycle___OG
            self.sumOfPositiveNegativeToLatexAndScheme(list_vars, {'varStr':'0', 'positive':True}, [associatedComponentIdList])

        #     list_equationVars.append(list_vars)
        #     print('list_equationVars: ', list_equationVars)
        #     # print('filteredDirectedCycle', directedCycle); import pdb;pdb.set_trace()
        # #convert equationVars to list_equations and store in parent
        # for list_vars in list_equationVars:
        #     self.sumOfPositiveNegativeToLatexAndScheme(list_vars, {'varStr':'0', 'positive':True}, associatedComponentIdList)
        return self.list_equations