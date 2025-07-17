import pprint
import inspect

from foundation.automat.common.stringcompare import StringCompare

pp = pprint.PrettyPrinter(indent=4)

def test__damerauLevenshtein__schemegrammarparser_distributivity(verbose=False):

    a = '(+ (* $ $) (* $ $))'#'(+ (* $0 $1) (* $0 $2))'
    b = '(* $ (+ $ $))'#'(* $0 (+ $1 $2))'
    r = StringCompare.damerauLevenshtein(a, b)

    if verbose:
        print(r)
    print(inspect.currentframe().f_code.co_name, 'PASSED? ', 
        
        )


if __name__=='__main__':
    test__damerauLevenshtein__schemegrammarparser_distributivity(True)