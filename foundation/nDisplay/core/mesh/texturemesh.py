from OpenGL.GL import glGenVertexArrays, glBindVertexArray, GL_ARRAY_BUFFER, GL_STATIC_DRAW, GL_FLOAT
import numpy as np

class TextureMesh:
    """
    Courtesy of Andrew of www.youtube.com/@GetIntoGameDev

    This mesh only has position, texture information
    """
    def __init__(self, vertices):
        """
        
        :param vertices:
        s, t values are for texture
        [
            (1, 2, 3, 0.1, 0.2), # x, y, z, s, t values
            (4, 5, 6, 0.1, 0.2),
            (7, 8, 9, 0.1, 0.2)
        ]
        """
        #here will will just flatten the vertices
        #since we expect the items in vertices to be 3-tuples, the list will be exactly 2-levels deep.
        #so we can safely use this list comprehension to flatten the input vertices
        self.vertices = [a for c in vertices for a in c]
        self.vertex_count = len(self.vertices) // 8
        self.vertices = np.array(self.vertices, dtype=np.float32)

    def sendToShader():
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        #Vertices
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
        #position
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
        #texture
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))