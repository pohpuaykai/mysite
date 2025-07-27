from math import ceil

from foundation.automat.common.spanningtree import SpanningTree

class RCCLOrthogonalLayout:
    """
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
component|source_components should be origin of URDL
if component is leaf_of_st, then add an artificialNode to extend the component
if there are components on same XY as the URDL, then choose the bent instead of the recurring_straight
if component, then the next placement should be a line, example
    when placing origin, if origin is a component, we should try to make UD and LR first (so that component is on a wire, not in a corner)
    when placing component, 
        if component is U or D of parent, then the next node should be U or D. 
        if component is R or L of parent, then the next node should be R or L.

wire should connect to centre of SVGComponent's x or y
SVGComponent should be rotated to the correct orientation
last SVGComponent of either x or y, should use end of x or y instead of start
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Overview 
we take a undirectedGraph G which comes from an electrical circuit, and try to draw an SVG (a xy-coordinate for each node) on a xy-farplane with G.
0. Use a graph with wires, wire nodes are artificialNodes? WIRE MUST HAVE BOUNDINGBOX<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Make a MinimumSpanningTree mst of G, T (and R are the removed_edges from G), where the weights are smaller for nodes with more neighbours #[TODO MANY optimisations can be made to the assignment to make schematics look pretty, reduce crossing_number]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
2. We try to fit T into a square_grid, that only has unit_xy-coordinates, and by assigning a string of U=(+1 in y-axis); R=(+1 in x-axis); D=(-1 in y-axis); L=(-1 in x-axis) [we call this unit_xy-coordinates]
  0. Take the node with most neighbours in T, r
  1. Split up r, if r has more than 4 neighbours, try to make the split even. let number of neighbours of r be m
    0. add k = floor(m/4) artificial_nodes, by grouping existing neighbours of r in k groups. [TODO MANY optimisations can be made to the grouping to make the schematics look pretty, reduce crossing_number]
    1. for each k artificial_nodes, add an item to T, where the key is the artificial_node, and the neighbours are the members of its group
  2. BFS T, split up nodes t that has more than 2 neighbours, let n be number of neighbours of t
    0. add k = floor(n/2) artificial_nodes, by grouping existing neighbours of t in k groups. [TODO MANY optimisations can be made to the grouping to make the schematics look pretty, reduce crossing_number]
    1. for each k artificial_nodes, add an item to T, where the key is the artificial_node, and the neighbours are the members of its group
  3. Assign U, R, D, L to the neighbours of r [TODO MANY optimisations can be made to the assignment to make schematics look pretty, reduce crossing_number]
  4. Look for nodes that lead to paths that end in deg1 nodes
    0. go through T.items(), find all keys whose len(neighbours)=1: S
    1. for each node s in S, keep getting its parent, until its parent has more than 2 neighbours, then record s -> XX_X
  5. BFS T, for each node n, if parent of n: (ignore r) (check every node has at most 3 neighbours), only assign neighbour that has no assignment (might be parent.)
    0 . if XX, assign neighbour to X
    1 . if _UR, 
      0. if neighbour in XX_X, assign R
      1. else assign U
    2 . if _RU, 
      0. if neighbour in XX_X, assign U
      1. else assign R
    3 . if _RD, 
      0. if neighbour in XX_X, assign D
      1. else assign R
    4 . if _DR, 
      0. if neighbour in XX_X, assign R
      1. else assign D
    5 . if _DL, 
      0. if neighbour in XX_X, assign L
      1. else assign D
    6 . if _LD, 
      0. if neighbour in XX_X, assign D
      1. else assign L
    7 . if _LU, 
      0. if neighbour in XX_X, assign U
      1. else assign L
    8 . if _UL, 
      0. if neighbour in XX_X, assign L
      1. else assign U
    9 . if U, 
      0. assign any neighbours in XX_X -> U
      1. assign any neighbours NOT in XX_X -> R
    10. if R,
      0. assign any neighbours in XX_X -> R
      1. assign any neighbours NOT in XX_X -> D
    11. if D, 
      0. assign any neighbours in XX_X -> D
      1. assign any neighbours NOT in XX_X -> L
    12. if L, 
      0. assign any neighbours in XX_X -> L
      1. assign any neighbours NOT in XX_X -> U
3. Convert all the unit_xy-coordinate of each node to numeric_unit_xy-coordinate
  0. every U becomes +1 in y
  1. every R becomes +1 in x
  2. every D becomes -1 in y
  3. every L becomes -1 in x
4. Add a artificial_node for each edge e in R, if each coordinate in unit_xy-coordinate of each node n of e are different in their coordinates, add e (with the artificial_node, with its unit_xy-coordinate) to T
  0. for e=(A,B) in R
    0. if Ax!=Bx & Ay!=By: 
      0. add numeric_xy-coordinate(v) = (Ax, By) to T, neighbours(v)=[A, B] [TODO MANY optimisations can be done here, we can choose to select (Bx, Ay) and it might lead to lesser crossings] 
    1. else directly connect A and B in T
      0. add A to neighbours(B)
      1. add B to neighbours(A)
5. Convert the numeric_unit_xy-coordinate of each node to actual distance by providing enough distance between component symbols
  0. Center all the numeric_unit_xy-coordinate by moving the bottom-left to (0.0, 0.0)
  1. Tag all x_coordinate to its nodeId, Tag all y_coordinate to its nodeId
  2. Sort all x_coordinate in increasing order
    0. For each x_coordinate, get its nodeId, and type, and boundingBox(default for artificialNode).
    1. To that x_coordinate, add previous_added_amount, boundingBox.width, wire width
      0. Store the new_end_coordinates (get associated y) of node, and new_start_coordinates (get associated y) of node (for adding wire positions)
  3. Sort all y_coordinate in increasing order
    0. For each y_coordinate, get its nodeId, and type, and boundingBox(default for artificialNode).
    1. To that y_coordinate, add previous_added_amount, boundingBox.height, wire height
      0. Store the new_end_coordinates (get associated x) of node, and new_start_coordiantes (get associated x) of node (for adding wire positions)
  4. Collate all the x_coordinate & y_coordinate back to xy_coordinate, key is nodeId
    """

    def __init__(self, g, id__type, type__boundingBox, artificialNodeHeight, artificialNodeWidth, xSpacingBetweenComponent, ySpacingBetweenComponent):
        """
        g should not contain any wires

        type__boundingBox, dictionary from componentType to its SVG boundingBox, which contains actual height and actual width when placed on SVG
        """
        # print('g******************************************')
        # print(g)
        # print('id__type***********************************')
        # print(id__type)
        self.g = g; self.id__type=id__type; self.type__boundingBox = type__boundingBox; 
        if 'wire' not in self.type__boundingBox:
            self.type__boundingBox['wire'] = {'width':artificialNodeWidth, 'height':artificialNodeHeight}
        self.artificialNodeHeight = artificialNodeHeight; self.artificialNodeWidth = artificialNodeWidth;
        self.xSpacingBetweenComponent = xSpacingBetweenComponent; self.ySpacingBetweenComponent = ySpacingBetweenComponent

    def makeSchematics(self, svg=False):
        self.svg = svg
        #get maxIdx of all nodes
        self.maxNodeIdx = max(self.g.keys()) + 1
        self.nodeId__unitXYCoordinateString = {}
        self.XX_X = []
        self.nodeId__numericXYCoordinateTuple = {}
        self._makeSpanningTree()
        # print('completed makeSpanningTree: ', self.T, self.R)
        self._fitIntoSquareGrid()
        self._convertUnitToNumericCoordinate()
        self._addRemovedEdgesBack()
        self.nodeId__inflatedNumericStartCoordinateTuple = {}; # we are not keeping the end_xy_coordinate because boundingBox has height&width
        self.list_wireStartCoordinateEndCoordinateTuple = []
        self.svgStr = None
        self._convertToActualSVGDistance()
        if self.svg:
            return self.nodeId__inflatedNumericStartCoordinateTuple, self.list_wireStartCoordinateEndCoordinateTuple, self.svgStr
        else:
            return self.nodeId__inflatedNumericStartCoordinateTuple, self.list_wireStartCoordinateEndCoordinateTuple

    def _makeSpanningTree(self):
        #
        # vertexIterable = []; edgeIterableSortable = []
        # for parent, neighbours in self.g.items():
        #     vertexIterable.append(parent)
        #     for neighbour in neighbours:
        #       edgeIterableSortable.append((parent, neighbour))
        # nodeId__noOfNeighbours = dict(map(lambda t: (t[0], len(t[1])), self.g.items()))
        # maxNoOfNeigbours = max(map(lambda t: t[1], nodeId__noOfNeighbours.items()))
        # edgeWeight = {}#[TODO MANY optimisations can be made to the assignment to make schematics look pretty, reduce crossing_number]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # for edge in edgeIterableSortable:
        #     eW = 2*maxNoOfNeigbours - (nodeId__noOfNeighbours[edge[0]]+nodeId__noOfNeighbours[edge[1]])#least_number_of_neighbour nodes get picked first
        #     edgeWeight[edge] = eW
        # self.T, self.R = SpanningTree.minimumSpanningTreeKruskal(vertexIterable, edgeIterableSortable, edgeWeight)
        # print('self.T', self.T)
        # print('self.R', self.R)
        #
        #try BFS
        startNode = None; maxNoOfNeigbours = -1
        for parent, neighbours in filter(lambda t: self.id__type[t[0]] in ['battery', 'AC_signal_generator'], self.g.items()):
            noOfNeighbours = len(neighbours)
            if noOfNeighbours > maxNoOfNeigbours:
                maxNoOfNeigbours = noOfNeighbours; startNode = parent
        self.T, self.R = SpanningTree.undirectedSpanningTreeDBFSSearchUndirectedGraph(self.g, startNode=startNode, breadthFirst=True)
        # print('self.T', self.T)
        # print('self.R', self.R)

    def _fitIntoSquareGrid(self):
        #0. Take the node with (is a component not a wire) and (preferably a source_component) and (most neighbours in T), r
        self.r = None; maxNoOfNeigbours = -1
        for parent, neighbours in filter(lambda t: self.id__type[t[0]] in ['battery', 'AC_signal_generator'], self.T.items()):
            noOfNeighbours = len(neighbours)
            if noOfNeighbours > maxNoOfNeigbours:
                maxNoOfNeigbours = noOfNeighbours; self.r = parent


        #1. Split up r, if r has more than 4 neighbours, try to make the split even. let number of neighbours of r be m [TODO MANY optimisations can be made to the grouping to make the schematics look pretty, reduce crossing_number] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        if len(self.T[self.r]) > 4:
            splitTuple = self.getSplitTuple(len(self.T[self.r]), 4); beginningIdx = 0; addedArtificialNodes = []
            for noOfMembers in splitTuple:
                artificialNode = self.getArtificialNodeIdx(); addedArtificialNodes.append(artificialNode)
                self.T[artificialNode] = self.T[self.r][beginningIdx:noOfMembers]
                beginningIdx += noOfMembers
            self.T[self.r] = addedArtificialNodes
            # print('r splitTuple:', splitTuple);print('augmented self.T', self.T)
        #2. BFS T, split up nodes t that has more than 2 neighbours, let n be number of neighbours of t [TODO MANY optimisations can be made to the grouping to make the schematics look pretty, reduce crossing_number] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        queue = [self.r]; visited = [self.r]
        while len(queue) > 0:
            current = queue.pop(0)#BFS
            #split here
            if current != self.r and len(self.T[current]) > 3:# we do not count the backwardNeighbour
                splitTuple = self.getSplitTuple(len(self.T[current]), 2); beginningIdx = 0; addedArtificialNodes = []
                
                for noOfMembers in splitTuple:
                    artificialNode = self.getArtificialNodeIdx(); addedArtificialNodes.append(artificialNode)
                    # import pdb;pdb.set_trace()
                    self.T[artificialNode] = self.T[current][beginningIdx:beginningIdx+noOfMembers]
                    beginningIdx += noOfMembers
                self.T[current] = addedArtificialNodes
                # print("queue", queue, 'splitTuple: ', splitTuple); import pdb;pdb.set_trace()
            #
            for neighbour in self.T[current]:
                if neighbour not in visited:
                    queue.append(neighbour); visited.append(neighbour)

        #?. If spanningTree ends in a component, add an artificialNode between componentNode(leaf) and removed_edge
        # print(list(filter(lambda nodeId: len(self.T[nodeId])==1 and self.id__type[nodeId]!='wire', self.g.keys())), '<<<<<')
        for nodeId in filter(lambda nodeId: len(self.T[nodeId])==1 and self.id__type[nodeId]!='wire', self.g.keys()): #g.keys will contain all the nodeId, since g is undirected
            #nodeId not in self.T is a leaf
            #find all removed_edges containing nodeId, add an artificialNode for each removed_edges, so that the component will not be at the edge of the schematic
            R___new = []; visited_directed_edge = []
            for removed_edge in self.R:
                if removed_edge in visited_directed_edge:
                    continue
                else:
                    visited_directed_edge.append(removed_edge); visited_directed_edge.append((removed_edge[1], removed_edge[0]))
                # print(removed_edge, ' ', nodeId, ' in ', removed_edge, ' ', nodeId in removed_edge)
                if nodeId in removed_edge:
                    otherNodeId = removed_edge[abs(1-removed_edge.index(nodeId))]
                    artificialNode = self.getArtificialNodeIdx();
                    R___new.append((otherNodeId, artificialNode)) # other direction not added
                    existing = self.T.get(nodeId, [])
                    existing.append(artificialNode)
                    self.T[nodeId] = existing
                    self.T[artificialNode] = [nodeId] # backward connection for undirected
                else:
                    R___new.append(removed_edge)
            self.R = R___new

        # print('EndsInComponentExtended:')
        # print('self.T', self.T)
        # print('self.R', self.R)



        #3. Assign U, R, D, L to the neighbours of r [TODO MANY optimisations can be made to the assignment to make schematics look pretty, reduce crossing_number]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        if self.id__type[self.r] == 'wire':#prefer bent
            self.nodeId__unitXYCoordinateString.update(dict(zip(self.T[self.r], ['U', 'R', 'D', 'L'])))#This UDLR arrangement ensures that UD and LR are assigned together, resulting in a straightline through the first node r if it is a non-wire, TODO could be better optimised
        
        else:
            self.nodeId__unitXYCoordinateString.update(dict(zip(self.T[self.r], ['U', 'D', 'L', 'R'])))#This UDLR arrangement ensures that UD and LR are assigned together, resulting in a straightline through the first node r if it is a non-wire, TODO could be better optimised
        
        # print('nodeId__unitXYCoordinateString', self.nodeId__unitXYCoordinateString); print('self.r', self.r)
        # #4. Look for nodes that lead to paths that end in deg1 nodes, and place then preferably in a straightline. ( not needed)
        # leafIds = []
        for nodeId, neighbours in self.T.items():
            if len(neighbours) == 1:
                #go 'up' the tree, until we meet deg>2 parent
                parent = nodeId; visited = [nodeId];
                while len(self.T[parent]) ==2:
                    one, two = self.T[parent]
                    if one in visited and two in visited:
                        parent = None
                        break # cannot find any deg>2 'parent'
                    elif one in visited: # 'parent' is two
                        parent = two; visited.append(two)
                    elif two in visited: # 'parent' is one
                        parent = one; visited.append(one)
                if parent is not None:
                    self.XX_X.append(parent)
        
        #
        #5. BFS T, for each node n, if parent of n: (ignore r) (check every node has at most 3 neighbours), only assign neighbour that has no assignment (might be parent.)
        # queue = [r]; visited = [r]
        # print('splited self.T', self.T)
        queue = list(self.T[self.r]); visited = [self.r] + list(self.T[self.r])
        while len(queue) > 0:
            # print('queue: ', queue)
            current = queue.pop(0)#BFS
            #
            current___unitXYCoordinateString = self.nodeId__unitXYCoordinateString[current]#ignore r
            #
            for neighbourIdx, neighbour in enumerate(self.T[current]):
                if neighbour not in visited:
                    # print('current: ', current, ' neighbour: ', neighbour); import pdb;pdb.set_trace()
                    #assign
                    #this doesn't work, branch with many componentNodes will overlap
                    # if neighbour in self.id__type and self.id__type[neighbour] != 'wire':
                    #     self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString[-1]#continue the parent path to ensure straightline for component

                    if len(current___unitXYCoordinateString) >= 2 and current___unitXYCoordinateString[-1] == current___unitXYCoordinateString[-2]:
                        #0 . if XX, assign neighbour to X
                        self.nodeId__unitXYCoordinateString[neighbour] = (current___unitXYCoordinateString+current___unitXYCoordinateString[-1])
                    elif current___unitXYCoordinateString.endswith('UR'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('U')): # needs to check that other neighbour does not end with R
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('U'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'

                    elif current___unitXYCoordinateString.endswith('RU'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('R')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('R'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                    elif current___unitXYCoordinateString.endswith('RD'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('R')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('R'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                    elif current___unitXYCoordinateString.endswith('DR'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('D')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('D'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                    elif current___unitXYCoordinateString.endswith('DL'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('D')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('D'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                    elif current___unitXYCoordinateString.endswith('LD'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('L')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('L'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                    elif current___unitXYCoordinateString.endswith('LU'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('L')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('L'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                    elif current___unitXYCoordinateString.endswith('UL'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('U')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('U'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                    elif current___unitXYCoordinateString.endswith('U'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('R')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('R'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                    elif current___unitXYCoordinateString.endswith('R'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('D')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('D'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                    elif current___unitXYCoordinateString.endswith('D'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('L')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('L'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                    elif current___unitXYCoordinateString.endswith('L'):
                        #
                        if neighbour in self.XX_X or (self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('U')):
                        # if self.nodeId__unitXYCoordinateString.get(self.T[current][abs(1-neighbourIdx)], '').endswith('U'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                    #
                    if neighbour in self.id__type and self.id__type[neighbour] == 'wire': # bend if its a wireNode
                        if current___unitXYCoordinateString.endswith('U'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                        elif current___unitXYCoordinateString.endswith('R'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'

                        elif current___unitXYCoordinateString.endswith('D'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'

                        elif current___unitXYCoordinateString.endswith('L'):
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                    queue.append(neighbour); visited.append(neighbour)
        print('self.nodeId__unitXYCoordinateString****************************************************************')
        print(self.nodeId__unitXYCoordinateString)

    def _convertUnitToNumericCoordinate(self):
        # 0. every U becomes +1 in y
        # 1. every R becomes +1 in x
        # 2. every D becomes -1 in y
        # 3. every L becomes -1 in x
        self.nodeId__numericXYCoordinateTuple[self.r] = (0, 0)
        for nodeId, unitXYCoordinateString in self.nodeId__unitXYCoordinateString.items():
            U = unitXYCoordinateString.count('U'); R = unitXYCoordinateString.count('R');
            D = unitXYCoordinateString.count('D'); L = unitXYCoordinateString.count('L');
            self.nodeId__numericXYCoordinateTuple[nodeId] = (R-L, U-D)
        print('self.nodeId__numericXYCoordinateTuple***************************_convertUnitToNumericCoordinate***********************************')
        print(self.nodeId__numericXYCoordinateTuple)

    def _addRemovedEdgesBack(self):
        alreadyAdded = set()#R may contain both direction of the edge, we only need one
        for (A, B) in self.R:#A, B are nodeIds, 
            # print('adding back: ', (A, B))
            if (A, B) not in alreadyAdded and A != self.r and B != self.r:
                A___nc = self.nodeId__numericXYCoordinateTuple[A]; B___nc = self.nodeId__numericXYCoordinateTuple[B]
                # print('A___nc', A___nc); print('B___nc', B___nc)
                if A___nc[0] != B___nc[0] and A___nc[1] != B___nc[1]: #A and B are diagonal to each other
                    artificialNode = self.getArtificialNodeIdx()
                    self.T[artificialNode] = [A, B]
                    # there are 2 possible places to put the artificialNode because A and B are diagonal to each other
                    onePossiblePlacement = (A___nc[0], B___nc[1])
                    # import pdb;pdb.set_trace()
                    if onePossiblePlacement in self.nodeId__numericXYCoordinateTuple.values(): # onePossiblePlacement collide with existing node
                        onePossiblePlacement = (B___nc[0], A___nc[1])
                    else:
                        #check which onePossiblePlacement overlap with most nodes, and take the one with lesser collision, when connection is made
                        otherPossiblePlacement = (B___nc[0], A___nc[1]); onePossiblePlacementCollisionCount = 0; otherPossiblePlacementCollisionCount = 0;
                        for _, nC in self.nodeId__numericXYCoordinateTuple.items():
                            if nC[0] == onePossiblePlacement[0] or nC[1] == onePossiblePlacement[1]:
                                onePossiblePlacementCollisionCount += 1
                            if nC[0] == otherPossiblePlacement[0] or nC[1] == otherPossiblePlacement[1]:
                                otherPossiblePlacementCollisionCount += 1
                        if otherPossiblePlacementCollisionCount < onePossiblePlacementCollisionCount:
                            onePossiblePlacement = otherPossiblePlacement
                    self.nodeId__numericXYCoordinateTuple[artificialNode] = onePossiblePlacement
                    # print('got artificialNode: ', artificialNode, ' coordinate: ', onePossiblePlacement)
                else:
                    self.T[A].append(B); self.T[B].append(A)#its inplace... right?
                alreadyAdded.add((A, B)); alreadyAdded.add((B, A))
        print('self.nodeId__numericXYCoordinateTuple******************************_addRemovedEdgesBack********************************')
        print(self.nodeId__numericXYCoordinateTuple)
        print('self.T', self.T)

    def _convertToActualSVGDistance(self):
        """
5. Convert the numeric_unit_xy-coordinate of each node to actual distance by providing enough distance between component symbols
  0. Center all the numeric_unit_xy-coordinate by moving the bottom-left to (0.0, 0.0)
  1. Tag all x_coordinate to its nodeId, Tag all y_coordinate to its nodeId
  2. Sort all x_coordinate in increasing order
    0. For each x_coordinate, get its nodeId, and type, and boundingBox(default for artificialNode).
    1. To that x_coordinate, add previous_added_amount, boundingBox.width, wire width
      0. Store the new_end_coordinates (get associated y) of node, and new_start_coordinates (get associated y) of node (for adding wire positions)
  3. Sort all y_coordinate in increasing order
    0. For each y_coordinate, get its nodeId, and type, and boundingBox(default for artificialNode).
    1. To that y_coordinate, add previous_added_amount, boundingBox.height, wire height
      0. Store the new_end_coordinates (get associated x) of node, and new_start_coordiantes (get associated x) of node (for adding wire positions)
  4. Collate all the x_coordinate & y_coordinate back to xy_coordinate, key is nodeId
        """
        print('_convertToActualSVGDistance________________________________________________________________________________________')
        minX = min(map(lambda t: t[1][0], self.nodeId__numericXYCoordinateTuple.items())) 
        minY = min(map(lambda t: t[1][1], self.nodeId__numericXYCoordinateTuple.items()))
        xCoordinate__list_nodeId = {}; nodeId__xCoordinate = {}; yCoordinate__list_nodeId = {}; nodeId__yCoordinate = {};
        for nodeId, (xCoordinate, yCoordinate) in self.nodeId__numericXYCoordinateTuple.items():
            xCoordinate -= minX; yCoordinate -= minY
            existing = xCoordinate__list_nodeId.get(xCoordinate, [])
            existing.append(nodeId)
            xCoordinate__list_nodeId[xCoordinate] = existing

            nodeId__xCoordinate[nodeId] = xCoordinate
            existing = yCoordinate__list_nodeId.get(yCoordinate, [])
            existing.append(nodeId)
            yCoordinate__list_nodeId[yCoordinate] = existing

            nodeId__yCoordinate[nodeId] = yCoordinate

        print('xCoordinate__list_nodeId', xCoordinate__list_nodeId)#OK
        print('yCoordinate__list_nodeId', yCoordinate__list_nodeId)#OK
        #? is each component vertical or horizontal
        def verticalOrHorizontal(nodeId):
            nodeCoordinate = self.nodeId__numericXYCoordinateTuple[nodeId]; verticalCount = 0; horizontalCount = 0;
            for neighbourId in self.T[nodeId]:
                neighbourCoordinate = self.nodeId__numericXYCoordinateTuple[neighbourId]
                if abs(neighbourCoordinate[0]-nodeCoordinate[0]) == 0:#neighbour is vertical to nodeId
                    verticalCount +=1
                else:# neighbour is horizontal to nodeId
                    horizontalCount += 1
            if verticalCount == horizontalCount:
                raise Exception()
            if verticalCount > horizontalCount:
                return 'v'
            else:
                return 'h'

        self.nodeId__verticalOrHorizontal = {}
        for nodeId in filter(lambda nodeId: self.id__type[nodeId] != 'wire', self.g.keys()):
            self.nodeId__verticalOrHorizontal[nodeId] = verticalOrHorizontal(nodeId)

        #2
        nodeId__startEndXCoordinateTuple = {}; 
        previousAddedAmount = 0;
        for idx, xCoordinate in enumerate(sorted(list(xCoordinate__list_nodeId.keys()))):
            maxXSize = 0
            for nodeId in xCoordinate__list_nodeId[xCoordinate]:
                type = self.id__type.get(nodeId, 'artificial')
                boundingBox = self.type__boundingBox.get(type, {'height':self.artificialNodeHeight, 'width':self.artificialNodeWidth})
                #CHECK for rotation here, we assume everything is horizontal, so if self.nodeId__verticalOrHorizontal=='v', then we need to rotate 90degrees
                if self.nodeId__verticalOrHorizontal.get(nodeId, 'h') == 'v':
                    width = boundingBox['height']
                else:
                    width = boundingBox['width']
                # startXCoordinate = previousAddedAmount + xCoordinate; endXCoordinate = previousAddedAmount + xCoordinate + width#what do you add the xCoordinate for? that is the unitCoordinate not absoluteCoordinate<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                startXCoordinate = previousAddedAmount; endXCoordinate = previousAddedAmount + width#what do you add the xCoordinate for? that is the unitCoordinate not absoluteCoordinate<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                
                nodeId__startEndXCoordinateTuple[nodeId] = (startXCoordinate, endXCoordinate)
                maxXSize = max(maxXSize, width)
            # previousAddedAmount += maxXSize + self.xSpacingBetweenComponent
            previousAddedAmount += maxXSize + self.xSpacingBetweenComponent
        print('nodeId__startEndXCoordinateTuple', nodeId__startEndXCoordinateTuple)

        #3
        nodeId__startEndYCoordinateTuple = {}
        previousAddedAmount = 0;
        for idx, yCoordinate in enumerate(sorted(list(yCoordinate__list_nodeId.keys()))):
            maxYSize = 0
            for nodeId in yCoordinate__list_nodeId[yCoordinate]:
                type = self.id__type.get(nodeId, 'artificial')
                boundingBox = self.type__boundingBox.get(type, {'height':self.artificialNodeHeight, 'width':self.artificialNodeWidth})
                #CHECK for rotation here, we assume everything is horizontal, so if self.nodeId__verticalOrHorizontal=='v', then we need to rotate 90degrees
                if self.nodeId__verticalOrHorizontal.get(nodeId, 'h') == 'v':
                    height = boundingBox['width']
                else:
                    height = boundingBox['height']
                # startYCoordinate = previousAddedAmount + yCoordinate; endYCoordinate = previousAddedAmount + yCoordinate + height#what do you add the yCoordinate for? that is the unitCoordinate not absoluteCoordinate<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                startYCoordinate = previousAddedAmount; endYCoordinate = previousAddedAmount + height#what do you add the yCoordinate for? that is the unitCoordinate not absoluteCoordinate<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                nodeId__startEndYCoordinateTuple[nodeId] = (startYCoordinate, endYCoordinate)
                maxYSize = max(maxYSize, height)
            print('previousAddedAmount', previousAddedAmount)
            # previousAddedAmount += maxYSize + self.ySpacingBetweenComponent
            previousAddedAmount += maxYSize + self.ySpacingBetweenComponent
            print('previousAddedAmountNEW:', previousAddedAmount, 'maxYSize', maxYSize, 'self.ySpacingBetweenComponent', self.ySpacingBetweenComponent, 'sum', maxYSize + self.ySpacingBetweenComponent); import pdb;pdb.set_trace()
        print('nodeId__startEndYCoordinateTuple', nodeId__startEndYCoordinateTuple)

        #4 for translation
        for nodeId in self.nodeId__numericXYCoordinateTuple.keys():
            (startXCoordinate, endXCoordinate) = nodeId__startEndXCoordinateTuple[nodeId]
            (startYCoordinate, endYCoordinate) = nodeId__startEndYCoordinateTuple[nodeId]
            #CHECK for rotation here, we assume everything is horizontal, so if self.nodeId__verticalOrHorizontal=='v', then we need to rotate 90degrees
            # if self.nodeId__verticalOrHorizontal.get(nodeId, 'h') == 'v':#rotate within self<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            #     coordinate = (startYCoordinate, startXCoordinate)
            # else:
            #     coordinate = (startXCoordinate, startYCoordinate)
            self.nodeId__inflatedNumericStartCoordinateTuple[nodeId] = (startXCoordinate, startYCoordinate)

        print('JUST before adding SVGWire****************************************************')
        print('self.T', self.T)
        print('nodeId__startEndXCoordinateTuple', nodeId__startEndXCoordinateTuple)
        print('nodeId__startEndYCoordinateTuple', nodeId__startEndYCoordinateTuple)
        print('self.nodeId__numericXYCoordinateTuple', self.nodeId__numericXYCoordinateTuple) # for determining UDLR

        addedEdges = set() # check for both directions, we only need to add once
        for nodeId, neighbours in self.T.items():
            (startXCoordinate, endXCoordinate) = nodeId__startEndXCoordinateTuple[nodeId]
            (startYCoordinate, endYCoordinate) = nodeId__startEndYCoordinateTuple[nodeId]
            (startXUnit, startYUnit) = self.nodeId__numericXYCoordinateTuple[nodeId]
            print('nId:', nodeId, 'X: ', (startXCoordinate, endXCoordinate), ' Y: ', (startYCoordinate, endYCoordinate))
            # startXYCoordinate = (endXCoordinate, endYCoordinate)
            for neighbour in neighbours: # only take the leftToRight downToUp direction<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                if (nodeId, neighbour) not in addedEdges:
                    (nstartXCoordinate, nendXCoordinate) = nodeId__startEndXCoordinateTuple[neighbour]
                    (nstartYCoordinate, nendYCoordinate) = nodeId__startEndYCoordinateTuple[neighbour]
                    (endXUnit, endYUnit) = self.nodeId__numericXYCoordinateTuple[neighbour]
                    if startXUnit != endXUnit and startYUnit != endYUnit:
                        raise Exception(f'nodes {nodeId} and {neighbour} are not orthogonal!')
                    elif startXUnit == endXUnit:#downToUp
                        if startYUnit > endYUnit: # nodeId is up, neighbour is down
                            startXYCoordinate = (min(nendXCoordinate, startXCoordinate),nendYCoordinate); endXYCoordinate = (min(nendXCoordinate, startXCoordinate),startYCoordinate);
                            # if (self.id__type.get(nodeId, 'artificial') not in ['artificial', 'wire']) or (self.id__type.get(neighbour, 'artificial') not in ['artificial', 'wire']):
                            #     #center the X coordinate, since either nodeId or neighbour is a component
                            #     startXYCoordinate = ((nendXCoordinate+startXCoordinate)/2, nendYCoordinate); endXYCoordinate = ((nendXCoordinate+startXCoordinate)/2, startYCoordinate)
                        else: # nodeId is down, neighbour is up
                            startXYCoordinate = (min(endXCoordinate, nstartXCoordinate),endYCoordinate); endXYCoordinate = (min(endXCoordinate, nstartXCoordinate),nstartYCoordinate);
                            # if (self.id__type.get(nodeId, 'artificial') not in ['artificial', 'wire']) or (self.id__type.get(neighbour, 'artificial') not in ['artificial', 'wire']):
                            #     #center the X coordinate, since either nodeId or neighbour is a component
                            #     startXYCoordinate = ((endXCoordinate+nstartXCoordinate)/2, endYCoordinate); endXYCoordinate = ((endXCoordinate+nstartXCoordinate)/2, nstartYCoordinate)

                    elif startYUnit == endYUnit:#leftToRight
                        if startXUnit > endXUnit: # nodeId is right, neighbour is left
                            startXYCoordinate = (nendXCoordinate,min(nendYCoordinate, startYCoordinate)); endXYCoordinate = (startXCoordinate,min(nendYCoordinate, startYCoordinate));
                            if (self.id__type.get(nodeId, 'artificial') not in ['artificial', 'wire']) or (self.id__type.get(neighbour, 'artificial') not in ['artificial', 'wire']):
                                #center the Y coordinate, since either nodeId or neighbour is a component
                                startXYCoordinate = (nendXCoordinate, (nendYCoordinate+startYCoordinate)/2); endXYCoordinate = (startXCoordinate, (nendYCoordinate+startYCoordinate)/2)
                        else: # nodeId is left, neighbour is right
                            startXYCoordinate = (endXCoordinate,min(endYCoordinate, nstartYCoordinate)); endXYCoordinate = (nstartXCoordinate,min(endYCoordinate, nstartYCoordinate));
                            # if (self.id__type.get(nodeId, 'artificial') not in ['artificial', 'wire']) or (self.id__type.get(neighbour, 'artificial') not in ['artificial', 'wire']):
                            #     #center the Y coordinate, since either nodeId or neighbour is a component
                            #     startXYCoordinate = (endXCoordinate, (endYCoordinate+nstartYCoordinate)/2); endXYCoordinate = (nstartXCoordinate, (endYCoordinate+nstartYCoordinate)/2)

                    print('start: ', (startXUnit, startYUnit), ' end: ', (endXUnit, endYUnit))
                    # endXYCoordinate = (startXCoordinate, startYCoordinate)
                    print('neighbour:', neighbour, 'X: ', (startXCoordinate, endXCoordinate), ' Y: ', (startYCoordinate, endYCoordinate))
                    # print('connect: ', nodeId, '', startXYCoordinate, ';', neighbour, ':', endXYCoordinate)
                    self.list_wireStartCoordinateEndCoordinateTuple.append((startXYCoordinate, endXYCoordinate))
                    addedEdges.add((nodeId, neighbour)); addedEdges.add((neighbour, nodeId))

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<make SVG for testing?
        if self.svg:

            def textStyle(fontStr="italic 8px serif;", fillStr="#fff"):
                return f"""<style>
            .textStyle {{
                font: {fontStr};
                fill: {fillStr};
            }}
                </style>"""

            def polyline(points, stroke, stroke_width, fill):
                #example points: [[1, 2], [3, 4]]
                # const formatted_points = points.reduce((acc, cv) => acc.concat(cv), [])
                #print(points)
                formatted_points_str = ""
                for x, y in points:
                    formatted_points_str+=f'{x},{y} '
                return f'<polyline points="{formatted_points_str}" stroke="{stroke}" stroke-width="{stroke_width}" fill="{fill}"/>'#maybe use path?


            def svg(width, height, viewBox, content, fontStr="italic 40px serif;", fillStr="#ffffff", style=""):
                #xmlns="http://wwww.w3.org/2000/svg"
                #xmlns:xlink="http://www.w3.org/1999/xlink"
                return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{viewBox[0]} {viewBox[1]} {viewBox[2]} {viewBox[3]}" style="{style}">{textStyle(fontStr, fillStr)}
                {content}</svg>"""


            import os; 
            from foundation.nDisplay import NDISPLAY_MODULE_DIR
            import json; import xml.etree.ElementTree as ET; from io import StringIO
            ET.register_namespace('', "http://www.w3.org/2000/svg")
            mapping_file = open(os.path.join(NDISPLAY_MODULE_DIR, 'three', 'public', 'static', 'settings', 'ComponentType__SVGFilepath.json'), 'r')
            componentType__svgStr = {} # add a svg for artificialNode....<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            XCOORDINATEPLACEHOLDER = '@@X@@'; YCOORDINATEPLACEHOLDER = '@@Y@@'; ROTATIONPLACEHOLDER = '@@R@@'
            for componentType, svgFilepath___stub in json.loads(mapping_file.read()).items():
                boundingBox = self.type__boundingBox.get(componentType, {'height':self.artificialNodeHeight, 'width':self.artificialNodeWidth})
                svg_file = open(os.path.join(NDISPLAY_MODULE_DIR, 'three', 'public', 'static', svgFilepath___stub), 'r')
                svg_content = svg_file.read()
                svgRoot = ET.fromstring(svg_content)
                g = list(svgRoot)[0]#strip the top svg tag, and then add translate
                xMid = boundingBox['height']/2; yMid = boundingBox['width']/2
                g.set('transform', f'translate({XCOORDINATEPLACEHOLDER} {YCOORDINATEPLACEHOLDER}) rotate({ROTATIONPLACEHOLDER} {xMid} {yMid})')
                newGTree = ET.ElementTree(g)
                buffer = StringIO()
                newGTree.write(buffer, encoding='unicode')
                componentType__svgStr[componentType] = buffer.getvalue()
                svg_file.close()
            mapping_file.close()
            #

            svgContent = ''
            for nodeId, inflatedNumericStartCoordinateTuple in self.nodeId__inflatedNumericStartCoordinateTuple.items():
                componentType = self.id__type.get(nodeId, 'artificial')
                svgStrEmptyPosition = componentType__svgStr.get(componentType, '<g></g>')# add a svg for artificialNode....<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                #CHECK for rotation here, we assume everything is horizontal, so if self.nodeId__verticalOrHorizontal=='v', then we need to rotate 90degrees
                if self.nodeId__verticalOrHorizontal.get(nodeId, 'h') == 'v':
                    rotation = '90'
                else:
                    rotation = '0'
                svgStr = svgStrEmptyPosition.replace(XCOORDINATEPLACEHOLDER, str(inflatedNumericStartCoordinateTuple[0])).replace(YCOORDINATEPLACEHOLDER, str(inflatedNumericStartCoordinateTuple[1])).replace(ROTATIONPLACEHOLDER, rotation)
                svgContent += svgStr

            stroke = '#000000'; stroke_width = 3.5; fill = '#000000';
            for wireStartCoordinateEndCoordinateTuple in self.list_wireStartCoordinateEndCoordinateTuple:
                svgStr = polyline(wireStartCoordinateEndCoordinateTuple , stroke, stroke_width, fill)
                svgContent += svgStr


            self.svgStr = svg(16384, 16384, [0, 0, 16384, 16384], svgContent)#, style="background-color:#000000")

        

    #####HELPERS
    def getSplitTuple(self, noOfNeighbours, maxNoOfNeigbours):
      """
if noOfNeighbours == 10 and maxNoOfNeighbours == 4, return (3, 3, 4)
if noOfNeighbours == 17 and maxNoOfNeighbours == 4, return (3, 3, 3, 4, 4)
      """
      minimumNumberOfArtificialNodesNeeded = int(ceil(noOfNeighbours/maxNoOfNeigbours))
      neighboursPerNode = noOfNeighbours // minimumNumberOfArtificialNodesNeeded; numberOfLeftOverNeighbours = noOfNeighbours % minimumNumberOfArtificialNodesNeeded
      return tuple(((minimumNumberOfArtificialNodesNeeded-numberOfLeftOverNeighbours)*[neighboursPerNode])+(numberOfLeftOverNeighbours*[neighboursPerNode+1]))


    def getArtificialNodeIdx(self):
      newArtificialNode = self.maxNodeIdx
      self.maxNodeIdx += 1
      return newArtificialNode