from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend

class BipartiteSolver:

    def __init__(self, listOfCollectedEquations, dependentVariableStr, independentVariableStrs, verbose=False):
        self.listOfCollectedEquations = listOfCollectedEquations
        self.dependentVariableStr = dependentVariableStr
        self.independentVariableStrs = independentVariableStrs
        self.vertexIdIssuer = VertexIdIssuer()
        self.verbose=verbose

    def _solve(self, simplify=False):
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
        list_independentVariablesIds = sorted(list(list_independentVariablesIds))
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(list(map(lambda eq: eq.schemeStr, listOfCollectedEquations)))
        # print('listOfVariables', listOfVariables)
        # print('equationVariables_g', equationVariables_g)
        # print('vertexId__equationVariableId', vertexId__equationVariableId)
        # print('equationId__vertexId', equationId__vertexId)
        # print('variableId__vertexId', variableId__vertexId)
        # print('type__list_vertexIds', type__list_vertexIds)
        # print('equationKey', equationKey)
        # print('variableKey', variableKey)
        # print('dependentVariableId', dependentVariableId)
        # print(list_independentVariablesIds, 'list_independentVariablesIds')
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # import pdb;pdb.set_trace()


        substitutionPath, equationVertexId__tuple_variableVertexIdContaining = Recommend.bipartiteSearch(
            listOfCollectedEquations, 
            listOfVariables, 
            equationVariables_g, 
            vertexId__equationVariableId, 
            equationId__vertexId, 
            variableId__vertexId,
            type__list_vertexIds, 
            equationKey, 
            variableKey, 
            dependentVariableId, 
            list_independentVariablesIds
        )
        print('substitutionPath: ', substitutionPath)
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
                'variables':list(vorEquation.variables.keys()),
                'scheme':vorEquation.schemeStr,
                'root':vorEquation.rootOfTree,
            },
            'hin':{},
            'sub':'',
            'vor__subSteps':[],
            'hin__subSteps':[],
        })
        import pprint;pp = pprint.PrettyPrinter(indent=4)
        def remove_AST_AND_RootOfTree(subStepList):
            newSubStepList = []
            for subStep in subStepList:
                del subStep['resultAST']
                del subStep['resultRootOfTree']
                newSubStepList.append(subStep)
            return newSubStepList
        print('converting to solvingSteps<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        for idx, vertexId in enumerate(substitutionPath[2:]):
            print('vertexId', vertexId)
            if idx % 2 == 0: # vertexId==equationVertexId
                hinEquation = listOfCollectedEquations[vertexId__equationVariableId[vertexId]]
                # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                # print('hinEquation.schemeStr: ', hinEquation.schemeStr, 'root:', hinEquation.rootOfTree, 'ast:', hinEquation.astScheme)
                # print('vorEquation.schemeStr: ', vorEquation.schemeStr, 'root:', vorEquation.rootOfTree, 'ast:', vorEquation.astScheme)
                # print('subjectOfEquation: ', entVariable)
                # print('simplify: ', simplify)
                # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                hinDict = {
                    'latex':Latexparser(ast=hinEquation.astScheme, rootOfTree=hinEquation.rootOfTree)._unparse(),
                    'variables':list(hinEquation.variables.keys()),
                    'scheme':hinEquation.schemeStr,
                    'root':hinEquation.rootOfTree
                }
                #make substitution, changes should be made on the hinEquation, hinEquation is accumulator of all the substitutations
                _ast, _functions, _variables, _primitives, _totalNodeCount, _stepsWithoutSimplify___hin, _stepsWithoutSimplify___vor = hinEquation.linearEliminationBySubstitution(vorEquation, entVariable, simplify=simplify)
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~solvedHin:')
                print('SOLVED hinEquation.schemeStr: ', hinEquation.schemeStr)
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('hinEq steps:')
                pp.pprint(_stepsWithoutSimplify___hin)
                print('vorEq steps:')
                pp.pprint(_stepsWithoutSimplify___vor); import pdb;pdb.set_trace()

                #for now, we just take out the ast, rootOfTree from the _stepsWithoutSimplify
                _stepsWithoutSimplify___hin = remove_AST_AND_RootOfTree(_stepsWithoutSimplify___hin)
                _stepsWithoutSimplify___vor = remove_AST_AND_RootOfTree(_stepsWithoutSimplify___vor)
                # print('substitutionStepAst ', (idx/2), ': ', hinEquation.astScheme, ' subVar: ', entVariable)
                # pp.pprint(hinEquation.astScheme)
                # print('substitutionStepLatex ', (idx/2), ': ', Latexparser(ast=hinEquation.astScheme, rootOfTree=hinEquation.rootOfTree)._unparse(), ' subVar: ', entVariable)
                # print('substitutionStep ', (idx/2), ': ', hinEquation.schemeStr, ' subVar: ', entVariable)
                
                vorEquation = hinEquation
                vorDict = {
                        'latex':Latexparser(ast=vorEquation.astScheme, rootOfTree=vorEquation.rootOfTree)._unparse(),
                        'variables':list(vorEquation.variables.keys()),
                        'scheme':vorEquation.schemeStr,
                        'root':vorEquation.rootOfTree
                    }
                broadSteps.append({
                    'hin': hinDict,
                    'vor':vorDict,
                    'sub':entVariable,
                    'vor__subSteps':list(reversed(_stepsWithoutSimplify___vor)),
                    'hin__subSteps':list(reversed(_stepsWithoutSimplify___hin))
                })
            else: # vertexId==variableVertexId
                entVariable = listOfVariables[vertexId__equationVariableId[vertexId]]

        #
        print('passing to combingSearch: ', vorEquation.schemeStr)
        #
        from foundation.automat.parser.sorte.schemeparser import Schemeparser

        eq = Equation(equationStr=vorEquation.schemeStr, parserName='scheme')
        chosenSchemeStrsWithSolvingSteps = Recommend.combingSearch(eq)
        chosenSchemeStrWithSolvingSteps = chosenSchemeStrsWithSolvingSteps[0] # for now we just take the first one
        vor__subSteps = []
        for (manipulationFilename, direction, idx) in chosenSchemeStrWithSolvingSteps['solvingStep']:

            manipulateClass = Recommend.getManipulateClass(manipulationFilename)
            # import pdb;pdb.set_trace()
            manipulate = manipulateClass(eq, direction, idx, calculateSchemeNodeChanges=True, verbose=self.verbose)
            returnTup = manipulate.apply(startPos__nodeId=eq.startPos__nodeId, toAst=True)#there is no need for hint? eq has the latest startPos__nodeId<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            sgp, manipulateType, manipulateClassName, manipulateDirection, manipulateIdx = returnTup
            schemeStr = sgp.oStr
            latexStr = sgp.schemeparser___oStr._toLatex()

            vor__subSteps.append({#should the subSteps exclude the last step? since that is the main step?
                'resultSchemeStr':schemeStr,
                'resultAST':sgp.schemeparser___oStr.ast,
                'resultLatexStr':latexStr,#parse the latex here? or in Recommend?<<<<<<<<<<
                'resultRootOfTree':sgp.schemeparser___oStr.rootOfTree,
                'resultVariables':list(set(sgp.schemeparser___oStr.variables.keys())),
                'stepType':'simplification',
            })
            eq = Equation(equationStr=schemeStr, parserName='scheme')

        schemeparser = Schemeparser(equationStr=chosenSchemeStrWithSolvingSteps['schemeStr'])
        ast, functions, variables, primitives, totalNodeCount, startPos__nodeId = schemeparser._parse()
        variablesSet = list(set(variables.keys()))
        broadSteps.append({

            'vor':{#take the end of chosenSchemeStrWithSolvingSteps
                'latex':Latexparser(ast=ast, rootOfTree=schemeparser.rootOfTree)._unparse(),
                'variables':variablesSet,
                'scheme':chosenSchemeStrWithSolvingSteps['schemeStr'],
                'root':schemeparser.rootOfTree
            },
            'hin':{#take the end of chosenSchemeStrWithSolvingSteps
                'latex':Latexparser(ast=ast, rootOfTree=schemeparser.rootOfTree)._unparse(),
                'variables':variablesSet,
                'scheme':chosenSchemeStrWithSolvingSteps['schemeStr'],
                'root':schemeparser.rootOfTree
            },
            
            # 'vor':vorDict,
            # 'hin':{#take the end of chosenSchemeStrWithSolvingSteps
            #     'latex':Latexparser(ast=ast, rootOfTree=schemeparser.rootOfTree)._unparse(),
            #     'variables':variablesSet,
            #     'scheme':chosenSchemeStrWithSolvingSteps['schemeStr'],
            #     'root':schemeparser.rootOfTree
            # },

            # 'hin':vorDict,
            # 'vor': {#take the end of chosenSchemeStrWithSolvingSteps
            #     'latex':Latexparser(ast=ast, rootOfTree=schemeparser.rootOfTree)._unparse(),
            #     'variables':variablesSet,
            #     'scheme':chosenSchemeStrWithSolvingSteps['schemeStr'],
            #     'root':schemeparser.rootOfTree
            # },
            'sub':'',
            'vor__subSteps':remove_AST_AND_RootOfTree(vor__subSteps),
            'hin__subSteps':[]
        })

        return broadSteps


class VertexIdIssuer:
    def __init__(self):
        self.vertexId = -1
        self.vertexId__equationVariableId = {}
    def getVertexId(self, equationVariableId):
        self.vertexId += 1
        self.vertexId__equationVariableId[self.vertexId] = equationVariableId
        return self.vertexId