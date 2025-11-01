import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend


pp = pprint.PrettyPrinter(indent=4)

def bipartiteSearch__dc_twoResistor_series(verbose=False):
    list_equationStrs = [
        '(= I_{R_{0}} I_{DC_{1}})', 
        '(= I_{R_{0}} I_{R_{3}})', 
        '(= (+ (- (- 0 V_{R_{0}}) V_{R_{3}}) V_{DC_{1}}) 0)', 
        '(= (/ V_{R_{0}} I_{R_{0}}) R_{R_{0}})', 
        '(= (/ V_{DC_{1}} I_{DC_{1}}) R_{DC_{1}})', 
        '(= (/ V_{R_{3}} I_{R_{3}}) R_{R_{3}})'
    ]
    list_variables = [
        'I_{R_{0}}', #0
        'I_{DC_{1}}', #1
        'I_{R_{3}}', #2
        'V_{R_{0}}', #3
        'V_{R_{3}}', #4
        'V_{DC_{1}}', #5
        'R_{R_{0}}', #6
        'R_{DC_{1}}', #7
        'R_{R_{3}}' #8
    ]

    equationVariables_bg = {1: [0, 3, 9], 0: [1, 2], 2: [0, 11], 3: [1, 4], 4: [3, 13], 6: [5, 9], 5: [6, 7, 8], 7: [5, 13], 8: [5, 11], 9: [6, 1, 10], 10: [9], 11: [8, 2, 12], 12: [11], 13: [7, 4, 14], 14: [13]}

    vertexId__equationVariableId = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 5, 9: 3, 10: 6, 11: 4, 12: 7, 13: 5, 14: 8}

    equationId__vertexId = {0: 0, 1: 3, 2: 5, 3: 9, 4: 11, 5: 13}
    variableId__vertexId = {0: 1, 1: 2, 2: 4, 3: 6, 4: 7, 5: 8, 6: 10, 7: 12, 8: 14}
    type__list_vertexIds = {'equation': [0, 3, 5, 9, 11, 13], 'variable': [1, 2, 4, 6, 7, 8, 10, 12, 14]}
    equationKey = 'equation'
    variableKey = 'variable'
    dependentVariableId = 7
    list_independentVariableIds = [6, 8]
    list_equations = list(map(lambda equationStr: Equation(equationStr=equationStr, parserName='scheme'), list_equationStrs))
    #######################################################
    substitutionPath, equationVertexId__tuple_variableVertexIdContaining___NEW = Recommend.bipartiteSearch(
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        variableId__vertexId,
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds)
    expected_substitutionPath = [5, 6, 9, 8, 11, 7, 13, 2, 0, 4, 3]
    expected_equationVertexId__tuple_variableVertexIdContaining = {15: (1, 7, 8, 10), 16: (1, 2, 7, 10, 12), 17: (2, 7, 10, 12), 18: (2, 4, 7, 10, 12), 19: (1, 7, 10, 12), 20: (1, 4, 7, 10, 12), 21: (1, 2, 4, 10, 12, 14), 22: (1, 2, 10, 12), 23: (1, 2, 4, 10, 12), 24: (2, 4, 10, 12, 14), 25: (2, 4, 7, 10, 12, 14), 26: (1, 4, 10, 12, 14), 27: (1, 4, 7, 10, 12, 14), 28: (1, 2, 10, 12, 14), 29: (1, 2, 7, 10, 12, 14), 30: (1, 10, 12, 14), 31: (1, 7, 10, 12, 14)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', substitutionPath == expected_substitutionPath)
    if verbose:
        # print('listOfCollectedEquations')
        # pp.pprint(list(map(lambda equation: equation._eqs, listOfCollectedEquations)))
        # print('listOfVariables')
        # pp.pprint(listOfVariables)
        # print('vertexId__equationVariableId')
        # pp.pprint(vertexId__equationVariableId)
        # print('equationVariables_g')
        # pp.pprint(equationVariables_g)
        # print('type__list_vertexIds')
        # pp.pprint(type__list_vertexIds)
        print('substitutionPath')
        print(substitutionPath)
        print('equationVertexId__tuple_variableVertexIdContaining___NEW')
        print(equationVertexId__tuple_variableVertexIdContaining___NEW)


    
def bipartiteSearch__dc_twoResistor_parallel(verbose=False):
    # from foundation.automat.core.equation import Equation
    list_equationStrs = [
    '(= (+ (+ (- 0 I_{DC_{8}}) I_{R_{0}}) I_{R_{3}}) 0)', 
    '(= (+ (- 0 V_{R_{0}}) V_{DC_{8}}) 0)', 
    '(= (- V_{DC_{8}} V_{R_{3}}) 0)', 
    '(= (/ V_{R_{0}} I_{R_{0}}) R_{R_{0}})', 
    '(= (/ V_{R_{3}} I_{R_{3}}) R_{R_{3}})', 
    '(= (/ V_{DC_{8}} I_{DC_{8}}) R_{DC_{8}})'
    ]
    list_variables = [
    'I_{DC_{8}}', 
    'I_{R_{0}}', 
    'I_{R_{3}}', 
    'V_{R_{0}}', 
    'V_{DC_{8}}', 
    'V_{R_{3}}', 
    'R_{R_{0}}', 
    'R_{R_{3}}', 
    'R_{DC_{8}}'
    ]
    equationVariables_bg = {1: [0, 13], 0: [1, 2, 3], 2: [0, 9], 3: [0, 11], 5: [4, 9], 4: [5, 6], 6: [4, 7, 13], 7: [6, 8], 8: [7, 11], 9: [5, 2, 10], 10: [9], 11: [8, 3, 12], 12: [11], 13: [6, 1, 14], 14: [13]}
    vertexId__equationVariableId = {0: 0, 1: 0, 2: 1, 3: 2, 4: 1, 5: 3, 6: 4, 7: 2, 8: 5, 9: 3, 10: 6, 11: 4, 12: 7, 13: 5, 14: 8}
    equationId__vertexId = {0: 0, 1: 4, 2: 7, 3: 9, 4: 11, 5: 13}
    variableId__vertexId = {0: 1, 1: 2, 2: 3, 3: 5, 4: 6, 5: 8, 6: 10, 7: 12, 8: 14}
    type__list_vertexIds = {'equation': [0, 4, 7, 9, 11, 13], 'variable': [1, 2, 3, 5, 6, 8, 10, 12, 14]}
    equationKey = 'equation'
    variableKey = 'variable'
    dependentVariableId = 8
    list_independentVariableIds = [6, 7]
    list_equations = list(map(lambda equationStr: Equation(equationStr=equationStr, parserName='scheme'), list_equationStrs))
    #######################################################
    substitutionPath, equationVertexId__tuple_variableVertexIdContaining___NEW = Recommend.bipartiteSearch(
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        variableId__vertexId,
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds)
    expected_substitutionPath = [0, 3, 11, 2, 9, 1, 13, 8, 7, 5, 4]
    expected_equationVertexId__tuple_variableVertexIdContaining = {15: (2, 3, 6, 14), 16: (3, 5, 6, 10, 14), 17: (5, 6, 8, 10, 12, 14), 18: (5, 6, 10, 12, 14), 19: (6, 8, 10, 12, 14), 20: (6, 10, 12, 14)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', substitutionPath == expected_substitutionPath)
    if verbose:
        # print('listOfCollectedEquations')
        # pp.pprint(list(map(lambda equation: equation._eqs, listOfCollectedEquations)))
        # print('listOfVariables')
        # pp.pprint(listOfVariables)
        # print('vertexId__equationVariableId')
        # pp.pprint(vertexId__equationVariableId)
        # print('equationVariables_g')
        # pp.pprint(equationVariables_g)
        # print('type__list_vertexIds')
        # pp.pprint(type__list_vertexIds)
        print('substitutionPath')
        print(substitutionPath)
        print('equationVertexId__tuple_variableVertexIdContaining___NEW')
        print(equationVertexId__tuple_variableVertexIdContaining___NEW)




    
def bipartiteSearch__ac_twoCapacitor_parallel(verbose=False):
    # from foundation.automat.core.equation import Equation
    list_equationStrs = ['(= I_{C_{0}} (* C_{C_{0}} (/ (* d V_{C_{0}}) (* d t))))', '(= I_{C_{3}} (* C_{C_{3}} (/ (* d V_{C_{3}}) (* d t))))', '(= I_{AC_{8}} (* C_{AC_{8}} (/ (* d V_{AC_{8}}) (* d t))))', '(= (+ (+ (- 0 I_{AC_{8}}) I_{C_{0}}) I_{C_{3}}) 0)', '(= (+ (- 0 V_{C_{0}}) V_{AC_{8}}) 0)', '(= (- V_{AC_{8}} V_{C_{3}}) 0)']
    list_variables = ['I_{C_{0}}', 'C_{C_{0}}', 'd', 'V_{C_{0}}', 't', 'I_{C_{3}}', 'C_{C_{3}}', 'V_{C_{3}}', 'I_{AC_{8}}', 'C_{AC_{8}}', 'V_{AC_{8}}']
    equationVariables_bg = {1: [0, 14], 0: [1, 2, 3, 4, 5], 2: [0], 3: [0, 6, 10], 4: [0, 15], 5: [0, 6, 10], 7: [6, 14], 6: [7, 8, 3, 9, 5], 8: [6], 9: [6, 16], 11: [10, 14], 10: [11, 12, 3, 13, 5], 12: [10], 13: [10, 15, 16], 14: [11, 1, 7], 15: [4, 13], 16: [13, 9]}
    vertexId__equationVariableId = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 1, 7: 5, 8: 6, 9: 7, 10: 2, 11: 8, 12: 9, 13: 10, 14: 3, 15: 4, 16: 5}
    equationId__vertexId = {0: 0, 1: 6, 2: 10, 3: 14, 4: 15, 5: 16}
    variableId__vertexId = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 7, 6: 8, 7: 9, 8: 11, 9: 12, 10: 13}
    type__list_vertexIds = {'equation': [0, 6, 10, 14, 15, 16], 'variable': [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13]}
    equationKey = 'equation'
    variableKey = 'variable'
    dependentVariableId = 9
    list_independentVariableIds = [1, 6]
    list_equations = list(map(lambda equationStr: Equation(equationStr=equationStr, parserName='scheme'), list_equationStrs))
    #######################################################
    substitutionPath, equationVertexId__tuple_variableVertexIdContaining___NEW = Recommend.bipartiteSearch(
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        variableId__vertexId,
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds)
    expected_substitutionPath = [0, 3, 11, 2, 9, 1, 13, 8, 7, 5, 4]
    expected_equationVertexId__tuple_variableVertexIdContaining = {15: (2, 3, 6, 14), 16: (3, 5, 6, 10, 14), 17: (5, 6, 8, 10, 12, 14), 18: (5, 6, 10, 12, 14), 19: (6, 8, 10, 12, 14), 20: (6, 10, 12, 14)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', substitutionPath == expected_substitutionPath)
    if verbose:
        # print('listOfCollectedEquations')
        # pp.pprint(list(map(lambda equation: equation._eqs, listOfCollectedEquations)))
        # print('listOfVariables')
        # pp.pprint(listOfVariables)
        # print('vertexId__equationVariableId')
        # pp.pprint(vertexId__equationVariableId)
        # print('equationVariables_g')
        # pp.pprint(equationVariables_g)
        # print('type__list_vertexIds')
        # pp.pprint(type__list_vertexIds)
        print('substitutionPath')
        print(substitutionPath)
        print('equationVertexId__tuple_variableVertexIdContaining___NEW')
        print(equationVertexId__tuple_variableVertexIdContaining___NEW)



    
def bipartiteSearch__ac_twoCapacitor_series(verbose=False):
    # from foundation.automat.core.equation import Equation
    list_equationStrs = ['(= I_{C_{0}} (* C_{C_{0}} (/ (* d V_{C_{0}}) (* d t))))', '(= I_{C_{3}} (* C_{C_{3}} (/ (* d V_{C_{3}}) (* d t))))', '(= I_{AC_{1}} (* C_{AC_{1}} (/ (* d V_{AC_{1}}) (* d t))))', '(= I_{C_{0}} I_{AC_{1}})', '(= I_{C_{0}} I_{C_{3}})', '(= (+ (- (- 0 V_{C_{0}}) V_{C_{3}}) V_{AC_{1}}) 0)']
    list_variables = ['I_{C_{0}}', 'C_{C_{0}}', 'd', 'V_{C_{0}}', 't', 'I_{C_{3}}', 'C_{C_{3}}', 'V_{C_{3}}', 'I_{AC_{1}}', 'C_{AC_{1}}', 'V_{AC_{1}}']
    equationVariables_bg = {1: [0, 14, 15], 0: [1, 2, 3, 4, 5], 2: [0], 3: [0, 6, 10], 4: [0, 16], 5: [0, 6, 10], 7: [6, 15], 6: [7, 8, 3, 9, 5], 8: [6], 9: [6, 16], 11: [10, 14], 10: [11, 12, 3, 13, 5], 12: [10], 13: [10, 16], 14: [1, 11], 15: [1, 7], 16: [4, 9, 13]}
    vertexId__equationVariableId = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 1, 7: 5, 8: 6, 9: 7, 10: 2, 11: 8, 12: 9, 13: 10, 14: 3, 15: 4, 16: 5}
    equationId__vertexId = {0: 0, 1: 6, 2: 10, 3: 14, 4: 15, 5: 16}
    variableId__vertexId = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 7, 6: 8, 7: 9, 8: 11, 9: 12, 10: 13}
    type__list_vertexIds = {'equation': [0, 6, 10, 14, 15, 16], 'variable': [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13]}
    equationKey = 'equation'
    variableKey = 'variable'
    dependentVariableId = 9
    list_independentVariableIds = [1, 6]
    list_equations = list(map(lambda equationStr: Equation(equationStr=equationStr, parserName='scheme'), list_equationStrs))
    #######################################################
    substitutionPath, equationVertexId__tuple_variableVertexIdContaining___NEW = Recommend.bipartiteSearch(
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        variableId__vertexId,
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds)
    expected_substitutionPath = [0, 3, 11, 2, 9, 1, 13, 8, 7, 5, 4]
    expected_equationVertexId__tuple_variableVertexIdContaining = {15: (2, 3, 6, 14), 16: (3, 5, 6, 10, 14), 17: (5, 6, 8, 10, 12, 14), 18: (5, 6, 10, 12, 14), 19: (6, 8, 10, 12, 14), 20: (6, 10, 12, 14)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', substitutionPath == expected_substitutionPath)
    if verbose:
        # print('listOfCollectedEquations')
        # pp.pprint(list(map(lambda equation: equation._eqs, listOfCollectedEquations)))
        # print('listOfVariables')
        # pp.pprint(listOfVariables)
        # print('vertexId__equationVariableId')
        # pp.pprint(vertexId__equationVariableId)
        # print('equationVariables_g')
        # pp.pprint(equationVariables_g)
        # print('type__list_vertexIds')
        # pp.pprint(type__list_vertexIds)
        print('substitutionPath')
        print(substitutionPath)
        print('equationVertexId__tuple_variableVertexIdContaining___NEW')
        print(equationVertexId__tuple_variableVertexIdContaining___NEW)

###########################################

    
def bipartiteSearch__ac_twoInductor_parallel(verbose=False):
    # from foundation.automat.core.equation import Equation
    list_equationStrs = ['(= V_{I_{0}} (* L_{I_{0}} (/ (* d I_{I_{0}}) (* d t))))', '(= V_{I_{3}} (* L_{I_{3}} (/ (* d I_{I_{3}}) (* d t))))', '(= V_{AC_{8}} (* L_{AC_{8}} (/ (* d I_{AC_{8}}) (* d t))))', '(= (+ (+ (- 0 I_{AC_{8}}) I_{I_{0}}) I_{I_{3}}) 0)', '(= (+ (- 0 V_{I_{0}}) V_{AC_{8}}) 0)', '(= (- V_{AC_{8}} V_{I_{3}}) 0)']
    list_variables = ['V_{I_{0}}', 'L_{I_{0}}', 'd', 'I_{I_{0}}', 't', 'V_{I_{3}}', 'L_{I_{3}}', 'I_{I_{3}}', 'V_{AC_{8}}', 'L_{AC_{8}}', 'I_{AC_{8}}']
    equationVariables_bg = {1: [0, 15], 0: [1, 2, 3, 4, 5], 2: [0], 3: [0, 6, 10], 4: [0, 14], 5: [0, 6, 10], 7: [6, 16], 6: [7, 8, 3, 9, 5], 8: [6], 9: [6, 14], 11: [10, 15, 16], 10: [11, 12, 3, 13, 5], 12: [10], 13: [10, 14], 14: [13, 4, 9], 15: [1, 11], 16: [11, 7]}
    vertexId__equationVariableId = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 1, 7: 5, 8: 6, 9: 7, 10: 2, 11: 8, 12: 9, 13: 10, 14: 3, 15: 4, 16: 5}
    equationId__vertexId = {0: 0, 1: 6, 2: 10, 3: 14, 4: 15, 5: 16}
    variableId__vertexId = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 7, 6: 8, 7: 9, 8: 11, 9: 12, 10: 13}
    type__list_vertexIds = {'equation': [0, 6, 10, 14, 15, 16], 'variable': [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13]}
    equationKey = 'equation'
    variableKey = 'variable'
    dependentVariableId = 9
    list_independentVariableIds = [1, 6]
    list_equations = list(map(lambda equationStr: Equation(equationStr=equationStr, parserName='scheme'), list_equationStrs))
    #######################################################
    substitutionPath, equationVertexId__tuple_variableVertexIdContaining___NEW = Recommend.bipartiteSearch(
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        variableId__vertexId,
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds)
    expected_substitutionPath = [0, 3, 11, 2, 9, 1, 13, 8, 7, 5, 4]
    expected_equationVertexId__tuple_variableVertexIdContaining = {15: (2, 3, 6, 14), 16: (3, 5, 6, 10, 14), 17: (5, 6, 8, 10, 12, 14), 18: (5, 6, 10, 12, 14), 19: (6, 8, 10, 12, 14), 20: (6, 10, 12, 14)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', substitutionPath == expected_substitutionPath)
    if verbose:
        # print('listOfCollectedEquations')
        # pp.pprint(list(map(lambda equation: equation._eqs, listOfCollectedEquations)))
        # print('listOfVariables')
        # pp.pprint(listOfVariables)
        # print('vertexId__equationVariableId')
        # pp.pprint(vertexId__equationVariableId)
        # print('equationVariables_g')
        # pp.pprint(equationVariables_g)
        # print('type__list_vertexIds')
        # pp.pprint(type__list_vertexIds)
        print('substitutionPath')
        print(substitutionPath)
        print('equationVertexId__tuple_variableVertexIdContaining___NEW')
        print(equationVertexId__tuple_variableVertexIdContaining___NEW)



    
def bipartiteSearch__ac_twoInductor_series(verbose=False):
    # from foundation.automat.core.equation import Equation
    list_equationStrs = ['(= V_{I_{0}} (* L_{I_{0}} (/ (* d I_{I_{0}}) (* d t))))', '(= V_{I_{3}} (* L_{I_{3}} (/ (* d I_{I_{3}}) (* d t))))', '(= V_{AC_{1}} (* L_{AC_{1}} (/ (* d I_{AC_{1}}) (* d t))))', '(= I_{I_{0}} I_{AC_{1}})', '(= I_{I_{0}} I_{I_{3}})', '(= (+ (- (- 0 V_{I_{0}}) V_{I_{3}}) V_{AC_{1}}) 0)']
    list_variables = ['V_{I_{0}}', 'L_{I_{0}}', 'd', 'I_{I_{0}}', 't', 'V_{I_{3}}', 'L_{I_{3}}', 'I_{I_{3}}', 'V_{AC_{1}}', 'L_{AC_{1}}', 'I_{AC_{1}}']
    equationVariables_bg = {1: [0, 16], 0: [1, 2, 3, 4, 5], 2: [0], 3: [0, 6, 10], 4: [0, 14, 15], 5: [0, 6, 10], 7: [6, 16], 6: [7, 8, 3, 9, 5], 8: [6], 9: [6, 15], 11: [10, 16], 10: [11, 12, 3, 13, 5], 12: [10], 13: [10, 14], 14: [4, 13], 15: [4, 9], 16: [1, 7, 11]}
    vertexId__equationVariableId = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 1, 7: 5, 8: 6, 9: 7, 10: 2, 11: 8, 12: 9, 13: 10, 14: 3, 15: 4, 16: 5}
    equationId__vertexId = {0: 0, 1: 6, 2: 10, 3: 14, 4: 15, 5: 16}
    variableId__vertexId = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 7, 6: 8, 7: 9, 8: 11, 9: 12, 10: 13}
    type__list_vertexIds = {'equation': [0, 6, 10, 14, 15, 16], 'variable': [1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 13]}
    equationKey = 'equation'
    variableKey = 'variable'
    dependentVariableId = 9
    list_independentVariableIds = [1, 6]
    list_equations = list(map(lambda equationStr: Equation(equationStr=equationStr, parserName='scheme'), list_equationStrs))
    #######################################################
    substitutionPath, equationVertexId__tuple_variableVertexIdContaining___NEW = Recommend.bipartiteSearch(
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        variableId__vertexId,
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds)
    expected_substitutionPath = [0, 3, 11, 2, 9, 1, 13, 8, 7, 5, 4]
    expected_equationVertexId__tuple_variableVertexIdContaining = {15: (2, 3, 6, 14), 16: (3, 5, 6, 10, 14), 17: (5, 6, 8, 10, 12, 14), 18: (5, 6, 10, 12, 14), 19: (6, 8, 10, 12, 14), 20: (6, 10, 12, 14)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', substitutionPath == expected_substitutionPath)
    if verbose:
        # print('listOfCollectedEquations')
        # pp.pprint(list(map(lambda equation: equation._eqs, listOfCollectedEquations)))
        # print('listOfVariables')
        # pp.pprint(listOfVariables)
        # print('vertexId__equationVariableId')
        # pp.pprint(vertexId__equationVariableId)
        # print('equationVariables_g')
        # pp.pprint(equationVariables_g)
        # print('type__list_vertexIds')
        # pp.pprint(type__list_vertexIds)
        print('substitutionPath')
        print(substitutionPath)
        print('equationVertexId__tuple_variableVertexIdContaining___NEW')
        print(equationVertexId__tuple_variableVertexIdContaining___NEW)

###########################################
    
def bipartiteSearch__dc_twoDiode_parallel(verbose=False):
    # from foundation.automat.core.equation import Equation
    list_equationStrs = ['(= (+ (+ (- 0 I_{DC_{8}}) I_{D_{0}}) I_{D_{3}}) 0)', '(= (+ (- 0 V_{D_{0}}) V_{DC_{8}}) 0)', '(= (- V_{DC_{8}} V_{D_{3}}) 0)', '(= (/ V_{DC_{8}} I_{DC_{8}}) R_{DC_{8}})', '(= I_{D_{0}} (* I_{D^C_{0}} (- (^ e (/ V_{D_{0}} (/ (* (* n_{D_{0}} k) T_{D_{0}}) q))) 1)))', '(= I_{D_{3}} (* I_{D^C_{3}} (- (^ e (/ V_{D_{3}} (/ (* (* n_{D_{3}} k) T_{D_{3}}) q))) 1)))']
    list_variables = ['I_{DC_{8}}', 'I_{D_{0}}', 'I_{D_{3}}', 'V_{D_{0}}', 'V_{DC_{8}}', 'V_{D_{3}}', 'R_{DC_{8}}', 'I_{D^C_{0}}', 'n_{D_{0}}', 'k', 'T_{D_{0}}', 'q', 'I_{D^C_{3}}', 'n_{D_{3}}', 'T_{D_{3}}']
    equationVariables_bg = {1: [0, 9], 0: [1, 2, 3], 2: [0, 11], 3: [0, 17], 5: [4, 11], 4: [5, 6], 6: [4, 7, 9], 7: [6, 8], 8: [7, 17], 9: [6, 1, 10], 10: [9], 11: [2, 12, 5, 13, 14, 15, 16], 12: [11], 13: [11], 14: [11, 17], 15: [11], 16: [11, 17], 17: [3, 18, 8, 19, 14, 20, 16], 18: [17], 19: [17], 20: [17]}
    vertexId__equationVariableId = 0: 0, 1: 0, 2: 1, 3: 2, 4: 1, 5: 3, 6: 4, 7: 2, 8: 5, 9: 3, 10: 6, 11: 4, 12: 7, 13: 8, 14: 9, 15: 10, 16: 11, 17: 5, 18: 12, 19: 13, 20: 14}
    equationId__vertexId = {0: 0, 1: 4, 2: 7, 3: 9, 4: 11, 5: 17}
    variableId__vertexId = {0: 1, 1: 2, 2: 3, 3: 5, 4: 6, 5: 8, 6: 10, 7: 12, 8: 13, 9: 14, 10: 15, 11: 16, 12: 18, 13: 19, 14: 20}
    type__list_vertexIds = {'equation': [0, 4, 7, 9, 11, 17], 'variable': [1, 2, 3, 5, 6, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20]}
    equationKey = 'equation'
    variableKey = 'variable'
    dependentVariableId = 4
    list_independentVariableIds = [3, 5]
    list_equations = list(map(lambda equationStr: Equation(equationStr=equationStr, parserName='scheme'), list_equationStrs))
    #######################################################
    substitutionPath, equationVertexId__tuple_variableVertexIdContaining___NEW = Recommend.bipartiteSearch(
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        variableId__vertexId,
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds)
    expected_substitutionPath = [0, 3, 11, 2, 9, 1, 13, 8, 7, 5, 4]
    expected_equationVertexId__tuple_variableVertexIdContaining = {15: (2, 3, 6, 14), 16: (3, 5, 6, 10, 14), 17: (5, 6, 8, 10, 12, 14), 18: (5, 6, 10, 12, 14), 19: (6, 8, 10, 12, 14), 20: (6, 10, 12, 14)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', substitutionPath == expected_substitutionPath)
    if verbose:
        # print('listOfCollectedEquations')
        # pp.pprint(list(map(lambda equation: equation._eqs, listOfCollectedEquations)))
        # print('listOfVariables')
        # pp.pprint(listOfVariables)
        # print('vertexId__equationVariableId')
        # pp.pprint(vertexId__equationVariableId)
        # print('equationVariables_g')
        # pp.pprint(equationVariables_g)
        # print('type__list_vertexIds')
        # pp.pprint(type__list_vertexIds)
        print('substitutionPath')
        print(substitutionPath)
        print('equationVertexId__tuple_variableVertexIdContaining___NEW')
        print(equationVertexId__tuple_variableVertexIdContaining___NEW)



    
def bipartiteSearch__dc_twoDiode_series(verbose=False):
    # from foundation.automat.core.equation import Equation
    list_equationStrs = ['(= I_{D_{0}} I_{DC_{1}})', '(= I_{D_{0}} I_{D_{3}})', '(= (+ (- (- 0 V_{D_{0}}) V_{D_{3}}) V_{DC_{1}}) 0)', '(= (/ V_{DC_{1}} I_{DC_{1}}) R_{DC_{1}})', '(= I_{D_{0}} (* I_{D^C_{0}} (- (^ e (/ V_{D_{0}} (/ (* (* n_{D_{0}} k) T_{D_{0}}) q))) 1)))', '(= I_{D_{3}} (* I_{D^C_{3}} (- (^ e (/ V_{D_{3}} (/ (* (* n_{D_{3}} k) T_{D_{3}}) q))) 1)))']
    list_variables = ['I_{D_{0}}', 'I_{DC_{1}}', 'I_{D_{3}}', 'V_{D_{0}}', 'V_{D_{3}}', 'V_{DC_{1}}', 'R_{DC_{1}}', 'I_{D^C_{0}}', 'n_{D_{0}}', 'k', 'T_{D_{0}}', 'q', 'I_{D^C_{3}}', 'n_{D_{3}}', 'T_{D_{3}}']
    equationVariables_bg = {1: [0, 3, 11], 0: [1, 2], 2: [0, 9], 3: [1, 4], 4: [3, 17], 6: [5, 11], 5: [6, 7, 8], 7: [5, 17], 8: [5, 9], 9: [8, 2, 10], 10: [9], 11: [1, 12, 6, 13, 14, 15, 16], 12: [11], 13: [11], 14: [11, 17], 15: [11], 16: [11, 17], 17: [4, 18, 7, 19, 14, 20, 16], 18: [17], 19: [17], 20: [17]}
    vertexId__equationVariableId = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 5, 9: 3, 10: 6, 11: 4, 12: 7, 13: 8, 14: 9, 15: 10, 16: 11, 17: 5, 18: 12, 19: 13, 20: 14}
    equationId__vertexId = {0: 0, 1: 3, 2: 5, 3: 9, 4: 11, 5: 17}
    variableId__vertexId = {0: 1, 1: 2, 2: 4, 3: 6, 4: 7, 5: 8, 6: 10, 7: 12, 8: 13, 9: 14, 10: 15, 11: 16, 12: 18, 13: 19, 14: 20}
    type__list_vertexIds = {'equation': [0, 3, 5, 9, 11, 17], 'variable': [1, 2, 4, 6, 7, 8, 10, 12, 13, 14, 15, 16, 18, 19, 20]}
    equationKey = 'equation'
    variableKey = 'variable'
    dependentVariableId = 1
    list_independentVariableIds = [0, 2]
    list_equations = list(map(lambda equationStr: Equation(equationStr=equationStr, parserName='scheme'), list_equationStrs))
    #######################################################
    substitutionPath, equationVertexId__tuple_variableVertexIdContaining___NEW = Recommend.bipartiteSearch(
        list_equations, 
        list_variables, 
        equationVariables_bg, 
        vertexId__equationVariableId, 
        equationId__vertexId, 
        variableId__vertexId,
        type__list_vertexIds, 
        equationKey, 
        variableKey, 
        dependentVariableId, 
        list_independentVariableIds)
    expected_substitutionPath = [0, 3, 11, 2, 9, 1, 13, 8, 7, 5, 4]
    expected_equationVertexId__tuple_variableVertexIdContaining = {15: (2, 3, 6, 14), 16: (3, 5, 6, 10, 14), 17: (5, 6, 8, 10, 12, 14), 18: (5, 6, 10, 12, 14), 19: (6, 8, 10, 12, 14), 20: (6, 10, 12, 14)}

    print(inspect.currentframe().f_code.co_name, ' PASSED? ', substitutionPath == expected_substitutionPath)
    if verbose:
        # print('listOfCollectedEquations')
        # pp.pprint(list(map(lambda equation: equation._eqs, listOfCollectedEquations)))
        # print('listOfVariables')
        # pp.pprint(listOfVariables)
        # print('vertexId__equationVariableId')
        # pp.pprint(vertexId__equationVariableId)
        # print('equationVariables_g')
        # pp.pprint(equationVariables_g)
        # print('type__list_vertexIds')
        # pp.pprint(type__list_vertexIds)
        print('substitutionPath')
        print(substitutionPath)
        print('equationVertexId__tuple_variableVertexIdContaining___NEW')
        print(equationVertexId__tuple_variableVertexIdContaining___NEW)

######################################################################################


if __name__=='__main__':
    # bipartiteSearch__dc_twoResistor_series(True)
    # bipartiteSearch__dc_twoResistor_parallel(True)
    bipartiteSearch__ac_twoCapacitor_parallel(True)
    # bipartiteSearch__ac_twoCapacitor_series(True)
    # bipartiteSearch__ac_twoInductor_parallel(True)
    # bipartiteSearch__ac_twoInductor_series(True)
    # bipartiteSearch__dc_twoDiode_parallel(True)
    # bipartiteSearch__dc_twoDiode_series(True)