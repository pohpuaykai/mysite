import inspect
import pprint


from foundation.nDisplay.core.stage import Stage



from foundation.nDisplay.geom3Shapes.nurbs import nurbsSurface
import numpy as np
from OpenGL import arrays
import OpenGL.GL as gl

    
pp = pprint.PrettyPrinter(indent=4)


def test__nurbs__basic(verbose=False):


    def buildControlPoints():
        """
        Courtsey of http://bazaar.launchpad.net/~mcfletch/openglcontext/trunk/view/head:/tests/redbook_surface.py

        
        #from "OpenGL/GLU/glunurbs.py", MAX_ORDER = 8
        #order-3 polynomial are recommended by Rhino-CAD software developers
        # tKnots = []#for order-3 polynomial, len(tKnots) - width = 3
        #for order-3 polynomial, len(sKnots) - length = 3[order], len(sKnots) < 2* (len(sKnots) - length) => 2*length < len(sKnots)
        # #2*length < length +3 => length < 3[order]
        # #2 * (len(sKnots) - 3) < len(sKnots) => len(sKnots) < 2 * 3[order]
        # this means that 
        # 1. len(control) <= 8
        # 2. len(sKnots) <= 16 and len(tKnots) <= 16


        This function generates a constant3D array of 
        [#length
            [#width
              [-3. -3. -3.]#step
              [-3. -1. -3.]
              [-3.  1. -3.]
              [-3.  3. -3.]
            ]

            [
              [-1. -3. -3.]
              [-1. -1.  3.]
              [-1.  1.  3.]
              [-1.  3. -3.]
            ]

            [
              [ 1. -3. -3.]
              [ 1. -1.  3.]
              [ 1.  1.  3.]
              [ 1.  3. -3.]
            ]

            [
              [ 3. -3. -3.]
              [ 3. -1. -3.]
              [ 3.  1. -3.]
              [ 3.  3. -3.]
            ]
        ]

        #which means the restriction of PyOpenGL
        """
        ctlpoints = arrays.GLfloatArray.zeros((4, 4, 3))
        for u in range( 4 ):
            for v in range( 4 ):
                ctlpoints[u][v][0] = 2.0*(u - 1.5)
                ctlpoints[u][v][1] = 2.0*(v - 1.5)
                if (u == 1 or u == 2) and (v == 1 or v == 2):
                    ctlpoints[u][v][2] = 3.0
                else:
                    ctlpoints[u][v][2] = -3.0
        return ctlpoints

    """
https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/glMaterial.xml

    face
    Specifies which face or faces are being updated. Must be one of GL_FRONT, GL_BACK, or GL_FRONT_AND_BACK.

    pname
    Specifies the material parameter of the face or faces that is being updated. Must be one of GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_EMISSION, GL_SHININESS, GL_AMBIENT_AND_DIFFUSE, or GL_COLOR_INDEXES.

    params
    Specifies a pointer to the value or values that pname will be set to.
    """
    #gl.glMaterialfv(gl.GL_FRONT, gl.GL_DIFFUSE, np.array([0.7, 0.7, 0.7, 1.0],'f'));
    #gl.glMaterialfv(gl.GL_FRONT, gl.GL_SPECULAR, np.array([1.0, 1.0, 1.0, 1.0],'f'));
    #gl.glMaterialfv(gl.GL_FRONT, gl.GL_SHININESS, np.array([100.0],'f'));

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
        # sKnots = []
        
        
        
        # control = [#length
        #     [#width
        #         [],#step
        #         []
        #     ],
        #     [
        #         [],
        #         []
        #     ],
        # ]
        sKnots = np.array([0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0], "f")
        tKnots = np.array([0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0], "f")
        control = buildControlPoints()
        type = gl.GL_MAP2_VERTEX_3
        nurbsSurface(sKnots, tKnots, control, type, colors)
    width = 800
    height = 600
    metronome = 10
    displayCaption = "Nurbs testing"
    fieldOfView = 45
    zNear = 0.1
    zFar = 50
    verbose = False
    stage = Stage(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)
    # print(inspect.currentframe().f_code.co_name, ' PASSED? ') # visual Human Interaction, hard to ...


if __name__=='__main__':
    test__nurbs__basic(True) # not passed yet