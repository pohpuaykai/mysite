from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class OhmlawEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections):
        super().__init__(networkGraph, id__type)
        self.id__positiveLeadsDirections = id__positiveLeadsDirections # this is not needed?

    def findEquations(self):
        """
        All components that are not wire|source, will have OhmsLaw
        """
        for componentId, componentType in self.id__type.items():
            if componentType not in ['wire', 'AC_signal_generator', 'battery']:
                resistanceVariable = self.getVariable('resistance', componentType, componentId)
                voltageVariable = self.getVariable('voltage', componentType, componentId)
                currentVariable = self.getVariable('current', componentType, componentId)
                self.simpleRatioToLatexAndScheme(resistanceVariable, voltageVariable, currentVariable)