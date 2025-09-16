import pprint
import inspect

from foundation.automat.common.longestcommonsubsequence import LongestCommonSubsequence

pp = pprint.PrettyPrinter(indent=4)


def test__schemeGrammarUpgrade__communtativity1vor(verbose=False):
    """
    """
    iPattern = '(+ $0 $1)'
    oPattern = '(+ $1 $0)'
    iMatchedFrags, oMatchedFrags = LongestCommonSubsequence.lcss(iPattern, oPattern)
    iExpected = [   
        {'e': 4, 's': 0, 'w': '(+ $'},
        {'e': 7, 's': 5, 'w': ' $'},
        {'e': 9, 's': 8, 'w': ')'}
    ]
    oExpected = [   
        {'e': 4, 's': 0, 'w': '(+ $'},
        {'e': 7, 's': 5, 'w': ' $'},
        {'e': 9, 's': 8, 'w': ')'}
    ]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


def test__schemeGrammarUpgrade__pythagoreanangle1vor(verbose=False):
    """
    """
    iPattern = '(+ (^ (sin $0) 2) (^ (cos $0) 2))'
    oPattern = '1'
    iMatchedFrags, oMatchedFrags = LongestCommonSubsequence.lcss(iPattern, oPattern)
    iExpected = []
    oExpected = []
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


def test__schemeGrammarUpgrade__subtractzero1vor(verbose=False):
    """
    """
    iPattern = '(- 0 $0)'
    oPattern = '$0'
    iMatchedFrags, oMatchedFrags = LongestCommonSubsequence.lcss(iPattern, oPattern)
    iExpected = [{'e': 7, 's': 5, 'w': '$0'}]
    oExpected = [{'e': 2, 's': 0, 'w': '$0'}]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


def test__schemeGrammarUpgrade__doubleinverse1vor(verbose=False):
    """
    """
    iPattern = '(/ (/ $2 $0) $1)'
    oPattern = '(/ $2 (* $0 $1))'
    iMatchedFrags, oMatchedFrags = LongestCommonSubsequence.lcss(iPattern, oPattern)
    iExpected = [{'e': 11, 's': 3, 'w': '(/ $2 $0'}, {'e': 16, 's': 12, 'w': ' $1)'}]
    oExpected = [   
        {'e': 5, 's': 0, 'w': '(/ $2'},
        {'e': 14, 's': 8, 'w': ' $0 $1'},
        {'e': 16, 's': 15, 'w': ')'}
    ]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)



def test__manipulateTest__subtractZero(verbose=False):
    """
    """
    iPattern = '(- (* I_{R_{C}} R_{C}) V^{Q1}_{BE})'
    oPattern = '(- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0)'
    iMatchedFrags, oMatchedFrags, iUnmatchedFrags, oUnmatchedFrags = LongestCommonSubsequence.lcssWithUnmatched(iPattern, oPattern)
    iExpected = [{'e': 35, 's': 0, 'w': '(- (* I_{R_{C}} R_{C}) V^{Q1}_{BE})'}]
    oExpected = [   {'e': 37, 's': 3, 'w': '(- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}'},
    {'e': 41, 's': 40, 'w': ')'}]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
        print('iUnmatchedFrags')
        pp.pprint(iUnmatchedFrags)
        print('oUnmatchedFrags')
        pp.pprint(oUnmatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)



