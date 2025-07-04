from abc import ABC, abstractmethod

from foundation.automat.core.equation import Equation
from foundation.automat.parser.sorte.latexparser import Latexparser
from foundation.automat.common.smallcyclefinder import SmallCycleFinder

class EquationFinder(ABC):

    def __init__(self, networkGraph, id__type):
        """
        #assign a direction for each pair of leads of each component, by finding faces
        #group components into paths (for series addition), group paths into balls (for parallel addition)<<<<<<<<<<<<<<<<<<<graph_pruning collect all degree_2(non-wire) nodes

        #get the latex and scheme 
        """
        self.networkGraph = networkGraph
        self.id__type = id__type
        self.cycles = SmallCycleFinder.findCycles(networkGraph)
        self.directedCycles = []
        self.list_equations = []
        self.componentId__list_variables = dict(map(lambda idx: (idx, []), id__type))
        self.assignDirectionToEdges()#produces self.directedCycles
        self.superNodeIds = []
        self.list_nodeIds___deg2 = [] # for KCL
        self.tuple_startSuperNodeId_endSuperNodeId__list_path = {} # each item is a ball, for parallel_addition..., for paths do flatten(self.tuple_startSuperNodeId_endSuperNodeId__list_path.values()), 
        self.superNodeUndirectedGraph = {}# connect supernodes directly to superNodes, ignoring paths inbetween # for KCL
        self.groupComponentsIntoPathsAndBalls()

    @abstractmethod
    def findEquations(self):
        pass

    @classmethod
    def getAllEquationFinders(cls):#Automatically import all Python files in the package directory
        equationFinders = []
        import os; import importlib; import inspect
        module_dir = os.path.dirname(__file__); #print(module_dir, '<<<<<module_dir')
        for module in os.listdir(module_dir):
            if module.endswith('.py') and module not in ['__init__.py', 'equationfinder.py']:
                module_name = module[:-3] # remove .py
                # print('module_name::', module_name)
                # module_obj = importlib.import_module(f'.', package=__name__)
                module_obj = importlib.import_module(f'..{module_name}', package=__name__)
                for name, cls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                    if name in ['EquationFinder']:
                        continue
                    equationFinders.append(cls)
                    # print(name, '<<<<<<<className')#this is an equationfinder, but need to run it <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    # globals()[name] = cls # export the class as well
                    # for method_name, method in inspect.getmembers(cls, predicate=inspect.ismethod):
                    #     if (isinstance(inspect.getattr_static(cls, method_name), staticmethod)) or \
                    #        (isinstance(inspect.getattr_static(cls, method_name), classmethod)):
                    #        #is a static or class method
                    #        globals()[method_name] = method
        return equationFinders

    def groupComponentsIntoPathsAndBalls(self):
        """
        nodes with degree > 2 are superNodes, everything between any 2 superNodes, is a path(for series_addition)
        if there are no superNodes, then there is only 1 big path
        all paths that share the same superNodes are to be grouped together into balls(for parallel_addition)
        
        """
        for parentNode, children in self.networkGraph.items():
            if len(children) > 2:
                self.superNodeIds.append(parentNode)
            elif len(children) == 2:
                self.list_nodeIds___deg2.append(parentNode) # for KCL
        # find superNodes in directedCycles
        for directedCycle in self.directedCycles:
            indexOnDirectedCycle__superNodeId = {}
            for superNodeId in self.superNodeIds:
                try:#find the index of superNodeId on directedCycle, if index is 0 , it could be -1 also (first and last of directedCycle)
                    indexOnDirectedCycle__superNodeId[directedCycle.index(superNodeId)] = superNodeId
                except: # throws ValueError if superNodeId is not found on directedCycle
                    pass
            #get paths
            sortedIndices_indexOnDirectedCycle = sorted(indexOnDirectedCycle__superNodeId.keys())
            for idxOfIdxOnCycle in range(0, len(sortedIndices_indexOnDirectedCycle)):
                startIdxOnCycle = sortedIndices_indexOnDirectedCycle[idxOfIdxOnCycle]; startSuperNodeId = indexOnDirectedCycle__superNodeId[startIdxOnCycle]
                if idxOfIdxOnCycle == len(sortedIndices_indexOnDirectedCycle) - 1: # if its the lastIdx, go back on itself
                    # endIdxOnCycle = #need to make indices loop around..., purely indexing does not work in Python
                    directedPath = tuple(directedCycle[startIdxOnCycle+1:len(sortedIndices_indexOnDirectedCycle)]+directedCycle[:sortedIndices_indexOnDirectedCycle[0]])
                    endSuperNodeId = indexOnDirectedCycle__superNodeId[sortedIndices_indexOnDirectedCycle[0]]
                else:
                    endIdxOnCycle = sortedIndices_indexOnDirectedCycle[idxOfIdxOnCycle+1]
                    directedPath = tuple(directedCycle[startIdxOnCycle+1:endIdxOnCycle])#+1 on startIdxOnCycle to exclude the superNode
                    endSuperNodeId = indexOnDirectedCycle__superNodeId[endIdxOnCycle]
                #check for repeats and store
                existingPaths = self.tuple_startSuperNodeId_endSuperNodeId__list_path.get((startSuperNodeId, endSuperNodeId), [])#check both (startSuperNodeId, endSuperNodeId) & (endSuperNodeId, startSuperNodeId), but store only (startSuperNodeId, endSuperNodeId)
                if len(existingPaths) == 0: #check the other direction
                    existingPaths = self.tuple_startSuperNodeId_endSuperNodeId__list_path.get((endSuperNodeId, startSuperNodeId), [])
                if directedPath not in existingPaths:
                    existingPaths.append(directedPath)
                self.tuple_startSuperNodeId_endSuperNodeId__list_path[(startSuperNodeId, endSuperNodeId)] = existingPaths
                #add to superNodeUndirectedGraph
                existingNeighbours = self.superNodeUndirectedGraph.get(startSuperNodeId, [])
                if endSuperNodeId not in existingNeighbours:
                    existingNeighbours.append(endSuperNodeId)
                self.superNodeUndirectedGraph[startSuperNodeId] = existingNeighbours
                #add the other direction edge
                existingNeighbours = self.superNodeUndirectedGraph.get(endSuperNodeId, [])
                if startSuperNodeId not in existingNeighbours:
                    existingNeighbours.append(startSuperNodeId)
                self.superNodeUndirectedGraph[endSuperNodeId] = existingNeighbours


    def assignDirectionToEdges(self):
        self.directedEdges = []
        #init, first cycle there are no directedEdges, so we assign according to the existing cycle's list direction
        startNode = self.cycles[0][0]
        for idx in range(1, len(self.cycles[0])):
            endNode = self.cycles[0][idx]
            self.directedEdges.append((startNode, endNode))
            startNode = endNode
        self.directedCycles.append(self.cycles[0])
        #check if the cycle has any directedEdges, then we go according to that direction
        for cycleIdx in range(1, len(self.cycles)):
            cycle = self.cycles[cycleIdx]
            #look for directedEdges
            startNode = cycle[0]
            for idx in range(1, len(cycle)):
                endNode = cycle[idx]
                if (startNode, endNode) in self.directedEdges:
                    break
                elif (endNode, startNode) in self.directedEdges:
                    cycle = reversed(cycle)
                    break
                startNode = endNode
            #add directedEdges
            self.directedCycles.append(cycle)
            startNode = cycle[0]
            for idx in range(1, len(cycle)):
                endNode = cycle[idx]
                self.directedEdges.append((startNode, endNode))
                startNode = endNode


    def addVariableToComponentIdx(self, componentIdx, variableStr):
        if variableStr not in self.componentId__list_variables[componentIdx]: # might be repeated because different equationFinder ask for the same variable
            self.componentId__list_variables[componentIdx].append(variableStr)

    def getEdgeDirection(self, edge):
        """
        
        :param edge: edge is a 2-tuple
        """
        return edge if edge in self.directedEdges else (edge[1], edge[0])

    def getVariable(self, electricalType, componentType, nodeId):
        """
        This returns an appropriate variable that is parsable by LatexParser

        :param electricalType: voltage, current, resistance, capacitance, inductance, reactance (TODO should be an Enum)
        :param componentType: (TODO should be an Enum)
            ac_signal_generator
            battery
            capacitor
            diode
            inductor
            oscillator
            resistor
            transistor
        :param nodeId: integer
        """
        main_symbol = ''
        if electricalType in ['voltage']:
            main_symbol = 'V'
        elif electricalType in ['current']:
            main_symbol = 'I'
        elif electricalType in ['resistance']:
            main_symbol = 'R'
        elif electricalType in ['capacitance']:
            main_symbol = 'C'
        elif electricalType in ['inductance']:
            main_symbol = 'L'
        elif electricalType in ['impedance']:
            main_symbol = 'X'
        elif electricalType in ['frequency']:
            main_symbol = 'w'
        elif electricalType in ['temperature']:
            main_symbol = 'T'
        elif electricalType in ['current_amplification']:
            main_symbol = '\\alpha'
        else:
            raise Exception()
        subscript = ''
        if componentType in ['ac_signal_generator']:
            subscript = 'AC'
        elif componentType in ['battery']:
            subscript = 'DC'
        elif componentType in ['capacitor']:
            subscript = 'C'
        elif componentType in ['diode']:
            subscript = 'D'
        elif componentType in ['inductor']:
            subscript = 'I'
        elif componentType in ['oscillator']:
            subscript = 'O'
        elif componentType in ['resistor']:
            subscript = 'R'
        elif componentType in ['transistor_emitter']:
            subscript = 'TE'
        elif componentType in ['transistor_common']:
            subscript = 'TC'
        elif componentType in ['transistor_base']:
            subscript = 'TB'
        elif componentType in ['transistor_emitter_common']:
            subscript = 'TEC'
        elif componentType in ['transistor_base_common']:
            subscript = 'TBC'
        elif componentType in ['transistor_emitter_base']:
            subscript = 'TEB'
        else:#undefined like totalsum
            subscript = componentType



        subsubscript = str(nodeId)
        return f'{main_symbol}_{{ {subscript}_{{ {subsubscript} }} }}'

    def sumOfPositiveNegativeToLatexAndScheme(self, list_vars, equivalentVariableDict, addAsEquation=True):
        latexStr = Latexparser.makePlusAndMinus(list_vars, equivalentVariableDict)
        print('latexStr: ', latexStr)
        if addAsEquation:
            self.addLatexStrAsEquation(latexStr)
        else:
            return latexStr

    def harmonicSumOfPositiveNegativeToLatexAndScheme(self, list_vars, equivalentVariableDict):
        latexStr = Latexparser.makeHarmonicPlusAndMinusEqualsZero(list_vars)
        print('latexStr: ', latexStr)
        self.addLatexStrAsEquation(latexStr)

    def simpleRatioToLatexAndScheme(self, equivalentRatio, numerator, denominator):
        latexStr = Latexparser.makeSimpleRatio(equivalentRatio, numerator, denominator)
        print('latexStr: ', latexStr)
        self.addLatexStrAsEquation(latexStr)

    def firstOrderSeperableDifferentialEquation(self, equivalent, derivativeMultiplier, differentiand, differentiator):
        latexStr = Latexparser.makeFirstOrderSeparableDifferentialEquation(equivalent, derivativeMultiplier, differentiand, differentiator)
        print('latexStr: ', latexStr)
        self.addLatexStrAsEquation(latexStr)

    def makeLinearFirstOrderDifferentialEquation(self, equivalent, listOfTerms):
        """#solving steps are here: https://en.wikipedia.org/wiki/Matrix_differential_equation <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<automate when you reach many BJT
        listOfTerms = [
            {'coefficient':, 'differentiand': , 'differentiator': },
        ]
        """
        latexStr = Latexparser.makeLinearFirstOrderDifferentialEquation(equivalent, listOfTerms)
        print('latexStr: ', latexStr)
        self.addLatexStrAsEquation(latexStr)

    def addLatexStrAsEquation(self, latexStr):# TODO associate equation with components used, and equationFinder used.<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        equation = Equation(equationStr=latexStr, parserName='latex')
        print('schemeStr: ', equation.schemeStr)
        self.list_equations.append(equation)

    def makeRatio(self, numerator, denominator):
        latexStr = Latexparser.makeRatio(numerator, denominator)
        return latexStr

    def exponentialMinusOne(self, equivalent, multiplicative, exponent):
        latexStr = Latexparser.exponentialMinusOne(equivalent, multiplicative, exponent)
        print('latexStr: ', latexStr)
        self.addLatexStrAsEquation(latexStr)

    def getConstantVariable(self, name):
        """
        Things like boltzmann_constant, charge_of_electron, avogradro_constant, imaginery_number
        """
        if name == 'boltzmann_constant':
            return 'k'
        elif name == 'charge_of_an_electron':
            return 'q'
        elif name == 'imaginery_number':
            return 'i'