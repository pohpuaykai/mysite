import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser, BracketStorage, BracketType

pp = pprint.PrettyPrinter(indent=4)

#unit tests
def test__bracketStorage__insert0(verbose=False):
    
    braSt = BracketStorage()
    braSt.insertBracket('(', 0, ')', 4) #(1+1)=2

    expected_closeBraType__sortedPosList = {')': [4]}
    expected_openBraType__sortedPosList = {'(': [0]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 4, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 0, 0, 4)]
    expected_openBraPos__bracketId = {0: 0}
    expected_closeBraPos__bracketId = {4: 0}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)


def test__bracketStorage__remove0(verbose=False):
    
    braSt = BracketStorage()
    openBraPos = 0
    braSt.insertBracket('(', openBraPos, ')', 4) #(1+1)=2
    braSt.removeBracket(openBraPos)

    expected_closeBraType__sortedPosList = {}
    expected_openBraType__sortedPosList = {}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {}
    expected_list_tuple_width_id_openPos_closePos = []
    expected_openBraPos__bracketId = {}
    expected_closeBraPos__bracketId = {}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)

def test__bracketStorage__update0(verbose=False):
    
    braSt = BracketStorage()
    defaultOpen, defaultClose = '(', ')'
    bracketId = braSt.insertBracket(defaultOpen, 2, defaultClose, 3) #(1+1)=2 #FAKE bra, actually + startEnd
    braSt.updateBracket(bracketId, defaultOpen, 0, defaultClose, 4)


    expected_closeBraType__sortedPosList = {')': [4]}
    expected_openBraType__sortedPosList = {'(': [0]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 4, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 0, 0, 4)]
    expected_openBraPos__bracketId = {0: 0}
    expected_closeBraPos__bracketId = {4: 0}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)


def test__bracketStorage__getBraPosImmediateRightOfPos0(verbose=False):
    
    #things to check
    # closeBraType__sortedPosList = {}
    # openBraType__sortedPosList = {}
    # id__tuple_openPos_openBraType_closePos_closeBraType = {}
    # list_tuple_width_id_openPos_closePos = []
    # openBraPos__bracketId = {}
    # closeBraPos__bracketId = {}

    braSt = BracketStorage()
    braSt.insertBracket('(', 0, ')', 4) #(1+1)=2
    insertIdx = braSt.getBraPosImmediateRightOfPos(3, BracketType.ROUND, False)

    expected_closeBraType__sortedPosList = {')': [4]}
    expected_openBraType__sortedPosList = {'(': [0]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 4, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 0, 0, 4)]
    expected_openBraPos__bracketId = {0: 0}
    expected_closeBraPos__bracketId = {4: 0}
    expected_insertIdx = 4

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId and\
        expected_insertIdx == insertIdx
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)
        print(insertIdx)




def test__bracketStorage__getBraPosImmediateLeftOfPos0(verbose=False):
    
    braSt = BracketStorage()
    braSt.insertBracket('(', 0, ')', 4) #(1+1)=2
    insertIdx = braSt.getBraPosImmediateLeftOfPos(3, BracketType.ROUND, False)

    expected_closeBraType__sortedPosList = {')': [4]}
    expected_openBraType__sortedPosList = {'(': [0]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 4, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 0, 0, 4)]
    expected_openBraPos__bracketId = {0: 0}
    expected_closeBraPos__bracketId = {4: 0}
    expected_insertIdx = 4

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId and\
        expected_insertIdx == insertIdx
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)
        print(insertIdx)



def test__bracketStorage__exists0(verbose=False):
    
    braSt = BracketStorage()
    braSt.insertBracket('(', 0, ')', 4) #(1+1)=2
    has = braSt.exists(0, BracketType.ROUND, True)

    expected_closeBraType__sortedPosList = {')': [4]}
    expected_openBraType__sortedPosList = {'(': [0]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 4, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 0, 0, 4)]
    expected_openBraPos__bracketId = {0: 0}
    expected_closeBraPos__bracketId = {4: 0}
    expected_has = True

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId and\
        expected_has == has
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)
        print(has)



