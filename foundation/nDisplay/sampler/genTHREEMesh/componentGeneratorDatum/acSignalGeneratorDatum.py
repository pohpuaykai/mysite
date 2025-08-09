import os

from foundation.nDisplay.sampler.bottomupsampler import BottomUpSampler

"""
NOT REAL

Diameter of body = 140 mm
Length of body = 50 mm
Diameter of left_lead = 0.7 mm
Length of left_lead = 30 mm
Diameter of right_lead = 0.7 mm
Length of right_lead = 30 mm
"""



def realRoot(number, power):
    if number < 0:
        return -math.pow(abs(number), 1/power)
    else:
        return math.pow(number, 1/power)

def bodyColorFunction(x, y, z, u, v):
    # if (3*math.pi/12)<=v and v<=(4*math.pi/12):
    #     return (192, 192, 192)
    return (10, 10, 10) # defaultColor, light-black
def leftLeadColorFunction(x, y, z, u, v):
    return (192, 192, 192)#silver-grey
def rightLeadColorFunction(x, y, z, u, v):
    return (192, 192, 192)#silver-grey
import math; theMathModule = locals()['math'];

body_diameter = 140
body_length = 50

left_lead_length = 30
left_lead_diameter = 0.7
right_lead_length = 30
right_lead_diameter = 0.7

left_lead_yStart = -left_lead_length
left_lead_xzCentre = -10
right_lead_yStart = -right_lead_length
right_lead_xzCentre = 10


listOfVertices, listOfIndices, listOfColors = BottomUpSampler.bottomUpPieceWiseSampler([
    {#body of the signalGenerator
        'uStart':0,
        'uEnd':body_length,
        'uStep':1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-1,
        'vEnd':1,
        'vStep':1/36,
        'xFormulaLambda':lambda v, y: eval('(body_diameter/2)*(math.sqrt(1-(math.pow(X , 32))))*realRoot(math.cos(math.pi*v), 3)', locals={'v':v, 'X': (y/(body_length-0)), 'body_diameter':body_diameter, 'realRoot':realRoot, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('(body_diameter/2)*(math.sqrt(1-(math.pow(X , 32))))*math.sin(math.pi*v)', locals={'v':v, 'X': (y/(body_length-0)), 'body_diameter':body_diameter, 'realRoot':realRoot, 'math':theMathModule}),
        'colorFunction':bodyColorFunction
    },
    {#left lead 
        'uStart':left_lead_yStart,#'uStart':-left_lead_length,
        'uEnd':left_lead_yStart+left_lead_length,#'uEnd':0,
        'uStep':1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-math.pi,
        'vEnd':math.pi,
        'vStep':math.pi/12,
        'xFormulaLambda':lambda v, y: eval('0.5*left_lead_diameter*math.cos(v)+left_lead_xzCentre', locals={'v':v, 'y':y, 'left_lead_diameter':left_lead_diameter, 'left_lead_xzCentre':left_lead_xzCentre, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('0.5*left_lead_diameter*math.sin(v)', locals={'v':v, 'y':y, 'left_lead_diameter':left_lead_diameter, 'left_lead_xzCentre':left_lead_xzCentre, 'math':theMathModule}),
        'colorFunction':leftLeadColorFunction
    },
    {#right lead 
        'uStart':right_lead_yStart,#'uStart':-17,
        'uEnd':right_lead_yStart+right_lead_length,#'uEnd':0,
        'uStep':1,
        'yFormulaLambda':lambda u: eval('u', locals={'u':u, 'math':theMathModule}),
        'vStart':-math.pi,
        'vEnd':math.pi,
        'vStep':math.pi/12,
        'xFormulaLambda':lambda v, y: eval('0.5*right_lead_diameter*math.cos(v)+right_lead_xzCentre', locals={'v':v, 'y':y, 'right_lead_diameter':right_lead_diameter, 'right_lead_xzCentre':right_lead_xzCentre, 'math':theMathModule}),
        'zFormulaLambda':lambda v, y: eval('0.5*right_lead_diameter*math.sin(v)', locals={'v':v, 'y':y, 'right_lead_diameter':right_lead_diameter, 'right_lead_xzCentre':right_lead_xzCentre, 'math':theMathModule}),
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
{
    'touchingFaceCoordinates':[
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



    'touchingCoordinate':(xzCentre, yStart, 0), #middle of downFace


}


    

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
{
    'touchingFaceCoordinates':[
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



    'touchingCoordinate':(xzCentre, yStart, 0),  #middle of downFace



}



    
]


positiveLeadsDirections = [(0, 1)] # if leftSolderableLead to rightSolderableLead, the positive, numbers are indices of solderableLeads


if __name__=='__main__':
    name = 'ACSignalGenerator'
    type = 'AC_signal_generator'
    print(f'generating Component{name} from UserPreset datum')
    from foundation.nDisplay.sampler.genTHREEMesh.reader.threecomponentgenerator import THREEComponentGenerator
    THREEComponentGenerator().generateMeshFile(name, type, listOfVertices, listOfIndices, listOfColors, solderableLeads, positiveLeadsDirections)