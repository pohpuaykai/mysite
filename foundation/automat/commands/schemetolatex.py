


import ast
import sys
from foundation.automat.parser.sorte.latexparser import Latexparser
from foundation.automat.parser.sorte.schemeparser import Schemeparser
if __name__=='__main__':
    schemeStr = sys.argv[1]
    asTree, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = Schemeparser(equationStr=schemeStr)._parse()
    # print(asTree)
    latexStr = Latexparser(ast=asTree)._unparse()
    print(latexStr)