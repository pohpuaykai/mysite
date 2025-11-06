
from foundation.automat.core.manipulate.manipulate import Manipulate


class Exponentialderivative(Manipulate):
    """

    """
    TYPE = 'essential'
    NO_OF_MANIPULATIONS = '2'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(D (^ e $0) $1)', 'return': '(* (^ e $0) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (^ e $0) (D $0 $1))', 'return': '(D (^ e $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (^ $0 $1) $2)', 'return': '(* (^ $0 $1) (+ (* (D $1 $2) (log e $0)) (* (D $0 $2) (/ $1 $0))))'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(* (^ $0 $1) (+ (* (D $1 $2) (log e $0)) (* (D $0 $2) (/ $1 $0))))', 'return': '(D (^ $0 $1) $2)'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)