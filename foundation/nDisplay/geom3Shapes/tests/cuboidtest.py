import inspect
import pprint


from foundation.nDisplay.core.stage import Stage

pp = pprint.PrettyPrinter(indent=4)


def test__cuboid__basic(verbose=False):
    #TODO clean up from stagetest.py
    #TODO actually a resistor is more like a long long disk?
    from foundation.nDisplay.geom3Shapes.cylinder import cylinder
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
        cylinder(baseRadius, topRadius, height, slices, stacks, texture, drawStyle, normals, orientation)
    width = 800
    height = 600
    metronome = 10
    displayCaption = "Cylinder testing"
    fieldOfView = 45
    zNear = 0.1
    zFar = 50
    verbose = False
    stage = Stage(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ') # visual Human Interaction, hard to ...
    if verbose:
        pp.pprint(subTree)


if __name__=='__main__':
    test__cuboid__basic(True) # not passed yet