def test__schemegrammar__substractzeroAtback(verbose=False):
    """
    """
    iPattern = '(- $ 0)'
    oPattern = '$'
    iMatchedFrags, oMatchedFrags, iUnmatchedFrags, oUnmatchedFrags = LongestCommonSubsequence.lcssWithUnmatched(iPattern, oPattern)
    iExpected = [{'e': 4, 's': 3, 'w': '$'}]
    oExpected = [{'e': 1, 's': 0, 'w': '$'}]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
        print('iUnmatchedFrags')
        pp.pprint(iUnmatchedFrags)
        print('oUnmatchedFrags')
        pp.pprint(oUnmatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


def test__schemeGrammarUpgrade__doubleinverse1vorNoArgNumMoreThan1Dollar(verbose=False):
    """
    """
    iPattern = '(/ (/ $ $) $)'
    oPattern = '(/ $ (* $ $))'
    iMatchedFrags, oMatchedFrags, iUnmatchedFrags, oUnmatchedFrags = LongestCommonSubsequence.lcssWithUnmatched(iPattern, oPattern)
    iExpected = [   
    {'e': 4, 's': 0, 'w': '(/ ('},
    {'e': 10, 's': 5, 'w': ' $ $)'},
    {'e': 13, 's': 12, 'w': ')'}]
    oExpected = [   
    {'e': 2, 's': 0, 'w': '(/'},
    {'e': 6, 's': 4, 'w': ' ('},
    {'e': 13, 's': 7, 'w': ' $ $))'}]
    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
        print('iUnmatchedFrags')
        pp.pprint(iUnmatchedFrags)
        print('oUnmatchedFrags')
        pp.pprint(oUnmatchedFrags)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', iMatchedFrags == iExpected and oExpected == oExpected)


def test__lcssEntities__nrootVsqrt(verbose=False):
    """"""
    from foundation.automat.parser.sorte.schemeparser import Schemeparser
    iPattern = '(nroot $4 $1)'
    iParser = Schemeparser(equationStr=iPattern)
    ast_i, functionsD_i, variablesD_i, primitives_i, totalNodeCount_i, startPos__nodeId_i = iParser._parse()
    #find the nodeId to label {node[1]:node[0]}
    stack = [iParser.rootOfTree]; nodeId__label_i = {}
    while len(stack) > 0:
        current = stack.pop()
        nodeId__label_i[current[1]] = current[0]
        children = ast_i.get(current, [])
        stack += children
    s1Entities = [] # we need positions of f and its non functional arguments
    for startPos, nodeId in startPos__nodeId_i.items():#this includes the whole length
        l = len(nodeId__label_i[nodeId])
        s1Entities.append((startPos, startPos+l))
    oPattern = '(sqrt $4 $1)'
    oParser = Schemeparser(equationStr=oPattern)
    ast_o, functionsD_o, variablesD_o, primitives_o, totalNodeCount_o, startPos__nodeId_o = oParser._parse()
    #find the nodeId to label {node[1]:node[0]}
    stack = [oParser.rootOfTree]; nodeId__label_o = {}
    while len(stack) > 0:
        current = stack.pop()
        nodeId__label_o[current[1]] = current[0]
        children = ast_o.get(current, [])
        stack += children
    s2Entities = []
    for startPos, nodeId in startPos__nodeId_o.items():
        l = len(nodeId__label_o[nodeId])
        s2Entities.append((startPos, startPos+l))

    print('s1Entities', s1Entities); print('s2Entities', s2Entities); import pdb;pdb.set_trace()

    iMatchedFrags, oMatchedFrags, iUnmatchedFrags, oUnmatchedFrags, rejoinedIFrags, rejoinedOFrags = LongestCommonSubsequence.lcssWithEntitiesUnmatchedRejoined(iPattern, oPattern, s1Entities, s2Entities)

    iMatchedFrags_expected = [{'e': 1, 's': 0, 'w': '('}, {'e': 13, 's': 6, 'w': ' $4 $1)'}]
    oMatchedFrags_expected = [{'e': 1, 's': 0, 'w': '('}, {'e': 12, 's': 5, 'w': ' $4 $1)'}]
    iUnmatchedFrags_expected = [{'e': 6, 's': 1, 'w': 'nroot'}]
    oUnmatchedFrags_expected = [{'e': 5, 's': 1, 'w': 'sqrt'}]
    rejoinedIFrags_expected = [
    {'e': 1, 'matched': True, 's': 0, 'w': '('},
    {'e': 6, 'matched': False, 's': 1, 'w': 'nroot'},
    {'e': 13, 'matched': True, 's': 6, 'w': ' $4 $1)'}]
    rejoinedOFrags_expected = [
    {'e': 1, 'matched': True, 's': 0, 'w': '('},
    {'e': 5, 'matched': False, 's': 1, 'w': 'sqrt'},
    {'e': 12, 'matched': True, 's': 5, 'w': ' $4 $1)'}]

    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
        print('iUnmatchedFrags')
        pp.pprint(iUnmatchedFrags)
        print('oUnmatchedFrags')
        pp.pprint(oUnmatchedFrags)
        print('rejoinedIFrags')
        pp.pprint(rejoinedIFrags)
        print('rejoinedOFrags')
        pp.pprint(rejoinedOFrags)

    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        iMatchedFrags == iMatchedFrags_expected \
        and oMatchedFrags == oMatchedFrags_expected \
        and iUnmatchedFrags == iUnmatchedFrags_expected \
        and oUnmatchedFrags == oUnmatchedFrags_expected \
        and rejoinedIFrags == rejoinedIFrags_expected \
        and rejoinedOFrags == rejoinedOFrags_expected
    )



