

import sys
from foundation.automat.arithmetic.generator.standardconfigoneargument import Standardconfigoneargument
if __name__=='__main__':
    flag = sys.argv[1] if len(sys.argv) > 1 else 'alles'
    toRun = None
    if flag == 'alles':
        toRun = None
    else:
        toRun = flag
    print('standardconfigoneargument START ', toRun)
    Standardconfigoneargument.generateConfigurations(verbose=True, toRun=toRun)
    print('standardconfigoneargument END')