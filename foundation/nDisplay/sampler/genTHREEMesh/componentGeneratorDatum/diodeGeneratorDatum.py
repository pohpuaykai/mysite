import os

from foundation.nDisplay.sampler.rotatesampler import RotateSampler

"""
DO-41 (DO-204AL) mm

length : 5.2
diameter: 2.7
"""
body_length = 5.2
body_diameter = 2.7

length = body_length # total_length


import math; theMathModule = locals()['math'];

vertices, indices, colors = RotateSampler.rotatePieceWiseSample([
    {#body
        'formulaLambda':lambda x: eval('h', locals={'h':body_diameter/2}),
        'xStart':(-length/2),
        'xEnd':(-length/2)+(body_length),
        'xStep':0.1,
        'dStart':0,
        'dEnd':360,
        'dStep':30,
        'xRange__color':{
            ((-length/2),(-length/2)+(0.2*body_length)):(192, 192, 192),#silver band is the component bias direction
        },
        'defaultColor':(0, 0, 0)
    },
])

"""Left-side solderable_lead
left = -length*(3/4)
right = -length/2
up = diameter/2
down = -diameter/2
in = diameter/2
out = -diameter/2
"""
diameter = body_diameter
solderableLeads = [
    [
    ( 
    [
        (-length*(3/4), diameter/2, diameter/2), #(left, up, in) x, y, z
        (-length/2, diameter/2, diameter/2), #(right, up, in)
        (-length/2, diameter/2, -diameter/2), #(right, up, out)
        (-length*(3/4), diameter/2, -diameter/2), #(left, up, out)
        (-length*(3/4), -diameter/2, diameter/2), #(left, down, in)
        (-length/2, -diameter/2, diameter/2), #(right, down, in)
        (-length/2, -diameter/2, -diameter/2), #(right, down, out)
        (-length*(3/4), -diameter/2, -diameter/2), #(left, down, out)
    ],#touchingBoxesCoordinates
        ((-length*(3/4), 0, 0), (-length, 0, 0))
    ),#insertVectorCoordinates, start end
    ####
    ( 
    [
        (length*(3/4), diameter/2, diameter/2), #(left, up, in) x, y, z
        (length/2, diameter/2, diameter/2), #(right, up, in)
        (length/2, diameter/2, -diameter/2), #(right, up, out)
        (length*(3/4), diameter/2, -diameter/2), #(left, up, out)
        (length*(3/4), -diameter/2, diameter/2), #(left, down, in)
        (length/2, -diameter/2, diameter/2), #(right, down, in)
        (length/2, -diameter/2, -diameter/2), #(right, down, out)
        (length*(3/4), -diameter/2, -diameter/2), #(left, down, out)
    ],#touchingBoxesCoordinates
        ((length*(3/4), 0, 0), (length, 0, 0))
    ),#insertVectorCoordinates, start end
    ]
]

if __name__=='__main__':
    print('generating Component Mesh from UserPreset datum')
    from foundation.nDisplay.sampler.genTHREEMesh.reader.threecomponentgenerator import THREEComponentGenerator
    THREEComponentGenerator().generateMeshFile('Diode', vertices, indices, colors, solderableLeads)