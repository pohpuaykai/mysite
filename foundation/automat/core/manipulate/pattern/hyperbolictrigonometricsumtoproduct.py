
from foundation.automat.core.manipulate.manipulate import Manipulate


class Hyperbolictrigonometricsumtoproduct(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(+ (sinh $0) (sinh $1))', 'return': '(* (* 2 (sinh (/ (+ $0 $1) 2))) (cosh (/ (- $0 $1) 2)))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (* 2 (sinh (/ (+ $0 $1) 2))) (cosh (/ (- $0 $1) 2)))', 'return': '(+ (sinh $0) (sinh $1))'}}, {'type': 'regex', 'vor': {'scheme': '(+ (cosh $0) (cosh $1))', 'return': '(* (* 2 (cosh (/ (+ $0 $1) 2))) (cosh (/ (- $0 $1) 2)))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (* 2 (cosh (/ (+ $0 $1) 2))) (cosh (/ (- $0 $1) 2)))', 'return': '(+ (cosh $0) (cosh $1))'}}, {'type': 'regex', 'vor': {'scheme': '(- (sinh $0) (sinh $1))', 'return': '(* (* 2 (cosh (/ (+ $0 $1) 2))) (sinh (/ (- $0 $1) 2)))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (* 2 (cosh (/ (+ $0 $1) 2))) (sinh (/ (- $0 $1) 2)))', 'return': '(- (sinh $0) (sinh $1))'}}, {'type': 'regex', 'vor': {'scheme': '(- (cosh $0) (cosh $1))', 'return': '(* (* 2 (sinh (/ (+ $0 $1) 2))) (sinh (/ (- $0 $1) 2)))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(* (* 2 (sinh (/ (+ $0 $1) 2))) (sinh (/ (- $0 $1) 2)))', 'return': '(- (cosh $0) (cosh $1))'}}]
        super().__init__(equation, direction, idx, verbose=verbose)