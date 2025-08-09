from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class ShockleydiodeEquationFinder(EquationFinder):
    usageTags = ['all']

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def findEquations(self):
        """
        #current_diode=diode_saturation_current(e^(V_{D}/(nkT/q))-1)
        n is ideality factor aka quality factor aka emission coefficient aka material constant
        k is Boltzmann constant
        T is temperature of the component
        q is charge of an electron

        """
        for componentId, componentType in self.id__type.items():
            if componentType in ['diode']:
                diodeCurrentVariable = EquationFinder.getVariable("current", componentType, componentId)#<<<<<<<
                self.addVariableToComponentIdx(componentId, diodeCurrentVariable)
                diode_saturationCurrentVariable = EquationFinder.getVariable("current", componentType, componentId)#<<<<<<<
                self.addVariableToComponentIdx(componentId, diode_saturationCurrentVariable)
                diodeVoltageVariable = EquationFinder.getVariable("voltage", componentType, componentId)#<<<<<<<
                self.addVariableToComponentIdx(componentId, diodeVoltageVariable)
                ideality_factorVariable = EquationFinder.getVariable("current", componentType, componentId)#<<<<<<<
                self.addVariableToComponentIdx(componentId, ideality_factorVariable)
                boltzmann_constantVariable = self.getConstantVariable("boltzmann_constant")
                charge_of_an_electronVariable = self.getConstantVariable("charge_of_an_electron")
                temperatureVariable = EquationFinder.getVariable("temperature", componentType, componentId)#<<<<<<<
                self.addVariableToComponentIdx(componentId, temperatureVariable)
                temperatureVoltage = self.makeRatio(f'{ideality_factorVariable} {boltzmann_constantVariable} {temperatureVariable}', charge_of_an_electronVariable)
                exponent = self.makeRatio(diodeVoltageVariable, temperatureVoltage)
                self.exponentialMinusOne(diodeCurrentVariable, diode_saturationCurrentVariable, exponent)
        return self.list_equations