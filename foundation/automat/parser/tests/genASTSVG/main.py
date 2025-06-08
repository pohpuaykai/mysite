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

    nodeId__pNodeId = {}
    level__list_nodeId = {}
    stack = [{"node":rootNode, "level":0, "parent":None}]
    maxNodeId = 0
    while len(stack) > 0:
        c = stack.pop()
        maxNodeId = max(maxNodeId, getId(c["node"]))
        #
        list_nodeId = level__list_nodeId.get(c['level'], [])
        list_nodeId.append({
            "nodeId":getId(c["node"]),# nodeId
            "parentId":c['parent']
        })
        level__list_nodeId[c['level']] = list_nodeId
        #
        for node in ast.get(c['node'], []):#node is (sym, nodeId)
            stack.append({
                "node":node,
                "level":c['level']+1,
                "parent":getId(c['node'])
            })
            nodeId__pNodeId[getId(node)]=getId(c['node'])
    #sort each level, by parent, then by id, then place it on the SVG
    heightOfBox, widthOfBox, topPadding, leftPadding = 40, 80, 40, 40

    #position the nodes
    #all nodes are SVG rect
    print('level__list_nodeId', level__list_nodeId)
    nodeId__label__coordinate = {}
    for level, list_dict_nodeId_parentId in level__list_nodeId.items():
        heightOffset = (level) * (heightOfBox+topPadding) +topPadding
        #colorsInHex = generateNspacedBrightColors(len(list_dict_nodeId_parentId))
        ##
        if maxNodeId > 10:
            sortingLambda = lambda d: str(str(d['parentId'])[::-1]+'|'+str(d['nodeId'])[::-1])[::-1]
        else:
            sortingLambda = lambda d: str(d['parentId'])+'|'+str(d['nodeId'])
        ##
        for idx, dic in enumerate(sorted(list_dict_nodeId_parentId, key=sortingLambda)):
            widthOffset = idx*(widthOfBox+leftPadding)
            nodeId__label__coordinate[dic['nodeId']]={
                "heightOffset":heightOffset,
                "widthOffset":widthOffset
            }
            content += rect(widthOffset, heightOffset, 
                "#ffffff",
                "#ffffff",#colorsInHex[idx],
                widthOfBox, heightOfBox)
            #the 3/8|3/4 factor is related to textFont, so....TODO
            content += text(widthOffset+3*widthOfBox/16, heightOffset+3*heightOfBox/4, html.escape(nodeId__funcName[dic['nodeId']]))#1 & 1 are missing
    #draw the connecting lines, with distinct_colors
    colorsInHex = generateNspacedBrightColors(len(nodeId__pNodeId))
    for n, (cnid, pnid) in enumerate(nodeId__pNodeId.items()):
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
            bright, dark = colorInHex, complementColorInHex
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
    
    sampleAST = {
    ('*', 2): [('7', 1), ('^', 4)],
    ('*', 8): [('3', 7), ('^', 10)],
    ('*', 14): [('5', 13), ('^', 16)],
    ('*', 20): [('nroot', 19), ('^', 22)],
    ('*', 26): [('pi', 25), ('^', 28)],
    ('+', 12): [('-', 6), ('-', 18)],
    ('+', 24): [('+', 12), ('-', 30)],
    ('-', 6): [('*', 2), ('*', 8)],
    ('-', 18): [('*', 14), ('*', 20)],
    ('-', 30): [('*', 26), ('42', 31)],
    ('=', 0): [('P', 32), ('+', 24)],
    ('^', 4): [('x', 3), ('13', 5)],
    ('^', 10): [('x', 9), ('9', 11)],
    ('^', 16): [('x', 15), ('8', 17)],
    ('^', 22): [('x', 21), ('4', 23)],
    ('^', 28): [('x', 27), ('2', 29)],
    ('nroot', 19): [(2, 34), ('2', 33)]}
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

    sampleAST = {
    ('*', 29): [('7', 14), ('^', 1)],
    ('*', 30): [('3', 17), ('^', 2)],
    ('*', 31): [('5', 20), ('^', 3)],
    ('*', 32): [('sqrt', 11), ('^', 4)],
    ('*', 33): [('pi', 12), ('^', 5)],
    ('+', 9): [('-', 6), ('-', 7)],
    ('+', 10): [('+', 9), ('-', 8)],
    ('-', 6): [('*', 29), ('*', 30)],
    ('-', 7): [('*', 31), ('*', 32)],
    ('-', 8): [('*', 33), ('42', 28)],
    ('=', 0): [('P', 13), ('+', 10)],
    ('^', 1): [('x', 15), ('13', 16)],
    ('^', 2): [('x', 18), ('9', 19)],
    ('^', 3): [('x', 21), ('8', 22)],
    ('^', 4): [('x', 24), ('4', 25)],
    ('^', 5): [('x', 26), ('2', 27)],
    ('sqrt', 11): [('2', 23)]}
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
