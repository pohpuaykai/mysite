import inspect
import pprint


from foundation.nDisplay.core.stage import Stage

pp = pprint.PrettyPrinter(indent=4)


def test__partialdisk__basic(verbose=False):
    from foundation.nDisplay.geom3Shapes.partialdisk import partialdisk
    def piece():
        internalRadius = 5.0
        externalRadius = 9.0
        slices = 3
        rings = 3
        startAngle = 0
        angle = 20
        drawStyle = glu.GLU_FILL
        partialDisk(internalRadius, externalRadius, slices, rings, startAngle, angle, drawStyle)
    width = 800
    height = 600
    metronome = 10
    displayCaption = "PartialDisk testing"
    fieldOfView = 45
    zNear = 0.1
    zFar = 50
    verbose = False
    stage = Stage(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ') # visual Human Interaction, hard to ...
    if verbose:
        pp.pprint(subTree)


if __name__=='__main__':
    test__partialdisk__basic(True) # not passed yet