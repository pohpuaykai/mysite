import inspect
import pprint

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


def test__moreThan1Op__seriesResistance0(verbose=False):
    latexEq = 'R_1=R_2+R_3'
    subject = 'R_2'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'R_1-R_3=R_2' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '+',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('-', 0): [('R_1', 2), ('R_3', 6)],
                         ('=', 1): [('-', 0), ('R_2', 4)]},
        'resultLatexStr': 'R_1-R_3=R_2',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= (- R_1 R_3) R_2)',
        'resultVariables': ['R_1', 'R_3', 'R_2'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__seriesResistance1(verbose=False):
    latexEq = 'R_1=R_2+R_3'
    subject = 'R_3'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'R_1-R_2=R_3' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '+',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('-', 0): [('R_1', 2), ('R_2', 4)],
                         ('=', 1): [('-', 0), ('R_3', 6)]},
        'resultLatexStr': 'R_1-R_2=R_3',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= (- R_1 R_2) R_3)',
        'resultVariables': ['R_1', 'R_2', 'R_3'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)


def test__moreThan1Op__parallelResistance0(verbose=False):
    latexEq = '\\frac{1}{R_1}=\\frac{1}{R_2}+\\frac{1}{R_3}'
    subject = 'R_1'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'R_1=\\frac{1}{\\frac{1}{R_2}+\\frac{1}{R_3}}' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '/',
        'id': 1,
        'lastId': 4,
        'resultAST': {   ('+', 0): [('/', 2), ('/', 3)],
                         ('/', 1): [('1', 5), ('+', 0)],
                         ('/', 2): [('1', 8), ('R_2', 9)],
                         ('/', 3): [('1', 11), ('R_3', 12)],
                         ('=', 4): [('R_1', 6), ('/', 1)]},
        'resultLatexStr': 'R_1=\\frac{1}{\\frac{1}{R_2}+\\frac{1}{R_3}}',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= R_1 (/ 1 (+ (/ 1 R_2) (/ 1 R_3))))',
        'resultVariables': ['R_1', 'R_2', 'R_3'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__parallelResistance1(verbose=False):
    latexEq = '\\frac{1}{R_1}=\\frac{1}{R_2}+\\frac{1}{R_3}'
    subject = 'R_2'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{1}{\\frac{1}{R_1}-\\frac{1}{R_3}}=R_2' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '/',
        'id': 2,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('/', 1), ('/', 3)],
                         ('/', 1): [('1', 5), ('R_1', 6)],
                         ('/', 2): [('1', 8), ('-', 0)],
                         ('/', 3): [('1', 11), ('R_3', 12)],
                         ('=', 4): [('/', 2), ('R_2', 9)]},
        'resultLatexStr': '\\frac{1}{\\frac{1}{R_1}-\\frac{1}{R_3}}=R_2',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (/ 1 (- (/ 1 R_1) (/ 1 R_3))) R_2)',
        'resultVariables': ['R_1', 'R_3', 'R_2'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('/', 1), ('/', 3)],
                         ('/', 1): [('1', 5), ('R_1', 6)],
                         ('/', 2): [('1', 8), ('R_2', 9)],
                         ('/', 3): [('1', 11), ('R_3', 12)],
                         ('=', 4): [('-', 0), ('/', 2)]},
        'resultLatexStr': '\\frac{1}{R_1}-\\frac{1}{R_3}=\\frac{1}{R_2}',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (- (/ 1 R_1) (/ 1 R_3)) (/ 1 R_2))',
        'resultVariables': ['R_1', 'R_3', 'R_2'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__parallelResistance2(verbose=False):
    latexEq = '\\frac{1}{R_1}=\\frac{1}{R_2}+\\frac{1}{R_3}'
    subject = 'R_3'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{1}{\\frac{1}{R_1}-\\frac{1}{R_2}}=R_3' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '/',
        'id': 3,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('/', 1), ('/', 2)],
                         ('/', 1): [('1', 5), ('R_1', 6)],
                         ('/', 2): [('1', 8), ('R_2', 9)],
                         ('/', 3): [('1', 11), ('-', 0)],
                         ('=', 4): [('/', 3), ('R_3', 12)]},
        'resultLatexStr': '\\frac{1}{\\frac{1}{R_1}-\\frac{1}{R_2}}=R_3',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (/ 1 (- (/ 1 R_1) (/ 1 R_2))) R_3)',
        'resultVariables': ['R_1', 'R_2', 'R_3'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('/', 1), ('/', 2)],
                         ('/', 1): [('1', 5), ('R_1', 6)],
                         ('/', 2): [('1', 8), ('R_2', 9)],
                         ('/', 3): [('1', 11), ('R_3', 12)],
                         ('=', 4): [('-', 0), ('/', 3)]},
        'resultLatexStr': '\\frac{1}{R_1}-\\frac{1}{R_2}=\\frac{1}{R_3}',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (- (/ 1 R_1) (/ 1 R_2)) (/ 1 R_3))',
        'resultVariables': ['R_1', 'R_2', 'R_3'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__ohmPowerLaw0(verbose=False): # TODO nroot of even power, so include +-
    latexEq = 'P=\\frac{V^2}{R}'
    subject = 'V'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\sqrt{PR}=V' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '^',
        'id': 0,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('P', 3), ('R', 6)],
                         ('=', 2): [('nroot', 0), ('V', 4)],
                         ('nroot', 0): [('2', 5), ('*', 1)]},
        'resultLatexStr': '\\sqrt{PR}=V',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (nroot 2 (* P R)) V)',
        'resultVariables': ['P', 'R', 'V'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('P', 3), ('R', 6)],
                         ('=', 2): [('*', 1), ('^', 0)],
                         ('^', 0): [('V', 4), ('2', 5)]},
        'resultLatexStr': 'PR=V^2',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (* P R) (^ V 2))',
        'resultVariables': ['P', 'R', 'V'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__ohmPowerLaw1(verbose=False):
    latexEq = 'P=\\frac{V^2}{R}'
    subject = 'R'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{V^2}{P}=R' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('/', 1): [('^', 0), ('P', 3)],
                         ('=', 2): [('/', 1), ('R', 6)],
                         ('^', 0): [('V', 4), ('2', 5)]},
        'resultLatexStr': '\\frac{V^2}{P}=R',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (/ (^ V 2) P) R)',
        'resultVariables': ['V', 'P', 'R'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__ohmPowerLaw2(verbose=False): # TODO nroot of even power, so include +-
    latexEq = 'P=I^2R'
    subject = 'I'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\sqrt{\\frac{P}{R}}=I' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '^',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('/', 6): [('P', 2), ('R', 5)],
                         ('=', 1): [('nroot', 0), ('I', 3)],
                         ('nroot', 0): [('2', 4), ('/', 6)]},
        'resultLatexStr': '\\sqrt{\\frac{P}{R}}=I',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= (nroot 2 (/ P R)) I)',
        'resultVariables': ['P', 'R', 'I'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 6,
        'lastId': 1,
        'resultAST': {   ('/', 6): [('P', 2), ('R', 5)],
                         ('=', 1): [('/', 6), ('^', 0)],
                         ('^', 0): [('I', 3), ('2', 4)]},
        'resultLatexStr': '\\frac{P}{R}=I^2',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= (/ P R) (^ I 2))',
        'resultVariables': ['P', 'R', 'I'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__ohmPowerLaw3(verbose=False):
    latexEq = 'P=I^2R'
    subject = 'R'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{P}{I^2}=R' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '*',
        'id': 6,
        'lastId': 1,
        'resultAST': {   ('/', 6): [('P', 2), ('^', 0)],
                         ('=', 1): [('/', 6), ('R', 5)],
                         ('^', 0): [('I', 3), ('2', 4)]},
        'resultLatexStr': '\\frac{P}{I^2}=R',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= (/ P (^ I 2)) R)',
        'resultVariables': ['P', 'I', 'R'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__transistorOhmLaw0(verbose=False):
    latexEq = 'I_B=\\frac{V_B-V_{BE}}{R_B}'
    subject = 'V_B'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'I_B R_B+V_{BE}=V_B' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '-',
        'id': 0,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('I_B', 3), ('R_B', 9)],
                         ('+', 0): [('*', 1), ('V_{BE}', 7)],
                         ('=', 2): [('+', 0), ('V_B', 5)]},
        'resultLatexStr': 'I_BR_B+V_{BE}=V_B',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (+ (* I_B R_B) V_{BE}) V_B)',
        'resultVariables': ['I_B', 'R_B', 'V_{BE}', 'V_B'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('I_B', 3), ('R_B', 9)],
                         ('-', 0): [('V_B', 5), ('V_{BE}', 7)],
                         ('=', 2): [('*', 1), ('-', 0)]},
        'resultLatexStr': 'I_BR_B=V_B-V_{BE}',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (* I_B R_B) (- V_B V_{BE}))',
        'resultVariables': ['I_B', 'R_B', 'V_B', 'V_{BE}'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)


