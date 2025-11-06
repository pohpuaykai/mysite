
from foundation.automat.core.manipulate.manipulate import Manipulate


class Equalitycancellation(Manipulate):
    """

    """
    TYPE = 'essential'
    NO_OF_MANIPULATIONS = '7'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(= (* $0 $1) (* $0 $2))', 'return': '(= $1 $2)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(= $1 $2)', 'return': '(= (* $0 $1) (* $0 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(= (/ $0 $1) (/ $2 $1))', 'return': '(= $0 $2)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(= $0 $2)', 'return': '(= (/ $0 $1) (/ $2 $1))'}}, {'type': 'regex', 'vor': {'scheme': '(= (+ $0 $1) (+ $0 $2))', 'return': '(= $1 $2)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(= $1 $2)', 'return': '(= (+ $0 $1) (+ $0 $2))'}}, {'type': 'regex', 'vor': {'scheme': '(= (- $1 $0) (- $2 $0))', 'return': '(= $1 $2)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(= $1 $2)', 'return': '(= (- $1 $0) (- $2 $0))'}}, {'type': 'regex', 'vor': {'scheme': '(= (* $0 $1) $0)', 'return': '(= $1 1)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(= $1 1)', 'return': '(= (* $0 $1) $0)'}}, {'type': 'regex', 'vor': {'scheme': '(= (* (* $0 $1) $2) $0)', 'return': '(= (* $1 $2) 1)'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(= (* $1 $2) 1)', 'return': '(= (* (* $0 $1) $2) $0)'}}, {'type': 'regex', 'vor': {'scheme': '(= $0 (/ (* $1 $0) $2))', 'return': '(= 1 (/ $1 $2))'}, 'minArgs': {'$0': 0, '$1': 0}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(= 1 (/ $1 $2))', 'return': '(= $0 (/ (* $1 $0) $2))'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)