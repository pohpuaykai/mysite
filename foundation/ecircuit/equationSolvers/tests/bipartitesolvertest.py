import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.ecircuit.equationSolvers.bipartitesolver import BipartiteSolver


pp = pprint.PrettyPrinter(indent=4)

def bipartiteSolver__dc_twoResistor_parallel(verbose=False):
    listOfCollectedEquations=list(map(lambda schemeStr: Equation(equationStr=schemeStr, parserName='scheme'), [
    '(= (+ (+ (- 0 I_{DC_{8}}) I_{R_{0}}) I_{R_{3}}) 0)', 
    '(= (+ (- 0 V_{R_{0}}) V_{DC_{8}}) 0)', 
    '(= (- V_{DC_{8}} V_{R_{3}}) 0)', 
    '(= (/ V_{R_{0}} I_{R_{0}}) R_{R_{0}})', 
    '(= (/ V_{R_{3}} I_{R_{3}}) R_{R_{3}})', 
    '(= (/ V_{DC_{8}} I_{DC_{8}}) R_{DC_{8}})']))
    dependentVariableStr='R_{DC_{8}}'
    independentVariableStrs=['R_{R_{0}}', 'R_{R_{3}}']
    solver = BipartiteSolver(listOfCollectedEquations, dependentVariableStr, independentVariableStrs, verbose=verbose)
    broadSteps = solver._solve(simplify=True)
    expected_broadSteps = None


    print(inspect.currentframe().f_code.co_name, ' PASSED? ', broadSteps == expected_broadSteps)
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
        print('broadSteps')
        print(broadSteps)



if __name__=='__main__':
    # bipartiteSearch__dc_twoResistor_series(True)# still wrong, returning this:[6, 7, 10, 8, 14, 1, 0, 4, 3, 2, 5, 9, 12], maybe because its the longer path, but we do not need one of the equations
    bipartiteSolver__dc_twoResistor_parallel(True)