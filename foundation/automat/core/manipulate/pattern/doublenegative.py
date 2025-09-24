
from foundation.automat.core.manipulate.manipulate import Manipulate


class Doublenegative(Manipulate):
    """

    """
    TYPE = 'pretty'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(- 0 (- 0 $0))', 'return': '$0'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '$0', 'return': '(- 0 (- 0 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(- (- 0 $0) (- 0 $1))', 'return': '(- $1 $0)'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(- $1 $0)', 'return': '(- (- 0 $0) (- 0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(- 0 (+ (- 0 $0) $1))', 'return': '(- $0 $1)'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(- $0 $1)', 'return': '(- 0 (+ (- 0 $0) $1))'}}]
        super().__init__(equation, direction, idx, verbose=verbose)