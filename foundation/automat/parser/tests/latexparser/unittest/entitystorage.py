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
    list_tuple_funcStart_funcEnd_nodeId = entSt.getAllEndPosOfEntityType(EntityType.PURE_INFIX)

    expected_list_tuple_funcStart_funcEnd_nodeId = [(1, 2, 0), (3, 4, 1), (5, 6, 2)]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected_list_tuple_funcStart_funcEnd_nodeId == list_tuple_funcStart_funcEnd_nodeId
    )
    if verbose:
        print('list_tuple_funcStart_funcEnd_nodeId', list_tuple_funcStart_funcEnd_nodeId)
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
    list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart = entSt.getAllNodeIdFuncNameWidthStartWidthEnd()
    expected_list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart = [
    (0, '+', 1, 2, 1),
    (1, '+', 3, 4, 3),
    (2, '=', 5, 6, 5)
    ]

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart == expected_list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart
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
    entSt = EntityStorage()
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

    expected_list_tuple_widthStart_nodeId = [(4, 3), (0, 0), (6, 4), (0, 1), (10, 5), (0, 2), (14, 6)]
    expected_list_tuple_widthEnd_nodeId = [(5, 3), (12, 0), (7, 4), (11, 1), (11, 5), (15, 2), (15, 6)]
    expected_nodeId__widthStart = {0: 0, 1: 0, 2: 0, 3: 4, 4: 6, 5: 10, 6: 14} # <<<<<<<<<<<<<<<<<<nodeId 0, 1 are not correct
    expected_nodeId__widthEnd = {0: 12, 1: 11, 2: 15, 3: 5, 4: 7, 5: 11, 6: 15}
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


def test__entityStorage__addUnConfirmedPCrelationship0(verbose=False):
    entSt = EntityStorage()
    entSt.insert(funcName, funcStart, funcEnd, entityType, parentNodeId=None, argIdx=None, widthStart=None, widthEnd=None)
    entSt.addUnConfirmedPCrelationship(funcName, argId, openBraType, openBraPos, closeBraType, closeBraPos)
    expected = None

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
    )
    if verbose:
        print(str(entSt))


def test__entityStorage__getAllUnConfirmedPCrelationship0(verbose=False):
    entSt = EntityStorage()
    nodeId = entSt.insert(funcName, funcStart, funcEnd, entityType, parentNodeId=None, argIdx=None, widthStart=None, widthEnd=None)
    entSt.getAllUnConfirmedPCrelationship(nodeId)
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


if __name__=='__main__':
    # test__entityStorage__insert0(True)
    # test__entityStorage__getNodeIdFunNameByFuncStart0(True)
    # test__entityStorage__addConfirmedPCrelationshipById0(True)
    # test__entityStorage__existEntityAt0(True)
    # test__entityStorage__widthMaxUpdate0(True)
    # test__entityStorage__getAllEndPosOfEntityType0(True)
    # test__entityStorage__getAllNodeIdFuncNameWidthStartWidthEnd0(True)
    # test__entityStorage__addConfirmedPCrelationship0(True)
    # test__entityStorage__addUnConfirmedPCrelationship0(True)
    # test__entityStorage__getAllUnConfirmedPCrelationship0(True)
    # test__entityStorage__getWidestFit0(True)
    # test__entityStorage____updateTemplatesToWiderEnclosingBracketsAndRemove0(True)
    # test__entityStorage__getAllContainingByWidth0(True)
    # test__entityStorage__remove0(True)
