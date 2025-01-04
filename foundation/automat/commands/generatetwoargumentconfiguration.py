

import sys
from foundation.automat.arithmetic.generator.standardconfigtwoargument import Standardconfigtwoargument
if __name__=='__main__':
    flag = sys.argv[1] if len(sys.argv) > 1 else 'alles'
    toRun = None
    if flag == 'alles':
        toRun = None
    else:
        toRun = flag
    print('standardconfigtwoargument START ', toRun)
    Standardconfigtwoargument.generateConfigurations(verbose=True, toRun=toRun)
    print('standardconfigtwoargument END')