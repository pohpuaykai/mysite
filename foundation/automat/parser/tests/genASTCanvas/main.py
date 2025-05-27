
def genASTSVG(ast, rootNode, canvasId):
    content = f'var c = document.getElementById("{canvasId}");var ctx = c.getContext("2d");'

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
    heightOfBox, widthOfBox, topPadding, leftPadding = 20, 20, 5, 5

    #position the nodes
    #all nodes are SVG rect
    # print('level__list_nodeId', level__list_nodeId)
    nodeId__label__coordinate = {}
    for level, list_dict_nodeId_parentId in level__list_nodeId.items():
        heightOffset = (level) * (heightOfBox+topPadding) +topPadding
        for idx, dic in enumerate(sorted(list_dict_nodeId_parentId, key=lambda d: d['parentId'])):
            widthOffset = idx*(widthOfBox+leftPadding)
            nodeId__label__coordinate[dic['nodeId']]={
                "heightOffset":heightOffset,
                "widthOffset":widthOffset
            }
            # content += rect(widthOffset, heightOffset, "#fff", "#000", widthOfBox, heightOfBox)
            # content += text(widthOffset, heightOffset, nodeId__funcName[dic['nodeId']])#1 & 1 are missing
            content += rect(widthOffset, heightOffset, widthOfBox, heightOfBox)
            content += text(widthOffset+2*leftPadding, heightOffset+2*topPadding, nodeId__funcName[dic['nodeId']])
    #draw the connecting lines
    for cnid, pnid in nodeId__pNodeId.items():
        cCoordDict = nodeId__label__coordinate[cnid]
        pCoordDict = nodeId__label__coordinate[pnid]
        # content += polyline([
        #     (pCoordDict['widthOffset'], pCoordDict['heightOffset']),
        #     (cCoordDict['widthOffset'], cCoordDict['heightOffset']),
        # ], "#fff", 3, "#000") #stroke_width=3
        print("adding line: ", )
        content += line(pCoordDict['widthOffset'], pCoordDict['heightOffset'], 
            cCoordDict['widthOffset'], cCoordDict['heightOffset'])#TODO<<<<<<<pCoordDict should be bottom-centre of the square, and it should be right
    return content

def rect(x, y, width, height):
    return f"""ctx.moveTo({x}, {y});ctx.lineTo({x+width}, {y});
    ctx.lineTo({x+width}, {y+height});ctx.lineTo({x}, {y+height});ctx.lineTo({x}, {y});ctx.stroke();"""

def text(x, y, content, font="12px Arial"):
    return f'ctx.fillText("{content}", {x}, {y});'

def line(x0, y0, x1, y1):
    return f"""ctx.moveTo({x0}, {y0});ctx.lineTo({x1}, {y1});ctx.lineWidth=1;ctx.strokeStyle='#063C75';ctx.stroke();"""

if __name__=="__main__":
    # print("genASTSVG")

    #1+1=2
    sampleAST = {
        ("=", 0):[("+", 1), ("2", 2)],
        ("+", 1):[("1", 4), ("1", 5)]
    }
    rootNode = ("=", 0)

    SVGContent = genASTSVG(sampleAST, rootNode, "myCanvas")
    print(SVGContent)