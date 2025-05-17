import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser, BracketStorage, BracketType, EntityStorage, EntityType

pp = pprint.PrettyPrinter(indent=4)



def test__entityStorage__insert0(verbose=False):
    """
1+1+1=3
 ^ ^ ^
 1 3 5

pos 1: nodeId 0
pos 3: nodeId 1
pos 5: nodeId 2
    """
    entSt = EntityStorage(eqStrLen=len('1+1+1=3'))
    entSt.insert(
        '+', 1, 2, EntityType.PURE_INFIX, widthStart=0, widthEnd=3
    )
    entSt.insert(
        '+', 3, 4, EntityType.PURE_INFIX, widthStart=0, widthEnd=5
    )
    entSt.insert(
        '=', 5, 6, EntityType.PURE_INFIX, widthStart=0, widthEnd=7
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
    expected_tuple_nodeId_argIdx__pNodeId = {}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {
    (0, 0): (None, 0, None, 1),
    (0, 1): (None, 1, None, 7),
    (1, 0): (None, 0, None, 3),
    (1, 1): (None, 3, None, 7),
    (2, 0): (None, 0, None, 5),
    (2, 1): (None, 5, None, 7)}

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
    entSt = EntityStorage(eqStrLen=len('1+1+1=3'))
    entSt.insert(
        '+', 1, 2, EntityType.PURE_INFIX, widthStart=0, widthEnd=3
    )
    entSt.insert(
        '+', 3, 4, EntityType.PURE_INFIX, widthStart=0, widthEnd=5
    )
    entSt.insert(
        '=', 5, 6, EntityType.PURE_INFIX, widthStart=0, widthEnd=7
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
    entSt = EntityStorage(eqStrLen=len('1+1+1=3'))
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
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {
    (0, 0): (None, 0, None, 1),
    (0, 1): (None, 1, None, 7),
    (1, 1): (None, 3, None, 7),
    (2, 1): (None, 5, None, 7)}

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
    entSt = EntityStorage(eqStrLen=len('1+1+1=3'))
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
    entSt = EntityStorage(eqStrLen=7)
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




def test__entityStorage__getAllNodeIdFuncNameWidthStartWidthEnd0(verbose=False):
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
    entSt = EntityStorage(eqStrLen=len('1+1+1=3'))
    entSt.insert(
        '+', 1, 2, EntityType.PURE_INFIX, widthStart=1, widthEnd=2
    )
    entSt.insert(
        '+', 3, 4, EntityType.PURE_INFIX, widthStart=3, widthEnd=4
    )
    entSt.insert(
        '=', 5, 6, EntityType.PURE_INFIX, widthStart=5, widthEnd=6
    )
    list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd = entSt.getAllNodeIdFuncNameWidthStartWidthEnd()
    expected_list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd = [(0, '+', 1, 2, 1, 2), (1, '+', 3, 4, 3, 4), (2, '=', 5, 6, 5, 6)]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd == expected_list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd
    )
    if verbose:
        print('list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd', list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd)
        print(str(entSt))


def test__entityStorage__addConfirmedPCrelationship0(verbose=False):
    """
((((1+1))+1))=3
^^^^^^^^^^^^^^^
012345678911111
          01234

infixes:
pos 5: nodeId 0 +
pos 9: nodeId 1 +
pos 13: nodeId 2 =

2        (ws: we:)
|
1 (arg0) (ws: we:)
|
0 (arg0) (ws: we:)

nums:
3 4  -> 0 5
4 6  -> 0 5
5 10 -> 1 9
6 14 -> 2 13


brackets:
(0, 12)
(1, 11)
(2, 8)
(3, 7)


(0, 12)~(1, 11) touching_each_other and enclosing pos5 <<<<<<<<set0

(2, 8)~(3, 7) touching_each_other and enclosing pos5 <<<<<<<<set1

but
__updateTemplatesToWiderEnclosingBracketsAndRemove only returns 1 set, that is set0 and then deletes everything
    """
    entSt = EntityStorage(eqStrLen=len('((((1+1))+1))=3'))
    entSt.insert(
        '+', 5, 6, EntityType.PURE_INFIX, widthStart=5, widthEnd=6
    )#0
    entSt.insert(
        '+', 9, 10, EntityType.PURE_INFIX, widthStart=9, widthEnd=10
    )#1
    entSt.insert(
        '=', 13, 14, EntityType.PURE_INFIX, widthStart=13, widthEnd=14
    )#2
    #
    entSt.insert(
        '1', 4, 5, EntityType.PURE_NUMBER, widthStart=4, widthEnd=5
    )#3
    entSt.insert(
        '1', 6, 7, EntityType.PURE_NUMBER, widthStart=6, widthEnd=7
    )#4
    entSt.insert(
        '1', 10, 11, EntityType.PURE_NUMBER, widthStart=10, widthEnd=11
    )#5
    entSt.insert(
        '3', 14, 15, EntityType.PURE_NUMBER, widthStart=14, widthEnd=15
    )#6

    braSt = BracketStorage() #<<<<<<<<<<<<<<also need to check if braSt was updated correctly <<<add some brackets to testcase
    braSt.insertBracket(BracketType.ROUND.value[0], 0, BracketType.ROUND.value[1], 12)
    braSt.insertBracket(BracketType.ROUND.value[0], 1, BracketType.ROUND.value[1], 11)
    braSt.insertBracket(BracketType.ROUND.value[0], 2, BracketType.ROUND.value[1], 8)
    braSt.insertBracket(BracketType.ROUND.value[0], 3, BracketType.ROUND.value[1], 7)
    braSt = entSt.addConfirmedPCrelationship(5, 3, 0, bracketstorage=braSt)#pFuncStart, cNodeId, argId
    braSt = entSt.addConfirmedPCrelationship(5, 4, 1, bracketstorage=braSt)
    braSt = entSt.addConfirmedPCrelationship(9, 5, 1, bracketstorage=braSt)
    braSt = entSt.addConfirmedPCrelationship(13, 6, 1, bracketstorage=braSt)
    braSt = entSt.addConfirmedPCrelationship(9, 0, 0, bracketstorage=braSt)
    braSt = entSt.addConfirmedPCrelationship(13, 1, 0, bracketstorage=braSt)
    #NOTE nodeId=0 is lowest_child and its width is not updated.
    #NOTE nodeId=1 is (0, 12), width up til the largest braclet
    #NOTE nodeId=2 is the =, width is the whole equation (0, 14)
    """
    nodeId ~ widthStart ~ widthEnd
    0 ~ 2 ~ 8
    1 ~ 0 ~ 12
    2 ~ 0  ~ 15
    3 ~ 4 ~ 5
    4 ~ 6 ~ 7
    5 ~ 10 ~ 11
    6 ~ 14 ~ 15
    """

    expected_list_tuple_widthStart_nodeId = [(4, 3), (2, 0), (6, 4), (0, 1), (10, 5), (0, 2), (14, 6)]
    expected_list_tuple_widthEnd_nodeId = [(5, 3), (8, 0), (7, 4), (12, 1), (11, 5), (15, 2), (15, 6)]
    expected_nodeId__widthStart = {0: 2, 1: 0, 2: 0, 3: 4, 4: 6, 5: 10, 6: 14} # <<<<<<<<<<<<<<<<<<nodeId 0, 1 are not correct
    expected_nodeId__widthEnd = {0: 8, 1: 12, 2: 15, 3: 5, 4: 7, 5: 11, 6: 15}
    expected_entityType__list_nodeId = {EntityType.PURE_INFIX:[0, 1, 2], EntityType.PURE_NUMBER:[3, 4, 5, 6]}
    expected_funcStart__nodeId = {4: 3, 5: 0, 6: 4, 9: 1, 10: 5, 13: 2, 14: 6}
    expected_funcName__list_nodeId = {'+': [0, 1], '1': [3, 4, 5], '3': [6], '=': [2]}
    expected_nodeId__entityType = {   
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    2: EntityType.PURE_INFIX,
    3: EntityType.PURE_NUMBER,
    4: EntityType.PURE_NUMBER,
    5: EntityType.PURE_NUMBER,
    6: EntityType.PURE_NUMBER}
    expected_nodeId__funcName = {0: '+', 1: '+', 2: '=', 3: '1', 4: '1', 5: '1', 6: '3'}
    expected_nodeId__funcStart = {0: 5, 1: 9, 2: 13, 3: 4, 4: 6, 5: 10, 6: 14}
    expected_nodeId__funcEnd = {0: 6, 1: 10, 2: 14, 3: 5, 4: 7, 5: 11, 6: 15}
    expected_tuple_nodeId_argIdx__pNodeId = {(0, 0): 1, (1, 0): 2, (3, 0): 0, (4, 1): 0, (5, 1): 1, (6, 1): 2}#<<<but already got answer.
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {}

    expected_closeBraType__sortedPosList = {}
    expected_openBraType__sortedPosList = {}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {}
    expected_list_tuple_width_id_openPos_closePos = []
    expected_openBraPos__bracketId = {}
    expected_closeBraPos__bracketId = {}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId \
        and expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId \
        and expected_nodeId__widthStart == entSt.nodeId__widthStart \
        and expected_nodeId__widthEnd == entSt.nodeId__widthEnd \
        and expected_entityType__list_nodeId == entSt.entityType__list_nodeId \
        and expected_funcStart__nodeId == entSt.funcStart__nodeId \
        and expected_funcName__list_nodeId == entSt.funcName__list_nodeId \
        and expected_nodeId__entityType == entSt.nodeId__entityType \
        and expected_nodeId__funcName == entSt.nodeId__funcName \
        and expected_nodeId__funcStart == entSt.nodeId__funcStart \
        and expected_nodeId__funcEnd == entSt.nodeId__funcEnd \
        and expected_tuple_nodeId_argIdx__pNodeId == entSt.tuple_nodeId_argIdx__pNodeId \
        and expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == entSt.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos
    )
    if verbose:
        print(str(entSt))
        print(str(braSt))


