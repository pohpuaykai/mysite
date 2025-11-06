
from foundation.automat.core.manipulate.manipulate import Manipulate


class Pythagoreanangle(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'
    NO_OF_MANIPULATIONS = '6'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(+ (^ (sin $0) 2) (^ (cos $0) 2))', 'return': '1'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '1', 'return': '(+ (^ (sin $0) 2) (^ (cos $0) 2))'}}, {'type': 'regex', 'vor': {'scheme': '(+ 1 (^ (tan $0) 2))', 'return': '(^ (sec $0) 2)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(^ (sec $0) 2)', 'return': '(+ 1 (^ (tan $0) 2))'}}, {'type': 'regex', 'vor': {'scheme': '(+ (^ (cot $0) 2) 1)', 'return': '(^ (cosec $0) 2)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(^ (cosec $0) 2)', 'return': '(+ (^ (cot $0) 2) 1)'}}, {'type': 'regex', 'vor': {'scheme': '(- (^ (cosh $0) 2) (^ (sinh $0) 2))', 'return': '1'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '1', 'return': '(- (^ (cosh $0) 2) (^ (sinh $0) 2))'}}, {'type': 'regex', 'vor': {'scheme': '(^ (sech $0) 2)', 'return': '(- 1 (^ (tanh $0) 2))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- 1 (^ (tanh $0) 2))', 'return': '(^ (sech $0) 2)'}}, {'type': 'regex', 'vor': {'scheme': '(^ (cosech $0) 2)', 'return': '(- (^ (coth $0) 2) 1)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- (^ (coth $0) 2) 1)', 'return': '(^ (cosech $0) 2)'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)