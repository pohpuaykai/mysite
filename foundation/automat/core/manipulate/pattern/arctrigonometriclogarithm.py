
from foundation.automat.core.manipulate.manipulate import Manipulate


class Arctrigonometriclogarithm(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(arcsin $0)', 'return': '(- 0 (* i (log e (+ (* i $0) (nroot 2 (- 1 (^ $0 2)))))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- 0 (* i (log e (+ (* i $0) (nroot 2 (- 1 (^ $0 2)))))))', 'return': '(arcsin $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arccos $0)', 'return': '(- 0 (* i (log e (+ $0 (nroot 2 (- (^ $0 2) 1))))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- 0 (* i (log e (+ $0 (nroot 2 (- (^ $0 2) 1))))))', 'return': '(arccos $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arctan $0)', 'return': '(* (/ i 2) (log e (/ (+ i $0) (- i $0))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(* (/ i 2) (log e (/ (+ i $0) (- i $0))))', 'return': '(arctan $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arccosec $0)', 'return': '(- 0 (* i (log e (+ (/ i $0) (nroot 2 (- 1 (/ 1 (^ $0 2))))))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- 0 (* i (log e (+ (/ i $0) (nroot 2 (- 1 (/ 1 (^ $0 2))))))))', 'return': '(arccosec $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arcsec $0)', 'return': '(- 0 (* i (log e (+ (/ 1 $0) (* i (nroot 2 (- 1 (/ 1 (^ $0 2)))))))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- 0 (* i (log e (+ (/ 1 $0) (* i (nroot 2 (- 1 (/ 1 (^ $0 2)))))))))', 'return': '(arcsec $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arccot $0)', 'return': '(* (/ i 2) (log e (/ (- $0 i) (+ $0 i))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(* (/ i 2) (log e (/ (- $0 i) (+ $0 i))))', 'return': '(arccot $0)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)