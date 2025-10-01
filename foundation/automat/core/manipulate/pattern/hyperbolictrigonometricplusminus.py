
from foundation.automat.core.manipulate.manipulate import Manipulate


class Hyperbolictrigonometricplusminus(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(sinh (+ $0 $1))', 'return': '(+ (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(+ (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))', 'return': '(sinh (+ $0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(cosh (+ $0 $1))', 'return': '(+ (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(+ (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))', 'return': '(cosh (+ $0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(tanh (+ $0 $1))', 'return': '(/ (+ (tanh $0) (tanh $1)) (+ 1 (* (tanh $0) (tanh $1))))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ (+ (tanh $0) (tanh $1)) (+ 1 (* (tanh $0) (tanh $1))))', 'return': '(tanh (+ $0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(sinh (- $0 $1))', 'return': '(- (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(- (* (sinh $0) (cosh $1)) (* (cosh $0) (sinh $1)))', 'return': '(sinh (- $0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(cosh (- $0 $1))', 'return': '(- (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(- (* (cosh $0) (cosh $1)) (* (sinh $0) (sinh $1)))', 'return': '(cosh (- $0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(tanh (- $0 $1))', 'return': '(/ (- (tanh $0) (tanh $1)) (- 1 (* (tanh $0) (tanh $1))))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ (- (tanh $0) (tanh $1)) (- 1 (* (tanh $0) (tanh $1))))', 'return': '(tanh (- $0 $1))'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)