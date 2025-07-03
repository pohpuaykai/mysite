from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class InductortimingEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections):
        super().__init__(networkGraph, id__type)
        self.id__positiveLeadsDirections = id__positiveLeadsDirections

    def findEquations(self):
        """every inductor will have this first_order_seperable_differential_equation, where 
        equivalent = voltage through inductor
        derivativeMultiplier = inductance of inductor
        differentiand = current of inductor
        differentiator = time
        """

        for componentId, componentType in self.id__type.items():
            if componentType in ['capacitor']:
                currentVariable = self.getVariable('current', componentType, componentId)
                inductanceVariable = self.getVariable('inductance', componentType, componentId)
                voltageVariable = self.getVariable('voltage', componentType, componentId)
                timeVariable = 't' # TODO standardise? might it have variable collision with other time? more than 1 time? when there is problems with time please check here
                self.firstOrderSeperableDifferentialEquation(voltageVariable, inductanceVariable, currentVariable, timeVariable)