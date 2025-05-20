import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser, BracketStorage, BracketType, EntityStorage, EntityType

pp = pprint.PrettyPrinter(indent=4)



# def test__remove_space0(verbose=False):
#     #from https://en.wikipedia.org/wiki/Quaternionic_matrix
    
#     equationStr = " a + bi + cj + dk =  \\begin{pmatrix} a+ bi&c+d i  \\\\-c+di &a  -bi \\\\ \\end{pmatrix}"
#     parser = Latexparser(equationStr, verbose=verbose)
#     parser._remove_all_spacing()
#     expected_equationStr = 'a+bi+cj+dk=\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}'
#     print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
#         expected_equationStr == parser.equationStr
#     )
#     if verbose:
#         print(parser.equationStr)
        

def test__find_matrices0(verbose=False):
    #(a+bi+cj+dk)(a+bi+cj+dk)
    
    equationStr = "\\begin{pmatrix}(a^2-b^2-c^2-d^2)+i(2ab)&2ac+i(2ad)\\\\-2ac+i(2ad)&(a^2+b^2-c^2-d^2)-i(2ab)\\\\\\end{pmatrix}=\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}"
    parser = Latexparser(equationStr, verbose=verbose)
    # parser._remove_all_spacing()
    parser._find_matrices()

    expected_list_tuple_widthStart_nodeId = [(0, 0), (104, 1), (155, 2)]
    expected_list_tuple_widthEnd_nodeId = [(103, 0), (155, 1), (206, 2)]
    expected_nodeId__widthStart = {0: 0, 1: 104, 2: 155}
    expected_nodeId__widthEnd = {0: 103, 1: 155, 2: 206}
    expected_entityType__list_nodeId = {EntityType.MATRIX: [0, 1, 2]}
    expected_funcStart__nodeId = {0: 0, 104: 1, 155: 2}
    expected_funcName__list_nodeId = {'pmatrix': [0, 1, 2]}
    expected_nodeId__entityType = {
        0: EntityType.MATRIX,
        1: EntityType.MATRIX,
        2: EntityType.MATRIX}
    expected_nodeId__funcName = {0: 'pmatrix', 1: 'pmatrix', 2: 'pmatrix'}
    expected_nodeId__funcStart = {0: 0, 1: 104, 2: 155}
    expected_nodeId__funcEnd = {0: 103, 1: 155, 2: 206}
    expected_tuple_nodeId_argIdx__pNodeId = {}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        parser.entitystorage.list_tuple_widthStart_nodeId == expected_list_tuple_widthStart_nodeId\
        and parser.entitystorage.list_tuple_widthEnd_nodeId == expected_list_tuple_widthEnd_nodeId\
        and parser.entitystorage.nodeId__widthStart == expected_nodeId__widthStart\
        and parser.entitystorage.nodeId__widthEnd == expected_nodeId__widthEnd\
        and parser.entitystorage.entityType__list_nodeId == expected_entityType__list_nodeId\
        and parser.entitystorage.funcStart__nodeId == expected_funcStart__nodeId\
        and parser.entitystorage.funcName__list_nodeId == expected_funcName__list_nodeId\
        and parser.entitystorage.nodeId__entityType == expected_nodeId__entityType\
        and parser.entitystorage.nodeId__funcName == expected_nodeId__funcName\
        and parser.entitystorage.nodeId__funcStart == expected_nodeId__funcStart\
        and parser.entitystorage.nodeId__funcEnd == expected_nodeId__funcEnd\
        and parser.entitystorage.tuple_nodeId_argIdx__pNodeId == expected_tuple_nodeId_argIdx__pNodeId\
        and parser.entitystorage.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos\
        
    )
    if verbose:
        print(str(parser.entitystorage))

def test___isPosInMatrixTag0(verbose=False):
    """
\\begin{pmatrix}(a^2-b^2-c^2-d^2)+i(2ab)&2ac+i(2ad)\\\\-2ac+i(2ad)&(a^2+b^2-c^2-d^2)-i(2ab)\\\\\\end{pmatrix}=\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}
^                                                                                                            ^^                                                        ^               
0                                                                                                            11                                                        1
                                                                                                             00                                                        5
                                                                                                             34                                                        4
    """
    #(a+bi+cj+dk)(a+bi+cj+dk)

    equationStr = "\\begin{pmatrix}(a^2-b^2-c^2-d^2)+i(2ab)&2ac+i(2ad)\\\\-2ac+i(2ad)&(a^2+b^2-c^2-d^2)-i(2ab)\\\\\\end{pmatrix}=\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}"
    parser = Latexparser(equationStr, verbose=verbose)
    # parser._remove_all_spacing()
    parser._find_matrices()
    has = parser.isPosInMatrixTag(120)

    expected_has = True

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        has == expected_has
        )
    if verbose:
        print(str(parser.entitystorage))
        print(has)


