import inspect
import pprint

from foundation.automat.parser.sorte import Schemeparser


def test__schemeParserTest__add(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= a (+ b c))'
    latexStr = Schemeparser(equationStr=equationStr, verbose=verbose)._toLatex()
    expected_latexStr = 'a=b+c'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (latexStr == expected_latexStr))
    if verbose:
        pp.pprint(latexStr)


def test__schemeParserTest__harmonicMean(verbose=False):
    #HARMONIC MEAN : https://en.wikipedia.org/wiki/Harmonic_mean
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= (/ 1 a) (+ (/ 1 b) (/ 1 c)))'
    latexStr = Schemeparser(equationStr=equationStr, verbose=verbose)._toLatex()
    expected_latexStr = '\\frac{1}{a}=\\frac{1}{b}+\\frac{1}{c}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (latexStr == expected_latexStr))
    if verbose:
        pp.pprint(latexStr)


def test__schemeParserTest__phasorDiagram(verbose=False):
    #Phasor Diagram : https://en.wikipedia.org/wiki/Euler%27s_formula
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= (^ e (* i x)) (+ (cos x) (* i (sin x))))'
    latexStr = Schemeparser(equationStr=equationStr, verbose=verbose)._toLatex()
    expected_latexStr = 'e^{ix}=\\cos(x)+i\\sin(x)'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (latexStr == expected_latexStr))
    if verbose:
        pp.pprint(latexStr)


def test__schemeParserTest__ebersMollModelp1(verbose=False):
    #Ebers-Moll model : https://en.wikipedia.org/wiki/Bipolar_junction_transistor#Ebers%E2%80%93Moll_model
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= I_E (* I_{ES} (- (^ e (/ V_{BE} V_T) 1))))'
    latexStr = Schemeparser(equationStr=equationStr, verbose=verbose)._toLatex()
    expected_latexStr = None
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (latexStr == expected_latexStr))
    if verbose:
        pp.pprint(latexStr)


def test__schemeParserTest__earlyEffectModel(verbose=False):
    #https://en.wikipedia.org/wiki/Early_effect#Large-signal_model
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= I_E (* I_S (* (^ e (/ V_{BE} V_T)) (+ 1 (/ V_{CE} V_A)))))'
    latexStr = Schemeparser(equationStr=equationStr, verbose=verbose)._toLatex()
    expected_latexStr = None
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (latexStr == expected_latexStr))
    if verbose:
        pp.pprint(latexStr)


if __name__=='__main__':
    # test__schemeParserTest__add()
    # test__schemeParserTest__harmonicMean(True)
    # test__schemeParserTest__phasorDiagram(True)
    # test__schemeParserTest__ebersMollModelp1(True) # does not work
    test__schemeParserTest__earlyEffectModel(True) # does not work very well with weird variables....