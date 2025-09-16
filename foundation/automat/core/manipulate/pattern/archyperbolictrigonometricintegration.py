
from foundation.automat.core.manipulate.manipulate import Manipulate


class Archyperbolictrigonometricintegration(Manipulate):
    """

    """
    TYPE = 'integration_archyperbolictrigonometric'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(int (* (sech (arcsinh $0)) (D $0 $1)) $1)', 'return': '(+ (arcsinh $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arcsinh $0) $2)', 'return': '(int (* (sech (arcsinh $0)) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (cosech (arccosh $0)) (D $0 $1)) $1)', 'return': '(+ (arccosh $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arccosh $0) $2)', 'return': '(int (* (cosech (arccosh $0)) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (/ (+ 1 (cosh (* 2 (arctanh $0)))) 2) (D $0 $1)) $1)', 'return': '(+ (arctanh $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arctanh $0) $2)', 'return': '(int (* (/ (+ 1 (cosh (* 2 (arctanh $0)))) 2) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (* (- 0 (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1)) $1)', 'return': '(+ (arcsech $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arcsech $0) $2)', 'return': '(int (* (* (- 0 (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (* (- 0 (sinh (arccosech $0)))) (D $0 $1)) $1)', 'return': '(+ (arccosech $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arccosech $0) $2)', 'return': '(int (* (* (- 0 (sinh (arccosech $0)))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (/ (- 1 (sinh (arccoth $0))) 2) (D $0 $1)) $1)', 'return': '(+ (arccoth $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arccoth $0) $2)', 'return': '(int (* (/ (- 1 (sinh (arccoth $0))) 2) (D $0 $1)) $1)'}}]
        super().__init__(equation, direction, idx, verbose=verbose)