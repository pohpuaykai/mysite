
from foundation.automat.arithmetic.function import Function


class Sineh(Function):
    """

    """
    TYPE = 'trigonometric'
    FUNC_NAME = 'sinh'

    def __init_subclass__(cls, **kwargs):
        kwargs['type'] = 'trigonometric'
        kwargs['funcName'] = 'sinh'
        super().__init_subclass__(**kwargs)

    def __init__(self, equation, idInAst, verbose=False):
        """

        """
        super().__init__(equation, idInAst, verbose=verbose)
        self.reverses = {
            
                ("R", "0"): self._reverseR0,
            
                ("L", "0"): self._reverseL0
            
        }

    
    def _reverseR0(self, replacementDictionary, totalNodeCount, startPos__nodeId):
        """
        replacementDictionary are the rows in the AST mapping that needs to be replaced.
        Aim of this function is to make #1 input, the subject
        replacementDictionary will always have exactly 2 rows, because of the nature of equality.
        One of the list have this tuple ('sinh', nodeId) on the #2 argument. Since this is
        the function that will operate on it.

        :param replacementDictionary: 
        :type replacementDictionary: dict[tuple[str, int], list[tuple[str, int]]]
        :param totalNodeCount:
        :type totalNodeCount: int
        :return: tuple
         - input that was reversed
         - mapping from FuncName to how many of FuncName was added by this reversal, if its a negative, then its removal
         - total number of primitives that was added. If its negative, then primitives was removed
         - total number of nodes that was added. If its negative, the nodes were removed
        :rtype: tuple [
            dict[str, dict[str, Any]],
            dict[str, int],
            int,
            int
        ]
        """
        #error checking 
        if len(replacementDictionary) != 2: # always be 2 due to nature of equality
            raise Exception('replacementDictionary incorrect length')
        key0 = None
        key1 = None
        for key, value in replacementDictionary.items():
            #We are checking for id-equivalence of this function, instead of name-equivalence like '==self.FUNC_NAME'
            if len(value) > 1 and value[1][1] == self.idInAst:# value[1][0] == self.FUNC_NAME:# value[1] assumes that operation on the right-side
                key0 = key
            else:
                key1 = key
        if key0 is None or key1 is None:
            raise Exception("replacementDictionary not according to format")

        permutation = {(0, 0): (1, 0), (0, 1): (0, 0), (1, 0): (0, 1)}
        from copy import deepcopy
        newStartPos__nodeId = deepcopy(startPos__nodeId)
        rowCol__nodeId = {
            (0, 0):replacementDictionary[key0][0][1], # [1], um die ausWeisungen zu bekommen
            (0, 1):replacementDictionary[key0][1][1],
            (1, 0):replacementDictionary[key1][0][1],
            (1, 1):replacementDictionary[key1][1][1]
        }
        nodeId__startPos = dict(map(lambda t: (t[1],t[0]), startPos__nodeId.items()))
        for iRowCol, oRowCol in permutation.items():
            iNodeId = rowCol__nodeId[iRowCol]
            oNodeId = rowCol__nodeId[oRowCol]
            startPos = nodeId__startPos[iNodeId]
            newStartPos__nodeId[startPos] = oNodeId

        
        from foundation.automat.arithmetic.standard.arcsineh import Arcsineh
        
        return {key0: {"newKey": key0, "newValue": ((Arcsineh.FUNC_NAME, replacementDictionary[key0][1][1]), replacementDictionary[key1][0])}, key1: {"newKey": (Arcsineh.FUNC_NAME, key1[1]), "newValue": (replacementDictionary[key0][0],)}}, {Sineh.FUNC_NAME: -1, Arcsineh.FUNC_NAME: 1}, {}, 0, newStartPos__nodeId

    
    def _reverseL0(self, replacementDictionary, totalNodeCount, startPos__nodeId):
        """
        replacementDictionary are the rows in the AST mapping that needs to be replaced.
        Aim of this function is to make #1 input, the subject
        replacementDictionary will always have exactly 2 rows, because of the nature of equality.
        One of the list have this tuple ('sinh', nodeId) on the #2 argument. Since this is
        the function that will operate on it.

        :param replacementDictionary: 
        :type replacementDictionary: dict[tuple[str, int], list[tuple[str, int]]]
        :param totalNodeCount:
        :type totalNodeCount: int
        :return: tuple
         - input that was reversed
         - mapping from FuncName to how many of FuncName was added by this reversal, if its a negative, then its removal
         - total number of primitives that was added. If its negative, then primitives was removed
         - total number of nodes that was added. If its negative, the nodes were removed
        :rtype: tuple [
            dict[str, dict[str, Any]],
            dict[str, int],
            int,
            int
        ]
        """
        #error checking 
        if len(replacementDictionary) != 2: # always be 2 due to nature of equality
            raise Exception('replacementDictionary incorrect length')
        key0 = None
        key1 = None
        for key, value in replacementDictionary.items():
            #We are checking for id-equivalence of this function, instead of name-equivalence like '==self.FUNC_NAME'
            if len(value) > 1 and value[0][1] == self.idInAst:# value[0][0] == self.FUNC_NAME:# value[1] assumes that operation on the right-side
                key0 = key
            else:
                key1 = key
        if key0 is None or key1 is None:
            raise Exception("replacementDictionary not according to format")

        permutation = {(0, 0): (1, 0), (0, 1): (0, 0), (1, 0): (0, 1)}
        from copy import deepcopy
        newStartPos__nodeId = deepcopy(startPos__nodeId)
        rowCol__nodeId = {
            (0, 0):replacementDictionary[key0][0][1], # [1], um die ausWeisungen zu bekommen
            (0, 1):replacementDictionary[key0][1][1],
            (1, 0):replacementDictionary[key1][0][1],
            (1, 1):replacementDictionary[key1][1][1]
        }
        nodeId__startPos = dict(map(lambda t: (t[1],t[0]), startPos__nodeId.items()))
        for iRowCol, oRowCol in permutation.items():
            iNodeId = rowCol__nodeId[iRowCol]
            oNodeId = rowCol__nodeId[oRowCol]
            startPos = nodeId__startPos[iNodeId]
            newStartPos__nodeId[startPos] = oNodeId

        
        from foundation.automat.arithmetic.standard.arcsineh import Arcsineh
        
        return {key0: {"newKey": key0, "newValue": (replacementDictionary[key1][0], (Arcsineh.FUNC_NAME, replacementDictionary[key0][0][1]))}, key1: {"newKey": (Arcsineh.FUNC_NAME, key1[1]), "newValue": (replacementDictionary[key0][1],)}}, {Sineh.FUNC_NAME: -1, Arcsineh.FUNC_NAME: 1}, {}, 0, newStartPos__nodeId

    

    def _calculate(self, v0):
        """
        Used to get the numerical value of this function, when all the inputs applied are numerical.
        Also used in substitution method of parent :class:`Function`

        
        :param v0: 0-th input of this function
        :type v0: float
        
        :return: calculated numerical result
        :rtype: float
        """
        from math import sinh
        num=sin(v0)
        return num