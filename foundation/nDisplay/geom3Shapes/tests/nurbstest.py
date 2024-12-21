import inspect
import pprint


from foundation.nDisplay.core.stage import Stage

pp = pprint.PrettyPrinter(indent=4)


def test__nurbs__basic(verbose=False):

    from foundation.nDisplay.geom3Shapes.nurbs import nurbsSurface
    import OpenGL.GL as gl
    def piece():
        #from "OpenGL/GLU/glunurbs.py", MAX_ORDER = 8
        #order-3 polynomial are recommendsed by Rhino-CAD software developers
        sKnots = []#for order-3 polynomial, len(sKnots) - length = 3[order], len(sKnots) < 2* (len(sKnots) - length) => 2*length < len(sKnots)
        #2*length < length +3 => length < 3[order]
        #2 * (len(sKnots) - 3) < len(sKnots) => len(sKnots) < 2 * 3[order]
        tKnots = []#for order-3 polynomial, len(tKnots) - width = 3
        control = [#length
            [#width
                [],#step
                []
            ],
            [
                [],
                []
            ],
        ]
        type = gl.GL_MAP2_VERTEX_3
        nurbsSurface(sKnots, tKnots, control, type)
    width = 800
    height = 600
    metronome = 10
    displayCaption = "Nurbs testing"
    fieldOfView = 45
    zNear = 0.1
    zFar = 50
    verbose = False
    stage = Stage(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ') # visual Human Interaction, hard to ...
    if verbose:
        pp.pprint(subTree)


if __name__=='__main__':
    test__nurbs__basic(True) # not passed yet