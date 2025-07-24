from copy import copy, deepcopy
from enum import Enum
import re

from foundation.automat.arithmetic.function import Function
from foundation.automat.common import BinarySearch, isNum, lenOrZero, FindTreeInTree
from foundation.automat.parser.parser import Parser

class BracketType(Enum):
    ROUND = '(', ')'
    SQUARE = '[', ']'
    CURLY = '{', '}'

    def openBras():
        return list(map(lambda member: member.value[0], BracketType.__members__.values()))

    def closeBras():
        return list(map(lambda member: member.value[1], BracketType.__members__.values()))

    def allBras():
        return BracketType.openBras() + BracketType.closeBras()


class EntityType(Enum):
    PURE_NUMBER = 'pure_number'
    IMPLICIT_INFIX = 'implicit_infix'
    PURE_VARIABLE = 'pure_variable'
    BACKSLASH_VARIABLE = 'backslash_variable'
    BACKSLASH_FUNCTION = 'backslash_function'
    BACKSLASH_NUMBER = 'backslash_number'
    PURE_INFIX = 'pure_infix'
    BACKSLASH_INFIX = 'backslash_infix'
    COMPOSITE_VARIABLE = 'composite_variable' # example V^{Q1}_{BE}, Voltage between B and E of transistor Q1
    MATRIX = 'matrix'

    FROM_CONVERSION = 'from_conversion' # entities added pendant conversion of latexAST to schemeAST

