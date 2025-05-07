class Latexparser(): # TODO follow the inheritance of _latexparser
    
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
        6a. ALL_X_INF = MATRICES+BACKSLASH+VARIABLES+NUMBERS+OTHER_brackets (EVERYTHING EXCEPT INFIX??)
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
    BACKSLASH_INFIX = ['\\times', '\\cdot','\\%','\\to']
    PRIOIRITIZED_INFIX = [ '^', '/','//', '*', '-', '+']#['^', '/', '*', '-', '+'] 
    INFIX = BACKSLASH_INFIX+PRIOIRITIZED_INFIX+['=']# the smaller the number the higher the priority
    OPEN_BRACKETS = ['{', '[', '(']
    CLOSE_BRACKETS = ['}', ']', ')']
    close__open = dict(zip(CLOSE_BRACKETS, OPEN_BRACKETS))
    open__close = dict(zip(OPEN_BRACKETS, CLOSE_BRACKETS))

    ##### PUT BACK LATER
    #TRIGOFUNCTION = Function.TRIGONOMETRIC_NAMES() # then no need to map between latex and scheme
    TRIGOFUNCTION = ['arccos', 'cos', 'arcsin', 'sin', 'arctan', 'tan', 
    'arccsc', 'csc', 'arcsec', 'sec', 'arccot', 'cot', 'arsinh', 'sinh', 'arcosh', 'cosh', 
    'artanh', 'tanh', 'arcsch', 'csch', 'arsech', 'sech', 'arcoth', 'coth']
    ######
    BACKSLASH_EXPECTED_INPUTS = { #all possible returns according to input_type, for easy collating
        '^{}()':[
                {'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'argLen<2'}, #exponential
                {'preSym':'', 'optional':False, 'openBra':'(', 'closeBra':')', 'braOptional':'False'} # angle
        ],
        '()':[
                {'preSym':'', 'optional':False, 'openBra':'(', 'closeBra':')', 'braOptional':'False'}
        ],
        '_{}()':[
                {'preSym':'_', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'argLen<2'},
                {'preSym':'', 'optional':False, 'openBra':'(', 'closeBra':')', 'braOptional':'False'}
        ],
        '{}{}':[
                {'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
        ],
        '[]{}':[
                {'preSym':'', 'optional':True, 'openBra':'[', 'closeBra':']', 'braOptional':'False'},
                {'preSym':'', 'optional':False, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
        ],
        '_{}^{}{}':[
                {'preSym':'_', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'},
                {'preSym':'', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'False'}
            ]
    }
    
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
    #TODO move this up to BACKSLASH_EXPECTED_INPUTS ??
    VARIABLENAMESTAKEANARG = ['overline', 'underline', 'widehat', 'widetilde', 'overrightarrow', 'overleftarrow', 'overbrace', 'underbrace'
    #Math mode accents
    'acute', 'breve', 'ddot', 'grave', 'tilde', 'bar', 'check', 'dot', 'hat', 'vec'
    ] # these 'functions' must be preceded by {
    """['arccos', 'cos', 'arcsin', 'sin', 'arctan', 'tan', 
    'arccsc', 'csc', 'arcsec', 'sec', 'arccot', 'cot', 'arsinh', 'sinh', 'arcosh', 'cosh', 
    'artanh', 'tanh', 'arcsch', 'csch', 'arsech', 'sech', 'arcoth', 'coth']"""
    #INTEGRALS = ['int', 'oint', 'iint'] # TODO hikitoru this from sfunctors # remove
    FUNCTIONNAMES = TRIGOFUNCTION + ['frac', 'sqrt',  'log', 'ln'] + INTEGRALS
    EXCLUDE_BACKSLASH = ['\\to']
    
    def __init__(self, equationStr=None, ast=None, verbose=False):
        self.rawEquationStr = equationStr
        self.equationStr = None #processed rawEquationStr
        self.matrices_pos_type = None
        self.infixs_pos_type = None
        self.variables_pos_type = None
        self.symnum_pos_type = None #symbolic number like \\pi, i
        self.number_pos_type = None #decimal numbers like 123, 23.2, -3.4
        self.node_id = 0
        
    def _remove_all_spacing(self):
        self.equationStr = self.rawEquationStr.replace(" ", '')
        
    def _find_matrices(self):
        """
        
        I can only think of 3 ways to do this? Implement one first, and then later do both, and parallelise
        1. go character by character
        2. use re.findall, match outer \begin\end <<<<<<<<<< we going with this
        3. str.find, chop and str.find, and then match outer \begin\end
        
        """
        import re
        matrixStartTags = list(map(lambda m: 
            (m.start(), m.end(), m.group()), 
            re.finditer(r"\\begin\{\wmatrix\}", self.equationStr))) # the help page guarantees sorted, right to left, might be better to sort
        matrixEndTags = list(map(lambda m: 
            (m.start(), m.end(), m.group()), 
            re.finditer(r"\\end\{\wmatrix\}", self.equationStr))) # the help page guarantees sorted, right to left, might be better to sort
        self.matrices_pos_type = list(zip(matrixStartTags, reversed(matrixEndTags)))
        #collate all the matrix_start_end_tag, like bubblemerge, then we get many non-overlapping intervals
        #collate all non-overlaping intervals, to removed for leftover-finding
        
   
    def _find_infix(self):
        """
        Again, the same 3 ways as _find_matrices
        1. go character by character
        2. use re.findall <<<<<<<<<
        3. str.find, chop and str.find, and then match outer \begin\end
        
        """
        import re
        self.infixs_pos_type = []
        for infix in self.INFIX:
            infix_pos_type_list = list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"\{infix}", self.equationStr)))
            self.infixs_pos_type += infix_pos_type_list
        
    def _find_brackets(self):
        """
        
        2a. Keep position of all the brackets as a kind of datastorage, need to get all the 
        DO NOT INCLUDE MATRIX. (remove from OTHER_brackets)
        2d. check if left&right infixes (put to infix as inputs) (remove from OTHER_brackets)
        """
        #collate all the matrix_start_end_tag, like bubblemerge, then we get many non-overlapping intervals
        
        bracketStorage = {}
        brackets = set()
        for k, templateList in BACKSLASH_EXPECTED_INPUTS.items():
            for template in templateList:
                brackets.add((template['openBra'] template['closeBra']))
        for openBracket, closeBracket in brackets: # order in which we process the brackets does not matter
            openBracket_pos_type_list = list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"\\{openBracket}", self.equationStr))) # the help page guarantees sorted, right to left, might be better to sort
            closeBracket_pos_type_list = list(map(lambda m: (m.start(), m.end(), m.group()), re.finditer(f"\\{closeBracket}", self.equationStr))) # the help page guarantees sorted, right to left, might be better to sort
            #check if its between matrix_start_end_tag,
            #if so, do not store.
        # TODO store the bracket...  how to make it short_to_query? WHAT are your queries?
        
        
        
        
    def _find_backslash(self):
        """
        
        3. find start_position of all the backslashs (sqrt is special), EXCLUDE EXCLUDE_BACKSLASH like \to, because its an infix
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
        3. str.find, chop and str.find, and then match outer \begin\end
        find the inputs to these backslash using _getExpectedBackslashInputs as template
        Exclude all the backslash_infix
        
        """
        import re
        self.backslash_pos_type = []
        self.variables_pos_type = []
        self.symnum_pos_type = [] #symbolic number like \\pi, i
        for m in re.finditer(r"\\([a-zA-z]+)", self.equationStr):
            if m.group() in BACKSLASH_INFIX: # remove the backslash_infix from backslash
                continue
            if m.group() in VARIABLENAMESTAKEANARG: # variable_function is actually a variable
                self.variables_pos_type.append(m.group())
            inputTemplate = _getExpectedBackslashInputs(m.group())
            if inputTemplate is None: # number that starts with backslash. like \\pi
                self.symnum_pos_type.append(m.group())
            #backslash function at_this_point
            #search for immediateNextBracket inputs from m.start(), until m.end() 
            #inputTemplate = {'preSym':'^', 'optional':True, 'openBra':'{', 'closeBra':'}', 'braOptional':'argLen<2'}
            #if i search for same brackets, for every inputTemplate, i go through the same_parts_of_the_equation many...many...times a wasted time?
            
        
        
    def _find_variables_or_numbers(self):
        pass
        
    def _find_implicit_0(self):
        pass
        
    def _find_implicit_multiply(self):
        pass
        
    def _find_infixes_width(self):
        pass
        
    def _match_child_to_parent_input(self):
        pass
        
    def _format_to_pyStyledAST(self):
        pass
        
    def _convert_to_schemeStyledAST(self):
        #handle Latex specials
        pass
        
    def _get_statistics(self):
        pass