def test__entityStorage__addUnConfirmedPCrelationship0(verbose=False):
    """
\\sin(x+\\pi)=-\\sin(x)
^ ^  ^^^^ ^ ^^^^ ^  ^^^
0 1  4567 8 1111 1  111
            0123 4  789

entSt.insert ORDER:
+     6
=     11
-     12
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<braSt.insertBraket
pi  8
sin 1 <addUnconfirm
sin 14 <addUnconfirm
x     5
x     18

braSt.insertBracket ORDER:
(4, 10)
(17, 19)
    """
    braSt = BracketStorage() 
    entSt = EntityStorage(eqStrLen=len('\\sin(x+\\pi)=-\\sin(x)'))
    entSt.insert('+', 6, 7, EntityType.PURE_INFIX, 
        widthStart=6, widthEnd=7)
    entSt.insert('=', 11, 12, EntityType.PURE_INFIX, 
        widthStart=11, widthEnd=12)
    entSt.insert('-', 12, 13, EntityType.PURE_INFIX, 
        widthStart=12, widthEnd=13)
    #<<<<<<<<<<<
    braSt.insertBracket(BracketType.ROUND.value[0], 4, BracketType.ROUND.value[1], 10)
    braSt.insertBracket(BracketType.ROUND.value[0], 17, BracketType.ROUND.value[1], 19)
    #<<<<<<<<<<<
    entSt.insert('pi', 8, 10, EntityType.BACKSLASH_NUMBER, 
        widthStart=8, widthEnd=10)#\\pi
    entSt.insert('sin', 1, 4, EntityType.BACKSLASH_FUNCTION, 
        widthStart=1, widthEnd=4)

    entSt.addUnConfirmedPCrelationship(1, 1, BracketType.ROUND.value[0], 4, BracketType.ROUND.value[1], 10)

    entSt.insert('sin', 14, 17, EntityType.BACKSLASH_FUNCTION, 
        widthStart=14, widthEnd=17)

    entSt.addUnConfirmedPCrelationship(14, 1, BracketType.ROUND.value[0], 17, BracketType.ROUND.value[1], 19)

    entSt.insert('x', 5, 6, EntityType.PURE_VARIABLE, 
        widthStart=5, widthEnd=6)
    entSt.insert('x', 18, 19, EntityType.PURE_VARIABLE, 
        widthStart=18, widthEnd=19)

    """
    nodeId ~ widthStart ~ widthEnd
    0 ~ 6 ~ 7
    1 ~ 11 ~ 12
    2 ~ 12 ~ 13
    3 ~ 8 ~ 10
    4 ~ 1 ~ 4
    5 ~ 14 ~ 17
    6 ~ 5 ~ 6
    7 ~ 18 ~ 19
    """
    expected_list_tuple_widthStart_nodeId = [(1, 4), (5, 6), (6, 0), (8, 3), (11, 1), (12, 2), (14, 5), (18, 7)]
    expected_list_tuple_widthEnd_nodeId = [(4, 4), (6, 6), (7, 0), (10, 3), (12, 1), (13, 2), (17, 5), (19, 7)]
    expected_nodeId__widthStart = {0: 6, 1: 11, 2: 12, 3: 8, 4: 1, 5: 14, 6: 5, 7: 18}
    expected_nodeId__widthEnd = {0: 7, 1: 12, 2: 13, 3: 10, 4: 4, 5: 17, 6: 6, 7: 19}
    expected_entityType__list_nodeId = {
        EntityType.PURE_INFIX: [0, 1, 2],
        EntityType.BACKSLASH_NUMBER: [3],
        EntityType.BACKSLASH_FUNCTION: [4, 5],
        EntityType.PURE_VARIABLE: [6, 7]}
    expected_funcStart__nodeId = {1: 4, 5: 6, 6: 0, 8: 3, 11: 1, 12: 2, 14: 5, 18: 7}
    expected_funcName__list_nodeId = {'+': [0], '-': [2], '=': [1], 'pi': [3], 'sin': [4, 5], 'x': [6, 7]}
    expected_nodeId__entityType = {
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    2: EntityType.PURE_INFIX,
    3: EntityType.BACKSLASH_NUMBER,
    4: EntityType.BACKSLASH_FUNCTION,
    5: EntityType.BACKSLASH_FUNCTION,
    6: EntityType.PURE_VARIABLE,
    7: EntityType.PURE_VARIABLE}
    expected_nodeId__funcName = {0: '+', 1: '=', 2: '-', 3: 'pi', 4: 'sin', 5: 'sin', 6: 'x', 7: 'x'}
    expected_nodeId__funcStart = {0: 6, 1: 11, 2: 12, 3: 8, 4: 1, 5: 14, 6: 5, 7: 18}
    expected_nodeId__funcEnd = {0: 7, 1: 12, 2: 13, 3: 10, 4: 4, 5: 17, 6: 6, 7: 19}
    expected_tuple_nodeId_argIdx__pNodeId = {}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {
    (0, 0): (None, 0, None, 6),
    (0, 1): (None, 6, None, 20),
    (1, 0): (None, 0, None, 11),
    (1, 1): (None, 11, None, 20),
    (2, 0): (None, 0, None, 12),
    (2, 1): (None, 12, None, 20),
    (4, 1): ('(', 4, ')', 10),
    (5, 1): ('(', 17, ')', 19)}
    expected_closeBraType__sortedPosList = {')': [10, 19]}
    expected_openBraType__sortedPosList = {'(': [4, 17]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (4, '(', 10, ')'), 1: (17, '(', 19, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(2, 1, 17, 19), (6, 0, 4, 10)]
    expected_openBraPos__bracketId = {4: 0, 17: 1}
    expected_closeBraPos__bracketId = {10: 0, 19: 1}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId and\
        expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId and\
        expected_nodeId__widthStart == entSt.nodeId__widthStart and\
        expected_nodeId__widthEnd == entSt.nodeId__widthEnd and\
        expected_entityType__list_nodeId == entSt.entityType__list_nodeId and\
        expected_funcStart__nodeId == entSt.funcStart__nodeId and\
        expected_funcName__list_nodeId == entSt.funcName__list_nodeId and\
        expected_nodeId__entityType == entSt.nodeId__entityType and\
        expected_nodeId__funcName == entSt.nodeId__funcName and\
        expected_nodeId__funcStart == entSt.nodeId__funcStart and\
        expected_nodeId__funcEnd == entSt.nodeId__funcEnd and\
        expected_tuple_nodeId_argIdx__pNodeId == entSt.tuple_nodeId_argIdx__pNodeId and\
        expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == entSt.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos and\
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and\
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and\
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId
    )
    if verbose:
        print(str(entSt))
        print(str(braSt))


