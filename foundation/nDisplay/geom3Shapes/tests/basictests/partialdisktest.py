import inspect
import pprint


from foundation.nDisplay.core.stage import Stage

from foundation.nDisplay.geom3Shapes.partialdisk import partialDisk
import OpenGL.GL as gl
import OpenGL.GLU as glu

pp = pprint.PrettyPrinter(indent=4)


def test__partialdisk__basic(verbose=False):
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
        internalRadius = 0.5
        externalRadius = 0.9
        slices = 3
        rings = 3
        startAngle = 0
        angle = 20
        drawStyle = glu.GLU_FILL
        partialDisk(internalRadius, externalRadius, slices, rings, startAngle, angle, drawStyle, colors)
    width = 800
    height = 600
    metronome = 10
    displayCaption = "PartialDisk testing"
    fieldOfView = 45
    zNear = 0.1
    zFar = 50
    verbose = False
    stage = Stage(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)
    # print(inspect.currentframe().f_code.co_name, ' PASSED? ') # visual Human Interaction, hard to ...


if __name__=='__main__':
    test__partialdisk__basic(True) # not passed yet