class BracketStorage:
    """USE 
    
        # GET CLOSEST OPENBRACKET OF A TYPE, TO THE RIGHT OF A POSITION <<<_find_backslash 'sREQUEST
        #  IS THERE A - RIGHT OF OPENBRACKETS? <<<_find_implicit_0 'sREQUEST
        #  GET ALL START END POSITION OF ALL BRACKETS <<<_find_implicit_multiply 'sREQUEST
        #  GET ALL BRACKETS CLOSEIMRIGHT|OPENIMLEFT|TIGHTESTENCLOSE of infix <<<_find_infixes_width 'sREQUEST
        #Design a datastructure, good for all the above.
        #give an id to each pair of bracket for easy removal (linking the open and close) <<< for enclosure_query too?
        #dict__close_right, key=bracket_type, value=close_bracket_position_list_ascending
        #dict__close_to_open, key=position_of_close_bracket, value=position_of_open_bracket
        #dict__open_left, key=bracket_type, value=open_bracket_position_list_ascending
        #dict__open_to_close, key=position_of_open_bracket, value=position_of_close_bracket
        #dict__id_openclosepos, key=id, value=tuple__openPos_closePos
        #dict__type_widthId, key=bracket_type, value=list__tuple__width_id
        #agis GET_ALL
    """
    closeBraType__sortedPosList = {}
    closeBraPos__openBraPos = {}
    openBraType__sortedPosList = {}
    openBraPos__closeBraPos = {}
    id__tuple_openPos_closePos = {}
    braType__list_tuple_width_id = {}
    
    def insertBracket(self, openBraType, openBraPos, closeBraType, closeBraPos):
        """
        return id
        """
        pass
        
    def removeBracket(self, id):
        """"""
        pass
    
    def getBraPosImmediateRightOfPos(self, pos, typeOfBracket, open):
        """
        
        open==True, means we are looking for openbracket, else we are looking for closebracket
        """
        pass
        
    
    def getBraPosImmediateLeftOfPos(self, pos, typeOfBracket, open):;
        """
        open==True, means we are looking for openbracket, else we are looking for closebracket
        """
        pass
        
    def getAllBracket(self):
        """
        return all the bracket in tuple (openBraType, openBraPos, closeBraType, closeBraPos)
        """
        pass
        
    def getTightestEnclosingPos(self, pos):
        """
        return tightest bracket, that contains pos
        """
        pass