from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class CompleximpedancesumEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections):
        super().__init__(networkGraph, id__type)
        self.id__positiveLeadsDirections = id__positiveLeadsDirections

    def findEquations(self):
        """
        complex_impedance_sum model # every path|ball that only has linear_components(resistor|capacitor|inductor), 
        parallel<->harmonic_sum(complex_impedance), 
        series<->normal_sum(complex_impedance)
        """
        imaginery_number = self.getConstantVariable('imaginery_number')
        totalVariableIdx = max(list(id__type.keys()))
        for (startSuperNodeId, endSuperNodeId), list_path in self.tuple_startSuperNodeId_endSuperNodeId__list_path:
            nonlinearBall=False#check if every component between startSuperNodeId and endSuperNodeId are only (resistor|capacitor|inductor)
            for directedPath in list_path:
                list_var=[];nonlinearPath=False#check if every component in directedPath are only (resistor|capacitor|inductor)
                for componentId in directedPath:
                    componentType = self.id__type[componentId]
                    if componentType in ['wire', 'battery', 'AC_signal_generator']: #filter out all the wire, source
                        continue
                    if componentType not in ['resistor', 'capacitor', 'inductor']:
                        nonlinearBall = True; nonlinearPath = True
                        break
                    #else add the variables on this path to list_var
                    if componentType in ['resistor']:
                        variable = self.getVariable('resistance', componentType, componentId)
                        list_var.append(variable)
                    elif componentType in ['capacitor']:
                        capacitanceVariable = self.getVariable('capacitance', componentType, componentId)
                        frequencyVariable = self.getVariable('frequency', componentType, componentId)
                        list_var.append(self.makeRatio('1', f'{imaginery_number} {frequencyVariable} {capacitanceVariable}'))
                    elif componentType in ['inductor']:
                        inductanceVariable = self.getVariable('inductance', componentType, componentId)
                        frequencyVariable = self.getVariable('frequency', componentType, componentId)
                        list_var.append(f'{imaginery_number} {frequencyVariable} {inductanceVariable}')
                if not nonlinearPath: # add_normal
                    totalImpedanceVariable = self.getVariable('impedance', 'total', totalVariableIdx)#not a real component<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WHAT ID?
                    totalVariableIdx += 1
                    self.sumOfPositiveNegativeToLatexAndScheme(list_vars, {'varStr':totalImpedanceVariable, 'positive':True})#<<not associated with any
                    latexStrWithEqual = self.sumOfPositiveNegativeToLatexAndScheme(list_vars, {'varStr':'', 'positive':True}, addAsEquation=False) # just to get the imcomplete equation for harmonic_add later
                    latexStr = latexStrWithEqual.replace('=', '')
                    list_equationVars.append({'varStr':latexStr, 'positive':True})#for harmonic_sum
            if not nonlinearBall: #add_harmonic
                totalImpedanceVariable = self.getVariable('impedance', 'total', totalVariableIdx)#not a real component<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WHAT ID?
                totalVariableIdx += 1
                self.sumOfPositiveNegativeToLatexAndScheme(list_equationVars, {'varStr':totalImpedanceVariable, 'positive':True})
