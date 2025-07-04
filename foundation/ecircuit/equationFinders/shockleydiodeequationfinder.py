from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class ShockleydiodeEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections):
        super().__init__(networkGraph, id__type)
        self.id__positiveLeadsDirections = id__positiveLeadsDirections

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
                diodeCurrentVariable = self.getVariable("current", componentType, componentId)#<<<<<<<
                diode_saturationCurrentVariable = self.getVariable("current", componentType, componentId)#<<<<<<<
                diodeVoltageVariable = self.getVariable("voltage", componentType, componentId)#<<<<<<<
                ideality_factorVariable = self.getVariable("current", componentType, componentId)#<<<<<<<
                boltzmann_constantVariable = self.getConstantVariable("boltzmann_constant")
                charge_of_an_electronVariable = self.getConstantVariable("charge_of_an_electron")
                temperatureVariable = self.getVariable("temperature", componentType, componentId)#<<<<<<<
                temperatureVoltage = self.makeRatio(f'{ideality_factorVariable} {boltzmann_constantVariable} {temperatureVariable}', charge_of_an_electronVariable)
                exponent = self.makeRatio(diodeVoltageVariable, temperatureVoltage)
                self.exponentialMinusOne(diodeCurrentVariable, diode_saturationCurrentVariable, exponent)