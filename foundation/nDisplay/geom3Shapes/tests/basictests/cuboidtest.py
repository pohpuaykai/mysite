import inspect
import pprint


from foundation.nDisplay.core.stage import Stage
from foundation.nDisplay.common.vectordimensioncounter import ColorCounter

from foundation.nDisplay.geom3Shapes.cuboid import cube
import OpenGL.GL as gl
import OpenGL.GLU as glu

pp = pprint.PrettyPrinter(indent=4)


def test__cuboid__basic(verbose=False):
    #TODO clean up from stagetest.py
    #TODO actually a resistor is more like a long long disk?
    width = 800
    height = 600
    #START: drawing cube
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
    )

    #surface
    surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

    #colors (jerky colors)
    # colors = (
    # (1,0,0),
    # (0,1,0),
    # (0,0,1),
    # (0,1,0),
    # (1,1,1),
    # (0,1,1),
    # (1,0,0),
    # (0,1,0),
    # (0,0,1),
    # (1,0,0),
    # (1,1,1),
    # (0,1,1),
    # )
    #TODO refactor ....
    class colorarray:
        def __init__(self):
            self.cc = ColorCounter()
        def __getitem__(self, key):
            return self.cc.next()
    #
    colors = colorarray()
    def piece():
        cube(vertices, edges, surfaces, colors)
    width = 800
    height = 600
    metronome = 10
    displayCaption = "Cuboid testing"
    fieldOfView = 45
    zNear = 0.1
    zFar = 50
    verbose = False
    stage = Stage(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)
    # print(inspect.currentframe().f_code.co_name, ' PASSED? ') # visual Human Interaction, hard to ...


if __name__=='__main__':
    test__cuboid__basic(True) # not passed yet