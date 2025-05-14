import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser, BracketStorage, BracketType, EntityStorage, EntityType

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
    expected_insertIdx = float('-inf')

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


def test__entityStorage__insert0(verbose=False):
    """
1+1+1=3
 ^ ^ ^
 1 3 5

pos 1: nodeId 0
pos 3: nodeId 1
pos 5: nodeId 2
    """
    entSt = EntityStorage()
    entSt.insert(
        '+', 1, 2, EntityType.PURE_INFIX, parentNodeId=1, argIdx=0, widthStart=0, widthEnd=3
    )
    entSt.insert(
        '+', 3, 4, EntityType.PURE_INFIX, parentNodeId=2, argIdx=0, widthStart=0, widthEnd=5
    )
    entSt.insert(
        '=', 5, 6, EntityType.PURE_INFIX, parentNodeId=None, argIdx=None, widthStart=0, widthEnd=7
    )

    expected_list_tuple_widthStart_nodeId = [(0, 2), (0, 1), (0, 0)]
    expected_list_tuple_widthEnd_nodeId = [(3, 0), (5, 1), (7, 2)]
    expected_nodeId__widthStart = {0: 0, 1: 0, 2: 0}
    expected_nodeId__widthEnd = {0: 3, 1: 5, 2: 7}
    expected_entityType__list_nodeId = {EntityType.PURE_INFIX:[0, 1, 2]}
    expected_funcStart__nodeId = {1: 0, 3: 1, 5: 2}
    expected_funcName__list_nodeId = {'+': [0, 1], '=': [2]}
    expected_nodeId__entityType = {   
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    2: EntityType.PURE_INFIX}
    expected_nodeId__funcName = {0: '+', 1: '+', 2: '='}
    expected_nodeId__funcStart = {0: 1, 1: 3, 2: 5}
    expected_nodeId__funcEnd = {0: 2, 1: 4, 2: 6}
    expected_tuple_nodeId_argIdx__pNodeId = {(0, 0): 1, (1, 0): 2}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId and \
        expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId and \
        expected_nodeId__widthStart == entSt.nodeId__widthStart and \
        expected_nodeId__widthEnd == entSt.nodeId__widthEnd and \
        expected_entityType__list_nodeId == entSt.entityType__list_nodeId and \
        expected_funcStart__nodeId == entSt.funcStart__nodeId and \
        expected_funcName__list_nodeId == entSt.funcName__list_nodeId and \
        expected_nodeId__entityType == entSt.nodeId__entityType and \
        expected_nodeId__funcName == entSt.nodeId__funcName and \
        expected_nodeId__funcStart == entSt.nodeId__funcStart and \
        expected_nodeId__funcEnd == entSt.nodeId__funcEnd and \
        expected_tuple_nodeId_argIdx__pNodeId == entSt.tuple_nodeId_argIdx__pNodeId and \
        expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == entSt.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos
    )
    if verbose:
        print(str(entSt))


def test__entityStorage__getNodeIdFunNameByFuncStart0(verbose=False):
    """
1+1+1=3
 ^ ^ ^
 1 3 5

pos 1: nodeId 0
pos 3: nodeId 1
pos 5: nodeId 2
    """
    entSt = EntityStorage()
    entSt.insert(
        '+', 1, 2, EntityType.PURE_INFIX, parentNodeId=1, argIdx=0, widthStart=0, widthEnd=3
    )
    entSt.insert(
        '+', 3, 4, EntityType.PURE_INFIX, parentNodeId=2, argIdx=0, widthStart=0, widthEnd=5
    )
    entSt.insert(
        '=', 5, 6, EntityType.PURE_INFIX, parentNodeId=None, argIdx=None, widthStart=0, widthEnd=7
    )
    nodeId, funcName = entSt.getNodeIdFunNameByFuncStart(3)

    expected_nodeId = 1
    expected_funcName = '+'

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_nodeId == nodeId and\
        expected_funcName == funcName
    )
    if verbose:
        print(str(entSt))


