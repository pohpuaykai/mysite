
from foundation.automat.core.manipulate.manipulate import Manipulate


class Trigonometricequivalence(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(/ (sin $0) (cos $0))', 'return': '(tan $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(tan $0)', 'return': '(/ (sin $0) (cos $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ (cos $0) (sin $0))', 'return': '(cot $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(cot $0)', 'return': '(/ (cos $0) (sin $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ "1" (sin $0))', 'return': '(cosec $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(cosec $0)', 'return': '(/ "1" (sin $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ "1" (cos $0))', 'return': '(sec $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(sec $0)', 'return': '(/ "1" (cos $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ "1" (tan $0))', 'return': '(cot $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(cot $0)', 'return': '(/ "1" (tan $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ "1" (cot $0))', 'return': '(tan $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(tan $0)', 'return': '(/ "1" (cot $0))'}}, {'type': 'regex', 'vor': {'scheme': '(sin (- "0" x))', 'return': '(- "0" (sin x))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- "0" (sin x))', 'return': '(sin (- "0" x))'}}, {'type': 'regex', 'vor': {'scheme': '(cos (- "0" x))', 'return': '(cos x)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(cos x)', 'return': '(cos (- "0" x))'}}, {'type': 'regex', 'vor': {'scheme': '(sin x)', 'return': '(/ (- (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) (* "2" "i"))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (- (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) (* "2" "i"))', 'return': '(sin x)'}}, {'type': 'regex', 'vor': {'scheme': '(cos x)', 'return': '(/ (+ (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) "2")'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (+ (^ "e" (* "i" x)) (^ "e" (- "0" (* "i" x)))) "2")', 'return': '(cos x)'}}, {'type': 'regex', 'vor': {'scheme': '(^ "e" (* "i" x))', 'return': '(+ (cos x) (* "i" (sin x)))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(+ (cos x) (* "i" (sin x)))', 'return': '(^ "e" (* "i" x))'}}]
        super().__init__(equation, direction, idx, verbose=verbose)