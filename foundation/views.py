import os
from json import loads, dumps

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from foundation.decorators import ticketable
from foundation.models import Ticket

#https://doc.babylonjs.com/features/introductionToFeatures/chap1/first_app
def index(request):
    return render(request, os.path.join(settings.BASE_DIR, 'foundation', 'nDisplay', 'three', 'public', 'index.html'))
    # return render(request, "foundation/index.html", {})#TODO please remove this<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@ticketable
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
    # import pprint
    # pp = pprint.PrettyPrinter(indent=4)
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
    # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # print('networkGraph')
    # pp.pprint(networkGraph)
    # pp.pprint(id__type)
    # pp.pprint(id__positiveLeadsDirections)
    # print('edge__solderableIndices:')
    # pp.pprint(edge__solderableIndices)
    # print('id__positiveLeadsDirections')
    # pp.pprint(id__positiveLeadsDirections)
    # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # import pdb;pdb.set_trace()

    # componentId__list_variables = {}
    # def updateDictList(newComponentId__list_variables):
    #     for newComponentId, newList_variables in newComponentId__list_variables.items():
    #         existing = componentId__list_variables.get(newComponentId, [])
    #         existing += newList_variables
    #         componentId__list_variables[newComponentId] = list(set(existing))

    from foundation.ecircuit.equationFinders.equationfinder import EquationFinder
    EquationFinder._has_run_common_code = False # run common code on every HTTPRequest
    # print('existing EquationFinder has ', len(EquationFinder.list_equations), ' equations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # EquationFinder.list_equations = []
    # equationStr__variables = {}
    returnData = []
    # listOfCollectedEquationStrs = []; listOfCollectedEquations = []; #allVariables = set()
    #backend to associate formulas with graph information and variable information
    """
    {
        'equation':,#inLatexFormat
        'equationFinderDisplayName':,#like "Ohms Law", "Kirchoff Voltage Law"
        'list_list_networkNodeIds':,#like for Kirchoff Voltage Law, a list of directedCycles, for Ohms Law, list_list of nodeIds?
        'variableInfos':[
            {
                'variable':,
                'networkNodeIds':, # for totals, take a list of networkIds
            }
        ]
    }
    """
    for equationFinderClass in EquationFinder.getAllEquationFinders():
        # equationFinderClass.list_equations = []
        # print('running class: ', equationFinderClass.__name__, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        # print('len(equationStr__variables)', len(equationStr__variables))

        for infoD in equationFinderClass(networkGraph, id__type, id__positiveLeadsDirections, edge__solderableIndices).findEquations():
            equation = infoD['equation']; list_list_networkNodeIds = infoD['list_list_networkNodeIds']

            ######for debugging of frontEnd_matching of variableLetterString to meshUUID <<<<<<<<<<<<<remove after the test is done
            # if not(equation._eqs =='-V_{R_{0}}-V_{R_{3}}+V_{DC_{1}}=0'):
            #     continue # so far only this equation is giving problems on the frontEnd, so we restrict the backend to make testing easier for frontend
            #######################################################################################################################


            variableStr__nodeId = {}
            for nodeId, list_variableStr in EquationFinder.componentId__list_variables.items():
                for variableStr in list_variableStr:
                    variableStr__nodeId[variableStr] = nodeId

            returnData.append({
                'equation':equation._eqs,
                'equationFinderDisplayName':equationFinderClass.equationFinderDisplayName,
                'list_list_networkNodeIds':list_list_networkNodeIds,#like for Kirchoff Voltage Law, a list of directedCycles, for Ohms Law, list_list of nodeIds?
                'variableInfos':EquationFinder.componentId__list_variables,
                'variables':list(equation.variables.keys()),
                'variableStr__nodeId':variableStr__nodeId
            })

    # pp.pprint(returnData)
    #cache this, return the cache id, and then for solveEquations endpoint, give option of using the cached items, like Equation instead of equationStr, to speed things <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    return HttpResponse(dumps(returnData), content_type="text/plain")