def test__entityStorage__getAllUnConfirmedPCrelationship0(verbose=False):
    """
\\sin(x+\\pi)=-\\sin(x)
^ ^  ^^^^ ^ ^^^^ ^  ^^^
0 1  4567 8 1111 1  111
            0123 4  789

entSt.insert ORDER:
+     6
=     11
-     12
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<braSt.insertBraket
pi  8
sin 1 <addUnconfirm
sin 14 <addUnconfirm
x     5
x     18

braSt.insertBracket ORDER:
(4, 10)
(17, 19)
    """
    braSt = BracketStorage() 
    entSt = EntityStorage(eqStrLen=len('\\sin(x+\\pi)=-\\sin(x)'))
    entSt.insert('+', 6, 7, EntityType.PURE_INFIX, 
        widthStart=6, widthEnd=7)
    entSt.insert('=', 11, 12, EntityType.PURE_INFIX, 
        widthStart=11, widthEnd=12)
    entSt.insert('-', 12, 13, EntityType.PURE_INFIX, 
        widthStart=12, widthEnd=13)
    #<<<<<<<<<<<
    braSt.insertBracket(BracketType.ROUND.value[0], 4, BracketType.ROUND.value[1], 10)
    braSt.insertBracket(BracketType.ROUND.value[0], 17, BracketType.ROUND.value[1], 19)
    #<<<<<<<<<<<
    entSt.insert('pi', 8, 10, EntityType.BACKSLASH_NUMBER, 
        widthStart=8, widthEnd=10)#\\pi
    entSt.insert('sin', 1, 4, EntityType.BACKSLASH_FUNCTION, 
        widthStart=1, widthEnd=4)

    entSt.addUnConfirmedPCrelationship(1, 1, BracketType.ROUND.value[0], 4, BracketType.ROUND.value[1], 10)

    entSt.insert('sin', 14, 17, EntityType.BACKSLASH_FUNCTION, 
        widthStart=14, widthEnd=17)

    entSt.addUnConfirmedPCrelationship(14, 1, BracketType.ROUND.value[0], 17, BracketType.ROUND.value[1], 19)

    entSt.insert('x', 5, 6, EntityType.PURE_VARIABLE, 
        widthStart=5, widthEnd=6)
    entSt.insert('x', 18, 19, EntityType.PURE_VARIABLE, 
        widthStart=18, widthEnd=19)


    list_tuple_openBraPos_closeBraPos_argIdx__nodeId0 = entSt.getAllUnConfirmedPCrelationship(0)
    list_tuple_openBraPos_closeBraPos_argIdx__nodeId1 = entSt.getAllUnConfirmedPCrelationship(1)
    list_tuple_openBraPos_closeBraPos_argIdx__nodeId2 = entSt.getAllUnConfirmedPCrelationship(2)
    list_tuple_openBraPos_closeBraPos_argIdx__nodeId4 = entSt.getAllUnConfirmedPCrelationship(4)
    list_tuple_openBraPos_closeBraPos_argIdx__nodeId5 = entSt.getAllUnConfirmedPCrelationship(5)

    """
    nodeId ~ widthStart ~ widthEnd
    0 ~ 6 ~ 7
    1 ~ 11 ~ 12
    2 ~ 12 ~ 13
    3 ~ 8 ~ 10
    4 ~ 1 ~ 4
    5 ~ 14 ~ 17
    6 ~ 5 ~ 6
    7 ~ 18 ~ 19
    """
    expected_list_tuple_widthStart_nodeId = [(1, 4), (5, 6), (6, 0), (8, 3), (11, 1), (12, 2), (14, 5), (18, 7)]
    expected_list_tuple_widthEnd_nodeId = [(4, 4), (6, 6), (7, 0), (10, 3), (12, 1), (13, 2), (17, 5), (19, 7)]
    expected_nodeId__widthStart = {0: 6, 1: 11, 2: 12, 3: 8, 4: 1, 5: 14, 6: 5, 7: 18}
    expected_nodeId__widthEnd = {0: 7, 1: 12, 2: 13, 3: 10, 4: 4, 5: 17, 6: 6, 7: 19}
    expected_entityType__list_nodeId = {
        EntityType.PURE_INFIX: [0, 1, 2],
        EntityType.BACKSLASH_NUMBER: [3],
        EntityType.BACKSLASH_FUNCTION: [4, 5],
        EntityType.PURE_VARIABLE: [6, 7]}
    expected_funcStart__nodeId = {1: 4, 5: 6, 6: 0, 8: 3, 11: 1, 12: 2, 14: 5, 18: 7}
    expected_funcName__list_nodeId = {'+': [0], '-': [2], '=': [1], 'pi': [3], 'sin': [4, 5], 'x': [6, 7]}
    expected_nodeId__entityType = {
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    2: EntityType.PURE_INFIX,
    3: EntityType.BACKSLASH_NUMBER,
    4: EntityType.BACKSLASH_FUNCTION,
    5: EntityType.BACKSLASH_FUNCTION,
    6: EntityType.PURE_VARIABLE,
    7: EntityType.PURE_VARIABLE}
    expected_nodeId__funcName = {0: '+', 1: '=', 2: '-', 3: 'pi', 4: 'sin', 5: 'sin', 6: 'x', 7: 'x'}
    expected_nodeId__funcStart = {0: 6, 1: 11, 2: 12, 3: 8, 4: 1, 5: 14, 6: 5, 7: 18}
    expected_nodeId__funcEnd = {0: 7, 1: 12, 2: 13, 3: 10, 4: 4, 5: 17, 6: 6, 7: 19}
    expected_tuple_nodeId_argIdx__pNodeId = {}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {
    (0, 0): (None, 0, None, 6),
    (0, 1): (None, 6, None, 20),
    (1, 0): (None, 0, None, 11),
    (1, 1): (None, 11, None, 20),
    (2, 0): (None, 0, None, 12),
    (2, 1): (None, 12, None, 20),
    (4, 1): ('(', 4, ')', 10),
    (5, 1): ('(', 17, ')', 19)}
    expected_closeBraType__sortedPosList = {')': [10, 19]}
    expected_openBraType__sortedPosList = {'(': [4, 17]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {0: (4, '(', 10, ')'), 1: (17, '(', 19, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(2, 1, 17, 19), (6, 0, 4, 10)]
    expected_openBraPos__bracketId = {4: 0, 17: 1}
    expected_closeBraPos__bracketId = {10: 0, 19: 1}

    expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId0 = [(0,6,0),(6,20,1)]
    expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId1 = [(0,11,0),(11,20,1)]
    expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId2 = [(0,12,0),(12,20,1)]
    expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId4 = [(4,10,1)]
    expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId5 = [(17,19,1)]



    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId and\
        expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId and\
        expected_nodeId__widthStart == entSt.nodeId__widthStart and\
        expected_nodeId__widthEnd == entSt.nodeId__widthEnd and\
        expected_entityType__list_nodeId == entSt.entityType__list_nodeId and\
        expected_funcStart__nodeId == entSt.funcStart__nodeId and\
        expected_funcName__list_nodeId == entSt.funcName__list_nodeId and\
        expected_nodeId__entityType == entSt.nodeId__entityType and\
        expected_nodeId__funcName == entSt.nodeId__funcName and\
        expected_nodeId__funcStart == entSt.nodeId__funcStart and\
        expected_nodeId__funcEnd == entSt.nodeId__funcEnd and\
        expected_tuple_nodeId_argIdx__pNodeId == entSt.tuple_nodeId_argIdx__pNodeId and\
        expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == entSt.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos and\
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and\
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and\
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId and\
        expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId0 == list_tuple_openBraPos_closeBraPos_argIdx__nodeId0 and\
        expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId1 == list_tuple_openBraPos_closeBraPos_argIdx__nodeId1 and\
        expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId2 == list_tuple_openBraPos_closeBraPos_argIdx__nodeId2 and\
        expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId4 == list_tuple_openBraPos_closeBraPos_argIdx__nodeId4 and\
        expected_list_tuple_openBraPos_closeBraPos_argIdx__nodeId5 == list_tuple_openBraPos_closeBraPos_argIdx__nodeId5
    )
    if verbose:
        print(str(entSt))
        print(str(braSt))
        print('list_tuple_openBraPos_closeBraPos_argIdx__nodeId0')
        print(list_tuple_openBraPos_closeBraPos_argIdx__nodeId0)
        print('list_tuple_openBraPos_closeBraPos_argIdx__nodeId1')
        print(list_tuple_openBraPos_closeBraPos_argIdx__nodeId1)
        print('list_tuple_openBraPos_closeBraPos_argIdx__nodeId2')
        print(list_tuple_openBraPos_closeBraPos_argIdx__nodeId2)
        print('list_tuple_openBraPos_closeBraPos_argIdx__nodeId4')
        print(list_tuple_openBraPos_closeBraPos_argIdx__nodeId4)
        print('list_tuple_openBraPos_closeBraPos_argIdx__nodeId5')
        print(list_tuple_openBraPos_closeBraPos_argIdx__nodeId5)




def test__entityStorage__getWidestFit0(verbose=False):
    """
\\sin(x+\\pi)=-\\sin(x)
^ ^  ^^^^ ^ ^^^^ ^  ^^^
0 1  4567 8 1111 1  111
            0123 4  789

entSt.insert ORDER:
+     6
=     11
-     12
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<braSt.insertBracket
pi  8
sin 1 <addUnconfirm
sin 14 <addUnconfirm
x     5
x     18
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<_find_infixes_arg_brackets_width [add children to backslashes]

braSt.insertBracket ORDER:
(4, 10)
(17, 19)
    """
    braSt = BracketStorage() 
    entSt = EntityStorage(eqStrLen=len('\\sin(x+\\pi)=-\\sin(x)'))
    entSt.insert('+', 6, 7, EntityType.PURE_INFIX, 
        widthStart=6, widthEnd=7)
    entSt.insert('=', 11, 12, EntityType.PURE_INFIX, 
        widthStart=11, widthEnd=12)
    entSt.insert('-', 12, 13, EntityType.PURE_INFIX, 
        widthStart=12, widthEnd=13)
    #<<<<<<<<<<<
    braSt.insertBracket(BracketType.ROUND.value[0], 4, BracketType.ROUND.value[1], 10)
    braSt.insertBracket(BracketType.ROUND.value[0], 17, BracketType.ROUND.value[1], 19)
    #<<<<<<<<<<<
    entSt.insert('pi', 8, 10, EntityType.BACKSLASH_NUMBER, 
        widthStart=8, widthEnd=10)#\\pi
    entSt.insert('sin', 1, 4, EntityType.BACKSLASH_FUNCTION, 
        widthStart=1, widthEnd=4)

    entSt.addUnConfirmedPCrelationship(1, 1, BracketType.ROUND.value[0], 4, BracketType.ROUND.value[1], 10)

    entSt.insert('sin', 14, 17, EntityType.BACKSLASH_FUNCTION, 
        widthStart=14, widthEnd=17)

    entSt.addUnConfirmedPCrelationship(14, 1, BracketType.ROUND.value[0], 17, BracketType.ROUND.value[1], 19)

    entSt.insert('x', 5, 6, EntityType.PURE_VARIABLE, 
        widthStart=5, widthEnd=6)
    entSt.insert('x', 18, 19, EntityType.PURE_VARIABLE, 
        widthStart=18, widthEnd=19)

    braSt = entSt.addConfirmedPCrelationship(6, 6, 0, bracketstorage=braSt) # also removes the (4, 10) containing this arg
    braSt = entSt.addConfirmedPCrelationship(6, 3, 1, bracketstorage=braSt) # also removes the (4, 10) containing this arg

    nodeId4, funcName4 = entSt.getWidestFit(4, 10)
    nodeId5, funcName5 = entSt.getWidestFit(17, 19)

    """
    nodeId ~ widthStart ~ widthEnd
    0 ~ 6 ~ 7                      +
    1 ~ 11 ~ 12                    =
    2 ~ 12 ~ 13                    -
    3 ~ 8 ~ 10                     pi
    4 ~ 1 ~ 4                      sin
    5 ~ 14 ~ 17                    sin
    6 ~ 5 ~ 6                      x
    7 ~ 18 ~ 19                    x
    """
    expected_list_tuple_widthStart_nodeId = [(1, 4), (5, 6), (4, 0), (8, 3), (11, 1), (12, 2), (14, 5), (18, 7)]
    expected_list_tuple_widthEnd_nodeId = [(4, 4), (6, 6), (10, 0), (10, 3), (12, 1), (13, 2), (17, 5), (19, 7)]
    expected_nodeId__widthStart = {0: 4, 1: 11, 2: 12, 3: 8, 4: 1, 5: 14, 6: 5, 7: 18}
    expected_nodeId__widthEnd = {0: 10, 1: 12, 2: 13, 3: 10, 4: 4, 5: 17, 6: 6, 7: 19}
    expected_entityType__list_nodeId = {
        EntityType.PURE_INFIX: [0, 1, 2],
        EntityType.BACKSLASH_NUMBER: [3],
        EntityType.BACKSLASH_FUNCTION: [4, 5],
        EntityType.PURE_VARIABLE: [6, 7]}
    expected_funcStart__nodeId = {1: 4, 5: 6, 6: 0, 8: 3, 11: 1, 12: 2, 14: 5, 18: 7}
    expected_funcName__list_nodeId = {'+': [0], '-': [2], '=': [1], 'pi': [3], 'sin': [4, 5], 'x': [6, 7]}
    expected_nodeId__entityType = {
    0: EntityType.PURE_INFIX,
    1: EntityType.PURE_INFIX,
    2: EntityType.PURE_INFIX,
    3: EntityType.BACKSLASH_NUMBER,
    4: EntityType.BACKSLASH_FUNCTION,
    5: EntityType.BACKSLASH_FUNCTION,
    6: EntityType.PURE_VARIABLE,
    7: EntityType.PURE_VARIABLE}
    expected_nodeId__funcName = {0: '+', 1: '=', 2: '-', 3: 'pi', 4: 'sin', 5: 'sin', 6: 'x', 7: 'x'}
    expected_nodeId__funcStart = {0: 6, 1: 11, 2: 12, 3: 8, 4: 1, 5: 14, 6: 5, 7: 18}
    expected_nodeId__funcEnd = {0: 7, 1: 12, 2: 13, 3: 10, 4: 4, 5: 17, 6: 6, 7: 19}
    expected_tuple_nodeId_argIdx__pNodeId = {(3, 1): 0, (6, 0): 0}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {
    # (0, 0): (None, 0, None, 6),
    # (0, 1): (None, 6, None, 20),
    (1, 0): (None, 0, None, 11),
    (1, 1): (None, 11, None, 20),
    (2, 0): (None, 0, None, 12),
    (2, 1): (None, 12, None, 20),
    (4, 1): ('(', 4, ')', 10),
    (5, 1): ('(', 17, ')', 19)}
    expected_closeBraType__sortedPosList = {')': [19]}
    expected_openBraType__sortedPosList = {'(': [17]}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {1: (17, '(', 19, ')')}
    expected_list_tuple_width_id_openPos_closePos = [(2, 1, 17, 19)]
    expected_openBraPos__bracketId = {17: 1}
    expected_closeBraPos__bracketId = {19: 1}

    expected_nodeId4 = 0
    expected_funcName4 = '+'
    expected_nodeId5 = 7
    expected_funcName5 = 'x'

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId and\
        expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId and\
        expected_nodeId__widthStart == entSt.nodeId__widthStart and\
        expected_nodeId__widthEnd == entSt.nodeId__widthEnd and\
        expected_entityType__list_nodeId == entSt.entityType__list_nodeId and\
        expected_funcStart__nodeId == entSt.funcStart__nodeId and\
        expected_funcName__list_nodeId == entSt.funcName__list_nodeId and\
        expected_nodeId__entityType == entSt.nodeId__entityType and\
        expected_nodeId__funcName == entSt.nodeId__funcName and\
        expected_nodeId__funcStart == entSt.nodeId__funcStart and\
        expected_nodeId__funcEnd == entSt.nodeId__funcEnd and\
        expected_tuple_nodeId_argIdx__pNodeId == entSt.tuple_nodeId_argIdx__pNodeId and\
        expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == entSt.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos and\
        expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList and\
        expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList and\
        expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType and\
        expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos and\
        expected_openBraPos__bracketId == braSt.openBraPos__bracketId and\
        expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId and\
        expected_nodeId4 == nodeId4 and\
        expected_funcName4 == funcName4 and\
        expected_nodeId5 == nodeId5 and\
        expected_funcName5 == funcName5
    )
    if verbose:
        print(str(entSt))
        print(str(braSt))
        print('nodeId4', nodeId4)
        print('funcName4', funcName4)
        print('nodeId5', nodeId5)
        print('funcName5', funcName5)




