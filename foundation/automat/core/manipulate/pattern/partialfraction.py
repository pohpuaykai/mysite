
from foundation.automat.core.manipulate.manipulate import Manipulate


class Partialfraction(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = None
        super().__init__(equation, direction, idx, verbose=verbose)