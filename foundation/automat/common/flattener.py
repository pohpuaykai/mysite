class Flattener:


    @classmethod
    def isPrimitive(cls, val):
        return isinstance(val, int) or isinstance(val, float) or isinstance(val, complex) or isinstance(val, bool) or isinstance(val, str) or isinstance(val, bytes)

    @classmethod
    def flatten(cls, listOfListOf):
        """TODO test
        TODO documentation
        """
        values = []
        stack = [listOfListOf]
        while len(stack) > 0:
            currentIterable = stack.pop()
            for item in currentIterable:
                if cls.isPrimitive(item):
                    values.append(item)
                else:
                    stack.append(item)
        return values