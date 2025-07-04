from foundation.ecircuit.equationFinders.equationfinder import EquationFinder

class BJTcurrentamplificationEquationFinder(EquationFinder):

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections):
        super().__init__(networkGraph, id__type)
        self.id__positiveLeadsDirections = id__positiveLeadsDirections

    def findEquations(self):
        """
        ######################KCL
        I_E=I_B+I_C

        #######################amplification
        #alpha=current_common/current_emitter
        #beta(hfe)=current_common/current_base
        #alpha=beta/(beta+1)
        #beta=alpha/(1-alpha)

        #######################switching
        #emitter_saturation_current
        #should have internal resistance, and they follow ohmslaw(Hybrid-pi_model) (R_{CE}=V_{CE}/I_{C}), (R_{BE}=V_{BE}/I_{B}),  # which class to put this (NOT DONE YET)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #should have internal capacitance, and they should take (0)compleximpedancesum (1)capacitortimingmodel(affects the transition of (cutoff->active) & of (saturation->active)) # which class to put this (NOT DONE YET)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        for componentId, componentType in self.id__type.items():
            if componentType in ['transistor']:
                commonCurrentVariable = self.getVariable("current", 'transistor_common', componentId)#<<<<<<<
                emitterCurrentVariable = self.getVariable("current", 'transistor_emitter', componentId)#<<<<<<<
                baseCurrentVariable = self.getVariable("current", 'transistor_base', componentId)#<<<<<<<<<
                commonVoltageVariable = self.getVariable("voltage", 'transistor_common', componentId)#<<<<<<<
                emitterVoltageVariable = self.getVariable("voltage", 'transistor_emitter', componentId)#<<<<<<<
                baseVoltageVariable = self.getVariable("voltage", 'transistor_base', componentId)#<<<<<<<<<
                commonResistanceVariable = self.getVariable("resistance", 'transistor_common', componentId)#<<<<<<<
                emitterVoltageVariable = self.getVariable("resistance", 'transistor_emitter', componentId)#<<<<<<<
                baseVoltageVariable = self.getVariable("resistance", 'transistor_base', componentId)#<<<<<<<<<
                alphaVariable = self.getVariable("current_amplification", 'transistor_emitter_common', componentId) #<<<<<<<
                betaVariable = self.getVariable("current_amplification", 'transistor_base_common', componentId) #<<<<<<<<
                baseCollectorCapacitanceVariable = self.getVariable("capacitance", 'transistor_base_common', componentId)#also capacitance_{\mu} # feeds back collector into base <-> causes Miller effect
                baseEmitterCapacitanceVariable = self.getVariable("capacitance", 'transistor_base_common', componentId)#also capacitance_{\pi} # stores charge <->sets delays in forward biasing
                #KCL
                self.sumOfPositiveNegativeToLatexAndScheme(self, [{'varStr':baseCurrentVariable, 'positive':True}, {'varStr':commonCurrentVariable, 'positive':True}], {'varStr':emitterCurrentVariable, 'positive':True})
                #amplication
                self.simpleRatioToLatexAndScheme(alphaVariable, commonCurrentVariable, emitterCurrentVariable)
                self.simpleRatioToLatexAndScheme(betaVariable, commonCurrentVariable, baseCurrentVariable)
                self.simpleRatioToLatexAndScheme(alphaVariable, betaVariable, betaVariable+'+1')
                self.simpleRatioToLatexAndScheme(betaVariable, alphaVariable, '1-'+alphaVariable)
                #OhmsLaw (Hybrid-pi_model)
                self.simpleRatioToLatexAndScheme(commonResistanceVariable, commonVoltageVariable+'-'+emitterVoltageVariable, commonCurrentVariable)#take R_{CE}=commonResistanceVariable, V_{CE}=commonVoltageVariable-emitterVoltageVariable
                self.simpleRatioToLatexAndScheme(baseResistanceVariable, baseVoltageVariable+'-'+emitterVoltageVariable, baseCurrentVariable)#take R_{BE}=baseResistanceVariable, V_{BE}=baseVoltageVariable-emitterVoltageVariable
                
                #compleximpedance should be included in CompleximpedancesumEquationFinder.py<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                #capacitortimingmodel (aka switching_timing_models)
                timeVariable = 't' # TODO standardise? might it have variable collision with other time? more than 1 time? when there is problems with time please check here
                self.makeLinearFirstOrderDifferentialEquation(baseCurrentVariable, [
                    {'coefficient':baseEmitterCapacitanceVariable, 'differentiand':baseVoltageVariable+'-'+emitterVoltageVariable , 'differentiator':timeVariable },
                    {'coefficient':baseCollectorCapacitanceVariable, 'differentiand':baseVoltageVariable+'-'+commonVoltageVariable , 'differentiator':timeVariable }
                ])
                self.firstOrderSeperableDifferentialEquation(currentVariable, baseCollectorCapacitanceVariable, voltageVariable, timeVariable)
