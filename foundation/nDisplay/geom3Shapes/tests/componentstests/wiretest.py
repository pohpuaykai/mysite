import inspect
import pprint


from foundation.nDisplay.core.stage import Stage



from foundation.nDisplay.geom3Shapes.nurbs import nurbsSurface
from foundation.nDisplay.geom3Shapes.cylinder import cylinder
import numpy as np
from OpenGL import arrays
import OpenGL.GL as gl

def wire(p0, p1, shapesToAvoid, innerRadius, outerRadius):
    """
    p0 and p1 are 3-tuples that are two points in space
    so the wires are supposed to go from p0 to p1
    
    But the wire have to avoid all the things in shapesToAvoid,
    things, things in shapesToAvoid can be:
    1. cuboids
    2. cylinders
    3. spheres

    wires also have an 
    1. innerRadius (insulator)
    2. outerRadius (conductor)


    """
    pass


if __name__=='__main__':
    wire()