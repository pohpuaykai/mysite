
from foundation.automat.core.manipulate.manipulate import Manipulate


class Multiplynegative(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(* "-1" $0)', 'return': '(- 0 $0)'}, 'hin': {'scheme': '(- 0 $0)', 'return': '(* "-1" $0)'}}]
        super().__init__(equation, verbose=verbose)