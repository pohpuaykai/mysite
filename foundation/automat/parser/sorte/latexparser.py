from copy import copy, deepcopy
from enum import Enum
import re

from foundation.automat.arithmetic.function import Function
from foundation.automat.common import BinarySearch, isNum, lenOrZero, EnclosureTree

class BracketType(Enum):
    ROUND = '(', ')'
    SQUARE = '[', ']'
    CURLY = '{', '}'

class EntityType(Enum):
    PURE_NUMBER = 'pure_number'
    IMPLICIT_INFIX = 'implicit_infix'
    PURE_VARIABLE = 'pure_variable'
    BACKSLASH_VARIABLE = 'backslash_variable'
    BACKSLASH_FUNCTION = 'backslash_function'
    BACKSLASH_NUMBER = 'backslash_number'
    PURE_INFIX = 'pure_infix'
    BACKSLASH_INFIX = 'backslash_infix'
    MATRIX = 'matrix'

class Latexparser(): # TODO follow the inheritance of _latexparser
    
    """
    
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
    
    
    BELOW is unit-testable, yay
    PLAN: (also need a LIST_OF_ALL_OCCUPIED for variable_finding[CONTIGUOUSleftovers])
    ~~NODES FINDING~~~ INCLUDE ITEM_ID for each 
    EXPECTED INPUTS FOR EACH TYPE (INFIX, BACKSLASH)
    0. remove ALL spacing from the Latex equation? (keep spacing_info to prompt user(FUTURE)) - a badcase: 222 actually means 2*2*2
        0a. find all \begin{}\end{} # these are MATRICES (note start_position and end_position) and bracket positions of START_END_TAG
        
    1. find position of all infixes (infixes might be multi character), note all the ^(exponent), DS:
        {
            name:'',
            start_position:[int], end_position = start_position+len(name)
            length: #length >0, since these are not implicit
            expected_inputs: #this will be a fixed dictionary. DO NOT PUT IT HERE
            inputs:  #there are inputs no enclosed by brackets, data type is list
            width:{start_position:[int], end_position:[int]} # initially empty
        }
        1a. occupied is only the symbol itself
    2. find position of all OTHER_brackets, first find all brackets
        2a. Keep position of all the brackets as a kind of datastorage
        2b. check if there is a ^(exponent), to their direct right or left (note in brackets) [tree_building]
            2b1.^ to the left (power) [only for ASTreeConstructionBODMAS, input of infix] (remove from OTHER_brackets)
            2b2.^ to the right (base) [also for implicit_multiply remove_from_OTHER_brackets_after_implicit_multiply]
        2c. DO NOT INCLUDE backslash brackets AND DO NOT INCLUDE MATRIX. (remove from OTHER_brackets)
        2d. check if left&right infixes (put to infix as inputs) (remove from OTHER_brackets)
    3. find start_position of all the backslashs (sqrt is special), EXCLUDE EXCLUDE_BACKSLASH like \to, because its an infix
        3a. their _(if any) and its immediateNextBracket, their ^(if any) and its immediateNextBracket and {} [tree_building]
        3b. remove all the ^ from infixes, that are actually backslash_exponents
        3c. note its end_position, also 
        3d. occupied is only the name and the backslash
        3e. note the WHOLE_end_position (different from 2d), these are BACKSLASH
        3f. BACKSLASHES always have at most 3 inputs
        3g. remove VARIABLENAMESTAKEANARG and put in variables
    4. find all leftover_positions(NOT infix|backslash|immediateNextBracket|NOT MATRICE), these are variable_fragments(may contain NESTED _{})
        4a. collate consecutive. (may contain alphanumeric and brackets(may have exponent within brackets) and underscore BUT NOT EXPONENT) example V_{BE^0}
            4a1.ONLY _{ are variable_subscripts. may have real brackets
                4a1a. find all _{ and their closure }, GROUP AS ONE, call this _{C
            4a2. N is a number, V is not number and not _{C, C is _{C
            4a3. scan from left to right, 
                4a4. if we go from N to V, break off. this means N is implicitly multiplied by V
                4a5. if we reach C, break off. This is the end of a independent variable
                4a6. else, keep collecting temp.
        
            4a4. These are VARIABLES|NUMBERS, also note start_position and length
        4b. remove these variable_brackets _{C from OTHER_brackets
    
    5. implicit_0 (-)(NOTHING_ELSE?) need to add to the list of all infixes, indicated by length 0. need starting_position
        5a. left of (nothing|open_brackets) , 
            5a1. nothing is the left_most of the equationStr
            5a2. search for open_brackets that have - (+ have no need of implicit_zero)
    ***OTHER_brackets should only contain right_input_for_^ OR enclosures_for_implicit_multiply OR ORDER_ENCLOSURES[which_op_comes_first, associativity, should_only_enclose_infixes_but_user_can_put_redundant_brackets] at_this_point
    6. implicit_multiply need to add to the list of all infixes, indicated by length 0. need starting_position
        6a. ALL_X_INF = MATRICES+BACKSLASH+VARIABLES+NUMBERS (EVERYTHING EXCEPT INFIX and OTHER_brackets??)
        6b. match the start_position and end_position of ALL_X_INF to each other, if they are immediateNext to each other, then add implicit multiply
        6c. right_input_for_^ OR enclosures_for_implicit_multiply from OTHER_brackets
    ***OTHER_brackets should only contain ORDER_ENCLOSURES[which_op_comes_first] at_this_point ?????????
    ***implicit_0 and implicit_multiply already has all its children [tree_building] at_this_point
    
    7. get width(start~end) of infixes
        7a. (by enclosing_brackets) or (by inputs) [tree_building]
        LOOK immediate LEFT&RIGHT of infix [tree_building] | but if immediate LEFT&RIGHT of infix are redundant_brackets? 
        then just update as width, and not as inputs
        7b. Check OTHER_brackets for enclosure that are wider than current_width_of_infix
        
    ***everything has width at_this_point
    ~~~ASTree construction~~~ by widest enclosing position? there is no need for brackets? 
    #process those_with_inputs(BACKSLASH&INFIX) by position (left to right)
    we only need to process: (MAYBE 2 list, like a bipartite_graph?, then iterate until (list_1 only has 1)|(list_2 is empty))
    1. those without parent but needs to have parents : EVERYTHING EXCEPT the top (usually =) MATRICES&INFIX&BACKSLASH&VARIABLE&NUMBERS
    2. those without children but need to have children : BACKSLASH & INFIXES
    
    pop list_2 -> a
    for each empty input of a ***********specify width for all the types
        for each item in list_1 ??????
            we want widest input that fits input_position_of_a break ties with PRIOIRITIZED_INFIX, and then from left_to_right
        remove selected_item from list_1
        
            
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

    '_{C}^{C}{C}': [#['sum', 'prod', 'int']
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




    '_{O}^{O}{C}': [#['partial', 'nabla', 'Delta']
                {'argId':0, 'preSym':'_', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':1, 'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':2, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
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
    '_{C}^{C}{C}': ['sum', 'prod', 'int'],
    '_{C}^{O}{C}': ['iint', 'iiint', 'oint', 'oiint'],
    '_{O}(C)': ['log'],
    '_{O}^{O}{C}': ['partial', 'nabla', 'Delta'],
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
        if funcName in ['sum', 'prod', 'int']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{C}^{C}{C}']
        if funcName in ['iint', 'iiint', 'oint', 'oiint']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{C}^{O}{C}']
        if funcName in ['log']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{O}(C)']
        if funcName in ['partial', 'nabla', 'Delta']:
            return self.BACKSLASH_EXPECTED_INPUTS['_{O}^{O}{C}']
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
    EXCLUDE_BACKSLASH_INFIX = ['to'] #because its an infix
    
    def __init__(self, equationStr=None, ast=None, verbose=False):
        self.equationStr = equationStr #processed rawEquationStr
        self.matrices_pos_type = None # replace with entitystorage, the collating of intervals (bubble merge) needs work
        self.allBrackets = None # all of the bracket STATIC, 
        self.openBraPos__bracketId = None # STATIC
        self.bracketstorage = BracketStorage()
        self.entitystorage = EntityStorage(eqStrLen=len(self.equationStr))
        self.mabracketstorage = BracketStorage()
        self.list_openTagPos = None
        self.list_closeTagPos = None
        self.openTagPos__closeTagPos = None
        self.closeTagPos__openTagPos = None
        self.occupiedPositions = []
        # self.all_brackets_pos = None
        self.all_preSym_pos = None
        self.latexAST = None
    

    # def _remove_all_spacing(self):
    #     self.equationStr = self.rawEquationStr.replace(" ", '')
    #     self.entitystorage = EntityStorage(eqStrLen=len(self.equationStr))
        
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


        tagName__openPosStack = {}
        for pos, isOpen, tagName, keepPos in sorted(list_tuple_pos_tagType, key=lambda tup: tup[0]): # if pos touch, then sort is bad
            openPosStack = tagName__openPosStack.get(tagName, [])
            if isOpen:
                openPosStack.append(keepPos)
            else:
                #found a matchingClose at pos
                openPos = openPosStack.pop()
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
                            'args':[]
                        }
                )
            tagName__openPosStack[tagName] = openPosStack


        #TODO this works like bubble_merge, if bubble_merge is not used anymore, please remove. Or replace this with bubble_merge. easier to analysis
        """
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
        self.mabracketstorageDefault = BracketType.ROUND
        self.mabracketstorageDefaultOpen = self.mabracketstorageDefault.value[0]
        self.mabracketstorageDefaultClose = self.mabracketstorageDefault.value[1]
        # self.mabracketstorage = BracketStorage()#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<move to EntityStorage TODO
        for openTagPos, closeTagPos in openTagPos__closeTagPos.items():
            self.mabracketstorage.insertBracket(self.mabracketstorageDefaultOpen, openTagPos, self.mabracketstorageDefaultClose, closeTagPos)


    def isPosInMatrixTag(self, pos):#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<move to EntityStorage TODO 

        """
        if there is matrix_tag enclosing pos, then pos is in a matrix_tag

        """

        return len(list(self.mabracketstorage.getAllEnclosingBraOfPos(pos, self.mabracketstorageDefault))) > 0


    def _find_infix(self):
        """
        Again, the same 3 ways as _find_matrices
        1. go character by character
        2. use re.findall <<<<<<<<<
        3. str.find, chop and str.find, and then match outer \\begin\\end
        
        """
        self.infixs_pos_type = []
        for infix in self.INFIX:
            infix_pos_type_list = list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"{re.escape(infix)}", self.equationStr)))
            
            for start, end, group in infix_pos_type_list:
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<might have gotten IMPLICIT_INFIX -
                self.entitystorage.insert(group, start, end, EntityType.PURE_INFIX, widthStart=start, widthEnd=end)

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
            self.endOfOpenBraPos.append(end)


        closeBracket_pos_type_list = []
        for closeBracket in closeBraTypes:
            for start, end, group in list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"\\{closeBracket}", self.equationStr))):
                closeBracket_pos_type_list.append((start, end, group))
                # self.all_brackets_pos.append(start)
        for start, end, closeBraType in closeBracket_pos_type_list:
            list_tuple_pos_braType_isOpen.append((start, closeBraType, False))
            self.endOfOpenBraPos.append(end)

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
            
        
        
        
        
        Again, the same 3 ways as _find_matrices
        1. go character by character
        2. use re.findall<<<<<<<<<
        3. str.find, chop and str.find, and then match outer \\begin\\end
        find the inputs to these backslash using _getExpectedBackslashInputs as template
        Exclude all the backslash_infix
        
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
                    EntityType.BACKSLASHVARIABLE, widthStart=funcStart, widthEnd=funcEnd, bracketstorage=self.bracketstorage)
            list_template = self._getExpectedBackslashInputs(funcName)
            if list_template is None: # number that starts with backslash. like \\pi
                
                self.bracketstorage=self.entitystorage.insert(funcName, funcStart, funcEnd, EntityType.BACKSLASH_NUMBER, 
                    widthStart=funcStart, widthEnd=funcEnd, bracketstorage=self.bracketstorage)
                continue # skip args finding
            #type == BACKSLASH_FUNCTION
            self.bracketstorage=self.entitystorage.insert(
                funcName, 
                funcStart, 
                funcEnd, 
                EntityType.BACKSLASH_FUNCTION, widthStart=funcStart, widthEnd=funcEnd, bracketstorage=self.bracketstorage)
            #backslash function at_this_point
            #search for immediateNextBracket inputs from m.start(), until m.end() 

            #BUT preSym could be in ANY ORDER
            """
            split inputTemplate as 2 stacks, compulsoryStack and optionalList (depends on 'optional')
            while the compulsoryStack is full, 
                inputTemplate = compulsoryStack.pop()
                if nextChar == preSym:
                    find_bracket_get_arg_store
                else:
                    for inputTemplate in optionalList:
                        gotArg = find_bracket_get_arg_store
                        if gotArg:
                            optionalList.remove(inputTemplate)
                            break
                set_nextChar
            for inputTemplate in optionalList:
                gotArg = find_bracket_get_arg_store
                if gotArg:
                    optionalList.remove(inputTemplate)
                    break
            -----------------------------------------------
            #find_bracket_get_arg_store

            if nextChar == inputTemplate['openBra']:
                #get corresponding closePos
                closeBraPos, closeBraType = self.bracketStorage.getCorrespondingCloseBraPos(nextCharPos)
                #TAKEARG as everything between nextCharPos+len(nextChar) and closeBraPos, store
                #NOTE bracket position if any, store
                nextCharPos = closeBraPos + len(closeBraType)
                nextChar = equation[nextCharPos] #<<<<<<<<<<<<<<<<<<<<<<<<<<<
                self.bracketstorage.removeBracket(openBraPos)#<<<<< do no do that
                if inputTemplate['preSym'] in ['^']: # controlSymbols mixing with mathSymbols
                    self.infixs_pos_type.remove((m.start(), m.end(), m.group()))
            elif inputTemplate['braOptional'] == 'False':
                raise Exception #here is !gotArg
            elif inputTemplate['braOptional'] == 'argLen<2':
                #TAKEARG as nextCharPos+1, store
                #NOTE NO_BRACKETS, store
                nextCharPos += 1
                nextChar = equation[nextCharPos] #<<<<<<<<<<<<<<<<<<<<<<<<<<<
                self.bracketstorage.removeBracket(openBraPos)#<<<<< do no do that
                if inputTemplate['preSym'] in ['^']: # controlSymbols mixing with mathSymbols
                    self.infixs_pos_type.remove((m.start(), m.end(), m.group()))
            else:
                raise Exception('Unhandled') #here is !gotArg
            return gotArg, nextCharPos, nextChar
            """

            compulsoryStack0, compulsoryStack1, optionalList0, optionalList1, everyOtherPreSym = [], [], [], [], []
            for template in list_template:
                if template['optional']:
                    optionalList0.insert(0, template) # to keep the order in the list_template
                else:
                    compulsoryStack0.insert(0, template) # to keep the order in the list_template
                #hasBlankPreSym, everyOtherPreSym
                if template['preSym'] != '':
                    everyOtherPreSym.append(template['preSym'])
            #could empty everyOtherPreSym, if not hasBlankPreSym

            ##
            def findBracketGetArgStore(funcStart, funcEnd, funcName, template, nextChar, nextCharPos, everyOtherPreSym):
                closeBraPos, closeBraType = None, None
                #This is for _find_variable_or_number
                if nextChar in set_all_possible_preSym:
                    self.all_preSym_pos.append(nextCharPos)
                #

                nextCharPos += len(template['preSym'])
                nextChar = self.equationStr[nextCharPos]

                if (template['preSym']=='' and self.equationStr[nextCharPos] not in everyOtherPreSym and self.equationStr[nextCharPos] == template['openBra']) or\
                (self.equationStr[nextCharPos] == template['openBra']): # found bracket,
                    gotArg = True
                    #get corresponding closePos
                    closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(nextCharPos)
                    self.bracketstorage.tagAsBackslashBrackets(nextCharPos)
                    self.entitystorage.addUnConfirmedPCrelationship(funcStart, template['argId'], self.equationStr[nextCharPos], nextCharPos, closeBraType, closeBraPos)
                    #for backslash, we can update width here, not necessary for infix
                    self.entitystorage.widthMaxUpdate(funcStart, None, closeBraPos+len(closeBraType))
                    # self.bracketstorage.removeBracket(nextCharPos)

                    #TAKEARG as everything between nextCharPos+len(nextChar) and closeBraPos, store
                    #NOTE bracket position if any, store
                    # nextChar = self.equationStr[nextCharPos]
                    if template['preSym'] in ['^']: # controlSymbols mixing with mathSymbols
                        """

            2b. check if there is a ^(exponent), to their direct right or left (note in brackets) [tree_building]
                2b1.^ to the left (power) [only for ASTreeConstructionBODMAS, input of infix] (remove from OTHER_brackets)
                2b2.^ to the right (base) [also for implicit_multiply remove_from_OTHER_brackets_after_implicit_multiply]

                        """
                        #remove from self.infixs_pos_type # TODO binarySearch, this is not very efficient, ENTITIES STORAGE.
                        posOfPreSym = nextCharPos - len(template['openBra'])
                        self.entitystorage.remove(posOfPreSym)
                    nextCharPos = closeBraPos
                elif template['braOptional'] == 'False': # no bracket but not neccessary
                    #log
                    gotArg = False #raise Exception #here is !gotArg
                elif template['braOptional'] == 'argLen<2': #no bracket, args of length 1 needed
                    #TAKEARG as nextCharPos+1, store
                    #NOTE NO_BRACKETS, store
                    gotArg = True
                    self.entitystorage.addUnConfirmedPCrelationship(funcStart, template['argId'], None, nextCharPos, None, nextCharPos+1)#TODO test this branch<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    self.entitystorage.widthMaxUpdate(funcStart, None, closeBraPos)
                    if template['preSym'] in ['^']: # controlSymbols mixing with mathSymbols
                        #remove from self.infixs_pos_type # TODO binarySearch, this is not very efficient
                        posOfPreSym = nextCharPos - len(template['openBra'])
                        self.entitystorage.remove(posOfPreSym)
                else:
                    #log
                    gotArg = False#raise Exception('Unhandled') #here is !gotArg
                    if foundType in ['backslash_function', 'backslash_variable']:
                        raise Exception()
                return gotArg, nextCharPos, closeBraPos, closeBraType


            def processOptionalList(funcStart, funcEnd, funcName, eOptionalList, template, nextChar, nextCharPos, everyOtherPreSym):
                gotArg, closeBraPos, closeBraType = False, len(self.equationStr), None#if eOptionalList is empty
                self.entitystorage.addUnConfirmedPCrelationship(funcStart, template['argId'], self.equationStr[nextCharPos], nextCharPos, closeBraType, closeBraPos - len(closeBraType) if closeBraType is not None else None)
                for template in eOptionalList:
                    gotArg, nextCharPos, closeBraPos, closeBraType = findBracketGetArgStore(funcStart, funcEnd, funcName, template, nextChar, nextCharPos, everyOtherPreSym)
                    if gotArg:
                        eOptionalList.remove(template)
                        break
                return eOptionalList, gotArg, nextCharPos, closeBraPos, closeBraType
            ##
            nextCharPos = funcEnd
            nextChar = self.equationStr[nextCharPos]
            while len(compulsoryStack0) > 0 or len(compulsoryStack1) > 0:
                rStack = compulsoryStack0 if len(compulsoryStack0) >0 else compulsoryStack1
                oStack = compulsoryStack1 if len(compulsoryStack0) >0 else compulsoryStack0
                while len(rStack) > 0:
                    template = rStack.pop()
                    gotArg, nextCharPos0, closeBraPos0, closeBraType0 = findBracketGetArgStore(funcStart, funcEnd, funcName, template, nextChar, nextCharPos, everyOtherPreSym)
                    nextChar = self.equationStr[nextCharPos0]
                    if gotArg:
                    #jump to next char
                        nextCharPos, nextChar, closeBraPos, closeBraType = nextCharPos0+len(closeBraType0), self.equationStr[nextCharPos], closeBraPos0, closeBraType0
                    else:
                        oStack.insert(0, template) # to keep the order in the list_template
                    #update compulsoryStack0 and compulsoryStack1
                compulsoryStack0, compulsoryStack1 = oStack, rStack
                orStack = optionalList0 if len(optionalList0) >0 else optionalList1
                ooStack = optionalList1 if len(optionalList0) >0 else optionalList0
                while len(orStack) > 0:
                    template = orStack.pop()
                    optionalList, gotArg, nextCharPos0, closeBraPos0, closeBraType0 = processOptionalList(funcStart, funcEnd, funcName, optionalList, template, nextChar, nextCharPos, everyOtherPreSym)
                    nextChar = self.equationStr[nextCharPos0]
                    if gotArg:
                    #jump to next char
                        nextCharPos, nextChar, closeBraPos, closeBraType = nextCharPos0+len(closeBraType0), self.equationStr[nextCharPos], closeBraPos0, closeBraType0
                    else:
                        ooStack.insert(0, template) # to keep the order in the list_template
                optionalList0, optionalList1 = orStack, ooStack

                    #update optionalList0 and optionalList1



        
    def _find_variables_or_numbers(self):
        """ RELIES on the spacing on the equationStr, please do not remove spacing from the equationStr
**** WHAT IF we take out everything that has been found so far AND all of the brackets.
**** when we get all the variables(without _{}) and numbers,
**** and then we put the _{} back to the variables that are supposed to have _{}

    4. From equationStr, take out everything we found so far and all the brackets.
        4a. LeftOverPositions=A\
            4a1.everything_between_ALL_matrixTags
            4a1.infix(nameonly)
            4a2.backslash(name&preSymonlyNOargs) & backslash_variables
            4a3.ALL BRACKETS
        4b. scan from left to right,  [N is a number, V is not number]
            4b1. if (we go from N to V) and (not consecutive), break off, collect collected_variables. this means N is implicitly multiplied by V
            4b2. else, keep collecting temp.
        4c. go through all collected_variables
            4c1. immediateRight, lookFor _{ , make them part of the variable.
            4c2. remove variable_brackets _{, from OTHER_brackets

        4d. These are VARIABLES|NUMBERS, also note start_position and length

        """
        #collate infix|backslash|matrices pos {infix_brackets are not removed, will be a problem if infix_brackets are curly}
        #backslash_brackets ONLY
        #matrices pos THE WHOLE MATRIX, not just the tags

        infixName_occupied = []
        for nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd in self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX):
            for pos in range(funcStart, funcEnd):
                infixName_occupied.append(pos)
        infixName_occupied = sorted(infixName_occupied)

        backslashName_occupied = []
        for nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd in self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.BACKSLASH_VARIABLE):
            for pos in range(widthStart, widthEnd):
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
            pos in self.all_preSym_pos:
                continue # we skip these
            leftOverPosList.append(pos)

        accumulator, accumulatorStartPos, accumulatorEndPos, accumulatorType, prevLeftOverPos= None, None, None, None, None
        for leftOverPos in leftOverPosList:
            leftOverChar = self.equationStr[leftOverPos]
            # isNume = isNum(leftOverChar)
            if accumulatorType is None:
                accumulator = leftOverChar
                accumulatorStartPos = leftOverPos
                accumulatorEndPos = accumulatorStartPos + len(leftOverChar) # len(leftOverChar) should always = 1
                accumulatorType = 'N' if isNum(leftOverChar) else 'V' # this is prevIsNume
                prevLeftOverPos = leftOverPos
            elif (accumulatorType == 'N' and not isNum(leftOverChar)) or \
            (prevLeftOverPos + 1 != leftOverPos) or (re.match(r'\s', leftOverChar)): #break off conditions: 0. going_from_N_to_V. 1. not_consecutive (excluding space)2. is whitespace
                accumulator = re.sub(r'\s', '', accumulator)
                if isNum(accumulator): # pure_number
                    self.bracketstorage=self.entitystorage.insert(
                    accumulator, accumulatorStartPos, accumulatorEndPos, EntityType.PURE_NUMBER, 
                    widthStart=accumulatorStartPos, widthEnd=accumulatorEndPos, bracketstorage=self.bracketstorage)#fixed width
                else: # pure variable (just not a backslash variable, can still have _{}, just need to widthMaxUpdate if we find _{})
                    self.bracketstorage=self.entitystorage.insert(
                    accumulator, accumulatorStartPos, accumulatorEndPos, EntityType.PURE_VARIABLE, 
                    widthStart=accumulatorStartPos, widthEnd=accumulatorEndPos, bracketstorage=self.bracketstorage) #width waiting for _{} later
                #reset
                accumulator = leftOverChar
                accumulatorStartPos = leftOverPos
                accumulatorEndPos = accumulatorStartPos + len(leftOverChar)
                accumulatorType = 'N' if isNum(leftOverChar) else 'V'
                prevLeftOverPos = leftOverPos
            else: # keep accumulating
                accumulator += leftOverChar
                accumulatorEndPos += len(leftOverChar)
                accumulatorType = 'N' if isNum(leftOverChar) else 'V'
                prevLeftOverPos = leftOverPos
                #startPos same. accumulatorType V->N or pure V or pure N is fine.
        #last collection
        if len(accumulator) > 0:
            accumulator = re.sub(r'\s', '', accumulator)
            if isNum(accumulator): # pure_number
                self.bracketstorage=self.entitystorage.insert(
                accumulator, accumulatorStartPos, accumulatorEndPos, EntityType.PURE_NUMBER, 
                widthStart=accumulatorStartPos, widthEnd=accumulatorEndPos, bracketstorage=self.bracketstorage)#fixed width
            else: # pure variable (just not a backslash variable, can still have _{}, just need to widthMaxUpdate if we find _{})
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
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<this is messing up the width of e
        #TODO this method is very similar to find_backslash args. REFACTOR? or use import ast to refactor (good training)
        # for funcStart, funcEnd, nodeId in self.entitystorage.getAllEndPosOfEntityType(EntityType.PURE_VARIABLE):
        for nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd in self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_VARIABLE):
            nextPos = funcEnd
            closeBraPos = None
            removeCaret__pos, removeCaretBra__pos = None, None
            if self.entitystorage.existEntityAt('^', nextPos): # get the exponential immediate after funcEnd <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                openBraPos = self.bracketstorage.getBraPosImmediateRightOfPos(nextPos+len('^'), BracketType.CURLY, True)
                removeCaret__pos = nextPos#
                if 0 <= openBraPos and openBraPos < len(self.equationStr):
                    closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(openBraPos)
                #remove from other brackets
                    removeCaretBra__pos = openBraPos#
                    nextPos = closeBraPos
                else: # a single character
                    nextPos += len('^')
                #check if there is _ after the arg1 of the exponential immediate after funcEnd
                if self.equationStr[nextPos] == '_':
                    if removeCaret__pos:#remove FAKE EXPONENTIAL
                        self.entitystorage.remove(removeCaret__pos)#remove ^ only if its continued with _
                    if removeCaretBra__pos:
                        self.bracketstorage.remove(removeCaretBra__pos) #only if its continued with _
            #################
                    openBraPos = self.bracketstorage.getBraPosImmediateRightOfPos(nextPos, BracketType.CURLY, True)
                    if 0 <= openBraPos and openBraPos < len(self.equationStr): #TODO these seemed to be used together very often... condense into a method?????????????
                        closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(openBraPos)
                    #remove from other brackets
                        self.bracketstorage.remove(openBraPos)
                    else: #a single character
                        closeBraPos = nextPos + 1

                    #UPDATE width, if we found _ or ^_
                    if closeBraPos:
                        self.entitystorage.widthMaxUpdate(funcStart, None, closeBraPos)
                        #update enclosing_touching brackets
                        self.bracketstorage = self.entitystorage._EntityStorage__updateTemplatesToWiderEnclosingBracketsAndRemove(
                            #takes nodeId
                            list(map(lambda t: t[0], self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_VARIABLE))), #has to be done here, since we need to check for superscript_pure_variableS
                            # self.entitystorage.getAllEndPosOfEntityType(EntityType.PURE_VARIABLE), #has to be done here, since we need to check for superscript_pure_variableS
                            bracketstorage=self.bracketstorage)




    def _find_implicit_0(self):
        """

    5. implicit_0 (-)(NOTHING_ELSE?) need to add to the list of all infixes, indicated by length 0. need starting_position
        5a. left of (nothing|open_brackets) , 
            5a1. nothing is the left_most of the equationStr
            5a2. search for open_brackets that have - (+ have no need of implicit_zero), to their right
            5a3. any infix that have -, to their right

        """
        def addImplictMinus(funcPos):

            #check if we already inserted this as PURE_INFIX ( should be yes)
            pNodeId = self.entitystorage.updateIfExists(funcPos, entityType=EntityType.IMPLICIT_INFIX) # returns None with no throw, if not exist.

            self.bracketstorage = self.entitystorage.insert(# insert 0 with parentNodeId
                '0', funcPos, funcPos, EntityType.PURE_NUMBER, 
                parentNodeId=pNodeId, argIdx=0, widthStart=funcPos, widthEnd=funcPos, bracketstorage=self.bracketstorage)

        affected = ['-']
        #5a1
        if self.equationStr[0] in affected:
            addImplictMinus(0)
        #all openbrackets except Matrices, no need bracketstorage
        #5a2
        for openBraPos in self.endOfOpenBraPos:
            if self.isPosInMatrixTag(openBraPos) or openBraPos >= len(self.equationStr):# or self.isPosInMatrixTag(closeBraPos):
                continue
            if self.equationStr[openBraPos] in affected: #if openBraPos, is the end of the bracket DO NOT +1
                addImplictMinus(openBraPos)
        #5a3
        for nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd in self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX, EntityType.BACKSLASH_INFIX):
            if self.equationStr[funcEnd] in affected:
                addImplictMinus(funcEnd)




    def _find_infixes_arg_brackets_width(self):

        #
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
        for nodeId, funcName, widthStart, widthEnd, funcStart, funcEnd in sorted(self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX), key=lambda t: t[4]): # by funcStart
            """
            that is direct right of 
            """

            # print('nodeId', nodeId, ' funcName', funcName)
            """priority: entity; touching side bracket; enclosing bracket"""

            all_openBracket_type = list(map(lambda t: t.value[0], BracketType))
            all_closeBracket_type = list(map(lambda t: t.value[1], BracketType))
            #right
            if self.equationStr[funcEnd] in all_openBracket_type:
                closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(funcEnd)
                self.entitystorage.addUnConfirmedPCrelationship(funcStart, 1, self.equationStr[funcEnd], funcEnd, closeBraType, closeBraPos)
                # self.bracketstorage.removeBracket(openBraPos) # it is really ok to remove brackets at all?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                self.entitystorage.widthMaxUpdateById(nodeId, widthStart, closeBraPos)#right=End
            else:# i did not check for IMMDIATE RIGHT????? what if there are things between?
                cNodeId = self.entitystorage.getEntityImmediateRightOfPos(funcEnd) # need to remove implicit <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                cWidthEnd = self.entitystorage.nodeId__widthEnd.get(cNodeId)#WHAT IF THERE IS NO WIDTH, because cNodeId is a infix, thats not processed yet?
                self.entitystorage.widthMaxUpdateById(nodeId, widthStart, cWidthEnd)#right=End



            all_closeBracket_type = list(map(lambda t: t.value[1], BracketType))
            if self.equationStr[funcStart-1] in all_closeBracket_type:
                # print('foundBracket');import pdb;pdb.set_trace()
                openBraPos, openBraType = self.bracketstorage.getCorrespondingOpenBraPos(funcStart-1)
                self.entitystorage.addUnConfirmedPCrelationship(funcStart, 0, openBraType, openBraPos, self.equationStr[funcStart-1], funcStart-1)
                # self.bracketstorage.removeBracket(closeBraPos)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                self.entitystorage.widthMaxUpdateById(nodeId, openBraPos, widthEnd)#left=Start
            else:#cannot add confirmedRelationship, because implicit multiply not in yet, implicit multiply depends on width
                cNodeId = self.entitystorage.getEntityImmediateLeftOfPos(funcStart)
                cWidthStart = self.entitystorage.nodeId__widthStart.get(cNodeId)
                # print('foundEntity', self.entitystorage.nodeId__funcStart[cNodeId], self.entitystorage.nodeId__funcName[cNodeId]);import pdb;pdb.set_trace()
                self.entitystorage.widthMaxUpdateById(nodeId, cWidthStart, widthEnd)#left=Start





    def _update_all_width_by_enclosing_brackets_width_remove(self):
        #remove all the user stupid multiple enclosing brackets
        #CHECK wider enclosing brackets, for EVERYTHING 
        self.bracketstorage = self.entitystorage._EntityStorage__updateTemplatesToWiderEnclosingBracketsAndRemove(
            list(self.entitystorage.nodeId__funcStart.keys()), #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<UPDATES should be done by EntityType, and then from left to right????
            bracketstorage=self.bracketstorage)

        
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
        list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd = sorted(self.entitystorage.getAllNodeIdFuncNameWidthStartWidthEnd(), key=lambda t:t[4])
        # print('sorted: ', list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd);import pdb;pdb.set_trace()

        for idx in range(0, len(list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd)-1):
            vorDing = list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd[idx]
            hinDing = list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd[idx+1]
            vorDingEntityType = self.entitystorage.nodeId__entityType[vorDing[0]]
            hinDingEntityType = self.entitystorage.nodeId__entityType[hinDing[0]]
            # print(idx,'GOT:', vorDing, hinDing);import pdb;pdb.set_trace()
            #START_CONDITIONAL
            ##### REMOVE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            ##### REMOVE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if (vorDingEntityType in [EntityType.BACKSLASH_INFIX, EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX]) or (hinDingEntityType in [EntityType.BACKSLASH_INFIX, EntityType.PURE_INFIX, EntityType.IMPLICIT_INFIX]):
                continue
            #END_CONDITIONAL
            # print('checkConsec', vorDing[3]+1, hinDing[2], '$$$$$$$$$$$$$$')
            if (vorDing[3] +1 == hinDing[2])\
             or (vorDing[3] == hinDing[2]): #3=widthEnd & 2=widthStart
                # print('addmul:', vorDing, hinDing, '*********************')
                pNodeId = self.entitystorage.insert('*', vorDing[3]+1, hinDing[2], EntityType.IMPLICIT_INFIX, 
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
                """
                self.entitystorage.addUnConfirmedPCrelationshipById(pNodeId, 0, None, vorDing[2], None, vorDing[3])
                self.entitystorage.addUnConfirmedPCrelationshipById(pNodeId, 1, None, hinDing[2], None, hinDing[3])

    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<what is in self.bracketstorage at_this_point?????

        
    def _match_child_to_parent_input(self):
        """
    ***everything has width at_this_point EXCEPT INFIXES
    ~~~ASTree construction~~~ by widest enclosing position? there is no need for brackets? 
    #process those_with_inputs(BACKSLASH&INFIX) by position (left to right)
    we only need to process: (MAYBE 2 list, like a bipartite_graph?, then iterate until (list_1 only has 1)|(list_2 is empty))
    1. those without parent but needs to have parents : EVERYTHING EXCEPT the top (usually =) MATRICES&INFIX&BACKSLASH&VARIABLE&NUMBERS
    2. those without children but need to have children : BACKSLASH & INFIXES  <<<<<<<<start from the SLOTs with smallest width
    (ALL of the BACKSLASH_FUNCTIONS) and (some of the args of INFIXES) will have SLOT like 
{
                        'nodeId':self.getNodeId(),
                                'funcType':'infix',
                                'funcName':m.group(),
                                'funcStart':m.start(),
                                'funcEnd':m.end(),
                        'widthStart':,
                        'widthEnd':,
                                'args':[
{
        'nodeId':None, <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<SLOT
                'argIdx':inputTemplate['argIdx'],
                'openBra':nextChar,# <<<<<<<<<<<<<<<if noBra arglen=1, store as None
                'openBraPos':nextCharPos, 
                'closeBra':closeBraType,
                'closeBraPos': closeBraPos
            }
                                ]
                    }
    
    pop list_2 -> a
    for each empty input of a ***********specify width for all the types
        for each item in list_1 ??????
            we want widest input that fits input_position_of_a break ties with PRIOIRITIZED_INFIX, and then from left_to_right
        remove selected_item from list_1
        

PSEUDOCODE:



        """
        #TODO did you move UNConfirmed to Confirmed?
        list_tuple_openSlotPos_closeSlotPos = []
        for (pNodeId, cArgIdx), (openBra, openSlotPos, closeBra, closeSlotPos) in self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos.items():
            list_tuple_openSlotPos_closeSlotPos.append((openBraPos, closeBraPos))
        def firstContainsSecond(b0, b1):
            return b0[0] <= b1[0] and b1[1] <= b0[1]
        def getId(braTuple):
            return list_tuple_openSlotPos_closeSlotPos.index(braTuple)
        roots, leaves, enclosureTree, levelToIDs, idToLevel = EnclosureTree.makeEnclosureTreeWithLevelRootLeaves(
            list_tuple_openSlotPos_closeSlotPos, firstContainsSecond, getId)


        for level, list_slotId in sorted(levelToIDs.items(), key=lambda tup: tup[0], reverse=True):#bigger number is smaller
            tuple_openSlotPos_closeSlotPos__tuple_funcName_funcId_funcStart_funcEnd = {} # clear this for this new level
            for slotId in list_slotId:
                openSlotPos, closeSlotPos = list_tuple_openSlotPos_closeSlotPos[slotId]


                list_tuple_nodeId_funcName_funcStart_funcEnd = self.entitystorage.getAllEntityIdWithinFuncStartAndFuncEnd(openBraPos, closeBraPos)
                for nodeId, funcName, funcStart, funcEnd in list_tuple_nodeId_funcName_funcStart_funcEnd:
                    new_list_tuple_nodeId_funcName_funcStart_funcEnd = []
                    #START easier to read if this is a function by itself
                    removableEntities, subNodeId, subFuncName = [], None, None
                    for (oldOpenSlotPos, oldCloseSlotPos), (foldedFuncName, foldedNodeId, foldedFuncStart, foldedFuncEnd) in tuple_openSlotPos_closeSlotPos__tuple_funcName_funcId_funcStart_funcEnd.items():

                        #look for (funcStart, funcEnd) <= EACH tuple_openSlotPos_closeSlotPos__tuple_funcName_funcId
                        if oldOpenSlotPos <= funcStart and funcEnd <= oldCloseSlotPos:
                            removableEntities.append((oldOpenSlotPos, oldCloseSlotPos, foldedFuncName, foldedNodeId, foldedFuncStart, foldedFuncEnd))
                            subNodeId, subFuncName = foldedNodeId, foldedFuncName
                    #END easier to read if this a function by itself
                    #if found substitute away 
                    for (oldOpenSlotPos, oldCloseSlotPos, foldedFuncName, foldedNodeId, foldedFuncStart, foldedFuncEnd) in removableEntities:
                        if oldOpenSlotPos <= funcStart and funcEnd <= oldCloseSlotPos:
                            newlist_tuple_nodeId_funcName_funcStart_funcEnd.append((foldedNodeId, foldedFuncName, foldedFuncStart, foldedFuncEnd))
                        else:
                            newlist_tuple_nodeId_funcName_funcStart_funcEnd.append((nodeId, funcName, funcStart, funcEnd))
                
                #removed subtitutables from previous levels
            nodeId__priority = {}
            stack = sorted(newlist_tuple_nodeId_funcName_funcStart_funcEnd, key=lambda tup:self.getPriority(tup[1], defaultDict=nodeId__priority))
            while len(stack) > 0:
                (pNodeId, pFuncName, pFuncStart, pFuncEnd) = stack.pop()
                #fold
                #get Unconfirmed Pos of entity (SLOTs)
                list_tuple_openSlotPos_closeSlotPos_argIdx = self.entitystorage.getAllUnConfirmedPCrelationship(pNodeId)

                for openSlotPos, closeSlotPos, argIdx in list_tuple_openSlotPos_closeSlotPos_argIdx:
                    cNodeId, cFuncName, cFuncStart, cFuncEnd = self.entitystorage.getWidestFit(openSlotPos, closeSlotPos) 

                    tuple_openSlotPos_closeSlotPos_argIdx__tuple_funcName_funcId_funcStart_funcEnd[(openSlotPos, closeSlotPos, argIdx)] = (cNodeId, cFuncName, cFuncStart, cFuncEnd)#put folded in this level for next level to use
                    #set ChosenPriority
                    nodeId__priority[pNodeId] = float('inf') # so that unused
                    #add Confirmed relationsip
                    self.entitystorage.addConfirmedPCrelationshipById(pNodeId, cNodeId, argIdx)








        # #do are the brackets nested in each other ==> EnclosureTree
        # list_tuple_openBraPos_closeBraPos = list(map(lambda tup: (tup[0], tup[2]), self.bracketstorage.id__tuple_openPos_openBraType_closePos_closeBraType.values()))
        # def firstContainsSecond(b0, b1):
        #     return b0[0] <= b1[0] and b1[1] <= b0[1]
        # def getId(braTuple):
        #     return self.bracketstorage.openBraPos__bracketId[braTuple[0]]
        # roots, leaves, enclosureTree, levelToIDs, idToLevel = EnclosureTree.makeEnclosureTreeWithLevelRootLeaves(list_tuple_openBraPos_closeBraPos, firstContainsSecond, getId)

        # bracketId__list_rmArgTup = {}#
        # for level, list_bracketId in sorted(levelToIDs.items(), key=lambda tup: tup[0], reverse=True):
        #     for bracketId in list_bracketId:
        #         openBraPos, _, closeBraPos, _ = self.bracketstorage.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
        #         list_tuple_nodeId_funcName_funcStart_funcEnd = self.entitystorage.getAllEntityIdWithinFuncStartAndFuncEnd(openBraPos, closeBraPos)

        #         #when removing using bracketId__list_rm_ArgTup, we should DFS downward and remove those as well
        #         enclosureTreeStack = enclosureTree[bracketId]
        #         while len(enclosureTreeStack) > 0:
        #             eBracketId = enclosureTreeStack.pop()
        #             for rmArgTup in bracketId__list_rmArgTup.get(eBracketId, []):#only remove those that are linked in enclosureTree? See notepad !@#0
        #                 list_tuple_nodeId_funcName_funcStart_funcEnd.remove(rmArgTup)
        #             for cBracketId in enclosureTree[eBracketId]:
        #                 enclosureTreeStack.append(cBracketId)





        #         #find the args that needs to be removed
        #         # list_enclosureBracketId=enclosureTree[bracketId]#list of eBracketId that are in bracketId
        #         # for eBracketId in list_enclosureBracketId:
        #         #     print('going to remove: ', bracketId__list_rmArgTup, '(bracketId__list_rmArgTup)');print('from: ', list_tuple_nodeId_funcName_funcStart_funcEnd);import pdb;pdb.set_trace()
        #         #     for rmArgTup in bracketId__list_rmArgTup.get(eBracketId, []):#only remove those that are linked in enclosureTree? See notepad !@#0
        #         #         list_tuple_nodeId_funcName_funcStart_funcEnd.remove(rmArgTup)
        #         #END:find the args that needs to be removed



        #         #get priorities
        #         list_tuple_nodeId_funcName_funcStart_funcEnd = sorted(list_tuple_nodeId_funcName_funcStart_funcEnd, key=lambda tup: tup[2]+tup[3])
        #         nodeId__priority = {}
        #         for nodeId, funcName, funcStart, funcEnd in list_tuple_nodeId_funcName_funcStart_funcEnd:
        #             nodeId__priority[nodeId] = self.getPriority(funcName)
        #         #END:get priorities
        #         #still need to update bracketId__list_rmArgTup if len(list_tuple_nodeId_funcName_funcStart_funcEnd) == 1
        #         if len(list_tuple_nodeId_funcName_funcStart_funcEnd) == 1:
        #             existing_list = bracketId__list_rmArgTup.get(bracketId, [])
        #             existing_list.append(list_tuple_nodeId_funcName_funcStart_funcEnd[0])
        #             bracketId__list_rmArgTup[bracketId] = existing_list
        #         #match p|c
        #         while len(list_tuple_nodeId_funcName_funcStart_funcEnd) > 1:
        #             #find lowest priority
        #             lowestPriority, lpNodeId, lpFuncName, lpFuncStart, lpFuncEnd = float('inf'), None, None, None, None
        #             for nodeId, funcName, funcStart, funcEnd in list_tuple_nodeId_funcName_funcStart_funcEnd:
        #                 #find lowest priority # DEAL WITH frac and /!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #                 if nodeId__priority[nodeId] < lowestPriority:
        #                     lowestPriority = nodeId__priority[nodeId]
        #                     lpNodeId, lpFuncName, lpFuncStart, lpFuncEnd = nodeId, funcName, funcStart, funcEnd
        #             #END find lowest priority
        #             #get Unconfirmed Pos of entity (SLOTs)
        #             list_tuple_openBraPos_closeBraPos_argIdx = self.entitystorage.getAllUnConfirmedPCrelationship(lpNodeId)
        #             #make confirmed ...arg #GEt the widest width
        #             argPrioritySum = 0
        #             rmlist_tuple_nodeId_funcName_funcStart_funcEnd = []
        #             for argOpenBraPos, argCloseBraPos, argIdx in list_tuple_openBraPos_closeBraPos_argIdx:
        #                 cNodeId, cFuncName, cFuncStart, cFuncEnd = self.entitystorage.getWidestFit(argOpenBraPos, argCloseBraPos)
        #                 #<<<<<<<<<<<<<<<<<<<<<<<<<<<one of the UNCONFIRMED nodeId==58 openBraPos was removed in this statement?????
        #                 self.bracketstorage = self.entitystorage.addConfirmedPCrelationshipById(lpNodeId, cNodeId, argIdx, bracketstorage=self.bracketstorage) #TODO does this update the ONLY the width of the parent, lpNodeId????
        #                 #remove ...arg from list_tuple_nodeId_funcName_funcStart_funcEnd
        #                 ctuple_nodeId_funcName_funcStart_funcEnd = (cNodeId, cFuncName, cFuncStart, cFuncEnd)

        #                 try:
        #                     list_tuple_nodeId_funcName_funcStart_funcEnd.remove(ctuple_nodeId_funcName_funcStart_funcEnd)
        #                 except:#the ctuple might not be there, since they are removed when bracketId__list_rmArgTup
        #                     pass
        #                 #REMOVE lpNodeId tooo?

        #                 #add ... arg to bracketId__rmArgTup[bracketId]
        #                 existing_list = bracketId__list_rmArgTup.get(bracketId, [])
        #                 existing_list+=list_tuple_nodeId_funcName_funcStart_funcEnd
        #                 bracketId__list_rmArgTup[bracketId] = existing_list
        #                 argPrioritySum += self.getPriority(cFuncName)#argPrioritySum += nodeId__priority[cNodeId]

        #             #add to nodeId__priority, so it doesn't get picked again??????
        #             nodeId__priority[lpNodeId] += argPrioritySum


        
    def _format_to_pyStyledAST(self):
        """
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
        """
        pass
        
    def _get_statistics(self):
        """

    ~~~Get statistics~~~
    1. totalNodeCount
    2. functions count
    3. primitives count
    4. variables count
        """
        pass


    def _parse(self):
        #TODO Pool multiprocessing with method priorities (Chodai!) -- dependency ha chain desu yo, sou shitara, motto hayaku arimasu ka? import ast; find variable_dependency_network between methods
        return self.ast, self.functions, self.variables, self.primitives, self.totalNodeCount, self.startPos__nodeId

#####################################################

    def _unparse(self): # TODO from AST to LaTeX string... 
        return self._recursiveUnparse(self.equalTuple)


    def _recursiveUnparse(self, keyTuple):
        pass

class EntityStorage:
    """
    Entity is a node that is found in the equationStr, might or might not, have all its args (might not have widthStart, widthEnd)

    This acts like a database for Entities, allowing CRUD

    WHAT ARE THE QUERIES? THIS WILL DETERMINE THE UNDERLYING DATASTRUCTURE.
    Q3:StatisticalCounts
    """


    def __init__(self, eqStrLen):
        self.eqStrLen = eqStrLen
        self.node_id = 0
        self.entity_template = {
            'nodeId':None,
            'funcType':None,
            'funcName':None,
            'funcStart':None,
            'funcEnd':None,
            'widthStart':None,
            'widthEnd':None,
            'args':[]
        }
        self.arg_template = {
            'nodeId':None,
            'funcName':None,
            'argIdx':None,
            # 'openBra':None,
            # 'openBraPos':None,
            # 'closeBra':None,
            # 'closeBraPos': None
        }

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<needs to be tagged with nodeId.. or your algo, doesn't work.
        self.list_tuple_widthStart_nodeId = [] # for BS, OR it can hold tuples. with nodeId, and then nodeId to everything else., find widthStart instead of id
        self.list_tuple_widthEnd_nodeId = [] # for BS


        self.nodeId__widthStart = {}
        self.nodeId__widthEnd = {}
        self.entityType__list_nodeId = {}
        self.funcStart__nodeId = {}
        # self.funcName__nodeId = {} #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<a lot of nodeIds
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
            # import pdb;pdb.set_trace()
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


    def widthMaxUpdate(self, funcStart, widthStart, widthEnd): #update to max(current, width), if None, then do not update
        nodeId = self.funcStart__nodeId[funcStart]
        self.widthMaxUpdateById(nodeId, widthStart, widthEnd)


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

    def getWidestFit(self, openBraPos, closeBraPos):# get widest nodeId that still between (openBraPos, closeBraPos)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        list_nodeIdContaining = self.getAllContainingByWidth(openBraPos, closeBraPos)
        # print('open', openBraPos, 'close', closeBraPos, 'gWF list_nodeIdContaining: ', list_nodeIdContaining);import pdb;pdb.set_trace()
        maxWidth, maxNodeId, maxFuncName = float('-inf'), None, None
        for nodeId in list_nodeIdContaining:
            width = self.nodeId__widthEnd[nodeId] - self.nodeId__widthStart[nodeId]
            if width > maxWidth:
                maxWidth = width; maxNodeId = nodeId; maxFuncName = self.nodeId__funcName[nodeId]
        return maxNodeId, maxFuncName, self.nodeId__funcStart[maxNodeId], self.nodeId__funcEnd[maxNodeId]

    def __updateTemplatesToWiderEnclosingBracketsAndRemove(self, nodeIds, bracketstorage): 
        for nodeId in nodeIds:
            widthStart = self.nodeId__widthStart[nodeId]
            #because we exclude the front_backslash_character that we removed so that touching matches
            entityType = self.nodeId__entityType[nodeId]
            widthEnd = self.nodeId__widthEnd[nodeId]
            allEnclosingTouchingBra = bracketstorage.getAllEnclosingTouchingBraOfPos(self.nodeId__funcStart[nodeId], widthStart, widthEnd, BracketType.ROUND)
            if len(allEnclosingTouchingBra) > 0:
                widestWidth = 0
                widestBra = None
                for width, bracketId, openBraPos, closeBraPos in allEnclosingTouchingBra:
                    if width > widestWidth:
                        widestWidth = width
                        widestBra = (width, bracketId, openBraPos, closeBraPos)
                    # bracketstorage.removeBracket(openBraPos) # because this bracket cannot contain anything else
                self.updateWidth(nodeId, widestBra[2], widestBra[3])
        return bracketstorage
        #

    def getAllContainingByWidth(self, startPos, endPos):#all the entities within startPos and endPos, 
        startWidthIdx = BinarySearch.binarySearchPre(self.list_tuple_widthStart_nodeId, startPos, key=lambda t:t[0])
        endWidthIdx = BinarySearch.binarySearchPre(self.list_tuple_widthEnd_nodeId, endPos, key=lambda t:t[0], breakTie='r')#breakTie give right most, there might be multiple same endWidth of implicit add implicit mul
        # print('s', startPos, 'e', endPos, '!!!!!!!getAllContainingByWidth:', self.list_tuple_widthStart_nodeId, '&&&&&&&&&&&',self.list_tuple_widthEnd_nodeId)
        # import pdb;pdb.set_trace()
        set_containingNodeIdByStartWidth = set(map(lambda t:t[1], self.list_tuple_widthStart_nodeId[startWidthIdx:]))#verysimiliar0refactor?ONLYdifferIn:PositionTODO
        set_containingNodeIdByEndWidth = set(map(lambda t:t[1], self.list_tuple_widthEnd_nodeId[:endWidthIdx+1]))#verysimiliar0refactor?ONLYdifferIn:PositionTODO
        #off by 1 revealed by test__entityStorage__getWidestFit0
        list_nodeId = list(set_containingNodeIdByStartWidth.intersection(set_containingNodeIdByEndWidth))
        return list_nodeId


    def getAllNodeIdFuncNameWidthStartWidthEnd(self, *entityTypes):
        if len(entityTypes) == 0:
            entityTypes = list(EntityType.__members__.values())
        list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd = []
        for entityType in entityTypes:
            for nodeId in self.entityType__list_nodeId.get(entityType, []):
                list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd.append((
                    nodeId, self.nodeId__funcName[nodeId], self.nodeId__widthStart[nodeId], self.nodeId__widthEnd[nodeId], self.nodeId__funcStart[nodeId], self.nodeId__funcEnd[nodeId]
                ))
        return list_tuple_nodeId_funcName_widthStart_widthEnd_funcStart_funcEnd

    def getEntityImmediateLeftOfPos(self, pos):
        idx = BinarySearch.binarySearchPre(self.list_tuple_widthEnd_nodeId, pos, key=lambda t:t[0])
        nodeId = self.list_tuple_widthEnd_nodeId[idx][1]#[idx-1][1]
        # import pdb;pdb.set_trace()
        return nodeId

    def getEntityImmediateRightOfPos(self, pos):
        idx = BinarySearch.binarySearchPre(self.list_tuple_widthStart_nodeId, pos, key=lambda t:t[0])
        nodeId = self.list_tuple_widthStart_nodeId[idx][1]
        return nodeId

    def remove(self, funcStart):
        """This is used by _find_backslash, TODO unit_test
        """
        nodeId = self.funcStart__nodeId[funcStart]
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
            if nodeId0 == nodeId or pNodeid == nodeId:
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


    def updateWidth(self, nodeId, widthStart, widthEnd):
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



    def updateIfExists(self, funcPos, entityType=None):#TODO include other possible updates to the fields
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
        #TODO log to tell the user 

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

        s = 'list_tuple_widthStart_nodeId'+os.linesep
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
        s += pp.pformat(self.tuple_nodeId_argIdx__pNodeId)+os.linesep
        s += 'tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos'+os.linesep
        s += pp.pformat(self.tuple_nodeId_cArgIdx__tuple_openBra_openBraPos_closeBra_closeBraPos)+os.linesep

        #funcName, widthStart, widthEnd <<<for width-checking
        list_tuple_funcName_widthStart_widthEnd = []
        for nodeId, widthStart in self.nodeId__widthStart.items():
            widthEnd = self.nodeId__widthEnd[nodeId]
            funcName = self.nodeId__funcName[nodeId]
            funcStart = self.nodeId__funcStart[nodeId]
            funcEnd = self.nodeId__funcEnd[nodeId]
            list_tuple_funcName_widthStart_widthEnd.append((funcName, widthStart, widthEnd, funcStart, funcEnd))

        s += pp.pformat(list_tuple_funcName_widthStart_widthEnd)+os.linesep

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


    def _getArgTemplate(self):
        pass


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

    def tagAsBackslashBrackets(self, openPos):
        self.list_backslashBracketOpenPos.append(openPos)

    def isBackslashBracket(self, openPos):
        return openPos in self.list_backslashBracketOpenPos
        
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

        return bracketPos in theDict__sortedPosList[typeOfBracket]

    def getCorrespondingCloseBraPos(self, openBraPos):
        bracketId = self.openBraPos__bracketId[openBraPos]
        (_, _, closePos, closeBraType) = self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
        return closePos, closeBraType

    def getCorrespondingOpenBraPos(self, closeBraPos):
        bracketId = self.closeBraPos__bracketId[closeBraPos]
        (openPos, openBraType, _, _) = self.id__tuple_openPos_openBraType_closePos_closeBraType[bracketId]
        return openPos, openBraType

    def getAllBracket(self):# make a AST_dependency diagram... (good place to learn)
        """
        return all the bracket in tuple (openBraType, openBraPos, closeBraType, closeBraPos)
        """
        return list(self.id__tuple_openPos_openBraType_closePos_closeBraType.values())
    
    def getAllEnclosingBraOfPos(self, pos, typeOfBracket):
        """
        Find 
        closest_close_left_of_pos :
        closest_open_right_of_pos :
         in id__tuple_openPos_openBraType_closePos_closeBraType
         remove all tuple__closePos<=closest_close_left_of_pos
         remove all tuple__openPos>=closest_open_right_of_pos
        if empty, there is no enclosing brackets for pos

        else
            get all the remaining id, find smallest_width in list_tuple_width_id 
        

        :param typeOfBracket: BracketType.ROUND, BracketType.SQUARE, BracketType.CURLY
        :type typeOfBracket: BracketType Enum
        """

        nearest_close_left_of_pos = self.getBraPosImmediateLeftOfPos(pos, typeOfBracket, False) #no such thing...-inf
        nearest_open_right_of_pos = self.getBraPosImmediateRightOfPos(pos, typeOfBracket, True) #no such thing...inf
        filt__list_tuple_width_id_openPos_closePos = filter(
            lambda tuple_width_id_openPos_closePos: 
                nearest_close_left_of_pos<tuple_width_id_openPos_closePos[3] and \
                tuple_width_id_openPos_closePos[2]<nearest_open_right_of_pos, 
            self.list_tuple_width_id_openPos_closePos)
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
        filt__list_tuple_width_id_openPos_closePos = self.getAllEnclosingBraOfPos(pos, typeOfBracket)
        if len(filt__list_tuple_width_id_openPos_closePos) > 0:
            minWidth, selectedOpenPos, selectedClosePos = float('inf'), None, None
            for width, bracketId, openPos, closePos in self.list_tuple_width_id_openPos_closePos:
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