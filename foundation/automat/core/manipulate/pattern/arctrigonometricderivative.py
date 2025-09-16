
from foundation.automat.core.manipulate.manipulate import Manipulate


class Arctrigonometricderivative(Manipulate):
    """

    """
    TYPE = 'derivative_trigonometric'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(D (arcsin $0) $1)', 'return': '(* (/ 1 (nroot 2 (- 1 (* $0 $0)))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (/ 1 (nroot 2 (- 1 (* $0 $0)))) (D $0 $1))', 'return': '(D (arcsin $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arccos $0) $1)', 'return': '(* (- 0 (/ 1 (nroot 2 (- 1 (* $0 $0))))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (- 0 (/ 1 (nroot 2 (- 1 (* $0 $0))))) (D $0 $1))', 'return': '(D (arccos $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arctan $0) $1)', 'return': '(* (/ 1 (+ 1 (* $0 $0))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (/ 1 (+ 1 (* $0 $0))) (D $0 $1))', 'return': '(D (arctan $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arcsec $0) $1)', 'return': '(* (/ 1 (* $0 (nroot 2 (- (* $0 $0) 1)))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (/ 1 (* $0 (nroot 2 (- (* $0 $0) 1)))) (D $0 $1))', 'return': '(D (arcsec $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arccosec $0) $1)', 'return': '(* (nroot 2 (- (* $0 $0) 1)) (D $1 $0))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (nroot 2 (- (* $0 $0) 1)) (D $1 $0))', 'return': '(D (arccosec $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arccot $0) $1)', 'return': '(* (- 0 (/ 1 (+ 1 (* $0 $0)))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (- 0 (/ 1 (+ 1 (* $0 $0)))) (D $0 $1))', 'return': '(D (arccot $0) $1)'}}]
        super().__init__(equation, direction, idx, verbose=verbose)