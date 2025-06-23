import pprint

from foundation.nDisplay.sampler.bottomupsampler
 import BottomUpSampler

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
    def piece0ColorFunction(x, y, z):
        return (0, 0, 0) # defaultColor
    import math; theMathModule = locals()['math'];
    datum = [
        {
            'uStart':,
            'uEnd':,
            'uStep':,
            'yFormulaLambda':lambda u: eval('', locals={'u':u, 'math':theMathModule}),
            'vStart':,
            'vEnd':,
            'vStep':,
            'xFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
            'zFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
            'colorFunction':piece0ColorFunction
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

if __name__=='__main__':
    test()