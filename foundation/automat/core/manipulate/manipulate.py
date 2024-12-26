import re

class Manipulate:
    """
    parent class of all patterns

    #~ DRAFT ~#
    input:
    1. Equation


    """

    def __init__(self, equation, direction, idx, verbose=False):
        self.eq = equation
        self.verbose = verbose
        #make and store the scheme string
        self.schemeStr = equation.toString('scheme')
        from foundation.automat.common.schemegrammarparser import SchemeGrammarParser
        self.grammarParserClass = SchemeGrammarParser
        self.grammarParser = None
        self.inputGrammar = self.rawRegexes[idx][direction]['scheme']
        self.outputGrammar = self.rawRegexes[idx][direction]['return']


    def initGrammerParser(self):
        #check if inputGrammar has no variables, 
        #if inputGrammar has no variables, then replace the outputGrammar's variables with variable, that is not in eq
        self.grammarParser = self.grammarParserClass(self.inputGrammar, self.outputGrammar)#memoise the grammarParser TODO
        # if len(self.grammarParser.variables) == 0:
        if len(set(self.grammarParser.outVariables)) > len(set(self.grammarParser.variables)):
            missingMetaVariables = list(set(self.grammarParser.outVariables) - set(self.grammarParser.variables))
            variable_eVariable__tupleList = []
            varList = list(self.eq.variables.keys())
            # for outVariable in self.grammarParser.outVariables:
            for outVariable in missingMetaVariables:
                eVariable = self.giveMeAVariableNotInThisList(varList)
                varList.append(eVariable)
                variable_eVariable__tupleList.append((outVariable, eVariable))
            import copy
            subsitutedOutputGrammar = copy.deepcopy(self.outputGrammar)
            for variable, eVariable in variable_eVariable__tupleList:
                subsitutedOutputGrammar = subsitutedOutputGrammar.replace(variable, eVariable)
            #TODO refactor?
            #FOR THIS CASE: #it was not matched to any variables, or inputPattern has no variables
            self.grammarParser.subsitutedOutputGrammar = subsitutedOutputGrammar
            #FOR THIS CASE: #match&not_just_variable_and_space&less_variable_available
            self.grammarParser.additionalReplacementStrForVariablesDict = dict(variable_eVariable__tupleList)


    def outputGrammarHasVariables(self):
        if self.grammarParser is None:
            self.initGrammerParser()
        return len(self.grammarParser.outVariables) > 0


    def applicable(self):
        """
        #~ DRAFT ~#
        check if equation is manipulatable with this pattern
        """
        if self.grammarParser is None:
            self.initGrammerParser()
        self.grammarParser.buildEnclosureTree(self.schemeStr)
        return not self.grammarParser.noMatches


    def apply(self):
        """
        #~ DRAFT ~#
        return manipulated equation
        """
        if not self.outputGrammarHasVariables(): # no variables
            if self.verbose:
                print(f'{self.outputGrammar} has no grammar')
            return self.outputGrammar # output does not depend on input variables, no manipulation needed.
        if self.applicable(): # here we have matches
            return self.grammarParser.parse(self.schemeStr)
        return self.schemeStr


    def giveMeAVariableNotInThisList(self, varList):
        """
        look for variables that start with v_
        if None, then return v_{0}
        else:
            look for the number after v_ or v_{
            if no number after v_
                then return v_{0}
            else
                return v_{num+1}
        """
        variablePrefix = 'v_'
        variableStartingWithPrefix = None
        for variable in varList:
            if variable.startswith(variablePrefix+'{'): # we expect the variable to close with '}', following LatexSyntax
                startPosOfCurlyBracket = variable.index(variablePrefix+'{') + len(variablePrefix+'{')
                #since we expect this to be the first openbracket, then the close bracket must be the last '}' == no need bracket-matching
                endPosOfCurlyBracket = variable.rindex('}')
                try:
                    num = int(variable[startPosOfCurlyBracket:endPosOfCurlyBracket])
                except:
                    num = 0
            elif variable.startswith(variablePrefix): # we expect the next position to be a number, following LatexSyntax
                posOfEndOfVariablePrefix = variable.index(variablePrefix) + len(variablePrefix)
                try:
                    num = int(variable[posOfEndOfVariablePrefix:posOfEndOfVariablePrefix+1]) + 1 # we only expect a 1 character number, following LatexSyntax
                    #then we add 1 to get the next
                except:
                    num = 0 #next character after variablePrefix is not a num
            else:
                num = 0
        return f'v_{{{num}}}'