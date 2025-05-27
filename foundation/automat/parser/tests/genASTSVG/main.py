
def genASTSVG(ast, rootNode):
    content = ""

    nodeId__funcName = {}
    for parentNode, list_childNode in ast.items():
        nodeId__funcName[parentNode[1]] = parentNode[0]
        for childNode in list_childNode:
            nodeId__funcName[childNode[1]] = childNode[0]

    nodeId__pNodeId = {}
    level__list_nodeId = {}
    stack = [{"node":rootNode, "level":0, "parent":None}]
    while len(stack) > 0:
        c = stack.pop()
        #
        list_nodeId = level__list_nodeId.get(c['level'], [])
        list_nodeId.append({
            "nodeId":c["node"][1],# nodeId
            "parentId":c['parent']
        })
        level__list_nodeId[c['level']] = list_nodeId
        #
        childLevel=c['level']+1
        for node in ast.get(c['node'], []):#node is (sym, nodeId)
            stack.append({
                "node":node,
                "level":childLevel,
                "parent":c['node'][1]
            })
            nodeId__pNodeId[node[1]]=c['node'][1]
    #sort each level, by parent, then by id, then place it on the SVG
    heightOfBox, widthOfBox, topPadding, leftPadding = 9, 9, 2, 2

    #position the nodes
    #all nodes are SVG rect
    print('level__list_nodeId', level__list_nodeId)
    nodeId__label__coordinate = {}
    for level, list_dict_nodeId_parentId in level__list_nodeId.items():
        heightOffset = level * (heightOfBox+topPadding)
        for idx, dic in enumerate(sorted(list_dict_nodeId_parentId, key=lambda d: d['parentId'])):
            widthOffset = idx*(widthOfBox+leftPadding)
            nodeId__label__coordinate[dic['nodeId']]={
                "heightOffset":heightOffset,
                "widthOffset":widthOffset
            }
            content += rect(widthOffset, heightOffset, "#fff", "#000", widthOfBox, heightOfBox)
            content += text(widthOffset, heightOffset, nodeId__funcName[dic['nodeId']])#1 & 1 are missing
    #draw the connecting lines
    for cnid, pnid in nodeId__pNodeId.items():
        cCoordDict = nodeId__label__coordinate[cnid]
        pCoordDict = nodeId__label__coordinate[pnid]
        content += polyline([
            (pCoordDict['widthOffset'], pCoordDict['heightOffset']),
            (cCoordDict['widthOffset'], cCoordDict['heightOffset']),
        ], "#fff", 3, "#000") #stroke_width=3

    return svg(512, 512, [0, 0, 512, 512], content)



def svg(width, height, viewBox, content):
    #xmlns="http://wwww.w3.org/2000/svg"
    #xmlns:xlink="http://www.w3.org/1999/xlink"
    return f'<svg width="{width}" height="{height}" viewBox="{viewBox[0]} {viewBox[1]} {viewBox[2]} {viewBox[3]}">{content}</svg>'


def rect(x, y, fill, stroke, width, height):
    return f'<rect x="{x}" y="{y}" fill="{fill}" stroke="{stroke}" width="{width}" height="{height}"/>'

def circle(cx, cy, r, fill):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'

def polyline(points, stroke, stroke_width, fill):
    #example points: [[1, 2], [3, 4]]
    # const formatted_points = points.reduce((acc, cv) => acc.concat(cv), [])
    print(points)
    formatted_points_str = ""
    for x, y in points:
        formatted_points_str+=f'{x},{y} '
    return f'<polyline points="{formatted_points_str}" stroke="{stroke}" stroke-width="{stroke_width}" fill="{fill}"/>'

def text(x, y, content):
    return f'<text x="{x}" y="{y}">{content}</text>'

if __name__=="__main__":
    print("genASTSVG")

    #1+1=2
    sampleAST = {
        ("=", 0):[("+", 1), ("2", 2)],
        ("+", 1):[("1", 4), ("1", 5)]
    }
    rootNode = ("=", 0)

    SVGContent = genASTSVG(sampleAST, rootNode)
    print(SVGContent)