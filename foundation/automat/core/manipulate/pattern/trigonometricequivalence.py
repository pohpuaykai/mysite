
from foundation.automat.core.manipulate.manipulate import Manipulate


class Trigonometricequivalence(Manipulate):
    """

    """
    TYPE = 'trigonometric_standard'

    def __init__(self, equation, direction, idx, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(/ (sin $0) (cos $0))', 'return': '(tan $0)'}, 'hin': {'scheme': '(tan $0)', 'return': '(/ (sin $0) (cos $0))'}, 'minArgs': {'$0': 0}}, {'type': 'regex', 'vor': {'scheme': '(/ (cos $0) (sin $0))', 'return': '(cot $0)'}, 'hin': {'scheme': '(cot $0)', 'return': '(/ (cos $0) (sin $0))'}, 'minArgs': {'$0': 0}}, {'type': 'regex', 'vor': {'scheme': '(/ 1 (sin $0))', 'return': '(cosec $0)'}, 'hin': {'scheme': '(cosec $0)', 'return': '(/ 1 (sin $0))'}, 'minArgs': {'$0': 0}}, {'type': 'regex', 'vor': {'scheme': '(/ 1 (cos $0))', 'return': '(sec $0)'}, 'hin': {'scheme': '(sec $0)', 'return': '(/ 1 (sec $0))'}, 'minArgs': {'$0': 0}}, {'type': 'regex', 'vor': {'scheme': '(/ 1 (tan $0))', 'return': '(cot $0)'}, 'hin': {'scheme': '(cot $0)', 'return': '(/ 1 (tan $0))'}, 'minArgs': {'$0': 0}}, {'type': 'regex', 'vor': {'scheme': '(/ 1 (cot $0))', 'return': '(tan $0)'}, 'hin': {'scheme': '(tan $0)', 'return': '(/ 1 (cot $0))'}, 'minArgs': {'$0': 0}}]
        super().__init__(equation, direction, idx, verbose=verbose)