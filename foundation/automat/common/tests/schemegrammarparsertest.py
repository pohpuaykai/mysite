import pprint
import inspect

from foundation.automat.common.schemegrammarparser import SchemeGrammarParser

pp = pprint.PrettyPrinter(indent=4)


def test__ideal__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(+ 1 2)'
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword)
    expected = '(+ 2 1)'
    expected_verPosWord = [   
    {'d': 'a', 'e': 7, 'n': 0, 's': 0, 't': 'n', 'v': '$1', 'w': '(+ 2 1)'},
    {'d': 'r', 'e': 7, 'n': 0, 's': 0, 't': 'n', 'v': '$1', 'w': '(+ 1 2)'},
    {'d': 'e', 'e': 5, 'n': 3, 's': 3, 't': 'p', 'v': '$0', 'w': '1'},
    {'d': 'e', 'e': 3, 'n': 2, 's': 5, 't': 'p', 'v': '$1', 'w': '2'}]

    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )


def test__idealNested__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(+ (+ c d) e)'
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword)
    expected = '(+ e (+ d c))' 
    # e from 11 to 3 change:-8
    # (+ c d) from 3 to 5 change:+2
    # c from 6 to 10 change:+4
    # d from 8 to 8 change:0
    expected_verPosWord = [   
    {   'd': 'a',
        'e': 13,
        'n': 0,
        's': 0,
        't': 'n',
        'v': '$1',
        'w': '(+ e (+ d c))'},
    {   'd': 'r',
        'e': 13,
        'n': 0,
        's': 0,
        't': 'n',
        'v': '$1',
        'w': '(+ (+ c d) e)'},
    {'d': 'e', 'e': 5, 'n': 3, 's': 3, 't': 'p', 'v': '$0', 'w': '(+ d c)'},
    {'d': 'e', 'e': 3, 'n': 2, 's': 11, 't': 'p', 'v': '$1', 'w': 'e'},
    {'d': 'e', 'e': 10, 'n': 5, 's': 6, 't': 'p', 'v': '$0', 'w': 'c'},
    {'d': 'e', 'e': 8, 'n': 4, 's': 8, 't': 'p', 'v': '$1', 'w': 'd'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )


def test__simpleLeft__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= a (+ b c))'
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword)
    expected = '(= a (+ c b))'
    expected_verPosWord = [   
    {'d': 'a', 'e': 12, 'n': 0, 's': 5, 't': 'n', 'v': '$1', 'w': '(+ c b)'},
    {'d': 'r', 'e': 12, 'n': 0, 's': 5, 't': 'n', 'v': '$1', 'w': '(+ b c)'},
    {'d': 'e', 'e': 10, 'n': 3, 's': 8, 't': 'p', 'v': '$0', 'w': 'b'},
    {'d': 'e', 'e': 8, 'n': 2, 's': 10, 't': 'p', 'v': '$1', 'w': 'c'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )



def test__simpleRight__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ b c) a)'
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword)
    expected = '(= (+ c b) a)'
    expected_verPosWord = [   
    {'d': 'a', 'e': 10, 'n': 0, 's': 3, 't': 'n', 'v': '$1', 'w': '(+ c b)'},
    {'d': 'r', 'e': 10, 'n': 0, 's': 3, 't': 'n', 'v': '$1', 'w': '(+ b c)'},
    {'d': 'e', 'e': 8, 'n': 3, 's': 6, 't': 'p', 'v': '$0', 'w': 'b'},
    {'d': 'e', 'e': 6, 'n': 2, 's': 8, 't': 'p', 'v': '$1', 'w': 'c'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )



def test__sameLevel__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ a b) (+ c d))'
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword)
    expected = '(= (+ b a) (+ d c))'
    expected_verPosWord = [   
    {'d': 'a', 'e': 18, 'n': 0, 's': 11, 't': 'n', 'v': '$1', 'w': '(+ d c)'},
    {'d': 'r', 'e': 18, 'n': 0, 's': 11, 't': 'n', 'v': '$1', 'w': '(+ c d)'},
    {'d': 'a', 'e': 10, 'n': 0, 's': 3, 't': 'n', 'v': '$0', 'w': '(+ b a)'},
    {'d': 'r', 'e': 10, 'n': 0, 's': 3, 't': 'n', 'v': '$0', 'w': '(+ a b)'},
    {'d': 'e', 'e': 16, 'n': 4, 's': 14, 't': 'p', 'v': '$0', 'w': 'c'},
    {'d': 'e', 'e': 14, 'n': 3, 's': 16, 't': 'p', 'v': '$1', 'w': 'd'},
    {'d': 'e', 'e': 8, 'n': 6, 's': 6, 't': 'p', 'v': '$0', 'w': 'a'},
    {'d': 'e', 'e': 6, 'n': 5, 's': 8, 't': 'p', 'v': '$1', 'w': 'b'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )



def test__nested__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= a (+ d (+ c b)))'
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword)
    expected = '(= a (+ (+ b c) d))'
    #d OG: 8 RE: 16 change: 8
    #(+ c b) OG: 10 RE: 8 change: -2
    expected_verPosWord = [   {   'd': 'a',
        'e': 18,
        'n': 0,
        's': 5,
        't': 'n',
        'v': '$1',
        'w': '(+ (+ b c) d)'},
    {   'd': 'r',
        'e': 18,
        'n': 0,
        's': 5,
        't': 'n',
        'v': '$1',
        'w': '(+ d (+ c b))'},
    {'d': 'e', 'e': 16, 'n': 5, 's': 8, 't': 'p', 'v': '$0', 'w': 'd'},
    {'d': 'e', 'e': 8, 'n': 2, 's': 10, 't': 'p', 'v': '$1', 'w': '(+ b c)'},
    {'d': 'e', 'e': 13, 'n': 4, 's': 13, 't': 'p', 'v': '$0', 'w': 'c'},
    {'d': 'e', 'e': 11, 'n': 3, 's': 15, 't': 'p', 'v': '$1', 'w': 'b'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )



def test__nestedSameLevel__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ a b) (+ (+ c d) e))'
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword)
    expected = '(= (+ b a) (+ e (+ d c)))'
    expected_verPosWord = [   
    {   'd': 'a',
        'e': 24,
        'n': 0,
        's': 11,
        't': 'n',
        'v': '$1',
        'w': '(+ e (+ d c))'},
    {   'd': 'r',
        'e': 24,
        'n': 0,
        's': 11,
        't': 'n',
        'v': '$1',
        'w': '(+ (+ c d) e)'},
    {'d': 'a', 'e': 10, 'n': 0, 's': 3, 't': 'n', 'v': '$0', 'w': '(+ b a)'},
    {'d': 'r', 'e': 10, 'n': 0, 's': 3, 't': 'n', 'v': '$0', 'w': '(+ a b)'},
    {'d': 'e', 'e': 16, 'n': 4, 's': 14, 't': 'p', 'v': '$0', 'w': '(+ d c)'},
    {'d': 'e', 'e': 14, 'n': 3, 's': 22, 't': 'p', 'v': '$1', 'w': 'e'},
    {'d': 'e', 'e': 21, 'n': 6, 's': 17, 't': 'p', 'v': '$0', 'w': 'c'},
    {'d': 'e', 'e': 19, 'n': 5, 's': 19, 't': 'p', 'v': '$1', 'w': 'd'},
    {'d': 'e', 'e': 8, 'n': 8, 's': 6, 't': 'p', 'v': '$0', 'w': 'a'},
    {'d': 'e', 'e': 6, 'n': 7, 's': 8, 't': 'p', 'v': '$1', 'w': 'b'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )



def test__2deep2wide__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ (+ a b) (+ c d)) (+ (+ e f) (+ g h)))'
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword)
    expected = '(= (+ (+ d c) (+ b a)) (+ (+ h g) (+ f e)))'
    expected_verPosWord = [   {   'd': 'a',
        'e': 42,
        'n': 0,
        's': 23,
        't': 'n',
        'v': '$1',
        'w': '(+ (+ h g) (+ f e))'},
    {   'd': 'r',
        'e': 42,
        'n': 0,
        's': 23,
        't': 'n',
        'v': '$1',
        'w': '(+ (+ e f) (+ g h))'},
    {   'd': 'a',
        'e': 22,
        'n': 0,
        's': 3,
        't': 'n',
        'v': '$0',
        'w': '(+ (+ d c) (+ b a))'},
    {   'd': 'r',
        'e': 22,
        'n': 0,
        's': 3,
        't': 'n',
        'v': '$0',
        'w': '(+ (+ a b) (+ c d))'},
    {'d': 'e', 'e': 34, 'n': 6, 's': 26, 't': 'p', 'v': '$0', 'w': '(+ f e)'},
    {'d': 'e', 'e': 26, 'n': 3, 's': 34, 't': 'p', 'v': '$1', 'w': '(+ h g)'},
    {'d': 'e', 'e': 31, 'n': 5, 's': 37, 't': 'p', 'v': '$0', 'w': 'g'},
    {'d': 'e', 'e': 29, 'n': 4, 's': 39, 't': 'p', 'v': '$1', 'w': 'h'},
    {'d': 'e', 'e': 39, 'n': 8, 's': 29, 't': 'p', 'v': '$0', 'w': 'e'},
    {'d': 'e', 'e': 37, 'n': 7, 's': 31, 't': 'p', 'v': '$1', 'w': 'f'},
    {'d': 'e', 'e': 14, 'n': 12, 's': 6, 't': 'p', 'v': '$0', 'w': '(+ b a)'},
    {'d': 'e', 'e': 6, 'n': 9, 's': 14, 't': 'p', 'v': '$1', 'w': '(+ d c)'},
    {'d': 'e', 'e': 11, 'n': 11, 's': 17, 't': 'p', 'v': '$0', 'w': 'c'},
    {'d': 'e', 'e': 9, 'n': 10, 's': 19, 't': 'p', 'v': '$1', 'w': 'd'},
    {'d': 'e', 'e': 19, 'n': 14, 's': 9, 't': 'p', 'v': '$0', 'w': 'a'},
    {'d': 'e', 'e': 17, 'n': 13, 's': 11, 't': 'p', 'v': '$1', 'w': 'b'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )



def test__2deep2wideSkip__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ (+ a b) (+ c d)) (+ (+ e f) (+ g h)))'
    nodeIdsToSkip = [12]
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword, nodeIdsToSkip)
    expected = '(= (+ (+ d c) (+ a b)) (+ (+ h g) (+ f e)))'
    expected_verPosWord = [   {   'd': 'a',
        'e': 42,
        'n': 0,
        's': 23,
        't': 'n',
        'v': '$1',
        'w': '(+ (+ h g) (+ f e))'},
    {   'd': 'r',
        'e': 42,
        'n': 0,
        's': 23,
        't': 'n',
        'v': '$1',
        'w': '(+ (+ e f) (+ g h))'},
    {   'd': 'a',
        'e': 22,
        'n': 0,
        's': 3,
        't': 'n',
        'v': '$0',
        'w': '(+ (+ d c) (+ a b))'},
    {   'd': 'r',
        'e': 22,
        'n': 0,
        's': 3,
        't': 'n',
        'v': '$0',
        'w': '(+ (+ a b) (+ c d))'},
    {'d': 'e', 'e': 34, 'n': 6, 's': 26, 't': 'p', 'v': '$0', 'w': '(+ f e)'},
    {'d': 'e', 'e': 26, 'n': 3, 's': 34, 't': 'p', 'v': '$1', 'w': '(+ h g)'},
    {'d': 'e', 'e': 31, 'n': 5, 's': 37, 't': 'p', 'v': '$0', 'w': 'g'},
    {'d': 'e', 'e': 29, 'n': 4, 's': 39, 't': 'p', 'v': '$1', 'w': 'h'},
    {'d': 'e', 'e': 39, 'n': 8, 's': 29, 't': 'p', 'v': '$0', 'w': 'e'},
    {'d': 'e', 'e': 37, 'n': 7, 's': 31, 't': 'p', 'v': '$1', 'w': 'f'},
    {'d': 'e', 'e': 14, 'n': 12, 's': 6, 't': 'p', 'v': '$0', 'w': '(+ a b)'},
    {'d': 'e', 'e': 6, 'n': 9, 's': 14, 't': 'p', 'v': '$1', 'w': '(+ d c)'},
    {'d': 'e', 'e': 11, 'n': 11, 's': 17, 't': 'p', 'v': '$0', 'w': 'c'},
    {'d': 'e', 'e': 9, 'n': 10, 's': 19, 't': 'p', 'v': '$1', 'w': 'd'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )



def test__notApplicable__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= a (- (* c (/ 5 10)))) c))'
    nodeIdsToSkip = [12]
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword, nodeIdsToSkip)
    expected = '(= a (- (* c (/ 5 10)))) c))'
    expected_verPosWord = [   {   'd': 'a',
        'e': 28,
        'n': 0,
        's': 0,
        't': 'n',
        'v': '$1',
        'w': '(= a (- (* c (/ 5 10)))) c))'},
    {   'd': 'r',
        'e': 28,
        'n': 0,
        's': 0,
        't': 'n',
        'v': '$1',
        'w': '(= a (- (* c (/ 5 10)))) c))'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )


def test__functionCountChanges__subtractZero(verbose=False):
    """
    This case requires the matchedFrag and unmatchedFrag.... TODO
    """
    inputPattern = '(- $0 0)'
    outputPattern = '$0' # try to nest this to see if it will work
    schemeword = '(= (* I_{R} R) (- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0))'
    nodeIdsToSkip = []
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword, nodeIdsToSkip)
    expected = '(= (* I_{R} R) (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}))'
    expected_verPosWord = [   
    {   'd': 'a',
        'e': 56,
        'n': 0,
        's': 15,
        't': 'n',
        'v': '$0',
        'w': '(- (* I_{R_{C}} R_{C}) V^{Q1}_{BE})'},
    {   'd': 'r',
        'e': 56,
        'n': 0,
        's': 15,
        't': 'n',
        'v': '$0',
        'w': '(- (- (* I_{R_{C}} R_{C}) V^{Q1}_{BE}) 0)'},
    {'d': 'r', 'e': 18, 'n': 1, 's': 15, 't': 'p', 'v': None, 'w': '(- '},
    {'d': 'r', 'e': 56, 'n': 1, 's': 53, 't': 'p', 'v': None, 'w': ' 0)'},
    {   'd': 'e',
        'e': 15,
        'n': 2,
        's': 18,
        't': 'p',
        'v': '$0',
        'w': '(- (* I_{R_{C}} R_{C}) V^{Q1}_{BE})'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )


def test__functionCountChanges__distributivity(verbose=False):
    """"""
    inputPattern = '(+ (* $0 $1) (* $0 $2))'
    outputPattern = '(* $0 (+ $1 $2))'
    schemeword = '(= a (+ (* b12 c34) (* b12 d56)))'#'(= a (+ (* b c) (* b d)))'
    nodeIdsToSkip = []
    parser = SchemeGrammarParser(inputPattern, outputPattern, verbose=verbose, recordMaking=True)
    manipulatedSchemeword = parser.parse(schemeword, nodeIdsToSkip)
    expected = '(= a (* b12 (+ c34 d56)))'#'(= a (* b (+ c d)))'
    expected_verPosWord = [   
    {'d': 'r', 'e': 14, 'n': 1, 's': 11, 't': 'p', 'v': '$0', 'w': 'b12'},
    {   'd': 'a',
        'e': 32,
        'n': 0,
        's': 5,
        't': 'n',
        'v': '$2',
        'w': '(* b12 (+ c34 d56))'},
    {   'd': 'r',
        'e': 32,
        'n': 0,
        's': 5,
        't': 'n',
        'v': '$2',
        'w': '(+ (* b12 c34) (* b12 d56))'},
    {'d': 'r', 'e': 8, 'n': 1, 's': 5, 't': 'p', 'v': None, 'w': '(+ '},
    {'d': 'r', 'e': 14, 'n': 1, 's': 10, 't': 'p', 'v': None, 'w': ' b12'},
    {'d': 'r', 'e': 19, 'n': 1, 's': 18, 't': 'p', 'v': None, 'w': ')'},
    {'d': 'r', 'e': 22, 'n': 1, 's': 21, 't': 'p', 'v': None, 'w': '*'},
    {'d': 'a', 'e': 14, 'n': 1, 's': 13, 't': 'p', 'v': None, 'w': '+'},
    {'d': 'e', 'e': 15, 'n': 4, 's': 15, 't': 'p', 'v': '$1', 'w': 'c34'},
    {'d': 'e', 'e': 19, 'n': 2, 's': 27, 't': 'p', 'v': '$2', 'w': 'd56'}]
    if verbose:
        print('OG:')
        print(schemeword)
        print('result:')
        print(manipulatedSchemeword)
        print('verPosWord(positional changes):')
        pp.pprint(parser.verPosWord) # positional changes
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and \
        expected_verPosWord == parser.verPosWord 
        )


if __name__=='__main__':
    test__ideal__addition()
    test__idealNested__addition()
    test__simpleLeft__addition()
    test__simpleRight__addition()
    test__sameLevel__addition()
    test__nested__addition()
    test__nestedSameLevel__addition()
    test__2deep2wide__addition()
    test__2deep2wideSkip__addition()
    test__notApplicable__addition()
    test__functionCountChanges__subtractZero()
    test__functionCountChanges__distributivity()