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


        def addEquation(associatedComponentIdList, componentId, componentType):
            voltageVariable = EquationFinder.getVariable('voltage', componentType, componentId)
            self.addVariableToComponentIdx(componentId, voltageVariable)
            inductanceVariable = EquationFinder.getVariable('inductance', componentType, componentId)
            self.addVariableToComponentIdx(componentId, inductanceVariable)
            currentVariable = EquationFinder.getVariable('current', componentType, componentId)
            self.addVariableToComponentIdx(componentId, currentVariable)
            timeVariable = 't' # TODO standardise? might it have variable collision with other time? more than 1 time? when there is problems with time please check here
            self.addVariableToComponentIdx(componentId, timeVariable)
            self.firstOrderSeperableDifferentialEquation(voltageVariable, inductanceVariable, currentVariable, timeVariable, [associatedComponentIdList])


        for componentId, componentType in filter(lambda t: t[1] in ['inductor'], self.id__type.items()):
            addEquation([componentId], componentId, componentType)

        for componentId, componentType in filter(lambda t: t[1] in ['AC_signal_generator'], self.id__type.items()):
            #need to check if there are any loops_or_nodes_in_common with this common, which has a capacitor, then we should have to add this formula
            #check for loops
            for directedCycleWithSigGen in filter(lambda directedCycle: componentId in directedCycle, self.directedCycles):
                if any(list(map(lambda componentId: self.id__type[componentId] in ['inductor'], directedCycleWithSigGen))):
                    addEquation([componentId], componentId, componentType)
                    break
                # import pdb;pdb.set_trace()

            #check for nodes
        return self.list_equations