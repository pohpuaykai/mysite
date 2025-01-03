
from foundation.automat.core.manipulate.manipulate import Manipulate


class Logarithm(Manipulate):
    """

    """
    TYPE = 'essential'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(log $0 (* $1 $2))', 'return': '(+ (log $0 $1) (log $0 $2))'}, 'hin': {'scheme': '(+ (log $0 $1) (log $0 $2))', 'return': '(log $0 (* $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 (/ $1 $2))', 'return': '(- (log $0 $1) (log $0 $2))'}, 'hin': {'scheme': '(- (log $0 $1) (log $0 $2))', 'return': '(log $0 (/ $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 (^ $1 $2))', 'return': '(* $2 (log $0 $1))'}, 'hin': {'scheme': '(* $2 (log $0 $1))', 'return': '(log $0 (^ $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 (nroot $1 $2))', 'return': '(/ (log $0 $2) $1)'}, 'hin': {'scheme': '(/ (log $0 $2) $1)', 'return': '(log $0 (nroot $1 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(/ (log $2 $1) (log $2 $0))', 'return': '(log $0 $1)'}, 'hin': {'scheme': '(log $0 $1)', 'return': '(/ (log $2 $1) (log $2 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 $0)', 'return': '1'}, 'hin': {'scheme': '1', 'return': '(log $0 $0)'}}, {'type': 'regex', 'vor': {'scheme': '(log $0 1)', 'return': '0'}, 'hin': {'scheme': '0', 'return': '(log $0 1)'}}]
        super().__init__(equation, direction, idx, verbose=verbose)