import os

from foundation.nDisplay.sampler.bottomupsampler import BottomUpSampler

"""
FairChild Semiconductor SS9018 AM/FM Amplifier, Local Oscillator of FM/VHF Tuner
High Current Gain Bandwidth Product f_T=1.1 GHz (Typ)
NPN Epitaxial Silicon Transistor




Width of round_body (X-axis) = 4.58 mm
Height of round_body (Y-axis) = 4.58 mm
Length of round_body (Z-axis) = 3.8 mm


WidthBack of trapezius_body (X-axis) = 3.6
HeightBack of trapezius_body (Y-axis) = 4.58
LengthBack of trapezius_body (Z-axis) = 1.02


WidthFront of trapezius_body (X-axis) = 4.58
HeightFront of trapezius_body (Y-axis) = 4.58
LengthFront of trapezius_body (Z-axis) = 1.02



Diameter of left_lead = 0.46 mm
Length of left_lead = 14.47 mm
Diameter of middle_lead = 0.46 mm
Length of middle_lead = 14.47 mm
Diameter of right_lead = 0.46 mm
Length of right_lead = 14.47 mm
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
def middleLeadColorFunction(x, y, z, u, v):
    return (192, 192, 192)#silver-grey
def rightLeadColorFunction(x, y, z, u, v):
    return (192, 192, 192)#silver-grey
import math; theMathModule = locals()['math'];


def realRoot(number, power):
    if number < 0:
        return -math.pow(abs(number), 1/power)
    else:
        return math.pow(number, 1/power)





####
round_body_width = 4.58
round_body_height = 4.58
round_body_length = 3.8
round_body_yStart = 0

trapezius_body_widthBack = 3.6
trapezius_body_heightBack = 4.58
trapezius_body_lengthBack = 1.02
trapezius_body_widthFront = 4.58
trapezius_body_heightFront = 4.58
trapezius_body_lengthFront = 1.02

trapezius_body_yStart = 0
####


left_lead_length = 14.5#14.47
left_lead_diameter = 0.46
middle_lead_length = 14.5#14.47
middle_lead_diameter = 0.46
right_lead_length = 14.5#14.47
right_lead_diameter = 0.46

left_lead_yStart = -left_lead_length
left_lead_xzCentre = -1.27
middle_lead_yStart = -middle_lead_length
middle_lead_xzCentre = 0
right_lead_yStart = -right_lead_length
right_lead_xzCentre = 1.27

#####
sideXWidth=(trapezius_body_widthFront-trapezius_body_widthBack)/2
gradient=trapezius_body_lengthFront/sideXWidth

def xFormulaLambda(v, y):
    if -trapezius_body_widthFront/2 <= v and v <= trapezius_body_widthFront/2:
        return v
    if trapezius_body_widthFront/2 < v and v <= trapezius_body_widthFront/2+sideXWidth:
        return trapezius_body_widthFront/2-(v-trapezius_body_widthFront/2)
    if trapezius_body_widthFront/2+sideXWidth < v and v <= trapezius_body_widthFront/2+sideXWidth+trapezius_body_widthBack:
        return (trapezius_body_widthFront/2-sideXWidth)-(v-(trapezius_body_widthFront/2+sideXWidth))
    if trapezius_body_widthFront/2+sideXWidth+trapezius_body_widthBack < v and v <= trapezius_body_widthFront/2+sideXWidth+trapezius_body_widthBack+sideXWidth:
        return (-trapezius_body_widthBack/2)-(v-(trapezius_body_widthFront/2+sideXWidth+trapezius_body_widthBack))

def zFormulaLambda(v, y):
    if -trapezius_body_widthFront/2 <= v and v <= trapezius_body_widthFront/2:
        return 0
    if trapezius_body_widthFront/2 < v and v <= trapezius_body_widthFront/2+sideXWidth:
        return -((v-trapezius_body_widthFront/2)*gradient)
    if trapezius_body_widthFront/2+sideXWidth < v and v <= trapezius_body_widthFront/2+sideXWidth+trapezius_body_widthBack:
        return -trapezius_body_lengthBack
    if trapezius_body_widthFront/2+sideXWidth+trapezius_body_widthBack < v and v <= trapezius_body_widthFront/2+sideXWidth+trapezius_body_widthBack+sideXWidth:
        return -trapezius_body_lengthBack-((v-(trapezius_body_widthFront/2+sideXWidth+trapezius_body_widthBack))*-gradient)

listOfVertices, listOfIndices, listOfColors = BottomUpSampler.bottomUpPieceWiseSampler([
    {#trapezius body of the transistor
        'uStart':trapezius_body_yStart,
        'uEnd':trapezius_body_yStart+trapezius_body_heightFront,
        'uStep':0.1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-trapezius_body_widthFront/2,
        'vEnd':trapezius_body_widthFront/2+sideXWidth+trapezius_body_widthBack+sideXWidth,
        'vStep':0.1,
        'xFormulaLambda':lambda v, y: eval('xFormulaLambda(v, y)', locals={'v':v, 'y':y, 'xFormulaLambda':xFormulaLambda, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('zFormulaLambda(v, y)', locals={'v':v, 'y':y, 'zFormulaLambda':zFormulaLambda, 'math':theMathModule}),
        'colorFunction':bodyColorFunction
    },
    {# round body of the transistor
        'uStart':round_body_yStart,
        'uEnd':round_body_yStart+round_body_height,
        'uStep':0.1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':0,#half circle
        'vEnd':1,
        'vStep':1/12,
        'xFormulaLambda':lambda v, y: eval('(round_body_width/2)*math.cos(math.pi*v)', locals={'v':v, 'y':y, 'round_body_width':round_body_width, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('(round_body_length/2)*math.sin(math.pi*v)', locals={'v':v, 'y':y, 'round_body_length':round_body_length, 'math':theMathModule}),
        'colorFunction':bodyBaseColorFunction
    },
    {#left lead
        'uStart':left_lead_yStart,#'uStart':-left_lead_length,
        'uEnd':left_lead_yStart+left_lead_length,#'uEnd':0,
        'uStep':0.1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-1,
        'vEnd':1,
        'vStep':1/12,
        'xFormulaLambda':lambda v, y: eval('0.5*left_lead_diameter*math.cos(math.pi*v)+left_lead_xzCentre', locals={'v':v, 'y':y, 'left_lead_diameter':left_lead_diameter, 'left_lead_xzCentre':left_lead_xzCentre, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('0.5*left_lead_diameter*math.sin(math.pi*v)', locals={'v':v, 'y':y, 'left_lead_diameter':left_lead_diameter, 'left_lead_xzCentre':left_lead_xzCentre, 'math':theMathModule}),
        'colorFunction':leftLeadColorFunction
    },
    {#middle lead
        'uStart':middle_lead_yStart,#'uStart':-left_lead_length,
        'uEnd':middle_lead_yStart+middle_lead_length,#'uEnd':0,
        'uStep':0.1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-1,
        'vEnd':1,
        'vStep':1/12,
        'xFormulaLambda':lambda v, y: eval('0.5*middle_lead_diameter*math.cos(math.pi*v)+middle_lead_xzCentre', locals={'v':v, 'y':y, 'middle_lead_diameter':middle_lead_diameter, 'middle_lead_xzCentre':middle_lead_xzCentre, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('0.5*middle_lead_diameter*math.sin(math.pi*v)', locals={'v':v, 'y':y, 'middle_lead_diameter':middle_lead_diameter, 'middle_lead_xzCentre':middle_lead_xzCentre, 'math':theMathModule}),
        'colorFunction':middleLeadColorFunction
    },
    {#right lead
        'uStart':right_lead_yStart,#'uStart':-17,
        'uEnd':right_lead_yStart+right_lead_length,#'uEnd':0,
        'uStep':0.1,
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
#left_lead
length = left_lead_length
diameter = left_lead_diameter
yStart = left_lead_yStart
xzCentre = left_lead_xzCentre

"""left_lead has no rightTouchingBox, too close to solder anything

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


