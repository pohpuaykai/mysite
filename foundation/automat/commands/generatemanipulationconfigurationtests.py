


import sys
from foundation.automat.core.manipulate.tests.configurationtests.generator.generator import Generator
if __name__=='__main__':
    flag = sys.argv[1] if len(sys.argv) > 1 else 'alles'
    toRun = None
    if flag == 'alles':
        toRun = None
    else:
        toRun = flag
    print('generating standard function class files START', toRun)
    Generator(verbose=True).generateClass(toRun=toRun)
    print('generating standard function class files END')