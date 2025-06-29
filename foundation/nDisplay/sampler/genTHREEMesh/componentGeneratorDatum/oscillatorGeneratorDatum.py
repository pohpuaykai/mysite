import os

from foundation.nDisplay.sampler.bottomupsampler import BottomUpSampler

"""
HC-49US Quartz Crystal


Frequency Range (Hz) = 3.570 ~ 3.999


Width of body (X-axis) = 10.5 mm
Height of body (Y-axis) = 3.5 mm
Length of body (Z-axis) = 3.8 mm

Width of body_base (X-axis) = 11.35 mm
Height of body_base (Y-axis) = 0.5 mm #estimated, not in schematics
Length of body_base (Z-axis) = 4.65 mm



Diameter of left_lead = 0.43 mm
Length of left_lead = 12.7 mm
Diameter of right_lead = 0.43 mm
Length of right_lead = 12.7 mm
"""

def bodyColorFunction(x, y, z, u, v):
    # if (3*math.pi/12)<=v and v<=(4*math.pi/12):
    #     return (192, 192, 192)
    return (192, 192, 192) # defaultColor, light-black

def bodyBaseColorFunction(x, y, z, u, v):
    # if (3*math.pi/12)<=v and v<=(4*math.pi/12):
    #     return (192, 192, 192)
    return (192, 192, 192) # defaultColor, light-black
def leftLeadColorFunction(x, y, z, u, v):
    return (192, 192, 192)#silver-grey
def rightLeadColorFunction(x, y, z, u, v):
    return (192, 192, 192)#silver-grey
import math; theMathModule = locals()['math'];


def realRoot(number, power):
    if number < 0:
        return -math.pow(abs(number), 1/power)
    else:
        return math.pow(number, 1/power)




body_base_width = 11.35 
body_base_height = 0.5
body_base_length = 4.65
body_base_yStart = 0

body_width = 10.5
body_height = 3.5
body_length = 3.8
body_yStart = body_base_yStart + body_base_height


left_lead_length = 5
left_lead_diameter = 0.7
right_lead_length = 5
right_lead_diameter = 0.7

left_lead_yStart = -left_lead_length
left_lead_xzCentre = -2.5
right_lead_yStart = -right_lead_length
right_lead_xzCentre = 2.5


