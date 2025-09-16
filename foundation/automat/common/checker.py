import re

class Booler:
    """
    Methods in this class always return boolean
    """

    @classmethod
    def isFloat(cls, num):
        try:
            float(num)
            return True
        except:
            return False


    @classmethod
    def isNum(cls, possibilityNumberString): # OpenAI says this one more efficient... cause no throw Exception.
        NONNUMERIC_NUMBERS = ['e', 'i', '\\pi']
        return re.match('[-]*\\d+(?:\\.{1}\\d+)*$', possibilityNumberString) is not None or possibilityNumberString in NONNUMERIC_NUMBERS
