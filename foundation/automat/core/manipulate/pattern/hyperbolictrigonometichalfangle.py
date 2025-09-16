
from foundation.automat.core.manipulate.manipulate import Manipulate


class Hyperbolictrigonometichalfangle(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(sinh (/ $0 "2"))', 'return': '(/ (sinh $0) (nroot "2" (* "2" (+ (cosh $0) "1"))))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (sinh $0) (nroot "2" (* "2" (+ (cosh $0) "1"))))', 'return': '(sinh (/ $0 "2"))'}}, {'type': 'regex', 'vor': {'scheme': '(cosh (/ $0 "2"))', 'return': '(nroot "2" (/ (+ (cosh $0) "1") "2"))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(nroot "2" (/ (+ (cosh $0) "1") "2"))', 'return': '(cosh (/ $0 "2"))'}}, {'type': 'regex', 'vor': {'scheme': '(tanh (/ $0 "2"))', 'return': '(/ (sinh $0) (+ (cosh $0) "1"))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(/ (sinh $0) (+ (cosh $0) "1"))', 'return': '(tanh (/ $0 "2"))'}}]
        super().__init__(equation, direction, idx, verbose=verbose)