listOfVertices, listOfIndices, listOfColors = BottomUpSampler.bottomUpPieceWiseSampler([
    {#body of the capacitor
        'uStart':body_yStart,
        'uEnd':body_yStart+body_height,
        'uStep':0.1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-1,
        'vEnd':1,
        'vStep':1/12,
        'xFormulaLambda':lambda v, y: eval('(body_width/2)*(math.sqrt(1-(math.pow(X , 32))))*realRoot(math.cos(math.pi*v), 3)', locals={'v':v, 'X': (y-body_yStart)/body_height, 'body_width':body_width, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('(body_length/2)*(math.sqrt(1-(math.pow(X , 32))))*math.sin(math.pi*v)', locals={'v':v, 'X': (y-body_yStart)/body_height, 'body_length':body_length, 'math':theMathModule}),
        'colorFunction':bodyColorFunction
    },
    {#body_base of the capacitor, x-z not affected by y
        'uStart':body_base_yStart,
        'uEnd':body_base_yStart+body_base_height,
        'uStep':0.1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-1,
        'vEnd':1,
        'vStep':1/12,
        'xFormulaLambda':lambda v, y: eval('(body_base_width/2)*realRoot(math.cos(math.pi*v), 3)', locals={'v':v, 'y':y, 'body_base_width':body_base_width, 'realRoot':realRoot, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('(body_base_length/2)*math.sin(math.pi*v)', locals={'v':v, 'y':y, 'body_base_length':body_base_length, 'math':theMathModule}),
        'colorFunction':bodyBaseColorFunction
    },
    {#left lead -ve (shorter)
        'uStart':left_lead_yStart,#'uStart':-left_lead_length,
        'uEnd':left_lead_yStart+left_lead_length,#'uEnd':0,
        'uStep':1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-1,
        'vEnd':1,
        'vStep':1/12,
        'xFormulaLambda':lambda v, y: eval('0.5*left_lead_diameter*math.cos(math.pi*v)+left_lead_xzCentre', locals={'v':v, 'y':y, 'left_lead_diameter':left_lead_diameter, 'left_lead_xzCentre':left_lead_xzCentre, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('0.5*left_lead_diameter*math.sin(math.pi*v)', locals={'v':v, 'y':y, 'left_lead_diameter':left_lead_diameter, 'left_lead_xzCentre':left_lead_xzCentre, 'math':theMathModule}),
        'colorFunction':leftLeadColorFunction
    },
    {#right lead +ve (longer)
        'uStart':right_lead_yStart,#'uStart':-17,
        'uEnd':right_lead_yStart+right_lead_length,#'uEnd':0,
        'uStep':1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-1,
        'vEnd':1,
        'vStep':1/12,
        'xFormulaLambda':lambda v, y: eval('0.5*right_lead_diameter*math.cos(math.pi*v)+right_lead_xzCentre', locals={'v':v, 'y':y, 'right_lead_diameter':right_lead_diameter, 'right_lead_xzCentre':right_lead_xzCentre, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('0.5*right_lead_diameter*math.sin(math.pi*v)', locals={'v':v, 'y':y, 'right_lead_diameter':right_lead_diameter, 'right_lead_xzCentre':right_lead_xzCentre, 'math':theMathModule}),
        'colorFunction':rightLeadColorFunction
    },
])





##########################################################################################
#left_lead -ve (shorter)
length = left_lead_length
diameter = left_lead_diameter
yStart = left_lead_yStart
xzCentre = left_lead_xzCentre

"""left|right<->down|up

left_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))-(diameter*(1/2))
right = xzCentre-(diameter*(1/2))
in = (diameter*(1/2))
out = -(diameter*(1/2))


right_touchingBox
down = yStart
up = yStart+length
left = xzCentre+(diameter*(1/2))
right = xzCentre+(diameter*(1/2))+(diameter*(1/2))
in = (diameter*(1/2))
out = -(diameter*(1/2))


down_touchingBox
down = yStart-(length*(1/4))
up = yStart
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = (diameter*(1/2))
out = -(diameter*(1/2))


in_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = (diameter*(1/2))+(diameter*(1/2))
out = (diameter*(1/2))


out_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = -(diameter*(1/2))
out = -(diameter*(1/2))-(diameter*(1/2))

"""


solderableLeads = [
    #left_lead
    [
        ([#left_touchingBox #left -> right
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (left, up, inx)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, down, inx)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, down, out)
        ]),
#<<<<<<<<<<<<


        ([#down_touchingBox # down -> up
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, up, out)
        ]),
#<<<<<<<<<<<<


        ([#in_touchingBox # in -> out
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, down, inx)
        ]),
#<<<<<<<<<<<<

        ([#out_touchingBox # out -> in
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, up, out)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, down, out)
        ]),
#<<<<<<<<<<<<

    ],

]


"""left|right<->down|up

right_touchingBox
down = yStart
up = yStart+length
left = xzCentre+(diameter*(1/2))
right = xzCentre+(diameter*(1/2))+(diameter*(1/2))
in = (diameter*(1/2))
out = -(diameter*(1/2))


left_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))-(diameter*(1/2))
right = xzCentre-(diameter*(1/2))
in = (diameter*(1/2))
out = -(diameter*(1/2))


down_touchingBox
down = yStart-(length*(1/4))
up = yStart
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = (diameter*(1/2))
out = -(diameter*(1/2))


in_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = (diameter*(1/2))+(diameter*(1/2))
out = (diameter*(1/2))


out_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = -(diameter*(1/2))
out = -(diameter*(1/2))-(diameter*(1/2))

"""


#right_lead +ve (longer)
length = right_lead_length
diameter = right_lead_diameter
yStart = right_lead_yStart
xzCentre = right_lead_xzCentre

#right_lead +ve (longer)
length = right_lead_length
diameter = right_lead_diameter
yStart = right_lead_yStart
xzCentre = right_lead_xzCentre

solderableLeads += [

    #right_lead
    [
        ([#right_touchingBox # right -> left
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (right, up, out)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, down, out)
        ]),
#<<<<<<<<<<<<


        ([#down_touchingBox # down -> up
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, down, out)
        ]),
#<<<<<<<<<<<<


        ([#in_touchingBox # in -> out
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, up, inx)<
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, up, inx)<
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, down, inx)<
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, down, inx)<
        ]),
#<<<<<<<<<<<<

        ([#out_touchingBox out -> in
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, up, out)<
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, up, out)<
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, down, out)<
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, down, out)<
        ]),
#<<<<<<<<<<<<


    ],
]





if __name__=='__main__':
    name = 'Oscillator'
    print(f'generating Component{name} from UserPreset datum')
    from foundation.nDisplay.sampler.genTHREEMesh.reader.threecomponentgenerator import THREEComponentGenerator
    THREEComponentGenerator().generateMeshFile(name, listOfVertices, listOfIndices, listOfColors, solderableLeads)