def test__entityStorage__addConfirmedPCrelationshipById0(verbose=False):
    """
1+1+1=3
 ^ ^ ^
 1 3 5

pos 1: nodeId 0
pos 3: nodeId 1
pos 5: nodeId 2

2        (ws:1 we:6)
|
1 (arg0) (ws:1 we:4)
|
0 (arg0) (ws:1 we:2)
    """
    entSt = EntityStorage()
    entSt.insert(
        '+', 1, 2, EntityType.PURE_INFIX, widthStart=1, widthEnd=2
    )
    entSt.insert(
        '+', 3, 4, EntityType.PURE_INFIX, widthStart=3, widthEnd=4
    )
    entSt.insert(
        '=', 5, 6, EntityType.PURE_INFIX, widthStart=5, widthEnd=6
    )
    entSt.addConfirmedPCrelationshipById(1, 0, 0)
    entSt.addConfirmedPCrelationshipById(2, 1, 0)

    expected_list_tuple_widthStart_nodeId = [(1, 0), (1, 1), (1, 2)]
    expected_list_tuple_widthEnd_nodeId = [(2, 0), (4, 1), (6, 2)]
    expected_nodeId__widthStart = {0: 1, 1: 1, 2: 1}
    expected_nodeId__widthEnd = {0: 2, 1: 4, 2: 6}
    expected_entityType__list_nodeId = {EntityType.PURE_INFIX:[0, 1, 2]}
    expected_funcStart__nodeId = {1: 0, 3: 1, 5: 2}
    expected_funcName__list_nodeId = {'+': [0, 1], '=': [2]}
    expected_nodeId__entityType = {   
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    2: EntityType.PURE_INFIX}
    expected_nodeId__funcName = {0: '+', 1: '+', 2: '='}
    expected_nodeId__funcStart = {0: 1, 1: 3, 2: 5}
    expected_nodeId__funcEnd = {0: 2, 1: 4, 2: 6}
    expected_tuple_nodeId_argIdx__pNodeId = {(0, 0): 1, (1, 0): 2}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId and \
        expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId and \
        expected_nodeId__widthStart == entSt.nodeId__widthStart and \
        expected_nodeId__widthEnd == entSt.nodeId__widthEnd and \
        expected_entityType__list_nodeId == entSt.entityType__list_nodeId and \
        expected_funcStart__nodeId == entSt.funcStart__nodeId and \
        expected_funcName__list_nodeId == entSt.funcName__list_nodeId and \
        expected_nodeId__entityType == entSt.nodeId__entityType and \
        expected_nodeId__funcName == entSt.nodeId__funcName and \
        expected_nodeId__funcStart == entSt.nodeId__funcStart and \
        expected_nodeId__funcEnd == entSt.nodeId__funcEnd and \
        expected_tuple_nodeId_argIdx__pNodeId == entSt.tuple_nodeId_argIdx__pNodeId and \
        expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == entSt.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos
    )
    if verbose:
        print(str(entSt))



def test__entityStorage__existEntityAt0(verbose=False):
    """
1+1+1=3
 ^ ^ ^
 1 3 5

pos 1: nodeId 0
pos 3: nodeId 1
pos 5: nodeId 2

2        (ws:1 we:6)
|
1 (arg0) (ws:1 we:4)
|
0 (arg0) (ws:1 we:2)
    """
    entSt = EntityStorage()
    entSt.insert(
        '+', 1, 2, EntityType.PURE_INFIX, widthStart=1, widthEnd=2
    )
    entSt.insert(
        '+', 3, 4, EntityType.PURE_INFIX, widthStart=3, widthEnd=4
    )
    entSt.insert(
        '=', 5, 6, EntityType.PURE_INFIX, widthStart=5, widthEnd=6
    )
    nodeId0Exists = entSt.existEntityAt('+', 1)
    nodeId1Exists = entSt.existEntityAt('+', 3)
    nodeId2Exists = entSt.existEntityAt('=', 5)

    expected = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        nodeId0Exists and nodeId1Exists and nodeId2Exists
    )
    if verbose:
        print('nodeId0Exists', nodeId0Exists)
        print('nodeId1Exists', nodeId1Exists)
        print('nodeId2Exists', nodeId2Exists)
        print(str(entSt))



def test__entityStorage__widthMaxUpdate0(verbose=False):
    entSt = EntityStorage()
    entSt.insert(
        '=', 5, 6, EntityType.PURE_INFIX, widthStart=5, widthEnd=6
    )
    entSt.widthMaxUpdate(5, 0, 7)

    expected_list_tuple_widthStart_nodeId = [(0, 0)]
    expected_list_tuple_widthEnd_nodeId = [(7, 0)]
    expected_nodeId__widthStart = {0: 0}
    expected_nodeId__widthEnd = {0: 7}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId and \
        expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId and \
        expected_nodeId__widthStart == entSt.nodeId__widthStart and \
        expected_nodeId__widthEnd == entSt.nodeId__widthEnd
    )
    if verbose:
        print(str(entSt))



