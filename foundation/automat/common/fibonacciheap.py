import math

class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.mark = False
        self.left = self
        self.right = self

class FibonacciHeap:
    """
    Courtesy of https://www.geeksforgeeks.org/fibonacci-heap-in-python/
    """
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0
        self.node_map = {}

    def isEmpty(self):
        return self.min_node is None

    def insert(self, key):
        self.node_map[key] = True
        node = FibonacciHeapNode(key)
        if self.min_node is None:
            self.min_node = node
        else:
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right = node
            node.right.left = node
            if node.key < self.min_node.key:
                self.min_node = node
        self.num_nodes += 1
        return node

    def minimum(self):
        if self.min_node is None:
            return None
        return self.min_node.key

    def merge(self, other_heap):
        if self.min_node is None:
            self.min_node = other_heap.min_node
        elif other_heap.min_node is not None:
            self.min_node.right.left = other_heap.min_node.left
            other_heap.min_node.left.right = self.min_node.right
            self.min_node.right = other_heap.min_node
            other_heap.min_node.left = self.min_node
            if other_heap.min_node.key < self.min_node.key:
                self.min_node = other_heap.min_node
        self.num_nodes += other_heap.num_nodes

        self.node_map.update(other_heap.node_map)

    def _removeFromRootList(self, node):
        if node == node.right:
            self.min_node = None
        else:
            node.left.right = node.right
            node.right.left = node.left
            if node == self.min_node:
                self.min_node = node.right
        del self.node_map[node.key]

    def _link(self, node1, node2):
        self._remove_from_root_list(node2)
        node2.left = node2.right = node2
        node2.parent = node1
        if node1.child is None:
            node1.child = node2
        else:
            node2.left = node1.child
            node2.right = node1.child.right
            node1.child.right = node2
            node2.right.left = node2
        node1.degree += 1
        node2.mark = False

    def _consolidate(self):
        max_degree = math.ceil(math.log(self.num_nodes, 2))
        degree_table = [None] * (max_degree + 1)
        current = self.min_node
        while True:
            degree = current.degree
            next_node = current.right
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if current.key > other.key:
                    current, other = other, current
                self._link(current, other)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = current
            if next_node == self.min_node:
                break
            current = next_node

        self.min_node = None
        for node in degree_table:
            if node is not None:
                if self.min_node is None:
                    self.min_node = node
                else:
                    node.left.right = node.right
                    node.right.left = node.left
                    node.left = self.min_node
                    node.right = self.min_node.right
                    self.min_node.right = node
                    node.right.left = node
                    if node.key < self.min_node.key:
                        self.min_node = node

    def extractMin(self):
        min_node = self.min_node
        if min_node is not None:
            if min_node.child is not None:
                children = [child for child in self._iterate(min_node.child)]
                for child in children:
                    child.parent = None
                    self.min_node.left.right = child
                    child.left = self.min_node.left
                    child.right = self.min_node
                    self.min_node.left = child
                    if child.key < self.min_node.key:
                        self.min_node = child
            self._remove_from_root_list(min_node)
            if min_node == min_node.right:
                self.min_node = None
            else:
                self.min_node = min_node.right
                self._consolidate()
            self.num_nodes -= 1
        del self.node_map[min_node.key]
        return min_node

    def _cut(self, node, parent):
        if node == node.right:
            parent.child = None
        else:
            node.left.right = node.right
            node.right.left = node.left
            if node == parent.child:
                parent.child = node.right
        parent.degree -= 1
        self.min_node.left.right = node
        node.left = self.min_node.left
        node.right = self.min_node
        self.min_node.left = node
        node.parent = None
        node.mark = False
        del self.node_map[node.key]

    def _cascadeCut(self, node):
        parent = node.parent
        if parent is not None:
            if not node.mark:
                node.mark = True
            else:
                self._cut(node, parent)
                self._cascadeCut(parent)

    def decreaseKey(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than current key.")
        node.key = new_key
        parent = node.parent
        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascadeCut(parent)
        if node.key < self.min_node.key:
            self.min_node = node

    def delete(self, node):
        self.decreaseKey(node, float('-inf'))
        self.extractMin()

    def _iterate(self, node):
        while True:
            yield node
            if node.child is not None:
                for n in self._iterate(node.child):
                    yield n
            node = node.right
            if node == self.min_node:
                break

    def contain(self, key):
        return key in self.node_map


#TODO a seperate test file and testing
# Example Usage
heap = FibonacciHeap()
node1 = heap.insert(3)
node2 = heap.insert(5)
node3 = heap.insert(1)
node4 = heap.insert(9)
node5 = heap.insert(7)

print("Minimum Key:", heap.minimum())  # Output: 1

heap.decreaseKey(node5, 2)
print("New Minimum Key after Decrease Key:", heap.minimum())  # Output: 1

print("Extracted Minimum Key:", heap.extractMin().key)  # Output: 1
print("Minimum Key after Extract Min:", heap.minimum())  # Output: 2