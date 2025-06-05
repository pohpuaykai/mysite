import html


def genASTSVG(ast, rootNode, getId, getLabel):
    content = ""

    nodeId__funcName = {}
    for parentNode, list_childNode in ast.items():
        nodeId__funcName[getId(parentNode)] = getLabel(parentNode)
        for childNode in list_childNode:
            nodeId__funcName[getId(childNode)] = getLabel(childNode)

    nodeId__pNodeId = {}
    level__list_nodeId = {}
    stack = [{"node":rootNode, "level":0, "parent":None}]
    while len(stack) > 0:
        c = stack.pop()
        #
        list_nodeId = level__list_nodeId.get(c['level'], [])
        list_nodeId.append({
            "nodeId":getId(c["node"]),# nodeId
            "parentId":c['parent']
        })
        level__list_nodeId[c['level']] = list_nodeId
        #
        childLevel=c['level']+1
        for node in ast.get(c['node'], []):#node is (sym, nodeId)
            stack.append({
                "node":node,
                "level":childLevel,
                "parent":getId(c['node'])
            })
            nodeId__pNodeId[getId(node)]=getId(c['node'])
    #sort each level, by parent, then by id, then place it on the SVG
    heightOfBox, widthOfBox, topPadding, leftPadding = 40, 40, 40, 40

    #position the nodes
    #all nodes are SVG rect
    #print('level__list_nodeId', level__list_nodeId)
    nodeId__label__coordinate = {}
    for level, list_dict_nodeId_parentId in level__list_nodeId.items():
        heightOffset = (level) * (heightOfBox+topPadding) +topPadding
        colorsInHex = generateNspacedColors(len(list_dict_nodeId_parentId))
        for idx, dic in enumerate(sorted(list_dict_nodeId_parentId, key=lambda d: d['parentId'], reverse=True)):
            widthOffset = idx*(widthOfBox+leftPadding)
            nodeId__label__coordinate[dic['nodeId']]={
                "heightOffset":heightOffset,
                "widthOffset":widthOffset
            }
            content += rect(widthOffset, heightOffset, 
                # "#fff", 
                # "#000", 
                "#fff",
                colorsInHex[idx],
                widthOfBox, heightOfBox)
            #the 3/8|3/4 factor is related to textFont, so....TODO
            content += text(widthOffset+3*widthOfBox/8, heightOffset+3*heightOfBox/4, html.escape(nodeId__funcName[dic['nodeId']]))#1 & 1 are missing
    #draw the connecting lines, with distinct_colors
    colorsInHex = generateNspacedColors(len(nodeId__pNodeId))
    for n, (cnid, pnid) in enumerate(nodeId__pNodeId.items()):
        cCoordDict = nodeId__label__coordinate[cnid]
        pCoordDict = nodeId__label__coordinate[pnid]
        content += polyline([
            (pCoordDict['widthOffset']+(widthOfBox/2), pCoordDict['heightOffset']+(heightOfBox)),
            (cCoordDict['widthOffset']+(widthOfBox/2), cCoordDict['heightOffset']),
        ], 
        #"#000", 
        colorsInHex[n],
        1, "#fff") #stroke_width=3 # start: bottom_middle, end: top_middle

    return svg(8192, 8192, [0, 0, 8192, 8192], content)


def textStyle(fontStr="italic 8px serif;", fillStr="#fff"):
    return f"""<style>
.textStyle {{
    font: {fontStr};
    fill: {fillStr};
}}
    </style>"""



def svg(width, height, viewBox, content, fontStr="italic 40px serif;", fillStr="#fff"):
    #xmlns="http://wwww.w3.org/2000/svg"
    #xmlns:xlink="http://www.w3.org/1999/xlink"
    return f"""<svg width="{width}" height="{height}" viewBox="{viewBox[0]} {viewBox[1]} {viewBox[2]} {viewBox[3]}">{textStyle(fontStr, fillStr)}
    {content}</svg>"""


def rect(x, y, fill, stroke, width, height):
    return f'<rect x="{x}" y="{y}" fill="{fill}" stroke="{stroke}" width="{width}" height="{height}"/>'

def circle(cx, cy, r, fill):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'

def polyline(points, stroke, stroke_width, fill):
    #example points: [[1, 2], [3, 4]]
    # const formatted_points = points.reduce((acc, cv) => acc.concat(cv), [])
    #print(points)
    formatted_points_str = ""
    for x, y in points:
        formatted_points_str+=f'{x},{y} '
    return f'<polyline points="{formatted_points_str}" stroke="{stroke}" stroke-width="{stroke_width}" fill="{fill}"/>'

def text(x, y, content):
    return f'<text x="{x}" y="{y}">{content}</text>'


