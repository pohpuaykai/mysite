import inspect
import pprint


from foundation.nDisplay.core.stage import Stage

pp = pprint.PrettyPrinter(indent=4)


def test__sphere__basic(verbose=False):
    from foundation.nDisplay.geom3Shapes.sphere import sphere
    def piece():
        radius = 0.5
        slices = 20
        rings = 20
        drawStyle = glu.GLU_FILL
        sphere(radius, slices, rings, drawStyle)
    width = 800
    height = 600
    metronome = 10
    displayCaption = "Sphere testing"
    fieldOfView = 45
    zNear = 0.1
    zFar = 50
    verbose = False
    stage = Stage(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)

    print(inspect.currentframe().f_code.co_name, ' PASSED? ') # visual Human Interaction, hard to ...
    if verbose:
        pp.pprint(subTree)


if __name__=='__main__':
    test__sphere__basic(True) # not passed yet