
from foundation.automat.core.manipulate.manipulate import Manipulate


class Arctrigonometricderivative(Manipulate):
    """

    """
    TYPE = 'derivative_trigonometric'

    def __init__(self, equation, direction, idx, verbose):
        """

        """
        self.rawRegexes = None
        super().__init__(equation, direction, idx, verbose=verbose)