def test__find_infix0(verbose=False): #TODO infix test for \\to;\\cross;\\cdot
    """
    #\forall k \\in \\Z^+ and \forall prime_number p, equationStr = 1 | -1 a multivalue function

(\\frac{p+1}{2})*((p-1)/2)^{(k-1)(p-1)/2})\\%p=-1
^^ ^   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^
01 2   678911111111112222222222333333333344 44444
           01234567890123456789012345678901 23456

    """
    
    equationStr = "(\\frac{p+1}{2})*((p-1)/2)^{(k-1)(p-1)/2})\\%p=-1"
    parser = Latexparser(equationStr, verbose=verbose)
    # parser._remove_all_spacing()
    parser._find_matrices()
    parser._find_infix()

    expected_list_tuple_widthStart_nodeId = [(8, 10),(15, 5),(19, 6),(22, 3),(25, 2),(29, 7),(34, 8),(37, 4),(41, 1),(44, 0),(45, 9)]
    expected_list_tuple_widthEnd_nodeId = [(9, 10), (16, 5), (20, 6), (23, 3), (26, 2), (30, 7), (35, 8), (38, 4), (43, 1), (45, 0), (46, 9)]
    expected_nodeId__widthStart = {0: 44, 1: 41, 2: 25, 3: 22, 4: 37, 5: 15, 6: 19, 7: 29, 8: 34, 9: 45, 10: 8}
    expected_nodeId__widthEnd = {0: 45, 1: 43, 2: 26, 3: 23, 4: 38, 5: 16, 6: 20, 7: 30, 8: 35, 9: 46, 10: 9}
    expected_entityType__list_nodeId = {EntityType.PURE_INFIX: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    expected_funcStart__nodeId = {8: 10, 15: 5, 19: 6, 22: 3, 25: 2, 29: 7, 34: 8, 37: 4, 41: 1, 44: 0, 45: 9}
    expected_funcName__list_nodeId = {
    '*': [5],
    '+': [10],
    '-': [6, 7, 8, 9],
    '/': [3, 4],
    '=': [0],
    '\\%': [1],
    '^': [2]}
    expected_nodeId__entityType = {
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    2: EntityType.PURE_INFIX,
    3: EntityType.PURE_INFIX,
    4: EntityType.PURE_INFIX,
    5: EntityType.PURE_INFIX,
    6: EntityType.PURE_INFIX,
    7: EntityType.PURE_INFIX,
    8: EntityType.PURE_INFIX,
    9: EntityType.PURE_INFIX,
    10: EntityType.PURE_INFIX}
    expected_nodeId__funcName = {
    0: '=',
    1: '\\%',
    2: '^',
    3: '/',
    4: '/',
    5: '*',
    6: '-',
    7: '-',
    8: '-',
    9: '-',
    10: '+'}
    expected_nodeId__funcStart = {0: 44, 1: 41, 2: 25, 3: 22, 4: 37, 5: 15, 6: 19, 7: 29, 8: 34, 9: 45, 10: 8}
    expected_nodeId__funcEnd = {0: 45, 1: 43, 2: 26, 3: 23, 4: 38, 5: 16, 6: 20, 7: 30, 8: 35, 9: 46, 10: 9}
    expected_tuple_nodeId_argIdx__pNodeId = {}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {
    (0, 0): (None, 0, None, 44),
    (0, 1): (None, 44, None, 47),
    (1, 0): (None, 0, None, 41),
    (1, 1): (None, 41, None, 47),
    (2, 0): (None, 0, None, 25),
    (2, 1): (None, 25, None, 47),
    (3, 0): (None, 0, None, 22),
    (3, 1): (None, 22, None, 47),
    (4, 0): (None, 0, None, 37),
    (4, 1): (None, 37, None, 47),
    (5, 0): (None, 0, None, 15),
    (5, 1): (None, 15, None, 47),
    (6, 0): (None, 0, None, 19),
    (6, 1): (None, 19, None, 47),
    (7, 0): (None, 0, None, 29),
    (7, 1): (None, 29, None, 47),
    (8, 0): (None, 0, None, 34),
    (8, 1): (None, 34, None, 47),
    (9, 0): (None, 0, None, 45),
    (9, 1): (None, 45, None, 47),
    (10, 0): (None, 0, None, 8),
    (10, 1): (None, 8, None, 47)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        parser.entitystorage.list_tuple_widthStart_nodeId == expected_list_tuple_widthStart_nodeId\
        and parser.entitystorage.list_tuple_widthEnd_nodeId == expected_list_tuple_widthEnd_nodeId\
        and parser.entitystorage.nodeId__widthStart == expected_nodeId__widthStart\
        and parser.entitystorage.nodeId__widthEnd == expected_nodeId__widthEnd\
        and parser.entitystorage.entityType__list_nodeId == expected_entityType__list_nodeId\
        and parser.entitystorage.funcStart__nodeId == expected_funcStart__nodeId\
        and parser.entitystorage.funcName__list_nodeId == expected_funcName__list_nodeId\
        and parser.entitystorage.nodeId__entityType == expected_nodeId__entityType\
        and parser.entitystorage.nodeId__funcName == expected_nodeId__funcName\
        and parser.entitystorage.nodeId__funcStart == expected_nodeId__funcStart\
        and parser.entitystorage.nodeId__funcEnd == expected_nodeId__funcEnd\
        and parser.entitystorage.tuple_nodeId_argIdx__pNodeId == expected_tuple_nodeId_argIdx__pNodeId\
        and parser.entitystorage.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos\
        
    )
    if verbose:
        print(str(parser.entitystorage))

def test__find_brackets0(verbose=False):
    """
\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}f(x)e^{-i2\\pi\\frac{n}{P}x}dx}(e^{i2\\pi\\frac{n}{P}x})}
      ^                  ^^      ^          ^ ^       ^^      ^ ^^ ^      ^   ^ ^    ^ ^ ^  ^             ^ ^^ ^ ^  ^^  ^            ^ ^^ ^ ^^^
      5                  22      2          3 4       44      5 55 5      6   6 7    7 7 8  8             9 99 1 1  11  1            1 11 1 111
                         12      8          8 0       78      4 67 9      5   9 1    6 8 0  3             5 78 0 0  00  0            2 22 2 222
                                                                                                               0 2  56  9            0 23 5 789
    """
    #Fourier transform
    equationStr = "\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2} f(x)e^{-i2\\pi\\frac{n}{P}x}dx}(e^{i2\\pi\\frac{n}{P}x})}"
    parser = Latexparser(equationStr, verbose=verbose)
    # parser._remove_all_spacing()
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {   
    0: (5, '{', 21, '}'),
    1: (28, '{', 38, '}'),
    2: (40, '{', 47, '}'),
    3: (54, '{', 56, '}'),
    4: (57, '{', 59, '}'),
    5: (65, '{', 69, '}'),
    6: (71, '{', 76, '}'),
    7: (78, '(', 80, ')'),
    8: (95, '{', 97, '}'),
    9: (98, '{', 100, '}'),
    10: (83, '{', 102, '}'),
    11: (48, '{', 105, '}'),
    12: (120, '{', 122, '}'),
    13: (123, '{', 125, '}'),
    14: (109, '{', 127, '}'),
    15: (106, '(', 128, ')'),
    16: (22, '{', 129, '}')}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
parser.bracketstorage.id__tuple_openPos_openBraType_closePos_closeBraType == expected_id__tuple_openPos_openBraType_closePos_closeBraType
        )
    if verbose:
        print(str(parser.bracketstorage))


