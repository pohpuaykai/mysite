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
        while counter < end:
            yield counter
            counter += step

    @classmethod
    def rotateSample(cls, formulaLambda, xStart, xEnd, xStep, dStart, dEnd, dStep):
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
        vertices, indices = [], []
        xPoints, dPoints = list(cls.frange(xStart, xEnd, xStep)), list(cls.frange(dStart, dEnd, dStep))
        for xIdx, x in enumerate(xPoints):#each wheel
            f = formulaLambda(x)
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
                    indices.append((v00, v01, v10));indices.append((v10, v11, v00))
        return vertices, indices





    @classmethod
    def rotatePieceWiseSample(cls, *formulaLambdaWithEndPoints):
        """
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
        touTriangles = []
        for formulaLambdaWithEndPoint in formulaLambdaWithEndPoints:
            vertices, triangles = rotateSampler(**formulaLambdaWithEndPoint)
            touVertices += vertices
            touTriangles += touTriangles
        return touVertices, touTriangles