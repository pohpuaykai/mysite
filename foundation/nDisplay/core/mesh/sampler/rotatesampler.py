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
        takes a formulaStr, that takes a x, and returns a y, 
        rotates it about x-axis, and gives many points on the surface formed by the rotation
        the points are restricted by the sampling parameters
        [xStart:xEnd:xStep], this is the x input to formulaStr
        [dStart:dEnd:dStep], this is the degrees of rotation
        
        we expect formulaStr to only take in x.
        If your formulaStr has other parameters , please fill it in with lambda first.
        For example:
        formulaStr = 'l/(1+math.pow(math.e, -s * x))'
        #fill the parameters, that is is not x
        completedFormulaStr = lambda x: eval(formulaStr, locals={'l':1, 's':1, 'x':x})
        
        """
        #TODO check if [xStart:xEnd:xStep] and [dStart:dEnd:dStep] makes sense
        vertices = []
        for x in frange(xStart, xEnd, xStep):
            f = formulaLambda(x) * formulaLambda(x)
            for d in frange(dStart, dEnd, dStep):
                y_p = math.sqrt((math.atan(d)+1)/(f))#positive y
                z_p = y_p * math.atan(d)
                vertices.append((x, y_p, z_p))
                vertices.append((x, -y_p, -z_p))
                
        return vertices

    @classmethod
    def rotatePieceWiseSample(cls, *formulaLambdaWithEndPoints):
        """
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
        for formulaLambdaWithEndPoint in formulaLambdaWithEndPoints:
            touVertices.append(rotateSampler(**formulaLambdaWithEndPoint))
        return touVertices