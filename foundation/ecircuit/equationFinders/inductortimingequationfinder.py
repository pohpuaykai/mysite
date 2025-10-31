from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class InductortimingEquationFinder(EquationFinder):
    equationFinderDisplayName = "Inductor Timing"
    usageTags = ['all']

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def findEquations(self):
        """every inductor will have this first_order_seperable_differential_equation, where 
        equivalent = voltage through inductor
        derivativeMultiplier = inductance of inductor
        differentiand = current of inductor
        differentiator = time
        """

        for componentId, componentType in self.id__type.items():
            if componentType in ['inductor']:
                associatedComponentIdList = [componentId]
                currentVariable = EquationFinder.getVariable('current', componentType, componentId)
                self.addVariableToComponentIdx(componentId, currentVariable)
                inductanceVariable = EquationFinder.getVariable('inductance', componentType, componentId)
                self.addVariableToComponentIdx(componentId, inductanceVariable)
                voltageVariable = EquationFinder.getVariable('voltage', componentType, componentId)
                self.addVariableToComponentIdx(componentId, voltageVariable)
                timeVariable = 't' # TODO standardise? might it have variable collision with other time? more than 1 time? when there is problems with time please check here
                self.addVariableToComponentIdx(componentId, timeVariable)
                self.firstOrderSeperableDifferentialEquation(voltageVariable, inductanceVariable, currentVariable, timeVariable, [associatedComponentIdList])
        return self.list_equations