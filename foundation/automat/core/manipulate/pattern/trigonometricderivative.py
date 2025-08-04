
from foundation.automat.core.manipulate.manipulate import Manipulate


class Trigonometricderivative(Manipulate):
    """

    """
    TYPE = 'derivative_trigonometric'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(D (sin $0) $1)', 'return': '(* (cos $0) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (cos $0) (D $0 $1))', 'return': '(D (sin $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (cos $0) $1)', 'return': '(* (- "0" (sin $0)) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (- "0" (sin $0)) (D $0 $1))', 'return': '(D (cos $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (tan $0) $1)', 'return': '(* (^ (sec $0) "2") (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (^ (sec $0) "2") (D $0 $1))', 'return': '(D (tan $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (sec $0) $1)', 'return': '(* (* (sec $0) (tan $0)) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (* (sec $0) (tan $0)) (D $0 $1))', 'return': '(D (sec $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (cosec $0) $1)', 'return': '(* (- "0" (* (cosec $0) (cot $0))) (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (- "0" (* (cosec $0) (cot $0))) (D $0 $1))', 'return': '(D (cosec $0) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(D (cot $0) $1)', 'return': '(* (- "0" (^ cosec $0) "2") (D $0 $1))'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (- "0" (^ cosec $0) "2") (D $0 $1))', 'return': '(D (cot $0) $1)'}}]
        super().__init__(equation, direction, idx, verbose=verbose)