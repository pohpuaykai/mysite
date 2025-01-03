
from foundation.automat.core.manipulate.manipulate import Manipulate


class Logarithmicderivative(Manipulate):
    """

    """
    TYPE = 'derivative_logarithm'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = None
        super().__init__(equation, direction, idx, verbose=verbose)