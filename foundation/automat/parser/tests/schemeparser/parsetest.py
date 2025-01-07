import inspect
import pprint

from foundation.automat.parser.sorte import Schemeparser


def test__schemeParserTest__add(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= a (+ b c))'
    parser = Schemeparser(equationStr=equationStr, verbose=verbose)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # ast = parser.ast
    # pp.pprint(ast)
    expected_ast = {
    ('=', 0):[('a', 1), ('+', 2)],
    ('+', 2):[('b', 3), ('c', 4)]
    }
    expected_startPos__nodeId = {1: 0, 3: 1, 6: 2, 8: 3, 10: 4}
    expected_nodeId__len = {0: 13, 1: 1, 2: 7, 3: 1, 4: 1}
    # unparsedStr = parser._unparse()
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        ast==expected_ast and \
        startPos__nodeId==expected_startPos__nodeId and \
        parser.nodeId__len==expected_nodeId__len
    )
    if verbose:
        pp.pprint(ast)
        pp.pprint(startPos__nodeId)
        pp.pprint(parser.nodeId__len)


def test__schemeParserTest__harmonicMean(verbose=False):
    #HARMONIC MEAN : https://en.wikipedia.org/wiki/Harmonic_mean
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= (/ 1 a) (+ (/ 1 b) (/ 1 c)))'
    parser = Schemeparser(equationStr=equationStr, verbose=verbose)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # ast = parser.ast
    # pp.pprint(ast)
    expected_ast = {   
    ('+', 2): [('/', 5), ('/', 6)],
    ('/', 1): [('1', 3), ('a', 4)],
    ('/', 5): [('1', 7), ('b', 8)],
    ('/', 6): [('1', 9), ('c', 10)],
    ('=', 0): [('/', 1), ('+', 2)]}
    expected_startPos__nodeId = {1: 0, 4: 1, 6: 3, 8: 4, 12: 2, 15: 5, 17: 7, 19: 8, 23: 6, 25: 9, 27: 10}
    expected_nodeId__len = {0: 31, 1: 7, 2: 19, 3: 1, 4: 1, 5: 7, 6: 7, 7: 1, 8: 1, 9: 1, 10: 1}
    # unparsedStr = parser._unparse()
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        ast==expected_ast and \
        startPos__nodeId==expected_startPos__nodeId and \
        parser.nodeId__len==expected_nodeId__len
    )
    if verbose:
        pp.pprint(ast)
        pp.pprint(startPos__nodeId)
        pp.pprint(parser.nodeId__len)


def test__schemeParserTest__phasorDiagram(verbose=False):
    #Phasor Diagram : https://en.wikipedia.org/wiki/Euler%27s_formula
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= (^ e (* i x)) (+ (cos x) (* i (sin x))))'
    parser = Schemeparser(equationStr=equationStr, verbose=verbose)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # ast = parser.ast
    # pp.pprint(ast)
    expected_ast ={   
    ('*', 4): [('i', 7), ('x', 8)],
    ('*', 6): [('i', 10), ('sin', 11)],
    ('+', 2): [('cos', 5), ('*', 6)],
    ('=', 0): [('^', 1), ('+', 2)],
    ('^', 1): [('e', 3), ('*', 4)],
    ('cos', 5): [('x', 9)],
    ('sin', 11): [('x', 12)]}
    expected_startPos__nodeId = {   
    1: 0,
    4: 1,
    6: 3,
    9: 4,
    11: 7,
    13: 8,
    18: 2,
    21: 5,
    25: 9,
    29: 6,
    31: 10,
    34: 11,
    38: 12}
    expected_nodeId__len = {   
    0: 43,
    1: 13,
    2: 25,
    3: 1,
    4: 7,
    5: 7,
    6: 13,
    7: 1,
    8: 1,
    9: 1,
    10: 1,
    11: 7,
    12: 1}
    # unparsedStr = parser._unparse()
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        ast==expected_ast and \
        startPos__nodeId==expected_startPos__nodeId and \
        parser.nodeId__len==expected_nodeId__len
    )
    if verbose:
        pp.pprint(ast)
        pp.pprint(startPos__nodeId)
        pp.pprint(parser.nodeId__len)