def generateNspacedColors(numOfColors):
    import random
    maxNum = 16 * 16 * 16 # the maxColor
    randomOffset = random.randint(0,maxNum)
    colorsInHex=[]
    for deciNum in list(range(0, maxNum, maxNum//numOfColors)):
        colorsInHex.append(hex((deciNum+randomOffset)%maxNum).replace('0x', '#'))

    #we sort the colorsInHex to give the maximum difference between each consecutive color (TODO this is not the max_difference?)
    colorsInHex = colorsInHex[::2]+colorsInHex[1::2] # even_space+odd_space

    return colorsInHex

#########(easy way out)
def HTMLTemplate(content):
    return f"""<html><head></head><body>{content}</body></html>"""

def writeTo(filepath, content):
    file = open(filepath, 'w')
    file.write(content)
    file.close()


if __name__=="__main__":#Use AST to convert to JavaScript (good training), or write HTML file (easy way out)
    print("genASTSVG")
    ################################################################
    #' 3x^{9} = 3x^{2}x^{7}'
    sampleAST = {   
    ('*', 2): [('3', 1), ('^', 4)],
    ('*', 6): [('*', 2), ('^', 8)],
    ('*', 11): [('3', 10), ('^', 13)],
    ('=', 0): [('*', 11), ('*', 6)],
    ('^', 4): [('x', 3), ('2', 5)],
    ('^', 8): [('x', 7), ('7', 9)],
    ('^', 13): [('x', 12), ('9', 14)]}
    rootNode = ("=", 0)

    def getId(node):
        return node[1]

    def getLabel(node):
        return node[0]
    #################################################################



    ##################################################################
    # sampleAST = {   (4, 5): [],
    # (4, 17): [   (12, 16),
    #              (14, 16),
    #              (8, 9),
    #              (9, 11),
    #              (6, 11),
    #              (4, 5),
    #              (12, 12),
    #              (12, 14),
    #              (5, 17),
    #              (6, 9),
    #              (7, 8)],
    # (5, 17): [   (12, 16),
    #              (14, 16),
    #              (8, 9),
    #              (9, 11),
    #              (6, 11),
    #              (12, 12),
    #              (12, 14),
    #              (6, 9),
    #              (7, 8)],
    # (6, 9): [(8, 9), (7, 8)],
    # (6, 11): [(8, 9), (9, 11), (6, 9), (7, 8)],
    # (7, 8): [],
    # (8, 9): [],
    # (9, 11): [],
    # (12, 12): [],
    # (12, 14): [(12, 12)],
    # (12, 16): [(14, 16), (12, 12), (12, 14)],
    # (14, 16): [],
    # (18, 20): [(19, 20), (19, 19)],
    # (19, 19): [],
    # (19, 20): [(19, 19)],
    # (19, 35): [   (24, 27),
    #               (32, 34),
    #               (26, 27),
    #               (31, 32),
    #               (25, 26),
    #               (27, 34),
    #               (24, 29),
    #               (24, 32),
    #               (29, 34),
    #               (19, 20),
    #               (24, 34),
    #               (19, 19),
    #               (30, 31)],
    # (24, 27): [(26, 27), (25, 26)],
    # (24, 29): [(24, 27), (26, 27), (25, 26)],
    # (24, 32): [(24, 27), (26, 27), (31, 32), (25, 26), (24, 29), (30, 31)],
    # (24, 34): [   (24, 27),
    #               (32, 34),
    #               (26, 27),
    #               (31, 32),
    #               (25, 26),
    #               (27, 34),
    #               (24, 29),
    #               (24, 32),
    #               (29, 34),
    #               (30, 31)],
    # (25, 26): [],
    # (26, 27): [],
    # (27, 34): [(32, 34), (31, 32), (29, 34), (30, 31)],
    # (29, 34): [(32, 34), (31, 32), (30, 31)],
    # (30, 31): [],
    # (31, 32): [],
    # (32, 34): []}

    # sampleAST = {
    # (4, 5): [],
    # (4, 17): [(4, 5), (5, 17)],
    # (5, 17): [(12, 16), (6, 11)],
    # (6, 9): [(8, 9), (7, 8)],
    # (6, 11): [(9, 11), (6, 9)],
    # (7, 8): [],
    # (8, 9): [],
    # (9, 11): [],
    # (12, 12): [],
    # (12, 14): [(12, 12)],
    # (12, 16): [(12, 14), (14, 16)],
    # (14, 16): [],
    # (18, 20): [(19, 20)],
    # (19, 19): [],
    # (19, 20): [(19, 19)],
    # (19, 35): [(19, 20), (24, 34)],
    # (24, 27): [(26, 27), (25, 26)],
    # (24, 29): [(24, 27)],
    # (24, 32): [(30, 31), (24, 29), (31, 32)],
    # (24, 34): [(24, 32), (27, 34)],
    # (25, 26): [],
    # (26, 27): [],
    # (27, 34): [(29, 34)],
    # (29, 34): [(30, 31), (32, 34), (31, 32)],
    # (30, 31): [],
    # (31, 32): [],
    # (32, 34): []}

    # rootNode = (4, 17)# [(4, 17), (19, 35)]

    # interval__idx = {
    # (4, 5): 0,
    # (4, 17): 1,
    # (5, 17): 2,
    # (6, 9): 3,
    # (6, 11): 4,
    # (7, 8): 5,
    # (8, 9): 6,
    # (9, 11): 7,
    # (12, 12): 8,
    # (12, 14): 9,
    # (12, 16): 10,
    # (14, 16): 11,
    # (18, 20): 12,
    # (19, 19): 13,
    # (19, 20): 14,
    # (19, 35): 15,
    # (24, 27): 16,
    # (24, 29): 17,
    # (24, 32): 18,
    # (24, 34): 19,
    # (25, 26): 20,
    # (26, 27): 21,
    # (27, 34): 22,
    # (29, 34): 23,
    # (30, 31): 24,
    # (31, 32): 25,
    # (32, 34): 26}

    # def getId(node):#needs to be positive integer
    #     return interval__idx[node]

    # def getLabel(node):#needs to be str
    #     return str(node)
    ##################################################################

    SVGContent = genASTSVG(sampleAST, rootNode, getId, getLabel)
    # print(SVGContent)
    from datetime import datetime
    import os
    foldername = 'examples'
    folderpath = os.path.join(os.path.dirname(__file__), foldername)# TODO exclude from .git
    if not os.path.isdir(folderpath):
        os.makedirs(folderpath)
    filename = datetime.strftime(datetime.utcnow(), "%Y%m%d%H%M%S.html")
    filepath = os.path.join(folderpath, filename)
    writeTo(filepath, HTMLTemplate(SVGContent))