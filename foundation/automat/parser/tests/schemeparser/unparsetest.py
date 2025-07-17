import inspect
import pprint

from foundation.automat.parser.sorte import Schemeparser

pp = pprint.PrettyPrinter(indent=4)

def test__schemeParserTest__add(verbose=False):

    expected_ast = {
    ('=', 0):[('a', 1), ('+', 2)],
    ('+', 2):[('b', 3), ('c', 4)]
    }
    equationStr = '(= a (+ b c))'
    parser = Schemeparser(ast=expected_ast, verbose=verbose)
    # ast = parser.ast
    # pp.pprint(ast)
    unparsedStr = parser._unparse()
    rootOfTree = parser.rootOfTree
    expected_rootOfTree = ('=', 0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (equationStr==unparsedStr) and (rootOfTree==expected_rootOfTree))
    if verbose:
        pp.pprint(parser.ast)


def test__schemeParserTest__harmonicMean(verbose=False):
    #HARMONIC MEAN : https://en.wikipedia.org/wiki/Harmonic_mean

    expected_ast = {   ('+', 2): [('/', 5), ('/', 6)],
    ('/', 1): [('1', 3), ('a', 4)],
    ('/', 5): [('1', 7), ('b', 8)],
    ('/', 6): [('1', 9), ('c', 10)],
    ('=', 0): [('/', 1), ('+', 2)]}
    equationStr = '(= (/ 1 a) (+ (/ 1 b) (/ 1 c)))'
    parser = Schemeparser(ast=expected_ast, verbose=verbose)
    # ast = parser.ast
    # pp.pprint(ast)
    unparsedStr = parser._unparse()
    rootOfTree = parser.rootOfTree
    expected_rootOfTree = ('=', 0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (equationStr==unparsedStr) and (rootOfTree==expected_rootOfTree))
    if verbose:
        pp.pprint(parser.ast)


def test__schemeParserTest__phasorDiagram(verbose=False):
    #Phasor Diagram : https://en.wikipedia.org/wiki/Euler%27s_formula

    expected_ast ={   ('*', 4): [('i', 7), ('x', 8)],
    ('*', 6): [('i', 10), ('sin', 11)],
    ('+', 2): [('cos', 5), ('*', 6)],
    ('=', 0): [('^', 1), ('+', 2)],
    ('^', 1): [('e', 3), ('*', 4)],
    ('cos', 5): [('x', 9)],
    ('sin', 11): [('x', 12)]}
    equationStr = '(= (^ e (* i x)) (+ (cos x) (* i (sin x))))'
    parser = Schemeparser(ast=expected_ast, verbose=verbose)
    # ast = parser.ast
    # pp.pprint(ast)
    unparsedStr = parser._unparse()
    rootOfTree = parser.rootOfTree
    expected_rootOfTree = ('=', 0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (equationStr==unparsedStr) and (rootOfTree==expected_rootOfTree))
    if verbose:
        pp.pprint(parser.ast)


def test__schemeParserTest__ebersMollModelp1(verbose=False):
    #Ebers-Moll model : https://en.wikipedia.org/wiki/Bipolar_junction_transistor#Ebers%E2%80%93Moll_model

    expected_ast = {   
    ('*', 2): [('I_{ES}', 3), ('-', 4)],
    ('-', 4): [('^', 5), ('1', 6)],
    ('/', 8): [('V_{BE}', 9), ('V_T', 10)],
    ('=', 0): [('I_E', 1), ('*', 2)],
    ('^', 5): [('e', 7), ('/', 8)]}
    equationStr = '(= I_E (* I_{ES} (- (^ e (/ V_{BE} V_T)) 1)))'
    parser = Schemeparser(ast=expected_ast, verbose=verbose)
    # ast = parser.ast
    # pp.pprint(ast)
    unparsedStr = parser._unparse()
    rootOfTree = parser.rootOfTree
    expected_rootOfTree = ('=', 0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (equationStr==unparsedStr) and (rootOfTree==expected_rootOfTree))


def test__schemeParserTest__earlyEffectModel(verbose=False):
    #https://en.wikipedia.org/wiki/Early_effect#Large-signal_model

    expected_ast = {   ('*', 2): [('I_S', 3), ('*', 4)],
    ('*', 4): [('^', 5), ('+', 6)],
    ('+', 6): [('1', 9), ('/', 10)],
    ('/', 8): [('V_{BE}', 11), ('V_T', 12)],
    ('/', 10): [('V_{CE}', 13), ('V_A', 14)],
    ('=', 0): [('I_E', 1), ('*', 2)],
    ('^', 5): [('e', 7), ('/', 8)]}
    equationStr = '(= I_E (* I_S (* (^ e (/ V_{BE} V_T)) (+ 1 (/ V_{CE} V_A)))))'
    parser = Schemeparser(ast=expected_ast, verbose=verbose)
    # ast = parser.ast
    # pp.pprint(ast)
    unparsedStr = parser._unparse()
    rootOfTree = parser.rootOfTree
    expected_rootOfTree = ('=', 0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (equationStr==unparsedStr) and (rootOfTree==expected_rootOfTree))


def test__schemeParserTest__productRule(verbose=False):

    expected_ast = {
        ('*', 20): [('/', 1), ('*', 22)],
        ('*', 21): [('d', 6), ('x', 7)],
        ('*', 22): [('u', 8), ('v', 9)],
        ('*', 23): [('u', 10), ('/', 2)],
        ('*', 24): [('d', 11), ('v', 12)],
        ('*', 25): [('d', 13), ('x', 14)],
        ('*', 26): [('v', 15), ('/', 3)],
        ('*', 27): [('d', 16), ('u', 17)],
        ('*', 28): [('d', 18), ('x', 19)],
        ('+', 0): [('*', 23), ('*', 26)],
        ('/', 1): [('d', 5), ('*', 21)],
        ('/', 2): [('*', 24), ('*', 25)],
        ('/', 3): [('*', 27), ('*', 28)],
        ('=', 4): [('*', 20), ('+', 0)]
    }
    equationStr = '(= (* (/ d (* d x)) (* u v)) (+ (* u (/ (* d v) (* d x))) (* v (/ (* d u) (* d x)))))'
    parser = Schemeparser(ast=expected_ast, verbose=verbose)
    # ast = parser.ast
    # pp.pprint(ast)
    unparsedStr = parser._unparse()
    rootOfTree = parser.rootOfTree
    expected_rootOfTree = ('=', 4)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', (equationStr==unparsedStr) and (rootOfTree==expected_rootOfTree))

    if verbose:
        print(unparsedStr)
        print(rootOfTree)

if __name__=='__main__':
    test__schemeParserTest__add()
    test__schemeParserTest__harmonicMean()
    test__schemeParserTest__phasorDiagram()
    test__schemeParserTest__ebersMollModelp1()
    test__schemeParserTest__earlyEffectModel()
    test__schemeParserTest__productRule(True)# TODO USE in SchemeGrammarParser