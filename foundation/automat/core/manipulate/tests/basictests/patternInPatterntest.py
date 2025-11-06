import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)

def test_findPatternInPatternAndThenGeneratePattern(verbose=False):
    manipulateClassEQ = Recommend.getManipulateClass('distributivity')
    direction = 'vor'
    idx = 0
    mEQ = manipulateClassEQ(direction, idx)#can manipulationClass not have schemeWord??<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # import pdb;pdb.set_trace()
    eq = Equation(mEQ.inputGrammar, 'scheme') # this is also a manipulation, but we only want the string
    manipulateClass = Recommend.getManipulateClass('communtativity')
    #manipulateClass.NO_OF_MANIPULATIONS [lower bound of idx], direction={vor, hin}
    manipulate = manipulateClass(direction, idx, calculateSchemeNodeChanges=True, verbose=verbose)
    """
    There is something wrong with 
    manipulate.py, line 112
    """
    returnTup = manipulate.apply(eq)#, startPos__nodeId=hint['startPos__nodeId'], toAst=True)
    if verbose:
        print(returnTup)


if __name__=='__main__':
    test_findPatternInPatternAndThenGeneratePattern(True)