def test__schemeParserTest__ebersMollModelp1(verbose=False):
    #Ebers-Moll model : https://en.wikipedia.org/wiki/Bipolar_junction_transistor#Ebers%E2%80%93Moll_model
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= I_E (* I_{ES} (- (^ e (/ V_{BE} V_T)) 1)))'
    parser = Schemeparser(equationStr=equationStr, verbose=verbose)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # ast = parser.ast
    # pp.pprint(ast)
    expected_ast = {   
    ('*', 2): [('I_{ES}', 3), ('-', 4)],
    ('-', 4): [('^', 5), ('1', 6)],
    ('/', 8): [('V_{BE}', 9), ('V_T', 10)],
    ('=', 0): [('I_E', 1), ('*', 2)],
    ('^', 5): [('e', 7), ('/', 8)]}
    expected_startPos__nodeId = {1: 0, 3: 1, 8: 2, 10: 3, 18: 4, 21: 5, 23: 7, 26: 8, 28: 9, 35: 10, 41: 6}
    expected_nodeId__len = {0: 45, 1: 3, 2: 37, 3: 6, 4: 26, 5: 20, 6: 1, 7: 1, 8: 14, 9: 6, 10: 3}
    # unparsedStr = parser._unparse()
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        ast==expected_ast and \
        startPos__nodeId==expected_startPos__nodeId and \
        parser.nodeId__len==expected_nodeId__len
    )
    if verbose:
        pp.pprint(ast)
        pp.pprint(startPos__nodeId)
        pp.pprint(parser.nodeId__len)


def test__schemeParserTest__earlyEffectModel(verbose=False):
    #https://en.wikipedia.org/wiki/Early_effect#Large-signal_model
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= I_E (* I_S (* (^ e (/ V_{BE} V_T)) (+ 1 (/ V_{CE} V_A)))))'
    parser = Schemeparser(equationStr=equationStr, verbose=verbose)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # ast = parser.ast
    # pp.pprint(ast)
    expected_ast = {   
    ('*', 2): [('I_S', 3), ('*', 4)],
    ('*', 4): [('^', 5), ('+', 6)],
    ('+', 6): [('1', 9), ('/', 10)],
    ('/', 8): [('V_{BE}', 11), ('V_T', 12)],
    ('/', 10): [('V_{CE}', 13), ('V_A', 14)],
    ('=', 0): [('I_E', 1), ('*', 2)],
    ('^', 5): [('e', 7), ('/', 8)]}
    expected_startPos__nodeId = {   
    1: 0,
    3: 1,
    8: 2,
    10: 3,
    15: 4,
    18: 5,
    20: 7,
    23: 8,
    25: 11,
    32: 12,
    39: 6,
    41: 9,
    44: 10,
    46: 13,
    53: 14}
    expected_nodeId__len = {   
    0: 61,
    1: 3,
    2: 53,
    3: 3,
    4: 45,
    5: 20,
    6: 20,
    7: 1,
    8: 14,
    9: 1,
    10: 14,
    11: 6,
    12: 3,
    13: 6,
    14: 3}
    # unparsedStr = parser._unparse()
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        ast==expected_ast and \
        startPos__nodeId==expected_startPos__nodeId and \
        parser.nodeId__len==expected_nodeId__len
    )
    if verbose:
        pp.pprint(ast)
        pp.pprint(startPos__nodeId)
        pp.pprint(parser.nodeId__len)


def test__makeSubject__linearEliminationBySubstitution(verbose=False):
    #https://en.wikipedia.org/wiki/Early_effect#Large-signal_model
    pp = pprint.PrettyPrinter(indent=4)

    equationStr = '(= (* I_{R} R) (- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0))'
    parser = Schemeparser(equationStr=equationStr, verbose=verbose)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # ast = parser.ast
    # pp.pprint(ast)
    expected_ast = {   
    ('*', 1): [('I_{R}', 3), ('R', 4)],
    ('*', 7): [('I_{R_{C}}', 9), ('R_{C}', 10)],
    ('-', 2): [('-', 5), ('0', 6)],
    ('-', 5): [('*', 7), ('V^{Q1}_{BE}', 8)],
    ('=', 0): [('*', 1), ('-', 2)]}
    expected_startPos__nodeId = {1: 0, 4: 1, 6: 3, 12: 4, 16: 2, 19: 5, 22: 7, 24: 9, 34: 10, 41: 8, 54: 6}
    expected_nodeId__len = None
    # unparsedStr = parser._unparse()
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        ast==expected_ast and \
        startPos__nodeId==expected_startPos__nodeId and \
        parser.nodeId__len==expected_nodeId__len
    )
    if verbose:
        pp.pprint(ast)
        pp.pprint(startPos__nodeId)
        pp.pprint(parser.nodeId__len)


if __name__=='__main__':
    test__schemeParserTest__add()
    test__schemeParserTest__harmonicMean()
    test__schemeParserTest__phasorDiagram()
    test__schemeParserTest__ebersMollModelp1()
    test__schemeParserTest__earlyEffectModel()
    # test__makeSubject__linearEliminationBySubstitution(True) # untested because simplify is simply not ready!