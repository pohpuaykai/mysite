
from foundation.automat.core.manipulate.manipulate import Manipulate


class Rootbasenegative(Manipulate):
    """

    """
    TYPE = 'pretty'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(nroot (- 0 $0) $1)', 'return': '(nroot $0 (/ 1 $1))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(nroot $0 (/ 1 $1))', 'return': '(nroot (- 0 $0) $1)'}}]
        super().__init__(equation, direction, idx, verbose=verbose)