


import sys
from foundation.automat.core.manipulate.generator.patternate import Patternate
if __name__=='__main__':
    flag = sys.argv[1] if len(sys.argv) > 1 else 'alles'
    toRun = None
    if flag == 'alles':
        toRun = None
    else:
        toRun = flag
    print('generating standard function class files START', toRun)
    Patternate(verbose=True).generateClass(toRun=toRun)
    print('generating standard function class files END')