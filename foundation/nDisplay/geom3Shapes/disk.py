import random

import OpenGL.GL as gl
import OpenGL.GLU as glu

def disk(internalRadius, externalRadius, slices, rings, drawStyle, colors):
    """

    #TODO need to convert to Mesh to be compatible
    """
    x = 0
    diskQ = glu.gluNewQuadric()
    gl.glPushMatrix() # save first position

    x+= random.randint(0, len(colors)-1)# this is shimmering.... but not 'continous(gradient) colors'
    x = x% len(colors)
    # print(x)
    gl.glColor3fv(colors[x])# this is flashing.... but not 'continous(gradient) colors' & cannot use vertices to select source of color change...

    glu.gluQuadricDrawStyle(diskQ, drawStyle)
    #https://learn.microsoft.com/en-us/windows/win32/opengl/gludisk
    #https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluDisk.xml
    glu.gluDisk(diskQ, internalRadius, externalRadius, slices, rings)
    #glu.gluDeleteQuadric(diskQ);
    gl.glPopMatrix() # load first position


