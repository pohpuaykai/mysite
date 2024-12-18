import inspect
import pprint

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


def test__moreThan1Op__seriesResistance0(verbose=False):
    latexEq = 'R_1=R_2+R_3'
    subject = 'R_2'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'R_1-R_3=R_2' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)


def test__moreThan1Op__seriesResistance1(verbose=False):
    latexEq = 'R_1=R_2+R_3'
    subject = 'R_3'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'R_1-R_2=R_3' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)


def test__moreThan1Op__parallelResistance0(verbose=False):
    latexEq = '\\frac{1}{R_1}=\\frac{1}{R_2}+\\frac{1}{R_3}'
    subject = 'R_1'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'R_1=\\frac{1}{\\frac{1}{R_2}+\\frac{1}{R_3}}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__parallelResistance1(verbose=False):
    latexEq = '\\frac{1}{R_1}=\\frac{1}{R_2}+\\frac{1}{R_3}'
    subject = 'R_2'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{1}{\\frac{1}{R_1}-\\frac{1}{R_3}}=R_2' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__parallelResistance2(verbose=False):
    latexEq = '\\frac{1}{R_1}=\\frac{1}{R_2}+\\frac{1}{R_3}'
    subject = 'R_3'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{1}{\\frac{1}{R_1}-\\frac{1}{R_2}}=R_3' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__ohmPowerLaw0(verbose=False): # TODO nroot of even power, so include +-
    latexEq = 'P=\\frac{V^2}{R}'
    subject = 'V'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\sqrt{PR}=V' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__ohmPowerLaw1(verbose=False):
    latexEq = 'P=\\frac{V^2}{R}'
    subject = 'R'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{V^2}{P}=R' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__ohmPowerLaw2(verbose=False): # TODO nroot of even power, so include +-
    latexEq = 'P=I^2R'
    subject = 'I'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\sqrt{\\frac{P}{R}}=I' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__ohmPowerLaw3(verbose=False):
    latexEq = 'P=I^2R'
    subject = 'R'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{P}{I^2}=R' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__transistorOhmLaw0(verbose=False):
    latexEq = 'I_B=\\frac{V_B-V_{BE}}{R_B}'
    subject = 'V_B'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'I_B R_B+V_{BE}=V_B' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)


def test__moreThan1Op__transistorOhmLaw1(verbose=False):
    latexEq = 'I_B=\\frac{V_B-V_{BE}}{R_B}'
    subject = 'V_{BE}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'V_B -I_B R_B=V_{BE}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__transistorOhmLaw2(verbose=False):
    latexEq = 'I_B=\\frac{V_B-V_{BE}}{R_B}'
    subject = 'R_B'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{V_B -V_{BE}}{I_B}=R_B' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__ebermollsModel0(verbose=False):
    latexEq = 'I_C=I_S(e^{\\frac{V_{BE}}{V_T}}-1)'
    subject = 'I_S'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{I_C }{e^{\\frac{V_{BE} }{V_T}}-1}=I_S' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__ebermollsModel1(verbose=False):
    latexEq = 'I_C=I_S(e^{\\frac{V_{BE}}{V_T}}-1)'
    subject = 'V_{BE}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\ln(\\frac{I_C }{I_S}+1)V_T=V_{BE}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__ebermollsModel2(verbose=False):
    latexEq = 'I_C=I_S(e^{\\frac{V_{BE}}{V_T}}-1)'
    subject = 'V_T'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{V_{BE} }{\\ln(\\frac{I_C }{I_S}+1)}=V_T' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__acVoltage0(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = 'V_{peak}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{v_t }{\\sin(\\omega t+\\phi)}=V_{peak}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__acVoltage1(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = 'omega'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{\\arcsin(\\frac{v_t }{V_{peak}})-\\phi}{t}=\\omega'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__moreThan1Op__acVoltage2(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = 't'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{\\arcsin(\\frac{v_t }{V_{peak}})-\\phi}{\\omega}=t' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__moreThan1Op__acVoltage3(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = 'phi'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\arcsin(\\frac{v_t }{V_{peak}})-\\omega t=\\phi'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__acPower0(verbose=False):
    latexEq = 'P=V_{rms}I_{rms}\\cos(\\phi)'
    subject = 'V_{rms}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{\\frac{P}{\\cos(\\phi )}}{I_{rms}}=V_{rms}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__acPower1(verbose=False):
    latexEq = 'P=V_{rms}I_{rms}\\cos(\\phi)'
    subject = 'I_{rms}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{\\frac{P}{\\cos(\\phi )}}{V_{rms}}=I_{rms}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__moreThan1Op__acPower2(verbose=False):
    latexEq = 'P=V_{rms}I_{rms}\\cos(\\phi)'
    subject = 'phi'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\arccos(\\frac{P}{V_{rms} I_{rms}})=\\phi'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__6levelsDeep__impedanceOfParallelRLCCircuit0(verbose=False):
    latexEq = 'Z = ( \\frac{1}{R} + j ( \\omega C - \\frac{1}{\\omega L} ) )^{-1}'
    subject = 'R'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{1}{\\sqrt[-1]{Z}-j(\\omega C-\\frac{1}{\\omega L})}=R'
    #TODO \\sqrt[-1]{Z} is a bit weird... maybe 'fix' this in latexUnparse?, very unconventional to write like that
    #TODO \\sqrt[-1]{Z} ==> \\frac{-1}{Z}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__6levelsDeep__impedanceOfParallelRLCCircuit1(verbose=False):
    latexEq = 'Z = ( \\frac{1}{R} + j ( \\omega C - \\frac{1}{\\omega L} ) )^{-1}'
    subject = 'C'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}+\\frac{1}{\\omega L}}{\\omega}=C'
    #TODO \\sqrt[-1]{Z} is a bit weird... maybe 'fix' this in latexUnparse?, very unconventional to write like that
    #TODO \\sqrt[-1]{Z} ==> \\frac{-1}{Z}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__6levelsDeep__impedanceOfParallelRLCCircuit2(verbose=False):
    latexEq = 'Z = ( \\frac{1}{R} + j ( \\omega C - \\frac{1}{\\omega L} ) )^{-1}'
    subject = 'L'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{\\frac{1}{\\omega C-\\frac{\\sqrt[-1]{Z}-\\frac{1}{R}}{j}}}{\\omega}=L'
    #TODO \\sqrt[-1]{Z} is a bit weird... maybe 'fix' this in latexUnparse?, very unconventional to write like that
    #TODO \\sqrt[-1]{Z} ==> \\frac{-1}{Z}
    # TODO DOUBLE_INVERSE=>simplification_in_AST
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)