def test__entityStorage__getAllEndPosOfEntityType0(verbose=False):
    """
1+1+1=3
 ^ ^ ^
 1 3 5

pos 1: nodeId 0
pos 3: nodeId 1
pos 5: nodeId 2

2        (ws:1 we:6)
|
1 (arg0) (ws:1 we:4)
|
0 (arg0) (ws:1 we:2)
    """
    entSt = EntityStorage()
    entSt.insert(
        '+', 1, 2, EntityType.PURE_INFIX, widthStart=1, widthEnd=2
    )
    entSt.insert(
        '+', 3, 4, EntityType.PURE_INFIX, widthStart=3, widthEnd=4
    )
    entSt.insert(
        '=', 5, 6, EntityType.PURE_INFIX, widthStart=5, widthEnd=6
    )
    list_tuple_funcStart_funcEnd = entSt.getAllEndPosOfEntityType(EntityType.PURE_INFIX)

    expected_list_tuple_funcStart_funcEnd = [
    (1, 2),
    (3, 4),
    (5, 6)
    ]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_funcStart_funcEnd == list_tuple_funcStart_funcEnd
    )
    if verbose:
        print(str(entSt))




def test__entityStorage__addConfirmedPCrelationship0(verbose=False):
    """
((((1+1))+1))=3
^^^^ ^ ^^^ ^^^
0123 5 789 111
           123

infixes:
pos 5: nodeId 0 +
pos 9: nodeId 1 +
pos 13: nodeId 2 =

2        (ws: we:)
|
1 (arg0) (ws: we:)
|
0 (arg0) (ws: we:)

brackets:
(0, 12)
(1, 11)
(2, 8)
(3, 7)
    """
    entSt = EntityStorage()
    entSt.insert(
        '+', 5, 6, EntityType.PURE_INFIX, widthStart=5, widthEnd=6
    )
    entSt.insert(
        '+', 9, 10, EntityType.PURE_INFIX, widthStart=9, widthEnd=10
    )
    entSt.insert(
        '=', 13, 14, EntityType.PURE_INFIX, widthStart=13, widthEnd=14
    )

    braSt = BracketStorage() #<<<<<<<<<<<<<<also need to check if braSt was updated correctly <<<add some brackets to testcase
    braSt.insertBracket(BracketType.ROUND.value[0], 0, BracketType.ROUND.value[1], 12)
    braSt.insertBracket(BracketType.ROUND.value[0], 1, BracketType.ROUND.value[1], 11)
    braSt.insertBracket(BracketType.ROUND.value[0], 2, BracketType.ROUND.value[1], 8)
    braSt.insertBracket(BracketType.ROUND.value[0], 3, BracketType.ROUND.value[1], 7)
    entSt.addConfirmedPCrelationship(9, 0, 0, bracketstorage=braSt)
    entSt.addConfirmedPCrelationship(13, 1, 0, bracketstorage=braSt)

    expected_list_tuple_widthStart_nodeId = [(1, 0), (1, 1), (1, 2)]
    expected_list_tuple_widthEnd_nodeId = [(2, 0), (4, 1), (6, 2)]
    expected_nodeId__widthStart = {0: 1, 1: 1, 2: 1}
    expected_nodeId__widthEnd = {0: 2, 1: 4, 2: 6}
    expected_entityType__list_nodeId = {EntityType.PURE_INFIX:[0, 1, 2]}
    expected_funcStart__nodeId = {1: 0, 3: 1, 5: 2}
    expected_funcName__list_nodeId = {'+': [0, 1], '=': [2]}
    expected_nodeId__entityType = {   
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    2: EntityType.PURE_INFIX}
    expected_nodeId__funcName = {0: '+', 1: '+', 2: '='}
    expected_nodeId__funcStart = {0: 1, 1: 3, 2: 5}
    expected_nodeId__funcEnd = {0: 2, 1: 4, 2: 6}
    expected_tuple_nodeId_argIdx__pNodeId = {(0, 0): 1, (1, 0): 2}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId and \
        expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId and \
        expected_nodeId__widthStart == entSt.nodeId__widthStart and \
        expected_nodeId__widthEnd == entSt.nodeId__widthEnd and \
        expected_entityType__list_nodeId == entSt.entityType__list_nodeId and \
        expected_funcStart__nodeId == entSt.funcStart__nodeId and \
        expected_funcName__list_nodeId == entSt.funcName__list_nodeId and \
        expected_nodeId__entityType == entSt.nodeId__entityType and \
        expected_nodeId__funcName == entSt.nodeId__funcName and \
        expected_nodeId__funcStart == entSt.nodeId__funcStart and \
        expected_nodeId__funcEnd == entSt.nodeId__funcEnd and \
        expected_tuple_nodeId_argIdx__pNodeId == entSt.tuple_nodeId_argIdx__pNodeId and \
        expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == entSt.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos
    )
    if verbose:
        print(str(entSt))
        print(str(braSt))


