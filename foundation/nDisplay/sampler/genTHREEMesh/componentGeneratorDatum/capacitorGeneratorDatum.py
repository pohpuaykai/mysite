import os

from foundation.nDisplay.sampler.bottomupsampler import BottomUpSampler

"""
Panasonic Aluminium Electrolytic Capacitors (Radial Lead Type)
Radial Lead Type
Series: M Type: A

Cap. (mF) = 220

Diameter of body = 5.5 mm
Length of body = 12 mm
Diameter of left_lead = 0.55 mm
Length of left_lead = 14 mm
Diameter of right_lead = 0.55 mm
Length of right_lead = 17 mm
"""



def bodyColorFunction(x, y, z, u, v):
    if (3*math.pi/12)<=v and v<=(4*math.pi/12):
        return (192, 192, 192)
    return (0, 0, 0) # defaultColor
def leftLeadColorFunction(x, y, z, u, v):
    return (192, 192, 192)
def rightLeadColorFunction(x, y, z, u, v):
    return (192, 192, 192)
import math; theMathModule = locals()['math'];

left_lead_length = 14
left_lead_diameter = 0.55
right_lead_length = 17
right_lead_diameter = 0.55

left_lead_yStart = -left_lead_length
left_lead_xzCentre = -1
right_lead_yStart = -right_lead_length
right_lead_xzCentre = 1


listOfVertices, listOfIndices, listOfColors = BottomUpSampler.bottomUpPieceWiseSampler([
    {#body of the capacitor
        'uStart':0,
        'uEnd':12,
        'uStep':0.1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-math.pi,
        'vEnd':math.pi,
        'vStep':math.pi/12,
        'xFormulaLambda':lambda v, y: eval('5.5*(math.sqrt(1-(math.pow(X , 4)))-0.1*math.exp(-math.pow(8*(X+0.43), 2)))*math.cos(v)', locals={'v':v, 'X': (y-((0+12)/2))/(12-0), 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('5.5*(math.sqrt(1-(math.pow(X , 4)))-0.1*math.exp(-math.pow(8*(X+0.43), 2)))*math.sin(v)', locals={'v':v, 'X': (y-((0+12)/2))/(12-0), 'math':theMathModule}),
        'colorFunction':bodyColorFunction
    },
    {#left lead -ve (shorter)
        'uStart':left_lead_yStart,#'uStart':-left_lead_length,
        'uEnd':left_lead_yStart+left_lead_length,#'uEnd':0,
        'uStep':1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-math.pi,
        'vEnd':math.pi,
        'vStep':math.pi/12,
        'xFormulaLambda':lambda v, y: eval('0.5*left_lead_diameter*math.cos(v)+left_lead_xzCentre', locals={'v':v, 'y':y, 'left_lead_diameter':left_lead_diameter, 'left_lead_xzCentre':left_lead_xzCentre, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('0.5*left_lead_diameter*math.sin(v)+left_lead_xzCentre', locals={'v':v, 'y':y, 'left_lead_diameter':left_lead_diameter, 'left_lead_xzCentre':left_lead_xzCentre, 'math':theMathModule}),
        'colorFunction':leftLeadColorFunction
    },
    {#right lead +ve (longer)
        'uStart':right_lead_yStart,#'uStart':-17,
        'uEnd':right_lead_yStart+right_lead_length,#'uEnd':0,
        'uStep':1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-math.pi,
        'vEnd':math.pi,
        'vStep':math.pi/12,
        'xFormulaLambda':lambda v, y: eval('0.5*right_lead_diameter*math.cos(v)+right_lead_xzCentre', locals={'v':v, 'y':y, 'right_lead_diameter':right_lead_diameter, 'right_lead_xzCentre':right_lead_xzCentre, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('0.5*right_lead_diameter*math.sin(v)+right_lead_xzCentre', locals={'v':v, 'y':y, 'right_lead_diameter':right_lead_diameter, 'right_lead_xzCentre':right_lead_xzCentre, 'math':theMathModule}),
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
in = xzCentre+(diameter*(1/2))
out = xzCentre-(diameter*(1/2))


right_touchingBox
down = yStart
up = yStart+length
left = xzCentre+(diameter*(1/2))
right = xzCentre+(diameter*(1/2))+(diameter*(1/2))
in = xzCentre+(diameter*(1/2))
out = xzCentre-(diameter*(1/2))


down_touchingBox
down = yStart-(length*(1/4))
up = yStart
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = xzCentre+(diameter*(1/2))
out = xzCentre-(diameter*(1/2))


in_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = xzCentre+(diameter*(1/2))+(diameter*(1/2))
out = xzCentre+(diameter*(1/2))


out_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = xzCentre-(diameter*(1/2))
out = xzCentre-(diameter*(1/2))-(diameter*(1/2))

"""


solderableLeads = [
    #left_lead
    [
        ([#left_touchingBox #left -> right
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre-(diameter*(1/2))-(diameter*(1/2)), yStart+(length*(1/2)), xzCentre), #startPoint
            (xzCentre-(diameter*(1/2)), yStart+(length*(1/2)), xzCentre)  #endPoint
        )),
#<<<<<<<<<<<<

        ([#right_touchingBox #right -> left <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (right, up, out)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (left, up, out)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (right, down, out)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre+(diameter*(1/2))+(diameter*(1/2)), yStart+(length*(1/2)), xzCentre), #startPoint
            (xzCentre+(diameter*(1/2)), yStart+(length*(1/2)), xzCentre)  #endPoint
        )),
#<<<<<<<<<<<<

        ([#down_touchingBox # down -> up
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  xzCentre+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  xzCentre+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  xzCentre-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  xzCentre-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart-(length*(1/4)), xzCentre), #startPoint
            (xzCentre, yStart, xzCentre)  #endPoint
        )),
#<<<<<<<<<<<<


        ([#in_touchingBox # in -> out
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2))+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2))+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2))+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2))+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), xzCentre+(diameter*(1/2))+(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), xzCentre+(diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<

        ([#out_touchingBox # out -> in
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2))-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2))-(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2))-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2))-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), xzCentre-(diameter*(1/2))-(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), xzCentre-(diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<

    ],

]



"""left|right<->down|up

right_touchingBox
down = yStart
up = yStart+length
left = xzCentre+(diameter*(1/2))
right = xzCentre+(diameter*(1/2))+(diameter*(1/2))
in = xzCentre+(diameter*(1/2))
out = xzCentre-(diameter*(1/2))


left_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))-(diameter*(1/2))
right = xzCentre-(diameter*(1/2))
in = xzCentre+(diameter*(1/2))
out = xzCentre-(diameter*(1/2))


down_touchingBox
down = yStart-(length*(1/4))
up = yStart
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = xzCentre+(diameter*(1/2))
out = xzCentre-(diameter*(1/2))


in_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = xzCentre+(diameter*(1/2))+(diameter*(1/2))
out = xzCentre+(diameter*(1/2))


out_touchingBox
down = yStart
up = yStart+length
left = xzCentre-(diameter*(1/2))
right = xzCentre+(diameter*(1/2))
in = xzCentre-(diameter*(1/2))
out = xzCentre-(diameter*(1/2))-(diameter*(1/2))

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
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (right, up, out)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (left, up, out)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2))+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (right, down, out)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre+(diameter*(1/2))+(diameter*(1/2)), yStart+(length*(1/2)), xzCentre), #startPoint
            (xzCentre+(diameter*(1/2)), yStart+(length*(1/2)), xzCentre)  #endPoint
        )),
#<<<<<<<<<<<<

        ([#left_touchingBox # left -> right
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2))-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre-(diameter*(1/2))-(diameter*(1/2)), yStart+(length*(1/2)), xzCentre), #startPoint
            (xzCentre-(diameter*(1/2)), yStart+(length*(1/2)), xzCentre)  #endPoint
        )),
