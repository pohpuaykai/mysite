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
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__ohmPowerLaw0(verbose=False):
    latexEq = 'P=\\frac{V^2}{R}'
    subject = 'V'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__ohmPowerLaw2(verbose=False):
    latexEq = 'P=I^2R'
    subject = 'I'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = 'I_S=\\frac{I_C}{e^{\\frac{V_{BE}}{V_T}}-1}' # to be filled in 
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
    expectedLatexStr = 'V_{BE}=V_T \\ln(\\frac{I_C}{I_S}+1)' # to be filled in 
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
    expectedLatexStr = 'V_T= \\frac{V_{BE}}{\\ln(\\frac{I_C}{I_S}+1)}' # to be filled in 
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
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)



def test__moreThan1Op__acVoltage1(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = '\\omega'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__moreThan1Op__acVoltage3(verbose=False):
    latexEq = 'v_t=V_{peak}\\sin(\\omega t+\\phi)'
    subject = '\\phi'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = None # to be filled in 
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
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




def test__moreThan1Op__acPower2(verbose=False):
    latexEq = 'P=V_{rms}I_{rms}\\cos(\\phi)'
    subject = '\\phi'
    eq0 = Equation(latexEq, 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject(subject)
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print('OG: ', latexEq)
        print('subject: ', subject)
        print('TF: ', latexStr)




if __name__=='__main__':
    # test__moreThan1Op__seriesResistance0(True)
    # test__moreThan1Op__seriesResistance1(True)
    # test__moreThan1Op__parallelResistance0(True)
    test__moreThan1Op__parallelResistance1(True) # not tested yet
    # test__moreThan1Op__parallelResistance2(True) # not tested yet
    # test__moreThan1Op__ohmPowerLaw0(True) # not tested yet
    # test__moreThan1Op__ohmPowerLaw1(True) # not tested yet
    # test__moreThan1Op__ohmPowerLaw2(True) # not tested yet
    # test__moreThan1Op__ohmPowerLaw3(True) # not tested yet
    # test__moreThan1Op__transistorOhmLaw0(True) # not tested yet
    # test__moreThan1Op__transistorOhmLaw1(True) # not tested yet
    # test__moreThan1Op__transistorOhmLaw2(True) # not tested yet
    # test__moreThan1Op__ebermollsModel0(True) # not tested yet
    # test__moreThan1Op__ebermollsModel1(True) # not tested yet
    # test__moreThan1Op__ebermollsModel2(True) # not tested yet
    # test__moreThan1Op__acVoltage0(True) # not tested yet
    # test__moreThan1Op__acVoltage1(True) # not tested yet
    # test__moreThan1Op__acVoltage2(True) # not tested yet
    # test__moreThan1Op__acVoltage3(True) # not tested yet
    # test__moreThan1Op__acPower0(True) # not tested yet
    # test__moreThan1Op__acPower1(True) # not tested yet
    # test__moreThan1Op__acPower2(True) # not tested yet