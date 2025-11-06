
from foundation.automat.core.manipulate.manipulate import Manipulate


class ToDifferentialOperator(Manipulate):
    """

    """
    TYPE = 'essential'
    NO_OF_MANIPULATIONS = '4'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(* (/ d (* d $1)) $0)', 'return': '(D $0 $1)'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(D $0 $1)', 'return': '(* (/ d (* d $1)) $0)'}}, {'type': 'regex', 'vor': {'scheme': '(/ (* d $0) (* d $1))', 'return': '(D $0 $1)'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(D $0 $1)', 'return': '(/ (* d $0) (* d $1))'}}, {'type': 'regex', 'vor': {'scheme': '(* (/ partial (* partial $1)) $0)', 'return': '(D $0 $1)'}, 'minArgs': {'$0': 1, '$1': 1}, 'hin': {'scheme': '(D $0 $1)', 'return': '(* (/ partial (* partial $1)) $0)'}}, {'type': 'regex', 'vor': {'scheme': '(/ (* partial $0) (* partial $1))', 'return': '(D $0 $1)'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(D $0 $1)', 'return': '(/ (* partial $0) (* partial $1))'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)