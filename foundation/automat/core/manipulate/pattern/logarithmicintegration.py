
from foundation.automat.core.manipulate.manipulate import Manipulate


class Logarithmicintegration(Manipulate):
    """

    """
    TYPE = 'integration_logarithm'
    NO_OF_MANIPULATIONS = '3'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(int (/ (- (* (* (D $1 $2) (/ 1 $1)) (log e $0)) (* (* (D $0 $2) (/ 1 $0)) (log e $1))) (^ (log e $0) 2)) $2)', 'return': '(+ (log $0 $1) $3)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1, '$3': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None, '$3': 0}, 'preCond': {'$0': None, '$1': None, '$2': None, '$3': None}, 'hin': {'scheme': '(+ (log $0 $1) $3)', 'return': '(int (/ (- (* (* (D $1 $2) (/ 1 $1)) (log e $0)) (* (* (D $0 $2) (/ 1 $0)) (log e $1))) (^ (log e $0) 2)) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(int (/ (D $1 $2) (* $1 (log e $0))) $2)', 'return': '(+ (log $0 $1) $3)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1, '$3': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None, '$3': 0}, 'preCond': {'$0': None, '$1': None, '$2': None, '$3': None}, 'hin': {'scheme': '(+ (log $0 $1) $3)', 'return': '(int (/ (D $1 $2) (* $1 (log e $0))) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(int (/ (D $0 $1) $1) $1)', 'return': '(+ (log e $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (log e $0) $2)', 'return': '(int (/ (D $0 $1) $1) $1)'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)