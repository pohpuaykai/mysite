import OpenGL.GL as gl
import OpenGL.GLU as glu

def disk(internalRadius, externalRadius, slices, rings, drawStyle):
    diskQ = glu.gluNewQuadric()
    gl.glPushMatrix() # save first position
    glu.gluQuadricDrawStyle(diskQ, drawStyle)
    #https://learn.microsoft.com/en-us/windows/win32/opengl/gludisk
    #https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluDisk.xml
    glu.gluDisk(diskQ, internalRadius, externalRadius, slices, rings)
    #glu.gluDeleteQuadric(diskQ);
    gl.glPopMatrix() # load first position


