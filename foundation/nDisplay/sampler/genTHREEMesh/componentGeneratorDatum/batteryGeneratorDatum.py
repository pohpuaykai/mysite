import os

from foundation.nDisplay.sampler.rotatesampler import RotateSampler

"""
Energizer E91 mm

length (excluding top button and bottom): 49.5
diameter: 14.50
button length: 1.0
button diameter: 5.5
bottom length: 0.1
bottom diameter: 7.0
"""
body_length = 49.5
body_diameter = 14.5
button_length = 1.0
button_diameter = 5.5
bottom_length = 0.1
bottom_diameter = 7.0

length = bottom_length+body_length+bottom_length # total_length


import math; theMathModule = locals()['math'];

vertices, indices, colors = RotateSampler.rotatePieceWiseSample([
    {#button
        'formulaLambda':lambda x: eval('h', locals={'h':button_diameter/2}),
        'xStart':(-length/2),
        'xEnd':(-length/2)+(button_length),
        'xStep':0.1,
        'dStart':0,
        'dEnd':360,
        'dStep':30,
        'xRange__color':{
        },
        'defaultColor':(192, 192, 192)
    },
    {#body
        'formulaLambda':lambda x: eval('h', locals={'h':body_diameter/2}),
        'xStart':(-length/2)+(button_length),
        'xEnd':(-length/2)+(button_length+body_length),
        'xStep':0.1,
        'dStart':0,
        'dEnd':360,
        'dStep':30,
        'xRange__color':{
            ((-length/2)+(button_length),(-length/2)+(button_length+0.3*body_length)):(0, 0, 0),#Black band is the brand name
        },
        'defaultColor':(192, 192, 192)
    },
    {#bottom
        'formulaLambda':lambda x: eval('h', locals={'h':bottom_diameter/2}),
        'xStart':(-length/2)+(button_length)+(body_length),
        'xEnd':(-length/2)+(button_length)+(body_length)+(bottom_length),
        'xStep':0.1,
        'dStart':0,
        'dEnd':360,
        'dStep':30,
        'xRange__color':{
        },
        'defaultColor':(192, 192, 192)
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
    #left_lead
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






    #right_lead
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



if __name__=='__main__':
    print('generating Component Mesh from UserPreset datum')
    from foundation.nDisplay.sampler.genTHREEMesh.reader.threecomponentgenerator import THREEComponentGenerator
    THREEComponentGenerator().generateMeshFile('Battery', [vertices], [indices], [colors], solderableLeads)