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
        print(latexStr)


def test__schemeParserTest__harmonicMean(verbose=False):
    #HARMONIC MEAN : https://en.wikipedia.org/wiki/Harmonic_mean
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= (/ 1 a) (+ (/ 1 b) (/ 1 c)))'
    latexStr = Schemeparser(equationStr=equationStr, verbose=verbose)._toLatex()
    expected_latexStr = '\\frac{1}{a}=\\frac{1}{b}+\\frac{1}{c}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (latexStr == expected_latexStr))
    if verbose:
        print(latexStr)


def test__schemeParserTest__phasorDiagram(verbose=False):
    #Phasor Diagram : https://en.wikipedia.org/wiki/Euler%27s_formula
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= (^ e (* i x)) (+ (cos x) (* i (sin x))))'
    latexStr = Schemeparser(equationStr=equationStr, verbose=verbose)._toLatex()
    expected_latexStr = 'e^{ix}=\\cos(x)+i\\sin(x)'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (latexStr == expected_latexStr))
    if verbose:
        print(latexStr)


def test__schemeParserTest__ebersMollModelp1(verbose=False):
    #Ebers-Moll model : https://en.wikipedia.org/wiki/Bipolar_junction_transistor#Ebers%E2%80%93Moll_model
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= I_E (* I_{ES} (- (^ e (/ V_{BE} V_T)) 1)))'
    latexStr = Schemeparser(equationStr=equationStr, verbose=verbose)._toLatex()
    expected_latexStr = 'I_E =I_{ES} (e^{\\frac{V_{BE} }{V_T}}-1)'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (latexStr == expected_latexStr))
    if verbose:
        print(latexStr)


def test__schemeParserTest__earlyEffectModel(verbose=False):
    #https://en.wikipedia.org/wiki/Early_effect#Large-signal_model
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= I_E (* I_S (* (^ e (/ V_{BE} V_T)) (+ 1 (/ V_{CE} V_A)))))'
    latexStr = Schemeparser(equationStr=equationStr, verbose=verbose)._toLatex()
    expected_latexStr = 'I_E =I_S e^{\\frac{V_{BE} }{V_T}}(1+\\frac{V_{CE} }{V_A})'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (latexStr == expected_latexStr))
    if verbose:
        print(latexStr)


if __name__=='__main__':
    test__schemeParserTest__add()
    test__schemeParserTest__harmonicMean()
    test__schemeParserTest__phasorDiagram()
    test__schemeParserTest__ebersMollModelp1()
    test__schemeParserTest__earlyEffectModel()