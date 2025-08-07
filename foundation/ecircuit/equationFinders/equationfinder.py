from abc import ABC, abstractmethod

from foundation.automat.core.equation import Equation
from foundation.automat.parser.sorte.latexparser import Latexparser
from foundation.automat.common.smallcyclefinder import SmallCycleFinder

class EquationFinder(ABC):

    cycles = []
    # directedCycles = []
    # list_equations = [] # persist across HTTP Request (not what we want)
    componentId__list_variables = {}
    superNodeIds = []
    list_nodeIds___deg2 = [] # for KCL
    tuple_startSuperNodeId_endSuperNodeId__list_path = {} # each item is a ball, for parallel_addition..., for paths do flatten(self.tuple_startSuperNodeId_endSuperNodeId__list_path.values()), 
    superNodeUndirectedGraph = {}# connect supernodes directly to superNodes, ignoring paths inbetween # for KCL
    _has_run_common_code = False

    def __init__(self, networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices):
        """
        #assign a direction for each pair of leads of each component, by finding faces
        #group components into paths (for series addition), group paths into balls (for parallel addition):graph_pruning collect all degree_2(non-wire) nodes

        #get the latex and scheme 
        """
        self.networkGraph = networkGraph
        self.id__type = id__type
        self.id__positiveLeadsDirections = id__positiveLeadsDirections
        self.edge__solderableIndices = edge__solderableIndices
        print('self.edge__solderableIndices', self.edge__solderableIndices, '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        if not EquationFinder._has_run_common_code:#THIS CODES are repeated for everyChild class... 
            self.cycles = SmallCycleFinder.findCycles(self.networkGraph)
            self.directedCycles = []#We want it to persist across HTTP requests?
            self.directedEdges = [] # a part of directedCycles, for convienence
            self.list_equations = []#EquationFinder.list_equations
            EquationFinder.componentId__list_variables = dict(map(lambda idx: (idx, []), id__type))
            self.assignDirectionToEdges()#produces self.directedCycles
            self.superNodeIds = EquationFinder.superNodeIds
            self.list_nodeIds___deg2 = EquationFinder.list_nodeIds___deg2 # for KCL
            self.tuple_startSuperNodeId_endSuperNodeId__list_path = EquationFinder.tuple_startSuperNodeId_endSuperNodeId__list_path # each item is a ball, for parallel_addition..., for paths do flatten(self.tuple_startSuperNodeId_endSuperNodeId__list_path.values()), 
            self.superNodeUndirectedGraph = EquationFinder.superNodeUndirectedGraph#{}# connect supernodes directly to superNodes, ignoring paths inbetween # for KCL
            # self.edge__solderableIndices = EquationFinder.edge__solderableIndices
            EquationFinder.edge__solderableIndices =self.edge__solderableIndices
            self.groupComponentsIntoPathsAndBalls()
            print('superNodeIds: ')
            print(self.superNodeIds)
            print('list_nodeIds___degs: ')
            print(self.list_nodeIds___deg2)
            print('tuple_startSuperNodeId_endSuperNodeId__list_path')
            print(self.tuple_startSuperNodeId_endSuperNodeId__list_path)
            print('superNodeUndirectedGraph: ')
            print(self.superNodeUndirectedGraph)
            print(EquationFinder._has_run_common_code, 'ran before<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            EquationFinder._has_run_common_code = True
        else:
            self.cycles = EquationFinder.cycles
            self.directedCycles = EquationFinder.directedCycles
            self.directedEdges = EquationFinder.directedEdges
            self.list_equations = []#EquationFinder.list_equations
            EquationFinder.componentId__list_variables = dict(map(lambda idx: (idx, []), id__type))
            self.superNodeIds = EquationFinder.superNodeIds
            self.list_nodeIds___deg2 = EquationFinder.list_nodeIds___deg2 # for KCL
            self.tuple_startSuperNodeId_endSuperNodeId__list_path = EquationFinder.tuple_startSuperNodeId_endSuperNodeId__list_path # each item is a ball, for parallel_addition..., for paths do flatten(self.tuple_startSuperNodeId_endSuperNodeId__list_path.values()), 
            self.superNodeUndirectedGraph = EquationFinder.superNodeUndirectedGraph# connect supernodes directly to superNodes, ignoring paths inbetween # for KCL
            self.edge__solderableIndices = EquationFinder.edge__solderableIndices

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
        return equationFinders

    def groupComponentsIntoPathsAndBalls(self):
        """
        nodes with degree > 2 are superNodes, everything between any 2 superNodes, is a path(for series_addition)
        if there are no superNodes, then there is only 1 big path
        all paths that share the same superNodes are to be grouped together into balls(for parallel_addition)
        
        """
        for parentNode, children in self.networkGraph.items():
            if len(children) > 2:
                EquationFinder.superNodeIds.append(parentNode)
            elif len(children) == 2:
                EquationFinder.list_nodeIds___deg2.append(parentNode) # for KCL
        # find superNodes in directedCycles
        for directedCycle in self.directedCycles:#EquationFinder.directedCycles:
            indexOnDirectedCycle__superNodeId = {}
            for superNodeId in EquationFinder.superNodeIds:
                try:#find the index of superNodeId on directedCycle, if index is 0 , it could be -1 also (first and last of directedCycle)
                    indexOnDirectedCycle__superNodeId[directedCycle.index(superNodeId)] = superNodeId
                except: # throws ValueError if superNodeId is not found on directedCycle
                    pass
            #get paths
            sortedIndices_indexOnDirectedCycle = sorted(indexOnDirectedCycle__superNodeId.keys())
            for idxOfIdxOnCycle in range(0, len(sortedIndices_indexOnDirectedCycle)):
                startIdxOnCycle = sortedIndices_indexOnDirectedCycle[idxOfIdxOnCycle]
                startSuperNodeId = indexOnDirectedCycle__superNodeId[startIdxOnCycle]
                if idxOfIdxOnCycle == len(sortedIndices_indexOnDirectedCycle) - 1: # if its the lastIdx, go back on itself
                    # endIdxOnCycle = #need to make indices loop around..., purely indexing does not work in Python
                    # directedPath = tuple(directedCycle[startIdxOnCycle+1:len(sortedIndices_indexOnDirectedCycle)]+directedCycle[:sortedIndices_indexOnDirectedCycle[0]])
                    directedPath = tuple(directedCycle[startIdxOnCycle+1:]+directedCycle[1:sortedIndices_indexOnDirectedCycle[0]])
                    
                    endSuperNodeId = indexOnDirectedCycle__superNodeId[sortedIndices_indexOnDirectedCycle[0]]
                    #####
                    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~0')
                    # print((startSuperNodeId, endSuperNodeId), (endSuperNodeId, startSuperNodeId))
                    # print('directedCycle: ', directedCycle); print('startIdxOnCycle', startIdxOnCycle);
                    # print('sortedIndices_indexOnDirectedCycle', sortedIndices_indexOnDirectedCycle)
                    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~0')
                    #####
                else:
                    endIdxOnCycle = sortedIndices_indexOnDirectedCycle[idxOfIdxOnCycle+1]
                    directedPath = tuple(directedCycle[startIdxOnCycle+1:endIdxOnCycle])#+1 on startIdxOnCycle to exclude the superNode
                    endSuperNodeId = indexOnDirectedCycle__superNodeId[endIdxOnCycle]
                    #####
                    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1')
                    # print((startSuperNodeId, endSuperNodeId), (endSuperNodeId, startSuperNodeId)); 
                    # print('startIdxOnCycle', startIdxOnCycle); print('endIdxOnCycle', endIdxOnCycle)
                    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1')
                    #####
                #check for repeats and store
                existingPaths = EquationFinder.tuple_startSuperNodeId_endSuperNodeId__list_path.get((startSuperNodeId, endSuperNodeId), [])#check both (startSuperNodeId, endSuperNodeId) & (endSuperNodeId, startSuperNodeId), but store only (startSuperNodeId, endSuperNodeId)
                if len(existingPaths) == 0: #check the other direction
                    existingPaths = EquationFinder.tuple_startSuperNodeId_endSuperNodeId__list_path.get((endSuperNodeId, startSuperNodeId), [])
                if directedPath not in existingPaths:
                    existingPaths.append(directedPath)
                EquationFinder.tuple_startSuperNodeId_endSuperNodeId__list_path[(startSuperNodeId, endSuperNodeId)] = existingPaths
                #add to superNodeUndirectedGraph
                existingNeighbours = EquationFinder.superNodeUndirectedGraph.get(startSuperNodeId, [])
                if endSuperNodeId not in existingNeighbours:
                    existingNeighbours.append(endSuperNodeId)
                EquationFinder.superNodeUndirectedGraph[startSuperNodeId] = existingNeighbours
                #add the other direction edge
                existingNeighbours = EquationFinder.superNodeUndirectedGraph.get(endSuperNodeId, [])
                if startSuperNodeId not in existingNeighbours:
                    existingNeighbours.append(startSuperNodeId)
                EquationFinder.superNodeUndirectedGraph[endSuperNodeId] = existingNeighbours


    def assignDirectionToEdges(self):
        # self.directedEdges = []
        #init, first cycle there are no directedEdges, so we assign according to the existing cycle's list direction
        startNode = self.cycles[0][0]
        for idx in range(1, len(self.cycles[0])):
            endNode = self.cycles[0][idx]
            self.directedEdges.append((startNode, endNode))
            startNode = endNode
        self.directedCycles.append(self.cycles[0])#EquationFinder.directedCycles.append(self.cycles[0])
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
                    cycle = list(reversed(cycle))
                    break
                startNode = endNode
            #check if all the non-wire-components are connected in edge__solderableIndices
            startNonWireComponent = None; solderableIdx = None;
            print('cycle:', cycle, 'startNode: ', startNode, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            for startNodeId in range(0, len(cycle)-1):
                # endNodeId = cycle[startNodeId+1]; edge = (startNodeId, endNodeId)
                endNode = cycle[startNodeId+1]; startNode = cycle[startNodeId]; edge = (startNode, endNode)
                print(edge);
                if startNonWireComponent is not None and self.id__type[endNode] not in ['wire']:
                    solderableIdx = self.edge__solderableIndices[edge]
                    if startNonWireComponent != endNode:
                        self.edge__solderableIndices[(startNonWireComponent, endNode)] = solderableIdx
                        self.edge__solderableIndices[(endNode, startNonWireComponent)] = solderableIdx
                        # print('adding: ', (startNonWireComponent, endNode))
                    startNonWireComponent = endNode; #reset
                if startNonWireComponent is None and self.id__type[startNode] not in ['wire']:
                    startNonWireComponent = startNode
            # print('self.edge__solderableIndices', self.edge__solderableIndices)
            #
            EquationFinder.edge__solderableIndices = self.edge__solderableIndices
            print('EquationFinder.edge__solderableIndices', EquationFinder.edge__solderableIndices)

            #add directedEdges
            self.directedCycles.append(cycle)#EquationFinder.directedCycles.append(cycle)
            startNode = cycle[0]
            for idx in range(1, len(cycle)):
                endNode = cycle[idx]
                self.directedEdges.append((startNode, endNode))
                startNode = endNode
        EquationFinder.directedCycles = self.directedCycles # we want it to persist across HTTP Requests
        EquationFinder.directedEdges = self.directedEdges  # we want it to persist across HTTP Requests
        # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CREATED self.directedCycles', self.directedCycles)


    def addVariableToComponentIdx(self, componentIdx, variableStr):
        if componentIdx not in EquationFinder.componentId__list_variables or variableStr not in EquationFinder.componentId__list_variables[componentIdx]: # might be repeated because different equationFinder ask for the same variable
            existing = EquationFinder.componentId__list_variables.get(componentIdx, [])
            existing.append(variableStr)
            EquationFinder.componentId__list_variables[componentIdx] = existing
            # EquationFinder.componentId__list_variables[componentIdx].append(variableStr)

    def componentDirectionPositive(self, directedEdge):#TODO this should be renamed to componentDirectionPositive
        solderableIndices = self.edge__solderableIndices[directedEdge]
        isPositive = list(solderableIndices) in self.id__positiveLeadsDirections[directedEdge[0]] # take the start...., or should have taken the end? directedEdges[1]
        # print('>>>>>', list(solderableIndices), self.id__positiveLeadsDirections[directedEdge[0]], isPositive)
        return isPositive

    def directedEdgeIsPositive(self, directedEdge):#TODO this should be renamed to directedEdgeIsPositive
        """
        
        :param edge: edge is a 2-tuple
        """
        # return edge if edge in self.directedEdges else (edge[1], edge[0])
        # print(directedEdge, self.directedEdges, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<directedEdgeIsPositive<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')#
        return directedEdge in self.directedEdges

    @classmethod
    def getVariable(cls, electricalType, componentType, nodeId):
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
        return f'{main_symbol}_{{{subscript}_{{{subsubscript}}}}}'

    def sumOfPositiveNegativeToLatexAndScheme(self, list_vars, equivalentVariableDict, addAsEquation=True):
        latexStr = Latexparser.makePlusAndMinus(list_vars, equivalentVariableDict)
        print('sumOfPositiveNegativeToLatexAndScheme; latexStr: ', latexStr)
        if addAsEquation:
            self.addLatexStrAsEquation(latexStr)
        else:
            return latexStr

    def harmonicSumOfPositiveNegativeToLatexAndScheme(self, list_vars, equivalentVariableDict):
        latexStr = Latexparser.makeHarmonicPlusAndMinusEqualsZero(list_vars, equivalentVariableDict)
        print('harmonicSumOfPositiveNegativeToLatexAndScheme; latexStr: ', latexStr)
        self.addLatexStrAsEquation(latexStr)

    def simpleRatioToLatexAndScheme(self, equivalentRatio, numerator, denominator):
        latexStr = Latexparser.makeSimpleRatio(equivalentRatio, numerator, denominator)
        print('simpleRatioToLatexAndScheme; latexStr: ', latexStr)
        self.addLatexStrAsEquation(latexStr)

    def firstOrderSeperableDifferentialEquation(self, equivalent, derivativeMultiplier, differentiand, differentiator):
        latexStr = Latexparser.makeFirstOrderSeparableDifferentialEquation(equivalent, derivativeMultiplier, differentiand, differentiator)
        print('firstOrderSeperableDifferentialEquation; latexStr: ', latexStr)
        self.addLatexStrAsEquation(latexStr)

    def makeLinearFirstOrderDifferentialEquation(self, equivalent, listOfTerms):
        """#solving steps are here: https://en.wikipedia.org/wiki/Matrix_differential_equation <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<automate when you reach many BJT
        listOfTerms = [
            {'coefficient':, 'differentiand': , 'differentiator': },
        ]
        """
        latexStr = Latexparser.makeLinearFirstOrderDifferentialEquation(equivalent, listOfTerms)
        print('makeLinearFirstOrderDifferentialEquation; latexStr: ', latexStr)
        self.addLatexStrAsEquation(latexStr)

    def addLatexStrAsEquation(self, latexStr):# TODO associate equation with components used, and equationFinder used.<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        equation = Equation(equationStr=latexStr, parserName='latex')
        # print('schemeStr: ', equation.schemeStr)
        self.list_equations.append(equation)

    def makeRatio(self, numerator, denominator):
        latexStr = Latexparser.makeRatio(numerator, denominator)
        print('makeRatio; latexStr: ', latexStr)
        return latexStr

    def exponentialMinusOne(self, equivalent, multiplicative, exponent):
        latexStr = Latexparser.exponentialMinusOne(equivalent, multiplicative, exponent)
        print('exponentialMinusOne; latexStr: ', latexStr)
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