import OpenGL.GL as gl
import random

def cube(vertices, edges, surfaces, colors):
    """
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

    #connections
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
    """
    #surfaces
    gl.glBegin(gl.GL_QUADS)
    # x = 0#(2) gives solid colors
    for surface in surfaces:
        x = 0#(1) gives color gradient
        # gl.glColor3fv(colors[x])
        for vertex in surface:
            # x += 1#(1) gives color gradient
            # x+= random.randint(0, len(colors)-1)# this is shimmering.... but not 'continous(gradient) colors'

            # x = x% len(colors)
            # print(x)
            gl.glColor3fv(colors[x])
            gl.glVertex3fv(vertices[vertex])
        # x += 1#(2) gives solid colors
    gl.glEnd()

    #wireframe...
    gl.glBegin(gl.GL_LINES)
    for edge in edges:
        for vertex in edge:
            gl.glVertex3fv(vertices[vertex])
    gl.glEnd()