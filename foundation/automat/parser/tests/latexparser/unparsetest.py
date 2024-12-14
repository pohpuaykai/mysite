import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser


def test__contiguousLeftOvers__decimalPlaces(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('+', 5): [('-', 3), ('1.0', 6)],
    ('-', 3): [('0', 2), ('0.5', 4)],
    ('=', 0): [('+', 5), ('0.5', 1)]}

    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '-0.5+1.0=0.5'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)



def test__collateBackslashInfixLeftOversToContiguous__exponentialOverMultiply(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 2): [('3', 1), ('^', 4)],
    ('*', 6): [('*', 2), ('^', 8)],
    ('*', 11): [('3', 10), ('^', 13)],
    ('=', 0): [('*', 11), ('*', 6)],
    ('^', 4): [('x', 3), ('2', 5)],
    ('^', 8): [('x', 7), ('7', 9)],
    ('^', 13): [('x', 12), ('9', 14)]}

    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '3x^9=3x^2x^7'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)



def test__interLevelSubTreeGrafting__exponentialOverEnclosingBrackets(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 3): [('19', 2), ('y', 4)],
    ('*', 11): [('4', 10), ('^', 13)],
    ('+', 5): [('*', 3), ('^', 7)],
    ('+', 9): [('+', 5), ('*', 11)],
    ('=', 0): [('^', 15), ('F', 1)],
    ('^', 7): [('z', 6), ('4', 8)],
    ('^', 13): [('w', 12), ('12', 14)],
    ('^', 15): [('+', 9), ('30', 16)]}

    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '(19y+z^4+4w^{12})^{30}=F'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__schemeToLatex__variablesWithCurlyBrackets(verbose=False):#TODO add to parser....and handle
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 2): [('I_{ES}', 3), ('-', 4)],
    ('-', 4): [('^', 5), ('1', 6)],
    ('/', 8): [('V_{BE}', 9), ('V_T', 10)],
    ('=', 0): [('I_E', 1), ('*', 2)],
    ('^', 5): [('e', 7), ('/', 8)]}

    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'I_E =I_{ES} (e^{\\frac{V_{BE} }{V_T}}-1)'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__findingBackSlashAndInfixOperations__Trig0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 4): [('2', 3), ('sin', 5)],
    ('*', 6): [('*', 4), ('cos', 7)],
    ('*', 14): [('2', 13), ('x_0', 15)],
    ('-', 2): [('0', 1), ('*', 6)],
    ('-', 9): [('0', 8), ('sin', 10)],
    ('=', 0): [('-', 9), ('-', 2)],
    ('cos', 7): [('x_0', 12)],
    ('sin', 5): [('x_0', 11)],
    ('sin', 10): [('*', 14)]}

    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '-\\sin(2x_0)=-2\\sin(x_0)\\cos(x_0)'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__findingBackSlashAndInfixOperations__Trig1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('+', 3): [('^', 10), ('^', 9)],
    ('=', 0): [('+', 3), ('1', 1)],
    ('^', 9): [('cos', 4), ('2', 7)],
    ('^', 10): [('sin', 2), ('2', 6)],
    ('cos', 4): [('x', 8)],
    ('sin', 2): [('x', 5)]}

    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\sin^2(x)+\\cos^2(x)=1'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__findingBackSlashAndInfixOperations__Trig2(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('+', 3): [('^', 10), ('^', 9)],
    ('=', 0): [('+', 3), ('1', 1)],
    ('^', 9): [('cos', 4), ('2', 5)],
    ('^', 10): [('sin', 2), ('2', 7)],
    ('cos', 4): [('x', 6)],
    ('sin', 2): [('x', 8)]}

    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\sin^2(x)+\\cos^2(x)=1'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)



