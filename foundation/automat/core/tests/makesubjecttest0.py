import inspect
import pprint

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


def test__moreThan1Op__seriesResistance0(verbose=False):
    eq0 = Equation('R_1=R_2+R_3', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('R_2')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__seriesResistance1(verbose=False):
    eq0 = Equation('R_1=R_2+R_3', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('R_3')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__moreThan1Op__parallelResistance0(verbose=False):
    eq0 = Equation('\\frac{1}{R_1}=\\frac{1}{R_2}+\\frac{1}{R_3}', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('R_1')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__parallelResistance1(verbose=False):
    eq0 = Equation('\\frac{1}{R_1}=\\frac{1}{R_2}+\\frac{1}{R_3}', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('R_2')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__parallelResistance2(verbose=False):
    eq0 = Equation('\\frac{1}{R_1}=\\frac{1}{R_2}+\\frac{1}{R_3}', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('R_3')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__ohmPowerLaw0(verbose=False):
    eq0 = Equation('P=\\frac{V^2}{R}', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('V')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)




def test__moreThan1Op__ohmPowerLaw1(verbose=False):
    eq0 = Equation('P=\\frac{V^2}{R}', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('R')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__ohmPowerLaw2(verbose=False):
    eq0 = Equation('P=I^2R', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('I')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__ohmPowerLaw3(verbose=False):
    eq0 = Equation('P=I^2R', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('R')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__transistorOhmLaw0(verbose=False):
    eq0 = Equation('I_B=\\frac{V_B-V_{BE}}{R_B}', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('V_B')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)


def test__moreThan1Op__transistorOhmLaw1(verbose=False):
    eq0 = Equation('I_B=\\frac{V_B-V_{BE}}{R_B}', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('V_{BE}')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__transistorOhmLaw2(verbose=False):
    eq0 = Equation('I_B=\\frac{V_B-V_{BE}}{R_B}', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('R_B')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__ebermollsModel0(verbose=False):
    eq0 = Equation('I_C=I_S(e^{\\frac{V_{BE}}{V_T}}-1)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('I_S')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'I_S=\\frac{I_C}{e^{\\frac{V_{BE}}{V_T}}-1}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__ebermollsModel1(verbose=False):
    eq0 = Equation('I_C=I_S(e^{\\frac{V_{BE}}{V_T}}-1)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('V_{BE}')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'V_{BE}=V_T \\ln(\\frac{I_C}{I_S}+1)' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__ebermollsModel2(verbose=False):
    eq0 = Equation('I_C=I_S(e^{\\frac{V_{BE}}{V_T}}-1)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('V_{BE}')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = 'V_T= \\frac{V_{BE}}{\\ln(\\frac{I_C}{I_S}+1)}' # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__acVoltage0(verbose=False):
    eq0 = Equation('v_t=V_{peak}\\sin(\\omega t+\\phi)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('V_{peak}')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__acVoltage1(verbose=False):
    eq0 = Equation('v_t=V_{peak}\\sin(\\omega t+\\phi)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('\\omega')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)




def test__moreThan1Op__acVoltage2(verbose=False):
    eq0 = Equation('v_t=V_{peak}\\sin(\\omega t+\\phi)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('t')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)




def test__moreThan1Op__acVoltage3(verbose=False):
    eq0 = Equation('v_t=V_{peak}\\sin(\\omega t+\\phi)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('\\phi')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__acPower0(verbose=False):
    eq0 = Equation('P=V_{rms}I_{rms}\\cos(\\phi)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('V_{rms}')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)



def test__moreThan1Op__acPower1(verbose=False):
    eq0 = Equation('P=V_{rms}I_{rms}\\cos(\\phi)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('I_{rms}')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)




def test__moreThan1Op__acPower2(verbose=False):
    eq0 = Equation('P=V_{rms}I_{rms}\\cos(\\phi)', 'latex', verbose=verbose)
    modifiedAST = eq0.makeSubject('\\phi')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST)._unparse()
    expectedLatexStr = None # to be filled in 
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expectedLatexStr == latexStr)
    if verbose:
        print(latexStr)




if __name__=='__main__':
    test__moreThan1Op__seriesResistance0(True) # not tested yet
    test__moreThan1Op__seriesResistance1(True) # not tested yet
    test__moreThan1Op__parallelResistance0(True) # not tested yet
    test__moreThan1Op__parallelResistance1(True) # not tested yet
    test__moreThan1Op__parallelResistance2(True) # not tested yet
    test__moreThan1Op__ohmPowerLaw0(True) # not tested yet
    test__moreThan1Op__ohmPowerLaw1(True) # not tested yet
    test__moreThan1Op__ohmPowerLaw2(True) # not tested yet
    test__moreThan1Op__ohmPowerLaw3(True) # not tested yet
    test__moreThan1Op__transistorOhmLaw0(True) # not tested yet
    test__moreThan1Op__transistorOhmLaw1(True) # not tested yet
    test__moreThan1Op__transistorOhmLaw2(True) # not tested yet
    test__moreThan1Op__ebermollsModel0(True) # not tested yet
    test__moreThan1Op__ebermollsModel1(True) # not tested yet
    test__moreThan1Op__ebermollsModel2(True) # not tested yet
    test__moreThan1Op__acVoltage0(True) # not tested yet
    test__moreThan1Op__acVoltage1(True) # not tested yet
    test__moreThan1Op__acVoltage2(True) # not tested yet
    test__moreThan1Op__acVoltage3(True) # not tested yet
    test__moreThan1Op__acPower0(True) # not tested yet
    test__moreThan1Op__acPower1(True) # not tested yet
    test__moreThan1Op__acPower2(True) # not tested yet