
from foundation.automat.core.manipulate.manipulate import Manipulate


class Trigonometricintegration(Manipulate):
    """

    """
    TYPE = 'integration_trigonometric'
    NO_OF_MANIPULATIONS = '6'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(int (* (cos $0) (D $0 $1)) $1)', 'return': '(+ (sin $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (sin $0) $2)', 'return': '(int (* (cos $0) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (- 0 (sin $0)) (D $0 $1)) $1)', 'return': '(+ (cos $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (cos $0) $2)', 'return': '(int (* (- 0 (sin $0)) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (^ (sec $0) 2) (D $0 $1)) $1)', 'return': '(+ (tan $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (tan $0) $2)', 'return': '(int (* (^ (sec $0) 2) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (* (sec $0) (tan $0)) (D $0 $1)) $1)', 'return': '(+ (sec $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (sec $0) $2)', 'return': '(int (* (* (sec $0) (tan $0)) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (- 0 (* (cosec $0) (cot $0))) (D $0 $1)) $1)', 'return': '(+ (cosec $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (cosec $0) $2)', 'return': '(int (* (- 0 (* (cosec $0) (cot $0))) (D $0 $1)) $1)'}}, {'type': 'regex', 'vor': {'scheme': '(int (* (- 0 (^ cosec $0) 2) (D $0 $1)) $1)', 'return': '(+ (cot $0) $2)'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': 0}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (cot $0) $2)', 'return': '(int (* (- 0 (^ cosec $0) 2) (D $0 $1)) $1)'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)