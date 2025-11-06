import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)

def test_findPatternInPatternAndThenGeneratePattern(verbose=False):
    manipulateClassEQ = Recommend.getManipulateClass('distributivity')
    import pdb;pdb.set_trace()
    eq = Equation(manipulateClassEQ.inputGrammar, 'scheme') # this is also a manipulation, but we only want the string
    manipulateClass = Recommend.getManipulateClass('communtativity')
    #how to get the direction and idx from the manipulateClass itself?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<not possible, maybe put it in?
    import pdb;pdb.set_trace()
    manipulate = manipulateClass(eq, idd['direction'], idd['idx'], calculateSchemeNodeChanges=True, verbose=self.verbose)
    returnTup = manipulate.apply(startPos__nodeId=hint['startPos__nodeId'], toAst=True)
    if verbose:
        print(returnTup)


if __name__=='__main__':
    test_findPatternInPatternAndThenGeneratePattern(True)