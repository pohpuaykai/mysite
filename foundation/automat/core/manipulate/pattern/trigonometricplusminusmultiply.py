
from foundation.automat.core.manipulate.manipulate import Manipulate


class Trigonometricplusminusmultiply(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'

    def __init__(self, equation, direction, idx, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(sin (+ $0 $1))', 'return': '(+ (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))'}, 'hin': {'scheme': '(+ (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))', 'return': '(sin (+ $0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(sin (- $0 $1))', 'return': '(- (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))'}, 'hin': {'scheme': '(- (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))', 'return': '(sin (- $0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(cos (+ $0 $1))', 'return': '(- (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))'}, 'hin': {'scheme': '(- (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))', 'return': '(cos (+ $0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(cos (- $0 $1))', 'return': '(+ (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))'}, 'hin': {'scheme': '(+ (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))', 'return': '(cos (- $0 $1))'}}]
        super().__init__(equation, direction, idx, verbose=verbose)