def test__entityStorage____updateTemplatesToWiderEnclosingBracketsAndRemove0(verbose=False):
    """
((((\\sin((x+\\pi)))+(\\sin(x)))))=0
^^^^^ ^  ^^^^^ ^ ^^^^^^ ^  ^^^^^^^^^
01234 56789111 11111112 222222222333
           012 34567890 123456789012



entSt.insert ORDER:
0  +     11
1  +     18
2  =     31
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<braSt.insertBracket
3  pi    13
4  sin   4 <addUnconfirm
5  sin   20 <addUnconfirm
6  x     10
7  x     25
8  0     32
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<_find_infixes_arg_brackets_width [add children to backslashes]

braSt.insertBracket ORDER:
(0, 30) ~ 0
(1, 29) ~ 1
(2, 28) ~ 2
(3, 17) ~ 3
(8, 16) ~ 4
(9, 15) ~ 5
(19, 27) ~ 6
(24, 26) ~ 7

    """
    braSt = BracketStorage()
    entSt = EntityStorage(eqStrLen=len('((((\\sin((x+\\pi)))+(\\sin(x)))))=0'))


    entSt.insert('+', 11, 12, EntityType.PURE_INFIX, 
        widthStart=11, widthEnd=12) #0
    entSt.insert('+', 18, 19, EntityType.PURE_INFIX, 
        widthStart=18, widthEnd=19) #1
    entSt.insert('=', 31, 32, EntityType.PURE_INFIX, 
        widthStart=31, widthEnd=32) #2
    #<<<<<<<<<<<
    braSt.insertBracket(BracketType.ROUND.value[0], 0, BracketType.ROUND.value[1], 30)
    braSt.insertBracket(BracketType.ROUND.value[0], 1, BracketType.ROUND.value[1], 29)
    braSt.insertBracket(BracketType.ROUND.value[0], 2, BracketType.ROUND.value[1], 28)
    braSt.insertBracket(BracketType.ROUND.value[0], 3, BracketType.ROUND.value[1], 17)
    braSt.insertBracket(BracketType.ROUND.value[0], 8, BracketType.ROUND.value[1], 16)
    braSt.insertBracket(BracketType.ROUND.value[0], 9, BracketType.ROUND.value[1], 15)
    braSt.insertBracket(BracketType.ROUND.value[0], 19, BracketType.ROUND.value[1], 27)
    braSt.insertBracket(BracketType.ROUND.value[0], 24, BracketType.ROUND.value[1], 26)
    #<<<<<<<<<<<
    entSt.insert('pi', 13, 15, EntityType.BACKSLASH_NUMBER, 
        widthStart=13, widthEnd=15)#\\pi #3
    entSt.insert('sin', 4, 8, EntityType.BACKSLASH_FUNCTION, 
        widthStart=4, widthEnd=8) #4

    openBraPos = 8 # (sin, 5)
    entSt.addUnConfirmedPCrelationship(4, 1, BracketType.ROUND.value[0], openBraPos, BracketType.ROUND.value[1], 16)#<<<<<in main_code, _find_backslash will remove the bracket. add auto remove to addUnConfirmedPCrelationship??
    braSt.removeBracket(openBraPos)
    entSt.widthMaxUpdate(4, openBraPos, 16)

    entSt.insert('sin', 20, 24, EntityType.BACKSLASH_FUNCTION, 
        widthStart=20, widthEnd=24) #5

    openBraPos = 24 # (sin, 21)
    entSt.addUnConfirmedPCrelationship(20, 1, BracketType.ROUND.value[0], openBraPos, BracketType.ROUND.value[1], 26)#<<<<<in main_code, _find_backslash will remove the bracket. add auto remove to addUnConfirmedPCrelationship??
    
    braSt.removeBracket(openBraPos)
    entSt.widthMaxUpdate(20, openBraPos, 26)
    # print('updating nodeId: 5~~~~~~~~~~~~~~~~~~~~~~~~')
    braSt = entSt._EntityStorage__updateTemplatesToWiderEnclosingBracketsAndRemove([5], braSt)
    # print(str(entSt))#<<<<< not updated at all #(19, 27) ~ 6 NOT USED?

    entSt.insert('x', 10, 11, EntityType.PURE_VARIABLE, 
        widthStart=10, widthEnd=11) #6
    entSt.insert('x', 25, 26, EntityType.PURE_VARIABLE, 
        widthStart=25, widthEnd=26) #7
    entSt.insert('0', 32, 33, EntityType.PURE_NUMBER, 
        widthStart=32, widthEnd=33) #7

    # print('addConfirmedPCrelationship');
    braSt = entSt.addConfirmedPCrelationship(11, 6, 0, bracketstorage=braSt) #(sin, 11) also removes the (4, 10) containing this arg
    braSt = entSt.addConfirmedPCrelationship(11, 3, 1, bracketstorage=braSt) # also removes the (4, 10) containing this arg
    braSt = entSt._EntityStorage__updateTemplatesToWiderEnclosingBracketsAndRemove([4, 5], braSt)
    # print('after updating 4, 5')
    # print(str(entSt))
    braSt = entSt.addConfirmedPCrelationship(18, 4, 0, bracketstorage=braSt)#funcStart, cNodeId, argId (sin, 18)
    # print('after addConfirmedPCrelationship on arg0') #<<<<<<< nodeId = 1 width was updated here to (4, 19)
    # print(str(entSt))
    braSt = entSt.addConfirmedPCrelationship(18, 5, 1, bracketstorage=braSt)#funcStart, cNodeId, argId
    # print(str(entSt)) #<<<<<<<<< nodeId = 1 width was updated to (4, 26)
    # print('removing by __updateTemplatesToWiderEnclosingBracketsAndRemove for nodeId 1')
    braSt = entSt._EntityStorage__updateTemplatesToWiderEnclosingBracketsAndRemove([1], braSt) #here widthStart: 5 and widthEnd:26 ????

    braSt = entSt.addConfirmedPCrelationship(31, 1, 0, bracketstorage=braSt)
    braSt = entSt.addConfirmedPCrelationship(31, 8, 1, bracketstorage=braSt)

    """
nodeId ~ widthStart ~ widthEnd
0 ~ 9 ~ 15
1 ~ 0 ~ 30
2 ~ 0 ~ 33
3 ~ 13 ~ 15
4 ~ 3 ~ 17
5 ~ 19 ~ 27
6 ~ 10 ~ 11
7 ~ 25 ~ 26
8 ~ 32 ~ 33
    """

    expected_list_tuple_widthStart_nodeId = [(3, 4), (10, 6), (9, 0), (13, 3), (0, 1), (19, 5), (25, 7), (0, 2), (32, 8)]
    expected_list_tuple_widthEnd_nodeId = [(11, 6), (17, 4), (15, 0), (15, 3), (30, 1), (26, 7), (27, 5), (33, 2), (33, 8)]
    expected_nodeId__widthStart = {0: 9, 1: 0, 2: 0, 3: 13, 4: 3, 5: 19, 6: 10, 7: 25, 8: 32}
    expected_nodeId__widthEnd = {0: 15, 1: 30, 2: 33, 3: 15, 4: 17, 5: 27, 6: 11, 7: 26, 8: 33}
    expected_entityType__list_nodeId = {
        EntityType.PURE_NUMBER: [8],
        EntityType.BACKSLASH_NUMBER: [3],
        EntityType.BACKSLASH_FUNCTION: [4, 5],
        EntityType.PURE_INFIX: [0, 1, 2],
        EntityType.PURE_VARIABLE: [6, 7]}
    expected_funcStart__nodeId = {4: 4, 10: 6, 11: 0, 13: 3, 18: 1, 20: 5, 25: 7, 31: 2, 32: 8}
    expected_funcName__list_nodeId = {'+': [0, 1], '0': [8], '=': [2], 'pi': [3], 'sin': [4, 5], 'x': [6, 7]}
    expected_nodeId__entityType = {
        0: EntityType.PURE_INFIX,
        1: EntityType.PURE_INFIX,
        2: EntityType.PURE_INFIX,
        3: EntityType.BACKSLASH_NUMBER,
        4: EntityType.BACKSLASH_FUNCTION,
        5: EntityType.BACKSLASH_FUNCTION,
        6: EntityType.PURE_VARIABLE,
        7: EntityType.PURE_VARIABLE,
        8: EntityType.PURE_NUMBER}
    expected_nodeId__funcName = {0: '+', 1: '+', 2: '=', 3: 'pi', 4: 'sin', 5: 'sin', 6: 'x', 7: 'x', 8: '0'}
    expected_nodeId__funcStart = {0: 11, 1: 18, 2: 31, 3: 13, 4: 4, 5: 20, 6: 10, 7: 25, 8: 32}
    expected_nodeId__funcEnd = {0: 12, 1: 19, 2: 32, 3: 15, 4: 8, 5: 24, 6: 11, 7: 26, 8: 33}
    expected_tuple_nodeId_argIdx__pNodeId = {(1, 0): 2, (3, 1): 0, (4, 0): 1, (5, 1): 1, (6, 0): 0, (8, 1): 2}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {(4, 1): ('(', 8, ')', 16), (5, 1): ('(', 24, ')', 26)}
    expected_closeBraType__sortedPosList = {}
    expected_openBraType__sortedPosList = {}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {}
    expected_list_tuple_width_id_openPos_closePos = []
    expected_openBraPos__bracketId = {}
    expected_closeBraPos__bracketId = {}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId \
        and expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId \
        and expected_nodeId__widthStart == entSt.nodeId__widthStart \
        and expected_nodeId__widthEnd == entSt.nodeId__widthEnd \
        and expected_entityType__list_nodeId == entSt.entityType__list_nodeId \
        and expected_funcStart__nodeId == entSt.funcStart__nodeId \
        and expected_funcName__list_nodeId == entSt.funcName__list_nodeId \
        and expected_nodeId__entityType == entSt.nodeId__entityType \
        and expected_nodeId__funcName == entSt.nodeId__funcName \
        and expected_nodeId__funcStart == entSt.nodeId__funcStart \
        and expected_nodeId__funcEnd == entSt.nodeId__funcEnd \
        and expected_tuple_nodeId_argIdx__pNodeId == entSt.tuple_nodeId_argIdx__pNodeId \
        and expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == entSt.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos \
        and expected_closeBraType__sortedPosList == braSt.closeBraType__sortedPosList \
        and expected_openBraType__sortedPosList == braSt.openBraType__sortedPosList \
        and expected_id__tuple_openPos_openBraType_closePos_closeBraType == braSt.id__tuple_openPos_openBraType_closePos_closeBraType \
        and expected_list_tuple_width_id_openPos_closePos == braSt.list_tuple_width_id_openPos_closePos \
        and expected_openBraPos__bracketId == braSt.openBraPos__bracketId \
        and expected_closeBraPos__bracketId == braSt.closeBraPos__bracketId
    )

    if verbose:
        print(str(entSt))
        print(str(braSt))




