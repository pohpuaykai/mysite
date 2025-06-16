import pprint

# from foundation.nDisplay.core.mesh.sampler.rotateSampler import RotateSampler
# from foundation.nDisplay.core.mesh.mesh import Mesh
from foundation.nDisplay.sampler.rotatesampler import RotateSampler

pp = pprint.PrettyPrinter(indent=4)

def test__meshgenerator__cylinder(verbose=False):
    #TEST 1: cylinder
    formulaStr = 'h'
    import math; theMathModule = locals()['math'];
    formulaLambda = lambda x: eval(formulaStr, locals={'h':10/(1+math.pow(math.e, 0.3*4)), 'x':x, 'math':theMathModule})
    vertices, indices, startPointIndices, endPointIndices = RotateSampler.rotateSample(formulaLambda, -4, 4, 1, 0, 360, 30)
    # vertices, indices, startPointIndices, endPointIndices = RotateSampler.rotateSample(formulaLambda, -1, 1, 0.5, 0, 360, 90)
    
    if verbose:
        # print('vertices')
        # pp.pprint(vertices)
        # print('indices')
        # pp.pprint(indices)
        # pp.pprint(endPointIndices)
        from foundation.nDisplay.sampler.genTHREEMesh.reader.threemeshgenerator import THREEMeshGenerator
        THREEMeshGenerator().generateMeshFile('cylinder', vertices, indices, '0xff0000')


def test__meshgenerator__wall(verbose=False):
    #TEST 2: wall (left-to-right)
    formulaStr = 'h/(1+math.pow(math.e, -s * x))' # l is the height of the slope, s is the steepness of the slope
    import math; theMathModule = locals()['math'];
    formulaLambda = lambda x: eval(formulaStr, locals={'h':10, 's':0.3, 'x':x, 'math':theMathModule})
    vertices, indices, startPointIndices, endPointIndices = RotateSampler.rotateSample(formulaLambda, -6, -4, 0.01, 0, 360, 30)
    # mesh = Mesh(vertices)
    if verbose:
        # print('vertices')
        # pp.pprint(vertices)
        # print('indices')
        # pp.pprint(indices)
        from foundation.nDisplay.sampler.genTHREEMesh.reader.threemeshgenerator import THREEMeshGenerator
        THREEMeshGenerator().generateMeshFile('wall', vertices, indices, '0xff0000')

def test__meshgenerator__trench(verbose=False):
    #TEST 3: trench (left-to-right)
    formulaStr = 'h/(1+math.pow(math.e, s * x))' # l is the height of the slope, s is the steepness of the slope
    import math; theMathModule = locals()['math'];
    formulaLambda = lambda x: eval(formulaStr, locals={'h':10, 's':0.3, 'x':x, 'math':theMathModule})
    vertices, indices, startPointIndices, endPointIndices = RotateSampler.rotateSample(formulaLambda, 4, 6, 0.01, 0, 360, 30)
    # mesh = Mesh(vertices)
    if verbose:
        # print('vertices')
        # pp.pprint(vertices)
        # print('indices')
        # pp.pprint(indices)
        from foundation.nDisplay.sampler.genTHREEMesh.reader.threemeshgenerator import THREEMeshGenerator
        THREEMeshGenerator().generateMeshFile('trench', vertices, indices, '0xff0000')


def test__meshgenerator__piecewise_trench_cylinder_wall(verbose=False):
    #TEST 4: piece-wise, trench-cylinder-wall
    import math; theMathModule = locals()['math'];
    vertices, indices = RotateSampler.rotatePieceWiseSample([
        {#wall
            'formulaLambda':lambda x: eval('h/(1+math.pow(math.e, -s * x))', locals={'h':10, 's':0.3, 'x':x, 'math':theMathModule}),
            'xStart':-6,
            'xEnd':-4,
            'xStep':0.01,
            'dStart':0,
            'dEnd':360,
            'dStep':30
        },
        {#cylinder
            'formulaLambda':lambda x: eval('h', locals={'h':10/(1+math.pow(math.e, 0.3*4))}),
            'xStart':-4,
            'xEnd':4,
            'xStep':1,
            'dStart':0,
            'dEnd':360,
            'dStep':30
        },
        {#trench
            'formulaLambda':lambda x: eval('h/(1+math.pow(math.e, s * x))', locals={'h':10, 's':0.3, 'x':x, 'math':theMathModule}),
            'xStart':4,
            'xEnd':6,
            'xStep':0.01,
            'dStart':0,
            'dEnd':360,
            'dStep':30
        }
    ])
    # mesh = Mesh(vertices)
    if verbose:
        # print('vertices')
        # pp.pprint(vertices)
        # print('indices')
        # pp.pprint(indices)
        from foundation.nDisplay.sampler.genTHREEMesh.reader.threemeshgenerator import THREEMeshGenerator
        THREEMeshGenerator().generateMeshFile('resistor_outline', vertices, indices, '0xff0000')


#TEST 5 add colors, follow CUBE


if __name__=='__main__':
    # test__meshgenerator__cylinder(True)
    # test__meshgenerator__wall(True)
    # test__meshgenerator__trench(True)
    test__meshgenerator__piecewise_trench_cylinder_wall(True)