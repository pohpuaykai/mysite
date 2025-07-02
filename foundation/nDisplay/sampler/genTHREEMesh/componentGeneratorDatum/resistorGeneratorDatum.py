import os

from foundation.nDisplay.sampler.rotatesampler import RotateSampler

"""
Vishay MBA/SMA 0204, MBB/SMA 0207, MBE/SMA 0414 Dimensions in millimeter

MBB/SMA 0207
Length: 6.5 mm
Diameter: 0.6 mm
Lead Length: 28 mm
Lead Diameter: 0.6 mm
"""

length = 6.5
diameter = 0.6


import math; theMathModule = locals()['math'];
slopeness = 3/4
vertices, indices, colors = RotateSampler.rotatePieceWiseSample([
    # {#cylinder
    #     'formulaLambda':lambda x: eval('h', locals={'h':3/(1+math.pow(math.e, -0.5))}),
    #     'xStart':-6,
    #     'xEnd':-4,
    #     'xStep':0.1,
    #     'dStart':0,
    #     'dEnd':360,
    #     'dStep':30,
    #     'xRange__color':{
    #         (-5.7, -4.2):(81, 38, 39),#Brown band
    #     },
    #     'defaultColor':(96, 157, 167)
    # },
    {#ball, 0<=slopness<=1, smaller number less slopy
        'formulaLambda':lambda x: eval('h*math.sqrt(1-math.pow( 2*slopeness*( x- ((S+E)/2) ) / (E-S), 2))', locals={'slopeness':slopeness, 'x':x, 'h':(diameter/2), 'S':(-length/2), 'E':(-length/2)+(0.25* (length)), 'math':theMathModule}),
        'xStart':-length/2, # fixed for that length
        'xEnd':(-length/2)+(0.25* (length)),
        'xStep':0.05,
        'dStart':0,
        'dEnd':360,
        'dStep':30,
        'xRange__color':{
            ((-length/2)+(0.05*(length)), (-length/2)+(0.2*(length))):(81, 38, 39), #brown
        },
        'defaultColor':(96, 157, 167)
    },
    {#cylinder
        'formulaLambda':lambda x: eval('h*math.sqrt(1-math.pow( 2*slopeness*( x- ((S+E)/2) ) / (E-S), 2))', locals={'slopeness':slopeness, 'x':(-length/2)+(0.25* (length)),'h':(diameter/2), 'S':(-length/2)+(0.25* (length)), 'E':(-length/2)+(0.75* (length))}),
        'xStart':(-length/2)+(0.25* (length)),
        'xEnd':(-length/2)+(0.75* (length)),
        'xStep':0.1,
        'dStart':0,
        'dEnd':360,
        'dStep':30,
        'xRange__color':{
            ((-length/2)+(0.25* (length)), (-length/2)+(0.35* (length))):(81, 38, 39),#Brown band
            ((-length/2)+(0.45* (length)), (-length/2)+(0.55* (length))):(15, 81, 144),#Blue band
            ((-length/2)+(0.65* (length)), (-length/2)+(0.75* (length))):(255, 3, 0),#Red band
        },
        'defaultColor':(96, 157, 167)
    },
    {#ball
        'formulaLambda':lambda x: eval('h*math.sqrt(1-math.pow( 2*slopeness*( x- ((S+E)/2) ) / (E-S), 2))', locals={'slopeness':slopeness, 'x':x, 'h':(diameter/2), 'S':(-length/2)+(0.75* (length)), 'E':(-length/2)+(1.0* (length)), 'math':theMathModule}),
        'xStart':(-length/2)+(0.75* (length)),
        'xEnd':(-length/2)+(1.0* (length)),
        'xStep':0.01,
        'dStart':0,
        'dEnd':360,
        'dStep':30,
        'xRange__color':{
            ((-length/2)+(0.8* (length)), (-length/2)+(0.95* (length))):(255, 3, 0),#Red
        },
        'defaultColor':(96, 157, 167)
    },
    # {#cylinder
    #     'formulaLambda':lambda x: eval('h', locals={'h':3/(1+math.pow(math.e, -0.5))}),
    #     'xStart':4,
    #     'xEnd':6,
    #     'xStep':0.1,
    #     'dStart':0,
    #     'dEnd':360,
    #     'dStep':30,
    #     'xRange__color':{
            
    #     },
    #     'defaultColor':(96, 157, 167)
    # }
])

