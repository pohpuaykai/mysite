import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser


def test__contiguousLeftOvers__decimalPlaces(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = ' -0.5 + 1.0 = 0.5'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('+', 5): [('-', 3), ('1.0', 6)],
    ('-', 3): [('0', 2), ('0.5', 4)],
    ('=', 0): [('+', 5), ('0.5', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsSimple(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_{BE}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('V_{BE}', 1), ('V', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsWithNums(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_{Z1}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('V_{Z1}', 1), ('V', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__weirdVariables__variablesWithCurlyBracketsWithInCurlyBrackets(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_{Z_{1}}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('V_{Z_{1}}', 1), ('V', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsWithInCurlyBracketsMoreComplex(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_{in}=R I_R + V_{Z_{1}}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 3): [('R', 2), ('I_R', 4)],
    ('+', 5): [('*', 3), ('V_{Z_{1}}', 6)],
    ('=', 0): [('V_{in}', 1), ('+', 5)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)




def test__weirdVariables__variablesWithCaret(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)
    #if we have underscore, then caret, then es ist exponential
    equationStr = 'V=V^{Q_{1}}_{BE}' #TODO if caret follows an underscore, then its not exponential, sondern, der ganz Ding ist ein VARIABLE
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('V', 2), ('V^{Q_{1}}_{BE}', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCaretRealExponent(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)
    #if we have underscore, then caret, then es ist exponential
    equationStr = 'V^x=V^{Q_{1}}_{BE}^x' #TODO if caret follows an underscore, then its not exponential, sondern, der ganz Ding ist ein VARIABLE
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('=', 0): [('^', 5), ('^', 2)],
    ('^', 2): [('V^{Q_{1}}_{BE}', 1), ('x', 3)],
    ('^', 5): [('V', 4), ('x', 6)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCaretMoreComplex(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)
    #if we have underscore, then caret, then es ist exponential
    equationStr = 'I_{R_{C}} R_{C} - V^{Q_{1}}_{BE} - I_{R} R = 0' #TODO if caret follows an underscore, then its not exponential, sondern, der ganz Ding ist ein VARIABLE
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 3): [('I_{R_{C}}', 2), ('R_{C}', 4)],
    ('*', 9): [('I_{R}', 8), ('R', 10)],
    ('-', 5): [('*', 3), ('V^{Q_{1}}_{BE}', 6)],
    ('-', 7): [('-', 5), ('*', 9)],
    ('=', 0): [('-', 7), ('0', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsMinus(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_B-V_{BE}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('-', 2): [('V_B', 1), ('V_{BE}', 3)], ('=', 0): [('-', 2), ('V', 4)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{V_B-V_{BE}}{R_B}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('-', 4): [('V_B', 3), ('V_{BE}', 5)],
    ('/', 2): [('-', 4), ('R_B', 6)],
    ('=', 0): [('/', 2), ('V', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsImplicitMultiply0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'P=V_{rms}I_{rms}\\cos(\\phi)'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 2): [('V_{rms}', 1), ('I_{rms}', 3)],
    ('*', 4): [('*', 2), ('cos', 5)],
    ('=', 0): [('P', 6), ('*', 4)],
    ('cos', 5): [('phi', 7)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsImplicitMultiply1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'a_{bc}d_{ef}g_{hi}j_{k}\\cos(\\phi)=O'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 2): [('a_{bc}', 1), ('d_{ef}', 3)],
    ('*', 4): [('*', 2), ('g_{hi}', 5)],
    ('*', 6): [('*', 4), ('j_{k}', 7)],
    ('*', 8): [('*', 6), ('cos', 9)],
    ('=', 0): [('*', 8), ('O', 10)],
    ('cos', 9): [('phi', 11)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__makeSubject__manyVariablesStandingTogether(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'A_v = ( R_L + \\frac{R_2}{1 + s C R_2} )'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 8): [('s', 7), ('C', 9)],
    ('*', 10): [('*', 8), ('R_2', 11)],
    ('+', 3): [('R_L', 2), ('/', 4)],
    ('+', 6): [('1', 5), ('*', 10)],
    ('/', 4): [('R_2', 12), ('+', 6)],
    ('=', 0): [('A_v', 1), ('+', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__collateBackslashInfixLeftOversToContiguous__exponentialOverMultiply(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = ' 3x^{9} = 3x^{2}x^{7}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 2): [('3', 1), ('^', 4)],
    ('*', 6): [('*', 2), ('^', 8)],
    ('*', 11): [('3', 10), ('^', 13)],
    ('=', 0): [('*', 11), ('*', 6)],
    ('^', 4): [('x', 3), ('2', 5)],
    ('^', 8): [('x', 7), ('7', 9)],
    ('^', 13): [('x', 12), ('9', 14)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__interLevelSubTreeGrafting__exponentialOverEnclosingBrackets(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(19y + z^4 + 4w^{12})^{30} = F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 3): [('19', 2), ('y', 4)],
    ('*', 11): [('4', 10), ('^', 13)],
    ('+', 5): [('*', 3), ('^', 7)],
    ('+', 9): [('+', 5), ('*', 11)],
    ('=', 0): [('^', 15), ('F', 1)],
    ('^', 7): [('z', 6), ('4', 8)],
    ('^', 13): [('w', 12), ('12', 14)],
    ('^', 15): [('+', 9), ('30', 16)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__interLevelSubTreeGrafting__exponentialOverEnclosingBracketsNegativePower(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1)^{-1} = 1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('-', 4): [('0', 3), ('1', 5)],
    ('=', 0): [('^', 2), ('1', 6)],
    ('^', 2): [('1', 1), ('-', 4)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__interLevelSubTreeGrafting__exponentialOverEnclosingBracketsNegativePower0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1)^{\\sin(x)-1} = 1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('-', 5): [('sin', 4), ('1', 6)],
    ('=', 0): [('^', 3), ('1', 1)],
    ('^', 3): [('1', 2), ('-', 5)],
    ('sin', 4): [('x', 7)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Trig0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '-\\sin( 2x_0 ) = -2\\sin(x_0)\\cos(x_0)'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 4): [('2', 3), ('sin', 5)],
    ('*', 6): [('*', 4), ('cos', 7)],
    ('*', 14): [('2', 13), ('x_0', 15)],
    ('-', 2): [('0', 1), ('*', 6)],
    ('-', 9): [('0', 8), ('sin', 10)],
    ('=', 0): [('-', 9), ('-', 2)],
    ('cos', 7): [('x_0', 12)],
    ('sin', 5): [('x_0', 11)],
    ('sin', 10): [('*', 14)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast) # rename ast to latex_ast 


def test__findingBackSlashAndInfixOperations__Trig1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sin^2(x) + \\cos^2(x)=1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('+', 3): [('^', 10), ('^', 9)],
    ('=', 0): [('+', 3), ('1', 1)],
    ('^', 9): [('cos', 4), ('2', 7)],
    ('^', 10): [('sin', 2), ('2', 6)],
    ('cos', 4): [('x', 8)],
    ('sin', 2): [('x', 5)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Trig2(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sin^{2}(x)+\\cos^{2}(x)=1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('+', 3): [('^', 10), ('^', 9)],
    ('=', 0): [('+', 3), ('1', 1)],
    ('^', 9): [('cos', 4), ('2', 5)],
    ('^', 10): [('sin', 2), ('2', 7)],
    ('cos', 4): [('x', 6)],
    ('sin', 2): [('x', 8)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Sqrt0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sqrt{4}=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('nroot', 1), ('2', 2)], ('nroot', 1): [(2, 4), ('4', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Sqrt1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sqrt[3]{9}=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('nroot', 2), ('2', 1)], ('nroot', 2): [('3', 3), ('9', 4)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Ln(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\ln(e)=1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('log', 2), ('1', 1)], ('log', 2): [('e', 4), ('e', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Frac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{12}{24}=\\frac{1000}{2000}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('/', 1): [('1000', 4), ('2000', 3)],
    ('/', 2): [('12', 6), ('24', 5)],
    ('=', 0): [('/', 2), ('/', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Log0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log_{12}(8916100448256)=12'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('=', 0): [('log', 2), ('12', 1)],
    ('log', 2): [('12', 4), ('8916100448256', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Log1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log(100)=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('log', 1), ('2', 2)], ('log', 1): [(10, 4), ('100', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__tildeVariable(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\tilde{x}=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('tilde', 1), ('2', 2)], ('tilde', 1): [('x', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__SchrodingerWaveEquation(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\widehat{H}\\Psi=\\widehat{E}\\Psi'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 2): [('widehat', 1), ('Psi', 3)],
    ('*', 5): [('widehat', 4), ('Psi', 6)],
    ('=', 0): [('*', 5), ('*', 2)],
    ('widehat', 1): [('E', 7)],
    ('widehat', 4): [('H', 8)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__infixInBackslash__paraboloid(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'z=\\sqrt{x^2+y^2}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('+', 6): [('^', 4), ('^', 8)],
    ('=', 0): [('z', 2), ('nroot', 1)],
    ('^', 4): [('x', 3), ('2', 5)],
    ('^', 8): [('y', 7), ('2', 9)],
    ('nroot', 1): [(2, 10), ('+', 6)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__sqrtWithPowerCaretRightOtherInfix__hill(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'z=-\\sqrt[2]{x^2+y^2}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('+', 8): [('^', 6), ('^', 10)],
    ('-', 2): [('0', 1), ('nroot', 3)],
    ('=', 0): [('z', 4), ('-', 2)],
    ('^', 6): [('x', 5), ('2', 7)],
    ('^', 10): [('y', 9), ('2', 11)],
    ('nroot', 3): [('2', 12), ('+', 8)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__nonInfixBrackets__addImplicitMultiply(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1+(1+(1+1)))(((1+1)+1)+1)=16'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 9): [('+', 3), ('+', 15)],
    ('+', 3): [('1', 2), ('+', 5)],
    ('+', 5): [('1', 4), ('+', 7)],
    ('+', 7): [('1', 6), ('1', 8)],
    ('+', 11): [('1', 10), ('1', 12)],
    ('+', 13): [('+', 11), ('1', 14)],
    ('+', 15): [('+', 13), ('1', 16)],
    ('=', 0): [('*', 9), ('16', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__nonInfixBrackets__addImplicitMultiply0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1+(1+1)(1+1)+1)+1=7'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 6): [('+', 4), ('+', 8)],
    ('+', 2): [('1', 1), ('*', 6)],
    ('+', 4): [('1', 3), ('1', 5)],
    ('+', 8): [('1', 7), ('1', 9)],
    ('+', 10): [('+', 2), ('1', 11)],
    ('+', 12): [('+', 10), ('1', 13)],
    ('=', 0): [('+', 12), ('7', 14)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__nonInfixBrackets__addImplicitMultiply1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((1+(1+(1+1)))(((1+1)+1)+1)+1)+1=18'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 9): [('+', 3), ('+', 15)],
    ('+', 3): [('1', 2), ('+', 5)],
    ('+', 5): [('1', 4), ('+', 7)],
    ('+', 7): [('1', 6), ('1', 8)],
    ('+', 11): [('1', 10), ('1', 12)],
    ('+', 13): [('+', 11), ('1', 14)],
    ('+', 15): [('+', 13), ('1', 16)],
    ('+', 17): [('*', 9), ('1', 18)],
    ('+', 19): [('+', 17), ('1', 20)],
    ('=', 0): [('+', 19), ('18', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__priorityBetweenInfixForBrackets(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{2}{(x-1)(x+1)}=c'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 6): [('-', 4), ('+', 8)],
    ('+', 8): [('x', 7), ('1', 9)],
    ('-', 4): [('x', 3), ('1', 5)],
    ('/', 2): [('2', 10), ('*', 6)],
    ('=', 0): [('/', 2), ('c', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracketInBackslashArg(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{2}{(x-1)(x+1)} = \\frac{1}{x-1} - \\frac{1}{x+1}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 8): [('-', 6), ('+', 10)],
    ('+', 10): [('x', 9), ('1', 11)],
    ('+', 19): [('x', 18), ('1', 20)],
    ('-', 3): [('/', 2), ('/', 4)],
    ('-', 6): [('x', 5), ('1', 7)],
    ('-', 15): [('x', 14), ('1', 16)],
    ('/', 1): [('2', 12), ('*', 8)],
    ('/', 2): [('1', 13), ('-', 15)],
    ('/', 4): [('1', 17), ('+', 19)],
    ('=', 0): [('/', 1), ('-', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracketInBackslashArgWithExponent(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'c=\\sin((x-3)^2)'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('-', 4): [('x', 3), ('3', 5)],
    ('=', 0): [('c', 2), ('sin', 1)],
    ('^', 6): [('-', 4), ('2', 7)],
    ('sin', 1): [('^', 6)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracketInBackslashArgImplicitZero(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{2}{(x-1)(x+1)} = \\frac{1}{x-1} + \\frac{-1}{x+1}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 8): [('-', 6), ('+', 10)],
    ('+', 3): [('/', 2), ('/', 4)],
    ('+', 10): [('x', 9), ('1', 11)],
    ('+', 21): [('x', 20), ('1', 22)],
    ('-', 6): [('x', 5), ('1', 7)],
    ('-', 15): [('0', 14), ('1', 16)],
    ('-', 18): [('x', 17), ('1', 19)],
    ('/', 1): [('2', 12), ('*', 8)],
    ('/', 2): [('1', 13), ('-', 18)],
    ('/', 4): [('-', 15), ('+', 21)],
    ('=', 0): [('/', 1), ('+', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracket(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'x^2-6x+9=(x-3)^2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 6): [('6', 5), ('x', 7)],
    ('+', 8): [('-', 4), ('9', 9)],
    ('-', 4): [('^', 2), ('*', 6)],
    ('-', 11): [('x', 10), ('3', 12)],
    ('=', 0): [('+', 8), ('^', 13)],
    ('^', 2): [('x', 1), ('2', 3)],
    ('^', 13): [('-', 11), ('2', 14)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__manyFracCaretEnclosingBrac__partialFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{x^2}{(x-2)(x-3)^2}=\\frac{4}{x-2}+\\frac{-3}{x-3}+\\frac{9}{(x-3)^2}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 13): [('-', 11), ('^', 17)],
    ('+', 3): [('/', 2), ('/', 4)],
    ('+', 5): [('+', 3), ('/', 6)],
    ('-', 11): [('x', 10), ('2', 12)],
    ('-', 15): [('x', 14), ('3', 16)],
    ('-', 21): [('x', 20), ('2', 22)],
    ('-', 24): [('x', 23), ('3', 25)],
    ('-', 29): [('0', 28), ('3', 30)],
    ('-', 33): [('x', 32), ('3', 34)],
    ('/', 1): [('^', 8), ('*', 13)],
    ('/', 2): [('4', 19), ('-', 21)],
    ('/', 4): [('-', 29), ('-', 33)],
    ('/', 6): [('9', 31), ('^', 26)],
    ('=', 0): [('/', 1), ('+', 5)],
    ('^', 8): [('x', 7), ('2', 9)],
    ('^', 17): [('-', 15), ('2', 18)],
    ('^', 26): [('-', 24), ('2', 27)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__fracWithLogNoBase__changeLogBaseFormula(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log_{b}(a)=\\frac{\\log_{c}(a)}{\\log_{c}(b)}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('/', 1): [('log', 4), ('log', 3)],
    ('=', 0): [('log', 2), ('/', 1)],
    ('log', 2): [('b', 5), ('a', 6)],
    ('log', 3): [('c', 8), ('b', 7)],
    ('log', 4): [('c', 10), ('a', 9)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__sqrtInSqrt(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sqrt[\\sqrt{\\frac{\\pi}{22}}]{\\sqrt[\\sin(\\pi)]{\\pi}}=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('/', 5): [('pi', 9), ('22', 8)],
    ('=', 0): [('nroot', 2), ('F', 1)],
    ('nroot', 2): [('nroot', 3), ('nroot', 4)],
    ('nroot', 3): [(2, 11), ('/', 5)],
    ('nroot', 4): [('sin', 7), ('pi', 6)],
    ('sin', 7): [('pi', 10)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__trigInTrig(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sin^{20-\\cos^{43}(1-\\frac{\\pi}{5})}(9-\\tan^4(\\theta))+5=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('+', 3): [('^', 19), ('5', 4)],
    ('-', 6): [('9', 5), ('^', 20)],
    ('-', 9): [('20', 8), ('^', 21)],
    ('-', 14): [('1', 13), ('/', 15)],
    ('/', 15): [('pi', 18), ('5', 17)],
    ('=', 0): [('+', 3), ('F', 1)],
    ('^', 19): [('sin', 2), ('-', 9)],
    ('^', 20): [('tan', 7), ('4', 12)],
    ('^', 21): [('cos', 10), ('43', 16)],
    ('cos', 10): [('-', 14)],
    ('sin', 2): [('-', 6)],
    ('tan', 7): [('theta', 11)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__logInLog(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log_{\\ln(90-x)}(\\log(z^5))=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('-', 9): [('90', 8), ('x', 10)],
    ('=', 0): [('log', 2), ('F', 1)],
    ('^', 6): [('z', 5), ('5', 7)],
    ('log', 2): [('log', 4), ('log', 3)],
    ('log', 3): [(10, 11), ('^', 6)],
    ('log', 4): [('e', 12), ('-', 9)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__fracInFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{\\frac{\\sin^2(x)+\\cos^2(x)}{\\sin^2(x)-\\cos^2(x)}}{\\frac{\\cos(2x)-\\sin(2x)}{\\cos(2x)+\\sin(2x)}}=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 18): [('2', 17), ('x', 19)],
    ('*', 21): [('2', 20), ('x', 22)],
    ('*', 24): [('2', 23), ('x', 25)],
    ('*', 27): [('2', 26), ('x', 28)],
    ('+', 6): [('cos', 5), ('sin', 7)],
    ('+', 12): [('^', 40), ('^', 39)],
    ('-', 9): [('cos', 8), ('sin', 10)],
    ('-', 15): [('^', 38), ('^', 37)],
    ('/', 2): [('/', 4), ('/', 3)],
    ('/', 3): [('-', 9), ('+', 6)],
    ('/', 4): [('+', 12), ('-', 15)],
    ('=', 0): [('/', 2), ('F', 1)],
    ('^', 37): [('cos', 16), ('2', 36)],
    ('^', 38): [('sin', 14), ('2', 34)],
    ('^', 39): [('cos', 13), ('2', 30)],
    ('^', 40): [('sin', 11), ('2', 31)],
    ('cos', 5): [('*', 21)],
    ('cos', 8): [('*', 27)],
    ('cos', 13): [('x', 29)],
    ('cos', 16): [('x', 35)],
    ('sin', 7): [('*', 18)],
    ('sin', 10): [('*', 24)],
    ('sin', 11): [('x', 32)],
    ('sin', 14): [('x', 33)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__highPowersAndRandomCoefficientsPITEST(verbose=False): # TODO not entirely correct... should treat P(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'P = 7x^{13} - 3x^{9} + 5x^{8} - \\sqrt{2}x^{4} + \\pi x^{2} - 42' # 'P(x) = 7x^{13} - 3x^{9} + 5x^{8} - \\sqrt{2}x^{4} + \\pi x^{2} - 42', but we cannot handle P(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 2): [('7', 1), ('^', 4)],
    ('*', 8): [('3', 7), ('^', 10)],
    ('*', 14): [('5', 13), ('^', 16)],
    ('*', 20): [('nroot', 19), ('^', 22)],
    ('*', 26): [('pi', 25), ('^', 28)],
    ('+', 12): [('-', 6), ('-', 18)],
    ('+', 24): [('+', 12), ('-', 30)],
    ('-', 6): [('*', 2), ('*', 8)],
    ('-', 18): [('*', 14), ('*', 20)],
    ('-', 30): [('*', 26), ('42', 31)],
    ('=', 0): [('P', 32), ('+', 24)],
    ('^', 4): [('x', 3), ('13', 5)],
    ('^', 10): [('x', 9), ('9', 11)],
    ('^', 16): [('x', 15), ('8', 17)],
    ('^', 22): [('x', 21), ('4', 23)],
    ('^', 28): [('x', 27), ('2', 29)],
    ('nroot', 19): [(2, 34), ('2', 33)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__nestedPolynomial(verbose=False): # TODO not entirely correct... should treat Q(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'Q = (x^3 - 2x^2 + 5x - 7)^2 - (x - 1)^3 + 3x^{21}' # 'Q(x) = (x^3 - 2x^2 + 5x - 7)^2 - (x - 1)^3 + 3x^{21}', but we cannot handle Q(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 6): [('2', 5), ('^', 8)],
    ('*', 12): [('5', 11), ('x', 13)],
    ('*', 26): [('3', 25), ('^', 28)],
    ('+', 10): [('-', 4), ('-', 14)],
    ('+', 24): [('^', 22), ('*', 26)],
    ('-', 4): [('^', 2), ('*', 6)],
    ('-', 14): [('*', 12), ('7', 15)],
    ('-', 18): [('^', 16), ('+', 24)],
    ('-', 20): [('x', 19), ('1', 21)],
    ('=', 0): [('Q', 30), ('-', 18)],
    ('^', 2): [('x', 1), ('3', 3)],
    ('^', 8): [('x', 7), ('2', 9)],
    ('^', 16): [('+', 10), ('2', 17)],
    ('^', 22): [('-', 20), ('3', 23)],
    ('^', 28): [('x', 27), ('21', 29)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__nonIntegerAndNegativeCoefficientsDECIMALPOINTTEST(verbose=False): # TODO not entirely correct... should treat R(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'R = -0.5x^{10} + 3.14x^{8} - \\frac{2}{3}x^{5} + 1.618x^{3} - \\frac{1}{x}' # 'R(x) = -0.5x^{10} + 3.14x^{8} - \\frac{2}{3}x^{5} + 1.618x^{3} - \\frac{1}{x}', but we cannot handle R(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 4): [('0.5', 3), ('^', 6)],
    ('*', 10): [('3.14', 9), ('^', 12)],
    ('*', 16): [('/', 15), ('^', 18)],
    ('*', 22): [('1.618', 21), ('^', 24)],
    ('+', 8): [('-', 2), ('-', 14)],
    ('+', 20): [('+', 8), ('-', 26)],
    ('-', 2): [('0', 1), ('*', 4)],
    ('-', 14): [('*', 10), ('*', 16)],
    ('-', 26): [('*', 22), ('/', 27)],
    ('/', 15): [('2', 32), ('3', 29)],
    ('/', 27): [('1', 30), ('x', 31)],
    ('=', 0): [('R', 28), ('+', 20)],
    ('^', 6): [('x', 5), ('10', 7)],
    ('^', 12): [('x', 11), ('8', 13)],
    ('^', 18): [('x', 17), ('5', 19)],
    ('^', 24): [('x', 23), ('3', 25)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__mixedVariablesAndPowersPOWERCOTEVARIABLEDOUBLEVARIABLETEST(verbose=False): # TODO not entirely correct... should treat S(x, y) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'S = x^5y^4 - 7x^3y^2 + 2x^2 - y^3 + x^2y - 4' # 'S(x, y) = x^5y^4 - 7x^3y^2 + 2x^2 - y^3 + x^2y - 4', but we cannot handle S(x, y) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 4): [('^', 2), ('^', 6)],
    ('*', 10): [('7', 9), ('^', 12)],
    ('*', 14): [('*', 10), ('^', 16)],
    ('*', 20): [('2', 19), ('^', 22)],
    ('*', 32): [('^', 30), ('y', 33)],
    ('+', 18): [('-', 8), ('-', 24)],
    ('+', 28): [('+', 18), ('-', 34)],
    ('-', 8): [('*', 4), ('*', 14)],
    ('-', 24): [('*', 20), ('^', 26)],
    ('-', 34): [('*', 32), ('4', 35)],
    ('=', 0): [('S', 36), ('+', 28)],
    ('^', 2): [('x', 1), ('5', 3)],
    ('^', 6): [('y', 5), ('4', 7)],
    ('^', 12): [('x', 11), ('3', 13)],
    ('^', 16): [('y', 15), ('2', 17)],
    ('^', 22): [('x', 21), ('2', 23)],
    ('^', 26): [('y', 25), ('3', 27)],
    ('^', 30): [('x', 29), ('2', 31)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__irrationalAndTranscendentalNumbersPOWERCOTEBACKSLASH(verbose=False): # TODO not entirely correct... should treat T(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'T = e^{x} - \\cos(x)x^4 + x^3\\sin(x) - \\ln(x^2+1)' # 'T(x) = e^{x} - \\cos(x)x^4 + x^3\\sin(x) - \\ln(x^2+1)', but we cannot handle T(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 6): [('cos', 5), ('^', 8)],
    ('*', 14): [('^', 12), ('sin', 15)],
    ('+', 10): [('-', 4), ('-', 16)],
    ('+', 22): [('^', 20), ('1', 23)],
    ('-', 4): [('^', 2), ('*', 6)],
    ('-', 16): [('*', 14), ('log', 17)],
    ('=', 0): [('T', 18), ('+', 10)],
    ('^', 2): [('e', 1), ('x', 3)],
    ('^', 8): [('x', 7), ('4', 9)],
    ('^', 12): [('x', 11), ('3', 13)],
    ('^', 20): [('x', 19), ('2', 21)],
    ('cos', 5): [('x', 24)],
    ('log', 17): [('e', 26), ('+', 22)],
    ('sin', 15): [('x', 25)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__degree5(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(x - 1)(x + 2)(x - 3)(x + 4)(x - 5) = x^5 - 3x^4 - 32x^3 + 94x^2 + 31x - 120'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 6): [('3', 5), ('^', 8)],
    ('*', 12): [('32', 11), ('^', 14)],
    ('*', 18): [('94', 17), ('^', 20)],
    ('*', 24): [('31', 23), ('x', 25)],
    ('*', 31): [('-', 29), ('+', 33)],
    ('*', 35): [('*', 31), ('-', 37)],
    ('*', 39): [('*', 35), ('+', 41)],
    ('*', 43): [('*', 39), ('-', 45)],
    ('+', 16): [('-', 10), ('*', 18)],
    ('+', 22): [('+', 16), ('-', 26)],
    ('+', 33): [('x', 32), ('2', 34)],
    ('+', 41): [('x', 40), ('4', 42)],
    ('-', 4): [('^', 2), ('*', 6)],
    ('-', 10): [('-', 4), ('*', 12)],
    ('-', 26): [('*', 24), ('120', 27)],
    ('-', 29): [('x', 28), ('1', 30)],
    ('-', 37): [('x', 36), ('3', 38)],
    ('-', 45): [('x', 44), ('5', 46)],
    ('=', 0): [('*', 43), ('+', 22)],
    ('^', 2): [('x', 1), ('5', 3)],
    ('^', 8): [('x', 7), ('4', 9)],
    ('^', 14): [('x', 13), ('3', 15)],
    ('^', 20): [('x', 19), ('2', 21)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__degree6(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(x - 1)(x - 2)(x + 3)(x + 4)(x - 5)(x + 6) = x^6 + 5x^5 - 35x^4 - 75x^3 + 368x^2 + 246x - 720'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 6): [('5', 5), ('^', 8)],
    ('*', 12): [('35', 11), ('^', 14)],
    ('*', 18): [('75', 17), ('^', 20)],
    ('*', 24): [('368', 23), ('^', 26)],
    ('*', 30): [('246', 29), ('x', 31)],
    ('*', 37): [('-', 35), ('-', 39)],
    ('*', 41): [('*', 37), ('+', 43)],
    ('*', 45): [('*', 41), ('+', 47)],
    ('*', 49): [('*', 45), ('-', 51)],
    ('*', 53): [('*', 49), ('+', 55)],
    ('+', 4): [('^', 2), ('-', 16)],
    ('+', 22): [('+', 4), ('*', 24)],
    ('+', 28): [('+', 22), ('-', 32)],
    ('+', 43): [('x', 42), ('3', 44)],
    ('+', 47): [('x', 46), ('4', 48)],
    ('+', 55): [('x', 54), ('6', 56)],
    ('-', 10): [('*', 6), ('*', 12)],
    ('-', 16): [('-', 10), ('*', 18)],
    ('-', 32): [('*', 30), ('720', 33)],
    ('-', 35): [('x', 34), ('1', 36)],
    ('-', 39): [('x', 38), ('2', 40)],
    ('-', 51): [('x', 50), ('5', 52)],
    ('=', 0): [('*', 53), ('+', 28)],
    ('^', 2): [('x', 1), ('6', 3)],
    ('^', 8): [('x', 7), ('5', 9)],
    ('^', 14): [('x', 13), ('4', 15)],
    ('^', 20): [('x', 19), ('3', 21)],
    ('^', 26): [('x', 25), ('2', 27)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__degree7(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(x - 1)(x + 2)(x - 3)(x + 4)(x - 5)(x + 6)(x - 7) = x^7 + 4x^6 - 37x^5 - 58x^4 + 520x^3 + 201x^2 - 2156x + 5040'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 6): [('4', 5), ('^', 8)],
    ('*', 12): [('37', 11), ('^', 14)],
    ('*', 18): [('58', 17), ('^', 20)],
    ('*', 24): [('520', 23), ('^', 26)],
    ('*', 30): [('201', 29), ('^', 32)],
    ('*', 36): [('2156', 35), ('x', 37)],
    ('*', 43): [('-', 41), ('+', 45)],
    ('*', 47): [('*', 43), ('-', 49)],
    ('*', 51): [('*', 47), ('+', 53)],
    ('*', 55): [('*', 51), ('-', 57)],
    ('*', 59): [('*', 55), ('+', 61)],
    ('*', 63): [('*', 59), ('-', 65)],
    ('+', 4): [('^', 2), ('-', 16)],
    ('+', 22): [('+', 4), ('*', 24)],
    ('+', 28): [('+', 22), ('-', 34)],
    ('+', 38): [('+', 28), ('5040', 39)],
    ('+', 45): [('x', 44), ('2', 46)],
    ('+', 53): [('x', 52), ('4', 54)],
    ('+', 61): [('x', 60), ('6', 62)],
    ('-', 10): [('*', 6), ('*', 12)],
    ('-', 16): [('-', 10), ('*', 18)],
    ('-', 34): [('*', 30), ('*', 36)],
    ('-', 41): [('x', 40), ('1', 42)],
    ('-', 49): [('x', 48), ('3', 50)],
    ('-', 57): [('x', 56), ('5', 58)],
    ('-', 65): [('x', 64), ('7', 66)],
    ('=', 0): [('*', 63), ('+', 38)],
    ('^', 2): [('x', 1), ('7', 3)],
    ('^', 8): [('x', 7), ('6', 9)],
    ('^', 14): [('x', 13), ('5', 15)],
    ('^', 20): [('x', 19), ('4', 21)],
    ('^', 26): [('x', 25), ('3', 27)],
    ('^', 32): [('x', 31), ('2', 33)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((x + 2x^2 - 3)^2)((x^2 - x + 1)^3)((x^3 + 2x - 5)) = x^{10} + 4x^9 - 2x^8 - 41x^7 - 69x^6 + 142x^5 + 420x^4 - 567x^3 - 174x^2 + 185x - 75'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 6): [('4', 5), ('^', 8)],
    ('*', 12): [('2', 11), ('^', 14)],
    ('*', 18): [('41', 17), ('^', 20)],
    ('*', 24): [('69', 23), ('^', 26)],
    ('*', 30): [('142', 29), ('^', 32)],
    ('*', 36): [('420', 35), ('^', 38)],
    ('*', 42): [('567', 41), ('^', 44)],
    ('*', 48): [('174', 47), ('^', 50)],
    ('*', 54): [('185', 53), ('x', 55)],
    ('*', 61): [('2', 60), ('^', 63)],
    ('*', 69): [('^', 67), ('^', 77)],
    ('*', 79): [('*', 69), ('+', 83)],
    ('*', 85): [('2', 84), ('x', 86)],
    ('+', 4): [('^', 2), ('-', 22)],
    ('+', 28): [('+', 4), ('*', 30)],
    ('+', 34): [('+', 28), ('-', 46)],
    ('+', 52): [('+', 34), ('-', 56)],
    ('+', 59): [('x', 58), ('-', 65)],
    ('+', 75): [('-', 73), ('1', 76)],
    ('+', 83): [('^', 81), ('-', 87)],
    ('-', 10): [('*', 6), ('*', 12)],
    ('-', 16): [('-', 10), ('*', 18)],
    ('-', 22): [('-', 16), ('*', 24)],
    ('-', 40): [('*', 36), ('*', 42)],
    ('-', 46): [('-', 40), ('*', 48)],
    ('-', 56): [('*', 54), ('75', 57)],
    ('-', 65): [('*', 61), ('3', 66)],
    ('-', 73): [('^', 71), ('x', 74)],
    ('-', 87): [('*', 85), ('5', 88)],
    ('=', 0): [('*', 79), ('+', 52)],
    ('^', 2): [('x', 1), ('10', 3)],
    ('^', 8): [('x', 7), ('9', 9)],
    ('^', 14): [('x', 13), ('8', 15)],
    ('^', 20): [('x', 19), ('7', 21)],
    ('^', 26): [('x', 25), ('6', 27)],
    ('^', 32): [('x', 31), ('5', 33)],
    ('^', 38): [('x', 37), ('4', 39)],
    ('^', 44): [('x', 43), ('3', 45)],
    ('^', 50): [('x', 49), ('2', 51)],
    ('^', 63): [('x', 62), ('2', 64)],
    ('^', 67): [('+', 59), ('2', 68)],
    ('^', 71): [('x', 70), ('2', 72)],
    ('^', 77): [('+', 75), ('3', 78)],
    ('^', 81): [('x', 80), ('3', 82)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((x^2 + x - 1)^2)((x^3 - 2x + 4)^2)((x^2 + 3x - 7)) = x^{10} - 3x^9 - 20x^8 + 60x^7 + 161x^6 - 260x^5 - 385x^4 + 494x^3 + 509x^2 - 378x + 196'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 6): [('3', 5), ('^', 8)],
    ('*', 12): [('20', 11), ('^', 14)],
    ('*', 18): [('60', 17), ('^', 20)],
    ('*', 24): [('161', 23), ('^', 26)],
    ('*', 30): [('260', 29), ('^', 32)],
    ('*', 36): [('385', 35), ('^', 38)],
    ('*', 42): [('494', 41), ('^', 44)],
    ('*', 48): [('509', 47), ('^', 50)],
    ('*', 54): [('378', 53), ('x', 55)],
    ('*', 67): [('^', 65), ('^', 77)],
    ('*', 73): [('2', 72), ('x', 74)],
    ('*', 79): [('*', 67), ('+', 83)],
    ('*', 85): [('3', 84), ('x', 86)],
    ('+', 16): [('-', 10), ('*', 18)],
    ('+', 22): [('+', 16), ('-', 34)],
    ('+', 40): [('+', 22), ('*', 42)],
    ('+', 46): [('+', 40), ('-', 52)],
    ('+', 56): [('+', 46), ('196', 57)],
    ('+', 61): [('^', 59), ('-', 63)],
    ('+', 75): [('-', 71), ('4', 76)],
    ('+', 83): [('^', 81), ('-', 87)],
    ('-', 4): [('^', 2), ('*', 6)],
    ('-', 10): [('-', 4), ('*', 12)],
    ('-', 28): [('*', 24), ('*', 30)],
    ('-', 34): [('-', 28), ('*', 36)],
    ('-', 52): [('*', 48), ('*', 54)],
    ('-', 63): [('x', 62), ('1', 64)],
    ('-', 71): [('^', 69), ('*', 73)],
    ('-', 87): [('*', 85), ('7', 88)],
    ('=', 0): [('*', 79), ('+', 56)],
    ('^', 2): [('x', 1), ('10', 3)],
    ('^', 8): [('x', 7), ('9', 9)],
    ('^', 14): [('x', 13), ('8', 15)],
    ('^', 20): [('x', 19), ('7', 21)],
    ('^', 26): [('x', 25), ('6', 27)],
    ('^', 32): [('x', 31), ('5', 33)],
    ('^', 38): [('x', 37), ('4', 39)],
    ('^', 44): [('x', 43), ('3', 45)],
    ('^', 50): [('x', 49), ('2', 51)],
    ('^', 59): [('x', 58), ('2', 60)],
    ('^', 65): [('+', 61), ('2', 66)],
    ('^', 69): [('x', 68), ('3', 70)],
    ('^', 77): [('+', 75), ('2', 78)],
    ('^', 81): [('x', 80), ('2', 82)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((x^2 + 2x^3 - 4)^3)((x^2 - x + 2)^2)((x^3 + 3x - 5)) = x^{15} + 8x^{14} - 14x^{13} - 191x^{12} + 48x^{11} + 1218x^{10} - 60x^9 - 2700x^8 - 1452x^7 + 4375x^6 + 3476x^5 - 2922x^4 - 1685x^3 + 655x^2 + 103x - 400'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 6): [('8', 5), ('^', 8)],
    ('*', 12): [('14', 11), ('^', 14)],
    ('*', 18): [('191', 17), ('^', 20)],
    ('*', 24): [('48', 23), ('^', 26)],
    ('*', 30): [('1218', 29), ('^', 32)],
    ('*', 36): [('60', 35), ('^', 38)],
    ('*', 42): [('2700', 41), ('^', 44)],
    ('*', 48): [('1452', 47), ('^', 50)],
    ('*', 54): [('4375', 53), ('^', 56)],
    ('*', 60): [('3476', 59), ('^', 62)],
    ('*', 66): [('2922', 65), ('^', 68)],
    ('*', 72): [('1685', 71), ('^', 74)],
    ('*', 78): [('655', 77), ('^', 80)],
    ('*', 84): [('103', 83), ('x', 85)],
    ('*', 93): [('2', 92), ('^', 95)],
    ('*', 101): [('^', 99), ('^', 109)],
    ('*', 111): [('*', 101), ('+', 115)],
    ('*', 117): [('3', 116), ('x', 118)],
    ('+', 4): [('^', 2), ('-', 16)],
    ('+', 22): [('+', 4), ('*', 24)],
    ('+', 28): [('+', 22), ('-', 46)],
    ('+', 52): [('+', 28), ('*', 54)],
    ('+', 58): [('+', 52), ('-', 70)],
    ('+', 76): [('+', 58), ('*', 78)],
    ('+', 82): [('+', 76), ('-', 86)],
    ('+', 91): [('^', 89), ('-', 97)],
    ('+', 107): [('-', 105), ('2', 108)],
    ('+', 115): [('^', 113), ('-', 119)],
    ('-', 10): [('*', 6), ('*', 12)],
    ('-', 16): [('-', 10), ('*', 18)],
    ('-', 34): [('*', 30), ('*', 36)],
    ('-', 40): [('-', 34), ('*', 42)],
    ('-', 46): [('-', 40), ('*', 48)],
    ('-', 64): [('*', 60), ('*', 66)],
    ('-', 70): [('-', 64), ('*', 72)],
    ('-', 86): [('*', 84), ('400', 87)],
    ('-', 97): [('*', 93), ('4', 98)],
    ('-', 105): [('^', 103), ('x', 106)],
    ('-', 119): [('*', 117), ('5', 120)],
    ('=', 0): [('*', 111), ('+', 82)],
    ('^', 2): [('x', 1), ('15', 3)],
    ('^', 8): [('x', 7), ('14', 9)],
    ('^', 14): [('x', 13), ('13', 15)],
    ('^', 20): [('x', 19), ('12', 21)],
    ('^', 26): [('x', 25), ('11', 27)],
    ('^', 32): [('x', 31), ('10', 33)],
    ('^', 38): [('x', 37), ('9', 39)],
    ('^', 44): [('x', 43), ('8', 45)],
    ('^', 50): [('x', 49), ('7', 51)],
    ('^', 56): [('x', 55), ('6', 57)],
    ('^', 62): [('x', 61), ('5', 63)],
    ('^', 68): [('x', 67), ('4', 69)],
    ('^', 74): [('x', 73), ('3', 75)],
    ('^', 80): [('x', 79), ('2', 81)],
    ('^', 89): [('x', 88), ('2', 90)],
    ('^', 95): [('x', 94), ('3', 96)],
    ('^', 99): [('+', 91), ('3', 100)],
    ('^', 103): [('x', 102), ('2', 104)],
    ('^', 109): [('+', 107), ('2', 110)],
    ('^', 113): [('x', 112), ('3', 114)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)




#
def test__paveWayForDifferentiation__productRule(verbose=False):# TODO not entirely correct, have to group the \frac{d}{dx} together as one NODE
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{d}{dx}uv=u\\frac{dv}{dx}+v\\frac{du}{dx}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('*', 2): [('/', 1), ('uv', 3)],
    ('*', 5): [('u', 4), ('/', 6)],
    ('*', 9): [('v', 8), ('/', 10)],
    ('+', 7): [('*', 5), ('*', 9)],
    ('/', 1): [('d', 12), ('dx', 11)],
    ('/', 6): [('dv', 16), ('dx', 15)],
    ('/', 10): [('du', 14), ('dx', 13)],
    ('=', 0): [('*', 2), ('+', 7)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__paveWayForDifferentiation__sumRule(verbose=False):# TODO not entirely correct, have to group the \frac{d}{dx} together as one NODE
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{d}{dx}(u+v)=\\frac{du}{dx}+\\frac{dv}{dx}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 2): [('/', 1), ('+', 4)],
    ('+', 4): [('u', 3), ('v', 5)],
    ('+', 7): [('/', 6), ('/', 8)],
    ('/', 1): [('d', 10), ('dx', 9)],
    ('/', 6): [('du', 12), ('dx', 11)],
    ('/', 8): [('dv', 14), ('dx', 13)],
    ('=', 0): [('*', 2), ('+', 7)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)
#

def test__paveWayForIntegration__enclosingBracketNonBackslash(verbose=False): # TODO not entirely correct, have to group the \int{}*dx together as one NODE, and also DEFINITE INTEGRALS
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\int{(x-3)(x+1)}dx=\\frac{1}{3}x^3-3x^2-3x+C'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 2): [('int', 1), ('dx', 3)],
    ('*', 5): [('/', 4), ('^', 7)],
    ('*', 11): [('3', 10), ('^', 13)],
    ('*', 17): [('3', 16), ('x', 18)],
    ('*', 24): [('-', 22), ('+', 26)],
    ('+', 19): [('-', 15), ('C', 20)],
    ('+', 26): [('x', 25), ('1', 27)],
    ('-', 9): [('*', 5), ('*', 11)],
    ('-', 15): [('-', 9), ('*', 17)],
    ('-', 22): [('x', 21), ('3', 23)],
    ('/', 4): [('1', 28), ('3', 29)],
    ('=', 0): [('*', 2), ('+', 19)],
    ('^', 7): [('x', 6), ('3', 8)],
    ('^', 13): [('x', 12), ('2', 14)],
    ('int', 1): [('*', 24)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__paveWayForIntegrtion__exponentOnEnclosingNonBackslash(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\int{(x-1)(x+1)^2}dx=\\frac{1}{4}x^4+\\frac{1}{3}x^3-\\frac{1}{2}x^2-x+C'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = None # to be filled in
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


if __name__=='__main__':
    test__contiguousLeftOvers__decimalPlaces()
    test__weirdVariables__variablesWithCurlyBracketsSimple()
    test__weirdVariables__variablesWithCurlyBracketsWithNums()
    test__weirdVariables__variablesWithCurlyBracketsWithInCurlyBrackets()
    test__weirdVariables__variablesWithCurlyBracketsWithInCurlyBracketsMoreComplex()
    test__weirdVariables__variablesWithCaret()
    test__weirdVariables__variablesWithCaretRealExponent()
    test__weirdVariables__variablesWithCaretMoreComplex()
    test__weirdVariables__variablesWithCurlyBracketsMinus()
    test__weirdVariables__variablesWithCurlyBracketsFrac()
    test__weirdVariables__variablesWithCurlyBracketsImplicitMultiply0()
    test__weirdVariables__variablesWithCurlyBracketsImplicitMultiply1()
    test__makeSubject__manyVariablesStandingTogether()
    test__collateBackslashInfixLeftOversToContiguous__exponentialOverMultiply()
    test__interLevelSubTreeGrafting__exponentialOverEnclosingBrackets()
    test__interLevelSubTreeGrafting__exponentialOverEnclosingBracketsNegativePower()
    test__interLevelSubTreeGrafting__exponentialOverEnclosingBracketsNegativePower0()
    test__findingBackSlashAndInfixOperations__Trig0()
    test__findingBackSlashAndInfixOperations__Trig1()
    test__findingBackSlashAndInfixOperations__Trig2()
    test__findingBackSlashAndInfixOperations__Sqrt0()
    test__findingBackSlashAndInfixOperations__Sqrt1()
    test__findingBackSlashAndInfixOperations__Ln()
    test__findingBackSlashAndInfixOperations__Frac()
    test__findingBackSlashAndInfixOperations__Log0()
    test__findingBackSlashAndInfixOperations__Log1()
    test__findingBackSlashAndInfixOperations__tildeVariable()
    test__findingBackSlashAndInfixOperations__SchrodingerWaveEquation()
    test__infixInBackslash__paraboloid()
    test__sqrtWithPowerCaretRightOtherInfix__hill()
    test__nonInfixBrackets__addImplicitMultiply()
    test__nonInfixBrackets__addImplicitMultiply0()
    test__nonInfixBrackets__addImplicitMultiply1()
    test__BODMAS__priorityBetweenInfixForBrackets()
    test__BODMAS__enclosingBracketInBackslashArg()
    test__BODMAS__enclosingBracketInBackslashArgWithExponent()
    test__BODMAS__enclosingBracketInBackslashArgImplicitZero()
    test__BODMAS__enclosingBracket()
    test__manyFracCaretEnclosingBrac__partialFrac()
    test__fracWithLogNoBase__changeLogBaseFormula()
    test__backslashInfixInBackslash__sqrtInSqrt()
    test__backslashInfixInBackslash__trigInTrig()
    test__backslashInfixInBackslash__logInLog()
    test__backslashInfixInBackslash__fracInFrac()
    test__hassliche__highPowersAndRandomCoefficientsPITEST()
    test__hassliche__nestedPolynomial()
    test__hassliche__nonIntegerAndNegativeCoefficientsDECIMALPOINTTEST()
    test__hassliche__mixedVariablesAndPowersPOWERCOTEVARIABLEDOUBLEVARIABLETEST()
    test__hassliche__irrationalAndTranscendentalNumbersPOWERCOTEBACKSLASH()
    test__hassliche__degree5()
    test__hassliche__degree6()
    test__hassliche__degree7()
    test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm()
    test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm0()
    test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm1()
    test__paveWayForDifferentiation__productRule()
    test__paveWayForDifferentiation__sumRule()
    test__paveWayForIntegration__enclosingBracketNonBackslash()
    # test__paveWayForIntegrtion__exponentOnEnclosingNonBackslash(True) # not tested yet << still throws, TODO refactor brackslash args into a list, ... and the rest of the code...