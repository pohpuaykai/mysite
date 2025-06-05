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



def test__find_infix0(verbose=False):
    """
(2x+1)(x+2)=2x^2+3x+2
^^^^^^^^^^^^^^^^^^^^^
012345678911111111112
          01234567890
    """

    equationStr = "(2x+1)(x+2)=2x^2+3x+2"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.entitystorage)) # TODO




def test__find_brackets0(verbose=False):
    """
(2x+1)(x+2)=2x^2+3x+2
^^^^^^^^^^^^^^^^^^^^^
012345678911111111112
          01234567890
    """

    equationStr = "(2x+1)(x+2)=2x^2+3x+2"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.bracketstorage)) # TODO



def test__find_backslash0(verbose=False):
    """
\\sin((2x+1)(x+2))=\\sin(2x^2+3x+2)
^ ^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^
0 123456789111111111 12222222222333
           012345678 90123456789012



    """

    equationStr = "\\sin((2x+1)(x+2))=\\sin(2x^2+3x+2)"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<overscan to ^


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.entitystorage))
        print(str(parser.bracketstorage))


def test__find_variables_or_numbers0(verbose=False):
    """
\\sin((2x+1)(x+2))=\\sin(2x^2+3x+2)
^ ^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^
0 123456789111111111 12222222222333
           012345678 90123456789012
    """

    equationStr = "\\sin((2x+1)(x+2))=\\sin(2x^2+3x+2)"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.entitystorage))
        print(str(parser.bracketstorage))

def test__find_implicit_00(verbose=False):
    """
\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)
^ ^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^
0 123456789111111111 1222222222233333
           012345678 9012345678901234
    """

    equationStr = "\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()
    parser._find_implicit_0()



    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.entitystorage))



def test__find_infixes_arg_brackets_width0(verbose=False):
    """
\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)
^ ^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^
0 12345678911111111112 22222222233333
           01234567890 12345678901234


    """

    equationStr = "\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()
    parser._find_infixes_arg_brackets_width()
    parser._find_implicit_0()


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.entitystorage))
        print(str(parser.bracketstorage))



def test__update_all_width_by_enclosing_brackets_width_remove0(verbose=False):
    """
\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)
^ ^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^
0 123456789111111111 1222222222233333
           012345678 9012345678901234


    """

    equationStr = "\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()
    parser._find_infixes_arg_brackets_width()
    parser._find_implicit_0()
    parser._update_all_width_by_enclosing_brackets_width_remove()



    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.entitystorage))
        print(str(parser.bracketstorage))



def test__find_implicit_multiply0(verbose=False):
    """
\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)
^ ^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^
0 123456789111111111 1222222222233333
           012345678 9012345678901234

    """

    equationStr = "\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()
    parser._find_infixes_arg_brackets_width()
    parser._find_implicit_0()
    parser._update_all_width_by_enclosing_brackets_width_remove()
    parser._find_implicit_multiply()


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.entitystorage))
        print(str(parser.bracketstorage))


def test__match_child_to_parent_input0(verbose=False):
    """
\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)
^ ^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^
0 123456789111111111 1222222222233333
           012345678 9012345678901234

    """

    equationStr = "\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()
    parser._find_infixes_arg_brackets_width()
    parser._find_implicit_0()
    parser._update_all_width_by_enclosing_brackets_width_remove()
    parser._find_implicit_multiply()
    parser._match_child_to_parent_input()


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    # if verbose:
        
    #     print(str(parser.bracketstorage))
    #     print(str(parser.entitystorage))
        



def test__format_to_pyStyledAST0(verbose=False):
    """
\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)
^ ^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^
0 123456789111111111 1222222222233333
           012345678 9012345678901234

    """

    equationStr = "\\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._find_matrices()
    parser._find_infix()
    parser._find_brackets()
    parser._find_backslash()
    parser._find_variables_or_numbers()
    parser._find_infixes_arg_brackets_width()
    parser._find_implicit_0()
    parser._update_all_width_by_enclosing_brackets_width_remove()
    parser._find_implicit_multiply()
    parser._match_child_to_parent_input()
    parser._format_to_pyStyledAST()


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print(str(parser.bracketstorage))
        print(str(parser.entitystorage))
        print(parser.latexAST)



def test__convert_to_schemeStyledAST0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO


def test__get_statistics0(verbose=False):


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', )
    if verbose:
        print() # TODO


if __name__=='__main__':
    # test__find_matrices0()
    # test___isPosInMatrixTag0()

    # test__find_infix0(True)
    # test__find_brackets0(True)
    # test__find_backslash0(True)
    # test__find_variables_or_numbers0(True)
    # test__find_implicit_00(True)
    # test__find_infixes_arg_brackets_width0(True) # this will need to take implicit multiply as,, but they are not FOUND YET<<<<<<<<<<
    # test__update_all_width_by_enclosing_brackets_width_remove0(True)
    # test__find_implicit_multiply0(True) # if make this before test__find_infixes_arg_brackets_width0, we need the full_width
    test__match_child_to_parent_input0(True)
    # test__format_to_pyStyledAST0(True)
    #test__convert_to_schemeStyledAST0(True)
    #test__get_statistics0(True)