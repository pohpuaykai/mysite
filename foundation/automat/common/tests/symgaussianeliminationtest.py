import inspect
import pprint

from foundation.automat.common.mstprim import MstPrim

def sge__numeric__test(verbose=True):#test case numeric
    additionGroup = Group(identity=0)
    multiplyGroup = Group(identity=1)
    def add(a,b):
        return a+b
    def minus(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
        

    additionGroup.otverse=add
    additionGroup.inverse=minus
    multiplyGroup.otverse=multiply
    multiplyGroup.inverse=divide
    field = Field(additionGroup, multiplyGroup)

    table = [[1,2],[3,4]]
    expected = [[1,0],[0,1]]
    sge=SGE(field,table)
    solved=sge.solve()


def sge__symbolic__test(verbose=True):#test case symbolic
    """
    #test case symbolic, this does not work, 
    #1. need to parse the inputs for +,-,*,/ into a tree
    #2. needs to combine the aParseTree and bParseTree... somehow
    TODO
    """
    import re
    numPattern = '(\d*)(\D+)'
    def breakNumStr(numString):
        possibleMatch = re.search(numString, numPattern)
        if possibleMatch:
            return possibleMatch.groups()#num, non-num
            
    def add(a,b):#TODO incomplete what about have +, -, *,/ already in the a and b?
        aNum, aNNum = breakNumStr(a) # requires that parser....
        bNum, bNNum = breakNumStr(b)
        if aNNum == bNNum:
            return f'{aNum+bNum}{aNNum}'
        else:
            return f'{a}+{b}'
            
    def minus(a,b):
        aNum, aNNum = breakNumStr(a)
        bNum, bNNum = breakNumStr(b)
        if aNNum == bNNum:
            return f'{aNum-bNum}{aNNum}'
        else:
            return f'{a}-{b}'