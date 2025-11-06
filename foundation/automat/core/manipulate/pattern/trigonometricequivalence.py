
from foundation.automat.core.manipulate.manipulate import Manipulate


class Trigonometricequivalence(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'
    NO_OF_MANIPULATIONS = '11'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(/ (sin $0) (cos $0))', 'return': '(tan $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(tan $0)', 'return': '(/ (sin $0) (cos $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ (cos $0) (sin $0))', 'return': '(cot $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(cot $0)', 'return': '(/ (cos $0) (sin $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ 1 (sin $0))', 'return': '(cosec $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(cosec $0)', 'return': '(/ 1 (sin $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ 1 (cos $0))', 'return': '(sec $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(sec $0)', 'return': '(/ 1 (cos $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ 1 (tan $0))', 'return': '(cot $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(cot $0)', 'return': '(/ 1 (tan $0))'}}, {'type': 'regex', 'vor': {'scheme': '(/ 1 (cot $0))', 'return': '(tan $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(tan $0)', 'return': '(/ 1 (cot $0))'}}, {'type': 'regex', 'vor': {'scheme': '(sin (- 0 $0))', 'return': '(- 0 (sin $0))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- 0 (sin $0))', 'return': '(sin (- 0 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(cos (- 0 $0))', 'return': '(cos $0)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(cos $0)', 'return': '(cos (- 0 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(sin $0)', 'return': '(/ (- (^ e (* i $0)) (^ e (- 0 (* i $0)))) (* 2 i))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (- (^ e (* i $0)) (^ e (- 0 (* i $0)))) (* 2 i))', 'return': '(sin $0)'}}, {'type': 'regex', 'vor': {'scheme': '(cos $0)', 'return': '(/ (+ (^ e (* i $0)) (^ e (- 0 (* i $0)))) 2)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (+ (^ e (* i $0)) (^ e (- 0 (* i $0)))) 2)', 'return': '(cos $0)'}}, {'type': 'regex', 'vor': {'scheme': '(^ e (* i $0))', 'return': '(+ (cos $0) (* i (sin $0)))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(+ (cos $0) (* i (sin $0)))', 'return': '(^ e (* i $0))'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)