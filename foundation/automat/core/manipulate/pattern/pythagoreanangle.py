
from foundation.automat.core.manipulate.manipulate import Manipulate


class Pythagoreanangle(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'

    def __init__(self, equation, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(+ (', 'return': '(+ (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))'}, 'hin': {'scheme': '(+ (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))', 'return': '(sin (+ $0 $1))'}}]
        super().__init__(equation, verbose=verbose)