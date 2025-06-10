from datetime import datetime
import html
import os


def genASTSVG(ast, rootNode, getId, getLabel):
    content = ""

    nodeId__funcName = {}
    for parentNode, list_childNode in ast.items():
        nodeId__funcName[getId(parentNode)] = getLabel(parentNode)
        for childNode in list_childNode:
            nodeId__funcName[getId(childNode)] = getLabel(childNode)

    nodeId__tuple_pNodeId_order = {}
    level__list_nodeId = {}
    stack = [{"node":rootNode, "level":0, "parent":None}]
    maxNodeId = 0
    while len(stack) > 0:
        c = stack.pop()
        maxNodeId = max(maxNodeId, getId(c["node"]))
        #
        list_nodeId = level__list_nodeId.get(c['level'], [])
        list_nodeId.append(getId(c["node"]))
        level__list_nodeId[c['level']] = list_nodeId
        #
        for order, node in enumerate(ast.get(c['node'], [])):#node is (sym, nodeId)
            stack.append({
                "node":node,
                "level":c['level']+1,
                "parent":getId(c['node'])
            })
            nodeId__tuple_pNodeId_order[getId(node)]=(getId(c['node']), order)
    #sort each level, by parent, then by id, then place it on the SVG
    print(nodeId__tuple_pNodeId_order)
    heightOfBox, widthOfBox, topPadding, leftPadding = 40, 160, 40, 10

    #position the nodes
    #all nodes are SVG rect
    print('level__list_nodeId', level__list_nodeId)
    nodeId__label__coordinate = {}
    for level, list_nodeId in level__list_nodeId.items():
        heightOffset = (level) * (heightOfBox+topPadding) +topPadding
        #colorsInHex = generateNspacedBrightColors(len(list_nodeId))
        def sortingKey(nodeId):
            if nodeId not in nodeId__tuple_pNodeId_order:
                return float('inf')
            #sort by parent's order
            pNodeId = nodeId__tuple_pNodeId_order[nodeId][0]
            return int(nodeId__tuple_pNodeId_order.get(pNodeId, (None, pNodeId))[1])*len(list_nodeId)*len(list_nodeId)+nodeId__tuple_pNodeId_order[nodeId][1]
            #return int(nodeId__tuple_pNodeId_order[nodeId][0])*len(list_nodeId)*len(list_nodeId)*-1+nodeId__tuple_pNodeId_order[nodeId][1]
        sorted_list_nodeId = sorted(list_nodeId, key=lambda nodeId: sortingKey(nodeId))
        #update the nodeId__tuple_pNodeId_order
        for index, nodeId in enumerate(sorted_list_nodeId):
            if nodeId in nodeId__tuple_pNodeId_order:
                pNodeId, oldOrder = nodeId__tuple_pNodeId_order[nodeId]
                nodeId__tuple_pNodeId_order[nodeId] = (pNodeId, index)
        #
        for idx, nodeId in enumerate(sorted_list_nodeId):
            widthOffset = idx*(widthOfBox+leftPadding)
            nodeId__label__coordinate[nodeId]={
                "heightOffset":heightOffset,
                "widthOffset":widthOffset
            }
            content += rect(widthOffset, heightOffset, 
                "#ffffff",
                "#ffffff",#colorsInHex[idx],
                widthOfBox, heightOfBox)
            #the 3/8|3/4 factor is related to textFont, so....TODO
            content += text(widthOffset+1*widthOfBox/16, heightOffset+3*heightOfBox/4, html.escape(nodeId__funcName[nodeId]))#1 & 1 are missing
    #draw the connecting lines, with distinct_colors
    colorsInHex = generateNspacedBrightColors(len(nodeId__tuple_pNodeId_order))
    for n, (cnid, (pnid, order)) in enumerate(nodeId__tuple_pNodeId_order.items()):
        cCoordDict = nodeId__label__coordinate[cnid]
        pCoordDict = nodeId__label__coordinate[pnid]
        
        x0, y0 = pCoordDict['widthOffset']+(widthOfBox/2), pCoordDict['heightOffset']+(heightOfBox)
        x1, y1 = cCoordDict['widthOffset']+(widthOfBox/2), cCoordDict['heightOffset']
        if x0 == x1:
            x1 += 3 #if same, the frame will be empty
        if y0 == y1:
            y1 += 3 #if same, the frame will be empty
        content += polyline([
            (x0, y0), (x1, y1)
        ], 
        #"#ffffff", 
        colorsInHex[n],
        2, "#ffffff") #stroke_width=3 # start: bottom_middle, end: top_middle

    return svg(16384, 16384, [0, 0, 16384, 16384], content, style="background-color:#000000")


def textStyle(fontStr="italic 8px serif;", fillStr="#fff"):
    return f"""<style>
.textStyle {{
    font: {fontStr};
    fill: {fillStr};
}}
    </style>"""



