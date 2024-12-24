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
    manipulatedSchemeword = SchemeGrammarParser(inputPattern, outputPattern).parse(schemeword)
    expected = '(+ 2 1)'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == manipulatedSchemeword)


def test__idealNested__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(+ (+ c d) e)'
    manipulatedSchemeword = SchemeGrammarParser(inputPattern, outputPattern).parse(schemeword)
    expected = '(+ e (+ d c))'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == manipulatedSchemeword)


def test__simpleLeft__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= a (+ b c))'
    manipulatedSchemeword = SchemeGrammarParser(inputPattern, outputPattern).parse(schemeword)
    expected = '(= a (+ c b))'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == manipulatedSchemeword)



def test__simpleRight__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ b c) a)'
    manipulatedSchemeword = SchemeGrammarParser(inputPattern, outputPattern).parse(schemeword)
    expected = '(= (+ c b) a)'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == manipulatedSchemeword)



def test__sameLevel__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ a b) (+ c d))'
    manipulatedSchemeword = SchemeGrammarParser(inputPattern, outputPattern).parse(schemeword)
    expected = '(= (+ b a) (+ d c))'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == manipulatedSchemeword)



def test__nested__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= a (+ d (+ c b)))'
    manipulatedSchemeword = SchemeGrammarParser(inputPattern, outputPattern).parse(schemeword)
    expected = '(+ 2 1)'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == manipulatedSchemeword)



def test__nestedSameLevel__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ a b) (+ (+ c d) e))'
    manipulatedSchemeword = SchemeGrammarParser(inputPattern, outputPattern).parse(schemeword)
    expected = '(= (+ b a) (+ e (+ d c)))'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == manipulatedSchemeword)



def test__2deep2wide__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ (+ a b) (+ c d)) (+ (+ e f) (+ g h)))'
    manipulatedSchemeword = SchemeGrammarParser(inputPattern, outputPattern).parse(schemeword)
    expected = '(= (+ (+ d c) (+ b a)) (+ (+ h g) (+ f e)))'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == manipulatedSchemeword)



def test__2deep2wideSkip__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= (+ (+ a b) (+ c d)) (+ (+ e f) (+ g h)))'
    nodeIdsToSkip = [12]
    manipulatedSchemeword = SchemeGrammarParser(inputPattern, outputPattern).parse(schemeword, nodeIdsToSkip)
    expected = '(= (+ (+ d c) (+ a b)) (+ (+ h g) (+ f e)))'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == manipulatedSchemeword)



def test__notApplicable__addition(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    inputPattern = '(+ $0 $1)'
    outputPattern = '(+ $1 $0)'
    schemeword = '(= a (- (* c (/ 5 10)))) c))'
    nodeIdsToSkip = [12]
    parser = SchemeGrammarParser(inputPattern, outputPattern)
    manipulatedSchemeword = parser.parse(schemeword, nodeIdsToSkip)
    expected = '(= a (- (* c (/ 5 10)))) c))'
    if verbose:
        print(manipulatedSchemeword)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        expected == manipulatedSchemeword and parser.noMatches
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