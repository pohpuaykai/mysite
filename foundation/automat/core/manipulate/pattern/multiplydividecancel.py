
from foundation.automat.core.manipulate.manipulate import Manipulate


class Multiplydividecancel(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(* (/ $1 $0) $0)', 'return': '$1'}, 'hin': {'scheme': '$1', 'return': '(* (/ $1 $0) $0)'}}, {'type': 'regex', 'vor': {'scheme': '(/ (* $1 $0) $0)', 'return': '$1'}, 'hin': {'scheme': '$1', 'return': '(/ (* $1 $0) $0)'}}]
        super().__init__(equation, verbose=verbose)