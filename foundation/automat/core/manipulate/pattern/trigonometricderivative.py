
from foundation.automat.core.manipulate.manipulate import Manipulate


class Trigonometricderivative(Manipulate):
    """

    """
    TYPE = 'derivative_trigonometric'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = None
        super().__init__(equation, direction, idx, verbose=verbose)