#<<<<<<<<<<<<

        ([#down_touchingBox # down -> up
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  xzCentre+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  xzCentre+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  xzCentre-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart-(length*(1/4)) ,  xzCentre-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart-(length*(1/4)), xzCentre), #startPoint
            (xzCentre, yStart, xzCentre)  #endPoint
        )),
#<<<<<<<<<<<<


        ([#in_touchingBox # in -> out
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2))+(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2))+(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre+(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2))+(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2))+(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre+(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), xzCentre+(diameter*(1/2))+(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), xzCentre+(diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<

        ([#out_touchingBox out -> in
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (left, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2)) ), # (right, up, inx)
( xzCentre+(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2))-(diameter*(1/2)) ), # (right, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart+length ,  xzCentre-(diameter*(1/2))-(diameter*(1/2)) ), # (left, up, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (left, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2)) ), # (right, down, inx)
( xzCentre+(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2))-(diameter*(1/2)) ), # (right, down, out)
( xzCentre-(diameter*(1/2)) ,  yStart ,  xzCentre-(diameter*(1/2))-(diameter*(1/2)) ), # (left, down, out)
        ], 
        (
            (xzCentre, yStart+(length*(1/2)), xzCentre-(diameter*(1/2))-(diameter*(1/2))), #startPoint
            (xzCentre, yStart+(length*(1/2)), xzCentre-(diameter*(1/2)))  #endPoint
        )),
#<<<<<<<<<<<<


    ],
]




if __name__=='__main__':
    name = 'Capacitor'
    print(f'generating Component{name} from UserPreset datum')
    from foundation.nDisplay.sampler.genTHREEMesh.reader.threecomponentgenerator import THREEComponentGenerator
    THREEComponentGenerator().generateMeshFile('Capacitor', listOfVertices, listOfIndices, listOfColors, solderableLeads)