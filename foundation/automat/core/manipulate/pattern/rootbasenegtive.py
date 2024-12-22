
from foundation.automat.core.manipulate.manipulate import Manipulate


class Rootbasenegtive(Manipulate):
    """

    """
    TYPE = 'pretty'

    def __init__(self, equation, verbose):
        """

        """
        self.rawRegexes = [{'type': 'regex', 'vor': {'scheme': '(nroot -P %)', 'return': '(nroot P (/ 1 %))'}, 'hin': {'scheme': '(nroot P (/ 1 %))', 'return': '(nroot -P %)'}}]
        super().__init__(equation, verbose=verbose)