
from foundation.automat.core.manipulate.manipulate import Manipulate


class Cubicpolynomial(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose):
        """

        """
        self.rawRegexes = None
        super().__init__(equation, direction, idx, verbose=verbose)