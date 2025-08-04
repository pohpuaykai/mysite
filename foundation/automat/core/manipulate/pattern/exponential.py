
from foundation.automat.core.manipulate.manipulate import Manipulate


class Exponential(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(^ $0 0)', 'return': '1'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': 0}, 'preCond': {'$0': None}, 'hin': {'scheme': '1', 'return': '(^ $0 0)'}}, {'type': 'regex', 'vor': {'scheme': '(^ $0 1)', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': 0}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(^ $0 1)'}}, {'type': 'regex', 'vor': {'scheme': '(^ $0 (+ $1 $2))', 'return': '(* (^ $0 $1) (^ $0 $2))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(* (^ $0 $1) (^ $0 $2))', 'return': '(^ $0 (+ $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(^ (^ $0 $1) $2)', 'return': '(^ $0 (* $1 $2))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(^ $0 (* $1 $2))', 'return': '(^ (^ $0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(* (^ $1 $0) (^ $2 $0))', 'return': '(^ (* $1 $2) $0)'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(^ (* $1 $2) $0)', 'return': '(* (^ $1 $0) (^ $2 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(^ $0 (- "0" $1))', 'return': '(/ "1" (^ $0 $1))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ "1" (^ $0 $1))', 'return': '(^ $0 (- "0" $1))'}}]
        super().__init__(equation, direction, idx, verbose=verbose)