def test__lcssEntities__nrootAsReciprocalPower(verbose=False):
    """"""
    from foundation.automat.parser.sorte.schemeparser import Schemeparser
    iPattern = '(^ (nroot $ $) $)'
    iParser = Schemeparser(equationStr=iPattern)
    ast_i, functionsD_i, variablesD_i, primitives_i, totalNodeCount_i, startPos__nodeId_i = iParser._parse()
    #find the nodeId to label {node[1]:node[0]}
    stack = [iParser.rootOfTree]; nodeId__label_i = {}
    while len(stack) > 0:
        current = stack.pop()
        nodeId__label_i[current[1]] = current[0]
        children = ast_i.get(current, [])
        stack += children
    s1Entities = [] # we need positions of f and its non functional arguments
    for startPos, nodeId in startPos__nodeId_i.items():#this includes the whole length
        l = len(nodeId__label_i[nodeId])
        s1Entities.append((startPos, startPos+l))
    oPattern = '(^ $ (/ $ $))'
    oParser = Schemeparser(equationStr=oPattern)
    ast_o, functionsD_o, variablesD_o, primitives_o, totalNodeCount_o, startPos__nodeId_o = oParser._parse()
    #find the nodeId to label {node[1]:node[0]}
    stack = [oParser.rootOfTree]; nodeId__label_o = {}
    while len(stack) > 0:
        current = stack.pop()
        nodeId__label_o[current[1]] = current[0]
        children = ast_o.get(current, [])
        stack += children
    s2Entities = []
    for startPos, nodeId in startPos__nodeId_o.items():
        l = len(nodeId__label_o[nodeId])
        s2Entities.append((startPos, startPos+l))

    print('s1Entities', s1Entities); print('s2Entities', s2Entities); import pdb;pdb.set_trace()

    iMatchedFrags, oMatchedFrags, iUnmatchedFrags, oUnmatchedFrags, rejoinedIFrags, rejoinedOFrags = LongestCommonSubsequence.lcssWithEntitiesUnmatchedRejoined(iPattern, oPattern, s1Entities, s2Entities)

    iMatchedFrags_expected = [
    {'e': 4, 's': 0, 'w': '(^ ('},
    {'e': 14, 's': 9, 'w': ' $ $)'},
    {'e': 17, 's': 16, 'w': ')'}]
    oMatchedFrags_expected = [
    {'e': 2, 's': 0, 'w': '(^'},
    {'e': 6, 's': 4, 'w': ' ('},
    {'e': 13, 's': 7, 'w': ' $ $))'}]
    iUnmatchedFrags_expected = [{'e': 9, 's': 4, 'w': 'nroot'}, {'e': 16, 's': 14, 'w': ' $'}]
    oUnmatchedFrags_expected = [{'e': 4, 's': 2, 'w': ' $'}, {'e': 7, 's': 6, 'w': '/'}]
    rejoinedIFrags_expected = [
    {'e': 4, 'matched': True, 's': 0, 'w': '(^ ('},
    {'e': 9, 'matched': False, 's': 4, 'w': 'nroot'},
    {'e': 14, 'matched': True, 's': 9, 'w': ' $ $)'},
    {'e': 16, 'matched': False, 's': 14, 'w': ' $'},
    {'e': 17, 'matched': True, 's': 16, 'w': ')'}]
    rejoinedOFrags_expected = [
    {'e': 2, 'matched': True, 's': 0, 'w': '(^'},
    {'e': 4, 'matched': False, 's': 2, 'w': ' $'},
    {'e': 6, 'matched': True, 's': 4, 'w': ' ('},
    {'e': 7, 'matched': False, 's': 6, 'w': '/'},
    {'e': 13, 'matched': True, 's': 7, 'w': ' $ $))'}]

    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
        print('iUnmatchedFrags')
        pp.pprint(iUnmatchedFrags)
        print('oUnmatchedFrags')
        pp.pprint(oUnmatchedFrags)
        print('rejoinedIFrags')
        pp.pprint(rejoinedIFrags)
        print('rejoinedOFrags')
        pp.pprint(rejoinedOFrags)

    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        iMatchedFrags == iMatchedFrags_expected \
        and oMatchedFrags == oMatchedFrags_expected \
        and iUnmatchedFrags == iUnmatchedFrags_expected \
        and oUnmatchedFrags == oUnmatchedFrags_expected \
        and rejoinedIFrags == rejoinedIFrags_expected \
        and rejoinedOFrags == rejoinedOFrags_expected
    )





