import os
from json import loads, dumps

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

#https://doc.babylonjs.com/features/introductionToFeatures/chap1/first_app
# Create your views here.
def index(request):
    return render(request, os.path.join(settings.BASE_DIR, 'foundation', 'nDisplay', 'three', 'public', 'index.html'))
    # return render(request, "foundation/index.html", {})#TODO please remove this<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def automat_findEquationsAndSolve(request):

    """
    #KVL (this is also voltage_divider) #MST, APSP on MST, find subtracted edges, putback subtracted edges with shortestpath to form faces
    # KCL (this is also current_divider) # each wire component's neighbour_components' current should sum up to zero, need the direction of the source also...? What is there are many sources?
    #OhmLaw # every non-wire|non-source component, has V=IR
    #capcitor derivative model (timing) #every capacitor has this
    #inductor derivative model (timing) # every inductor has this
    #complex_impedance_sum model # every path|ball that only has linear_components(resistor|capacitor|inductor), parallel<->harmonic_sum(complex_impedance), series<->normal_sum(complex_impedance)
    #hFE transistor -> every transistor #https://en.wikipedia.org/wiki/Bipolar_junction_transistor
    #Eber-molls -> every transistor #https://en.wikipedia.org/wiki/Bipolar_junction_transistor
    #Shockley diode model -> every diode
    #Thevenin
    #Norton
    

    #solve with symgaussianelimination (? more well studied then bipartite_graph? not possible for differentiation&integration?), 
    but log the step taken to solve for (controllable_variables) in terms of (intermediate_variables)
    
    """
    circuit_details = loads(request.body)
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(circuit_details)
    #because json keys has to be str.
    # exec(f"global networkGraph;networkGraph={circuit_details['networkGraph']}"); 
    networkGraph = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['networkGraph'].items()))
    # networkGraphNoWires = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['networkGraphNoWires'].items()))
    id__type = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['id__type'].items()))
    id__positiveLeadsDirections = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['id__positiveLeadsDirections'].items()))
    edge__solderableIndices = {}
    for edge, solderableLeads in circuit_details['edge__solderableIndices'].items():
        edgeStart___str, edgeEnd___str = edge.split(',')
        edge__solderableIndices[(int(edgeStart___str), int(edgeEnd___str))] = tuple(solderableLeads)
    # networkGraph = circuit_details['networkGraph']; id__type = circuit_details['id__type']
    print('networkGraph')
    pp.pprint(networkGraph)
    # print('networkGraphNoWires')
    # pp.pprint(networkGraphNoWires)
    pp.pprint(id__type)
    pp.pprint(id__positiveLeadsDirections)
    print('edge__solderableIndices:')
    pp.pprint(edge__solderableIndices)
    print('dependentId: ', circuit_details['dependentId'])
    print('dependentVarType: ', circuit_details['dependentVarType'])
    print('list_independentId: ', circuit_details['list_independentId'])
    print('list_independentVarType: ', circuit_details['list_independentVarType'])
    list_tuple_independentId__independentVarType = zip(circuit_details['list_independentId'], circuit_details['list_independentVarType'])
    print('dict_independentId__independentVarType: ', list_tuple_independentId__independentVarType)


    from foundation.ecircuit.equationFinders.equationfinder import EquationFinder
    EquationFinder._has_run_common_code = False # run common code on every HTTPRequest
    # print('existing EquationFinder has ', len(EquationFinder.list_equations), ' equations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # EquationFinder.list_equations = []
    listOfCollectedEquationStrs = []; listOfCollectedEquations = []; #allVariables = set()
    for equationFinderClass in EquationFinder.getAllEquationFinders():
        # equationFinderClass.list_equations = []
        print('running class: ', equationFinderClass.__name__, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        print('len(listOfCollectedEquations)', len(listOfCollectedEquations))
        for equation in equationFinderClass(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices).findEquations():
            listOfCollectedEquationStrs.append(equation._eqs)
            listOfCollectedEquations.append(equation)
            variables = equation.variablesScheme
            # for variable in variables.keys():
            #     allVariables.add(variable)
    # allVariables = sorted(list(allVariables))
    # EquationFinder._has_run_common_code = False
    #print the equations on THREE.scene
    # listOfCollectedEquations = []
    # for equation in EquationFinder.list_equations:
    #     listOfCollectedEquations.append(equation._eqs)


    #for now randomly choose a dependentVariable, and choose 3 independentVariables.
    # nonWireVariables = list(filter(lambda s: 'wire' not in s, allVariables))
    # dependentVariableStr = nonWireVariables[0]; independentVariableStrs = nonWireVariables[1:4]

    dependentVariableStr = EquationFinder.getVariable(circuit_details['dependentVarType'], id__type[circuit_details['dependentId']], circuit_details['dependentId']);
    independentVariableStrs = []
    for componentId, variableType in list_tuple_independentId__independentVarType:
        independentVariableStrs.append(EquationFinder.getVariable(
            variableType, 
            id__type[componentId], 
            componentId
        ))


    print('listOfCollectedEquations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print(listOfCollectedEquationStrs); print(len(listOfCollectedEquations));
    print('dependentVariableStr', dependentVariableStr); print('independentVariableStrs', independentVariableStrs)
    print('listOfCollectedEquations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    from foundation.ecircuit.equationSolvers.bipartitesolver import BipartiteSolver

    # dependentVariableStr = 'X_{total_{6}}'#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<hard code for now
    # independentVariableStrs = ['V_{R_{1}}', 'V_{R_{0}}', 'V_{DC_{4}}']#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<hard code for now
    steps = BipartiteSolver(listOfCollectedEquations, dependentVariableStr, independentVariableStrs)._solve()





    # from foundation.ecircuit.orthogonalLayouts.rcclorthogonallayout import RCCLOrthogonalLayout

    return HttpResponse(dumps({'equations':listOfCollectedEquationStrs, 'solvingSteps':steps}), content_type="text/plain")