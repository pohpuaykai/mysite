
from foundation.automat.core.manipulate.manipulate import Manipulate


class Archyperbolictrigonometricderivative(Manipulate):
    """

    """
    TYPE = 'derivative_archyperbolictrigonometric'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(D (arcsinh $0) $1)', 'return': '(* (sech (arcsinh $0)) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (sech (arcsinh $0)) (D $0 $1))', 'return': '(D (arcsinh $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arccosh $0) $1)', 'return': '(* (cosech (arccosh $0)) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (cosech (arccosh $0)) (D $0 $1))', 'return': '(D (arccosh $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arctanh $0) $1)', 'return': '(* (/ (+ 1 (cosh (* 2 (arctanh $0)))) 2) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (/ (+ 1 (cosh (* 2 (arctanh $0)))) 2) (D $0 $1))', 'return': '(D (arctanh $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arcsech $0) $1)', 'return': '(* (* (- 0 (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (* (- 0 (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1))', 'return': '(D (arcsech $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arccosech $0) $1)', 'return': '(* (* (- 0 (sinh (arccosech $0)))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (* (- 0 (sinh (arccosech $0)))) (D $0 $1))', 'return': '(D (arccosech $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (arccoth $0) $1)', 'return': '(* (/ (- 1 (sinh (arccoth $0))) 2) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (/ (- 1 (sinh (arccoth $0))) 2) (D $0 $1))', 'return': '(D (arccoth $0) $1)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)