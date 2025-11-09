import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend
from foundation.automat.parser.sorte.schemeparser import Schemeparser


pp = pprint.PrettyPrinter(indent=4)

def test_findPatternInPatternAndThenGeneratePatternAddition(verbose=False):
    manipulateClassEQ = Recommend.getManipulateClass('distributivity')
    directionEQ = 'vor'
    idxEQ = 0
    mEQ = manipulateClassEQ(directionEQ, idxEQ)#can manipulationClass not have schemeWord??<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # import pdb;pdb.set_trace()
    eq = Equation(mEQ.inputGrammar, 'scheme') # this is also a manipulation, but we only want the string
    manipulateClass = Recommend.getManipulateClass('communtativity')
    #manipulateClass.NO_OF_MANIPULATIONS [lower bound of idx], direction={vor, hin}
    idx = 0
    direction = 'vor'
    manipulate = manipulateClass(direction, idx, calculateSchemeNodeChanges=True, verbose=verbose)
    returnTup = manipulate.apply(eq, startPos__nodeId=eq.startPos__nodeId)#, startPos__nodeId=hint['startPos__nodeId'], toAst=True)
    eq, _, _, _, _ = returnTup
    if verbose:
        print(eq.schemeStr)
        # print(eq.latexStr)


def test_findPatternInPatternAndThenGeneratePatternMultiplication(verbose=False):
    manipulateClassEQ = Recommend.getManipulateClass('distributivity')
    directionEQ = 'vor'
    idxEQ = 0
    mEQ = manipulateClassEQ(directionEQ, idxEQ)#can manipulationClass not have schemeWord??<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # import pdb;pdb.set_trace()
    eq = Equation(mEQ.inputGrammar, 'scheme') # this is also a manipulation, but we only want the string
    manipulateClass = Recommend.getManipulateClass('communtativity')
    #manipulateClass.NO_OF_MANIPULATIONS [lower bound of idx], direction={vor, hin}
    idx = 1
    direction = 'vor'
    manipulate = manipulateClass(direction, idx, calculateSchemeNodeChanges=True, verbose=verbose)
    returnTup = manipulate.apply(eq, startPos__nodeId=eq.startPos__nodeId)#, startPos__nodeId=hint['startPos__nodeId'], toAst=True)
    eq, _, _, _, _ = returnTup
    if verbose:
        print(eq.schemeStr)
        # print(eq.latexStr)
    


def test_findPatternInPatternAndThenGeneratePatternSkipNodes(verbose=False): # this is also MODE2
    manipulateClassEQ = Recommend.getManipulateClass('partialfraction')
    directionEQ = 'vor'
    idxEQ = 0
    mEQ = manipulateClassEQ(directionEQ, idxEQ)#can manipulationClass not have schemeWord??<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # import pdb;pdb.set_trace()
    eq = Equation(mEQ.inputGrammar, 'scheme') # this is also a manipulation, but we only want the string
    manipulateClass = Recommend.getManipulateClass('communtativity')
    #manipulateClass.NO_OF_MANIPULATIONS [lower bound of idx], direction={vor, hin}
    idx = 1
    direction = 'vor'
    manipulate = manipulateClass(direction, idx, calculateSchemeNodeChanges=True, verbose=verbose)
    returnTup = manipulate.apply(eq, startPos__nodeId=eq.startPos__nodeId)#, startPos__nodeId=hint['startPos__nodeId'], toAst=True)
    eq, _, _, _, _ = returnTup
    if verbose:
        print(eq.schemeStr)
        # print(eq.latexStr)



def test_findPatternInPatternAndThenGeneratePatternSkipNodesMODE0(verbose=False):
    manipulateClassEQ = Recommend.getManipulateClass('pythagoreanangle')#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    directionEQ = 'hin'
    idxEQ = 0
    mEQ = manipulateClassEQ(directionEQ, idxEQ)
    # import pdb;pdb.set_trace()
    eq = Equation(mEQ.inputGrammar, 'scheme') # this is also a manipulation, but we only want the string
    manipulateClass = Recommend.getManipulateClass('logarithm')#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #manipulateClass.NO_OF_MANIPULATIONS [lower bound of idx], direction={vor, hin}
    idx = 5
    direction = 'hin'
    manipulate = manipulateClass(direction, idx, calculateSchemeNodeChanges=True, verbose=verbose)
    returnTup = manipulate.apply(eq, startPos__nodeId=eq.startPos__nodeId)#, startPos__nodeId=hint['startPos__nodeId'], toAst=True)
    eq, _, _, _, _ = returnTup
    if verbose:
        print(eq.schemeStr)
        # print(eq.latexStr)



def test_findPatternInPatternAndThenGeneratePatternSkipNodesMODE1(verbose=False):
    manipulateClassEQ = Recommend.getManipulateClass('pythagoreanangle')#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    directionEQ = 'hin'
    idxEQ = 0
    mEQ = manipulateClassEQ(directionEQ, idxEQ)#can manipulationClass not have schemeWord??<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    print('schemeword:', mEQ.inputGrammar)
    eq = Equation(mEQ.inputGrammar, 'scheme') # this is also a manipulation, but we only want the string
    manipulateClass = Recommend.getManipulateClass('exponential')#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #manipulateClass.NO_OF_MANIPULATIONS [lower bound of idx], direction={vor, hin}
    idx = 1
    direction = 'hin'
    manipulate = manipulateClass(direction, idx, calculateSchemeNodeChanges=True, verbose=verbose)
    returnTup = manipulate.apply(eq, startPos__nodeId=eq.startPos__nodeId)#, startPos__nodeId=hint['startPos__nodeId'], toAst=True)
    eq, _, _, _, _ = returnTup
    if verbose:
        print(eq.schemeStr if eq is not None else None)
        # print(eq.latexStr)





if __name__=='__main__':
    # test_findPatternInPatternAndThenGeneratePatternAddition(True)
    # test_findPatternInPatternAndThenGeneratePatternMultiplication(True)
    # test_findPatternInPatternAndThenGeneratePatternSkipNodes(True)
    
    # test_findPatternInPatternAndThenGeneratePatternSkipNodesMODE0(True)
    test_findPatternInPatternAndThenGeneratePatternSkipNodesMODE1(True)