def svg(width, height, viewBox, content, fontStr="italic 40px serif;", fillStr="#ffffff", style=""):
    #xmlns="http://wwww.w3.org/2000/svg"
    #xmlns:xlink="http://www.w3.org/1999/xlink"
    return f"""<svg width="{width}" height="{height}" viewBox="{viewBox[0]} {viewBox[1]} {viewBox[2]} {viewBox[3]}" style="{style}">{textStyle(fontStr, fillStr)}
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


def generateNspacedColors(numOfColors, noSort=True):
    import random
    remainder = numOfColors %2
    numOfColors = numOfColors //2 + remainder
    maxNum = 256 * 256 * 256 # the maxColor
    randomOffset = random.randint(0,maxNum)
    colorsInHex=[]
    for deciNum in list(range(0, maxNum, maxNum//numOfColors)):
        colorsInHex.append(hex((deciNum+randomOffset)%maxNum).replace('0x', '#'))
    

    #we sort the colorsInHex to give the maximum difference between each consecutive color (TODO this is not the max_difference?)
    colorsInHex = colorsInHex[::2]+colorsInHex[1::2] # even_space+odd_space
    if noSort:
        return colorsInHex

    #generate complement color, sort into bright(bigger), dark(smaller)
    if remainder == 1:
        remainderColors = [colorsInHex[-1]]
        colorsInHex = colorsInHex[:-1]
    else:
        remainderColors = []
    brightColors, darkColors = [], []
    for color in colorsInHex:
        colorInHex = int(color.replace('#', '0x'), 16)
        complementColorInHex = maxNum - colorInHex
        if complementColorInHex > colorInHex:
            bright, dark = complementColorInHex, colorInHex
        else:
            bright, dark = colorInHex, complementColorInHex
        brightColor = str(hex(bright)).replace('0x', '#')
        darkColor = str(hex(dark)).replace('0x', '#')
        brightColors.append(brightColor)
        darkColors.append(darkColor)
    if remainder == 1:# is remainderColors dark or bright?
        colorInHex = int(remainderColors[0].replace('#', '0x'), 16)
        complementColorInHex = maxNum - colorInHex
        if complementColorInHex > colorInHex:#LIGHT
            brightColors.append(remainderColors[0])
        else:
            darkColors.append(remainderColors[0])
    return brightColors, darkColors
    

def generateNspacedBrightColors(numOfColors):
    brightColors, _ = generateNspacedColors(2 * numOfColors, noSort=False)
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print(brightColors)
    return brightColors

def generateNspacedDarkColors(numOfColors):
    _, darkColors = generateNspacedColors(2 * numOfColors, noSort=False)
    return darkColors

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
        return str((node[0],node[1])).replace("'", '')
    #################################################################



    ##################################################################
    # \\sin(-(2x+1)(x+2))=-\\sin(2x^2+3x+2)
    sampleAST = {
    ('-', 2): [('0', 21), ('*', 26)], 
    ('-', 3): [('0', 22), ('sin', 9)], 
    ('*', 23): [('2', 10), ('x', 11)], 
    ('+', 4): [('*', 23), ('1', 12)], 
    ('+', 5): [('x', 13), ('2', 14)], 
    ('*', 26): [('+', 4), ('+', 5)], 
    ('sin', 8): [('-', 2)], 
    ('^', 1): [('x', 16), ('2', 17)], 
    ('*', 24): [('2', 15), ('^', 1)], 
    ('*', 25): [('3', 18), ('x', 19)], 
    ('+', 6): [('*', 24), ('*', 25)], 
    ('+', 7): [('+', 6), ('2', 20)], 
    ('sin', 9): [('+', 7)], 
    ('=', 0): [('-', 2), ('-', 3)]}
    rootNode = ("=", 0)
    def getId(node):
        return node[1]

    def getLabel(node):
        return str((node[0],node[1])).replace("'", '')
    ##################################################################


    ##################################################################
    # I_{R_{C}} R_{C} - V^{Q_{1}}_{BE} - I_{R} R = 0
    filenameprefix = datetime.strftime(datetime.utcnow(), "%Y%m%d%H%M%S")
    foldername = 'examples'
    folderpath = os.path.join(os.path.dirname(__file__), foldername)# TODO exclude from .git
    if not os.path.isdir(folderpath):
        os.makedirs(folderpath)
    #**********************************************************************BEFORE
    
    sampleAST = {("=", 0):[('1', 1), ('1', 2)]}
    rootNode = ("=", 0)
    def getId(node):
        return node[1]

    def getLabel(node):
        return str((node[0],node[1])).replace("'", '')
        
    
    SVGContent = genASTSVG(sampleAST, rootNode, getId, getLabel)
    filename = f"{filenameprefix}_before.html"
    filepath = os.path.join(folderpath, filename)
    writeTo(filepath, HTMLTemplate(SVGContent))
    #******************************************************************AFTER

    sampleAST = {   ('*', 35): [('-', 5), ('^', 1)],
    ('*', 36): [('int', 11), ('dx', 20)],
    ('*', 37): [('/', 12), ('^', 2)],
    ('*', 38): [('/', 13), ('^', 3)],
    ('*', 39): [('/', 14), ('^', 4)],
    ('+', 8): [('x', 17), ('1', 18)],
    ('+', 9): [('*', 37), ('-', 7)],
    ('+', 10): [('+', 9), ('C', 34)],
    ('-', 5): [('x', 15), ('1', 16)],
    ('-', 6): [('*', 38), ('*', 39)],
    ('-', 7): [('-', 6), ('x', 33)],
    ('/', 12): [('1', 21), ('4', 22)],
    ('/', 13): [('1', 25), ('3', 26)],
    ('/', 14): [('1', 29), ('2', 30)],
    ('=', 0): [('*', 36), ('+', 10)],
    ('^', 1): [('+', 8), ('2', 19)],
    ('^', 2): [('x', 23), ('4', 24)],
    ('^', 3): [('x', 27), ('3', 28)],
    ('^', 4): [('x', 31), ('2', 32)],
    ('int', 11): [('*', 35)]}
    rootNode = ("=", 0)
    def getId(node):
        return node[1]

    def getLabel(node):
        return str((node[0],node[1])).replace("'", '')
    
    SVGContent = genASTSVG(sampleAST, rootNode, getId, getLabel)
    filename = f"{filenameprefix}_after.html"
    filepath = os.path.join(folderpath, filename)
    writeTo(filepath, HTMLTemplate(SVGContent))
    ##################################################################
