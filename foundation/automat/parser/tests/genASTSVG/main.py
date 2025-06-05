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
    maxNum = 256 * 256 * 256 # the maxColor
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
        return str((node[0],node[1]))
    #################################################################



    ##################################################################
    # \\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)
    sampleAST = {
    ('-', 1): [('0', 21), ('*', 26)], 
    ('-', 2): [('0', 22)], 
    ('*', 23): [('2', 10), ('x', 11)], 
    ('+', 3): [('*', 23), ('1', 12)], 
    ('+', 4): [('x', 13), ('2', 14)], 
    ('*', 26): [('+', 3), ('+', 4)], 
    ('^', 0): [('x', 16), ('2', 17)], 
    ('*', 24): [('2', 15), ('^', 0)], 
    ('*', 25): [('3', 18), ('x', 19)], 
    ('+', 5): [('*', 24), ('*', 25)], 
    ('+', 6): [('+', 5), ('2', 20)], 
    ('=', 7): [('-', 1), ('+', 6)]}
    rootNode = ("=", 7)
    def getId(node):
        return node[1]

    def getLabel(node):
        return str((node[0],node[1]))
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