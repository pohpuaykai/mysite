from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class CapacitortimingEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def findEquations(self):
        """every capacitor will have this first_order_seperable_differential_equation, where 
        equivalent = current through capacitor
        derivativeMultiplier = capacitance of capacitor
        differentiand = voltage of capacitor
        differentiator = time
        """

        for componentId, componentType in self.id__type.items():
            if componentType in ['capacitor']:
                currentVariable = self.getVariable('current', componentType, componentId)
                self.addVariableToComponentIdx(componentId, currentVariable)
                capacitanceVariable = self.getVariable('capacitance', componentType, componentId)
                self.addVariableToComponentIdx(componentId, capacitanceVariable)
                voltageVariable = self.getVariable('voltage', componentType, componentId)
                self.addVariableToComponentIdx(componentId, voltageVariable)
                timeVariable = 't' # TODO standardise? might it have variable collision with other time? more than 1 time? when there is problems with time please check here
                self.firstOrderSeperableDifferentialEquation(currentVariable, capacitanceVariable, voltageVariable, timeVariable)
        return self.list_equations