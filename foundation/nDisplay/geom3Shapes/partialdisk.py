import OpenGL.GLU as glu


def partialDisk(internalRadius, externalRadius, slices, rings, startAngle, angle, drawStyle):
    partialDiskQ = glu.gluNewQuadric()
    gl.glPushMatrix() # save first position
    glu.gluQuadricDrawStyle(partialDiskQ, drawStyle)
    #https://learn.microsoft.com/en-us/windows/win32/opengl/glupartialdisk
    #https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluPartialDisk.xml
    glu.gluPartialDisk(partialDiskQ, internalRadius, externalRadius, slices, rings, startAngle, angle)
    #glu.gluDeleteQuadric(partialDiskQ);
    gl.glPopMatrix() # load first position

