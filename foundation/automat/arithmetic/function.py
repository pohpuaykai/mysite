from abc import ABC
from copy import deepcopy
import importlib
import inspect
import os

from foundation.automat import AUTOMAT_MODULE_DIR
from foundation.automat.common.backtracker import Backtracker


class Function:#(metaclass=FunctionHook):
    """
    Should be able to take an AST (dictionary, key: node (tuple[label, id]), value: list of neighbours (list[tuple[label, id]])
    and do:
    (1) each of its inputs (one at a time) the 'root of the sub-AST' (sub-subject of the equation) through inverses primitive
    (2) substitute primitives in variables, evaluate the sub-AST and replace sub-AST with primitve node
    (3) form a bunch of displayable
        (a) "Scheme - styled_string" (with pretty option)
        (b) "Latex - styled_string"
        (c) MathML (html)


    """
    _FUNC_NAMES = []
    _FUNCNAME__MODULENAME = {}
    _FUNCNAME__CLASSNAME = {}
    _TRIGNOMETRIC_NAMES = []

    def __init__subclass(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # import pdb;pdb.set_trace()
        # if kwargs.get('type') == 'trigonometric' and kwargs.get('funcName') is not None: # somehow, this is nie gerennt, wenn TRIGONOMETRIC_NAMES hiess
        #     cls._TRIGONOMETRIC_NAMES.append(kwargs.get('funcName'))
        # if type == 'trigonometric':
        #     cls.TRIGONOMETRIC_NAMES.append(funcName)
        # import pdb;pdb.set_trace()

    # @property # for now it wll return a property-object, and the expected list... , TODO so we will use it as a cls_method FOR NOW
    @classmethod
    def TRIGONOMETRIC_NAMES(cls): #TODO refactor0
        if len(cls._TRIGNOMETRIC_NAMES) == 0:
            #gather all the trigonometric function names
            module_dir = os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'standard')
            for module in os.listdir(module_dir):
                # print('***', module)
                if module.endswith('.py') and module != '__init__.py':
                    module_name = module[:-3] # remove .py
                    module_obj = importlib.import_module(f'.{module_name}', package='foundation.automat.arithmetic.standard')
                    for name, ocls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                        if name in ['Function']:
                            continue
                        # print('name***', name, '***ocls***', ocls)
                        # import pdb;pdb.set_trace()
                        if ocls.TYPE == 'trigonometric':
                            # import pdb;pdb.set_trace()
                            cls._TRIGNOMETRIC_NAMES.append(ocls.FUNC_NAME)

        return cls._TRIGNOMETRIC_NAMES


    @classmethod
    def FUNC_NAMES(cls): #TODO refactor0
        if len(cls._FUNC_NAMES) == 0:
            #gather all the function names
            module_dir = os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'standard')
            for module in os.listdir(module_dir):
                if module.endswith('.py') and module != '__init__.py':
                    module_name = module[:-3] # remove .py
                    module_obj = importlib.import_module(f'.{module_name}', package='foundation.automat.arithmetic.standard')
                    for name, ocls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                        if name in ['Function']: #skip the parent of all function
                            continue
                        cls._FUNC_NAMES.append(ocls.FUNC_NAME)
        return cls._FUNC_NAMES


    @classmethod
    def FUNCNAME__MODULENAME(cls): #TODO refactor0
        if len(cls._FUNCNAME__MODULENAME) == 0:
            #gather all the function names
            module_dir = os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'standard')
            for module in os.listdir(module_dir):
                if module.endswith('.py') and module != '__init__.py':
                    module_name = module[:-3] # remove .py
                    module_obj = importlib.import_module(f'.{module_name}', package='foundation.automat.arithmetic.standard')
                    for klassName, ocls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                        if klassName in ['Function']: #skip the parent of all function
                            continue
                        cls._FUNCNAME__MODULENAME[ocls.FUNC_NAME] = module_name
        return cls._FUNCNAME__MODULENAME


    @classmethod
    def FUNCNAME__CLASSNAME(cls): # TODO refactor0
        if len(cls._FUNCNAME__CLASSNAME) == 0:
            #gather all the function names
            module_dir = os.path.join(AUTOMAT_MODULE_DIR, 'arithmetic', 'standard')
            for module in os.listdir(module_dir):
                if module.endswith('.py') and module != '__init__.py':
                    module_name = module[:-3] # remove.py
                    module_obj = importlib.import_module(f'.{module_name}', package='foundation.automat.arithmetic.standard')
                    for klassName, ocls in inspect.getmembers(module_obj, predicate=inspect.isclass):
                        if klassName in ['Function']: # skip the parent of all function
                            continue
                        cls._FUNCNAME__CLASSNAME[ocls.FUNC_NAME] = klassName
        return cls._FUNCNAME__CLASSNAME



    def __init__(self, equation, idInAst, verbose=False):
        self.eq = equation
        self.inverses = None
        self.verbose = verbose
        self.idInAst = idInAst


    def reverse(self, equationSide, argumentIdx, nodeIds):
        """
        make argumentIdx the subject of the subAST

        :param argumentIdx: the index of the argument of self(this function) to make into the subject of the formula
        :type argumentIdx: int
        :param nodeIds: node ids (of the AST) to do the inversion on
        :type nodeIds: list[int]
        :return: multiple returns
            - Modified Abstract Syntax Tree
            - mapping from FUNC_NAME to (number of increase in FUNC_NAME in new tree, will be negative if it decrease)
            - mapping from variable_str to (number of increase in variable_str in new tree, will be negative it decrease)
            - how many primitives were added?
            - how many total nodes were added to the AST?
        :rtype: tuple[
            dict[tuple[str, int], list[tuple[str, int]]],
            dict[str, int],
            dict[str, int],
            int,
            int]
        """
        ast = deepcopy(self.eq.ast)
        replacementDictionary = {}
        for key, value in ast.items():
            if key[1] in nodeIds:
                replacementDictionary[key] = value

        if self.verbose:
            print('replacementDictionary')
            print(replacementDictionary)
            print('len(replacementDictionary):', len(replacementDictionary))
            print('reverses key: ', (equationSide, str(argumentIdx)))


        #will raise error if function of the node with `nodeId` is not equals to self.FUNC_NAME, handle in child.inverse
        (invertedResults, functionCountChange, primitiveCountChange, totalNodeCountChange) = self.reverses[(equationSide, str(argumentIdx))](
            replacementDictionary, self.eq.totalNodeCount)

        if self.verbose:
            print('invertedResults')
            print(invertedResults)


        for oldKey, oldValue in invertedResults.items():
            if oldKey in ast: # due to addition of operations, `oldKey` might not exist in ast
                del ast[oldKey]
            ast[oldValue['newKey']] = list(oldValue['newValue'])
        return ast, functionCountChange, primitiveCountChange, totalNodeCountChange

    def evalFunctor(self):
        """

        #~ DRAFT ~#
        
        evaluates the AST for functors like Differentiation and Integration


        TODO this is a sketch... please test&correct
        """
        #prevent circular import
        from foundation.automat.arithmetic.sfunctor import FUNCTOR_NAMES_TO_CLASS
        queue = [self.ast] # TODO need to insert the root.... of the AST.... which i did not put in...
        while len(queue) != 0:
            current = queue.pop()
            if current.label in FUNCTOR_NAMES_TO_CLASS: 
                neighbours = self.ast[current.label]
                subroot = neighbours[0]
                withrespectto = neighbours[1]
                self.ast = FUNCTOR_NAMES_TO_CLASS[current.label]._calculate(subroot, withrespectto)
                # put which neighbours in queue again?
