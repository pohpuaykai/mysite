"""

https://stackoverflow.com/questions/5988686/creating-a-3d-sphere-in-opengl-using-visual-c/5989676#5989676  <<<jagged sphere

http://jerome.jouvie.free.fr/opengl-tutorials/Tutorial7.php  <<< has 'cut-and-paste code' for sphere... but pyGame library does not have those functions?
"""
import OpenGL.GL as gl
import OpenGL.GLU as glu

def sphere(radius, slices, rings, drawStyle):
    sphereQ = glu.gluNewQuadric()
    gl.glPushMatrix() # save first position
    glu.gluQuadricDrawStyle(sphereQ, drawStyle)
    #https://learn.microsoft.com/en-us/windows/win32/opengl/glusphere
    #https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluSphere.xml
    glu.gluSphere(sphereQ, radius, slices, rings) 
    #glu.gluDeleteQuadric(sphereQ);
    gl.glPopMatrix() # load first position