def test__entityStorage__getAllContainingByWidth0(verbose=False):

    """
\\sin(x+\\pi)=-\\sin(x)
^ ^  ^^^^ ^ ^^^^ ^  ^^^
0 1  4567 8 1111 1  111
            0123 4  789

entSt.insert ORDER:
+     6
=     11
-     12
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<braSt.insertBracket
pi  8
sin 1 <addUnconfirm
sin 14 <addUnconfirm
x     5
x     18
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<_find_infixes_arg_brackets_width [add children to backslashes]

braSt.insertBracket ORDER:
(4, 10)
(17, 19)
    """
    braSt = BracketStorage() 
    entSt = EntityStorage(eqStrLen=len('\\sin(x+\\pi)=-\\sin(x)'))
    entSt.insert('+', 6, 7, EntityType.PURE_INFIX, 
        widthStart=6, widthEnd=7)
    entSt.insert('=', 11, 12, EntityType.PURE_INFIX, 
        widthStart=11, widthEnd=12)
    entSt.insert('-', 12, 13, EntityType.PURE_INFIX, 
        widthStart=12, widthEnd=13)
    #<<<<<<<<<<<
    braSt.insertBracket(BracketType.ROUND.value[0], 4, BracketType.ROUND.value[1], 10)
    braSt.insertBracket(BracketType.ROUND.value[0], 17, BracketType.ROUND.value[1], 19)
    #<<<<<<<<<<<
    entSt.insert('pi', 8, 10, EntityType.BACKSLASH_NUMBER, 
        widthStart=8, widthEnd=10)#\\pi
    entSt.insert('sin', 1, 4, EntityType.BACKSLASH_FUNCTION, 
        widthStart=1, widthEnd=4)

    entSt.addUnConfirmedPCrelationship(1, 1, BracketType.ROUND.value[0], 4, BracketType.ROUND.value[1], 10)

    entSt.insert('sin', 14, 17, EntityType.BACKSLASH_FUNCTION, 
        widthStart=14, widthEnd=17)

    entSt.addUnConfirmedPCrelationship(14, 1, BracketType.ROUND.value[0], 17, BracketType.ROUND.value[1], 19)

    entSt.insert('x', 5, 6, EntityType.PURE_VARIABLE, 
        widthStart=5, widthEnd=6)
    entSt.insert('x', 18, 19, EntityType.PURE_VARIABLE, 
        widthStart=18, widthEnd=19)

    list_nodeId = entSt.getAllContainingByWidth(4, 10)
    expected_list_nodeId = [0, 3, 6]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_list_nodeId == list_nodeId
    )
    if verbose:
        print('list_nodeId', list_nodeId)
        print(str(entSt))


