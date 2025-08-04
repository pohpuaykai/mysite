
from foundation.automat.core.manipulate.manipulate import Manipulate


class Logarithmicderivative(Manipulate):
    """

    """
    TYPE = 'derivative_logarithm'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(D (log $0 $1) $2)', 'return': '(/ (- (* (* (D $1 $2) (/ "1" $1)) (log "e" $0)) (* (* (D $0 $2) (/ "1" $0)) (log "e" $1))) (^ (log "e" $0) "2"))'}, 'minArgs': {'$0': 1, '$1': 1, '$2': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(/ (- (* (* (D $1 $2) (/ "1" $1)) (log "e" $0)) (* (* (D $0 $2) (/ "1" $0)) (log "e" $1))) (^ (log "e" $0) "2"))', 'return': '(D (log $0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(D (log $0 $1) $2)', 'return': '(/ (D $1 $2) (* $1 (log "e" $0)))'}, 'minArgs': {'$0': 0, '$1': 1, '$2': 1}, 'maxArgs': {'$0': None, '$1': None, '$2': None}, 'preCond': {'$0': None, '$1': None, '$2': None}, 'hin': {'scheme': '(/ (D $1 $2) (* $1 (log "e" $0)))', 'return': '(D (log $0 $1) $2)'}}, {'type': 'regex', 'vor': {'scheme': '(D (log "e" $0) $1)', 'return': '(/ (D $0 $1) $1)'}, 'minArgs': {'$0': 1, '$1': 1}, 'maxArgs': {'$0': None, '$1': None}, 'preCond': {'$0': None, '$1': None}, 'hin': {'scheme': '(/ (D $0 $1) $1)', 'return': '(D (log "e" $0) $1)'}}]
        super().__init__(equation, direction, idx, verbose=verbose)