def test__findingBackSlashAndInfixOperations__Sqrt0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {('=', 0): [('nroot', 1), ('2', 2)], ('nroot', 1): [(2, 4), ('4', 3)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\sqrt{4}=2'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__findingBackSlashAndInfixOperations__Sqrt1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {('=', 0): [('nroot', 2), ('2', 1)], ('nroot', 2): [('3', 3), ('9', 4)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\sqrt[3]{9}=2'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)



def test__findingBackSlashAndInfixOperations__Ln(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {('=', 0): [('log', 2), ('1', 1)], ('log', 2): [('e', 4), ('e', 3)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\ln(e)=1'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)



def test__findingBackSlashAndInfixOperations__Frac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('/', 1): [('1000', 4), ('2000', 3)],
    ('/', 2): [('12', 6), ('24', 5)],
    ('=', 0): [('/', 2), ('/', 1)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\frac{12}{24}=\\frac{1000}{2000}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__findingBackSlashAndInfixOperations__Log0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('=', 0): [('log', 2), ('12', 1)],
    ('log', 2): [('12', 4), ('8916100448256', 3)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\log_{12}(8916100448256)=12'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__findingBackSlashAndInfixOperations__Log1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {('=', 0): [('log', 1), ('2', 2)], ('log', 1): [(10, 4), ('100', 3)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\log(100)=2'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__findingBackSlashAndInfixOperations__tildeVariable(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {('=', 0): [('tilde', 1), ('2', 2)], ('tilde', 1): [('x', 3)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\tilde{x}=2'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__findingBackSlashAndInfixOperations__SchrodingerWaveEquation(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 2): [('widehat', 1), ('Psi', 3)],
    ('*', 5): [('widehat', 4), ('Psi', 6)],
    ('=', 0): [('*', 5), ('*', 2)],
    ('widehat', 1): [('E', 7)],
    ('widehat', 4): [('H', 8)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\widehat{H}\\Psi=\\widehat{E}\\Psi'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__infixInBackslash__paraboloid(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('+', 6): [('^', 4), ('^', 8)],
    ('=', 0): [('z', 2), ('nroot', 1)],
    ('^', 4): [('x', 3), ('2', 5)],
    ('^', 8): [('y', 7), ('2', 9)],
    ('nroot', 1): [(2, 10), ('+', 6)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'z=\\sqrt{x^2+y^2}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__sqrtWithPowerCaretRightOtherInfix__hill(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('+', 8): [('^', 6), ('^', 10)],
    ('-', 2): [('0', 1), ('nroot', 3)],
    ('=', 0): [('z', 4), ('-', 2)],
    ('^', 6): [('x', 5), ('2', 7)],
    ('^', 10): [('y', 9), ('2', 11)],
    ('nroot', 3): [('2', 12), ('+', 8)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'z=-\\sqrt{x^2+y^2}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__nonInfixBrackets__addImplicitMultiply(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 9): [('+', 3), ('+', 15)],
    ('+', 3): [('1', 2), ('+', 5)],
    ('+', 5): [('1', 4), ('+', 7)],
    ('+', 7): [('1', 6), ('1', 8)],
    ('+', 11): [('1', 10), ('1', 12)],
    ('+', 13): [('+', 11), ('1', 14)],
    ('+', 15): [('+', 13), ('1', 16)],
    ('=', 0): [('*', 9), ('16', 1)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '(1+1+1+1)(1+1+1+1)=16'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__nonInfixBrackets__addImplicitMultiply0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 6): [('+', 4), ('+', 8)],
    ('+', 2): [('1', 1), ('*', 6)],
    ('+', 4): [('1', 3), ('1', 5)],
    ('+', 8): [('1', 7), ('1', 9)],
    ('+', 10): [('+', 2), ('1', 11)],
    ('+', 12): [('+', 10), ('1', 13)],
    ('=', 0): [('+', 12), ('7', 14)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '1+(1+1)(1+1)+1+1=7'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__nonInfixBrackets__addImplicitMultiply1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 9): [('+', 3), ('+', 15)],
    ('+', 3): [('1', 2), ('+', 5)],
    ('+', 5): [('1', 4), ('+', 7)],
    ('+', 7): [('1', 6), ('1', 8)],
    ('+', 11): [('1', 10), ('1', 12)],
    ('+', 13): [('+', 11), ('1', 14)],
    ('+', 15): [('+', 13), ('1', 16)],
    ('+', 17): [('*', 9), ('1', 18)],
    ('+', 19): [('+', 17), ('1', 20)],
    ('=', 0): [('+', 19), ('18', 1)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '(1+1+1+1)(1+1+1+1)+1+1=18'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__BODMAS__priorityBetweenInfixForBrackets(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 6): [('-', 4), ('+', 8)],
    ('+', 8): [('x', 7), ('1', 9)],
    ('-', 4): [('x', 3), ('1', 5)],
    ('/', 2): [('2', 10), ('*', 6)],
    ('=', 0): [('/', 2), ('c', 1)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\frac{2}{(x-1)(x+1)}=c'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__BODMAS__enclosingBracketInBackslashArg(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 8): [('-', 6), ('+', 10)],
    ('+', 10): [('x', 9), ('1', 11)],
    ('+', 19): [('x', 18), ('1', 20)],
    ('-', 3): [('/', 2), ('/', 4)],
    ('-', 6): [('x', 5), ('1', 7)],
    ('-', 15): [('x', 14), ('1', 16)],
    ('/', 1): [('2', 12), ('*', 8)],
    ('/', 2): [('1', 13), ('-', 15)],
    ('/', 4): [('1', 17), ('+', 19)],
    ('=', 0): [('/', 1), ('-', 3)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\frac{2}{(x-1)(x+1)}=\\frac{1}{x-1}-\\frac{1}{x+1}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__BODMAS__enclosingBracketInBackslashArgWithExponent(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('-', 4): [('x', 3), ('3', 5)],
    ('=', 0): [('c', 2), ('sin', 1)],
    ('^', 6): [('-', 4), ('2', 7)],
    ('sin', 1): [('^', 6)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'c=\\sin((x-3)^2)'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__BODMAS__enclosingBracketInBackslashArgImplicitZero(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 8): [('-', 6), ('+', 10)],
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
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\frac{2}{(x-1)(x+1)}=\\frac{1}{x-1}+\\frac{-1}{x+1}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__BODMAS__enclosingBracket(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 6): [('6', 5), ('x', 7)],
    ('+', 8): [('-', 4), ('9', 9)],
    ('-', 4): [('^', 2), ('*', 6)],
    ('-', 11): [('x', 10), ('3', 12)],
    ('=', 0): [('+', 8), ('^', 13)],
    ('^', 2): [('x', 1), ('2', 3)],
    ('^', 13): [('-', 11), ('2', 14)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'x^2-6x+9=(x-3)^2'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__manyFracCaretEnclosingBrac__partialFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 13): [('-', 11), ('^', 17)],
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
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\frac{x^2}{(x-2)(x-3)^2}=\\frac{4}{x-2}+\\frac{-3}{x-3}+\\frac{9}{(x-3)^2}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__fracWithLogNoBase__changeLogBaseFormula(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('/', 1): [('log', 4), ('log', 3)],
    ('=', 0): [('log', 2), ('/', 1)],
    ('log', 2): [('b', 5), ('a', 6)],
    ('log', 3): [('c', 8), ('b', 7)],
    ('log', 4): [('c', 10), ('a', 9)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\log_b(a)=\\frac{\\log_c(a)}{\\log_c(b)}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__backslashInfixInBackslash__sqrtInSqrt(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('/', 5): [('pi', 9), ('22', 8)],
    ('=', 0): [('nroot', 2), ('F', 1)],
    ('nroot', 2): [('nroot', 3), ('nroot', 4)],
    ('nroot', 3): [(2, 11), ('/', 5)],
    ('nroot', 4): [('sin', 7), ('pi', 6)],
    ('sin', 7): [('pi', 10)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\sqrt[\\sqrt{\\frac{\\pi }{22}}]{\\sqrt[\\sin(\\pi )]{\\pi}}=F'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__backslashInfixInBackslash__trigInTrig(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
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
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\sin^{20-\\cos^{43}(1-\\frac{\\pi }{5})}(9-\\tan^4(\\theta))+5=F'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__backslashInfixInBackslash__logInLog(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('-', 9): [('90', 8), ('x', 10)],
    ('=', 0): [('log', 2), ('F', 1)],
    ('^', 6): [('z', 5), ('5', 7)],
    ('log', 2): [('log', 4), ('log', 3)],
    ('log', 3): [(10, 11), ('^', 6)],
    ('log', 4): [('e', 12), ('-', 9)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\log_{\\ln(90-x)}(\\log(z^5))=F'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__backslashInfixInBackslash__fracInFrac(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
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
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\frac{\\frac{\\sin^2(x)+\\cos^2(x)}{\\sin^2(x)-\\cos^2(x)}}{\\frac{\\cos(2x)-\\sin(2x)}{\\cos(2x)+\\sin(2x)}}=F'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__highPowersAndRandomCoefficientsPITEST(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 2): [('P', 1), ('x', 3)],
    ('*', 5): [('7', 4), ('^', 7)],
    ('*', 11): [('3', 10), ('^', 13)],
    ('*', 17): [('5', 16), ('^', 19)],
    ('*', 23): [('nroot', 22), ('^', 25)],
    ('*', 29): [('pi', 28), ('^', 31)],
    ('+', 15): [('-', 9), ('-', 21)],
    ('+', 27): [('+', 15), ('-', 33)],
    ('-', 9): [('*', 5), ('*', 11)],
    ('-', 21): [('*', 17), ('*', 23)],
    ('-', 33): [('*', 29), ('42', 34)],
    ('=', 0): [('*', 2), ('+', 27)],
    ('^', 7): [('x', 6), ('13', 8)],
    ('^', 13): [('x', 12), ('9', 14)],
    ('^', 19): [('x', 18), ('8', 20)],
    ('^', 25): [('x', 24), ('4', 26)],
    ('^', 31): [('x', 30), ('2', 32)],
    ('nroot', 22): [(2, 36), ('2', 35)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'Px=7x^{13}-3x^9+5x^8-\\sqrt{2}x^4+\\pi x^2-42'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__nestedPolynomial(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 6): [('2', 5), ('^', 8)],
    ('*', 12): [('5', 11), ('x', 13)],
    ('*', 26): [('3', 25), ('^', 28)],
    ('*', 31): [('Q', 30), ('x', 32)],
    ('+', 10): [('-', 4), ('-', 14)],
    ('+', 24): [('^', 22), ('*', 26)],
    ('-', 4): [('^', 2), ('*', 6)],
    ('-', 14): [('*', 12), ('7', 15)],
    ('-', 18): [('^', 16), ('+', 24)],
    ('-', 20): [('x', 19), ('1', 21)],
    ('=', 0): [('*', 31), ('-', 18)],
    ('^', 2): [('x', 1), ('3', 3)],
    ('^', 8): [('x', 7), ('2', 9)],
    ('^', 16): [('+', 10), ('2', 17)],
    ('^', 22): [('-', 20), ('3', 23)],
    ('^', 28): [('x', 27), ('21', 29)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'Qx=(x^3-2x^2+5x-7)^2-(x-1)^3+3x^{21}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__nonIntegerAndNegativeCoefficientsDECIMALPOINTTEST(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 2): [('R', 1), ('x', 3)],
    ('*', 7): [('0.5', 6), ('^', 9)],
    ('*', 13): [('3.14', 12), ('^', 15)],
    ('*', 19): [('/', 18), ('^', 21)],
    ('*', 25): [('1.618', 24), ('^', 27)],
    ('+', 11): [('-', 5), ('-', 17)],
    ('+', 23): [('+', 11), ('-', 29)],
    ('-', 5): [('0', 4), ('*', 7)],
    ('-', 17): [('*', 13), ('*', 19)],
    ('-', 29): [('*', 25), ('/', 30)],
    ('/', 18): [('2', 31), ('3', 32)],
    ('/', 30): [('1', 33), ('x', 34)],
    ('=', 0): [('*', 2), ('+', 23)],
    ('^', 9): [('x', 8), ('10', 10)],
    ('^', 15): [('x', 14), ('8', 16)],
    ('^', 21): [('x', 20), ('5', 22)],
    ('^', 27): [('x', 26), ('3', 28)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'Rx=-0.5x^{10}+3.14x^8-\\frac{2}{3}x^5+1.618x^3-\\frac{1}{x}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__mixedVariablesAndPowersPOWERCOTEVARIABLEDOUBLEVARIABLETEST(verbose=False):#TODO does not handle S(x, y) very well.
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 2): [('S', 1), ('*', 4)],
    ('*', 4): [('x,', 3), ('y', 5)],
    ('*', 9): [('^', 7), ('^', 11)],
    ('*', 15): [('7', 14), ('^', 17)],
    ('*', 19): [('*', 15), ('^', 21)],
    ('*', 25): [('2', 24), ('^', 27)],
    ('*', 37): [('^', 35), ('y', 38)],
    ('+', 23): [('-', 13), ('-', 29)],
    ('+', 33): [('+', 23), ('-', 39)],
    ('-', 13): [('*', 9), ('*', 19)],
    ('-', 29): [('*', 25), ('^', 31)],
    ('-', 39): [('*', 37), ('4', 40)],
    ('=', 0): [('*', 2), ('+', 33)],
    ('^', 7): [('x', 6), ('5', 8)],
    ('^', 11): [('y', 10), ('4', 12)],
    ('^', 17): [('x', 16), ('3', 18)],
    ('^', 21): [('y', 20), ('2', 22)],
    ('^', 27): [('x', 26), ('2', 28)],
    ('^', 31): [('y', 30), ('3', 32)],
    ('^', 35): [('x', 34), ('2', 36)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'S\\x, y=x^5y^4-7x^3y^2+2x^2-y^3+x^2y-4' # TODO ugly
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__irrationalAndTranscendentalNumbersPOWERCOTEBACKSLASH(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 2): [('T', 1), ('x', 3)],
    ('*', 9): [('cos', 8), ('^', 11)],
    ('*', 17): [('^', 15), ('sin', 18)],
    ('+', 13): [('-', 7), ('-', 19)],
    ('+', 26): [('^', 24), ('1', 27)],
    ('-', 7): [('^', 5), ('*', 9)],
    ('-', 19): [('*', 17), ('log', 20)],
    ('=', 0): [('*', 2), ('+', 13)],
    ('^', 5): [('e', 4), ('x', 6)],
    ('^', 11): [('x', 10), ('4', 12)],
    ('^', 15): [('x', 14), ('3', 16)],
    ('^', 24): [('x', 23), ('2', 25)],
    ('cos', 8): [('x', 21)],
    ('log', 20): [('e', 28), ('+', 26)],
    ('sin', 18): [('x', 22)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = 'Tx=e^x-\\cos(x)x^4+x^3\\sin(x)-\\ln(x^2+1)'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__degree5(verbose=False):#TODO ugly.... ?
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 6): [('3', 5), ('^', 8)],
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
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '(x-1)(x+2)(x-3)(x+4)(x-5)=(x^5-3x^4)-(32x^3)+94x^2+31x-120'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__degree6(verbose=False):#TODO ugly
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
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
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '(x-1)(x-2)(x+3)(x+4)(x-5)(x+6)=x^6+(5x^5-35x^4)-(75x^3)+368x^2+246x-720'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__degree7(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = None # need to wait for parsetest...
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '(x - 1)(x + 2)(x - 3)(x + 4)(x - 5)(x + 6)(x - 7) = x^7 + 4x^6 - 37x^5 - 58x^4 + 520x^3 + 201x^2 - 2156x + 5040'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = None # need to wait for parsetest...
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '((x + 2x^2 - 3)^2)((x^2 - x + 1)^3)((x^3 + 2x - 5)) = x^{10} + 4x^9 - 2x^8 - 41x^7 - 69x^6 + 142x^5 + 420x^4 - 567x^3 - 174x^2 + 185x - 75'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm0(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = None # need to wait for parsetest...
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '((x^2 + x - 1)^2)((x^3 - 2x + 4)^2)((x^2 + 3x - 7)) = x^{10} - 3x^9 - 20x^8 + 60x^7 + 161x^6 - 260x^5 - 385x^4 + 494x^3 + 509x^2 - 378x + 196'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm1(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = None # need to wait for parsetest...
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '((x^2 + 2x^3 - 4)^3)((x^2 - x + 2)^2)((x^3 + 3x - 5)) = x^{15} + 8x^{14} - 14x^{13} - 191x^{12} + 48x^{11} + 1218x^{10} - 60x^9 - 2700x^8 - 1452x^7 + 4375x^6 + 3476x^5 - 2922x^4 - 1685x^3 + 655x^2 + 103x - 400'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)



#
def test__paveWayForDifferentiation__productRule(verbose=False):#TODO ugly
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   
    ('*', 2): [('/', 1), ('uv', 3)],
    ('*', 5): [('u', 4), ('/', 6)],
    ('*', 9): [('v', 8), ('/', 10)],
    ('+', 7): [('*', 5), ('*', 9)],
    ('/', 1): [('d', 12), ('dx', 11)],
    ('/', 6): [('dv', 16), ('dx', 15)],
    ('/', 10): [('du', 14), ('dx', 13)],
    ('=', 0): [('*', 2), ('+', 7)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\frac{d}{\\dx}\\uv=u\\frac{\\dv }{\\dx}+v\\frac{\\du }{\\dx}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__paveWayForDifferentiation__sumRule(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 2): [('/', 1), ('+', 4)],
    ('+', 4): [('u', 3), ('v', 5)],
    ('+', 7): [('/', 6), ('/', 8)],
    ('/', 1): [('d', 10), ('dx', 9)],
    ('/', 6): [('du', 12), ('dx', 11)],
    ('/', 8): [('dv', 14), ('dx', 13)],
    ('=', 0): [('*', 2), ('+', 7)]}
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\frac{d}{\\dx}(u+v)=\\frac{\\du }{\\dx}+\\frac{\\dv }{\\dx}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__paveWayForIntegration__enclosingBracketNonBackslash(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('*', 2): [('int', 1), ('dx', 3)],
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
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\int{(x-3)(x+1)}\\dx=(\\frac{1}{3}x^3-3x^2)-(3x)+C'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


def test__paveWayForIntegrtion__exponentOnEnclosingNonBackslash(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = None # waiting for parsertest
    parser = Latexparser(ast=ast, verbose=verbose)
    eqsStr = parser._unparse()
    expected_eqsStr = '\\int{(x-1)(x+1)^2}dx=\\frac{1}{4}x^4+\\frac{1}{3}x^3-\\frac{1}{2}x^2-x+C'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == eqsStr)
    if verbose:
        print(eqsStr)


if __name__=='__main__':
    test__contiguousLeftOvers__decimalPlaces()
    test__collateBackslashInfixLeftOversToContiguous__exponentialOverMultiply()
    test__interLevelSubTreeGrafting__exponentialOverEnclosingBrackets()
    test__schemeToLatex__variablesWithCurlyBrackets()
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
    # test__hassliche__degree7(True) # not tested yet, use nDisplay to help please
    # test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm(True) # not tested yet, use nDisplay to help please
    # test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm0(True) # not tested yet, use nDisplay to help please
    # test__hassliche__moreThanOneAdditiveTermInEachMultiplicativeTerm1(True) # not tested yet, use nDisplay to help please
    # test__paveWayForDifferentiation__productRule(True) # not tested yet =>  UGLY differentiation, functions u and v... (same problem as S(x, y))
    # test__paveWayForDifferentiation__sumRule(True)  # not tested yet =>  UGLY differentiation, functions u and v... (same problem as S(x, y))
    # test__paveWayForIntegration__enclosingBracketNonBackslash(True) # not tested yet =>  UGLY differentiation, functions u and v... (same problem as S(x, y))
    # test__paveWayForIntegrtion__exponentOnEnclosingNonBackslash(True) # not tested yet << still throws, TODO refactor brackslash args into a list, ... and the rest of the code...