import re

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
        #make and store the scheme string
        self.schemeStr = equation.toString('scheme')
        from foundation.automat.common.schemegrammarparser import SchemeGrammarParser
        self.grammarParserClass = SchemeGrammarParser
        self.grammarParser = None


    def outputGrammarHasVariables(self, inputGrammar, outputGrammar):
        if self.grammarParser is None:
            self.grammarParser = self.grammarParserClass(inputGrammar, outputGrammar)#memoise the grammarParser TODO
        return len(self.grammarParser.outVariables) > 0


    def applicable(self, inputGrammar, outputGrammar):
        """
        #~ DRAFT ~#
        check if equation is manipulatable with this pattern
        """
        if self.grammarParser is None:
            self.grammarParser = self.grammarParserClass(inputGrammar, outputGrammar)#memoise the grammarParser TODO
        self.grammarParser.buildEnclosureTree(self.schemeStr)
        return not self.grammarParser.noMatches


    def apply(self, inputGrammar, outputGrammar):
        """
        #~ DRAFT ~#
        return manipulated equation
        """
        if not self.outputGrammarHasVariables(inputGrammar, outputGrammar): # no variables
            if self.verbose:
                print(f'{outputGrammar} has no grammar')
            return outputGrammar # output does not depend on input variables, no manipulation needed.
        if self.applicable(inputGrammar, outputGrammar): # here we have matches
            return self.grammarParser.parse(self.schemeStr)
        return self.schemeStr

