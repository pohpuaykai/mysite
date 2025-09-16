
from foundation.automat.core.manipulate.manipulate import Manipulate


class Arctrigonometricintegration(Manipulate):
    """

    """
    TYPE = 'integration_trigonometric'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(int (* (/ 1 (nroot 2 (- 1 (* $0 $0)))) (D $0 $1)) $1)', 'return': '(+ (arcsin $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arcsin $0) $2)', 'return': '(int (* (/ 1 (nroot 2 (- 1 (* $0 $0)))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (- 0 (/ 1 (nroot 2 (- 1 (* $0 $0))))) (D $0 $1)) $1)', 'return': '(+ (arccos $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arccos $0) $2)', 'return': '(int (* (- 0 (/ 1 (nroot 2 (- 1 (* $0 $0))))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (/ 1 (+ 1 (* $0 $0))) (D $0 $1)) $1)', 'return': '(+ (arctan $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arctan $0) $2)', 'return': '(int (* (/ 1 (+ 1 (* $0 $0))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (/ 1 (* $0 (nroot 2 (- (* $0 $0) 1)))) (D $0 $1)) $1)', 'return': '(+ (arcsec $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arcsec $0) $2)', 'return': '(int (* (/ 1 (* $0 (nroot 2 (- (* $0 $0) 1)))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (nroot 2 (- (* $0 $0) 1)) (D $0 $1)) $1)', 'return': '(+ (arccosec $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arccosec $0) $2)', 'return': '(int (* (nroot 2 (- (* $0 $0) 1)) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (- 0 (/ 1 (+ 1 (* $0 $0)))) (D $0 $1)) $1)', 'return': '(+ (arccot $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (arccot $0) $2)', 'return': '(int (* (- 0 (/ 1 (+ 1 (* $0 $0)))) (D $0 $1)) $1)'}}]
        super().__init__(equation, direction, idx, verbose=verbose)