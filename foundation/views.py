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

    from foundation.automat.common.spanningtree import SpanningTree # temporary-> for testing
    from foundation.automat.common.allpairshortestpath import AllPairShortestPath #temporary -> for testing
    # from foundation.automat.common.smallcyclefinder import SmallCycleFinder
    """
    #KVL (this is also voltage_divider)
    # KCL (this is also current_divider)
    #series sum -> resistor
    #series sum -> capacitor
    #series sum -> inductor
    #parallel sum -> resistor
    #parallel sum -> capacitor
    #parallel sum -> inductor
    #OhmLaw
    #Thevenin
    #Norton
    #capcitor derivative model (timing)
    #inductor derivative model (timing)
    #hFE transistor
    #Eber-molls
    #Shockley diode model
    

    #solve with symgaussianelimination (? more well studied then bipartite_graph? not possible for differentiation&integration?), 
    but log the step taken to solve for (controllable_variables) in terms of (intermediate_variables)
    
    """
    circuit_details = loads(request.body)
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(circuit_details)
    return HttpResponse('', content_type="text/plain")