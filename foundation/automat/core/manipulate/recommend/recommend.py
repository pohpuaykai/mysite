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

    @classmethod
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

    @classmethod
    def sortForHeuristicsRelevantTo(cls, eq, manipulations):
        manipulations = sorted(manipulations, key=lambda row: cls.mostNumberOfIPatternNodes___SORTINGHEURISTIC(row['iTotalNodeCount']))
        return manipulations

    @classmethod
    def filterForHeuristicsRelevantTo(cls, eq, manipulations):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<does not need to take in eq, only needs schemeparser<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<REFACTOR
        #TODO please move to this the end of this function, should not be done here
        manipulations = cls.sortForHeuristicsRelevantTo(eq, manipulations)
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
            cls.breadthOfIPatternAtMostEquation___FILTERHEURISTIC(row['iWidth'], breadthOfEquation), manipulations))
        
        # print('1.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row:
            cls.depthOfIPatternAtMostEquation___FILTERHEURISTIC(row['iDepth'], depthOfEquation),manipulations))
        
        # print('2.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row:
            cls.totalEntityCountOfIPatternAtMostEquation___FILTERHEURISTIC(row['iTotalNodeCount'], entityTotalCountOfEquation), manipulations))
        
        # print('3.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row: #iVariables will only contain $ variable for iPattern
            cls.entityCountsOfIPatternInEquation___FILTERHEURISTIC(combiningDictionaries(row['iPrimitives'], row['iFunctions']), equationEntityToCount), manipulations))
        
        # print('4.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row: #metaData needs to store iPatternEntityStartEndPos
            cls.orderOfEntitiesOfIPatternInEquation___FILTERHEURISTIC(row['iLabelsInOrderOfStartPos'], row['iMode'], equationEntityStartEndPos), manipulations))
        
        # print('5.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        manipulations = list(filter(lambda row: #metaData needs to store iPatternBracketSpaceList
            cls.orderofBracketAndSpacesOfIPatternInEquation___FILTERHEURISTIC(row['iListWithoutLabels'], equationBracketSpaceList), manipulations))
        
        # print('6.*****************************')
        # print('still there?:', len(list(filter(lambda row: row['identity']['filename']=='distributivity' and row['identity']['idx']==0, manipulations)))>0); import pdb;pdb.set_trace()
        

        return manipulations



    def simplify(self, eq, hint=None):
        #run FILTER_HEURISTIC and SORTIN_HEURISTIC
        simplifyingManipulations = self.getRowsInMeta('totalNodeCountIO', '>0') # the number of nodes get lesser, its ok, its this is a 1 step
        simplifyingManipulations = Recommend.filterForHeuristicsRelevantTo(eq, simplifyingManipulations)
        #TODO SORTIN_HEURISTICs, simplest iPattern first?
        simplifyingManipulations = sorted(simplifyingManipulations, key=lambda row: row['oTotalNodeCount'])
        #TODO more SORTIN_HEURISTICs?

        if hint is None: # maybe this should not be here... <<<<<<<<<<<<<<<
            self.combingSearch()
        else:
            #run through each manipulation
            rmIdentities = list(map(lambda row: row['identity'], simplifyingManipulations))
            for idd in rmIdentities:
                manipulateClass = Recommend.getManipulateClass(idd['filename'])
                # import pdb;pdb.set_trace()
                manipulate = manipulateClass(eq, idd['direction'], idd['idx'], calculateSchemeNodeChanges=True, verbose=self.verbose)
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

    @classmethod
    def breadthOfIPatternAtMostEquation___FILTERHEURISTIC(cls, breadthOfIPattern, breadthOfEquation):#<<<<<<<<<<<<<<needs to do breadth in schemeParser
        """
        breadth of IPattern as a schemeTree, must be less than or equals to the breadth of equation as a schemeTree
        """
        return breadthOfIPattern <= breadthOfEquation

    @classmethod
    def depthOfIPatternAtMostEquation___FILTERHEURISTIC(cls, depthOfIPattern, depthOfEquation):#<<<<<<<<<<<<<<<<<<needs to do depth in schemeParser
        """
        depth Of IPattern as a schemeTree, must be less than or equals to the depth of equation as a schemeTree
        """
        return depthOfIPattern <= depthOfEquation

    #{HEURISTICS SchemeStructural} the positions of the brackets_and_spaces of the iPattern must be found in the positions of the brackets_and_spaces of the equation, otherwise there is no need to consider that equation. 
    @classmethod
    def totalEntityCountOfIPatternAtMostEquation___FILTERHEURISTIC(cls, entityTotalCountOfIPattern, entityTotalCountOfEquation):
        """
        entityTotalCount is the total number of schemeLabels in either IPattern or Equation

        if there are (strictly) more schemeLabels in IPattern than there are schemeLabels in Equation, then iPattern cannot be found in Equation
        """
        return entityTotalCountOfIPattern <= entityTotalCountOfEquation

    @classmethod
    def entityCountsOfIPatternInEquation___FILTERHEURISTIC(cls, iPatternEntityToCount, equationEntityToCount):
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
        
    @classmethod
    def orderOfEntitiesOfIPatternInEquation___FILTERHEURISTIC(cls, iPatternEntityStartEndPos, iMode, equationEntityStartEndPos):#<<<<<<<<<<<<<<<<<<<<<<<<<needs to call the method already in the schemeparser and cache the results, so that SGP can use it too
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

    @classmethod
    def orderofBracketAndSpacesOfIPatternInEquation___FILTERHEURISTIC(cls, iPatternBracketSpaceList, equationBracketSpaceList):
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

    @classmethod
    def mostNumberOfIPatternNodes___SORTINGHEURISTIC(cls, iTotalNodeCount):
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
        cls, 
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

        #the whole substitution is calculated (with or without simplification?), so that we can have resultingSchemeStr for SimplificationMatching<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<this seems very heavy.... and double_work? unless we can somehow make each calculationLighter, or on the side(parallelProcessing, like the state is doing manicure while being in the PQueue)
        #preference to have similiar formulas calculated in together in succession, this might be too specific for resistance_sum_derivation, but can be weighted according to wanted V unwanted variables<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        :param dependentVariableId: is a vertexId, (not from list_equations nor list_variables)
        :param list_independentVariableIds: are vertexIds (not from list_equations nor list_variables)
        :param type__list_vertexIds: type is either (0)equationKey or (1)variableKey (the partite of each vertexId), values are a list of vertexIds of its key's partite
        


        #for eCircuits we can use thevenin or norton to simplify large circuits, should implement this in another kind of solver?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        #implement MaximumDepth for this too<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

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
        # print('******************************************************************************')
        # import pdb;pdb.set_trace()
        #get all the parameters passed to this function, so that we can write a unit test{END}
        from copy import copy
        #
        import pprint; pp = pprint.PrettyPrinter(indent=4)
        #
        bipartiteTreeExpand = True

        #group the equations by similarity (this was working well when we wanted to find the resistorSumFormulas for series2Resistor & parallel2Resistor)# we might want to put heuristics in classes, and then turn them on and off as per experience(neuralnetwork?), since this might be a special case(over_trained_heuristic)?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        list_equationStrs = list(map(lambda equation: equation.schemeStr, list_equations))
        from foundation.automat.parser.sorte.schemeparser import Schemeparser
        def getEntitiesOfPattern(patternStr):
            parser = Schemeparser(equationStr=patternStr)
            ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = parser._parse()
            stack = [parser.rootOfTree]; nodeId__label = {}
            while len(stack) > 0:
                current = stack.pop()
                nodeId__label[current[1]] = current[0]
                children = ast.get(current, [])
                stack += children
            entities = []
            for startPos, nodeId in startPos__nodeId.items():
                l = len(nodeId__label[nodeId])
                entities.append((startPos, startPos+l))
            return entities, functionsD, variablesD, primitives, totalNodeCount
        #
        idx__entities = {}; 
        # idx__functions = {}; idx__variables = {}; idx__primitives = {} # more complex divisors of cutoff, can be devised...later<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        idx__divisorOfCutOff = {} # for now, we use a simple divisorOfCutOff
        for idx, schemeStr in enumerate(list_equationStrs):
            entities, functions, variables, primitives, totalNodeCount = getEntitiesOfPattern(schemeStr)
            idx__entities[idx] = entities
            # idx__functions[idx] = functions
            # idx__primitives[idx] = primitives
            # idx__variables[idx] = variables
            idx__divisorOfCutOff[idx] = totalNodeCount + 0.0 # to make it float
        #
        from foundation.automat.common.stringcompare import StringCompare
        tuple_comparisonIdx__score = {}
        for idx0, schemeStr0 in enumerate(list_equationStrs):
            for idx1, schemeStr1 in enumerate(list_equationStrs[idx0+1:]):
                idx1 += idx0+1
                tuple_comparisonIdx__score[(idx0, idx1)] = StringCompare.damerauLevenschsteinMimickWithEntities( # this could be altered to give scores more suitable for the set of equations
                    schemeStr0, schemeStr1, idx__entities[idx0], idx__entities[idx1]) / (idx__divisorOfCutOff[idx0]+idx__divisorOfCutOff[idx1])
        #everything above was for generating tuple_comparisonIdx__score, which is grouping equations together, which we will do from here
        #use UnionFind+cutoffScore...
        cutoffScore = 0.34#hardcode for now... there must be someway to parametrise this? neuralnetwork? BTW, this is a score, of how equation look alike
        from foundation.automat.common.unionfindbyrankwithpathcompression import UnionFindByRankWithPathCompression
        uf = UnionFindByRankWithPathCompression(len(list_equationStrs))
        for (idx0, idx1), score in tuple_comparisonIdx__score.items():
            if score < cutoffScore:
                uf.union(idx0, idx1)
        #use uf to give high priority if adjacent equations are in the same union.
        #convert groupings to vertexId
        verticesIdGroupings = []
        for group in uf.grouping():
            verticesIdGroupings.append(list(map(lambda equationId: equationId__vertexId[equationId], group)))
        #


        #within the same group of equations, there are same variables between all the equations, give each variable a count of the number of times they appear. when choosing a variable to subtitute away, choose the one that appears the least... #this heuristic was (this was working well when we wanted to find the resistorSumFormulas for series2Resistor & parallel2Resistor)
        def updateCountDict(d0, d1):
            """d0&d1 are dictionaries from string to integer"""
            commonKeys = set(d0.keys()).intersection(set(d1.keys()))
            d0UniqueKeys = set(d0.keys()) - commonKeys
            d1UniqueKeys = set(d1.keys()) - commonKeys
            allUniqueKeys = d0UniqueKeys.union(d1UniqueKeys)
            d2 = copy(d0)
            d2.update(d1)
            groupTotalVariableCount = dict(filter(lambda t: t[0] in allUniqueKeys, d2.items()))
            for commonKey in commonKeys:
                groupTotalVariableCount[commonKey] = d0[commonKey] + d1[commonKey]
            return groupTotalVariableCount
        ufGroupIdx__groupTotalVariableCount = {}
        for group in uf.grouping():
            groupTotalVariableCount = {}
            for equationIdx in group:
                equation = list_equations[equationIdx]
                groupTotalVariableCount = updateCountDict(groupTotalVariableCount, equation.variables)
            groupTotalVariableCount = dict(map(lambda t: (list_variables.index(t[0]), t[1]), groupTotalVariableCount.items()))
            ufGroupIdx = uf.find(equationIdx)
            ufGroupIdx__groupTotalVariableCount[ufGroupIdx] = groupTotalVariableCount
            # import pdb;pdb.set_trace()
        #

        #another heuristic might be crammer_method|GE? that will tell us which equation to choose and eliminate first? I think this will work very well...... a way into this heuristic is that  we do the <<2.3.5AmoreComplexCircuit>> bipartiteSolverWay manually, and then match bipartiteSolverWay to the CramerMethod<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


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
        allVariableVertexIds = list(map(lambda variableId: variableId__vertexId[variableId], range(0, len(list_variables))))
        wantedVariableVertexIds = list(map(lambda variableId: variableId__vertexId[variableId], [dependentVariableId]+list_independentVariableIds))
        unwantedVariableVertexIds = list(set(allVariableVertexIds) - set(wantedVariableVertexIds))
        allEquationVertexIds = list(map(lambda equationId: equationId__vertexId[equationId], range(0, len(list_equations))))
        originalEquationVertexIds = copy(allEquationVertexIds)
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

        #finding a startNode, maybe start with the most number of unwanted variable...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        maxEquationVertexId = None;maxTotalCount = -1
        wantedVariables = list(map(lambda variableId: variableId__vertexId[variableId], [dependentVariableId]+list_independentVariableIds))
        unwantedVariables = list(map(lambda variableId: variableId__vertexId[variableId], set(range(0, len(list_variables))) - set(wantedVariables)))
        # print('unwantedVariables: ', unwantedVariables)
        for equationId, equation in enumerate(list_equations):
            # variables__count = equation.variablesScheme; 
            variables__count = dict(map(lambda n: (n, 1), equationVariables_bg[equationId__vertexId[equationId]]))#it has to have only 1 count, otherwise it will not work?
            totalWantedVariableCount = 0
            # print('variables__count: ', variables__count)
            # for wantedVariable in set(variables__count.keys()).intersection(set(wantedVariables)):
            # for unwantedVariable in set(variables__count.keys()).intersection(unwantedVariables):
            #     # totalWantedVariableCount += variables__count[wantedVariable]
            #     totalWantedVariableCount += variables__count[unwantedVariable]
            totalWantedVariableCount = len(set(variables__count.keys()).intersection(unwantedVariables))
            # print('equationId: ', equationId, 'variables__count', variables__count, 'totalWantedVariableCount', totalWantedVariableCount, 'maxTotalCount: ', maxTotalCount)
            if totalWantedVariableCount > maxTotalCount:
                maxTotalCount = totalWantedVariableCount; maxEquationVertexId = equationId__vertexId[equationId]



        #
        def is_contiguous_sublist(sublist, mainlist):
            n = len(mainlist)
            m = len(sublist)
            if m > n:
                return False
            for i in range(n - m + 1):
                if mainlist[i:i+m] == sublist:
                    return True
            return False
        #


        #check if all the variables to be substituted away are in our path
        #or we can start from a variable, then add the appropriate equation to the beginning of the resulting path
        #maxEquationVertexId might be None... then for now just get a random one...
        # if maxEquationVertexId is None:#[TODO many optimizations possible here] Ou est vers origin, ja?
        #     maxEquationVertexId = allEquationVertexIds[0] # startNode
        # print('unwantedVariableVertexIds', unwantedVariableVertexIds); print('wantedVariableVertexIds', wantedVariableVertexIds)
        # print('startNode: ', maxEquationVertexId); import pdb;pdb.set_trace()

        #
        variableCount = {}
        for variableVertexId in equationVariables_bg[maxEquationVertexId]:
            variableCount[variableVertexId] = 1
        #


        priorityQueue = PriorityQueue(); 
        priorityQueue.insert({
            'current':maxEquationVertexId, 
            'path':[maxEquationVertexId],
            'visited':[],
            #we assume that this equation only has 1 of each variable
            'variableCount':variableCount
        }, -1)
        # maxLength=0; maxLengthPaths = []
        HIGH_WEIGHTS = 100; LOW_WEIGHTS = 0; 
        WANTEDVARIABLE_PENALTY = -2* HIGH_WEIGHTS # substituting away an unwanted variable
        NEWEQUATION_PENALTY = -2 * len(allVariableVertexIds) * HIGH_WEIGHTS
        INCREASE_IN_UNWANTED_VARIABLE_PENALTY = -2* HIGH_WEIGHTS
        INCREASE_IN_WANTED_VARIABLE_PENALTY = 3* HIGH_WEIGHTS
        # SAME_EQUATION_GROUP_REWARDS = 3 * HIGH_WEIGHTS * len(allEquationVertexIds)
        # SAME_EQUATION_GROUP_VARIABLE_COUNT_PENALTY = -3 * HIGH_WEIGHTS * len(allEquationVertexIds)
        SAME_EQUATION_GROUP_REWARDS = 4 * HIGH_WEIGHTS * len(uf.grouping()) # we want SAME_EQUATION_GROUP_REWARDS > SAME_EQUATION_GROUP_VARIABLE_COUNT_REWARD, in all the situations<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        SAME_EQUATION_GROUP_VARIABLE_COUNT_REWARD = 0.5 * HIGH_WEIGHTS * len(uf.grouping())
        TRYING_TO_ELIMINATE_VARIABLE_WITH_MORE_THAN_ONE_COUNT_PENALTY = -float('inf')#should be -infinity because this will produce a path that is not usable...
        #[TODO many optimizations possible here]
        # PATHLENGTH_FACTOR = 10
        PATHLENGTH_FACTOR = 2 # will tend to favour BFs if number is low (what is low? it has to be relative to score...), and then to favour DFs if number is high
        visitedPaths = [] # paths that have been explored before, we can use a set , since order does not matter? or we have to use a list?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<not used yet<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        # while len(stack)>0:
        while len(priorityQueue)>0:
            #######
            # print('priorityQueue: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            # print(priorityQueue.sortedList)
            #######
            # current___dict = priorityQueue.popMax()
            priority, current___dict = priorityQueue.popMaxWithPriority()
            current = current___dict['current']

            #############early termination, what if you waited for a few possible solutions first? how many to wait for?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if set(originalEquationVertexIds).issubset(set(current___dict['path'])): #we used all the original equations
                # print('used up all the ORIGINAL equations')
                # print('p: ', priority)
                # pp.pprint(current___dict)
                # import pdb;pdb.set_trace()
                return current___dict['path'], equationVertexId__tuple_variableVertexIdContaining___NEW
            #############


            visited = copy(current___dict['visited'])
            visited.append(current)
                    

            #heuristic early termination: when you have used all the_original_equations? Not the expanded ones?



            #also neighbours that like to previous_equation_group, should be explored first?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if current in allEquationVertexIds:#neighbours will be variables
                def sortKey(vertexIdx, path):#should also consider current path<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    key = 0
                    if vertexIdx in unwantedVariableVertexIds:
                        key += 10*LOW_WEIGHTS # we want this to be higher than 
                        eq0VertexId = path[-1]
                        if eq0VertexId in originalEquationVertexIds:
                            groupTotalVariableCount = ufGroupIdx__groupTotalVariableCount[uf.find(vertexId__equationVariableId[eq0VertexId])]
                            if vertexId__equationVariableId[vertexIdx] in groupTotalVariableCount:
                                variableCountInGroup = groupTotalVariableCount[vertexId__equationVariableId[vertexIdx]]
                                key += (variableCountInGroup/sum(groupTotalVariableCount.values())) * LOW_WEIGHTS
                    else:
                        key += 10*HIGH_WEIGHTS
                    #find previous group of equation in uf, rank by group_variable_occurence#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    return key

                #we will deal with unwanted variables first
                neighbours = sorted(equationVariables_bg[current], key=lambda vertexId: sortKey(vertexId, current___dict['path']))
                # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BE variables')
                # print(current___dict['path'])
                # print('neighbours', neighbours)
                # import pdb;pdb.set_trace()
            else:#neighbours will be equations
                def sortKey(vertexIdx, path):#should also consider current path<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    key = 0
                    if vertexIdx in originalEquationVertexIds:
                        key += 10*LOW_WEIGHTS
                        # print('checking: ', path[-2], vertexIdx, 'same group?: ', path[-2] != vertexIdx and uf.together(vertexId__equationVariableId[path[-2]], vertexId__equationVariableId[vertexIdx]))
                        # print(path[-2], vertexIdx, '<<<<<these should be vertexIdx')
                        if path[-2] in originalEquationVertexIds:
                            if path[-2] != vertexIdx and uf.together(vertexId__equationVariableId[path[-2]], vertexId__equationVariableId[vertexIdx]):
                                key+= LOW_WEIGHTS
                            else:
                                key+= HIGH_WEIGHTS
                    else:
                        key += 10*HIGH_WEIGHTS
                    #find previous group of equation in uf, if neighbour in the group, give higher priority#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                    return key
                #we will choose old Equations first not new equations
                neighbours = sorted(equationVariables_bg[current], key=lambda vertexId: sortKey(vertexId, current___dict['path']))
                # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< BE equations')
                # print(current___dict['path'])
                # print('neighbours', neighbours)
                # import pdb;pdb.set_trace()


            #############
            # print('new equations: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            # print(equationVertexId__tuple_variableVertexIdContaining___NEW)
            # if current___dict['path'][:10] == [6, 7, 10, 8, 14, 1, 0, 4, 3, 2]:
            # if current___dict['path'][:12] == [6, 7, 10, 8, 14, 9, 12, 1, 0, 4, 3, 2]:
            # if current___dict['path'][:3] == [0, 3, 11]:
                # print('current:', current)
                # print('neighbours: ', neighbours)
            # print('p: ', priority)
            # pp.pprint(current___dict)
            # import pdb;pdb.set_trace()
            #############
            for orderOfExploration, neighbour in enumerate(neighbours):#[TODO optimisation possibility] equationVariables_bg[current] can be sorted, because you are depending on the orderOfExploration
                if neighbour not in visited:
                    newPath = current___dict['path']+[neighbour]

                    childDict = {
                        'current':neighbour, 
                        'path':newPath, 
                        'visited':visited+[neighbour],
                        'variableCount':current___dict['variableCount']
                        # we assume that this equation only has 1 of each variable
                    }
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
                        if len(newPath) > 2 and neighbour in allEquationVertexIds:#equationVertexId__tuple_variableVertexIdContaining: #this means we have 1equation, 1variable ending the path and neighbour is the next equation
                            


                            # print('newPath: ', newPath)
                            equationVertexId0, variableVertexIdToEliminate, equationVertexId1 = newPath[-3:]
                            # print('equationVertexId0', equationVertexId0)
                            # equation0VariableIds = equationVertexId__tuple_variableVertexIdContaining[equationVertexId0]
                            # equation1VariableIds = equationVertexId__tuple_variableVertexIdContaining[equationVertexId1]
                            # newEquationVariableIds = set(equation0VariableIds).union(set(equation1VariableIds)) - set([variableVertexIdToEliminate])
                            



                            #we need to update the variableCount
                            variableCount = copy(current___dict['variableCount'])
                            tuple_variableVertexIdContaining = equationVertexId__tuple_variableVertexIdContaining[neighbour]
                            for variableVertexId, count in current___dict['variableCount'].items():
                                if variableVertexId != variableVertexIdToEliminate:
                                    if variableVertexId in tuple_variableVertexIdContaining:
                                        variableCount[variableVertexId] += 1
                                    # else:
                                    #     variableCount[variableVertexId] = 1
                                else:
                                    variableCount[variableVertexId] -= 1
                                    if variableCount[variableVertexId] == 0:
                                        del variableCount[variableVertexId]
                            for newVariableVertexId in set(tuple_variableVertexIdContaining) - set(current___dict['variableCount'].keys()):
                                if newVariableVertexId != variableVertexIdToEliminate:
                                    variableCount[newVariableVertexId] = 1
                            childDict['variableCount'] = variableCount


                            tuple_variableVertexIdContaining = tuple(sorted(variableCount.keys()))
                            #add newEquationVariableIds into the 
                            # print('tuple_variableVertexIdContaining__equationVertexId')
                            # print(tuple_variableVertexIdContaining__equationVertexId); import pdb;pdb.set_trace()
                            # print('tuple_variableVertexIdContaining', tuple_variableVertexIdContaining)
                            # print('tuple_variableVertexIdContaining__equationVertexId', tuple_variableVertexIdContaining__equationVertexId)
                            # import pdb;pdb.set_trace()
                            if tuple_variableVertexIdContaining not in tuple_variableVertexIdContaining__equationVertexId: # this prevents infiniteLoop, but it is not working<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                newEquationId, newEquationVertexId = equationVertexIdIssuer.getNewEquationIdAndEquationVertexId()
                                allEquationVertexIds.append(newEquationVertexId)
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
                            else:
                                newEquationVertexId = tuple_variableVertexIdContaining__equationVertexId[tuple_variableVertexIdContaining]
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
                        #Priority Heuristic>
                        childDictPriority = HIGH_WEIGHTS if neighbour in unwantedVariableVertexIds or neighbour in allEquationVertexIds else LOW_WEIGHTS
                        
                        # this is for sorting
                        childDictPriority = childDictPriority - orderOfExploration if neighbour in unwantedVariableVertexIds else childDictPriority # do not subtract orderofExploration if it is a equation
                        #

                        childDictPriority += PATHLENGTH_FACTOR * len(childDict['path']) # should continue on the longest path, and not jump other timeframe of shorter path,  and then at some point in the history go for the shorter path first, when most of the original equations are exhausted?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        childDictPriority += WANTEDVARIABLE_PENALTY if neighbour in wantedVariableVertexIds else 0 # because this means we will substitute the wanted variable away
                        if neighbour in allEquationVertexIds: #if it is an equation
                            variableVertexIds = list(equationVertexId__tuple_variableVertexIdContaining[neighbour]) # this is not a good way to get the containing_variables, because, we removed the variables from equationVariables_bg
                            eliminatedVariableVertexId = childDict['path'][-2]
                            # print('neighbour', neighbour)
                            # print('variableVertexIds: ', variableVertexIds)
                            for variableVertexId in variableVertexIds:
                                if variableVertexId != eliminatedVariableVertexId: #ignore the variable that will be eliminated
                                    if variableVertexId in wantedVariableVertexIds:
                                        # print('wanted added: ', INCREASE_IN_WANTED_VARIABLE_PENALTY, 'to', childDictPriority, '=', childDictPriority+INCREASE_IN_WANTED_VARIABLE_PENALTY)
                                        childDictPriority += INCREASE_IN_WANTED_VARIABLE_PENALTY
                                    else: # it is unwanted
                                        # print('unwanted added: ', INCREASE_IN_UNWANTED_VARIABLE_PENALTY, 'to', childDictPriority, '=', childDictPriority+INCREASE_IN_UNWANTED_VARIABLE_PENALTY)
                                        childDictPriority += INCREASE_IN_UNWANTED_VARIABLE_PENALTY
                        #if try to substitute away a variable that has more count than 1, then give a heavy penalty
                        if neighbour in allVariableVertexIds and childDict['variableCount'].get(neighbour, 0) > 1:
                            childDictPriority += TRYING_TO_ELIMINATE_VARIABLE_WITH_MORE_THAN_ONE_COUNT_PENALTY
                            #

                        #why is this path not rewarded:
                        # pathToInvestigate = [5, 6, 9, 8, 11, 7, 13, 2, 0]
                        # if newPath == pathToInvestigate:
                        #     print('len(newPath) > 2', len(newPath) > 2)
                        #     print('neighbour in allEquationVertexIds', neighbour in allEquationVertexIds)
                        #     print('(originalEquationVertexIds >= set(newPath[::2]))', (set(originalEquationVertexIds) >= set(newPath[::2])))
                        #     import pdb;pdb.set_trace()
                        #


                        if len(newPath) > 2 and neighbour in allEquationVertexIds and (set(originalEquationVertexIds) >= set(newPath[::2])):#does not contain any equationVertexId, that nonoriginal<<<<<<
                            #within the same group of equations, there are same variables between all the equations, give each variable a count of the number of times they appear. when choosing a variable to subtitute away, choose the one that appears the least... #this heuristic was (this was working well when we wanted to find the resistorSumFormulas for series2Resistor & parallel2Resistor)
                            variableIdx = vertexId__equationVariableId[newPath[-2]] # you want all the previous equations
                            previousEquationIdx = vertexId__equationVariableId[newPath[-1]]
                            ufGroupIdx = uf.find(previousEquationIdx)
                            # variableIdx = vertexId__equationVariableId[newPath[-2]]
                            # print("ufGroupIdx__groupTotalVariableCount", ufGroupIdx__groupTotalVariableCount); import pdb;pdb.set_trace()
                            if variableIdx in ufGroupIdx__groupTotalVariableCount[ufGroupIdx]:
                                groupTotalVariableCount = ufGroupIdx__groupTotalVariableCount[ufGroupIdx]
                                variableCount = groupTotalVariableCount[variableIdx]
                                totalVariableCountInGroup = sum(map(lambda t: t[1], groupTotalVariableCount.items()))
                                penaltyAmt = SAME_EQUATION_GROUP_VARIABLE_COUNT_REWARD * ((totalVariableCountInGroup - variableCount)/(totalVariableCountInGroup*len(newPath))) # the more of the same variable in the same equation_group, the higher the penalty...
                                childDictPriority += penaltyAmt
                                #rewarded?
                                # pathsToInvestigate = [[5, 6, 9, 8, 11, 7, 13, 2, 0], [5, 7, 13, 4, 3, 8, 11, 1, 9, 2, 0]]
                                # if newPath in pathsToInvestigate:
                                #     print(newPath, 'is penalised for same_variable_count: ', penaltyAmt,'result:', childDictPriority)
                                #     import pdb;pdb.set_trace()
                                #
                                # print(newPath, childDictPriority); import pdb;pdb.set_trace()
                            #
                        #if neighbour(an OG equation) is in the same union as the last equation, then give a higher priority
                        # if len(newPath) > 2 and neighbour in allEquationVertexIds and neighbour in originalEquationVertexIds:
                        #     equationVertexId0, variableVertexIdToEliminate, equationVertexId1 = newPath[-3:]
                        #     if equationVertexId0 in originalEquationVertexIds and uf.together(vertexId__equationVariableId[neighbour], vertexId__equationVariableId[equationVertexId0]):
                        #         childDictPriority += SAME_EQUATION_GROUP_REWARDS
                                # print('added rewards to newPath: ', newPath)

                        #SAME_EQUATION_GROUP_REWARDS, we want similiar equations(odd_index on path) to be processed together...
                        equationVertexIdList = newPath[::2]
                        for equationVertexIdGroupList in verticesIdGroupings:
                            # if equationVertexIdGroupList <= equationVertexIdList: # <= means subList, so both the order and content has to match before this is true
                            if is_contiguous_sublist(equationVertexIdGroupList, equationVertexIdList):
                                rewardAmt = SAME_EQUATION_GROUP_REWARDS * len(equationVertexIdGroupList)
                                childDictPriority += rewardAmt # please note that we might repeat this reward more than once for the same criteria<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                #rewarded?
                                # pathsToInvestigate = [[5, 6, 9, 8, 11, 7, 13, 2, 0], [5, 7, 13, 4, 3, 8, 11, 1, 9, 2, 0]]
                                # if newPath in pathsToInvestigate:
                                #     print(newPath, 'is rewarded for same_equation_group: ', rewardAmt, 'result:', childDictPriority)
                                #     import pdb;pdb.set_trace()
                                #


                        #Priority Heuristic<
                        if bipartiteTreeExpand:
                            childDictPriority += NEWEQUATION_PENALTY if neighbour in equationVertexId__tuple_variableVertexIdContaining___NEW else 0
                        # print('inserting: ', childDict, childDictPriority)
                        # print('priority: ', childDictPriority)
                        #Heuristics: should orders in the same group matter? if we already reached a group before, should we proceed with that group first?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        if childDictPriority > float('-inf'):#we discard everything that is -infinity
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
        # print('maxLengthPaths')
        # print(maxLengthPaths)
        # import pdb; pdb.set_trace()
        favouritePath = maxLengthPaths[0] # [TODO many optimisations possible here]
        if bipartiteTreeExpand:
            return favouritePath, equationVertexId__tuple_variableVertexIdContaining___NEW
        else:
            return favouritePath, {}

    @classmethod
    def combingSearch(cls, equation, maximumDepth=7, verbose=False): #<<<<<<<<<<<maybe rename to solve|simplify
        """
        an option for early return? if we see the same formula showing up for more than "the_number_of_times_number_of_schemeNodes" of the formula, then return, also if history ends with all node_swapping_manipulations{no_increase_no_decrease}, then they are the same formulas
        """#if manipulation is node_swapping, check the last_consecutive_history for it, it should not be repeated in the last_consecutive_history
        ####for debugging
        import pprint; pp = pprint.PrettyPrinter(indent=4)
        ####
        import sys
        from copy import deepcopy
        from foundation.automat.common.priorityqueue import PriorityQueue

        from foundation.automat.core.equation import Equation
        visitedSchemeStrs = [equation.schemeStr]#<<<<<<<<<<<<<<<<<<instead of using set, use list, so that you can see when each schemeStr was added<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # manipulations = Recommend.getMetaData()
        schemeLeastLength = sys.maxsize; leastLengthSchemeEquations = []; solvingSteps = []
        priorityQueue = PriorityQueue(); 
        priorityQueue.insert({
            'eq':equation,
            'depth':0,
            'history':[],
            'unHistory':[]#the equivalent of history, but in reverse fo each item in history
        }, -1)
        if verbose:
            currentReachedMaximumDepth = 0
        while len(priorityQueue) > 0:
            state = priorityQueue.popMax()
            eq = state['eq']; depth = state['depth']; history = state['history']; unHistory = state['unHistory']
            #
            if verbose:
                if depth > currentReachedMaximumDepth:
                    currentReachedMaximumDepth = depth
                    print('new depth: ', currentReachedMaximumDepth)
            #

            if depth >= maximumDepth:
                # print('stopping search... because one of the states reached maximumDepth')
                #what to return?
                break
            manipulations = cls.filterForHeuristicsRelevantTo(eq, Recommend.getMetaData()) # branches
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
                if historyKey in history[-1:] or unHistoryKey in unHistory[-1:]:
                    # print('skipping manipulate: ', historyKey)
                    continue #skip, we do not want to directly undo our affords
                manipulateClass = cls.getManipulateClass(idd['filename'])
                manipulate = manipulateClass(eq, idd['direction'], idd['idx'], verbose=verbose)
                # print('*************************************************separate call ', historyKey)
                returnTup = manipulate.apply(startPos__nodeId=eq.startPos__nodeId, toAst=False)
                if returnTup is not None: # successfully applied manipulation,  we will return it first
                    # sgp, manipulateType, manipulateClassName, manipulateDirection, manipulateIdx = returnTup
                    manipulatedSchemeWord, manipulateType, manipulateClassName, manipulateDirection, manipulateIdx = returnTup
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

                    # eq___new = Equation(sgp.oStr, parserName='scheme')
                    # eq___new.astScheme = sgp.getAST___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    # eq___new.rootOfTree = sgp.getRootOfTree___oStr() # this is not renamed...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    # eq___new.startPos__nodeIdScheme = sgp.startPos__nodeId___oStr
                    # eq___new.nodeId__lenScheme = sgp.getNodeId__len___oStr()# this is schemeNodeLen, not schemeLabelLen, nodeId needs to be recalculated
                    # if sgp.oStr not in visitedSchemeStrs:
                    if manipulatedSchemeWord not in visitedSchemeStrs:
                        history___new = deepcopy(history); unHistory___new = deepcopy(unHistory)
                        history___new.append((idd['filename'], idd['direction'], idd['idx']))
                        reverseDirection = 'vor' if idd['direction'] == 'hin' else 'hin'
                        unHistory___new.append((idd['filename'], reverseDirection, idd['idx']))
                        visitedSchemeStrs.append(manipulatedSchemeWord)# visitedSchemeStrs.append(sgp.oStr)
                        #
                        if len(manipulatedSchemeWord) < schemeLeastLength:
                            solvingSteps = []
                            leastLengthSchemeEquations = []
                            schemeLeastLength = len(manipulatedSchemeWord)
                        if len(manipulatedSchemeWord) == schemeLeastLength:
                            leastLengthSchemeEquations.append(manipulatedSchemeWord)
                            solvingSteps.append(history___new)
                        #
                        #priority settings
                        #Heuristics: stack simplifications together, here the more experience the better
                        priority = -(depth+1) #Heuristics: if it can reach more reducingManipulation, then higher priority<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        #
                        childDict = {
                            'eq':Equation(manipulatedSchemeWord, parserName='scheme'),
                            'depth':depth+1,
                            'history':history___new,
                            'unHistory':unHistory___new#the equivalent of history, but in reverse fo each item in history
                        }
                        priorityQueue.insert(childDict, priority)
                        #
                        # print(visitedSchemeStrs); 
                        # pp.pprint({
                        #     'eq':eq___new.schemeStr,
                        #     'depth':depth+1,
                        #     'history':history___new,
                        #     'unHistory':unHistory___new#the equivalent of history, but in reverse fo each item in history
                        # });import pdb;pdb.set_trace()
                        #
                        #heuristics, if a certain type of history has been tried before, reorder the priority_queue to try something new?
                        #heuristics, so there are simplification_patterns where the nodes decrease from iPattern to oPattern, these should also serve as targets, so formulas that have the most potential to be matched by these patterns, should be given higher priority..<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        #heuristics, if we can simplify until there is only 1 of each variable, we can solve for anyVariable, by makeSubject<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        
                    # else: #if we visit the same formula again... and there is a smaller depth? like in bellmanFord, add a new pattern? but the maintenance will have to give it a name
        # print('we actually finished running, this was not expected', visitedSchemeStrs)
        # minStrLen = min(map(lambda s: len(s), visitedSchemeStrs)) # but some schemeStrings with same length, might be unfactorised, have 2 as a factor, instead of 1, for example. 
        # minSchemeStrs = sorted(list(filter(lambda s: len(s)==minStrLen, visitedSchemeStrs)))
        #but i also need the solving steps..<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #with the least number of variables, and least number of non1s?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # return minSchemeStrs

        #return solutions with the least number of variables, and least number of non1s along with their 
        from foundation.automat.parser.sorte.schemeparser import Schemeparser# prevent circular_import
        minimumVariableCount = sys.maxsize; 
        minimumNon01Count = sys.maxsize;
        chosenSchemeStrs = []; chosenASTs = []; chosenRootOfTrees = []; chosenVariables = []
        chosenIndices = []
        for idx, schemeStr in enumerate(leastLengthSchemeEquations):
            schemeparser = Schemeparser(equationStr=schemeStr)
            ast, functions, variables, primitives, totalNodeCount, startPos__nodeId = schemeparser._parse()
            totalVariableCount = sum(list(functions.values()))
            totalNon01Count = sum(list(map(lambda t: t[1], filter(lambda t: t[0] not in ['0', '1'], primitives.items()))))
            if totalVariableCount < minimumVariableCount or totalNon01Count < minimumNon01Count:
                minimumVariableCount = totalVariableCount
                minimumNon01Count = totalNon01Count
                chosenSchemeStrs = []; chosenASTs = []; chosenRootOfTrees = []; chosenVariables = []
                chosenIndices = []
            if totalVariableCount == minimumVariableCount or totalNon01Count == minimumNon01Count:
                chosenSchemeStrs.append(schemeStr); chosenASTs.append(ast); chosenRootOfTrees.append(schemeparser.rootOfTree); chosenVariables.append(list(set(variables.values())))
                chosenIndices.append(idx)
        #get the few with the smallest history
        chosenSchemeStrWithSolvingSteps = []; 
        relevantSolvingSteps = list(filter(lambda t: t[0] in chosenIndices, enumerate(solvingSteps)))
        smallestHistoryLength = min(list(map(lambda idx_solvingStep: len(idx_solvingStep[1]), relevantSolvingSteps)))
        for idx, solvingStep in relevantSolvingSteps:
            if len(solvingStep) == smallestHistoryLength:
                theIdx = chosenIndices.index(idx)
                ss = chosenSchemeStrs[theIdx]
                chosenSchemeStrWithSolvingSteps.append({
                    'schemeStr':ss,
                    'solvingStep':solvingStep,
                    'ast':chosenASTs[theIdx],
                    'rootOfTree':chosenRootOfTrees[theIdx],
                    'variables':chosenVariables[theIdx]
                })
        return chosenSchemeStrWithSolvingSteps


    @classmethod
    def _loadYAMLFromFilePath(cls, filepath):
        with open(filepath, 'r') as f:
            data = safe_load(f)
            return data