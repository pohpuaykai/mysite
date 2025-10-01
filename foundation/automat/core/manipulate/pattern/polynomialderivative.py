
from foundation.automat.core.manipulate.manipulate import Manipulate


class Polynomialderivative(Manipulate):
    """

    """
    TYPE = 'derivative_polynomial'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(D $0 $0)', 'return': '1'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '1', 'return': '(D $0 $0)'}}, {'type': 'regex', 'vor': {'scheme': '(D (* $0 (^ $1 $2)) $1)', 'return': '(* $0 (* $2 (^ $1 (- $2 1))))'}, 'minArgs': {'$0': 0, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(* $0 (* $2 (^ $1 (- $2 1))))', 'return': '(D (* $0 (^ $1 $2)) $1)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)