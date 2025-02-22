import inspect
import pprint


from foundation.nDisplay.core.stage import Stage

from foundation.nDisplay.geom3Shapes.cylinder import cylinder
import OpenGL.GL as gl
import OpenGL.GLU as glu

pp = pprint.PrettyPrinter(indent=4)


def test__cylinder__basic(verbose=False):
    #TODO actually a resistor is more like a long long disk?
    #colors
    colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )
    def piece():
        baseRadius = 1
        topRadius = 1
        height = 3
        slices = 20
        stacks = 20
        texture = False
        drawStyle = glu.GLU_FILL
        normals = glu.GLU_SMOOTH
        orientation = glu.GLU_INSIDE
        #gl.glColor3fv((1, 0, 0)) # colors the inside/outside of the cylinder (1, 0, 0)
        #material has no effect... maybe because no light source...
        #gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT, [0.7, 0.7, 0.7, 0.5]) #http://jerome.jouvie.free.fr/opengl-tutorials/Tutorial14.php
        cylinder(baseRadius, topRadius, height, slices, stacks, texture, drawStyle, normals, orientation, colors)
    width = 800
    height = 600
    metronome = 10
    displayCaption = "Cylinder testing"
    fieldOfView = 45
    zNear = 0.1
    zFar = 50
    verbose = False
    stage = Stage(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)
    # print(inspect.currentframe().f_code.co_name, ' PASSED? ') # visual Human Interaction, hard to ...


if __name__=='__main__':
    test__cylinder__basic(True) # not passed yet