solderableLeads = [
    #left_lead
    [
        ([#left_touchingBox #left -> right
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (left, up, inx)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (right, up, inx)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, down, inx)
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, down, inx)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre-(diameter*(1/2))-(diameter*(1/2)), yStart+(length*(1/2)), 0), #startPoint
            (xzCentre-(diameter*(1/2)), yStart+(length*(1/2)), 0)  #endPoint
        )),
#<<<<<<<<<<<<


        ([#down_touchingBox # down -> up
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  (diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  (diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  -(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  -(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart-(length*(1/4)), 0), #startPoint
            (xzCentre, yStart, 0)  #endPoint
        )),
#<<<<<<<<<<<<


        ([#in_touchingBox # in -> out
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), (diameter*(1/2))+(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), (diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<

        ([#out_touchingBox # out -> in
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), -(diameter*(1/2))-(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), -(diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<

    ],

]




"""middle_lead has no rightTouchingBox and no leftTouchingBox, too close to solder anything

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


#middle_lead
length = middle_lead_length
diameter = middle_lead_diameter
yStart = middle_lead_yStart
xzCentre = middle_lead_xzCentre

solderableLeads += [

    #right_lead
    [

        ([#down_touchingBox # down -> up
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  (diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  (diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  -(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  -(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart-(length*(1/4)), 0), #startPoint
            (xzCentre, yStart, 0)  #endPoint
        )),
#<<<<<<<<<<<<


        ([#in_touchingBox # in -> out
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), (diameter*(1/2))+(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), (diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<

        ([#out_touchingBox out -> in
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), -(diameter*(1/2))-(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), -(diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<


    ],
]



"""right_lead has no leftTouchingBox too close to solder anything

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


#right_lead +ve (longer)
length = right_lead_length
diameter = right_lead_diameter
yStart = right_lead_yStart
xzCentre = right_lead_xzCentre

solderableLeads += [

    #right_lead
    [
        ([#right_touchingBox # right -> left
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (right, up, out)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (left, up, out)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, down, out)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre+(diameter*(1/2))+(diameter*(1/2)), yStart+(length*(1/2)), 0), #startPoint
            (xzCentre+(diameter*(1/2)), yStart+(length*(1/2)), 0)  #endPoint
        )),
#<<<<<<<<<<<<


        ([#down_touchingBox # down -> up
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  (diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  (diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  -(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  -(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart-(length*(1/4)), 0), #startPoint
            (xzCentre, yStart, 0)  #endPoint
        )),
#<<<<<<<<<<<<


        ([#in_touchingBox # in -> out
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  (diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2))+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  (diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), (diameter*(1/2))+(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), (diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<

        ([#out_touchingBox out -> in
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  -(diameter*(1/2))-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), -(diameter*(1/2))-(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), -(diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<


    ],
]




if __name__=='__main__':
    name = 'Transistor'
    print(f'generating Component{name} from UserPreset datum')
    from foundation.nDisplay.sampler.genTHREEMesh.reader.threecomponentgenerator import THREEComponentGenerator
    THREEComponentGenerator().generateMeshFile(name, listOfVertices, listOfIndices, listOfColors, solderableLeads)