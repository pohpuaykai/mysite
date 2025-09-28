import inspect
import pprint

from foundation.automat.core.equation import Equation
from foundation.automat.core.manipulate.recommend.recommend import Recommend


pp = pprint.PrettyPrinter(indent=4)



def test__deriveMetaInformation__basic(verbose=False):#TODO does not work
    eqs = '(= a (+ b c))' # fill it in
    eqsType = 'scheme'
    #filename = 'communtativity'
    direction = 'vor'
    idx = 0
    eq0 = Equation(eqs, eqsType)
    rec = Recommend(eq0, verbose=verbose)
    manipulatedSchemeEquation = rec._deriveMetaInformation() # (+ $0 $1)
    expected = '(= a (+ c b))' # (+ $1 $0)
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', expected == manipulatedSchemeEquation)
    if verbose:
        print(manipulatedSchemeEquation)


def prevu__groupSimiliarEquationsTogether(verbose=False):#also similar patterns should have more matches(use this as a fast way to check if a iPattern will match an equation)? and you can define your own similar now with stringcompare.eDL<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    list_equationStrs = [
        '(= I_{R_{0}} I_{DC_{1}})', 
        '(= I_{R_{0}} I_{R_{3}})', 
        '(= I_{DC_{1}} I_{R_{3}})', 
        '(= (+ (- (- 0 V_{R_{0}}) V_{R_{3}}) V_{DC_{1}}) 0)', 
        '(= (/ V_{R_{0}} I_{R_{0}}) R_{R_{0}})', 
        '(= (/ V_{DC_{1}} I_{DC_{1}}) R_{DC_{1}})', 
        '(= (/ V_{R_{3}} I_{R_{3}}) R_{R_{3}})'
    ]#preferably the eDL will avoid counting variables, and only the schemeStructure and functions
    #
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
    cutoffScore = 0.34#hardcode for now... there must be someway to parametrise this?
    from foundation.automat.common.unionfindbyrankwithpathcompression import UnionFindByRankWithPathCompression
    uf = UnionFindByRankWithPathCompression(len(list_equationStrs))
    for (idx0, idx1), score in tuple_comparisonIdx__score.items():
        if score < cutoffScore:
            uf.union(idx0, idx1)
    list_list_idx = uf.grouping()
    #convert to vertexId
    if verbose:
        # pp.pprint(idx__entities)
        pp.pprint(tuple_comparisonIdx__score)
        pp.pprint(list_list_idx)
        """
        Matrix of similiarity is here (or you can change the way eDL measure schemeStr Distance...):
{   (0, 1): 0.3333333333333333,
    (0, 2): 0.3333333333333333,
    (0, 3): 1.5,
    (0, 4): 0.75,
    (0, 5): 0.75,
    (0, 6): 0.75,
    (1, 2): 0.3333333333333333,
    (1, 3): 1.5,
    (1, 4): 0.75,
    (1, 5): 0.75,
    (1, 6): 0.75,
    (2, 3): 1.5,
    (2, 4): 0.75,
    (2, 5): 0.75,
    (2, 6): 0.75,
    (3, 4): 0.8571428571428571,
    (3, 5): 0.8571428571428571,
    (3, 6): 0.8571428571428571,
    (4, 5): 0.2,
    (4, 6): 0.2,
    (5, 6): 0.2}
        Maybe use laplacian_matrix(then your solver must first solve polynomial...(numerical can be done with newton method))? 
        or we just have a sharp_cutoff value for now? Or should the sharp_cutoff be parametrised, by sum lens(countingEntitiesAs1) of the schemeStrs (ONLY)?
        {Ou est vers origin, ja?} maybe the oddOnes should be chosen as startNode?
        """



if __name__=='__main__':
    # test__deriveMetaInformation__basic(True)
    prevu__groupSimiliarEquationsTogether(True)