import math

class RotateSampler:
    """
    Courtesy of Andrew of www.youtube.com/@GetIntoGameDev
    """

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
    def rotateSample(cls, formulaLambda, xStart, xEnd, xStep, dStart, dEnd, dStep, xRange__color, defaultColor):
        """
        TODO triangles are untested. Please test.

        takes a formulaStr, that takes a x, and returns a y, 
        rotates it about x-axis, and gives many points on the surface formed by the rotation
        the points are restricted by the sampling parameters
        [xStart:xEnd:xStep], this is the x input to formulaStr
        [dStart:dEnd:dStep], this is the degrees of rotation, in DEGREE
        
        we expect formulaStr to only take in x.
        If your formulaStr has other parameters , please fill it in with lambda first.
        For example:
        formulaStr = 'l/(1+math.pow(math.e, -s * x))'
        #fill the parameters, that is is not x
        completedFormulaStr = lambda x: eval(formulaStr, locals={'l':1, 's':1, 'x':x})
        
        """
        #TODO check if [xStart:xEnd:xStep] and [dStart:dEnd:dStep] makes sense
        list_tuple_xRange_color = sorted(xRange__color.items(), key=lambda t:t[0][0]) # ascending first coordinate of xRange
        def colorOfCoordinate(x):
            for (xStart, xEnd), color in list_tuple_xRange_color:
                if xStart <= x < xEnd:
                    return color
            return defaultColor

        vertices, indices, colors = [], [], []
        xPoints, dPoints = list(cls.frange(xStart, xEnd, xStep)), list(cls.frange(dStart, dEnd, dStep))
        for xIdx, x in enumerate(xPoints):#each wheel
            f, color = formulaLambda(x), colorOfCoordinate(x)
            # print('wheelIdx', xIdx, ' each wheel has ', len(dPoints))
            for dIdx, d in enumerate(dPoints):#each point in each wheel
                vertices.append((x, f*math.cos(math.radians(d)), f*math.sin(math.radians(d))))
                #connect between wheels, this wheel and previous wheel
                if xIdx > 0:
                    prevWheelIdx, thisWheelIdx = xIdx-1, xIdx
                    prevPointIdx, thisPointIdx = (dIdx-1)%len(dPoints), dIdx
                    p00, p01, p10, p11 = (prevWheelIdx, prevPointIdx), (prevWheelIdx, thisPointIdx), (thisWheelIdx, prevPointIdx), (thisWheelIdx, thisPointIdx)
                    #convert (wheelIdx, pointIdx) to vertexIdx
                    def wheelIdxPointIdxTOvertexIdx(wheelIdx, pointIdx):
                        return wheelIdx*len(dPoints)+pointIdx
                    v00, v01, v10, v11 = wheelIdxPointIdxTOvertexIdx(p00[0], p00[1]), wheelIdxPointIdxTOvertexIdx(p01[0], p01[1]), wheelIdxPointIdxTOvertexIdx(p10[0], p10[1]), wheelIdxPointIdxTOvertexIdx(p11[0], p11[1])
                    #form 2 triangles
                    indices.append((v00, v10, v01));indices.append((v11, v01, v10)) # indices are triangles
                    #add the color_3_tuple of this triangle
                    colors.append(color);colors.append(color)
        return vertices, indices, colors, indices[:2*len(dPoints)], indices[-2*len(dPoints):]# 2 triangles for each point on the wheel





    @classmethod
    def rotatePieceWiseSample(cls, formulaLambdaWithEndPoints):
        """
        ASSUME points go in the x-axis, from smaller x to bigger x
        TODO test

        :param formulaLambdaWithEndPoints:
        Example (the whole list):
        [
        {#trench
            'formulaLambda':lambda x: eval('h/(1+math.pow(math.e, s * x))', locals={'h':1, 's':1, 'x':x}),
            'xStart':-2,
            'xEnd':-1,
            'xStep':0.1,
            'dStart':0,
            'dEnd':360,
            'dStep':90
        },
        {#cylinder
            'formulaLambda':lambda x: eval('hx', locals={'h':1}),
            'xStart':-1,
            'xEnd':1,
            'xStep':0.1,
            'dStart':0,
            'dEnd':360,
            'dStep':90
        },
        
        {#wall
            'formulaLambda':lambda x: eval('h/(1+math.pow(math.e, -s * x))', locals={'h':1, 's':1, 'x':x}),
            'xStart':1,
            'xEnd':2,
            'xStep':0.1,
            'dStart':0,
            'dEnd':360,
            'dStep':90
        }
        ]
        """
        touVertices = []
        touIndices = []#####indices of touVertices, grouped into triangles
        touColors = []
        prevEndPointIndices, prevTotalIndex, prevNoOfIndices = [], 0, 0
        for pieceIdx, formulaLambdaWithEndPoint in enumerate(formulaLambdaWithEndPoints):
            print(formulaLambdaWithEndPoint)
            vertices, indices, colors, startPointIndices, endPointIndices = cls.rotateSample(**formulaLambdaWithEndPoint)
            touVertices += vertices
            touColors += colors
            if pieceIdx > 0:
                #for the 
                #increment endPointIndices by previous number of vertices
                newEndPointIndices = []
                for indice in prevEndPointIndices:
                    newIndice = []
                    for coordinate in indice:
                        newIndice.append(coordinate+prevTotalIndex-prevNoOfIndices)
                    newEndPointIndices.append(tuple(newIndice))
                prevEndPointIndices = newEndPointIndices
                #increment startPointIndices by previous number of vertices
                newStartPointIndices = []
                for indice in startPointIndices:
                    newIndice = []
                    for coordinate in indice:
                        newIndice.append(coordinate+prevTotalIndex)
                    newStartPointIndices.append(tuple(newIndice))
                startPointIndices = newStartPointIndices
                #connection can only be made only if endpoints and startpoints have the same number of points.....
                newIndices = []
                for quadIdx in range(0, len(endPointIndices)):
                    prevTriangleIdx, thisTriangleIdx = (quadIdx-1)%len(endPointIndices), quadIdx
                    (p00, p10, p01), (p11, p01, p10), (t00, t10, t01), (t11, t01, t10) = prevEndPointIndices[prevTriangleIdx], prevEndPointIndices[thisTriangleIdx], startPointIndices[prevTriangleIdx], startPointIndices[thisTriangleIdx]
                    newIndices.append((p10, t00, p11));newIndices.append((t01, p11, t00))
                #increment indices by previous number of vertices
                for indice in indices:
                    newIndice = []
                    for coordinate in indice:
                        newIndice.append(coordinate+prevTotalIndex)
                    newIndices.append(tuple(newIndice))
                indices = newIndices
            touIndices += indices
            prevEndPointIndices = endPointIndices
            prevTotalIndex += len(vertices)
            prevNoOfIndices = len(vertices)
        return touVertices, touIndices, touColors