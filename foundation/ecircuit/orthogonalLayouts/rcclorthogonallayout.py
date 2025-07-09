from math import ceil

from foundation.automat.common.spanningtree import SpanningTree

class RCCLOrthogonalLayout:
    """
Overview 
we take a undirectedGraph G which comes from an electrical circuit, and try to draw an SVG (a xy-coordinate for each node) on a xy-farplane with G.
0. Use a graph whose nodes are not wires. (capture that in JS)
1. Make a MinimumSpanningTree mst of G, T (and R are the removed_edges from G), where the weights are smaller for nodes with more neighbours
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
        self.g = g; self.id__type=id__type; self.type__boundingBox = type__boundingBox; 
        self.artificialNodeHeight = artificialNodeHeight; self.artificialNodeWidth = artificialNodeWidth;
        self.xSpacingBetweenComponent = xSpacingBetweenComponent; self.ySpacingBetweenComponent = ySpacingBetweenComponent

    def makeSchematics(self, svg=False):
        self.svg = svg
        #get maxIdx of all nodes
        self.maxNodeIdx = max(self.g.keys())
        self.nodeId__unitXYCoordinateString = {}
        self.XX_X = []
        self.nodeId__numericXYCoordinateTuple = {}
        self._makeSpanningTree()
        print('completed makeSpanningTree: ', self.T, self.R)
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
        vertexIterable = []; edgeIterableSortable = []
        for parent, neighbours in self.g.items():
            vertexIterable.append(parent)
            for neighbour in neighbours:
              edgeIterableSortable.append((parent, neighbour))
        nodeId__noOfNeighbours = dict(map(lambda t: (t[0], len(t[1])), self.g.items()))
        maxNoOfNeigbours = max(map(lambda t: t[1], nodeId__noOfNeighbours.items()))
        edgeWeight = {}
        for edge in edgeIterableSortable:
            eW = 2*maxNoOfNeigbours - (nodeId__noOfNeighbours[edge[0]]+nodeId__noOfNeighbours[edge[1]])
            edgeWeight[edge] = eW
        self.T, self.R = SpanningTree.minimumSpanningTreeKruskal(vertexIterable, edgeIterableSortable, edgeWeight)

    def _fitIntoSquareGrid(self):
        #0. Take the node with most neighbours in T, r
        self.r = None; maxNoOfNeigbours = -1
        for parent, neighbours in self.T.items():
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
            print('r splitTuple:', splitTuple);print('augmented self.T', self.T)
        #2. BFS T, split up nodes t that has more than 2 neighbours, let n be number of neighbours of t [TODO MANY optimisations can be made to the grouping to make the schematics look pretty, reduce crossing_number] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        queue = [self.r]; visited = [self.r]
        while len(queue) > 0:
            current = queue.pop(0)#BFS
            #split here
            if current != self.r and len(self.T[current]) > 2:
                splitTuple = self.getSplitTuple(len(self.T[current]), 2); beginningIdx = 0; addedArtificialNodes = []
                for noOfMembers in splitTuple:
                    artificialNode = self.getArtificialNodeIdx(); addedArtificialNodes.append(artificialNode)
                    self.T[artificialNode] = self.T[current][beginningIdx:noOfMembers]
                    beginningIdx += noOfMembers
                self.T[current] = addedArtificialNodes
                print("queue", queue, 'splitTuple: ', splitTuple); import pdb;pdb.set_trace()
            #
            for neighbour in self.T[current]:
                if neighbour not in visited:
                    queue.append(neighbour); visited.append(neighbour)
        #3. Assign U, R, D, L to the neighbours of r [TODO MANY optimisations can be made to the assignment to make schematics look pretty, reduce crossing_number]<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        self.nodeId__unitXYCoordinateString.update(dict(zip(self.T[self.r], ['U', 'R', 'D', 'L'])))#just a simple assignment, TODO could be better optimised
        print('nodeId__unitXYCoordinateString', self.nodeId__unitXYCoordinateString)
        #4. Look for nodes that lead to paths that end in deg1 nodes
        leafIds = []
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
        queue = list(self.T[self.r]); visited = [self.r] + list(self.T[self.r])
        while len(queue) > 0:
            current = queue.pop(0)#BFS
            #
            current___unitXYCoordinateString = self.nodeId__unitXYCoordinateString[current]#ignore r
            #
            for neighbour in self.T[current]:
                if neighbour not in visited:
                    #assign
                    self.nodeId__unitXYCoordinateString[neighbour];
                    if len(current___unitXYCoordinateString) >= 2 and current___unitXYCoordinateString[-1] == current___unitXYCoordinateString[-2]:
                        #0 . if XX, assign neighbour to X
                        self.nodeId__unitXYCoordinateString[neighbour] = (current___unitXYCoordinateString+current___unitXYCoordinateString[-1])
                    elif current___unitXYCoordinateString.endswith('UR'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'

                    elif current___unitXYCoordinateString.endswith('RU'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                    elif current___unitXYCoordinateString.endswith('RD'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                    elif current___unitXYCoordinateString.endswith('DR'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                    elif current___unitXYCoordinateString.endswith('DL'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                    elif current___unitXYCoordinateString.endswith('LD'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                    elif current___unitXYCoordinateString.endswith('LU'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                    elif current___unitXYCoordinateString.endswith('UL'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                    elif current___unitXYCoordinateString.endswith('U'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                    elif current___unitXYCoordinateString.endswith('R'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'R'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                    elif current___unitXYCoordinateString.endswith('D'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'D'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                    elif current___unitXYCoordinateString.endswith('L'):
                        #
                        if neighbour in self.XX_X:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'L'
                        else:
                            self.nodeId__unitXYCoordinateString[neighbour] = current___unitXYCoordinateString + 'U'
                    #
                    queue.append(neighbour); visited.append(neighbour)

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

    def _addRemovedEdgesBack(self):
        for (A, B) in self.R:#A, B are nodeIds
            if A != self.r and B != self.r:
                A___nc = self.nodeId__numericXYCoordinateTuple[A]; B___nc = self.nodeId__numericXYCoordinateTuple[B]
                if A___nc[0] != B___nc[0] and A___nc[1] != B___nc[1]:
                    artificialNode = self.getArtificialNodeIdx()
                    self.T[artificialNode] = [A, B]
                    self.nodeId__numericXYCoordinateTuple[artificialNode] = (A___nc[0], B___nc[1])
                else:
                    self.T[A].append(B); self.T[B].append(A)#its inplace... right?

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
        print(self.nodeId__numericXYCoordinateTuple)
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
        #2
        nodeId__startEndXCoordinateTuple = {}; 
        previousAddedAmount = 0;
        for idx, xCoordinate in enumerate(sorted(list(xCoordinate__list_nodeId.keys()))):
            for nodeId in xCoordinate__list_nodeId[xCoordinate]:
                type = self.id__type.get(nodeId, 'artificial')
                boundingBox = self.type__boundingBox.get(type, {'height':self.artificialNodeHeight, 'width':self.artificialNodeWidth})
                startXCoordinate = previousAddedAmount + xCoordinate; endXCoordinate = previousAddedAmount + xCoordinate + boundingBox['width']
                nodeId__startEndXCoordinateTuple[nodeId] = (startXCoordinate, endXCoordinate)
                previousAddedAmount += boundingBox['width'] + self.xSpacingBetweenComponent

        #3
        nodeId__startEndYCoordinateTuple = {}
        previousAddedAmount = 0;
        for idx, yCoordinate in enumerate(sorted(list(yCoordinate__list_nodeId.keys()))):
            for nodeId in yCoordinate__list_nodeId[yCoordinate]:
                type = self.id__type.get(nodeId, 'artificial')
                boundingBox = self.type__boundingBox.get(type, {'height':self.artificialNodeHeight, 'width':self.artificialNodeWidth})
                startYCoordinate = previousAddedAmount + yCoordinate; endYCoordinate = previousAddedAmount + yCoordinate + boundingBox['height']
                nodeId__startEndYCoordinateTuple[nodeId] = (startYCoordinate, endYCoordinate)
                previousAddedAmount += boundingBox['height'] + self.ySpacingBetweenComponent

        #4
        for nodeId in self.nodeId__numericXYCoordinateTuple.keys():
            (startXCoordinate, endXCoordinate) = nodeId__startEndXCoordinateTuple[nodeId]
            (startYCoordinate, endYCoordinate) = nodeId__startEndYCoordinateTuple[nodeId]
            self.nodeId__inflatedNumericStartCoordinateTuple[nodeId] = (startXCoordinate, startYCoordinate)

        for nodeId, neighbours in self.T.items():
            (startXCoordinate, endXCoordinate) = nodeId__startEndXCoordinateTuple[nodeId]
            (startYCoordinate, endYCoordinate) = nodeId__startEndYCoordinateTuple[nodeId]
            startXYCoordinate = (endXCoordinate, endYCoordinate)
            for neighbour in neighbours:
                (startXCoordinate, endXCoordinate) = nodeId__startEndXCoordinateTuple[neighbour]
                (startYCoordinate, endYCoordinate) = nodeId__startEndYCoordinateTuple[neighbour]
                endXYCoordinate = (startXCoordinate, startYCoordinate)
                self.list_wireStartCoordinateEndCoordinateTuple.append((startXYCoordinate, endXYCoordinate))

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
                return f"""<svg width="{width}" height="{height}" viewBox="{viewBox[0]} {viewBox[1]} {viewBox[2]} {viewBox[3]}" style="{style}">{textStyle(fontStr, fillStr)}
                {content}</svg>"""


            import os; 
            from foundation.nDisplay import NDISPLAY_MODULE_DIR
            import json; import xml.etree.ElementTree as ET; from io import StringIO
            ET.register_namespace('', "http://www.w3.org/2000/svg")
            mapping_file = open(os.path.join(NDISPLAY_MODULE_DIR, 'three', 'public', 'static', 'settings', 'ComponentType__SVGFilepath.json'), 'r')
            componentType__svgStr = {} # add a svg for artificialNode....<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            XCOORDINATEPLACEHOLDER = '@@X@@'; YCOORDINATEPLACEHOLDER = '@@Y@@'
            for componentType, svgFilepath___stub in json.loads(mapping_file.read()).items():
                svg_file = open(os.path.join(NDISPLAY_MODULE_DIR, 'three', 'public', 'static', svgFilepath___stub), 'r')
                svg_content = svg_file.read()
                print(svg_content)
                svgRoot = ET.fromstring(svg_content)
                g = list(svgRoot)[0]#strip the top svg tag, and then add translate
                g.set('transform', f'translate({XCOORDINATEPLACEHOLDER}, {YCOORDINATEPLACEHOLDER})')
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
                svgStr = svgStrEmptyPosition.replace(XCOORDINATEPLACEHOLDER, str(inflatedNumericStartCoordinateTuple[0])).replace(YCOORDINATEPLACEHOLDER, str(inflatedNumericStartCoordinateTuple[1]))
                svgContent += svgStr

            stroke = '#ffffff'; stroke_width = 2; fill = '#ffffff';
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