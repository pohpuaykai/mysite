import pprint

# from foundation.nDisplay.core.mesh.sampler.rotateSampler import RotateSampler
# from foundation.nDisplay.core.mesh.mesh import Mesh
from foundation.nDisplay.sampler.rotatesampler import RotateSampler

pp = pprint.PrettyPrinter(indent=4)

def test__meshgenerator__cylinder(verbose=False):
    #TEST 1: cylinder
    formulaStr = 'h'
    import math; theMathModule = locals()['math'];
    formulaLambda = lambda x: eval(formulaStr, locals={'h':3/(1+math.pow(math.e, 0.5)), 'x':x, 'math':theMathModule})
    xRange__color = {#non-overlapping
        (-1, -1.3):'0xff0000',
        (1, 1.3):'0x0000ff',
    }
    defaultColor = '0x00ff00'
    vertices, indices, colors, startPointIndices, endPointIndices = RotateSampler.rotateSample(formulaLambda, -2, 2, 0.1, 0, 360, 30, xRange__color, defaultColor)
    # vertices, indices, colors, startPointIndices, endPointIndices = RotateSampler.rotateSample(formulaLambda, -1, 1, 0.5, 0, 360, 90)
    
    if verbose:
        # print('vertices')
        # pp.pprint(vertices)
        # print('indices')
        # pp.pprint(indices)
        # pp.pprint(startPointIndices)
        # pp.pprint(endPointIndices)
        from foundation.nDisplay.sampler.genTHREEMesh.reader.threemeshgenerator import THREEMeshGenerator
        THREEMeshGenerator().generateMeshFile('trench', vertices, indices, colors)


def test__meshgenerator__wall(verbose=False):
    #TEST 2: wall (left-to-right)
    formulaStr = 'h/(1+math.pow(math.e, -s * (x-3)))' # l is the height of the slope, s is the steepness of the slope
    import math; theMathModule = locals()['math'];
    formulaLambda = lambda x: eval(formulaStr, locals={'h':3, 's':0.5, 'x':x, 'math':theMathModule})
    vertices, indices, colors, startPointIndices, endPointIndices = RotateSampler.rotateSample(formulaLambda, 2, 4, 0.01, 0, 360, 30, xRange__color)
    # mesh = Mesh(vertices)
    if verbose:
        # print('vertices')
        # pp.pprint(vertices)
        # print('indices')
        # pp.pprint(indices)
        from foundation.nDisplay.sampler.genTHREEMesh.reader.threemeshgenerator import THREEMeshGenerator
        THREEMeshGenerator().generateMeshFile('trench', vertices, indices, colors)

def test__meshgenerator__trench(verbose=False):
    #TEST 3: trench (left-to-right)
    formulaStr = 'h/(1+math.pow(math.e, s * (x+3)))' # l is the height of the slope, s is the steepness of the slope
    import math; theMathModule = locals()['math'];
    formulaLambda = lambda x: eval(formulaStr, locals={'h':3, 's':0.5, 'x':x, 'math':theMathModule})
    vertices, indices, colors, startPointIndices, endPointIndices = RotateSampler.rotateSample(formulaLambda, -4, -2, 0.01, 0, 360, 30, xRange__color)
    # mesh = Mesh(vertices)
    if verbose:
        # print('vertices')
        # pp.pprint(vertices)
        # print('indices')
        # pp.pprint(indices)
        from foundation.nDisplay.sampler.genTHREEMesh.reader.threemeshgenerator import THREEMeshGenerator
        THREEMeshGenerator().generateMeshFile('trench', vertices, indices, colors)


def test__meshgenerator__piecewise_trench_cylinder_wall(verbose=False):
    #TEST 4: piece-wise, trench-cylinder-wall==5_Band_Resistor_Brown_Brown_Blue_Red_Red==11.6kOhm_+2%
    import math; theMathModule = locals()['math'];
    vertices, indices, colors = RotateSampler.rotatePieceWiseSample([
        {#cylinder
            'formulaLambda':lambda x: eval('h', locals={'h':3/(1+math.pow(math.e, -0.5))}),
            'xStart':-6,
            'xEnd':-4,
            'xStep':0.1,
            'dStart':0,
            'dEnd':360,
            'dStep':30,
            'xRange__color':{
                (-5.7, -4.2):(81, 38, 39),#Brown band
            },
            'defaultColor':(96, 157, 167)
        },
        {#trench
            'formulaLambda':lambda x: eval('h/(1+math.pow(math.e, s * (x+3)))', locals={'h':3, 's':0.5, 'x':x, 'math':theMathModule}),
            'xStart':-4,
            'xEnd':-2,
            'xStep':0.01,
            'dStart':0,
            'dEnd':360,
            'dStep':30,
            'xRange__color':{
                
            },
            'defaultColor':(96, 157, 167)
        },
        {#cylinder
            'formulaLambda':lambda x: eval('h', locals={'h':3/(1+math.pow(math.e, 0.5))}),
            'xStart':-2,
            'xEnd':2,
            'xStep':0.1,
            'dStart':0,
            'dEnd':360,
            'dStep':30,
            'xRange__color':{
                (-2, -1.2):(81, 38, 39),#Brown band
                (-0.4, 0.4):(15, 81, 144),#Blue band
                (1.2, 2):(255, 33, 0),#Red band
            },
            'defaultColor':(96, 157, 167)
        },
        {#wall
            'formulaLambda':lambda x: eval('h/(1+math.pow(math.e, -s * (x-3)))', locals={'h':3, 's':0.5, 'x':x, 'math':theMathModule}),
            'xStart':2,
            'xEnd':4,
            'xStep':0.01,
            'dStart':0,
            'dEnd':360,
            'dStep':30,
            'xRange__color':{
                # (2.2, 3.7):(255, 33, 0),#Red
            },
            'defaultColor':(96, 157, 167)
        },
        {#cylinder
            'formulaLambda':lambda x: eval('h', locals={'h':3/(1+math.pow(math.e, -0.5))}),
            'xStart':4,
            'xEnd':6,
            'xStep':0.1,
            'dStart':0,
            'dEnd':360,
            'dStep':30,
            'xRange__color':{
                
            },
            'defaultColor':(96, 157, 167)
        }
    ])
    # mesh = Mesh(vertices)
    if verbose:
        # print('vertices')
        # pp.pprint(vertices)
        # print('indices')
        # pp.pprint(indices)
        from foundation.nDisplay.sampler.genTHREEMesh.reader.threemeshgenerator import THREEMeshGenerator
        THREEMeshGenerator().generateMeshFile('trench', vertices, indices, colors)


#TEST 5 add colors, follow CUBE


if __name__=='__main__':
    test__meshgenerator__cylinder(True)
    # test__meshgenerator__wall(True)
    # test__meshgenerator__trench(True)
    # test__meshgenerator__piecewise_trench_cylinder_wall(True)