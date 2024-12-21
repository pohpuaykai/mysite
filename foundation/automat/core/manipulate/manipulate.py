class Manipulate:
    """
    parent class of all patterns

    #~ DRAFT ~#
    input:
    1. Equation


    """

    def __init__(self, equation, verbose):
        self.eq = equation
        self.verbose = verbose


    def applicable(self):
        """
        #~ DRAFT ~#
        check if equation is manipulatable with this pattern
        """
        pass

    def apply(self):
        """
        #~ DRAFT ~#
        return manipulated equation
        """
        if self.applicable():
            pass