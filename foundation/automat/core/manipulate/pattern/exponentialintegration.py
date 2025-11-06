
from foundation.automat.core.manipulate.manipulate import Manipulate


class Exponentialintegration(Manipulate):
    """

    """
    TYPE = 'essential'
    NO_OF_MANIPULATIONS = '2'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(int (* (^ e $0) (D $0 $1)) $1)', 'return': '(+ (^ e $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (^ e $0) $2)', 'return': '(int (* (^ e $0) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (^ $0 $1) (+ (* (D $1 $2) (log e $0)) (* (D $0 $2) (/ $1 $0)))) $2)', 'return': '(+ (^ $0 $1) $3)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1, '$3': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None, '$3': 0}, 'preCond': {'$0': None, '$1': None, '$2': None, '$3': None}, 'hin': {'scheme': '(+ (^ $0 $1) $3)', 'return': '(int (* (^ $0 $1) (+ (* (D $1 $2) (log e $0)) (* (D $0 $2) (/ $1 $0)))) $2)'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)