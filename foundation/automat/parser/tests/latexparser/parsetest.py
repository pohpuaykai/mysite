import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser


def test__contiguousLeftOvers__decimalPlaces(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = ' -0.5 + 1.0 = 0.5'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 1): [('-', 0), ('1.0', 4)],
    ('-', 0): [('0', 6), ('0.5', 3)],
    ('=', 2): [('+', 1), ('0.5', 5)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsSimple(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_{BE}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('V_{BE}', 1), ('V', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsWithNums(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_{Z1}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('V_{Z1}', 1), ('V', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__weirdVariables__variablesWithCurlyBracketsWithInCurlyBrackets(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_{Z_{1}}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('V_{Z_{1}}', 1), ('V', 4)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsWithInCurlyBracketsMoreComplex(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_{in}=R I_R + V_{Z_{1}}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 10): [('R', 4), ('I_R', 5)],
    ('+', 0): [('*', 10), ('V_{Z_{1}}', 7)],
    ('=', 1): [('V_{in}', 2), ('+', 0)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)




def test__weirdVariables__variablesWithCaret(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)
    #if we have underscore, then caret, then es ist exponential
    equationStr = 'V=V^{Q_{1}}_{BE}' #TODO if caret follows an underscore, then its not exponential, sondern, der ganz Ding ist ein VARIABLE
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 1): [('V', 2), ('V^{Q_{1}}_{BE}', 3)]}
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
    ('=', 3): [('^', 0), ('^', 2)],
    ('^', 0): [('V', 4), ('x', 5)],
    ('^', 2): [('V^{Q_{1}}_{BE}', 6), ('x', 10)]}
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
    ('*', 17): [('I_{R_{C}}', 4), ('R_{C}', 7)],
    ('*', 18): [('I_{R}', 13), ('R', 15)],
    ('-', 1): [('*', 17), ('V^{Q_{1}}_{BE}', 9)],
    ('-', 2): [('-', 1), ('*', 18)],
    ('=', 3): [('-', 2), ('0', 16)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsMinus(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_B-V_{BE}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('-', 0): [('V_B', 2), ('V_{BE}', 4)], ('=', 1): [('-', 0), ('V', 6)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{V_B-V_{BE}}{R_B}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 0): [('V_B', 3), ('V_{BE}', 5)],
    ('/', 1): [('-', 0), ('R_B', 7)],
    ('=', 2): [('/', 1), ('V', 9)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsImplicitMultiply0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'P=V_{rms}I_{rms}\\cos(\\phi)'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 8): [('V_{rms}', 4), ('I_{rms}', 6)],
    ('*', 9): [('*', 8), ('\\cos', 0)],
    ('=', 2): [('P', 3), ('*', 9)],
    ('\\cos', 0): [('\\phi', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsImplicitMultiply1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'a_{bc}d_{ef}g_{hi}j_{k}\\cos(\\phi)=O'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 12): [('a_{bc}', 3), ('d_{ef}', 5)],
    ('*', 13): [('*', 12), ('g_{hi}', 7)],
    ('*', 14): [('*', 13), ('j_{k}', 9)],
    ('*', 15): [('*', 14), ('\\cos', 0)],
    ('=', 2): [('*', 15), ('O', 11)],
    ('\\cos', 0): [('\\phi', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__makeSubject__manyVariablesStandingTogether(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'A_v = ( R_L + \\frac{R_2}{1 + s C R_2} )'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 15): [('s', 11), ('C', 12)],
    ('*', 16): [('*', 15), ('R_2', 13)],
    ('+', 0): [('R_L', 6), ('/', 2)],
    ('+', 1): [('1', 10), ('*', 16)],
    ('/', 2): [('R_2', 8), ('+', 1)],
    ('=', 3): [('A_v', 4), ('+', 0)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__collateBackslashInfixLeftOversToContiguous__exponentialOverMultiply(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = ' 3x^{9} = 3x^{2}x^{7}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 12): [('3', 4), ('^', 0)],
    ('*', 13): [('3', 7), ('^', 1)],
    ('*', 14): [('*', 13), ('^', 2)],
    ('=', 3): [('*', 12), ('*', 14)],
    ('^', 0): [('x', 5), ('9', 6)],
    ('^', 1): [('x', 8), ('2', 9)],
    ('^', 2): [('x', 10), ('7', 11)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__interLevelSubTreeGrafting__exponentialOverEnclosingBrackets(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(19y + z^4 + 4w^{12})^{30} = F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 15): [('19', 6), ('y', 7)],
    ('*', 16): [('4', 10), ('^', 1)],
    ('+', 3): [('*', 15), ('^', 0)],
    ('+', 4): [('+', 3), ('*', 16)],
    ('=', 5): [('^', 2), ('F', 14)],
    ('^', 0): [('z', 8), ('4', 9)],
    ('^', 1): [('w', 11), ('12', 12)],
    ('^', 2): [('+', 4), ('30', 13)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__interLevelSubTreeGrafting__exponentialOverEnclosingBracketsNegativePower(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1)^{-1} = 1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 1): [('0', 6), ('1', 4)],
    ('=', 2): [('^', 0), ('1', 5)],
    ('^', 0): [('1', 3), ('-', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__interLevelSubTreeGrafting__exponentialOverEnclosingBracketsNegativePower0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1)^{\\sin(x)-1} = 1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 1): [('sin', 2), ('1', 6)],
    ('=', 3): [('^', 0), ('1', 7)],
    ('^', 0): [('1', 4), ('-', 1)],
    ('sin', 2): [('x', 5)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Trig0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '-\\sin( 2x_0 ) = -2\\sin(x_0)\\cos(x_0)'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 16): [('2', 6), ('x_0', 7)],
    ('*', 17): [('2', 9), ('sin', 3)],
    ('*', 18): [('*', 17), ('cos', 4)],
    ('-', 0): [('0', 14), ('sin', 2)],
    ('-', 1): [('0', 15), ('*', 18)],
    ('=', 5): [('-', 0), ('-', 1)],
    ('cos', 4): [('x_0', 12)],
    ('sin', 2): [('*', 16)],
    ('sin', 3): [('x_0', 10)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast) # rename ast to latex_ast 


def test__findingBackSlashAndInfixOperations__Trig1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sin^2(x) + \\cos^2(x)=1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 2): [('^', 11), ('^', 12)],
    ('=', 5): [('+', 2), ('1', 10)],
    ('^', 11): [('sin', 3), ('2', 6)],
    ('^', 12): [('cos', 4), ('2', 8)],
    ('cos', 4): [('x', 9)],
    ('sin', 3): [('x', 7)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Trig2(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sin^{2}(x)+\\cos^{2}(x)=1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 2): [('^', 11), ('^', 12)],
    ('=', 5): [('+', 2), ('1', 10)],
    ('^', 11): [('sin', 3), ('2', 6)],
    ('^', 12): [('cos', 4), ('2', 8)],
    ('cos', 4): [('x', 9)],
    ('sin', 3): [('x', 7)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Sqrt0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sqrt{4}=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 1): [('nroot', 0), ('2', 3)], ('nroot', 0): [('2', 4), ('4', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Sqrt1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sqrt[3]{8}=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 1): [('nroot', 0), ('2', 4)], ('nroot', 0): [('3', 2), ('8', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Ln(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\ln(e)=1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 1): [('log', 0), ('1', 3)], ('log', 0): [('e', 4), ('e', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Frac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{12}{24}=\\frac{1000}{2000}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('/', 0): [('12', 3), ('24', 4)],
    ('/', 1): [('1000', 5), ('2000', 6)],
    ('=', 2): [('/', 0), ('/', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Log0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log_{12}(8916100448256)=12'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('=', 1): [('log', 0), ('12', 4)],
    ('log', 0): [('12', 2), ('8916100448256', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Log1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log(100)=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 1): [('log', 0), ('2', 3)], ('log', 0): [('10', 4), ('100', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__tildeVariable(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\tilde{x}=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 1): [('tilde', 0), ('2', 3)], ('tilde', 0): [('x', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__SchrodingerWaveEquation(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\widehat{H}\\Psi=\\widehat{E}\\Psi'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 7): [('widehat', 0), ('Psi', 1)],
    ('*', 8): [('widehat', 2), ('Psi', 3)],
    ('=', 4): [('*', 7), ('*', 8)],
    ('widehat', 0): [('H', 5)],
    ('widehat', 2): [('E', 6)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__infixInBackslash__paraboloid(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'z=\\sqrt{x^2+y^2}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 2): [('^', 0), ('^', 1)],
    ('=', 4): [('z', 5), ('nroot', 3)],
    ('^', 0): [('x', 6), ('2', 7)],
    ('^', 1): [('y', 8), ('2', 9)],
    ('nroot', 3): [('2', 10), ('+', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__sqrtWithPowerCaretRightOtherInfix__hill(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'z=-\\sqrt[2]{x^2+y^2}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 3): [('^', 0), ('^', 1)],
    ('-', 2): [('0', 12), ('nroot', 4)],
    ('=', 5): [('z', 6), ('-', 2)],
    ('^', 0): [('x', 8), ('2', 9)],
    ('^', 1): [('y', 10), ('2', 11)],
    ('nroot', 4): [('2', 7), ('+', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__nonInfixBrackets__addImplicitMultiply(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1+(1+(1+1)))(((1+1)+1)+1)=16'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 16): [('+', 0), ('+', 5)],
    ('+', 0): [('1', 7), ('+', 1)],
    ('+', 1): [('1', 8), ('+', 2)],
    ('+', 2): [('1', 9), ('1', 10)],
    ('+', 3): [('1', 11), ('1', 12)],
    ('+', 4): [('+', 3), ('1', 13)],
    ('+', 5): [('+', 4), ('1', 14)],
    ('=', 6): [('*', 16), ('16', 15)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__nonInfixBrackets__addImplicitMultiply0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1+(1+1)(1+1)+1)+1=7'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 14): [('+', 1), ('+', 2)],
    ('+', 0): [('1', 6), ('*', 14)],
    ('+', 1): [('1', 7), ('1', 8)],
    ('+', 2): [('1', 9), ('1', 10)],
    ('+', 3): [('+', 0), ('1', 11)],
    ('+', 4): [('+', 3), ('1', 12)],
    ('=', 5): [('+', 4), ('7', 13)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__nonInfixBrackets__addImplicitMultiply1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((1+(1+(1+1)))(((1+1)+1)+1)+1)+1=18'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 20): [('+', 0), ('+', 5)],
    ('+', 0): [('1', 9), ('+', 1)],
    ('+', 1): [('1', 10), ('+', 2)],
    ('+', 2): [('1', 11), ('1', 12)],
    ('+', 3): [('1', 13), ('1', 14)],
    ('+', 4): [('+', 3), ('1', 15)],
    ('+', 5): [('+', 4), ('1', 16)],
    ('+', 6): [('*', 20), ('1', 17)],
    ('+', 7): [('+', 6), ('1', 18)],
    ('=', 8): [('+', 7), ('18', 19)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__priorityBetweenInfixForBrackets(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{2}{(x-1)(x+1)}=c'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 10): [('-', 0), ('+', 1)],
    ('+', 1): [('x', 7), ('1', 8)],
    ('-', 0): [('x', 5), ('1', 6)],
    ('/', 2): [('2', 4), ('*', 10)],
    ('=', 3): [('/', 2), ('c', 9)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracketInBackslashArg(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{2}{(x-1)(x+1)} = \\frac{1}{x-1} - \\frac{1}{x+1}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 20): [('-', 0), ('+', 3)],
    ('+', 3): [('x', 12), ('1', 13)],
    ('+', 4): [('x', 18), ('1', 19)],
    ('-', 0): [('x', 10), ('1', 11)],
    ('-', 1): [('x', 15), ('1', 16)],
    ('-', 2): [('/', 6), ('/', 7)],
    ('/', 5): [('2', 9), ('*', 20)],
    ('/', 6): [('1', 14), ('-', 1)],
    ('/', 7): [('1', 17), ('+', 4)],
    ('=', 8): [('/', 5), ('-', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracketInBackslashArgWithExponent(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'c=\\sin((x-3)^2)'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 1): [('x', 5), ('3', 6)],
    ('=', 3): [('c', 4), ('sin', 2)],
    ('^', 0): [('-', 1), ('2', 7)],
    ('sin', 2): [('^', 0)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracketInBackslashArgImplicitZero(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{2}{(x-1)(x+1)} = \\frac{1}{x-1} + \\frac{-1}{x+1}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 22): [('-', 0), ('+', 3)],
    ('+', 3): [('x', 13), ('1', 14)],
    ('+', 4): [('/', 7), ('/', 8)],
    ('+', 5): [('x', 19), ('1', 20)],
    ('-', 0): [('x', 11), ('1', 12)],
    ('-', 1): [('x', 16), ('1', 17)],
    ('-', 2): [('0', 21), ('1', 18)],
    ('/', 6): [('2', 10), ('*', 22)],
    ('/', 7): [('1', 15), ('-', 1)],
    ('/', 8): [('-', 2), ('+', 5)],
    ('=', 9): [('/', 6), ('+', 4)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracket(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'x^2-6x+9=(x-3)^2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 14): [('6', 8), ('x', 9)],
    ('+', 4): [('-', 2), ('9', 10)],
    ('-', 2): [('^', 0), ('*', 14)],
    ('-', 3): [('x', 11), ('3', 12)],
    ('=', 5): [('+', 4), ('^', 1)],
    ('^', 0): [('x', 6), ('2', 7)],
    ('^', 1): [('-', 3), ('2', 13)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__manyFracCaretEnclosingBrac__partialFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{x^2}{(x-2)(x-3)^2}=\\frac{4}{x-2}+\\frac{-3}{x-3}+\\frac{9}{(x-3)^2}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 34): [('-', 3), ('^', 1)],
    ('+', 9): [('/', 12), ('/', 13)],
    ('+', 10): [('+', 9), ('/', 14)],
    ('-', 3): [('x', 18), ('2', 19)],
    ('-', 4): [('x', 20), ('3', 21)],
    ('-', 5): [('x', 24), ('2', 25)],
    ('-', 6): [('0', 33), ('3', 26)],
    ('-', 7): [('x', 27), ('3', 28)],
    ('-', 8): [('x', 30), ('3', 31)],
    ('/', 11): [('^', 0), ('*', 34)],
    ('/', 12): [('4', 23), ('-', 5)],
    ('/', 13): [('-', 6), ('-', 7)],
    ('/', 14): [('9', 29), ('^', 2)],
    ('=', 15): [('/', 11), ('+', 10)],
    ('^', 0): [('x', 16), ('2', 17)],
    ('^', 1): [('-', 4), ('2', 22)],
    ('^', 2): [('-', 8), ('2', 32)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__fracWithLogNoBase__changeLogBaseFormula(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log_{b}(a)=\\frac{\\log_{c}(a)}{\\log_{c}(b)}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('/', 1): [('log', 2), ('log', 3)],
    ('=', 4): [('log', 0), ('/', 1)],
    ('log', 0): [('b', 5), ('a', 6)],
    ('log', 2): [('c', 7), ('a', 8)],
    ('log', 3): [('c', 9), ('b', 10)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__sqrtInSqrt(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sqrt[\\sqrt{\\frac{\\pi}{22}}]{\\sqrt[\\sin(\\pi)]{\\pi}}=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('/', 2): [('pi', 3), ('22', 9)],
    ('=', 8): [('nroot', 0), ('F', 10)],
    ('nroot', 0): [('nroot', 1), ('nroot', 4)],
    ('nroot', 1): [('2', 12), ('/', 2)],
    ('nroot', 4): [('sin', 5), ('pi', 7)],
    ('sin', 5): [('pi', 6)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__trigInTrig(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sin^{20-\\cos^{43}(1-\\frac{\\pi}{5})}(9-\\tan^4(\\theta))+5=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 6): [('^', 24), ('5', 20)],
    ('-', 3): [('20', 14), ('^', 22)],
    ('-', 4): [('1', 16), ('/', 9)],
    ('-', 5): [('9', 18), ('^', 23)],
    ('/', 9): [('pi', 10), ('5', 17)],
    ('=', 13): [('+', 6), ('F', 21)],
    ('^', 22): [('cos', 8), ('43', 15)],
    ('^', 23): [('tan', 11), ('4', 19)],
    ('^', 24): [('sin', 7), ('-', 3)],
    ('cos', 8): [('-', 4)],
    ('sin', 7): [('-', 5)],
    ('tan', 11): [('theta', 12)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__logInLog(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log_{\\ln(90-x)}(\\log(z^5))=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 1): [('90', 6), ('x', 7)],
    ('=', 5): [('log', 2), ('F', 10)],
    ('^', 0): [('z', 8), ('5', 9)],
    ('log', 2): [('log', 3), ('log', 4)],
    ('log', 3): [('e', 11), ('-', 1)],
    ('log', 4): [('10', 12), ('^', 0)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__fracInFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{\\frac{\\sin^2(x)+\\cos^2(x)}{\\sin^2(x)-\\cos^2(x)}}{\\frac{\\cos(2x)-\\sin(2x)}{\\cos(2x)+\\sin(2x)}}=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 37): [('2', 28), ('x', 29)],
    ('*', 38): [('2', 30), ('x', 31)],
    ('*', 39): [('2', 32), ('x', 33)],
    ('*', 40): [('2', 34), ('x', 35)],
    ('+', 6): [('^', 41), ('^', 42)],
    ('+', 7): [('cos', 17), ('sin', 18)],
    ('-', 4): [('^', 43), ('^', 44)],
    ('-', 5): [('cos', 15), ('sin', 16)],
    ('/', 8): [('/', 9), ('/', 14)],
    ('/', 9): [('+', 6), ('-', 4)],
    ('/', 14): [('-', 5), ('+', 7)],
    ('=', 19): [('/', 8), ('F', 36)],
    ('^', 41): [('sin', 10), ('2', 20)],
    ('^', 42): [('cos', 11), ('2', 22)],
    ('^', 43): [('sin', 12), ('2', 24)],
    ('^', 44): [('cos', 13), ('2', 26)],
    ('cos', 11): [('x', 23)],
    ('cos', 13): [('x', 27)],
    ('cos', 15): [('*', 37)],
    ('cos', 17): [('*', 39)],
    ('sin', 10): [('x', 21)],
    ('sin', 12): [('x', 25)],
    ('sin', 16): [('*', 38)],
    ('sin', 18): [('*', 40)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__highPowersAndRandomCoefficientsPITEST(verbose=False): # TODO not entirely correct... should treat P(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'P = 7x^{13} - 3x^{9} + 5x^{8} - \\sqrt{2}x^{4} + \\pi x^{2} - 42' # 'P(x) = 7x^{13} - 3x^{9} + 5x^{8} - \\sqrt{2}x^{4} + \\pi x^{2} - 42', but we cannot handle P(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 29): [('7', 14), ('^', 0)],
    ('*', 30): [('3', 17), ('^', 1)],
    ('*', 31): [('5', 20), ('^', 2)],
    ('*', 32): [('nroot', 10), ('^', 3)],
    ('*', 33): [('pi', 11), ('^', 4)],
    ('+', 8): [('-', 5), ('-', 6)],
    ('+', 9): [('+', 8), ('-', 7)],
    ('-', 5): [('*', 29), ('*', 30)],
    ('-', 6): [('*', 31), ('*', 32)],
    ('-', 7): [('*', 33), ('42', 28)],
    ('=', 12): [('P', 13), ('+', 9)],
    ('^', 0): [('x', 15), ('13', 16)],
    ('^', 1): [('x', 18), ('9', 19)],
    ('^', 2): [('x', 21), ('8', 22)],
    ('^', 3): [('x', 24), ('4', 25)],
    ('^', 4): [('x', 26), ('2', 27)],
    ('nroot', 10): [('2', 34), ('2', 23)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__nestedPolynomial(verbose=False): # TODO not entirely correct... should treat Q(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'Q = (x^3 - 2x^2 + 5x - 7)^2 - (x - 1)^3 + 3x^{21}' # 'Q(x) = (x^3 - 2x^2 + 5x - 7)^2 - (x - 1)^3 + 3x^{21}', but we cannot handle Q(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 28): [('2', 15), ('^', 1)],
    ('*', 29): [('5', 18), ('x', 19)],
    ('*', 30): [('3', 25), ('^', 4)],
    ('+', 9): [('-', 5), ('-', 6)],
    ('+', 10): [('-', 7), ('*', 30)],
    ('-', 5): [('^', 0), ('*', 28)],
    ('-', 6): [('*', 29), ('7', 20)],
    ('-', 7): [('^', 2), ('^', 3)],
    ('-', 8): [('x', 22), ('1', 23)],
    ('=', 11): [('Q', 12), ('+', 10)],
    ('^', 0): [('x', 13), ('3', 14)],
    ('^', 1): [('x', 16), ('2', 17)],
    ('^', 2): [('+', 9), ('2', 21)],
    ('^', 3): [('-', 8), ('3', 24)],
    ('^', 4): [('x', 26), ('21', 27)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__nonIntegerAndNegativeCoefficientsDECIMALPOINTTEST(verbose=False): # TODO not entirely correct... should treat R(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'R = -0.5x^{10} + 3.14x^{8} - \\frac{2}{3}x^{5} + 1.618x^{3} - \\frac{1}{x}' # 'R(x) = -0.5x^{10} + 3.14x^{8} - \\frac{2}{3}x^{5} + 1.618x^{3} - \\frac{1}{x}', but we cannot handle R(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 29): [('0.5', 13), ('^', 0)],
    ('*', 30): [('3.14', 16), ('^', 1)],
    ('*', 31): [('/', 9), ('^', 2)],
    ('*', 32): [('1.618', 23), ('^', 3)],
    ('+', 7): [('-', 4), ('-', 5)],
    ('+', 8): [('+', 7), ('-', 6)],
    ('-', 4): [('0', 28), ('*', 29)],
    ('-', 5): [('*', 30), ('*', 31)],
    ('-', 6): [('*', 32), ('/', 10)],
    ('/', 9): [('2', 19), ('3', 20)],
    ('/', 10): [('1', 26), ('x', 27)],
    ('=', 11): [('R', 12), ('+', 8)],
    ('^', 0): [('x', 14), ('10', 15)],
    ('^', 1): [('x', 17), ('8', 18)],
    ('^', 2): [('x', 21), ('5', 22)],
    ('^', 3): [('x', 24), ('3', 25)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__mixedVariablesAndPowersPOWERCOTEVARIABLEDOUBLEVARIABLETEST(verbose=False): # TODO not entirely correct... should treat S(x, y) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'S = x^5y^4 - 7x^3y^2 + 2x^2 - y^3 + x^2y - 4' # 'S(x, y) = x^5y^4 - 7x^3y^2 + 2x^2 - y^3 + x^2y - 4', but we cannot handle S(x, y) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 32): [('^', 0), ('^', 1)],
    ('*', 33): [('7', 18), ('^', 2)],
    ('*', 34): [('*', 33), ('^', 3)],
    ('*', 35): [('2', 23), ('^', 4)],
    ('*', 36): [('^', 6), ('y', 30)],
    ('+', 10): [('-', 7), ('-', 8)],
    ('+', 11): [('+', 10), ('-', 9)],
    ('-', 7): [('*', 32), ('*', 34)],
    ('-', 8): [('*', 35), ('^', 5)],
    ('-', 9): [('*', 36), ('4', 31)],
    ('=', 12): [('S', 13), ('+', 11)],
    ('^', 0): [('x', 14), ('5', 15)],
    ('^', 1): [('y', 16), ('4', 17)],
    ('^', 2): [('x', 19), ('3', 20)],
    ('^', 3): [('y', 21), ('2', 22)],
    ('^', 4): [('x', 24), ('2', 25)],
    ('^', 5): [('y', 26), ('3', 27)],
    ('^', 6): [('x', 28), ('2', 29)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__irrationalAndTranscendentalNumbersPOWERCOTEBACKSLASH(verbose=False): # TODO not entirely correct... should treat T(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'T = e^{x} - \\cos(x)x^4 + x^3\\sin(x) - \\ln(x^2+1)' # 'T(x) = e^{x} - \\cos(x)x^4 + x^3\\sin(x) - \\ln(x^2+1)', but we cannot handle T(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 24): [('cos', 8), ('^', 1)],
    ('*', 25): [('^', 2), ('sin', 9)],
    ('+', 6): [('-', 4), ('-', 5)],
    ('+', 7): [('^', 3), ('1', 23)],
    ('-', 4): [('^', 0), ('*', 24)],
    ('-', 5): [('*', 25), ('log', 10)],
    ('=', 11): [('T', 12), ('+', 6)],
    ('^', 0): [('e', 13), ('x', 14)],
    ('^', 1): [('x', 16), ('4', 17)],
    ('^', 2): [('x', 18), ('3', 19)],
    ('^', 3): [('x', 21), ('2', 22)],
    ('cos', 8): [('x', 15)],
    ('log', 10): [('e', 28), ('+', 7)],
    ('sin', 9): [('x', 20)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__degree5(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(x - 1)(x + 2)(x - 3)(x + 4)(x - 5) = x^5 - 3x^4 - 32x^3 + 94x^2 + 31x - 120'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 39): [('-', 4), ('+', 10)],
    ('*', 40): [('*', 39), ('-', 5)],
    ('*', 41): [('*', 40), ('+', 11)],
    ('*', 42): [('*', 41), ('-', 6)],
    ('*', 43): [('3', 27), ('^', 1)],
    ('*', 44): [('32', 30), ('^', 2)],
    ('*', 45): [('94', 33), ('^', 3)],
    ('*', 46): [('31', 36), ('x', 37)],
    ('+', 10): [('x', 17), ('2', 18)],
    ('+', 11): [('x', 21), ('4', 22)],
    ('+', 12): [('-', 8), ('*', 45)],
    ('+', 13): [('+', 12), ('-', 9)],
    ('-', 4): [('x', 15), ('1', 16)],
    ('-', 5): [('x', 19), ('3', 20)],
    ('-', 6): [('x', 23), ('5', 24)],
    ('-', 7): [('^', 0), ('*', 43)],
    ('-', 8): [('-', 7), ('*', 44)],
    ('-', 9): [('*', 46), ('120', 38)],
    ('=', 14): [('*', 42), ('+', 13)],
    ('^', 0): [('x', 25), ('5', 26)],
    ('^', 1): [('x', 28), ('4', 29)],
    ('^', 2): [('x', 31), ('3', 32)],
    ('^', 3): [('x', 34), ('2', 35)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__degree6(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(x - 1)(x - 2)(x + 3)(x + 4)(x - 5)(x + 6) = x^6 + 5x^5 - 35x^4 - 75x^3 + 368x^2 + 246x - 720'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 47): [('-', 5), ('-', 6)],
    ('*', 48): [('*', 47), ('+', 11)],
    ('*', 49): [('*', 48), ('+', 12)],
    ('*', 50): [('*', 49), ('-', 7)],
    ('*', 51): [('*', 50), ('+', 13)],
    ('*', 52): [('5', 32), ('^', 1)],
    ('*', 53): [('35', 35), ('^', 2)],
    ('*', 54): [('75', 38), ('^', 3)],
    ('*', 55): [('368', 41), ('^', 4)],
    ('*', 56): [('246', 44), ('x', 45)],
    ('+', 11): [('x', 22), ('3', 23)],
    ('+', 12): [('x', 24), ('4', 25)],
    ('+', 13): [('x', 28), ('6', 29)],
    ('+', 14): [('^', 0), ('-', 9)],
    ('+', 15): [('+', 14), ('*', 55)],
    ('+', 16): [('+', 15), ('-', 10)],
    ('-', 5): [('x', 18), ('1', 19)],
    ('-', 6): [('x', 20), ('2', 21)],
    ('-', 7): [('x', 26), ('5', 27)],
    ('-', 8): [('*', 52), ('*', 53)],
    ('-', 9): [('-', 8), ('*', 54)],
    ('-', 10): [('*', 56), ('720', 46)],
    ('=', 17): [('*', 51), ('+', 16)],
    ('^', 0): [('x', 30), ('6', 31)],
    ('^', 1): [('x', 33), ('5', 34)],
    ('^', 2): [('x', 36), ('4', 37)],
    ('^', 3): [('x', 39), ('3', 40)],
    ('^', 4): [('x', 42), ('2', 43)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__degree7(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(x - 1)(x + 2)(x - 3)(x + 4)(x - 5)(x + 6)(x - 7) = x^7 + 4x^6 - 37x^5 - 58x^4 + 520x^3 + 201x^2 - 2156x + 5040'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 55): [('-', 6), ('+', 13)],
    ('*', 56): [('*', 55), ('-', 7)],
    ('*', 57): [('*', 56), ('+', 14)],
    ('*', 58): [('*', 57), ('-', 8)],
    ('*', 59): [('*', 58), ('+', 15)],
    ('*', 60): [('*', 59), ('-', 9)],
    ('*', 61): [('4', 37), ('^', 1)],
    ('*', 62): [('37', 40), ('^', 2)],
    ('*', 63): [('58', 43), ('^', 3)],
    ('*', 64): [('520', 46), ('^', 4)],
    ('*', 65): [('201', 49), ('^', 5)],
    ('*', 66): [('2156', 52), ('x', 53)],
    ('+', 13): [('x', 23), ('2', 24)],
    ('+', 14): [('x', 27), ('4', 28)],
    ('+', 15): [('x', 31), ('6', 32)],
    ('+', 16): [('^', 0), ('-', 11)],
    ('+', 17): [('+', 16), ('*', 64)],
    ('+', 18): [('+', 17), ('-', 12)],
    ('+', 19): [('+', 18), ('5040', 54)],
    ('-', 6): [('x', 21), ('1', 22)],
    ('-', 7): [('x', 25), ('3', 26)],
    ('-', 8): [('x', 29), ('5', 30)],
    ('-', 9): [('x', 33), ('7', 34)],
    ('-', 10): [('*', 61), ('*', 62)],
    ('-', 11): [('-', 10), ('*', 63)],
    ('-', 12): [('*', 65), ('*', 66)],
    ('=', 20): [('*', 60), ('+', 19)],
    ('^', 0): [('x', 35), ('7', 36)],
    ('^', 1): [('x', 38), ('6', 39)],
    ('^', 2): [('x', 41), ('5', 42)],
    ('^', 3): [('x', 44), ('4', 45)],
    ('^', 4): [('x', 47), ('3', 48)],
    ('^', 5): [('x', 50), ('2', 51)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((x + 2x^2 - 3)^2)((x^2 - x + 1)^3)((x^3 + 2x - 5)) = x^{10} + 4x^9 - 2x^8 - 41x^7 - 69x^6 + 142x^5 + 420x^4 - 567x^3 - 174x^2 + 185x - 75'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 76): [('^', 1), ('^', 3)],
    ('*', 77): [('*', 76), ('+', 25)],
    ('*', 78): [('2', 32), ('^', 0)],
    ('*', 79): [('2', 44), ('x', 45)],
    ('*', 80): [('4', 49), ('^', 6)],
    ('*', 81): [('2', 52), ('^', 7)],
    ('*', 82): [('41', 55), ('^', 8)],
    ('*', 83): [('69', 58), ('^', 9)],
    ('*', 84): [('142', 61), ('^', 10)],
    ('*', 85): [('420', 64), ('^', 11)],
    ('*', 86): [('567', 67), ('^', 12)],
    ('*', 87): [('174', 70), ('^', 13)],
    ('*', 88): [('185', 73), ('x', 74)],
    ('+', 23): [('x', 31), ('-', 14)],
    ('+', 24): [('-', 15), ('1', 40)],
    ('+', 25): [('^', 4), ('-', 16)],
    ('+', 26): [('^', 5), ('-', 19)],
    ('+', 27): [('+', 26), ('*', 84)],
    ('+', 28): [('+', 27), ('-', 21)],
    ('+', 29): [('+', 28), ('-', 22)],
    ('-', 14): [('*', 78), ('3', 35)],
    ('-', 15): [('^', 2), ('x', 39)],
    ('-', 16): [('*', 79), ('5', 46)],
    ('-', 17): [('*', 80), ('*', 81)],
    ('-', 18): [('-', 17), ('*', 82)],
    ('-', 19): [('-', 18), ('*', 83)],
    ('-', 20): [('*', 85), ('*', 86)],
    ('-', 21): [('-', 20), ('*', 87)],
    ('-', 22): [('*', 88), ('75', 75)],
    ('=', 30): [('*', 77), ('+', 29)],
    ('^', 0): [('x', 33), ('2', 34)],
    ('^', 1): [('+', 23), ('2', 36)],
    ('^', 2): [('x', 37), ('2', 38)],
    ('^', 3): [('+', 24), ('3', 41)],
    ('^', 4): [('x', 42), ('3', 43)],
    ('^', 5): [('x', 47), ('10', 48)],
    ('^', 6): [('x', 50), ('9', 51)],
    ('^', 7): [('x', 53), ('8', 54)],
    ('^', 8): [('x', 56), ('7', 57)],
    ('^', 9): [('x', 59), ('6', 60)],
    ('^', 10): [('x', 62), ('5', 63)],
    ('^', 11): [('x', 65), ('4', 66)],
    ('^', 12): [('x', 68), ('3', 69)],
    ('^', 13): [('x', 71), ('2', 72)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((x^2 + x - 1)^2)((x^3 - 2x + 4)^2)((x^2 + 3x - 7)) = x^{10} - 3x^9 - 20x^8 + 60x^7 + 161x^6 - 260x^5 - 385x^4 + 494x^3 + 509x^2 - 378x + 196'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 76): [('^', 1), ('^', 3)],
    ('*', 77): [('*', 76), ('+', 24)],
    ('*', 78): [('2', 38), ('x', 39)],
    ('*', 79): [('3', 44), ('x', 45)],
    ('*', 80): [('3', 49), ('^', 6)],
    ('*', 81): [('20', 52), ('^', 7)],
    ('*', 82): [('60', 55), ('^', 8)],
    ('*', 83): [('161', 58), ('^', 9)],
    ('*', 84): [('260', 61), ('^', 10)],
    ('*', 85): [('385', 64), ('^', 11)],
    ('*', 86): [('494', 67), ('^', 12)],
    ('*', 87): [('509', 70), ('^', 13)],
    ('*', 88): [('378', 73), ('x', 74)],
    ('+', 22): [('^', 0), ('-', 14)],
    ('+', 23): [('-', 15), ('4', 40)],
    ('+', 24): [('^', 4), ('-', 16)],
    ('+', 25): [('-', 18), ('*', 82)],
    ('+', 26): [('+', 25), ('-', 20)],
    ('+', 27): [('+', 26), ('*', 86)],
    ('+', 28): [('+', 27), ('-', 21)],
    ('+', 29): [('+', 28), ('196', 75)],
    ('-', 14): [('x', 33), ('1', 34)],
    ('-', 15): [('^', 2), ('*', 78)],
    ('-', 16): [('*', 79), ('7', 46)],
    ('-', 17): [('^', 5), ('*', 80)],
    ('-', 18): [('-', 17), ('*', 81)],
    ('-', 19): [('*', 83), ('*', 84)],
    ('-', 20): [('-', 19), ('*', 85)],
    ('-', 21): [('*', 87), ('*', 88)],
    ('=', 30): [('*', 77), ('+', 29)],
    ('^', 0): [('x', 31), ('2', 32)],
    ('^', 1): [('+', 22), ('2', 35)],
    ('^', 2): [('x', 36), ('3', 37)],
    ('^', 3): [('+', 23), ('2', 41)],
    ('^', 4): [('x', 42), ('2', 43)],
    ('^', 5): [('x', 47), ('10', 48)],
    ('^', 6): [('x', 50), ('9', 51)],
    ('^', 7): [('x', 53), ('8', 54)],
    ('^', 8): [('x', 56), ('7', 57)],
    ('^', 9): [('x', 59), ('6', 60)],
    ('^', 10): [('x', 62), ('5', 63)],
    ('^', 11): [('x', 65), ('4', 66)],
    ('^', 12): [('x', 68), ('3', 69)],
    ('^', 13): [('x', 71), ('2', 72)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((x^2 + 2x^3 - 4)^3)((x^2 - x + 2)^2)((x^3 + 3x - 5)) = x^{15} + 8x^{14} - 14x^{13} - 191x^{12} + 48x^{11} + 1218x^{10} - 60x^9 - 2700x^8 - 1452x^7 + 4375x^6 + 3476x^5 - 2922x^4 - 1685x^3 + 655x^2 + 103x - 400'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 103): [('^', 2), ('^', 4)],
    ('*', 104): [('*', 103), ('+', 33)],
    ('*', 105): [('2', 44), ('^', 1)],
    ('*', 106): [('3', 56), ('x', 57)],
    ('*', 107): [('8', 61), ('^', 7)],
    ('*', 108): [('14', 64), ('^', 8)],
    ('*', 109): [('191', 67), ('^', 9)],
    ('*', 110): [('48', 70), ('^', 10)],
    ('*', 111): [('1218', 73), ('^', 11)],
    ('*', 112): [('60', 76), ('^', 12)],
    ('*', 113): [('2700', 79), ('^', 13)],
    ('*', 114): [('1452', 82), ('^', 14)],
    ('*', 115): [('4375', 85), ('^', 15)],
    ('*', 116): [('3476', 88), ('^', 16)],
    ('*', 117): [('2922', 91), ('^', 17)],
    ('*', 118): [('1685', 94), ('^', 18)],
    ('*', 119): [('655', 97), ('^', 19)],
    ('*', 120): [('103', 100), ('x', 101)],
    ('+', 31): [('^', 0), ('-', 20)],
    ('+', 32): [('-', 21), ('2', 52)],
    ('+', 33): [('^', 5), ('-', 22)],
    ('+', 34): [('^', 6), ('-', 24)],
    ('+', 35): [('+', 34), ('*', 110)],
    ('+', 36): [('+', 35), ('-', 27)],
    ('+', 37): [('+', 36), ('*', 115)],
    ('+', 38): [('+', 37), ('-', 29)],
    ('+', 39): [('+', 38), ('*', 119)],
    ('+', 40): [('+', 39), ('-', 30)],
    ('-', 20): [('*', 105), ('4', 47)],
    ('-', 21): [('^', 3), ('x', 51)],
    ('-', 22): [('*', 106), ('5', 58)],
    ('-', 23): [('*', 107), ('*', 108)],
    ('-', 24): [('-', 23), ('*', 109)],
    ('-', 25): [('*', 111), ('*', 112)],
    ('-', 26): [('-', 25), ('*', 113)],
    ('-', 27): [('-', 26), ('*', 114)],
    ('-', 28): [('*', 116), ('*', 117)],
    ('-', 29): [('-', 28), ('*', 118)],
    ('-', 30): [('*', 120), ('400', 102)],
    ('=', 41): [('*', 104), ('+', 40)],
    ('^', 0): [('x', 42), ('2', 43)],
    ('^', 1): [('x', 45), ('3', 46)],
    ('^', 2): [('+', 31), ('3', 48)],
    ('^', 3): [('x', 49), ('2', 50)],
    ('^', 4): [('+', 32), ('2', 53)],
    ('^', 5): [('x', 54), ('3', 55)],
    ('^', 6): [('x', 59), ('15', 60)],
    ('^', 7): [('x', 62), ('14', 63)],
    ('^', 8): [('x', 65), ('13', 66)],
    ('^', 9): [('x', 68), ('12', 69)],
    ('^', 10): [('x', 71), ('11', 72)],
    ('^', 11): [('x', 74), ('10', 75)],
    ('^', 12): [('x', 77), ('9', 78)],
    ('^', 13): [('x', 80), ('8', 81)],
    ('^', 14): [('x', 83), ('7', 84)],
    ('^', 15): [('x', 86), ('6', 87)],
    ('^', 16): [('x', 89), ('5', 90)],
    ('^', 17): [('x', 92), ('4', 93)],
    ('^', 18): [('x', 95), ('3', 96)],
    ('^', 19): [('x', 98), ('2', 99)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__newSymbolsLimitTheorem__sumRule(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = "\\lim_{x\\to\\bar{x}}{(f+g)(x)}=\\lim_{x\\to\\bar{x}}{f(x)}+\\lim_{x\\to\\bar{x}}{g(x)}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 25): [('+', 3), ('x', 16)],
    ('*', 26): [('f', 19), ('x', 20)],
    ('*', 27): [('g', 23), ('x', 24)],
    ('+', 3): [('f', 14), ('g', 15)],
    ('+', 4): [('lim', 7), ('lim', 9)],
    ('=', 11): [('lim', 5), ('+', 4)],
    ('\\to', 0): [('x', 12), ('bar', 6)],
    ('\\to', 1): [('x', 17), ('bar', 8)],
    ('\\to', 2): [('x', 21), ('bar', 10)],
    ('bar', 6): [('x', 13)],
    ('bar', 8): [('x', 18)],
    ('bar', 10): [('x', 22)],
    ('lim', 5): [('\\to', 0), ('*', 25)],
    ('lim', 7): [('\\to', 1), ('*', 26)],
    ('lim', 9): [('\\to', 2), ('*', 27)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__newSymbolsLimitTheorem__productRule(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = "\\lim_{x\\to\\bar{x}}{(f g)(x)}=(\\lim_{x\\to\\bar{x}}{f(x)})(\\lim_{x\\to\\bar{x}}{g(x)})"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 23): [('*', 25), ('x', 14)],
    ('*', 24): [('lim', 5), ('lim', 7)],
    ('*', 25): [('f', 12), ('g', 13)],
    ('*', 26): [('f', 17), ('x', 18)],
    ('*', 27): [('g', 21), ('x', 22)],
    ('=', 9): [('lim', 3), ('*', 24)],
    ('\\to', 0): [('x', 10), ('bar', 4)],
    ('\\to', 1): [('x', 15), ('bar', 6)],
    ('\\to', 2): [('x', 19), ('bar', 8)],
    ('bar', 4): [('x', 11)],
    ('bar', 6): [('x', 16)],
    ('bar', 8): [('x', 20)],
    ('lim', 3): [('\\to', 0), ('*', 23)],
    ('lim', 5): [('\\to', 1), ('*', 26)],
    ('lim', 7): [('\\to', 2), ('*', 27)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__newSymbolsLimitTheorem__constantTimesRule(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = "\\lim_{x\\to\\bar{x}}{(c f)(x)}=c(\\lim_{x\\to\\bar{x}}{f(x)})"#the space between c and f is important for this parser
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 17): [('*', 18), ('x', 11)],
    ('*', 18): [('c', 9), ('f', 10)],
    ('*', 19): [('c', 12), ('lim', 4)],
    ('*', 20): [('f', 15), ('x', 16)],
    ('=', 6): [('lim', 2), ('*', 19)],
    ('\\to', 0): [('x', 7), ('bar', 3)],
    ('\\to', 1): [('x', 13), ('bar', 5)],
    ('bar', 3): [('x', 8)],
    ('bar', 5): [('x', 14)],
    ('lim', 2): [('\\to', 0), ('*', 17)],
    ('lim', 4): [('\\to', 1), ('*', 20)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__newSymbolsLimitTheorem__quotientRule(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = "\\lim_{x\\to\\bar{x}}{(\\frac{f}{g})(x)}=\\frac{\\lim_{x\\to\\bar{x}}{f(x)}}{\\lim_{x\\to\\bar{x}}{g(x)}}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 25): [('/', 5), ('x', 16)],
    ('*', 26): [('f', 19), ('x', 20)],
    ('*', 27): [('g', 23), ('x', 24)],
    ('/', 5): [('f', 14), ('g', 15)],
    ('/', 6): [('lim', 7), ('lim', 9)],
    ('=', 11): [('lim', 3), ('/', 6)],
    ('\\to', 0): [('x', 12), ('bar', 4)],
    ('\\to', 1): [('x', 17), ('bar', 8)],
    ('\\to', 2): [('x', 21), ('bar', 10)],
    ('bar', 4): [('x', 13)],
    ('bar', 8): [('x', 18)],
    ('bar', 10): [('x', 22)],
    ('lim', 3): [('\\to', 0), ('*', 25)],
    ('lim', 7): [('\\to', 1), ('*', 26)],
    ('lim', 9): [('\\to', 2), ('*', 27)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__newSymbols__fourierSeries(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = "\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}{f(x)e^{-i 2\\pi\\frac{n}{P}x}dx}(e^{i 2\\pi\\frac{n}{P}x})}}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 48): [('*', 49), ('^', 4)],
    ('*', 49): [('/', 16), ('int', 17)],
    ('*', 50): [('f', 30), ('x', 31)],
    ('*', 51): [('*', 50), ('^', 3)],
    ('*', 52): [('i', 33), ('2', 34)],
    ('*', 53): [('*', 52), ('pi', 18)],
    ('*', 54): [('*', 53), ('/', 19)],
    ('*', 55): [('*', 54), ('x', 37)],
    ('*', 56): [('*', 51), ('dx', 38)],
    ('*', 57): [('i', 40), ('2', 41)],
    ('*', 58): [('*', 57), ('pi', 20)],
    ('*', 59): [('*', 58), ('/', 21)],
    ('*', 60): [('*', 59), ('x', 44)],
    ('-', 7): [('0', 45), ('theta', 14)],
    ('-', 8): [('0', 46), ('/', 6)],
    ('-', 9): [('0', 47), ('*', 55)],
    ('/', 5): [('P', 26), ('2', 27)],
    ('/', 6): [('P', 28), ('2', 29)],
    ('/', 16): [('1', 24), ('P', 25)],
    ('/', 19): [('n', 35), ('P', 36)],
    ('/', 21): [('n', 42), ('P', 43)],
    ('=', 22): [('n', 23), ('-', 7)],
    ('\\to', 0): [('theta', 11), ('infty', 12)],
    ('^', 3): [('e', 32), ('-', 9)],
    ('^', 4): [('e', 39), ('*', 60)],
    ('int', 17): [('/', 5), ('-', 8), ('*', 56)],
    ('lim', 10): [('\\to', 0), ('sum', 13)],
    ('sum', 13): [('=', 22), ('theta', 15), ('*', 48)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)

def test__newSymbols__parallelSumOfCapacitance(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    #_find_variables_or_numbers COMPOUND)_VARIABLE need CURLY BRACKET, else will BREAK TODO
    equationStr="C^{parallelTotal}_{k}=\\frac{\\prod_{k_0=1}^{k}{C_{k_0}}}{\\sum_{k_1=1}^{k}{\\frac{\\prod_{k_0=1}^{k}{C_{k_0}}}{C_{k_1}}}}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('/', 4): [('prod', 5), ('sum', 6)],
    ('/', 7): [('prod', 8), ('C_{k_1}', 34)],
    ('=', 9): [('C^{parallelTotal}_{k}', 13), ('/', 4)],
    ('=', 10): [('k_0', 16), ('1', 18)],
    ('=', 11): [('k_1', 23), ('1', 25)],
    ('=', 12): [('k_0', 27), ('1', 29)],
    ('prod', 5): [('=', 10), ('k', 19), ('C_{k_0}', 20)],
    ('prod', 8): [('=', 12), ('k', 30), ('C_{k_0}', 31)],
    ('sum', 6): [('=', 11), ('k', 26), ('/', 7)]}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)

def test__newSymbols__faradayIntegralForm(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr="\\oint_{\\partial{\\Omega}}{\\vec{E}\\cdot d \\vec{l}} =-\\frac{d}{d t}\\iint_{\\Omega}{\\vec{B}\\cdot d \\vec{S}}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 24): [('\\cdot', 0), ('vec', 7)],
    ('*', 25): [('d', 18), ('t', 19)],
    ('*', 26): [('/', 8), ('iint', 9)],
    ('*', 27): [('\\cdot', 1), ('vec', 12)],
    ('-', 2): [('0', 23), ('*', 26)],
    ('/', 8): [('d', 17), ('*', 25)],
    ('=', 13): [('oint', 3), ('-', 2)],
    ('\\cdot', 0): [('vec', 6), ('d', 15)],
    ('\\cdot', 1): [('vec', 11), ('d', 21)],
    ('iint', 9): [('Omega', 10), ('*', 27)],
    ('oint', 3): [('partial', 4), ('*', 24)],
    ('partial', 4): [('Omega', 5)],
    ('vec', 6): [('E', 14)],
    ('vec', 7): [('l', 16)],
    ('vec', 11): [('B', 20)],
    ('vec', 12): [('S', 22)]}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)

def test__newSymbols__faradayDifferentialForm(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr="\\nabla\\times\\vec{E}=-\\frac{\\partial{\\vec{B}}}{\\partial{t}}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 1): [('0', 12), ('/', 4)],
    ('/', 4): [('partial', 5), ('partial', 7)],
    ('=', 8): [('\\times', 0), ('-', 1)],
    ('\\times', 0): [('nabla', 2), ('vec', 3)],
    ('partial', 5): [('vec', 6)],
    ('partial', 7): [('t', 11)],
    ('vec', 3): [('E', 9)],
    ('vec', 6): [('B', 10)]}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)

def test__newSymbols__gaussIntegralForm(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)
    #NOT expecting \\epsilon_0, \\epsilon will work<<<<<<<refactor _ & ^ arg finding, we always use these (_find_variable|_find_backslash) TODO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    equationStr="\\oiint_{\\partial{\\Omega}}{\\vec{E}\\cdot d \\vec{S}}=\\frac{1}{\\epsilon}\\iiint_{\\Omega}{\\rho d V}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 18): [('\\cdot', 0), ('vec', 5)],
    ('*', 19): [('/', 6), ('iiint', 8)],
    ('*', 20): [('rho', 10), ('d', 16)],
    ('*', 21): [('*', 20), ('V', 17)],
    ('/', 6): [('1', 15), ('epsilon', 7)],
    ('=', 11): [('oiint', 1), ('*', 19)],
    ('\\cdot', 0): [('vec', 4), ('d', 13)],
    ('iiint', 8): [('Omega', 9), ('*', 21)],
    ('oiint', 1): [('partial', 2), ('*', 18)],
    ('partial', 2): [('Omega', 3)],
    ('vec', 4): [('E', 12)],
    ('vec', 5): [('S', 14)]}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__newSymbols__greenSecondVectorIdentityDifferentialForm(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)
    
    equationStr="p\\Delta{q}-q\\Delta{p}=\\nabla\\cdot(p\\nabla{q}-q\\nabla{p})"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 17): [('p', 9), ('Delta', 3)],
    ('*', 18): [('q', 11), ('Delta', 4)],
    ('*', 19): [('p', 13), ('nabla', 6)],
    ('*', 20): [('*', 19), ('q', 14)],
    ('*', 21): [('q', 15), ('nabla', 7)],
    ('*', 22): [('*', 21), ('p', 16)],
    ('-', 1): [('*', 17), ('*', 18)],
    ('-', 2): [('*', 20), ('*', 22)],
    ('=', 8): [('-', 1), ('\\cdot', 0)],
    ('Delta', 3): [('q', 10)],
    ('Delta', 4): [('p', 12)],
    ('\\cdot', 0): [('nabla', 5), ('-', 2)]}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



#
def test__paveWayForDifferentiation__productRule(verbose=False):# TODO not entirely correct, have to group the \frac{d}{dx} together as one NODE
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{d}{dx}u v=u\\frac{d v}{dx}+v\\frac{d u}{dx}'#the space between u v is important for this parser
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 17): [('/', 1), ('u', 7)],
    ('*', 18): [('*', 17), ('v', 8)],
    ('*', 19): [('u', 9), ('/', 2)],
    ('*', 20): [('d', 10), ('v', 11)],
    ('*', 21): [('v', 13), ('/', 3)],
    ('*', 22): [('d', 14), ('u', 15)],
    ('+', 0): [('*', 19), ('*', 21)],
    ('/', 1): [('d', 5), ('dx', 6)],
    ('/', 2): [('*', 20), ('dx', 12)],
    ('/', 3): [('*', 22), ('dx', 16)],
    ('=', 4): [('*', 18), ('+', 0)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__paveWayForDifferentiation__sumRule(verbose=False):# TODO not entirely correct, have to group the \frac{d}{dx} together as one NODE
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{d}{dx}(u+v)=\\frac{d u}{dx}+\\frac{d v}{dx}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 16): [('/', 2), ('+', 0)],
    ('*', 17): [('d', 10), ('u', 11)],
    ('*', 18): [('d', 13), ('v', 14)],
    ('+', 0): [('u', 8), ('v', 9)],
    ('+', 1): [('/', 3), ('/', 4)],
    ('/', 2): [('d', 6), ('dx', 7)],
    ('/', 3): [('*', 17), ('dx', 12)],
    ('/', 4): [('*', 18), ('dx', 15)],
    ('=', 5): [('*', 16), ('+', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)
#

def test__paveWayForIntegration__enclosingBracketNonBackslash(verbose=False): # TODO not entirely correct, have to group the \int{}*dx together as one NODE, and also DEFINITE INTEGRALS
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\int{(x-3)(x+1)}dx=\\frac{1}{3}x^3-3x^2-3x+C'
    parser = Latexparser(equationStr, verbose=verbose) # TODO _find_backslash hangs when cannot find all its compulsory, it should throw to user after 3 tries
    parser._parse()
    expected_ast = {
    ('*', 25): [('-', 2), ('+', 5)],
    ('*', 26): [('int', 7), ('dx', 14)],
    ('*', 27): [('/', 8), ('^', 0)],
    ('*', 28): [('3', 19), ('^', 1)],
    ('*', 29): [('3', 22), ('x', 23)],
    ('+', 5): [('x', 12), ('1', 13)],
    ('+', 6): [('-', 4), ('C', 24)],
    ('-', 2): [('x', 10), ('3', 11)],
    ('-', 3): [('*', 27), ('*', 28)],
    ('-', 4): [('-', 3), ('*', 29)],
    ('/', 8): [('1', 15), ('3', 16)],
    ('=', 9): [('*', 26), ('+', 6)],
    ('^', 0): [('x', 17), ('3', 18)],
    ('^', 1): [('x', 20), ('2', 21)],
    ('int', 7): [('*', 25)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__paveWayForIntegrtion__exponentOnEnclosingNonBackslash(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\int{(x-1)(x+1)^2}dx=\\frac{1}{4}x^4+\\frac{1}{3}x^3-\\frac{1}{2}x^2-x+C'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 35): [('-', 4), ('^', 0)],
    ('*', 36): [('int', 10), ('dx', 20)],
    ('*', 37): [('/', 11), ('^', 1)],
    ('*', 38): [('/', 12), ('^', 2)],
    ('*', 39): [('/', 13), ('^', 3)],
    ('+', 7): [('x', 17), ('1', 18)],
    ('+', 8): [('*', 37), ('-', 6)],
    ('+', 9): [('+', 8), ('C', 34)],
    ('-', 4): [('x', 15), ('1', 16)],
    ('-', 5): [('*', 38), ('*', 39)],
    ('-', 6): [('-', 5), ('x', 33)],
    ('/', 11): [('1', 21), ('4', 22)],
    ('/', 12): [('1', 25), ('3', 26)],
    ('/', 13): [('1', 29), ('2', 30)],
    ('=', 14): [('*', 36), ('+', 9)],
    ('^', 0): [('+', 7), ('2', 19)],
    ('^', 1): [('x', 23), ('4', 24)],
    ('^', 2): [('x', 27), ('3', 28)],
    ('^', 3): [('x', 31), ('2', 32)],
    ('int', 10): [('*', 35)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__matrix__determinantMetricTensor(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\det(\\begin{pmatrix}E&F\\F&G\\end{pmatrix})=E G-F^2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = None
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
    test__newSymbolsLimitTheorem__sumRule()
    test__newSymbolsLimitTheorem__productRule()
    test__newSymbolsLimitTheorem__constantTimesRule()
    test__newSymbolsLimitTheorem__quotientRule()
    test__newSymbols__fourierSeries()
    test__newSymbols__parallelSumOfCapacitance()
    test__newSymbols__faradayIntegralForm()
    test__newSymbols__faradayDifferentialForm()
    test__newSymbols__gaussIntegralForm()
    test__newSymbols__greenSecondVectorIdentityDifferentialForm()
    #
    #
    test__paveWayForDifferentiation__productRule()
    test__paveWayForDifferentiation__sumRule()
    test__paveWayForIntegration__enclosingBracketNonBackslash()
    test__paveWayForIntegrtion__exponentOnEnclosingNonBackslash()
    #matrix test cases
    # test__matrix__determinantMetricTensor(True)
    #Test Metric_Tensor? Good for Mechanical Engineering later :) See ChatGPT for test case
    #https://en.wikipedia.org/wiki/Finite_strain_theory#Deformation_tensors
    #https://en.wikipedia.org/wiki/Piola%E2%80%93Kirchhoff_stress_tensors