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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('-', 0): [('R_1', 2), ('R_3', 6)],
                         ('=', 1): [('-', 0), ('R_2', 4)]},
        'resultSchemeStr': '(= (- R_1 R_3) R_2)'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('-', 0): [('R_1', 2), ('R_2', 4)],
                         ('=', 1): [('-', 0), ('R_3', 6)]},
        'resultSchemeStr': '(= (- R_1 R_2) R_3)'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 1,
        'lastId': 4,
        'resultAST': {   ('+', 0): [('/', 2), ('/', 3)],
                         ('/', 1): [('1', 5), ('+', 0)],
                         ('/', 2): [('1', 8), ('R_2', 9)],
                         ('/', 3): [('1', 11), ('R_3', 12)],
                         ('=', 4): [('R_1', 6), ('/', 1)]},
        'resultSchemeStr': '(= R_1 (/ 1 (+ (/ 1 R_2) (/ 1 R_3))))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 2,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('/', 1), ('/', 3)],
                         ('/', 1): [('1', 5), ('R_1', 6)],
                         ('/', 2): [('1', 8), ('-', 0)],
                         ('/', 3): [('1', 11), ('R_3', 12)],
                         ('=', 4): [('/', 2), ('R_2', 9)]},
        'resultSchemeStr': '(= (/ 1 (- (/ 1 R_1) (/ 1 R_3))) R_2)'},
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('/', 1), ('/', 3)],
                         ('/', 1): [('1', 5), ('R_1', 6)],
                         ('/', 2): [('1', 8), ('R_2', 9)],
                         ('/', 3): [('1', 11), ('R_3', 12)],
                         ('=', 4): [('-', 0), ('/', 2)]},
        'resultSchemeStr': '(= (- (/ 1 R_1) (/ 1 R_3)) (/ 1 R_2))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 3,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('/', 1), ('/', 2)],
                         ('/', 1): [('1', 5), ('R_1', 6)],
                         ('/', 2): [('1', 8), ('R_2', 9)],
                         ('/', 3): [('1', 11), ('-', 0)],
                         ('=', 4): [('/', 3), ('R_3', 12)]},
        'resultSchemeStr': '(= (/ 1 (- (/ 1 R_1) (/ 1 R_2))) R_3)'},
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('/', 1), ('/', 2)],
                         ('/', 1): [('1', 5), ('R_1', 6)],
                         ('/', 2): [('1', 8), ('R_2', 9)],
                         ('/', 3): [('1', 11), ('R_3', 12)],
                         ('=', 4): [('-', 0), ('/', 3)]},
        'resultSchemeStr': '(= (- (/ 1 R_1) (/ 1 R_2)) (/ 1 R_3))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '^',
        'id': 0,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('P', 3), ('R', 6)],
                         ('=', 2): [('nroot', 0), ('V', 4)],
                         ('nroot', 0): [('2', 5), ('*', 1)]},
        'resultSchemeStr': '(= (nroot 2 (* P R)) V)'},
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('P', 3), ('R', 6)],
                         ('=', 2): [('*', 1), ('^', 0)],
                         ('^', 0): [('V', 4), ('2', 5)]},
        'resultSchemeStr': '(= (* P R) (^ V 2))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('/', 1): [('^', 0), ('P', 3)],
                         ('=', 2): [('/', 1), ('R', 6)],
                         ('^', 0): [('V', 4), ('2', 5)]},
        'resultSchemeStr': '(= (/ (^ V 2) P) R)'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '^',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('/', 6): [('P', 2), ('R', 5)],
                         ('=', 1): [('nroot', 0), ('I', 3)],
                         ('nroot', 0): [('2', 4), ('/', 6)]},
        'resultSchemeStr': '(= (nroot 2 (/ P R)) I)'},
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 6,
        'lastId': 1,
        'resultAST': {   ('/', 6): [('P', 2), ('R', 5)],
                         ('=', 1): [('/', 6), ('^', 0)],
                         ('^', 0): [('I', 3), ('2', 4)]},
        'resultSchemeStr': '(= (/ P R) (^ I 2))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 6,
        'lastId': 1,
        'resultAST': {   ('/', 6): [('P', 2), ('^', 0)],
                         ('=', 1): [('/', 6), ('R', 5)],
                         ('^', 0): [('I', 3), ('2', 4)]},
        'resultSchemeStr': '(= (/ P (^ I 2)) R)'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '-',
        'id': 0,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('I_B', 3), ('R_B', 9)],
                         ('+', 0): [('*', 1), ('V_{BE}', 7)],
                         ('=', 2): [('+', 0), ('V_B', 5)]},
        'resultSchemeStr': '(= (+ (* I_B R_B) V_{BE}) V_B)'
    },
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('I_B', 3), ('R_B', 9)],
                         ('-', 0): [('V_B', 5), ('V_{BE}', 7)],
                         ('=', 2): [('*', 1), ('-', 0)]},
        'resultSchemeStr': '(= (* I_B R_B) (- V_B V_{BE}))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '-',
        'id': 0,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('I_B', 3), ('R_B', 9)],
                         ('-', 0): [('V_B', 5), ('*', 1)],
                         ('=', 2): [('-', 0), ('V_{BE}', 7)]},
        'resultSchemeStr': '(= (- V_B (* I_B R_B)) V_{BE})'
    },
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('*', 1): [('I_B', 3), ('R_B', 9)],
                         ('-', 0): [('V_B', 5), ('V_{BE}', 7)],
                         ('=', 2): [('*', 1), ('-', 0)]},
        'resultSchemeStr': '(= (* I_B R_B) (- V_B V_{BE}))'
    }
    ]
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
    expectedLatexStr = '\\frac{V_B -V_{BE}}{I_B}=R_B' # to be filled in 
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 1,
        'lastId': 2,
        'resultAST': {   ('-', 0): [('V_B', 5), ('V_{BE}', 7)],
                         ('/', 1): [('-', 0), ('I_B', 3)],
                         ('=', 2): [('/', 1), ('R_B', 9)]},
        'resultSchemeStr': '(= (/ (- V_B V_{BE}) I_B) R_B)'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 14,
        'lastId': 3,
        'resultAST': {   ('-', 1): [('^', 0), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('-', 1)],
                         ('=', 3): [('/', 14), ('I_S', 6)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultSchemeStr': '(= (/ I_C (- (^ e (/ V_{BE} V_T)) 1)) I_S)'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 2,
        'lastId': 3,
        'resultAST': {   ('*', 2): [('log', 0), ('V_T', 11)],
                         ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('*', 2), ('V_{BE}', 9)],
                         ('log', 0): [('e', 8), ('+', 1)]},
        'resultSchemeStr': '(= (* (log e (+ (/ I_C I_S) 1)) V_T) V_{BE})'},
    {   'argumentIdx': 1,
        'functionName': '^',
        'id': 0,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('log', 0), ('/', 2)],
                         ('log', 0): [('e', 8), ('+', 1)]},
        'resultSchemeStr': '(= (log e (+ (/ I_C I_S) 1)) (/ V_{BE} V_T))'},
    {   'argumentIdx': 0,
        'functionName': '-',
        'id': 1,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('+', 1), ('^', 0)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultSchemeStr': '(= (+ (/ I_C I_S) 1) (^ e (/ V_{BE} V_T)))'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 14,
        'lastId': 3,
        'resultAST': {   ('-', 1): [('^', 0), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('/', 14), ('-', 1)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultSchemeStr': '(= (/ I_C I_S) (- (^ e (/ V_{BE} V_T)) 1))'}]
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
    expectedLatexStr = '\\frac{V_{BE} }{\\ln(\\frac{I_C }{I_S}+1)}=V_T' # to be filled in 
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 2,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('log', 0)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('/', 2), ('V_T', 11)],
                         ('log', 0): [('e', 8), ('+', 1)]},
        'resultSchemeStr': '(= (/ V_{BE} (log e (+ (/ I_C I_S) 1))) V_T)'},
    {   'argumentIdx': 1,
        'functionName': '^',
        'id': 0,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('log', 0), ('/', 2)],
                         ('log', 0): [('e', 8), ('+', 1)]},
        'resultSchemeStr': '(= (log e (+ (/ I_C I_S) 1)) (/ V_{BE} V_T))'},
    {   'argumentIdx': 0,
        'functionName': '-',
        'id': 1,
        'lastId': 3,
        'resultAST': {   ('+', 1): [('/', 14), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('+', 1), ('^', 0)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultSchemeStr': '(= (+ (/ I_C I_S) 1) (^ e (/ V_{BE} V_T)))'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 14,
        'lastId': 3,
        'resultAST': {   ('-', 1): [('^', 0), ('1', 13)],
                         ('/', 2): [('V_{BE}', 9), ('V_T', 11)],
                         ('/', 14): [('I_C', 4), ('I_S', 6)],
                         ('=', 3): [('/', 14), ('-', 1)],
                         ('^', 0): [('e', 8), ('/', 2)]},
        'resultSchemeStr': '(= (/ I_C I_S) (- (^ e (/ V_{BE} V_T)) 1))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 10,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('+', 0): [('*', 11), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('sin', 1)],
                         ('=', 4): [('/', 10), ('V_{peak}', 7)],
                         ('sin', 1): [('+', 0)]},
        'resultSchemeStr': '(= (/ v_t (sin (+ (* omega t) phi))) V_{peak})'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 11,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('arcsin', 1), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('/', 11): [('-', 0), ('t', 9)],
                         ('=', 4): [('/', 11), ('omega', 2)],
                         ('arcsin', 1): [('/', 10)]},
        'resultSchemeStr': '(= (/ (- (arcsin (/ v_t V_{peak})) phi) t) omega)'},
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('-', 0): [('arcsin', 1), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('-', 0), ('*', 11)],
                         ('arcsin', 1): [('/', 10)]},
        'resultSchemeStr': '(= (- (arcsin (/ v_t V_{peak})) phi) (* omega t))'},
    {   'argumentIdx': 0,
        'functionName': 'sin',
        'id': 1,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('+', 0): [('*', 11), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('arcsin', 1), ('+', 0)],
                         ('arcsin', 1): [('/', 10)]},
        'resultSchemeStr': '(= (arcsin (/ v_t V_{peak})) (+ (* omega t) phi))'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 10,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('+', 0): [('*', 11), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('/', 10), ('sin', 1)],
                         ('sin', 1): [('+', 0)]},
        'resultSchemeStr': '(= (/ v_t V_{peak}) (sin (+ (* omega t) phi)))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 11,
        'lastId': 4,
        'resultAST': {   ('-', 0): [('arcsin', 1), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('/', 11): [('-', 0), ('omega', 2)],
                         ('=', 4): [('/', 11), ('t', 9)],
                         ('arcsin', 1): [('/', 10)]},
        'resultSchemeStr': '(= (/ (- (arcsin (/ v_t V_{peak})) phi) omega) t)'},
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('-', 0): [('arcsin', 1), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('-', 0), ('*', 11)],
                         ('arcsin', 1): [('/', 10)]},
        'resultSchemeStr': '(= (- (arcsin (/ v_t V_{peak})) phi) (* omega t))'},
    {   'argumentIdx': 0,
        'functionName': 'sin',
        'id': 1,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('+', 0): [('*', 11), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('arcsin', 1), ('+', 0)],
                         ('arcsin', 1): [('/', 10)]},
        'resultSchemeStr': '(= (arcsin (/ v_t V_{peak})) (+ (* omega t) phi))'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 10,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('+', 0): [('*', 11), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('/', 10), ('sin', 1)],
                         ('sin', 1): [('+', 0)]},
        'resultSchemeStr': '(= (/ v_t V_{peak}) (sin (+ (* omega t) phi)))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 0,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('-', 0): [('arcsin', 1), ('*', 11)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('-', 0), ('phi', 3)],
                         ('arcsin', 1): [('/', 10)]},
        'resultSchemeStr': '(= (- (arcsin (/ v_t V_{peak})) (* omega t)) phi)'},
    {   'argumentIdx': 0,
        'functionName': 'sin',
        'id': 1,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('+', 0): [('*', 11), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('arcsin', 1), ('+', 0)],
                         ('arcsin', 1): [('/', 10)]},
        'resultSchemeStr': '(= (arcsin (/ v_t V_{peak})) (+ (* omega t) phi))'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 10,
        'lastId': 4,
        'resultAST': {   ('*', 11): [('omega', 2), ('t', 9)],
                         ('+', 0): [('*', 11), ('phi', 3)],
                         ('/', 10): [('v_t', 5), ('V_{peak}', 7)],
                         ('=', 4): [('/', 10), ('sin', 1)],
                         ('sin', 1): [('+', 0)]},
        'resultSchemeStr': '(= (/ v_t V_{peak}) (sin (+ (* omega t) phi)))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 8,
        'lastId': 2,
        'resultAST': {   ('/', 8): [('/', 9), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('cos', 0)],
                         ('=', 2): [('/', 8), ('V_{rms}', 4)],
                         ('cos', 0): [('phi', 1)]},
        'resultSchemeStr': '(= (/ (/ P (cos phi)) I_{rms}) V_{rms})'},
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 9,
        'lastId': 2,
        'resultAST': {   ('*', 8): [('V_{rms}', 4), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('cos', 0)],
                         ('=', 2): [('/', 9), ('*', 8)],
                         ('cos', 0): [('phi', 1)]},
        'resultSchemeStr': '(= (/ P (cos phi)) (* V_{rms} I_{rms}))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 8,
        'lastId': 2,
        'resultAST': {   ('/', 8): [('/', 9), ('V_{rms}', 4)],
                         ('/', 9): [('P', 3), ('cos', 0)],
                         ('=', 2): [('/', 8), ('I_{rms}', 6)],
                         ('cos', 0): [('phi', 1)]},
        'resultSchemeStr': '(= (/ (/ P (cos phi)) V_{rms}) I_{rms})'},
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 9,
        'lastId': 2,
        'resultAST': {   ('*', 8): [('V_{rms}', 4), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('cos', 0)],
                         ('=', 2): [('/', 9), ('*', 8)],
                         ('cos', 0): [('phi', 1)]},
        'resultSchemeStr': '(= (/ P (cos phi)) (* V_{rms} I_{rms}))'
    }
    ]
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
    expectedLatexStr = '\\arccos(\\frac{P}{V_{rms} I_{rms}})=\\phi'
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cos',
        'id': 0,
        'lastId': 2,
        'resultAST': {   ('*', 8): [('V_{rms}', 4), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('*', 8)],
                         ('=', 2): [('arccos', 0), ('phi', 1)],
                         ('arccos', 0): [('/', 9)]},
        'resultSchemeStr': '(= (arccos (/ P (* V_{rms} I_{rms}))) phi)'},
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 9,
        'lastId': 2,
        'resultAST': {   ('*', 8): [('V_{rms}', 4), ('I_{rms}', 6)],
                         ('/', 9): [('P', 3), ('*', 8)],
                         ('=', 2): [('/', 9), ('cos', 0)],
                         ('cos', 0): [('phi', 1)]},
        'resultSchemeStr': '(= (/ P (* V_{rms} I_{rms})) (cos phi))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
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
        'resultSchemeStr': '(= (/ 1 (- (nroot (- 0 1) Z) (* j (- (* omega C) '
                           '(/ 1 (* omega L)))))) R)'},
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
        'resultSchemeStr': '(= (- (nroot (- 0 1) Z) (* j (- (* omega C) (/ 1 '
                           '(* omega L))))) (/ 1 R))'},
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
        'resultSchemeStr': '(= (nroot (- 0 1) Z) (+ (/ 1 R) (* j (- (* omega '
                           'C) (/ 1 (* omega L))))))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
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
        'resultSchemeStr': '(= (/ (+ (/ (- (nroot (- 0 1) Z) (/ 1 R)) j) (/ 1 '
                           '(* omega L))) omega) C)'},
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
        'resultSchemeStr': '(= (+ (/ (- (nroot (- 0 1) Z) (/ 1 R)) j) (/ 1 (* '
                           'omega L))) (* omega C))'},
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
        'resultSchemeStr': '(= (/ (- (nroot (- 0 1) Z) (/ 1 R)) j) (- (* omega '
                           'C) (/ 1 (* omega L))))'},
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
        'resultSchemeStr': '(= (- (nroot (- 0 1) Z) (/ 1 R)) (* j (- (* omega '
                           'C) (/ 1 (* omega L)))))'},
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
        'resultSchemeStr': '(= (nroot (- 0 1) Z) (+ (/ 1 R) (* j (- (* omega '
                           'C) (/ 1 (* omega L))))))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
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
        'resultSchemeStr': '(= (/ (/ 1 (- (* omega C) (/ (- (nroot (- 0 1) Z) '
                           '(/ 1 R)) j))) omega) L)'},
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
        'resultSchemeStr': '(= (/ 1 (- (* omega C) (/ (- (nroot (- 0 1) Z) (/ '
                           '1 R)) j))) (* omega L))'},
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
        'resultSchemeStr': '(= (- (* omega C) (/ (- (nroot (- 0 1) Z) (/ 1 R)) '
                           'j)) (/ 1 (* omega L)))'},
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
        'resultSchemeStr': '(= (/ (- (nroot (- 0 1) Z) (/ 1 R)) j) (- (* omega '
                           'C) (/ 1 (* omega L))))'},
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
        'resultSchemeStr': '(= (- (nroot (- 0 1) Z) (/ 1 R)) (* j (- (* omega '
                           'C) (/ 1 (* omega L)))))'},
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
        'resultSchemeStr': '(= (nroot (- 0 1) Z) (+ (/ 1 R) (* j (- (* omega '
                           'C) (/ 1 (* omega L))))))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
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
        'resultSchemeStr': '(= (* (- (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ '
                           '1 (* (* s C) R_2)))))))) 1) R_1) R_f)'},
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
        'resultSchemeStr': '(= (- (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ 1 '
                           '(* (* s C) R_2)))))))) 1) (/ R_f R_1))'},
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
        'resultSchemeStr': '(= (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ 1 (* '
                           '(* s C) R_2)))))))) (+ 1 (/ R_f R_1)))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
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
        'resultSchemeStr': '(= (/ R_f (- (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 '
                           '(+ 1 (* (* s C) R_2)))))))) 1)) R_1)'},
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
        'resultSchemeStr': '(= (- (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ 1 '
                           '(* (* s C) R_2)))))))) 1) (/ R_f R_1))'},
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
        'resultSchemeStr': '(= (- A_v (/ 1 (+ 1 (/ R_o (+ R_L (/ R_2 (+ 1 (* '
                           '(* s C) R_2)))))))) (+ 1 (/ R_f R_1)))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
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
        'resultSchemeStr': '(= (* (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (+ R_L '
                           '(/ R_2 (+ 1 (* (* s C) R_2))))) R_o)'},
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
        'resultSchemeStr': '(= (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))'},
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
        'resultSchemeStr': '(= (/ 1 (- A_v (+ 1 (/ R_f R_1)))) (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2)))))))'},
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
        'resultSchemeStr': '(= (- A_v (+ 1 (/ R_f R_1))) (/ 1 (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
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
        'resultSchemeStr': '(= (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) '
                           '1)) (/ R_2 (+ 1 (* (* s C) R_2)))) R_L)'},
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
        'resultSchemeStr': '(= (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1)) '
                           '(+ R_L (/ R_2 (+ 1 (* (* s C) R_2)))))'},
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
        'resultSchemeStr': '(= (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))'},
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
        'resultSchemeStr': '(= (/ 1 (- A_v (+ 1 (/ R_f R_1)))) (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2)))))))'},
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
        'resultSchemeStr': '(= (- A_v (+ 1 (/ R_f R_1))) (/ 1 (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
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
        'resultSchemeStr': '(= (/ (/ (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 '
                           '(/ R_f R_1)))) 1)) R_L)) 1) R_2) C) s)'},
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
        'resultSchemeStr': '(= (/ (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ '
                           'R_f R_1)))) 1)) R_L)) 1) R_2) (* s C))'},
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
        'resultSchemeStr': '(= (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f '
                           'R_1)))) 1)) R_L)) 1) (* (* s C) R_2))'},
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
        'resultSchemeStr': '(= (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f '
                           'R_1)))) 1)) R_L)) (+ 1 (* (* s C) R_2)))'},
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
        'resultSchemeStr': '(= (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) '
                           '1)) R_L) (/ R_2 (+ 1 (* (* s C) R_2))))'},
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
        'resultSchemeStr': '(= (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1)) '
                           '(+ R_L (/ R_2 (+ 1 (* (* s C) R_2)))))'},
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
        'resultSchemeStr': '(= (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))'},
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
        'resultSchemeStr': '(= (/ 1 (- A_v (+ 1 (/ R_f R_1)))) (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2)))))))'},
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
        'resultSchemeStr': '(= (- A_v (+ 1 (/ R_f R_1))) (/ 1 (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
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
        'resultSchemeStr': '(= (/ (/ (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 '
                           '(/ R_f R_1)))) 1)) R_L)) 1) R_2) s) C)'},
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
        'resultSchemeStr': '(= (/ (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ '
                           'R_f R_1)))) 1)) R_L)) 1) R_2) (* s C))'},
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
        'resultSchemeStr': '(= (- (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f '
                           'R_1)))) 1)) R_L)) 1) (* (* s C) R_2))'},
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
        'resultSchemeStr': '(= (/ R_2 (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f '
                           'R_1)))) 1)) R_L)) (+ 1 (* (* s C) R_2)))'},
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
        'resultSchemeStr': '(= (- (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) '
                           '1)) R_L) (/ R_2 (+ 1 (* (* s C) R_2))))'},
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
        'resultSchemeStr': '(= (/ R_o (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1)) '
                           '(+ R_L (/ R_2 (+ 1 (* (* s C) R_2)))))'},
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
        'resultSchemeStr': '(= (- (/ 1 (- A_v (+ 1 (/ R_f R_1)))) 1) (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))'},
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
        'resultSchemeStr': '(= (/ 1 (- A_v (+ 1 (/ R_f R_1)))) (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2)))))))'},
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
        'resultSchemeStr': '(= (- A_v (+ 1 (/ R_f R_1))) (/ 1 (+ 1 (/ R_o (+ '
                           'R_L (/ R_2 (+ 1 (* (* s C) R_2))))))))'
    }
    ]
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
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 14,
        'lastId': 1,
        'resultAST': {   ('*', 13): [('I_{Z_{1}}', 2), ('R_{Z_{1}}', 5)],
                         ('-', 0): [('V_{in}', 8), ('*', 13)],
                         ('/', 14): [('-', 0), ('R', 10)],
                         ('=', 1): [('/', 14), ('I_{R}', 11)]},
        'resultSchemeStr': '(= (/ (- V_{in} (* I_{Z_{1}} R_{Z_{1}})) R) '
                           'I_{R})'},
    {   'argumentIdx': 1,
        'functionName': '-',
        'id': 0,
        'lastId': 1,
        'resultAST': {   ('*', 13): [('I_{Z_{1}}', 2), ('R_{Z_{1}}', 5)],
                         ('*', 14): [('R', 10), ('I_{R}', 11)],
                         ('-', 0): [('V_{in}', 8), ('*', 13)],
                         ('=', 1): [('-', 0), ('*', 14)]},
        'resultSchemeStr': '(= (- V_{in} (* I_{Z_{1}} R_{Z_{1}})) (* R '
                           'I_{R}))'}
    ]
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




