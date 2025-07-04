from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class KVLEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections):
        super().__init__(networkGraph, id__type)
        self.id__positiveLeadsDirections = id__positiveLeadsDirections

    def findEquations(self):
        #requires the polarity of each edge
        list_equationVars = []
        for directedCycle in self.directedCycles:
            # print(directedCycle)
            #skip wires by filtering them out
            directedCycle = list(filter(lambda nodeId: self.id__type[nodeId] != 'wire', directedCycle))
            # print('filteredDirectedCycle', directedCycle)
            startNode = directedCycle[0]
            list_vars = []
            for idx in range(1, len(directedCycle)):
                endNode = directedCycle[idx]
                directedEdge = (startNode, endNode); componentType = self.id__type[startNode]
                # if componentType in ['wire']:
                #     continue # skip wire.
                variable = self.getVariable('voltage', componentType, startNode)
                if directedEdge in self.id__positiveLeadsDirections[startNode]:
                    list_vars.append({'varStr':variable, 'positive':True})#add positive Voltage variable
                    self.addVariableToComponentIdx(startNode, variable)
                else:
                    list_vars.append({'varStr':variable, 'positive':False})#add negative Voltage variable
                    self.addVariableToComponentIdx(startNode, variable)
                startNode = endNode
            list_equationVars.append(list_vars)
        #convert equationVars to list_equations and store in parent
        for list_vars in list_equationVars:
            self.sumOfPositiveNegativeToLatexAndScheme(list_vars, {'varStr':'0', 'positive':True})