class Latexparser(Parser):
    
    """
    Naive Parser for Latex Strings. More details about 'Latex' format, check
    https://www.latex-project.org/help/documentation/classes.pdf

    More concise guide to LaTeX mathematical symbols (courtsey of Rice University):
    https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf
    offline copy in parser.docs as "symbols.pdf"

    According to :- https://sg.mirrors.cicku.me/ctan/info/symbols/comprehensive/symbols-a4.pdf

    $ % _ } & # {  are special characters, 
    we will pretend that %, & and # does not exist, since we are not doing matrices for now

    Also according to https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes#Adding_math_to_LaTeX
    we need to enclose the MATH equation with one of these:
    1. \[ \]
    2. $ $
    3. \begin{displaymath} \end{displaymath}
    4. \begin{equation} \end{equation}

    But we will assume that there is no need for that now, and only when user execute toString, 
    will we return with enclosed \[\]
    
    restructuring
    
    
    
    new symbols to parse and check:
    \integral
    \lim  (\to is an infix)
    \sum  (this one has equals = at the base)
    \prod  (this one has equals = at the base)
    \nabla
    \Delta
    \partial
    \cdot (dot product)
    (cross product)
    
    determinant (simplified as det?? only?)
    also 
    \begin{vmatrix}\end{vmatrix}
    \begin{Vmatrix}\end{Vmatrix}
    
    matrices:
    starts with \begin{pmatrix}|\begin{bmatrix}|\begin{matrix}, needs to end with the same
    Within all \begin, '&' delimits the column, '\\' delimits the row
    
    
    MATRIX: each matrix cell to be treated as a Latex formula. So we write whole matrix as a node on AST for now. then recursively parse each matrix_cell into AST. (treat matrix as multi-input function).
    
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO remove all the useless_methods, add a summary of this in comments here
            
    go through all items, looking at inputs of each, create nodeId to list[nodeId] dictionary, store as latex tree
    
    ~~~Handle special cases of Latex~~~
    1. (sqrt a) => (nroot 2 a)
    2. (ln a) => (log e a)
    3. (log a) => (log 10 a)
    4. (frac a b) => (/ a b)
    5. (TRIG p t) => (^ (TRIG t) p)
    WHAT ABOUT THE NEW FUNCTIONS?
    6. 
    
    ~~~Get statistics~~~
    1. totalNodeCount
    2. functions count
    3. primitives count
    4. variables count
    
    
    >>>>>>>>> 10x UNIT TEST FIRST
    
    recursively, call this function on each cell in matrix
    """
    #\cdot is vector dot product  #\times is vector cross product
    BACKSLASH_INFIX = ['\\to', '\\times', '\\cdot','\\%']#vectors op prioritised over backslash
    PRIOIRITIZED_INFIX = [ '^', '/','//', '*', '-', '+']#['^', '/', '*', '-', '+'] 
    INFIX = BACKSLASH_INFIX+PRIOIRITIZED_INFIX+['='] #the smaller the number the higher the priority
    OPEN_BRACKETS = ['{', '[', '(']
    CLOSE_BRACKETS = ['}', ']', ')']
    close__open = dict(zip(CLOSE_BRACKETS, OPEN_BRACKETS))
    open__close = dict(zip(OPEN_BRACKETS, CLOSE_BRACKETS))

    ##### PUT BACK LATER
    TRIGOFUNCTION = Function.TRIGONOMETRIC_NAMES() # then no need to map between latex and scheme
    # TRIGOFUNCTION = ['arccos', 'cos', 'arcsin', 'sin', 'arctan', 'tan', 
    # 'arccsc', 'csc', 'arcsec', 'sec', 'arccot', 'cot', 'arsinh', 'sinh', 'arcosh', 'cosh', 
    # 'artanh', 'tanh', 'arcsch', 'csch', 'arsech', 'sech', 'arcoth', 'coth']
    ######


    def getLatexSpecialCases(self, funcName, reverse=False):
        """
        True|False is "whether or not this node is optional to output", 

        resultTemplate:[
( ((), ), [ ((), ), ((), ), ...]) # top row to match input row ((funcName, nodeId), True|False, templateId)

]
        """
        def addTrig():
            l = {}
            for trigFuncName in Latexparser.TRIGOFUNCTION:
                l[trigFuncName] = {
                    'inputTemplate':( ((trigFuncName, '$0'), False, 0), [ (('$1', '$2'), True, 1), (('$3', '$4'), False, 2)]),
                    'outputTemplate':[
                        ( ((trigFuncName, '$0'), False, 0), [ (('$3', '$4'), False, 1)]),
                        ( (('^', '$5'), True, 2), [ ((trigFuncName, '$0'), False, 0), (('$1', '$2'), False, 3)]) # if parentNode is present, then Are_the_children_optional?
                    ],
                    'insertToEntityStorage':['^'],
                    'rootOfResultTemplate': 2,# for parent replacement in childrenList
                    'reverseTag':trigFuncName,
                    'reversePriority':0
                }
            return l
        LATEX_SPECIAL_CASES = {
            'sqrt': {
                'inputTemplate':( (('sqrt', '$0'), False, 0), [ (('$1', '$2'), True, 1), (('$3', '$4'), False, 2)]),
                'outputTemplate':[
                    ( (('nroot', '$0'), False, 0), [ (('$1', '$2'), False, 1), (('$3', '$4'), False, 2)]),
                ],
                'insertToEntityStorage':[],
                'var__defaults':{'$1':'2'},
                'rootOfResultTemplate': 0,# for parent replacement in childrenList
                'reverseTag':'nroot',
                'reversePriority':0
            },
            'ln':{
                'inputTemplate':( (('ln', '$0'), False, 0), [ (('$3', '$4'), False, 2)]),
                'outputTemplate':[
                    ( (('log', '$0'), False, 0), [ (('$1', '$2'), False, 1), (('$3', '$4'), False, 2)]),
                ],
                'var__defaults':{'$1':'e'},
                'insertToEntityStorage':[],
                'rootOfResultTemplate': 0,# for parent replacement in childrenList
                'reverseTag':'log',
                'reversePriority':0

            },
            'log':{
                'inputTemplate':( (('log', '$0'), False, 0), [ (('$1', '$2'), True, 2), (('$3', '$4'), False, 3)]),
                'outputTemplate':[
                    ( (('log', '$0'), False, 0), [ (('$1', '$2'), True, 2), (('$3', '$4'), False, 3)]),
                ],
                'var__defaults':{'$1':'10'},
                'insertToEntityStorage':[],
                'rootOfResultTemplate': 0,# for parent replacement in childrenList
                'reverseTag':'log',
                'reversePriority':1
            },
            'frac':{
                'inputTemplate':( (('frac', '$0'), False, 0), [ (('$1', '$2'), False, 1), (('$3', '$4'), False, 2)]),
                'outputTemplate':[
                    ( (('/', '$0'), False, 0), [ (('$1', '$2'), False, 1), (('$3', '$4'), False, 2)]),
                ],
                'insertToEntityStorage':[],
                'rootOfResultTemplate': 0,# for parent replacement in childrenList
                'reverseTag':'/',
                'reversePriority':0
            },
        }
        LATEX_SPECIAL_CASES.update(addTrig())
        if reverse:
            list_instructions = []
            for _, instructions in LATEX_SPECIAL_CASES.items():
                if instructions['reverseTag'] == funcName:
                    list_instructions.append(instructions)
            return list_instructions
        else:
            return LATEX_SPECIAL_CASES.get(funcName)



    def getPriority(self, funcName):
        if funcName == 'frac':
            funcName = '/'
        if funcName not in self.INFIX:
            # return len(self.INFIX)
            return float('inf') # lowest priority
        return self.INFIX.index(funcName)


    BACKSLASH_EXPECTED_INPUTS = { #all possible returns according to input_type, for easy collating


        '(C)': [#['ln', 'det']
                {'argId':0, 'preSym':'', 'optional':False, 'openBra':'(', 'closeBra':')', 'braOptional':'False'}
        ],
        '[O]{C}': [#['sqrt']
                {'argId':0, 'preSym':'', 'optional':True, 'openBra':'[', 'closeBra':']', 'braOptional':'False'},
                {'argId':1, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
        ],
        '^{O}(C)': [#['TRIG']
                {'argId':0, 'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'argLen<2'}, #exponential
                {'argId':1, 'preSym':'', 'optional':False, 'openBra':'(', 'closeBra':')', 'braOptional':'False'} # angle
        ],
        '_{C}{C}': [#['lim']
                {'argId':0, 'preSym':'_', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'argLen<2'},
                {'argId':1, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
        ],

        '_{O}^{O}{C}': [#[int']
                {'argId':0, 'preSym':'_', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':1, 'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':2, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
            ],
        '_{C}^{C}{C}': [#['sum', 'prod']
                {'argId':0, 'preSym':'_', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':1, 'preSym':'^', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':2, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
            ],




        '_{C}^{O}{C}': [#['iint', 'iiint', 'oint', 'oiint']
                {'argId':0, 'preSym':'_', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':1, 'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':2, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
            ],




        '_{O}(C)': [#['log']
                    {'argId':0, 'preSym':'_', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'argLen<2'},
                    {'argId':1, 'preSym':'', 'optional':False, 'openBra':'(', 'closeBra':')', 'braOptional':'False'}
            ],




        '_{O}^{O}{C}': [#['partial', 'Delta']
                    {'argId':0, 'preSym':'_', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                    {'argId':1, 'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                    {'argId':2, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
                ],




        '_{O}^{O}{O}': [#['nabla']
                    {'argId':0, 'preSym':'_', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                    {'argId':1, 'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                    {'argId':2, 'preSym':'', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
                ],

        '{C}': [#VARIABLENAMESTAKEANARG
                    {'argId':0, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
            ],




        '{C}{C}': [#['frac']
                    {'argId':0, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                    {'argId':1, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
            ]


    }#argId is for ASTree building
    
    def _getExpectedBackslashInputs(self, funcName):
        """
        
        preSym is the prefix for the input. 
        optional is if the preSym is necessary (TODO convert to enum? ENUM)
        openBra is the opening_delimiter of input
        closeBra is the closing_delimiter of input
        braOptional is if the openBra and closeBra are optional. (TODO convert to enum? ENUM) 
        
        {   '(C)': ['ln', 'det'],
    '[O]{C}': ['sqrt'],
    '^{O}(C)': ['TRIG'],

    '_{C}(C)': ['lim'],
    '_{C}^{O}{O}':['int'],
    '_{C}^{C}{C}': ['sum', 'prod'],
    '_{C}^{O}{C}': ['iint', 'iiint', 'oint', 'oiint'],
    '_{O}(C)': ['log'],
    '_{O}^{O}{C}': ['partial', 'nabla', 'Delta'],
    '_{O}^{O}{O}':['nabla'].
    '{C}': ['VARIABLENAMESTAKEANARG'],
    '{C}{C}': ['frac']}
        """
        if funcName in ['ln', 'det']:
            return self.BACKSLASH_EXPECTED_INPUTS['(C)']
        if funcName in ['sqrt']:
            return self.BACKSLASH_EXPECTED_INPUTS['[O]{C}']
        if funcName in self.TRIGOFUNCTION:
            return self.BACKSLASH_EXPECTED_INPUTS['^{O}(C)']
        if funcName in ['lim']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{C}{C}']
        if funcName in ['int']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{O}^{O}{C}']
        if funcName in ['sum', 'prod', 'int']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{C}^{C}{C}']
        if funcName in ['iint', 'iiint', 'oint', 'oiint']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{C}^{O}{C}']
        if funcName in ['log']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{O}(C)']
        if funcName in ['partial', 'Delta']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{O}^{O}{C}']
        if funcName in ['nabla']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{O}^{O}{O}']
        if funcName in self.VARIABLENAMESTAKEANARG:
            return self.BACKSLASH_EXPECTED_INPUTS['{C}']
        if funcName in ['frac']:
            return self.BACKSLASH_EXPECTED_INPUTS['{C}{C}']


    #TODO move this up to BACKSLASH_EXPECTED_INPUTS ??
    VARIABLENAMESTAKEANARG = ['overline', 'underline', 'widehat', 'widetilde', 'overrightarrow', 'overleftarrow', 'overbrace', 'underbrace'
    #Math mode accents
    'acute', 'breve', 'ddot', 'grave', 'tilde', 'bar', 'check', 'dot', 'hat', 'vec'
    ] # these 'functions' must be preceded by {
    """['arccos', 'cos', 'arcsin', 'sin', 'arctan', 'tan', 
    'arccsc', 'csc', 'arcsec', 'sec', 'arccot', 'cot', 'arsinh', 'sinh', 'arcosh', 'cosh', 
    'artanh', 'tanh', 'arcsch', 'csch', 'arsech', 'sech', 'arcoth', 'coth']"""
    #INTEGRALS = ['int', 'oint', 'iint'] # TODO hikitoru this from sfunctors # remove
    #FUNCTIONNAMES = TRIGOFUNCTION + ['frac', 'sqrt',  'log', 'ln'] + INTEGRALS # remove?
    EXCLUDE_BACKSLASH_INFIX = list(map(lambda s: s.replace('\\', ''), BACKSLASH_INFIX))#['to'] #because its an infix
    
    def __init__(self, equationStr=None, ast=None, rootOfTree=None, verbose=False):
        self.verbose=verbose
        self.parserName = 'latex'#VAR:inheritance

        if ast is None: # parse Mode
            self.equationStr = equationStr #processed rawEquationStr
            self.matrices_pos_type = None # replace with entitystorage, the collating of intervals (bubble merge) needs work
            self.allBrackets = None # all of the bracket STATIC, 
            self.openBraPos__bracketId = None # STATIC
            self.bracketstorage = BracketStorage()
            self.entitystorage = EntityStorage(equationStr=self.equationStr)
            self.mabracketstorage = BracketStorage() #VAR: matrix
            self.mabracketstorageDefault = BracketType.ROUND
            self.bsbracketstorage = BracketStorage() #VAR: backslash
            self.bsbracketstorageDefault = BracketType.ROUND
            self.list_openTagPos = None
            self.list_closeTagPos = None
            self.openTagPos__closeTagPos = None
            self.closeTagPos__openTagPos = None
            self.occupiedPositions = []
            self.overallEqual_startPos = None # includes 0, and len(self.equationStr)-1
            self.overallEqual_nodes = None # element: ('=', nodeId)
            self.all_preSym_pos = None

            self.latexAST = None #VAR:OUTPUTS
            self.rootOfTree = None
            self.functions, self.variables, self.primitives, self.totalNodeCount, = None, None, None, None #VAR:OUTPUTS
            self.list_of_ast_roots = []
        else: # unparse Mode
            self.ast = ast
            self.rootOfTree = rootOfTree
            self.leaves = set()
            self.backslashes ={}
            self.nodeIdToInfixArgsBrackets = {}
    

    def _find_matrices(self):
        """
        
        I can only think of 3 ways to do this? Implement one first, and then later do both, and parallelise
        1. go character by character
        2. use re.findall, match outer \\begin\\end <<<<<<<<<< we going with this
        3. str.find, chop and str.find, and then match outer \\begin\\end
        
        """
        self.matrices_pos_type = []
        #skip_bracket_accounting
        list_tuple_pos_tagType = []
        startTagEndPos__startTagStartPos = {}
        endTagStartPos__endTagEndPos = {}
        for startTagStartPos, startTagEndPos, startTagName in map(lambda m: (m.start(), m.end(), m.group(1)), re.finditer(r"\\begin\{(\wmatrix)\}", self.equationStr)):
            startTagEndPos__startTagStartPos[startTagEndPos] = startTagStartPos
            list_tuple_pos_tagType.append((startTagEndPos, True, startTagName, startTagStartPos)) # True is open

        for endTagStartPos, endTagEndPos, endTagName in map(lambda m: (m.start(), m.end(), m.group(1)), re.finditer(r"\\end\{(\wmatrix)\}", self.equationStr)):
            endTagStartPos__endTagEndPos[endTagStartPos] = endTagEndPos
            list_tuple_pos_tagType.append((endTagStartPos, False, endTagName, endTagEndPos)) # False is close

        # import pdb;pdb.set_trace()

        tagName__openPosStack = {}
        for innerPos, isOpen, tagName, keepPos in sorted(list_tuple_pos_tagType, key=lambda tup: tup[0]): # if pos touch, then sort is bad
            openPosStack = tagName__openPosStack.get(tagName, [])
            if isOpen:
                openPosStack.append((keepPos, innerPos))
            else:
                #found a matchingClose at pos
                openPos, openInnerPos = openPosStack.pop()
                nodeId = self.entitystorage.insert(tagName, openPos, keepPos, EntityType.MATRIX, None, None, openPos, keepPos)
                self.matrices_pos_type.append(
                        {
                            'nodeId':nodeId,
                            'funcType':'matrix',
                            'funcName':tagName,
                            'funcStart':openPos,
                            'funcEnd':keepPos,
                            'widthStart':openPos,
                            'widthEnd':keepPos,
                            'innerStartPos':openInnerPos,#only for matrices
                            'innerEndPos':innerPos,#only for matrices
                            'args':[]
                        }
                )
            tagName__openPosStack[tagName] = openPosStack


        #TODO this works like bubble_merge, if bubble_merge is not used anymore, please remove. Or replace this with bubble_merge. easier to analyse
        """#the main difference between this and bubble_merge is that bubble_merge tells you which bubbles are merge together?
        ~~PREPARING FOR MATRIX CONTAINMENT QUERY~~  isPosInMatrixTag

        split into list_openTagPos, list_closeTagPos
        openTagPos__closeTagPos
        closeTagPos__openTagPos

        Add new newTag = (openTagPos, closeTagPos)
        if len(list_openTagPos) == 0:
            add to both list_openTagPos and list_closeTagPos
        
        closeInOpenIdx = BS closeTagPos in list_openTagPos
        openInCloseIdx = BS openTagPos in list_closeTagPos

        ***all i in list_openTagPos, i<closeInOpenIdx will be merged with newTag at_this_point
        ***all i in list_closeTagPos, openInCloseIdx<i will be merged with newTag at_this_point
        set__openTagPos = filter(i<closeInOpenIdx, list_openTagPos)
        set__closeTagPos = filter(openInCloseIdx<i, list_closeTagPos)
        ***0. existing_open in newTag; 1. existing_close in newTag 2. both 0&1 at_this_point
        set__embedded = set__openTagPos.intersection(set__closeTagPos)  [2]
        set__openTagPos = set__openTagPos - set__embedded  [0]
        set__closeTagPos = set__closeTagPos - set__embedded  [1]
        
        [2] #whole_tag_got_EATEN
        REMOVE set__embedded FROM list_openTagPos; list_closeTagPos; openTagPos__closeTagPos; closeTagPos__openTagPos
        BSADD openTagPos to list_openTagPos
        BSADD closeTagPos to list_closeTagPos
        ADD (openTagPos, closeTagPos) to openTagPos__closeTagPos
        ADD (closeTagPos, openTagPos) to closeTagPos__openTagPos

        [0] #opens_got_EATEN
        REMOVE set__openTagPos FROM list_openTagPos; openTagPos__closeTagPos; closeTagPos__openTagPos
        IF NOT ALREADY ADDED from [2]:
            BSADD openTagPos to list_openTagPos
            ADD (openTagPos, closeTagPos) to openTagPos__closeTagPos
            ADD (closeTagPos, openTagPos) to closeTagPos__openTagPos

        [1] #closes_got_EATEN
        REMOVE set__closeTagPos FROM list_closeTagPos; openTagPos__closeTagPos; openTagPos__closeTagPos
        IF NOT ALREADY ADDED from [2]|[1]:
            BSADD closeTagPos to list_closeTagPos
            ADD (openTagPos, closeTagPos) to openTagPos__closeTagPos
            ADD (closeTagPos, openTagPos) to closeTagPos__openTagPos

        ***there is NON_OVERLAPPING_NON_REPEATING_INTERVALS: list_openTagPos (sorted), list_closeTagPos (sorted), openTagPos__closeTagPos, closeTagPos__openTagPos at_this_point
        #we need some way for the user to check if pos is in any of the above intervals
        #we copy from BracketStorage.getTightestEnclosingPos (should this be refactored into a shared method? TODO)

        Find 
        closest_close_left_of_pos :
        closest_open_right_of_pos :
         in id__tuple_openPos_openBraType_closePos_closeBraType
         remove all tuple__closePos<=closest_close_left_of_pos
         remove all tuple__openPos>=closest_open_right_of_pos
        if empty, there is no enclosing brackets for pos
        """

        list_openTagPos, list_closeTagPos, openTagPos__closeTagPos, closeTagPos__openTagPos = [], [], {}, {}
        if len(self.matrices_pos_type) > 0:
            for template in self.matrices_pos_type:
                openTagPos, closeTagPos = template['widthStart'], template['widthEnd']
                openTagPos__closeTagPos[openTagPos] = closeTagPos
                closeTagPos__openTagPos[closeTagPos] = openTagPos

            for template in self.matrices_pos_type:
                openTagPos, closeTagPos = template['widthStart'], template['widthEnd']
                insertIdx = BinarySearch.binarySearchPre(list_openTagPos, openTagPos)
                list_openTagPos.insert(insertIdx, openTagPos)

                insertIdx = BinarySearch.binarySearchPre(list_closeTagPos, closeTagPos)
                list_closeTagPos.insert(insertIdx, closeTagPos)


                closeInOpenIdx = BinarySearch.binarySearchPre(list_openTagPos, closeTagPos)
                openInCloseIdx = BinarySearch.binarySearchPre(list_closeTagPos, openTagPos)
                
                closeInOpenPos = float('-inf') # means nothing is intersecting with closeTagPos
                if 0<= closeInOpenIdx and closeInOpenIdx < len(list_openTagPos):
                    closeInOpenPos = list_openTagPos[closeInOpenIdx]

                openInClosePos = float('inf') # means nothing is intersecting with openTagPos
                if 0<= openInCloseIdx and openInCloseIdx < len(list_closeTagPos):
                    openInClosePos = list_closeTagPos[openInCloseIdx]


                set__openTagPos = set(filter(lambda pos: pos<closeInOpenPos, list_openTagPos)) #if empty, means nothing in list_openTagPos intersect with closeBra of template
                set__closeTagPos = set(filter(lambda pos: openInClosePos<pos, list_closeTagPos)) #if empty, means nothing in list_closeTagPos intersect with openBra of template

                #convert openTagPos to close, and then do intersection, and then 
                set__openEmbedded = set(map(lambda i: closeTagPos__openTagPos[i], set__closeTagPos)).intersection(set__openTagPos)  #[2]
                set__closeEmbedded = set(map(lambda i: openTagPos__closeTagPos[i], set__openTagPos)).intersection(set__closeTagPos)  #[2]
                set__openTagPos = set__openTagPos - set__openEmbedded  #[0]
                set__closeTagPos = set__closeTagPos - set__closeEmbedded  #[1]

                #[2] #whole_tag_got_EATEN
                added = False
                if len(set__openEmbedded) > 0:
                    # REMOVE set__embedded FROM list_openTagPos; list_closeTagPos; openTagPos__closeTagPos; closeTagPos__openTagPos
                    for i in set__openEmbedded:
                        list_openTagPos.remove(i)
                        if i in openTagPos__closeTagPos:
                            del openTagPos__closeTagPos[i]

                    for i in set__closeEmbedded:
                        list_closeTagPos.remove(i)
                        if i in closeTagPos__openTagPos:
                            del closeTagPos__openTagPos[i]

                    #BSADD openTagPos to list_openTagPos
                    #TODO replace with BinarySearch.binarySearchIdx(l, findMe, approximate=True)
                    #<<<<<<<<<<<<<<<<<<<<remove the EATEN tag from list_openTagPos
                    insertIdx = BinarySearch.binarySearchPre(list_openTagPos, openTagPos)
                    list_openTagPos.insert(insertIdx, openTagPos)

                    #BSADD closeTagPos to list_closeTagPos
                    #TODO replace with BinarySearch.binarySearchIdx(l, findMe, approximate=True)
                    #<<<<<<<<<<<<<<<<<<<<remove the EATEN tag from list_closeTagPos
                    insertIdx = BinarySearch.binarySearchPre(list_closeTagPos, closeTagPos)
                    list_closeTagPos.insert(insertIdx, closeTagPos)

                    #ADD (openTagPos, closeTagPos) to openTagPos__closeTagPos
                    openTagPos__closeTagPos[openTagPos] = closeTagPos

                    #ADD (closeTagPos, openTagPos) to closeTagPos__openTagPos
                    closeTagPos__openTagPos[closeTagPos] = openTagPos

                    added = True


                #[0] #opens_got_EATEN
                if len(set__openTagPos) > 0:
                    """

        REMOVE set__openTagPos FROM list_openTagPos; openTagPos__closeTagPos; closeTagPos__openTagPos
        IF NOT ALREADY ADDED from [2]:
            BSADD openTagPos to list_openTagPos
            ADD (openTagPos, closeTagPos) to openTagPos__closeTagPos
            ADD (closeTagPos, openTagPos) to closeTagPos__openTagPos
                    """
                    for i in set__openTagPos:
                        list_openTagPos.remove(i)
                        if i in openTagPos__closeTagPos:
                            del openTagPos__closeTagPos[i]
                    if not added:
                        #TODO replace with BinarySearch.binarySearchIdx(l, findMe, approximate=True)
                        insertIdx = BinarySearch.binarySearchPre(list_openTagPos, openTagPos)
                        list_openTagPos.insert(insertIdx, openTagPos)

                        added = True

                #[1] #closes_got_EATEN
                if len(set__closeTagPos) > 0:
                    """

        REMOVE set__closeTagPos FROM list_closeTagPos; openTagPos__closeTagPos; openTagPos__closeTagPos
        IF NOT ALREADY ADDED from [2]|[1]:
            BSADD closeTagPos to list_closeTagPos
            ADD (openTagPos, closeTagPos) to openTagPos__closeTagPos
            ADD (closeTagPos, openTagPos) to closeTagPos__openTagPos
                    """
                    for i in set__closeTagPos:
                        list_closeTagPos.remove(i)
                        if i in closeTagPos__openTagPos:
                            del closeTagPos__openTagPos[i]
                    if not added:
                        #TODO replace with BinarySearch.binarySearchIdx(l, findMe, approximate=True)
                        insertIdx = BinarySearch.binarySearchPre(list_closeTagPos, closeTagPos)
                        list_closeTagPos.insert(insertIdx, closeTagPos)

                        added = True

        #collate all the matrix_start_end_tag, like bubblemerge, then we get many non-overlapping intervals
        #collate all non-overlaping intervals, to removed for leftover-finding
        #put it all in a new bracketStorage
        # self.mabracketstorageDefault = BracketType.ROUND
        self.mabracketstorageDefaultOpen = self.mabracketstorageDefault.value[0]
        self.mabracketstorageDefaultClose = self.mabracketstorageDefault.value[1]
        # self.mabracketstorage = BracketStorage()#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<move to EntityStorage TODO
        for openTagPos, closeTagPos in openTagPos__closeTagPos.items():
            self.mabracketstorage.insertBracket(self.mabracketstorageDefaultOpen, openTagPos, self.mabracketstorageDefaultClose, closeTagPos)


    def _processEachElementOfMatrix(self):#This can be done in parallel with the main_process<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
        # print(self.matrices_pos_type)
        for matrixPropDict in self.matrices_pos_type:
            for rowIdx, row in enumerate(self.equationStr[matrixPropDict["innerStartPos"]:matrixPropDict["innerEndPos"]].split("\\")):
                for colIdx, cell in enumerate(row.split("&")):
                    print(cell, (rowIdx, colIdx), '********************')
                    parser = Latexparser(cell, verbose=self.verbose)#TODO cannot handle single letter E
                    parser._parse()
                    print(parser.ast) # might be empty, if there is only 1 leaf
                    print(str(parser.entitystorage))
                    #may be a third tag for matrix position? in the same tree? Or keep a seperate nodeId__tuple_matrixNodeId_rowIdx_colIdx?
                    #should we MINIMALLY merge the entitiestorageS of each cell together?
                    #merge ast back to main.... HOW to store this information with (rowIdx, colIdx)? If seperateTree, will be difficult to DFS...
                    print('***********************')
        pass


    def _find_infix(self):
        self.infix_pos_type_list = []
        for infix in self.INFIX:
            self.infix_pos_type_list += list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"{re.escape(infix)}", self.equationStr)))


        #is = enclosed_in_brackets?
        nonequals_pos_type_list = list(filter(lambda tup: tup[2]!='=', self.infix_pos_type_list))

        for start, end, group in nonequals_pos_type_list: # = should be inserted first to ensure = has smaller idx
            #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<might have gotten IMPLICIT_INFIX -
            nodeIdx = self.entitystorage.insert(group, start, end, EntityType.PURE_INFIX, widthStart=start, widthEnd=end)

    def isPosInMatrixTag(self, pos):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<move to EntityStorage TODO 

        """
        if there is matrix_tag enclosing pos, then pos is in a matrix_tag

        the first exist is because the first \\ is ignore... TODO might be a off-by-one
        """

        return self.mabracketstorage.exists(pos, self.mabracketstorageDefault, True) or\
        len(list(self.mabracketstorage.getAllEnclosingBraOfPos(pos, self.mabracketstorageDefault))) > 0

    def isPosInBackslashBrackets(self, pos):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<move to EntityStorage TODO 
        """"""
        # import pdb;pdb.set_trace()
        if pos is None:
            return False
        return self.bsbracketstorage.exists(pos, self.bsbracketstorageDefault, True) or\
        len(list(self.bsbracketstorage.getAllEnclosingBraOfPos(pos, self.bsbracketstorageDefault)))


    def _find_brackets(self):
        """
        
        2a. Keep position of all the brackets as a kind of datastorage, need to get all the 
        DO NOT INCLUDE MATRIX. (remove from OTHER_brackets)

        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<2d obsolete
        2d. check if left&right infixes (put to infix as inputs) (remove from OTHER_brackets)
        """
        # self.all_brackets_pos = []
        self.endOfOpenBraPos = []
        #skip_bracket_accounting

        openOrClose__tuple_braType = {}
        openBraTypes, closeBraTypes = set(), set()
        for k, templateList in self.BACKSLASH_EXPECTED_INPUTS.items(): # this get all the possible bracket combinations, incase Enum missed out
            for template in templateList:
                openBraTypes.add(template['openBra'])
                closeBraTypes.add(template['closeBra'])
                openOrClose__tuple_braType[template['openBra']] = (template['openBra'], template['closeBra'])
                openOrClose__tuple_braType[template['closeBra']] = (template['openBra'], template['closeBra'])

        list_tuple_pos_braType_isOpen = [] #skip_list
        openBracket_pos_type_list = []
        for openBracket in openBraTypes:
            for start, end, group in list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"\\{openBracket}", self.equationStr))):
                openBracket_pos_type_list.append((start, end, group))
                # self.all_brackets_pos.append(start)
        for start, end, openBraType in openBracket_pos_type_list:
            #TODO could have done the self.isPosInMatrixTag() here, which is more efficient?
            list_tuple_pos_braType_isOpen.append((start, openBraType, True))
            self.endOfOpenBraPos.append(end) # for add_implicit_0


        closeBracket_pos_type_list = []
        for closeBracket in closeBraTypes:
            for start, end, group in list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"\\{closeBracket}", self.equationStr))):
                closeBracket_pos_type_list.append((start, end, group))
                # self.all_brackets_pos.append(start)
        for start, end, closeBraType in closeBracket_pos_type_list:
            list_tuple_pos_braType_isOpen.append((start, closeBraType, False))
            # self.endOfOpenBraPos.append(end)


        #bracket_accounting with skip_list
        braType__openPosStack = {}
        for pos, braType, isOpen in sorted(list_tuple_pos_braType_isOpen, key=lambda tup: tup[0]):
            braType = openOrClose__tuple_braType[braType]#braType could be ( or )
            openPosStack = braType__openPosStack.get(braType, [])
            if isOpen: #pos is openPos
                openPosStack.append(pos)
            else: #pos is closePos
                openPos = openPosStack.pop()
                if self.isPosInMatrixTag(openPos):
                    continue # skip
                self.bracketstorage.insertBracket(braType[0], openPos, braType[1], pos)
            braType__openPosStack[braType] = openPosStack


        # print(str(self.entitystorage))
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$');import pdb;pdb.set_trace()

        
    def _find_backslash(self):
        """
        
        3. find start_position of all the backslashs (sqrt is special), EXCLUDE EXCLUDE_BACKSLASH like \\to, because its an infix
            3a. their _(if any) and its immediateNextBracket, their ^(if any) and its immediateNextBracket and {} [tree_building]
            3b. remove all the ^ from infixes, that are actually backslash_exponents
            3c. note its end_position, also 
            3d. occupied is only the name and the backslash
            3e. note the WHOLE_end_position (different from 2d), these are BACKSLASH
            3f. BACKSLASHES always have at most 3 inputs
            3g. remove VARIABLENAMESTAKEANARG and put in variables
        
        
        2c. DO NOT INCLUDE backslash brackets (remove backslash brackets from bracketStorage 
        
        2b. check if there is a ^(exponent), to their direct right or left (note in brackets) [tree_building]
            2b1.^ to the left (power) [only for ASTreeConstructionBODMAS, input of infix] (remove from OTHER_brackets)
            2b2.^ to the right (base) [also for implicit_multiply remove_from_OTHER_brackets_after_implicit_multiply]
        
        """
        self.all_preSym_pos = []
        set_all_possible_preSym = set()
        #for _find_variable_or_number
        for shortkey, list_template in self.BACKSLASH_EXPECTED_INPUTS.items():
            for template in list_template:
                set_all_possible_preSym.add(template['preSym'])

        import re
        list_backslashReResult = list(map(lambda m: (m.start(), m.end(), m.group(1)), re.finditer(r"\\([a-zA-Z]+)", self.equationStr)))
        for funcStart, funcEnd, funcName in list_backslashReResult:
            # print(funcStart, funcEnd, funcName);import pdb;pdb.set_trace()
            #process matrix
            if self.mabracketstorage.exists(funcStart, BracketType.ROUND, True) or \
                self.isPosInMatrixTag(funcEnd) or \
                self.mabracketstorage.exists(funcStart, BracketType.ROUND, False):
                # print(funcStart, funcEnd, funcName, 'skip');import pdb;pdb.set_trace()
                continue
            #
            if funcName in self.EXCLUDE_BACKSLASH_INFIX:
                continue
            foundType = 'backslash_function'
            if funcName in self.BACKSLASH_INFIX: # remove the backslash_infix from backslash
                self.entitystorage.remove(funcStart)
                continue
            if funcName in self.VARIABLENAMESTAKEANARG: # variable_function is actually a variable
                foundType = 'backslash_variable'
                self.bracketstorage=self.entitystorage.insert(
                    funcName, 
                    funcStart, 
                    funcEnd, 
                    EntityType.BACKSLASH_VARIABLE, widthStart=funcStart, widthEnd=funcEnd, bracketstorage=self.bracketstorage)
            list_template = self._getExpectedBackslashInputs(funcName)
            if list_template is None: # number that starts with backslash. like \\pi
                self.bracketstorage=self.entitystorage.insert(funcName, funcStart, funcEnd, EntityType.BACKSLASH_NUMBER, 
                    widthStart=funcStart, widthEnd=funcEnd, bracketstorage=self.bracketstorage)
                continue # skip args finding
            #type == BACKSLASH_FUNCTION
            if foundType == 'backslash_function':
                self.bracketstorage=self.entitystorage.insert(
                    funcName, 
                    funcStart, 
                    funcEnd, 
                    EntityType.BACKSLASH_FUNCTION, widthStart=funcStart, widthEnd=funcEnd, bracketstorage=self.bracketstorage)
            #backslash function at_this_point
            #search for immediateNextBracket inputs from m.start(), until m.end() 

            # allNonEmptyPreSym = set(filter(lambda c: len(c)>0, map(lambda template: template['preSym'], template_list))) # related to (len(template['preSym']==0)) {But i forgot in which case it was used}



            def captureUnConfirmedArg(pointerPos, closeBraType, closeBraPos):
                self.entitystorage.addUnConfirmedPCrelationship(funcStart, template['argId'], self.equationStr[pointerPos], pointerPos, closeBraType, closeBraPos)
                if closeBraType is not None:
                    # self.bracketstorage.tagAsBackslashBrackets(pointerPos)#pointerPos is openBraPos
                    self.bsbracketstorage.insertBracket(self.bsbracketstorageDefault.value[0], pointerPos, self.bsbracketstorageDefault.value[1], closeBraPos)
                    # import pdb;pdb.set_trace()
                #for backslash, we can update width here, not necessary for infix
                # print('closeBraPos', closeBraPos, 'closeBraType', closeBraType)
                self.entitystorage.widthMaxUpdate(funcStart, None, closeBraPos+lenOrZero(closeBraType))
                # print('capturedArg: ', self.equationStr[pointerPos+1:closeBraPos]);import pdb;pdb.set_trace()



            # we allow user to process template_list in any ORDER, BUT we try to search in our order first
            no_of_tries_of_optionalTemplate, MAX_NUMBER_OF_TRIES_WITH_OPTIONAL = 0, 2 # increment no_of_tries when we try an optional OR when there is only optional left
            stack = deepcopy(list_template)
            pointerPos = funcEnd
            while len(stack) > 0 and not all(map(lambda template: template['optional'], stack)) and (pointerPos<len(self.equationStr)):# \exists compulsory_template
                template = stack.pop(0)
                #START make sure we do not try optionals forever.
                if template['optional']:
                    no_of_tries_of_optionalTemplate += 1
                    if no_of_tries_of_optionalTemplate > MAX_NUMBER_OF_TRIES_WITH_OPTIONAL:
                        break # exit
                else:# compulsory -> reset no_of_tries_of_optionalTemplate
                    no_of_tries_of_optionalTemplate = 0#But Compulsory will try forever.... NOT SURE IF WE WANT THIS?
                #END make sure we do not try optionals forever.


                nextCha = self.equationStr[pointerPos]
                # print('0template', template, 'pointerPos', pointerPos, 'nextCha', nextCha);import pdb;pdb.set_trace()
                if len(template['preSym']) == 0:
                    # print('1template', template, 'pointerPos', pointerPos, 'nextCha', nextCha);import pdb;pdb.set_trace()
                    if nextCha == template['openBra']:
                        # print('2template', template, 'pointerPos', pointerPos, 'nextCha', nextCha);import pdb;pdb.set_trace()
                        closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(pointerPos)
                        captureUnConfirmedArg(pointerPos, closeBraType, closeBraPos)
                        pointerPos = closeBraPos + len(closeBraType);nextCha = self.equationStr[pointerPos] if pointerPos < len(self.equationStr) else None
                    elif template['braOptional'] == 'argLen<2' and template['braOptional'] == 'True':# NO preSym and no need bracket for argLen=1...
                        raise Exception('Ugly Template, no PreSym and no need Bracket for argLen=1')

                    else: #it should fit another template (WRONG_ORDER of our template from the_USER)
                        stack.append(template)
                        # print('PUTBACK****************************************************************************')
                        continue

                else:# len(template['preSym']) > 0
                    # print('3template', template, 'pointerPos', pointerPos, 'nextCha', nextCha);import pdb;pdb.set_trace()
                    ######################################
                    if template['preSym'] in ['^'] and nextCha in ['^']: # controlSymbols mixing with mathSymbols
                        """

            2b. check if there is a ^(exponent), to their direct right or left (note in brackets) [tree_building]
                2b1.^ to the left (power) [only for ASTreeConstructionBODMAS, input of infix] (remove from OTHER_brackets)
                2b2.^ to the right (base) [also for implicit_multiply remove_from_OTHER_brackets_after_implicit_multiply]

                        """
                        #remove from self.infixs_pos_type # TODO binarySearch, this is not very efficient, ENTITIES STORAGE.
                        # import pdb;pdb.set_trace()
                        self.entitystorage.remove(pointerPos)
                    #######################################
                    if template['preSym'] == nextCha:
                        pointerPos += len(template['preSym']);nextCha = self.equationStr[pointerPos] if pointerPos < len(self.equationStr) else None
                        # print('4template', template, 'pointerPos', pointerPos, 'nextCha', nextCha);import pdb;pdb.set_trace()
                        if nextCha == template['openBra']:
                            # print('5template', template, 'pointerPos', pointerPos, 'nextCha', nextCha);import pdb;pdb.set_trace()
                            closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(pointerPos)
                            captureUnConfirmedArg(pointerPos, closeBraType, closeBraPos)
                            pointerPos = closeBraPos + len(closeBraType);nextCha = self.equationStr[pointerPos] if pointerPos < len(self.equationStr) else None
                        elif template['braOptional'] == 'argLen<2':#nextCha doesnt match template['openBra'], but we allow argLen=1 to have no brackets
                            # 
                            captureUnConfirmedArg(pointerPos, None, pointerPos+1)
                            # print('6template', template, 'pointerPos', pointerPos, 'nextCha', nextCha);import pdb;pdb.set_trace()
                            self.bracketstorage.allOpenPosOfBackslashArgsNoBrackets.append(pointerPos)
                            pointerPos += 1;nextCha = self.equationStr[pointerPos] if pointerPos < len(self.equationStr) else None
                        elif template['braOptional'] == 'False':
                            raise Exception('Ugly Template, with PreSym but no need Brackets for argLen>1')
                        else:# it should fit another template (WRONG_ORDER of our template from the_USER)
                            stack.append(template)
                            # print('PUTBACK****************************************************************************')
                            continue
                    else:#preSym no match nextCha, and there is some preSym {it should fit another template (WRONG_ORDER of our template from the_USER)}
                        stack.append(template)
                        # print('PUTBACK****************************************************************************')
                        continue


        # print(str(self.entitystorage))
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$');import pdb;pdb.set_trace()

    def _insert_equals(self):
        """
        Again, the same 3 ways as _find_matrices
        1. go character by character
        2. use re.findall <<<<<<<<<
        3. str.find, chop and str.find, and then match outer \\begin\\end
        
        WHAT ARE OVERALLEQUAL?
        In this Symmetric Form of a line in 3D-space, there are 2 OVERALLEQUAL, they are on position 
        15, 31

        \\frac{x-x_0}{a}=\\frac{y-y_0}{b}=\\frac{z-z_0}{c}
        ^ ^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^
        0 1234567891111111 1112222222222333 33333334444444
                   0123456 7890123456789012 34567890123456

        OVERALLEQUAL seperate the equation. unlike:

        \\sum_{k=0}^{n}k=\\frac{n(n+1)}{2}
        ^ ^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^
        0 1234567891111111 111222222222233
                   0123456 789012345678901

        There are 2 =, on position 7 and position 15. The = on position 15 is OVERALLEQUAL, but the = on position 7 is NOT an OVERALLEQUAL
        """
        # self.equals_info_list = list(filter(lambda tup: tup[2]=='=', self.infix_pos_type_list)) # this equals for _find_implicit_0
        #is = enclosed_in_brackets?
        equals_pos_type_list = list(filter(lambda tup: tup[2]=='=' and not self.isPosInBackslashBrackets(tup[1]), self.infix_pos_type_list))
        # import pdb;pdb.set_trace()
        self.overallEqual_startPos = []
        for start, end, _ in equals_pos_type_list:
            ###OLD : no brackets around this =
            # isOverallEqual = False
            # for bracketType in list(BracketType.__members__.values()):
            #     selectedOpenClosePos = self.bracketstorage.getTightestEnclosingPos(start, bracketType)
            #     if selectedOpenClosePos is None:
            #         isOverallEqual = True
            #         break
            ###OLD
            isOverallEqual = True
            for bracketType in list(BracketType.__members__.values()):
                if len(list(self.bracketstorage.getAllEnclosingBraOfPos(end, bracketType))) >0:
                    import pdb;pdb.set_trace()
                    isOverallEqual = False
                    break

            if isOverallEqual:# this is a overall bracket
                self.overallEqual_startPos.append(start)
        # print('self.overallEqual_startPos', self.overallEqual_startPos)
        #overallEquals SPLIT the equationStr into equal parts
        self.overallEqual_startPos = sorted(self.overallEqual_startPos)
        self.overallEqual_startPos.insert(0, 0)
        self.overallEqual_startPos.append(len(self.equationStr)-1)#-1 so that its startPos
        start__tuple_widthStart_widthEnd = {}
        for i in range(0, len(self.overallEqual_startPos)-1):
            startPos0, startPos1 = self.overallEqual_startPos[i], self.overallEqual_startPos[i+1]
            if startPos1 != len(self.equationStr) - 1:
                #startPos1_at_key because we added 0 at the beginning that does not belong to the original list of overallEqual_startPos
                start__tuple_widthStart_widthEnd[startPos1] = (startPos0, self.overallEqual_startPos[i+2]+len('=')) 

        self.overallEqual_nodes = []
        # import pdb;pdb.set_trace()
        equals_pos_type_list = list(filter(lambda tup: tup[2]=='=', self.infix_pos_type_list))
        for start, end, group in equals_pos_type_list: # = should be inserted first to ensure = has smaller idx
            #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<might have gotten IMPLICIT_INFIX -
            if start in start__tuple_widthStart_widthEnd: # is overAllEqual
                widthStart, widthEnd = start__tuple_widthStart_widthEnd[start]
            else:
                widthStart, widthEnd = start, end # will be updated later
            nodeIdx = self.entitystorage.insert(group, start, end, EntityType.PURE_INFIX, widthStart=widthStart, widthEnd=widthEnd)
            if start in self.overallEqual_startPos:
                self.overallEqual_nodes.append(('=', nodeIdx))
        # print('self.overallEqual_nodes', self.overallEqual_nodes)


        # print(str(self.entitystorage))
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$');import pdb;pdb.set_trace()

        
    def _find_variables_or_numbers(self):
        """ RELIES on the spacing on the equationStr, please do not remove spacing from the equationStr
**** WHAT IF we take out everything that has been found so far AND all of the brackets.
**** when we get all the variables(without _{}) and numbers,
**** and then we put the _{} back to the variables that are supposed to have _{}

        """
        #collate infix|backslash|matrices pos {infix_brackets are not removed, will be a problem if infix_brackets are curly}
        #backslash_brackets ONLY
        #matrices pos THE WHOLE MATRIX, not just the tags

        def stripWithReturn(s):
            o = s.strip()
            end0 = s.find(o)
            start1 = end0+len(o)
            return o, (0, end0), (start1, len(s))

        def isNume(numStr):
            return isNum(numStr) or numStr in ['.', ',']#its a char (string with len 1)

        infixName_occupied = []
        for nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd in self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX):
            for pos in range(funcStart, funcEnd):
                infixName_occupied.append(pos)
        infixName_occupied = sorted(infixName_occupied)

        backslashName_occupied = []
        for nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd in self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.BACKSLASH_VARIABLE):
            for pos in range(funcStart, funcEnd):
                backslashName_occupied.append(pos)

        for nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd in self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.BACKSLASH_FUNCTION, EntityType.BACKSLASH_INFIX, EntityType.BACKSLASH_NUMBER):
            for pos in range(funcStart, funcEnd):
                backslashName_occupied.append(pos)
        backslashName_occupied = sorted(backslashName_occupied)

        leftOverPosList = []
        for pos in range(0, len(self.equationStr)):
            if self.isPosInMatrixTag(pos) or \
            pos in infixName_occupied or \
            pos in backslashName_occupied or \
            self.bracketstorage.isABracketPos(pos) or \
            pos in self.all_preSym_pos or\
            self.equationStr[pos] in ['_', '^', '=']: #^ and _ used as control later in this method
                continue # we skip these
            leftOverPosList.append(pos)

        # import pdb;pdb.set_trace()

        accumulator, accumulatorStartPos, accumulatorEndPos, accumulatorType, prevLeftOverPos= None, None, None, None, None
        for leftOverPos in leftOverPosList:
            leftOverChar = self.equationStr[leftOverPos]
            # print(leftOverChar)
            if accumulatorType is None:
                accumulator = leftOverChar
                accumulatorStartPos = leftOverPos
                accumulatorEndPos = accumulatorStartPos + len(leftOverChar) # len(leftOverChar) should always = 1
                accumulatorType = 'N' if isNume(leftOverChar) else 'V' # this is prevIsNume
                prevLeftOverPos = leftOverPos
            elif (accumulatorType == 'N' and not isNume(leftOverChar)) or \
            (prevLeftOverPos + 1 != leftOverPos) or (re.match(r'\s', leftOverChar)): #break off conditions: 0. going_from_N_to_V. 1. not_consecutive (excluding space)2. is whitespace
                accumulator, (_, firstRemovedEnd), (lastRemovedStart, _) = stripWithReturn(accumulator)
                accumulatorStartPos, accumulatorEndPos = accumulatorStartPos+firstRemovedEnd, accumulatorStartPos+lastRemovedStart
                if isNume(accumulator) and len(accumulator) > 0: # pure_number
                    self.bracketstorage=self.entitystorage.insert(
                    accumulator, accumulatorStartPos, accumulatorEndPos, EntityType.PURE_NUMBER, 
                    widthStart=accumulatorStartPos, widthEnd=accumulatorEndPos, bracketstorage=self.bracketstorage)#fixed width
                elif  len(accumulator) > 0: # pure variable (just not a backslash variable, can still have _{}, just need to widthMaxUpdate if we find _{})
                    self.bracketstorage=self.entitystorage.insert(
                    accumulator, accumulatorStartPos, accumulatorEndPos, EntityType.PURE_VARIABLE, 
                    widthStart=accumulatorStartPos, widthEnd=accumulatorEndPos, bracketstorage=self.bracketstorage) #width waiting for _{} later
                #reset
                accumulator = leftOverChar
                accumulatorStartPos = leftOverPos
                accumulatorEndPos = accumulatorStartPos + len(leftOverChar)
                accumulatorType = 'N' if isNume(leftOverChar) else 'V'
                prevLeftOverPos = leftOverPos
            else: # keep accumulating
                accumulator += leftOverChar
                accumulatorEndPos += len(leftOverChar)
                accumulatorType = 'N' if isNume(leftOverChar) else 'V'
                prevLeftOverPos = leftOverPos
                #startPos same. accumulatorType V->N or pure V or pure N is fine.
        #last collection
        if len(accumulator) > 0:
            accumulator, (_, firstRemovedEnd), (lastRemovedStart, _) = stripWithReturn(accumulator)
            accumulatorStartPos, accumulatorEndPos = accumulatorStartPos+firstRemovedEnd, accumulatorStartPos+lastRemovedStart
            if isNume(accumulator) and len(accumulator) > 0: # pure_number
                self.bracketstorage=self.entitystorage.insert(
                accumulator, accumulatorStartPos, accumulatorEndPos, EntityType.PURE_NUMBER, 
                widthStart=accumulatorStartPos, widthEnd=accumulatorEndPos, bracketstorage=self.bracketstorage)#fixed width
            elif  len(accumulator) > 0: # pure variable (just not a backslash variable, can still have _{}, just need to widthMaxUpdate if we find _{})
                self.bracketstorage=self.entitystorage.insert(
                accumulator, accumulatorStartPos, accumulatorEndPos, EntityType.PURE_VARIABLE, 
                widthStart=accumulatorStartPos, widthEnd=accumulatorEndPos, bracketstorage=self.bracketstorage) #width waiting for _{} later
            

        """
        4c. go through all collected_variables
            4c1. immediateRight, lookFor _{ , make them part of the variable.
            4c2. remove variable_brackets _{, from OTHER_brackets
            #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        ALSO this case:

    #if we have underscore, then caret, then es ist exponential
    equationStr = 'V^x=V^{Q_{1}}_{BE}^x' #TODO if caret follows an underscore, then its not exponential, sondern, der ganz Ding ist ein VARIABLE

    #if we have underscore, then caret, then es ist exponential
    equationStr = 'V=V^{Q_{1}}_{BE}' #TODO if caret follows an underscore, then its not exponential, sondern, der ganz Ding ist ein VARIABLE
    
    

        remove everything that is associated to the new COMPOUND_VARIABLE

        """
        # print('******************************')
        # print(str(self.bracketstorage))
        # print(str(self.entitystorage))
        # print('******************************');import pdb;pdb.set_trace()
        MAX_NUMBER_OF_TRIES_WITH_SAME_LEN_LIST = 2
        number_of_tries, last_list_len = 0, None
        pureVarsToCheckIfComposite = self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_VARIABLE)
        # print(pureVarsToCheckIfComposite)
        while len(pureVarsToCheckIfComposite) > 0:
            nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd = pureVarsToCheckIfComposite.pop(0)

            # print(nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            nextPos = funcEnd
            closeBraPos = None
            removeCaret__pos, removeCaretBra__pos = None, None
            if nextPos < len(self.equationStr) and self.equationStr[nextPos] == '^':#self.entitystorage.existEntityAt('^', nextPos): # get the exponential immediate after funcEnd <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                # print('found ^')
                caret_openBraPos = nextPos+1#self.bracketstorage.getBraPosImmediateRightOfPos(nextPos+len('^'), BracketType.CURLY, True)
                removeCaret__pos = nextPos#
                if self.equationStr[caret_openBraPos] == BracketType.CURLY.value[0]:#0 <= caret_openBraPos and caret_openBraPos < len(self.equationStr):
                    caret_closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(caret_openBraPos)
                #remove from other brackets
                    removeCaretBra__pos = caret_openBraPos#
                    nextPos = caret_closeBraPos + len(closeBraType)
                else: # a single character
                    nextPos += len('^')
                # import pdb;pdb.set_trace()
            #################
                #check if there is _ after the arg1 of the exponential immediate after funcEnd
                if nextPos < len(self.equationStr) and self.equationStr[nextPos] == '_':
                    # print('found a _'); import pdb;pdb.set_trace()
                    if removeCaret__pos:#remove FAKE EXPONENTIAL
                        self.entitystorage.remove(removeCaret__pos)#remove ^ only if its continued with _
                    openBraPos = self.bracketstorage.getBraPosImmediateRightOfPos(nextPos, BracketType.CURLY, True)
                    if self.equationStr[openBraPos] == BracketType.CURLY.value[0]: #TODO these seemed to be used together very often... condense into a method?????????????
                        closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(openBraPos)
                    #remove from other brackets
                        self.bracketstorage.removeBracket(openBraPos)
                        self.bracketstorage.removeBracket(caret_openBraPos)
                    else: #a single character
                        openBraPos, closeBraPos = funcEnd, nextPos+len('_')# +len(BracketType.CURLY.value[1]) is added later
                    # import pdb;pdb.set_trace()
                    #UPDATE width, if we found _ or ^_
                    if closeBraPos:
                        self.entitystorage.widthMaxUpdateById(nodeId, None, closeBraPos+len(BracketType.CURLY.value[1]))
                        #should update funcName, EntityType?=COMPOSITE_VARIABLE, funcEnd<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
                        # print('updating funcName:', self.equationStr[funcStart:closeBraPos+len(BracketType.CURLY.value[1])])
                        self.entitystorage.updateFuncName(nodeId, self.equationStr[funcStart:closeBraPos+len(BracketType.CURLY.value[1])])
                        self.entitystorage.updateEntityType(nodeId, EntityType.COMPOSITE_VARIABLE)
                        self.entitystorage.updateFuncEnd(nodeId, closeBraPos+len(BracketType.CURLY.value[1]))
                        self.entitystorage.removeEntityBetween(caret_openBraPos+len(BracketType.CURLY.value[0]), closeBraPos+len(BracketType.CURLY.value[1]))#funcStart, funcEnd
                        # print('removing all brackets between: ', caret_openBraPos+len(BracketType.CURLY.value[0]), ' and ', closeBraPos+len(BracketType.CURLY.value[1]))
                        self.bracketstorage.removeBracketsBetween(caret_openBraPos+len(BracketType.CURLY.value[0]), closeBraPos+len(BracketType.CURLY.value[1]))
                        #entities are changed. while(){} is better
                        pureVarsToCheckIfComposite = self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_VARIABLE)

                        #update enclosing_touching brackets
                        # self.bracketstorage = self.entitystorage._EntityStorage__updateTemplatesToWiderEnclosingBracketsAndRemove(
                        #     #takes nodeId
                        #     list(map(lambda t: t[0], self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_VARIABLE))), #has to be done here, since we need to check for superscript_pure_variableS
                        #     # self.entitystorage.getAllEndPosOfEntityType(EntityType.PURE_VARIABLE), #has to be done here, since we need to check for superscript_pure_variableS
                        #     bracketstorage=self.bracketstorage)
            else:

            #################
                #check if there is _ after the arg1 of the exponential immediate after funcEnd
                if nextPos < len(self.equationStr) and self.equationStr[nextPos] == '_':
                    # print('no ^, got _'); import pdb;pdb.set_trace()
                    openBraPos = nextPos+1#self.bracketstorage.getBraPosImmediateRightOfPos(nextPos, BracketType.CURLY, True)
                    if self.equationStr[openBraPos] == BracketType.CURLY.value[0]: 
                        closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(openBraPos)
                    #remove from other brackets
                        self.bracketstorage.removeBracket(openBraPos)
                    else: #a single character
                        openBraPos, closeBraPos = funcEnd, nextPos+len('_')# +len(BracketType.CURLY.value[1]) is added later
                        # import pdb;pdb.set_trace()

                    #UPDATE width, if we found _ or ^_
                    if closeBraPos:
                        self.entitystorage.widthMaxUpdateById(nodeId, None, closeBraPos+len(BracketType.CURLY.value[1]))
                        #should update funcName, EntityType?=COMPOSITE_VARIABLE, funcEnd<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
                        self.entitystorage.updateFuncName(nodeId, self.equationStr[funcStart:closeBraPos+len(BracketType.CURLY.value[1])])
                        self.entitystorage.updateEntityType(nodeId, EntityType.COMPOSITE_VARIABLE)
                        self.entitystorage.updateFuncEnd(nodeId, closeBraPos+len(BracketType.CURLY.value[1]))
                        # print(')))))'); import pdb;pdb.set_trace()
                        self.entitystorage.removeEntityBetween(openBraPos+len(BracketType.CURLY.value[0]), closeBraPos+len(BracketType.CURLY.value[1]))#funcStart, funcEnd
                        self.bracketstorage.removeBracketsBetween(openBraPos+len(BracketType.CURLY.value[0]), closeBraPos+len(BracketType.CURLY.value[1]))
                        #entities are changed. while(){} is better
                        pureVarsToCheckIfComposite = self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_VARIABLE)

                        #update enclosing_touching brackets
                        # self.bracketstorage = self.entitystorage._EntityStorage__updateTemplatesToWiderEnclosingBracketsAndRemove(
                        #     #takes nodeId
                        #     list(map(lambda t: t[0], self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_VARIABLE))), #has to be done here, since we need to check for superscript_pure_variableS
                        #     # self.entitystorage.getAllEndPosOfEntityType(EntityType.PURE_VARIABLE), #has to be done here, since we need to check for superscript_pure_variableS
                        #     bracketstorage=self.bracketstorage)

            # print(str(self.entitystorage))
            # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$');import pdb;pdb.set_trace()
            if last_list_len == len(pureVarsToCheckIfComposite): # try_until_nothing_to_change
                number_of_tries += 1
                if number_of_tries >= MAX_NUMBER_OF_TRIES_WITH_SAME_LEN_LIST:
                    break # stop it
            else:
                last_list_len = len(pureVarsToCheckIfComposite)
                number_of_tries = 0


        # print(str(self.entitystorage))
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$');import pdb;pdb.set_trace()


    def _find_infixes_arg_brackets_width(self):

        #NEEDS TO BE DONE BEFORE IMPLICIT(which has zero len), else, 
        """ONLY FOR infix, that backslash_function and backslash_variable's args are already found in _find_backslash
        immediate Right of Arg
            anyImmediatebracket, its corresponding close will extend its length
        immediate Left of Arg
            if we found a curly_close, it might, belong to backslash
        immediate right of arg

    6. get width(start~end) of infixes|backslash_function|backslash_variable
        6a. (by enclosing_brackets) or (by inputs) [tree_building]
        LOOK immediate LEFT&RIGHT of infix [tree_building] | but if immediate LEFT&RIGHT of infix are redundant_brackets? 
        then just update as width, and not as inputs
        6b. Check OTHER_brackets for enclosure that are wider than current_width_of_infix
        
        """
        """
        Using dictionary for widthStart__nodeId&widthEnd__nodeId is fine, because, 

        _find_infixes_backslashes_backslashvars_width
        ~got length of infix and position of infix, and inputs has to be immediate next to the infix, all the spaces are removed, so entities has to be touching

        _find_implicit_multiply
        ~entities have to be immediate next to each other, all the spaces are removed, so entities has to be touching

        _match_child_to_parent_input
        ~in _find_infixes_backslashes_backslashvars_width, we used the enclosing brackets to ensure that all entities widthStart and widthEnd are extended to the fullest, all the spaces are removed, so SLOT and entities are touching

        All require entities to be touching, so the indexing of dictionary works. (alternative was using BinarySearch on a list)
        """
        # for funcStart, funcEnd, nodeId in self.entitystorage.getAllEndPosOfEntityType(EntityType.PURE_INFIX):
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<PRIORITY is wrong
        # list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd = sorted(self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_INFIX), key=lambda t:self.INFIX.index(t[1]))
        for nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd in self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX): # by funcStart
            """
            that is direct right of 
            """
            """priority: entity; touching side bracket; enclosing bracket"""

            all_openBracket_type = list(map(lambda t: t.value[0], BracketType))
            # all_closeBracket_type = list(map(lambda t: t.value[1], BracketType))
            #right
            if self.equationStr[funcEnd] in all_openBracket_type:
                closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(funcEnd)
                if closeBraPos is None:
                    continue
                self.entitystorage.addUnConfirmedPCrelationship(funcStart, 1, self.equationStr[funcEnd], funcEnd, closeBraType, closeBraPos)
                # self.bracketstorage.removeBracket(openBraPos) # it is really ok to remove brackets at all?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                self.entitystorage.widthMaxUpdateById(nodeId, widthStart, closeBraPos)#right=End

            else:# i did not check for IMMDIATE RIGHT????? what if there are things between?
                cNodeId = self.entitystorage.getEntityImmediateRightOfPos(funcEnd) # need to remove implicit <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                cWidthEnd = self.entitystorage.nodeId__widthEnd.get(cNodeId)#WHAT IF THERE IS NO WIDTH, because cNodeId is a infix, thats not processed yet?
                self.entitystorage.widthMaxUpdateById(nodeId, widthStart, cWidthEnd)#right=End


            all_closeBracket_type = list(map(lambda t: t.value[1], BracketType))
            if self.equationStr[funcStart-1] in all_closeBracket_type:
                openBraPos, openBraType = self.bracketstorage.getCorrespondingOpenBraPos(funcStart-1)
                if openBraPos is None:
                    continue
                self.entitystorage.addUnConfirmedPCrelationship(funcStart, 0, openBraType, openBraPos, self.equationStr[funcStart-1], funcStart-1)
                # self.bracketstorage.removeBracket(closeBraPos)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                self.entitystorage.widthMaxUpdateById(nodeId, openBraPos, widthEnd)#left=Start

            else:#cannot add confirmedRelationship, because implicit multiply not in yet, implicit multiply depends on width
                cNodeId = self.entitystorage.getEntityImmediateLeftOfPos(funcStart)
                cWidthStart = self.entitystorage.nodeId__widthStart.get(cNodeId)
                self.entitystorage.widthMaxUpdateById(nodeId, cWidthStart, widthEnd)#left=Start

        # print(str(self.entitystorage))
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$');import pdb;pdb.set_trace()


    def _find_implicit_0(self):
        """
        LOOK for every -? if before - is NOT 0, then add 0?



    5. implicit_0 (-)(NOTHING_ELSE? yes every infix? example: *-5, \\to -5) need to add to the list of all infixes, indicated by length 0. need starting_position
        5a. left of (nothing|open_brackets) , 
            5a1. right of each OVERALLEquals, is a -
            5a2. search for open_brackets that have - (+ have no need of implicit_zero), to their right

        """

        def stripWithReturn(s):
            o = s.strip()
            end0 = s.find(o)
            start1 = end0+len(o)
            return o, (0, end0), (start1, len(s))


        def addImplictMinus(funcPos):
            #check if we already inserted this as PURE_INFIX ( should be yes)
            #keep widthEnd as it is
            pNodeId = self.entitystorage.updateIfExists(funcPos, entityType=EntityType.IMPLICIT_INFIX, widthStart=funcPos) # returns None with no throw, if not exist.

            #also update width
            self.entitystorage.insert(# insert 0 with parentNodeId
                '0', funcPos, funcPos, EntityType.PURE_NUMBER, 
                parentNodeId=pNodeId, argIdx=0, widthStart=funcPos, widthEnd=funcPos)#pure_number width should not be updated
            # print('added implicit 0-')

        # print('self.overallEqual_startPos', self.overallEqual_startPos)
        affected = ['-']

        #5a
        subEquationStr, (_, firstRemovedEnd), (_, _) =stripWithReturn(self.equationStr)
        # print(firstRemovedEnd);import pdb;pdb.set_trace()
        if subEquationStr[0] in affected:
            addImplictMinus(firstRemovedEnd)
        #5a1
        # for idx in range(0, len(self.overallEqual_startPos)-1):#not just overallEquals
        #     startPos, endPos = self.overallEqual_startPos[idx], self.overallEqual_startPos[idx+1]+len('=')
        for idx, (nodeId, funcName, widthStart, widthEnd, startPos, endPos) in enumerate(self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX, EntityType.IMPLICIT_INFIX)):
            # if idx != 0:
            #         startPos += len(funcName)
            subEquationStr, (_, lastRemovedStart), (_, _) = stripWithReturn(self.equationStr[endPos:])
            # print(nodeId, funcName, subEquationStr);import pdb;pdb.set_trace()
            if subEquationStr[0] in affected:
                addImplictMinus(endPos+lastRemovedStart)

        # print('self.endOfOpenBraPos', self.endOfOpenBraPos);import pdb;pdb.set_trace()
        #all openbrackets except Matrices, no need bracketstorage
        #5a2
        for openBraPos in self.endOfOpenBraPos:
            if self.isPosInMatrixTag(openBraPos) or openBraPos >= len(self.equationStr):# or self.isPosInMatrixTag(closeBraPos):
                continue
            if self.equationStr[openBraPos] in affected: #if openBraPos, is the end of the bracket DO NOT +1
                # import pdb;pdb.set_trace()
                addImplictMinus(openBraPos)


    def _update_all_width_by_enclosing_brackets_width_remove(self):
        #remove all the user stupid multiple enclosing brackets
        #CHECK wider enclosing brackets, for EVERYTHING 
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<UPDATES should be done by EntityType, and then from left to right????
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<only need to update for INFIX and BACKSLASH_FUNCTIONS|BACKSLASH_VARIABLES?
        """

        PURE_NUMBER = 'pure_number'
        IMPLICIT_INFIX = 'implicit_infix'
        PURE_VARIABLE = 'pure_variable'
        BACKSLASH_VARIABLE = 'backslash_variable'
        BACKSLASH_FUNCTION = 'backslash_function'
        BACKSLASH_NUMBER = 'backslash_number'
        PURE_INFIX = 'pure_infix'
        BACKSLASH_INFIX = 'backslash_infix'
        MATRIX = 'matrix'
        """
        self.bracketstorage = self.entitystorage._EntityStorage__updateEntityToWiderWidth(self.entitystorage.getAllNodeIds(), self.bracketstorage, self)

        # print(str(self.entitystorage))
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$');import pdb;pdb.set_trace()


        
    def _find_implicit_multiply(self):
        """

    ***OTHER_brackets should only contain right_input_for_^ OR enclosures_for_implicit_multiply OR ORDER_ENCLOSURES[which_op_comes_first, associativity, should_only_enclose_infixes_but_user_can_put_redundant_brackets] at_this_point

        Expand everthing(mat|infix|Backslash|variable|number) to it's full width(inclusive of all the enclosing brackets, and for infix it's the inclusive of both side arguments also note for infix if there are enclosing brackets), 
        sort everything by widthstartpos. Go through everything in pairs(sliding_window).
        If they Touch each other (in their full width):
            If one or both are infixes, they must be enclosed in brackets to add implicit* (we included the enclosing into the widthstart&widthend, so no need to check this? just add implicit multiply)
            Else add implicit*


        CHECK for enclosing_brackets for implicit_multiply
        REMOVE all implicit_multiply from OTHER_brackets
        UPDATE widthStart__nodeId, widthEnd__nodeId for BS
    ***OTHER_brackets should only contain ORDER_ENCLOSURES[which_op_comes_first] at_this_point ?????????
    ***implicit_0 and implicit_multiply already has all its children [tree_building] at_this_point
        """

        #also look for touching bras to insert * and addUnConfirmedPCrelationshipById
        #startPos is the_start_of_touching_pos, endPos is the_end_of_touching_pos


        addedImplicitMultiplyStartPos = []
        # print('getAllTouchingBras', self.bracketstorage.getAllTouchingBras(self.equationStr));import pdb;pdb.set_trace();
        for startPos, endPos in self.bracketstorage.getAllTouchingBras(self.equationStr):
            #TODO also should check if startPos-1 is preSym, then its backslash, and we discard<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            endPoszStartPos = self.bracketstorage.getCorrespondingCloseBraPos(endPos)
            # this has to be on the point of backslashbracket not within
            if self.bsbracketstorage.exists(startPos, self.bsbracketstorageDefault, True) or \
            self.bsbracketstorage.exists(endPoszStartPos, self.bsbracketstorageDefault, False) or \
            (startPos-1 in self.bracketstorage.allOpenPosOfBackslashArgsNoBrackets):
                continue
            # print('added as touchingBras');import pdb;pdb.set_trace()
            pNodeId = self.entitystorage.insert('*', startPos, startPos, EntityType.IMPLICIT_INFIX, 
                parentNodeId=None, argIdx=None, widthStart=startPos, widthEnd=startPos)
            addedImplicitMultiplyStartPos.append(startPos)
            # for cNodeId, _, widthStart, widthEnd, _, _ in self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd():
            #     if widthEnd == startPos:#vorDing
            #         self.entitystorage.addUnConfirmedPCrelationshipById(pNodeId, 0, None, widthStart, None, widthEnd)
            #     if widthStart == endPos:#hinDing
            #         self.entitystorage.addUnConfirmedPCrelationshipById(pNodeId, 1, None, widthStart, None, widthEnd)


        list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd = self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd()
        for idx in range(0, len(list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd)-1):
            vorDing = list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd[idx]
            hinDing = list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd[idx+1]
            vorDingEntityType = self.entitystorage.nodeId__entityType[vorDing[0]]
            hinDingEntityType = self.entitystorage.nodeId__entityType[hinDing[0]]
            #START_CONDITIONAL
            if (vorDingEntityType in [EntityType.BACKSLASH_INFIX, EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX]) or (hinDingEntityType in [EntityType.BACKSLASH_INFIX, EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX]):
                continue

            #END_CONDITIONAL
            # print(str(self.entitystorage));print(self.equationStr[vorDing[3]:hinDing[2]]);import pdb;pdb.set_trace()
            #find all the entities between vorDing and hinDing, can only be brackets and whitespace, then we add implicit multiply # this is the same as touchingBras
            addImplictMultiply, openBraPos, closeBraPos = vorDing[3] <= hinDing[2], None, None
            for i in range(vorDing[3], hinDing[2]):
                c = self.equationStr[i]
                # print(c, c not in BracketType.allBras(), 
                #     not c.isspace(), 
                #     vorDing[3]-1 in self.bracketstorage.allOpenPosOfBackslashArgsNoBrackets,
                #     len(addedImplicitMultiplyStartPos) > 0 and i in addedImplicitMultiplyStartPos);
                if (c not in BracketType.allBras() and not c.isspace()) or \
                (vorDing[3]-1 in self.bracketstorage.allOpenPosOfBackslashArgsNoBrackets) or \
                (len(addedImplicitMultiplyStartPos) > 0 and i in addedImplicitMultiplyStartPos): # do not add the same as touchingBras
                    addImplictMultiply=False
                    break
                # import pdb;pdb.set_trace()
                #bracket_accounting, if there are openBra and closeBra, then its also touchingBras which cannot be. so once we hit either openBra or closeBra, we can decide which to put on
                if c in BracketType.openBras():
                    #wait for the nearest
                    openBraPos = i
                    break
                elif c in BracketType.closeBras():
                    #take the farthest
                    closeBraPos = i
                    # print('closeBraPos', closeBraPos, i, c)
            # import pdb;pdb.set_trace()
            #adding implicit should be sticking to any farthest brackets.
            if openBraPos is not None and closeBraPos is not None:
                #TODO also should check if startPos-1 is preSym, then its backslash, and we discard<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                closeBraPosStartPos = self.bracketstorage.getCorrespondingCloseBraPos(closeBraPos)

                if self.isPosInBackslashBrackets(openBraPos) or self.isPosInBackslashBrackets(closeBraPosStartPos) or (openBraPos-1 in self.bracketstorage.allOpenPosOfBackslashArgsNoBrackets):
                    addImplictMultiply = False
                    # import pdb;pdb.set_trace()
                else:
                    raise Exception() # this is equivalent to touchingBra, which is avoided by (i in addedImplicitMultiplyStartPos)
            else:
                if openBraPos is not None:
                    funcStartEnd = openBraPos
                if closeBraPos is not None:
                    funcStartEnd = closeBraPos + len(')')
                if openBraPos is None and closeBraPos is None:
                    funcStartEnd = min(vorDing[3], hinDing[2]+1)
            # import pdb;pdb.set_trace()

            # if (vorDing[3] +1 == hinDing[2])\
            #  or (vorDing[3] == hinDing[2]): #3=widthEnd & 2=widthStart
            if addImplictMultiply:
                # print('funcStartEnd', funcStartEnd); import pdb;pdb.set_trace()
                pNodeId = self.entitystorage.insert('*', funcStartEnd, funcStartEnd, EntityType.IMPLICIT_INFIX, 
                    parentNodeId=None, argIdx=None, widthStart=vorDing[2], widthEnd=hinDing[3])
                """TODO deal later
                Contains 
                0. function calls f(x)
                1. differential   dx
                """
                # self.bracketstorage = self.entitystorage.addConfirmedPCrelationshipById(pNodeId, vorDing[0], 0, bracketstorage=self.bracketstorage)
                # self.bracketstorage = self.entitystorage.addConfirmedPCrelationshipById(pNodeId, hinDing[0], 1, bracketstorage=self.bracketstorage)
                """
 [ (58, '*', 119, 118)]<<<<<these implicit-multiply does not have openBraPos
 tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos
 
 addUnConfirmedPCrelationshipById( nodeId, argId, openBraType, openBraPos, closeBraType, closeBraPos)
                """
                # self.entitystorage.addUnConfirmedPCrelationshipById(pNodeId, 0, None, vorDing[2], None, vorDing[3])
                # self.entitystorage.addUnConfirmedPCrelationshipById(pNodeId, 1, None, hinDing[2], None, hinDing[3])

        # print(str(self.entitystorage))
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$');import pdb;pdb.set_trace()

    def _match_child_to_parent_input(self):
        """
        0. Update all the entities to the widest possible width
        1. Get all overall_equals attributes: nodeId, funcName, entityType, funcStart, funcEnd, widthStart, widthEnd
        2. Use self.bracketstorage.toTree to make a tree by whether or not brackets are enclosing, returns
            0. parent__listOfChildren
            1. openPosition__closePosition
            2. openPosition__level
            3. openPosition__bracketLen
        3. Use self.overallEqual_startPos = [0, ..., len(self.equationStr)], where the ... are the startPos of the overall_equals; as TOP level
            0. Use openPosition__level to go level-by-level
                0. Use openPosition__closePosition to get (openPosition, closePosition)
                    0. Get all the Entity attributes between (openPosition, closePosition) -> original_list_of_entities, attributes=(nodeId, funcName, entityType, funcStart, funcEnd, widthStart, widthEnd)
                    1. exclude OverallEquals from original_list_of_entities
                    2. Use parent__listOfChildren & openPosition__closePosition & replaceBetween & openClose__rootOfSubTree, to replace entities_that_have_been_treefied_in_some_position
                        0. Use parent__listOfChildren to get bracket_children of openPosition -> cOpenPosition
                        1. Use openPosition__closePosition to get cClosePosition of cOpenPosition
                        2. Use (cOpenPosition, cClosePosition) to get openClose__rootOfSubTree, to get the rootOfSubTree of all entities_that_have_been_treefied_in_some_position
                        3. Use replaceBetween, to replace all entities_that_have_been_treefied_in_some_position between (openPosition, closePosition), with rootOfSubTree, in original_list_of_entities
                    3. Get backslashes_list from original_list_of_entities
                    4. Use openClose__rootOfSubTree & getSlots & addConfirmedPCrelationshipById, to replace rootOfSubTree in backslash's arguments from backslashes_list in original_list_of_entities
                        0. Use getSlots on backslash_node_id to get all arguments (slotStartPos, slotEndPos, argIdx)
                        1. Use openClose__rootOfSubTree, to get rootOfSubTree between (slotStartPos, slotEndPos)
                        2. Use addConfirmedPCrelationshipById to add parent|child relationship between backslash and rootOfSubTree
                    5. Get all infixes from original_list_of_entities -> infixes_list
                    6. Going by infixes_list, each infix's left and right in original_list_of_entities, connect them as parent|child, until we have only 1 infix left -> that 1 infix is the infixRoot
        4. Connect infixRoot to overallEqual as parent|child

        WHERE IS THE ROOTs? either
        0. all the overallEquals
        1. the last infixRoot<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        self.bracketstorage = self.entitystorage._EntityStorage__updateEntityToWiderWidth(self.entitystorage.getAllNodeIds(), self.bracketstorage, self)

        # print(str(self.entitystorage))
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        self.list_of_ast_roots = []
        OVERALLEquals_list_nodeId_funcName_entityType_funcStart_funcEnd_widthStart_widthEnd = []
        for nodeId in self.entitystorage.getAllNodeIds():
            funcName, funcStart = self.entitystorage.nodeId__funcName[nodeId], self.entitystorage.nodeId__funcStart[nodeId]
            if funcName == '=' and funcStart in self.overallEqual_startPos:
                OVERALLEquals_list_nodeId_funcName_entityType_funcStart_funcEnd_widthStart_widthEnd.append((
                    nodeId, self.entitystorage.nodeId__entityType[nodeId] ,funcStart, self.entitystorage.nodeId__funcEnd[nodeId] , self.entitystorage.nodeId__widthStart[nodeId], self.entitystorage.nodeId__widthEnd[nodeId] ,
                ))
                self.list_of_ast_roots.append(('=', nodeId))
        OVERALLEquals_list_nodeId_funcName_entityType_funcStart_funcEnd_widthStart_widthEnd = sorted(OVERALLEquals_list_nodeId_funcName_entityType_funcStart_funcEnd_widthStart_widthEnd, key=lambda ele: ele[3])
        prevOVERALLEquals = None
        # print('self.overallEqual_startPos', self.overallEqual_startPos)
        # print(str(self.bracketstorage))
        tuple_startPos_endPos__NAMES__fromBracketAccounting = self.bracketstorage.toTree(self.overallEqual_startPos, self.equationStr) # this effectively takes care of brackets, so you don't have to care about brackets from here
        
        for idx in range(0, len(self.overallEqual_startPos)-1):#self.overallEqual_startPos include 0{at the beginning} and (len(self.equationStr)-1){at the end}
            startPos, endPos = self.overallEqual_startPos[idx], self.overallEqual_startPos[idx+1]
            parent__listOfChildren = tuple_startPos_endPos__NAMES__fromBracketAccounting[(startPos, endPos)]['parent__listOfChildren']
            openPosition__closePosition = tuple_startPos_endPos__NAMES__fromBracketAccounting[(startPos, endPos)]['openPosition__closePosition']
            openPosition__level = tuple_startPos_endPos__NAMES__fromBracketAccounting[(startPos, endPos)]['openPosition__level']
            openPosition__bracketLen = tuple_startPos_endPos__NAMES__fromBracketAccounting[(startPos, endPos)]['openPosition__bracketLen']
            #go by level, get openPosition~closePosition of level.
            level__list_openPosition = {}
            for openPosition, level in openPosition__level.items():
                existing = level__list_openPosition.get(level, [])
                existing.append(openPosition)
                level__list_openPosition[level] = existing

            def replaceBetween(cOpenPosition, cClosePosition, original_list_of_entities, rootOfSubTree):
                #original_list_of_entities, element=(nodeId, funcName, entityType, funcStart, funcEnd, widthStart, widthEnd)
                #for infixes use funcStart|funcEnd, for everything else use widthStart|widthEnd
                new_original_list_of_entities = []
                addedRoot = False
                for entTup in original_list_of_entities:
                    entStartWidth, entEndWidth = None, None
                    if entTup[2] in [EntityType.IMPLICIT_INFIX, EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX]:
                        entStartWidth, entEndWidth = entTup[3], entTup[4]
                    else:
                        entStartWidth, entEndWidth = entTup[5], entTup[6]
                    #found startWidth, endWidth
                    if cOpenPosition < entStartWidth and entEndWidth <= cClosePosition:#< and not <=, because we want avoid implicits
                        if not addedRoot:
                            addedRoot = True
                            new_original_list_of_entities.append(rootOfSubTree)
                    else:
                        new_original_list_of_entities.append(entTup)
                return new_original_list_of_entities

            """
            What about the backslash, whose arguments have no brackets? -----> use slot, 
            """
            openClose__rootOfSubTree = {} #interTree
            #IntraTree
            sortedByLevel = sorted(level__list_openPosition.items(), key=lambda t: t[0], reverse=True)#0 is the top, and increases down the level
            # print('sortedByLevel', sortedByLevel); import pdb;pdb.set_trace()
            justSelectedInfixId = []
            for level, list_openPosition in sortedByLevel:
                for openPosition in list_openPosition:
                    closePosition = openPosition__closePosition[openPosition]
                    #get all entities between openPosition and closePosition => original_list_of_entities
                    #+1 exclude the openBracket
                    original_list_of_entities = self.entitystorage.getAllEntityBetween(openPosition+openPosition__bracketLen[openPosition], closePosition) # element=(nodeId, funcName, entityType, funcStart, funcEnd, widthStart, widthEnd)
                    
                    original_list_of_entities = sorted(original_list_of_entities, key=lambda ele: ele[4])#
                    # import pdb;pdb.set_trace()
                    #TODO need to remove OVERALLEquals
                    if '=' == original_list_of_entities[0][1]:# = == funcName
                        original_list_of_entities = original_list_of_entities[1:] # exclude first element
                    # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', level)
                    # print('all entities between : ', openPosition+openPosition__bracketLen[openPosition], ' and', closePosition, '', list(map(lambda t: (t[1], t[0]), original_list_of_entities)))
                    #replace with ROOT_OF_SUBTREE using parent__listOfChildren (this removes all brackets) in original_list_of_entities
                    for cOpenPosition in parent__listOfChildren.get(openPosition, []):
                        cClosePosition = openPosition__closePosition[cOpenPosition]
                        rootOfSubTree = openClose__rootOfSubTree[(cOpenPosition, cClosePosition)] # rootOfSubTree=element=(nodeId, funcName, entityType, funcStart, funcEnd, widthStart, widthEnd), infixes_use_func, everythingelse_use_width
                        # print('$$$$replacements OG: ', list(map(lambda t: (t[1], t[0]), original_list_of_entities)))
                        original_list_of_entities = replaceBetween(cOpenPosition, cClosePosition, original_list_of_entities, rootOfSubTree)
                        # print('$$$$replacements RE: ', list(map(lambda t: (t[1], t[0]), original_list_of_entities)))
                        # print('RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
                    original_list_of_entities = sorted(original_list_of_entities, key=lambda ele: ele[4])#
                    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WHAT TO DO IF THERE ARE backslash in this?
                    #find all the backslash in original_list_of_entities
                    backslashes_list = list(filter(lambda ele: ele[2] in [EntityType.BACKSLASH_FUNCTION, EntityType.BACKSLASH_VARIABLE], original_list_of_entities))
                    for backslashEle in backslashes_list:
                        slots = self.entitystorage.getSlots(backslashEle[0]) #element: (startPos, endPos)
                        for slotStartPos, slotEndPos, argIdx in slots:
                            #check if they are in 
                            rootOfSubTree = openClose__rootOfSubTree.get((slotStartPos, slotEndPos), None)
                            # print('rootOfSubTree: ', (rootOfSubTree[1], rootOfSubTree[0])); import pdb;pdb.set_trace()
                            if rootOfSubTree is not None:
                                self.entitystorage.addConfirmedPCrelationshipById(backslashEle[0], rootOfSubTree[0], argIdx)
                                if rootOfSubTree in original_list_of_entities:
                                    original_list_of_entities.remove(rootOfSubTree)
                            else:
                                raise Exception()
                    #         import pdb;pdb.set_trace()
                    # import pdb;pdb.set_trace()
                    #take out all the infixes => infixes_list, process infixes_list by priority, UNLIKE backslash, infixes can be choosen over and over example * in : (1+(1+1)*(1+1)+1), is choosen twice
                    infixes_list = sorted(
                            list(filter(lambda ele: ele[2] in [EntityType.IMPLICIT_INFIX, EntityType.BACKSLASH_INFIX, EntityType.PURE_INFIX], original_list_of_entities)), 
                            key=lambda ele: self.getPriority(ele[1])+(len(self.INFIX) if ele[0] in justSelectedInfixId else 0)#+(len(self.INFIX) if ele[0] in rootOfSubTreeIdSubstituted else 0)
                            )#distance from the center_of_original_list_of_entities_byFuncStart<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    infixEle = infixes_list[0] if len(infixes_list) > 0 else original_list_of_entities[0] # default_value is lowest getPriority, break tie by the one closest_to_the_center
                    # print('len(original_list_of_entities) > 1', len(original_list_of_entities) > 1, 'infixEle is not None', infixEle is not None)
                    while len(original_list_of_entities) > 1:

                        infixes_list = sorted(
                            list(filter(lambda ele: ele[2] in [EntityType.IMPLICIT_INFIX, EntityType.BACKSLASH_INFIX, EntityType.PURE_INFIX], infixes_list)), 
                            key=lambda ele: self.getPriority(ele[1])+(len(self.INFIX) if ele[0] in justSelectedInfixId else 0)#+(len(self.INFIX) if ele[0] in rootOfSubTreeIdSubstituted else 0)
                            )#distance from the center_of_original_list_of_entities_byFuncStart<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        infixEle = infixes_list[0] if len(infixes_list) > 0 else original_list_of_entities[0] # default_value is lowest getPriority, break tie by the one closest_to_the_center
                        # print('choosing:infixes_list', list(map(lambda t: (t[1], t[0]), infixes_list)));import pdb;pdb.set_trace()
                        justSelectedInfixId.append(infixEle[0])
                        listIdx = original_list_of_entities.index(infixEle)
                        # print('**************************************************')
                        # print('OGList:', list(map(lambda t: (t[1], t[0]), original_list_of_entities)))
                        # print('mid: ', (infixEle[1], infixEle[0]))
                        leftEle = original_list_of_entities[listIdx-1]
                        self.entitystorage.addConfirmedPCrelationshipById(infixEle[0], leftEle[0], 0) #leftEle[0]=nodeId # interTree and IntraTree
                        rightEle = original_list_of_entities[listIdx+1]
                        self.entitystorage.addConfirmedPCrelationshipById(infixEle[0], rightEle[0], 1) #rightEle[0]=nodeId # interTree and IntraTree
                        #remove left|right from original_list_of_entities
                        if leftEle in original_list_of_entities:
                            original_list_of_entities.remove(leftEle)
                        if rightEle in original_list_of_entities:
                            original_list_of_entities.remove(rightEle)
                        if leftEle in infixes_list:
                            infixes_list.remove(leftEle)
                        if rightEle in infixes_list:
                            infixes_list.remove(rightEle)
                    #     print('OGList:', list(map(lambda t: (t[1], t[0]), original_list_of_entities)))
                    #     print('************************************************** infixEle:', (infixEle[1], infixEle[0]))
                    # print('doneWith infixes_list ಠ_ಠ (๑˃̵ᴗ˂̵)و ﾞ ♥ •͈ᴗ•͈  ಥ_ಥ (ؑ‷ᵕؑ̇‷)◞✧ ♡  ◡̈   ٩(^‿^)۶')
                    openClose__rootOfSubTree[(openPosition, closePosition)] = infixEle
            #         print('updated openClose__rootOfSubTree');import pdb;pdb.set_trace()
            #     print('openClose__rootOfSubTree ', openClose__rootOfSubTree, ' SUBBERRRRRRSUSBUBSUBSUBSUBSUBSUBSUBSUBSUSBUSBUSB ')
            # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', level, ' topOfEqualSubTree: ', infixEle);import pdb;pdb.set_trace()
            #make the connection between OVEREquals and topOfEqualSubTree
            if prevOVERALLEquals is not None:
                equalEntity = OVERALLEquals_list_nodeId_funcName_entityType_funcStart_funcEnd_widthStart_widthEnd[idx-1]
                self.entitystorage.addConfirmedPCrelationshipById(equalEntity[0], prevOVERALLEquals[0], 0)
                self.entitystorage.addConfirmedPCrelationshipById(equalEntity[0], infixEle[0], 1)
                # print('*******ADDDDDD EQUALS'); import pdb;pdb.set_trace()
            prevOVERALLEquals = infixEle

        # print(str(self.entitystorage))
        if len(self.list_of_ast_roots) == 0:
            # print('this should not happen if there is an overallEquals')
            self.list_of_ast_roots.append((infixEle[1], infixEle[0]))

        #bad but quick fix for now
        self.rootOfTree = self.list_of_ast_roots[0]



        
    def _format_to_pyStyledAST(self):
        """
        If there are many OVERALLEquals(self.overallEqual_nodes), then, there will be many roots

        We can add a FAKE ROOT that == ('', 0), over all the OVERALLEquals. Easy for tree-algos ===>???????

