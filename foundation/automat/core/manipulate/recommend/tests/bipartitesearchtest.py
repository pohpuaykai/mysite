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



if __name__=='__main__':
    # bipartiteSearch__dc_twoResistor_series(True)
    bipartiteSearch__dc_twoResistor_parallel(True)