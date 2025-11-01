from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class OhmlawEquationFinder(EquationFinder):
    equationFinderDisplayName = "Ohm Law"
    usageTags = ['all']

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def findEquations(self):
        """
        All components that are not wire|diode|capacitor|inductor, will have OhmsLaw. I feel Shockley is a kind of OhmsLaw, in the derivative?
        """
        for componentId, componentType in self.id__type.items():
            if componentType not in ['wire', 'diode', 'capacitor', 'inductor', 'AC_signal_generator']:
                resistanceVariable = EquationFinder.getVariable('resistance', componentType, componentId)
                self.addVariableToComponentIdx(componentId, resistanceVariable)
                voltageVariable = EquationFinder.getVariable('voltage', componentType, componentId)
                self.addVariableToComponentIdx(componentId, voltageVariable)
                currentVariable = EquationFinder.getVariable('current', componentType, componentId)
                self.addVariableToComponentIdx(componentId, currentVariable)
                associatedComponentIdList = [componentId]
                self.simpleRatioToLatexAndScheme(resistanceVariable, voltageVariable, currentVariable, [associatedComponentIdList])
        return self.list_equations