
from foundation.automat.core.manipulate.manipulate import Manipulate


class Nroot(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(nroot $0 (^ $1 $2))', 'return': '(^ $1 (/ $2 $0))'}, 'hin': {'scheme': '(^ $1 (/ $2 $0))', 'return': '(nroot $0 (^ $1 $2))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}}, {'type': 'regex', 'vor': {'scheme': '(^ (nroot $0 $1) $2)', 'return': '(nroot $0 (^ $1 $2))'}, 'hin': {'scheme': '(nroot $0 (^ $1 $2))', 'return': '(^ (nroot $0 $1) $2)'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}}, {'type': 'regex', 'vor': {'scheme': '(^ (nroot $0 $1) $2)', 'return': '(^ $1 (/ $2 $0))'}, 'hin': {'scheme': '(^ $1 (/ $2 $0))', 'return': '(^ (nroot $0 $1) $2)'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}}, {'type': 'regex', 'vor': {'scheme': '(nroot $2 (* $0 $1))', 'return': '(* (nroot $2 $0) (nroot $2 $1))'}, 'hin': {'scheme': '(* (nroot $2 $0) (nroot $2 $1))', 'return': '(nroot $2 (* $0 $1))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}}, {'type': 'regex', 'vor': {'scheme': '(nroot $2 (/ $0 $1))', 'return': '(/ (nroot $2 $0) (nroot $2 $1))'}, 'hin': {'scheme': '(/ (nroot $2 $0) (nroot $2 $1))', 'return': '(nroot $2 (/ $0 $1))'}, 'minArgs': {'$0': 0, '$1': 0, '$2': 0}}]
        super().__init__(equation, direction, idx, verbose=verbose)