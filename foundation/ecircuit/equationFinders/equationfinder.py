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
        self.groupComponentsIntoPaths()
        self.groupPathsIntoBalls()

    @abstractmethod
    def findEquations(self):
        pass

    def getAllEquationFinders(self):
        pass#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<copy from foundation.automat.core.equation

    def groupPathsIntoBalls(self):
        pass#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def groupComponentsIntoPaths(self):
        pass#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

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
        elif electricalType in ['reactance']:
            main_symbol = 'X'
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
        elif componentType in ['transistor']:
            subscript = 'T'


        subsubscript = str(nodeId)
        return f'{main_symbol}_{{ {subscript}_{{ {subsubscript} }} }}'

    def sumOfPositiveNegativeToLatexAndScheme(self, list_vars):
        latexStr = Latexparser.readListOfPlusAndMinusEqualsZero(list_vars)
        print('latexStr: ', latexStr)
        equation = Equation(equationStr=latexStr, parserName='latex')
        print('schemeStr: ', equation.schemeStr)
        self.list_equations.append(equation)
