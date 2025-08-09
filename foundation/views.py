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


def automat_findEquations(request):

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
    networkGraph = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['networkGraph'].items()))
    # networkGraphNoWires = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['networkGraphNoWires'].items()))
    id__type = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['id__type'].items()))
    id__positiveLeadsDirections = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['id__positiveLeadsDirections'].items()))
    edge__solderableIndices = {}
    for edge, solderableLeads in circuit_details['edge__solderableIndices'].items():
        edgeStart___str, edgeEnd___str = edge.split(',')
        edge__solderableIndices[(int(edgeStart___str), int(edgeEnd___str))] = tuple(solderableLeads)
    print('networkGraph')
    pp.pprint(networkGraph)
    pp.pprint(id__type)
    pp.pprint(id__positiveLeadsDirections)
    print('edge__solderableIndices:')
    pp.pprint(edge__solderableIndices)
    print('id__positiveLeadsDirections')
    pp.pprint(id__positiveLeadsDirections)

    componentId__list_variables = {}
    def updateDictList(newComponentId__list_variables):
        for newComponentId, newList_variables in newComponentId__list_variables.items():
            existing = componentId__list_variables.get(newComponentId, [])
            existing += newList_variables
            componentId__list_variables[newComponentId] = list(set(existing))

    from foundation.ecircuit.equationFinders.equationfinder import EquationFinder
    EquationFinder._has_run_common_code = False # run common code on every HTTPRequest
    # print('existing EquationFinder has ', len(EquationFinder.list_equations), ' equations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # EquationFinder.list_equations = []
    equationStr__variables = {}
    # listOfCollectedEquationStrs = []; listOfCollectedEquations = []; #allVariables = set()
    for equationFinderClass in EquationFinder.getAllEquationFinders():
        # equationFinderClass.list_equations = []
        print('running class: ', equationFinderClass.__name__, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        # print('len(equationStr__variables)', len(equationStr__variables))
        for equation in equationFinderClass(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices).findEquations():
            
            # print('componentId__list_variables: ')
            updateDictList(EquationFinder.componentId__list_variables)
            # pp.pprint(componentId__list_variables)
            # print('>><><><><><><><><><><')
            equationStr__variables[equation._eqs] = list(equation.variablesScheme.keys())

    # print('equationStr__variables: ')
    # pp.pprint(equationStr__variables)
    # print('componentId__list_variables: ')
    # pp.pprint(EquationFinder.componentId__list_variables)
    # print('>><><><><><><><><><><')
    pp.pprint(equationStr__variables)
    #cache this, return the cache id, and then for solveEquations endpoint, give option of using the cached items, like Equation instead of equationStr, to speed things <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    return HttpResponse(dumps({'equationStr__variables':equationStr__variables, 'componentId__list_variables':componentId__list_variables}), content_type="text/plain")

def automat_solveEquations(request):
    """
    input:
    list_equationStr
    id__type
    dependentVarStr
    list_independentVarStr
    """
    equation_details = loads(request.body)
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    # print('equation_details: ')
    # pp.pprint(equation_details); import pdb;pdb.set_trace()
    id__type = dict(map(lambda t: (int(t[0]), t[1]), equation_details['id__type'].items()))
    list_equationStr = equation_details['list_equationStr']
    dependentVarStr = equation_details['dependentVarStr']
    list_independentVarStr = equation_details['list_independentVarStr']
    print('id__type')
    pp.pprint(id__type)
    print('list_equationStr')
    pp.pprint(list_equationStr)
    print('dependentVarStr')
    print(dependentVarStr)
    print('list_independentVarStr')
    pp.pprint(list_independentVarStr)
    # print('dependentId: ', equation_details['dependentId'])
    # print('dependentVarType: ', equation_details['dependentVarType'])
    # print('list_independentId: ', equation_details['list_independentId'])
    # print('list_independentVarType: ', equation_details['list_independentVarType'])
    # list_tuple_independentId__independentVarType = zip(equation_details['list_independentId'], equation_details['list_independentVarType'])
    # print('dict_independentId__independentVarType: ', list_tuple_independentId__independentVarType)
    # print('list_equationStr: ', equation_details['list_equationStr'])


    # dependentVariableStr = EquationFinder.getVariable(equation_details['dependentVarType'], id__type[equation_details['dependentId']], circuit_details['dependentId']);
    # independentVariableStrs = []
    # for componentId, variableType in list_tuple_independentId__independentVarType:
    #     independentVariableStrs.append(EquationFinder.getVariable(
    #         variableType, 
    #         id__type[componentId], 
    #         componentId
    #     ))



    print('listOfCollectedEquations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    print(list_equationStr); print(len(list_equationStr));
    print('dependentVarStr', dependentVarStr); print('list_independentVarStr', list_independentVarStr)
    print('listOfCollectedEquations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    from foundation.automat.core.equation import Equation
    listOfCollectedEquations = []; 
    for latexEquationStr in list_equationStr:
        listOfCollectedEquations.append(Equation(equationStr=latexEquationStr, parserName='latex'))

    from foundation.ecircuit.equationSolvers.bipartitesolver import BipartiteSolver

    # dependentVariableStr = 'X_{total_{6}}'#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<hard code for now
    # independentVariableStrs = ['V_{R_{1}}', 'V_{R_{0}}', 'V_{DC_{4}}']#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<hard code for now
    steps = BipartiteSolver(listOfCollectedEquations, dependentVarStr, list_independentVarStr)._solve()

    pp.pprint(steps)

    return HttpResponse(dumps({'steps':steps}), content_type="text/plain")