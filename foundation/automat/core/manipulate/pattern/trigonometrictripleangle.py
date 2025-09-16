
from foundation.automat.core.manipulate.manipulate import Manipulate


class Trigonometrictripleangle(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(sin (* 3 x))', 'return': '(- (* 3 (sin x)) (* 4 (^ (sin x) 3)))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- (* 3 (sin x)) (* 4 (^ (sin x) 3)))', 'return': '(sin (* 3 x))'}}, {'type': 'regex', 'vor': {'scheme': '(cos (* 3 x))', 'return': '(- (* 4 (^ (cos x) 3)) (* 3 (cos x)))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- (* 4 (^ (cos x) 3)) (* 3 (cos x)))', 'return': '(cos (* 3 x))'}}, {'type': 'regex', 'vor': {'scheme': '(tan (* 3 x))', 'return': '(/ (- (* 3 (tan x)) (^ (tan x) 3)) (- 1 (* 3 (^ (tan x) 2))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (- (* 3 (tan x)) (^ (tan x) 3)) (- 1 (* 3 (^ (tan x) 2))))', 'return': '(tan (* 3 x))'}}, {'type': 'regex', 'vor': {'scheme': '(cot (* 3 x))', 'return': '(/ (- (* 3 (cot x)) (^ (cot x) 3)) (- 1 (* 3 (^ (cot x) 2))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (- (* 3 (cot x)) (^ (cot x) 3)) (- 1 (* 3 (^ (cot x) 2))))', 'return': '(cot (* 3 x))'}}, {'type': 'regex', 'vor': {'scheme': '(sec (* 3 x))', 'return': '(/ (^ (sec x) 3) (- 4 (* 3 (^ (sec x) 2))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (^ (sec x) 3) (- 4 (* 3 (^ (sec x) 2))))', 'return': '(sec (* 3 x))'}}, {'type': 'regex', 'vor': {'scheme': '(cosec (* 3 x))', 'return': '(/ (^ (cosec x) 3) (- (* 3 (^ (cosec x) 3)) 4))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (^ (cosec x) 3) (- (* 3 (^ (cosec x) 3)) 4))', 'return': '(cosec (* 3 x))'}}]
        super().__init__(equation, direction, idx, verbose=verbose)