import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend


pp = pprint.PrettyPrinter(indent=4)



def test__deriveMetaInformation__basic(verbose=False):#TODO does not work
    eqs = '(= a (+ b c))' # fill it in
    eqsType = 'scheme'
    #filename = 'communtativity'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    rec = Recommend(eq0, verbose=verbose)
    manipulatedSchemeEquation = rec._deriveMetaInformation() # (+ $0 $1)
    expected = '(= a (+ c b))' # (+ $1 $0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)

    
def test__bipartiteSearch__dc_twoResistor_parallel(verbose=False):
    from foundation.automat.core.equation import Equation
    listOfCollectedEquationStrs = [
    '\\frac{1}{-R_{ R_{ 0 } }}+\\frac{1}{-R_{ R_{ 1 } }}=\\frac{1}{X_{ total_{ 6 } }}', 
    'I_{ R_{ 0 } }-I_{ R_{ 1 } }-I_{ DC_{ 4 } }=0', '-V_{ R_{ 1 } }-V_{ R_{ 0 } }=0', 
    'V_{ DC_{ 4 } }+V_{ R_{ 0 } }=0', 
    '\\frac{V_{ R_{ 0 } }}{I_{ R_{ 0 } }}=R_{ R_{ 0 } }', 
    '\\frac{V_{ R_{ 1 } }}{I_{ R_{ 1 } }}=R_{ R_{ 1 } }'
    ] # convert to equations

    listOfCollectedEquations = []; listOfVariables = []; #take the index in list as the id of these
    equationVariables_g = {}
    for equationId, equationStr in enumerate(listOfCollectedEquationStrs):
        equation = Equation(equationStr=equationStr, parserName='latex')
        variables = equation.variablesScheme
        for variable in variables.keys():
            try:
                variableId = listOfVariables.index(variable)
            except:
                variableId = len(listOfVariables)
                listOfVariables.append(variable)
            existingNeighbours = equationVariables_g.get(variableId, [])
            existingNeighbours.append(equationId)
            equationVariables_g[variableId] = existingNeighbours
            #
            existingNeighbours = equationVariables_g.get(equationId, [])
            existingNeighbours.append(variableId)
            equationVariables_g[equationId] = existingNeighbours
        # print(variables, '<<<<<,variables')
        listOfCollectedEquations.append(equation)

    dependentVariable = None#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    list_independentVariables = None#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    Recommend.bipartiteSearch(listOfCollectedEquations, listOfVariables, equationVariables_g, dependentVariable, list_independentVariables)

    if verbose:
        print(listOfCollectedEquations)
        print(listOfVariables)
        pp.pprint(equationVariables_g)


if __name__=='__main__':
    # test__deriveMetaInformation__basic(True)
    test__bipartiteSearch__dc_twoResistor_parallel(True)