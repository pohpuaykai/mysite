
from foundation.automat.core.manipulate.manipulate import Manipulate


class Hyperbolictrigonometricdoubleangle(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(cosh (* 2 $0))', 'return': '(+ (^ (sinh $0) 2) (^ (cosh $0) 2))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(+ (^ (sinh $0) 2) (^ (cosh $0) 2))', 'return': '(cosh (* 2 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(cosh (* 2 $0))', 'return': '(+ (* 2 (^ (sinh $0) 2)) 1)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(+ (* 2 (^ (sinh $0) 2)) 1)', 'return': '(cosh (* 2 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(cosh (* 2 $0))', 'return': '(- (* 2 (^ (cosh $0) 2)) 1)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- (* 2 (^ (cosh $0) 2)) 1)', 'return': '(cosh (* 2 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(sinh (* 2 $0))', 'return': '(* (* 2 (sinh $0)) (cosh $0))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(* (* 2 (sinh $0)) (cosh $0))', 'return': '(sinh (* 2 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(tanh (* 2 $0))', 'return': '(/ (* 2 (tanh $0)) (+ 1 (^ (tanh $0) 2)))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (* 2 (tanh $0)) (+ 1 (^ (tanh $0) 2)))', 'return': '(tanh (* 2 $0))'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)