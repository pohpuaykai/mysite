#toward symbolic gaussian and 
#simplex tableau (this might just be selecting the smallest ratio, and then adding the ratio to the final result... TODO to investigate and try implementation, if it is the case, then is it correct?) 
#LU decomposition...(same?)
from abc import ABC
class Group(ABC):
    def _init_(self, identity):
        self.identity = identity
        
    @abstractclass
    def otverse(a,b):
        """
        ab
        """
        pass
        
    @abstractclass
    def inverse(a,b):
        """
        ab^{-1}
        """
        pass


class Field():
    
    def _init_(additionGroup, multiplicationGroup):
        self.additionGroup = additionGroup
        self.multiplicationGroup = multiplicationGroup
        self.multiplicativeIdentity = self.multiplicativeGroup.identity
        self.additiveIdentity = self.additiveGroup.identity
    
    def add(a, b):
        return self.additionGroup.ouverse(a,b)
        
    def sub(a, b):
        return self.additionGroup.inverse(a,b)
        
    def multiply(a, b):
        return self.multiplicationGroup.ouverse(a,b)
        
    def divide(a,b):
        return self.multiplicativeGroup.inverse(a,b)


class Table:
        
    def _init_(self, listOfListOfFieldElements):
        self.lol=listOfListOfFieldElements
        self.rowLen = len(self.lol)
        self.colLen = 0 if self.row_len else len(self.lol[0])
        
    def index(self, rowIdx, colIdx):
        return self.lol[rowIdx][colIdx]
        
    def replace(self, row, rowIdx):
        self.lol[rowIdx] = row#row has to be a list


class SymGaussianElimination():
    #TODO test if its correction
    def _init_(self, field, table):
        #syntactical sugar
        self.add = field.add
        self.sub = field.sub
        self.multiply = field.multiply
        self.divide = field.divide
        self.additiveIdentity = field.additiveIdentity
        self.multiplicativeIdentity = field.multiplicativeIdentity
        self.table = Table(table)
        self.Uexecuted = False
            
    def nomalizeRow(rowIdx, firstNonZeroColIdx):
        fe = self.table.index(rowIdx, firstNonZeroColIdx)#fieldElement
        newRow = [self.table.index(rowIdx, colIdx) for  colIdx in range(0, firstNonZeroColIdx)]
        for colIdx in range(firstNonZeroColIdx+1, self.table.colLen):
            ne = self.divide(self.table.index(rowIdx, colIdx), fe)
            newRow.append(ne)
            
    def rowSubtraction(row0Idx, row1Idx, startColIdx):
        newRow = [self.additiveIdentity] * (startColIdx+1)#assume we count from 0
        for colIdx in range(startColIdx, self.table.colLen):
            ne = self.sub(self.table.index(row0Idx, colIdx), self.table.index(row1Idx, colIdx))# might be negative
            newRow.append(ne)
            
    def makeU(self):
        for colIdx in range(0, min(self.table.colLen, self.table.rowLen)):#rowLen>colLen
            newRow = self.normalizeRow(colIdx, colIdx)
            self.table.replace(colIdx, newRow) #needs to be inplace
            for rowIdx in range(colIdx+1, seld.table.rowLen):
                subRow = self.rowSubtraction(colIdx, rowIdx, colIdx)
                self.table.replace(subRow, rowId)
        self.Uexecuted = False
        
    def makeL(self):
        if not self.Uexecuted:
            raise Exception("did not makeU first")
        for row0Idx in range(min(self.table.colLen, self.table.rowLen), 0):
            for row1Idx in range(row0Idx-1, 0):
                subRow = self.rowSubtraction(row0Idx, row1Idx, row0Idx)
                self.table.replace(subRow, row1Idx)
                
    def solve(self):
        self.makeL()
        return self.table.lol
        
        
        