def test__entityStorage__getAllNodeIdFuncNameWidthStartWidthEnd0(True)
    entSt = EntityStorage()
    entSt.insert(funcName, funcStart, funcEnd, entityType, parentNodeId=None, argIdx=None, widthStart=None, widthEnd=None)
    entSt.getAllNodeIdFuncNameWidthStartWidthEnd()
    expected = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
    )
    if verbose:
        print(str(entSt))

def test__entityStorage__getAllUnConfirmedPCrelationship0(verbose=False):
    entSt = EntityStorage()
    entSt.insert(funcName, funcStart, funcEnd, entityType, parentNodeId=None, argIdx=None, widthStart=None, widthEnd=None)
    entSt.getAllUnConfirmedPCrelationship(funcStart)
    expected = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
    )
    if verbose:
        print(str(entSt))




def test__entityStorage__getWidestFit0(verbose=False):
    entSt = EntityStorage()
    entSt.insert(funcName, funcStart, funcEnd, entityType, parentNodeId=None, argIdx=None, widthStart=None, widthEnd=None)
    entSt.getWidestFit(openBraPos, closeBraPos)

    expected = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
    )
    if verbose:
        print(str(entSt))




def test__entityStorage____updateTemplatesToWiderEnclosingBracketsAndRemove0(verbose=False):
    entSt = EntityStorage()
    entSt.insert(funcName, funcStart, funcEnd, entityType, parentNodeId=None, argIdx=None, widthStart=None, widthEnd=None)
    entSt._EntityStorage__updateTemplatesToWiderEnclosingBracketsAndRemove(nodeIds, bracketstorage)

    expected = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
    )
    if verbose:
        print(str(entSt))




def test__entityStorage__getAllContainingByWidth0(verbose=False):
    entSt = EntityStorage()
    entSt.insert(funcName, funcStart, funcEnd, entityType, parentNodeId=None, argIdx=None, widthStart=None, widthEnd=None)
    entSt.getAllContainingByWidth(startPos, endPos)
    expected = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
    )
    if verbose:
        print(str(entSt))




def test__entityStorage__remove0(verbose=False):
    entSt = EntityStorage()
    entSt.insert(funcName, funcStart, funcEnd, entityType, parentNodeId=None, argIdx=None, widthStart=None, widthEnd=None)
    entSt.remove(funcStart)
    expected = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
    )
    if verbose:
        print(str(entSt))



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

    expected_matrices_pos_type = [   
    {   'args': [],
        'funcEnd': 103,
        'funcName': 'pmatrix',
        'funcStart': 0,
        'funcType': 'matrix',
        'nodeId': 0,
        'widthEnd': 103,
        'widthStart': 0},
    {   'args': [],
        'funcEnd': 155,
        'funcName': 'pmatrix',
        'funcStart': 104,
        'funcType': 'matrix',
        'nodeId': 1,
        'widthEnd': 155,
        'widthStart': 104},
    {   'args': [],
        'funcEnd': 206,
        'funcName': 'pmatrix',
        'funcStart': 155,
        'funcType': 'matrix',
        'nodeId': 2,
        'widthEnd': 206,
        'widthStart': 155}]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', parser.matrices_pos_type == expected_matrices_pos_type)
    if verbose:
        print(parser.matrices_pos_type)

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

    expected_matrices_pos_type = [   
    {   'args': [],
        'funcEnd': 103,
        'funcName': 'pmatrix',
        'funcStart': 0,
        'funcType': 'matrix',
        'nodeId': 0,
        'widthEnd': 103,
        'widthStart': 0},
    {   'args': [],
        'funcEnd': 155,
        'funcName': 'pmatrix',
        'funcStart': 104,
        'funcType': 'matrix',
        'nodeId': 1,
        'widthEnd': 155,
        'widthStart': 104},
    {   'args': [],
        'funcEnd': 206,
        'funcName': 'pmatrix',
        'funcStart': 155,
        'funcType': 'matrix',
        'nodeId': 2,
        'widthEnd': 206,
        'widthStart': 155}]
    expected_has = True

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        parser.matrices_pos_type == expected_matrices_pos_type and\
        has == expected_has
        )
    if verbose:
        print(parser.matrices_pos_type)
        print(has)