def test__entityStorage__updateIfExists(verbose=False):
    """mostly used for pure_infix_- to implicit_infix_-

\\sin(x+\\pi)=-\\sin(x)
^ ^  ^^^^ ^ ^^^^ ^  ^^^
0 1  4567 8 1111 1  111
            0123 4  789

entSt.insert ORDER:
+     6
=     11
-     12
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<braSt.insertBracket
pi  8
sin 1 <addUnconfirm
sin 14 <addUnconfirm
x     5
x     18
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<_find_infixes_arg_brackets_width [add children to backslashes]

braSt.insertBracket ORDER:
(4, 10)
(17, 19)
    """
    braSt = BracketStorage() 
    entSt = EntityStorage(eqStrLen=len('\\sin(x+\\pi)=-\\sin(x)'))
    entSt.insert('+', 6, 7, EntityType.PURE_INFIX, 
        widthStart=6, widthEnd=7)
    entSt.insert('=', 11, 12, EntityType.PURE_INFIX, 
        widthStart=11, widthEnd=12)
    entSt.insert('-', 12, 13, EntityType.PURE_INFIX, 
        widthStart=12, widthEnd=13)
    entSt.updateIfExists(12, entityType=EntityType.IMPLICIT_INFIX)

    nodeId2_entityType = entSt.nodeId__entityType[2]
    expected_nodeId2_entityType = EntityType.IMPLICIT_INFIX

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_nodeId2_entityType == nodeId2_entityType
    )
    if verbose:
        print(str(entSt))


