from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class CompleximpedancesumEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        super().__init__(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices)

    def findEquations(self):
        """
        complex_impedance_sum model # every path|ball that only has linear_components(resistor|capacitor|inductor), 
        parallel<->harmonic_sum(complex_impedance), 
        series<->normal_sum(complex_impedance)
        """
        imaginery_number = self.getConstantVariable('imaginery_number')
        totalVariableIdx = max(list(self.id__type.keys())) + 1
        

        visitedUndirected = set()
        for (startSuperNodeId, endSuperNodeId), list_path in self.tuple_startSuperNodeId_endSuperNodeId__list_path.items():
            if (startSuperNodeId, endSuperNodeId) in visitedUndirected:
                continue
            visitedUndirected.add((startSuperNodeId, endSuperNodeId));visitedUndirected.add((endSuperNodeId, startSuperNodeId))
            nonlinearBall=False;list_equationVars = []#check if every component between startSuperNodeId and endSuperNodeId are only (resistor|capacitor|inductor)
            for directedPath in list_path:
                nonlinearPath=False; list_var=[]#check if every component in directedPath are only (resistor|capacitor|inductor)
                for pathId, componentId in enumerate(directedPath):
                    componentType = self.id__type[componentId]
                    if componentType in ['wire', 'battery', 'AC_signal_generator']: #filter out all the wire, source
                        continue
                    if componentType not in ['resistor', 'capacitor', 'inductor']:
                        nonlinearBall = True; nonlinearPath = True
                        break
                    #else add the variables on this path to list_var
                    # if pathId
                    # if directedEdge in self.id__positiveLeadsDirections[startNode]: # directedEdge are in solderableLeadsIdx... needs a edge__solderableIndicesTuple
                    if pathId == 0:
                        directedEdge = (startSuperNodeId, componentId)
                    else:
                        directedEdge = (directedPath[pathId-1], componentId)
                    if componentType in ['resistor']:
                        variable = EquationFinder.getVariable('resistance', componentType, componentId)
                        self.addVariableToComponentIdx(componentId, variable)
                        list_var.append({'varStr':variable, 'positive':self.componentDirectionPositive(directedEdge)})
                    elif componentType in ['capacitor']:
                        capacitanceVariable = EquationFinder.getVariable('capacitance', componentType, componentId)
                        self.addVariableToComponentIdx(componentId, capacitanceVariable)
                        frequencyVariable = EquationFinder.getVariable('frequency', componentType, componentId)
                        self.addVariableToComponentIdx(componentId, frequencyVariable)
                        variable = self.makeRatio('1', f'{imaginery_number} {frequencyVariable} {capacitanceVariable}')
                        list_var.append({'varStr':variable, 'positive':self.componentDirectionPositive(directedEdge)})
                    elif componentType in ['inductor']:
                        inductanceVariable = EquationFinder.getVariable('inductance', componentType, componentId)
                        self.addVariableToComponentIdx(componentId, inductanceVariable)
                        frequencyVariable = EquationFinder.getVariable('frequency', componentType, componentId)
                        self.addVariableToComponentIdx(componentId, frequencyVariable)
                        variable = f'{imaginery_number} {frequencyVariable} {inductanceVariable}'
                        list_var.append({'varStr':variable, 'positive':self.componentDirectionPositive(directedEdge)})
                print('not nonlinearPath: ', not nonlinearPath, ' and len(list_var) > 0:', len(list_var) > 0)
                if not nonlinearPath and len(list_var) > 0: # add_normal
                    latexStrWithEqual = self.sumOfPositiveNegativeToLatexAndScheme(list_var, {'varStr':'', 'positive':True}, addAsEquation=False) # just to get the imcomplete equation for harmonic_add later
                    latexStr = latexStrWithEqual.replace('=', '')
                    list_equationVars.append({'varStr':latexStr, 'positive':True})#for harmonic_sum
                    if len(list_var) > 1:
                        totalImpedanceVariable = EquationFinder.getVariable('impedance', 'total', totalVariableIdx)#not a real component<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WHAT ID?
                        # self.addVariableToComponentIdx(componentId, totalImpedanceVariable)
                        self.addVariableToComponentIdx(totalVariableIdx, totalImpedanceVariable)
                        totalVariableIdx += 1
                        # print('list_var:', list_var)
                        self.sumOfPositiveNegativeToLatexAndScheme(list_var, {'varStr':totalImpedanceVariable, 'positive':True})#<<not associated with any

            if not nonlinearBall and len(list_equationVars) > 0: #add_harmonic
                totalImpedanceVariable = EquationFinder.getVariable('impedance', 'total', totalVariableIdx)#not a real component<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WHAT ID?
                # self.addVariableToComponentIdx(componentId, totalImpedanceVariable)
                self.addVariableToComponentIdx(totalVariableIdx, totalImpedanceVariable)
                totalVariableIdx += 1
                print('list_equationVars', list_equationVars, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                self.harmonicSumOfPositiveNegativeToLatexAndScheme(list_equationVars, {'varStr':totalImpedanceVariable, 'positive':True})
        return self.list_equations