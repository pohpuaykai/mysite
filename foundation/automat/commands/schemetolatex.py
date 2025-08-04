


import ast
import sys
from foundation.automat.parser.sorte.latexparser import Latexparser
from foundation.automat.parser.sorte.schemeparser import Schemeparser
if __name__=='__main__':
    schemeStr = sys.argv[1]
    schemeParser = Schemeparser(equationStr=schemeStr)
    asTree, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = schemeParser._parse()
    # print(asTree)
    latexStr = Latexparser(ast=asTree, rootOfTree=schemeParser.rootOfTree)._unparse()
    print(latexStr)