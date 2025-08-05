from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class EbermollsEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

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
                emitterCurrentVariable = EquationFinder.getVariable("current", componentType, componentId)#<<<<<<<
                self.addVariableToComponentIdx(componentId, emitterCurrentVariable)
                emitter_saturationCurrentVariable = EquationFinder.getVariable("current", componentType, componentId)#<<<<<<<
                self.addVariableToComponentIdx(componentId, emitter_saturationCurrentVariable)
                baseEmitterVoltageVariable = EquationFinder.getVariable("voltage", componentType, componentId)#<<<<<<<
                self.addVariableToComponentIdx(componentId, baseEmitterVoltageVariable)
                boltzmann_constantVariable = self.getConstantVariable("boltzmann_constant")
                charge_of_an_electronVariable = self.getConstantVariable("charge_of_an_electron")
                temperatureVariable = EquationFinder.getVariable("temperature", componentType, componentId)#<<<<<<<
                self.addVariableToComponentIdx(componentId, temperatureVariable)
                temperatureVoltage = self.makeRatio(f'{boltzmann_constantVariable} {temperatureVariable}', charge_of_an_electronVariable)
                exponent = self.makeRatio(baseEmitterVoltageVariable, temperatureVoltage)
                self.exponentialMinusOne(emitterCurrentVariable, emitter_saturationCurrentVariable, exponent)
        return self.list_equations