
from foundation.automat.core.manipulate.manipulate import Manipulate


class Hyperbolictrigonometricexponential(Manipulate):
    """

    """
    TYPE = 'essential'
    NO_OF_MANIPULATIONS = '5'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(^ e $0)', 'return': '(nroot 2 (/ (+ 1 (tanh $0)) (- 1 (tanh $0))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(nroot 2 (/ (+ 1 (tanh $0)) (- 1 (tanh $0))))', 'return': '(^ e $0)'}}, {'type': 'regex', 'vor': {'scheme': '(^ e $0)', 'return': '(/ (+ 1 (tanh (/ $0 2))) (- 1 (tanh (/ $0 2))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (+ 1 (tanh (/ $0 2))) (- 1 (tanh (/ $0 2))))', 'return': '(^ e $0)'}}, {'type': 'regex', 'vor': {'scheme': '(^ e (* i $0))', 'return': '(+ (sinh (* i $0)) (cosh (* i $0)))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(+ (sinh (* i $0)) (cosh (* i $0)))', 'return': '(^ e (* i $0))'}}, {'type': 'regex', 'vor': {'scheme': '(^ e $0)', 'return': '(+ (sinh $0) (cosh $0))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(+ (sinh $0) (cosh $0))', 'return': '(^ e $0)'}}, {'type': 'regex', 'vor': {'scheme': '(^ e (- 0 $0))', 'return': '(- (cosh $0) (sinh $0))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(- (cosh $0) (sinh $0))', 'return': '(^ e (- 0 $0))'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)