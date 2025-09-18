import pprint
import inspect

from foundation.automat.common.schemegrammarparser import SchemeGrammarParser
from foundation.automat.parser.sorte.schemeparser import Schemeparser

pp = pprint.PrettyPrinter(indent=4)


def test__ideal__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(+ 1 2)'#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<anything in "" should be treated as argLen=0, else it is a variable with argLen=1, functions_that_take_at_least_1_arg and above should have argLen>1
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    nodeIdsToSkip = []
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(+ 2 1)'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '+', 'm': 0, 'on': 0, 'ow': '+', 's': 1, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 2, 'iw': '2', 'm': 0, 'on': 1, 'ow': '2', 's': 5, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 5, 'in': 1, 'iw': '1', 'm': 0, 'on': 2, 'ow': '1', 's': 3, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 3: 2, 5: 1}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('original startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__idealNested__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(+ (+ c d) e)'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    nodeIdsToSkip = []
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(+ e (+ d c))' 
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '+', 'm': 0, 'on': 0, 'ow': '+', 's': 1, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 2, 'iw': 'e', 'm': 0, 'on': 1, 'ow': 'e', 's': 11, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 6, 'in': 1, 'iw': '+', 'm': 0, 'on': 2, 'ow': '+', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 8, 'in': 4, 'iw': 'd', 'm': 0, 'on': 3, 'ow': 'd', 's': 8, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 10, 'in': 3, 'iw': 'c', 'm': 0, 'on': 4, 'ow': 'c', 's': 6, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 3: 2, 6: 1, 8: 4, 10: 3}

    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('iEnclosureTree:')
        print(sgparser.iEnclosureTree)
        print('id__data:')
        pp.pprint(sgparser.iId__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__simpleLeft__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= a (+ b c))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    nodeIdsToSkip = []
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= a (+ c b))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'a', 'm': 0, 'on': 1, 'ow': 'a', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 2, 'iw': '+', 'm': 0, 'on': 2, 'ow': '+', 's': 6, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 8, 'in': 4, 'iw': 'c', 'm': 0, 'on': 3, 'ow': 'c', 's': 10, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 10, 'in': 3, 'iw': 'b', 'm': 0, 'on': 4, 'ow': 'b', 's': 8, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 3: 1, 6: 2, 8: 4, 10: 3}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('id__data:')
        pp.pprint(sgparser.iId__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__simpleRight__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ b c) a)'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    nodeIdsToSkip = []
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (+ c b) a)'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 4, 'in': 1, 'iw': '+', 'm': 0, 'on': 1, 'ow': '+', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 4, 'iw': 'c', 'm': 0, 'on': 3, 'ow': 'c', 's': 8, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 8, 'in': 3, 'iw': 'b', 'm': 0, 'on': 4, 'ow': 'b', 's': 6, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 11, 'in': 2, 'iw': 'a', 'm': 1, 'on': 2, 'ow': 'a', 's': 11, 't': 'hin', 'v': None}]
    expected_startPos__nodeId = {1: 0, 4: 1, 6: 4, 8: 3, 11: 2}

    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__sameLevel__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ a b) (+ c d))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    nodeIdsToSkip = []
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (+ b a) (+ d c))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 4, 'in': 1, 'iw': '+', 'm': 0, 'on': 1, 'ow': '+', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 4, 'iw': 'b', 'm': 0, 'on': 3, 'ow': 'b', 's': 8, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 8, 'in': 3, 'iw': 'a', 'm': 0, 'on': 4, 'ow': 'a', 's': 6, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 12, 'in': 2, 'iw': '+', 'm': 1, 'on': 2, 'ow': '+', 's': 12, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 14, 'in': 6, 'iw': 'd', 'm': 1, 'on': 5, 'ow': 'd', 's': 16, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 16, 'in': 5, 'iw': 'c', 'm': 1, 'on': 6, 'ow': 'c', 's': 14, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 4: 1, 6: 4, 8: 3, 12: 2, 14: 6, 16: 5}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__nested__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= a (+ d (+ c b)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    nodeIdsToSkip = []
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= a (+ (+ b c) d))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'a', 'm': 0, 'on': 1, 'ow': 'a', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 2, 'iw': '+', 'm': 0, 'on': 2, 'ow': '+', 's': 6, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 9, 'in': 4, 'iw': '+', 'm': 0, 'on': 3, 'ow': '+', 's': 11, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 11, 'in': 6, 'iw': 'b', 'm': 0, 'on': 5, 'ow': 'b', 's': 15, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 13, 'in': 5, 'iw': 'c', 'm': 0, 'on': 6, 'ow': 'c', 's': 13, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 16, 'in': 3, 'iw': 'd', 'm': 0, 'on': 4, 'ow': 'd', 's': 8, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 3: 1, 6: 2, 9: 4, 11: 6, 13: 5, 16: 3}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__nestedSameLevel__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ a b) (+ (+ c d) e))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    nodeIdsToSkip = []
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (+ b a) (+ e (+ d c)))'
    expected_schemeNodeChangeLog = [   
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 4, 'in': 1, 'iw': '+', 'm': 0, 'on': 1, 'ow': '+', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 4, 'iw': 'b', 'm': 0, 'on': 3, 'ow': 'b', 's': 8, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 8, 'in': 3, 'iw': 'a', 'm': 0, 'on': 4, 'ow': 'a', 's': 6, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 12, 'in': 2, 'iw': '+', 'm': 1, 'on': 2, 'ow': '+', 's': 12, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 14, 'in': 6, 'iw': 'e', 'm': 1, 'on': 5, 'ow': 'e', 's': 22, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 17, 'in': 5, 'iw': '+', 'm': 0, 'on': 6, 'ow': '+', 's': 15, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 19, 'in': 8, 'iw': 'd', 'm': 0, 'on': 7, 'ow': 'd', 's': 19, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 21, 'in': 7, 'iw': 'c', 'm': 0, 'on': 8, 'ow': 'c', 's': 17, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 4: 1, 6: 4, 8: 3, 12: 2, 14: 6, 17: 5, 19: 8, 21: 7}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__2deep2wide__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ (+ a b) (+ c d)) (+ (+ e f) (+ g h)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    nodeIdsToSkip = []
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (+ (+ d c) (+ b a)) (+ (+ h g) (+ f e)))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 4, 'in': 1, 'iw': '+', 'm': 0, 'on': 1, 'ow': '+', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 7, 'in': 4, 'iw': '+', 'm': 0, 'on': 3, 'ow': '+', 's': 15, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 9, 'in': 10, 'iw': 'd', 'm': 0, 'on': 7, 'ow': 'd', 's': 19, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 11, 'in': 9, 'iw': 'c', 'm': 0, 'on': 8, 'ow': 'c', 's': 17, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 15, 'in': 3, 'iw': '+', 'm': 0, 'on': 4, 'ow': '+', 's': 7, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 17, 'in': 8, 'iw': 'b', 'm': 0, 'on': 9, 'ow': 'b', 's': 11, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 19, 'in': 7, 'iw': 'a', 'm': 0, 'on': 10, 'ow': 'a', 's': 9, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 24, 'in': 2, 'iw': '+', 'm': 1, 'on': 2, 'ow': '+', 's': 24, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 27, 'in': 6, 'iw': '+', 'm': 0, 'on': 5, 'ow': '+', 's': 35, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 29, 'in': 14, 'iw': 'h', 'm': 0, 'on': 11, 'ow': 'h', 's': 39, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 31, 'in': 13, 'iw': 'g', 'm': 0, 'on': 12, 'ow': 'g', 's': 37, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 35, 'in': 5, 'iw': '+', 'm': 0, 'on': 6, 'ow': '+', 's': 27, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 37, 'in': 12, 'iw': 'f', 'm': 0, 'on': 13, 'ow': 'f', 's': 31, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 39, 'in': 11, 'iw': 'e', 'm': 0, 'on': 14, 'ow': 'e', 's': 29, 't': 'var', 'v': '$0'}]

    expected_startPos__nodeId = {
    1: 0,
    4: 1,
    7: 4,
    9: 10,
    11: 9,
    15: 3,
    17: 8,
    19: 7,
    24: 2,
    27: 6,
    29: 14,
    31: 13,
    35: 5,
    37: 12,
    39: 11}

    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__2deep2wideSkip__addition(verbose=False):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<give another example for skipNode that also has static changes to test allSchemeChanges, also another example that skips the top node
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ (+ a b) (+ c d)) (+ (+ e f) (+ g h)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # print('ast: ', ast); import pdb;pdb.set_trace()
    """
    {
    ('=', 0): [('+', 1), ('+', 2)], 
    ('+', 1): [('+', 3), ('+', 4)], 
    ('+', 2): [('+', 5), ('+', 6)], 
    ('+', 3): [('a', 7), ('b', 8)], 
    ('+', 4): [('c', 9), ('d', 10)], 
    ('+', 5): [('e', 11), ('f', 12)], 
    ('+', 6): [('g', 13), ('h', 14)]
    }
    """
    nodeIdsToSkip = [3]# please note that this is in schemeNodes, so its more convienent for the user
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (+ (+ d c) (+ a b)) (+ (+ h g) (+ f e)))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 4, 'in': 1, 'iw': '+', 'm': 0, 'on': 1, 'ow': '+', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 7, 'in': 4, 'iw': '+', 'm': 0, 'on': 3, 'ow': '+', 's': 15, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 9, 'in': 10, 'iw': 'd', 'm': 0, 'on': 7, 'ow': 'd', 's': 19, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 11, 'in': 9, 'iw': 'c', 'm': 0, 'on': 8, 'ow': 'c', 's': 17, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 15, 'in': 3, 'iw': '+', 'm': 0, 'on': 4, 'ow': '+', 's': 7, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 17, 'in': 7, 'iw': 'a', 'm': 0, 'on': 9, 'ow': 'a', 's': 9, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 19, 'in': 8, 'iw': 'b', 'm': 0, 'on': 10, 'ow': 'b', 's': 11, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 24, 'in': 2, 'iw': '+', 'm': 1, 'on': 2, 'ow': '+', 's': 24, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 27, 'in': 6, 'iw': '+', 'm': 0, 'on': 5, 'ow': '+', 's': 35, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 29, 'in': 14, 'iw': 'h', 'm': 0, 'on': 11, 'ow': 'h', 's': 39, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 31, 'in': 13, 'iw': 'g', 'm': 0, 'on': 12, 'ow': 'g', 's': 37, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 35, 'in': 5, 'iw': '+', 'm': 0, 'on': 6, 'ow': '+', 's': 27, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 37, 'in': 12, 'iw': 'f', 'm': 0, 'on': 13, 'ow': 'f', 's': 31, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 39, 'in': 11, 'iw': 'e', 'm': 0, 'on': 14, 'ow': 'e', 's': 29, 't': 'var', 'v': '$0'}]

    expected_startPos__nodeId = {
    1: 0,
    4: 1,
    7: 4,
    9: 10,
    11: 9,
    15: 3,
    17: 7,
    19: 8,
    24: 2,
    27: 6,
    29: 14,
    31: 13,
    35: 5,
    37: 12,
    39: 11}

    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__2deep2wideSkipTopLevel__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ (+ a b) (+ c d)) (+ (+ e f) (+ g h)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # print('ast: ', ast); import pdb;pdb.set_trace()
    """
    {
    ('=', 0): [('+', 1), ('+', 2)], 
    ('+', 1): [('+', 3), ('+', 4)], 
    ('+', 2): [('+', 5), ('+', 6)], 
    ('+', 3): [('a', 7), ('b', 8)], 
    ('+', 4): [('c', 9), ('d', 10)], 
    ('+', 5): [('e', 11), ('f', 12)], 
    ('+', 6): [('g', 13), ('h', 14)]
    }
    """
    nodeIdsToSkip = [1]# please note that this is in schemeNodes, so its more convienent for the user
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (+ (+ b a) (+ d c)) (+ (+ h g) (+ f e)))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 4, 'in': 1, 'iw': '+', 'm': 0, 'on': 1, 'ow': '+', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 7, 'in': 3, 'iw': '+', 'm': 0, 'on': 3, 'ow': '+', 's': 7, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 9, 'in': 8, 'iw': 'b', 'm': 0, 'on': 7, 'ow': 'b', 's': 11, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 11, 'in': 7, 'iw': 'a', 'm': 0, 'on': 8, 'ow': 'a', 's': 9, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 15, 'in': 4, 'iw': '+', 'm': 0, 'on': 4, 'ow': '+', 's': 15, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 17, 'in': 10, 'iw': 'd', 'm': 0, 'on': 9, 'ow': 'd', 's': 19, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 19, 'in': 9, 'iw': 'c', 'm': 0, 'on': 10, 'ow': 'c', 's': 17, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 24, 'in': 2, 'iw': '+', 'm': 1, 'on': 2, 'ow': '+', 's': 24, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 27, 'in': 6, 'iw': '+', 'm': 0, 'on': 5, 'ow': '+', 's': 35, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 29, 'in': 14, 'iw': 'h', 'm': 0, 'on': 11, 'ow': 'h', 's': 39, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 31, 'in': 13, 'iw': 'g', 'm': 0, 'on': 12, 'ow': 'g', 's': 37, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 35, 'in': 5, 'iw': '+', 'm': 0, 'on': 6, 'ow': '+', 's': 27, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 37, 'in': 12, 'iw': 'f', 'm': 0, 'on': 13, 'ow': 'f', 's': 31, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 39, 'in': 11, 'iw': 'e', 'm': 0, 'on': 14, 'ow': 'e', 's': 29, 't': 'var', 'v': '$0'}]

    expected_startPos__nodeId = {   1: 0,
    4: 1,
    7: 3,
    9: 8,
    11: 7,
    15: 4,
    17: 10,
    19: 9,
    24: 2,
    27: 6,
    29: 14,
    31: 13,
    35: 5,
    37: 12,
    39: 11}

    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__notApplicable__addition(verbose=False): # if no match show return the same startPos__nodeId<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= a (/ 3 (- 1 (- (* c (/ 5 10)))) c))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = [12]
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= a (/ 3 (- 1 (- (* c (/ 5 10)))) c))'
    expected_schemeNodeChangeLog = []
    expected_startPos__nodeId = {
    1: 0,
    3: 1,
    6: 2,
    8: 3,
    11: 4,
    13: 6,
    16: 7,
    19: 8,
    21: 9,
    24: 10,
    26: 11,
    28: 12,
    35: 5}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__functionCountChanges__subtractZero(verbose=False):
    """
    This case requires the matchedFrag and unmatchedFrag.... 
    """
    inputPattern = '(- $0 0)'
    outputPattern = '$0' # try to nest this to see if it will work
    schemeword = '(= (* I_{R} R) (- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$0':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (* I_{R} R) (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 4, 'in': 1, 'iw': '*', 'm': 0, 'on': 1, 'ow': '*', 's': 4, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 3, 'iw': 'I_{R}', 'm': 0, 'on': 3, 'ow': 'I_{R}', 's': 6, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 12, 'in': 4, 'iw': 'R', 'm': 0, 'on': 4, 'ow': 'R', 's': 12, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 16, 'in': 5, 'iw': '-', 'm': 0, 'on': 2, 'ow': '-', 's': 19, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 19, 'in': 7, 'iw': '*', 'm': 0, 'on': 5, 'ow': '*', 's': 22, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 21, 'in': 9, 'iw': 'I_{R_{C}}', 'm': 0, 'on': 7, 'ow': 'I_{R_{C}}', 's': 24, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 31, 'in': 10, 'iw': 'R_{C}', 'm': 0, 'on': 8, 'ow': 'R_{C}', 's': 34, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 38, 'in': 8, 'iw': 'V^{Q1}_{BE}', 'm': 0, 'on': 6, 'ow': 'V^{Q1}_{BE}', 's': 41, 't': 'var', 'v': '$0'},
    {   'd': 'r', 'e': 17, 'in': 2, 'iw': '-', 'm': 0, 'on': None, 'ow': None, 's': 16, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 55, 'in': 6, 'iw': '0', 'm': 0, 'on': None, 'ow': None, 's': 54, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {1: 0, 4: 1, 6: 3, 12: 4, 16: 5, 19: 7, 21: 9, 31: 10, 38: 8}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('iId__data:')
        pp.pprint(sgparser.iId__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__functionCountChanges__distributivity(verbose=False):
    """
    In this example the LCSS does not match the + of schemeword with the + of the expected... NOT SURE how to proceed to make a better match<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    """
    inputPattern = '(+ (* $0 $1) (* $0 $2))'
    outputPattern = '(* $0 (+ $1 $2))'
    schemeword = '(= a (+ (* b12 c34) (* b12 d56)))'#'(= a (+ (* b c) (* b d)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$0':0, '$1':0, '$2':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= a (* b12 (+ c34 d56)))'#'(= a (* b (+ c d)))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'a', 'm': 0, 'on': 1, 'ow': 'a', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 3, 'iw': '*', 'm': 0, 'on': 2, 'ow': '*', 's': 9, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 8, 'in': 5, 'iw': 'b12', 'm': 0, 'on': 3, 'ow': 'b12', 's': 11, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 13, 'in': 2, 'iw': '+', 'm': 0, 'on': 4, 'ow': '+', 's': 6, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 15, 'in': 6, 'iw': 'c34', 'm': 0, 'on': 5, 'ow': 'c34', 's': 15, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 19, 'in': 8, 'iw': 'd56', 'm': 0, 'on': 6, 'ow': 'd56', 's': 27, 't': 'var', 'v': '$2'},
    {   'd': 'r', 'e': 22, 'in': 4, 'iw': '*', 'm': 0, 'on': None, 'ow': None, 's': 21, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 26, 'in': 7, 'iw': 'b12', 'm': 0, 'on': None, 'ow': None, 's': 23, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 3: 1, 6: 3, 8: 5, 13: 2, 15: 6, 19: 8}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__moreVariableOutputThanInput__exponential1IsAnythingToThe0(verbose=False):
    """"""
    inputPattern = '1'
    outputPattern = '(^ $0 0)'
    schemeword = '(= a (+ 1 (+ 1 1)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$0':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= a (+ (^ v_{0} 0) (+ (^ v_{1} 0) (^ v_{2} 0))))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'a', 'm': 0, 'on': 1, 'ow': 'a', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 2, 'iw': '+', 'm': 0, 'on': 2, 'ow': '+', 's': 6, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 10, 'in': None, 'iw': None, 'm': 0, 'on': 3, 'ow': '^', 's': 9, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 16, 'in': None, 'iw': None, 'm': 0, 'on': 5, 'ow': 'v_{0}', 's': 11, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 18, 'in': None, 'iw': None, 'm': 0, 'on': 6, 'ow': '0', 's': 17, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 21, 'in': 4, 'iw': '+', 'm': 1, 'on': 4, 'ow': '+', 's': 11, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 25, 'in': None, 'iw': None, 'm': 1, 'on': 7, 'ow': '^', 's': 24, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 31, 'in': None, 'iw': None, 'm': 1, 'on': 9, 'ow': 'v_{1}', 's': 26, 't': 'var', 'v': '$0'},
    {   'd': 'a',  'e': 33, 'in': None, 'iw': None, 'm': 1, 'on': 10, 'ow': '0', 's': 32, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 37, 'in': None, 'iw': None, 'm': 2, 'on': 8, 'ow': '^', 's': 36, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 43, 'in': None, 'iw': None, 'm': 2, 'on': 11, 'ow': 'v_{2}', 's': 38, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 45, 'in': None, 'iw': None, 'm': 2, 'on': 12, 'ow': '0', 's': 44, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 9, 'in': 3, 'iw': '1', 'm': 0, 'on': None, 'ow': None, 's': 8, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 14, 'in': 5, 'iw': '1', 'm': 1, 'on': None, 'ow': None, 's': 13, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 16, 'in': 6, 'iw': '1', 'm': 2, 'on': None, 'ow': None, 's': 15, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {   1: 0,
    3: 1,
    6: 2,
    9: 7,
    11: 8,
    17: 9,
    21: 4,
    24: 10,
    26: 11,
    32: 12,
    36: 13,
    38: 14,
    44: 15}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('enclosureTree: ')
        pp.pprint(sgparser.iEnclosureTree)
        print('id__data:')
        pp.pprint(sgparser.iId__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__exponential1IsAnythingToThe0__skipNode(verbose=False):
    """"""
    inputPattern = '1'
    outputPattern = '(^ $0 0)'
    schemeword = '(= a (+ 1 (+ 1 1)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # print('ast', ast); import pdb;pdb.set_trace()
    """
    {
    ('=', 0): [('a', 1), ('+', 2)], 
    ('+', 2): [('1', 3), ('+', 4)], 
    ('+', 4): [('1', 5), ('1', 6)]
    }
    """
    nodeIdsToSkip = [5, 6]
    variableMinArgs = {'$0':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= a (+ (^ v_{0} 0) (+ 1 1)))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'a', 'm': 0, 'on': 1, 'ow': 'a', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 2, 'iw': '+', 'm': 0, 'on': 2, 'ow': '+', 's': 6, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 10, 'in': None, 'iw': None, 'm': 0, 'on': 3, 'ow': '^', 's': 9, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 16, 'in': None, 'iw': None, 'm': 0, 'on': 5, 'ow': 'v_{0}', 's': 11, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 18, 'in': None, 'iw': None, 'm': 0, 'on': 6, 'ow': '0', 's': 17, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 21, 'in': 4, 'iw': '+', 'm': 1, 'on': 4, 'ow': '+', 's': 11, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 23, 'in': 5, 'iw': '1', 'm': 1, 'on': 7, 'ow': '1', 's': 13, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 25, 'in': 6, 'iw': '1', 'm': 2, 'on': 8, 'ow': '1', 's': 15, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 9, 'in': 3, 'iw': '1', 'm': 0, 'on': None, 'ow': None, 's': 8, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {1: 0, 3: 1, 6: 2, 9: 7, 11: 8, 17: 9, 21: 4, 23: 5, 25: 6}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('enclosureTree: ')
        pp.pprint(sgparser.iEnclosureTree)
        print('id__data:')
        pp.pprint(sgparser.iId__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )





def test__manipulateLogarithm__logSameBaseAsArgumentGives1(verbose=False):
    """"""
    inputPattern = '1'
    outputPattern = '(log $0 $0)'
    schemeword = '(= a 1)'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$0':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= a (log v_{0} v_{0}))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'a', 'm': 0, 'on': 1, 'ow': 'a', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 9, 'in': None, 'iw': None, 'm': 0, 'on': 2, 'ow': 'log', 's': 6, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 15, 'in': None, 'iw': None, 'm': 0, 'on': 3, 'ow': 'v_{0}', 's': 10, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 21, 'in': None, 'iw': None, 'm': 0, 'on': 4, 'ow': 'v_{0}', 's': 16, 't': 'var', 'v': '$0'},
    {   'd': 'r', 'e': 6, 'in': 2, 'iw': '1', 'm': 0, 'on': None, 'ow': None, 's': 5, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {1: 0, 3: 1, 6: 3, 10: 4, 16: 5}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('id__data:')
        pp.pprint(sgparser.iId__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__manipulateExponential__exponential1IsAnythingToThe1(verbose=False):
    """"""
    inputPattern = '$0' # this kind can only replace arguments, function_replacement(unless this_function is a argument of another function) does not make sense
    outputPattern = '(^ $0 1)'
    schemeword = '(= a b)'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []#[0]
    variableMinArgs = {'$0':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (^ a 1) (^ b 1))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 5, 'in': None, 'iw': None, 'm': 0, 'on': 1, 'ow': '^', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 1, 'iw': 'a', 'm': 0, 'on': 3, 'ow': 'a', 's': 3, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 9, 'in': None, 'iw': None, 'm': 0, 'on': 4, 'ow': '1', 's': 8, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 13, 'in': None, 'iw': None, 'm': 1, 'on': 2, 'ow': '^', 's': 12, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 14, 'in': 2, 'iw': 'b', 'm': 1, 'on': 5, 'ow': 'b', 's': 5, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 17, 'in': None, 'iw': None, 'm': 1, 'on': 6, 'ow': '1', 's': 16, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {1: 0, 4: 3, 6: 1, 8: 4, 12: 5, 14: 2, 16: 6}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__exponential1IsAnythingToThe1__complicatedWithUserSkip(verbose=False):#swap the outputPattern and inputPattern in another test<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    """
    {
    ('=', 0): [('P', 1), ('*', 2)], 
    ('*', 2): [('^', 3), ('+', 4)], 
    ('^', 3): [('V_S', 5), ('2', 6)], 
    ('+', 4): [('/', 7), ('/', 8)], 
    ('/', 7): [('1', 9), ('+', 10)], 
    ('/', 8): [('1', 11), ('+', 12)], 
    ('+', 10): [('*', 13), ('R_6', 14)], 
    ('+', 12): [('R_{ON}', 15), ('R_7', 16)], 
    ('*', 13): [('2', 17), ('R_{ON}', 18)]
    }
    ('=', 0)
    """
    inputPattern = '$0' # this kind can only replace arguments, function_replacement(unless this_function is a argument of another function) does not make sense
    outputPattern = '(^ $0 1)'
    schemeword = '(= P (* (^ V_S 2) (+ (/ 1 (+ (* 2 R_{ON}) R_6)) (/ 1 (+ R_{ON} R_7)))))' # this is Example 6.8 page 320 <<Foundations>>
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    #
    # print(ast)
    # import pdb;pdb.set_trace()
    #
    nodeIdsToSkip = [0, 1, 2, 3, 4, 5, 6, 7, 8, 
    #9, 
    10, 
    #11, 
    12, 13, 14, 15, 16, 17, 18]#we only want all the 1s to become 1^1
    variableMinArgs = {'$0':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= P (* (^ V_S 2) (+ (/ (^ 1 1) (+ (* 2 R_{ON}) R_6)) (/ (^ 1 1) (+ R_{ON} R_7)))))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'P', 'm': 0, 'on': 1, 'ow': 'P', 's': 3, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 6, 'in': 2, 'iw': '*', 'm': 0, 'on': 2, 'ow': '*', 's': 6, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 9, 'in': 3, 'iw': '^', 'm': 0, 'on': 3, 'ow': '^', 's': 9, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 11, 'in': 5, 'iw': 'V_S', 'm': 0, 'on': 5, 'ow': 'V_S', 's': 11, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 15, 'in': 6, 'iw': '2', 'm': 1, 'on': 6, 'ow': '2', 's': 15, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 19, 'in': 4, 'iw': '+', 'm': 0, 'on': 4, 'ow': '+', 's': 19, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 22, 'in': 7, 'iw': '/', 'm': 0, 'on': 7, 'ow': '/', 's': 22, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 26, 'in': None, 'iw': None, 'm': 0, 'on': 9, 'ow': '^', 's': 25, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 27, 'in': 9, 'iw': '1', 'm': 0, 'on': 13, 'ow': '1', 's': 24, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 30, 'in': None, 'iw': None, 'm': 0, 'on': 14, 'ow': '1', 's': 29, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 33, 'in': 10, 'iw': '+', 'm': 0, 'on': 10, 'ow': '+', 's': 27, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 36, 'in': 13, 'iw': '*', 'm': 0, 'on': 15, 'ow': '*', 's': 30, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 38, 'in': 17, 'iw': '2', 'm': 0, 'on': 21, 'ow': '2', 's': 32, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 40, 'in': 18, 'iw': 'R_{ON}', 'm': 1, 'on': 22, 'ow': 'R_{ON}', 's': 34, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 48, 'in': 14, 'iw': 'R_6', 'm': 1, 'on': 16, 'ow': 'R_6', 's': 42, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 55, 'in': 8, 'iw': '/', 'm': 0, 'on': 8, 'ow': '/', 's': 49, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 59, 'in': None, 'iw': None, 'm': 0, 'on': 11, 'ow': '^', 's': 58, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 60, 'in': 11, 'iw': '1', 'm': 0, 'on': 17, 'ow': '1', 's': 51, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 63, 'in': None, 'iw': None, 'm': 0, 'on': 18, 'ow': '1', 's': 62, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 66, 'in': 12, 'iw': '+', 'm': 0, 'on': 12, 'ow': '+', 's': 54, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 68, 'in': 15, 'iw': 'R_{ON}', 'm': 0, 'on': 19, 'ow': 'R_{ON}', 's': 56, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 75, 'in': 16, 'iw': 'R_7', 'm': 1, 'on': 20, 'ow': 'R_7', 's': 63, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {
    1: 0,
    3: 1,
    6: 2,
    9: 3,
    11: 5,
    15: 6,
    19: 4,
    22: 7,
    25: 19,
    27: 9,
    29: 20,
    33: 10,
    36: 13,
    38: 17,
    40: 18,
    48: 14,
    55: 8,
    58: 21,
    60: 11,
    62: 22,
    66: 12,
    68: 15,
    75: 16}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )

def test__manipulateLogarithm__changeBaseFormula(verbose=False):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<0. more complicated changeBaseFormula, 1.0 more complicated changeBaseFormula with skipNodes
    """"""
    inputPattern = '(log $0 $1)'
    outputPattern = '(/ (log $2 $1) (log $2 $0))'
    schemeword = '(= a (log b c))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$0':0, '$1':0, '$2':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= a (/ (log v_{0} c) (log v_{0} b)))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'a', 'm': 0, 'on': 1, 'ow': 'a', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 7, 'in': None, 'iw': None, 'm': 0, 'on': 2, 'ow': '/', 's': 6, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 9, 'in': 2, 'iw': 'log', 'm': 0, 'on': 3, 'ow': 'log', 's': 6, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 18, 'in': None, 'iw': None, 'm': 0, 'on': 5, 'ow': 'v_{0}', 's': 13, 't': 'var', 'v': '$2'},
    {   'd': 'e', 'e': 19, 'in': 4, 'iw': 'c', 'm': 0, 'on': 6, 'ow': 'c', 's': 12, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 26, 'in': None, 'iw': None, 'm': 0, 'on': 4, 'ow': 'log', 's': 23, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 32, 'in': None, 'iw': None, 'm': 0, 'on': 7, 'ow': 'v_{0}', 's': 27, 't': 'var', 'v': '$2'},
    {   'd': 'e', 'e': 33, 'in': 3, 'iw': 'b', 'm': 0, 'on': 8, 'ow': 'b', 's': 10, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 3: 1, 6: 5, 9: 2, 13: 6, 19: 4, 23: 7, 27: 8, 33: 3}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__onlyVariable__multiplyDivideCancal(verbose=False):
    """
inputPattern
$0, means match all the arguments<<< this is essentially a plainOldSchemeParser catching all possible arguments?
$0 $1, means match all double arguments? so if we have
(+ 1 2 3 4), does it match
$0=1 $1=2
$0=2 $1=3
$0=3 $1=4 ? Then it is still a plainOldSchemeParser catching all possible arguments, and then making a slidingWindow equals to the number of arguments
if
$0 $1 ... $n, where n is an integer, its still a plainOldSchemeParser catching all possible arguments, and then making a slidingWindow...?
    """
    inputPattern = '$1'#this kind to be processed on a function seperate from findAll
    outputPattern = '(* (/ $1 $0) $0)'
    schemeword = '(= a a)'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (* (/ a v_{0}) v_{0}) (* (/ a v_{1}) v_{1}))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 5, 'in': None, 'iw': None, 'm': 0, 'on': 1, 'ow': '*', 's': 4, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 8, 'in': None, 'iw': None, 'm': 0, 'on': 3, 'ow': '/', 's': 7, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 9, 'in': 1, 'iw': 'a', 'm': 0, 'on': 7, 'ow': 'a', 's': 3, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 16, 'in': None, 'iw': None, 'm': 0, 'on': 8, 'ow': 'v_{0}', 's': 11, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 23, 'in': None, 'iw': None, 'm': 0, 'on': 4, 'ow': 'v_{0}', 's': 18, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 27, 'in': None, 'iw': None, 'm': 1, 'on': 2, 'ow': '*', 's': 26, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 30, 'in': None, 'iw': None, 'm': 1, 'on': 5, 'ow': '/', 's': 29, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 31, 'in': 2, 'iw': 'a', 'm': 1, 'on': 9, 'ow': 'a', 's': 5, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 38, 'in': None, 'iw': None, 'm': 1, 'on': 10, 'ow': 'v_{1}', 's': 33, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 45, 'in': None, 'iw': None, 'm': 1, 'on': 6, 'ow': 'v_{1}', 's': 40, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 4: 3, 7: 4, 9: 1, 11: 5, 18: 6, 26: 7, 29: 8, 31: 2, 33: 9, 40: 10}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__onlyVariable__multiplyDivideCancal6LevelsDeep(verbose=False):
    """
inputPattern
$0, means match all the arguments<<< this is essentially a plainOldSchemeParser catching all possible arguments?
$0 $1, means match all double arguments? so if we have
(+ 1 2 3 4), does it match
$0=1 $1=2
$0=2 $1=3
$0=3 $1=4 ? Then it is still a plainOldSchemeParser catching all possible arguments, and then making a slidingWindow equals to the number of arguments
if
$0 $1 ... $n, where n is an integer, its still a plainOldSchemeParser catching all possible arguments, and then making a slidingWindow...?
    """
    inputPattern = '$1'#this kind to be processed on a function seperate from findAll
    outputPattern = '(* (/ $1 $0) $0)'
    schemeword = '(= (+ (+ a (/ c (sin (* a w)))) (+ a (/ c (sin (* a w))))) (- 435 (* 4 97)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (* (/ (+ (* (/ (+ (* (/ a v_{6}) v_{6}) (* (/ (/ (* (/ c v_{12}) v_{12}) (* (/ (sin (* (/ (* (* (/ a v_{18}) v_{18}) (* (/ w v_{19}) v_{19})) v_{16}) v_{16})) v_{13}) v_{13})) v_{7}) v_{7})) v_{2}) v_{2}) (* (/ (+ (* (/ a v_{8}) v_{8}) (* (/ (/ (* (/ c v_{14}) v_{14}) (* (/ (sin (* (/ (* (* (/ a v_{20}) v_{20}) (* (/ w v_{21}) v_{21})) v_{17}) v_{17})) v_{15}) v_{15})) v_{9}) v_{9})) v_{3}) v_{3})) v_{0}) v_{0}) (* (/ (- (* (/ 435 v_{4}) v_{4}) (* (/ (* (* (/ 4 v_{10}) v_{10}) (* (/ 97 v_{11}) v_{11})) v_{5}) v_{5})) v_{1}) v_{1}))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 5, 'in': None, 'iw': None, 'm': 0, 'on': 1, 'ow': '*', 's': 4, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 8, 'in': None, 'iw': None, 'm': 0, 'on': 3, 'ow': '/', 's': 7, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 10, 'in': 1, 'iw': '+', 'm': 0, 'on': 7, 'ow': '+', 's': 4, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 14, 'in': None, 'iw': None, 'm': 0, 'on': 11, 'ow': '*', 's': 13, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 17, 'in': None, 'iw': None, 'm': 0, 'on': 15, 'ow': '/', 's': 16, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 19, 'in': 3, 'iw': '+', 'm': 0, 'on': 23, 'ow': '+', 's': 7, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 23, 'in': None, 'iw': None, 'm': 0, 'on': 31, 'ow': '*', 's': 22, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 26, 'in': None, 'iw': None, 'm': 0, 'on': 37, 'ow': '/', 's': 25, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 27, 'in': 7, 'iw': 'a', 'm': 0, 'on': 49, 'ow': 'a', 's': 9, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 34, 'in': None, 'iw': None, 'm': 0, 'on': 50, 'ow': 'v_{6}', 's': 29, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 41, 'in': None, 'iw': None, 'm': 0, 'on': 38, 'ow': 'v_{6}', 's': 36, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 45, 'in': None, 'iw': None, 'm': 1, 'on': 32, 'ow': '*', 's': 44, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 48, 'in': None, 'iw': None, 'm': 1, 'on': 39, 'ow': '/', 's': 47, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 50, 'in': 8, 'iw': '/', 'm': 0, 'on': 51, 'ow': '/', 's': 12, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 54, 'in': None, 'iw': None, 'm': 0, 'on': 61, 'ow': '*', 's': 53, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 57, 'in': None, 'iw': None, 'm': 0, 'on': 65, 'ow': '/', 's': 56, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 58, 'in': 13, 'iw': 'c', 'm': 0, 'on': 73, 'ow': 'c', 's': 14, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 66, 'in': None, 'iw': None, 'm': 0, 'on': 74, 'ow': 'v_{12}', 's': 60, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 74, 'in': None, 'iw': None, 'm': 0, 'on': 66, 'ow': 'v_{12}', 's': 68, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 78, 'in': None, 'iw': None, 'm': 1, 'on': 62, 'ow': '*', 's': 77, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 81, 'in': None, 'iw': None, 'm': 1, 'on': 67, 'ow': '/', 's': 80, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 83, 'in': 14, 'iw': 'sin', 'm': 0, 'on': 75, 'ow': 'sin', 's': 17, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 89, 'in': None, 'iw': None, 'm': 0, 'on': 81, 'ow': '*', 's': 88, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 92, 'in': None, 'iw': None, 'm': 0, 'on': 83, 'ow': '/', 's': 91, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 94, 'in': 17, 'iw': '*', 'm': 0, 'on': 87, 'ow': '*', 's': 22, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 98, 'in': None, 'iw': None, 'm': 0, 'on': 91, 'ow': '*', 's': 97, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 101, 'in': None, 'iw': None, 'm': 0, 'on': 95, 'ow': '/', 's': 100, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 102, 'in': 19, 'iw': 'a', 'm': 0, 'on': 103, 'ow': 'a', 's': 24, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 110, 'in': None, 'iw': None, 'm': 0, 'on': 104, 'ow': 'v_{18}', 's': 104, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 118, 'in': None, 'iw': None, 'm': 0, 'on': 96, 'ow': 'v_{18}', 's': 112, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 122, 'in': None, 'iw': None, 'm': 1, 'on': 92, 'ow': '*', 's': 121, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 125, 'in': None, 'iw': None, 'm': 1, 'on': 97, 'ow': '/', 's': 124, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 126, 'in': 20, 'iw': 'w', 'm': 1, 'on': 105, 'ow': 'w', 's': 26, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 134, 'in': None, 'iw': None, 'm': 1, 'on': 106, 'ow': 'v_{19}', 's': 128, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 142, 'in': None, 'iw': None, 'm': 1, 'on': 98, 'ow': 'v_{19}', 's': 136, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 151, 'in': None, 'iw': None, 'm': 0, 'on': 88, 'ow': 'v_{16}', 's': 145, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 159, 'in': None, 'iw': None, 'm': 0, 'on': 84, 'ow': 'v_{16}', 's': 153, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 168, 'in': None, 'iw': None, 'm': 1, 'on': 76, 'ow': 'v_{13}', 's': 162, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 176, 'in': None, 'iw': None, 'm': 1, 'on': 68, 'ow': 'v_{13}', 's': 170, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 184, 'in': None, 'iw': None, 'm': 1, 'on': 52, 'ow': 'v_{7}', 's': 179, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 191, 'in': None, 'iw': None, 'm': 1, 'on': 40, 'ow': 'v_{7}', 's': 186, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 199, 'in': None, 'iw': None, 'm': 0, 'on': 24, 'ow': 'v_{2}', 's': 194, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 206, 'in': None, 'iw': None, 'm': 0, 'on': 16, 'ow': 'v_{2}', 's': 201, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 210, 'in': None, 'iw': None, 'm': 1, 'on': 12, 'ow': '*', 's': 209, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 213, 'in': None, 'iw': None, 'm': 1, 'on': 17, 'ow': '/', 's': 212, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 215, 'in': 4, 'iw': '+', 'm': 0, 'on': 25, 'ow': '+', 's': 33, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 219, 'in': None, 'iw': None, 'm': 0, 'on': 33, 'ow': '*', 's': 218, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 222, 'in': None, 'iw': None, 'm': 0, 'on': 41, 'ow': '/', 's': 221, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 223, 'in': 9, 'iw': 'a', 'm': 0, 'on': 53, 'ow': 'a', 's': 35, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 230, 'in': None, 'iw': None, 'm': 0, 'on': 54, 'ow': 'v_{8}', 's': 225, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 237, 'in': None, 'iw': None, 'm': 0, 'on': 42, 'ow': 'v_{8}', 's': 232, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 241, 'in': None, 'iw': None, 'm': 1, 'on': 34, 'ow': '*', 's': 240, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 244, 'in': None, 'iw': None, 'm': 1, 'on': 43, 'ow': '/', 's': 243, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 246, 'in': 10, 'iw': '/', 'm': 0, 'on': 55, 'ow': '/', 's': 38, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 250, 'in': None, 'iw': None, 'm': 0, 'on': 63, 'ow': '*', 's': 249, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 253, 'in': None, 'iw': None, 'm': 0, 'on': 69, 'ow': '/', 's': 252, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 254, 'in': 15, 'iw': 'c', 'm': 0, 'on': 77, 'ow': 'c', 's': 40, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 262, 'in': None, 'iw': None, 'm': 0, 'on': 78, 'ow': 'v_{14}', 's': 256, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 270, 'in': None, 'iw': None, 'm': 0, 'on': 70, 'ow': 'v_{14}', 's': 264, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 274, 'in': None, 'iw': None, 'm': 1, 'on': 64, 'ow': '*', 's': 273, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 277, 'in': None, 'iw': None, 'm': 1, 'on': 71, 'ow': '/', 's': 276, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 279, 'in': 16, 'iw': 'sin', 'm': 0, 'on': 79, 'ow': 'sin', 's': 43, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 285, 'in': None, 'iw': None, 'm': 0, 'on': 82, 'ow': '*', 's': 284, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 288, 'in': None, 'iw': None, 'm': 0, 'on': 85, 'ow': '/', 's': 287, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 290, 'in': 18, 'iw': '*', 'm': 0, 'on': 89, 'ow': '*', 's': 48, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 294, 'in': None, 'iw': None, 'm': 0, 'on': 93, 'ow': '*', 's': 293, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 297, 'in': None, 'iw': None, 'm': 0, 'on': 99, 'ow': '/', 's': 296, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 298, 'in': 21, 'iw': 'a', 'm': 0, 'on': 107, 'ow': 'a', 's': 50, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 306, 'in': None, 'iw': None, 'm': 0, 'on': 108, 'ow': 'v_{20}', 's': 300, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 314, 'in': None, 'iw': None, 'm': 0, 'on': 100, 'ow': 'v_{20}', 's': 308, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 318, 'in': None, 'iw': None, 'm': 1, 'on': 94, 'ow': '*', 's': 317, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 321, 'in': None, 'iw': None, 'm': 1, 'on': 101, 'ow': '/', 's': 320, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 322, 'in': 22, 'iw': 'w', 'm': 1, 'on': 109, 'ow': 'w', 's': 52, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 330, 'in': None, 'iw': None, 'm': 1, 'on': 110, 'ow': 'v_{21}', 's': 324, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 338, 'in': None, 'iw': None, 'm': 1, 'on': 102, 'ow': 'v_{21}', 's': 332, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 347, 'in': None, 'iw': None, 'm': 0, 'on': 90, 'ow': 'v_{17}', 's': 341, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 355, 'in': None, 'iw': None, 'm': 0, 'on': 86, 'ow': 'v_{17}', 's': 349, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 364, 'in': None, 'iw': None, 'm': 1, 'on': 80, 'ow': 'v_{15}', 's': 358, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 372, 'in': None, 'iw': None, 'm': 1, 'on': 72, 'ow': 'v_{15}', 's': 366, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 380, 'in': None, 'iw': None, 'm': 1, 'on': 56, 'ow': 'v_{9}', 's': 375, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 387, 'in': None, 'iw': None, 'm': 1, 'on': 44, 'ow': 'v_{9}', 's': 382, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 395, 'in': None, 'iw': None, 'm': 1, 'on': 26, 'ow': 'v_{3}', 's': 390, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 402, 'in': None, 'iw': None, 'm': 1, 'on': 18, 'ow': 'v_{3}', 's': 397, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 410, 'in': None, 'iw': None, 'm': 0, 'on': 8, 'ow': 'v_{0}', 's': 405, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 417, 'in': None, 'iw': None, 'm': 0, 'on': 4, 'ow': 'v_{0}', 's': 412, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 421, 'in': None, 'iw': None, 'm': 1, 'on': 2, 'ow': '*', 's': 420, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 424, 'in': None, 'iw': None, 'm': 1, 'on': 5, 'ow': '/', 's': 423, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 426, 'in': 2, 'iw': '-', 'm': 0, 'on': 9, 'ow': '-', 's': 60, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 430, 'in': None, 'iw': None, 'm': 0, 'on': 13, 'ow': '*', 's': 429, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 433, 'in': None, 'iw': None, 'm': 0, 'on': 19, 'ow': '/', 's': 432, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 434, 'in': 5, 'iw': '435', 'm': 0, 'on': 27, 'ow': '435', 's': 62, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 443, 'in': None, 'iw': None, 'm': 0, 'on': 28, 'ow': 'v_{4}', 's': 438, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 450, 'in': None, 'iw': None, 'm': 0, 'on': 20, 'ow': 'v_{4}', 's': 445, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 454, 'in': None, 'iw': None, 'm': 1, 'on': 14, 'ow': '*', 's': 453, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 457, 'in': None, 'iw': None, 'm': 1, 'on': 21, 'ow': '/', 's': 456, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 459, 'in': 6, 'iw': '*', 'm': 0, 'on': 29, 'ow': '*', 's': 67, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 463, 'in': None, 'iw': None, 'm': 0, 'on': 35, 'ow': '*', 's': 462, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 466, 'in': None, 'iw': None, 'm': 0, 'on': 45, 'ow': '/', 's': 465, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 467, 'in': 11, 'iw': '4', 'm': 0, 'on': 57, 'ow': '4', 's': 69, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 475, 'in': None, 'iw': None, 'm': 0, 'on': 58, 'ow': 'v_{10}', 's': 469, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 483, 'in': None, 'iw': None, 'm': 0, 'on': 46, 'ow': 'v_{10}', 's': 477, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 487, 'in': None, 'iw': None, 'm': 1, 'on': 36, 'ow': '*', 's': 486, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 490, 'in': None, 'iw': None, 'm': 1, 'on': 47, 'ow': '/', 's': 489, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 491, 'in': 12, 'iw': '97', 'm': 1, 'on': 59, 'ow': '97', 's': 71, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 500, 'in': None, 'iw': None, 'm': 1, 'on': 60, 'ow': 'v_{11}', 's': 494, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 508, 'in': None, 'iw': None, 'm': 1, 'on': 48, 'ow': 'v_{11}', 's': 502, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 516, 'in': None, 'iw': None, 'm': 1, 'on': 30, 'ow': 'v_{5}', 's': 511, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 523, 'in': None, 'iw': None, 'm': 1, 'on': 22, 'ow': 'v_{5}', 's': 518, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 531, 'in': None, 'iw': None, 'm': 1, 'on': 10, 'ow': 'v_{1}', 's': 526, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 538, 'in': None, 'iw': None, 'm': 1, 'on': 6, 'ow': 'v_{1}', 's': 533, 't': 'var', 'v': '$0'}]
    expected_startPos__nodeId = {1: 0, 4: 23, 7: 24, 10: 1, 13: 25, 16: 26, 19: 3, 22: 27, 25: 28, 27: 7, 29: 29, 36: 30, 44: 31, 47: 32, 50: 8, 53: 33, 56: 34, 58: 13, 60: 35, 68: 36, 77: 37, 80: 38, 83: 14, 88: 39, 91: 40, 94: 17, 97: 41, 100: 42, 102: 19, 104: 43, 112: 44, 121: 45, 124: 46, 126: 20, 128: 47, 136: 48, 145: 49, 153: 50, 162: 51, 170: 52, 179: 53, 186: 54, 194: 55, 201: 56, 209: 57, 212: 58, 215: 4, 218: 59, 221: 60, 223: 9, 225: 61, 232: 62, 240: 63, 243: 64, 246: 10, 249: 65, 252: 66, 254: 15, 256: 67, 264: 68, 273: 69, 276: 70, 279: 16, 284: 71, 287: 72, 290: 18, 293: 73, 296: 74, 298: 21, 300: 75, 308: 76, 317: 77, 320: 78, 322: 22, 324: 79, 332: 80, 341: 81, 349: 82, 358: 83, 366: 84, 375: 85, 382: 86, 390: 87, 397: 88, 405: 89, 412: 90, 420: 91, 423: 92, 426: 2, 429: 93, 432: 94, 434: 5, 438: 95, 445: 96, 453: 97, 456: 98, 459: 6, 462: 99, 465: 100, 467: 11, 469: 101, 477: 102, 486: 103, 489: 104, 491: 12, 494: 105, 502: 106, 511: 107, 518: 108, 526: 109, 533: 110}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__latexParserUnparse__sqrtInSqrt(verbose=False):
    """"""
    inputPattern = '(nroot $4 $1)'# inputPattern = '(nroot $1 $3)'
    outputPattern = '(sqrt $4 $1)'# outputPattern = '(sqrt $1 $3)'
    schemeword = '(= (nroot (sqrt (/ pi 22)) (nroot (sin pi) pi)) F)'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$4':0, '$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (sqrt (sqrt (/ pi 22)) (sqrt (sin pi) pi)) F)'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 8, 'in': None, 'iw': None, 'm': 0, 'on': 1, 'ow': 'sqrt', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 10, 'in': 3, 'iw': 'sqrt', 'm': 0, 'on': 3, 'ow': 'sqrt', 's': 11, 't': 'var', 'v': '$4'},
    {   'd': 'e', 'e': 16, 'in': 5, 'iw': '/', 'm': 0, 'on': 5, 'ow': '/', 's': 17, 't': 'var', 'v': '$4'},
    {   'd': 'e', 'e': 18, 'in': 8, 'iw': 'pi', 'm': 0, 'on': 8, 'ow': 'pi', 's': 19, 't': 'var', 'v': '$4'},
    {   'd': 'e', 'e': 21, 'in': 9, 'iw': '22', 'm': 0, 'on': 9, 'ow': '22', 's': 22, 't': 'var', 'v': '$4'},
    {   'd': 'a', 'e': 31, 'in': None, 'iw': None, 'm': 0, 'on': 4, 'ow': 'sqrt', 's': 27, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 33, 'in': 6, 'iw': 'sin', 'm': 0, 'on': 6, 'ow': 'sin', 's': 35, 't': 'var', 'v': '$4'},
    {   'd': 'e', 'e': 37, 'in': 10, 'iw': 'pi', 'm': 0, 'on': 10, 'ow': 'pi', 's': 39, 't': 'var', 'v': '$4'},
    {   'd': 'e', 'e': 41, 'in': 7, 'iw': 'pi', 'm': 0, 'on': 7, 'ow': 'pi', 's': 43, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 46, 'in': 2, 'iw': 'F', 'm': 1, 'on': 2, 'ow': 'F', 's': 48, 't': 'hin', 'v': None},
    {   'd': 'r', 'e': 9, 'in': 1, 'iw': 'nroot', 'm': 0, 'on': None, 'ow': None, 's': 4, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 33, 'in': 4, 'iw': 'nroot', 'm': 0, 'on': None, 'ow': None, 's': 28, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {1: 0, 4: 11, 10: 3, 16: 5, 18: 8, 21: 9, 27: 12, 33: 6, 37: 10, 41: 7, 46: 2}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        # print('id__data:')
        # pp.pprint(sgparser.id__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
        # print('id__data: ')
        # pp.pprint(sgparser.id__data)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )



def test__latexParserUnparse__parallelSumOfCapacitance(verbose=False):
    """"""
    inputPattern = '(/ $1 $3)'
    outputPattern = '(frac $1 $3)'
    schemeword = '(= C^{parallelTotal}_{k} (/ (prod (= k_0 1) k C_{k_0}) (sum (= k_1 1) k (/ (prod (= k_0 1) k C_{k_0}) C_{k_1}))))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$3':0, '$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= C^{parallelTotal}_{k} (frac (prod (= k_0 1) k C_{k_0}) (sum (= k_1 1) k (frac (prod (= k_0 1) k C_{k_0}) C_{k_1}))))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'C^{parallelTotal}_{k}', 'm': 0, 'on': 1, 'ow': 'C^{parallelTotal}_{k}', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 30, 'in': None, 'iw': None, 'm': 0, 'on': 2, 'ow': 'frac', 's': 26, 't': 'static', 'v': None},#maybe can combine these in to EDIT with Damarau_Levenschstain_distance_modified_like LCSS for schemeSymbols? Something like TreeInTree, because LCSS can find all the bracket and space differences, and all the brackets and space encodes tree_structure. And then use the matched tree structures to match some of the schemeLabels that are different?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    {   'd': 'e', 'e': 32, 'in': 3, 'iw': 'prod', 'm': 0, 'on': 3, 'ow': 'prod', 's': 29, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 38, 'in': 5, 'iw': '=', 'm': 0, 'on': 5, 'ow': '=', 's': 35, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 40, 'in': 11, 'iw': 'k_0', 'm': 0, 'on': 11, 'ow': 'k_0', 's': 37, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 44, 'in': 12, 'iw': '1', 'm': 0, 'on': 12, 'ow': '1', 's': 41, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 47, 'in': 6, 'iw': 'k', 'm': 0, 'on': 6, 'ow': 'k', 's': 44, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 49, 'in': 7, 'iw': 'C_{k_0}', 'm': 0, 'on': 7, 'ow': 'C_{k_0}', 's': 46, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 59, 'in': 4, 'iw': 'sum', 'm': 0, 'on': 4, 'ow': 'sum', 's': 56, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 64, 'in': 8, 'iw': '=', 'm': 0, 'on': 8, 'ow': '=', 's': 61, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 66, 'in': 13, 'iw': 'k_1', 'm': 0, 'on': 13, 'ow': 'k_1', 's': 63, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 70, 'in': 14, 'iw': '1', 'm': 0, 'on': 14, 'ow': '1', 's': 67, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 73, 'in': 9, 'iw': 'k', 'm': 0, 'on': 9, 'ow': 'k', 's': 70, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 80, 'in': None, 'iw': None, 'm': 0, 'on': 10, 'ow': 'frac', 's': 76, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 82, 'in': 15, 'iw': 'prod', 'm': 0, 'on': 15, 'ow': 'prod', 's': 76, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 88, 'in': 17, 'iw': '=', 'm': 0, 'on': 17, 'ow': '=', 's': 82, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 90, 'in': 20, 'iw': 'k_0', 'm': 0, 'on': 20, 'ow': 'k_0', 's': 84, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 94, 'in': 21, 'iw': '1', 'm': 0, 'on': 21, 'ow': '1', 's': 88, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 97, 'in': 18, 'iw': 'k', 'm': 0, 'on': 18, 'ow': 'k', 's': 91, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 99, 'in': 19, 'iw': 'C_{k_0}', 'm': 0, 'on': 19, 'ow': 'C_{k_0}', 's': 93, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 108, 'in': 16, 'iw': 'C_{k_1}', 'm': 0, 'on': 16, 'ow': 'C_{k_1}', 's': 102, 't': 'var', 'v': '$3'},
    {   'd': 'r', 'e': 27, 'in': 2, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 26, 't': 'static', 'v': None},#maybe can combine these in to EDIT with Damarau_Levenschstain_distance_modified_like LCSS for schemeSymbols? Something like TreeInTree, because LCSS can find all the bracket and space differences, and all the brackets and space encodes tree_structure. And then use the matched tree structures to match some of the schemeLabels that are different?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    {   'd': 'r', 'e': 74, 'in': 10, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 73, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {
    1: 0,
    3: 1,
    26: 22,
    32: 3,
    38: 5,
    40: 11,
    44: 12,
    47: 6,
    49: 7,
    59: 4,
    64: 8,
    66: 13,
    70: 14,
    73: 9,
    76: 23,
    82: 15,
    88: 17,
    90: 20,
    94: 21,
    97: 18,
    99: 19,
    108: 16}
    if verbose:
        print('enclosureTree:')
        print(sgparser.iEnclosureTree)
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('id__data:')
        pp.pprint(sgparser.iId__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )





def test__latexParserUnparse__6levelsOfMatchesMODE2(verbose=False):
    """"""
    inputPattern = '(/ $1 $3)'
    outputPattern = '(frac $1 $3)'
    schemeword = '(= (+ 123 (nroot 12 12)) (/ (log 12 (+ 12 12)) (/ (^ (log 3 4) (log 5 6)) (/ (/ (/ (log 8 9) (/ (log 80 80) (- 36 47))) (- 33 44)) (- 53 64)))))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$3':0, '$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (+ 123 (nroot 12 12)) (frac (log 12 (+ 12 12)) (frac (^ (log 3 4) (log 5 6)) (frac (frac (frac (log 8 9) (frac (log 80 80) (- 36 47))) (- 33 44)) (- 53 64)))))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 4, 'in': 1, 'iw': '+', 'm': 0, 'on': 1, 'ow': '+', 's': 4, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 3, 'iw': '123', 'm': 0, 'on': 3, 'ow': '123', 's': 6, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 11, 'in': 4, 'iw': 'nroot', 'm': 0, 'on': 4, 'ow': 'nroot', 's': 11, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 17, 'in': 7, 'iw': '12', 'm': 0, 'on': 7, 'ow': '12', 's': 17, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 20, 'in': 8, 'iw': '12', 'm': 0, 'on': 8, 'ow': '12', 's': 20, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 30, 'in': None, 'iw': None, 'm': 0, 'on': 2, 'ow': 'frac', 's': 26, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 32, 'in': 5, 'iw': 'log', 'm': 0, 'on': 5, 'ow': 'log', 's': 29, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 36, 'in': 9, 'iw': '12', 'm': 0, 'on': 9, 'ow': '12', 's': 33, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 40, 'in': 10, 'iw': '+', 'm': 0, 'on': 10, 'ow': '+', 's': 37, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 42, 'in': 13, 'iw': '12', 'm': 0, 'on': 13, 'ow': '12', 's': 39, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 45, 'in': 14, 'iw': '12', 'm': 0, 'on': 14, 'ow': '12', 's': 42, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 55, 'in': None, 'iw': None, 'm': 0, 'on': 6, 'ow': 'frac', 's': 51, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 57, 'in': 11, 'iw': '^', 'm': 0, 'on': 11, 'ow': '^', 's': 51, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 60, 'in': 15, 'iw': 'log', 'm': 0, 'on': 15, 'ow': 'log', 's': 54, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 64, 'in': 19, 'iw': '3', 'm': 0, 'on': 19, 'ow': '3', 's': 58, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 66, 'in': 20, 'iw': '4', 'm': 0, 'on': 20, 'ow': '4', 's': 60, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 70, 'in': 16, 'iw': 'log', 'm': 0, 'on': 16, 'ow': 'log', 's': 64, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 74, 'in': 21, 'iw': '5', 'm': 0, 'on': 21, 'ow': '5', 's': 68, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 76, 'in': 22, 'iw': '6', 'm': 0, 'on': 22, 'ow': '6', 's': 70, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 85, 'in': None, 'iw': None, 'm': 0, 'on': 12, 'ow': 'frac', 's': 81, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 91, 'in': None, 'iw': None, 'm': 0, 'on': 17, 'ow': 'frac', 's': 87, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 97, 'in': None, 'iw': None, 'm': 0, 'on': 23, 'ow': 'frac', 's': 93, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 99, 'in': 27, 'iw': 'log', 'm': 0, 'on': 27, 'ow': 'log', 's': 84, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 103, 'in': 31, 'iw': '8', 'm': 0, 'on': 31, 'ow': '8', 's': 88, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 105, 'in': 32, 'iw': '9', 'm': 0, 'on': 32, 'ow': '9', 's': 90, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 113, 'in': None, 'iw': None, 'm': 0, 'on': 28, 'ow': 'frac', 's': 109, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 115, 'in': 33, 'iw': 'log', 'm': 0, 'on': 33, 'ow': 'log', 's': 97, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 119, 'in': 35, 'iw': '80', 'm': 0, 'on': 35, 'ow': '80', 's': 101, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 122, 'in': 36, 'iw': '80', 'm': 0, 'on': 36, 'ow': '80', 's': 104, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 127, 'in': 34, 'iw': '-', 'm': 0, 'on': 34, 'ow': '-', 's': 109, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 129, 'in': 37, 'iw': '36', 'm': 0, 'on': 37, 'ow': '36', 's': 111, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 132, 'in': 38, 'iw': '47', 'm': 0, 'on': 38, 'ow': '47', 's': 114, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 139, 'in': 24, 'iw': '-', 'm': 0, 'on': 24, 'ow': '-', 's': 121, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 141, 'in': 29, 'iw': '33', 'm': 0, 'on': 29, 'ow': '33', 's': 123, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 144, 'in': 30, 'iw': '44', 'm': 0, 'on': 30, 'ow': '44', 's': 126, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 150, 'in': 18, 'iw': '-', 'm': 0, 'on': 18, 'ow': '-', 's': 132, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 152, 'in': 25, 'iw': '53', 'm': 0, 'on': 25, 'ow': '53', 's': 134, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 155, 'in': 26, 'iw': '64', 'm': 0, 'on': 26, 'ow': '64', 's': 137, 't': 'var', 'v': '$3'},
    {   'd': 'r', 'e': 27, 'in': 2, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 26, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 49, 'in': 6, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 48, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 76, 'in': 12, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 75, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 79, 'in': 17, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 78, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 82, 'in': 23, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 81, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 95, 'in': 28, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 94, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {   1: 0,
    4: 1,
    6: 3,
    11: 4,
    17: 7,
    20: 8,
    26: 39,
    32: 5,
    36: 9,
    40: 10,
    42: 13,
    45: 14,
    51: 40,
    57: 11,
    60: 15,
    64: 19,
    66: 20,
    70: 16,
    74: 21,
    76: 22,
    81: 41,
    87: 42,
    93: 43,
    99: 27,
    103: 31,
    105: 32,
    109: 44,
    115: 33,
    119: 35,
    122: 36,
    127: 34,
    129: 37,
    132: 38,
    139: 24,
    141: 29,
    144: 30,
    150: 18,
    152: 25,
    155: 26}
    if verbose:
        print('enclosureTree:')
        print(sgparser.iEnclosureTree)
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('id__data:')
        pp.pprint(sgparser.iId__data)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )




def test__latexParserUnparser__impedanceOfParallelRLCCircuit1(verbose=False):
    """"""
    inputPattern = '(/ $1 $3)'
    outputPattern = '(frac $1 $3)'
    schemeword = '(= (/ (+ (/ (- (nroot (- 0 1) Z) (/ 1 R)) j) (/ 1 (* omega L))) omega) C)'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$3':0, '$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (frac (+ (frac (- (nroot (- 0 1) Z) (frac 1 R)) j) (frac 1 (* omega L))) omega) C)'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 8, 'in': None, 'iw': None, 'm': 0, 'on': 1, 'ow': 'frac', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 10, 'in': 3, 'iw': '+', 'm': 0, 'on': 3, 'ow': '+', 's': 7, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 17, 'in': None, 'iw': None, 'm': 0, 'on': 5, 'ow': 'frac', 's': 13, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 19, 'in': 7, 'iw': '-', 'm': 0, 'on': 7, 'ow': '-', 's': 13, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 22, 'in': 11, 'iw': 'nroot', 'm': 0, 'on': 11, 'ow': 'nroot', 's': 16, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 29, 'in': 15, 'iw': '-', 'm': 0, 'on': 15, 'ow': '-', 's': 23, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 31, 'in': 19, 'iw': '0', 'm': 0, 'on': 19, 'ow': '0', 's': 25, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 33, 'in': 20, 'iw': '1', 'm': 0, 'on': 20, 'ow': '1', 's': 27, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 36, 'in': 16, 'iw': 'Z', 'm': 0, 'on': 16, 'ow': 'Z', 's': 30, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 44, 'in': None, 'iw': None, 'm': 0, 'on': 12, 'ow': 'frac', 's': 40, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 45, 'in': 17, 'iw': '1', 'm': 0, 'on': 17, 'ow': '1', 's': 36, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 47, 'in': 18, 'iw': 'R', 'm': 0, 'on': 18, 'ow': 'R', 's': 38, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 51, 'in': 8, 'iw': 'j', 'm': 0, 'on': 8, 'ow': 'j', 's': 42, 't': 'var', 'v': '$3'},
    {   'd': 'a', 'e': 59, 'in': None, 'iw': None, 'm': 1, 'on': 6, 'ow': 'frac', 's': 55, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 60, 'in': 9, 'iw': '1', 'm': 1, 'on': 9, 'ow': '1', 's': 48, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 63, 'in': 10, 'iw': '*', 'm': 1, 'on': 10, 'ow': '*', 's': 51, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 65, 'in': 13, 'iw': 'omega', 'm': 1, 'on': 13, 'ow': 'omega', 's': 53, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 71, 'in': 14, 'iw': 'L', 'm': 1, 'on': 14, 'ow': 'L', 's': 59, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 76, 'in': 4, 'iw': 'omega', 'm': 0, 'on': 4, 'ow': 'omega', 's': 64, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 83, 'in': 2, 'iw': 'C', 'm': 1, 'on': 2, 'ow': 'C', 's': 71, 't': 'hin', 'v': None},
    {   'd': 'r', 'e': 5, 'in': 1, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 4, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 11, 'in': 5, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 10, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 35, 'in': 12, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 34, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 47, 'in': 6, 'iw': '/', 'm': 1, 'on': None, 'ow': None, 's': 46, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {   1: 0,
    4: 21,
    10: 3,
    13: 22,
    19: 7,
    22: 11,
    29: 15,
    31: 19,
    33: 20,
    36: 16,
    40: 23,
    45: 17,
    47: 18,
    51: 8,
    55: 24,
    60: 9,
    63: 10,
    65: 13,
    71: 14,
    76: 4,
    83: 2}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('enclosureTree:')
        pp.pprint(sgparser.iEnclosureTree)
        print('id__data:')
        pp.pprint(sgparser.iId__data)
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__latexParserUnparse__bipartiteSearch_dc_twoResistor_parallel_STEP1(verbose=False):
    """"""
    inputPattern = '(/ $0 $1)'
    outputPattern = '(\\frac $0 $1)'
    schemeword = '(= (/ (- (- 0 V_{ R_{ 1 } }) 0) I_{ R_{ 0 } }) (- 0 (/ 1 (- (/ 1 X_{ total_{ 6 } }) (/ 1 (- 0 R_{ R_{ 1 } }))))))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$0':0, '$1':0}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (\\frac (- (- 0 V_{ R_{ 1 } }) 0) I_{ R_{ 0 } }) (- 0 (\\frac 1 (- (\\frac 1 X_{ total_{ 6 } }) (\\frac 1 (- 0 R_{ R_{ 1 } }))))))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 9, 'in': None, 'iw': None, 'm': 0, 'on': 1, 'ow': '\\frac', 's': 4, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 11, 'in': 3, 'iw': '-', 'm': 0, 'on': 3, 'ow': '-', 's': 7, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 14, 'in': 7, 'iw': '-', 'm': 0, 'on': 7, 'ow': '-', 's': 10, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 16, 'in': 11, 'iw': '0', 'm': 0, 'on': 11, 'ow': '0', 's': 12, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 18, 'in': 12, 'iw': 'V_{ R_{ 1 } }', 'm': 0, 'on': 12, 'ow': 'V_{ R_{ 1 } }', 's': 14, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 33, 'in': 8, 'iw': '0', 'm': 0, 'on': 8, 'ow': '0', 's': 29, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 36, 'in': 4, 'iw': 'I_{ R_{ 0 } }', 'm': 0, 'on': 4, 'ow': 'I_{ R_{ 0 } }', 's': 32, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 52, 'in': 2, 'iw': '-', 'm': 1, 'on': 2, 'ow': '-', 's': 48, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 54, 'in': 5, 'iw': '0', 'm': 1, 'on': 5, 'ow': '0', 's': 50, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 62, 'in': None, 'iw': None, 'm': 1, 'on': 6, 'ow': '\\frac', 's': 57, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 63, 'in': 9, 'iw': '1', 'm': 1, 'on': 9, 'ow': '1', 's': 55, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 66, 'in': 10, 'iw': '-', 'm': 0, 'on': 10, 'ow': '-', 's': 58, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 74, 'in': None, 'iw': None, 'm': 0, 'on': 13, 'ow': '\\frac', 's': 69, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 75, 'in': 15, 'iw': '1', 'm': 0, 'on': 15, 'ow': '1', 's': 63, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 77, 'in': 16, 'iw': 'X_{ total_{ 6 } }', 'm': 0, 'on': 16, 'ow': 'X_{ total_{ 6 } }', 's': 65, 't': 'var', 'v': '$1'},
    {   'd': 'a', 'e': 102, 'in': None, 'iw': None, 'm': 1, 'on': 14, 'ow': '\\frac', 's': 97, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 103, 'in': 17, 'iw': '1', 'm': 1, 'on': 17, 'ow': '1', 's': 87, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 106, 'in': 18, 'iw': '-', 'm': 1, 'on': 18, 'ow': '-', 's': 90, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 108, 'in': 19, 'iw': '0', 'm': 1, 'on': 19, 'ow': '0', 's': 92, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 110, 'in': 20, 'iw': 'R_{ R_{ 1 } }', 'm': 1, 'on': 20, 'ow': 'R_{ R_{ 1 } }', 's': 94, 't': 'var', 'v': '$1'},
    {   'd': 'r', 'e': 5, 'in': 1, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 4, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 54, 'in': 6, 'iw': '/', 'm': 1, 'on': None, 'ow': None, 's': 53, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 62, 'in': 13, 'iw': '/', 'm': 0, 'on': None, 'ow': None, 's': 61, 't': 'static', 'v': None},
    {   'd': 'r', 'e': 86, 'in': 14, 'iw': '/', 'm': 1, 'on': None, 'ow': None, 's': 85, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {
    1: 0,
    4: 21,
    11: 3,
    14: 7,
    16: 11,
    18: 12,
    33: 8,
    36: 4,
    52: 2,
    54: 5,
    57: 22,
    63: 9,
    66: 10,
    69: 23,
    75: 15,
    77: 16,
    97: 24,
    103: 17,
    106: 18,
    108: 19,
    110: 20}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )

def test__differentiation__simple(verbose=False):
    """"""
    inputPattern = '(D (arcsin $0) $1)'
    outputPattern = '(* (/ 1 (nroot 2 (- 1 (* $0 $0)))) (D $0 $1))'
    schemeword = '(= h (/ (D (arcsin x) x) (+ 1 x)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {'$0':1, '$1':1}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= h (/ (* (/ 1 (nroot 2 (- 1 (* x x)))) (D x x)) (+ 1 x)))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'h', 'm': 0, 'on': 1, 'ow': 'h', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 2, 'iw': '/', 'm': 0, 'on': 2, 'ow': '/', 's': 6, 't': 'vor', 'v': None},
    {   'd': 'a', 'e': 10, 'in': None, 'iw': None, 'm': 0, 'on': 3, 'ow': '*', 's': 9, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 13, 'in': None, 'iw': None, 'm': 0, 'on': 5, 'ow': '/', 's': 12, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 15, 'in': None, 'iw': None, 'm': 0, 'on': 9, 'ow': '1', 's': 14, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 22, 'in': None, 'iw': None, 'm': 0, 'on': 10, 'ow': 'nroot', 's': 17, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 24, 'in': None, 'iw': None, 'm': 0, 'on': 13, 'ow': '2', 's': 23, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 27, 'in': None, 'iw': None, 'm': 0, 'on': 14, 'ow': '-', 's': 26, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 29, 'in': None, 'iw': None, 'm': 0, 'on': 15, 'ow': '1', 's': 28, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 32, 'in': None, 'iw': None, 'm': 0, 'on': 16, 'ow': '*', 's': 31, 't': 'static', 'v': None},
    {   'd': 'a', 'e': 34, 'in': None, 'iw': None, 'm': 0, 'on': 17, 'ow': 'x', 's': 33, 't': 'var', 'v': '$0'},
    {   'd': 'a', 'e': 36, 'in': None, 'iw': None, 'm': 0, 'on': 18, 'ow': 'x', 's': 35, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 42, 'in': 3, 'iw': 'D', 'm': 0, 'on': 6, 'ow': 'D', 's': 9, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 44, 'in': 9, 'iw': 'x', 'm': 0, 'on': 11, 'ow': 'x', 's': 19, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 46, 'in': 6, 'iw': 'x', 'm': 0, 'on': 12, 'ow': 'x', 's': 22, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 51, 'in': 4, 'iw': '+', 'm': 1, 'on': 4, 'ow': '+', 's': 26, 't': 'hin', 'v': None},
    {   'd': 'e', 'e': 53, 'in': 7, 'iw': '1', 'm': 1, 'on': 7, 'ow': '1', 's': 28, 't': 'hin', 'v': None},
    {   'd': 'e', 'e': 55, 'in': 8, 'iw': 'x', 'm': 1, 'on': 8, 'ow': 'x', 's': 30, 't': 'hin', 'v': None},
    {   'd': 'r', 'e': 18, 'in': 5, 'iw': 'arcsin', 'm': 0, 'on': None, 'ow': None, 's': 12, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {
    1: 0,
    3: 1,
    6: 2,
    9: 10,
    12: 11,
    14: 12,
    17: 13,
    23: 14,
    26: 15,
    28: 16,
    31: 17,
    33: 18,
    35: 19,
    42: 3,
    44: 9,
    46: 6,
    51: 4,
    53: 7,
    55: 8}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__differentiation__doesNotMeetvariableMinArgsCriteria(verbose=False):#<<<<<check changeBaseFormula again
    """"""
    inputPattern = '(D (arcsin $0) $1)'
    outputPattern = '(* (/ 1 (nroot 2 (- 1 (* $0 $0)))) (D $0 $1))'
    schemeword = '(= h (/ (D (arcsin 1) x) (+ 1 x)))'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # print(ast); import pdb;pdb.set_trace()
    """
    {
    ('=', 0): [('h', 1), ('/', 2)], 
    ('/', 2): [('D', 3), ('+', 4)], 
    ('D', 3): [('arcsin', 5), ('x', 6)], 
    ('+', 4): [('1', 7), ('x', 8)], 
    ('arcsin', 5): [('1', 9)]
    }
    self.schemeId__argCount:  {0: 3, 1: 1, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 1, 9: 0}
    """
    nodeIdsToSkip = []
    variableMinArgs = {'$0':1, '$1':1}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= h (/ (D (arcsin 1) x) (+ 1 x)))'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 3, 'in': 1, 'iw': 'h', 'm': 0, 'on': 1, 'ow': 'h', 's': 3, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 6, 'in': 2, 'iw': '/', 'm': 0, 'on': 2, 'ow': '/', 's': 6, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 9, 'in': 3, 'iw': 'D', 'm': 0, 'on': 3, 'ow': 'D', 's': 9, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 12, 'in': 5, 'iw': 'arcsin', 'm': 0, 'on': 5, 'ow': 'arcsin', 's': 12, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 19, 'in': 9, 'iw': '1', 'm': 0, 'on': 9, 'ow': '1', 's': 19, 't': 'var', 'v': '$0'},
    {   'd': 'e', 'e': 22, 'in': 6, 'iw': 'x', 'm': 0, 'on': 6, 'ow': 'x', 's': 22, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 26, 'in': 4, 'iw': '+', 'm': 1, 'on': 4, 'ow': '+', 's': 26, 't': 'hin', 'v': None},
    {   'd': 'e', 'e': 28, 'in': 7, 'iw': '1', 'm': 1, 'on': 7, 'ow': '1', 's': 28, 't': 'hin', 'v': None},
    {   'd': 'e', 'e': 30, 'in': 8, 'iw': 'x', 'm': 1, 'on': 8, 'ow': 'x', 's': 30, 't': 'hin', 'v': None}]
    expected_startPos__nodeId = {1: 0, 3: 1, 6: 2, 9: 3, 12: 5, 19: 9, 22: 6, 26: 4, 28: 7, 30: 8}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )


def test__latexParserUnparse__Trig1(verbose=False):
    """"""
    inputPattern = '(^ (sin $3) $1)'
    outputPattern = '(sin $1 $3)'
    schemeword = '(= (+ (^ (sin x) 2) (^ (cos x) 2)) 1)'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    # print(ast); import pdb;pdb.set_trace()
    """
    {
    ('=', 0): [('h', 1), ('/', 2)], 
    ('/', 2): [('D', 3), ('+', 4)], 
    ('D', 3): [('arcsin', 5), ('x', 6)], 
    ('+', 4): [('1', 7), ('x', 8)], 
    ('arcsin', 5): [('1', 9)]
    }
    self.schemeId__argCount:  {0: 3, 1: 1, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 1, 9: 0}
    """
    nodeIdsToSkip = []
    variableMinArgs = {}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (+ (sin 2 x) (^ (cos x) 2)) 1)'
    expected_schemeNodeChangeLog = [
    {   'd': 'e', 'e': 1, 'in': 0, 'iw': '=', 'm': 0, 'on': 0, 'ow': '=', 's': 1, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 4, 'in': 1, 'iw': '+', 'm': 0, 'on': 1, 'ow': '+', 's': 4, 't': 'vor', 'v': None},
    {   'd': 'e', 'e': 7, 'in': 5, 'iw': 'sin', 'm': 0, 'on': 3, 'ow': 'sin', 's': 10, 't': 'static', 'v': None},
    {   'd': 'e', 'e': 11, 'in': 6, 'iw': '2', 'm': 0, 'on': 5, 'ow': '2', 's': 17, 't': 'var', 'v': '$1'},
    {   'd': 'e', 'e': 13, 'in': 9, 'iw': 'x', 'm': 0, 'on': 6, 'ow': 'x', 's': 14, 't': 'var', 'v': '$3'},
    {   'd': 'e', 'e': 17, 'in': 4, 'iw': '^', 'm': 1, 'on': 4, 'ow': '^', 's': 21, 't': 'hin', 'v': None},
    {   'd': 'e', 'e': 20, 'in': 7, 'iw': 'cos', 'm': 1, 'on': 7, 'ow': 'cos', 's': 24, 't': 'hin', 'v': None},
    {   'd': 'e', 'e': 24, 'in': 10, 'iw': 'x', 'm': 1, 'on': 9, 'ow': 'x', 's': 28, 't': 'hin', 'v': None},
    {   'd': 'e', 'e': 27, 'in': 8, 'iw': '2', 'm': 1, 'on': 8, 'ow': '2', 's': 31, 't': 'hin', 'v': None},
    {   'd': 'e', 'e': 31, 'in': 2, 'iw': '1', 'm': 1, 'on': 2, 'ow': '1', 's': 35, 't': 'hin', 'v': None},
    {   'd': 'r', 'e': 8, 'in': 3, 'iw': '^', 'm': 0, 'on': None, 'ow': None, 's': 7, 't': 'static', 'v': None}]
    expected_startPos__nodeId = {1: 0, 4: 1, 7: 5, 11: 6, 13: 9, 17: 4, 20: 7, 24: 10, 27: 8, 31: 2}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )

def test__simpleParallel2ResistorSimplication__MultiplydividecancelVARIABLECONSISTENT(verbose=False): #<<<<<<<<<<<<<TODO make a test for MODE1
    """"""
    inputPattern = '(/ (* $1 $0) $0)'
    outputPattern = '$1'
    schemeword = '(= (/ (* R_{R_{0}} I_{R_{0}}) R_{R_{3}}) I_{R_{3}})'
    parser = Schemeparser(equationStr=schemeword)
    ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
    nodeIdsToSkip = []
    variableMinArgs = {}
    variableMaxArgs = {}
    sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
    sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
    manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
    expected = '(= (/ (* R_{R_{0}} I_{R_{0}}) R_{R_{3}}) I_{R_{3}})'
    expected_schemeNodeChangeLog = []
    expected_startPos__nodeId = {1: 0, 4: 1, 7: 3, 9: 5, 19: 6, 30: 4, 41: 2}
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('schemeNodeChangeLog(positional changes):')
        pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
        print('expected_startPos__nodeId: ')
        pp.pprint(sgparser.startPos__nodeId___oStr)
        print('OG startPos__nodeId: ')
        pp.pprint(startPos__nodeId)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword 
        and \
        expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
        and \
        expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
        )

# def test__latexParserUnparse__(verbose=False):
#     """"""
#     inputPattern = None
#     outputPattern = None
#     schemeword = None
#     parser = Schemeparser(equationStr=schemeword)
#     nodeIdsToSkip = []
#     variableMinArgs = {}
#     variableMaxArgs = {}
#     sgparser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose)
#     sgparser.matchIPattern(schemeword, startPos__nodeId=startPos__nodeId)
#     manipulatedSchemeword = sgparser.parse(nodeIdsToSkip=nodeIdsToSkip, variableMinArgs=variableMinArgs, variableMaxArgs=variableMaxArgs)
#     expected = None
#     expected_schemeNodeChangeLog = None
#     expected_startPos__nodeId = {}
#     if verbose:
#         print('OG:')
#         print(schemeword)
#         print('result:')
#         print(manipulatedSchemeword)
#         print('schemeNodeChangeLog(positional changes):')
#         pp.pprint(sgparser.schemeNodeChangeLog) # positional changes
#         print('expected_startPos__nodeId: ')
#         pp.pprint(sgparser.startPos__nodeId___oStr)
#         print('OG startPos__nodeId: ')
#         pp.pprint(startPos__nodeId)
#     print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
#         expected == manipulatedSchemeword 
#         and \
#         expected_schemeNodeChangeLog == sgparser.schemeNodeChangeLog #sgparser.schemeNodeChangeLog keeps swapping order... TODO why?
#         and \
#         expected_startPos__nodeId == sgparser.startPos__nodeId___oStr
#         )


if __name__=='__main__':
    #should include parts that can be differentiated and parts that cannot be differentiated<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    test__ideal__addition()
    test__idealNested__addition()
    test__simpleLeft__addition()
    test__simpleRight__addition()
    test__sameLevel__addition()
    test__nested__addition()
    test__nestedSameLevel__addition()
    test__2deep2wide__addition()
    test__2deep2wideSkip__addition()
    test__2deep2wideSkipTopLevel__addition()
    test__notApplicable__addition()
    test__functionCountChanges__subtractZero() #MODE2 decrease_in_static reverse_MODE1
    test__functionCountChanges__distributivity() #MODE2 simple decrease_in_static decrease_in_var
    test__moreVariableOutputThanInput__exponential1IsAnythingToThe0() # MODE0 complicated small_vorhin
    test__exponential1IsAnythingToThe0__skipNode() # MODE0 complicated small_vorhin skipNode
    test__manipulateLogarithm__logSameBaseAsArgumentGives1() # MODE0 

    test__manipulateExponential__exponential1IsAnythingToThe1() #MODE1_simple
    test__exponential1IsAnythingToThe1__complicatedWithUserSkip() #MODE1_complicatedWithSkip
    test__manipulateLogarithm__changeBaseFormula() #MODE2 simple increase_in_static generate_extra_outputVar
    test__onlyVariable__multiplyDivideCancal() #MODE1
    test__onlyVariable__multiplyDivideCancal6LevelsDeep() #MODE1 complicated
    test__latexParserUnparse__sqrtInSqrt() #MODE2 small_decrease_in_static
    test__latexParserUnparse__parallelSumOfCapacitance() #MODE2 decrease_in_static
    test__latexParserUnparse__6levelsOfMatchesMODE2() #MODE2 complicated decrease_in_static vorhin_with_many_schemeNodes
    test__latexParserUnparser__impedanceOfParallelRLCCircuit1() #MODE2 static_increase big_vorhin
    test__latexParserUnparse__bipartiteSearch_dc_twoResistor_parallel_STEP1()#MODE2 static_increase big_vorhin
    test__differentiation__simple()#MODE2 duplicated_iVar_in_oStr 
    test__differentiation__doesNotMeetvariableMinArgsCriteria()
    test__latexParserUnparse__Trig1()
    test__simpleParallel2ResistorSimplication__MultiplydividecancelVARIABLECONSISTENT()
    #after this test latexUnparse, equation.Manipulate again