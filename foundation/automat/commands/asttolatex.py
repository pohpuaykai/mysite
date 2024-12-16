


import ast
import sys
from foundation.automat.parser.sorte.latexparser import Latexparser
if __name__=='__main__':
    astStr = sys.argv[1]
    asTree = ast.literal_eval(astStr)
    # print(asTree)
    latexStr = Latexparser(ast=asTree)._unparse()
    print(latexStr)