def test__bracketStorage__getCorrespondingCloseBraPos0(verbose=False):
    
    braSt = BracketStorage()
    braSt.insertBracket('(', 0, ')', 4) #(1+1)=2
    closeBraPos, closeBraType = braSt.getCorrespondingCloseBraPos(0)

    expected_closeBraType__sortedPosList = {')': [4]}
    expected_openBraType__sortedPosList = {'(': [0]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 4, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 0, 0, 4)]
    expected_openBraPos__bracketId = {0: 0}
    expected_closeBraPos__bracketId = {4: 0}
    expected__closeBraPos = 4

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId and\
        expected__closeBraPos == closeBraPos
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)
        print(closeBraPos)



def test__bracketStorage__getCorrespondingOpenBraPos0(verbose=False):
    
    braSt = BracketStorage()
    braSt.insertBracket('(', 0, ')', 4) #(1+1)=2
    openBraPos, openBraType = braSt.getCorrespondingOpenBraPos(4)

    expected_closeBraType__sortedPosList = {')': [4]}
    expected_openBraType__sortedPosList = {'(': [0]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 4, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 0, 0, 4)]
    expected_openBraPos__bracketId = {0: 0}
    expected_closeBraPos__bracketId = {4: 0}
    expected_openBraPos = 0

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId and\
        expected_openBraPos == openBraPos
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)
        print(openBraPos)



def test__bracketStorage__getAllEnclosingBraOfPos0(verbose=False):
    
    #things to check
    # closeBraType__sortedPosList = {}
    # openBraType__sortedPosList = {}
    # id__tuple_openPos_openBraType_closePos_closeBraType = {}
    # list_tuple_width_id_openPos_closePos = []
    # openBraPos__bracketId = {}
    # closeBraPos__bracketId = {}

    braSt = BracketStorage()
    braSt.insertBracket('(', 0, ')', 4) #(1+1)=2
    list_tuple_width_id_openPos_closePos = list(braSt.getAllEnclosingBraOfPos(2, BracketType.ROUND))

    expected_closeBraType__sortedPosList = {')': [4]}
    expected_openBraType__sortedPosList = {'(': [0]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 4, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 0, 0, 4)]
    expected_openBraPos__bracketId = {0: 0}
    expected_closeBraPos__bracketId = {4: 0}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)



def test__bracketStorage__getAllEnclosingTouchingBraOfPos0(verbose=False):
    
    #things to check
    # closeBraType__sortedPosList = {}
    # openBraType__sortedPosList = {}
    # id__tuple_openPos_openBraType_closePos_closeBraType = {}
    # list_tuple_width_id_openPos_closePos = []
    # openBraPos__bracketId = {}
    # closeBraPos__bracketId = {}

    braSt = BracketStorage()
    """
    ((((1+1)))(1+1))=4
    ^^^^   ^^^^   ^^
    0123   7891   11
              0   45

    0  15 ~ id 0
    1  9  ~ id 1
    2  8  ~ id 2
    3  7  ~ id 3
    10 14 ~ id 4

    """
    id0 = braSt.insertBracket('(', 0, ')', 15) 
    id1 = braSt.insertBracket('(', 1, ')', 9)
    id2 = braSt.insertBracket('(', 2, ')', 8)
    id3 = braSt.insertBracket('(', 3, ')', 7)
    id4 = braSt.insertBracket('(', 10, ')', 14)
    list_tuple_width_id_openPos_closePos_oCcC = braSt.getAllEnclosingTouchingBraOfPos(5, BracketType.ROUND)

    expected_closeBraType__sortedPosList = {')': [7, 8, 9, 14, 15]}
    expected_openBraType__sortedPosList = {'(': [0, 1, 2, 3, 10]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 15, ')'), 1: (1, '(', 9, ')'), 2: (2, '(', 8, ')'), 3: (3, '(', 7, ')'), 4: (10, '(', 14, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 4, 10, 14), (4, 3, 3, 7), (6, 2, 2, 8), (8, 1, 1, 9), (15, 0, 0, 15)]
    expected_openBraPos__bracketId = {0: 0, 1: 1, 2: 2, 3: 3, 10: 4}
    expected_closeBraPos__bracketId = {15: 0, 9: 1, 8: 2, 7: 3, 14: 4}
    expected_list_tuple_width_id_openPos_closePos_oCcC = [
    (4, id3, 3, 7),
    (6, id2, 2, 8),
    (8, id1, 1, 9),
    ]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId and\
        expected_list_tuple_width_id_openPos_closePos_oCcC == list_tuple_width_id_openPos_closePos_oCcC
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)
        print(list_tuple_width_id_openPos_closePos_oCcC)