@ticketable
def automat_solveEquations(request):
    """
    input:
    list_equationStr
    id__type
    dependentVarStr
    list_independentVarStr
    """
    equation_details = loads(request.body)
    # import pprint
    # pp = pprint.PrettyPrinter(indent=4)
    # print('equation_details: ')
    # pp.pprint(equation_details); import pdb;pdb.set_trace()
    id__type = dict(map(lambda t: (int(t[0]), t[1]), equation_details['id__type'].items()))
    list_equationStr = equation_details['list_equationStr']
    dependentVarStr = equation_details['dependentVarStr']
    list_independentVarStr = list(set((filter(lambda varStr: varStr is not None, equation_details['list_independentVarStr']))))
    simplify = equation_details['simplify']
    # print('list_equationStr')
    # pp.pprint(list_equationStr)
    # print('simplify')
    # print(simplify)
    # print('id__type')
    # pp.pprint(id__type)
    # print('dependentVarStr')
    # print(dependentVarStr)
    # print('list_independentVarStr')
    # pp.pprint(list_independentVarStr)
    # import pdb;pdb.set_trace()


    # print('listOfCollectedEquations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # print(list_equationStr); print(len(list_equationStr));
    # print('dependentVarStr', dependentVarStr); print('list_independentVarStr', list_independentVarStr)
    # print('listOfCollectedEquations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    from foundation.automat.core.equation import Equation
    listOfCollectedEquations = []; 
    for latexEquationStr in list_equationStr:
        listOfCollectedEquations.append(Equation(equationStr=latexEquationStr, parserName='latex'))

    from foundation.ecircuit.equationSolvers.bipartitesolver import BipartiteSolver

    steps = BipartiteSolver(listOfCollectedEquations, dependentVarStr, list_independentVarStr)._solve(simplify=simplify)#frontend tell me if i should simplify

    # pp.pprint(steps)

    #linearise steps
    # branchedStepsIdx__latexStrs = {}; 
    branchedStepsIdxs = []; latexStrs = []; #zip it up on the other side
    runningStepsIdx__branchedStepsIdx = {}; runningStepsIdx = -1;
    list_tuple_latexStrVariableStr = []
    list_runningIdx__toClearAll = []; list_runningIdx__toKeep = []

    #steps[0] is always the beginning
    # beginning = steps.pop(0)
    beginning = steps[0]
    branchedStepsIdx = (0, 'vor'); runningStepsIdx += 1; runningStepsIdx__branchedStepsIdx[runningStepsIdx] = branchedStepsIdx; 
    branchedStepsIdxs.append(branchedStepsIdx); latexStrs.append(beginning['vor']['latex'])
    list_tuple_latexStrVariableStr.append((beginning['vor']['latex'], beginning['vor']['variables']))
    previousVorRunningStepsIdx = runningStepsIdx; previousHinRunningStepsIdx = None

    #
    for stepIdx, step in enumerate(steps[1:]): # skip first step
        hasVorSubStep = False
        for vorSubStepIdx, vorSubStep in enumerate(step['vor__subSteps']):
            branchedStepsIdx = (stepIdx+1, 'vor', vorSubStepIdx, 'vor__subSteps'); runningStepsIdx += 1; runningStepsIdx__branchedStepsIdx[runningStepsIdx] = branchedStepsIdx; 
            # if vorSubStepIdx == 1:
            #     list_branchedStepsIdx__toClearAll.append(branchedStepsIdx)
            branchedStepsIdxs.append(branchedStepsIdx); latexStrs.append(vorSubStep['resultLatexStr'])
            list_tuple_latexStrVariableStr.append((vorSubStep['resultLatexStr'], vorSubStep['resultVariables']))
            if vorSubStepIdx == len(step['vor__subSteps']) - 1: # last vor, vorSubStep might be empty, in which case we should keep the vor
                list_runningIdx__toKeep.append(runningStepsIdx); hasVorSubStep = True
        if not hasVorSubStep:
            list_runningIdx__toKeep.append(previousVorRunningStepsIdx);

        #hin always introduce a new equation
        branchedStepsIdx = (stepIdx+1, 'hin'); runningStepsIdx += 1; runningStepsIdx__branchedStepsIdx[runningStepsIdx] = branchedStepsIdx; 
        branchedStepsIdxs.append(branchedStepsIdx); latexStrs.append(step['hin']['latex'])
        list_tuple_latexStrVariableStr.append((step['hin']['latex'], step['hin']['variables']))
        previousHinRunningStepsIdx = runningStepsIdx


        hasHinSubStep = False
        for hinSubStepIdx, hinSubStep in enumerate(step['hin__subSteps']):
            branchedStepsIdx = (stepIdx+1, 'hin', hinSubStepIdx, 'hin__subSteps'); runningStepsIdx += 1; runningStepsIdx__branchedStepsIdx[runningStepsIdx] = branchedStepsIdx; 
            branchedStepsIdxs.append(branchedStepsIdx); latexStrs.append(hinSubStep['resultLatexStr'])
            list_tuple_latexStrVariableStr.append((hinSubStep['resultLatexStr'], hinSubStep['resultVariables']))
            if hinSubStepIdx == len(step['hin__subSteps']) - 1: # last hin, hinSubStep, might be empty, in which case we should keep the hin
                list_runningIdx__toKeep.append(runningStepsIdx); hasHinSubStep = True
        if not hasHinSubStep:
            list_runningIdx__toKeep.append(previousHinRunningStepsIdx)


        #vor is the running_equation, like running_balance
        branchedStepsIdx = (stepIdx+1, 'vor'); runningStepsIdx += 1; runningStepsIdx__branchedStepsIdx[runningStepsIdx] = branchedStepsIdx;
        branchedStepsIdxs.append(branchedStepsIdx); latexStrs.append(step['vor']['latex'])
        list_tuple_latexStrVariableStr.append((step['vor']['latex'], step['vor']['variables']))
        list_runningIdx__toClearAll.append(runningStepsIdx)
        previousVorRunningStepsIdx = runningStepsIdx


    # pp.pprint(runningStepsIdx__branchedStepsIdx);
    # import pdb;pdb.set_trace()

    return HttpResponse(dumps({
        'steps':steps, 'branchedStepsIdxs':branchedStepsIdxs, 
        'latexStrs':latexStrs, 
        'list_tuple_latexStrVariableStr': list_tuple_latexStrVariableStr, 
        'runningStepsIdx__branchedStepsIdx':runningStepsIdx__branchedStepsIdx,
        'list_runningIdx__toClearAll':list_runningIdx__toClearAll, 
        'list_runningIdx__toKeep':list_runningIdx__toKeep
    }), content_type="text/plain")


def pollable(request):
    # print('request.POST: ', request.POST); import pdb;pdb.set_trace()
    if 'ticketNum' in request.POST:#ticketNum is the id col of the SQLite
        try:
            ticketObj = Ticket.objects.get(id=int(request.POST['ticketNum']))
        except:
            return HttpResponse('', content_type="text/plain")
        responseContent = ticketObj.responseContent
        if responseContent is None: # this means that the backend thread is not done yet, so we should not delete the ticket
            return HttpResponse('', content_type='text/plain')
        ticketObj.delete()
        # print('***********************************************responseContent:')
        # print(responseContent)
        # print('***********************************************')
        return HttpResponse(responseContent, content_type="text/plain")
    return HttpResponse('', content_type="text/plain")
