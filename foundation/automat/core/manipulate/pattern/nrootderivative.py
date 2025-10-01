
from foundation.automat.core.manipulate.manipulate import Manipulate


class Nrootderivative(Manipulate):
    """

    """
    TYPE = 'nroot_derivative'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(D (nroot $0 $1) $2)', 'return': '(* (nroot $0 $1) (/ (- (/ (* (D $1 $2) $0) $1) (* (D $0 $2) (log e $1))) (^ $0 2)))'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(* (nroot $0 $1) (/ (- (/ (* (D $1 $2) $0) $1) (* (D $0 $2) (log e $1))) (^ $0 2)))', 'return': '(D (nroot $0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(D (nroot $0 $1) $2)', 'return': '(* (* (D $1 $2) (/ 1 $0)) (^ $1 (- (/ 1 $0) 1)))'}, 'minArgs': {'$0': 0, '$1': 1, '$2': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(* (* (D $1 $2) (/ 1 $0)) (^ $1 (- (/ 1 $0) 1)))', 'return': '(D (nroot $0 $1) $2)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)