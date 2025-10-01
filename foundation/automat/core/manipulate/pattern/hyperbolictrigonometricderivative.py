
from foundation.automat.core.manipulate.manipulate import Manipulate


class Hyperbolictrigonometricderivative(Manipulate):
    """

    """
    TYPE = 'derivative_hyperbolictrigonometric'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(D (sinh $0) $1)', 'return': '(* (cosh $0) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (cosh $0) (D $0 $1))', 'return': '(D (sinh $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (cosh $0) $1)', 'return': '(* (sinh $0) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (sinh $0) (D $0 $1))', 'return': '(D (cosh $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (tanh $0) $1)', 'return': '(* (/ 2 (+ (cosh (* 2 $0) 1))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (/ 2 (+ (cosh (* 2 $0) 1))) (D $0 $1))', 'return': '(D (tanh $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (sech $0) $1)', 'return': '(* (- 0 (* (tanh $0) (sech $0))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (- 0 (* (tanh $0) (sech $0))) (D $0 $1))', 'return': '(D (sech $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (cosech $0) $1)', 'return': '(* (- 0 (* (coth $0) (cosech $0))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (- 0 (* (coth $0) (cosech $0))) (D $0 $1))', 'return': '(D (cosech $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (coth $0) $1)', 'return': '(* (/ 2 (- 1 (sinh (* 2 $0)))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (/ 2 (- 1 (sinh (* 2 $0)))) (D $0 $1))', 'return': '(D (coth $0) $1)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)