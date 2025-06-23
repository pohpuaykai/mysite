import pprint

from foundation.nDisplay.sampler.bottomupsampler import BottomUpSampler

pp = pprint.PrettyPrinter(indent=4)

# def test(verbose):
#     """
#     start with 2D shapes at xz-farplane, end with 2D shapes at xz-farplane.
#     there must be same number of shapes at start_xz_farplane, as the number of shapes at start_xz_farplane
#     interpolate the in-between with yStart and yEnd and yFormula.

#     like a extrude-3Dprinter, going up from layers_in_xz_farplane
#     """
#     def piece0ColorFunction(x, y, z):
#         return (0, 0, 0) # defaultColor
#     import math; theMathModule = locals()['math'];
#     datum = [
#         {
#             'uStart':,
#             'uEnd':,
#             'uStep':,
#             'yFormulaLambda':lambda u: eval('', locals={'u':u, 'math':theMathModule}),
#             'vStart':,
#             'vEnd':,
#             'vStep':,
#             'xFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
#             'zFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
#             'colorFunction':piece0ColorFunction
#         },
#         # {
#         #     'uStart':,
#         #     'uEnd':,
#         #     'uStep':,
#         #     'yFormulaLambda':lambda u: eval('', locals={'u':u, 'math':theMathModule}),
#         #     'vStart':,
#         #     'vEnd':,
#         #     'vStep':,
#         #     'xFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
#         #     'zFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
#         #     'colorFunction':
#         # },
#     ]

def test_cylinder(verbose):
    """
    start with 2D shapes at xz-farplane, end with 2D shapes at xz-farplane.
    there must be same number of shapes at start_xz_farplane, as the number of shapes at start_xz_farplane
    interpolate the in-between with yStart and yEnd and yFormula.

    like a extrude-3Dprinter, going up from layers_in_xz_farplane
    """
    def bodyColorFunction(x, y, z, u, v):
        if (3*math.pi/12)<=v and v<=(4*math.pi/12):
            return (192, 192, 192)
        return (0, 0, 0) # defaultColor
    def leftLeadColorFunction(x, y, z, u, v):
        return (192, 192, 192)
    def rightLeadColorFunction(x, y, z, u, v):
        return (192, 192, 192)
    import math; theMathModule = locals()['math'];
    datum = [
        {#body of the capacitor
            'uStart':0,
            'uEnd':12,
            'uStep':0.1,
            'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
            'vStart':-math.pi,
            'vEnd':math.pi,
            'vStep':math.pi/12,
            'xFormulaLambda':lambda v, y: eval('5.5*(math.sqrt(1-(math.pow(X , 4)))-0.1*math.exp(-math.pow(8*(X+0.43), 2)))*math.cos(v)', locals={'v':v, 'X': (y-((0+12)/2))/(12-0), 'math':theMathModule}),
            'zFormulaLambda':lambda v, y: eval('5.5*(math.sqrt(1-(math.pow(X , 4)))-0.1*math.exp(-math.pow(8*(X+0.43), 2)))*math.sin(v)', locals={'v':v, 'X': (y-((0+12)/2))/(12-0), 'math':theMathModule}),
            'colorFunction':bodyColorFunction
        },
        {#left lead -ve (shorter)
            'uStart':-14,
            'uEnd':0,
            'uStep':1,
            'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
            'vStart':-math.pi,
            'vEnd':math.pi,
            'vStep':math.pi/12,
            'xFormulaLambda':lambda v, y: eval('0.55*math.cos(v)+1', locals={'v':v, 'y':y, 'math':theMathModule}),
            'zFormulaLambda':lambda v, y: eval('0.55*math.sin(v)+1', locals={'v':v, 'y':y, 'math':theMathModule}),
            'colorFunction':leftLeadColorFunction
        },
        {#right lead +ve (longer)
            'uStart':-17,
            'uEnd':0,
            'uStep':1,
            'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
            'vStart':-math.pi,
            'vEnd':math.pi,
            'vStep':math.pi/12,
            'xFormulaLambda':lambda v, y: eval('0.55*math.cos(v)-1', locals={'v':v, 'y':y, 'math':theMathModule}),
            'zFormulaLambda':lambda v, y: eval('0.55*math.sin(v)-1', locals={'v':v, 'y':y, 'math':theMathModule}),
            'colorFunction':rightLeadColorFunction
        },
        # {
        #     'uStart':,
        #     'uEnd':,
        #     'uStep':,
        #     'yFormulaLambda':lambda u: eval('', locals={'u':u, 'math':theMathModule}),
        #     'vStart':,
        #     'vEnd':,
        #     'vStep':,
        #     'xFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
        #     'zFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
        #     'colorFunction':
        # },
    ]
    if verbose:
        listOfVertices, listOfIndices, listOfColors = BottomUpSampler.bottomUpPieceWiseSampler(datum)
        from foundation.nDisplay.sampler.genTHREEMesh.reader.threemeshclassgenerator import THREEMeshClassGenerator
        THREEMeshClassGenerator().generateMeshFile('Capacitor', listOfVertices, listOfIndices, listOfColors)
        print('printed capacitor')

if __name__=='__main__':
    test_cylinder(True)