
from foundation.automat.core.manipulate.manipulate import Manipulate


class Distributivity(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(+ (* $0 $1) (* $0 $2))', 'return': '(* $0 (+ $1 $2))'}, 'hin': {'scheme': '(* $0 (+ $1 $2))', 'return': '(+ (* $0 $1) (* $0 $2))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}}, {'type': 'regex', 'vor': {'scheme': '(- (* $0 $1) (* $0 $2))', 'return': '(* $0 (- $1 $2))'}, 'hin': {'scheme': '(* $0 (- $1 $2))', 'return': '(- (* $0 $1) (* $0 $2))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}}, {'type': 'regex', 'vor': {'scheme': '(+ (/ $1 $0) (/ $2 $0))', 'return': '(/ (+ $1 $2) $0)'}, 'hin': {'scheme': '(/ (+ $1 $2) $0)', 'return': '(+ (/ $1 $0) (/ $2 $0))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}}, {'type': 'regex', 'vor': {'scheme': '(- (/ $1 $0) (/ $2 $0))', 'return': '(/ (- $1 $2) $0)'}, 'hin': {'scheme': '(/ (- $1 $2) $0)', 'return': '(- (/ $1 $0) (/ $2 $0))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}}]
        super().__init__(equation, direction, idx, verbose=verbose)