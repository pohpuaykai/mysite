


import ast
import sys
from foundation.automat.parser.sorte.schemeparser import Schemeparser
if __name__=='__main__':
    astStr = sys.argv[1]
    asTree = ast.literal_eval(astStr)
    # print(asTree)
    schemeStr = Schemeparser(ast=asTree)._unparse()
    print(schemeStr)