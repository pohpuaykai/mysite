import pprint
import inspect

from foundation.automat.common.binarysearch import BinarySearch

pp = pprint.PrettyPrinter(indent=4)


def test__binarySearchPre__manySameNumbers(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    testName = inspect.currentframe().f_code.co_name
    sortedList = [1, 2, 3, 3, 3, 3, 5, 6]
    #                  ^
    #         expected=2
    numToInsert = 3
    idx = BinarySearch.binarySearchPre(sortedList, numToInsert)
    expected = 2
    if verbose:
        print(testName, idx)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == idx)


def test__binarySearchPre__manySameNumbersLargestIndex(verbose=False):
    """
    sortedList[i] < numToInsert <= sortedList[i+1]
    """
    testName = inspect.currentframe().f_code.co_name
    sortedList = [1, 2, 3, 3, 3, 3, 5, 6]
    #                           ^
    #                  expected=5
    numToInsert = 3
    idx = BinarySearch.binarySearchPre(sortedList, numToInsert, breakTie='r')
    expected = 5
    if verbose:
        print(testName, idx)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == idx)


def test__binarySearchPre__leftMost(verbose=False):
    testName = inspect.currentframe().f_code.co_name
    sortedList = [1, 2, 3, 3, 3, 3, 5, 6]
    numToInsert = 0
    idx = BinarySearch.binarySearchPre(sortedList, numToInsert)
    expected = 0
    if verbose:
        print(testName, idx)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == idx)


def test__binarySearchPre__rightMost(verbose=False):
    testName = inspect.currentframe().f_code.co_name
    sortedList = [1, 2, 3, 3, 3, 3, 5, 6]
    numToInsert = 7
    idx = BinarySearch.binarySearchPre(sortedList, numToInsert)
    expected = 8
    if verbose:
        print(testName, idx)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == idx)


def test__binarySearchApp__manySameNumbers(verbose=False):
    """
    sortedList[i] <= numToInsert < sortedList[i+1]
    """
    testName = inspect.currentframe().f_code.co_name
    sortedList = [1, 2, 3, 3, 3, 3, 5, 6]
    #                     ^
    #            expected=3
    numToInsert = 3
    idx = BinarySearch.binarySearchApp(sortedList, numToInsert)
    expected = 3
    if verbose:
        print(testName, idx)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == idx)


def test__binarySearchApp__manySameNumbersLargestIndex(verbose=False):
    """
    sortedList[i] <= numToInsert < sortedList[i+1]
    """
    testName = inspect.currentframe().f_code.co_name
    sortedList = [1, 2, 3, 3, 3, 3, 5, 6]
    #                             ^
    #                    expected=3
    numToInsert = 3
    idx = BinarySearch.binarySearchApp(sortedList, numToInsert, breakTie='r')
    expected = 6
    if verbose:
        print(testName, idx)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == idx)


def test__binarySearchApp__leftMost(verbose=False):
    """
    sortedList[i] <= numToInsert < sortedList[i+1]
    """
    testName = inspect.currentframe().f_code.co_name
    sortedList = [1, 2, 3, 3, 3, 3, 5, 6]
    numToInsert = 0
    idx = BinarySearch.binarySearchApp(sortedList, numToInsert)
    expected = 0
    if verbose:
        print(testName, idx)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == idx)


def test__binarySearchApp__rightMost(verbose=False):
    testName = inspect.currentframe().f_code.co_name
    sortedList = [1, 2, 3, 3, 3, 3, 5, 6]
    numToInsert = 7
    idx = BinarySearch.binarySearchApp(sortedList, numToInsert)
    expected = 8
    if verbose:
        print(testName, idx)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', expected == idx)




def test__binarySearchApp__intervalsTouchesTest0(verbose=False):
    testName = inspect.currentframe().f_code.co_name
    sortedList = [0, 0]
    numToInsert = 0
    idx = BinarySearch.binarySearchPre(sortedList, numToInsert)
    expected = 0
    if verbose:
        print(testName, idx)
    print('PASSED? ', expected == idx)



def test__binarySearchApp__intervalsTouchesTest1(verbose=False):
    testName = inspect.currentframe().f_code.co_name
    sortedList = [0, 0]
    numToInsert = 0
    idx = BinarySearch.binarySearchApp(sortedList, numToInsert, breakTie='r')
    expected = 2
    if verbose:
        print(testName, idx)
    print('PASSED? ', expected == idx)


if __name__=='__main__':
    test__binarySearchPre__manySameNumbers()
    test__binarySearchPre__manySameNumbersLargestIndex()
    test__binarySearchPre__leftMost()
    test__binarySearchPre__rightMost()
    test__binarySearchApp__manySameNumbers()
    test__binarySearchApp__manySameNumbersLargestIndex()
    test__binarySearchApp__leftMost()
    test__binarySearchApp__rightMost()

    test__binarySearchApp__intervalsTouchesTest0()
    test__binarySearchApp__intervalsTouchesTest1()