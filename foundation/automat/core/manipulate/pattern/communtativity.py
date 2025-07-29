
from foundation.automat.core.manipulate.manipulate import Manipulate


class Communtativity(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(+ $0 $1)', 'return': '(+ $1 $0)'}, 'hin': {'scheme': '(+ $1 $0)', 'return': '(+ $0 $1)'}, 'minArgs': {'$0': 0, '$1': 0}}, {'type': 'regex', 'vor': {'scheme': '(* $0 $1)', 'return': '(* $1 $0)'}, 'hin': {'scheme': '(* $1 $0)', 'return': '(* $0 $1)'}, 'minArgs': {'$0': 0, '$1': 0}}, {'type': 'regex', 'vor': {'scheme': '(= $0 $1)', 'return': '(= $1 $0)'}, 'hin': {'scheme': '(= $1 $0)', 'return': '(= $0 $1)'}, 'minArgs': {'$0': 0, '$1': 0}}]
        super().__init__(equation, direction, idx, verbose=verbose)