def test__linearEliminationBySubstitution__eq1(verbose=False):# MINUS_ZERO=>simplication_in_AST TODO
    latexEq = 'I_{R_{C}} R_{C} - V^{Q1}_{BE} - I_{R} R = 0'
    subject = 'I_{R}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    #
    # print('In makesubjecttest0.py, schemeStr: ', eq0.schemeStr)
    # print('In makesubjecttest0.py, astScheme: ', eq0.astScheme)
    #
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject(subject, simplify=True) # PIONEER BATCH :)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    # This is simplify:
    expectedLatexStr = 'I_{R} =\\frac{I_{R_{C}} R_{C}-V^{Q1}_{BE}}{R}'
    # This is without simplify:
    #expectedLatexStr = 'I_{R} =\\frac{(I_{R_{C}} R_{C}-V^{Q1}_{BE})-(0)}{R}' # TO be filled in 
    expected__stepsWithoutSimplify = None
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
    # test__moreThan1Op__transistorOhmLaw2(True) # ugly
    test__moreThan1Op__ebermollsModel0()
    test__moreThan1Op__ebermollsModel1()
    # test__moreThan1Op__ebermollsModel2(True)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<log_e did not become ln
    test__moreThan1Op__acVoltage0()
    test__moreThan1Op__acVoltage1()
    test__moreThan1Op__acVoltage2()
    test__moreThan1Op__acVoltage3()
    test__moreThan1Op__acPower0()
    test__moreThan1Op__acPower1()
    # test__moreThan1Op__acPower2(True) # ugly
    test__6levelsDeep__impedanceOfParallelRLCCircuit0() # TODO weird latex unparse sqrt[-1], simplify?
    test__6levelsDeep__impedanceOfParallelRLCCircuit1() # TODO weird latex unparse sqrt[-1], simplify?
    test__6levelsDeep__impedanceOfParallelRLCCircuit2() # TODO weird latex unparse sqrt[-1], DOUBLE_INVERSE=>simplification_in_AST
    test__6levelsDeep__voltageGainOfNonInvertingOp0() 
    test__6levelsDeep__voltageGainOfNonInvertingOp1()
    test__6levelsDeep__voltageGainOfNonInvertingOp2()
    test__6levelsDeep__voltageGainOfNonInvertingOp3()
    test__6levelsDeep__voltageGainOfNonInvertingOp4()
    test__6levelsDeep__voltageGainOfNonInvertingOp5()
    test__linearEliminationBySubstitution__eq0()
    # test__linearEliminationBySubstitution__eq1(True) # MINUS_ZERO=>simplication_in_AST#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<something went wrong please check