
from foundation.automat.core.manipulate.manipulate import Manipulate


class Archyperbolictrigonometricdefinition(Manipulate):
    """

    """
    TYPE = 'archyperbolictrigonometric_standard'
    NO_OF_MANIPULATIONS = '12'
    

    def __init__(self, direction, idx, calculateSchemeNodeChanges=False, verbose=False):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(arcsinh (sinh $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arcsinh (sinh $0))'}}, {'type': 'regex', 'vor': {'scheme': '(sinh (arcsinh $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(sinh (arcsinh $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arccosh (cosh $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arccosh (cosh $0))'}}, {'type': 'regex', 'vor': {'scheme': '(cosh (arccosh $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(cosh (arccosh $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arctanh (tanh $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arctanh (tanh $0))'}}, {'type': 'regex', 'vor': {'scheme': '(tanh (arctanh $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(tanh (arctanh $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arcsech (sech $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arcsech (sech $0))'}}, {'type': 'regex', 'vor': {'scheme': '(sech (arcsech $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(sech (arcsech $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arccosech (cosech $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arccosech (cosech $0))'}}, {'type': 'regex', 'vor': {'scheme': '(cosech (arccosech $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(cosech (arccosech $0))'}}, {'type': 'regex', 'vor': {'scheme': '(arccoth (coth $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(arccoth (coth $0))'}}, {'type': 'regex', 'vor': {'scheme': '(coth (arccoth $0))', 'return': '$0'}, 'minArgs': {'$0': 0}, 'maxArgs': {'$0': None}, 'preCond': {'$0': None}, 'hin': {'scheme': '$0', 'return': '(coth (arccoth $0))'}}]
        super().__init__(direction, idx, calculateSchemeNodeChanges=calculateSchemeNodeChanges, verbose=verbose)