def test__moreThan1Op__transistorOhmLaw1(verbose=False):
    latexEq = 'I_B=\\frac{V_B-V_{BE}}{R_B}'
    subject = 'V_{BE}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'V_B -I_B R_B=V_{BE}' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '-',
        'id': 0,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('I_B', 3), ('R_B', 9)],
                         ('-', 0): [('V_B', 5), ('*', 1)],
                         ('=', 2): [('-', 0), ('V_{BE}', 7)]},
        'resultLatexStr': 'V_B-I_BR_B=V_{BE}',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (- V_B (* I_B R_B)) V_{BE})',
        'resultVariables': ['V_B', 'I_B', 'R_B', 'V_{BE}'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('I_B', 3), ('R_B', 9)],
                         ('-', 0): [('V_B', 5), ('V_{BE}', 7)],
                         ('=', 2): [('*', 1), ('-', 0)]},
        'resultLatexStr': 'I_BR_B=V_B-V_{BE}',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (* I_B R_B) (- V_B V_{BE}))',
        'resultVariables': ['I_B', 'R_B', 'V_B', 'V_{BE}'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__transistorOhmLaw2(verbose=False):
    latexEq = 'I_B=\\frac{V_B-V_{BE}}{R_B}'
    subject = 'R_B'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{V_B-V_{BE}}{I_B}=R_B' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('-', 0): [('V_B', 5), ('V_{BE}', 7)],
                         ('/', 1): [('-', 0), ('I_B', 3)],
                         ('=', 2): [('/', 1), ('R_B', 9)]},
        'resultLatexStr': '\\frac{V_B-V_{BE}}{I_B}=R_B',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (/ (- V_B V_{BE}) I_B) R_B)',
        'resultVariables': ['V_B', 'V_{BE}', 'I_B', 'R_B'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__ebermollsModel0(verbose=False):
    latexEq = 'I_C=I_S(e^{\\frac{V_{BE}}{V_T}}-1)'
    subject = 'I_S'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{I_C}{e^{\\frac{V_{BE}}{V_T}}-1}=I_S' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '*',
        'id': 14,
        'lastId': 3,
        'resultAST': {   ('-', 1): [('^', 0), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('-', 1)],
                         ('=', 3): [('/', 14), ('I_S', 6)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultLatexStr': '\\frac{I_C}{e^{\\frac{V_{BE}}{V_T}}-1}=I_S',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (/ I_C (- (^ e (/ V_{BE} V_T)) 1)) I_S)',
        'resultVariables': ['I_C', 'V_{BE}', 'V_T', 'I_S'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__ebermollsModel1(verbose=False):
    latexEq = 'I_C=I_S(e^{\\frac{V_{BE}}{V_T}}-1)'
    subject = 'V_{BE}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\ln(\\frac{I_C}{I_S}+1)V_T=V_{BE}' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '/',
        'id': 2,
        'lastId': 3,
        'resultAST': {   ('*', 2): [('log', 0), ('V_T', 11)],
                         ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('*', 2), ('V_{BE}', 9)],
                         ('log', 0): [('e', 8), ('+', 1)]},
        'resultLatexStr': '\\ln(\\frac{I_C}{I_S}+1)V_T=V_{BE}',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (* (log e (+ (/ I_C I_S) 1)) V_T) V_{BE})',
        'resultVariables': ['I_C', 'I_S', 'V_T', 'V_{BE}'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '^',
        'id': 0,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('log', 0), ('/', 2)],
                         ('log', 0): [('e', 8), ('+', 1)]},
        'resultLatexStr': '\\ln(\\frac{I_C}{I_S}+1)=\\frac{V_{BE}}{V_T}',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (log e (+ (/ I_C I_S) 1)) (/ V_{BE} V_T))',
        'resultVariables': ['I_C', 'I_S', 'V_{BE}', 'V_T'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '-',
        'id': 1,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('+', 1), ('^', 0)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultLatexStr': '\\frac{I_C}{I_S}+1=e^{\\frac{V_{BE}}{V_T}}',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (+ (/ I_C I_S) 1) (^ e (/ V_{BE} V_T)))',
        'resultVariables': ['I_C', 'I_S', 'V_{BE}', 'V_T'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 14,
        'lastId': 3,
        'resultAST': {   ('-', 1): [('^', 0), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('/', 14), ('-', 1)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultLatexStr': '\\frac{I_C}{I_S}=e^{\\frac{V_{BE}}{V_T}}-1',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (/ I_C I_S) (- (^ e (/ V_{BE} V_T)) 1))',
        'resultVariables': ['I_C', 'I_S', 'V_{BE}', 'V_T'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__ebermollsModel2(verbose=False):
    latexEq = 'I_C=I_S(e^{\\frac{V_{BE}}{V_T}}-1)'
    subject = 'V_T'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{V_{BE}}{\\ln(\\frac{I_C}{I_S}+1)}=V_T' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '/',
        'id': 2,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('log', 0)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('/', 2), ('V_T', 11)],
                         ('log', 0): [('e', 8), ('+', 1)]},
        'resultLatexStr': '\\frac{V_{BE}}{\\ln(\\frac{I_C}{I_S}+1)}=V_T',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (/ V_{BE} (log e (+ (/ I_C I_S) 1))) V_T)',
        'resultVariables': ['V_{BE}', 'I_C', 'I_S', 'V_T'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '^',
        'id': 0,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('log', 0), ('/', 2)],
                         ('log', 0): [('e', 8), ('+', 1)]},
        'resultLatexStr': '\\ln(\\frac{I_C}{I_S}+1)=\\frac{V_{BE}}{V_T}',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (log e (+ (/ I_C I_S) 1)) (/ V_{BE} V_T))',
        'resultVariables': ['I_C', 'I_S', 'V_{BE}', 'V_T'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '-',
        'id': 1,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('+', 1), ('^', 0)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultLatexStr': '\\frac{I_C}{I_S}+1=e^{\\frac{V_{BE}}{V_T}}',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (+ (/ I_C I_S) 1) (^ e (/ V_{BE} V_T)))',
        'resultVariables': ['I_C', 'I_S', 'V_{BE}', 'V_T'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 14,
        'lastId': 3,
        'resultAST': {   ('-', 1): [('^', 0), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('/', 14), ('-', 1)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultLatexStr': '\\frac{I_C}{I_S}=e^{\\frac{V_{BE}}{V_T}}-1',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (/ I_C I_S) (- (^ e (/ V_{BE} V_T)) 1))',
        'resultVariables': ['I_C', 'I_S', 'V_{BE}', 'V_T'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__acVoltage0(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = 'V_{peak}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{v_t}{\\sin(\\omega t+\\phi )}=V_{peak}' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '*',
        'id': 11,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('+', 0): [('*', 12), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('sin', 1)],
                         ('=', 4): [('/', 11), ('V_{peak}', 7)],
                         ('sin', 1): [('+', 0)]},
        'resultLatexStr': '\\frac{v_t}{\\sin(\\omega t+\\phi )}=V_{peak}',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (/ v_t (sin (+ (* omega t) phi))) V_{peak})',
        'resultVariables': ['v_t', 'omega', 't', 'phi', 'V_{peak}'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__acVoltage1(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = 'omega'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{\\arcsin(\\frac{v_t}{V_{peak}})-\\phi }{t}=\\omega '
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '*',
        'id': 12,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('arcsin', 1), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('/', 12): [('-', 0), ('t', 10)],
                         ('=', 4): [('/', 12), ('omega', 2)],
                         ('arcsin', 1): [('/', 11)]},
        'resultLatexStr': '\\frac{\\arcsin(\\frac{v_t}{V_{peak}})-\\phi '
                          '}{t}=\\omega ',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (/ (- (arcsin (/ v_t V_{peak})) phi) t) omega)',
        'resultVariables': ['v_t', 'V_{peak}', 'phi', 't', 'omega'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('-', 0): [('arcsin', 1), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('-', 0), ('*', 12)],
                         ('arcsin', 1): [('/', 11)]},
        'resultLatexStr': '\\arcsin(\\frac{v_t}{V_{peak}})-\\phi =\\omega t',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (- (arcsin (/ v_t V_{peak})) phi) (* omega t))',
        'resultVariables': ['v_t', 'V_{peak}', 'phi', 'omega', 't'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': 'sin',
        'id': 1,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('+', 0): [('*', 12), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('arcsin', 1), ('+', 0)],
                         ('arcsin', 1): [('/', 11)]},
        'resultLatexStr': '\\arcsin(\\frac{v_t}{V_{peak}})=\\omega t+\\phi ',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (arcsin (/ v_t V_{peak})) (+ (* omega t) phi))',
        'resultVariables': ['v_t', 'V_{peak}', 'omega', 't', 'phi'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 11,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('+', 0): [('*', 12), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('/', 11), ('sin', 1)],
                         ('sin', 1): [('+', 0)]},
        'resultLatexStr': '\\frac{v_t}{V_{peak}}=\\sin(\\omega t+\\phi )',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (/ v_t V_{peak}) (sin (+ (* omega t) phi)))',
        'resultVariables': ['v_t', 'V_{peak}', 'omega', 't', 'phi'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__moreThan1Op__acVoltage2(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = 't'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{\\arcsin(\\frac{v_t}{V_{peak}})-\\phi }{\\omega}=t' # to be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '*',
        'id': 12,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('arcsin', 1), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('/', 12): [('-', 0), ('omega', 2)],
                         ('=', 4): [('/', 12), ('t', 10)],
                         ('arcsin', 1): [('/', 11)]},
        'resultLatexStr': '\\frac{\\arcsin(\\frac{v_t}{V_{peak}})-\\phi '
                          '}{\\omega}=t',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (/ (- (arcsin (/ v_t V_{peak})) phi) omega) t)',
        'resultVariables': ['v_t', 'V_{peak}', 'phi', 'omega', 't'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('-', 0): [('arcsin', 1), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('-', 0), ('*', 12)],
                         ('arcsin', 1): [('/', 11)]},
        'resultLatexStr': '\\arcsin(\\frac{v_t}{V_{peak}})-\\phi =\\omega t',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (- (arcsin (/ v_t V_{peak})) phi) (* omega t))',
        'resultVariables': ['v_t', 'V_{peak}', 'phi', 'omega', 't'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': 'sin',
        'id': 1,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('+', 0): [('*', 12), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('arcsin', 1), ('+', 0)],
                         ('arcsin', 1): [('/', 11)]},
        'resultLatexStr': '\\arcsin(\\frac{v_t}{V_{peak}})=\\omega t+\\phi ',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (arcsin (/ v_t V_{peak})) (+ (* omega t) phi))',
        'resultVariables': ['v_t', 'V_{peak}', 'omega', 't', 'phi'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 11,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('+', 0): [('*', 12), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('/', 11), ('sin', 1)],
                         ('sin', 1): [('+', 0)]},
        'resultLatexStr': '\\frac{v_t}{V_{peak}}=\\sin(\\omega t+\\phi )',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (/ v_t V_{peak}) (sin (+ (* omega t) phi)))',
        'resultVariables': ['v_t', 'V_{peak}', 'omega', 't', 'phi'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__moreThan1Op__acVoltage3(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = 'phi'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arcsin(\\frac{v_t}{V_{peak}})-\\omega t=\\phi '
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('-', 0): [('arcsin', 1), ('*', 12)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('-', 0), ('phi', 3)],
                         ('arcsin', 1): [('/', 11)]},
        'resultLatexStr': '\\arcsin(\\frac{v_t}{V_{peak}})-\\omega t=\\phi ',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (- (arcsin (/ v_t V_{peak})) (* omega t)) phi)',
        'resultVariables': ['v_t', 'V_{peak}', 'omega', 't', 'phi'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': 'sin',
        'id': 1,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('+', 0): [('*', 12), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('arcsin', 1), ('+', 0)],
                         ('arcsin', 1): [('/', 11)]},
        'resultLatexStr': '\\arcsin(\\frac{v_t}{V_{peak}})=\\omega t+\\phi ',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (arcsin (/ v_t V_{peak})) (+ (* omega t) phi))',
        'resultVariables': ['v_t', 'V_{peak}', 'omega', 't', 'phi'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 11,
        'lastId': 4,
        'resultAST': {   ('*', 12): [('omega', 2), ('t', 10)],
                         ('+', 0): [('*', 12), ('phi', 3)],
                         ('/', 11): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('/', 11), ('sin', 1)],
                         ('sin', 1): [('+', 0)]},
        'resultLatexStr': '\\frac{v_t}{V_{peak}}=\\sin(\\omega t+\\phi )',
        'resultRootOfTree': ('=', 4),
        'resultSchemeStr': '(= (/ v_t V_{peak}) (sin (+ (* omega t) phi)))',
        'resultVariables': ['v_t', 'V_{peak}', 'omega', 't', 'phi'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__acPower0(verbose=False):
    latexEq = 'P=V_{rms}I_{rms}\\cos(\\phi)'
    subject = 'V_{rms}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{\\frac{P}{\\cos(\\phi)}}{I_{rms}}=V_{rms}'
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '*',
        'id': 8,
        'lastId': 2,
        'resultAST': {   ('/', 8): [('/', 9), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('cos', 0)],
                         ('=', 2): [('/', 8), ('V_{rms}', 4)],
                         ('cos', 0): [('phi', 1)]},
        'resultLatexStr': '\\frac{\\frac{P}{\\cos(\\phi)}}{I_{rms}}=V_{rms}',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (/ (/ P (cos phi)) I_{rms}) V_{rms})',
        'resultVariables': ['P', 'phi', 'I_{rms}', 'V_{rms}'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 9,
        'lastId': 2,
        'resultAST': {   ('*', 8): [('V_{rms}', 4), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('cos', 0)],
                         ('=', 2): [('/', 9), ('*', 8)],
                         ('cos', 0): [('phi', 1)]},
        'resultLatexStr': '\\frac{P}{\\cos(\\phi)}=V_{rms}I_{rms}',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (/ P (cos phi)) (* V_{rms} I_{rms}))',
        'resultVariables': ['P', 'phi', 'V_{rms}', 'I_{rms}'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)



