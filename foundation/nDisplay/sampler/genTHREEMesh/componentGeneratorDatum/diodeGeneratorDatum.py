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
            ((-length/2),(-length/2)+(0.2*body_length)):(192, 192, 192),#silver band is the component bias direction on the leftSide, leftSide is -ve
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







##########################################################################################
solderableLeads = [
    #left_lead -ve
    [
        ([#left_touchingBox #left -> right
( -length*(3/4) ,  diameter/2 ,  diameter/2 ), # (right, up, inx)
( -length*(3/4) ,  diameter/2 ,  -diameter/2 ), # (right, up, out)
( -length*(3/4) ,  -diameter/2 ,  diameter/2 ), # (right, down, inx)
( -length*(3/4) ,  -diameter/2 ,  -diameter/2 ), # (right, down, out)
        ]),
#<<<<<<<<<<<<

        ([#up_touchingBox #up -> down
( -length*(3/4) ,  diameter/2 + (diameter/2)*(1/2) ,  diameter/2 ), # (left, up, inx)
( -length/2 ,  diameter/2 + (diameter/2)*(1/2) ,  diameter/2 ), # (right, up, inx)
( -length/2 ,  diameter/2 + (diameter/2)*(1/2) ,  -diameter/2 ), # (right, up, out)
( -length*(3/4) ,  diameter/2 + (diameter/2)*(1/2) ,  -diameter/2 ), # (left, up, out)
        ]),
#<<<<<<<<<<<<

        ([#down_touchingBox # down -> up
( -length*(3/4) ,  -diameter/2 - (diameter/2)*(1/2) ,  diameter/2 ), # (left, down, inx)
( -length/2 ,  -diameter/2 - (diameter/2)*(1/2) ,  diameter/2 ), # (right, down, inx)
( -length/2 ,  -diameter/2 - (diameter/2)*(1/2) ,  -diameter/2 ), # (right, down, out)
( -length*(3/4) ,  -diameter/2 - (diameter/2)*(1/2) ,  -diameter/2 ), # (left, down, out)
        ]),
#<<<<<<<<<<<<


        ([#in_touchingBox # in -> out
( -length*(3/4) ,  diameter/2 ,  -diameter/2 - (diameter/2)*(1/2) ), # (left, up, inx)
( -length/2 ,  diameter/2 ,  -diameter/2 - (diameter/2)*(1/2) ), # (right, up, inx)
( -length*(3/4) ,  -diameter/2 ,  -diameter/2 - (diameter/2)*(1/2) ), # (left, down, inx)
( -length/2 ,  -diameter/2 ,  -diameter/2 - (diameter/2)*(1/2) ), # (right, down, inx)
        ]),
#<<<<<<<<<<<<

        ([#out_touchingBox # out -> in
( -length/2 ,  diameter/2 ,  diameter/2 + (diameter/2)*(1/2) ), # (right, up, out)
( -length*(3/4) ,  diameter/2 ,  diameter/2 + (diameter/2)*(1/2) ), # (left, up, out)
( -length/2 ,  -diameter/2 ,  diameter/2 + (diameter/2)*(1/2) ), # (right, down, out)
( -length*(3/4) ,  -diameter/2 ,  diameter/2 + (diameter/2)*(1/2) ), # (left, down, out)
        ]),
#<<<<<<<<<<<<

    ],






    #right_lead +ve
    [
        ([#right_touchingBox # right -> left
( length*(3/4) ,  diameter/2 ,  diameter/2 ), # (left, up, inx)
( length*(3/4) ,  diameter/2 ,  -diameter/2 ), # (left, up, out)
( length*(3/4) ,  -diameter/2 ,  diameter/2 ), # (left, down, inx)
( length*(3/4) ,  -diameter/2 ,  -diameter/2 ), # (left, down, out)
        ]),
#<<<<<<<<<<<<

        ([#up_touchingBox # up -> down
( length/2 ,  diameter/2 +(diameter/2)*(1/2) ,  diameter/2 ), # (left, up, inx)
( length*(3/4) ,  diameter/2 +(diameter/2)*(1/2) ,  diameter/2 ), # (right, up, inx)
( length*(3/4) ,  diameter/2 +(diameter/2)*(1/2) ,  -diameter/2 ), # (right, up, out)
( length/2 ,  diameter/2 +(diameter/2)*(1/2) ,  -diameter/2 ), # (left, up, out)
        ]),
#<<<<<<<<<<<<

        ([#down_touchingBox # down -> up
( length/2 ,  -diameter/2 -(diameter/2)*(1/2) ,  diameter/2 ), # (left, down, inx)
( length*(3/4) ,  -diameter/2 -(diameter/2)*(1/2) ,  diameter/2 ), # (right, down, inx)
( length*(3/4) ,  -diameter/2 -(diameter/2)*(1/2) ,  -diameter/2 ), # (right, down, out)
( length/2 ,  -diameter/2 -(diameter/2)*(1/2) ,  -diameter/2 ), # (left, down, out)
        ]),
#<<<<<<<<<<<<


        ([#in_touchingBox # in -> out
( length/2 ,  diameter/2 ,  diameter/2+(diameter/2)*(1/2) ), # (left, up, inx)
( length*(3/4) ,  diameter/2 ,  diameter/2+(diameter/2)*(1/2) ), # (right, up, inx)
( length/2 ,  -diameter/2 ,  diameter/2+(diameter/2)*(1/2) ), # (left, down, inx)
( length*(3/4) ,  -diameter/2 ,  diameter/2+(diameter/2)*(1/2) ), # (right, down, inx)
        ]),
#<<<<<<<<<<<<

        ([#out_touchingBox out -> in
( length*(3/4) ,  diameter/2 ,  -diameter/2-(diameter/2)*(1/2) ), # (right, up, out)
( length/2 ,  diameter/2 ,  -diameter/2-(diameter/2)*(1/2) ), # (left, up, out)
( length*(3/4) ,  -diameter/2 ,  -diameter/2-(diameter/2)*(1/2) ), # (right, down, out)
( length/2 ,  -diameter/2 ,  -diameter/2-(diameter/2)*(1/2) ), # (left, down, out)
        ]),
#<<<<<<<<<<<<


    ],
]


positiveLeadsDirections = [(0, 1)] # if leftSolderableLead to rightSolderableLead, the positive, numbers are indices of solderableLeads


if __name__=='__main__':
    name = 'Diode'
    type = 'diode'
    print('generating Component Mesh from UserPreset datum')
    from foundation.nDisplay.sampler.genTHREEMesh.reader.threecomponentgenerator import THREEComponentGenerator
    THREEComponentGenerator().generateMeshFile(name, type, [vertices], [indices], [colors], solderableLeads, positiveLeadsDirections)