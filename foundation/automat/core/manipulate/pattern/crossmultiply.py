
from foundation.automat.core.manipulate.manipulate import Manipulate


class Crossmultiply(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(+ (/ $0 $1) (/ $2 $3))', 'return': '(/ (+ (* $0 $3) (* $1 $2)) (* $1 $3))'}, 'hin': {'scheme': '(/ (+ (* $0 $3) (* $1 $2)) (* $1 $3))', 'return': '(+ (/ $0 $1) (/ $2 $3))'}, 'minArgs': {'$0': 0, '$1': 0}}]
        super().__init__(equation, direction, idx, verbose=verbose)