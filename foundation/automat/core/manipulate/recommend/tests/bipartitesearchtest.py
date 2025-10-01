import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend


pp = pprint.PrettyPrinter(indent=4)

def bipartiteSearch__dc_twoResistor_series(verbose=False):
    list_equationStrs = [
        '(= I_{R_{0}} I_{DC_{1}})', 
        '(= I_{R_{0}} I_{R_{3}})', #i don't have to use this equation, how do i know? my current early termination is not good enough, this equivalent is not present in the dc_parallel, maybe alter KCLequationFinder with linear_independence??<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        '(= I_{DC_{1}} I_{R_{3}})', 
        '(= (+ (- (- 0 V_{R_{0}}) V_{R_{3}}) V_{DC_{1}}) 0)', 
        '(= (/ V_{R_{0}} I_{R_{0}}) R_{R_{0}})', 
        '(= (/ V_{DC_{1}} I_{DC_{1}}) R_{DC_{1}})', 
        '(= (/ V_{R_{3}} I_{R_{3}}) R_{R_{3}})'
    ]
    list_variables = [
    'I_{R_{0}}', 
    'I_{DC_{1}}', 
    'I_{R_{3}}', 
    'V_{R_{0}}', 
    'V_{R_{3}}', 
    'V_{DC_{1}}', 
    'R_{R_{0}}', 
    'R_{DC_{1}}', 
    'R_{R_{3}}']
    equationVariables_bg = {1: [0, 3, 10], 0: [1, 2], 2: [0, 5, 12], 3: [1, 4], 4: [3, 5, 14], 5: [2, 4], 7: [6, 10], 6: [7, 8, 9], 8: [6, 14], 9: [6, 12], 10: [7, 1, 11], 11: [10], 12: [9, 2, 13], 13: [12], 14: [8, 4, 15], 15: [14]}
    vertexId__equationVariableId = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4, 9: 5, 10: 4, 11: 6, 12: 5, 13: 7, 14: 6, 15: 8}
    equationId__vertexId = {0: 0, 1: 3, 2: 5, 3: 6, 4: 10, 5: 12, 6: 14}
    variableId__vertexId = {0: 1, 1: 2, 2: 4, 3: 7, 4: 8, 5: 9, 6: 11, 7: 13, 8: 15}
    type__list_vertexIds = {'equation': [0, 3, 5, 6, 10, 12, 14], 'variable': [1, 2, 4, 7, 8, 9, 11, 13, 15]}
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
        list_independentVariableIds, verbose=verbose)
    expected_substitutionPath = None
    expected_equationVertexId__tuple_variableVertexIdContaining = None

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
    '(= (/ V_{DC_{8}} I_{DC_{8}}) R_{DC_{8}})']
    list_variables = ['I_{DC_{8}}', 'I_{R_{0}}', 'I_{R_{3}}', 'V_{R_{0}}', 'V_{DC_{8}}', 'V_{R_{3}}', 'R_{R_{0}}', 'R_{R_{3}}', 'R_{DC_{8}}']
    equationVariables_bg = {1: [0, 13], 0: [1, 2, 3], 2: [0, 9], 3: [0, 11], 5: [4, 9], 4: [5, 6], 6: [4, 7, 13], 7: [6, 8], 8: [7, 11], 9: [5, 2, 10], 10: [9], 11: [8, 3, 12], 12: [11], 13: [6, 1, 14], 14: [13]}
    vertexId__equationVariableId = {0: 0, 1: 0, 2: 1, 3: 2, 4: 1, 5: 3, 6: 4, 7: 2, 8: 5, 9: 3, 10: 6, 11: 4, 12: 7, 13: 5, 14: 8}
    equationId__vertexId = {0: 0, 1: 4, 2: 7, 3: 9, 4: 11, 5: 13} # during creation of new equation, this must also be updated
    variableId__vertexId = {0: 1, 1: 2, 2: 3, 3: 5, 4: 6, 5: 8, 6: 10, 7: 12, 8: 14} # this need not be updated, because no new variables are created, and so the maximum number of equations creatable, is 2^{numberOfVariables}
    type__list_vertexIds = {'equation': [0, 4, 7, 9, 11, 13], 'variable': [1, 2, 3, 5, 6, 8, 10, 12, 14]} # during creation of new equation, this must also be updated
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
        list_independentVariableIds, verbose=verbose)
    expected_substitutionPath = [0, 3, 11, 2, 9, 1, 13, 8, 7, 5, 4]
    expected_equationVertexId__tuple_variableVertexIdContaining = {#it took such a long way... might it be shortened with simplify? but will the 'shorter' way be faster?
    15: (2, 3, 6, 14),
    16: (1, 5, 6, 10, 14),
    17: (2, 6, 10),
    18: (2, 5, 8, 10),
    19: (1, 6, 8, 12, 14),
    20: (3, 6, 12),
    21: (2, 3, 5, 10, 12),
    22: (3, 5, 8, 12),
    23: (1, 3, 5, 8, 10, 12, 14),
    24: (2, 3, 8, 10, 12),
    25: (1, 5, 14),
    26: (1, 8, 14),
    27: (1, 5, 10, 14),
    28: (1, 2, 10, 14),
    29: (1, 8, 12, 14),
    30: (1, 3, 12, 14),
    31: (1, 3, 5, 10),
    32: (1, 3, 6, 14),
    33: (1, 3, 6, 10),
    34: (1, 3, 5, 8, 10),
    35: (1, 3, 5, 10, 12),
    36: (1, 3, 8, 10, 12),
    37: (1, 3, 10, 14),
    38: (2, 5, 6, 10, 14),
    39: (2, 5, 6, 8, 10, 12, 14),
    40: (2, 3, 5, 8, 10, 12, 14),
    41: (2, 5, 10, 14),
    42: (2, 5, 8, 10, 14),
    43: (2, 5, 8, 10, 12, 14),
    44: (2, 3, 5, 10, 12, 14),
    45: (2, 3, 5, 6, 10, 14),
    46: (2, 3, 5, 6, 10),
    47: (2, 3, 5, 8, 10),
    48: (2, 3, 5, 8, 10, 12),
    49: (2, 3, 5, 10, 14),
    50: (1, 6, 10, 14),
    51: (1, 2, 6, 8, 10, 14),
    52: (1, 2, 3, 6, 10, 12, 14),
    53: (1, 3, 6, 8, 12, 14),
    54: (1, 3, 6, 8, 10, 12, 14),
    55: (1, 3, 6, 8, 10, 14),
    56: (1, 3, 6, 10, 12, 14),
    57: (1, 2, 6, 8, 10, 12, 14),
    58: (1, 2, 3, 6, 8, 10, 12, 14),
    59: (1, 2, 6, 10, 14),
    60: (1, 2, 3, 6, 10, 14),
    61: (1, 2, 3, 6, 8, 10, 14),
    62: (1, 2, 3, 14),
    63: (1, 3, 14),
    64: (1, 2, 5, 8, 10, 12, 14),
    65: (1, 2, 3, 5, 10, 14),
    66: (1, 10, 14),
    67: (1, 2, 8, 10, 14),
    68: (1, 2, 3, 10, 12, 14),
    69: (1, 3, 8, 12, 14),
    70: (1, 3, 8, 10, 12, 14),
    71: (1, 3, 8, 10, 14),
    72: (1, 3, 10, 12, 14),
    73: (1, 2, 8, 10, 12, 14),
    74: (1, 2, 3, 8, 10, 12, 14),
    75: (1, 2, 3, 10, 14),
    76: (1, 2, 3, 8, 10, 14),
    77: (2, 5, 8, 10, 12),
    78: (2, 5, 6, 10, 12),
    79: (2, 5, 10, 12),
    80: (1, 2, 5, 10, 12, 14),
    81: (1, 2, 5, 6, 10, 14),
    82: (1, 2, 5, 6, 10),
    83: (1, 2, 5, 8, 10),
    84: (1, 2, 5, 10, 12),
    85: (1, 2, 5, 8, 10, 12),
    86: (1, 2, 5, 10, 14),
    87: (2, 5, 10, 12, 14),
    88: (2, 5, 6, 10),
    89: (1, 2, 5, 6, 10, 12, 14),
    90: (1, 2, 5, 6, 8, 10, 12, 14),
    91: (1, 2, 5, 6, 8, 10, 14),
    92: (1, 2, 5, 8, 10, 14),
    93: (1, 3, 6, 12, 14),
    94: (3, 5, 12),
    95: (1, 3, 5, 10, 12, 14),
    96: (2, 3, 10, 12),
    97: (1, 3, 10, 12),
    98: (2, 3, 5, 6, 10, 12, 14),
    99: (1, 2, 3, 5, 10, 12, 14),
    100: (1, 2, 3, 5, 10, 12),
    101: (1, 2, 3, 5, 6, 10, 12, 14),
    102: (3, 6, 8, 12),
    103: (2, 3, 6, 8, 10, 12, 14),
    104: (2, 3, 8, 10, 12, 14),
    105: (2, 3, 6, 8, 10, 12),
    106: (1, 2, 3, 6, 8, 10, 12),
    107: (1, 2, 3, 8, 10, 12),
    108: (2, 8, 10),
    109: (1, 2, 3, 8, 10),
    110: (1, 2, 3, 10, 12),
    111: (2, 6, 10, 14),
    112: (2, 6, 8, 10, 12, 14),
    113: (2, 10, 14),
    114: (2, 8, 10, 14),
    115: (2, 8, 10, 12, 14),
    116: (2, 3, 10, 12, 14),
    117: (2, 3, 6, 10, 14),
    118: (2, 3, 6, 10),
    119: (2, 3, 8, 10),
    120: (2, 3, 10, 14),
    121: (2, 8, 10, 12),
    122: (2, 6, 10, 12),
    123: (2, 10, 12),
    124: (1, 2, 10, 12, 14),
    125: (1, 2, 6, 10),
    126: (1, 2, 8, 10),
    127: (1, 2, 10, 12),
    128: (1, 2, 8, 10, 12),
    129: (2, 10, 12, 14),
    130: (1, 2, 6, 10, 12, 14),
    131: (2, 3, 6, 10, 12, 14),
    132: (1, 2, 8, 12),
    133: (1, 2, 6, 14),
    134: (1, 2, 6, 12),
    135: (1, 2, 5, 8, 12),
    136: (1, 2, 12, 14),
    137: (1, 2, 5, 10),
    138: (1, 2, 6, 8, 12, 14),
    139: (1, 2, 14),
    140: (1, 2, 8, 12, 14),
    141: (1, 2, 6, 12, 14),
    142: (1, 2, 5, 12),
    143: (1, 2, 6, 8, 12),
    144: (1, 2, 6, 8, 10, 12),
    145: (2, 3, 6, 10, 12),
    146: (1, 2, 3, 6, 10, 12),
    147: (1, 2, 3, 5, 12),
    148: (1, 2, 3, 6, 12, 14),
    149: (1, 2, 3, 12, 14),
    150: (1, 2, 3, 6, 12),
    151: (3, 6, 8, 12, 14),
    152: (3, 5, 6, 8, 10, 12, 14),
    153: (3, 5, 8, 10, 12, 14),
    154: (3, 5, 8, 12, 14),
    155: (3, 8, 12, 14),
    156: (3, 5, 8, 10, 12),
    157: (3, 6, 8, 10, 12),
    158: (3, 8, 10, 12),
    159: (3, 8, 10, 12, 14),
    160: (3, 6, 8, 10, 12, 14),
    161: (2, 3, 8, 12, 14),
    162: (2, 3, 5, 6, 8, 10, 12, 14),
    163: (2, 3, 5, 6, 8, 10, 12),
    164: (2, 3, 6, 8, 12, 14),
    165: (2, 3, 6, 8, 12),
    166: (2, 3, 5, 8, 12),
    167: (1, 6, 12, 14),
    168: (1, 3, 5, 6, 12, 14),
    169: (1, 3, 5, 6, 10, 12, 14),
    170: (1, 3, 5, 6, 10, 14),
    171: (1, 2, 3, 5, 6, 10, 14),
    172: (1, 3, 6, 10, 14),
    173: (1, 2, 5, 6, 12, 14),
    174: (1, 2, 3, 5, 6, 12, 14),
    175: (1, 2, 3, 5, 8, 10, 12, 14),
    176: (1, 2, 3, 8, 12, 14),
    177: (1, 12, 14),
    178: (1, 3, 5, 12, 14),
    179: (1, 3, 5, 10, 14),
    180: (1, 2, 5, 12, 14),
    181: (1, 2, 3, 5, 12, 14),
    182: (3, 5, 6, 8, 10, 12),
    183: (1, 3, 5, 6, 8, 10, 12, 14),
    184: (1, 3, 5, 6, 8, 10, 12),
    185: (1, 3, 5, 8, 10, 12),
    186: (1, 3, 6, 8, 10, 12),
    187: (1, 3, 6, 8, 12),
    188: (1, 3, 5, 8, 12),
    189: (1, 3, 5, 6, 8, 12, 14),
    190: (1, 3, 5, 8, 12, 14),
    191: (2, 3, 5, 10),
    192: (2, 5, 6, 8, 10, 14),
    193: (2, 3, 5, 6, 8, 10, 14),
    194: (2, 3, 5, 8, 10, 14),
    195: (2, 5, 6, 10, 12, 14),
    196: (2, 5, 6, 8, 10, 12),
    197: (2, 3, 5, 6, 10, 12),
    198: (1, 2, 3, 6, 8, 12, 14),
    199: (1, 2, 3, 10),
    200: (1, 2, 10),
    201: (2, 3, 10),
    202: (2, 6, 8, 10, 14),
    203: (2, 3, 6, 8, 10, 14),
    204: (2, 3, 8, 10, 14),
    205: (2, 6, 10, 12, 14),
    206: (2, 6, 8, 10, 12),
    207: (1, 6, 8, 10, 14),
    208: (2, 6, 8, 10),
    209: (1, 6, 8, 14),
    210: (1, 3, 6, 8, 10),
    211: (2, 3, 6, 8, 10),
    212: (1, 2, 6, 8, 10),
    213: (1, 2, 3, 6, 8, 12),
    214: (5, 8),
    215: (2, 3, 8, 14),
    216: (1, 5, 8, 10, 14),
    217: (1, 3, 8, 14),
    218: (1, 3, 8, 10),
    219: (1, 8, 10, 14),
    220: (1, 2, 8, 14),
    221: (1, 2, 3, 8, 12),
    222: (2, 3, 8, 12),
    223: (1, 3, 5, 8, 10, 14),
    224: (1, 2, 3, 5, 8, 10, 14),
    225: (1, 2, 5, 8, 12, 14),
    226: (1, 2, 3, 5, 8, 12, 14),
    227: (1, 3, 8, 12)}

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
    # bipartiteSearch__dc_twoResistor_series(True)# still wrong, returning this:[6, 7, 10, 8, 14, 1, 0, 4, 3, 2, 5, 9, 12], maybe because its the longer path, but we do not need one of the equations
    bipartiteSearch__dc_twoResistor_parallel(True)