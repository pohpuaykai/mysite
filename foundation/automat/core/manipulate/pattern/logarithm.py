
from foundation.automat.core.manipulate.manipulate import Manipulate


class Logarithm(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(log $0 (* $1 $2))', 'return': '(+ (log $0 $1) (log $0 $2))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (log $0 $1) (log $0 $2))', 'return': '(log $0 (* $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 (/ $1 $2))', 'return': '(- (log $0 $1) (log $0 $2))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(- (log $0 $1) (log $0 $2))', 'return': '(log $0 (/ $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 (^ $1 $2))', 'return': '(* $2 (log $0 $1))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(* $2 (log $0 $1))', 'return': '(log $0 (^ $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 (nroot $1 $2))', 'return': '(/ (log $0 $2) $1)'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(/ (log $0 $2) $1)', 'return': '(log $0 (nroot $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(/ (log $2 $1) (log $2 $0))', 'return': '(log $0 $1)'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(log $0 $1)', 'return': '(/ (log $2 $1) (log $2 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 $0)', 'return': '"1"'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '"1"', 'return': '(log $0 $0)'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 "1")', 'return': '"0"'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '"0"', 'return': '(log $0 "1")'}}]
        super().__init__(equation, direction, idx, verbose=verbose)