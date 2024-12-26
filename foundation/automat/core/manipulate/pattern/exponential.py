
from foundation.automat.core.manipulate.manipulate import Manipulate


class Exponential(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(^ $0 0)', 'return': '1'}, 'hin': {'scheme': '1', 'return': '(^ $0 0)'}}, {'type': 'regex', 'vor': {'scheme': '(^ $0 1)', 'return': '$0'}, 'hin': {'scheme': '$0', 'return': '(^ $0 1)'}}, {'type': 'regex', 'vor': {'scheme': '(^ $0 (+ $1 $2))', 'return': '(* (^ $0 $1) (^ $0 $2))'}, 'hin': {'scheme': '(* (^ $0 $1) (^ $0 $2))', 'return': '(^ $0 (+ $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(^ (^ $0 $1) $2)', 'return': '(^ $0 (* $1 $2))'}, 'hin': {'scheme': '(^ $0 (* $1 $2))', 'return': '(^ (^ $0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(* (^ $1 $0) (^ $2 $0))', 'return': '(^ (* $1 $2) $0)'}, 'hin': {'scheme': '(^ (* $1 $2) $0)', 'return': '(* (^ $1 $0) (^ $2 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(^ $0 (- "0" $1))', 'return': '(/ "1" (^ $0 $1))'}, 'hin': {'scheme': '(/ "1" (^ $0 $1))', 'return': '(^ $0 (- "0" $1))'}}]
        super().__init__(equation, direction, idx, verbose=verbose)