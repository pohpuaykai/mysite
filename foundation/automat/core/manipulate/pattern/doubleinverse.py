
from foundation.automat.core.manipulate.manipulate import Manipulate


class Doubleinverse(Manipulate):
    """

    """
    TYPE = 'pretty'

    def __init__(self, equation, direction, idx, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(/ (/ $2 $0) $1)', 'return': '(/ $2 (* $0 $1))'}, 'hin': {'scheme': '(/ $2 (* $0 $1))', 'return': '(/ (/ $2 $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(/ $0 (/ $2 $1))', 'return': '(/ (* $0 $1) $2)'}, 'hin': {'scheme': '(/ (* $0 $1) $2)', 'return': '(/ $0 (/ $2 $1))'}}]
        super().__init__(equation, direction, idx, verbose=verbose)