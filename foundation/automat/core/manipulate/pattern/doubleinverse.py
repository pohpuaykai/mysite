
from foundation.automat.core.manipulate.manipulate import Manipulate


class Doubleinverse(Manipulate):
    """

    """
    TYPE = 'pretty'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(/ (/ $2 $0) $1)', 'return': '(/ $2 (* $0 $1))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(/ $2 (* $0 $1))', 'return': '(/ (/ $2 $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(/ $0 (/ $2 $1))', 'return': '(/ (* $0 $1) $2)'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(/ (* $0 $1) $2)', 'return': '(/ $0 (/ $2 $1))'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)