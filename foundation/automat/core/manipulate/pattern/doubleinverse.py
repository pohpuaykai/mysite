
from foundation.automat.core.manipulate.manipulate import Manipulate


class Doubleinverse(Manipulate):
    """

    """
    TYPE = 'pretty'

    def __init__(self, equation, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(/ (/ % $0) $1)', 'return': '(/ % (* $0 $1))'}, 'hin': {'scheme': '(/ % (* $0 $1))', 'return': '(/ (/ % $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(/ $0 (/ % $1))', 'return': '(/ (* $0 $1) %)'}, 'hin': {'scheme': '(/ (* $0 $1) %)', 'return': '(/ $0 (/ % $1))'}}]
        super().__init__(equation, verbose=verbose)