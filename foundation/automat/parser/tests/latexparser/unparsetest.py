import inspect
import pprint

from foundation.automat.parser.sorte import Latexparser


def test__contiguousLeftOvers__decimalPlaces(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    ast = {   ('+', 5): [('-', 3), ('1.0', 6)],
    ('-', 3): [('0', 2), ('0.5', 4)],
    ('=', 0): [('+', 5), ('0.5', 1)]}

    parser = Latexparser(equationStr, verbose=verbose)
    parser._parse()
    expected_eqsStr = '-0.5 + 1.0 = 0.5'
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected_eqsStr == ast)
    if verbose:
        pp.pprint(parser.ast)


if __name__=='__main__':
    test__contiguousLeftOvers__decimalPlaces()