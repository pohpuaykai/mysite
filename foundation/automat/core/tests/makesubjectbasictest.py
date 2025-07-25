import inspect
import pprint

from foundation.automat.core.equation import Equation


pp = pprint.PrettyPrinter(indent=4)


def test__makeSubject2Input__addition0(verbose=False):
    eq0 = Equation('(= a (+ b c))', 'scheme', verbose=verbose) # a=b+c
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a-c=b' # to be filled in 
    expectedFunctions = {'-': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('-', 2), ('b', 3)], ('-', 2): [('a', 1), ('c', 4)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 1, 8: 4, 11: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('-', 2): [('a', 1), ('c', 4)],
                         ('=', 0): [('-', 2), ('b', 3)]},
        'resultSchemeStr': '(= (- a c) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)




def test__makeSubject2Input__addition1(verbose=False):
    eq0 = Equation('(= a (+ b c))', 'scheme', verbose=verbose) # a=b+c
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a-b=c' # to be filled in 
    expectedFunctions = {'-': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('-', 2), ('c', 4)], ('-', 2): [('a', 1), ('b', 3)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 1, 8: 3, 11: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('-', 2): [('a', 1), ('b', 3)],
                         ('=', 0): [('-', 2), ('c', 4)]},
        'resultSchemeStr': '(= (- a b) c)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__subtraction0(verbose=False):
    eq0 = Equation('(= a (- b c))', 'scheme', verbose=verbose) # a=b-c
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a+c=b' # to be filled in 
    expectedFunctions = {'+': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('+', 2), ('b', 3)], ('+', 2): [('a', 1), ('c', 4)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 1, 8: 4, 11: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '-',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('+', 2): [('a', 1), ('c', 4)],
                         ('=', 0): [('+', 2), ('b', 3)]},
        'resultSchemeStr': '(= (+ a c) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__subtraction1(verbose=False):
    eq0 = Equation('(= a (- b c))', 'scheme', verbose=verbose) # a=b-c
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'b-a=c' # to be filled in 
    expectedFunctions = {'-': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('-', 2), ('c', 4)], ('-', 2): [('b', 3), ('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 3, 8: 1, 11: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '-',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('-', 2): [('b', 3), ('a', 1)],
                         ('=', 0): [('-', 2), ('c', 4)]},
        'resultSchemeStr': '(= (- b a) c)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__multiply0(verbose=False):
    eq0 = Equation('(= a (* b c))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{a}{c}=b' # to be filled in 
    expectedFunctions = {'/': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('/', 2), ('b', 3)], ('/', 2): [('a', 1), ('c', 4)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 1, 8: 4, 11: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('/', 2): [('a', 1), ('c', 4)],
                         ('=', 0): [('/', 2), ('b', 3)]},
        'resultSchemeStr': '(= (/ a c) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__multiply1(verbose=False):
    eq0 = Equation('(= a (* b c))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{a}{b}=c' # to be filled in 
    expectedFunctions = {'/': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('/', 2), ('c', 4)], ('/', 2): [('a', 1), ('b', 3)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 1, 8: 3, 11: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('/', 2): [('a', 1), ('b', 3)],
                         ('=', 0): [('/', 2), ('c', 4)]},
        'resultSchemeStr': '(= (/ a b) c)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__divide0(verbose=False):
    eq0 = Equation('(= a (/ b c))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'ac=b' # to be filled in 
    expectedFunctions = {'*': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('*', 2), ('b', 3)], ('*', 2): [('a', 1), ('c', 4)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 1, 8: 4, 11: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('*', 2): [('a', 1), ('c', 4)],
                         ('=', 0): [('*', 2), ('b', 3)]},
        'resultSchemeStr': '(= (* a c) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__divide1(verbose=False):
    eq0 = Equation('(= a (/ b c))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\frac{b}{a}=c' # to be filled in 
    expectedFunctions = {'/': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('/', 2), ('c', 4)], ('/', 2): [('b', 3), ('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 3, 8: 1, 11: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('/', 2): [('b', 3), ('a', 1)],
                         ('=', 0): [('/', 2), ('c', 4)]},
        'resultSchemeStr': '(= (/ b a) c)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__exponent0(verbose=False):
    eq0 = Equation('(= a (^ b c))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\sqrt[c]{a}=b' # to be filled in 
    expectedFunctions = {'nroot': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('nroot', 2), ('b', 3)], ('nroot', 2): [('c', 4), ('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 10: 4, 12: 1, 15: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '^',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('nroot', 2), ('b', 3)],
                         ('nroot', 2): [('c', 4), ('a', 1)]},
        'resultSchemeStr': '(= (nroot c a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__exponent1(verbose=False):
    eq0 = Equation('(= a (^ b c))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\log_b(a)=c' # to be filled in 
    expectedFunctions = {'log': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('log', 2), ('c', 4)], ('log', 2): [('b', 3), ('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 8: 3, 10: 1, 13: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '^',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('log', 2), ('c', 4)],
                         ('log', 2): [('b', 3), ('a', 1)]},
        'resultSchemeStr': '(= (log b a) c)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__nroot0(verbose=False):
    eq0 = Equation('(= a (nroot b c))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\log_a(c)=b' # to be filled in 
    expectedFunctions = {'log': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('log', 2), ('b', 3)], ('log', 2): [('a', 1), ('c', 4)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 8: 1, 10: 4, 13: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'nroot',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('log', 2), ('b', 3)],
                         ('log', 2): [('a', 1), ('c', 4)]},
        'resultSchemeStr': '(= (log a c) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__nroot1(verbose=False):
    eq0 = Equation('(= a (nroot b c))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a^b=c' # to be filled in 
    expectedFunctions = {'^': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('^', 2), ('c', 4)], ('^', 2): [('a', 1), ('b', 3)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 1, 8: 3, 11: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': 'nroot',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('^', 2), ('c', 4)],
                         ('^', 2): [('a', 1), ('b', 3)]},
        'resultSchemeStr': '(= (^ a b) c)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__log0(verbose=False):
    eq0 = Equation('(= a (log b c))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\sqrt[a]{c}=b' # to be filled in 
    expectedFunctions = {'nroot': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('nroot', 2), ('b', 3)], ('nroot', 2): [('a', 1), ('c', 4)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 10: 1, 12: 4, 15: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'log',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('nroot', 2), ('b', 3)],
                         ('nroot', 2): [('a', 1), ('c', 4)]},
        'resultSchemeStr': '(= (nroot a c) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject2Input__log1(verbose=False):
    eq0 = Equation('(= a (log b c))', 'scheme', verbose=verbose) # a=log_b(c)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('c')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'b^a=c' # to be filled in 
    expectedFunctions = {'^': 1} # count
    expectedVariables = {'a': 1, 'b': 1, 'c': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('^', 2), ('c', 4)], ('^', 2): [('b', 3), ('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 6: 3, 8: 1, 11: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': 'log',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('^', 2), ('c', 4)],
                         ('^', 2): [('b', 3), ('a', 1)]},
        'resultSchemeStr': '(= (^ b a) c)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arccosec(verbose=False):
    eq0 = Equation('(= a (arccosec b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\cosec(a)=b' # to be filled in 
    expectedFunctions = {'cosec': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('cosec', 2), ('b', 3)], ('cosec', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 10: 1, 13: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccosec',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('cosec', 2), ('b', 3)],
                         ('cosec', 2): [('a', 1)]},
        'resultSchemeStr': '(= (cosec a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arccosech(verbose=False):
    eq0 = Equation('(= a (arccosech b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\cosech(a)=b' # to be filled in 
    expectedFunctions = {'cosech': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('cosech', 2), ('b', 3)], ('cosech', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 11: 1, 14: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccosech',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('cosech', 2), ('b', 3)],
                         ('cosech', 2): [('a', 1)]},
        'resultSchemeStr': '(= (cosech a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arccos(verbose=False):
    eq0 = Equation('(= a (arccos b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\cos(a)=b' # to be filled in 
    expectedFunctions = {'cos': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('cos', 2), ('b', 3)], ('cos', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 8: 1, 11: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccos',
        'id': 2,
        'lastId': 0,
        'resultAST': {('=', 0): [('cos', 2), ('b', 3)], ('cos', 2): [('a', 1)]},
        'resultSchemeStr': '(= (cos a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arccosh(verbose=False):
    eq0 = Equation('(= a (arccosh b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\cosh(a)=b' # to be filled in 
    expectedFunctions = {'cosh': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('cosh', 2), ('b', 3)], ('cosh', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 9: 1, 12: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccosh',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('cosh', 2), ('b', 3)],
                         ('cosh', 2): [('a', 1)]},
        'resultSchemeStr': '(= (cosh a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arccot(verbose=False):
    eq0 = Equation('(= a (arccot b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\cot(a)=b' # to be filled in 
    expectedFunctions = {'cot': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('cot', 2), ('b', 3)], ('cot', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 8: 1, 11: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccot',
        'id': 2,
        'lastId': 0,
        'resultAST': {('=', 0): [('cot', 2), ('b', 3)], ('cot', 2): [('a', 1)]},
        'resultSchemeStr': '(= (cot a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arccoth(verbose=False):
    eq0 = Equation('(= a (arccoth b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\coth(a)=b' # to be filled in 
    expectedFunctions = {'coth': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('coth', 2), ('b', 3)], ('coth', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 9: 1, 12: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccoth',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('coth', 2), ('b', 3)],
                         ('coth', 2): [('a', 1)]},
        'resultSchemeStr': '(= (coth a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arcsec(verbose=False):
    eq0 = Equation('(= a (arcsec b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\sec(a)=b' # to be filled in 
    expectedFunctions = {'sec': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('sec', 2), ('b', 3)], ('sec', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 8: 1, 11: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arcsec',
        'id': 2,
        'lastId': 0,
        'resultAST': {('=', 0): [('sec', 2), ('b', 3)], ('sec', 2): [('a', 1)]},
        'resultSchemeStr': '(= (sec a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arcsech(verbose=False):
    eq0 = Equation('(= a (arcsech b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\sech(a)=b' # to be filled in 
    expectedFunctions = {'sech': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('sech', 2), ('b', 3)], ('sech', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 9: 1, 12: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arcsech',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('sech', 2), ('b', 3)],
                         ('sech', 2): [('a', 1)]},
        'resultSchemeStr': '(= (sech a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arcsin(verbose=False):
    eq0 = Equation('(= a (arcsin b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\sin(a)=b' # to be filled in 
    expectedFunctions = {'sin': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('sin', 2), ('b', 3)], ('sin', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 8: 1, 11: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arcsin',
        'id': 2,
        'lastId': 0,
        'resultAST': {('=', 0): [('sin', 2), ('b', 3)], ('sin', 2): [('a', 1)]},
        'resultSchemeStr': '(= (sin a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arcsinh(verbose=False):
    eq0 = Equation('(= a (arcsinh b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\sinh(a)=b' # to be filled in 
    expectedFunctions = {'sinh': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('sinh', 2), ('b', 3)], ('sinh', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 9: 1, 12: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arcsinh',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('sinh', 2), ('b', 3)],
                         ('sinh', 2): [('a', 1)]},
        'resultSchemeStr': '(= (sinh a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arctan(verbose=False):
    eq0 = Equation('(= a (arctan b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\tan(a)=b' # to be filled in 
    expectedFunctions = {'tan': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('tan', 2), ('b', 3)], ('tan', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 8: 1, 11: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arctan',
        'id': 2,
        'lastId': 0,
        'resultAST': {('=', 0): [('tan', 2), ('b', 3)], ('tan', 2): [('a', 1)]},
        'resultSchemeStr': '(= (tan a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__arctanh(verbose=False):
    eq0 = Equation('(= a (arctanh b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\tanh(a)=b' # to be filled in 
    expectedFunctions = {'tanh': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('tanh', 2), ('b', 3)], ('tanh', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 9: 1, 12: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arctanh',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('tanh', 2), ('b', 3)],
                         ('tanh', 2): [('a', 1)]},
        'resultSchemeStr': '(= (tanh a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__cosec(verbose=False):
    eq0 = Equation('(= a (cosec b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arccosec(a)=b' # to be filled in 
    expectedFunctions = {'arccosec': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arccosec', 2), ('b', 3)], ('arccosec', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 13: 1, 16: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cosec',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arccosec', 2), ('b', 3)],
                         ('arccosec', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arccosec a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__cosech(verbose=False):
    eq0 = Equation('(= a (cosech b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arccosech(a)=b' # to be filled in 
    expectedFunctions = {'arccosech': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arccosech', 2), ('b', 3)], ('arccosech', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 14: 1, 17: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cosech',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arccosech', 2), ('b', 3)],
                         ('arccosech', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arccosech a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__cos(verbose=False):
    eq0 = Equation('(= a (cos b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arccos(a)=b' # to be filled in 
    expectedFunctions = {'arccos': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arccos', 2), ('b', 3)], ('arccos', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 11: 1, 14: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cos',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arccos', 2), ('b', 3)],
                         ('arccos', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arccos a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__cosh(verbose=False):
    eq0 = Equation('(= a (cosh b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arccosh(a)=b' # to be filled in 
    expectedFunctions = {'arccosh': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arccosh', 2), ('b', 3)], ('arccosh', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 12: 1, 15: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cosh',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arccosh', 2), ('b', 3)],
                         ('arccosh', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arccosh a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__cot(verbose=False):
    eq0 = Equation('(= a (cot b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arccot(a)=b' # to be filled in 
    expectedFunctions = {'arccot': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arccot', 2), ('b', 3)], ('arccot', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 11: 1, 14: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cot',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arccot', 2), ('b', 3)],
                         ('arccot', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arccot a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__coth(verbose=False):
    eq0 = Equation('(= a (coth b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arccoth(a)=b' # to be filled in 
    expectedFunctions = {'arccoth': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arccoth', 2), ('b', 3)], ('arccoth', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 12: 1, 15: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'coth',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arccoth', 2), ('b', 3)],
                         ('arccoth', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arccoth a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__sec(verbose=False):
    eq0 = Equation('(= a (sec b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arcsec(a)=b' # to be filled in 
    expectedFunctions = {'arcsec': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arcsec', 2), ('b', 3)], ('arcsec', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 11: 1, 14: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'sec',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arcsec', 2), ('b', 3)],
                         ('arcsec', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arcsec a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__sech(verbose=False):
    eq0 = Equation('(= a (sech b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arcsech(a)=b' # to be filled in 
    expectedFunctions = {'arcsech': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arcsech', 2), ('b', 3)], ('arcsech', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 12: 1, 15: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'sech',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arcsech', 2), ('b', 3)],
                         ('arcsech', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arcsech a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__sin(verbose=False):
    eq0 = Equation('(= a (sin b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arcsin(a)=b' # to be filled in 
    expectedFunctions = {'arcsin': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arcsin', 2), ('b', 3)], ('arcsin', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 11: 1, 14: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'sin',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arcsin', 2), ('b', 3)],
                         ('arcsin', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arcsin a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__sinh(verbose=False):
    eq0 = Equation('(= a (sinh b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arcsinh(a)=b' # to be filled in 
    expectedFunctions = {'arcsinh': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arcsinh', 2), ('b', 3)], ('arcsinh', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 12: 1, 15: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'sinh',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arcsinh', 2), ('b', 3)],
                         ('arcsinh', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arcsinh a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__tan(verbose=False):
    eq0 = Equation('(= a (tan b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arctan(a)=b' # to be filled in 
    expectedFunctions = {'arctan': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arctan', 2), ('b', 3)], ('arctan', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 11: 1, 14: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'tan',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arctan', 2), ('b', 3)],
                         ('arctan', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arctan a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__makeSubject1Input__tanh(verbose=False):
    eq0 = Equation('(= a (tanh b))', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = '\\arctanh(a)=b' # to be filled in 
    expectedFunctions = {'arctanh': 1} # count
    expectedVariables = {'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('arctanh', 2), ('b', 3)], ('arctanh', 2): [('a', 1)]}
    expected__startPos__nodeId = {1: 0, 4: 2, 12: 1, 15: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'tanh',
        'id': 2,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('arctanh', 2), ('b', 3)],
                         ('arctanh', 2): [('a', 1)]},
        'resultSchemeStr': '(= (arctanh a) b)'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)





def test__leftSide__addition0(verbose=False):
    eq0 = Equation('(= (+ a b) c )', 'scheme', verbose=verbose) # a=b+c
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=c-b' # to be filled in 
    expectedFunctions = {'-': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('-', 1)], ('-', 1): [('c', 2), ('b', 4)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 8: 2, 10: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '+',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('-', 1): [('c', 2), ('b', 4)],
                         ('=', 0): [('a', 3), ('-', 1)]},
        'resultSchemeStr': '(= a (- c b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__addition1(verbose=False):
    eq0 = Equation('(= (+ a b) c )', 'scheme', verbose=verbose) # a=b+c
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'b=c-a' # to be filled in 
    expectedFunctions = {'-': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('b', 4), ('-', 1)], ('-', 1): [('c', 2), ('a', 3)]}
    expected__startPos__nodeId = {1: 0, 3: 4, 6: 1, 8: 2, 10: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '+',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('-', 1): [('c', 2), ('a', 3)],
                         ('=', 0): [('b', 4), ('-', 1)]},
        'resultSchemeStr': '(= b (- c a))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__subtraction0(verbose=False):
    eq0 = Equation('(= (- a b) c)', 'scheme', verbose=verbose) # a=b-c
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=c+b' # to be filled in 
    expectedFunctions = {'+': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('+', 1)], ('+', 1): [('c', 2), ('b', 4)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 8: 2, 10: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '-',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('+', 1): [('c', 2), ('b', 4)],
                         ('=', 0): [('a', 3), ('+', 1)]},
        'resultSchemeStr': '(= a (+ c b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__subtraction1(verbose=False):
    eq0 = Equation('(= (- a b) c)', 'scheme', verbose=verbose) # a=b-c
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'b=a-c' # to be filled in 
    expectedFunctions = {'-': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('b', 4), ('-', 1)], ('-', 1): [('a', 3), ('c', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 4, 6: 1, 8: 3, 10: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '-',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('-', 1): [('a', 3), ('c', 2)],
                         ('=', 0): [('b', 4), ('-', 1)]},
        'resultSchemeStr': '(= b (- a c))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__multiply0(verbose=False):
    eq0 = Equation('(= (* a b) c)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\frac{c}{b}' # to be filled in 
    expectedFunctions = {'/': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('/', 1)], ('/', 1): [('c', 2), ('b', 4)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 8: 2, 10: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '*',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('/', 1): [('c', 2), ('b', 4)],
                         ('=', 0): [('a', 3), ('/', 1)]},
        'resultSchemeStr': '(= a (/ c b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__multiply1(verbose=False):
    eq0 = Equation('(= (* a b) c)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'b=\\frac{c}{a}' # to be filled in 
    expectedFunctions = {'/': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('b', 4), ('/', 1)], ('/', 1): [('c', 2), ('a', 3)]}
    expected__startPos__nodeId = {1: 0, 3: 4, 6: 1, 8: 2, 10: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '*',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('/', 1): [('c', 2), ('a', 3)],
                         ('=', 0): [('b', 4), ('/', 1)]},
        'resultSchemeStr': '(= b (/ c a))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__divide0(verbose=False):
    eq0 = Equation('(= (/ a b) c)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=cb' # to be filled in 
    expectedFunctions = {'*': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('*', 1)], ('*', 1): [('c', 2), ('b', 4)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 8: 2, 10: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '/',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('*', 1): [('c', 2), ('b', 4)],
                         ('=', 0): [('a', 3), ('*', 1)]},
        'resultSchemeStr': '(= a (* c b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__divide1(verbose=False):
    eq0 = Equation('(= (/ a b) c)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'b=\\frac{a}{c}' # to be filled in 
    expectedFunctions = {'/': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('b', 4), ('/', 1)], ('/', 1): [('a', 3), ('c', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 4, 6: 1, 8: 3, 10: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '/',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('/', 1): [('a', 3), ('c', 2)],
                         ('=', 0): [('b', 4), ('/', 1)]},
        'resultSchemeStr': '(= b (/ a c))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__exponent0(verbose=False):
    eq0 = Equation('(= (^ a b) c)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\sqrt[b]{c}' # to be filled in 
    expectedFunctions = {'nroot': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('nroot', 1)], ('nroot', 1): [('b', 4), ('c', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 12: 4, 14: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': '^',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('nroot', 1)],
                         ('nroot', 1): [('b', 4), ('c', 2)]},
        'resultSchemeStr': '(= a (nroot b c))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__exponent1(verbose=False):
    eq0 = Equation('(= (^ a b) c)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'b=\\log_a(c)' # to be filled in 
    expectedFunctions = {'log': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('b', 4), ('log', 1)], ('log', 1): [('a', 3), ('c', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 4, 6: 1, 10: 3, 12: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': '^',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('b', 4), ('log', 1)],
                         ('log', 1): [('a', 3), ('c', 2)]},
        'resultSchemeStr': '(= b (log a c))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__nroot0(verbose=False):
    eq0 = Equation('(= (nroot a b) c)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\log_c(b)' # to be filled in 
    expectedFunctions = {'log': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('log', 1)], ('log', 1): [('c', 2), ('b', 4)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 10: 2, 12: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'nroot',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('log', 1)],
                         ('log', 1): [('c', 2), ('b', 4)]},
        'resultSchemeStr': '(= a (log c b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__nroot1(verbose=False):
    eq0 = Equation('(= (nroot a b) c)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'b=c^a' # to be filled in 
    expectedFunctions = {'^': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('b', 4), ('^', 1)], ('^', 1): [('c', 2), ('a', 3)]}
    expected__startPos__nodeId = {1: 0, 3: 4, 6: 1, 8: 2, 10: 3}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': 'nroot',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('b', 4), ('^', 1)],
                         ('^', 1): [('c', 2), ('a', 3)]},
        'resultSchemeStr': '(= b (^ c a))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__log0(verbose=False):
    eq0 = Equation('(= (log a b) c)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\sqrt[c]{b}' # to be filled in 
    expectedFunctions = {'nroot': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('nroot', 1)], ('nroot', 1): [('c', 2), ('b', 4)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 12: 2, 14: 4}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'log',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('nroot', 1)],
                         ('nroot', 1): [('c', 2), ('b', 4)]},
        'resultSchemeStr': '(= a (nroot c b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__log1(verbose=False):
    eq0 = Equation('(= (log a b) c)', 'scheme', verbose=verbose) # a=log_b(c)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('b')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'b=a^c' # to be filled in 
    expectedFunctions = {'^': 1} # count
    expectedVariables = {'c': 1, 'a': 1, 'b': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 5 # count
    #
    expectedModifiedAST = {('=', 0): [('b', 4), ('^', 1)], ('^', 1): [('a', 3), ('c', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 4, 6: 1, 8: 3, 10: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 1,
        'functionName': 'log',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('b', 4), ('^', 1)],
                         ('^', 1): [('a', 3), ('c', 2)]},
        'resultSchemeStr': '(= b (^ a c))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arccosec(verbose=False):
    eq0 = Equation('(= (arccosec a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\cosec(b)' # to be filled in 
    expectedFunctions = {'cosec': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('cosec', 1)], ('cosec', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 12: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccosec',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('cosec', 1)],
                         ('cosec', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (cosec b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arccosech(verbose=False):
    eq0 = Equation('(= (arccosech a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\cosech(b)' # to be filled in 
    expectedFunctions = {'cosech': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('cosech', 1)], ('cosech', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 13: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccosech',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('cosech', 1)],
                         ('cosech', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (cosech b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arccos(verbose=False):
    eq0 = Equation('(= (arccos a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\cos(b)' # to be filled in 
    expectedFunctions = {'cos': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('cos', 1)], ('cos', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 10: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccos',
        'id': 1,
        'lastId': 0,
        'resultAST': {('=', 0): [('a', 3), ('cos', 1)], ('cos', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (cos b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arccosh(verbose=False):
    eq0 = Equation('(= (arccosh a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\cosh(b)' # to be filled in 
    expectedFunctions = {'cosh': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('cosh', 1)], ('cosh', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 11: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccosh',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('cosh', 1)],
                         ('cosh', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (cosh b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arccot(verbose=False):
    eq0 = Equation('(= (arccot a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\cot(b)' # to be filled in 
    expectedFunctions = {'cot': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('cot', 1)], ('cot', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 10: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccot',
        'id': 1,
        'lastId': 0,
        'resultAST': {('=', 0): [('a', 3), ('cot', 1)], ('cot', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (cot b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arccoth(verbose=False):
    eq0 = Equation('(= (arccoth a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\coth(b)' # to be filled in 
    expectedFunctions = {'coth': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('coth', 1)], ('coth', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 11: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arccoth',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('coth', 1)],
                         ('coth', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (coth b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arcsec(verbose=False):
    eq0 = Equation('(= (arcsec a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\sec(b)' # to be filled in 
    expectedFunctions = {'sec': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('sec', 1)], ('sec', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 10: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arcsec',
        'id': 1,
        'lastId': 0,
        'resultAST': {('=', 0): [('a', 3), ('sec', 1)], ('sec', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (sec b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arcsech(verbose=False):
    eq0 = Equation('(= (arcsech a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\sech(b)' # to be filled in 
    expectedFunctions = {'sech': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('sech', 1)], ('sech', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 11: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arcsech',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('sech', 1)],
                         ('sech', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (sech b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arcsin(verbose=False):
    eq0 = Equation('(= (arcsin a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\sin(b)' # to be filled in 
    expectedFunctions = {'sin': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('sin', 1)], ('sin', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 10: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arcsin',
        'id': 1,
        'lastId': 0,
        'resultAST': {('=', 0): [('a', 3), ('sin', 1)], ('sin', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (sin b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arcsinh(verbose=False):
    eq0 = Equation('(= (arcsinh a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\sinh(b)' # to be filled in 
    expectedFunctions = {'sinh': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('sinh', 1)], ('sinh', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 11: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arcsinh',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('sinh', 1)],
                         ('sinh', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (sinh b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arctan(verbose=False):
    eq0 = Equation('(= (arctan a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\tan(b)' # to be filled in 
    expectedFunctions = {'tan': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('tan', 1)], ('tan', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 10: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arctan',
        'id': 1,
        'lastId': 0,
        'resultAST': {('=', 0): [('a', 3), ('tan', 1)], ('tan', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (tan b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__arctanh(verbose=False):
    eq0 = Equation('(= (arctanh a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\tanh(b)' # to be filled in 
    expectedFunctions = {'tanh': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('tanh', 1)], ('tanh', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 11: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'arctanh',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('tanh', 1)],
                         ('tanh', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (tanh b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__cosec(verbose=False):
    eq0 = Equation('(= (cosec a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arccosec(b)' # to be filled in 
    expectedFunctions = {'arccosec': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arccosec', 1)], ('arccosec', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 15: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cosec',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arccosec', 1)],
                         ('arccosec', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arccosec b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__cosech(verbose=False):
    eq0 = Equation('(= (cosech a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arccosech(b)' # to be filled in 
    expectedFunctions = {'arccosech': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arccosech', 1)], ('arccosech', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 16: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cosech',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arccosech', 1)],
                         ('arccosech', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arccosech b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__cos(verbose=False):
    eq0 = Equation('(= (cos a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arccos(b)' # to be filled in 
    expectedFunctions = {'arccos': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arccos', 1)], ('arccos', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 13: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cos',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arccos', 1)],
                         ('arccos', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arccos b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__cosh(verbose=False):
    eq0 = Equation('(= (cosh a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arccosh(b)' # to be filled in 
    expectedFunctions = {'arccosh': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arccosh', 1)], ('arccosh', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 14: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cosh',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arccosh', 1)],
                         ('arccosh', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arccosh b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__cot(verbose=False):
    eq0 = Equation('(= (cot a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arccot(b)' # to be filled in 
    expectedFunctions = {'arccot': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arccot', 1)], ('arccot', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 13: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'cot',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arccot', 1)],
                         ('arccot', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arccot b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__coth(verbose=False):
    eq0 = Equation('(= (coth a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arccoth(b)' # to be filled in 
    expectedFunctions = {'arccoth': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arccoth', 1)], ('arccoth', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 14: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'coth',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arccoth', 1)],
                         ('arccoth', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arccoth b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__sec(verbose=False):
    eq0 = Equation('(= (sec a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arcsec(b)' # to be filled in 
    expectedFunctions = {'arcsec': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arcsec', 1)], ('arcsec', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 13: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'sec',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arcsec', 1)],
                         ('arcsec', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arcsec b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__sech(verbose=False):
    eq0 = Equation('(= (sech a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arcsech(b)' # to be filled in 
    expectedFunctions = {'arcsech': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arcsech', 1)], ('arcsech', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 14: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'sech',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arcsech', 1)],
                         ('arcsech', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arcsech b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__sin(verbose=False):
    eq0 = Equation('(= (sin a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arcsin(b)' # to be filled in 
    expectedFunctions = {'arcsin': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arcsin', 1)], ('arcsin', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 13: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'sin',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arcsin', 1)],
                         ('arcsin', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arcsin b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__sinh(verbose=False):
    eq0 = Equation('(= (sinh a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arcsinh(b)' # to be filled in 
    expectedFunctions = {'arcsinh': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arcsinh', 1)], ('arcsinh', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 14: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'sinh',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arcsinh', 1)],
                         ('arcsinh', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arcsinh b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__tan(verbose=False):
    eq0 = Equation('(= (tan a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arctan(b)' # to be filled in 
    expectedFunctions = {'arctan': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arctan', 1)], ('arctan', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 13: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'tan',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arctan', 1)],
                         ('arctan', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arctan b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)


def test__leftSide__tanh(verbose=False):
    eq0 = Equation('(= (tanh a) b)', 'scheme', verbose=verbose)
    before__ast = eq0.ast
    before__startPos__nodeId = eq0.startPos__nodeId
    modifiedAST, stepsWithoutSimplify = eq0.makeSubject('a')
    from foundation.automat.parser.sorte.latexparser import Latexparser
    latexStr = Latexparser(ast=modifiedAST, rootOfTree=eq0.rootOfTree)._unparse()
    expectedLatexStr = 'a=\\arctanh(b)' # to be filled in 
    expectedFunctions = {'arctanh': 1} # count
    expectedVariables = {'b': 1, 'a': 1} # count
    expectedPrimitives = {} # count
    expectedTotalNodeCount = 4 # count
    #
    expectedModifiedAST = {('=', 0): [('a', 3), ('arctanh', 1)], ('arctanh', 1): [('b', 2)]}
    expected__startPos__nodeId = {1: 0, 3: 3, 6: 1, 14: 2}
    expected__stepsWithoutSimplify = [
    {   'argumentIdx': 0,
        'functionName': 'tanh',
        'id': 1,
        'lastId': 0,
        'resultAST': {   ('=', 0): [('a', 3), ('arctanh', 1)],
                         ('arctanh', 1): [('b', 2)]},
        'resultSchemeStr': '(= a (arctanh b))'
    }
    ]
    #
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expectedLatexStr == latexStr and 
        expectedFunctions == eq0.functionsScheme and 
        expectedVariables == eq0.variablesScheme and 
        expectedPrimitives == eq0.primitivesScheme and
        expectedTotalNodeCount == eq0.totalNodeCountScheme and
        expectedModifiedAST == modifiedAST and
        expected__startPos__nodeId ==eq0.startPos__nodeIdScheme and
        expected__stepsWithoutSimplify == stepsWithoutSimplify
        )
    if verbose:
        print(latexStr)
        print(eq0.functionsScheme)
        print(eq0.variablesScheme)
        print(eq0.primitivesScheme)
        print(eq0.totalNodeCountScheme)
        print('********')
        print('modifiedSchemeStr')
        print(eq0.schemeStr)
        print('modifiedAST')
        print(modifiedAST)
        print('before _startPos__nodeId')
        pp.pprint(before__startPos__nodeId)
        print('after startPos__nodeId')
        pp.pprint(eq0.startPos__nodeIdScheme)
        print('stepsWithoutSimplify')
        pp.pprint(stepsWithoutSimplify)




if __name__=='__main__':
    test__makeSubject2Input__addition0()
    test__makeSubject2Input__addition1()
    test__makeSubject2Input__subtraction0()
    test__makeSubject2Input__subtraction1()
    test__makeSubject2Input__multiply0()
    test__makeSubject2Input__multiply1()
    test__makeSubject2Input__divide0()
    test__makeSubject2Input__divide1()
    test__makeSubject2Input__exponent0()
    test__makeSubject2Input__exponent1()
    test__makeSubject2Input__nroot0()
    test__makeSubject2Input__nroot1()
    test__makeSubject2Input__log0()
    test__makeSubject2Input__log1()
    test__makeSubject1Input__arccosec()
    test__makeSubject1Input__arccosech()
    test__makeSubject1Input__arccos()
    test__makeSubject1Input__arccosh()
    test__makeSubject1Input__arccot()
    test__makeSubject1Input__arccoth()
    test__makeSubject1Input__arcsec()
    test__makeSubject1Input__arcsech()
    test__makeSubject1Input__arcsin()
    test__makeSubject1Input__arcsinh()
    test__makeSubject1Input__arctan()
    test__makeSubject1Input__arctanh()
    test__makeSubject1Input__cosec()
    test__makeSubject1Input__cosech()
    test__makeSubject1Input__cos()
    test__makeSubject1Input__cosh()
    test__makeSubject1Input__cot()
    test__makeSubject1Input__coth()
    test__makeSubject1Input__sec()
    test__makeSubject1Input__sech()
    test__makeSubject1Input__sin()
    test__makeSubject1Input__sinh()
    test__makeSubject1Input__tan()
    test__makeSubject1Input__tanh()

    test__leftSide__addition0()
    test__leftSide__addition1()
    test__leftSide__subtraction0()
    test__leftSide__subtraction1()
    test__leftSide__multiply0()
    test__leftSide__multiply1()
    test__leftSide__divide0()
    test__leftSide__divide1()
    test__leftSide__exponent0()
    test__leftSide__exponent1()
    test__leftSide__nroot0()
    test__leftSide__nroot1()
    test__leftSide__log0()
    test__leftSide__log1()
    test__leftSide__arccosec()
    test__leftSide__arccosech()
    test__leftSide__arccos()
    test__leftSide__arccosh()
    test__leftSide__arccot()
    test__leftSide__arccoth()
    test__leftSide__arcsec()
    test__leftSide__arcsech()
    test__leftSide__arcsin()
    test__leftSide__arcsinh()
    test__leftSide__arctan()
    test__leftSide__arctanh()
    test__leftSide__cosec()
    test__leftSide__cosech()
    test__leftSide__cos()
    test__leftSide__cosh()
    test__leftSide__cot()
    test__leftSide__coth()
    test__leftSide__sec()
    test__leftSide__sech()
    test__leftSide__sin()
    test__leftSide__sinh()
    test__leftSide__tan()
    test__leftSide__tanh()