self.entitystorage.tuple_nodeId_argIdx__pNodeId
        """
        pNode__list_tuple_argId_cNode = {}
        for (nodeId, argIdx), pNodeId in self.entitystorage.tuple_nodeId_argIdx__pNodeId.items():
            pFuncName = self.entitystorage.nodeId__funcName[pNodeId]
            existingChildren = pNode__list_tuple_argId_cNode.get((pFuncName, pNodeId), [])
            funcName = self.entitystorage.nodeId__funcName[nodeId]
            existingChildren.append((argIdx, (funcName, nodeId)))
            pNode__list_tuple_argId_cNode[(pFuncName, pNodeId)] = existingChildren

        #sort all children, strip the argIdx from all the children
        self.latexAST = {}
        for pNode, list_tuple_argId_cNode in pNode__list_tuple_argId_cNode.items():
            list_cNode = []
            for argId, cNode in list_tuple_argId_cNode:
                list_cNode.append(cNode)
            self.latexAST[pNode] = list_cNode



    def _convert_to_schemeStyledAST(self):
        """
    ~~~Handle special cases of Latex~~~
    1. (sqrt a) => (nroot 2 a)
    2. (ln a) => (log e a)
    3. (log a) => (log 10 a)
    4. (frac a b) => (/ a b)
    5. (TRIG p t) => (^ (TRIG t) p)
    WHAT ABOUT THE NEW FUNCTIONS?
    6. (* (/ d (* d t)) A) => (ð A t) # d will collide with differential symbol
    7. (/ (* d u) (* d t)) => (ð u t)
    8. (*  (/ partial (partial t) A)
    9. (/ (partial u) (partial t)) => (ð u t)
    10.  => (∫ )
    
    \\int \\iint \\iiint \\oint \\oiint
    \\lim  (\\to is an infix)
    \\sum  (this one has equals = at the base)
    \\prod  (this one has equals = at the base)
    \\nabla
    \\Delta
    \\partial
    \\cdot (dot product)
    (cross product)
    
    determinant (simplified as det?? only?)
    also 
    \\begin{vmatrix}\\end{vmatrix}
    \\begin{Vmatrix}\\end{Vmatrix}
        """

        def replaceChildWithNewParent(current__replaced, children, parent):
            newChildren = []
            for child in children:
                replacementRoot = current__replaced.get(child, child)#UIOP! # TODO
                if parent != replacementRoot:
                    newChildren.append(replacementRoot)
                else:
                    newChildren.append(child)
            return newChildren

        def makeReplacementNode(pFuncName, pNodeId, var__val, instructions):
            if pFuncName in instructions['insertToEntityStorage']:
                replacementNodeId = self.entitystorage.insert(
                    pFuncName, -1, -1, EntityType.FROM_CONVERSION,
                    parentNodeId=None, #UIOP!
                    argIdx=None, #UIOP!
                    widthStart=-1, widthEnd=-1, bracketstorage=None)# stay as None
                replacementNode = (pFuncName, replacementNodeId)
            elif pNodeId in var__val:
                replacementNode = (var__val.get(pFuncName, pFuncName), var__val[pNodeId])
            elif pFuncName in instructions.get('var__defaults', {}):
                replacementFuncName = instructions.get('var__defaults', {})[pFuncName]
                replacementNodeId = self.entitystorage.insert(
                    replacementFuncName, -1, -1, EntityType.FROM_CONVERSION,
                    parentNodeId=None, #UIOP!
                    argIdx=None, #UIOP!
                    widthStart=-1, widthEnd=-1, bracketstorage=None)# stay as None
                replacementNode = (replacementFuncName, replacementNodeId)
            else:# then like the TRIG with exponential, but the user did not give it, and the whole outputRow should be abandoned
                # import pdb;pdb.set_trace()
                replacementNode = None
            return replacementNode

        self.ast, current__replaced = {}, {}
        for pNode, input_children in self.latexAST.items():
            # print(pNode, input_children)
            (pFuncName, pNodeId), var__val = pNode, {}
            instructions = self.getLatexSpecialCases(pFuncName)
            if instructions:
                parentTemplate, childTemplates = instructions['inputTemplate'][0], instructions['inputTemplate'][1]
                # print(parentTemplate, childTemplates)
                #match input_parent with inputTemplate_parent
                parentNodeIdVar = parentTemplate[0][1]
                var__val[parentNodeIdVar] = pNode[1]
                #START match input_children with inputTemplate_children
                # import pdb;pdb.set_trace()
                if len(input_children) > len(childTemplates):
                    raise Exception()

                #t[1][1] is optional_or_not, only for funcName, WE_ASSUME if funcName is missing then nodeId is missing
                templateIndicesOfCompulsory = sorted(list(map(lambda t: t[0], filter(lambda t: not t[1][1], enumerate(childTemplates)))))
                templateIndicesOfOptional = sorted(list(map(lambda t: t[0], filter(lambda t: t[1][1], enumerate(childTemplates)))))
                
                if len(input_children) < len(templateIndicesOfCompulsory):
                    #look for defaults
                    if len(instructions.get('var__defaults', {})) != (len(templateIndicesOfCompulsory) - len(input_children)):
                        raise Exception('NOT ENOUGH DEFAULT VALUES')
                    var__val.update(instructions['var__defaults'])
                    #remove defaults from templateIndicesOfCompulsory, WE_ASSUME only funcName will appear in var__defaults
                    for idx, template in enumerate(childTemplates):
                        if template[0][0] in var__val:
                            templateIndicesOfCompulsory.remove(idx)
                    #
                #we try to match childrens in the order of the input and template
                optionalIndicesToUse=templateIndicesOfOptional[:len(input_children)-len(templateIndicesOfCompulsory)]
                templateIndicesToUse=sorted(templateIndicesOfCompulsory+optionalIndicesToUse)
                for input_child, templateIdx in zip(input_children, templateIndicesToUse):
                    # import pdb;pdb.set_trace()
                    var__val[childTemplates[templateIdx][0][0]] = input_child[0]#[0] for funcName
                    if '$' in childTemplates[templateIdx][0][1]:# if its a var
                        var__val[childTemplates[templateIdx][0][1]] = input_child[1]
                #END match input_children with inputTemplate_children

                #heran, generate outputTemplate, darin we need to generate indices for instructions['insertToEntityStorage']
                replacement, bad = {}, False
                for outputTemplateParent, outputTemplateChildren in instructions['outputTemplate']:
                    #parent
                    pReplacementNode = makeReplacementNode(outputTemplateParent[0][0], outputTemplateParent[0][1], var__val, instructions)
                    #
                    if outputTemplateParent[2] == instructions['rootOfResultTemplate']:
                        current__replaced[pNode] = pReplacementNode
                    # print(current__replaced)
                    #
                    #children
                    replacementChildren = []
                    for outputTemplateChild in outputTemplateChildren:
                        cReplacementNode = makeReplacementNode(outputTemplateChild[0][0], outputTemplateChild[0][1], var__val, instructions)
                        if cReplacementNode is None:# then like the TRIG with exponential, but the user did not give it, and the whole outputRow should be abandoned
                            self.entitystorage.removeById(pReplacementNode[1])
                            del current__replaced[pNode]
                            bad = True
                            continue
                        replacementChildren.append(cReplacementNode)
                        
                    #
                    if not bad:
                        replacement[pReplacementNode] = replacementChildren

                #heran, we need to replace parent in children, with instructions['rootOfResultTemplate']
                newReplacement = {}
                for parent, children in replacement.items():
                    newReplacement[parent] = replaceChildWithNewParent(current__replaced, children, parent)
                replacement = newReplacement


                self.ast.update(replacement)
        #put in the rest, while replace parent in children, with instructions['rootOfResultTemplate']
        for pNode, existingChildrenList in self.latexAST.items():
            pFuncName, pNodeId = pNode
            instructions = self.getLatexSpecialCases(pFuncName)
            if not instructions:
                self.ast[pNode] = replaceChildWithNewParent(current__replaced, existingChildrenList, pNode)

        # #SPECIAL CASE FOR DIFFERENTIAL OPERATORS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<better to use SchemeGrammarParser for this?
        """
        Is it better to use SchemeGrammarParser? YES, we are using SGP for _unparse, here not using is ok, because we are only matching one node, but _unparse needs to match tree(template) to tree(ast)
        
        FindTreeInTree misses 
        (d/dx)(uv), because a misses a tree, by popping u instead of d

        """
        # """

        # 6. (* (/ d (* d t)) A) => (ð A t) # d will collide with differential symbol
        # 7. (/ (* d u) (* d t)) => (ð u t)
        # 8. (*  (/ partial (partial t) A)
        # 9. (/ (partial u) (partial t)) => (ð u t)
        # """
        # differentialOperatorSigns = ['d', 'partial']
        # differentialOperatorReplacementSign = '$$'
        # differentialTreePatterns = [
        #     {
        #     'tree':{#6 & 8
        #             ('*', '$0'):[('/', '$1'), ('$2', '$3')],
        #             ('/', '$1'):[('$$', '$4'), ('*', '$5')],
        #             ('*', '$5'):[('$$', '$6'), ('$7', '$8')]
        #         },
        #     'root':('*', '$0'),
        #     'replacementPattern':{
        #             ('ð', '$4'):[('$2', '$3'), ('$7', '$8')]
        #         },
        #     'replacementPatternRoot':('ð', '$4')
        #     },
        #     {
        #     'tree':{#7 & 9
        #             ('/', '$0'):[('*', '$1'), ('*', '$2')],
        #             ('*', '$1'):[('$$', '$3'), ('$4', '$5')],
        #             ('*', '$2'):[('$$', '$6'), ('$7', '$8')]
        #         },
        #     'root':('/', '$0'),
        #     'replacementPattern':{
        #             ('ð', '$3'):[('$4', '$5'), ('$7', '$8')]
        #         },
        #     'replacementPatternRoot':('ð', '$3')
        #     }
        # ]
        # def treeReplacement(tree, root, updateComponentOfNode):
        #     def updateNode(node):
        #         #assume each node is a tuple
        #         newNode = []
        #         for nodeComponent in list(node):
        #             newNode.append(updateComponentOfNode(nodeComponent))
        #         return tuple(newNode)
        #     stack, returnedTree = [root], {}
        #     while len(stack) > 0:
        #         jetzt = stack.pop()
        #         children = tree.get(jetzt, [])
        #         stack += children
        #         jetzt = updateNode(jetzt)
        #         newChildren = []
        #         for child in children:
        #             child = updateNode(child)
        #             newChildren.append(child)
        #         if len(newChildren) > 0:
        #             returnedTree[jetzt] = newChildren
        #     newRoot = updateNode(root)
        #     return newRoot, returnedTree

        # current__replaced = {}
        # newAst, nodesToAvoidInNewAst = {}, []
        # for differentialOperatorSign in differentialOperatorSigns:
        #     for differentialTreePattern in differentialTreePatterns:
        #         def replaceDifferentialOperatorSign(nodeComponent):
        #             if nodeComponent == differentialOperatorReplacementSign:
        #                 return differentialOperatorSign
        #             return nodeComponent
        #         treePatternRoot, treePattern = treeReplacement(differentialTreePattern['tree'], differentialTreePattern['root'], replaceDifferentialOperatorSign)
        #         print('searching for treePattern: ', treePattern)
        #         treeRoot__matchedVar__val = {}
        #         global GLOBAL___matchedVar__val
        #         GLOBAL___matchedVar__val = None
        #         def callbackForTreeTreeMatchingStart(targetTreeRoot):
        #             global GLOBAL___matchedVar__val
        #             GLOBAL___matchedVar__val = {}
        #             # print('initialized matchedVar__val', GLOBAL___matchedVar__val)

        #         def _nodeMatch(gesuchteCurrent, targetCurrent):
        #             global GLOBAL___matchedVar__val
        #             # print('_nodeMatch: matchedVar__val', GLOBAL___matchedVar__val)
        #             if GLOBAL___matchedVar__val is not None and gesuchteCurrent[1].startswith('$'):
        #                 GLOBAL___matchedVar__val[gesuchteCurrent[1]]=targetCurrent[1]
        #                 # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<_nodeMatch:', GLOBAL___matchedVar__val)

        #             if gesuchteCurrent[0].startswith('$'): #its a variable
        #                 if GLOBAL___matchedVar__val is not None:
        #                     GLOBAL___matchedVar__val[gesuchteCurrent[0]]=targetCurrent[0]
        #                 # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<_nodeMatch:', GLOBAL___matchedVar__val)
        #                 return True# variables match anything in targetTree, ignores Optional|Compulsory
        #             return gesuchteCurrent[0] == targetCurrent[0]
        #         def callbackForMatchCompletion(targetTreeRoot):#<<<<<<<<<<<<<<<<<<<<<<<<<<refactor the _unparse with this NEW_FUNCTION
        #             global GLOBAL___matchedVar__val
        #             treeRoot__matchedVar__val[targetTreeRoot] = GLOBAL___matchedVar__val
        #             # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>treeRoot__matchedVar__val:', treeRoot__matchedVar__val)
        #             GLOBAL___matchedVar__val = None


        #         def componentUpdate(nodeComponent, var__val):
        #             # print('nodeComponent', nodeComponent, var__val.get(nodeComponent, nodeComponent));import pdb;pdb.set_trace()
        #             return var__val.get(nodeComponent, nodeComponent)
        #         for rootNode in self.list_of_ast_roots:
        #             print(rootNode, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        #             for treeRoot, matchedTree in FindTreeInTree.findAllTreeInTree(
        #                 treePattern, treePatternRoot, self.ast, rootNode, 
        #                 _nodeMatch, 
        #                 callbackForMatchCompletion, 
        #                 callbackForTreeTreeMatchingStart):

        #                 replacementRoot, replacementTree = treeReplacement(differentialTreePattern['replacementPattern'], differentialTreePattern['replacementPatternRoot'], lambda x: componentUpdate(x, treeRoot__matchedVar__val[treeRoot]))
        #                 nodesToAvoidInNewAst += list(set(matchedTree.keys()) - set([treeRoot]))
        #                 newAst.update(replacementTree)
        #                 current__replaced[treeRoot] = replacementRoot
        #                 print('treeRoot', treeRoot)
        #                 print('matchedTree', matchedTree)
        #                 print('matchedVar__val', treeRoot__matchedVar__val[treeRoot])
        #                 print('replacementTree', replacementTree)
        #                 print('nodesToAvoidInNewAst', nodesToAvoidInNewAst)
        #                 print('_______________________________________________________________________');import pdb;pdb.set_trace()
        #                 #also need to replace the parent's children with new Nodes... the differential is a new node
        #                 #remove every node in matchedTree from newAst
        # for pNode, children in self.ast.items():
        #     if pNode not in nodesToAvoidInNewAst:
        #         newChildren = []
        #         for child in children:
        #             newChildren.append(current__replaced.get(child, child))
        #         newAst[pNode] = newChildren
        # print('newAst**********************')
        # print(newAst)



        
    def _get_statistics(self):
        """

count by EntityType:
    IMPLICIT_INFIX = 'implicit_infix'
    PURE_INFIX = 'pure_infix'
    BACKSLASH_INFIX = 'backslash_infix'
    BACKSLASH_FUNCTION = 'backslash_function'


    PURE_NUMBER = 'pure_number'
    BACKSLASH_NUMBER = 'backslash_number'


    PURE_VARIABLE = 'pure_variable'
    BACKSLASH_VARIABLE = 'backslash_variable'
    COMPOSITE_VARIABLE = 'composite_variable' # example V^{Q1}_{BE}, Voltage between B and E of transistor Q1



    MATRIX = 'matrix'

    FROM_CONVERSION = 'from_conversion' # entities added pendant conversion of latexAST to schemeAST NOT HERE

    ~~~Get statistics~~~
    1. totalNodeCount
    2. functions count
    3. primitives count
    4. variables count
    5. matrices count
        """
        
        self.totalNodeCount = 0
        self.functions = {}
        self.primitives = {}
        self.variables = {}
        stack = deepcopy(self.list_of_ast_roots)
        while len(stack) > 0:
            jetzt = stack.pop()
            children = self.ast.get(jetzt, [])
            stack += children
            self.totalNodeCount += 1
            entityType = self.entitystorage.nodeId__entityType[jetzt[1]]
            if entityType in [EntityType.IMPLICIT_INFIX, EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX, EntityType.BACKSLASH_FUNCTION]:
                self.functions[jetzt[0]] = self.functions.get(jetzt[0], 0) + 1
            elif entityType in [EntityType.PURE_NUMBER, EntityType.BACKSLASH_NUMBER]:
                self.primitives[jetzt[0]] = self.primitives.get(jetzt[0], 0) + 1
            elif entityType in [EntityType.PURE_VARIABLE, EntityType.BACKSLASH_VARIABLE, EntityType.COMPOSITE_VARIABLE]:
                self.variables[jetzt[0]] = self.variables.get(jetzt[0], 0) + 1
            #TODO matrix


    def _parse(self):
        #TODO Pool multiprocessing with method priorities (Chodai!) -- dependency ha chain desu yo, sou shitara, motto hayaku arimasu ka? import ast; find variable_dependency_network between methods
        
        self._find_matrices()
        self._processEachElementOfMatrix() # <<<<<<<<<<<<<<<<<< this can be processed in parallel with the main_thread......
        self._find_infix()
        self._find_brackets()
        self._find_backslash()
        self._insert_equals()
        self._find_variables_or_numbers()
        self._find_infixes_arg_brackets_width()
        self._find_implicit_0()
        self._update_all_width_by_enclosing_brackets_width_remove()
        self._find_implicit_multiply()
        self._match_child_to_parent_input()
        self._format_to_pyStyledAST()
        self._convert_to_schemeStyledAST()
        self._get_statistics()

        return self.ast, self.functions, self.variables, self.primitives, self.totalNodeCount, self.entitystorage.funcStart__nodeId

#####################################################

    def _convertASTToLatexStyleAST(self):
        """
        DFS, at each current, collect all symbols non duplicated

        for each symbol run list_instructions = self.getLatexSpecialCases(symbol, reverse=True), in order of 'reversePriority'
            convert(ast->scheme) the BFS_queue to schemeBFS, use schemegrammarparser, 
                schemeword=schemeBFS, 
                rawInputPattern=(ast->scheme)(list_instructions['outputTemplate']),  #if var__defaults is not empty, replace var with defaults in list_instructions['outputTemplate']
                rawOutputPattern=(ast->scheme)(list_instructions['inputTemplate'])   #if var__defaults is not empty, remove the tuple with var as the first entry in list_instructions['inputTemplate']
            convert the manipulatedSchemeWord back to AST





        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        remove FindTreeInTree, does lesser than schemegrammarparser, could do this for _convert_to_schemeStyledAST, so that our configuration will be more flexible (not restricted to 1_node_matching)
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        find all outputTemplate(subtree) in input
        - find root in input
        - DFS together
        """

        def stripOutArgsFromTemplate(templateWithArgs, templateRoot):
            # need to strip the outputTemplate of all the unnecessary arguments
            stripStack, outputTemplate = [templateRoot], {}# stripStack, outputTemplate = [outputTemplateRoot], {}
            while len(stripStack) > 0:
                tup = stripStack.pop()
                strippedChildren = []
                # print(dict(instructions['outputTemplate']));import pdb;pdb.set_trace()
                # for child in dict(instructions['outputTemplate']).get(tup, []):
                for child in templateWithArgs.get(tup, []):
                    strippedChildren.append(child[0])
                    stripStack.append(child)
                if len(strippedChildren)>0:
                    outputTemplate[tup[0]] = strippedChildren
            outputTemplateRoot = templateRoot[0]
            # import pdb;pdb.set_trace()
            return outputTemplate, outputTemplateRoot


        def findOutputTemplateRoot(instructions):
            outputTemplateRoot = None
            for outputTemplateParent, outputTemplateChildren in instructions['outputTemplate']:
                # import pdb;pdb.set_trace()
                if outputTemplateParent[2] == instructions['rootOfResultTemplate']: #only the id
                    outputTemplateRoot=outputTemplateParent
                    break
            return outputTemplateRoot

        from foundation.automat.common.schemegrammarparser import SchemeGrammarParser
        from foundation.automat.parser.sorte.schemeparser import Schemeparser


        nodeId__symbol___withInstructions = {}
        stack = [self.rootOfTree]
        while len(stack) > 0:
            current = stack.pop()
            if len(self.getLatexSpecialCases(current[0], reverse=True)) > 0:
                nodeId__symbol___withInstructions[current[1]] = current[0]
            kinder = self.ast.get(current, [])
            stack += kinder
        #found all symbols of self.ast
        # print('self.ast', self.ast)
        theAst = self.ast; theRootOfTree = self.rootOfTree; idxOf_nodeId__symbol___withInstructions = 0; astSchemeStr = None
        while len(nodeId__symbol___withInstructions) > 0:#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< after trying 2 cycles then stop?
            # print('nodeId__symbol___withInstructions: ', nodeId__symbol___withInstructions)
            # for symbol in list(all_symbols):
            # print(len(nodeId__symbol___withInstructions), '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TERM<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            if idxOf_nodeId__symbol___withInstructions >= len(nodeId__symbol___withInstructions):
                break
            nodeId, symbol = list(nodeId__symbol___withInstructions.items())[idxOf_nodeId__symbol___withInstructions];idxOf_nodeId__symbol___withInstructions+=1
            list_instructions = self.getLatexSpecialCases(symbol, reverse=True)
            # print('list_instructions: ', list_instructions)
            # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            # print('len(list_instructions): ', len(list_instructions))
            # if len(list_instructions) > 0:
            for instructionsIdx, instructions in enumerate(sorted(list_instructions, key=lambda dic: dic['reversePriority'], reverse=False)): # sort instructions by 'reversePriority'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                
                og_schemeparser = Schemeparser(ast=theAst, rootOfTree=theRootOfTree)
                astSchemeStr = og_schemeparser._unparse()
                # nodeId__startPos = dict(map(lambda t: (t[1], t[0]), og_schemeparser.startPos__nodeId.items()))
                # print('beginning: ', astSchemeStr, 'startPos__nodeId:', og_schemeparser.startPos__nodeId)#, 'nodeId__startPos: ', nodeId__startPos)
                
                # print('outputTemplate:')
                # print(instructions['outputTemplate'])
                # print('inputTemplate:')
                # print(instructions['inputTemplate'])
                #instructions['outputTemplate']
                outputTemplate, outputTemplateRoot = stripOutArgsFromTemplate(dict(instructions['outputTemplate']), findOutputTemplateRoot(instructions))
                OG_outputTemplate, OG_outputTemplateRoot = outputTemplate, outputTemplateRoot
                # print('outputTemplate: ', outputTemplate, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                # print('outputTemplateRoot: ', outputTemplateRoot)
                # print(rawInputPattern)
                #instructions['inputTemplate']
                inputTemplate, inputTemplateRoot = stripOutArgsFromTemplate(dict([instructions['inputTemplate']]), instructions['inputTemplate'][0])
                OG_inputTemplate, OG_inputTemplateRoot = inputTemplate, inputTemplateRoot
                # print('inputTemplate: ', inputTemplate, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                # print('inputTemplateRoot: ', inputTemplateRoot); 
                # import pdb;pdb.set_trace()
                if 'var__defaults' in instructions and len(instructions['var__defaults']) > 0:
                    newOutputTemplate = {}
                    for parent, children in outputTemplate.items():
                        # we assume var__defaults are never in parents
                        newChildren = []
                        for child in children:
                            if child[0] in instructions['var__defaults']:
                                newChildren.append((instructions['var__defaults'][child[0]], child[1]))
                            else:
                                newChildren.append(child)
                        newOutputTemplate[parent] = newChildren
                    outputTemplate = newOutputTemplate
                    #take out all tuples from inputTemplate that has first item in var__defaults.keys()
                    newInputTemplate = {}
                    for parent, children in inputTemplate.items():
                        # we assume var__defaults are never in parents
                        newChildren = []
                        for child in children:
                            if child[0] not in instructions['var__defaults']:
                                newChildren.append(child)
                        newInputTemplate[parent] = newChildren
                    inputTemplate = newInputTemplate
                    # print('var__defaults sub**************************************************')
                    # print('outputTemplate:', outputTemplate)
                    # print('inputTemplate:', inputTemplate)
                rawInputPattern = Schemeparser(ast=outputTemplate, rootOfTree=outputTemplateRoot)._unparse()
                rawOutputPattern = Schemeparser(ast=inputTemplate, rootOfTree=inputTemplateRoot)._unparse()
                # print("rawInputPattern", rawInputPattern)
                # print("rawOutputPattern", rawOutputPattern)
                sgparser = SchemeGrammarParser(rawInputPattern, rawOutputPattern, verbose=self.verbose, recordMaking=True) # this will go through the whole tree, so might as well, go through every thing from getLatexSpecialCases?
                manipulatedAstSchemeStr = sgparser.parse(astSchemeStr)
                # print('matchedWtihDefaults? ', rawInputPattern, not sgparser.noMatches, rawOutputPattern)
                if sgparser.noMatches and instructionsIdx==len(list_instructions)-1:#  # should try all the defaults first, then try all the non-defaults, we do that by only trying non-defaults on the last instruction (we assume that all the defaults are the same across list_instructions)
                    rawInputPattern = Schemeparser(ast=OG_outputTemplate, rootOfTree=OG_outputTemplateRoot)._unparse()
                    rawOutputPattern = Schemeparser(ast=OG_inputTemplate, rootOfTree=OG_inputTemplateRoot)._unparse()
                    sgparser = SchemeGrammarParser(rawInputPattern, rawOutputPattern, verbose=True, recordMaking=True) # this will go through the whole tree, so might as well, go through every thing from getLatexSpecialCases?
                    # print('OG: ', rawInputPattern, rawOutputPattern, 'astSchemeStr:', astSchemeStr)
                    manipulatedAstSchemeStr = sgparser.parse(astSchemeStr)
                    # print('@@@@@tried OG', rawInputPattern, 'matchedOG?:', not sgparser.noMatches, rawOutputPattern)
                if not sgparser.noMatches:
                    astSchemeStr = manipulatedAstSchemeStr
                    # import pprint; pp = pprint.PrettyPrinter(indent=4)
                    # pp.pprint(sgparser.verPosWord)
                    # matches = list(filter(lambda row: row['d']=='r' and row['v'] is not None, sgparser.verPosWord))
                    # print('matches: ')
                    # pp.pprint(matches)
                    ############
                    # pp.pprint(sgparser.matches)
                    ############
                    nodeIdToRemove = []
                    for match in sgparser.matches: # could contain argument matches also.
                        try:
                            nodeIdToRemove.append(og_schemeparser.startPos__nodeId[match['s']+len('(')])#len('(') assumes that we always replace only schemeFunctions and never schemePrimitives
                        except:
                            pass # skip argument matches
                    beforeLeftOverLen = len(nodeId__symbol___withInstructions)
                    nodeId__symbol___withInstructions = dict(filter(lambda t: t[0] not in nodeIdToRemove, nodeId__symbol___withInstructions.items()))
                    afterLeftOverLen = len(nodeId__symbol___withInstructions)
                    schemeparser = Schemeparser(equationStr=astSchemeStr)
                    theAst, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = schemeparser._parse() 
                    theRootOfTree = schemeparser.rootOfTree
                    if afterLeftOverLen < beforeLeftOverLen: # there could be matches but no decrease
                        idxOf_nodeId__symbol___withInstructions = 0; #reset 
                    # print('matches: ', matches);
                    # import pprint; pp = pprint.PrettyPrinter(indent=4)
                    # pp.pprint(sgparser.verPosWord)
                    # import pdb;pdb.set_trace()
                    #nodeId will change?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    # print(len(nodeId__symbol___withInstructions), '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TERM<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                    # import pdb;pdb.set_trace()
                # print('newSchemeStr: ', astSchemeStr)
                # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                # print(len(nodeId__symbol___withInstructions), '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TERM<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                # print('LEFTOVERs: ')
                # import pprint; pp = pprint.PrettyPrinter(indent=4)
                # pp.pprint(nodeId__symbol___withInstructions)
                # print('idxOf_nodeId__symbol___withInstructions: ', idxOf_nodeId__symbol___withInstructions)
                # if len(nodeId__symbol___withInstructions) <=0:
                #     break
                # if not sgparser.noMatches:##### cannot just try one, there might be other matches of other types somewhere else in the string. But if try all, then 
                #     break # we just want one match for each list_instructions, according to the reversePriority
                # HANDLE var__defaults
        #convert astSchemeStr back to ast
        if astSchemeStr is not None:
            schemeparser = Schemeparser(equationStr=astSchemeStr)
            ast, functionsD, variablesD, primitives, totalNodeCount, startPos__nodeId = schemeparser._parse()
            self.latexAST = ast; self.rootOfTree = schemeparser.rootOfTree
            # print('latexAST:')
            # print(self.latexAST);
            # print('self.rootOfTree:');
            # print(self.rootOfTree)
        else:
            self.latexAST = theAst















        # import pprint;pp = pprint.PrettyPrinter(indent=4)

        # def nodeMatch(gesuchteNode, targetNode):
        #     if gesuchteNode[0].startswith('$'): #its a variable
        #         return True# variables match anything in targetTree, ignores Optional|Compulsory
        #     return gesuchteNode[0] == targetNode[0]

        # def differenceBetweenOutputAndInput(instructions):
        #     # print('output versus input')
        #     # print(set(dict(instructions['outputTemplate']).keys()));
        #     # print(set([instructions['inputTemplate'][0]]));
        #     # print(list(set(dict(instructions['outputTemplate']).keys())-set([instructions['inputTemplate'][0]])))

        #     # import pdb;pdb.set_trace()

        #     #if set_difference compares by nodeId ONLY, then it will be right
        #     nodeDifferences, inNodeIds = [], set([instructions['inputTemplate'][0][0][1]])
        #     for inputTemplateParentNode in dict(instructions['outputTemplate']).keys():
        #         if inputTemplateParentNode[0][1] not in inNodeIds:
        #             nodeDifferences.append(inputTemplateParentNode)
        #     # import pdb;pdb.set_trace()
        #     return nodeDifferences
        #     # return list(set(dict(instructions['outputTemplate']).keys())-set([instructions['inputTemplate'][0]]))
        
        # #current__replaced-> for replacing child in parent's children
        # self.latexAST, current__replaced, badNodes, parentIdDifferenceToRemove = {}, {}, [], []
        # usedMatchedTrees = []

        # #topological_sort_BFS(top->bottom;left->bottom) for self.ast.items(), also to match the findTreeInTree
        # items = []
        # queue = [self.rootOfTree]
        # while len(queue) > 0:
        #     jetzt = queue.pop(0) # BFS
        #     kinder = self.ast.get(jetzt, [])
        #     queue += kinder
        #     if len(kinder) > 0:
        #         items.append((jetzt, kinder))



        # # for pNode, children in self.ast.items():#if this was processed from bottoms-up(topological_sort), then current__replaced will not have a problem| just do one more pass to replace parent's children
        # for pNode, children in items:
        #     list_instructions = self.getLatexSpecialCases(pNode[0], reverse=True)
        #     # print(pNode, children);import pdb;pdb.set_trace()
        #     candidateReplacements, candidateIndex__defaultsMatchedCount = [], dict(map(lambda t: (t[0], t[1]['reversePriority']), enumerate(list_instructions)))
        #     for candidateIndex, instructions in enumerate(list_instructions):####gives a list of candidate replacement......
        #         ######
        #         # print('instructions')
        #         # pp.pprint(instructions)
        #         ######
        #         templateNodeDifferenceToRemove = differenceBetweenOutputAndInput(instructions)
        #         candidate___current__replaced = {}
        #         outputTemplateRoot = None
        #         for outputTemplateParent, outputTemplateChildren in instructions['outputTemplate']:
        #             # import pdb;pdb.set_trace()
        #             if outputTemplateParent[2] == instructions['rootOfResultTemplate']: #only the id
        #                 outputTemplateRoot=outputTemplateParent
        #                 break
        #         # need to strip the outputTemplate of all the unnecessary arguments
        #         stripStack, outputTemplate = [outputTemplateRoot], {}
        #         while len(stripStack) > 0:
        #             tup = stripStack.pop()
        #             strippedChildren = []
        #             # print(dict(instructions['outputTemplate']));import pdb;pdb.set_trace()
        #             for child in dict(instructions['outputTemplate']).get(tup, []):
        #                 strippedChildren.append(child[0])
        #                 stripStack.append(child)
        #             if len(strippedChildren)>0:
        #                 outputTemplate[tup[0]] = strippedChildren
        #         outputTemplateRoot = outputTemplateRoot[0]
        #         #
        #         print('*******************************************************************************************************')
        #         print('matching pNode: ', pNode)
        #         print('usedMatchedTrees', usedMatchedTrees)
        #         print('outputTemplate: ', outputTemplate)
        #         print('outputTemplateRoot: ', outputTemplateRoot)
        #         var__val = {}
        #         #for same funcName (outputTemplateRoot), outputTemplateRoot:[matchedOutputTree] is CACHABLE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #         #matchedTrees should be order in which self.ast is processed, top->bottom;left->right
        #         #if here is top->bottom;left->right, then the above (self.ast.items) should also be top->bottom;left->right
        #         rootOfMatched = None
        #         for rootOfMatched, matchedOutputTree in FindTreeInTree.findAllTreeInTree(outputTemplate, outputTemplateRoot, self.ast, self.rootOfTree, nodeMatch):
        #             if (rootOfMatched, matchedOutputTree) in usedMatchedTrees:#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #                 continue
        #             print('~~~matchedOutputTree:', matchedOutputTree);import pdb;pdb.set_trace()
        #             #if tree has been matched, DO NOT USE IT AGAIN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #             #match the variables
        #             #callbackForMatchCompletion(targetTreeRoot):#<<<<<<<<<<<<<<<<<<<<<<<<<<refactor the _unparse with this NEW_FUNCTION
        #             templateStack, matchedStack = [outputTemplateRoot], [rootOfMatched]
        #             while len(templateStack) > 0 and len(matchedStack) > 0:
        #                 (templateName, templateId), (matchedName, matchedId) = templateStack.pop(), matchedStack.pop()
        #                 if templateName.startswith('$'):
        #                     var__val[templateName] = matchedName
        #                     # print('$$$$$$$matchedName', matchedName, instructions.get('var__defaults', {}).values()) # the default is 1, so we add 2 to choose this
        #                     if matchedName in instructions.get('var__defaults', {}).values():
        #                         candidateIndex__defaultsMatchedCount[candidateIndex] += 2
        #                 if templateId.startswith('$'):
        #                     var__val[templateId] = matchedId
        #                 # print(var__val);import pdb;pdb.set_trace()
        #                 templateStack += outputTemplate.get((templateName, templateId), [])
        #                 matchedStack += matchedOutputTree.get((matchedName, matchedId), [])
        #             break # just need one matched tree, this means last_used rootOfMatched will be put into usedMatchedTrees
        #         # print('var__val', var__val);import pdb;pdb.set_trace()
        #         #

        #         #match matched_variables into inputTemplate, entitystorage.insert missing variables->matched_inputTemplate
        #         templateParent, templateChildren = instructions['inputTemplate'] # we expecting only 1 line for instructions['inputTemplate']
        #         filledParentName = var__val.get(templateParent[0][0], templateParent[0][0])
        #         filledParentId = var__val.get(templateParent[0][1], templateParent[0][1])
        #         # print('filledParent:', (filledParentName, filledParentId));import pdb;pdb.set_trace()
        #         filledChildren = []
        #         for templateChild in templateChildren:
        #             filledChildName = var__val.get(templateChild[0][0], templateChild[0][0])#
        #             # print('filledChildName', filledChildName, 'defaults: ', instructions.get('var__defaults', {}).values())
        #             if filledChildName in instructions.get('var__defaults', {}).values(): #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<the more defaults it fits, the higher the priority of this candidateReplacement
        #                 candidateIndex__defaultsMatchedCount[candidateIndex] += 1
        #                 # print('matchedDefault, optional::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::', );import pdb;pdb.set_trace()
        #                 if templateChild[1]:#skip if optional
        #                     # print('skipping child$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        #                     continue
        #             filledChildId = var__val.get(templateChild[0][1], templateChild[0][1])#
        #             # print(templateChild);import pdb;pdb.set_trace()
        #             #
        #             if filledChildName.startswith('$') or str(filledChildId).startswith('$'):
        #                 continue#don't add this child
        #             # parentIdDifferenceToRemove using templateNodeDifferenceToRemove
        #             #fill up the nodes to ignore
        #             for templateNodeToRemove in templateNodeDifferenceToRemove:
        #                 templateNodeName, templateNodeId = templateNodeToRemove[0]
        #                 nodeToRemove = (var__val.get(templateNodeName, templateNodeName), var__val.get(templateNodeId, templateNodeId))
        #                 parentIdDifferenceToRemove.append(nodeToRemove)
        #                 candidate___current__replaced[nodeToRemove] = (filledParentName, filledParentId)
        #             #
        #             # print('parentIdDifferenceToRemove', parentIdDifferenceToRemove);import pdb;pdb.set_trace()
        #             filledChildren.append((filledChildName, filledChildId))
        #             # print(filledChildren, 'filedChildren<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        #         if len(filledChildren) == 0:#<<<< this is not accurate, if we cannot find child in var__val, should do optional|compulsory_matching with children (of pNode) TODO
        #             filledChildren = children
        #             filledParentName, filledParentId = pNode
        #         # print('latexAST',self.latexAST);import pdb;pdb.set_trace()
        #         # print('current__replaced', current__replaced)
        #         candidate___current__replaced[pNode] = (filledParentName, filledParentId)
        #         # print('candidate: ', {'candidate':{(filledParentName, filledParentId):filledChildren}, 'current__replaced':candidate___current__replaced})
        #         candidateReplacements.append({'candidate':{(filledParentName, filledParentId):filledChildren}, 'current__replaced':candidate___current__replaced}) 
        #     #
        #     if len(candidateIndex__defaultsMatchedCount) > 0: 
        #         # print('candidateReplacements:', candidateReplacements)
        #         # print('candidateIndex__defaultsMatchedCount', candidateIndex__defaultsMatchedCount);import pdb;pdb.set_trace()
                
        #         candidateReplacement = candidateReplacements[max(candidateIndex__defaultsMatchedCount.items(), key=lambda t:t[1])[0]]#IF DRAW?????????<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #         filledParent, filledChildren = list(candidateReplacement['candidate'].items())[0]
        #         current__replaced.update(candidateReplacement['current__replaced'])
        #         self.latexAST[filledParent] = filledChildren#
        #         if rootOfMatched is not None:
        #             usedMatchedTrees.append((rootOfMatched, matchedOutputTree))

        #         print('latexAST:', self.latexAST)
        #         # print('current__replaced:', current__replaced)
        #         #take out the difference between the instructions['outputTemplate'] and the instructions['inputTemplate']

        #     # if len(list_instructions) == 0:
        #     #     self.latexAST[pNode] = children

        # # print('badNodes', badNodes);import pdb;pdb.set_trace()
        # for pNode, children in self.ast.items():
        #     list_instructions = self.getLatexSpecialCases(pNode[0], reverse=True)
        #     if len(list_instructions) == 0 and pNode not in parentIdDifferenceToRemove:
        #         newChildren = []
        #         for child in children:
        #             newChildren.append(current__replaced.get(child, child))
        #         self.latexAST[pNode] = newChildren

        # print('replaced in parents children: ', self.latexAST)
        #     # #secondpass to replace parent's children, because we don't want to do topological_sort at the start
        #     # if len(list_instructions) > 0:
        #     #     newParent, newChildren = current__replaced.get(pNode, pNode), []
        #     #     for child in self.latexAST[newParent]:
        #     #         newChildren.append(current__replaced.get(child, child))
        #     #     self.latexAST[newParent] = newChildren


        #<<<<<<<<<<<<<<<<<<<<<<<<< for polynomials, like test__nonInfixBrackets__addImplicitMultiply; example: 1+(1+(1+1))=4, should be 1+1+1+1=4
        # from foundation.automat.common.termsofbaseop import TermsOfBaseOp
        # groupingByRightIdWithEarliestJoiner, groupsWithBaseOp = TermsOfBaseOp.nodeOfBaseOpByGroup(self.ast, '+') # should also return root of grouping, then we can check if parent of root is - TODO
        # from foundation.automat.common.flattener import Flattener
        # self.headsOfPlusTrees = []
        # groupingByRightId = []
        # # import pdb;pdb.set_trace()
        # for infoDict in groupingByRightIdWithEarliestJoiner:
        #     groupingByRightId.append(infoDict['group'])
        #     # import pdb;pdb.set_trace()
        #     # if len(infoDict['group']) > 1: # need the head and another, a group with just a head, then the head is not a head 
        #     self.headsOfPlusTrees.append(infoDict['earliestJoiner'])
        # self.plusIdsThatDoNotNeedBrackets = Flattener.flatten(groupingByRightId)


        #below for bracket formating, or we can use bracketstorage to add the old brackets back?

        """

    WHAT ABOUT THE NEW FUNCTIONS?
    6. 
    
    \\int \\iint \\iiint \\oint \\oiint
    \\lim  (\\to is an infix)
    \\sum  (this one has equals = at the base)
    \\prod  (this one has equals = at the base)
    \\nabla
    \\Delta
    \\partial
    \\cdot (dot product)
    (cross product)
    
    determinant (simplified as det?? only?)
    also 
    \\begin{vmatrix}\\end{vmatrix}
    \\begin{Vmatrix}\\end{Vmatrix}

        we assume that self.ast is a standard AST, we will store the transformed self.ast as self.latexAST

        Die Verschiedenen, die wir vorsichtiger merken mussen:
        [Scheme] => `Latex`
        1. [nroot] => `\\sqrt[n]`
        2. [/] => `\\frac`
        3. [(log a )] => `\\log` {if a = 10} or `\\ln` {if a = e} or `\\log_{a}`

        """


    def _classifyEntityType(self):
        #self.entitystorage.nodeId__entityType[nodeId]
        # self.entitystorage = EntityStorage()
        self.nodeId__entityType = {}
        stack = [self.rootOfTree]
        list_multiplicationNode = []
        while len(stack) > 0:
            node = stack.pop()
            if node[0] == '*':
                list_multiplicationNode.append(node)
            #
            if node[0] == '-' and self.latexAST[node][0][0] == '0':#implicit -
                self.nodeId__entityType[node[1]] = EntityType.IMPLICIT_INFIX
            elif node[0] in self.BACKSLASH_INFIX:
                self.nodeId__entityType[node[1]] = EntityType.BACKSLASH_INFIX
            elif node[0] in self.PRIOIRITIZED_INFIX+['=']:#PURE_INFIX
                self.nodeId__entityType[node[1]] = EntityType.PURE_INFIX
            elif node[0] in self.VARIABLENAMESTAKEANARG:
                self.nodeId__entityType[node[1]] = EntityType.BACKSLASH_VARIABLE
            elif isNum(node[0]):
                self.nodeId__entityType[node[1]] = EntityType.PURE_NUMBER
            elif self._getExpectedBackslashInputs(node[0]) is not None:
                self.nodeId__entityType[node[1]] = EntityType.BACKSLASH_FUNCTION
            elif self._getExpectedBackslashInputs(node[0]) is None and len(node[0]) <=1:
                self.nodeId__entityType[node[1]] = EntityType.PURE_VARIABLE
            elif self._getExpectedBackslashInputs(node[0]) is None and len(node[0]) > 1 and ('_' in node[0] or '^' in node[0]):
                self.nodeId__entityType[node[1]] = EntityType.COMPOSITE_VARIABLE
            elif self._getExpectedBackslashInputs(node[0]) is None and len(node[0]) > 1 and ('_' not in node[0] and '^' not in node[0]):
                self.nodeId__entityType[node[1]] = EntityType.BACKSLASH_NUMBER 

            #
            stack += self.latexAST.get(node, [])
        #check if these * are implicit
        for multiplicationNode in list_multiplicationNode:
            leftChild, rightChild = self.latexAST[multiplicationNode]
            leftChildEntityType, rightChildEntityType = self.nodeId__entityType[leftChild[1]], self.nodeId__entityType[rightChild[1]]
            #if both children are not INFIXES, then multiplicationNode is IMPLICIT_INFIX
            if (leftChildEntityType not in [EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX] or leftChild[0]!='^') or \
                (rightChildEntityType not in [EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX] or rightChild[0]!='^'):
                self.nodeId__entityType[multiplicationNode[1]] = EntityType.IMPLICIT_INFIX


    def _unparse(self): # TODO from AST to LaTeX string... 
        self._convertASTToLatexStyleAST()
        ###
        # import pprint;pp = pprint.PrettyPrinter(indent=4)
        # print('latexAST:', pp.pformat(self.latexAST));#import pdb;pdb.set_trace()
        ###
        self._classifyEntityType()
        return self._recursiveUnparse(self.rootOfTree, None)#we have OVERALLEquals self.overallEqual_startPos


    def _recursiveUnparse(self, node, parentNode):
        """
EntityTypes to handle:
    IMPLICIT_INFIX = 'implicit_infix'
    PURE_INFIX = 'pure_infix'
    BACKSLASH_INFIX = 'backslash_infix'


    BACKSLASH_FUNCTION = 'backslash_function'


    PURE_NUMBER = 'pure_number'
    PURE_VARIABLE = 'pure_variable'
    BACKSLASH_VARIABLE = 'backslash_variable'
    BACKSLASH_NUMBER = 'backslash_number'
    COMPOSITE_VARIABLE = 'composite_variable' # example V^{Q1}_{BE}, Voltage between B and E of transistor Q1



    MATRIX = 'matrix'

    FROM_CONVERSION = 'from_conversion' # entities added pendant conversion of latexAST to schemeAST NOT HERE

        """
        nodeName, nodeId = node
        entityType = self.nodeId__entityType[nodeId]#for unparser we do not have self.entitystorage yet.
        if entityType in [EntityType.COMPOSITE_VARIABLE]:
            #its a leaf
            return nodeName
        if entityType in [EntityType.PURE_NUMBER, EntityType.PURE_VARIABLE]:
            parentEntityType = self.nodeId__entityType[parentNode[1]]
            if parentEntityType in [EntityType.BACKSLASH_FUNCTION, EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX]:
                return nodeName
            return f'{nodeName} '# TODO do not put space if direct_parent, is enclosed by brackets, or direct_parent is infix<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        if entityType in [EntityType.BACKSLASH_NUMBER]:# this also wrongly includes i, e 
            parentEntityType = self.nodeId__entityType[parentNode[1]]
            if parentEntityType in [EntityType.BACKSLASH_FUNCTION, EntityType.BACKSLASH_INFIX]:
                return f'\\{nodeName}'
            return f'\\{nodeName} '
        if entityType in [EntityType.BACKSLASH_VARIABLE]:
            #should only have 1 variable as child?
            childNode = self.latexAST[node][0]
            return f'\\{nodeName}{{{childNode[0]}}}'
        if entityType in [EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX]:
            #ignore and put together, if infix, then with brackets, else just put together
            # print(node);import pdb;pdb.set_trace()
            leftNode, rightNode = self.latexAST[node][0], self.latexAST[node][1]
            leftStr, rightStr = self._recursiveUnparse(leftNode, node), self._recursiveUnparse(rightNode, node)
            leftEntityType, rightEntityType = self.nodeId__entityType[leftNode[1]], self.nodeId__entityType[rightNode[1]]
            if nodeName not in ['='] and (leftEntityType in [EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX] and leftNode[0]!='^'):
                leftStr = f'({leftStr})'
            if nodeName not in ['='] and (rightEntityType in [EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX] and rightNode[0]!='^'):
                rightStr = f'({rightStr})'
            if nodeName == '^' and len(rightNode[0])>1:
                rightStr = f'{{{rightStr}}}'
            if entityType in [EntityType.BACKSLASH_INFIX]:
                return f"{leftStr}{nodeName} {rightStr}"
            return f"{leftStr}{nodeName}{rightStr}"
        if entityType in [EntityType.BACKSLASH_FUNCTION]:
            childStrs = []
            for childNode in self.latexAST.get(node, []):
                childStrs.append(self._recursiveUnparse(childNode, node))
            templates = sorted(self._getExpectedBackslashInputs(nodeName), key=lambda d:d['argId'])
            #match optional|compulsory<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            optionalIndices = sorted(list(map(lambda d: d['argId'], filter(lambda d: d['optional'], templates))))
            compulsoryIndices = sorted(list(map(lambda d: d['argId'], filter(lambda d: not d['optional'], templates))))
            if len(childStrs)<len(compulsoryIndices): # not enough to fill up compulsory
                raise Exception()
            optionalIndicesToTake = optionalIndices[:len(childStrs)-len(compulsoryIndices)]
            indicesToTake = compulsoryIndices+optionalIndicesToTake
            templatesToUse = []
            for template in templates:
                if template['argId'] in indicesToTake:
                    templatesToUse.append(template)
            #
            #use preSym, and brackets to get the resulting string<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            resultingStr = f'\\{nodeName}'
            for template, childStr in zip(templatesToUse, childStrs):
                # print(template, childStr)
                if len(childStr) >  1 or template['braOptional']=='False' or nodeName in ['nabla']: # ULGY
                    childStr = f'{template["openBra"]}{childStr}{template["closeBra"]}'
                resultingStr+=f'{template['preSym']}{childStr}'
            return resultingStr

        #handle implicit_infix, we only have 2 types, - and *
        if entityType in [EntityType.IMPLICIT_INFIX]:
            if nodeName == '-':
                #remove the 0
                rightNode = self.latexAST[node][1]
                rightStr = self._recursiveUnparse(rightNode, node)
                return f'-{rightStr}'
            elif nodeName == '*':
                #ignore and put together, if infix, then with brackets, else just put together
                leftNode, rightNode = self.latexAST[node][0], self.latexAST[node][1]
                leftStr, rightStr = self._recursiveUnparse(leftNode, node), self._recursiveUnparse(rightNode, node)
                leftEntityType, rightEntityType = self.nodeId__entityType[leftNode[1]], self.nodeId__entityType[rightNode[1]]
                if (leftEntityType in [EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX] and leftNode[0]!='^'):
                    leftStr = f'({leftStr})'
                if (rightEntityType in [EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX] and rightNode[0]!='^'):
                    rightStr = f'({rightStr})'
                return f"{leftStr}{rightStr}"
            else:
                raise Exception()


        raise Exception(f"unHandled entityType: {entityType}")


    def latexToScheme(self):
        pass#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO<<<<<<<<scheme has to take a startNode


    @classmethod
    def makePlusAndMinus(cls, listOfPlusAndMinus, equivalentVariableDict):
        """
        used by ecircuit.equationFinders.equationfinder
        kvl
        kcl
        """
        latexStr = ''
        for i, dict_var in enumerate(listOfPlusAndMinus):
            if dict_var['positive']:
                if i != 0:
                    latexStr += f'+{dict_var["varStr"]}'
                else:
                    latexStr += dict_var["varStr"]
            else:
                latexStr += f'-{dict_var["varStr"]}'

        if equivalentVariableDict['positive']:
            return latexStr+f'={equivalentVariableDict["varStr"]}'
        else:
            return latexStr+f'=-{equivalentVariableDict["varStr"]}'
        # return latexStr+'=0'

    @classmethod
    def makeHarmonicPlusAndMinusEqualsZero(cls, listOfPlusAndMinus, equivalentVariableDict):
        """
        used by ecircuit.equationFinder.equationfinder
        compleximpedancesumequationfinder
        """
        latexStr = ''
        for i, dict_var in enumerate(listOfPlusAndMinus):
            if dict_var['positive']:
                if i != 0:
                    latexStr += f'+\\frac{{1}}{{{dict_var["varStr"]}}}'
                else:
                    latexStr += f'\\frac{{1}}{{{dict_var["varStr"]}}}'
            else:
                latexStr += f'-\\frac{{1}}{{{dict_var["varStr"]}}}'

        if equivalentVariableDict['positive']:
            return latexStr+f'=\\frac{{1}}{{{equivalentVariableDict["varStr"]}}}'
        else:
            return latexStr+f'=-\\frac{{1}}{{{equivalentVariableDict["varStr"]}}}'

    @classmethod
    def makePlusAndMinusEqualsZero(cls, listOfPlusAndMinus, equivalentVariableDict):
        """
        used by ecircuit.equationFinders.equationfinder
        resistorparallel
        capacitorseries
        inductorparallel
        """
        latexStr = ''
        for i, dict_var in enumerate(listOfPlusAndMinus):
            if dict_var['positive']:
                if i != 0:
                    latexStr += f'+\\frac{{1}}{{{dict_var["varStr"]}}}'
                else:
                    latexStr += f'\\frac{{1}}{{{dict_var["varStr"]}}}'
            else:
                latexStr += f'-\\frac{{1}}{{{dict_var["varStr"]}}}'
        if equivalentVariableDict['positive']:
            return latexStr+f'={equivalentVariableDict["varStr"]}'
        else:
            return latexStr+f'=-{equivalentVariableDict["varStr"]}'


    @classmethod
    def makeSimpleRatio(self, equivalentRatio, numerator, denominator):
        """
        used by ecircuit.equationFinders.equationfinder
        OhmsLaw
        """
        return f'\\frac{{{numerator}}}{{{denominator}}}={equivalentRatio}'

    @classmethod
    def makeFirstOrderSeparableDifferentialEquation(self, equivalent, derivativeMultiplier, differentiand, differentiator):
        """
        used by ecircuit.equationFinders.equationfinder
        capacitortiming
        inductortiming
        """
        return f'{equivalent} = {derivativeMultiplier} \\frac{{d {differentiand}}}{{d {differentiator}}}'

    @classmethod
    def makeLinearFirstOrderDifferentialEquation(self, equivalent, listOfTerms):
        """#solving steps are here: https://en.wikipedia.org/wiki/Matrix_differential_equation <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<automate when you reach many BJT
        listOfTerms = [
            {'coefficient':, 'differentiand': , 'differentiator': },
        ]
        """
        firstTerm = listOfTerms
        RHS = f'{firstTerm["coefficient"]} \\frac{{d {firstTerm["differentiand"]}}}{{d {firstTerm["differentiator"]}}}'
        for term in listOfTerms[1:]:
            RHS += f'+{term["coefficient"]} \\frac{{d {term["differentiand"]}}}{{d {term["differentiator"]}}}'
        return f'{equivalent}={RHS}'


    @classmethod
    def makeRatio(self, numerator, denominator):
        return f'\\frac{{{numerator}}}{{{denominator}}}'

    @classmethod
    def exponentialMinusOne(self, equivalent, multiplicative, exponent):
        return f'{equivalent}={multiplicative} (e^{{{exponent}}} -1)'


class EntityStorage:
    """
    Entity is a node that is found in the equationStr, might or might not, have all its args (might not have widthStart, widthEnd)

    This acts like a database for Entities, allowing CRUD

    WHAT ARE THE QUERIES? THIS WILL DETERMINE THE UNDERLYING DATASTRUCTURE.
    Q3:StatisticalCounts
    """


    def __init__(self, equationStr):
        self.equationStr = equationStr
        self.eqStrLen = len(equationStr)
        self.node_id = 0

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<needs to be tagged with nodeId.. or your algo, doesn't work.
        self.list_tuple_widthStart_nodeId = [] # for BS, OR it can hold tuples. with nodeId, and then nodeId to everything else., find widthStart instead of id
        self.list_tuple_widthEnd_nodeId = [] # for BS


        self.nodeId__widthStart = {}
        self.nodeId__widthEnd = {}
        self.entityType__list_nodeId = {}
        self.funcStart__nodeId = {}
        self.funcName__list_nodeId = {}
        #nodeId -> datum 
        self.nodeId__entityType = {}
        self.nodeId__funcName = {}
        self.nodeId__funcStart = {}
        self.nodeId__funcEnd = {}
        #p|c 
        self.tuple_nodeId_argIdx__pNodeId = {} # p(arent)NodeId_argIdx CONFIRMED p|c
        self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {} #c(hild)ArgIdx UNCONFIRMED p|c ( we only know the argument width.)


    def getAllEntityIdWithinFuncStartAndFuncEnd(self, startPos, endPos):
        list_tuple_nodeId_funcName_funcStart_funcEnd = []
        for nodeId, funcStart in self.nodeId__funcStart.items():#using self.funcStart__nodeId have collisions for implicit - (#fix? TODO)
            if startPos <= funcStart and funcStart <= endPos:
                list_tuple_nodeId_funcName_funcStart_funcEnd.append((nodeId, self.nodeId__funcName[nodeId], funcStart, self.nodeId__funcEnd[nodeId]))
        return list_tuple_nodeId_funcName_funcStart_funcEnd


    def insert(self, funcName, funcStart, funcEnd, entityType, parentNodeId=None, argIdx=None, widthStart=None, widthEnd=None, bracketstorage=None):
        nodeId = self._getNodeId()
        self.nodeId__entityType[nodeId] = entityType
        self.nodeId__funcName[nodeId] = funcName
        self.nodeId__funcStart[nodeId] = funcStart
        self.nodeId__funcEnd[nodeId] = funcEnd
        self.funcStart__nodeId[funcStart] = nodeId

        exlist_nodeId = self.funcName__list_nodeId.get(funcName, [])
        exlist_nodeId.append(nodeId)
        self.funcName__list_nodeId[funcName] = exlist_nodeId

        existing = self.entityType__list_nodeId.get(entityType, [])
        insertPos = BinarySearch.binarySearchPre(existing, nodeId)
        existing.insert(insertPos, nodeId)
        self.entityType__list_nodeId[entityType] = existing

        if widthStart is not None:
            self.nodeId__widthStart[nodeId] = widthStart

            insertPos = BinarySearch.binarySearchPre(self.list_tuple_widthStart_nodeId, widthStart, key=lambda t: t[0])
            self.list_tuple_widthStart_nodeId.insert(insertPos, (widthStart, nodeId))

        if widthEnd is not None:
            self.nodeId__widthEnd[nodeId] = widthEnd

            insertPos = BinarySearch.binarySearchPre(self.list_tuple_widthEnd_nodeId, widthEnd, key=lambda t: t[0])
            self.list_tuple_widthEnd_nodeId.insert(insertPos, (widthEnd, nodeId))

        if parentNodeId is not None and argIdx is not None: # if usr gives, then we assume this p|c is confirmed
            #<<<<<<<<<<<<<<<<<<<<differ to addConfirmed
            self.addConfirmedPCrelationshipById(parentNodeId, nodeId, argIdx, bracketstorage=bracketstorage)
        elif entityType in [EntityType.IMPLICIT_INFIX, EntityType.PURE_INFIX]:#everytime, infix added, AUTO add 2 unconfirmed.
            self.addUnConfirmedPCrelationship(funcStart, 0, None, 0, None, funcStart)#SLOTS open to all possibilities
            self.addUnConfirmedPCrelationship(funcStart, 1, None, funcStart, None, self.eqStrLen)

        if bracketstorage:
            return bracketstorage
        return nodeId

    def addUnConfirmedPCrelationship(self, funcStart, argId, openBraType, openBraPos, closeBraType, closeBraPos):
        """
self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {} #c(hild)ArgIdx UNCONFIRMED p|c ( we only know the argument width.)
        """
        nodeId = self.funcStart__nodeId[funcStart]
        self.addUnConfirmedPCrelationshipById(nodeId, argId, openBraType, openBraPos, closeBraType, closeBraPos)

    def addUnConfirmedPCrelationshipById(self, nodeId, argId, openBraType, openBraPos, closeBraType, closeBraPos):
        self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos[(nodeId, argId)] = (openBraType, openBraPos, closeBraType, closeBraPos)


    def addConfirmedPCrelationship(self, pFuncStart, cNodeId, argIdx, bracketstorage=None):
        pNodeId = self.funcStart__nodeId[pFuncStart]
        return self.addConfirmedPCrelationshipById(pNodeId, cNodeId, argIdx, bracketstorage=bracketstorage)

    def addConfirmedPCrelationshipById(self, pNodeId, cNodeId, argIdx, bracketstorage=None):
        #remove from UNCONFIRMED: self.nodeId__tuple_cArgIdx_openBra_openBraPos_closeBra_closeBraPos
        # self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos.pop((pNodeId, argIdx), None)
        #add to confirmed p|c:
        self.tuple_nodeId_argIdx__pNodeId[(cNodeId, argIdx)] = pNodeId
        #UPDATE width if EntityType == infix
        if self.nodeId__entityType[pNodeId] in [EntityType.IMPLICIT_INFIX, EntityType.PURE_INFIX]:
            if argIdx == 0: #only need to update widthStart to child's
                cWidthStart = self.nodeId__widthStart[cNodeId]
                # self.updateWidth(pNodeId, cWidthStart, None) # might ge wrong, if enclosing bracket was updated first
                self.widthMaxUpdateById(pNodeId, cWidthStart, self.nodeId__widthEnd[pNodeId])#bigger is correct
            elif argIdx == 1: #only need to update widthEnd to child's
                cWidthEnd = self.nodeId__widthEnd[cNodeId]
                # self.updateWidth(pNodeId, None, cWidthEnd) # might ge wrong, if enclosing bracket was updated first
                self.widthMaxUpdateById(pNodeId, self.nodeId__widthStart[pNodeId], cWidthEnd)#bigger is correct
            else:
                raise Exception(f'infix nodeId: {pNodeId}, argIdx not 0 nor 1: {argIdx}')

        if bracketstorage is not None: #update infix width and all enclosing brackets <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            self.__updateTemplatesToWiderEnclosingBracketsAndRemove([pNodeId], bracketstorage)
            return bracketstorage

    def existEntityAt(self, funcName, pos):#funcName is the actual symbol like '^', TODO rename to existFuncNameAt
        list_nodeId = self.funcName__list_nodeId.get(funcName, [])
        list_funcStart = list(map(lambda nodeId: self.nodeId__funcStart[nodeId], list_nodeId))
        return pos in list_funcStart#funcStart == pos

    def widthMaxUpdateById(self, nodeId, widthStart, widthEnd):
        if widthStart is not None:
            widthStart = min(widthStart, self.nodeId__widthStart[nodeId])#<<<<<<<<<<<<<<<<<<<<<<<<<should be min? so that width is maximised?
        if widthEnd is not None:
            widthEnd = max(widthEnd, self.nodeId__widthEnd[nodeId])
        self.updateWidth(nodeId, widthStart, widthEnd)


        entityType = self.nodeId__entityType[nodeId]
        if entityType in [EntityType.IMPLICIT_INFIX, EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX]:
            #leftEnd
            if (nodeId, 0) in self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos: #might not exist because removed by caller like "addConfirmedPCrelationship"
                l = list(self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos.get((nodeId, 0)))
                l[1] = widthStart
                self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos[(nodeId, 0)] = tuple(l)
            #rightEnd
            if (nodeId, 1) in self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos: # might not exist because removed by caller like "addConfirmedPCrelationship"
                r = list(self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos.get((nodeId, 1)))
                r[3] = widthEnd
                self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos[(nodeId, 1)] = tuple(r)

    #not used... remove?
    def widthMaxUpdate(self, funcStart, widthStart, widthEnd): #update to max(current, width), if None, then do not update
        nodeId = self.funcStart__nodeId[funcStart]
        self.widthMaxUpdateById(nodeId, widthStart, widthEnd)

    def updateFuncName(self, nodeId, funcName):
        #funcName__list_nodeId
        #nodeId__funcName
        oldFuncName = self.nodeId__funcName[nodeId]

        #remove old
        list_nodeId = self.funcName__list_nodeId.get(oldFuncName, [])
        list_nodeId.remove(nodeId)
        if len(list_nodeId) == 0:
            del self.funcName__list_nodeId[oldFuncName]
        else:
            self.funcName__list_nodeId[oldFuncName] = list_nodeId

        del self.nodeId__funcName[nodeId]

        #add new
        list_nodeId = self.funcName__list_nodeId.get(funcName, [])
        list_nodeId.append(nodeId)
        self.funcName__list_nodeId[funcName] = list_nodeId

        self.nodeId__funcName[nodeId] = funcName


    def updateEntityType(self, nodeId, entityType):
        #entityType__list_nodeId
        #nodeId__entityType
        oldEntityType = self.nodeId__entityType[nodeId]

        #remove old
        list_nodeId = self.entityType__list_nodeId.get(oldEntityType, [])
        list_nodeId.remove(nodeId)
        if len(list_nodeId) == 0:
            self.entityType__list_nodeId[oldEntityType]
        else:
            self.entityType__list_nodeId[oldEntityType] = list_nodeId

        del self.nodeId__entityType[nodeId]


        #add new
        list_nodeId = self.entityType__list_nodeId.get(entityType, [])
        list_nodeId.append(nodeId)
        self.entityType__list_nodeId[entityType] = list_nodeId

        self.nodeId__entityType[nodeId] = entityType


    def updateFuncEnd(self, nodeId, funcEnd):
        #nodeId__funcEnd
        self.nodeId__funcEnd[nodeId] = funcEnd





    def getAllUnConfirmedPCrelationship(self, pNodeId): # SLOT
        """
        unconfirmed:
        self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos # can only filter.... if we have a nodeId__list_cArgIdx, then it will be much faster??? TODO
        """
        list_tuple_openBraPos_closeBraPos_argIdx = []
        for (_, cArgIdx), (_, openBraPos, _, closeBraPos) in filter(
            lambda t: t[0][0]==pNodeId, self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos.items()):
            list_tuple_openBraPos_closeBraPos_argIdx.append((openBraPos, closeBraPos, cArgIdx))
        return list_tuple_openBraPos_closeBraPos_argIdx


    # remove? <<<<<<<<<<<<<<<<<<<<<<<<<<<<replace with self.__updateEntityToWiderWidth
    def __updateTemplatesToWiderEnclosingBracketsAndRemove(self, nodeIds, bracketstorage): #TODO rename to __updateEntitiesToWiderEnclosingBrackets
        for nodeId in nodeIds:
            widthStart = self.nodeId__widthStart[nodeId]
            #because we exclude the front_backslash_character that we removed so that touching matches
            entityType = self.nodeId__entityType[nodeId]
            widthEnd = self.nodeId__widthEnd[nodeId]
            selectedOpenClosePos = bracketstorage.getTightestEnclosingPos(self.nodeId__funcStart[nodeId], BracketType.ROUND)
            if selectedOpenClosePos:
                self.widthMaxUpdate(self.nodeId__funcStart[nodeId], selectedOpenClosePos[0], selectedOpenClosePos[1])
        return bracketstorage
    # remove? <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def __updateEntitiesToWiderEnclosingBracket(self, nodeId, bracketstorage):
        widthStart = self.nodeId__widthStart[nodeId]
        updated = False
        #because we exclude the front_backslash_character that we removed so that touching matches
        entityType = self.nodeId__entityType[nodeId]
        widthEnd = self.nodeId__widthEnd[nodeId]
        selectedOpenClosePos = bracketstorage.getTightestEnclosingPos(self.nodeId__funcStart[nodeId], BracketType.ROUND)
        if selectedOpenClosePos:
            self.updateWidth(nodeId, selectedOpenClosePos[0], selectedOpenClosePos[1])
            # print('startWidth', selectedOpenClosePos[0], 'endWidth', selectedOpenClosePos[1])
            updated = True
        return bracketstorage, updated

    def __updateEntitiesToWiderLeftEntities(self, nodeId, bracketstorage):#besides brackets, might be other entities
        funcStart, funcEnd = self.nodeId__funcStart[nodeId], self.nodeId__funcEnd[nodeId]
        updated = False
        list_tuple_nodeId_funcEnd = sorted(list(self.nodeId__funcEnd.items()), key=lambda tup: tup[1])#cannot be by funcStart because implicit have the same funcStart as some existing entities
        idxOfNodeId = list_tuple_nodeId_funcEnd.index((nodeId, funcEnd))
        if idxOfNodeId>0:
            nodeIdOfEntityLeftOfNodeId = list_tuple_nodeId_funcEnd[idxOfNodeId - 1][0]
            leftEntityType = self.nodeId__entityType[nodeIdOfEntityLeftOfNodeId]
            if leftEntityType in [EntityType.IMPLICIT_INFIX, EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX]:
                widthStart = self.nodeId__funcStart[nodeIdOfEntityLeftOfNodeId]
            else:
                widthStart = self.nodeId__widthStart[nodeIdOfEntityLeftOfNodeId]
            self.updateWidth(nodeId, widthStart,
                funcEnd)#no change to widthEnd
            # print('updated to nodeId of ', nodeIdOfEntityLeftOfNodeId, 'widthStart: ', widthStart, 'wdithEnd:', self.nodeId__funcEnd[nodeId])
            updated = True
        return bracketstorage, updated

    def __updateEntitiesToWiderRightEntities(self, nodeId, bracketstorage):#besides brackets, might be other entities
        funcStart, funcEnd = self.nodeId__funcStart[nodeId], self.nodeId__funcEnd[nodeId]
        updated = False
        list_tuple_nodeId_funcEnd = sorted(list(self.nodeId__funcEnd.items()), key=lambda tup: tup[1])#cannot be by funcStart because implicit have the same funcStart as some existing entities
        idxOfNodeId = list_tuple_nodeId_funcEnd.index((nodeId, funcEnd))
        if idxOfNodeId<len(list_tuple_nodeId_funcEnd) - 1:
            nodeIdOfEntityRightOfNodeId = list_tuple_nodeId_funcEnd[idxOfNodeId + 1][0]
            rightEntityType = self.nodeId__entityType[nodeIdOfEntityRightOfNodeId]
            if rightEntityType in [EntityType.IMPLICIT_INFIX, EntityType.PURE_INFIX, EntityType.BACKSLASH_INFIX]:
                widthEnd = self.nodeId__funcEnd[nodeIdOfEntityRightOfNodeId]
            else:
                widthEnd = self.nodeId__widthEnd[nodeIdOfEntityRightOfNodeId]

            self.updateWidth(nodeId, funcStart, #no change to widthStart
                widthEnd)
            # print('updated to nodeId of ', nodeIdOfEntityRightOfNodeId, 'widthStart: ', self.nodeId__funcStart[nodeId], 'wdithEnd:', widthEnd)
            updated = True
        return bracketstorage, updated


    def __updateInfixesToWiderLeftBracket(self, infixNodeIdx, bracketstorage, latexParser):
        funcStart = self.nodeId__funcStart[infixNodeIdx]
        updated = False
        for closeBra in BracketType.closeBras():
            possibleCloseBraPos = funcStart-len(closeBra)
            if self.equationStr[possibleCloseBraPos] == closeBra:
                openBraPos, _ = bracketstorage.getCorrespondingOpenBraPos(possibleCloseBraPos)
                if latexParser.isPosInBackslashBrackets(openBraPos):
                    return bracketstorage, updated
                self.updateWidth(infixNodeIdx, openBraPos, 
                    self.nodeId__widthEnd[infixNodeIdx])#no change to widthEnd
                # print('updated widthStart', openBraPos, 'widthEnd', self.nodeId__widthEnd[infixNodeIdx])
                updated = True
                break
        return bracketstorage, updated


    def __updateInfixesToWiderRightBracket(self, infixNodeIdx, bracketstorage, latexParser):
        funcEnd = self.nodeId__funcEnd[infixNodeIdx]
        updated = False
        for openBra in BracketType.openBras():
            possibleOpenBraPos = funcEnd+len(openBra)
            if possibleOpenBraPos<len(self.equationStr) and self.equationStr[possibleOpenBraPos] == openBra and not latexParser.isPosInBackslashBrackets(possibleOpenBraPos):
                closeBraPos, _ = bracketstorage.getCorrespondingCloseBraPos(possibleOpenBraPos)
                self.updateWidth(infixNodeIdx, self.nodeId__widthStart[infixNodeIdx], #no change to widthStart
                closeBraPos)
                # print('updated widthStart', self.nodeId__widthStart[infixNodeIdx], 'widthEnd', closeBraPos)
                updated = True
                break
        return bracketstorage, updated

    def __updateEntityToWiderWidth(self, nodeIds, bracketstorage, latexParser):
        """Width for all the possible EntityTypes

        For INFIX
        left|rightBra
        tightestenclosingBracket
        left|rightEntity


        For BACKSLASH
        itself+all_its_args

        For VARIABLE|NUMBER
        just_itself
        """
        for nodeId in nodeIds:

            entityType = self.nodeId__entityType[nodeId]

            if entityType in [EntityType.IMPLICIT_INFIX, EntityType.BACKSLASH_INFIX, EntityType.PURE_INFIX]:
                self.bracketstorage, updated = self.__updateInfixesToWiderLeftBracket(nodeId, bracketstorage, latexParser)
                self.bracketstorage, updated = self.__updateInfixesToWiderRightBracket(nodeId, bracketstorage, latexParser)

                if not updated:
                    self.bracketstorage, updated = self.__updateEntitiesToWiderEnclosingBracket(nodeId, bracketstorage)

                    if not updated:
                        self.bracketstorage, updated = self.__updateEntitiesToWiderLeftEntities(nodeId, bracketstorage)
                        self.bracketstorage, updated = self.__updateEntitiesToWiderRightEntities(nodeId, bracketstorage)

        return bracketstorage

        #not used, remove?
    def getWidestFits(self, openBraPos, closeBraPos, selfNodeId):# get widest nodeId that still between (openBraPos, closeBraPos)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """
        selfNodeId is a nodeId we should not return
        """

        list_nodeIdContaining = self.getAllContainingByWidth(openBraPos, closeBraPos)
        if selfNodeId in list_nodeIdContaining:
            list_nodeIdContaining.remove(selfNodeId)
        maxWidth, maxNodeId, maxFuncName = float('-inf'), None, None
        for nodeId in list_nodeIdContaining:
            width = self.nodeId__widthEnd[nodeId] - self.nodeId__widthStart[nodeId]
            if width > maxWidth:
                maxWidth = width; maxNodeId = nodeId; maxFuncName = self.nodeId__funcName[nodeId]

        listOfWidestFits = []#might have many widestFits
        for nodeId in list_nodeIdContaining:
            width = self.nodeId__widthEnd[nodeId] - self.nodeId__widthStart[nodeId]
            if width == maxWidth:
                listOfWidestFits.append((nodeId, self.nodeId__funcName[nodeId], self.nodeId__funcStart[nodeId], self.nodeId__funcEnd[nodeId]))
        return listOfWidestFits

    #not used, remove?
    def getAllContainingByWidth(self, startPos, endPos):#all the entities within startPos and endPos, 
        startWidthIdx = BinarySearch.binarySearchPre(self.list_tuple_widthStart_nodeId, startPos, key=lambda t:t[0])
        endWidthIdx = BinarySearch.binarySearchPre(self.list_tuple_widthEnd_nodeId, endPos, key=lambda t:t[0], breakTie='r')#breakTie give right most, there might be multiple same endWidth of implicit add implicit mul
        set_containingNodeIdByStartWidth = set(map(lambda t:t[1], self.list_tuple_widthStart_nodeId[startWidthIdx:]))#verysimiliar0refactor?ONLYdifferIn:PositionTODO
        set_containingNodeIdByEndWidth = set(map(lambda t:t[1], self.list_tuple_widthEnd_nodeId[:endWidthIdx+1]))#verysimiliar0refactor?ONLYdifferIn:PositionTODO
        #off by 1 revealed by test__entityStorage__getWidestFit0
        list_nodeId = list(set_containingNodeIdByStartWidth.intersection(set_containingNodeIdByEndWidth))
        return list_nodeId


    def getAllEntityByFuncName(self, sFuncName):
        list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd = []
        for nodeId, funcName in self.nodeId__funcName.items():
            if funcName == sFuncName:
                list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd.append((
                    nodeId, self.nodeId__funcName[nodeId], self.nodeId__widthStart[nodeId], self.nodeId__widthEnd[nodeId], self.nodeId__funcStart[nodeId], self.nodeId__funcEnd[nodeId]
                ))
        return list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd


    def getAllNodeIdFuncNameWidthStartWidthEnd(self, *entityTypes):
        if len(entityTypes) == 0:
            entityTypes = list(EntityType.__members__.values())
        list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd = []
        for entityType in entityTypes:
            for nodeId in self.entityType__list_nodeId.get(entityType, []):
                list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd.append((
                    nodeId, self.nodeId__funcName[nodeId], self.nodeId__widthStart[nodeId], self.nodeId__widthEnd[nodeId], self.nodeId__funcStart[nodeId], self.nodeId__funcEnd[nodeId]
                ))
        return sorted(list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd, key=lambda t: t[4])

    def getEntityImmediateLeftOfPos(self, pos):
        idx = BinarySearch.binarySearchPre(self.list_tuple_widthEnd_nodeId, pos, key=lambda t:t[0])
        nodeId = self.list_tuple_widthEnd_nodeId[idx][1]#[idx-1][1]
        return nodeId

    def getEntityImmediateRightOfPos(self, pos):
        idx = BinarySearch.binarySearchPre(self.list_tuple_widthStart_nodeId, pos, key=lambda t:t[0])
        nodeId = self.list_tuple_widthStart_nodeId[idx][1]
        return nodeId

    #not used for INFIXES, please remove slots for infixes
    def getSlots(self, nodeId):# get all the slots of nodeId
        slots = []
        for (pNodeId, cArgIdx), (_, openSlotPos, _, closeSlotPos) in self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos.items():
            if pNodeId == nodeId:
                slots.append((openSlotPos, closeSlotPos, cArgIdx))
        return slots


    def removeEntityBetween(self, funcStart, funcEnd):
        # print('removeEntityBetween', funcStart, funcEnd)
        entitiesFuncStartToRemove = set() # because nodeId__funcStart len changes and Python will throw
        for nodeId, eFuncStart in self.nodeId__funcStart.items():
            if funcStart <= eFuncStart:
                eFuncEnd = self.nodeId__funcEnd[nodeId]
                if eFuncEnd <= funcEnd:
                    entitiesFuncStartToRemove.add(eFuncStart)

        # print('funcStarts to remove: ', entitiesFuncStartToRemove)
        for funcStart in entitiesFuncStartToRemove:
            self.remove(funcStart)

    def removeById(self, nodeId):#TODO REFACTOR WHOLE CODE to use this 'remove', instead
        funcStart = self.nodeId__funcStart.pop(nodeId)

        self.funcStart__nodeId.pop(funcStart, None)

        entityType = self.nodeId__entityType.pop(nodeId)
        funcName = self.nodeId__funcName.pop(nodeId, None)
        self.nodeId__funcStart.pop(nodeId, None)
        self.nodeId__funcEnd.pop(nodeId, None)
        exlist_nodeId = self.funcName__list_nodeId.get(funcName, [])
        exlist_nodeId.remove(nodeId)
        if len(exlist_nodeId) ==0:
            self.funcName__list_nodeId.pop(funcName, None)
        else:
            self.funcName__list_nodeId[funcName] = exlist_nodeId

        #TODO removal of p|c relationship<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< and all the argIdx all children,so we loop through
        new___tuple_nodeId_argIdx__pNodeId = {}
        for (nodeId0, argIdx), pNodeId in self.tuple_nodeId_argIdx__pNodeId.items():
            if nodeId0 == nodeId or pNodeId == nodeId:
                continue
            new___tuple_nodeId_argIdx__pNodeId[(nodeId0, argIdx)] = pNodeId
        self.tuple_nodeId_argIdx__pNodeId = new___tuple_nodeId_argIdx__pNodeId 

        new___tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {}
        for (nodeId0, cArgIdx), braTup in self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos.items():
            if nodeId0 == nodeId:
                continue
            new___tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos[(nodeId0, cArgIdx)] = braTup
        self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = new___tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos

        list_nodeId = self.entityType__list_nodeId.pop(entityType)
        list_nodeId.remove(nodeId)
        if len(list_nodeId) ==0:
            self.entityType__list_nodeId.pop(entityType, None)
        else:
            self.entityType__list_nodeId[entityType] = list_nodeId

        widthEnd = self.nodeId__widthEnd.pop(nodeId, None)
        widthStart = self.nodeId__widthStart.pop(nodeId, None)

        if widthStart is not None:
            self.list_tuple_widthStart_nodeId.remove((widthStart, nodeId))

        if widthEnd is not None:
            self.list_tuple_widthEnd_nodeId.remove((widthEnd, nodeId))


    def remove(self, funcStart):
        """This is used by _find_backslash, TODO unit_test
        """
        nodeId = self.funcStart__nodeId[funcStart]
        self.removeById(nodeId)


    def updateWidth(self, nodeId, widthStart, widthEnd): ##########<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<clean up the updatewidths, its confusing
        """
        widths to update : maybe a method update WIDTH? can put into insert also?
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    self.list_tuple_widthStart_nodeId = [] # for BS, OR it can hold tuples. with nodeId, and then nodeId to everything else., find widthStart instead of id
    self.list_tuple_widthEnd_nodeId = [] # for BS
    self.nodeId__widthStart = {}
    self.nodeId__widthEnd = {}
        """
        if widthStart is not None:
            oldWidthStart = self.nodeId__widthStart[nodeId]
            self.nodeId__widthStart[nodeId] = widthStart
            if (oldWidthStart, nodeId) in self.list_tuple_widthStart_nodeId:
                idx = self.list_tuple_widthStart_nodeId.index((oldWidthStart, nodeId))
                self.list_tuple_widthStart_nodeId.pop(idx)
                insertIdx = BinarySearch.binarySearchPre(self.list_tuple_widthStart_nodeId, widthStart, key=lambda t:t[0])
                self.list_tuple_widthStart_nodeId.insert(insertIdx, (widthStart, nodeId))


        if widthEnd is not None:
            oldWidthEnd = self.nodeId__widthEnd[nodeId]
            self.nodeId__widthEnd[nodeId] = widthEnd
            if (oldWidthEnd, nodeId) in self.list_tuple_widthEnd_nodeId:
                idx = self.list_tuple_widthEnd_nodeId.index((oldWidthEnd, nodeId)) # refactor this TODO with the insert function
                self.list_tuple_widthEnd_nodeId.pop(idx)
                insertIdx = BinarySearch.binarySearchPre(self.list_tuple_widthEnd_nodeId, widthEnd, key=lambda t:t[0])
                self.list_tuple_widthEnd_nodeId.insert(insertIdx, (widthEnd, nodeId))



    def updateIfExists(self, funcPos, entityType=None, widthStart=None, widthEnd=None):#TODO include other possible updates to the fields
        nodeId = self.funcStart__nodeId[funcPos]
        #remove old
        oEntityType = self.nodeId__entityType.pop(nodeId)
        olist_nodeId = self.entityType__list_nodeId[oEntityType]
        olist_nodeId.remove(nodeId)
        self.entityType__list_nodeId[oEntityType] = olist_nodeId
        #add new
        self.nodeId__entityType[nodeId] = entityType
        elist_nodeId = self.entityType__list_nodeId.get(entityType, [])
        elist_nodeId.append(nodeId)
        self.entityType__list_nodeId[entityType] = elist_nodeId

        #width
        self.updateWidth(nodeId, widthStart, widthEnd)
        #TODO log to tell the user 
        return nodeId

    def __str__(self):
        """

        #TODO prefix the internal states, and use self to find in a single loop



        self.list_tuple_widthStart_nodeId = [] # for BS, OR it can hold tuples. with nodeId, and then nodeId to everything else., find widthStart instead of id
        self.list_tuple_widthEnd_nodeId = [] # for BS


        self.nodeId__widthStart = {}
        self.nodeId__widthEnd = {}
        self.entityType__list_nodeId = {}
        self.funcStart__nodeId = {}
        self.funcName__nodeId = {}
        #nodeId -> datum 
        self.nodeId__entityType = {}
        self.nodeId__funcName = {}
        self.nodeId__funcStart = {}
        self.nodeId__funcEnd = {}
        #p|c 
        self.tuple_nodeId_argIdx__pNodeId = {} # p(arent)NodeId_argIdx CONFIRMED p|c
        self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {} #c(hild)ArgIdx UNCONFIRMED p|c ( we only know the argument width.)

        """
        import os
        import pprint
        pp = pprint.PrettyPrinter(indent=4)

        nodeId__tuple_funcName_funcStart_funcEnd_widthStart_widthEnd = {}
        for nodeId, funcName in self.nodeId__funcName.items():
            funcStart = self.nodeId__funcStart[nodeId]
            funcEnd = self.nodeId__funcEnd[nodeId] # for user to tell implicit
            widthStart = self.nodeId__widthStart[nodeId]
            widthEnd = self.nodeId__widthEnd[nodeId]
            nodeId__tuple_funcName_funcStart_funcEnd_widthStart_widthEnd[nodeId] = (funcName, funcStart, funcEnd, widthStart, widthEnd)

        s = 'nodeId__tuple_funcName_funcStart_funcEnd_widthStart_widthEnd' +os.linesep
        s += pp.pformat(nodeId__tuple_funcName_funcStart_funcEnd_widthStart_widthEnd) # fo easy usage

        s += pp.pformat(self.tuple_nodeId_argIdx__pNodeId)+os.linesep
        s += 'tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos'+os.linesep#UNCONFIRMED

        tuple_nodeId_funcName_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos = {}
        for (nodeId, cArgIdx), v in self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos.items():
            tuple_nodeId_funcName_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos[(nodeId, self.nodeId__funcName[nodeId], cArgIdx)] = v

        s += pp.pformat(tuple_nodeId_funcName_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos)+os.linesep

        #below for checking system functioning
        s += 'list_tuple_widthStart_nodeId'+os.linesep
        s += pp.pformat(self.list_tuple_widthStart_nodeId)+os.linesep
        s += 'list_tuple_widthEnd_nodeId'+os.linesep
        s += pp.pformat(self.list_tuple_widthEnd_nodeId)+os.linesep
        s += 'nodeId__widthStart'+os.linesep
        s += pp.pformat(self.nodeId__widthStart)+os.linesep
        s += 'nodeId__widthEnd'+os.linesep
        s += pp.pformat(self.nodeId__widthEnd)+os.linesep
        s += 'entityType__list_nodeId'+os.linesep
        s += pp.pformat(self.entityType__list_nodeId)+os.linesep
        s += 'funcStart__nodeId'+os.linesep
        s += pp.pformat(self.funcStart__nodeId)+os.linesep
        s += 'funcName__list_nodeId'+os.linesep
        s += pp.pformat(self.funcName__list_nodeId)+os.linesep
        s += 'nodeId__entityType'+os.linesep
        s += pp.pformat(self.nodeId__entityType)+os.linesep
        s += 'nodeId__funcName'+os.linesep
        s += pp.pformat(self.nodeId__funcName)+os.linesep
        s += 'nodeId__funcStart'+os.linesep
        s += pp.pformat(self.nodeId__funcStart)+os.linesep
        s += 'nodeId__funcEnd'+os.linesep
        s += pp.pformat(self.nodeId__funcEnd)+os.linesep
        s += 'tuple_nodeId_argIdx__pNodeId'+os.linesep
        s += pp.pformat(self.tuple_nodeId_argIdx__pNodeId)
        #funcName, widthStart, widthEnd <<<for width-checking
        list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd = []
        for nodeId, widthStart in self.nodeId__widthStart.items():
            widthEnd = self.nodeId__widthEnd[nodeId]
            funcName = self.nodeId__funcName[nodeId]
            funcStart = self.nodeId__funcStart[nodeId]
            funcEnd = self.nodeId__funcEnd[nodeId]
            list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd.append((nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd))
        s += "list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd"+os.linesep
        s += pp.pformat(list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd)+os.linesep

        return s


    def _getNodeId(self):
        """
        NodeId Dispenser
        """
        oNodeId = copy(self.node_id)
        self.node_id += 1
        return oNodeId

    def _getEntityTemplate(self, nodeId, funcType, funcName, funcStart, funcEnd, widthStart=None, widthEnd=None):
        """
        Good for displaying...? Entities Iterator
        :param funcType:
        :type EntityType:
        """
        copy_template = deepcopy(self.entity_template)
        copy_template['nodeId'] = nodeId
        copy_template['funcType'] = funcType
        copy_template['funcName'] = funcName
        copy_template['funcStart'] = funcStart
        copy_template['funcEnd'] = funcEnd
        copy_template['widthStart'] = widthStart
        copy_template['widthEnd'] = widthEnd

    #not used, remove?
    def getAllNodeIds(self):
        return list(self.nodeId__funcStart.keys())


    def getParentAndArgId(self, nodeId):
        for (cNodeId, argIdx), pNodeId in self.tuple_nodeId_argIdx__pNodeId.items():
            if nodeId == cNodeId:
                return pNodeId, argIdx
        return None, None


    def getAllEntityBetween(self, openPos, closePos): 
        """element=(nodeId, funcName, entityType, funcStart, funcEnd, widthStart, widthEnd)"""
        allEntities = []
        allNodeIds = list(self.nodeId__funcStart.keys())
        for nodeId in allNodeIds:
            entityType = self.nodeId__entityType[nodeId]
            if entityType in [EntityType.IMPLICIT_INFIX, EntityType.PURE_INFIX]:#, EntityType.BACKSLASH_INFIX, EntityType.BACKSLASH_FUNCTION, EntityType.BACKSLASH_VARIABLE]:
                widthStart = self.nodeId__funcStart[nodeId]
                widthEnd = self.nodeId__funcEnd[nodeId]
            else:
                widthStart = self.nodeId__widthStart[nodeId]
                widthEnd = self.nodeId__widthEnd[nodeId]
            # print(openPos <= widthStart and widthEnd <= closePos, '!!!!!', nodeId, self.nodeId__funcName[nodeId], 'openPos <= widthStart', openPos <= widthStart, 'widthEnd <= closePos', widthEnd <= closePos)

            if openPos <= widthStart and widthEnd <= closePos:
                allEntities.append((nodeId, self.nodeId__funcName[nodeId], entityType, self.nodeId__funcStart[nodeId], self.nodeId__funcEnd[nodeId], self.nodeId__widthStart[nodeId], self.nodeId__widthEnd[nodeId]))
        return allEntities


class BracketStorage:
    """
    
        # GET CLOSEST OPENBRACKET OF A TYPE, TO THE RIGHT OF A POSITION <<<_find_backslash 'sREQUEST
        #  IS THERE A - RIGHT OF OPENBRACKETS? <<<_find_implicit_0 'sREQUEST
        #  GET ALL START END POSITION OF ALL BRACKETS <<<_find_implicit_multiply 'sREQUEST
        #  GET ALL BRACKETS CLOSEIMRIGHT|OPENIMLEFT|TIGHTESTENCLOSE of infix <<<_find_infixes_width 'sREQUEST
        #Design a datastructure, good for all the above.
        #give an id to each pair of bracket for easy removal (linking the open and close) <<< for enclosure_query too?
        #dict__close_right, key=bracket_type, value=close_bracket_position_list_ascending
        >>>>>>#dict__close_to_open, key=position_of_close_bracket, value=position_of_open_bracket
        #dict__open_left, key=bracket_type, value=open_bracket_position_list_ascending
        >>>>>>#dict__open_to_close, key=position_of_open_bracket, value=position_of_close_bracket
        #dict__id_openclosepos, key=id, value=tuple__openPos_closePos
        #dict__type_widthId, key=bracket_type, value=list__tuple__width_id
        #agis GET_ALL
    """



    def __init__(self):
        self.bracketId = 0
        self.closeBraType__sortedPosList = {}
        self.openBraType__sortedPosList = {}
        self.id__tuple_openPos_openBraType_closePos_closeBraType = {}
        self.list_tuple_width_id_openPos_closePos = []
        self.openBraPos__bracketId = {}
        self.closeBraPos__bracketId = {}
        self.endOfOpenBraPos = {}
        self.list_backslashBracketOpenPos = []
        self.allOpenPosOfBackslashArgsNoBrackets = []

    def _getBracketId(self):
        newBracketId = copy(self.bracketId)
        self.bracketId += 1
        return newBracketId
    
    def insertBracket(self, openBraType, openBraPos, closeBraType, closeBraPos):
        """
        EXAMPLES OF EACH INPUT
        openBraType:  (, {, [
        openBraPos: 3
        closeBraType: ), }, ]
        closeBraPos: 6


        return id


        we assume users DO NOT REPEATEDLY ADD SAME BRACKETS
        """
        bracketId = self._getBracketId()

        if openBraType not in self.openBraType__sortedPosList:
            self.openBraType__sortedPosList[openBraType] = []

        if closeBraType not in self.closeBraType__sortedPosList:
            self.closeBraType__sortedPosList[closeBraType] = []

        #binary search to find position to add
        insertPos = BinarySearch.binarySearchPre(
            self.list_tuple_width_id_openPos_closePos,
            #(closeBraPos - openBraPos, bracketId, openBraPos, closeBraPos),
            closeBraPos - openBraPos,
            key=lambda tuple_width_id: tuple_width_id[0] # sort by width ascending, getWidestEnclosingBra might depend on this
        )
        self.list_tuple_width_id_openPos_closePos.insert(insertPos, (closeBraPos - openBraPos, bracketId, openBraPos, closeBraPos))

        insertPos = BinarySearch.binarySearchPre(self.openBraType__sortedPosList[openBraType], openBraPos)
        self.openBraType__sortedPosList[openBraType].insert(insertPos, openBraPos)

        insertPos = BinarySearch.binarySearchPre(self.closeBraType__sortedPosList[closeBraType], closeBraPos)
        self.closeBraType__sortedPosList[closeBraType].insert(insertPos, closeBraPos)

        self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId] = (openBraPos, openBraType, closeBraPos, closeBraType)
        self.openBraPos__bracketId[openBraPos] = bracketId
        self.closeBraPos__bracketId[closeBraPos] = bracketId
        return bracketId

    # def tagAsBackslashBrackets(self, openPos):#self.bsbracketstorage as replacement
    #     self.list_backslashBracketOpenPos.append(openPos)

    # def isBackslashBracket(self, openPos):#self.bsbracketstorage as replacement
    #     return openPos in self.list_backslashBracketOpenPos


    def removeBracket(self, openBraPos):
        """
        """
        bracketId = self.openBraPos__bracketId[openBraPos]
        openBraPos, openBraType, closeBraPos, closeBraType = self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
        del self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]

        deletePos = BinarySearch.binarySearchPre(self.openBraType__sortedPosList[openBraType], openBraPos)
        del self.openBraType__sortedPosList[openBraType][deletePos]
        if len(self.openBraType__sortedPosList[openBraType]) == 0:
            del self.openBraType__sortedPosList[openBraType]

        deletePos = BinarySearch.binarySearchPre(self.closeBraType__sortedPosList[closeBraType], closeBraPos)
        del self.closeBraType__sortedPosList[closeBraType][deletePos]
        if len(self.closeBraType__sortedPosList[closeBraType]) == 0:
            del self.closeBraType__sortedPosList[closeBraType]

        self.list_tuple_width_id_openPos_closePos.remove((closeBraPos - openBraPos, bracketId, openBraPos, closeBraPos))

        del self.openBraPos__bracketId[openBraPos]
        del self.closeBraPos__bracketId[closeBraPos]

    def removeBracketsBetween(self, startPos, endPos):
        """
        """
        toRemove = []
        for bracketId, (openBraPos, _, closeBraPos, _) in self.id__tuple_openPos_openBraType_closePos_closeBraType.items():
            if startPos <= openBraPos and closeBraPos <= endPos:
                toRemove.append(openBraPos)
        for openBraPos in toRemove:
            self.removeBracket(openBraPos)


    def updateBracket(self, bracketId, openBraType, openBraPos, closeBraType, closeBraPos):
        oOpenBraPos, oOpenBraType, oCloseBraPos, oCloseBraType = self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
        del self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
        self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId] = (openBraPos, openBraType, closeBraPos, closeBraType)

        replaceIdx = self.closeBraType__sortedPosList[oCloseBraType].index(oCloseBraPos)
        self.closeBraType__sortedPosList[oCloseBraType][replaceIdx] = closeBraPos

        replaceIdx = self.openBraType__sortedPosList[oOpenBraType].index(oOpenBraPos)
        self.openBraType__sortedPosList[oOpenBraType][replaceIdx] = openBraPos

        replaceIdx = self.list_tuple_width_id_openPos_closePos.index((oCloseBraPos-oOpenBraPos, bracketId, oOpenBraPos, oCloseBraPos))
        self.list_tuple_width_id_openPos_closePos[replaceIdx] = (closeBraPos-openBraPos, bracketId, openBraPos, closeBraPos)

        del self.openBraPos__bracketId[oOpenBraPos]
        self.openBraPos__bracketId[openBraPos] = bracketId

        del self.closeBraPos__bracketId[oCloseBraPos]
        self.closeBraPos__bracketId[closeBraPos] = bracketId

    
    def getBraPosImmediateRightOfPos(self, pos, typeOfBracket, open):
        """
        open==True, means we are looking for openbracket, else we are looking for closebracket

        :param typeOfBracket: BracketType.ROUND, BracketType.SQUARE, BracketType.CURLY
        :type typeOfBracket: BracketType Enum
        """
        #get the right dict
        if open:
            theDict__sortedPosList = self.openBraType__sortedPosList
            typeOfBracket = typeOfBracket.value[0] # the open version of typeOfBracket
        else:
            theDict__sortedPosList = self.closeBraType__sortedPosList
            typeOfBracket = typeOfBracket.value[1] # the close version of typeOfBracket

        immediateRightIdx = BinarySearch.binarySearchPre(theDict__sortedPosList.get(typeOfBracket, []), pos) # always gives right_of_pos
        
        braPos = float('inf') # for getAllEnclosingBraOfPos, if there is no such thing
        if 0 <= immediateRightIdx and immediateRightIdx < len(theDict__sortedPosList.get(typeOfBracket, [])):
            braPos = theDict__sortedPosList[typeOfBracket][immediateRightIdx]
        return braPos
    
    def getBraPosImmediateLeftOfPos(self, pos, typeOfBracket, open):
        """

        open==True, means we are looking for openbracket, else we are looking for closebracket

        :param typeOfBracket: BracketType.ROUND, BracketType.SQUARE, BracketType.CURLY
        :type typeOfBracket: BracketType Enum
        """
        #get the right dict
        if open:
            theDict__sortedPosList = self.openBraType__sortedPosList
            typeOfBracket = typeOfBracket.value[0] # the open version of typeOfBracket
        else:
            theDict__sortedPosList = self.closeBraType__sortedPosList
            typeOfBracket = typeOfBracket.value[1] # the close version of typeOfBracket

        immediateRightIdx = BinarySearch.binarySearchPre(theDict__sortedPosList.get(typeOfBracket, []), pos) # always gives right_of_pos
        
        braPos = float('-inf') # for getAllEnclosingBraOfPos, if there is no such thing
        if 0 <= immediateRightIdx - 1 and immediateRightIdx - 1 < len(theDict__sortedPosList.get(typeOfBracket, [])):
            braPos = theDict__sortedPosList[typeOfBracket][immediateRightIdx - 1]
        return braPos

    def exists(self, bracketPos, typeOfBracket, open):
        """
        check if a bracket of type typeOfBracket, exists at position in equationStr, bracketPos

        :param typeOfBracket: BracketType.ROUND, BracketType.SQUARE, BracketType.CURLY
        :type typeOfBracket: BracketType Enum
        """
        # TODO can use this BinarySearch.binarySearchIdx(theDict__sortedPosList[typeOfBracket], pos)
        #get the right dict
        if open:
            theDict__sortedPosList = self.openBraType__sortedPosList
            typeOfBracket = typeOfBracket.value[0] # the open version of typeOfBracket
        else:
            theDict__sortedPosList = self.closeBraType__sortedPosList
            typeOfBracket = typeOfBracket.value[1] # the close version of typeOfBracket
        # import pdb;pdb.set_trace()
        return bracketPos in theDict__sortedPosList.get(typeOfBracket, [])

    def getCorrespondingCloseBraPos(self, openBraPos):
        if openBraPos not in self.openBraPos__bracketId:
            return None, None
        bracketId = self.openBraPos__bracketId[openBraPos]
        (_, _, closePos, closeBraType) = self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
        return closePos, closeBraType

    def getCorrespondingOpenBraPos(self, closeBraPos):
        if closeBraPos not in self.closeBraPos__bracketId:
            return None, None
        bracketId = self.closeBraPos__bracketId[closeBraPos]
        (openPos, openBraType, _, _) = self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
        return openPos, openBraType

    def getAllBracket(self):# make a AST_dependency diagram... (good place to learn)
        """
        return all the bracket in tuple (openBraType, openBraPos, closeBraType, closeBraPos)
        """
        return list(self.id__tuple_openPos_openBraType_closePos_closeBraType.values())
    
    def getAllTouchingBras(self, equationStr):
        """
        """
        touchingBrasPoss=[]
        for _, _, closeBraPos, closeBraType in self.getAllBracket():
            for openBraPos, openBraType, _, _ in self.getAllBracket():
                if closeBraPos < openBraPos:
                    startTouchingPos, endTouchingPos = closeBraPos+len(closeBraType), openBraPos
                    chasZweischen = equationStr[startTouchingPos:endTouchingPos]
                    if len(chasZweischen.strip()) == 0: #only whitespace between closeLeftBraket and openRightBraket, then they are touching
                        touchingBrasPoss.append((startTouchingPos, endTouchingPos))
        return touchingBrasPoss

    def getAllEnclosingBraOfPos(self, pos, typeOfBracket):
        filt__list_tuple_width_id_openPos_closePos = filter(lambda tuple_width_id_openPos_closePos:
            tuple_width_id_openPos_closePos[2]<pos and pos<=tuple_width_id_openPos_closePos[3]
            , self.list_tuple_width_id_openPos_closePos)
        return filt__list_tuple_width_id_openPos_closePos

    def getAllEnclosingTouchingBraOfPos(self, pos, widthStart, widthEnd, typeOfBracket):
        """
        There might be enclosingBra of pos p0 like so:

        (((p0))(p1))
        ^^^
        012

        In this case, we will only take 1 & 2. Although 0 also encloses p0, 0 also encloses p1, so we discard 0.

        This should solve the problem of users putting many same brackets around the same function|primitive


        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        one set of the brackets has to touch the original width

        :param typeOfBracket: BracketType.ROUND, BracketType.SQUARE, BracketType.CURLY
        :type typeOfBracket: BracketType Enum
        """
        list_tuple_width_id_openPos_closePos = list(self.getAllEnclosingBraOfPos(pos, typeOfBracket))
        #find the one that touches the original width
        #the pair with the largest openPos has to be the one touching original width, if not touching then non_of_brackets are touching
        #actually either side touching is FINE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        sortedByOpenPos = sorted(list_tuple_width_id_openPos_closePos, key=lambda tup: tup[2])
        sortedByClosePos = sorted(list_tuple_width_id_openPos_closePos, key=lambda tup: tup[3])
        """
        touching on both sides, else its not yours to claim. recheck: test__entityStorage__addConfirmedPCrelationship0
        """
        if (len(sortedByOpenPos) == 0 or (sortedByOpenPos[-1][2] + len(typeOfBracket.value[0]) != widthStart and sortedByOpenPos[-1][2] != widthStart)) or \
        (len(sortedByClosePos) == 0 or (sortedByClosePos[0][3] != widthEnd and sortedByClosePos[0][3] - len(typeOfBracket.value[1]) != widthEnd)):#need to minus (sortedByClosePos[0][3] - len(typeOfBracket.value[1]) != widthEnd)? check previous case, where i minused and then something went wrong....
            return []
        list_tuple_width_id_openPos_closePos__oC = [] # oC~openBraPos are Consecutive
        prevOpenBraPos = None
        for width, bracketId, openBraPos, closeBraPos in sorted(list_tuple_width_id_openPos_closePos, key=lambda tup: tup[2], reverse=True):#ascending by openBraPos
            _, openBraType, _, _ = self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
            if (prevOpenBraPos is None) or (openBraPos + len(openBraType) == prevOpenBraPos): # ensure openBraPos are consecutive
                list_tuple_width_id_openPos_closePos__oC.append((width, bracketId, openBraPos, closeBraPos))
                prevOpenBraPos = openBraPos
        list_tuple_width_id_openPos_closePos__oCcC = [] # cC~closeBraPos are Consecutive
        prevCloseBraPos = None
        for width, bracketId, openBraPos, closeBraPos in sorted(list_tuple_width_id_openPos_closePos__oC, key=lambda tup: tup[3]): #ascending by closeBraPos
            _, _, _, closeBraType = self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
            if (prevCloseBraPos is None) or (closeBraPos - len(closeBraType) == prevCloseBraPos): # ensure closeBraPos are consecutive
                list_tuple_width_id_openPos_closePos__oCcC.append((width, bracketId, openBraPos, closeBraPos))
                prevCloseBraPos = closeBraPos
        return list_tuple_width_id_openPos_closePos__oCcC


    def getTightestEnclosingPos(self, pos, typeOfBracket): #TODO is this ever used? make a AST_dependency diagram... (good place to learn)
        """

        return tightest bracket, that contains pos


        :param typeOfBracket: BracketType.ROUND, BracketType.SQUARE, BracketType.CURLY
        :type typeOfBracket: BracketType Enum
        """
        list_tuple_width_id_openPos_closePos = list(self.getAllEnclosingBraOfPos(pos, typeOfBracket))
        if len(list_tuple_width_id_openPos_closePos) > 0:
            minWidth, selectedOpenPos, selectedClosePos = float('inf'), None, None
            for width, bracketId, openPos, closePos in list_tuple_width_id_openPos_closePos:
                if width < minWidth:
                    minWidth, selectedOpenPos, selectedClosePos = width, openPos, closePos
            return selectedOpenPos, selectedClosePos

    def getWidestEnclosingBra(self, pos, typeOfBracket):
        """
        
        return tightest bracket, that contains pos

        :param typeOfBracket: BracketType.ROUND, BracketType.SQUARE, BracketType.CURLY
        :type typeOfBracket: BracketType Enum
        """
        list_tuple_width_id_openPos_closePos = list(self.getAllEnclosingBraOfPos(pos, typeOfBracket))#NOTE this is not consecutive
        if len(list_tuple_width_id_openPos_closePos) > 0:
            maxWidth, selectedOpenPos, selectedClosePos, selectedBracketId = float('-inf'), None, None, None
            for width, bracketId, openPos, closePos in self.list_tuple_width_id_openPos_closePos:
                if width > maxWidth:
                    maxWidth, selectedOpenPos, selectedClosePos, selectedBracketId = width, openPos, closePos, bracketId
            return selectedOpenPos, selectedClosePos, selectedBracketId

    def isABracketPos(self, pos):
        return pos in self.openBraPos__bracketId or pos in self.closeBraPos__bracketId

    def toTree(self, listOfOverallEqualPos, equationStr):#<<<<< this function has NO_NEED to be under BracketStorage
        """  
        Merely bracket accounting gives the level, every time we increment, we link that bracket to prev, this forms a tree

        recording the level will help us, go from the lowest to highest level

        We should not care about what kind of bracket?
        """
        def bracketAccounting(startPos, endPos):
            listOfPosition = []
            parent__listOfChildren = {} # returnable
            openPosition__closePosition = {} # returnable
            openPosition__level = {} #returnable
            openPosition__bracketLen = {} # returnable
            def handleOpenBracket(i):
                if len(listOfPosition) > 0: # has parent
                    parent = listOfPosition[-1] #peek
                else: # no parent
                    parent = None
                #add p|c relationship
                existing = parent__listOfChildren.get(parent, [])
                existing.append(i)
                parent__listOfChildren[parent] = existing
                #
                listOfPosition.append(i)
                #
                openPosition__level[i] = openPosition__level.get(parent, 0) + 1

            def handleCloseBracket(i):
                openPosition = listOfPosition.pop()
                openPosition__closePosition[openPosition] = i


            for i in range(startPos, endPos):
                # print('~~', startPos, endPos, listOfPosition, equationStr[i], equationStr[i] in BracketType.openBras())
                if equationStr[i] in BracketType.openBras() and self.isABracketPos(i):#its a OPEN_BRACKET, V_{BE} the brackets are removed, so BE is not an entity, when get allEntitiesBetween, return empty
                    handleOpenBracket(i)
                    openPosition__bracketLen[i] = 1
                elif equationStr[i] in BracketType.closeBras() and self.isABracketPos(i):#its a CLOSE_BRACKET, V_{BE} the brackets are removed, so BE is not an entity, when get allEntitiesBetween, return empty
                    handleCloseBracket(i)
                elif i in self.allOpenPosOfBackslashArgsNoBrackets:#they are of len=1, i is a OPEN_BRACKET AND CLOSE_BRACKET
                    handleOpenBracket(i)
                    openPosition__bracketLen[i] = 0
                    handleCloseBracket(i+1)# +1 is the len of the char
            return parent__listOfChildren, openPosition__closePosition, openPosition__level, openPosition__bracketLen


        """
        What about the backslash, whose arguments have no brackets? -----> use slot, <<<<<<<<<<<<<<<<<<<<<<<NOT! please remove slots, its useless TODO
        """


        #find the equation segments given by listOfOverallEqualPos, do bracketAccounting on each segment
        tuple_startPos_endPos__NAMES__fromBracketAccounting = {}
        for idx in range(0, len(listOfOverallEqualPos)-1):
            startPos, endPos = listOfOverallEqualPos[idx], listOfOverallEqualPos[idx+1]
            parent__listOfChildren, openPosition__closePosition, openPosition__level, openPosition__bracketLen = bracketAccounting(startPos, endPos+1) # include endPos
            #START add the TopLevel Parent that is startPos and endPos
            # print('add the TopLevel Parent that is startPos and endPos', startPos -1 if idx == 0 else startPos, endPos + 1 if idx == len(listOfOverallEqualPos)-2 else endPos)
            # import pdb;pdb.set_trace()
            new_parent__listOfChildren = {}
            for parent, listOfChildren in parent__listOfChildren.items():
                if parent is None:
                    parent = startPos -1 if idx == 0 else startPos
                new_parent__listOfChildren[parent] = listOfChildren
            new_parent__listOfChildren[None] = [startPos -1 if idx == 0 else startPos]

            parent__listOfChildren = new_parent__listOfChildren
            openPosition__closePosition[startPos -1 if idx == 0 else startPos]= endPos + 1 if idx == len(listOfOverallEqualPos)-2 else endPos
            openPosition__level[startPos -1 if idx == 0 else startPos] = 0
            openPosition__bracketLen[startPos -1 if idx == 0 else startPos] = 0
            #END add the TopLevel Parent that is startPos and endPos

            tuple_startPos_endPos__NAMES__fromBracketAccounting[(startPos, endPos)] = {
                'parent__listOfChildren':parent__listOfChildren,
                'openPosition__closePosition':openPosition__closePosition,
                'openPosition__level':openPosition__level,
                'openPosition__bracketLen':openPosition__bracketLen
            }
        # print('returning from toTree')
        # import pdb;pdb.set_trace()
        return tuple_startPos_endPos__NAMES__fromBracketAccounting




    def __str__(self):
        """
        print internal state of store

        #TODO prefix the internal states, and use self to find in a single loop
    closeBraType__sortedPosList = {}
    openBraType__sortedPosList = {}
    id__tuple_openPos_openBraType_closePos_closeBraType = {}
    list_tuple_width_id_openPos_closePos = []
    openBraPos__bracketId = {}
    closeBraPos__bracketId = {}

        """
        import os
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        s = 'closeBraType__sortedPosList' + os.linesep
        s+=pp.pformat(self.closeBraType__sortedPosList) + os.linesep
        s+='openBraType__sortedPosList' + os.linesep
        s+=pp.pformat(self.openBraType__sortedPosList) + os.linesep
        s+='id__tuple_openPos_openBraType_closePos_closeBraType' + os.linesep
        s+=pp.pformat(self.id__tuple_openPos_openBraType_closePos_closeBraType) + os.linesep
        s+='list_tuple_width_id_openPos_closePos' + os.linesep
        s+=pp.pformat(self.list_tuple_width_id_openPos_closePos) + os.linesep
        s+='openBraPos__bracketId' + os.linesep
        s+=pp.pformat(self.openBraPos__bracketId) + os.linesep
        s+='closeBraPos__bracketId' + os.linesep
        s+=pp.pformat(self.closeBraPos__bracketId) + os.linesep
        return s

