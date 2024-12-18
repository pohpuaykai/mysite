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
    eqs0 = 'V_{Z_{1}}=I_{Z_{1}} R_{Z_{1}}'
    eqs1 = 'V_{in}=R I_R + V_{Z_{1}}'
    eq0 = Equation(eqs0, 'latex', verbose=verbose)
    eq1 = Equation(eqs1, 'latex', verbose=verbose)
    variableToEliminate = 'V_{Z_{1}}'
    ast, functions, variables, primitives, totalNodeCount = eq0.linearEliminationBySubstitution(eq1, variableToEliminate)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=ast)._unparse()
    expectedLatexStr = 'V_{in} -RI_R=I_{Z_{1}}R_{Z_{1}}' # to be filled in 
    expectedFunctions = {'*': 2, '-': 1} # count
    expectedVariables = {'I_R': 1, 'I_{Z_{1}}': 1, 'R': 1, 'R_{Z_{1}}': 1, 'V_{in}': 1} # count
    expectedPrimitives = 0 # count
    expectedTotalNodeCount = 9 # count
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



def test__hatsukoi__step1(verbose=False): # TODO SAME_DIVISOR=> simplication_in_AST
    eqs0 = 'I_{Z_{1}} R_{Z_{1}}=V_{in}-R I_{R}'
    eqs1 = 'I_{R_{C}} R_{C} - V^{Q1}_{BE} - I_{R} R = 0'
    eq0 = Equation(eqs0, 'latex', verbose=verbose)
    eq1 = Equation(eqs1, 'latex', verbose=verbose)
    variableToEliminate = 'I_{R}'
    ast, functions, variables, primitives, totalNodeCount = eq0.linearEliminationBySubstitution(eq1, variableToEliminate)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=ast)._unparse()
    expectedLatexStr = '\\frac{V_{in} -I_{Z_{1}}R_{Z_{1}}}{R}=\\frac{(I_{R_{C}} R_{C}-V^{Q1}_{BE})-(0)}{R}' # to be filled in 
    expectedFunctions = {'*': 2, '-': 3, '/': 2} # count
    expectedVariables = {   
    'I_{R_{C}}': 1,
    'I_{Z_{1}}': 1,
    'R': 2,
    'R_{C}': 1,
    'R_{Z_{1}}': 1,
    'V^{Q1}_{BE}': 1,
    'V_{in}': 1} # count
    expectedPrimitives = 1 # count
    expectedTotalNodeCount = 17 # count
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



def test__hatsukoi__step2(verbose=False): # TODO MUlTIPLY_DIVIDE_CANCEL_OUT => simplication_in_AST
    eqs0 = '\\frac{V_{in}-I_{Z1} R_{Z1}}{R} = \\frac{I_{RC} R_{C} - V_{BE}}{R}'
    eqs1 = 'I_{RC} + I_{B} = I_{E}'
    eq0 = Equation(eqs0, 'latex', verbose=verbose)
    eq1 = Equation(eqs1, 'latex', verbose=verbose)
    variableToEliminate = 'I_{RC}'
    ast, functions, variables, primitives, totalNodeCount = eq0.linearEliminationBySubstitution(eq1, variableToEliminate)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=ast)._unparse()
    expectedLatexStr = '\\frac{\\frac{V_{in} -I_{Z1}R_{Z1}}{R}R+V_{BE}}{R_{C}}=I_{E} -I_{B}' # to be filled in 
    expectedFunctions = {'*': 2, '+': 1, '-': 2, '/': 2} # count
    expectedVariables = {   'I_{B}': 1,
    'I_{E}': 1,
    'I_{Z1}': 1,
    'R': 2,
    'R_{C}': 1,
    'R_{Z1}': 1,
    'V_{BE}': 1,
    'V_{in}': 1} # count
    expectedPrimitives = 0 # count
    expectedTotalNodeCount = 17 # count
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
    test__hatsukoi__step0()
    test__hatsukoi__step1() # TODO SAME_DIVISOR=> simplication_in_AST
    test__hatsukoi__step2() # TODO MUlTIPLY_DIVIDE_CANCEL_OUT => simplication_in_AST