import pprint
import inspect

from foundation.automat.common.stringcompare import StringCompare

pp = pprint.PrettyPrinter(indent=4)

def test__damerauLevenshtein__schemegrammarparser_distributivity(verbose=False):

    a = '(+ (* $ $) (* $ $))'#'(+ (* $0 $1) (* $0 $2))'
    b = '(* $ (+ $ $))'#'(* $0 (+ $1 $2))'
    r = StringCompare.damerauLevenshtein(a, b)
    expected_r = 7
    if verbose:
        print('distance:')
        print(r)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        r == expected_r
        )

def test__damerauLevenshteinMimick__schemegrammarparser_distributivity(verbose=False):

    a = '(+ (* $ $) (* $ $))'#'(+ (* $0 $1) (* $0 $2))'
    b = '(* $ (+ $ $))'#'(* $0 (+ $1 $2))'
    r = StringCompare.damerauLevenschsteinMimick(a, b)
    expected_r = 7
    if verbose:
        print('distance:')
        print(r)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        r == expected_r
        )


def test__damerauLevenshteinMimickWithEntities__schemegrammarparser_distributivity(verbose=False):
    #TODO copy from "new 10" of Notepad++
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
    s0Entities = [] # we need positions of f and its non functional arguments
    for startPos, nodeId in startPos__nodeId_i.items():#this includes the whole length
        l = len(nodeId__label_i[nodeId])
        s0Entities.append((startPos, startPos+l))
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
    s1Entities = []
    for startPos, nodeId in startPos__nodeId_o.items():
        l = len(nodeId__label_o[nodeId])
        s1Entities.append((startPos, startPos+l))
    r = StringCompare.damerauLevenschsteinMimickWithEntities(iPattern, oPattern, s0Entities, s1Entities)
    expected_r = 7
    if verbose:
        print('distance:')
        print(r)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        r == expected_r
        )



if __name__=='__main__':
    # test__damerauLevenshtein__schemegrammarparser_distributivity(True)
    # test__damerauLevenshteinMimick__schemegrammarparser_distributivity(True)
    test__damerauLevenshteinMimickWithEntities__schemegrammarparser_distributivity(True)
    #for schemeCompliance copy all the test cases from 
    #from foundation.automat.common.tests.longestcommonsubsequencetest<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #from foundation.automat.common.tests.schemegrammarparsertest<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #use this to group the similar formulas together and then apply them in succession for bipartiteGraph