import os
import re

from jinja2 import Environment, FileSystemLoader
import numpy as np
from yaml import safe_load

from foundation.automat import AUTOMAT_MODULE_DIR, info
# from foundation.automat.common.longestcommonsubsequence import LongestCommonSubsequence
# from foundation.automat.common.regexshorts import Regexshorts as rs
from foundation.automat.common.schemegrammarparser import SchemeGrammarParser
from foundation.automat.core.manipulate.manipulate import Manipulate

class Recommend:
    """
    recommends what to do to an equation to make it 'better'
    better is 
    1. simplification
    2. transforming to make it suit another purpose, like integration

    also reads manipulation/configuration to derive meta
    information about manipulations, for heuristic searching

    #~ DRAFT ~#
    input:
    1. Equation


    """
    PATTERN_FILENAMES__CLASSNAMES = Manipulate.PATTERN_FILENAMES__CLASSNAMES()
    #properties of _metaData
    _metaData = None
    _manipulateConfigFileFolder = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate','configuration')
    _metaFolder = os.path.join(AUTOMAT_MODULE_DIR, 'core', 'manipulate', 'recommend', 'meta')
    _metaFilename = 'manipulations_patterns.npy'
    #

    @classmethod
    def getMetaData(cls, redrive=False):
        if redrive:
            Recommend._metaData = cls._generateMetaInformation()
        else:
            try:
                Recommend._metaData = np.array(np.load(file=os.path.join(Recommend._metaFolder, Recommend._metaFilename), allow_pickle=True))
            except:
                import traceback; traceback.print_exc()
                print('failed to load from disk, so have to reload')
                Recommend._metaData = cls._generateMetaInformation()
        return Recommend._metaData



    def __init__(self, redrive=False, verbose=False):
        self.verbose=verbose


    def getManipulateClass(self, filename):
        className = Recommend.PATTERN_FILENAMES__CLASSNAMES[filename]
        import importlib, inspect
        module_obj = importlib.import_module(f'.{filename}', package='foundation.automat.core.manipulate.pattern')
        klassName, manipulateClass = list(filter(lambda tup: tup[0]==className,inspect.getmembers(module_obj, predicate=inspect.isclass)))[0]
        globals()[className] = manipulateClass
        return manipulateClass


    @classmethod
    def _generateMetaInformation(cls):
        from foundation.automat.parser.sorte.schemeparser import Schemeparser
        metaData = []
        for filename in os.listdir(cls._manipulateConfigFileFolder):
            if filename.endswith('.yaml'): # then its good! sei vorsichtung um nicht zu non-configuration-files zu beitragen
                config = cls._loadYAMLFromFilePath(os.path.join(cls._manipulateConfigFileFolder, filename))
                if 'manipulations' not in config or config['manipulations'] is None:
                    continue
                for idx, manipulations in enumerate(config['manipulations']):
                    if manipulations['type'] == 'regex':
                        typey = manipulations['type']
                        for direction, d in manipulations.items():
                            if direction in ['type', 'minArgs', 'maxArgs', 'preCond']:
                                continue
                            # print(d); print('config'); print(config)
                            # import pdb;pdb.set_trace()
                            iSchemeparser = Schemeparser(equationStr=d['scheme'])
                            oSchemeparser = Schemeparser(equationStr=d['return'])
                            iAst, iFunctions, iVariables, iPrimitives, iTotalNodeCount, iStartPos__nodeId = iSchemeparser._parse()
                            oAst, oFunctions, oVariables, oPrimitives, oTotalNodeCount, oStartPos__nodeId = oSchemeparser._parse()
                            iLabelsInOrderOfStartPos = list(map(lambda label: label[0] if label.startswith(SchemeGrammarParser.variableStartMarker) else label, iSchemeparser.getLabelsInOrderOfStartPos()))
                            iListWithoutLabels = list(map(lambda sublist: sublist.replace('(', '0').replace(' ', '1').replace(')', '2'), iSchemeparser.getListWithoutLabels()))

                            
                            iMode = SchemeGrammarParser.getMode(d['scheme'])
                            #need to get the mode for the iPattern<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                            metaData.append({#TODO sqlite database? lol OR implement your own BTree, werde settle for numpy for now
                                'identity':{
                                    'idx':idx,
                                    'direction':direction,
                                    'filename':filename[:filename.index('.')]
                                },
                                # 'i': {
                                #     'ast':iAst,
                                #     'functions':iFunctions,
                                #     'variables':iVariables,
                                #     'primitive':iPrimitives,
                                #     'totalNodeCount':iTotalNodeCount
                                # },
                                # 'o': {
                                #     'ast':oAst,
                                #     'functions':oFunctions,
                                #     'variables':oVariables,
                                #     'primitive':oPrimitives,
                                #     'totalNodeCount':oTotalNodeCount
                                # },
                                #i
                                'iAst':iAst,
                                'iFunctions':iFunctions,
                                'iVariables':iVariables,
                                'iPrimitives':iPrimitives,
                                'iTotalNodeCount':iTotalNodeCount,
                                'iStartPos__nodeId':iStartPos__nodeId,
                                'iDepth':iSchemeparser.getASTDepth(),
                                'iWidth':iSchemeparser.getASTWidth(),
                                'iLabelsInOrderOfStartPos':iLabelsInOrderOfStartPos,
                                'iListWithoutLabels':iListWithoutLabels,
                                'iMode':iMode,
                                #o
                                'oAst':oAst,
                                'oFunctions':oFunctions,
                                'oVariables':oVariables,
                                'oPrimitives':oPrimitives,
                                'oTotalNodeCount':oTotalNodeCount,
                                'oStartPos__nodeId':oStartPos__nodeId,
                                #differences
                                'type':typey,
                                'functionsIO':set(iFunctions.keys()) - set(oFunctions.keys()),
                                'functionsOI':set(oFunctions.keys()) - set(iFunctions.keys()),
                                'variablesIO':set(iVariables.keys()) - set(oVariables.keys()),
                                'variablesOI':set(oVariables.keys()) - set(iVariables.keys()),
                                'primitiveIO':set(iPrimitives.keys()) - set(oPrimitives.keys()),
                                'primitiveOI':set(oPrimitives.keys()) - set(iPrimitives.keys()),
                                'totalNodeCountIO':iTotalNodeCount - oTotalNodeCount
                            })
        np.save(file=os.path.join(cls._metaFolder, cls._metaFilename), arr=metaData, allow_pickle=True) # ValueError: Object arrays cannot be saved when allow_pickle=False
        #then https://numpy.org/doc/stable/reference/generated/numpy.save.html says its a security issue.... WHAT TO DO?
        # self.metaData = np.array(metaData)
        print('regenerated metaData') # this is to double_check how many times the metaData is regenerated and loaded from disk
        return np.array(metaData)


    def filterMetaList(self, metaList, searchCol, searchTerms):
        # print('metaList', metaList); print('searchCol', searchCol); print('searchTerms', searchTerms);
        # import pdb;pdb.set_trace()
        if isinstance(searchTerms, list): # we assume that searchCol's values are list of str
            def hasOneOfThese(row, terms):
                return len(terms.intersection(row[searchCol])) > 0
            mask = np.vectorize(lambda row: hasOneOfThese(row, set(searchTerms)))(metaList)
            return metaList[mask]
        # a range string '>5', '<=10.0'
        m = re.match('([><=]+)([-]*\\d+(?:\\.{1}\\d+)*)$', searchTerms)
        if m is not None:
            gle, numS = m.groups()
            num = float(numS)
            def findRange(row, gle, num):
                if gle == '>':
                    return row[searchCol] > num
                elif gle == '>=':
                    return row[searchCol] >= num
                elif gle == '<':
                    return row[searchCol] < num
                elif gle == '<=':
                    return row[searchCol] <= num
                elif gle == '==':
                    return row[searchCol] == num
                else:
                    raise Exception(f'We only take <, >, <=, >=, ==, but we got {gle}')
            mask = np.vectorize(lambda row: findRange(row, gle, num))(metaList)
            # import pdb;pdb.set_trace()
            return metaList[mask]

    def getRowsInMeta(self, searchCol, searchTerms):
        metaData = Recommend.getMetaData()
        return self.filterMetaList(metaData, searchCol, searchTerms)
        # return self.filterMetaList(self.metaData, searchCol, searchTerms)

    def sortForHeuristicsRelevantTo(self, eq, manipulations):
        manipulations = sorted(manipulations, key=lambda row: self.mostNumberOfIPatternNodes___SORTINGHEURISTIC(row['iTotalNodeCount']))
        return manipulations


    def filterForHeuristicsRelevantTo(self, eq, manipulations):
        #TODO please move to this the end of this function, should not be done here
        manipulations = self.sortForHeuristicsRelevantTo(eq, manipulations)
        #

        from copy import copy

        #HELPER
        def combiningDictionaries(iPrimitives, iFunctions):
            d = copy(iPrimitives); d.update(iFunctions)
            return d
        #
        breadthOfEquation = eq.schemeparser.getASTWidth()
        depthOfEquation = eq.schemeparser.getASTDepth()
        entityTotalCountOfEquation = eq.totalNodeCountScheme
        equationEntityToCount = combiningDictionaries(eq.primitivesScheme, eq.functionsScheme)#copy(self.eq.primitivesScheme).update(self.eq.functionsScheme)
        equationEntityStartEndPos = eq.schemeparser.getLabelsInOrderOfStartPos()
        equationBracketSpaceList = list(map(lambda sublist: sublist.replace('(', '0').replace(' ', '1').replace(')', '2'), eq.schemeparser.getListWithoutLabels()))
        #
        # print('0.*****************************')
        # print('schemeStr: ', eq.schemeStr)
        # print('len(manipulations):', len(manipulations))
        # print('breadthOfEquation: ', breadthOfEquation)
        # print('depthOfEquation: ', depthOfEquation)
        # print('equationEntityToCount: ', equationEntityToCount)
        # print('entityTotalCountOfEquation: ', entityTotalCountOfEquation)
        # print('equationEntityStartEndPos: ', equationEntityStartEndPos)
        # print('equationBracketSpaceList: ', equationBracketSpaceList)
        # import pdb;pdb.set_trace()
        #


        manipulations = list(filter(lambda row:
            self.breadthOfIPatternAtMostEquation___FILTERHEURISTIC(row['iWidth'], breadthOfEquation), manipulations))
        
        # print('1.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row:
            self.depthOfIPatternAtMostEquation___FILTERHEURISTIC(row['iDepth'], depthOfEquation),manipulations))
        
        # print('2.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row:
            self.totalEntityCountOfIPatternAtMostEquation___FILTERHEURISTIC(row['iTotalNodeCount'], entityTotalCountOfEquation), manipulations))
        
        # print('3.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row: #iVariables will only contain $ variable for iPattern
            self.entityCountsOfIPatternInEquation___FILTERHEURISTIC(combiningDictionaries(row['iPrimitives'], row['iFunctions']), equationEntityToCount), manipulations))
        
        # print('4.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row: #metaData needs to store iPatternEntityStartEndPos
            self.orderOfEntitiesOfIPatternInEquation___FILTERHEURISTIC(row['iLabelsInOrderOfStartPos'], row['iMode'], equationEntityStartEndPos), manipulations))
        
        # print('5.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row: #metaData needs to store iPatternBracketSpaceList
            self.orderofBracketAndSpacesOfIPatternInEquation___FILTERHEURISTIC(row['iListWithoutLabels'], equationBracketSpaceList), manipulations))
        
        # print('6.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        

        return manipulations



    def simplify(self, eq, hint=None):
        #run FILTER_HEURISTIC and SORTIN_HEURISTIC
        simplifyingManipulations = self.getRowsInMeta('totalNodeCountIO', '>0') # the number of nodes get lesser, its ok, its this is a 1 step
        simplifyingManipulations = self.filterForHeuristicsRelevantTo(eq, simplifyingManipulations)
        #TODO SORTIN_HEURISTICs, simplest iPattern first?
        simplifyingManipulations = sorted(simplifyingManipulations, key=lambda row: row['oTotalNodeCount'])
        #TODO more SORTIN_HEURISTICs?

        if hint is None: # maybe this should not be here... <<<<<<<<<<<<<<<
            self.combingSearch()
        else:
            #run through each manipulation
            rmIdentities = list(map(lambda row: row['identity'], simplifyingManipulations))
            for idd in rmIdentities:
                manipulateClass = self.getManipulateClass(idd['filename'])
                # import pdb;pdb.set_trace()
                manipulate = manipulateClass(eq, idd['direction'], idd['idx'], verbose=self.verbose)
                returnTup = manipulate.apply(startPos__nodeId=hint['startPos__nodeId'], toAst=True)#there is no need for hint? eq has the latest startPos__nodeId<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                if returnTup is not None: # successfully applied manipulation,  we will return it first
                    #
                    #use sgp.schemeId__argCount, and sgp.schemeNodeChangeLog to get function/variable/primitive count? for variable, schemeId__argCount=1, for function, schemeId__argCount>1, for primitive, schemeId__argCount=0
                    #but the downstream equation.simplify does not need countsOfFunctionVariablePrimitivesRemoved anymore!
                    #equation.simplify needs, can be reparsed by schemeparser, but those with nodeId, need to be changed to the OLD nodeIds provided by sgp
                    #or should they be provided by sgp? but it is weird to put latexParser in sgp...?
                    sgp, manipulateType, manipulateClassName, manipulateDirection, manipulateIdx = returnTup
                    rootOfTree___simplified = sgp.getRootOfTree___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    ast___simplified = sgp.getAST___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    startPos__nodeId___simplified = sgp.startPos__nodeId___oStr
                    nodeId__len___simplified = sgp.getNodeId__len___oStr()# this is schemeNodeLen, not schemeLabelLen, nodeId needs to be recalculated
                    schemeStr___simplified = sgp.oStr

                    functions___simplified = sgp.schemeparser___oStr.functions
                    variables___simplified = sgp.schemeparser___oStr.variables
                    primitives___simplified = sgp.schemeparser___oStr.primitives
                    totalNodeCount___simplified = sgp.schemeparser___oStr.totalNodeCount
                    latexStr___simplified = sgp.schemeparser___oStr._toLatex()

                    iPattern = sgp.iPattern
                    oPattern = sgp.oPattern
                    return rootOfTree___simplified, ast___simplified, startPos__nodeId___simplified, nodeId__len___simplified, schemeStr___simplified, functions___simplified, variables___simplified, primitives___simplified, totalNodeCount___simplified, latexStr___simplified, manipulateType, manipulateClassName, iPattern, oPattern


    def breadthOfIPatternAtMostEquation___FILTERHEURISTIC(self, breadthOfIPattern, breadthOfEquation):#<<<<<<<<<<<<<<needs to do breadth in schemeParser
        """
        breadth of IPattern as a schemeTree, must be less than or equals to the breadth of equation as a schemeTree
        """
        return breadthOfIPattern <= breadthOfEquation

    def depthOfIPatternAtMostEquation___FILTERHEURISTIC(self, depthOfIPattern, depthOfEquation):#<<<<<<<<<<<<<<<<<<needs to do depth in schemeParser
        """
        depth Of IPattern as a schemeTree, must be less than or equals to the depth of equation as a schemeTree
        """
        return depthOfIPattern <= depthOfEquation

    #{HEURISTICS SchemeStructural} the positions of the brackets_and_spaces of the iPattern must be found in the positions of the brackets_and_spaces of the equation, otherwise there is no need to consider that equation. 

    def totalEntityCountOfIPatternAtMostEquation___FILTERHEURISTIC(self, entityTotalCountOfIPattern, entityTotalCountOfEquation):
        """
        entityTotalCount is the total number of schemeLabels in either IPattern or Equation

        if there are (strictly) more schemeLabels in IPattern than there are schemeLabels in Equation, then iPattern cannot be found in Equation
        """
        return entityTotalCountOfIPattern <= entityTotalCountOfEquation

    def entityCountsOfIPatternInEquation___FILTERHEURISTIC(self, iPatternEntityToCount, equationEntityToCount):
        """
        iPatternEntityToCount is a dictionary from string to integer, where string is a schemeLabel and integer is the number of times the schemeLabel appears in iPattern
        equationEntityToCount is a dictionary from string to integer, where string is a schemeLabel and integer is the number of times the schemeLabel appears in equation

        if there is some schemeLabel that has greater count in iPattern, than in equationEntityToCount, then this iPattern cannot be found in equation, no need to try
        """
        for schemeLabel, count in iPatternEntityToCount.items():
            equationSchemeLabelCount = equationEntityToCount.get(schemeLabel, 0)
            if count > equationSchemeLabelCount:
                return False
        return True
        

    def orderOfEntitiesOfIPatternInEquation___FILTERHEURISTIC(self, iPatternEntityStartEndPos, iMode, equationEntityStartEndPos):#<<<<<<<<<<<<<<<<<<<<<<<<<needs to call the method already in the schemeparser and cache the results, so that SGP can use it too
        """
        we order the schemeLabels_of_iPattern by startPosition, and order the schemeLabels_of_Equation by startPosition
        if the schemeLabels_of_iPattern (as a list), cannot be found in the schemeLabels_of_Equation (as a list), then this iPattern cannot be found in equation, no need to try
        
        And the 'in' works like this:
        0. we let MODE1 pass, so we should only have MODE0 and MODE2
        1. chop up the iPatternEntityStartEndPos by $, then find each segment in order by PyRegex, but we join the list with () {cannot in the schemeLabels, by schemeDefinition}
        2. if some segment cannot be found in order, then return false
        """
        if iMode == 1:
            return True
        #heran we only have iMode==0 or iMode==2
        schemeLabelDelimiter = ')(' # this cannot be found in entityStartEndPos
        delimitedEquationEntityStartEndPos = schemeLabelDelimiter.join(equationEntityStartEndPos)
        def joinByAppending(list_str):#this way of appending, compared to the standard_python_join, prevents the BAD non_splitting of schemeLabelDelimiter+SchemeGrammarParser.variableStartMarker+schemeLabelDelimiter, if SchemeGrammarParser.variableStartMarker is at the end of the iPatternEntityStartEndPos
            ts = ''
            for s in list_str:
                ts += s + schemeLabelDelimiter
            return ts
        segments = list(filter(lambda s: s!= SchemeGrammarParser.variableStartMarker and len(s) > 0, 
            joinByAppending(iPatternEntityStartEndPos).split(SchemeGrammarParser.variableStartMarker+schemeLabelDelimiter)))
        equationStartPos = 0
        equationEntityStartEndPos = joinByAppending(equationEntityStartEndPos)
        # print('iPatternEntityStartEndPos', iPatternEntityStartEndPos)
        # print('equationEntityStartEndPos', equationEntityStartEndPos)
        # print('segments: ', segments); 
        # import pdb;pdb.set_trace()
        for segment in segments:
            try:
                equationStartPos = equationEntityStartEndPos[equationStartPos:].index(segment) + len(segment)
            except:
                return False
        return True

    def orderofBracketAndSpacesOfIPatternInEquation___FILTERHEURISTIC(self, iPatternBracketSpaceList, equationBracketSpaceList):
        """
        we order the bracketsAndSpacesOf{everything excluding the schemeLabels|entities} into iPatternBracketSpaceList, equationBracketSpaceList
        if the iPatternBracketSpaceList cannot be found in equationBracketSpaceList, then this iPattern cannot be found in equation, no need to try

        The 'in' works similiarly to orderOfEntitiesOfIPatternInEquation
        0. for MODE1, we need to add a space, because in MODE1 we do not count the schemeFunction. Also note that MODE1 will just be bunch of spaces
        1. 
        2. if some segment cannot be found in order, then return false

        """
        schemeStructureDelimiter = ')(' # this cannot be found in anySchemeStr, because there must be at least 1 space between openBracket and closeBracket
        delimitedEquationBracketSpaceList = schemeStructureDelimiter.join(equationBracketSpaceList)
        equationStartPos = 0
        for segment in iPatternBracketSpaceList:
            try:
                equationStartPos = delimitedEquationBracketSpaceList[equationStartPos:].index(segment) + len(segment)
            except:
                return False
        return True

    def mostNumberOfIPatternNodes___SORTINGHEURISTIC(self, iTotalNodeCount):
        return -iTotalNodeCount

    def reduceVariablesCount(self, variable):
        """
        #~ DRAFT ~#
        try to reduce the variablesCount(variable) -> 1


        variable should appear 2 or more times in self.eq
        ==
        self.eq.variables[variable] > 1

        look for the lowest-common-ancestor in AST of variable <<<TODO in `Equation`
        ON EACH SIDE OF THE EQUATION
        cut-out the subTree
        (or hinted simplify, where hint = {lastOp: root of the subTree})
        then run UNHINTED SEARCH??? << no need, will comb in simplify

        :param variable:
        :type variable:
        """
        self.eq._cutSubASTAtRoot(rootNode)


    @classmethod
    def bipartiteSearch(
        self, 
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
        list_independentVariableIds
        ):
        """THIS method seem ill suited to be in this class............. change file? >< Maybe create a new class called Eliminator take always takes a system of equations, also contains symbolicGaussian

        This was the original planned search. Implemented for ecircuit

        equations are nodes on 1 side of the bipartite, the other side are variables. variables connect to equations, if they appear in the equation. The connection is undirected

        There are 
        0. controllable_variables(manufacturers, variable_resistance, variable_capacitance, variable_inductance, amplification_of_transistor),
        1. fixed_variables(more like constants coming from specifications|after_choosing_manufacturers, like V_{cc}, load_max_current, transistor_threshold_voltage, collector_emitter_breakdown_voltage)
        2. intermediate_variables(not 0|1), we want to substitute these away...

        form a path P, going through all the intermediate_variables, path will alternate between equation & variable.
        In P, between 2 equations E0, E1 there is a variable V.
        Make V the subject of E0, and substitute V away in E1.
        Repeat for the whole P. We will get an equation without all the intermediate_variables.

        Then either plop in the values(simple calculation), or plot a graph with the equation(understand effects of circuit), or use equation for optimization(what to buy)

        Count_Tree_まま
        When we try to derive parallelSumOfResistors of 2_resistor_in_parallel_circuit, the bipartite_path_is_blocked on V_{DC}-V_{R_3}=0, because the next required step of elimination requires a equation that is not on the bipartiteGraph
        as we do linearEliminationBySubstitution, new Equations (set of variables) are produced, and some of them might have extra_variables_that_can_be_cancelled_out.
        If we could simplify equations, so that they do not have extra_variables_that_can_be_cancelled_out, the_set_of_variables_ignoring_position_in_equation, can be used as id for the equation
        If we have the_set_of_variables_ignoring_position_in_equation as id for equation, we can add newly created variables to the bipartite_graph {the underlying graph changes as we traverse it}
        And then that path becomes explorable_and_obtainable.
        This means:
        - WE HAVE TO WORK ON SIMPLIFY(finding the shortest_possible_standard_representation_of_an_equation) for id_of_equation
        - and then the update the bipartite_graph as we traverse it

        Also our current_method_of_substitution does not allow SchemeFunctions to be substituted away, if this was possible other paths to derive the parallel_sum_of_resistance might be possible... {ELEGANCE}

        #a possible HACK for now, without needing substitution and the maximum increase will only be 2^{number_of_variables} so no infiniteLoop, is
        #each equation has a set of variables, when we join them by a path, we can just union the variables and remove the intermediate variable to form the new vertex.
        #just that we have to let the user know how the new vertex was formed

        :param dependentVariableId: is a vertexId, (not from list_equations nor list_variables)
        :param list_independentVariableIds: are vertexIds (not from list_equations nor list_variables)
        :param type__list_vertexIds: type is either (0)equationKey or (1)variableKey (the partite of each vertexId), values are a list of vertexIds of its key's partite
        



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
        list_independentVariableIds

        """
        #get all the parameters passed to this function, so that we can write a unit test{START}
        # print('******************************************************************************')
        # print('list_equations:')
        # print(list(map(lambda equation: equation.schemeStr, list_equations)))
        # print('list_variables')
        # print(list_variables)
        # print('equationVariables_bg')
        # print(equationVariables_bg)
        # print('vertexId__equationVariableId')
        # print(vertexId__equationVariableId)
        # print('equationId__vertexId')
        # print(equationId__vertexId)
        # print('variableId__vertexId')
        # print(variableId__vertexId)
        # print('type__list_vertexIds')
        # print(type__list_vertexIds)
        # print('equationKey')
        # print(equationKey)
        # print('variableKey')
        # print(variableKey)
        # print('dependentVariableId')
        # print(dependentVariableId)
        # print('list_independentVariableIds')
        # print(list_independentVariableIds)
        # import pdb;pdb.set_trace()
        #get all the parameters passed to this function, so that we can write a unit test{END}
        from copy import copy
        #
        import pprint; pp = pprint.PrettyPrinter(indent=4)
        #
        bipartiteTreeExpand = False

        class EquationVertexIdIssuer:
            def __init__(self, currentMaxEquationId, currentMaxEquationVertexId):
                self.currentMaxEquationId = currentMaxEquationId
                self.currentMaxEquationVertexId = currentMaxEquationVertexId
            def getNewEquationIdAndEquationVertexId(self):
                self.currentMaxEquationId += 1; self.currentMaxEquationVertexId += 1
                return self.currentMaxEquationId, self.currentMaxEquationVertexId

        currentMaxEquationId = len(list_equations)-1; currentMaxEquationVertexId = max(list(equationId__vertexId.values())+list(variableId__vertexId.values()))
        # import pdb;pdb.set_trace()
        # print('currentMaxEquationVertexId', currentMaxEquationVertexId)
        equationVertexIdIssuer = EquationVertexIdIssuer(currentMaxEquationId, currentMaxEquationVertexId)

        #we are using tuple_variableVertexIdContaining as an id for equationVertexId
        tuple_variableVertexIdContaining__equationVertexId = {}#for checking duplicates
        equationVertexId__tuple_variableVertexIdContaining = {}
        for equationVertexId in equationId__vertexId.values():
            tuple_variableVertexIdContaining = tuple(sorted(equationVariables_bg[equationVertexId]))
            tuple_variableVertexIdContaining__equationVertexId[tuple_variableVertexIdContaining] = equationVertexId
            equationVertexId__tuple_variableVertexIdContaining[equationVertexId] = tuple_variableVertexIdContaining
        if bipartiteTreeExpand:
            equationVertexId__tuple_variableVertexIdContaining___NEW = {} # for user easy returns
        # print('equationVertexId__tuple_variableVertexIdContaining')
        # print(equationVertexId__tuple_variableVertexIdContaining); import pdb;pdb.set_trace()


        #[TODO optimization possible, if the bipartite graph equationVariables_bg is disconnected, only take the connected part that is related to dependent|indepedentVariables]
        from foundation.automat.common.priorityqueue import PriorityQueue
        #since we are finding all possible paths, what about save_points? (each save_point is [priority_queue, list_of_next_explored, index_of_visited_to_back_track]), everytime, we finish the PQ, but we cannot find an answer that gets all the unwantedVariables, we popOff a savePoint, but if we popOff more than 1 savePoint, savePoint0 and then savePoint1, we have to make sure we do not go back to the same savePoint0 again when we explore savePoint1... not sure how to do that
        allVariableVertexIds = list(map(lambda variableId: variableId__vertexId[variableId], range(0, len(list_variables))))
        wantedVariableVertexIds = list(map(lambda variableId: variableId__vertexId[variableId], [dependentVariableId]+list_independentVariableIds))
        unwantedVariableVertexIds = list(set(allVariableVertexIds) - set(wantedVariableVertexIds))
        allEquationVertexIds = list(map(lambda equationId: equationId__vertexId[equationId], range(0, len(list_equations))))
        #remove wantedVariableVertexIds
        equationVariables_bg___noWantedVariableVertexIds = {}
        for parentVertexId, childVertexIds in equationVariables_bg.items():
            if parentVertexId not in wantedVariableVertexIds:
                filteredChildVertexIds = []
                for childVertexId in childVertexIds:
                    if childVertexId not in wantedVariableVertexIds:
                        filteredChildVertexIds.append(childVertexId)
                equationVariables_bg___noWantedVariableVertexIds[parentVertexId] = filteredChildVertexIds
        equationVariables_bg = equationVariables_bg___noWantedVariableVertexIds

        #finding a startNode
        maxEquationVertexId = None;maxTotalCount = -1
        wantedVariables = []
        for wantedVariableId in [dependentVariableId]+list_independentVariableIds:
            wantedVariables.append(list_variables[wantedVariableId])
        for equationId, equation in enumerate(list_equations):
            variables__count = equation.variablesScheme; totalWantedVariableCount = 0
            for wantedVariable in set(variables__count.keys()).intersection(set(wantedVariables)):
                totalWantedVariableCount += variables__count[wantedVariable]
            if totalWantedVariableCount > maxTotalCount:
                maxTotalCount = totalWantedVariableCount; maxEquationVertexId = equationId__vertexId[equationId]



        #check if all the variables to be substituted away are in our path
        #or we can start from a variable, then add the appropriate equation to the beginning of the resulting path
        #maxEquationVertexId might be None... then for now just get a random one...
        if maxEquationVertexId is None:#[TODO many optimizations possible here] Ou est vers origin, ja?
            maxEquationVertexId = allEquationVertexIds[0] # startNode
        # print('unwantedVariableVertexIds', unwantedVariableVertexIds); print('wantedVariableVertexIds', wantedVariableVertexIds)
        # print('startNode: ', maxEquationVertexId)
        priorityQueue = PriorityQueue(); 
        priorityQueue.insert({
            'current':maxEquationVertexId, 
            'path':[maxEquationVertexId],
            'visited':[]
        }, -1)
        # maxLength=0; maxLengthPaths = []
        HIGH_WEIGHTS = 3000; LOW_WEIGHTS = 0; WANTEDVARIABLE_PENALTY = -2* HIGH_WEIGHTS#[TODO many optimizations possible here]
        PATHLENGTH_FACTOR = 10
        visitedPaths = [] # paths that have been explored before, we can use a set , since order does not matter? or we have to use a list?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<not used yet<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        # while len(stack)>0:
        while len(priorityQueue)>0:
            current___dict = priorityQueue.popMax()
            current = current___dict['current']
            visited = copy(current___dict['visited'])
            visited.append(current)
                    

            #############
            pp.pprint(current___dict)
            import pdb;pdb.set_trace()
            #############
            for orderOfExploration, neighbour in enumerate(sorted(equationVariables_bg[current], key=lambda vertexId: LOW_WEIGHTS if vertexId in unwantedVariableVertexIds or vertexId in allEquationVertexIds else HIGH_WEIGHTS)):#[TODO optimisation possibility] equationVariables_bg[current] can be sorted, because you are depending on the orderOfExploration
                if neighbour not in visited:
                    newPath = current___dict['path']+[neighbour]
                    childDict = {'current':neighbour, 'path':newPath, 'visited':visited+[neighbour]}
                    if bipartiteTreeExpand:
                        #
                        # if set(wantedVariableVertexIds).intersection(set(newPath)) == set(wantedVariableVertexIds): # we already hit all the wanted Variables
                        #     print('found!'); import pdb;pdb.set_trace()
                        #     favouritePath = newPath; break
                        #

                        #on the second equationVertexId, union all the variables of both equationsTogether to form a NEW equationVertexId{track this}
                        #add the NEW equationVertexId to equationVariables_bg
                        #childDict['current'] need to jump to the NEW equationVertexId
                        #{neighbour in equationVertexId__tuple_variableVertexIdContaining} is to check if neighbour is an equation
                        if len(newPath) > 2 and neighbour in equationVertexId__tuple_variableVertexIdContaining: #this means we have 1equation, 1variable ending the path and neighbour is the next equation
                            # print('newPath: ', newPath)
                            equationVertexId0, variableVertexIdToEliminate, equationVertexId1 = newPath[-3:]
                            # print('equationVertexId0', equationVertexId0)
                            equation0VariableIds = equationVertexId__tuple_variableVertexIdContaining[equationVertexId0]
                            equation1VariableIds = equationVertexId__tuple_variableVertexIdContaining[equationVertexId1]
                            newEquationVariableIds = set(equation0VariableIds).union(set(equation1VariableIds)) - set([variableVertexIdToEliminate])
                            tuple_variableVertexIdContaining = tuple(sorted(newEquationVariableIds))
                            #add newEquationVariableIds into the 
                            # print('tuple_variableVertexIdContaining__equationVertexId')
                            # print(tuple_variableVertexIdContaining__equationVertexId); import pdb;pdb.set_trace()
                            if tuple_variableVertexIdContaining not in tuple_variableVertexIdContaining__equationVertexId: # this prevents infiniteLoop, but it is not working<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                newEquationId, newEquationVertexId = equationVertexIdIssuer.getNewEquationIdAndEquationVertexId()
                                #this is just for TESTING please remove
                                # if newEquationVertexId > 512:
                                #     raise Exception() # cannot have more than 2^9 new equations
                                #
                                tuple_variableVertexIdContaining__equationVertexId[tuple_variableVertexIdContaining] = newEquationVertexId
                                equationVertexId__tuple_variableVertexIdContaining[newEquationVertexId] = tuple_variableVertexIdContaining
                                #graph update. update the new equation, also update its neighbours
                                equationNeighbourIds = list(set(tuple_variableVertexIdContaining)-set(wantedVariableVertexIds))
                                equationVariables_bg[newEquationVertexId] = equationNeighbourIds
                                for variableId in equationNeighbourIds:
                                    equationVariables_bg[variableId].append(newEquationVertexId)
                                #
                                vertexId__equationVariableId[newEquationVertexId] = newEquationId
                                equationId__vertexId[newEquationId] = newEquationVertexId
                                type__list_vertexIds[equationKey].append(newEquationVertexId)
                                equationVertexId__tuple_variableVertexIdContaining___NEW[newEquationVertexId] = tuple_variableVertexIdContaining
                            childDict['current'] = newEquationVertexId
                            # print('equationVariables_bg', equationVariables_bg)
                            #


                    #
                    if childDict['path'] not in visitedPaths:
                        visitedPaths.append(childDict['path'])
                        # if len(childDict['path']) > maxLength:
                        #     maxLength = len(childDict['path'])
                        #     maxLengthPaths = [] # only store longest path, this will not work if the #OfNodes(equationVariables_bg) increases as we process equationVariables_bg <Heuristic>
                        # if len(childDict['path']) == maxLength:#there might be many paths with same maxLength, if we have a choice, HOW TO CHOOSE<<<<<<<<<<<<<<<<<<<<<<<TODO?
                        #     maxLengthPaths.append(childDict['path'])
                        #Priority Heuristic
                        childDictPriority = HIGH_WEIGHTS if neighbour in unwantedVariableVertexIds or neighbour in allEquationVertexIds else LOW_WEIGHTS
                        childDictPriority = childDictPriority - orderOfExploration if neighbour in unwantedVariableVertexIds else childDictPriority # do not subtract orderofExploration if it is a equation
                        childDictPriority += PATHLENGTH_FACTOR * len(childDict['path']) # should continue on the longest path, and not jump other timeframe of shorter path
                        childDictPriority += WANTEDVARIABLE_PENALTY if neighbour in wantedVariableVertexIds else 0
                        priorityQueue.insert(childDict, childDictPriority)#-orderOfExploration try to ensure that those inserted later, have lower priority
                    #
                    # print('******')
                    # print('neighbour', neighbour, 'priority: ', childDictPriority-orderOfExploration)
                    # print('current: ', current, ' child: ', childDict['current'], 'currentPath: ', current___dict['path'], ' childPath: ', childDict['path'])
                    # print('priorityQueue')
                    # print(priorityQueue)
                    # print('visited:', current___dict['visited'])
                    # print('******')
        # print('returning substitutionPath:', maxLengthChildDict['path'])
        #pick your favourite path from maxLengthPaths?
        # print('maxLengthPaths:')
        # print(maxLengthPaths)
        # print('********')
        maxLen = min(map(lambda s: len(s), visitedPaths))
        maxLengthPaths = list(filter(lambda s: len(s)==maxLen, visitedPaths))
        favouritePath = maxLengthPaths[0] # [TODO many optimisations possible here]
        if bipartiteTreeExpand:
            return favouritePath, equationVertexId__tuple_variableVertexIdContaining___NEW
        else:
            return favouritePath, []


    def combingSearch(self, equation, maximumDepth=256): #<<<<<<<<<<<maybe rename to solve|simplify
        """
        an option for early return? if we see the same formula showing up for more than "the_number_of_times_number_of_schemeNodes" of the formula, then return, also if history ends with all node_swapping_manipulations{no_increase_no_decrease}, then they are the same formulas
        """#if manipulation is node_swapping, check the last_consecutive_history for it, it should not be repeated in the last_consecutive_history
        ####for debugging
        import pprint; pp = pprint.PrettyPrinter(indent=4)
        ####
        from copy import deepcopy
        from foundation.automat.common.priorityqueue import PriorityQueue

        from foundation.automat.core.equation import Equation
        visitedSchemeStrs = [equation.schemeStr]#<<<<<<<<<<<<<<<<<<instead of using set, use list, so that you can see when each schemeStr was added<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # manipulations = Recommend.getMetaData()
        priorityQueue = PriorityQueue(); 
        priorityQueue.insert({
            'eq':equation,
            'depth':0,
            'history':[],
            'unHistory':[]#the equivalent of history, but in reverse fo each item in history
        }, -1)
        while len(priorityQueue) > 0:
            state = priorityQueue.popMax()
            eq = state['eq']; depth = state['depth']; history = state['history']; unHistory = state['unHistory']
            if depth >= maximumDepth:
                # print('stopping search... because one of the states reached maximumDepth')
                #what to return?
                break
            manipulations = self.filterForHeuristicsRelevantTo(eq, Recommend.getMetaData()) # branches
            #####for debugging
            # print('~~~~~~~~~~~~~')
            # pp.pprint(state)
            # print('~~~~~~~~~~~~~')
            #####
            # print('len(manipulations): ', len(manipulations))
            for idd in map(lambda row: row['identity'], manipulations):
                #skip all the manipulations that you have just done
                historyKey = (idd['filename'], idd['direction'], idd['idx']); 
                reverseDirection = 'vor' if idd['direction'] == 'hin' else 'hin'
                unHistoryKey = (idd['filename'], reverseDirection, idd['idx'])
                if historyKey in history[-1:] or unHistoryKey in unHistory[-1:]: # this is not working <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    print('skipping manipulate: ', historyKey)
                    continue #skip, we do not want to directly undo our affords
                manipulateClass = self.getManipulateClass(idd['filename'])
                manipulate = manipulateClass(eq, idd['direction'], idd['idx'], verbose=self.verbose)
                # print('*************************************************separate call ', historyKey)
                returnTup = manipulate.apply(startPos__nodeId=eq.startPos__nodeId, toAst=True)
                if returnTup is not None: # successfully applied manipulation,  we will return it first
                    sgp, manipulateType, manipulateClassName, manipulateDirection, manipulateIdx = returnTup
                    # rootOfTree___simplified = sgp.getRootOfTree___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    # ast___simplified = sgp.getAST___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    # startPos__nodeId___simplified = sgp.startPos__nodeId___oStr
                    # nodeId__len___simplified = sgp.getNodeId__len___oStr()# this is schemeNodeLen, not schemeLabelLen, nodeId needs to be recalculated
                    # schemeStr___simplified = sgp.oStr

                    # functions___simplified = sgp.schemeparser___oStr.functions
                    # variables___simplified = sgp.schemeparser___oStr.variables
                    # primitives___simplified = sgp.schemeparser___oStr.primitives
                    # totalNodeCount___simplified = sgp.schemeparser___oStr.totalNodeCount
                    # latexStr___simplified = sgp.schemeparser___oStr._toLatex()

                    eq___new = Equation(sgp.oStr, parserName='scheme')
                    eq___new.astScheme = sgp.getAST___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    eq___new.rootOfTree = sgp.getRootOfTree___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    eq___new.startPos__nodeIdScheme = sgp.startPos__nodeId___oStr
                    eq___new.nodeId__lenScheme = sgp.getNodeId__len___oStr()# this is schemeNodeLen, not schemeLabelLen, nodeId needs to be recalculated
                    if sgp.oStr not in visitedSchemeStrs:
                        history = deepcopy(history); unHistory = deepcopy(unHistory)
                        history.append((idd['filename'], idd['direction'], idd['idx']))
                        reverseDirection = 'vor' if idd['direction'] == 'hin' else 'hin'
                        unHistory.append((idd['filename'], reverseDirection, idd['idx']))
                        visitedSchemeStrs.append(sgp.oStr)
                        priorityQueue.insert({
                            'eq':eq___new,
                            'depth':depth+1,
                            'history':history,
                            'unHistory':unHistory#the equivalent of history, but in reverse fo each item in history
                        }, -(depth+1))
                        #heuristics, so there are simplification_patterns where the nodes decrease from iPattern to oPattern, these should also serve as targets, so formulas that have the most potential to be matched by these patterns, should be given higher priority..<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        #heuristics, if we can simplify until there is only 1 of each variable, we can solve for anyvariable, by moving_left_to_right<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        #how to put the eq___new in? what priority?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    #else: #if we visit the same formula again... and there is a smaller depth? like in bellmanFord, add a new pattern? but the maintenance will have to give it a name
        # print('we actually finished running, this was not expected', visitedSchemeStrs)
        minStrLen = min(map(lambda s: len(s), visitedSchemeStrs))
        minSchemeStrs = sorted(list(filter(lambda s: len(s)==minStrLen, visitedSchemeStrs)))
        return minSchemeStrs

    @classmethod
    def _loadYAMLFromFilePath(cls, filepath):
        with open(filepath, 'r') as f:
            data = safe_load(f)
            return data