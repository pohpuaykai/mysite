import random

import OpenGL.GL as gl
import OpenGL.GLU as glu


def cylinder(baseRadius, topRadius, height, slices, stacks, texture, drawStyle, normals, orientation, colors):
    """
    #TODO need to convert to Mesh to be compatible


    From http://jerome.jouvie.free.fr/opengl-tutorials/Tutorial7.php

    #defines if the shape is textured
    glu.gluQuadricTexture(quadric, value) #Default: false
    #defines the rendering style of the quadric
    glu.gluQuadricDrawStyle(quadric, value) #Default: GLU_FILL
    #defines if the shape is drawn with normal and, if so, specify if it is per face or per vertex normal
    glu.gluQuadricNormals(quadric, value) #Default: GLU_SMOOTH
    #defines normal orientation, either points outside the shape or inside
    glu.gluQuadricOrientation(quadric, value) # Default: GLU_OUTSIDE


    http://jerome.jouvie.free.fr/opengl-tutorials/Tutorial7.php


    Mostly just a wrapper for glu.cylinder, more details here:

    #https://learn.microsoft.com/en-us/windows/win32/opengl/glucylinder
    #https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluCylinder.xml



    gluQuadricTexture True/False
    gluQuadricNormals GLU_NONE / GLU_FLAT / GLU_SMOOTH
    gluQuadricOrientation GLU_OUTSIDE / GLU_INSIDE


    gl.glMaterialfv
    gl.GL_AMBIENT
The params parameter contains four floating-point values that specify the ambient RGBA reflectance of the material. Integer values are mapped linearly such that the most positive representable value maps to 1.0, and the most negative representable value maps to -1.0. Floating-point values are mapped directly. Neither integer nor floating-point values are clamped. The default ambient reflectance for both front-facing and back-facing materials is (0.2, 0.2, 0.2, 1.0).

    gl.GL_DIFFUSE
The params parameter contains four floating-point values that specify the diffuse RGBA reflectance of the material. Integer values are mapped linearly such that the most positive representable value maps to 1.0, and the most negative representable value maps to -1.0. Floating-point values are mapped directly. Neither integer nor floating-point values are clamped. The default diffuse reflectance for both front-facing and back-facing materials is (0.8, 0.8, 0.8, 1.0).

    gl.GL_SPECULAR
The params parameter contains four floating-point values that specify the specular RGBA reflectance of the material. Integer values are mapped linearly such that the most positive representable value maps to 1.0, and the most negative representable value maps to -1.0. Floating-point values are mapped directly. Neither integer nor floating-point values are clamped. The default specular reflectance for both front-facing and back-facing materials is (0.0, 0.0, 0.0, 1.0).

    gl.GL_EMISSION
The params parameter contains four floating-point values that specify the RGBA emitted light intensity of the material. Integer values are mapped linearly such that the most positive representable value maps to 1.0, and the most negative representable value maps to -1.0. Floating-point values are mapped directly. Neither integer nor floating-point values are clamped. The default emission intensity for both front-facing and back-facing materials is (0.0, 0.0, 0.0, 1.0).

    gl.GL_SHININESS
The param parameter is a single integer value that specifies the RGBA specular exponent of the material. Integer values are mapped directly. Only values in the range [0, 128] are accepted. The default specular exponent for both front-facing and back-facing materials is 0.

    gl.GL_AMBIENT_AND_DIFFUSE
Equivalent to calling glMaterial twice with the same parameter values, once with GL_AMBIENT and once with GL_DIFFUSE.

    gl.GL_COLOR_INDEXES
The params parameter contains three floating-point values specifying the color indexes for ambient, diffuse, and specular lighting. These three values, and GL_SHININESS, are the only material values used by the color-index mode lighting equation. Refer to glLightModel for a discussion of color-index lighting.


    :param baseRadius:
    :type baseRadius:
    
    :param topRadius:
    :type topRadius:
    
    :param height:
    :type height:
    
    :param slices:
    :type slices:
    
    :param stacks:
    :type stacks:
    
    :param drawStyle:
    more information here:

    https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluQuadricDrawStyle.xml
    https://learn.microsoft.com/en-us/windows/win32/opengl/gluquadricdrawstyle
    https://www.ibm.com/docs/sl/aix/7.1?topic=library-gluquadricdrawstyle-subroutine


    valid enums for the second argument of glu:-
    import OpenGL.GLU as glu
    glu.GLU_FILL
    glu.GLU_LINE
    glu.GLU_SILHOUETTE
    glu.GLU_POINT
    :type drawStyle: :class:`OpenGL.constant.IntConstant`

    """
    x = 0
    cylinderQ = glu.gluNewQuadric()
    gl.glPushMatrix() # save first position

    x+= random.randint(0, len(colors)-1)# this is shimmering.... but not 'continous(gradient) colors'
    x = x% len(colors)
    # print(x)
    gl.glColor3fv(colors[x])# this is flashing.... but not 'continous(gradient) colors' & cannot use vertices to select source of color change...

    glu.gluQuadricTexture(cylinderQ, True)
    glu.gluQuadricDrawStyle(cylinderQ, drawStyle)
    glu.gluQuadricNormals(cylinderQ, glu.GLU_SMOOTH)
    glu.gluQuadricOrientation(cylinderQ, glu.GLU_INSIDE)
    glu.gluCylinder(cylinderQ, baseRadius, topRadius, height, slices, stacks)
    #glu.gluDeleteQuadric(cylinderQ);
    gl.glPopMatrix() # load first position


def cone(drawStyle):
    coneQ = glu.gluNewQuadric()
    gl.glPushMatrix() # save first position
    glu.gluQuadricDrawStyle(coneQ, drawStyle)
    #https://learn.microsoft.com/en-us/windows/win32/opengl/glucylinder
    #https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluCylinder.xml
    glu.gluCylinder(coneQ, 0.6, 0, 2.5, 20, 20) # according to this: http://jerome.jouvie.free.fr/opengl-tutorials/Tutorial7.php
    #glu.gluDeleteQuadric(coneQ);
    gl.glPopMatrix() # load first position
