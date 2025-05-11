from copy import copy
from enum import Enum

from foundation.automat.arithmetic.function import Function
from foundation.automat.common import BinarySearch, isNum

class BracketType(Enum):
    ROUND = '(', ')'
    SQUARE = '[', ']'
    CURLY = '{', '}'

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
    BACKSLASH_INFIX = ['\\times', '\\cdot','\\%','\\to']#vectors op prioritised over backslash
    PRIOIRITIZED_INFIX = [ '^', '/','//', '*', '-', '+']#['^', '/', '*', '-', '+'] 
    INFIX = ['=']+BACKSLASH_INFIX+PRIOIRITIZED_INFIX #the smaller the number the higher the priority
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
    BACKSLASH_EXPECTED_INPUTS = { #all possible returns according to input_type, for easy collating
        '^{}()':[
                {'argId':0, 'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'argLen<2'}, #exponential
                {'argId':1, 'preSym':'', 'optional':False, 'openBra':'(', 'closeBra':')', 'braOptional':'False'} # angle
        ],
        '()':[
                {'argId':0, 'preSym':'', 'optional':False, 'openBra':'(', 'closeBra':')', 'braOptional':'False'}
        ],
        '_{}()':[
                {'argId':0, 'preSym':'_', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'argLen<2'},
                {'argId':1, 'preSym':'', 'optional':False, 'openBra':'(', 'closeBra':')', 'braOptional':'False'}
        ],
        '{}{}':[
                {'argId':0, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':1, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
        ],
        '[]{}':[
                {'argId':0, 'preSym':'', 'optional':True, 'openBra':'[', 'closeBra':']', 'braOptional':'False'},
                {'argId':1, 'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
        ],
        '_{}^{}{}':[
                {'argId':0, 'preSym':'_', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':1, 'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'argId':2, 'preSym':'', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
            ],
        '{}': [
                {'argId':0, 'preSym':'', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
        ]
    }#argId is for ASTree building
    
    def _getExpectedBackslashInputs(funcName):
        """
        
        preSym is the prefix for the input. 
        optional is if the preSym is necessary (TODO convert to enum? ENUM)
        openBra is the opening_delimiter of input
        closeBra is the closing_delimiter of input
        braOptional is if the openBra and closeBra are optional. (TODO convert to enum? ENUM) 
        
        """
        if funcName in TRIGOFUNCTION: 
            #input_type: ^{}()
            return BACKSLASH_EXPECTED_INPUTS['^{}()']
        if funcName in ['ln', 'det']:  #det is determinant
            #input_type: ()
            return BACKSLASH_EXPECTED_INPUTS['()']
        if funcName in ['log', 'lim']:
            #input_type: _{}()
            return BACKSLASH_EXPECTED_INPUTS['_{}()']
        if funcName in ['frac']:
            #input_type: {}{}
            return BACKSLASH_EXPECTED_INPUTS['{}{}']
        if funcName in ['sqrt']:
            #input_type: []{}
            return BACKSLASH_EXPECTED_INPUTS['[]{}']
        if funcName in ['sum', 'prod', 'partial', 'nabla', 'Delta', 'int', 'iint', 'iiint', 'oint', 'oiint']:
            #input_type: _{}^{}{}
            return BACKSLASH_EXPECTED_INPUTS['_{}^{}{}']
        if funcName in VARIABLENAMESTAKEANARG:
            #input_type: {}
            return BACKSLASH_EXPECTED_INPUTS['{}']
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
    EXCLUDE_BACKSLASH = ['\\to']
    
    def __init__(self, equationStr=None, ast=None, verbose=False):
        self.rawEquationStr = equationStr
        self.equationStr = None #processed rawEquationStr
        self.matrices_pos_type = None
        self.infixs_pos_type = None
        self.variables_pos_type = None
        self.number_pos_type = None #decimal numbers like 123, 23.2, -3.4, also contain symbolic number like \\pi, i
        self.node_id = 0
        self.allBrackets = None # all of the bracket STATIC, 
        self.openBraPos__bracketId = None # STATIC
        self.bracketstorage = BracketStorage()
        self.list_openTagPos = None
        self.list_closeTagPos = None
        self.openTagPos__closeTagPos = None
        self.closeTagPos__openTagPos = None
        self.occupiedPositions = []
        self.backslashNames = None # this is for taking out occupied pos
        self.latexAST = None
    
    def getNodeId(self):
        """
        NodeId Dispenser
        """
        oNodeId = copy(self.node_id)
        self.node_id += 1
        return oNodeId

    def _remove_all_spacing(self):
        self.equationStr = self.rawEquationStr.replace(" ", '')
        
    def _find_matrices(self):
        """
        
        I can only think of 3 ways to do this? Implement one first, and then later do both, and parallelise
        1. go character by character
        2. use re.findall, match outer \\begin\\end <<<<<<<<<< we going with this
        3. str.find, chop and str.find, and then match outer \\begin\\end
        
        """
        self.matrices_pos_type = []
        import re
        matrixStartTags = list(map(lambda m: 
            (m.start(), m.end(), m.group()), 
            re.finditer(r"\\begin\{\wmatrix\}", self.equationStr))) # the help page guarantees sorted, right to left, might be better to sort
        matrixEndTags = list(map(lambda m: 
            (m.start(), m.end(), m.group()), 
            re.finditer(r"\\end\{\wmatrix\}", self.equationStr))) # the help page guarantees sorted, right to left, might be better to sort
        #self.matrices_pos_type = list(zip(matrixStartTags, reversed(matrixEndTags)))
        for (startTagStartPos, startTagEndPos, startTag), (endTagStartPos, endTagEndPos, endTag) in zip(matrixStartTags, reversed(matrixEndTags)):
            self.matrices_pos_type.append(
                    {
                        'nodeId':self.getNodeId(),
                        'funcType':'matrix',
                        'funcName':startTag,
                        'funcStart':startTagStartPos,
                        'funcEnd':endTagEndPos,
                        'widthStart':startTagStartPos,
                        'widthEnd':endTagEndPos,
                                'args':[]
                    }
            )
        """
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<also change the unit test
        """


        #TODO this works like bubble_merge, if bubble_merge is not used anymore, please remove. Or replace this with bubble_merge. easier to analysis
        """
        ~~PREPARING FOR MATRIX CONTAINMENT QUERY~~  __isPosInMatrixTag

        split into list_openTagPos, list_closeTagPos
        openTagPos__closeTagPos
        closeTagPos__openTagPos

        Add new newTag = (openTagPos, closeTagPos)
        if len(list_openTagPos) == 0:
            add to both list_openTagPos and list_closeTagPos
        else:
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
            # for (_, startTagEndPos, _), (endTagStartPos, _, _) in self.matrices_pos_type: #should have been startTagStartPos and endTagEndPos
            for template in self.matrices_pos_type:
                startTagStartPos, endTagEndPos = self.matrices_pos_type['widthStart'], self.matrices_pos_type['widthEnd']
                insertIdx = BinarySearch.binarySearchApp(list_openTagPos, startTagStartPos)
                list_openTagPos.insert(insertIdx, startTagStartPos)

                insertIdx = BinarySearch.binarySearchApp(list_closeTagPos, endTagEndPos)
                list_closeTagPos.insert(insertIdx, endTagEndPos)

                openTag_closeTagPos[startTagStartPos] = endTagEndPos
                closeTag_openTagPos[endTagEndPos] = startTagStartPos

                set__openTagPos = set(filter(lambda i: i<closeInOpenIdx, list_openTagPos))
                set__closeTagPos = set(filter(lambda i: openInCloseIdx<i, list_closeTagPos))

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
                    insertIdx = BinarySearch.binarySearchApp(list_openTagPos, startTagStartPos)
                    list_openTagPos.insert(insertIdx, startTagStartPos)

                    #BSADD closeTagPos to list_closeTagPos
                    #TODO replace with BinarySearch.binarySearchIdx(l, findMe, approximate=True)
                    insertIdx = BinarySearch.binarySearchApp(list_closeTagPos, endTagEndPos)
                    list_closeTagPos.insert(insertIdx, endTagEndPos)

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
                        insertIdx = BinarySearch.binarySearchApp(list_openTagPos, startTagStartPos)
                        list_openTagPos.insert(insertIdx, startTagStartPos)

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
                        insertIdx = BinarySearch.binarySearchPre(list_closeTagPos, endTagEndPos)
                        list_closeTagPos.insert(insertIdx, endTagEndPos)

                        added = True


                self.list_openMatrixTagPos, self.list_closeMatrixTagPos, self.openMatrixTagPos__closeMatrixTagPos, self.closeMatrixTagPos__openMatrixTagPos = \
                list_openTagPos, list_closeTagPos, openTagPos__closeTagPos, closeTagPos__openTagPos

        #collate all the matrix_start_end_tag, like bubblemerge, then we get many non-overlapping intervals
        #collate all non-overlaping intervals, to removed for leftover-finding
        
    def __isPosInMatrixTag(self, pos):

        """
        copied from bracketstorage: getTightestEnclosingPos

        Find 
        closest_close_left_of_pos :
        closest_open_right_of_pos :
         in id__tuple_openPos_openBraType_closePos_closeBraType
         remove all tuple__closePos<=closest_close_left_of_pos
         remove all tuple__openPos>=closest_open_right_of_pos
        if empty, there is no enclosing brackets for pos
        """
        #TODO replace with BinarySearch.binarySearchIdx(l, findMe, approximate=True)
        nearest_close_left_of_pos = BinarySearch.binarySearchPre(self.list_closeMatrixTagPos, pos) # always gives right_of_pos

        nearest_open_right_of_pos = BinarySearch.binarySearchPre(self.list_openMatrixTagPos, pos) - 1

        filt__list_tuple_openPos_closePos = filter(lambda tup: nearest_close_left_of_pos<tup[1] and tup[0]<nearest_open_right_of_pos, self.openMatrixTagPos__closeMatrixTagPos.items())
        
        if len(filt__list_tuple_openPos_closePos) > 0:
            for openPos, closePos in filt__list_tuple_openPos_closePos:
                if openPos <= pos and pos <= closePos:
                    return True
        return False


    def _find_infix(self):
        """
        Again, the same 3 ways as _find_matrices
        1. go character by character
        2. use re.findall <<<<<<<<<
        3. str.find, chop and str.find, and then match outer \\begin\\end
        
        """
        import re
        self.infixs_pos_type = []
        for infix in self.INFIX:
            infix_pos_type_list = list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"{infix}", self.equationStr)))
            
            for start, end, group in infix_pos_type_list:
                self.infixs_pos_type.append(
{
                        'nodeId':self.getNodeId(),
                        'funcType':'infix',
                        'funcName':group,
                        'funcStart':start,
                        'funcEnd':end,
                        'widthStart':None,#<<<<<<<<<<<<<<<<<<<<<<<<<UNKNOWN for now, since we do not know the args
                        'widthEnd':None,#<<<<<<<<<<<<<<<<<<<<<<<<<UNKNOWN for now, since we do not know the args
                        'args':[
{
        'nodeId':None,#just a SLOT
        'funcName':None,
                'argIdx':0,
                'openBra':None,
                'openBraPos':None, 
                'closeBra':None,
                'closeBraPos': None
},
{
        'nodeId':None,#just a SLOT
        'funcName':None,
                'argIdx':1,
                'openBra':None,
                'openBraPos':None, 
                'closeBra':None,
                'closeBraPos': None
}
                                ]
                    }
                )
        
    def _find_brackets(self):
        """
        
        2a. Keep position of all the brackets as a kind of datastorage, need to get all the 
        DO NOT INCLUDE MATRIX. (remove from OTHER_brackets)

        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<2d obsolete
        2d. check if left&right infixes (put to infix as inputs) (remove from OTHER_brackets)
        """
        #collate all the matrix_start_end_tag, like bubblemerge, then we get many non-overlapping intervals
        bracketStorage = {}
        brackets = set()
        for k, templateList in BACKSLASH_EXPECTED_INPUTS.items():
            for template in templateList:
                brackets.add((template['openBra'], template['closeBra']))
        self.allBrackets = []
        self.openBraPos__bracketId = {}
        for openBracket, closeBracket in brackets: # order in which we process the brackets does not matter
            openBracket_pos_type_list = list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"\\{openBracket}", self.equationStr))) # the help page guarantees sorted, right to left, might be better to sort
            closeBracket_pos_type_list = list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"\\{closeBracket}", self.equationStr))) # the help page guarantees sorted, right to left, might be better to sort
            #TODO remove redundant information
            matchedBrackets = list(zip(openBracket_pos_type_list, reversed(closeBracket_pos_type_list)))
            self.allBrackets += matchedBrackets
            for (_, openBraPos, openBraType), (closeBraPos, _, closeBraType) in matchedBrackets:
                #check if its between matrix_start_end_tag,
                if self.__isPosInMatrixTag(openBraPos) or self.__isPosInMatrixTag(closeBraPos):
                    continue
                #else, store
                self.bracketstorage.insertBracket(openBraType, openBraPos, closeBraType, closeBraPos)
        
        
        
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
        import re
        self.backslashNames = [] # this is for taking out occupied pos
        self.backslash_pos_type = []
        self.variables_pos_type = []
        self.number_pos_type = [] #symbolic number like \\pi, i
        for m in re.finditer(r"\\([a-zA-z]+)", self.equationStr):
            foundType = 'backslash_function'
            storeTemplate = {
                'nodeId':self.getNodeId(),
                'funcType':foundType,
                'funcName':m.group(),
                'funcStart':m.start(),
                'funcEnd':m.end(),
                'widthStart':m.start(),
                'widthEnd': m.end(),
                'args':[]
            }
            self.backslashNames.append((m.start(), m.end(), m.group()))
            if m.group() in BACKSLASH_INFIX: # remove the backslash_infix from backslash
                continue
            if m.group() in VARIABLENAMESTAKEANARG: # variable_function is actually a variable
                foundType = 'backslash_variable'
                storeTemplate['funcType'] = foundType
            inputTemplates = _getExpectedBackslashInputs(m.group())
            if inputTemplates is None: # number that starts with backslash. like \\pi
                foundType = 'backslash_number'
                storeTemplate['funcType'] = foundType
                self.number_pos_type.append(storeTemplate)
                continue # skip args finding
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
                self.bracketstorage.removeBracket(openBraPos)
                if inputTemplate['preSym'] in ['^']: # controlSymbols mixing with mathSymbols
                    self.infixs_pos_type.remove((m.start(), m.end(), m.group()))
            elif inputTemplate['braOptional'] == 'False':
                raise Exception #here is !gotArg
            elif inputTemplate['braOptional'] == 'argLen<2':
                #TAKEARG as nextCharPos+1, store
                #NOTE NO_BRACKETS, store
                nextCharPos += 1
                nextChar = equation[nextCharPos] #<<<<<<<<<<<<<<<<<<<<<<<<<<<
                self.bracketstorage.removeBracket(openBraPos)
                if inputTemplate['preSym'] in ['^']: # controlSymbols mixing with mathSymbols
                    self.infixs_pos_type.remove((m.start(), m.end(), m.group()))
            else:
                raise Exception('Unhandled') #here is !gotArg
            return gotArg, nextCharPos, nextChar
            """
            compulsoryStack, optionalList = [], []
            for templatList in inputTemplates:
                for template in templateList:
                    if template['optional']:
                        optionalList.append(template)
                    else:
                        compulsoryStack.append(template)
            nextCharPos = m.end()+len(template['preSym'])
            nextChar = template['openBra']
            while len(compulsoryStack) > 0:
                template = compulsoryStack.pop()
                if nextChar == template['preSym']:
                    gotArg, nextCharPos, nextChar, closeBraPos, closeBraType = findBracketGetArgStore(m, template, nextChar, nextCharPos)
                else:
                    eOptionalList, gotArg, nextCharPos, nextChar, closeBraPos, closeBraType = processOptionalList(optionalList, template, nextCharPos, nextChar)
                storeTemplate['widthEnd'] = max(storeTemplate['widthEnd'], closeBraPos)
                storeTemplate['args'].append({
                    'nodeId':None, # this means that its just a slot, and not precisely filled yet
                    'funcName':None, # this means that its just a slot, and not precisely filled yet
                    'argIdx':inputTemplate['argIdx'],
                    'openBra':nextChar,# <<<<<<<<<<<<<<<if noBra arglen=1, store as None
                    'openBraPos':nextCharPos, 
                    'closeBra':closeBraType,
                    'closeBraPos': closeBraPos
                })

            eOptionalList, gotArg, nextCharPos, nextChar, closeBraPos, closeBraType = processOptionalList(optionalList, nextCharPos, nextChar)
            storeTemplate['widthEnd'] = max(storeTemplate['widthEnd'], closeBraPos)
            storeTemplate['args'].append({
                'nodeId':None, # this means that its just a slot, and not precisely filled yet
                'funcName':None,  # this means that its just a slot, and not precisely filled yet
                'argIdx':inputTemplate['argIdx'],
                'openBra':nextChar,# <<<<<<<<<<<<<<<if noBra arglen=1, store as None
                'openBraPos':nextCharPos, 
                'closeBra':closeBraType,
                'closeBraPos': closeBraPos
            })
            if foundType == 'backslash_function':
                self.backslash_pos_type.append(storeTemplate)
            elif foundType == 'backslash_variable':
                self.variables_pos_type.append(storeTemplate)
            def processOptionalList(eOptionalList, template, nextChar, nextCharPos):
                for template in eOptionalList:
                    gotArg, nextCharPos, nextChar, closeBraPos, closeBraType = findBracketGetArgStore(m, template, nextChar, nextCharPos)
                    if gotArg:
                        eOptionalList.remove(template)
                        break
                return eOptionalList, gotArg, nextCharPos, nextChar, closeBraPos, closeBraType
            def findBracketGetArgStore(m, template, nextChar, nextCharPos):
                closeBraPos, closeBraType = None, None
                if nextChar == template['openBra']: # found bracket
                    #get corresponding closePos
                    closeBraPos, closeBraType = self.bracketStorage.getCorrespondingCloseBraPos(nextCharPos)
                    #TAKEARG as everything between nextCharPos+len(nextChar) and closeBraPos, store
                    #NOTE bracket position if any, store
                    nextCharPos = closeBraPos + len(closeBraType)
                    self.bracketstorage.removeBracket(openBraPos)
                    if template['preSym'] in ['^']: # controlSymbols mixing with mathSymbols
                        """

            2b. check if there is a ^(exponent), to their direct right or left (note in brackets) [tree_building]
                2b1.^ to the left (power) [only for ASTreeConstructionBODMAS, input of infix] (remove from OTHER_brackets)
                2b2.^ to the right (base) [also for implicit_multiply remove_from_OTHER_brackets_after_implicit_multiply]

                        """
                        self.infixs_pos_type.remove((m.start(), m.end(), m.group()))
                elif template['braOptional'] == 'False': # no bracket but not neccessary
                    #log
                    gotArg = False #raise Exception #here is !gotArg
                elif template['braOptional'] == 'argLen<2': #no bracket, args of length 1 needed
                    #TAKEARG as nextCharPos+1, store
                    #NOTE NO_BRACKETS, store
                    nextCharPos += 1
                    self.bracketstorage.removeBracket(openBraPos)
                    if template['preSym'] in ['^']: # controlSymbols mixing with mathSymbols
                        self.infixs_pos_type.remove((m.start(), m.end(), m.group()))
                else:
                    #log
                    gotArg = False#raise Exception('Unhandled') #here is !gotArg
                    if foundType in ['backslash_function', 'backslash_variable']:
                        raise Exception()
                return gotArg, nextCharPos, nextChar, closeBraPos, closeBraType


        
        
    def _find_variables_or_numbers(self):
        """
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
        4c. go through all collected_variables and backslash_variables
            4c1. immediateRight, lookFor _{ , make them part of the variable.
            4c2. remove variable_brackets _{, from OTHER_brackets

        4d. These are VARIABLES|NUMBERS, also note start_position and length

        """
        #collate infix|backslash|matrices pos {infix_brackets are not removed, will be a problem if infix_brackets are curly}
        #backslash_brackets ONLY
        #matrices pos THE WHOLE MATRIX, not just the tags
        #self.list_openMatrixTagPos, self.list_closeMatrixTagPos, self.openMatrixTagPos__closeMatrixTagPos, self.closeMatrixTagPos__openMatrixTagPos
        #self.infixs_pos_type : [(startpos, endpos, group)], the symbol only
        # self.variables_pos_type = None # might already have backslashVar inside.
        self.number_pos_type = [] #decimal numbers like 123, 23.2, -3.4

        infixName_occupied = []
        for start, end, group in self.infixs_pos_type:
            for pos in range(start, end):
                infixName_occupied.append(pos)
        infixName_occupied = sorted(infixName_occupied)

        backslashName_occupied = []
        for start, end, group in self.backslashNames:
            for pos in range(start, end):
                backslashName_occupied.append(pos)
        backslashName_occupied = sorted(backslashName_occupied)

        bracketSym_occupied = []
        for (_, openBraPos, _), (closeBraPos, _, _) in self.allBrackets:
            bracketSym.append(openBraPos)
            bracketSym.append(closeBraPos)
        bracketSym_occupied = sorted(bracketSym_occupied)

        leftOverPosList = []
        for pos in range(0, len(self.rawEquationStr)):
            if self.__isPosInMatrixTag(pos) or \
            pos in infixName_occupied or \
            pos in backslashName_occupied or \
            pos in bracketSym_occupied:
                continue # we skip these
            leftOverPosList.append(pos)


        accumulator, accumulatorStartPos, accumulatorEndPos, accumulatorType= None, None, None, None
        for leftOverPos in leftOverPosList:
            leftOverChar = self.rawEquationStr[leftOverPos]
            isNume = isNum(leftOverChar)
            if accumulatorType is None:
                accumulator = leftOverChar
                accumulatorStartPos = leftOverPos
                accumulatorEndPos = accumulatorStartPos + len(leftOverChar) # len(leftOverChar) should always = 1
                accumulatorType = 'N' if isNume else 'V'
            elif (accumulatorType == 'N' and not isNume) or \
            (leftOverPos != leftOverPos): #break off conditions: 0. going_from_N_to_V. 1. not_consecutive
                self.variables_pos_type.append(
                    {
                        'nodeId':self.getNodeId(),
                        'funcType':'pure_variable',
                        'funcName':accumulator,
                        'funcStart':accumulatorStartPos,
                        'funcEnd':accumulatorEndPos,
                        'widthStart':accumulatorStartPos,
                        'widthEnd':accumulatorEndPos,
                        'args':[]
                    }
                )#<<<<<<<<<<<<<<<<<<<<<<could contain things like i=sqrt(-1), which is a number not a variable, should have its OWN FUNCTYPE, .... ANYTHING ELSE LIKE SUCH?
                self.number_pos_type.append(
                    {
                        'nodeId':self.getNodeId(),
                        'funcType':'pure_number',
                        'funcName':accumulator,
                        'funcStart':accumulatorStartPos,
                        'funcEnd':accumulatorEndPos,
                        'widthStart':accumulatorStartPos,
                        'widthEnd':accumulatorEndPos,
                        'args':[]
                    }

                )
                #reset
                accumulator = leftOverChar
                accumulatorStartPos = leftOverPos
                accumulatorEndPos = accumulatorStartPos + len(leftOverChar)
                accumulatorType = 'N' if isNume else 'V'
            else: # keep accumulating
                accumulator += leftOverChar
                accumulatorEndPos += len(leftOverChar)
                #startPos same. accumulatorType V->N or pure V or pure N is fine.




    def _find_implicit_0(self):
        """

    5. implicit_0 (-)(NOTHING_ELSE?) need to add to the list of all infixes, indicated by length 0. need starting_position
        5a. left of (nothing|open_brackets) , 
            5a1. nothing is the left_most of the equationStr
            5a2. search for open_brackets that have - (+ have no need of implicit_zero)

        """
        def addImplictMinus(funcPos):
            zeroNodeId = self.getNodeId()
            self.infixs_pos_type.append(
                {
                    'nodeId':self.getNodeId(),
                    'funcType':'infix_implicit',
                    'funcName':'-',
                    'funcStart':funcPos,
                    'funcEnd':funcPos,
                    'widthStart':funcPos,
                    'widthEnd':None,#<<<<<<<<<<<<<<<<<<<<<UNKNOWN since argIdx=1 is UNKNOWN
                    'args':[
                        {
                            'nodeId':zeroNodeId,
                            'funcName':'0',
                            'argIdx':0,
                            'openBra':None,
                            'openBraPos':None, 
                            'closeBra':None,
                            'closeBraPos': None
                        },
                        {
                            'nodeId':None,# just a SLOT, not filled in yet
                            'funcName':None,# just a SLOT, not filled in yet
                            'argIdx':1,
                            'openBra':None,# <<<<<<<<<<<<<<<if noBra arglen=1, store as None
                            'openBraPos':None, 
                            'closeBra':None,
                            'closeBraPos': None
                        }
                    ]
                }
            )
            self.number_pos_type.append(
                    {
                        'nodeId':zeroNodeId,
                        'funcType':'pure_number',
                        'funcName':'0',
                        'funcStart':funcPos,
                        'funcEnd':funcPos,
                        'widthStart':funcPos,
                        'widthEnd':funcPos,
                        'args':[]
                    }
            )


        if self.rawEquationStr[0] in ['-']:
            addImplictMinus(0)
        #all openbrackets except Matrices, no need bracketstorage
        for (_, openBraPos, openBraType), (closeBraPos, _, closeBraType) in self.allBrackets:
            if self.__isPosInMatrixTag(openBraPos) or self.__isPosInMatrixTag(closeBraPos):
                continue
            if self.rawEquationStr[openBraPos + 1] in ['-']:
                addImplictMinus(openBraPos + 1)


    def _find_infixes_backslashes_backslashvars_width(self):
        """

        AFTER THIS FUNCTION, we should get LARGEST WIDTH of backslashes

    6. get width(start~end) of infixes|backslash_function|backslash_variable
        6a. (by enclosing_brackets) or (by inputs) [tree_building]
        LOOK immediate LEFT&RIGHT of infix [tree_building] | but if immediate LEFT&RIGHT of infix are redundant_brackets? 
        then just update as width, and not as inputs
        6b. Check OTHER_brackets for enclosure that are wider than current_width_of_infix
        
        """
        #backslashes and backslashvars already have all their inputs, so its relatively easier than infixes
        for storeTemplate in self.backslash_pos_type:# backslash function ONLY, no filter needed
            storeTemplate['widthStart'] = storeTemplate['funcStart'] # backslash is the start
            storeTemplate['widthEnd'] = storeTemplate['funcEnd'] # farthest of all the closeBraPos
            for argTemplate in storeTemplate['args']:
                storeTemplate['widthEnd'] = max(storeTemplate['widthEnd'], storeTemplate['closeBraPos'])

        for storeTemplate in self.variables_pos_type: # contains pureVar and backslashVar
            if storeTemplate['funcType'] in ['backslash_variable']:
                storeTemplate['widthStart'] = storeTemplate['funcStart'] # backslash is the start
                storeTemplate['widthEnd'] = storeTemplate['funcEnd'] # farthest of all the closeBraPos
                for argTemplate in storeTemplate['args']:
                    storeTemplate['widthEnd'] = max(storeTemplate['widthEnd'], storeTemplate['closeBraPos'])

        #(matrices_pos_type|backslash_pos_type|variables_pos_type|number_pos_type) all have widthStart&widthEnd at_this_point

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
        widthStart__tuple_nodeId_funcName = {}
        widthEnd__tuple_nodeId_funcName = {}
        #mixing entities up is ok, since they have the same template
        #NOTE +self.infixs_pos_type NOT INCLUDED YET!
        for template in self.matrices_pos_type+self.backslash_pos_type+self.variables_pos_type+self.number_pos_type:
            widthStart__tuple_nodeId_funcName[template['widthStart']] = (template['nodeId'], template['funcName'])
            widthEnd__tuple_nodeId_funcName[template['widthEnd']] = (template['nodeId'], template['funcName'])
        #
        for storeTemplate in self.infixs_pos_type:
            """
                        storeTemplate = {
                            'nodeId':self.getNodeId(),
                            'funcType':'infix',
                            'funcName':m.group(),
                            'funcStart':m.start(),
                            'funcEnd':m.end(),
                            'args':[]
                        }

            {
                    'nodeId':self.getNodeId(),
                            'argIdx':inputTemplate['argIdx'],
                            'openBra':nextChar,# <<<<<<<<<<<<<<<if noBra arglen=1, store as None
                            'openBraPos':nextCharPos, 
                            'closeBra':closeBraType,
                            'closeBraPos': closeBraPos
                        }
            """
            #is there closeBra left of infixSym?
            closeBraType = ')'
            closeBraPos = storeTemplate['funcStart'] - len(closeBraType)
            if self.bracketstorage.exists(closeBraPos, BracketType.ROUND, False):
                closeBraPos, closeBraType = self.bracketstorage.getCorrespondingCloseBraPos(closeBraPos)
                #<<<<<<<<<<<<<<<store in inputs [tree_building] INPUT0
                storeTemplate['args'].append({
                    'nodeId':None, # JUST a SLOT, might have alot of thing in the brackets
                    'funcName':None, # JUST a SLOT, might have alot of thing in the brackets
                    'argIdx':0,
                    'openBra':openBraType,# <<<<<<<<<<<<<<<if noBra arglen=1, store as None
                    'openBraPos':openBraPos, 
                    'closeBra':closeBraType,
                    'closeBraPos': closeBraPos
                })
                self.bracketstorage.removeBracket(openBraPos)
            else:#no closeBra left of infixSym
                #<<<<<<<<<<<<<<<store in inputs [tree_building] INPUT0
                argNodeId, argFuncName = widthEnd__tuple_nodeId_funcName[closeBraPos] # if this throws error, you made AN INDEX MISTAKE with widthEnd or closeBraPos
                storeTemplate['args'].append({
                    'nodeId':argNodeId,
                    'funcName':argFuncName,
                    'argIdx':0,
                    'openBra':None,# MIGHT HAVE ENCLOSING, but will it be used?
                    'openBraPos':None, 
                    'closeBra':None,
                    'closeBraPos': None
                })
                self.bracketstorage.removeBracket(openBraPos)
            # is there openBra right of infixSym?
            openBraType = '('
            openBraPos = storeTemplate['funcEnd']# + len(openBraType)
            if self.bracketstorage.exists(openBraPos, BracketType.ROUND, True):
                openBraPos, openBraType = self.bracketstorage.getCorrespondingOpenBraPos(openBraPos)
                #<<<<<<<<<<<<<<<store in inputs [tree_building] INPUT1
                storeTemplate['args'].append({
                    'nodeId':None, # JUST a SLOT, might have alot of thing in the brackets
                    'funcName':None,
                    'argIdx':1,
                    'openBra':None,# <<<<<<<<<<<<<<<if noBra arglen=1, store as None
                    'openBraPos':None, 
                    'closeBra':None,
                    'closeBraPos': None
                })
                self.bracketstorage.removeBracket(openBraPos)
            else:#no openBra right of infixSym
                #<<<<<<<<<<<<<<<store in inputs [tree_building] INPUT1
                argNodeId, argFuncName = widthStart__tuple_nodeId_funcName[openBraPos] # if this throws error, you made AN INDEX MISTAKE with widthStart or openBraPos
                
                storeTemplate['args'].append({
                    'nodeId':argNodeId,
                    'funcName':argFuncName,
                    'argIdx':1,
                    'openBra':None,# MIGHT HAVE ENCLOSING, but will it be used?
                    'openBraPos':None, 
                    'closeBra':None,
                    'closeBraPos': None
                })
                self.bracketstorage.removeBracket(openBraPos)

            #CHECK wider enclosing brackets, for EVERYTHING 
            self.matrices_pos_type = self.__updateTemplatesToWiderEnclosingBracketsAndRemove(self.matrices_pos_type)
            self.infixs_pos_type = self.__updateTemplatesToWiderEnclosingBracketsAndRemove(self.infixs_pos_type)
            self.backslash_pos_type = self.__updateTemplatesToWiderEnclosingBracketsAndRemove(self.backslash_pos_type)
            self.variables_pos_type = self.__updateTemplatesToWiderEnclosingBracketsAndRemove(self.variables_pos_type)
            self.number_pos_type = self.__updateTemplatesToWiderEnclosingBracketsAndRemove(self.number_pos_type)
            #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<what is in self.bracketstorage at_this_point?????

    def __updateTemplatesToWiderEnclosingBracketsAndRemove(self, list_template):#INPLACE????
        for template in list_template:
            allEnclosingTouchingBra = self.bracketstorage.getAllEnclosingTouchingBraOfPos(template['funcStart'], BracketType.ROUND)
            if len(allEnclosingTouchingBra) > 0:
                widestWidth = 0
                widestBra = None
                for width, bracketId, openBraPos, closeBraPos in allEnclosingTouchingBra:
                    if width > widestWidth:
                        widestWidth = width
                        widestBra = (width, bracketId, openBraPos, closeBraPos)
                    self.bracketstorage.removeBracket(openBraPos) # because these bracket cannot contain anything else
                template['widthStart'] = widestBra[2] #TODO is this change INPLACE????
                tempate['widthEnd'] = widestBra[3] #TODO is this change INPLACE????
                #self.bracketstorage.removeBracket(widestBra[2])# NO NEED, already removed in the loop
        return list_template

        
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
        def addImplictMultiply(funcPos, arg0NodeId, arg1NodeId, arg0WidthStart, arg1WidthEnd, arg0FuncName, arg1FuncName):

            implicitMultiply = {
                    'nodeId':self.getNodeId(),
                    'funcType':'infix_implicit',
                    'funcName':'*',
                    'funcStart':funcPos,
                    'funcEnd':funcPos,
                    'widthStart':arg0WidthStart,
                    'widthEnd':arg1WidthEnd,
                    'args':[
                        {
                            'nodeId':arg0NodeId,
                            'funcName':arg0FuncName,
                            'argIdx':0,
                            'openBra':None,# could be FILLED, but we don't need it, since p|c relationship built
                            'openBraPos':None,# could be FILLED, but we don't need it, since p|c relationship built
                            'closeBra':None,# could be FILLED, but we don't need it, since p|c relationship built
                            'closeBraPos': None# could be FILLED, but we don't need it, since p|c relationship built
                        },
                        {
                            'nodeId':arg1NodeId,
                            'funcName':arg1FuncName, 
                            'argIdx':1,
                            'openBra':None,# could be FILLED, but we don't need it, since p|c relationship built
                            'openBraPos':None,# could be FILLED, but we don't need it, since p|c relationship built
                            'closeBra':None,# could be FILLED, but we don't need it, since p|c relationship built
                            'closeBraPos': None# could be FILLED, but we don't need it, since p|c relationship built
                        }
                    ]
                }
            implicitMultiply = self.__updateTemplatesToWiderEnclosingBracketsAndRemove([implicitMultiply])[0] # necessary for p|c later
            self.infixs_pos_type.append(implicitMultiply)


        alle = self.matrices_pos_type+self.infixs_pos_type+self.backslash_pos_type+self.variables_pos_type+self.number_pos_type
        for idx in range(0, len(alle)-1):
            vorDing = alle[idx]
            hinDing = alle[idx+1]
            if vorDing['widthEnd'] + 1 == hinDing['widthStart']:
                addImplictMultiply(
                    vorDing['widthEnd'], 
                    vorDing['nodeId'], 
                    hinDing['nodeId'], 
                    vorDing['widthStart'], 
                    hinDing['widthEnd'],
                    vorDing['funcName'],
                    hinDing['funcName']
                    )
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<what is in self.bracketstorage at_this_point?????

        
    def _match_child_to_parent_input(self):
        """
    ***everything has width at_this_point
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
        
        """
        self.alle = self.matrices_pos_type+self.infixs_pos_type+self.backslash_pos_type+self.variables_pos_type+self.number_pos_type
        """
        Use BracketStorage to help make faster query for each SLOT.
        self.cpbracketstorage.insert <<<<<<<<<<<<insert all alle the widthstart, widthend as brackets (FAKE brackets, we just need the query)
        self.cpbracketstorage.getWidestEnclosingBra <<<<<< for each SLOT, find the widest for the SLOT (TODO implemented) REMOVE getTightestEnclosingBra?[seems like its never used]
        """
        default = BracketType.ROUND # FAKE TODO rename bracketstorage to more general
        defaultOpen, defaultClose = default #FAKE TODO rename bracketstorage to more general
        cpbracketstorage = BracketStorage()
        bracketId__tuple_nodeId_funcName = {}
        nodeId__bracketId = {}
        for template in self.alle:
            bracketId = cpbracketstorage.insertBracket(defaultOpen, template['widthStart'], defaultClose, template['widthEnd'])
            bracketId__tuple_nodeId_funcName[bracketId] = (template['nodeId'], template['funcName'])
            nodeId__bracketId[template['nodeId']] = bracketId

        """
        Of the childNeedy, backslash_pos_type args have widthStart and widthEnd, only infixs_pos_type might have no widthStart and widthEnd and might require BODMAS
        we will seperately deal with them
        """
        for template in self.backslash_pos_type:
            if arg['nodeId'] is None: #This is criterion for a SLOT
                #find the widest child, that is stored in cpbracketstorage
                pos = arg['closeBraPos']# pos = arg['openBraPos'] | arg['closeBraPos']#<<<<either have nodeId(argLen<2) | have closeBraPos: guaranteed from _find_backslash
                #if output from cpbracketstorage.getWidestEnclosingBra doesn't fit 3-piece tuple, then _find_backslash made a mistake
                answer = cpbracketstorage.getWidestEnclosingBra(pos, default)
                _, _, bracketId = answer # we don't have to care about the width, since backslash width is fixed, after you get the args
                nodeId, funcName = bracketId__tuple_nodeId_funcName[bracketId] 
                arg['nodeId'] = nodeId# TODO is this INPLACE?????
                arg['funcName'] = funcName# TODO is this INPLACE?????
        #the self.infixs_pos_type have fixed width. so no need to update the width in the loop. we can bulk update after
        # self.backslash_pos_type = self.__updateTemplatesToWiderEnclosingBracketsAndRemove(self.backslash_pos_type) # already done in _find_infixes_backslashes_backslashvars_width

        for template in sorted(self.infixs_pos_type, key=lambda infix: Latexparser.INFIX.index(infix)): # should be processed in PRIORITY, no matter where they are. BODMAS
            if arg['nodeId'] is None: #This is criterion for a SLOT
                #is it right or left arg?
                if arg['argIdx'] == 0:#left
                    # TAKE length of leftCloseBra and take a small step to the left
                    pos = template['funcStart'] - len(arg['closeBraPos']) - 1
                elif arg['argIdx'] ==  1:#right
                    # TAKE length of rightOpenBra and take a small step to the right
                    pos = template['funcEnd'] + len(arg['openBraPos']) + 1
                else:#unhandled
                    raise Exception(f'Infix {template["funcName"]}, id {template["nodeId"]} has argIdx {template["argIdx"]}, argIdx should only be 0 or 1')
                
                #MUST HAVE ANSWER. WHY?
                answer = cpbracketstorage.getWidestEnclosingBra(pos, default)
                argOpenPos, argClosePos, bracketId = answer
                nodeId, funcName = bracketId__tuple_nodeId_funcName[bracketId]
                arg['nodeId'] = nodeId#TODO is this INPLACE??????
                arg['funcName'] = funcName#TODO is this INPLACE????
                if arg['argIdx'] == 0:#left
                    #right (widthEnd) is unchanged
                    template['widthStart'] = argOpenPos#left is changed
                elif arg['argIdx'] == 1:#right
                    #left (widthStart) is unchanged
                    template['widthEnd'] = argClosePos#right is changed
                else:#unhandled
                    raise Exception(f'Infix {template["funcName"]}, id {template["nodeId"]} has argIdx {template["argIdx"]}, argIdx should only be 0 or 1')
                #the new width will affect arg of those infixs yet_to_be_processed, so infix width has to be processed in the loop
                template = self.__updateTemplatesToWiderEnclosingBracketsAndRemove([template])[0]
                self.cpbracketstorage.updateBracket(
                    nodeId__bracketId[template['nodeId']], 
                    defaultOpen, #FAKE TODO rename bracketstorage to more general
                    template['widthStart'], #FAKE TODO rename bracketstorage to more general
                    defaultClose, #FAKE TODO rename bracketstorage to more general
                    template['widthEnd'] #FAKE TODO rename bracketstorage to more general
                )



        
    def _format_to_pyStyledAST(self):
        """

    go through all items, looking at inputs of each, create nodeId to list[nodeId] dictionary, store as latex tree
        """
        self.latexAST = {}
        for template in self.alle:
            list_tuple_nodeId_argIdx = sorted(map(lambda argTem: (argTem['nodeId'], argTem['argIdx'], argTem['argFuncName']), template['args']), key=lambda tup: tup[1]) #tup[1] is the argIdx
            self.latexAST[(template['funcName'], template['nodeId'])] = list(map(lambda tup: (tup[2], tup[0]), list_tuple_nodeId_argIdx)) # tup[2] is argFuncName, tup[0] is nodeId
        
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
        #TODO Pool multiprocessing with method priorities (Chodai!) -- dependency ha chain desu yo, sou shitara, motto hayaku arimasu ka?
        return self.ast, self.functions, self.variables, self.primitives, self.totalNodeCount, self.startPos__nodeId

#####################################################

    def _unparse(self): # TODO from AST to LaTeX string... 
        return self._recursiveUnparse(self.equalTuple)


    def _recursiveUnparse(self, keyTuple):
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


    closeBraType__sortedPosList = {}
    openBraType__sortedPosList = {}
    id__tuple_openPos_openBraType_closePos_closeBraType = {}
    list_tuple_width_id_openPos_closePos = []
    openBraPos__bracketId = {}
    closeBraPos__bracketId = {}

    def __init__(self):
        self.bracketId = 0

    def _getBracketId(self):
        import copy
        newBracketId = copy.copy(self.bracketId)
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

        deletePos = BinarySearch.binarySearchPre(
            self.list_tuple_width_id_openPos_closePos,
            #(closeBraPos - openBraPos, bracketId, openBraPos, closeBraPos),
            closeBraPos - openBraPos,
            key=lambda tuple_width_id: tuple_width_id[0] # get width, getWidestEnclosingBra might depend on this
        )
        del self.list_tuple_width_id_openPos_closePos[deletePos]

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

        immediateRightIdx = BinarySearch.binarySearchPre(theDict__sortedPosList[typeOfBracket], pos) # always gives right_of_pos
        
        braPos = float('inf') # for getAllEnclosingBraOfPos, if there is no such thing
        if 0 <= immediateRightIdx and immediateRightIdx < len(theDict__sortedPosList[typeOfBracket]):
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

        immediateRightIdx = BinarySearch.binarySearchPre(theDict__sortedPosList[typeOfBracket], pos) # always gives right_of_pos
        
        braPos = float('-inf') # for getAllEnclosingBraOfPos, if there is no such thing
        if 0 <= immediateRightIdx - 1 and immediateRightIdx - 1 < len(theDict__sortedPosList[typeOfBracket]):
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

    def getAllBracket(self):#TODO is this ever used? make a AST_dependency diagram... (good place to learn)
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

    def getAllEnclosingTouchingBraOfPos(self, pos, typeOfBracket):
        """
        There might be enclosingBra of pos p0 like so:

        (((p0))(p1))
        ^^^
        012

        In this case, we will only take 1 & 2. Although 0 also encloses p0, 0 also encloses p1, so we discard 0.

        This should solve the problem of users putting many same brackets around the same function|primitive


        :param typeOfBracket: BracketType.ROUND, BracketType.SQUARE, BracketType.CURLY
        :type typeOfBracket: BracketType Enum
        """
        filt__list_tuple_width_id_openPos_closePos = self.getAllEnclosingBraOfPos(pos, typeOfBracket)
        list_tuple_width_id_openPos_closePos__oC = [] # oC~openBraPos are Consecutive
        prevOpenBraPos = None
        for width, bracketId, openBraPos, closeBraPos in sorted(filt__list_tuple_width_id_openPos_closePos, key=lambda tup: tup[2]):#ascending by openBraPos
            if (prevOpenBraPos is None) or (openBraPos - 1 == prevOpenBraPos): # ensure openBraPos are consecutive
                list_tuple_width_id_openPos_closePos__oC.append((width, bracketId, openBraPos, closeBraPos))
                prevOpenBraPos = openBraPos
        list_tuple_width_id_openPos_closePos__oCcC = [] # cC~closeBraPos are Consecutive
        prevCloseBraPos = None
        for width, bracketId, openBraPos, closeBraPos in sorted(list_tuple_width_id_openPos_closePos__oC, key=lambda tup: tup[3]): #ascending by closeBraPos
            if (prevCloseBraPos is None) or (closeBraPos - 1 == prevCloseBraPos): # ensure closeBraPos are consecutive
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