def test__find_infix0(verbose=False): #TODO infix test for \\to;\\cross;\\cdot
    #\forall k \in \Z^+ and \forall prime_number p, equationStr = 1 | -1 a multivalue function
    equationStr = "(\\frac{p+1}{2})*((p-1)/2)^{(k-1)(p-1)/2})\\%p=p-1"
    parser = Latexparser(equationStr, verbose=verbose)
    parser._remove_all_spacing()
    #parser._find_matrices()
    parser._find_infix()
    expected_infixs_pos_type = [   
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 45,
        'funcName': '=',
        'funcStart': 44,
        'funcType': 'infix',
        'nodeId': 0,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 43,
        'funcName': '\\%',
        'funcStart': 41,
        'funcType': 'infix',
        'nodeId': 1,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 26,
        'funcName': '^',
        'funcStart': 25,
        'funcType': 'infix',
        'nodeId': 2,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 23,
        'funcName': '/',
        'funcStart': 22,
        'funcType': 'infix',
        'nodeId': 3,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 38,
        'funcName': '/',
        'funcStart': 37,
        'funcType': 'infix',
        'nodeId': 4,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 16,
        'funcName': '*',
        'funcStart': 15,
        'funcType': 'infix',
        'nodeId': 5,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 20,
        'funcName': '-',
        'funcStart': 19,
        'funcType': 'infix',
        'nodeId': 6,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 30,
        'funcName': '-',
        'funcStart': 29,
        'funcType': 'infix',
        'nodeId': 7,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 35,
        'funcName': '-',
        'funcStart': 34,
        'funcType': 'infix',
        'nodeId': 8,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 47,
        'funcName': '-',
        'funcStart': 46,
        'funcType': 'infix',
        'nodeId': 9,
        'widthEnd': None,
        'widthStart': None},
    {   'args': [   {   'argIdx': 0,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None},
                    {   'argIdx': 1,
                        'closeBra': None,
                        'closeBraPos': None,
                        'funcName': None,
                        'nodeId': None,
                        'openBra': None,
                        'openBraPos': None}],
        'funcEnd': 9,
        'funcName': '+',
        'funcStart': 8,
        'funcType': 'infix',
        'nodeId': 10,
        'widthEnd': None,
        'widthStart': None}]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', parser.infixs_pos_type == expected_infixs_pos_type)
    if verbose:
        # print(parser.infixs_pos_type)
        print(parser.entitystorage) # TODO

def test__find_brackets(verbose=False):
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
    # test__bracketStorage__insert0()
    # test__bracketStorage__remove0()
    # test__bracketStorage__update0()
    # test__bracketStorage__getBraPosImmediateRightOfPos0()
    # test__bracketStorage__getBraPosImmediateLeftOfPos0()
    # test__bracketStorage__exists0()
    # test__bracketStorage__getCorrespondingCloseBraPos0()
    # test__bracketStorage__getCorrespondingOpenBraPos0()
    # test__bracketStorage__getAllEnclosingBraOfPos0()
    # test__bracketStorage__getAllEnclosingTouchingBraOfPos0()
    # test__bracketStorage__getWidestEnclosingBra0()

    # test__entityStorage__insert0()
    # test__entityStorage__getNodeIdFunNameByFuncStart0()
    test__entityStorage__addConfirmedPCrelationshipById0(True)
    # test__entityStorage__existEntityAt0()
    # test__entityStorage__widthMaxUpdate0()
    # test__entityStorage__getAllEndPosOfEntityType0()
    test__entityStorage__getAllNodeIdFuncNameWidthStartWidthEnd0(True)
    test__entityStorage__addConfirmedPCrelationship0(True)
    # test__entityStorage__getAllUnConfirmedPCrelationship0(True)
    # test__entityStorage__getWidestFit0(True)
    # test__entityStorage____updateTemplatesToWiderEnclosingBracketsAndRemove0(True)
    # test__entityStorage__getAllContainingByWidth0(True)
    # test__entityStorage__remove0(True)

    # test__remove_space0(True)
    # test__find_matrices0(True)
    # test___isPosInMatrixTag0(True)
    # test__find_infix0(True) 
    # test__find_brackets(True)
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