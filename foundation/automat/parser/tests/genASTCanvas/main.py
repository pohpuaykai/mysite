def genASTCanvas(ast, rootNode, canvasId):
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
    heightOfBox, widthOfBox, topPadding, leftPadding = 20, 20, 10, 10

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
            content += text(widthOffset+widthOfBox/2, heightOffset+heightOfBox/2, nodeId__funcName[dic['nodeId']])
    #draw the connecting lines
    for cnid, pnid in nodeId__pNodeId.items():
        cCoordDict = nodeId__label__coordinate[cnid]
        pCoordDict = nodeId__label__coordinate[pnid]
        # content += polyline([
        #     (pCoordDict['widthOffset'], pCoordDict['heightOffset']),
        #     (cCoordDict['widthOffset'], cCoordDict['heightOffset']),
        # ], "#fff", 3, "#000") #stroke_width=3
        #print("adding line: ", )
        content += line(pCoordDict['widthOffset']+(widthOfBox/2), pCoordDict['heightOffset']+(heightOfBox), 
            cCoordDict['widthOffset']+(widthOfBox/2), cCoordDict['heightOffset'])#TODO<<<<<<<pCoordDict should be bottom-centre of the square, and it should be right
    return content

def rect(x, y, width, height):
#    return f"""ctx.moveTo({x}, {y});ctx.lineTo({x+width}, {y});
#    ctx.lineTo({x+width}, {y+height});ctx.lineTo({x}, {y+height});ctx.lineTo({x}, {y});ctx.stroke();"""
    return f"""ctx.rect({x}, {y}, {width}, {height});"""

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

    #sample EnclosureTree from CasCadE
    sampleAST = {   (4, 5): [],
    (4, 17): [   (4, 5),
                 (5, 17),
                 (6, 9),
                 (9, 11),
                 (12, 14),
                 (14, 16),
                 (6, 11),
                 (7, 8),
                 (8, 9),
                 (12, 12),
                 (12, 16)],
    (5, 17): [   (6, 9),
                 (9, 11),
                 (12, 14),
                 (14, 16),
                 (6, 11),
                 (7, 8),
                 (8, 9),
                 (12, 12),
                 (12, 16)],
    (6, 9): [(7, 8), (8, 9)],
    (6, 11): [(6, 9), (9, 11), (7, 8), (8, 9)],
    (7, 8): [],
    (8, 9): [],
    (9, 11): [],
    (12, 12): [],
    (12, 14): [(12, 12)],
    (12, 16): [(12, 14), (14, 16), (12, 12)],
    (14, 16): [],
    (18, 20): [(19, 19), (19, 20)],
    (19, 19): [],
    (19, 20): [(19, 19)],
    (19, 35): [   (24, 27),
                  (27, 34),
                  (19, 19),
                  (24, 29),
                  (29, 34),
                  (24, 32),
                  (32, 34),
                  (19, 20),
                  (24, 34),
                  (25, 26),
                  (26, 27),
                  (30, 31),
                  (31, 32)],
    (24, 27): [(25, 26), (26, 27)],
    (24, 29): [(24, 27), (25, 26), (26, 27)],
    (24, 32): [(24, 27), (24, 29), (25, 26), (26, 27), (30, 31), (31, 32)],
    (24, 34): [   (24, 27),
                  (27, 34),
                  (24, 29),
                  (29, 34),
                  (24, 32),
                  (32, 34),
                  (25, 26),
                  (26, 27),
                  (30, 31),
                  (31, 32)],
    (25, 26): [],
    (26, 27): [],
    (27, 34): [(29, 34), (32, 34), (30, 31), (31, 32)],
    (29, 34): [(32, 34), (30, 31), (31, 32)],
    (30, 31): [],
    (31, 32): [],
    (32, 34): []}
    
    rootNode = 

    CanvasContent = genASTCanvas(sampleAST, rootNode, "myCanvas")
    print(CanvasContent)