def test__moreThan1Op__acPower1(verbose=False):
    latexEq = 'P=V_{rms}I_{rms}\\cos(\\phi)'
    subject = 'I_{rms}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{\\frac{P}{\\cos(\\phi)}}{V_{rms}}=I_{rms}'
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '*',
        'id': 8,
        'lastId': 2,
        'resultAST': {   ('/', 8): [('/', 9), ('V_{rms}', 4)],
                         ('/', 9): [('P', 3), ('cos', 0)],
                         ('=', 2): [('/', 8), ('I_{rms}', 6)],
                         ('cos', 0): [('phi', 1)]},
        'resultLatexStr': '\\frac{\\frac{P}{\\cos(\\phi)}}{V_{rms}}=I_{rms}',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (/ (/ P (cos phi)) V_{rms}) I_{rms})',
        'resultVariables': ['P', 'phi', 'V_{rms}', 'I_{rms}'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 9,
        'lastId': 2,
        'resultAST': {   ('*', 8): [('V_{rms}', 4), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('cos', 0)],
                         ('=', 2): [('/', 9), ('*', 8)],
                         ('cos', 0): [('phi', 1)]},
        'resultLatexStr': '\\frac{P}{\\cos(\\phi)}=V_{rms}I_{rms}',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (/ P (cos phi)) (* V_{rms} I_{rms}))',
        'resultVariables': ['P', 'phi', 'V_{rms}', 'I_{rms}'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__moreThan1Op__acPower2(verbose=False):
    latexEq = 'P=V_{rms}I_{rms}\\cos(\\phi)'
    subject = 'phi'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arccos(\\frac{P}{V_{rms}I_{rms}})=\\phi '
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': 'cos',
        'id': 0,
        'lastId': 2,
        'resultAST': {   ('*', 8): [('V_{rms}', 4), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('*', 8)],
                         ('=', 2): [('arccos', 0), ('phi', 1)],
                         ('arccos', 0): [('/', 9)]},
        'resultLatexStr': '\\arccos(\\frac{P}{V_{rms}I_{rms}})=\\phi ',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (arccos (/ P (* V_{rms} I_{rms}))) phi)',
        'resultVariables': ['P', 'V_{rms}', 'I_{rms}', 'phi'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 9,
        'lastId': 2,
        'resultAST': {   ('*', 8): [('V_{rms}', 4), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('*', 8)],
                         ('=', 2): [('/', 9), ('cos', 0)],
                         ('cos', 0): [('phi', 1)]},
        'resultLatexStr': '\\frac{P}{V_{rms}I_{rms}}=\\cos(\\phi)',
        'resultRootOfTree': ('=', 2),
        'resultSchemeStr': '(= (/ P (* V_{rms} I_{rms})) (cos phi))',
        'resultVariables': ['P', 'V_{rms}', 'I_{rms}', 'phi'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__6levelsDeep__impedanceOfParallelRLCCircuit0(verbose=False):
    latexEq = 'Z = ( \\frac{1}{R} + j ( \\omega C - \\frac{1}{\\omega L} ) )^{-1}'
    subject = 'R'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{1}{\\sqrt[-1]{Z}-j(\\omega C-\\frac{1}{\\omega L})}=R'
    #TODO \\sqrt[-1]{Z} is a bit weird... maybe 'fix' this in latexUnparse?, very unconventional to write like that
    #TODO \\sqrt[-1]{Z} ==> \\frac{-1}{Z}
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '/',
        'id': 4,
        'lastId': 8,
        'resultAST': {   ('*', 18): [('j', 12), ('-', 1)],
                         ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('-', 1): [('*', 19), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('*', 18)],
                         ('/', 4): [('1', 10), ('-', 3)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('=', 8): [('/', 4), ('R', 11)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\frac{1}{\\sqrt[-1]{Z}-j(\\omega '
                          'C-\\frac{1}{\\omega L})}=R',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (/ 1 (- (nroot (- 0 1) Z) (* j (- (* omega C) '
                           '(/ 1 (* omega L)))))) R)',
        'resultVariables': ['Z', 'j', 'omega', 'C', 'L', 'R'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 3,
        'lastId': 8,
        'resultAST': {   ('*', 18): [('j', 12), ('-', 1)],
                         ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('-', 1): [('*', 19), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('*', 18)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('=', 8): [('-', 3), ('/', 4)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\sqrt[-1]{Z}-j(\\omega C-\\frac{1}{\\omega '
                          'L})=\\frac{1}{R}',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (- (nroot (- 0 1) Z) (* j (- (* omega C) (/ 1 '
                           '(* omega L))))) (/ 1 R))',
        'resultVariables': ['Z', 'j', 'omega', 'C', 'L', 'R'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '^',
        'id': 0,
        'lastId': 8,
        'resultAST': {   ('*', 18): [('j', 12), ('-', 1)],
                         ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('+', 3): [('/', 4), ('*', 18)],
                         ('-', 1): [('*', 19), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('=', 8): [('nroot', 0), ('+', 3)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\sqrt[-1]{Z}=\\frac{1}{R}+j(\\omega '
                          'C-\\frac{1}{\\omega L})',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (nroot (- 0 1) Z) (+ (/ 1 R) (* j (- (* omega '
                           'C) (/ 1 (* omega L))))))',
        'resultVariables': ['Z', 'R', 'j', 'omega', 'C', 'L'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__6levelsDeep__impedanceOfParallelRLCCircuit1(verbose=False):
    latexEq = 'Z = ( \\frac{1}{R} + j ( \\omega C - \\frac{1}{\\omega L} ) )^{-1}'
    subject = 'C'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}+\\frac{1}{\\omega L}}{\\omega}=C'
    #TODO \\sqrt[-1]{Z} is a bit weird... maybe 'fix' this in latexUnparse?, very unconventional to write like that
    #TODO \\sqrt[-1]{Z} ==> \\frac{-1}{Z}
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '*',
        'id': 19,
        'lastId': 8,
        'resultAST': {   ('*', 20): [('omega', 7), ('L', 15)],
                         ('+', 1): [('/', 18), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('/', 4)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('/', 18): [('-', 3), ('j', 12)],
                         ('/', 19): [('+', 1), ('omega', 5)],
                         ('=', 8): [('/', 19), ('C', 13)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\frac{\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}+\\frac{1}{\\omega '
                          'L}}{\\omega}=C',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (/ (+ (/ (- (nroot (- 0 1) Z) (/ 1 R)) j) (/ 1 '
                           '(* omega L))) omega) C)',
        'resultVariables': ['Z', 'R', 'j', 'omega', 'L', 'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '-',
        'id': 1,
        'lastId': 8,
        'resultAST': {   ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('+', 1): [('/', 18), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('/', 4)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('/', 18): [('-', 3), ('j', 12)],
                         ('=', 8): [('+', 1), ('*', 19)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}+\\frac{1}{\\omega '
                          'L}=\\omega C',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (+ (/ (- (nroot (- 0 1) Z) (/ 1 R)) j) (/ 1 (* '
                           'omega L))) (* omega C))',
        'resultVariables': ['Z', 'R', 'j', 'omega', 'L', 'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 18,
        'lastId': 8,
        'resultAST': {   ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('-', 1): [('*', 19), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('/', 4)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('/', 18): [('-', 3), ('j', 12)],
                         ('=', 8): [('/', 18), ('-', 1)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}=\\omega '
                          'C-\\frac{1}{\\omega L}',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (/ (- (nroot (- 0 1) Z) (/ 1 R)) j) (- (* omega '
                           'C) (/ 1 (* omega L))))',
        'resultVariables': ['Z', 'R', 'j', 'omega', 'C', 'L'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 3,
        'lastId': 8,
        'resultAST': {   ('*', 18): [('j', 12), ('-', 1)],
                         ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('-', 1): [('*', 19), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('/', 4)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('=', 8): [('-', 3), ('*', 18)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\sqrt[-1]{Z}-\\frac{1}{R}=j(\\omega '
                          'C-\\frac{1}{\\omega L})',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (- (nroot (- 0 1) Z) (/ 1 R)) (* j (- (* omega '
                           'C) (/ 1 (* omega L)))))',
        'resultVariables': ['Z', 'R', 'j', 'omega', 'C', 'L'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '^',
        'id': 0,
        'lastId': 8,
        'resultAST': {   ('*', 18): [('j', 12), ('-', 1)],
                         ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('+', 3): [('/', 4), ('*', 18)],
                         ('-', 1): [('*', 19), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('=', 8): [('nroot', 0), ('+', 3)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\sqrt[-1]{Z}=\\frac{1}{R}+j(\\omega '
                          'C-\\frac{1}{\\omega L})',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (nroot (- 0 1) Z) (+ (/ 1 R) (* j (- (* omega '
                           'C) (/ 1 (* omega L))))))',
        'resultVariables': ['Z', 'R', 'j', 'omega', 'C', 'L'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__6levelsDeep__impedanceOfParallelRLCCircuit2(verbose=False):
    latexEq = 'Z = ( \\frac{1}{R} + j ( \\omega C - \\frac{1}{\\omega L} ) )^{-1}'
    subject = 'L'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{\\frac{1}{\\omega C-\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}}}{\\omega}=L'
    #TODO \\sqrt[-1]{Z} is a bit weird... maybe 'fix' this in latexUnparse?, very unconventional to write like that
    #TODO \\sqrt[-1]{Z} ==> \\frac{-1}{Z}
    # TODO DOUBLE_INVERSE=>simplification_in_AST
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '*',
        'id': 20,
        'lastId': 8,
        'resultAST': {   ('*', 19): [('omega', 5), ('C', 13)],
                         ('-', 1): [('*', 19), ('/', 18)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('/', 4)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('-', 1)],
                         ('/', 18): [('-', 3), ('j', 12)],
                         ('/', 20): [('/', 6), ('omega', 7)],
                         ('=', 8): [('/', 20), ('L', 15)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\frac{\\frac{1}{\\omega '
                          'C-\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}}}{\\omega}=L',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (/ (/ 1 (- (* omega C) (/ (- (nroot (- 0 1) Z) '
                           '(/ 1 R)) j))) omega) L)',
        'resultVariables': ['omega', 'C', 'Z', 'R', 'j', 'L'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 6,
        'lastId': 8,
        'resultAST': {   ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('-', 1): [('*', 19), ('/', 18)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('/', 4)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('-', 1)],
                         ('/', 18): [('-', 3), ('j', 12)],
                         ('=', 8): [('/', 6), ('*', 20)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\frac{1}{\\omega '
                          'C-\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}}=\\omega L',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (/ 1 (- (* omega C) (/ (- (nroot (- 0 1) Z) (/ '
                           '1 R)) j))) (* omega L))',
        'resultVariables': ['omega', 'C', 'Z', 'R', 'j', 'L'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '-',
        'id': 1,
        'lastId': 8,
        'resultAST': {   ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('-', 1): [('*', 19), ('/', 18)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('/', 4)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('/', 18): [('-', 3), ('j', 12)],
                         ('=', 8): [('-', 1), ('/', 6)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\omega '
                          'C-\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}=\\frac{1}{\\omega '
                          'L}',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (- (* omega C) (/ (- (nroot (- 0 1) Z) (/ 1 R)) '
                           'j)) (/ 1 (* omega L)))',
        'resultVariables': ['omega', 'C', 'Z', 'R', 'j', 'L'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 18,
        'lastId': 8,
        'resultAST': {   ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('-', 1): [('*', 19), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('/', 4)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('/', 18): [('-', 3), ('j', 12)],
                         ('=', 8): [('/', 18), ('-', 1)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}=\\omega '
                          'C-\\frac{1}{\\omega L}',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (/ (- (nroot (- 0 1) Z) (/ 1 R)) j) (- (* omega '
                           'C) (/ 1 (* omega L))))',
        'resultVariables': ['Z', 'R', 'j', 'omega', 'C', 'L'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 3,
        'lastId': 8,
        'resultAST': {   ('*', 18): [('j', 12), ('-', 1)],
                         ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('-', 1): [('*', 19), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('-', 3): [('nroot', 0), ('/', 4)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('=', 8): [('-', 3), ('*', 18)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\sqrt[-1]{Z}-\\frac{1}{R}=j(\\omega '
                          'C-\\frac{1}{\\omega L})',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (- (nroot (- 0 1) Z) (/ 1 R)) (* j (- (* omega '
                           'C) (/ 1 (* omega L)))))',
        'resultVariables': ['Z', 'R', 'j', 'omega', 'C', 'L'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '^',
        'id': 0,
        'lastId': 8,
        'resultAST': {   ('*', 18): [('j', 12), ('-', 1)],
                         ('*', 19): [('omega', 5), ('C', 13)],
                         ('*', 20): [('omega', 7), ('L', 15)],
                         ('+', 3): [('/', 4), ('*', 18)],
                         ('-', 1): [('*', 19), ('/', 6)],
                         ('-', 2): [('0', 17), ('1', 16)],
                         ('/', 4): [('1', 10), ('R', 11)],
                         ('/', 6): [('1', 14), ('*', 20)],
                         ('=', 8): [('nroot', 0), ('+', 3)],
                         ('nroot', 0): [('-', 2), ('Z', 9)]},
        'resultLatexStr': '\\sqrt[-1]{Z}=\\frac{1}{R}+j(\\omega '
                          'C-\\frac{1}{\\omega L})',
        'resultRootOfTree': ('=', 8),
        'resultSchemeStr': '(= (nroot (- 0 1) Z) (+ (/ 1 R) (* j (- (* omega '
                           'C) (/ 1 (* omega L))))))',
        'resultVariables': ['Z', 'R', 'j', 'omega', 'C', 'L'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)





def test__6levelsDeep__voltageGainOfNonInvertingOp0(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}' # the space between s, C and R_2 is a MUST!
    subject = 'R_f'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '((A_v-\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}})-1)R_1=R_f'
    #TODO latexparser._unparse must leave space between implicitMultiplies of single_variables, else, parsing will fail.
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '/',
        'id': 5,
        'lastId': 9,
        'resultAST': {   ('*', 5): [('-', 0), ('R_1', 15)],
                         ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 0): [('-', 1), ('1', 12)],
                         ('-', 1): [('A_v', 10), ('/', 6)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('*', 5), ('R_f', 13)]},
        'resultLatexStr': '((A_v-\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}})-1)R_1=R_f',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (* (- (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ '
                           '1 (* (* s C) R_2)))))))) 1) R_1) R_f)',
        'resultVariables': [   'A_v',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C',
                               'R_1',
                               'R_f'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 0,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 0): [('-', 1), ('1', 12)],
                         ('-', 1): [('A_v', 10), ('/', 6)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 0), ('/', 5)]},
        'resultLatexStr': '(A_v-\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}})-1=\\frac{R_f}{R_1}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ 1 '
                           '(* (* s C) R_2)))))))) 1) (/ R_f R_1))',
        'resultVariables': [   'A_v',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C',
                               'R_f',
                               'R_1'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 1,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('/', 6)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 1), ('+', 0)]},
        'resultLatexStr': 'A_v-\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}}=1+\\frac{R_f}{R_1}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ 1 (* '
                           '(* s C) R_2)))))))) (+ 1 (/ R_f R_1)))',
        'resultVariables': [   'A_v',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C',
                               'R_f',
                               'R_1'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__6levelsDeep__voltageGainOfNonInvertingOp1(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 'R_1'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{R_f}{(A_v-\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}})-1}=R_1'
    #TODO latexparser._unparse must leave space between implicitMultiplies of single_variables, else, parsing will fail.
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '/',
        'id': 5,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 0): [('-', 1), ('1', 12)],
                         ('-', 1): [('A_v', 10), ('/', 6)],
                         ('/', 5): [('R_f', 13), ('-', 0)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('/', 5), ('R_1', 15)]},
        'resultLatexStr': '\\frac{R_f}{(A_v-\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}})-1}=R_1',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ R_f (- (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 '
                           '(+ 1 (* (* s C) R_2)))))))) 1)) R_1)',
        'resultVariables': [   'R_f',
                               'A_v',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C',
                               'R_1'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 0,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 0): [('-', 1), ('1', 12)],
                         ('-', 1): [('A_v', 10), ('/', 6)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 0), ('/', 5)]},
        'resultLatexStr': '(A_v-\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}})-1=\\frac{R_f}{R_1}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ 1 '
                           '(* (* s C) R_2)))))))) 1) (/ R_f R_1))',
        'resultVariables': [   'A_v',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C',
                               'R_f',
                               'R_1'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 1,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('/', 6)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 1), ('+', 0)]},
        'resultLatexStr': 'A_v-\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}}=1+\\frac{R_f}{R_1}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ 1 (* '
                           '(* s C) R_2)))))))) (+ 1 (/ R_f R_1)))',
        'resultVariables': [   'A_v',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C',
                               'R_f',
                               'R_1'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__6levelsDeep__voltageGainOfNonInvertingOp2(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 'R_o'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    # print(modifiedAST)
    # expectedAST = {   ('*', 10): [('-', 9), ('+', 15)],
    # ('*', 20): [('s', 19), ('C', 21)],
    # ('*', 22): [('*', 20), ('R_2', 23)],
    # ('+', 3): [('1', 2), ('/', 4)],
    # ('+', 15): [('R_L', 14), ('/', 16)],
    # ('+', 18): [('1', 17), ('*', 22)],
    # ('-', 5): [('A_v', 1), ('+', 3)],
    # ('-', 9): [('/', 6), ('1', 8)],
    # ('/', 4): [('R_f', 12), ('R_1', 7)],
    # ('/', 6): [('1', 11), ('-', 5)],
    # ('/', 16): [('R_2', 24), ('+', 18)],
    # ('=', 0): [('*', 10), ('R_o', 13)]}
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '(\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1)(R_L+\\frac{R_2}{1+sCR_2})=R_o'
    #TODO latexparser._unparse must leave space between implicitMultiplies of single_variables, else, parsing will fail.
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '/',
        'id': 7,
        'lastId': 9,
        'resultAST': {   ('*', 7): [('-', 2), ('+', 3)],
                         ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('*', 7), ('R_o', 19)]},
        'resultLatexStr': '(\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1)(R_L+\\frac{R_2}{1+sCR_2})=R_o',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (* (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (+ R_L '
                           '(/ R_2 (+ 1 (* (* s C) R_2))))) R_o)',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               'R_2',
                               's',
                               'C',
                               'R_o'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 2,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 2), ('/', 7)]},
        'resultLatexStr': '\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1=\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 6,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('/', 6), ('+', 2)]},
        'resultLatexStr': '\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}=1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ 1 (- A_v (+ 1 (/ R_f R_1)))) (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2)))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 1,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 1), ('/', 6)]},
        'resultLatexStr': 'A_v-(1+\\frac{R_f}{R_1})=\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- A_v (+ 1 (/ R_f R_1))) (/ 1 (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__6levelsDeep__voltageGainOfNonInvertingOp3(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 'R_L'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-\\frac{R_2}{1+sCR_2}=R_L'
    #TODO latexparser._unparse must leave space between implicitMultiplies of single_variables, else, parsing will fail.
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '+',
        'id': 3,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('/', 8)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 3), ('R_L', 21)]},
        'resultLatexStr': '\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-\\frac{R_2}{1+sCR_2}=R_L',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) '
                           '1)) (/ R_2 (+ 1 (* (* s C) R_2)))) R_L)',
        'resultVariables': [   'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_2',
                               's',
                               'C',
                               'R_L'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 7,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('/', 7), ('+', 3)]},
        'resultLatexStr': '\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}=R_L+\\frac{R_2}{1+sCR_2}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1)) '
                           '(+ R_L (/ R_2 (+ 1 (* (* s C) R_2)))))',
        'resultVariables': [   'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 2,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 2), ('/', 7)]},
        'resultLatexStr': '\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1=\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 6,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('/', 6), ('+', 2)]},
        'resultLatexStr': '\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}=1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ 1 (- A_v (+ 1 (/ R_f R_1)))) (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2)))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 1,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 1), ('/', 6)]},
        'resultLatexStr': 'A_v-(1+\\frac{R_f}{R_1})=\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- A_v (+ 1 (/ R_f R_1))) (/ 1 (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__6levelsDeep__voltageGainOfNonInvertingOp4(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 's'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    # print(modifiedAST)
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{\\frac{\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}-1}{R_2}}{C}=s'
    # TODO DOUBLE_INVERSE=>simplification_in_AST
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 0,
        'functionName': '*',
        'id': 30,
        'lastId': 9,
        'resultAST': {   ('+', 0): [('1', 12), ('/', 5)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('-', 4): [('/', 8), ('1', 25)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('-', 3)],
                         ('/', 30): [('/', 31), ('C', 27)],
                         ('/', 31): [('-', 4), ('R_2', 28)],
                         ('=', 9): [('/', 30), ('s', 26)]},
        'resultLatexStr': '\\frac{\\frac{\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}-1}{R_2}}{C}=s',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ (/ (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 '
                           '(/ R_f R_1)))) 1)) R_L)) 1) R_2) C) s)',
        'resultVariables': [   'R_2',
                               'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               'C',
                               's'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 31,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('-', 4): [('/', 8), ('1', 25)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('-', 3)],
                         ('/', 31): [('-', 4), ('R_2', 28)],
                         ('=', 9): [('/', 31), ('*', 30)]},
        'resultLatexStr': '\\frac{\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}-1}{R_2}=sC',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ '
                           'R_f R_1)))) 1)) R_L)) 1) R_2) (* s C))',
        'resultVariables': [   'R_2',
                               'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 4,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('-', 4): [('/', 8), ('1', 25)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('-', 3)],
                         ('=', 9): [('-', 4), ('*', 31)]},
        'resultLatexStr': '\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}-1=sCR_2',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f '
                           'R_1)))) 1)) R_L)) 1) (* (* s C) R_2))',
        'resultVariables': [   'R_2',
                               'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 8,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('-', 3)],
                         ('=', 9): [('/', 8), ('+', 4)]},
        'resultLatexStr': '\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}=1+sCR_2',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f '
                           'R_1)))) 1)) R_L)) (+ 1 (* (* s C) R_2)))',
        'resultVariables': [   'R_2',
                               'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 3,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 3), ('/', 8)]},
        'resultLatexStr': '\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L=\\frac{R_2}{1+sCR_2}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) '
                           '1)) R_L) (/ R_2 (+ 1 (* (* s C) R_2))))',
        'resultVariables': [   'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 7,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('/', 7), ('+', 3)]},
        'resultLatexStr': '\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}=R_L+\\frac{R_2}{1+sCR_2}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1)) '
                           '(+ R_L (/ R_2 (+ 1 (* (* s C) R_2)))))',
        'resultVariables': [   'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 2,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 2), ('/', 7)]},
        'resultLatexStr': '\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1=\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 6,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('/', 6), ('+', 2)]},
        'resultLatexStr': '\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}=1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ 1 (- A_v (+ 1 (/ R_f R_1)))) (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2)))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 1,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 1), ('/', 6)]},
        'resultLatexStr': 'A_v-(1+\\frac{R_f}{R_1})=\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- A_v (+ 1 (/ R_f R_1))) (/ 1 (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__6levelsDeep__voltageGainOfNonInvertingOp5(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 'C'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{\\frac{\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}-1}{R_2}}{s}=C'
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '*',
        'id': 30,
        'lastId': 9,
        'resultAST': {   ('+', 0): [('1', 12), ('/', 5)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('-', 4): [('/', 8), ('1', 25)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('-', 3)],
                         ('/', 30): [('/', 31), ('s', 26)],
                         ('/', 31): [('-', 4), ('R_2', 28)],
                         ('=', 9): [('/', 30), ('C', 27)]},
        'resultLatexStr': '\\frac{\\frac{\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}-1}{R_2}}{s}=C',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ (/ (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 '
                           '(/ R_f R_1)))) 1)) R_L)) 1) R_2) s) C)',
        'resultVariables': [   'R_2',
                               'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 31,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('-', 4): [('/', 8), ('1', 25)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('-', 3)],
                         ('/', 31): [('-', 4), ('R_2', 28)],
                         ('=', 9): [('/', 31), ('*', 30)]},
        'resultLatexStr': '\\frac{\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}-1}{R_2}=sC',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ '
                           'R_f R_1)))) 1)) R_L)) 1) R_2) (* s C))',
        'resultVariables': [   'R_2',
                               'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 4,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('-', 4): [('/', 8), ('1', 25)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('-', 3)],
                         ('=', 9): [('-', 4), ('*', 31)]},
        'resultLatexStr': '\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}-1=sCR_2',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f '
                           'R_1)))) 1)) R_L)) 1) (* (* s C) R_2))',
        'resultVariables': [   'R_2',
                               'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 8,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('-', 3)],
                         ('=', 9): [('/', 8), ('+', 4)]},
        'resultLatexStr': '\\frac{R_2}{\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L}=1+sCR_2',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f '
                           'R_1)))) 1)) R_L)) (+ 1 (* (* s C) R_2)))',
        'resultVariables': [   'R_2',
                               'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 3,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('-', 3): [('/', 7), ('R_L', 21)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 3), ('/', 8)]},
        'resultLatexStr': '\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}-R_L=\\frac{R_2}{1+sCR_2}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) '
                           '1)) R_L) (/ R_2 (+ 1 (* (* s C) R_2))))',
        'resultVariables': [   'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 7,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('-', 2)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('/', 7), ('+', 3)]},
        'resultLatexStr': '\\frac{R_o}{\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1}=R_L+\\frac{R_2}{1+sCR_2}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1)) '
                           '(+ R_L (/ R_2 (+ 1 (* (* s C) R_2)))))',
        'resultVariables': [   'R_o',
                               'A_v',
                               'R_f',
                               'R_1',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 2,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('-', 2): [('/', 6), ('1', 18)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 2), ('/', 7)]},
        'resultLatexStr': '\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}-1=\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 6,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('-', 1)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('/', 6), ('+', 2)]},
        'resultLatexStr': '\\frac{1}{A_v-(1+\\frac{R_f}{R_1})}=1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (/ 1 (- A_v (+ 1 (/ R_f R_1)))) (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2)))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 1,
        'lastId': 9,
        'resultAST': {   ('*', 30): [('s', 26), ('C', 27)],
                         ('*', 31): [('*', 30), ('R_2', 28)],
                         ('+', 0): [('1', 12), ('/', 5)],
                         ('+', 2): [('1', 18), ('/', 7)],
                         ('+', 3): [('R_L', 21), ('/', 8)],
                         ('+', 4): [('1', 25), ('*', 31)],
                         ('-', 1): [('A_v', 10), ('+', 0)],
                         ('/', 5): [('R_f', 13), ('R_1', 15)],
                         ('/', 6): [('1', 17), ('+', 2)],
                         ('/', 7): [('R_o', 19), ('+', 3)],
                         ('/', 8): [('R_2', 23), ('+', 4)],
                         ('=', 9): [('-', 1), ('/', 6)]},
        'resultLatexStr': 'A_v-(1+\\frac{R_f}{R_1})=\\frac{1}{1+\\frac{R_o}{R_L+\\frac{R_2}{1+sCR_2}}}',
        'resultRootOfTree': ('=', 9),
        'resultSchemeStr': '(= (- A_v (+ 1 (/ R_f R_1))) (/ 1 (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))))',
        'resultVariables': [   'A_v',
                               'R_f',
                               'R_1',
                               'R_o',
                               'R_L',
                               'R_2',
                               's',
                               'C'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__linearEliminationBySubstitution__eq0(verbose=False):
    latexEq = 'I_{Z_{1}} R_{Z_{1}}=V_{in}-R I_{R}'
    subject = 'I_{R}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=False)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{V_{in}-I_{Z_{1}}R_{Z_{1}}}{R}=I_{R}' # TO be filled in 
    expected__stepsWithoutSimplify = [   {   'argumentIdx': 1,
        'functionName': '*',
        'id': 15,
        'lastId': 1,
        'resultAST': {   ('*', 14): [('I_{Z_{1}}', 2), ('R_{Z_{1}}', 5)],
                         ('-', 0): [('V_{in}', 8), ('*', 14)],
                         ('/', 15): [('-', 0), ('R', 11)],
                         ('=', 1): [('/', 15), ('I_{R}', 12)]},
        'resultLatexStr': '\\frac{V_{in}-I_{Z_{1}}R_{Z_{1}}}{R}=I_{R}',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= (/ (- V_{in} (* I_{Z_{1}} R_{Z_{1}})) R) I_{R})',
        'resultVariables': ['V_{in}', 'I_{Z_{1}}', 'R_{Z_{1}}', 'R', 'I_{R}'],
        'stepType': 'solving'},
    {   'argumentIdx': 1,
        'functionName': '-',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('*', 14): [('I_{Z_{1}}', 2), ('R_{Z_{1}}', 5)],
                         ('*', 15): [('R', 11), ('I_{R}', 12)],
                         ('-', 0): [('V_{in}', 8), ('*', 14)],
                         ('=', 1): [('-', 0), ('*', 15)]},
        'resultLatexStr': 'V_{in}-I_{Z_{1}}R_{Z_{1}}=RI_{R}',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= (- V_{in} (* I_{Z_{1}} R_{Z_{1}})) (* R I_{R}))',
        'resultVariables': ['V_{in}', 'I_{Z_{1}}', 'R_{Z_{1}}', 'R', 'I_{R}'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithoutSimplify == stepsWithoutSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithoutSimplify)




def test__linearEliminationBySubstitution__eq1(verbose=False):
    latexEq = 'I_{R_{C}} R_{C} - V^{Q1}_{BE} - I_{R} R = 0'
    subject = 'I_{R}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    #
    # print('In makesubjecttest0.py, schemeStr: ', eq0.schemeStr)
    # print('In makesubjecttest0.py, astScheme: ', eq0.astScheme)
    #
    modifiedAST, stepsWithSimplify = eq0.makeSubject(subject, simplify=True) # PIONEER BATCH :)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    # This is simplify:
    expectedLatexStr = 'I_{R}=\\frac{I_{R_{C}}R_{C}-V^{Q1}_{BE}}{R}'
    # This is without simplify:
    #expectedLatexStr = 'I_{R} =\\frac{(I_{R_{C}} R_{C}-V^{Q1}_{BE})-(0)}{R}' # TO be filled in 
    expected__stepsWithSimplify = [
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 17,
        'lastId': 3,
        'resultAST': {   ('*', 16): [('I_{R_{C}}', 4), ('R_{C}', 7)],
                         ('-', 1): [('*', 16), ('V^{Q1}_{BE}', 9)],
                         ('/', 17): [('-', 1), ('R', 14)],
                         ('=', 3): [('I_{R}', 12), ('/', 17)]},
        'resultLatexStr': 'I_{R}=\\frac{I_{R_{C}}R_{C}-V^{Q1}_{BE}}{R}',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= I_{R} (/ (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) '
                           'R))',
        'resultVariables': ['I_{R}', 'I_{R_{C}}', 'R_{C}', 'V^{Q1}_{BE}', 'R'],
        'stepType': 'solving'},
    {   'argumentIdx': None,
        'functionName': ('Subtractzero', 'essential', '(- $0 0)', '$0'),
        'id': None,
        'lastId': None,
        'resultAST': {   ('*', 16): [('I_{R_{C}}', 4), ('R_{C}', 7)],
                         ('*', 17): [('I_{R}', 12), ('R', 14)],
                         ('-', 1): [('*', 16), ('V^{Q1}_{BE}', 9)],
                         ('=', 3): [('*', 17), ('-', 1)]},
        'resultLatexStr': 'I_{R}R=I_{R_{C}}R_{C}-V^{Q1}_{BE}',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (* I_{R} R) (- (* I_{R_{C}} R_{C}) '
                           'V^{Q1}_{BE}))',
        'resultVariables': ['I_{R}', 'R', 'V^{Q1}_{BE}', 'I_{R_{C}}', 'R_{C}'],
        'stepType': 'simplification'},
    {   'argumentIdx': 1,
        'functionName': '-',
        'id': 2,
        'lastId': 3,
        'resultAST': {   ('*', 16): [('I_{R_{C}}', 4), ('R_{C}', 7)],
                         ('*', 17): [('I_{R}', 12), ('R', 14)],
                         ('-', 1): [('*', 16), ('V^{Q1}_{BE}', 9)],
                         ('-', 2): [('-', 1), ('0', 15)],
                         ('=', 3): [('*', 17), ('-', 2)]},
        'resultLatexStr': 'I_{R}R=(I_{R_{C}}R_{C}-V^{Q1}_{BE})-0',
        'resultRootOfTree': ('=', 3),
        'resultSchemeStr': '(= (* I_{R} R) (- (- (* I_{R_{C}} R_{C}) '
                           'V^{Q1}_{BE}) 0))',
        'resultVariables': ['I_{R}', 'R', 'I_{R_{C}}', 'R_{C}', 'V^{Q1}_{BE}'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithSimplify == stepsWithSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithSimplify)



def test__bipartiteSolver__simpleParallelCircuit0Vor(verbose=False):
    latexEq = 'V_{DC_{8}}=0+V_{R_{3}}'
    subject = 'V_{R_{3}}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    #
    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~In makesubjecttest0.py, schemeStr: ', eq0.schemeStr)
    # print('In makesubjecttest0.py, astScheme: ', eq0.astScheme)
    #
    modifiedAST, stepsWithSimplify = eq0.makeSubject(subject, simplify=True)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    # This is simplify:
    expectedLatexStr = 'V_{DC_{8}}=V_{R_{3}}'
    # This is without simplify:
    #expectedLatexStr = 'I_{R} =\\frac{(I_{R_{C}} R_{C}-V^{Q1}_{BE})-(0)}{R}' # TO be filled in 
    expected__stepsWithSimplify = [
    {   'argumentIdx': None,
        'functionName': ('Subtractzero', 'essential', '(- $0 0)', '$0'),
        'id': None,
        'lastId': None,
        'resultAST': {('=', 1): [('V_{DC_{8}}', 2), ('V_{R_{3}}', 6)]},
        'resultLatexStr': 'V_{DC_{8}}=V_{R_{3}}',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= V_{DC_{8}} V_{R_{3}})',
        'resultVariables': ['V_{DC_{8}}', 'V_{R_{3}}'],
        'stepType': 'simplification'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('-', 0): [('V_{DC_{8}}', 2), ('0', 5)],
                         ('=', 1): [('-', 0), ('V_{R_{3}}', 6)]},
        'resultLatexStr': 'V_{DC_{8}}-0=V_{R_{3}}',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= (- V_{DC_{8}} 0) V_{R_{3}})',
        'resultVariables': ['V_{DC_{8}}', 'V_{R_{3}}'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithSimplify == stepsWithSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithSimplify)



def test__bipartiteSolver__simpleParallelCircuit0Hin(verbose=False):
    latexEq = '\\frac{V_{R_{3}}}{I_{R_{3}}}=R_{R_{3}}'
    subject = 'V_{R_{3}}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    #
    # print('In makesubjecttest0.py, schemeStr: ', eq0.schemeStr)
    # print('In makesubjecttest0.py, astScheme: ', eq0.astScheme)
    #
    modifiedAST, stepsWithSimplify = eq0.makeSubject(subject, simplify=True)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    # This is simplify:
    expectedLatexStr = 'V_{R_{3}}=R_{R_{3}}I_{R_{3}}'
    # This is without simplify:
    #expectedLatexStr = 'I_{R} =\\frac{(I_{R_{C}} R_{C}-V^{Q1}_{BE})-(0)}{R}' # TO be filled in 
    expected__stepsWithSimplify = [
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('*', 0): [('R_{R_{3}}', 8), ('I_{R_{3}}', 5)],
                         ('=', 1): [('V_{R_{3}}', 2), ('*', 0)]},
        'resultLatexStr': 'V_{R_{3}}=R_{R_{3}}I_{R_{3}}',
        'resultRootOfTree': ('=', 1),
        'resultSchemeStr': '(= V_{R_{3}} (* R_{R_{3}} I_{R_{3}}))',
        'resultVariables': ['V_{R_{3}}', 'R_{R_{3}}', 'I_{R_{3}}'],
        'stepType': 'solving'}]
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and\
        expected__stepsWithSimplify == stepsWithSimplify
    )
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)
        print('stepsWithoutSimplify: ')
        pp.pprint(stepsWithSimplify)


if __name__=='__main__':
    test__moreThan1Op__seriesResistance0()
    test__moreThan1Op__seriesResistance1()
    test__moreThan1Op__parallelResistance0()
    test__moreThan1Op__parallelResistance1()
    test__moreThan1Op__parallelResistance2()
    test__moreThan1Op__ohmPowerLaw0()
    test__moreThan1Op__ohmPowerLaw1()
    test__moreThan1Op__ohmPowerLaw2()
    test__moreThan1Op__ohmPowerLaw3()
    # test__moreThan1Op__transistorOhmLaw0(True) # ugly
    # test__moreThan1Op__transistorOhmLaw1(True) # ugly
    test__moreThan1Op__transistorOhmLaw2()
    test__moreThan1Op__ebermollsModel0()
    test__moreThan1Op__ebermollsModel1()
    test__moreThan1Op__ebermollsModel2()
    test__moreThan1Op__acVoltage0()
    test__moreThan1Op__acVoltage1()
    test__moreThan1Op__acVoltage2()
    test__moreThan1Op__acVoltage3()
    test__moreThan1Op__acPower0()
    test__moreThan1Op__acPower1()
    test__moreThan1Op__acPower2()
    test__6levelsDeep__impedanceOfParallelRLCCircuit0() # TODO weird latex unparse sqrt[-1], simplify? #TODO write simplification_test for this
    test__6levelsDeep__impedanceOfParallelRLCCircuit1() # TODO weird latex unparse sqrt[-1], simplify? #TODO write simplification_test for this
    test__6levelsDeep__impedanceOfParallelRLCCircuit2() # TODO weird latex unparse sqrt[-1], DOUBLE_INVERSE=>simplification_in_AST #TODO write simplification_test for this
    test__6levelsDeep__voltageGainOfNonInvertingOp0() 
    test__6levelsDeep__voltageGainOfNonInvertingOp1()
    test__6levelsDeep__voltageGainOfNonInvertingOp2()
    test__6levelsDeep__voltageGainOfNonInvertingOp3()
    test__6levelsDeep__voltageGainOfNonInvertingOp4()
    test__6levelsDeep__voltageGainOfNonInvertingOp5()
    test__linearEliminationBySubstitution__eq0()
    test__linearEliminationBySubstitution__eq1() # MINUS_ZERO=>simplication_in_AST
    test__bipartiteSolver__simpleParallelCircuit0Vor()
    test__bipartiteSolver__simpleParallelCircuit0Hin()