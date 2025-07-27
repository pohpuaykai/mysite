from datetime import datetime
import inspect
import os
import pprint

from foundation.ecircuit import ECIRCUIT_MODULE_DIR
from foundation.ecircuit.orthogonalLayouts.rcclorthogonallayout import RCCLOrthogonalLayout


def test__genSVG__dc_twoResistor_parallel(verbose=False):
    pp = pprint.PrettyPrinter(indent=4)

    # g = {0: [1, 4], 1: [0, 4], 4: [0, 1]}
    g = {
    0: [2, 3],
    1: [2, 3],
    2: [0, 1, 6],
    3: [0, 1, 5],
    4: [5, 6],
    5: [4, 3],
    6: [4, 2]}
    id__type = {
        0: 'resistor',
        1: 'resistor',
        2: 'wire',
        3: 'wire',
        4: 'battery',
        5: 'wire',
        6: 'wire'}
    type__boundingBox = {
        "AC_signal_generator":{
            "width":79.92500305175781, 
            "height":66.1999740600586
        },
        "inductor":{
            "width":98,
            "height":12.342914581298828
        },
        "capacitor":{
            "width":28,
            "height":35
        },
        "battery":{
            "width":75.8416519165039,
            "height":79.61663818359375
        },
        "diode":{
            "width":63,
            "height":28
        },
        "oscillator":{
            "width":63,
            "height":14
        },
        "transistor":{
            "width":70,
            "height":84
        },
        "resistor":{
            "width":63,
            "height":14
        }
    }
    artificialNodeHeight = 1# artificialNodeHeight = 3.5
    artificialNodeWidth = 1# artificialNodeWidth = 3.5
    #spacing should be the max of the components that appear g?
    xSpacingBetweenComponent = 0 # spacing should be the max of the components that appear g?
    ySpacingBetweenComponent = 0
    for nodeId in g.keys():
        boundingBox = type__boundingBox.get(id__type[nodeId], {'height':artificialNodeHeight, 'width':artificialNodeWidth})
        xSpacingBetweenComponent = max(xSpacingBetweenComponent, boundingBox['width'])
        ySpacingBetweenComponent = max(ySpacingBetweenComponent, boundingBox['height'])
    #
    layouter = RCCLOrthogonalLayout(g, id__type, type__boundingBox, artificialNodeHeight, artificialNodeWidth, xSpacingBetweenComponent, ySpacingBetweenComponent)
    layouter.makeSchematics(svg=True)
    nodeId__inflatedNumericStartCoordinateTuple = layouter.nodeId__inflatedNumericStartCoordinateTuple
    list_wireStartCoordinateEndCoordinateTuple = layouter.list_wireStartCoordinateEndCoordinateTuple
    svgStr = layouter.svgStr

    outputDir = os.path.join(ECIRCUIT_MODULE_DIR, 'orthogonalLayouts', 'tests', 'rccl_SVGOuts')
    outputFilepath = os.path.join(outputDir, datetime.strftime(datetime.utcnow(), '%Y%m%d%H%M%S.svg'))
    outputFile = open(outputFilepath, 'w')
    outputFile.write(svgStr)
    outputFile.close()


    expected__nodeId__inflatedNumericStartCoordinateTuple = None
    expected__list_wireStartCoordinateEndCoordinateTuple = None
    expected__svgStr = None
    print(inspect.currentframe().f_code.co_name, ' PASSED? ', 
        expected__nodeId__inflatedNumericStartCoordinateTuple == nodeId__inflatedNumericStartCoordinateTuple and \
        expected__list_wireStartCoordinateEndCoordinateTuple == list_wireStartCoordinateEndCoordinateTuple and \
        expected__svgStr == svgStr
    )
    if verbose:
        print('nodeId__inflatedNumericStartCoordinateTuple***')
        pp.pprint(nodeId__inflatedNumericStartCoordinateTuple)
        print('list_wireStartCoordinateEndCoordinateTuple***')
        pp.pprint(list_wireStartCoordinateEndCoordinateTuple)
        print('svgStr***')
        print(svgStr)


if __name__=='__main__':
    test__genSVG__dc_twoResistor_parallel(True)