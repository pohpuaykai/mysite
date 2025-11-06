
from foundation.automat.core.manipulate.manipulate import Manipulate


class Nroot(Manipulate):
    """

    """
    TYPE = 'essential'
    NO_OF_MANIPULATIONS = '5'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(nroot $0 (^ $1 $2))', 'return': '(^ $1 (/ $2 $0))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(^ $1 (/ $2 $0))', 'return': '(nroot $0 (^ $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(^ (nroot $0 $1) $2)', 'return': '(nroot $0 (^ $1 $2))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(nroot $0 (^ $1 $2))', 'return': '(^ (nroot $0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(^ (nroot $0 $1) $2)', 'return': '(^ $1 (/ $2 $0))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(^ $1 (/ $2 $0))', 'return': '(^ (nroot $0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(nroot $2 (* $0 $1))', 'return': '(* (nroot $2 $0) (nroot $2 $1))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(* (nroot $2 $0) (nroot $2 $1))', 'return': '(nroot $2 (* $0 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(nroot $2 (/ $0 $1))', 'return': '(/ (nroot $2 $0) (nroot $2 $1))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(/ (nroot $2 $0) (nroot $2 $1))', 'return': '(nroot $2 (/ $0 $1))'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)