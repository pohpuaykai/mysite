import inspect
import pprint

from foundation.automat.common.smallcyclefinder import SmallCycleFinder


def smallcycles__dc_twoResistor_parallel(verbose=True):
    g = {
        0: [2, 3],
        1: [2, 3],
        2: [0, 1, 6],
        3: [0, 1, 5],
        4: [5, 6],
        5: [4, 3],
        6: [4, 2]}

    expected = None
    cycles = SmallCycleFinder.findCycles(g)


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == cycles)
    if verbose:
        print(cycles)

if __name__=='__main__':
    smallcycles__dc_twoResistor_parallel(True)