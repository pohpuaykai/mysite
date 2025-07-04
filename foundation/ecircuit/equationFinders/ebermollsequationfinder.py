from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class EbermollsEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections):
        super().__init__(networkGraph, id__type)
        self.id__positiveLeadsDirections = id__positiveLeadsDirections

    def findEquations(self):
        """
        #current_emitter=emitter_saturation_current(e^(V_{BE}/(kT/q))-1)
        V_{BE} voltage between Base and Emitter 
        k is Boltzmann constant
        T is temperature of the component
        q is charge of an electron

        """
        for componentId, componentType in self.id__type.items():
            if componentType in ['transistor']:
                emitterCurrentVariable = self.getVariable("current", componentType, componentId)#<<<<<<<
                emitter_saturationCurrentVariable = self.getVariable("current", componentType, componentId)#<<<<<<<
                baseEmitterVoltageVariable = self.getVariable("voltage", componentType, componentId)#<<<<<<<
                boltzmann_constantVariable = self.getConstantVariable("boltzmann_constant")
                charge_of_an_electronVariable = self.getConstantVariable("charge_of_an_electron")
                temperatureVariable = self.getVariable("temperature", componentType, componentId)#<<<<<<<
                temperatureVoltage = self.makeRatio(f'{boltzmann_constantVariable} {temperatureVariable}', charge_of_an_electronVariable)
                exponent = self.makeRatio(baseEmitterVoltageVariable, temperatureVoltage)
                self.exponentialMinusOne(emitterCurrentVariable, emitter_saturationCurrentVariable, exponent)