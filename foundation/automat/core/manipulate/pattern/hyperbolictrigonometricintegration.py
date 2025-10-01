
from foundation.automat.core.manipulate.manipulate import Manipulate


class Hyperbolictrigonometricintegration(Manipulate):
    """

    """
    TYPE = 'integration_hyperbolictrigonometric'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(int (* (cosh $0) (D $0 $1)) $1)', 'return': '(+ (sinh $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (sinh $0) $2)', 'return': '(int (* (cosh $0) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (sinh $0) (D $0 $1)) $1)', 'return': '(+ (cosh $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (cosh $0) $2)', 'return': '(int (* (sinh $0) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (/ 2 (+ (cosh (* 2 $0) 1))) (D $0 $1)) $1)', 'return': '(+ (tanh $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (tanh $0) $2)', 'return': '(int (* (/ 2 (+ (cosh (* 2 $0) 1))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (- 0 (* (tanh $0) (sech $0))) (D $0 $1)) $1)', 'return': '(+ (sech $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (sech $0) $2)', 'return': '(int (* (- 0 (* (tanh $0) (sech $0))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (- 0 (* (coth $0) (cosech $0))) (D $0 $1)) $1)', 'return': '(+ (cosech $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (cosech $0) $2)', 'return': '(int (* (- 0 (* (coth $0) (cosech $0))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (/ 2 (- 1 (sinh (* 2 $0)))) (D $0 $1)) $1)', 'return': '(+ (coth $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (coth $0) $2)', 'return': '(int (* (/ 2 (- 1 (sinh (* 2 $0)))) (D $0 $1)) $1)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)