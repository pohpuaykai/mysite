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
    def _loadYAMLFromFilePath(cls, filepath):
        with open(filepath, 'r') as f:
            data = safe_load(f)
            return data