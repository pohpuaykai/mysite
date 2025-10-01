
from foundation.automat.core.manipulate.manipulate import Manipulate


class Quadraticpolynomial(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)', 'return': '(= $3 (/ (+ (- 0 $1) (nroot 2 (- (^ $1 2) (* (* 4 $0) $2)))) (* 2 $0)))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0, '$3': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None, '$3': None}, 'preCond': {'$0': None, '$1': None, '$2': None, '$3': None}, 'hin': {'scheme': '(= $3 (/ (+ (- 0 $1) (nroot 2 (- (^ $1 2) (* (* 4 $0) $2)))) (* 2 $0)))', 'return': '(= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)'}}, {'type': 'regex', 'vor': {'scheme': '(= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)', 'return': '(= $3 (/ (- (- 0 $1) (nroot 2 (- (^ $1 2) (* (* 4 $0) $2)))) (* 2 $0)))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0, '$3': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None, '$3': None}, 'preCond': {'$0': None, '$1': None, '$2': None, '$3': None}, 'hin': {'scheme': '(= $3 (/ (- (- 0 $1) (nroot 2 (- (^ $1 2) (* (* 4 $0) $2)))) (* 2 $0)))', 'return': '(= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)'}}, {'type': 'regex', 'vor': {'scheme': '(= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)', 'return': '(= (+ (* $0 (^ (+ $3 (/ $1 (* 2 $0))) 2)) (- $2 (/ (^ $1 2) (* 4 $0)))) 0)'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0, '$3': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None, '$3': None}, 'preCond': {'$0': None, '$1': None, '$2': None, '$3': None}, 'hin': {'scheme': '(= (+ (* $0 (^ (+ $3 (/ $1 (* 2 $0))) 2)) (- $2 (/ (^ $1 2) (* 4 $0)))) 0)', 'return': '(= (+ (+ (* $0 (^ $3 2)) (* $1 $3)) $2) 0)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)