def test__entityStorage__remove0(verbose=False):
    entSt = EntityStorage(eqStrLen=len('\\sin(x+\\pi)=-\\sin(x)'))
    funcStart = 6
    entSt.insert('+', funcStart, 7, EntityType.PURE_INFIX, 
        widthStart=funcStart, widthEnd=7)
    entSt.remove(funcStart)



    expected_list_tuple_widthStart_nodeId = []
    expected_list_tuple_widthEnd_nodeId = []
    expected_nodeId__widthStart = {}
    expected_nodeId__widthEnd = {}
    expected_entityType__list_nodeId = {}
    expected_funcStart__nodeId = {}
    expected_funcName__list_nodeId = {}
    expected_nodeId__entityType = {}
    expected_nodeId__funcName = {}
    expected_nodeId__funcStart = {}
    expected_nodeId__funcEnd = {}
    expected_tuple_nodeId_argIdx__pNodeId = {}
    expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {}
    expected_closeBraType__sortedPosList = {}
    expected_openBraType__sortedPosList = {}
    expected_id__tuple_openPos_openBraType_closePos_closeBraType = {}
    expected_list_tuple_width_id_openPos_closePos = {}
    expected_openBraPos__bracketId = {}
    expected_closeBraPos__bracketId = {}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_widthStart_nodeId == entSt.list_tuple_widthStart_nodeId \
        and expected_list_tuple_widthEnd_nodeId == entSt.list_tuple_widthEnd_nodeId \
        and expected_nodeId__widthStart == entSt.nodeId__widthStart \
        and expected_nodeId__widthEnd == entSt.nodeId__widthEnd \
        and expected_entityType__list_nodeId == entSt.entityType__list_nodeId \
        and expected_funcStart__nodeId == entSt.funcStart__nodeId \
        and expected_funcName__list_nodeId == entSt.funcName__list_nodeId \
        and expected_nodeId__entityType == entSt.nodeId__entityType \
        and expected_nodeId__funcName == entSt.nodeId__funcName \
        and expected_nodeId__funcStart == entSt.nodeId__funcStart \
        and expected_nodeId__funcEnd == entSt.nodeId__funcEnd \
        and expected_tuple_nodeId_argIdx__pNodeId == entSt.tuple_nodeId_argIdx__pNodeId \
        and expected_tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos == entSt.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos \

    )

    if verbose:
        print(str(entSt))


if __name__=='__main__':
    test__entityStorage__insert0()
    test__entityStorage__getNodeIdFunNameByFuncStart0()
    test__entityStorage__addConfirmedPCrelationshipById0()
    test__entityStorage__existEntityAt0()
    test__entityStorage__widthMaxUpdate0()
    test__entityStorage__getAllNodeIdFuncNameWidthStartWidthEnd0()
    test__entityStorage__addConfirmedPCrelationship0()
    test__entityStorage__addUnConfirmedPCrelationship0()
    test__entityStorage__getAllUnConfirmedPCrelationship0()
    test__entityStorage__getWidestFit0()
    test__entityStorage____updateTemplatesToWiderEnclosingBracketsAndRemove0()
    test__entityStorage__getAllContainingByWidth0()
    test__entityStorage__updateIfExists()
    test__entityStorage__remove0()
