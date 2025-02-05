import random

import OpenGL.GLU as glu
import OpenGL.GL as gl

import numpy as np

def nurbsSurface(sKnots, tKnots, control, type, colors):
    """
    #TODO need to convert to Mesh to be compatible
    
    Resources for NURBS
    https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluNurbsCurve.xml
    https://stackoverflow.com/questions/13500458/opengl-nurbs-surface
    https://courses.cs.duke.edu/fall05/cps124/notes/10_curves/opengl_nurbs.pdf
    https://en.wikibooks.org/wiki/OpenGL_Programming/Modern_OpenGL_Tutorial_07

    https://www.ibm.com/docs/en/aix/7.1?topic=library-glunurbssurface-subroutine
    https://pyopengl.sourceforge.net/documentation/manual-3.0/gluNurbsSurface.html
    http://bazaar.launchpad.net/~mcfletch/openglcontext/trunk/view/head:/tests/redbook_trim.py
    http://bazaar.launchpad.net/~mcfletch/openglcontext/trunk/view/head:/tests/redbook_surface.py
    http://bazaar.launchpad.net/~mcfletch/openglcontext/trunk/view/head:/tests/redbook_surface_cb.py
    http://bazaar.launchpad.net/~mcfletch/openglcontext/trunk/view/head:/OpenGLContext/scenegraph/nurbs.py
    http://bazaar.launchpad.net/~mcfletch/pyopengl-demo/trunk/view/head:/PyOpenGL-Demo/GLUT/molehill.py
    http://bazaar.launchpad.net/~mcfletch/pyopengl-demo/trunk/view/head:/PyOpenGL-Demo/proesch/nurbs/nurbs.py


    OpenGL/GLU/glunurbs.py


    number of knots = #control_points + #order

    degreeOfNurbsCurve = #knots - #controlPoints - 1
    the larger the degreeOfNurbsCurve, the 'flatter' is the curve, the smaller the degreeOfNurbsCurve
    (at least 1) the more like a jagged line sticking to the polyline connecting controlPoints

    So, if degreeOfNurbsCurve=1, the curve will cross all the controlPoints, else the curve will only
    pass through control[0] and control[-1]

    :param sKnots: list of knots, values must be non-decreasing sequence between 0 and 1
    :type sKnots: list[float]

    :param tKnots: list of knots, values must be non-decreasing sequence between 0 and 1
    :type tKnots: list[float]
    
    :param control: 
    :type control:Specifies a pointer to an 3darray(array2 of array1 of array0) of control points. 
    each control point is a tuple of (x, y, z) in the Cartesian
    len(array0) = length = len(sKnots) - sOrder = #controlpoints
    len(array1) = width = len(tKnots) - tOrder = #controlpoints
    len(array2) = step

    sStride = width * step
    tStride = step

    :param type:
    from the original documentation (https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluNurbsSurface.xml):
    Specifies type of the surface. type can be any of the valid two-dimensional evaluator types (such as GL_MAP2_TEXTURE_COORD_2 or GL_MAP2_NORMAL or GL_MAP2_VERTEX_4).


    from OpenGL/GLU/glunurbs.py, we can see that (def gluNurbsCurve) just takes 'type' input from user, then 
    gives it directly to the raw OpenGL-function "baseFunction" (created by OpenGL/raw/GLU/__init__.py platform.createBaseFunction)
    so the direct documention (https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluNurbsSurface.xml) of 'type' should
    correspond to pyGame.OpenGL 'type' and it seems that any ENUM with prefix GL_MAP2_ will fit into this crevice.
    A quick search using Sublime, on the OpenGL library with searchTerm "GL_MAP2_", reveals these:
    GL_MAP2_BINORMAL_EXT
    GL_MAP2_COLOR_4
    GL_MAP2_GRID_DOMAIN
    GL_MAP2_GRID_SEGMENTS
    GL_MAP2_INDEX
    GL_MAP2_NORMAL
    GL_MAP2_TANGENT_EXT
    GL_MAP2_TEXTURE_COORD_1
    GL_MAP2_TEXTURE_COORD_2
    GL_MAP2_TEXTURE_COORD_3
    GL_MAP2_TEXTURE_COORD_4
    GL_MAP2_VERTEX_3
    GL_MAP2_VERTEX_4
    GL_MAP2_VERTEX_ATTRIB0_4_NV
    GL_MAP2_VERTEX_ATTRIB10_4_NV
    GL_MAP2_VERTEX_ATTRIB11_4_NV
    GL_MAP2_VERTEX_ATTRIB12_4_NV
    GL_MAP2_VERTEX_ATTRIB13_4_NV
    GL_MAP2_VERTEX_ATTRIB14_4_NV
    GL_MAP2_VERTEX_ATTRIB15_4_NV
    GL_MAP2_VERTEX_ATTRIB1_4_NV
    GL_MAP2_VERTEX_ATTRIB2_4_NV
    GL_MAP2_VERTEX_ATTRIB3_4_NV
    GL_MAP2_VERTEX_ATTRIB4_4_NV
    GL_MAP2_VERTEX_ATTRIB5_4_NV
    GL_MAP2_VERTEX_ATTRIB6_4_NV
    GL_MAP2_VERTEX_ATTRIB7_4_NV
    GL_MAP2_VERTEX_ATTRIB8_4_NV
    GL_MAP2_VERTEX_ATTRIB9_4_NV

    :type type: GLenum(type)
    """
    x=0
    nurbs = glu.gluNewNurbsRenderer()
    glu.gluBeginSurface(nurbs)
    #3 together also does nothing., putting at def piece of nurbstest also does nothing
    """MIGHT BE BECAUSE OF THESE:


        glEnable(GL_AUTO_NORMAL);
        glEnable(GL_NORMALIZE);

        gluNurbsProperty(self.theNurb, GLU_SAMPLING_TOLERANCE, 25.0);
        gluNurbsProperty(self.theNurb, GLU_DISPLAY_MODE, GLU_FILL);


        [from http://bazaar.launchpad.net/~mcfletch/openglcontext/trunk/view/head:/tests/redbook_surface.py]

        https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/glColorMaterial.xml
        says: glColorMaterial is  prefered to glMaterialfv
    """
    # gl.glMaterialfv(gl.GL_FRONT, gl.GL_DIFFUSE, np.array([0.7, 0.7, 0.7, 1.0],'f')); # seems to do nothing, both sides of the nurbs still white
    # gl.glMaterialfv(gl.GL_FRONT, gl.GL_SPECULAR, np.array([1.0, 1.0, 1.0, 1.0],'f')); # seems to do nothing, both sides of the nurbs still white
    # gl.glMaterialfv(gl.GL_FRONT, gl.GL_SHININESS, np.array([100.0],'f')); # seems to do nothing, both sides of the nurbs still white.
    x+= random.randint(0, len(colors)-1)# this is shimmering.... but not 'continous(gradient) colors'
    x = x% len(colors)
    """
controlPoints:
[[[-3. -3. -3.]
  [-3. -1. -3.]
  [-3.  1. -3.]
  [-3.  3. -3.]]

 [[-1. -3. -3.]
  [-1. -1.  3.]
  [-1.  1.  3.]
  [-1.  3. -3.]]

 [[ 1. -3. -3.]
  [ 1. -1.  3.]
  [ 1.  1.  3.]
  [ 1.  3. -3.]]

 [[ 3. -3. -3.]
  [ 3. -1. -3.]
  [ 3.  1. -3.]
  [ 3.  3. -3.]]]
    """
    #gl.glVertex3fv
    #maybe, use control, sKnots, tKnots as vertices?
    # print(x)
    gl.glColor3fv(colors[x])# this is flashing.... but not 'continous(gradient) colors' & cannot use vertices to select source of color change...

    glu.gluNurbsSurface(nurbs,sKnots, tKnots, control, type)
    """
    argTypes of gluNurbsCurve (raw OpenGL) can be found here: Lib/site-packages/OpenGL/raw/GLU/__init__.py
    argNames of glu.gluNurbsCurve can be found in OpenGL/GLU/glunurbs.py

    """
    glu.gluEndSurface(nurbs)