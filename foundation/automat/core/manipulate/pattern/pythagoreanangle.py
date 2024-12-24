
from foundation.automat.core.manipulate.manipulate import Manipulate


class Pythagoreanangle(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'

    def __init__(self, equation, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(+ (^ (sin $0) 2) (^ (cos $0) 2))', 'return': '1'}, 'hin': {'scheme': '1', 'return': '(+ (^ (sin $0) 2) (^ (cos $0) 2))'}}]
        super().__init__(equation, verbose=verbose)