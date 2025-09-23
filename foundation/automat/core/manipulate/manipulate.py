import importlib
import inspect
import os
import re

from foundation.automat import AUTOMAT_MODULE_DIR
from foundation.automat.parser.sorte.schemeparser import Schemeparser

class Manipulate:
    """
    parent class of all patterns

    #~ DRAFT ~#
    input:
    1. Equation


    https://en.wikipedia.org/wiki/Green%27s_identities<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO

    """

    _PATTERN_FILENAMES__CLASSNAMES = {}

    @classmethod
    def PATTERN_FILENAMES__CLASSNAMES(cls):
        if len(cls._PATTERN_FILENAMES__CLASSNAMES) == 0:
            module_dir = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate', 'pattern')
            for module in os.listdir(module_dir):
                # print('***', module)
                if module.endswith('.py') and module != '__init__.py':
                    module_name = module[:-3] # remove .py
                    module_obj = importlib.import_module(f'.{module_name}', package='foundation.automat.core.manipulate.pattern')
                    for cls_name, ocls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                        if cls_name in ['Manipulate']: # skip the parent of all function
                            continue
                        # print(module_name)
                        cls._PATTERN_FILENAMES__CLASSNAMES[module_name] = cls_name
        # import pdb;pdb.set_trace()
        return cls._PATTERN_FILENAMES__CLASSNAMES



    def __init__(self, equation, direction, idx, verbose=False):
        self.direction = direction; self.idx = idx

        self.eq = equation
        self.verbose = verbose
        #make and store the scheme string
        self.schemeStr = equation.schemeStr#equation.toString('scheme')
        from foundation.automat.common.schemegrammarparser import SchemeGrammarParser
        self.grammarParserClass = SchemeGrammarParser
        self.grammarParser = None
        self.inputGrammar = self.rawRegexes[idx][direction]['scheme']
        self.outputGrammar = self.rawRegexes[idx][direction]['return']
        self.variableMinArgs = self.removeItemIfValueIfNone(self.rawRegexes[idx].get('minArgs', {}))
        self.variableMaxArgs = self.removeItemIfValueIfNone(self.rawRegexes[idx].get('maxArgs', {}))


    def initGrammerParser(self):
        #check if inputGrammar has no variables, 
        #if inputGrammar has no variables, then replace the outputGrammar's variables with variable, that is not in eq
        self.grammarParser = self.grammarParserClass(self.inputGrammar, self.outputGrammar, verbose=self.verbose)#memoise the grammarParser TODO



    def outputGrammarHasVariables(self):
        if self.grammarParser is None:
            self.initGrammerParser()
        return len(self.grammarParser.oUniqueVariables) > 0


    def applicable(self, startPos__nodeId=None):
        """
        #~ DRAFT ~#
        check if equation is manipulatable with this pattern
        """
        if self.grammarParser is None:
            self.initGrammerParser()
        #
        if self.verbose:
            print('self.schemeStr', self.schemeStr)
        #
        # self.grammarParser.buildEnclosureTree(self.schemeStr)
        self.grammarParser.matchIPattern(self.schemeStr, startPos__nodeId=startPos__nodeId)
        # print('IS IT NO MATCH??????????????????????????????????????', self.inputGrammar, '|||', self.outputGrammar, self.grammarParser.noMatches, '|||', self.schemeStr)
        return not self.grammarParser.noMatches


    def apply(self, startPos__nodeId=None, toAst=False):
        """
        #~ DRAFT ~#
        return manipulated equation
        """
        # if not self.outputGrammarHasVariables(): # no variables
        #     if self.verbose:
        #         print(f'{self.outputGrammar} has no grammar')
        #     return self.outputGrammar # output does not depend on input variables, no manipulation needed.
        # import pdb;pdb.set_trace()
        # print('applying iPattern: ', self.inputGrammar, 'on', self.schemeStr, 'corresponding oPattern: ', self.outputGrammar)
        if self.applicable(startPos__nodeId): # here we have matches, BUT, we should permuate applying outputGrammar to all the matches{using skipNode}, sometimes, we do not want to change all the inputGrammar
            existingVariables = list(self.eq.variablesScheme.keys())
            # manipulatedSchemeWord = self.grammarParser.parse(self.schemeStr, existingVariables=existingVariables)
            # print('self.variableMinArgs: ', self.variableMinArgs); print('self.variableMaxArgs: ', self.variableMaxArgs); import pdb;pdb.set_trace()
            print(self.TYPE, self.__class__.__name__, self.direction, self.idx, 'applying oPattern: ', self.outputGrammar, '| ON|', self.schemeStr, 'associated iPattern: ', self.inputGrammar)
            manipulatedSchemeWord = self.grammarParser.parse(nodeIdsToSkip=[], variableMinArgs=self.variableMinArgs, variableMaxArgs=self.variableMaxArgs)
            
            # return Schemeparser(equationStr=manipulatedSchemeWord)

            if toAst: 

            # # TODO seems unelegant..., but we should not modify self.eq and it also seems unelegant to instantiate Equation again
            # # TODO perhaps Manipulate should be a object of Equation?

                return self.grammarParser, self.TYPE, self.__class__.__name__, self.direction, self.idx
                # return Schemeparser(equationStr=manipulatedSchemeWord), self.grammarParser.schemeNodeChangeLog, Schemeparser(equationStr=self.inputGrammar), Schemeparser(equationStr=self.outputGrammar)

            #     print(self.grammarParser.verPosWord)
            #     self.grammarParser.verPosWord 
            #     from foundation.automat.parser.sorte.schemeparser import Schemeparser
            #     iParser = Schemeparser(equationStr=self.schemeStr)
            #     iAst, iFunctionsD, iVariablesD, iPrimitives, iTotalNodeCount = iParser._parse() # on this parse the nodeIds are completely different than in the original eq
            #     oParser = Schemeparser(equationStr=manipulatedSchemeWord)
            #     oAst, oFunctionsD, oVariablesD, oPrimitives, oTotalNodeCount = oParser._parse() # on this parse the nodeIds are completely different than in the original eq
            #     #this means we depend on the grammarParser to tell us, what has been removed at what position. TODO

            #     # import pdb;pdb.set_trace()
            #     return oAst, oFunctionsD, oVariablesD, oPrimitives, oTotalNodeCount, oParser.startPos__nodeId, \
            #     iAst, iFunctionsD, iVariablesD, iPrimitives, iTotalNodeCount, iParser.startPos__nodeId, \
            #     self.schemeStr, manipulatedSchemeWord
            return manipulatedSchemeWord
        return None # pattern unapplicable


    #HELPER
    def removeItemIfValueIfNone(self, dictionary):
        dictionary___NEW = {}
        for key, value in dictionary.items():
            if value is not None:
                dictionary___NEW[key] = value
        return dictionary___NEW