import inspect
import pprint

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


def test__basic__moveAdditionAndEquate(verbose=False):
    eqs0 = 'a=b+c'
    eqs1 = 'd=b+e'
    eq0 = Equation(eqs0, 'latex', verbose=verbose)
    eq1 = Equation(eqs1, 'latex', verbose=verbose)
    variableToEliminate = 'b'
    ast, functions, variables, primitives, totalNodeCount = eq0.linearEliminationBySubstitution(eq1, variableToEliminate)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=ast)._unparse()
    expectedLatexStr = 'a-c=d-e' # to be filled in 
    expectedFunctions = {'-': 2} # count
    expectedVariables = {'a': 1, 'c': 1, 'd': 1, 'e': 1} # count
    expectedPrimitives = 0 # count
    expectedTotalNodeCount = 7 # count
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functions and 
        expectedVariables == eq0.variables and 
        expectedPrimitives == eq0.primitives and 
        expectedTotalNodeCount == eq0.totalNodeCount)
    if verbose:
        print('Results~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('OG: ', eqs0, ' ', eqs1)
        print('variable to Eliminate: ', variableToEliminate)
        print('TF: ', latexStr)
        print('Counts~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('results functions')
        pp.pprint(eq0.functions)
        print('results variables')
        pp.pprint(eq0.variables)
        print('results primitives')
        pp.pprint(eq0.primitives)
        print('results totalNodeCount')
        pp.pprint(eq0.totalNodeCount)



def test__hatsukoi__step0(verbose=False):
    eqs0 = 'V_{Z1}=I_{Z1} R_{Z1}'
    eqs1 = 'V_{in}=R I_R + V_{Z1}'
    eq0 = Equation(eqs0, 'latex', verbose=verbose)
    eq1 = Equation(eqs1, 'latex', verbose=verbose)
    variableToEliminate = 'V_{Z1}'
    ast, functions, variables, primitives, totalNodeCount = eq0.linearEliminationBySubstitution(eq1, variableToEliminate)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=ast)._unparse()
    expectedLatexStr = None # to be filled in 
    expectedFunctions = None # count
    expectedVariables = None # count
    expectedPrimitives = None # count
    expectedTotalNodeCount = None # count
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functions and 
        expectedVariables == eq0.variables and 
        expectedPrimitives == eq0.primitives and 
        expectedTotalNodeCount == eq0.totalNodeCount)
    if verbose:
        print('Results~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('OG: ', eqs0, ' ', eqs1)
        print('variable to Eliminate: ', variableToEliminate)
        print('TF: ', latexStr)
        print('Counts~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('results functions')
        pp.pprint(eq0.functions)
        print('results variables')
        pp.pprint(eq0.variables)
        print('results primitives')
        pp.pprint(eq0.primitives)
        print('results totalNodeCount')
        pp.pprint(eq0.totalNodeCount)



def test__hatsukoi__step1(verbose=False):
    eqs0 = 'I_{Z1} R_{Z1}=V_{in}-R I_{R}'
    eqs1 = 'I_{RC} R_{C} - V_{BEQ1} - I_{R} R = 0'
    eq0 = Equation(eqs0, 'latex', verbose=verbose)
    eq1 = Equation(eqs1, 'latex', verbose=verbose)
    variableToEliminate = 'I_{R}'
    ast, functions, variables, primitives, totalNodeCount = eq0.linearEliminationBySubstitution(eq1, variableToEliminate)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=ast)._unparse()
    expectedLatexStr = None # to be filled in 
    expectedFunctions = None # count
    expectedVariables = None # count
    expectedPrimitives = None # count
    expectedTotalNodeCount = None # count
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functions and 
        expectedVariables == eq0.variables and 
        expectedPrimitives == eq0.primitives and 
        expectedTotalNodeCount == eq0.totalNodeCount)
    if verbose:
        print('Results~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('OG: ', eqs0, ' ', eqs1)
        print('variable to Eliminate: ', variableToEliminate)
        print('TF: ', latexStr)
        print('Counts~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('results functions')
        pp.pprint(eq0.functions)
        print('results variables')
        pp.pprint(eq0.variables)
        print('results primitives')
        pp.pprint(eq0.primitives)
        print('results totalNodeCount')
        pp.pprint(eq0.totalNodeCount)



def test__hatsukoi__step2(verbose=False):
    eqs0 = '\\frac{V_{in}-I_{Z1} R_{Z1}}{R} = \\frac{I_{RC} R_{C} - V_{BE}}{R}'
    eqs1 = 'I_{RC} + I_{B} = I_{E}'
    eq0 = Equation(eqs0, 'latex', verbose=verbose)
    eq1 = Equation(eqs1, 'latex', verbose=verbose)
    variableToEliminate = 'I_{RC}'
    ast, functions, variables, primitives, totalNodeCount = eq0.linearEliminationBySubstitution(eq1, variableToEliminate)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=ast)._unparse()
    expectedLatexStr = None # to be filled in 
    expectedFunctions = None # count
    expectedVariables = None # count
    expectedPrimitives = None # count
    expectedTotalNodeCount = None # count
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functions and 
        expectedVariables == eq0.variables and 
        expectedPrimitives == eq0.primitives and 
        expectedTotalNodeCount == eq0.totalNodeCount)
    if verbose:
        print('Results~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('OG: ', eqs0, ' ', eqs1)
        print('variable to Eliminate: ', variableToEliminate)
        print('TF: ', latexStr)
        print('Counts~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('results functions')
        pp.pprint(eq0.functions)
        print('results variables')
        pp.pprint(eq0.variables)
        print('results primitives')
        pp.pprint(eq0.primitives)
        print('results totalNodeCount')
        pp.pprint(eq0.totalNodeCount)



if __name__=='__main__':
    test__basic__moveAdditionAndEquate()
    # test__hatsukoi__step0(True) # latex parser error, self.variables {'}': 1, 'V_{Z1': 1, 'R_{Z1': 1, 'I_{Z1': 1}
    # test__hatsukoi__step1(True) # latex parser error, self.variables {'V_': 1, 'R_{Z1': 1, '}': 1, 'I_{R}': 1, 'R': 1, 'I_{Z1': 1, 'in': 1}
    # test__hatsukoi__step2(True) # latex parser error, self.variables {'I_{Z1': 1, 'R_{Z1': 1, 'V_{BE}': 1, 'R': 1, '}': 1, 'V_': 1, 'I_{RC}': 1, 'R_{C}': 1, 'in': 1}