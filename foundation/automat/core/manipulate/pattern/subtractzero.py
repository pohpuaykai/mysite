
from foundation.automat.core.manipulate.manipulate import Manipulate


class Subtractzero(Manipulate):
    """

    """
    TYPE = 'essential'
    NO_OF_MANIPULATIONS = '3'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(+ 0 $0)', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(+ 0 $0)'}}, {'type': 'regex', 'vor': {'scheme': '(+ $0 0)', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(+ $0 0)'}}, {'type': 'regex', 'vor': {'scheme': '(- $0 0)', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(- $0 0)'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)