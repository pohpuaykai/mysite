import os
from json import loads

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
    pp.pprint(circuit_details)
    #because json keys has to be str.
    exec(f"global networkGraph;networkGraph={circuit_details['networkGraph']}"); 
    id__type = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['id__type'].items()))
    id__positiveLeadsDirections = dict(map(lambda t: (int(t[0]), t[1]), circuit_details['id__positiveLeadsDirections'].items()))
    # networkGraph = circuit_details['networkGraph']; id__type = circuit_details['id__type']
    pp.pprint(networkGraph)
    pp.pprint(id__type)
    pp.pprint(id__positiveLeadsDirections)

    from foundation.ecircuit.equationFinders.equationFinder import EquationFinder
    for equationFinderClass in EquationFinder.getAllEquationFinders():
        equationFinderClass().findEquations(networkGraph, id__type, id__positiveLeadsDirections)
    #print the equations on THREE.scene<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    return HttpResponse('', content_type="text/plain")