def test__6levelsDeep__voltageGainOfNonInvertingOp0(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}' # the space between s, C and R_2 is a MUST!
    subject = 'R_f'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '((A_v -\\frac{1}{1+\\frac{R_o }{R_L +\\frac{R_2}{1+sCR_2}}})-(1))R_1=R_f'
    #TODO latexparser._unparse must leave space between implicitMultiplies of single_variables, else, parsing will fail.
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__6levelsDeep__voltageGainOfNonInvertingOp1(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 'R_1'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{R_f }{(A_v -\\frac{1}{1+\\frac{R_o }{R_L +\\frac{R_2}{1+sCR_2}}})-(1)}=R_1'
    #TODO latexparser._unparse must leave space between implicitMultiplies of single_variables, else, parsing will fail.
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__6levelsDeep__voltageGainOfNonInvertingOp2(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 'R_o'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
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
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '(\\frac{1}{A_v -(1+\\frac{R_f }{R_1})}-1)(R_L +\\frac{R_2}{1+sCR_2})=R_o'
    #TODO latexparser._unparse must leave space between implicitMultiplies of single_variables, else, parsing will fail.
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__6levelsDeep__voltageGainOfNonInvertingOp3(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 'R_L'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{R_o }{\\frac{1}{A_v -(1+\\frac{R_f }{R_1})}-1}-\\frac{R_2}{1+sCR_2}=R_L'
    #TODO latexparser._unparse must leave space between implicitMultiplies of single_variables, else, parsing will fail.
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__6levelsDeep__voltageGainOfNonInvertingOp4(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 's'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    # print(modifiedAST)
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{\\frac{\\frac{R_2}{\\frac{R_o }{\\frac{1}{A_v -(1+\\frac{R_f }{R_1})}-1}-R_L}-1}{R_2}}{C}=s'
    # TODO DOUBLE_INVERSE=>simplification_in_AST
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__6levelsDeep__voltageGainOfNonInvertingOp5(verbose=False):
    latexEq = 'A_v = 1 + \\frac{R_f}{R_1} + \\frac{1}{1 + \\frac{R_o}{( R_L + \\frac{R_2}{1 + s C R_2} )}}'
    subject = 'C'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{\\frac{\\frac{R_2}{\\frac{R_o }{\\frac{1}{A_v -(1+\\frac{R_f }{R_1})}-1}-R_L}-1}{R_2}}{s}=C'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__linearEliminationBySubstitution__eq0(verbose=False):
    latexEq = 'I_{Z_{1}} R_{Z_{1}}=V_{in}-R I_{R}'
    subject = 'I_{R}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = '\\frac{V_{in} -I_{Z_{1}}R_{Z_{1}}}{R}=I_{R}' # TO be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__linearEliminationBySubstitution__eq1(verbose=False):# MINUS_ZERO=>simplication_in_AST TODO
    latexEq = 'I_{R_{C}} R_{C} - V^{Q1}_{BE} - I_{R} R = 0'
    subject = 'I_{R}'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'I_{R} =\\frac{(I_{R_{C}} R_{C}-V^{Q1}_{BE})-(0)}{R}' # TO be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



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
    test__moreThan1Op__transistorOhmLaw0()
    test__moreThan1Op__transistorOhmLaw1()
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
    test__6levelsDeep__impedanceOfParallelRLCCircuit0() # TODO weird latex unparse sqrt[-1]
    test__6levelsDeep__impedanceOfParallelRLCCircuit1() # TODO weird latex unparse sqrt[-1]
    test__6levelsDeep__impedanceOfParallelRLCCircuit2() # TODO weird latex unparse sqrt[-1], DOUBLE_INVERSE=>simplification_in_AST
    test__6levelsDeep__voltageGainOfNonInvertingOp0()
    test__6levelsDeep__voltageGainOfNonInvertingOp1()
    test__6levelsDeep__voltageGainOfNonInvertingOp2() #
    test__6levelsDeep__voltageGainOfNonInvertingOp3()
    test__6levelsDeep__voltageGainOfNonInvertingOp4() 
    test__6levelsDeep__voltageGainOfNonInvertingOp5()
    test__linearEliminationBySubstitution__eq0()
    test__linearEliminationBySubstitution__eq1() #TODO MINUS_ZERO=>simplication_in_AST