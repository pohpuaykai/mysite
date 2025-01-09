import inspect
import pprint

# from foundation.automat.core.equation import Equation
from foundation.automat.parser.sorte import Schemeparser


pp = pprint.PrettyPrinter(indent=4)


def test__startPosNodeId__makeSubject0(verbose=False):
    astScheme = {   
    ('*', 4): [('I_{R}', 7), ('R', 8)],
    ('*', 5): [('I_{R_{C}}', 9), ('R_{C}', 10)],
    ('-', 1): [('-', 3), ('*', 4)],
    ('-', 3): [('*', 5), ('V^{Q1}_{BE}', 6)],
    ('=', 0): [('-', 1), ('0', 2)]}
    parser = Schemeparser(ast=astScheme) # doing it this way to preserve the IDs
    schemeWord = parser._unparse()
    expected__schemeWord = '(= (- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) (* I_{R} R)) 0)'
    expected__nodeId__len = {0: 57, 1: 51, 2: 1, 3: 35, 4: 11, 5: 19, 6: 11, 7: 5, 8: 1, 9: 9, 10: 5}
    #startPos is the label, so if the node is a function it will exclude the starting OpenBracket
    expected__startPos__nodeId = {1: 0, 4: 1, 7: 3, 10: 5, 12: 9, 22: 10, 29: 6, 43: 4, 45: 7, 51: 8, 55: 2}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected__schemeWord == schemeWord and
        parser.nodeId__len == expected__nodeId__len and 
        parser.startPos__nodeId == expected__startPos__nodeId
    )
    if verbose:
        print('OG: ', schemeWord)
        pp.pprint(astScheme)
        print('nodeId__len')
        pp.pprint(parser.nodeId__len)
        print('startPos__nodeId')
        pp.pprint(parser.startPos__nodeId)


def test__startPosNodeId__makeSubject1(verbose=False):
    astScheme = {   
    ('*', 4): [('I_{R}', 7), ('R', 8)],
    ('*', 5): [('I_{R_{C}}', 9), ('R_{C}', 10)],
    ('-', 1): [('-', 3), ('0', 2)],
    ('-', 3): [('*', 5), ('V^{Q1}_{BE}', 6)],
    ('=', 0): [('*', 4), ('-', 1)]}
    parser = Schemeparser(ast=astScheme) # doing it this way to preserve the IDs
    schemeWord = parser._unparse()
    expected__schemeWord = '(= (* I_{R} R) (- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0))'
    expected__nodeId__len = {0: 57, 1: 41, 2: 1, 3: 35, 4: 11, 5: 19, 6: 11, 7: 5, 8: 1, 9: 9, 10: 5}
    #startPos is the label, so if the node is a function it will exclude the starting OpenBracket
    expected__startPos__nodeId = {1: 0, 4: 4, 6: 7, 12: 8, 16: 1, 19: 3, 22: 5, 24: 9, 34: 10, 41: 6, 54: 2}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected__schemeWord == schemeWord and
        parser.nodeId__len == expected__nodeId__len and 
        parser.startPos__nodeId == expected__startPos__nodeId
    )
    if verbose:
        print('OG: ', schemeWord)
        pp.pprint(astScheme)
        print('nodeId__len')
        pp.pprint(parser.nodeId__len)
        print('startPos__nodeId')
        pp.pprint(parser.startPos__nodeId)


def test__startPosNodeId__makeSubject2(verbose=False):
    astScheme = {   
    ('*', 5): [('I_{R_{C}}', 9), ('R_{C}', 10)],
    ('-', 1): [('-', 3), ('0', 2)],
    ('-', 3): [('*', 5), ('V^{Q1}_{BE}', 6)],
    ('/', 4): [('-', 1), ('R', 8)],
    ('=', 0): [('I_{R}', 7), ('/', 4)]}
    parser = Schemeparser(ast=astScheme) # doing it this way to preserve the IDs
    schemeWord = parser._unparse()
    expected__schemeWord = '(= I_{R} (/ (- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0) R))'
    expected__nodeId__len = {0: 57, 1: 41, 2: 1, 3: 35, 4: 47, 5: 19, 6: 11, 7: 5, 8: 1, 9: 9, 10: 5}
    #startPos is the label, so if the node is a function it will exclude the starting OpenBracket
    expected__startPos__nodeId = {1: 0, 3: 7, 10: 4, 13: 1, 16: 3, 19: 5, 21: 9, 31: 10, 38: 6, 51: 2, 54: 8}
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected__schemeWord == schemeWord and
        parser.nodeId__len == expected__nodeId__len and 
        parser.startPos__nodeId == expected__startPos__nodeId
    )
    if verbose:
        print('OG: ', schemeWord)
        pp.pprint(astScheme)
        print('nodeId__len')
        pp.pprint(parser.nodeId__len)
        print('startPos__nodeId')
        pp.pprint(parser.startPos__nodeId)



if __name__=='__main__':
    test__startPosNodeId__makeSubject0()
    test__startPosNodeId__makeSubject1()
    test__startPosNodeId__makeSubject2()