"""Left-side solderable_lead
left = -length*(3/4)
right = -length/2
up = diameter/2
down = -diameter/2
in = diameter/2
out = -diameter/2


left_touchingBox
left = -length*(3/4) - (length*(3/4))*(1/2)
right = -length*(3/4)
up = diameter/2
down = -diameter/2
in = diameter/2
out = -diameter/2


up_touchingBox
left = -length*(3/4)
right = -length/2
up = diameter/2 + (diameter/2)*(1/2)
down = diameter/2
in = diameter/2
out = -diameter/2


down_touchingBox
left = -length*(3/4)
right = -length/2
up = -diameter/2
down = -diameter/2 - (diameter/2)*(1/2)
in = diameter/2
out = -diameter/2


in_touchingBox
left = -length*(3/4)
right = -length/2
up = diameter/2
down = -diameter/2
in = -diameter/2
out = -diameter/2 - (diameter/2)*(1/2)


out_touchingBox
left = -length*(3/4)
right = -length/2
up = diameter/2
down = -diameter/2
in = diameter/2 + (diameter/2)*(1/2)
out = diameter/2


"""

"""Right-side solderable_lead
left = length/2
right = length*(3/4)
up = diameter/2
down = -diameter/2
in = diameter/2
out = -diameter/2




right_touchingBox
left = length*(3/4)
right = length*(3/4) + (length*(3/4))*(1/2)
up = diameter/2
down = -diameter/2
in = diameter/2
out = -diameter/2


up_touchingBox
left = length/2
right = length*(3/4)
up = diameter/2 +(diameter/2)*(1/2)
down = diameter/2
in = diameter/2
out = -diameter/2


down_touchingBox
left = length/2
right = length*(3/4)
up = -diameter/2
down = -diameter/2 -(diameter/2)*(1/2)
in = diameter/2
out = -diameter/2


in_touchingBox
left = length/2
right = length*(3/4)
up = diameter/2
down = -diameter/2
in = diameter/2+(diameter/2)*(1/2)
out = diameter/2


out_touchingBox
left = length/2
right = length*(3/4)
up = diameter/2
down = -diameter/2
in = -diameter/2
out = -diameter/2-(diameter/2)*(1/2)


"""
# solderableLeads = [
#     [
#     ( 
#     [
#         (-length*(3/4), diameter/2, diameter/2), #(left, up, in) x, y, z
#         (-length/2, diameter/2, diameter/2), #(right, up, in)
#         (-length/2, diameter/2, -diameter/2), #(right, up, out)
#         (-length*(3/4), diameter/2, -diameter/2), #(left, up, out)
#         (-length*(3/4), -diameter/2, diameter/2), #(left, down, in)
#         (-length/2, -diameter/2, diameter/2), #(right, down, in)
#         (-length/2, -diameter/2, -diameter/2), #(right, down, out)
#         (-length*(3/4), -diameter/2, -diameter/2), #(left, down, out)
#     ],#touchingBoxesCoordinates
#         ((-length*(3/4), 0, 0), (-length, 0, 0))
#     ),#insertVectorCoordinates, start end
#     ####
#     ( 
#     [
#         (length*(3/4), diameter/2, diameter/2), #(left, up, in) x, y, z
#         (length/2, diameter/2, diameter/2), #(right, up, in)
#         (length/2, diameter/2, -diameter/2), #(right, up, out)
#         (length*(3/4), diameter/2, -diameter/2), #(left, up, out)
#         (length*(3/4), -diameter/2, diameter/2), #(left, down, in)
#         (length/2, -diameter/2, diameter/2), #(right, down, in)
#         (length/2, -diameter/2, -diameter/2), #(right, down, out)
#         (length*(3/4), -diameter/2, -diameter/2), #(left, down, out)
#     ],#touchingBoxesCoordinates
#         ((length*(3/4), 0, 0), (length, 0, 0))
#     ),#insertVectorCoordinates, start end
#     ]
# ]








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


positiveLeadsDirections = [(0, 1), (1, 0)] # if leftSolderableLead to rightSolderableLead, the positive, numbers are indices of solderableLeads

if __name__=='__main__':
    name = 'Resistor'
    type = 'resistor'
    print('generating Component Mesh from UserPreset datum')
    from foundation.nDisplay.sampler.genTHREEMesh.reader.threecomponentgenerator import THREEComponentGenerator
    THREEComponentGenerator().generateMeshFile(name, type, [vertices], [indices], [colors], solderableLeads, positiveLeadsDirections)