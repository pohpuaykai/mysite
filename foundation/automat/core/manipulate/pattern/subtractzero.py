
from foundation.automat.core.manipulate.manipulate import Manipulate


class Subtractzero(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(- 0 $0)', 'return': '$0'}, 'hin': {'scheme': '$0', 'return': '(- 0 $0)'}, 'minArgs': {'$0': 0}}, {'type': 'regex', 'vor': {'scheme': '(- $0 0)', 'return': '$0'}, 'hin': {'scheme': '$0', 'return': '(- $0 0)'}, 'minArgs': {'$0': 0}}]
        super().__init__(equation, direction, idx, verbose=verbose)