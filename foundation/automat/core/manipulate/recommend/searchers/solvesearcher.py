import sys
from copy import deepcopy
from foundation.automat.common.priorityqueue import PriorityQueue

from foundation.automat.core.equation import Equation

class SolveSearcher:
    """
    #heuristics, if a certain type of history has been tried before, reorder the priority_queue to try something new?
    #heuristics, so there are simplification_patterns where the nodes decrease from iPattern to oPattern, these should also serve as targets, so formulas that have the most potential to be matched by these patterns, should be given higher priority..<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #heuristics, if we can simplify until there is only 1 of each variable, we can solve for anyVariable, by makeSubject<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    """

    def __init__(self):
        pass

    def search(self):
        visitedSchemeStrs = [equation.schemeStr]
        schemeLeastLength = sys.maxsize; leastLengthSchemeEquations = []; solvingSteps = []
        priorityQueue = PriorityQueue(); 
        priorityQueue.insert({
            'eq':equation,
            'depth':0,
            'history':[],
            'unHistory':[]#the equivalent of history, but in reverse fo each item in history
        }, -1)
        currentReachedMaximumDepth = 0
        while len(priorityQueue) > 0:
            state = priorityQueue.popMax()
            eq = state['eq']; depth = state['depth']; history = state['history']; unHistory = state['unHistory']
            
            if depth >= maximumDepth:
                # print('stopping search... because one of the states reached maximumDepth')
                #what to return?
                break

            manipulations = cls.filterForHeuristicsRelevantTo(eq, Recommend.getMetaData()) # branches

            
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
                returnTup = manipulate.apply(startPos__nodeId=eq.startPos__nodeId, toAst=False)
                if returnTup is not None:
                    manipulatedSchemeWord, manipulateType, manipulateClassName, manipulateDirection, manipulateIdx = returnTup
                    
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
                    # else: #if we visit the same formula again... and there is a smaller depth? like in bellmanFord, add a new pattern? but the maintenance will have to give it a name


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