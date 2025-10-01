
from foundation.automat.core.manipulate.manipulate import Manipulate


class Arctrigonometricdefinition(Manipulate):
    """

    """
    TYPE = 'arctrigonometric_standard'

    def __init__(self, equation, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(arcsin (sin $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arcsin (sin $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arccos (cos $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arccos (cos $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arctan (tan $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arctan (tan $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arcsec (sec $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arcsec (sec $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arccosec (cosec $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arccosec (cosec $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arccot (cot $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arccot (cot $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arcsech $0)', 'return': '(arccosh (/ 1 $0))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(arccosh (/ 1 $0))', 'return': '(arcsech $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arccosech $0)', 'return': '(arcsinh (/ 1 $0))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(arcsinh (/ 1 $0))', 'return': '(arccosech $0)'}}, {'type': 'regex', 'vor': {'scheme': '(arccoth $0)', 'return': '(arctanh (/ 1 $0))'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '(arctanh (/ 1 $0))', 'return': '(arccoth $0)'}}]
        super().__init__(equation, direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)