def test__bracketStorage__getWidestEnclosingBra0(verbose=False):
    
    #things to check
    # closeBraType__sortedPosList = {}
    # openBraType__sortedPosList = {}
    # id__tuple_openPos_openBraType_closePos_closeBraType = {}
    # list_tuple_width_id_openPos_closePos = []
    # openBraPos__bracketId = {}
    # closeBraPos__bracketId = {}

    braSt = BracketStorage()
    """
    ((((1+1)))(1+1))=4
    ^^^^   ^^^^   ^^
    0123   7891   11
              0   45

    0  15 ~ id 0
    1  9  ~ id 1
    2  8  ~ id 2
    3  7  ~ id 3
    10 14 ~ id 4

    """
    id0 = braSt.insertBracket('(', 0, ')', 15) 
    id1 = braSt.insertBracket('(', 1, ')', 9)
    id2 = braSt.insertBracket('(', 2, ')', 8)
    id3 = braSt.insertBracket('(', 3, ')', 7)
    id4 = braSt.insertBracket('(', 10, ')', 14)
    selectedOpenPos, selectedClosePos, selectedBracketId = braSt.getWidestEnclosingBra(5, BracketType.ROUND)

    expected_closeBraType__sortedPosList = {')': [7, 8, 9, 14, 15]}
    expected_openBraType__sortedPosList = {'(': [0, 1, 2, 3, 10]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (0, '(', 15, ')'), 1: (1, '(', 9, ')'), 2: (2, '(', 8, ')'), 3: (3, '(', 7, ')'), 4: (10, '(', 14, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(4, 4, 10, 14), (4, 3, 3, 7), (6, 2, 2, 8), (8, 1, 1, 9), (15, 0, 0, 15)]
    expected_openBraPos__bracketId = {0: 0, 1: 1, 2: 2, 3: 3, 10: 4}
    expected_closeBraPos__bracketId = {15: 0, 9: 1, 8: 2, 7: 3, 14: 4}
    expected_selectedOpenPos = 0
    expected_selectedClosePos = 15
    expected_selectedBracketId = id0

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and \
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and \
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId and\
        expected_selectedOpenPos == selectedOpenPos and\
        expected_selectedClosePos == selectedClosePos and\
        expected_selectedBracketId == selectedBracketId
    )
    if verbose:
        print(braSt.closeBraType__sortedPosList)
        print(braSt.openBraType__sortedPosList)
        print(braSt.id__tuple_openPos_openBraType_closePos_closeBraType)
        print(braSt.list_tuple_width_id_openPos_closePos)
        print(braSt.openBraPos__bracketId)
        print(braSt.closeBraPos__bracketId)
        print(selectedOpenPos)
        print(selectedClosePos)
        print(selectedBracketId)



def test__remove_space(verbose=False):
    #from https://en.wikipedia.org/wiki/Quaternionic_matrix
    
    equationStr = " a + bi + cj + dk =  \\begin{pmatrix} a+ bi&c+d i  \\\\-c+di &a  -bi \\\\ \\end{pmatrix}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._remove_all_spacing()
    if verbose:
        print(parser.equationStr)
        