def test__find_backslash0(verbose=False):#<<<<<<<<<<<<<<<<<<<also test with matrix, might give problem
    """
    
\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}{f(x)e^{-i2\\pi\\frac{n}{P}x}dx}(e^{i2\\pi\\frac{n}{P}x})}}
^ ^^^^^^ ^^^^^^ ^^^ ^^^^^^^^ ^^^^^^^^^ ^^^^^^^^^ ^^^^^^^^ ^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^^ ^^^ ^^^^^^^^^^^^^^^^^^^^^^ ^^^ ^^^^^^^^^^^^^^^
0 123456 789111 111 11112222 222222333 333333344 44444444 55555555556 6666666667777777777888888888 899 9999999911111111111111 111 111111111111111
            012 345 67890123 456789012 345678901 23456789 01234567890 1234567890123456789012345678 901 2345678900000000001111 111 111222222222233
                                                                                                               01234567890123 456 789012345678901
                                                                                                               
    """
    #Fourier transform
    equationStr = "\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}{f(x)e^{-i2\\pi\\frac{n}{P}x}dx}(e^{i2\\pi\\frac{n}{P}x})}}"
    parser = Latexparser(equationStr, verbose=verbose)
    # parser._remove_all_spacing()
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()

    expected_closeBraType__sortedPosList = {')': [81, 129], '}': [103, 128]}
    expected_openBraType__sortedPosList = {'(': [79, 107], '{': [84, 110]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {   
        7: (79, '(', 81, ')'),
        10: (84, '{', 103, '}'),
        14: (110, '{', 128, '}'),
        15: (107, '(', 129, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(2, 7, 79, 81), (18, 14, 110, 128), (19, 10, 84, 103), (22, 15, 107, 129)]
    expected_openBraPos__bracketId = {79: 7, 84: 10, 107: 15, 110: 14}
    expected_closeBraPos__bracketId = {81: 7, 103: 10, 128: 14, 129: 15}
    expected_list_tuple_widthStart_nodeId = [   
    (0, 11),
    (6, 12),
    (12, 1),
    (15, 13),
    (23, 14),
    (30, 0),
    (31, 8),
    (32, 15),
    (41, 16),
    (49, 17),
    (60, 18),
    (67, 6),
    (72, 9),
    (74, 7),
    (83, 4),
    (85, 10),
    (88, 19),
    (91, 20),
    (109, 5),
    (113, 21),
    (116, 22)]
    expected_list_tuple_widthEnd_nodeId = [
    (12, 12),
    (21, 13),
    (132, 11),
    (15, 1),
    (131, 14),
    (31, 0),
    (32, 8),
    (38, 15),
    (47, 16),
    (60, 17),
    (107, 18),
    (68, 6),
    (73, 9),
    (75, 7),
    (84, 4),
    (86, 10),
    (91, 19),
    (102, 20),
    (110, 5),
    (116, 21),
    (127, 22)]
    expected_nodeId__widthStart = {
        0: 30,
        1: 12,
        4: 83,
        5: 109,
        6: 67,
        7: 74,
        8: 31,
        9: 72,
        10: 85,
        11: 0,
        12: 6,
        13: 15,
        14: 23,
        15: 32,
        16: 41,
        17: 49,
        18: 60,
        19: 88,
        20: 91,
        21: 113,
        22: 116}

    expected_nodeId__widthEnd = {
        0: 31,
        1: 15,
        4: 84,
        5: 110,
        6: 68,
        7: 75,
        8: 32,
        9: 73,
        10: 86,
        11: 132,
        12: 12,
        13: 21,
        14: 131,
        15: 38,
        16: 47,
        17: 60,
        18: 107,
        19: 91,
        20: 102,
        21: 116,
        22: 127}
    expected_entityType__list_nodeId = {
        EntityType.PURE_INFIX: [0, 1, 4, 5, 6, 7, 8, 9, 10],
        EntityType.BACKSLASH_NUMBER: [12, 13, 15, 16, 19, 21],
        EntityType.BACKSLASH_FUNCTION: [11, 14, 17, 18, 20, 22]}
    expected_funcStart__nodeId = {
        0: 11,
        6: 12,
        12: 1,
        15: 13,
        23: 14,
        30: 0,
        31: 8,
        32: 15,
        41: 16,
        49: 17,
        60: 18,
        67: 6,
        72: 9,
        74: 7,
        83: 4,
        85: 10,
        88: 19,
        91: 20,
        109: 5,
        113: 21,
        116: 22}
    expected_funcName__list_nodeId = {
        '-': [8, 9, 10],
        '/': [6, 7],
        '=': [0],
        '\\to': [1],
        '^': [4, 5],
        'frac': [17, 20, 22],
        'infty': [13],
        'int': [18],
        'lim': [11],
        'pi': [19, 21],
        'sum': [14],
        'theta': [12, 15, 16]}
    expected_nodeId__entityType = {
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    4: EntityType.PURE_INFIX,
    5: EntityType.PURE_INFIX,
    6: EntityType.PURE_INFIX,
    7: EntityType.PURE_INFIX,
    8: EntityType.PURE_INFIX,
    9: EntityType.PURE_INFIX,
    10: EntityType.PURE_INFIX,
    11: EntityType.BACKSLASH_FUNCTION,
    12: EntityType.BACKSLASH_NUMBER,
    13: EntityType.BACKSLASH_NUMBER,
    14: EntityType.BACKSLASH_FUNCTION,
    15: EntityType.BACKSLASH_NUMBER,
    16: EntityType.BACKSLASH_NUMBER,
    17: EntityType.BACKSLASH_FUNCTION,
    18: EntityType.BACKSLASH_FUNCTION,
    19: EntityType.BACKSLASH_NUMBER,
    20: EntityType.BACKSLASH_FUNCTION,
    21: EntityType.BACKSLASH_NUMBER,
    22: EntityType.BACKSLASH_FUNCTION}
    expected_nodeId__funcName = {
    0: '=',
    1: '\\to',
    4: '^',
    5: '^',
    6: '/',
    7: '/',
    8: '-',
    9: '-',
    10: '-',
    11: 'lim',
    12: 'theta',
    13: 'infty',
    14: 'sum',
    15: 'theta',
    16: 'theta',
    17: 'frac',
    18: 'int',
    19: 'pi',
    20: 'frac',
    21: 'pi',
    22: 'frac'}
    expected_nodeId__funcStart = {
    0: 30,
    1: 12,
    4: 83,
    5: 109,
    6: 67,
    7: 74,
    8: 31,
    9: 72,
    10: 85,
    11: 0,
    12: 6,
    13: 15,
    14: 23,
    15: 32,
    16: 41,
    17: 49,
    18: 60,
    19: 88,
    20: 91,
    21: 113,
    22: 116}
    expected_nodeId__funcEnd = {
    0: 31,
    1: 15,
    4: 84,
    5: 110,
    6: 68,
    7: 75,
    8: 32,
    9: 73,
    10: 86,
    11: 4,
    12: 12,
    13: 21,
    14: 27,
    15: 38,
    16: 47,
    17: 54,
    18: 64,
    19: 91,
    20: 96,
    21: 116,
    22: 121}
    expected_tuple_nodeId_argIdx__pNodeId = {}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {
    (0, 0): (None, 0, None, 30),
    (0, 1): (None, 30, None, 132),
    (1, 0): (None, 0, None, 12),
    (1, 1): (None, 12, None, 132),
    (4, 0): (None, 0, None, 83),
    (4, 1): (None, 83, None, 132),
    (5, 0): (None, 0, None, 109),
    (5, 1): (None, 109, None, 132),
    (6, 0): (None, 0, None, 67),
    (6, 1): (None, 67, None, 132),
    (7, 0): (None, 0, None, 74),
    (7, 1): (None, 74, None, 132),
    (8, 0): (None, 0, None, 31),
    (8, 1): (None, 31, None, 132),
    (9, 0): (None, 0, None, 72),
    (9, 1): (None, 72, None, 132),
    (10, 0): (None, 0, None, 85),
    (10, 1): (None, 85, None, 132),
    (11, 0): ('{', 5, '}', 21),
    (11, 1): ('{', 22, '}', 131),
    (14, 0): ('{', 28, '}', 38),
    (14, 1): ('{', 40, '}', 47),
    (14, 2): ('{', 48, '}', 130),
    (17, 0): ('{', 54, '}', 56),
    (17, 1): ('{', 57, '}', 59),
    (18, 0): ('{', 65, '}', 69),
    (18, 1): ('{', 71, '}', 76),
    (18, 2): ('{', 77, '}', 106),
    (20, 0): ('{', 96, '}', 98),
    (20, 1): ('{', 99, '}', 101),
    (22, 0): ('{', 121, '}', 123),
    (22, 1): ('{', 124, '}', 126)}


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == parser.bracketstorage.closeBraType__sortedPosList \
        and expected_openBraType__sortedPosList == parser.bracketstorage.openBraType__sortedPosList \
        and expected_id__tuple_openPos_openBraType_closePos_closeBraType == parser.bracketstorage.id__tuple_openPos_openBraType_closePos_closeBraType\
        and expected_list_tuple_width_id_openPos_closePos == parser.bracketstorage.list_tuple_width_id_openPos_closePos\
        and expected_openBraPos__bracketId == parser.bracketstorage.openBraPos__bracketId\
        and expected_closeBraPos__bracketId == parser.bracketstorage.closeBraPos__bracketId\
        and expected_list_tuple_widthStart_nodeId == parser.entitystorage.list_tuple_widthStart_nodeId\
        and expected_list_tuple_widthEnd_nodeId == parser.entitystorage.list_tuple_widthEnd_nodeId\
        and expected_nodeId__widthStart == parser.entitystorage.nodeId__widthStart\
        and expected_nodeId__widthEnd == parser.entitystorage.nodeId__widthEnd\
        and expected_entityType__list_nodeId == parser.entitystorage.entityType__list_nodeId\
        and expected_funcStart__nodeId == parser.entitystorage.funcStart__nodeId\
        and expected_funcName__list_nodeId == parser.entitystorage.funcName__list_nodeId\
        and expected_nodeId__entityType == parser.entitystorage.nodeId__entityType\
        and expected_nodeId__funcName == parser.entitystorage.nodeId__funcName\
        and expected_nodeId__funcStart == parser.entitystorage.nodeId__funcStart\
        and expected_nodeId__funcEnd == parser.entitystorage.nodeId__funcEnd\
        and expected_tuple_nodeId_argIdx__pNodeId == parser.entitystorage.tuple_nodeId_argIdx__pNodeId\
        and expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == parser.entitystorage.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos
    )
    if verbose:
        print(str(parser.bracketstorage))
        print(str(parser.entitystorage))
        

def test__find_variables_or_numbers0(verbose=False):
    """
\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}{f(x)e^{-i 2\\pi\\frac{n}{P}x}dx}(e^{i 2\\pi\\frac{n}{P}x})}}
^ ^^^^^^ ^^^^^^ ^^^ ^^^^^^^^ ^^^^^^^^^ ^^^^^^^^^ ^^^^^^^^ ^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^ ^^^ ^^^^^^^^^^^^^^^^^^^^^^^ ^^^ ^^^^^^^^^^^^^^^
0 123456 789111 111 11112222 222222333 333333344 44444444 55555555556 66666666677777777778888888888 999 99999991111111111111111 111 111111111111111
            012 345 67890123 456789012 345678901 23456789 01234567890 12345678901234567890123456789 012 34567890000000000111111 111 122222222223333
                                                                                                               0123456789012345 678 901234567890123

                                                                                                               
    """
    #Fourier transform
    equationStr = "\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}{f(x)e^{-i 2\\pi\\frac{n}{P}x}dx}(e^{i 2\\pi\\frac{n}{P}x})}}"
    parser = Latexparser(equationStr, verbose=verbose)
    # parser._remove_all_spacing()
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()


    expected_closeBraType__sortedPosList = {')': [81, 131], '}': [104, 130]}
    expected_openBraType__sortedPosList = {'(': [79, 108], '{': [84, 111]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {
        7: (79, '(', 81, ')'),
        10: (84, '{', 104, '}'),
        14: (111, '{', 130, '}'),
        15: (108, '(', 131, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(2, 7, 79, 81), (19, 14, 111, 130), (20, 10, 84, 104), (23, 15, 108, 131)]
    expected_openBraPos__bracketId = {79: 7, 84: 10, 108: 15, 111: 14}
    expected_closeBraPos__bracketId = {81: 7, 104: 10, 130: 14, 131: 15}


    expected_list_tuple_widthStart_nodeId = [   (0, 11),
    (6, 12),
    (12, 1),
    (15, 13),
    (23, 14),
    (29, 23),
    (30, 0),
    (31, 8),
    (32, 15),
    (41, 16),
    (49, 17),
    (55, 24),
    (58, 25),
    (60, 18),
    (66, 26),
    (67, 6),
    (68, 27),
    (72, 9),
    (73, 28),
    (74, 7),
    (75, 29),
    (78, 30),
    (80, 31),
    (82, 32),
    (83, 4),
    (85, 10),
    (86, 33),
    (87, 34),
    (89, 19),
    (92, 20),
    (98, 35),
    (101, 36),
    (103, 37),
    (105, 38),
    (109, 39),
    (110, 5),
    (112, 40),
    (113, 41),
    (115, 21),
    (118, 22),
    (124, 42),
    (127, 43),
    (129, 44)]
    expected_list_tuple_widthEnd_nodeId = [
    (12, 12),
    (21, 13),
    (30, 23),
    (134, 11),
    (15, 1),
    (56, 24),
    (133, 14),
    (31, 0),
    (32, 8),
    (38, 15),
    (47, 16),
    (59, 25),
    (60, 17),
    (67, 26),
    (69, 27),
    (104, 32),
    (89, 34),
    (102, 36),
    (107, 38),
    (108, 18),
    (68, 6),
    (73, 9),
    (74, 28),
    (75, 7),
    (76, 29),
    (79, 30),
    (81, 31),
    (84, 4),
    (86, 10),
    (87, 33),
    (92, 19),
    (99, 35),
    (103, 20),
    (104, 37),
    (130, 39),
    (111, 5),
    (113, 40),
    (115, 41),
    (118, 21),
    (125, 42),
    (128, 43),
    (129, 22),
    (130, 44)]
    expected_nodeId__widthStart = {
    0: 30,
    1: 12,
    4: 83,
    5: 110,
    6: 67,
    7: 74,
    8: 31,
    9: 72,
    10: 85,
    11: 0,
    12: 6,
    13: 15,
    14: 23,
    15: 32,
    16: 41,
    17: 49,
    18: 60,
    19: 89,
    20: 92,
    21: 115,
    22: 118,
    23: 29,
    24: 55,
    25: 58,
    26: 66,
    27: 68,
    28: 73,
    29: 75,
    30: 78,
    31: 80,
    32: 82,
    33: 86,
    34: 87,
    35: 98,
    36: 101,
    37: 103,
    38: 105,
    39: 109,
    40: 112,
    41: 113,
    42: 124,
    43: 127,
    44: 129}
    expected_nodeId__widthEnd = {
        0: 31,
        1: 15,
        4: 84,
        5: 111,
        6: 68,
        7: 75,
        8: 32,
        9: 73,
        10: 86,
        11: 134,
        12: 12,
        13: 21,
        14: 133,
        15: 38,
        16: 47,
        17: 60,
        18: 108,
        19: 92,
        20: 103,
        21: 118,
        22: 129,
        23: 30,
        24: 56,
        25: 59,
        26: 67,
        27: 69,
        28: 74,
        29: 76,
        30: 79,
        31: 81,
        32: 104,
        33: 87,
        34: 89,
        35: 99,
        36: 102,
        37: 104,
        38: 107,
        39: 130,
        40: 113,
        41: 115,
        42: 125,
        43: 128,
        44: 130
        }
    expected_entityType__list_nodeId = {
        EntityType.PURE_NUMBER: [24, 27, 29, 34, 41],
        EntityType.BACKSLASH_NUMBER: [12, 13, 15, 16, 19, 21],
        EntityType.PURE_VARIABLE: [   23,
                                                     25,
                                                     26,
                                                     28,
                                                     30,
                                                     31,
                                                     32,
                                                     33,
                                                     35,
                                                     36,
                                                     37,
                                                     38,
                                                     39,
                                                     40,
                                                     42,
                                                     43,
                                                     44],
        EntityType.PURE_INFIX: [0, 1, 4, 5, 6, 7, 8, 9, 10],
        EntityType.BACKSLASH_FUNCTION: [   11,
                                                               14,
                                                               17,
                                                               18,
                                                               20,
                                                               22]}
    expected_funcStart__nodeId = {
        0: 11,
        6: 12,
        12: 1,
        15: 13,
        23: 14,
        29: 23,
        30: 0,
        31: 8,
        32: 15,
        41: 16,
        49: 17,
        55: 24,
        58: 25,
        60: 18,
        66: 26,
        67: 6,
        68: 27,
        72: 9,
        73: 28,
        74: 7,
        75: 29,
        78: 30,
        80: 31,
        82: 32,
        83: 4,
        85: 10,
        86: 33,
        87: 34,
        89: 19,
        92: 20,
        98: 35,
        101: 36,
        103: 37,
        105: 38,
        109: 39,
        110: 5,
        112: 40,
        113: 41,
        115: 21,
        118: 22,
        124: 42,
        127: 43,
        129: 44}
    expected_funcName__list_nodeId = {
    '-': [8, 9, 10],
    '/': [6, 7],
    '1': [24],
    '2': [27, 29, 34, 41],
    '=': [0],
    'P': [25, 26, 28, 36, 43],
    '\\to': [1],
    '^': [4, 5],
    'dx': [38],
    'e': [32, 39],
    'f': [30],
    'frac': [17, 20, 22],
    'i': [33, 40],
    'infty': [13],
    'int': [18],
    'lim': [11],
    'n': [23, 35, 42],
    'pi': [19, 21],
    'sum': [14],
    'theta': [12, 15, 16],
    'x': [31, 37, 44]}
    expected_nodeId__entityType = {
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    4: EntityType.PURE_INFIX,
    5: EntityType.PURE_INFIX,
    6: EntityType.PURE_INFIX,
    7: EntityType.PURE_INFIX,
    8: EntityType.PURE_INFIX,
    9: EntityType.PURE_INFIX,
    10: EntityType.PURE_INFIX,
    11: EntityType.BACKSLASH_FUNCTION,
    12: EntityType.BACKSLASH_NUMBER,
    13: EntityType.BACKSLASH_NUMBER,
    14: EntityType.BACKSLASH_FUNCTION,
    15: EntityType.BACKSLASH_NUMBER,
    16: EntityType.BACKSLASH_NUMBER,
    17: EntityType.BACKSLASH_FUNCTION,
    18: EntityType.BACKSLASH_FUNCTION,
    19: EntityType.BACKSLASH_NUMBER,
    20: EntityType.BACKSLASH_FUNCTION,
    21: EntityType.BACKSLASH_NUMBER,
    22: EntityType.BACKSLASH_FUNCTION,
    23: EntityType.PURE_VARIABLE,
    24: EntityType.PURE_NUMBER,
    25: EntityType.PURE_VARIABLE,
    26: EntityType.PURE_VARIABLE,
    27: EntityType.PURE_NUMBER,
    28: EntityType.PURE_VARIABLE,
    29: EntityType.PURE_NUMBER,
    30: EntityType.PURE_VARIABLE,
    31: EntityType.PURE_VARIABLE,
    32: EntityType.PURE_VARIABLE,
    33: EntityType.PURE_VARIABLE,
    34: EntityType.PURE_NUMBER,
    35: EntityType.PURE_VARIABLE,
    36: EntityType.PURE_VARIABLE,
    37: EntityType.PURE_VARIABLE,
    38: EntityType.PURE_VARIABLE,
    39: EntityType.PURE_VARIABLE,
    40: EntityType.PURE_VARIABLE,
    41: EntityType.PURE_NUMBER,
    42: EntityType.PURE_VARIABLE,
    43: EntityType.PURE_VARIABLE,
    44: EntityType.PURE_VARIABLE}
    expected_nodeId__funcName = {
    0: '=',
    1: '\\to',
    4: '^',
    5: '^',
    6: '/',
    7: '/',
    8: '-',
    9: '-',
    10: '-',
    11: 'lim',
    12: 'theta',
    13: 'infty',
    14: 'sum',
    15: 'theta',
    16: 'theta',
    17: 'frac',
    18: 'int',
    19: 'pi',
    20: 'frac',
    21: 'pi',
    22: 'frac',
    23: 'n',
    24: '1',
    25: 'P',
    26: 'P',
    27: '2',
    28: 'P',
    29: '2',
    30: 'f',
    31: 'x',
    32: 'e',
    33: 'i',
    34: '2',
    35: 'n',
    36: 'P',
    37: 'x',
    38: 'dx',
    39: 'e',
    40: 'i',
    41: '2',
    42: 'n',
    43: 'P',
    44: 'x'}
    expected_nodeId__funcStart = {
    0: 30,
    1: 12,
    4: 83,
    5: 110,
    6: 67,
    7: 74,
    8: 31,
    9: 72,
    10: 85,
    11: 0,
    12: 6,
    13: 15,
    14: 23,
    15: 32,
    16: 41,
    17: 49,
    18: 60,
    19: 89,
    20: 92,
    21: 115,
    22: 118,
    23: 29,
    24: 55,
    25: 58,
    26: 66,
    27: 68,
    28: 73,
    29: 75,
    30: 78,
    31: 80,
    32: 82,
    33: 86,
    34: 87,
    35: 98,
    36: 101,
    37: 103,
    38: 105,
    39: 109,
    40: 112,
    41: 113,
    42: 124,
    43: 127,
    44: 129}
    expected_nodeId__funcEnd = {
    0: 31,
    1: 15,
    4: 84,
    5: 111,
    6: 68,
    7: 75,
    8: 32,
    9: 73,
    10: 86,
    11: 4,
    12: 12,
    13: 21,
    14: 27,
    15: 38,
    16: 47,
    17: 54,
    18: 64,
    19: 92,
    20: 97,
    21: 118,
    22: 123,
    23: 30,
    24: 56,
    25: 59,
    26: 67,
    27: 69,
    28: 74,
    29: 76,
    30: 79,
    31: 81,
    32: 83,
    33: 87,
    34: 89,
    35: 99,
    36: 102,
    37: 104,
    38: 107,
    39: 110,
    40: 113,
    41: 115,
    42: 125,
    43: 128,
    44: 130}
    expected_tuple_nodeId_argIdx__pNodeId = {}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {
    (0, 0): (None, 0, None, 30),
    (0, 1): (None, 30, None, 134),
    (1, 0): (None, 0, None, 12),
    (1, 1): (None, 12, None, 134),
    (4, 0): (None, 0, None, 83),
    (4, 1): (None, 83, None, 134),
    (5, 0): (None, 0, None, 110),
    (5, 1): (None, 110, None, 134),
    (6, 0): (None, 0, None, 67),
    (6, 1): (None, 67, None, 134),
    (7, 0): (None, 0, None, 74),
    (7, 1): (None, 74, None, 134),
    (8, 0): (None, 0, None, 31),
    (8, 1): (None, 31, None, 134),
    (9, 0): (None, 0, None, 72),
    (9, 1): (None, 72, None, 134),
    (10, 0): (None, 0, None, 85),
    (10, 1): (None, 85, None, 134),
    (11, 0): ('{', 5, '}', 21),
    (11, 1): ('{', 22, '}', 133),
    (14, 0): ('{', 28, '}', 38),
    (14, 1): ('{', 40, '}', 47),
    (14, 2): ('{', 48, '}', 132),
    (17, 0): ('{', 54, '}', 56),
    (17, 1): ('{', 57, '}', 59),
    (18, 0): ('{', 65, '}', 69),
    (18, 1): ('{', 71, '}', 76),
    (18, 2): ('{', 77, '}', 107),
    (20, 0): ('{', 97, '}', 99),
    (20, 1): ('{', 100, '}', 102),
    (22, 0): ('{', 123, '}', 125),
    (22, 1): ('{', 126, '}', 128)}


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == parser.bracketstorage.closeBraType__sortedPosList \
        and expected_openBraType__sortedPosList == parser.bracketstorage.openBraType__sortedPosList \
        and expected_id__tuple_openPos_openBraType_closePos_closeBraType == parser.bracketstorage.id__tuple_openPos_openBraType_closePos_closeBraType\
        and expected_list_tuple_width_id_openPos_closePos == parser.bracketstorage.list_tuple_width_id_openPos_closePos\
        and expected_openBraPos__bracketId == parser.bracketstorage.openBraPos__bracketId\
        and expected_closeBraPos__bracketId == parser.bracketstorage.closeBraPos__bracketId\
        and expected_list_tuple_widthStart_nodeId == parser.entitystorage.list_tuple_widthStart_nodeId\
        and expected_list_tuple_widthEnd_nodeId == parser.entitystorage.list_tuple_widthEnd_nodeId\
        and expected_nodeId__widthStart == parser.entitystorage.nodeId__widthStart\
        and expected_nodeId__widthEnd == parser.entitystorage.nodeId__widthEnd\
        and expected_entityType__list_nodeId == parser.entitystorage.entityType__list_nodeId\
        and expected_funcStart__nodeId == parser.entitystorage.funcStart__nodeId\
        and expected_funcName__list_nodeId == parser.entitystorage.funcName__list_nodeId\
        and expected_nodeId__entityType == parser.entitystorage.nodeId__entityType\
        and expected_nodeId__funcName == parser.entitystorage.nodeId__funcName\
        and expected_nodeId__funcStart == parser.entitystorage.nodeId__funcStart\
        and expected_nodeId__funcEnd == parser.entitystorage.nodeId__funcEnd\
        and expected_tuple_nodeId_argIdx__pNodeId == parser.entitystorage.tuple_nodeId_argIdx__pNodeId\
        and expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == parser.entitystorage.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos
    )
    if verbose:
        print(str(parser.bracketstorage))
        print(str(parser.entitystorage))


def test__find_implicit_00(verbose=False):
    """
\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}{f(x)e^{-i 2\\pi\\frac{n}{P}x}dx}(e^{i 2\\pi\\frac{n}{P}x})}}
^ ^^^^^^ ^^^^^^ ^^^ ^^^^^^^^ ^^^^^^^^^ ^^^^^^^^^ ^^^^^^^^ ^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^ ^^^ ^^^^^^^^^^^^^^^^^^^^^^^ ^^^ ^^^^^^^^^^^^^^^
0 123456 789111 111 11112222 222222333 333333344 44444444 55555555556 66666666677777777778888888888 999 99999991111111111111111 111 111111111111111
            012 345 67890123 456789012 345678901 23456789 01234567890 12345678901234567890123456789 012 34567890000000000111111 111 122222222223333
                                                                                                               0123456789012345 678 901234567890123

                                                                                                               
    """
    #Fourier transform
    equationStr = "\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}{f(x)e^{-i 2\\pi\\frac{n}{P}x}dx}(e^{i 2\\pi\\frac{n}{P}x})}}"
    parser = Latexparser(equationStr, verbose=verbose)
    # parser._remove_all_spacing()
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()
    parser._find_implicit_0()


    expected_closeBraType__sortedPosList = {')': [81, 131], '}': [104, 130]}
    expected_openBraType__sortedPosList = {'(': [79, 108], '{': [84, 111]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {
    7: (79, '(', 81, ')'),
    10: (84, '{', 104, '}'),
    14: (111, '{', 130, '}'),
    15: (108, '(', 131, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(2, 7, 79, 81), (19, 14, 111, 130), (20, 10, 84, 104), (23, 15, 108, 131)]
    expected_openBraPos__bracketId = {79: 7, 84: 10, 108: 15, 111: 14}
    expected_closeBraPos__bracketId = {81: 7, 104: 10, 130: 14, 131: 15}


    expected_list_tuple_widthStart_nodeId = [   (0, 11),
    (6, 12),
    (12, 1),
    (15, 13),
    (23, 14),
    (29, 23),
    (30, 0),
    (31, 8),
    (32, 15),
    (41, 16),
    (49, 17),
    (55, 24),
    (58, 25),
    (60, 18),
    (66, 26),
    (67, 6),
    (68, 27),
    (72, 45),
    (72, 9),
    (73, 28),
    (74, 7),
    (75, 29),
    (78, 30),
    (80, 31),
    (82, 32),
    (83, 4),
    (85, 46),
    (85, 10),
    (86, 33),
    (87, 34),
    (89, 19),
    (92, 20),
    (98, 35),
    (101, 36),
    (103, 37),
    (105, 38),
    (109, 39),
    (110, 5),
    (112, 40),
    (113, 41),
    (115, 21),
    (118, 22),
    (124, 42),
    (127, 43),
    (129, 44)]
    expected_list_tuple_widthEnd_nodeId = [   (12, 12),
    (21, 13),
    (30, 23),
    (134, 11),
    (15, 1),
    (56, 24),
    (133, 14),
    (31, 0),
    (32, 8),
    (38, 15),
    (47, 16),
    (59, 25),
    (60, 17),
    (67, 26),
    (69, 27),
    (72, 45),
    (104, 32),
    (89, 34),
    (102, 36),
    (107, 38),
    (108, 18),
    (68, 6),
    (73, 9),
    (74, 28),
    (75, 7),
    (76, 29),
    (79, 30),
    (81, 31),
    (84, 4),
    (85, 46),
    (86, 10),
    (87, 33),
    (92, 19),
    (99, 35),
    (103, 20),
    (104, 37),
    (130, 39),
    (111, 5),
    (113, 40),
    (115, 41),
    (118, 21),
    (125, 42),
    (128, 43),
    (129, 22),
    (130, 44)]
    expected_nodeId__widthStart = {   0: 30,
    1: 12,
    4: 83,
    5: 110,
    6: 67,
    7: 74,
    8: 31,
    9: 72,
    10: 85,
    11: 0,
    12: 6,
    13: 15,
    14: 23,
    15: 32,
    16: 41,
    17: 49,
    18: 60,
    19: 89,
    20: 92,
    21: 115,
    22: 118,
    23: 29,
    24: 55,
    25: 58,
    26: 66,
    27: 68,
    28: 73,
    29: 75,
    30: 78,
    31: 80,
    32: 82,
    33: 86,
    34: 87,
    35: 98,
    36: 101,
    37: 103,
    38: 105,
    39: 109,
    40: 112,
    41: 113,
    42: 124,
    43: 127,
    44: 129,
    45: 72,
    46: 85}
    expected_nodeId__widthEnd = {
    0: 31,
    1: 15,
    4: 84,
    5: 111,
    6: 68,
    7: 75,
    8: 32,
    9: 73,
    10: 86,
    11: 134,
    12: 12,
    13: 21,
    14: 133,
    15: 38,
    16: 47,
    17: 60,
    18: 108,
    19: 92,
    20: 103,
    21: 118,
    22: 129,
    23: 30,
    24: 56,
    25: 59,
    26: 67,
    27: 69,
    28: 74,
    29: 76,
    30: 79,
    31: 81,
    32: 104,
    33: 87,
    34: 89,
    35: 99,
    36: 102,
    37: 104,
    38: 107,
    39: 130,
    40: 113,
    41: 115,
    42: 125,
    43: 128,
    44: 130,
    45: 72,
    46: 85}
    expected_entityType__list_nodeId = {
    EntityType.PURE_INFIX: [0, 1, 4, 5, 6, 7, 8],
    EntityType.PURE_NUMBER: [24, 27, 29, 34, 41, 45, 46],
    EntityType.BACKSLASH_NUMBER: [12, 13, 15, 16, 19, 21],
    EntityType.IMPLICIT_INFIX: [9, 10],
    EntityType.PURE_VARIABLE: [   23,
                                                     25,
                                                     26,
                                                     28,
                                                     30,
                                                     31,
                                                     32,
                                                     33,
                                                     35,
                                                     36,
                                                     37,
                                                     38,
                                                     39,
                                                     40,
                                                     42,
                                                     43,
                                                     44],
    EntityType.BACKSLASH_FUNCTION: [   11,
                                                               14,
                                                               17,
                                                               18,
                                                               20,
                                                               22]}
    expected_funcStart__nodeId = {   0: 11,
    6: 12,
    12: 1,
    15: 13,
    23: 14,
    29: 23,
    30: 0,
    31: 8,
    32: 15,
    41: 16,
    49: 17,
    55: 24,
    58: 25,
    60: 18,
    66: 26,
    67: 6,
    68: 27,
    72: 45,
    73: 28,
    74: 7,
    75: 29,
    78: 30,
    80: 31,
    82: 32,
    83: 4,
    85: 46,
    86: 33,
    87: 34,
    89: 19,
    92: 20,
    98: 35,
    101: 36,
    103: 37,
    105: 38,
    109: 39,
    110: 5,
    112: 40,
    113: 41,
    115: 21,
    118: 22,
    124: 42,
    127: 43,
    129: 44}
    expected_funcName__list_nodeId = {
    '-': [8, 9, 10],
    '/': [6, 7],
    '0': [45, 46],
    '1': [24],
    '2': [27, 29, 34, 41],
    '=': [0],
    'P': [25, 26, 28, 36, 43],
    '\\to': [1],
    '^': [4, 5],
    'dx': [38],
    'e': [32, 39],
    'f': [30],
    'frac': [17, 20, 22],
    'i': [33, 40],
    'infty': [13],
    'int': [18],
    'lim': [11],
    'n': [23, 35, 42],
    'pi': [19, 21],
    'sum': [14],
    'theta': [12, 15, 16],
    'x': [31, 37, 44]}
    expected_nodeId__entityType = {
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    4: EntityType.PURE_INFIX,
    5: EntityType.PURE_INFIX,
    6: EntityType.PURE_INFIX,
    7: EntityType.PURE_INFIX,
    8: EntityType.PURE_INFIX,
    9: EntityType.IMPLICIT_INFIX,
    10: EntityType.IMPLICIT_INFIX,
    11: EntityType.BACKSLASH_FUNCTION,
    12: EntityType.BACKSLASH_NUMBER,
    13: EntityType.BACKSLASH_NUMBER,
    14: EntityType.BACKSLASH_FUNCTION,
    15: EntityType.BACKSLASH_NUMBER,
    16: EntityType.BACKSLASH_NUMBER,
    17: EntityType.BACKSLASH_FUNCTION,
    18: EntityType.BACKSLASH_FUNCTION,
    19: EntityType.BACKSLASH_NUMBER,
    20: EntityType.BACKSLASH_FUNCTION,
    21: EntityType.BACKSLASH_NUMBER,
    22: EntityType.BACKSLASH_FUNCTION,
    23: EntityType.PURE_VARIABLE,
    24: EntityType.PURE_NUMBER,
    25: EntityType.PURE_VARIABLE,
    26: EntityType.PURE_VARIABLE,
    27: EntityType.PURE_NUMBER,
    28: EntityType.PURE_VARIABLE,
    29: EntityType.PURE_NUMBER,
    30: EntityType.PURE_VARIABLE,
    31: EntityType.PURE_VARIABLE,
    32: EntityType.PURE_VARIABLE,
    33: EntityType.PURE_VARIABLE,
    34: EntityType.PURE_NUMBER,
    35: EntityType.PURE_VARIABLE,
    36: EntityType.PURE_VARIABLE,
    37: EntityType.PURE_VARIABLE,
    38: EntityType.PURE_VARIABLE,
    39: EntityType.PURE_VARIABLE,
    40: EntityType.PURE_VARIABLE,
    41: EntityType.PURE_NUMBER,
    42: EntityType.PURE_VARIABLE,
    43: EntityType.PURE_VARIABLE,
    44: EntityType.PURE_VARIABLE,
    45: EntityType.PURE_NUMBER,
    46: EntityType.PURE_NUMBER}
    expected_nodeId__funcName = {   0: '=',
    1: '\\to',
    4: '^',
    5: '^',
    6: '/',
    7: '/',
    8: '-',
    9: '-',
    10: '-',
    11: 'lim',
    12: 'theta',
    13: 'infty',
    14: 'sum',
    15: 'theta',
    16: 'theta',
    17: 'frac',
    18: 'int',
    19: 'pi',
    20: 'frac',
    21: 'pi',
    22: 'frac',
    23: 'n',
    24: '1',
    25: 'P',
    26: 'P',
    27: '2',
    28: 'P',
    29: '2',
    30: 'f',
    31: 'x',
    32: 'e',
    33: 'i',
    34: '2',
    35: 'n',
    36: 'P',
    37: 'x',
    38: 'dx',
    39: 'e',
    40: 'i',
    41: '2',
    42: 'n',
    43: 'P',
    44: 'x',
    45: '0',
    46: '0'}
    expected_nodeId__funcStart = {   0: 30,
    1: 12,
    4: 83,
    5: 110,
    6: 67,
    7: 74,
    8: 31,
    9: 72,
    10: 85,
    11: 0,
    12: 6,
    13: 15,
    14: 23,
    15: 32,
    16: 41,
    17: 49,
    18: 60,
    19: 89,
    20: 92,
    21: 115,
    22: 118,
    23: 29,
    24: 55,
    25: 58,
    26: 66,
    27: 68,
    28: 73,
    29: 75,
    30: 78,
    31: 80,
    32: 82,
    33: 86,
    34: 87,
    35: 98,
    36: 101,
    37: 103,
    38: 105,
    39: 109,
    40: 112,
    41: 113,
    42: 124,
    43: 127,
    44: 129,
    45: 72,
    46: 85}
    expected_nodeId__funcEnd = {   0: 31,
    1: 15,
    4: 84,
    5: 111,
    6: 68,
    7: 75,
    8: 32,
    9: 73,
    10: 86,
    11: 4,
    12: 12,
    13: 21,
    14: 27,
    15: 38,
    16: 47,
    17: 54,
    18: 64,
    19: 92,
    20: 97,
    21: 118,
    22: 123,
    23: 30,
    24: 56,
    25: 59,
    26: 67,
    27: 69,
    28: 74,
    29: 76,
    30: 79,
    31: 81,
    32: 83,
    33: 87,
    34: 89,
    35: 99,
    36: 102,
    37: 104,
    38: 107,
    39: 110,
    40: 113,
    41: 115,
    42: 125,
    43: 128,
    44: 130,
    45: 72,
    46: 85}
    expected_tuple_nodeId_argIdx__pNodeId = {}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {
    (0, 0): (None, 0, None, 30),
    (0, 1): (None, 30, None, 134),
    (1, 0): (None, 0, None, 12),
    (1, 1): (None, 12, None, 134),
    (4, 0): (None, 0, None, 83),
    (4, 1): (None, 83, None, 134),
    (5, 0): (None, 0, None, 110),
    (5, 1): (None, 110, None, 134),
    (6, 0): (None, 0, None, 67),
    (6, 1): (None, 67, None, 134),
    (7, 0): (None, 0, None, 74),
    (7, 1): (None, 74, None, 134),
    (8, 0): (None, 0, None, 31),
    (8, 1): (None, 31, None, 134),
    (9, 0): (None, 0, None, 72),
    (9, 1): (None, 72, None, 134),
    (10, 0): (None, 0, None, 85),
    (10, 1): (None, 85, None, 134),
    (11, 0): ('{', 5, '}', 21),
    (11, 1): ('{', 22, '}', 133),
    (14, 0): ('{', 28, '}', 38),
    (14, 1): ('{', 40, '}', 47),
    (14, 2): ('{', 48, '}', 132),
    (17, 0): ('{', 54, '}', 56),
    (17, 1): ('{', 57, '}', 59),
    (18, 0): ('{', 65, '}', 69),
    (18, 1): ('{', 71, '}', 76),
    (18, 2): ('{', 77, '}', 107),
    (20, 0): ('{', 97, '}', 99),
    (20, 1): ('{', 100, '}', 102),
    (22, 0): ('{', 123, '}', 125),
    (22, 1): ('{', 126, '}', 128)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == parser.bracketstorage.closeBraType__sortedPosList \
        and expected_openBraType__sortedPosList == parser.bracketstorage.openBraType__sortedPosList \
        and expected_id__tuple_openPos_openBraType_closePos_closeBraType == parser.bracketstorage.id__tuple_openPos_openBraType_closePos_closeBraType\
        and expected_list_tuple_width_id_openPos_closePos == parser.bracketstorage.list_tuple_width_id_openPos_closePos\
        and expected_openBraPos__bracketId == parser.bracketstorage.openBraPos__bracketId\
        and expected_closeBraPos__bracketId == parser.bracketstorage.closeBraPos__bracketId\
        and expected_list_tuple_widthStart_nodeId == parser.entitystorage.list_tuple_widthStart_nodeId\
        and expected_list_tuple_widthEnd_nodeId == parser.entitystorage.list_tuple_widthEnd_nodeId\
        and expected_nodeId__widthStart == parser.entitystorage.nodeId__widthStart\
        and expected_nodeId__widthEnd == parser.entitystorage.nodeId__widthEnd\
        and expected_entityType__list_nodeId == parser.entitystorage.entityType__list_nodeId\
        and expected_funcStart__nodeId == parser.entitystorage.funcStart__nodeId\
        and expected_funcName__list_nodeId == parser.entitystorage.funcName__list_nodeId\
        and expected_nodeId__entityType == parser.entitystorage.nodeId__entityType\
        and expected_nodeId__funcName == parser.entitystorage.nodeId__funcName\
        and expected_nodeId__funcStart == parser.entitystorage.nodeId__funcStart\
        and expected_nodeId__funcEnd == parser.entitystorage.nodeId__funcEnd\
        and expected_tuple_nodeId_argIdx__pNodeId == parser.entitystorage.tuple_nodeId_argIdx__pNodeId\
        and expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == parser.entitystorage.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos
    )
    if verbose:
        print(str(parser.bracketstorage))
        print(str(parser.entitystorage))


def test__find_implicit_multiply0(verbose=False):
    """
\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}{f(x)e^{-i 2\\pi\\frac{n}{P}x}dx}(e^{i 2\\pi\\frac{n}{P}x})}}
^ ^^^^^^ ^^^^^^ ^^^ ^^^^^^^^ ^^^^^^^^^ ^^^^^^^^^ ^^^^^^^^ ^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^ ^^^ ^^^^^^^^^^^^^^^^^^^^^^^ ^^^ ^^^^^^^^^^^^^^^
0 123456 789111 111 11112222 222222333 333333344 44444444 55555555556 66666666677777777778888888888 999 99999991111111111111111 111 111111111111111
            012 345 67890123 456789012 345678901 23456789 01234567890 12345678901234567890123456789 012 34567890000000000111111 111 122222222223333
                                                                                                               0123456789012345 678 901234567890123

                                                                                                               
    """
    #Fourier transform
    equationStr = "\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2}{f(x)e^{-i 2\\pi\\frac{n}{P}x}dx}(e^{i 2\\pi\\frac{n}{P}x})}}"
    parser = Latexparser(equationStr, verbose=verbose)
    # parser._remove_all_spacing()
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()
    parser._find_implicit_0()
    parser._find_implicit_multiply()


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.bracketstorage))
        print(str(parser.entitystorage))


def test__find_infixes_arg_brackets_width0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO

def test__update_all_width_by_enclosing_brackets_width_remove0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO

def test__match_child_to_parent_input0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO
        
def test__format_to_pyStyledAST0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO
        
def test__convert_to_schemeStyledAST0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO


def test__get_statistics0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO


if __name__=='__main__':
    # test__remove_space0() #REMOVE################
    # test__find_matrices0()
    # test___isPosInMatrixTag0()
    # test__find_infix0() 
    # test__find_brackets0()
    # test__find_backslash0()
    # test__find_variables_or_numbers0()
    # test__find_implicit_00()
    test__find_implicit_multiply0(True)
    # test__find_infixes_arg_brackets_width0(True)
    # test__update_all_width_by_enclosing_brackets_width_remove0(True)
    #test__match_child_to_parent_input0(True)
    #test__format_to_pyStyledAST0(True)
    #test__convert_to_schemeStyledAST0(True)
    #test__get_statistics0(True)