from foundation.automat.common.binarysearch import BinarySearch

class PriorityQueue:#UNIT_TEST<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO

    def __init__(self):
        self.sortedList = []

    def insert(self, item, priority):
        tuple_priority_item = (priority, item)
        insertIdx = BinarySearch.binarySearchPre(self.sortedList, priority, key=lambda t: t[0])
        self.sortedList.insert(insertIdx, tuple_priority_item)

    def popMax(self):
        tuple_priority_item = self.sortedList.pop()
        return tuple_priority_item[1]


    def popMaxWithPriority(self):
        tuple_priority_item = self.sortedList.pop()
        return tuple_priority_item

    def popMin(self):
        tuple_priority_item = self.sortedList.pop(0)
        return tuple_priority_item[1]

    def __len__(self):
        return len(self.sortedList)

    def __str__(self):
        return str(self.sortedList)