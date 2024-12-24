
from foundation.automat.core.manipulate.manipulate import Manipulate


class Communtativity(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(+ $0 $1)', 'return': '(+ $1 $0)'}, 'hin': {'scheme': '(+ $1 $0)', 'return': '(+ $0 $1)'}}, {'type': 'regex', 'vor': {'scheme': '(* $0 $1)', 'return': '(* $1 $0)'}, 'hin': {'scheme': '(* $1 $0)', 'return': '(* $0 $1)'}}, {'type': 'regex', 'vor': {'scheme': '(= $0 $1)', 'return': '(= $1 $0)'}, 'hin': {'scheme': '(= $1 $0)', 'return': '(= $0 $1)'}}]
        super().__init__(equation, verbose=verbose)