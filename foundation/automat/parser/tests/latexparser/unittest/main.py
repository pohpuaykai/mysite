import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser, BracketStorage, BracketType, EntityStorage, EntityType

pp = pprint.PrettyPrinter(indent=4)



def test__remove_space0(verbose=False):
    #from https://en.wikipedia.org/wiki/Quaternionic_matrix
    
    equationStr = " a + bi + cj + dk =  \\begin{pmatrix} a+ bi&c+d i  \\\\-c+di &a  -bi \\\\ \\end{pmatrix}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._remove_all_spacing()
    expected_equationStr = 'a+bi+cj+dk=\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_equationStr == parser.equationStr
    )
    if verbose:
        print(parser.equationStr)
        

def test__find_matrices0(verbose=False):
    #(a+bi+cj+dk)(a+bi+cj+dk)
    
    equationStr = "\\begin{pmatrix}(a^2-b^2-c^2-d^2)+i(2ab)&2ac+i(2ad)\\\\-2ac+i(2ad)&(a^2+b^2-c^2-d^2)-i(2ab)\\\\\\end{pmatrix}=\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._remove_all_spacing()
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
    parser._remove_all_spacing()
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
    #\forall k \in \Z^+ and \forall prime_number p, equationStr = 1 | -1 a multivalue function

(\\frac{p+1}{2})*((p-1)/2)^{(k-1)(p-1)/2})\\%p=p-1
^^ ^   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^
01 2   678911111111112222222222333333333344 444444
           01234567890123456789012345678901 234567

    """
    
    equationStr = "(\\frac{p+1}{2})*((p-1)/2)^{(k-1)(p-1)/2})\\%p=p-1"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._remove_all_spacing()
    parser._find_matrices()
    parser._find_infix()

    expected_list_tuple_widthStart_nodeId = None
    expected_list_tuple_widthEnd_nodeId = None
    expected_nodeId__widthStart = {0: 44, 1: 41, 2: 25, 3: 22, 4: 37, 5: 15, 6: 19, 7: 29, 8: 34, 9: 46, 10: 8}
    expected_nodeId__widthEnd = None
    expected_entityType__list_nodeId = None
    expected_funcStart__nodeId = None
    expected_funcName__list_nodeId = {
    '*': [5],
    '+': [10],
    '-': [6, 7, 8, 9],
    '/': [3, 4],
    '=': [0],
    '\\%': [1],
    '^': [2]}
    expected_nodeId__entityType = None
    expected_nodeId__funcName = None
    expected_nodeId__funcStart = None
    expected_nodeId__funcEnd = None
    expected_tuple_nodeId_argIdx__pNodeId = None
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = None

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
    parser._remove_all_spacing()
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
        #parser.bracketstorage.id__tuple_openPos_openBraType_closePos_closeBraType
        pp.pprint(parser.bracketstorage.id__tuple_openPos_openBraType_closePos_closeBraType)

def test__find_backslash0(verbose=False):
    #Fourier transform
    equationStr = "\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2} f(x)e^{-i2\\pi\\frac{n}{P}x}dx}(e^{i2\\pi\\frac{n}{P}x})}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._remove_all_spacing()
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    expected = None


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print('backslash_pos_type', parser.backslash_pos_type)
        print('variables_pos_type', parser.variables_pos_type)
        print('number_pos_type', parser.number_pos_type)
        

def test__find_variables_or_numbers0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO
        
def test__find_implicit_00(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO
        
def test__find_implicit_multiply0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO


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
    # test__remove_space0()
    # test__find_matrices0()
    # test___isPosInMatrixTag0()
    test__find_infix0(True) 
    # test__find_brackets0(True)
    # test__find_backslash0(True)
    #test__find_variables_or_numbers0(True)
    #test__find_implicit_00(True)
    # test__find_infixes_arg_brackets_width0(True)
    # test__update_all_width_by_enclosing_brackets_width_remove0(True)
    #test__find_implicit_multiply0(True)
    #test__match_child_to_parent_input0(True)
    #test__format_to_pyStyledAST0(True)
    #test__convert_to_schemeStyledAST0(True)
    #test__get_statistics0(True)