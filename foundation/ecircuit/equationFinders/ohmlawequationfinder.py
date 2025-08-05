from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class OhmlawEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def findEquations(self):
        """
        All components that are not wire|source, will have OhmsLaw
        """
        for componentId, componentType in self.id__type.items():
            if componentType not in ['wire', 'AC_signal_generator', 'battery']:
                resistanceVariable = EquationFinder.getVariable('resistance', componentType, componentId)
                self.addVariableToComponentIdx(componentId, resistanceVariable)
                voltageVariable = EquationFinder.getVariable('voltage', componentType, componentId)
                self.addVariableToComponentIdx(componentId, voltageVariable)
                currentVariable = EquationFinder.getVariable('current', componentType, componentId)
                self.addVariableToComponentIdx(componentId, currentVariable)
                self.simpleRatioToLatexAndScheme(resistanceVariable, voltageVariable, currentVariable)
        return self.list_equations