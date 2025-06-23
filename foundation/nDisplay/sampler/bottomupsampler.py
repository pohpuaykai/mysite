import math

class BottomUpSampler:

    @classmethod
    def frange(cls, start, end, step):
        """
        frange float-range
        same as range, but allows floating-point step
        """
        #TODO checking of validity of start, end, step
        counter = start
        while counter <= end:
            yield counter
            counter += step

    @classmethod
    def bottomUpSample(cls, uStart, uEnd, uStep, yFormulaLambda, vStart, vEnd, vStep, xFormulaLambda, zFormulaLambda, colorFunction):
        """
        
        :param uStart:
        :param uEnd:
        :param uStep:
        :param yFormulaLambda: takes u and returns y
        :param vStart:
        :param vEnd:
        :param vStep:
        :param xFormulaLambda: takes a v, can have y in its formulaStr, so needs y to be calculated first, and exist in locals()
        :param zFormulaLambda: takes a v, can have y in its formulaStr, so needs y to be calculated first, and exist in locals()
        :param colorFunction: takes a x, y, z, and returns a RGB
        """
        vertices, indices, colors = [], [], []
        uPoints, vPoints = list(cls.frange(uStart, uEnd, uStep)), list(cls.frange(vStart, vEnd, vStep))
        for uIdx, u in enumerate(uPoints):
            y = yFormulaLambda(u)
            for vIdx, v in enumerate(vPoints):
                x = xFormulaLambda(v); z = zFormulaLambda(v)
                vertices.append((x, y, z)); colors.append(colorFunction(x, y, z))
                #connect between wheels, this wheel and previous wheel
                if uIdx > 0:
                    prevWheelIdx, thisWheelIdx = uIdx-1, uIdx
                    prevPointIdx, thisPointIdx = (vIdx-1)%len(vPoints), vIdx
                    p00, p01, p10, p11 = (prevWheelIdx, prevPointIdx), (prevWheelIdx, thisPointIdx), (thisWheelIdx, prevPointIdx), (thisWheelIdx, thisPointIdx)
                    #convert (wheelIdx, pointIdx) to vertexIdx
                    def wheelIdxPointIdxTOvertexIdx(wheelIdx, pointIdx):
                        return wheelIdx*len(vPoints)+pointIdx
                    v00, v01, v10, v11 = wheelIdxPointIdxTOvertexIdx(p00[0], p00[1]), wheelIdxPointIdxTOvertexIdx(p01[0], p01[1]), wheelIdxPointIdxTOvertexIdx(p10[0], p10[1]), wheelIdxPointIdxTOvertexIdx(p11[0], p11[1])
                    #form 2 triangles
                    indices.append((v00, v10, v01));indices.append((v11, v01, v10)) # indices are triangles
        return vertices, indices, colors

    @classmethod
    def bottomUpPieceWiseSampler(cls, uVStartEnds):
        """ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO connect this with CAS? parametrise a "surface" with u and v, USE CAS to xFormulaLambda=(D x v) and zFormulaLambda=(D z v) and yFormulaLambda=(D y u), and then can try any funny formulas, or use Hilbert_space_filling_curve_for_indexing?
        
        We assume that the pieces are disjoint

        Example:
[
        {
            'uStart':,
            'uEnd':,
            'uStep':,
            'yFormulaLambda':lambda u: eval('', locals={'u':u, 'math':theMathModule}),
            'vStart':,
            'vEnd':,
            'vStep':,
            'xFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
            'zFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule})
        },
        {
            'uStart':,
            'uEnd':,
            'uStep':,
            'yFormulaLambda':lambda u: eval('', locals={'u':u, 'math':theMathModule}),
            'vStart':,
            'vEnd':,
            'vStep':,
            'xFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule}),
            'zFormulaLambda':lambda v: eval('', locals={'v':v, 'math':theMathModule})
        },
    ]
        """
        prevTotalIndex = 0
        touVertices, touIndices, touColors = [], [], []
        for pieceIdx, uVStartEnd in enumerate(uVStartEnds):
            vertices, indices, colors = cls.bottomUpSample(**uVStartEnd)
            touVertices += vertices
            touColors += colors
            if pieceIdx > 0:
                newIndices = []
                for indice in indices:
                    newIndice = []
                    for coordinate in indice:
                        newIndice.append(coordinate+prevTotalIndex)
                    newIndices.append(newIndice)
                indices = newIndices
            touIndices += indices
            prevTotalIndex += len(indices)
        return touVertices, touIndices, touColors