
from foundation.automat.core.manipulate.manipulate import Manipulate


class Derivativerules(Manipulate):
    """

    """
    TYPE = 'essential'
    NO_OF_MANIPULATIONS = '4'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(D ($0 $1) $2)', 'return': '(* (D ($0 $1) $1) (D $1 $2))'}, 'minArgs': {'$0': 2, '$1': 1, '$2': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(* (D ($0 $1) $1) (D $1 $2))', 'return': '(D ($0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(D (+ $0 $1) $2)', 'return': '(+ (D $0 $2) (D $1 $2))'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (D $0 $2) (D $1 $2))', 'return': '(D (+ $0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(D (* $0 $1) $2)', 'return': '(+ (* $0 (D $1 $2)) (* $1 (D $0 $2)))'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(+ (* $0 (D $1 $2)) (* $1 (D $0 $2)))', 'return': '(D (* $0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(D (/ $0 $1) $2)', 'return': '(/ (- (* $1 (D $0 $2)) (* $0 (D $1 $2))) (* $1 $1))'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(/ (- (* $1 (D $0 $2)) (* $0 (D $1 $2))) (* $1 $1))', 'return': '(D (/ $0 $1) $2)'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)