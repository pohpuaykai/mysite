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
    '\\frac{1}{-R_{ R_{ 0 } }}+\\frac{1}{-R_{ R_{ 1 } }}=\\frac{1}{X_{ total_{ 6 } }}', #0
    'I_{ R_{ 0 } }-I_{ R_{ 1 } }-I_{ DC_{ 4 } }=0', #1
    '-V_{ R_{ 1 } }-V_{ R_{ 0 } }=0', #2
    'V_{ DC_{ 4 } }+V_{ R_{ 0 } }=0', #3
    '\\frac{V_{ R_{ 0 } }}{I_{ R_{ 0 } }}=R_{ R_{ 0 } }', #4
    '\\frac{V_{ R_{ 1 } }}{I_{ R_{ 1 } }}=R_{ R_{ 1 } }' #5
    ] # convert to equations

    listOfCollectedEquations = []; listOfVariables = []; #take the index in list as the id of these
    equationVariables_g = {}; 
    type__list_vertexIds = {}; equationKey = 'equation'; variableKey = 'variable';
    equationId__vertexId = {}
    variableId__vertexId = {};#only for this script
    class VertexIdIssuer:
        def __init__(self):
            self.vertexId = -1
            self.vertexId__equationVariableId = {}
        def getVertexId(self, equationVariableId):
            self.vertexId += 1
            self.vertexId__equationVariableId[self.vertexId] = equationVariableId
            return self.vertexId

    vertexIdIssuer = VertexIdIssuer()
    for equationId, equationStr in enumerate(listOfCollectedEquationStrs):
        equation = Equation(equationStr=equationStr, parserName='latex')
        equationVertexId = vertexIdIssuer.getVertexId(equationId)
        equationId__vertexId[equationId] = equationVertexId
        #
        existingNeighbours = type__list_vertexIds.get(equationKey, [])
        existingNeighbours.append(equationVertexId)
        type__list_vertexIds[equationKey] = existingNeighbours
        #
        variables = equation.variablesScheme
        for variable in variables.keys():
            try:
                variableId = listOfVariables.index(variable)
                variableVertexId = variableId__vertexId[variableId]
            except:
                variableId = len(listOfVariables)
                listOfVariables.append(variable)
                variableVertexId = vertexIdIssuer.getVertexId(variableId)
                variableId__vertexId[variableId] = variableVertexId
            # print(variable, variableId, variableVertexId); import pdb;pdb.set_trace()
            #
            existingNeighbours = type__list_vertexIds.get(variableKey, [])
            if variableVertexId not in existingNeighbours:
                existingNeighbours.append(variableVertexId)
            type__list_vertexIds[variableKey] = existingNeighbours
            #
            existingNeighbours = equationVariables_g.get(variableVertexId, [])
            existingNeighbours.append(equationVertexId)
            equationVariables_g[variableVertexId] = existingNeighbours
            #
            existingNeighbours = equationVariables_g.get(equationVertexId, [])
            existingNeighbours.append(variableVertexId)
            equationVariables_g[equationVertexId] = existingNeighbours
        # print(variables, '<<<<<,variables')
        listOfCollectedEquations.append(equation)

    vertexId__equationVariableId = vertexIdIssuer.vertexId__equationVariableId
    dependentVariableId = 2#'X_{ total_{ 6 } }'
    list_independentVariablesIds = [6, 7, 8]#['V_{ R_{ 1 } }', 'V_{ R_{ 0 } }', 'V_{ DC_{ 4 } }']

    # #this is also the solving steps? Just the rough steps... not detailed enough<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<should include the actual manipulation steps :)
    substitutionPath = Recommend.bipartiteSearch(listOfCollectedEquations, listOfVariables, equationVariables_g, vertexId__equationVariableId, equationId__vertexId, type__list_vertexIds, equationKey, variableKey, dependentVariableId, list_independentVariablesIds)

    #incorporate for displaying_of_latex
    from foundation.automat.parser.sorte.latexparser import Latexparser
    #
    vorEquation = list_equations[vertexId__equationVariableId[substitutionPath[0]]]
    entVariable = list_variables[vertexId__equationVariableId[substitutionPath[1]]]
    print('start: ', Latexparser(ast=vorEquation.astScheme, rootOfTree=)._unparse()
    for idx, vertexId in enumerate(substitutionPath[2:]):
        if idx % 2 == 0: # vertexId==equationVertexId
            hinEquation = list_equations[vertexId__equationVariableId[vertexId]]
            #make substitution, changes should be made on the hinEquation, hinEquation is accumulator of all the substitutations
            hinEquation.linearEliminationBySubstitution(vorEquation, entVariable)#This method is not inplace (please see foundation.automat.core.tests.lineareliminationbysubstitution.py)
            print('substitutionStep ', (idx/2), ': ', hinEquation.astScheme, ' subVar: ', entVariable)
            vorEquation = hinEquation
        else: # vertexId==variableVertexId
            entVariable = list_variables[vertexId__equationVariableId[vertexIdx]]

    if verbose:
        print('listOfCollectedEquations')
        pp.pprint(list(map(lambda equation: equation._eqs, listOfCollectedEquations)))
        print('listOfVariables')
        pp.pprint(listOfVariables)
        print('vertexId__equationVariableId')
        pp.pprint(vertexId__equationVariableId)
        print('equationVariables_g')
        pp.pprint(equationVariables_g)
        print('type__list_vertexIds')
        pp.pprint(type__list_vertexIds)
        print('substitutionPath')
        print(substitutionPath)


if __name__=='__main__':
    # test__deriveMetaInformation__basic(True)
    test__bipartiteSearch__dc_twoResistor_parallel(True)