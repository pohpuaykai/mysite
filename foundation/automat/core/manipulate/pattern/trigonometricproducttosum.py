
from foundation.automat.core.manipulate.manipulate import Manipulate


class Trigonometricproducttosum(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(* (cos $0) (cos $1))', 'return': '(/ (+ (cos (- $0 $1)) (cos (+ $0 $1))) 2)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ (+ (cos (- $0 $1)) (cos (+ $0 $1))) 2)', 'return': '(* (cos $0) (cos $1))'}}, {'type': 'regex', 'vor': {'scheme': '(* (sin $0) (sin $1))', 'return': '(/ (- (cos (- $0 $1)) (cos (+ $0 $1))) 2)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ (- (cos (- $0 $1)) (cos (+ $0 $1))) 2)', 'return': '(* (sin $0) (sin $1))'}}, {'type': 'regex', 'vor': {'scheme': '(* (sin $0) (cos $1))', 'return': '(/ (+ (sin (+ $0 $1)) (sin (- $0 $1))) 2)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ (+ (sin (+ $0 $1)) (sin (- $0 $1))) 2)', 'return': '(* (sin $0) (cos $1))'}}, {'type': 'regex', 'vor': {'scheme': '(* (cos $0) (sin $1))', 'return': '(/ (- (sin (+ $0 $1)) (sin (- $0 $1))) 2)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ (- (sin (+ $0 $1)) (sin (- $0 $1))) 2)', 'return': '(* (cos $0) (sin $1))'}}, {'type': 'regex', 'vor': {'scheme': '(* (tan $0) (tan $1))', 'return': '(/ (- (cos (- $0 $1)) (cos (+ $0 $1))) (+ (cos (- $0 $1)) (cos (+ $0 $1))))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ (- (cos (- $0 $1)) (cos (+ $0 $1))) (+ (cos (- $0 $1)) (cos (+ $0 $1))))', 'return': '(* (tan $0) (tan $1))'}}, {'type': 'regex', 'vor': {'scheme': '(* (tan $0) (cot $1))', 'return': '(/ (+ (sin (+ $0 $1)) (sin (- $0 $1))) (- (sin (+ $0 $1)) (sin (- $0 $1))))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ (+ (sin (+ $0 $1)) (sin (- $0 $1))) (- (sin (+ $0 $1)) (sin (- $0 $1))))', 'return': '(* (tan $0) (cot $1))'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)