import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend


pp = pprint.PrettyPrinter(indent=4)



def test__deriveMetaInformation__basic(verbose=False):
    eqs = '(= a (+ b c))' # fill it in
    eqsType = 'scheme'
    #filename = 'communtativity'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    rec = Recommend(eq0, verbose=verbose)
    manipulatedSchemeEquation = rec._deriveMetaInformation() # (+ $0 $1)
    expected = '(= a (+ c b))' # (+ $1 $0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    


if __name__=='__main__':
    test__deriveMetaInformation__basic(True)
    