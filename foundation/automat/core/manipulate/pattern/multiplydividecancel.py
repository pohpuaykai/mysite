
from foundation.automat.core.manipulate.manipulate import Manipulate


class Multiplydividecancel(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(* (/ % $0) $0)', 'return': '%'}, 'hin': {'scheme': '%', 'return': '(* (/ % $0) $0)'}}, {'type': 'regex', 'vor': {'scheme': '(/ (* % $0) $0)', 'return': '%'}, 'hin': {'scheme': '%', 'return': '(/ (* % $0) $0)'}}]
        super().__init__(equation, verbose=verbose)