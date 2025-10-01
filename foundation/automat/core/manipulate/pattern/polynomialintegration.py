
from foundation.automat.core.manipulate.manipulate import Manipulate


class Polynomialintegration(Manipulate):
    """

    """
    TYPE = 'integration_polynomial'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(int 1 $0)', 'return': '(+ $0 $1)'}, 'minArgs': {'$0': 1, '$1': 0}, 'maxArgs': {'$0': None, '$1': 0}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(+ $0 $1)', 'return': '(int 1 $0)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* $0 (* $2 (^ $1 (- $2 1)))) $1)', 'return': '(+ (* $0 (^ $1 $2)) $3)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1, '$3': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None, '$3': 0}, 'preCond': {'$0': None, '$1': None, '$2': None, '$3': None}, 'hin': {'scheme': '(+ (* $0 (^ $1 $2)) $3)', 'return': '(int (* $0 (* $2 (^ $1 (- $2 1)))) $1)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)