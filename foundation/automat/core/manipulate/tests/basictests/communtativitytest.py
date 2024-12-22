import inspect
import pprint

from foundation.automat.core.equation import Equation
# from foundation.automat.core.manipulate import Manipulate
from foundation.automat.core.manipulate.pattern.communtativity import Communtativity


pp = pprint.PrettyPrinter(indent=4)


def test__oneLevelDepthOneSide__all(verbose=False):
    eq0 = Equation('(= a (+ b c))', 'scheme')
    ma0 = Communtativity(eq0, verbose=verbose)
    patternDict = ma0.rawRegexes[0] # TODO do for all
    if verbose:
        pp.pprint(patternDict)
    manipulatedSchemeEquation = ma0.apply(patternDict['vor']['propreRegex'], patternDict['vor']['return'])
    expected = '' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        # pp.pprint(subTree)
        print(manipulatedSchemeEquation)


if __name__=='__main__':
    test__oneLevelDepthOneSide__all(True) # not yet pass