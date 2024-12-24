import inspect
import pprint


from foundation.nDisplay.core.stage import Stage

from foundation.nDisplay.geom3Shapes.disk import disk
import OpenGL.GL as gl
import OpenGL.GLU as glu

pp = pprint.PrettyPrinter(indent=4)


def test__disk__basic(verbose=False):
    #TODO actually a resistor is more like a long long disk?
    def piece():
        internalRadius = 0.5
        externalRadius = 0.9
        slices = 3
        rings = 3
        drawStyle = glu.GLU_FILL
        disk(internalRadius, externalRadius, slices, rings, drawStyle)
    width = 800
    height = 600
    metronome = 10
    displayCaption = "Disk testing"
    fieldOfView = 45
    zNear = 0.1
    zFar = 50
    verbose = False
    stage = Stage(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)
    # print(inspect.currentframe().f_code.co_name, ' PASSED? ') # visual Human Interaction, hard to ...


if __name__=='__main__':
    test__disk__basic(True) # not passed yet