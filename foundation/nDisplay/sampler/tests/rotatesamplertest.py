from foundation.nDisplay.core.mesh.sampler.rotateSampler import RotateSampler
from foundation.nDisplay.core.mesh.mesh import Mesh

def test__meshgenerator__cylinder(verbose=False):
    #TEST 1: cylinder
    formulaStr = 'hx'
    formulaLambda = lambda x: eval(formulaStr, locals={'h':1})
    vertices = RotateSampler.rotateSample(formulaLambda, -1, 1, 0.1, 0, 360, 45)
    mesh = Mesh(vertices)


def test__meshgenerator__wall(verbose=False):
    #TEST 2: wall (left-to-right)
    formulaStr = 'h/(1+math.pow(math.e, -s * x))' # l is the height of the slope, s is the steepness of the slope
    formulaLambda = lambda x: eval(formulaStr, locals={'h':1, 's':1, 'x':x})
    vertices = RotateSampler.rotateSample(formulaLambda, -1, 1, 0.1, 0, 360, 45)
    mesh = Mesh(vertices)

def test__meshgenerator__trench(verbose=False):
    #TEST 3: trench (left-to-right)
    formulaStr = 'h/(1+math.pow(math.e, s * x))' # l is the height of the slope, s is the steepness of the slope
    formulaLambda = lambda x: eval(formulaStr, locals={'h':1, 's':1, 'x':x})
    vertices = RotateSampler.rotateSample(formulaStr, locals={'h':1, 's':1, 'x':x})
    mesh = Mesh(vertices)


def test__meshgenerator__piecewise_trench_cylinder_wall(verbose=False):
    #TEST 4: piece-wise, trench-cylinder-wall
    vertices = RotateSampler.rotatePieceWiseSample([
        {#trench
            'formulaLambda':lambda x: eval('h/(1+math.pow(math.e, s * x))', locals={'h':1, 's':1, 'x':x}),
            'xStart':-2,
            'xEnd':-1,
            'xStep':0.1,
            'dStart':0,
            'dEnd':360,
            'dStep':90
        },
        {#cylinder
            'formulaLambda':lambda x: eval('hx', locals={'h':1}),
            'xStart':-1,
            'xEnd':1,
            'xStep':0.1,
            'dStart':0,
            'dEnd':360,
            'dStep':90
        },
        {#wall
            'formulaLambda':lambda x: eval('h/(1+math.pow(math.e, -s * x))', locals={'h':1, 's':1, 'x':x}),
            'xStart':1,
            'xEnd':2,
            'xStep':0.1,
            'dStart':0,
            'dEnd':360,
            'dStep':90
        }
    ])
    mesh = Mesh(vertices)


#TEST 5 add colors, follow CUBE


if __name__=='__main__':
    test__meshgenerator__cylinder(True)
    test__meshgenerator__wall(True)
    test__meshgenerator__trench(True)
    test__meshgenerator__piecewise_trench_cylinder_wall(True)