


import sys
from foundation.automat.arithmetic.generator.standard import StandardFunctionClassGenerator
if __name__=='__main__':
    flag = sys.argv[1] if len(sys.argv) > 1 else 'alles'
    toRun = None
    if flag == 'alles':
        toRun = None
    else:
        toRun = flag
    print('generating standard function class files START', toRun)
    StandardFunctionClassGenerator().generateClass(verbose=True, toRun=toRun)
    print('generating standard function class files END')