def test__find_matrices(verbose=False):
    #(a+bi+cj+dk)(a+bi+cj+dk)
    
    equationStr = "\\begin{pmatrix}(a^2-b^2-c^2-d^2)+i(2ab)&2ac+i(2ad)\\\\-2ac+i(2ad)&(a^2+b^2-c^2-d^2)-i(2ab)\\\\\\end{pmatrix}=\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}\\begin{pmatrix}a+bi&c+di\\\\-c+di&a-bi\\\\\\end{pmatrix}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._remove_all_spacing()
    parser._find_matrices()
    expected = [
    ((1, 16, '\\begin{pmatrix}'), (194, 207, '\\end{pmatrix}')), 
    ((105, 120, '\\begin{pmatrix}'), (143, 156, '\\end{pmatrix}')), 
    ((156, 171, '\\begin{pmatrix}'), (91, 104, '\\end{pmatrix}'))
    ]
    if verbose:
        print(parser.matrices_pos_type)

def test__find_infix(verbose=False): #TODO infix test for \\to;\\cross;\\cdot
    #\forall k \in \Z^+ and \forall prime_number p, equationStr = 1 | -1 a multivalue function
    equationStr = "(\\frac{p+1}{2})*((p-1)/2)^{(k-1)(p-1)/2})\\%p=p-1"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._remove_all_spacing()
    #parser._find_matrices()
    parser._find_infix()
    expected = [
    (26, 27, '^'), 
    (23, 24, '/'), 
    (38, 39, '/'), 
    (42, 44, '\\%'), 
    (16, 17, '*'), 
    (20, 21, '-'), 
    (30, 31, '-'), 
    (35, 36, '-'), 
    (47, 48, '-'), 
    (9, 10, '+'), 
    (45, 46, '=')
    ]
    if verbose:
        print(parser.infixs_pos_type) #TODO
        
def test__find_brackets(verbose=False):
    if verbose:
        print() # TODO
        
def test__find_backslash(verbose=False):
    
    equationStr = "\\lim_{\\theta\\to\\infty}{\\sum_{n=-\\theta}^{\\theta}{\\frac{1}{P}\\int_{P/2}^{-P/2} f(x)e^{-i2\\pi\\frac{n}{P}x}dx}(e^{i2\\pi\\frac{n}{P}x})}"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._remove_all_spacing()
    #parser._find_matrices()
    #parser._find_infix()
    parser._find_backslash()
    expected = None
    if verbose:
        print() # TODO
        

def test__find_variables_or_numbers(verbose=False):
    if verbose:
        print() # TODO
        
def test__find_implicit_0(verbose=False):
    if verbose:
        print() # TODO
        
def test__find_implicit_multiply(verbose=False):
    if verbose:
        print() # TODO
        
def test__find_infixes_width(verbose=False):
    if verbose:
        print() # TODO
        
def test__match_child_to_parent_input(verbose=False):
    if verbose:
        print() # TODO
        
def test__format_to_pyStyledAST(verbose=False):
    if verbose:
        print() # TODO
        
def test__convert_to_schemeStyledAST(verbose=False):
    if verbose:
        print() # TODO
        
def test__get_statistics(verbose=False):
    if verbose:
        print() # TODO

if __name__=='__main__':
    test__bracketStorage__insert0()
    test__bracketStorage__remove0()
    test__bracketStorage__update0()
    test__bracketStorage__getBraPosImmediateRightOfPos0()
    test__bracketStorage__getBraPosImmediateLeftOfPos0()
    test__bracketStorage__exists0()
    test__bracketStorage__getCorrespondingCloseBraPos0()
    test__bracketStorage__getCorrespondingOpenBraPos0()
    test__bracketStorage__getAllEnclosingBraOfPos0()
    test__bracketStorage__getAllEnclosingTouchingBraOfPos0()
    test__bracketStorage__getWidestEnclosingBra0()

    #test__remove_space(True) # pass
    #test__find_matrices(True)
    #test__find_infix(True)
    #test__find_backslash(True)
    #test__find_brackets(True)
    #test__find_variables_or_numbers(True)
    #test__find_implicit_0(True)
    #test__find_implicit_multiply(True)
    #test__find_infixes_width(True)
    #test__match_child_to_parent_input(True)
    #test__format_to_pyStyledAST(True)
    #test__convert_to_schemeStyledAST(True)
    #test__get_statistics(True)