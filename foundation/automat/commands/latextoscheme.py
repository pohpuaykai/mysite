


import ast
import sys
from foundation.automat.parser.sorte.latexparser import Latexparser
if __name__=='__main__':
    latexStr = sys.argv[1]
    # print('latexStr(removed):', latexStr.replace('\\', ''))
    # print('latexStr: ', latexStr)
    schemeStr = Latexparser(equationStr=latexStr).latexToScheme()
    print(schemeStr)