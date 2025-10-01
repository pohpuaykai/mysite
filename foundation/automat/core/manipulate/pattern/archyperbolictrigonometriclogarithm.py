
from foundation.automat.core.manipulate.manipulate import Manipulate


class Archyperbolictrigonometriclogarithm(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(arcsinh $0)', 'return': '(log e (+ $0 (nroot 2 (+ (^ $0 2) 1))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(log e (+ $0 (nroot 2 (+ (^ $0 2) 1))))', 'return': '(arcsinh $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arccosh $0)', 'return': '(log e (+ $0 (nroot 2 (- (^ $0 2) 1))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(log e (+ $0 (nroot 2 (- (^ $0 2) 1))))', 'return': '(arccosh $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arctanh $0)', 'return': '(/ (log e (/ (+ 1 $0) (- 1 $0))) 2)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (log e (/ (+ 1 $0) (- 1 $0))) 2)', 'return': '(arctanh $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arccoth $0)', 'return': '(/ (log e (/ (+ $0 1) (- $0 1))) 2)'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (log e (/ (+ $0 1) (- $0 1))) 2)', 'return': '(arccoth $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arcsech $0)', 'return': '(log e (+ (/ 1 $0) (nroot 2 (- (/ 1 (^ $0 2)) 1))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(log e (+ (/ 1 $0) (nroot 2 (- (/ 1 (^ $0 2)) 1))))', 'return': '(arcsech $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arcsech $0)', 'return': '(log e (/ (+ 1 (nroot 2 (- 1 (^ $0 2)))) $0))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(log e (/ (+ 1 (nroot 2 (- 1 (^ $0 2)))) $0))', 'return': '(arcsech $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arccosech $0)', 'return': '(log e (+ (/ 1 $0) (nroot 2 (+ (/ 1 (^ $0 2)) 1))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(log e (+ (/ 1 $0) (nroot 2 (+ (/ 1 (^ $0 2)) 1))))', 'return': '(arccosech $0)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)