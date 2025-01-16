class VectorDimensionCounter:
    def __init__(self, dimension, step, lowerBound, upperBound):
        if step >= (upperBound - lowerBound):
            raise Exception('step is too much')
        self.dimension = dimension
        self.step = step
        self.precision = len(str(step).split('.')[1])
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.d = 0
        self.c = [self.lowerBound] * self.dimension
        
    def next(self):
        self.c[self.d] += self.step
        self.c[self.d] = round(self.c[self.d], self.precision) # sometimes gives rounding error while adding
        if self.c[self.d] >= self.upperBound:
            self.c[self.d] = self.lowerBound
            self.d += 1
            self.d = self.d % self.dimension
            self.c[self.d] += self.step
        return self.c


class ColorCounter:
    def __init__(self):
        self.vdc = VectorDimensionCounter(3, 0.01, 0.0, 1.0)

    def next(self):
        return self.vdc.next()