def test__lcssEntities__nrootAsReciprocalPower0(verbose=False):
    """"""
    from foundation.automat.parser.sorte.schemeparser import Schemeparser
    iPattern = '(^ (nroot $0 $1) $2)'
    iParser = Schemeparser(equationStr=iPattern)
    ast_i, functionsD_i, variablesD_i, primitives_i, totalNodeCount_i, startPos__nodeId_i = iParser._parse()
    #find the nodeId to label {node[1]:node[0]}
    stack = [iParser.rootOfTree]; nodeId__label_i = {}
    while len(stack) > 0:
        current = stack.pop()
        nodeId__label_i[current[1]] = current[0]
        children = ast_i.get(current, [])
        stack += children
    s1Entities = [] # we need positions of f and its non functional arguments
    for startPos, nodeId in startPos__nodeId_i.items():#this includes the whole length
        l = len(nodeId__label_i[nodeId])
        s1Entities.append((startPos, startPos+l))
    oPattern = '(^ $1 (/ $2 $0))'
    oParser = Schemeparser(equationStr=oPattern)
    ast_o, functionsD_o, variablesD_o, primitives_o, totalNodeCount_o, startPos__nodeId_o = oParser._parse()
    #find the nodeId to label {node[1]:node[0]}
    stack = [oParser.rootOfTree]; nodeId__label_o = {}
    while len(stack) > 0:
        current = stack.pop()
        nodeId__label_o[current[1]] = current[0]
        children = ast_o.get(current, [])
        stack += children
    s2Entities = []
    for startPos, nodeId in startPos__nodeId_o.items():
        l = len(nodeId__label_o[nodeId])
        s2Entities.append((startPos, startPos+l))

    # print('s1Entities', s1Entities); print('s2Entities', s2Entities); import pdb;pdb.set_trace()

    iMatchedFrags, oMatchedFrags, iUnmatchedFrags, oUnmatchedFrags, rejoinedIFrags, rejoinedOFrags = LongestCommonSubsequence.lcssWithEntitiesUnmatchedRejoined(iPattern, oPattern, s1Entities, s2Entities)

    iMatchedFrags_expected = [
    {'e': 4, 's': 0, 'w': '(^ ('},
    {'e': 14, 's': 9, 'w': ' $ $)'},
    {'e': 17, 's': 16, 'w': ')'}]
    oMatchedFrags_expected = [
    {'e': 2, 's': 0, 'w': '(^'},
    {'e': 6, 's': 4, 'w': ' ('},
    {'e': 13, 's': 7, 'w': ' $ $))'}]
    iUnmatchedFrags_expected = [{'e': 9, 's': 4, 'w': 'nroot'}, {'e': 16, 's': 14, 'w': ' $'}]
    oUnmatchedFrags_expected = [{'e': 4, 's': 2, 'w': ' $'}, {'e': 7, 's': 6, 'w': '/'}]
    rejoinedIFrags_expected = [
    {'e': 4, 'matched': True, 's': 0, 'w': '(^ ('},
    {'e': 9, 'matched': False, 's': 4, 'w': 'nroot'},
    {'e': 14, 'matched': True, 's': 9, 'w': ' $ $)'},
    {'e': 16, 'matched': False, 's': 14, 'w': ' $'},
    {'e': 17, 'matched': True, 's': 16, 'w': ')'}]
    rejoinedOFrags_expected = [
    {'e': 2, 'matched': True, 's': 0, 'w': '(^'},
    {'e': 4, 'matched': False, 's': 2, 'w': ' $'},
    {'e': 6, 'matched': True, 's': 4, 'w': ' ('},
    {'e': 7, 'matched': False, 's': 6, 'w': '/'},
    {'e': 13, 'matched': True, 's': 7, 'w': ' $ $))'}]

    if verbose:
        print('iMatchedFrags')
        pp.pprint(iMatchedFrags)
        print('oMatchedFrags')
        pp.pprint(oMatchedFrags)
        print('iUnmatchedFrags')
        pp.pprint(iUnmatchedFrags)
        print('oUnmatchedFrags')
        pp.pprint(oUnmatchedFrags)
        print('rejoinedIFrags')
        pp.pprint(rejoinedIFrags)
        print('rejoinedOFrags')
        pp.pprint(rejoinedOFrags)

    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        iMatchedFrags == iMatchedFrags_expected \
        and oMatchedFrags == oMatchedFrags_expected \
        and iUnmatchedFrags == iUnmatchedFrags_expected \
        and oUnmatchedFrags == oUnmatchedFrags_expected \
        and rejoinedIFrags == rejoinedIFrags_expected \
        and rejoinedOFrags == rejoinedOFrags_expected
    )



if __name__=='__main__':
    # test__schemeGrammarUpgrade__communtativity1vor()
    # test__schemeGrammarUpgrade__pythagoreanangle1vor()
    # test__schemeGrammarUpgrade__subtractzero1vor()
    # test__schemeGrammarUpgrade__doubleinverse1vor()
    # test__manipulateTest__subtractZero()
    # test__schemegrammar__substractzeroAtback()
    # test__schemeGrammarUpgrade__doubleinverse1vorNoArgNumMoreThan1Dollar()
    # test__lcssEntities__nrootVsqrt()
    # test__lcssEntities__nrootAsReciprocalPower()
    test__lcssEntities__nrootAsReciprocalPower0(True) # this test show that lcss is not meant for $0.... maybe try levenschstein? or we need some custom solution