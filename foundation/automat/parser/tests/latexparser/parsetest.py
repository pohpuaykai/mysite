import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser


def test__contiguousLeftOvers__decimalPlaces(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = ' -0.5 + 1.0 = 0.5'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('+', 2): [('-', 1), ('1.0', 4)],
    ('-', 1): [('0', 6), ('0.5', 3)],
    ('=', 0): [('+', 2), ('0.5', 5)]}
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
    expected_ast = {   ('*', 10): [('R', 4), ('I_R', 5)],
    ('+', 1): [('*', 10), ('V_{Z_{1}}', 7)],
    ('=', 0): [('V_{in}', 2), ('+', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)




def test__weirdVariables__variablesWithCaret(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)
    #if we have underscore, then caret, then es ist exponential
    equationStr = 'V=V^{Q_{1}}_{BE}' #TODO if caret follows an underscore, then its not exponential, sondern, der ganz Ding ist ein VARIABLE
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('V', 2), ('V^{Q_{1}}_{BE}', 3)]}
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
    ('=', 0): [('^', 1), ('^', 3)],
    ('^', 1): [('V', 4), ('x', 5)],
    ('^', 3): [('V^{Q_{1}}_{BE}', 6), ('x', 10)]}
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
    ('-', 2): [('*', 17), ('V^{Q_{1}}_{BE}', 9)],
    ('-', 3): [('-', 2), ('*', 18)],
    ('=', 0): [('-', 3), ('0', 16)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsMinus(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'V_B-V_{BE}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('-', 1): [('V_B', 2), ('V_{BE}', 4)], ('=', 0): [('-', 1), ('V', 6)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__weirdVariables__variablesWithCurlyBracketsFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{V_B-V_{BE}}{R_B}=V'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 1): [('V_B', 3), ('V_{BE}', 5)],
    ('/', 2): [('-', 1), ('R_B', 7)],
    ('=', 0): [('/', 2), ('V', 9)]}
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
    ('*', 9): [('*', 8), ('cos', 1)],
    ('=', 0): [('P', 3), ('*', 9)],
    ('cos', 1): [('phi', 2)]}
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
    ('*', 15): [('*', 14), ('cos', 1)],
    ('=', 0): [('*', 15), ('O', 11)],
    ('cos', 1): [('phi', 2)]}
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
    ('+', 1): [('R_L', 6), ('/', 3)],
    ('+', 2): [('1', 10), ('*', 16)],
    ('/', 3): [('R_2', 8), ('+', 2)],
    ('=', 0): [('A_v', 4), ('+', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__collateBackslashInfixLeftOversToContiguous__exponentialOverMultiply(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = ' 3x^{9} = 3x^{2}x^{7}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 12): [('3', 4), ('^', 1)],
    ('*', 13): [('3', 7), ('^', 2)],
    ('*', 14): [('*', 13), ('^', 3)],
    ('=', 0): [('*', 12), ('*', 14)],
    ('^', 1): [('x', 5), ('9', 6)],
    ('^', 2): [('x', 8), ('2', 9)],
    ('^', 3): [('x', 10), ('7', 11)]}
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
    ('*', 16): [('4', 10), ('^', 2)],
    ('+', 4): [('*', 15), ('^', 1)],
    ('+', 5): [('+', 4), ('*', 16)],
    ('=', 0): [('^', 3), ('F', 14)],
    ('^', 1): [('z', 8), ('4', 9)],
    ('^', 2): [('w', 11), ('12', 12)],
    ('^', 3): [('+', 5), ('30', 13)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__interLevelSubTreeGrafting__exponentialOverEnclosingBracketsNegativePower(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1)^{-1} = 1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 2): [('0', 6), ('1', 4)],
    ('=', 0): [('^', 1), ('1', 5)],
    ('^', 1): [('1', 3), ('-', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__interLevelSubTreeGrafting__exponentialOverEnclosingBracketsNegativePower0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1)^{\\sin(x)-1} = 1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   
    ('-', 2): [('sin', 3), ('1', 6)],
    ('=', 0): [('^', 1), ('1', 7)],
    ('^', 1): [('1', 4), ('-', 2)],
    ('sin', 3): [('x', 5)]}
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
    ('*', 17): [('2', 9), ('sin', 4)],
    ('*', 18): [('*', 17), ('cos', 5)],
    ('-', 1): [('0', 14), ('sin', 3)],
    ('-', 2): [('0', 15), ('*', 18)],
    ('=', 0): [('-', 1), ('-', 2)],
    ('cos', 5): [('x_0', 12)],
    ('sin', 3): [('*', 16)],
    ('sin', 4): [('x_0', 10)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast) # rename ast to latex_ast 


def test__findingBackSlashAndInfixOperations__Trig1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sin^2(x) + \\cos^2(x)=1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 3): [('^', 11), ('^', 12)],
    ('=', 0): [('+', 3), ('1', 10)],
    ('^', 11): [('sin', 4), ('2', 6)],
    ('^', 12): [('cos', 5), ('2', 8)],
    ('cos', 5): [('x', 9)],
    ('sin', 4): [('x', 7)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Trig2(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sin^{2}(x)+\\cos^{2}(x)=1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 3): [('^', 11), ('^', 12)],
    ('=', 0): [('+', 3), ('1', 10)],
    ('^', 11): [('sin', 4), ('2', 6)],
    ('^', 12): [('cos', 5), ('2', 8)],
    ('cos', 5): [('x', 9)],
    ('sin', 4): [('x', 7)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Sqrt0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sqrt{4}=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('nroot', 1), ('2', 3)], ('nroot', 1): [('2', 4), ('4', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Sqrt1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sqrt[3]{9}=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('nroot', 1), ('2', 4)], ('nroot', 1): [('3', 2), ('9', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Ln(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\ln(e)=1'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('log', 1), ('1', 3)], ('log', 1): [('e', 4), ('e', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Frac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{12}{24}=\\frac{1000}{2000}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('/', 1): [('12', 3), ('24', 4)],
    ('/', 2): [('1000', 5), ('2000', 6)],
    ('=', 0): [('/', 1), ('/', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Log0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log_{12}(8916100448256)=12'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('=', 0): [('log', 1), ('12', 4)],
    ('log', 1): [('12', 2), ('8916100448256', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__Log1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log(100)=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('log', 1), ('2', 3)], ('log', 1): [('10', 4), ('100', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__tildeVariable(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\tilde{x}=2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {('=', 0): [('tilde', 1), ('2', 3)], ('tilde', 1): [('x', 2)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__findingBackSlashAndInfixOperations__SchrodingerWaveEquation(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\widehat{H}\\Psi=\\widehat{E}\\Psi'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 7): [('widehat', 1), ('Psi', 2)],
    ('*', 8): [('widehat', 3), ('Psi', 4)],
    ('=', 0): [('*', 7), ('*', 8)],
    ('widehat', 1): [('H', 5)],
    ('widehat', 3): [('E', 6)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__infixInBackslash__paraboloid(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'z=\\sqrt{x^2+y^2}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 3): [('^', 1), ('^', 2)],
    ('=', 0): [('z', 5), ('nroot', 4)],
    ('^', 1): [('x', 6), ('2', 7)],
    ('^', 2): [('y', 8), ('2', 9)],
    ('nroot', 4): [('2', 10), ('+', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__sqrtWithPowerCaretRightOtherInfix__hill(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'z=-\\sqrt[2]{x^2+y^2}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 4): [('^', 1), ('^', 2)],
    ('-', 3): [('0', 12), ('nroot', 5)],
    ('=', 0): [('z', 6), ('-', 3)],
    ('^', 1): [('x', 8), ('2', 9)],
    ('^', 2): [('y', 10), ('2', 11)],
    ('nroot', 5): [('2', 7), ('+', 4)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__nonInfixBrackets__addImplicitMultiply(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1+(1+(1+1)))(((1+1)+1)+1)=16'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 16): [('+', 1), ('+', 6)],
    ('+', 1): [('1', 7), ('+', 2)],
    ('+', 2): [('1', 8), ('+', 3)],
    ('+', 3): [('1', 9), ('1', 10)],
    ('+', 4): [('1', 11), ('1', 12)],
    ('+', 5): [('+', 4), ('1', 13)],
    ('+', 6): [('+', 5), ('1', 14)],
    ('=', 0): [('*', 16), ('16', 15)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__nonInfixBrackets__addImplicitMultiply0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(1+(1+1)(1+1)+1)+1=7'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 14): [('+', 2), ('+', 3)],
    ('+', 1): [('1', 6), ('*', 14)],
    ('+', 2): [('1', 7), ('1', 8)],
    ('+', 3): [('1', 9), ('1', 10)],
    ('+', 4): [('+', 1), ('1', 11)],
    ('+', 5): [('+', 4), ('1', 12)],
    ('=', 0): [('+', 5), ('7', 13)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__nonInfixBrackets__addImplicitMultiply1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((1+(1+(1+1)))(((1+1)+1)+1)+1)+1=18'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 20): [('+', 1), ('+', 6)],
    ('+', 1): [('1', 9), ('+', 2)],
    ('+', 2): [('1', 10), ('+', 3)],
    ('+', 3): [('1', 11), ('1', 12)],
    ('+', 4): [('1', 13), ('1', 14)],
    ('+', 5): [('+', 4), ('1', 15)],
    ('+', 6): [('+', 5), ('1', 16)],
    ('+', 7): [('*', 20), ('1', 17)],
    ('+', 8): [('+', 7), ('1', 18)],
    ('=', 0): [('+', 8), ('18', 19)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__priorityBetweenInfixForBrackets(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{2}{(x-1)(x+1)}=c'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 10): [('-', 1), ('+', 2)],
    ('+', 2): [('x', 7), ('1', 8)],
    ('-', 1): [('x', 5), ('1', 6)],
    ('/', 3): [('2', 4), ('*', 10)],
    ('=', 0): [('/', 3), ('c', 9)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracketInBackslashArg(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{2}{(x-1)(x+1)} = \\frac{1}{x-1} - \\frac{1}{x+1}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 20): [('-', 1), ('+', 4)],
    ('+', 4): [('x', 12), ('1', 13)],
    ('+', 5): [('x', 18), ('1', 19)],
    ('-', 1): [('x', 10), ('1', 11)],
    ('-', 2): [('x', 15), ('1', 16)],
    ('-', 3): [('/', 7), ('/', 8)],
    ('/', 6): [('2', 9), ('*', 20)],
    ('/', 7): [('1', 14), ('-', 2)],
    ('/', 8): [('1', 17), ('+', 5)],
    ('=', 0): [('/', 6), ('-', 3)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracketInBackslashArgWithExponent(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'c=\\sin((x-3)^2)'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 2): [('x', 5), ('3', 6)],
    ('=', 0): [('c', 4), ('sin', 3)],
    ('^', 1): [('-', 2), ('2', 7)],
    ('sin', 3): [('^', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracketInBackslashArgImplicitZero(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{2}{(x-1)(x+1)} = \\frac{1}{x-1} + \\frac{-1}{x+1}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 22): [('-', 1), ('+', 4)],
    ('+', 4): [('x', 13), ('1', 14)],
    ('+', 5): [('/', 8), ('/', 9)],
    ('+', 6): [('x', 19), ('1', 20)],
    ('-', 1): [('x', 11), ('1', 12)],
    ('-', 2): [('x', 16), ('1', 17)],
    ('-', 3): [('0', 21), ('1', 18)],
    ('/', 7): [('2', 10), ('*', 22)],
    ('/', 8): [('1', 15), ('-', 2)],
    ('/', 9): [('-', 3), ('+', 6)],
    ('=', 0): [('/', 7), ('+', 5)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__BODMAS__enclosingBracket(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'x^2-6x+9=(x-3)^2'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {   ('*', 14): [('6', 8), ('x', 9)],
    ('+', 5): [('-', 3), ('9', 10)],
    ('-', 3): [('^', 1), ('*', 14)],
    ('-', 4): [('x', 11), ('3', 12)],
    ('=', 0): [('+', 5), ('^', 2)],
    ('^', 1): [('x', 6), ('2', 7)],
    ('^', 2): [('-', 4), ('2', 13)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__manyFracCaretEnclosingBrac__partialFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{x^2}{(x-2)(x-3)^2}=\\frac{4}{x-2}+\\frac{-3}{x-3}+\\frac{9}{(x-3)^2}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 34): [('-', 4), ('^', 2)],
    ('+', 10): [('/', 13), ('/', 14)],
    ('+', 11): [('+', 10), ('/', 15)],
    ('-', 4): [('x', 18), ('2', 19)],
    ('-', 5): [('x', 20), ('3', 21)],
    ('-', 6): [('x', 24), ('2', 25)],
    ('-', 7): [('0', 33), ('3', 26)],
    ('-', 8): [('x', 27), ('3', 28)],
    ('-', 9): [('x', 30), ('3', 31)],
    ('/', 12): [('^', 1), ('*', 34)],
    ('/', 13): [('4', 23), ('-', 6)],
    ('/', 14): [('-', 7), ('-', 8)],
    ('/', 15): [('9', 29), ('^', 3)],
    ('=', 0): [('/', 12), ('+', 11)],
    ('^', 1): [('x', 16), ('2', 17)],
    ('^', 2): [('-', 5), ('2', 22)],
    ('^', 3): [('-', 9), ('2', 32)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__fracWithLogNoBase__changeLogBaseFormula(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log_{b}(a)=\\frac{\\log_{c}(a)}{\\log_{c}(b)}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('/', 2): [('log', 3), ('log', 4)],
    ('=', 0): [('log', 1), ('/', 2)],
    ('log', 1): [('b', 5), ('a', 6)],
    ('log', 3): [('c', 7), ('a', 8)],
    ('log', 4): [('c', 9), ('b', 10)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__sqrtInSqrt(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sqrt[\\sqrt{\\frac{\\pi}{22}}]{\\sqrt[\\sin(\\pi)]{\\pi}}=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('/', 3): [('pi', 4), ('22', 9)],
    ('=', 0): [('nroot', 1), ('F', 10)],
    ('nroot', 1): [('nroot', 2), ('nroot', 5)],
    ('nroot', 2): [('2', 12), ('/', 3)],
    ('nroot', 5): [('sin', 6), ('pi', 8)],
    ('sin', 6): [('pi', 7)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__trigInTrig(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\sin^{20-\\cos^{43}(1-\\frac{\\pi}{5})}(9-\\tan^4(\\theta))+5=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('+', 7): [('^', 24), ('5', 20)],
    ('-', 4): [('20', 14), ('^', 22)],
    ('-', 5): [('1', 16), ('/', 10)],
    ('-', 6): [('9', 18), ('^', 23)],
    ('/', 10): [('pi', 11), ('5', 17)],
    ('=', 0): [('+', 7), ('F', 21)],
    ('^', 22): [('cos', 9), ('43', 15)],
    ('^', 23): [('tan', 12), ('4', 19)],
    ('^', 24): [('sin', 8), ('-', 4)],
    ('cos', 9): [('-', 5)],
    ('sin', 8): [('-', 6)],
    ('tan', 12): [('theta', 13)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__backslashInfixInBackslash__logInLog(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\log_{\\ln(90-x)}(\\log(z^5))=F'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('-', 2): [('90', 6), ('x', 7)],
    ('=', 0): [('log', 3), ('F', 10)],
    ('^', 1): [('z', 8), ('5', 9)],
    ('log', 3): [('log', 4), ('log', 5)],
    ('log', 4): [('e', 11), ('-', 2)],
    ('log', 5): [('10', 12), ('^', 1)]}
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
    ('+', 7): [('^', 41), ('^', 42)],
    ('+', 8): [('cos', 18), ('sin', 19)],
    ('-', 5): [('^', 43), ('^', 44)],
    ('-', 6): [('cos', 16), ('sin', 17)],
    ('/', 9): [('/', 10), ('/', 15)],
    ('/', 10): [('+', 7), ('-', 5)],
    ('/', 15): [('-', 6), ('+', 8)],
    ('=', 0): [('/', 9), ('F', 36)],
    ('^', 41): [('sin', 11), ('2', 20)],
    ('^', 42): [('cos', 12), ('2', 22)],
    ('^', 43): [('sin', 13), ('2', 24)],
    ('^', 44): [('cos', 14), ('2', 26)],
    ('cos', 12): [('x', 23)],
    ('cos', 14): [('x', 27)],
    ('cos', 16): [('*', 37)],
    ('cos', 18): [('*', 39)],
    ('sin', 11): [('x', 21)],
    ('sin', 13): [('x', 25)],
    ('sin', 17): [('*', 38)],
    ('sin', 19): [('*', 40)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__highPowersAndRandomCoefficientsPITEST(verbose=False): # TODO not entirely correct... should treat P(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'P = 7x^{13} - 3x^{9} + 5x^{8} - \\sqrt{2}x^{4} + \\pi x^{2} - 42' # 'P(x) = 7x^{13} - 3x^{9} + 5x^{8} - \\sqrt{2}x^{4} + \\pi x^{2} - 42', but we cannot handle P(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 29): [('7', 14), ('^', 1)],
    ('*', 30): [('3', 17), ('^', 2)],
    ('*', 31): [('5', 20), ('^', 3)],
    ('*', 32): [('nroot', 11), ('^', 4)],
    ('*', 33): [('pi', 12), ('^', 5)],
    ('+', 9): [('-', 6), ('-', 7)],
    ('+', 10): [('+', 9), ('-', 8)],
    ('-', 6): [('*', 29), ('*', 30)],
    ('-', 7): [('*', 31), ('*', 32)],
    ('-', 8): [('*', 33), ('42', 28)],
    ('=', 0): [('P', 13), ('+', 10)],
    ('^', 1): [('x', 15), ('13', 16)],
    ('^', 2): [('x', 18), ('9', 19)],
    ('^', 3): [('x', 21), ('8', 22)],
    ('^', 4): [('x', 24), ('4', 25)],
    ('^', 5): [('x', 26), ('2', 27)],
    ('nroot', 11): [('2', 34), ('2', 23)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__nestedPolynomial(verbose=False): # TODO not entirely correct... should treat Q(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'Q = (x^3 - 2x^2 + 5x - 7)^2 - (x - 1)^3 + 3x^{21}' # 'Q(x) = (x^3 - 2x^2 + 5x - 7)^2 - (x - 1)^3 + 3x^{21}', but we cannot handle Q(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 28): [('2', 15), ('^', 2)],
    ('*', 29): [('5', 18), ('x', 19)],
    ('*', 30): [('3', 25), ('^', 5)],
    ('+', 10): [('-', 6), ('-', 7)],
    ('+', 11): [('-', 8), ('*', 30)],
    ('-', 6): [('^', 1), ('*', 28)],
    ('-', 7): [('*', 29), ('7', 20)],
    ('-', 8): [('^', 3), ('^', 4)],
    ('-', 9): [('x', 22), ('1', 23)],
    ('=', 0): [('Q', 12), ('+', 11)],
    ('^', 1): [('x', 13), ('3', 14)],
    ('^', 2): [('x', 16), ('2', 17)],
    ('^', 3): [('+', 10), ('2', 21)],
    ('^', 4): [('-', 9), ('3', 24)],
    ('^', 5): [('x', 26), ('21', 27)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__nonIntegerAndNegativeCoefficientsDECIMALPOINTTEST(verbose=False): # TODO not entirely correct... should treat R(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'R = -0.5x^{10} + 3.14x^{8} - \\frac{2}{3}x^{5} + 1.618x^{3} - \\frac{1}{x}' # 'R(x) = -0.5x^{10} + 3.14x^{8} - \\frac{2}{3}x^{5} + 1.618x^{3} - \\frac{1}{x}', but we cannot handle R(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 29): [('0.5', 13), ('^', 1)],
    ('*', 30): [('3.14', 16), ('^', 2)],
    ('*', 31): [('/', 10), ('^', 3)],
    ('*', 32): [('1.618', 23), ('^', 4)],
    ('+', 8): [('-', 5), ('-', 6)],
    ('+', 9): [('+', 8), ('-', 7)],
    ('-', 5): [('0', 28), ('*', 29)],
    ('-', 6): [('*', 30), ('*', 31)],
    ('-', 7): [('*', 32), ('/', 11)],
    ('/', 10): [('2', 19), ('3', 20)],
    ('/', 11): [('1', 26), ('x', 27)],
    ('=', 0): [('R', 12), ('+', 9)],
    ('^', 1): [('x', 14), ('10', 15)],
    ('^', 2): [('x', 17), ('8', 18)],
    ('^', 3): [('x', 21), ('5', 22)],
    ('^', 4): [('x', 24), ('3', 25)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__mixedVariablesAndPowersPOWERCOTEVARIABLEDOUBLEVARIABLETEST(verbose=False): # TODO not entirely correct... should treat S(x, y) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'S = x^5y^4 - 7x^3y^2 + 2x^2 - y^3 + x^2y - 4' # 'S(x, y) = x^5y^4 - 7x^3y^2 + 2x^2 - y^3 + x^2y - 4', but we cannot handle S(x, y) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 32): [('^', 1), ('^', 2)],
    ('*', 33): [('7', 18), ('^', 3)],
    ('*', 34): [('*', 33), ('^', 4)],
    ('*', 35): [('2', 23), ('^', 5)],
    ('*', 36): [('^', 7), ('y', 30)],
    ('+', 11): [('-', 8), ('-', 9)],
    ('+', 12): [('+', 11), ('-', 10)],
    ('-', 8): [('*', 32), ('*', 34)],
    ('-', 9): [('*', 35), ('^', 6)],
    ('-', 10): [('*', 36), ('4', 31)],
    ('=', 0): [('S', 13), ('+', 12)],
    ('^', 1): [('x', 14), ('5', 15)],
    ('^', 2): [('y', 16), ('4', 17)],
    ('^', 3): [('x', 19), ('3', 20)],
    ('^', 4): [('y', 21), ('2', 22)],
    ('^', 5): [('x', 24), ('2', 25)],
    ('^', 6): [('y', 26), ('3', 27)],
    ('^', 7): [('x', 28), ('2', 29)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__irrationalAndTranscendentalNumbersPOWERCOTEBACKSLASH(verbose=False): # TODO not entirely correct... should treat T(x) differently... not sure how yet
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = 'T = e^{x} - \\cos(x)x^4 + x^3\\sin(x) - \\ln(x^2+1)' # 'T(x) = e^{x} - \\cos(x)x^4 + x^3\\sin(x) - \\ln(x^2+1)', but we cannot handle T(x) now
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 24): [('cos', 9), ('^', 2)],
    ('*', 25): [('^', 3), ('sin', 10)],
    ('+', 7): [('-', 5), ('-', 6)],
    ('+', 8): [('^', 4), ('1', 23)],
    ('-', 5): [('^', 1), ('*', 24)],
    ('-', 6): [('*', 25), ('log', 11)],
    ('=', 0): [('T', 12), ('+', 7)],
    ('^', 1): [('e', 13), ('x', 14)],
    ('^', 2): [('x', 16), ('4', 17)],
    ('^', 3): [('x', 18), ('3', 19)],
    ('^', 4): [('x', 21), ('2', 22)],
    ('cos', 9): [('x', 15)],
    ('log', 11): [('e', 28), ('+', 8)],
    ('sin', 10): [('x', 20)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__degree5(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(x - 1)(x + 2)(x - 3)(x + 4)(x - 5) = x^5 - 3x^4 - 32x^3 + 94x^2 + 31x - 120'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 39): [('-', 5), ('+', 11)],
    ('*', 40): [('*', 39), ('-', 6)],
    ('*', 41): [('*', 40), ('+', 12)],
    ('*', 42): [('*', 41), ('-', 7)],
    ('*', 43): [('3', 27), ('^', 2)],
    ('*', 44): [('32', 30), ('^', 3)],
    ('*', 45): [('94', 33), ('^', 4)],
    ('*', 46): [('31', 36), ('x', 37)],
    ('+', 11): [('x', 17), ('2', 18)],
    ('+', 12): [('x', 21), ('4', 22)],
    ('+', 13): [('-', 9), ('*', 45)],
    ('+', 14): [('+', 13), ('-', 10)],
    ('-', 5): [('x', 15), ('1', 16)],
    ('-', 6): [('x', 19), ('3', 20)],
    ('-', 7): [('x', 23), ('5', 24)],
    ('-', 8): [('^', 1), ('*', 43)],
    ('-', 9): [('-', 8), ('*', 44)],
    ('-', 10): [('*', 46), ('120', 38)],
    ('=', 0): [('*', 42), ('+', 14)],
    ('^', 1): [('x', 25), ('5', 26)],
    ('^', 2): [('x', 28), ('4', 29)],
    ('^', 3): [('x', 31), ('3', 32)],
    ('^', 4): [('x', 34), ('2', 35)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__degree6(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(x - 1)(x - 2)(x + 3)(x + 4)(x - 5)(x + 6) = x^6 + 5x^5 - 35x^4 - 75x^3 + 368x^2 + 246x - 720'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 47): [('-', 6), ('-', 7)],
    ('*', 48): [('*', 47), ('+', 12)],
    ('*', 49): [('*', 48), ('+', 13)],
    ('*', 50): [('*', 49), ('-', 8)],
    ('*', 51): [('*', 50), ('+', 14)],
    ('*', 52): [('5', 32), ('^', 2)],
    ('*', 53): [('35', 35), ('^', 3)],
    ('*', 54): [('75', 38), ('^', 4)],
    ('*', 55): [('368', 41), ('^', 5)],
    ('*', 56): [('246', 44), ('x', 45)],
    ('+', 12): [('x', 22), ('3', 23)],
    ('+', 13): [('x', 24), ('4', 25)],
    ('+', 14): [('x', 28), ('6', 29)],
    ('+', 15): [('^', 1), ('-', 10)],
    ('+', 16): [('+', 15), ('*', 55)],
    ('+', 17): [('+', 16), ('-', 11)],
    ('-', 6): [('x', 18), ('1', 19)],
    ('-', 7): [('x', 20), ('2', 21)],
    ('-', 8): [('x', 26), ('5', 27)],
    ('-', 9): [('*', 52), ('*', 53)],
    ('-', 10): [('-', 9), ('*', 54)],
    ('-', 11): [('*', 56), ('720', 46)],
    ('=', 0): [('*', 51), ('+', 17)],
    ('^', 1): [('x', 30), ('6', 31)],
    ('^', 2): [('x', 33), ('5', 34)],
    ('^', 3): [('x', 36), ('4', 37)],
    ('^', 4): [('x', 39), ('3', 40)],
    ('^', 5): [('x', 42), ('2', 43)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__degree7(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(x - 1)(x + 2)(x - 3)(x + 4)(x - 5)(x + 6)(x - 7) = x^7 + 4x^6 - 37x^5 - 58x^4 + 520x^3 + 201x^2 - 2156x + 5040'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 55): [('-', 7), ('+', 14)],
    ('*', 56): [('*', 55), ('-', 8)],
    ('*', 57): [('*', 56), ('+', 15)],
    ('*', 58): [('*', 57), ('-', 9)],
    ('*', 59): [('*', 58), ('+', 16)],
    ('*', 60): [('*', 59), ('-', 10)],
    ('*', 61): [('4', 37), ('^', 2)],
    ('*', 62): [('37', 40), ('^', 3)],
    ('*', 63): [('58', 43), ('^', 4)],
    ('*', 64): [('520', 46), ('^', 5)],
    ('*', 65): [('201', 49), ('^', 6)],
    ('*', 66): [('2156', 52), ('x', 53)],
    ('+', 14): [('x', 23), ('2', 24)],
    ('+', 15): [('x', 27), ('4', 28)],
    ('+', 16): [('x', 31), ('6', 32)],
    ('+', 17): [('^', 1), ('-', 12)],
    ('+', 18): [('+', 17), ('*', 64)],
    ('+', 19): [('+', 18), ('-', 13)],
    ('+', 20): [('+', 19), ('5040', 54)],
    ('-', 7): [('x', 21), ('1', 22)],
    ('-', 8): [('x', 25), ('3', 26)],
    ('-', 9): [('x', 29), ('5', 30)],
    ('-', 10): [('x', 33), ('7', 34)],
    ('-', 11): [('*', 61), ('*', 62)],
    ('-', 12): [('-', 11), ('*', 63)],
    ('-', 13): [('*', 65), ('*', 66)],
    ('=', 0): [('*', 60), ('+', 20)],
    ('^', 1): [('x', 35), ('7', 36)],
    ('^', 2): [('x', 38), ('6', 39)],
    ('^', 3): [('x', 41), ('5', 42)],
    ('^', 4): [('x', 44), ('4', 45)],
    ('^', 5): [('x', 47), ('3', 48)],
    ('^', 6): [('x', 50), ('2', 51)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((x + 2x^2 - 3)^2)((x^2 - x + 1)^3)((x^3 + 2x - 5)) = x^{10} + 4x^9 - 2x^8 - 41x^7 - 69x^6 + 142x^5 + 420x^4 - 567x^3 - 174x^2 + 185x - 75'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 76): [('^', 2), ('^', 4)],
    ('*', 77): [('*', 76), ('+', 26)],
    ('*', 78): [('2', 32), ('^', 1)],
    ('*', 79): [('2', 44), ('x', 45)],
    ('*', 80): [('4', 49), ('^', 7)],
    ('*', 81): [('2', 52), ('^', 8)],
    ('*', 82): [('41', 55), ('^', 9)],
    ('*', 83): [('69', 58), ('^', 10)],
    ('*', 84): [('142', 61), ('^', 11)],
    ('*', 85): [('420', 64), ('^', 12)],
    ('*', 86): [('567', 67), ('^', 13)],
    ('*', 87): [('174', 70), ('^', 14)],
    ('*', 88): [('185', 73), ('x', 74)],
    ('+', 24): [('x', 31), ('-', 15)],
    ('+', 25): [('-', 16), ('1', 40)],
    ('+', 26): [('^', 5), ('-', 17)],
    ('+', 27): [('^', 6), ('-', 20)],
    ('+', 28): [('+', 27), ('*', 84)],
    ('+', 29): [('+', 28), ('-', 22)],
    ('+', 30): [('+', 29), ('-', 23)],
    ('-', 15): [('*', 78), ('3', 35)],
    ('-', 16): [('^', 3), ('x', 39)],
    ('-', 17): [('*', 79), ('5', 46)],
    ('-', 18): [('*', 80), ('*', 81)],
    ('-', 19): [('-', 18), ('*', 82)],
    ('-', 20): [('-', 19), ('*', 83)],
    ('-', 21): [('*', 85), ('*', 86)],
    ('-', 22): [('-', 21), ('*', 87)],
    ('-', 23): [('*', 88), ('75', 75)],
    ('=', 0): [('*', 77), ('+', 30)],
    ('^', 1): [('x', 33), ('2', 34)],
    ('^', 2): [('+', 24), ('2', 36)],
    ('^', 3): [('x', 37), ('2', 38)],
    ('^', 4): [('+', 25), ('3', 41)],
    ('^', 5): [('x', 42), ('3', 43)],
    ('^', 6): [('x', 47), ('10', 48)],
    ('^', 7): [('x', 50), ('9', 51)],
    ('^', 8): [('x', 53), ('8', 54)],
    ('^', 9): [('x', 56), ('7', 57)],
    ('^', 10): [('x', 59), ('6', 60)],
    ('^', 11): [('x', 62), ('5', 63)],
    ('^', 12): [('x', 65), ('4', 66)],
    ('^', 13): [('x', 68), ('3', 69)],
    ('^', 14): [('x', 71), ('2', 72)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((x^2 + x - 1)^2)((x^3 - 2x + 4)^2)((x^2 + 3x - 7)) = x^{10} - 3x^9 - 20x^8 + 60x^7 + 161x^6 - 260x^5 - 385x^4 + 494x^3 + 509x^2 - 378x + 196'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 76): [('^', 2), ('^', 4)],
    ('*', 77): [('*', 76), ('+', 25)],
    ('*', 78): [('2', 38), ('x', 39)],
    ('*', 79): [('3', 44), ('x', 45)],
    ('*', 80): [('3', 49), ('^', 7)],
    ('*', 81): [('20', 52), ('^', 8)],
    ('*', 82): [('60', 55), ('^', 9)],
    ('*', 83): [('161', 58), ('^', 10)],
    ('*', 84): [('260', 61), ('^', 11)],
    ('*', 85): [('385', 64), ('^', 12)],
    ('*', 86): [('494', 67), ('^', 13)],
    ('*', 87): [('509', 70), ('^', 14)],
    ('*', 88): [('378', 73), ('x', 74)],
    ('+', 23): [('^', 1), ('-', 15)],
    ('+', 24): [('-', 16), ('4', 40)],
    ('+', 25): [('^', 5), ('-', 17)],
    ('+', 26): [('-', 19), ('*', 82)],
    ('+', 27): [('+', 26), ('-', 21)],
    ('+', 28): [('+', 27), ('*', 86)],
    ('+', 29): [('+', 28), ('-', 22)],
    ('+', 30): [('+', 29), ('196', 75)],
    ('-', 15): [('x', 33), ('1', 34)],
    ('-', 16): [('^', 3), ('*', 78)],
    ('-', 17): [('*', 79), ('7', 46)],
    ('-', 18): [('^', 6), ('*', 80)],
    ('-', 19): [('-', 18), ('*', 81)],
    ('-', 20): [('*', 83), ('*', 84)],
    ('-', 21): [('-', 20), ('*', 85)],
    ('-', 22): [('*', 87), ('*', 88)],
    ('=', 0): [('*', 77), ('+', 30)],
    ('^', 1): [('x', 31), ('2', 32)],
    ('^', 2): [('+', 23), ('2', 35)],
    ('^', 3): [('x', 36), ('3', 37)],
    ('^', 4): [('+', 24), ('2', 41)],
    ('^', 5): [('x', 42), ('2', 43)],
    ('^', 6): [('x', 47), ('10', 48)],
    ('^', 7): [('x', 50), ('9', 51)],
    ('^', 8): [('x', 53), ('8', 54)],
    ('^', 9): [('x', 56), ('7', 57)],
    ('^', 10): [('x', 59), ('6', 60)],
    ('^', 11): [('x', 62), ('5', 63)],
    ('^', 12): [('x', 65), ('4', 66)],
    ('^', 13): [('x', 68), ('3', 69)],
    ('^', 14): [('x', 71), ('2', 72)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '((x^2 + 2x^3 - 4)^3)((x^2 - x + 2)^2)((x^3 + 3x - 5)) = x^{15} + 8x^{14} - 14x^{13} - 191x^{12} + 48x^{11} + 1218x^{10} - 60x^9 - 2700x^8 - 1452x^7 + 4375x^6 + 3476x^5 - 2922x^4 - 1685x^3 + 655x^2 + 103x - 400'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 103): [('^', 3), ('^', 5)],
    ('*', 104): [('*', 103), ('+', 34)],
    ('*', 105): [('2', 44), ('^', 2)],
    ('*', 106): [('3', 56), ('x', 57)],
    ('*', 107): [('8', 61), ('^', 8)],
    ('*', 108): [('14', 64), ('^', 9)],
    ('*', 109): [('191', 67), ('^', 10)],
    ('*', 110): [('48', 70), ('^', 11)],
    ('*', 111): [('1218', 73), ('^', 12)],
    ('*', 112): [('60', 76), ('^', 13)],
    ('*', 113): [('2700', 79), ('^', 14)],
    ('*', 114): [('1452', 82), ('^', 15)],
    ('*', 115): [('4375', 85), ('^', 16)],
    ('*', 116): [('3476', 88), ('^', 17)],
    ('*', 117): [('2922', 91), ('^', 18)],
    ('*', 118): [('1685', 94), ('^', 19)],
    ('*', 119): [('655', 97), ('^', 20)],
    ('*', 120): [('103', 100), ('x', 101)],
    ('+', 32): [('^', 1), ('-', 21)],
    ('+', 33): [('-', 22), ('2', 52)],
    ('+', 34): [('^', 6), ('-', 23)],
    ('+', 35): [('^', 7), ('-', 25)],
    ('+', 36): [('+', 35), ('*', 110)],
    ('+', 37): [('+', 36), ('-', 28)],
    ('+', 38): [('+', 37), ('*', 115)],
    ('+', 39): [('+', 38), ('-', 30)],
    ('+', 40): [('+', 39), ('*', 119)],
    ('+', 41): [('+', 40), ('-', 31)],
    ('-', 21): [('*', 105), ('4', 47)],
    ('-', 22): [('^', 4), ('x', 51)],
    ('-', 23): [('*', 106), ('5', 58)],
    ('-', 24): [('*', 107), ('*', 108)],
    ('-', 25): [('-', 24), ('*', 109)],
    ('-', 26): [('*', 111), ('*', 112)],
    ('-', 27): [('-', 26), ('*', 113)],
    ('-', 28): [('-', 27), ('*', 114)],
    ('-', 29): [('*', 116), ('*', 117)],
    ('-', 30): [('-', 29), ('*', 118)],
    ('-', 31): [('*', 120), ('400', 102)],
    ('=', 0): [('*', 104), ('+', 41)],
    ('^', 1): [('x', 42), ('2', 43)],
    ('^', 2): [('x', 45), ('3', 46)],
    ('^', 3): [('+', 32), ('3', 48)],
    ('^', 4): [('x', 49), ('2', 50)],
    ('^', 5): [('+', 33), ('2', 53)],
    ('^', 6): [('x', 54), ('3', 55)],
    ('^', 7): [('x', 59), ('15', 60)],
    ('^', 8): [('x', 62), ('14', 63)],
    ('^', 9): [('x', 65), ('13', 66)],
    ('^', 10): [('x', 68), ('12', 69)],
    ('^', 11): [('x', 71), ('11', 72)],
    ('^', 12): [('x', 74), ('10', 75)],
    ('^', 13): [('x', 77), ('9', 78)],
    ('^', 14): [('x', 80), ('8', 81)],
    ('^', 15): [('x', 83), ('7', 84)],
    ('^', 16): [('x', 86), ('6', 87)],
    ('^', 17): [('x', 89), ('5', 90)],
    ('^', 18): [('x', 92), ('4', 93)],
    ('^', 19): [('x', 95), ('3', 96)],
    ('^', 20): [('x', 98), ('2', 99)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)



def test__newSymbolsLimitTheorem__sumRule(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = "\\lim_{x\\to\\bar{x}}{(f+g)(x)}=\\lim_{x\\to\\bar{x}}{f(x)}+\\lim_{x\\to\\bar{x}}{g(x)}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 25): [('+', 4), ('x', 16)],
    ('*', 26): [('f', 19), ('x', 20)],
    ('*', 27): [('g', 23), ('x', 24)],
    ('+', 4): [('f', 14), ('g', 15)],
    ('+', 5): [('lim', 8), ('lim', 10)],
    ('=', 3): [('lim', 6), ('+', 5)],
    ('\\to', 0): [('x', 12), ('bar', 7)],
    ('\\to', 1): [('x', 17), ('bar', 9)],
    ('\\to', 2): [('x', 21), ('bar', 11)],
    ('bar', 7): [('x', 13)],
    ('bar', 9): [('x', 18)],
    ('bar', 11): [('x', 22)],
    ('lim', 6): [('\\to', 0), ('*', 25)],
    ('lim', 8): [('\\to', 1), ('*', 26)],
    ('lim', 10): [('\\to', 2), ('*', 27)]}
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
    ('*', 24): [('lim', 6), ('lim', 8)],
    ('*', 25): [('f', 12), ('g', 13)],
    ('*', 26): [('f', 17), ('x', 18)],
    ('*', 27): [('g', 21), ('x', 22)],
    ('=', 3): [('lim', 4), ('*', 24)],
    ('\\to', 0): [('x', 10), ('bar', 5)],
    ('\\to', 1): [('x', 15), ('bar', 7)],
    ('\\to', 2): [('x', 19), ('bar', 9)],
    ('bar', 5): [('x', 11)],
    ('bar', 7): [('x', 16)],
    ('bar', 9): [('x', 20)],
    ('lim', 4): [('\\to', 0), ('*', 23)],
    ('lim', 6): [('\\to', 1), ('*', 26)],
    ('lim', 8): [('\\to', 2), ('*', 27)]}
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
    ('*', 19): [('c', 12), ('lim', 5)],
    ('*', 20): [('f', 15), ('x', 16)],
    ('=', 2): [('lim', 3), ('*', 19)],
    ('\\to', 0): [('x', 7), ('bar', 4)],
    ('\\to', 1): [('x', 13), ('bar', 6)],
    ('bar', 4): [('x', 8)],
    ('bar', 6): [('x', 14)],
    ('lim', 3): [('\\to', 0), ('*', 17)],
    ('lim', 5): [('\\to', 1), ('*', 20)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__newSymbolsLimitTheorem__quotientRule(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = "\\lim_{x\\to\\bar{x}}{(\\frac{f}{g})(x)}=\\frac{\\lim_{x\\to\\bar{x}}{f(x)}}{\\lim_{x\\to\\bar{x}}{g(x)}}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 25): [('/', 6), ('x', 16)],
    ('*', 26): [('f', 19), ('x', 20)],
    ('*', 27): [('g', 23), ('x', 24)],
    ('/', 6): [('f', 14), ('g', 15)],
    ('/', 7): [('lim', 8), ('lim', 10)],
    ('=', 3): [('lim', 4), ('/', 7)],
    ('\\to', 0): [('x', 12), ('bar', 5)],
    ('\\to', 1): [('x', 17), ('bar', 9)],
    ('\\to', 2): [('x', 21), ('bar', 11)],
    ('bar', 5): [('x', 13)],
    ('bar', 9): [('x', 18)],
    ('bar', 11): [('x', 22)],
    ('lim', 4): [('\\to', 0), ('*', 25)],
    ('lim', 8): [('\\to', 1), ('*', 26)],
    ('lim', 10): [('\\to', 2), ('*', 27)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)
#
def test__paveWayForDifferentiation__productRule(verbose=False):# TODO not entirely correct, have to group the \frac{d}{dx} together as one NODE
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{d}{dx}u v=u\\frac{dv}{dx}+v\\frac{du}{dx}'#the space between u v is important for this parser
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 15): [('/', 2), ('u', 7)],
    ('*', 16): [('*', 15), ('v', 8)],
    ('*', 17): [('u', 9), ('/', 3)],
    ('*', 18): [('v', 12), ('/', 4)],
    ('+', 1): [('*', 17), ('*', 18)],
    ('/', 2): [('d', 5), ('dx', 6)],
    ('/', 3): [('dv', 10), ('dx', 11)],
    ('/', 4): [('du', 13), ('dx', 14)],
    ('=', 0): [('*', 16), ('+', 1)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__paveWayForDifferentiation__sumRule(verbose=False):# TODO not entirely correct, have to group the \frac{d}{dx} together as one NODE
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\frac{d}{dx}(u+v)=\\frac{du}{dx}+\\frac{dv}{dx}'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 14): [('/', 3), ('+', 1)],
    ('+', 1): [('u', 8), ('v', 9)],
    ('+', 2): [('/', 4), ('/', 5)],
    ('/', 3): [('d', 6), ('dx', 7)],
    ('/', 4): [('du', 10), ('dx', 11)],
    ('/', 5): [('dv', 12), ('dx', 13)],
    ('=', 0): [('*', 14), ('+', 2)]}
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
    ('*', 25): [('-', 3), ('+', 6)],
    ('*', 26): [('int', 8), ('dx', 14)],
    ('*', 27): [('/', 9), ('^', 1)],
    ('*', 28): [('3', 19), ('^', 2)],
    ('*', 29): [('3', 22), ('x', 23)],
    ('+', 6): [('x', 12), ('1', 13)],
    ('+', 7): [('-', 5), ('C', 24)],
    ('-', 3): [('x', 10), ('3', 11)],
    ('-', 4): [('*', 27), ('*', 28)],
    ('-', 5): [('-', 4), ('*', 29)],
    ('/', 9): [('1', 15), ('3', 16)],
    ('=', 0): [('*', 26), ('+', 7)],
    ('^', 1): [('x', 17), ('3', 18)],
    ('^', 2): [('x', 20), ('2', 21)],
    ('int', 8): [('*', 25)]}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_ast == parser.ast)
    if verbose:
        pp.pprint(parser.ast)


def test__paveWayForIntegrtion__exponentOnEnclosingNonBackslash(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '\\int{(x-1)(x+1)^2}dx=\\frac{1}{4}x^4+\\frac{1}{3}x^3-\\frac{1}{2}x^2-x+C'
    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_ast = {
    ('*', 35): [('-', 5), ('^', 1)],
    ('*', 36): [('int', 11), ('dx', 20)],
    ('*', 37): [('/', 12), ('^', 2)],
    ('*', 38): [('/', 13), ('^', 3)],
    ('*', 39): [('/', 14), ('^', 4)],
    ('+', 8): [('x', 17), ('1', 18)],
    ('+', 9): [('*', 37), ('-', 7)],
    ('+', 10): [('+', 9), ('C', 34)],
    ('-', 5): [('x', 15), ('1', 16)],
    ('-', 6): [('*', 38), ('*', 39)],
    ('-', 7): [('-', 6), ('x', 33)],
    ('/', 12): [('1', 21), ('4', 22)],
    ('/', 13): [('1', 25), ('3', 26)],
    ('/', 14): [('1', 29), ('2', 30)],
    ('=', 0): [('*', 36), ('+', 10)],
    ('^', 1): [('+', 8), ('2', 19)],
    ('^', 2): [('x', 23), ('4', 24)],
    ('^', 3): [('x', 27), ('3', 28)],
    ('^', 4): [('x', 31), ('2', 32)],
    ('int', 11): [('*', 35)]}
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
    test__paveWayForDifferentiation__productRule()
    test__paveWayForDifferentiation__sumRule()
    test__paveWayForIntegration__enclosingBracketNonBackslash()
    test__paveWayForIntegrtion__exponentOnEnclosingNonBackslash()
    #matrix test cases
    test__matrix__determinantMetricTensor(True)
    #Test Metric_Tensor? Good for Mechanical Engineering later :)