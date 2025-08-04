from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend

class BipartiteSolver:

    def __init__(self, listOfCollectedEquations, dependentVariableStr, independentVariableStrs):
        self.listOfCollectedEquations = listOfCollectedEquations
        self.dependentVariableStr = dependentVariableStr
        self.independentVariableStrs = independentVariableStrs
        self.vertexIdIssuer = VertexIdIssuer()

    def _solve(self):
        """

        """

        listOfCollectedEquations = self.listOfCollectedEquations; listOfVariables = []; #take the index in list as the id of these
        equationVariables_g = {}; 
        type__list_vertexIds = {}; equationKey = 'equation'; variableKey = 'variable';
        equationId__vertexId = {}
        variableId__vertexId = {};#only for this script
        dependentVariableId = None
        list_independentVariablesIds = set()


        vertexId__EquationOrVariable = {}# for DEBUGGING


        # for equationId, equationStr in enumerate(self.listOfCollectedEquationStrs):
        for equationId, equation in enumerate(listOfCollectedEquations):
            # equation = Equation(equationStr=equationStr, parserName='latex')
            equationVertexId = self.vertexIdIssuer.getVertexId(equationId)
            vertexId__EquationOrVariable[equationVertexId] = 'equation'
            # print('equation*****', equationId, equationVertexId)
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
                    variableVertexId = self.vertexIdIssuer.getVertexId(variableId)
                    variableId__vertexId[variableId] = variableVertexId
                # print('variable*****', variableId, variableVertexId)
                #capture dependentVariable and independentVariables
                if variable == self.dependentVariableStr:
                    dependentVariableId = variableId
                elif variable in self.independentVariableStrs:
                    list_independentVariablesIds.add(variableId)
                #
                # print(variable, variableId, variableVertexId); import pdb;pdb.set_trace()
                #

                vertexId__EquationOrVariable[variableVertexId] = 'variable'
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
            # listOfCollectedEquations.append(equation)

        vertexId__equationVariableId = self.vertexIdIssuer.vertexId__equationVariableId
        # dependentVariableId = 2#'X_{ total_{ 6 } }'
        # list_independentVariablesIds = [6, 7, 8]#['V_{ R_{ 1 } }', 'V_{ R_{ 0 } }', 'V_{ DC_{ 4 } }']
        list_independentVariablesIds = sorted(list(list_independentVariablesIds))
        print(dependentVariableId, 'dependentVariableId')
        print(list_independentVariablesIds, 'list_independentVariablesIds')
        print('equationVariables_g', equationVariables_g)
        print('vertexId__equationVariableId', vertexId__equationVariableId)
        print('vertexId__EquationOrVariable', vertexId__EquationOrVariable)

        substitutionPath = Recommend.bipartiteSearch(listOfCollectedEquations, listOfVariables, equationVariables_g, vertexId__equationVariableId, equationId__vertexId, type__list_vertexIds, equationKey, variableKey, dependentVariableId, list_independentVariablesIds)
        broadSteps = []

        #incorporate for displaying_of_latex
        from foundation.automat.parser.sorte.latexparser import Latexparser
        #
        # import pdb;pdb.set_trace()
        vorEquation = listOfCollectedEquations[vertexId__equationVariableId[substitutionPath[0]]]
        entVariable = listOfVariables[vertexId__equationVariableId[substitutionPath[1]]]
        # print('start: ', Latexparser(ast=vorEquation.astScheme, rootOfTree=vorEquation.rootOfTree)._unparse())
        broadSteps.append({
            'vor':{
                'latex':Latexparser(ast=vorEquation.astScheme, rootOfTree=vorEquation.rootOfTree)._unparse(),
                'scheme':vorEquation.schemeStr,
                'root':vorEquation.rootOfTree,
            },
            'sub':''
        })
        print('converting to solvingSteps<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        for idx, vertexId in enumerate(substitutionPath[2:]):
            print('vertexId', vertexId)
            if idx % 2 == 0: # vertexId==equationVertexId
                hinEquation = listOfCollectedEquations[vertexId__equationVariableId[vertexId]]
                hinDict = {
                    'latex':Latexparser(ast=hinEquation.astScheme, rootOfTree=hinEquation.rootOfTree)._unparse(),
                    'scheme':hinEquation.schemeStr,
                    'root':hinEquation.rootOfTree
                }
                #make substitution, changes should be made on the hinEquation, hinEquation is accumulator of all the substitutations
                _ast, _functions, _variables, _primitives, _totalNodeCount, _stepsWithoutSimplify___hin, _stepsWithoutSimplify___vor = hinEquation.linearEliminationBySubstitution(vorEquation, entVariable)
                # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                # print('hinEq steps:')
                # pp.pprint(_stepsWithoutSimplify___hin)
                # print('vorEq steps:')
                # pp.pprint(_stepsWithoutSimplify___vor)
                # print('substitutionStepAst ', (idx/2), ': ', hinEquation.astScheme, ' subVar: ', entVariable)
                # pp.pprint(hinEquation.astScheme)
                # print('substitutionStepLatex ', (idx/2), ': ', Latexparser(ast=hinEquation.astScheme, rootOfTree=hinEquation.rootOfTree)._unparse(), ' subVar: ', entVariable)
                # print('substitutionStep ', (idx/2), ': ', hinEquation.schemeStr, ' subVar: ', entVariable)
                
                vorEquation = hinEquation
                broadSteps.append({
                    'hin': hinDict,
                    'vor':{
                        'latex':Latexparser(ast=vorEquation.astScheme, rootOfTree=vorEquation.rootOfTree)._unparse(),
                        'scheme':vorEquation.schemeStr,
                        'root':vorEquation.rootOfTree
                    },
                    'sub':entVariable
                })
            else: # vertexId==variableVertexId
                entVariable = listOfVariables[vertexId__equationVariableId[vertexId]]
        return broadSteps


class VertexIdIssuer:
    def __init__(self):
        self.vertexId = -1
        self.vertexId__equationVariableId = {}
    def getVertexId(self, equationVariableId):
        self.vertexId += 1
        self.vertexId__equationVariableId[self.vertexId] = equationVariableId
        return self.vertexId