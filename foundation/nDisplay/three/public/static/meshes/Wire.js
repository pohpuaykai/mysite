import * as THREE from '../three/three.module.js';
import {kDTree} from '../common/kDTree.js';
import {RayIntersectBox} from '../common/RayIntersectBox.js';

/**
 *
 * connects 2 components together with this wire
 * 0. find tF0=touchingFace0 of component0 and tF1=touchingFace1 of component1 with smallest distance apart
 * 1. wB = THREE.Box3().setFromPoints(corners(tF0)+corners(tF1))
 * 2. Find C0=corner of F0 closest to tF0, Find tFC0=corner of tF0 closest to any face of wB
 * 3. Find C1=corner of F1 closest to tF1, Find tFC1=corner of tF1 closest to any face of WB
 * 4. Find path_of_wire, we expect the path_of_wire to be shortest distance between C0 and C1, following the edges of wB
 *   0. Connect tBC0 to C0
 *   1. Use Hamming_code to check away_by, and which path to follow, note that C0 and C1 are corners of wB.
 *     0. Translate index_of_C0_in_wB and index_of_C1_in_wB to HammingCode -> hIndex_of_C0_in_wB and hIndex_of_C1_in_wB
 *     1. difference_number = XOR(hIndex_of_C0_in_wB, hIndex_of_C1_in_wB)
 *     2. Change difference_number into binaryString bs of length 3, lastVertexIdx = hIndex_of_C0_in_wB
 *       0. If there is a "1" in the first digit of difference_number, 
 *         0. If lastVertexIdx is a "1" in the first digit, add xx0_hIndex_of_wB to path_of_wire, where xx are the third&second digit of lastVertexIdx respectively
 *           0. Update lastVertexIdx to the xx0_hIndex_of_wB just added
 *         1. If lastVertexIdx is a "0" in the first digit, add xx1_hIndex_of_wB to path_of_wire, where xx are the third&second digit of lastVertexIdx respectively
 *           0. Update lastVertexIdx to the xx1_hIndex_of_wB just added
 *       1. If there is a "1" in the second digit of difference_number,
 *         0. If lastVertexIdx is a "1" in the second digit, add x0x_hIndex_of_wB to path_of_wire, where x x are the third&first digit of lastVertexIdx respectively
 *           0. Update lastVertexIdx to the x0x_hIndex_of_wB just added
 *         1. If lastVertexIdx is a "0" in the second digit, add x1x_hIndex_of_wB to path_of_wire, where x x are the third&first digit of lasteVertexIdx respectively
 *           0. Update lastVertexIdx to the x1x_hIndex_of_wB just added
 *       2. If there is a "1" in the third digit of difference_number, 
 *         0. If lastVertexIdx is a "1" in the third digit, add 0xx_hIndex_of_wB to path_of_wire, where xx are the second&first digit of lastVertexIdx respectively
 *           0. Update lastVertexIdx to the 0xx_hIndex_of_wB just added
 *         1. If lastVertexIdx is a "0" in the third digit, add 1xx_hIndex_of_wB to path_of_wire, where xx are the second&first digit of lastVertexIdx respectively
 *           0. Update lastVertexIdx to the 1xx_hIndex_of_wB just added
 *   2. Connect path_of_wire to tBC1
 *         
 * 
 * Every point in path_of_wire is a BEND, the first and last BENDs are not 90 degrees
 */
class Wire extends THREE.Line {//TODO  try to add thickness (FOR MAXWELL!) to it, by replacing it with CylinderGeometry, and the bends with ShapeGeometry (bezierCurve) or TubeGeometry, maybe use a quadratic_curve to make the bend shape<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    constructor(component0, component1) {
        /**
         * HELPERS start
         * **/

        /**
         * Euclidean Distance
         * **/
        function vectorLength(v) {
            return Math.sqrt((v[0]*v[0])+(v[1]*v[1])+(v[2]*v[2]));
        }

        function distance(v0, v1) {
            const v = [v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2]];
            return vectorLength(v);
        }


        /**
         * 
         * equals within certain bound
         * **/
        function aEquals(number0, number1) {
            const boundWidth = 0.0001;
            return number0-boundWidth <= number1 && number1 <= number0+boundWidth;
        }




        /**
         * A list of floats, whose amount is divisible by 3. Rearrange every 3 floats into a coordinate point.
         * **/
        function threeFloatsToAPoint(coordinates) {
            const points = []; let point = [];
            for (let i=0; i<coordinates.length; i++) {
                point.push(coordinates[i]);
                if (i%3 == 2) {
                    points.push(point); point = [];
                }
            }
            return points;
        }


        /**
         * 
         * **/
        function findClosestCornerOfWireBoxAndCornerOfTouchingBox(wB, tF) {
            let closestDistance = Number.MAX_VALUE; let wBC = null; let tFC = null; let CIndexOfwB = null;
            for (let i=0; i<tF.length; i++) {
                let tFCorner = tF[i];
                for(let j=0; j<wB.length; j++) {
                    let wBCorner = wB[j];
                    const d = distance(tFCorner, wBCorner);
                    if (closestDistance > d) {
                        closestDistance = d; wBC = wBCorner; tFC = tFCorner; CIndexOfwB = j;
                    }
                }
            }
            return [wBC, CIndexOfwB, tFC];
        }


        function cEquals(coordinate0, coordinate1) {
            for(let i=0; i<coordinate0.length; i++) {
                if (! aEquals(coordinate0[i], coordinate1[i])) {
                    return false;
                }
            }
            return true;
        }

        /**
         * HELPERS end
         * **/


/**
 * just take one corner for each touchingBoxes of component0, to make kDTree T,
 * 
 * then take one corner for each touchingBoxes of component1, to do nearestNeighbourSeach in T
 * **/

        //0
        let cornerCoordinates__d_touchingBox_insertVector = {}
        const cornersOfTouchingBoxes0 = new kDTree();
        const solderableLeads0 = component0.getAllTouchingBoxesAndInsertVectors();
        for (let i0=0; i0<solderableLeads0.length; i0++) {
            const solderableLead0 = solderableLeads0[i0];
            for (let j0=0; j0<solderableLead0.length; j0++) {
                const touchingBox0 = solderableLead0[j0]['touchingBox'];//three.Mesh has exactly 8 vertices for a cuboid
                // const insertVector0 = solderableLead0[j0]['insertVector'];
                const cornerCoordinates = touchingBox0[0];//first corner, vertices is a flat list

                cornersOfTouchingBoxes0.insert(cornerCoordinates);
                cornerCoordinates__d_touchingBox_insertVector[cornerCoordinates] = {
                    'touchingBox':touchingBox0//, 'insertVector':insertVector0
                }

            }
        }

        let minimumDistanceofComponents = Number.MAX_VALUE;
        let tF0 = null;
        // let iV0 = null;
        let tF1 = null;
        // let iV1 = null;
        // console.log('****');console.log(cornersOfTouchingBoxes0);console.log(cornerCoordinates__d_touchingBox_insertVector);console.log('****');
        const solderableLeads1 = component1.getAllTouchingBoxesAndInsertVectors();
        for (let i1=0; i1<solderableLeads1.length; i1++) {
            const solderableLead1 = solderableLeads1[i1];
            for (let j1=0; j1<solderableLead1.length; j1++) {
                const touchingBox1 = solderableLead1[j1]['touchingBox'];//three.Mesh has exactly 8 vertices for a cuboid
                // const insertVector1 = solderableLead1[j1]['insertVector'];

                // const cornerCoordinates = threeFloatsToAPoint(touchingBox1.geometry.getAttribute('position').array);
                const cornerCoordinates = touchingBox1;
                for (let k1=0; k1<cornerCoordinates.length; k1++) {
                    const cornerCoordinate = cornerCoordinates[k1];
                    const nearestNeighbourInfoDict = cornersOfTouchingBoxes0.nearestNeighbour(cornerCoordinate);//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    const nearestNeighbour = nearestNeighbourInfoDict['nearestNeighbour'];
                    const nearestNeighbourDistance = nearestNeighbourInfoDict['nearestNeighbourDistance'];
                    if (minimumDistanceofComponents > nearestNeighbourDistance) {
                        minimumDistanceofComponents = nearestNeighbourDistance;

                        let d_touchingBox_insertVector = cornerCoordinates__d_touchingBox_insertVector[nearestNeighbour];
                        tF0 = d_touchingBox_insertVector['touchingBox'];
                        tF1 = touchingBox1;
                    }
                }
            }
        }

        //*****confirming we got tB0, iV0, tB1, iV1, the two touchingBoxes( and the direction of connection) to connect together.
        // console.log("tF0", tF0);console.log("tF1", tF1);

        //1
        const wBTHREEBox = new THREE.Box3();
        const pointsFromtF0tF1 = [];
        for(let i=0; i<tF0.length; i++) {
            pointsFromtF0tF1.push(new THREE.Vector3(tF0[i][0], tF0[i][1], tF0[i][2]));
        }
        for(let i=0; i<tF1.length; i++) {
            pointsFromtF0tF1.push(new THREE.Vector3(tF1[i][0], tF1[i][1], tF1[i][2]));
        }
        wBTHREEBox.setFromPoints(pointsFromtF0tF1);
        // console.log('wBTHREEBox:', wBTHREEBox, 'tB0', tB0, 'tB1', tB1);
        //convert wB to list of corners vertices
        /**
         * 
         * 0(left, up, in), 1(right, up, in), 2(right, up, out), 3(left, up, out),
         * 4(left, down, in), 5(right, down, in), 6(right, down, out), 7(left, down, out)
         * 
         * left~min.x; right~max.x
         * down~min.y; up~max.y
         * out~min.z; inx~max.z
         * **/
        const left = wBTHREEBox.min.x; const right = wBTHREEBox.max.x;
        const down = wBTHREEBox.min.y; const up = wBTHREEBox.max.y;
        const out = wBTHREEBox.min.z; const inx = wBTHREEBox.max.z;//in is a Javascript keyword, so. we add an x to the end of in 
        const wB = [
            [left, up, inx],
            [right, up, inx],
            [right, up, out],
            [left, up, out],
            [left, down, inx],
            [right, down, inx],
            [right, down, out],
            [left, down, out],
        ];

        //**** confirming we got wB:
        // console.log('wB', wB);

        //4 
        let C0; let C0IndexOfwB; let tbC0;
        [C0, C0IndexOfwB, tbC0] = findClosestCornerOfWireBoxAndCornerOfTouchingBox(wB, tF0)


        //5 Repeat 4 for tB1
        let C1; let C1IndexOfwB; let tbC1;
        [C1, C1IndexOfwB, tbC1] = findClosestCornerOfWireBoxAndCornerOfTouchingBox(wB, tF1)


        //**** confirming we got C0, C0IndexOfwB, tbC0, C1, C1IndexOfwB, tbC1
        // console.log('C0', C0); console.log('C0IndexOfwB', C0IndexOfwB); console.log('tbC0', tbC0);
        // console.log('C1', C1); console.log('C1IndexOfwB', C1IndexOfwB); console.log('tbC1', tbC1);

        //6  connect them all together
        // console.log('wB', wB);
        // console.log('')
        //
        const wirePath = [];
        //6.1.0
        const OG__HammingCode = {0:0, 1:1, 2:5, 3:4, 4:2, 5:3, 6:7, 7:6};
        //
        const HammingCode__OG = {}
        for (var OG in OG__HammingCode) {
            const hammingCode = OG__HammingCode[OG]; HammingCode__OG[hammingCode] = OG;
        }
        //
        const C0hIndexOfwB = OG__HammingCode[C0IndexOfwB]; const C1hIndexOfwB = OG__HammingCode[C1IndexOfwB];
        const difference_number = (C0hIndexOfwB ^ C1hIndexOfwB).toString(2).padStart(3, '0'); //^ is XOR, toString(2) is to change it to binaryString
        // console.log('C0hIndexOfwB', C0hIndexOfwB); console.log('C1hIndexOfwB', C1hIndexOfwB);
        // console.log("difference_number", difference_number);
        wirePath.push(tbC0);
        if (! cEquals(tbC0, C0)) {
            wirePath.push(C0);//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<check if tbC0==C0
        }
        
        let lastVertexIdx = C0hIndexOfwB.toString(2).padStart(3, '0');
        for (let digitNum=0; digitNum<difference_number.length; digitNum++) {
            if (difference_number[digitNum] == '1') {
                // console.log('difference_number', difference_number, ' on digitNum:', digitNum);
                let newVertexIdx;
                if (lastVertexIdx[digitNum] == '1') {
                    let newVertexIdxArr = lastVertexIdx.split('');//in hIndex
                    newVertexIdxArr[digitNum] = '0';//flip the bit on digitNum
                    newVertexIdx = newVertexIdxArr.join('');
                } else if (lastVertexIdx[digitNum] == '0') {
                    let newVertexIdxArr = lastVertexIdx.split('');//in hIndex
                    newVertexIdxArr[digitNum] = '1';//flip the bit on digitNum
                    newVertexIdx = newVertexIdxArr.join('');
                } else {
                    throw new Error("")
                }
                wirePath.push(wB[HammingCode__OG[parseInt(newVertexIdx, 2)]]); //convert newVertexIdx back to coordinates of wB, and push onto wirePath
                // console.log('XOR checking, pushed:', wB[HammingCode__OG[parseInt(newVertexIdx, 2)]]);
                lastVertexIdx = newVertexIdx;
            }
        }
        if (! cEquals(wirePath[wirePath.length -1], tbC1)) {
            wirePath.push(tbC1);//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<check if last coordinate same as tbC1
        }
        

        // console.log('wirePath');console.log(wirePath);


        //TODO  try to add thickness (FOR MAXWELL!) to it, by replacing it with CylinderGeometry, and the bends with ShapeGeometry (bezierCurve) or TubeGeometry, maybe use a quadratic_curve to make the bend shape<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        const material = new THREE.LineBasicMaterial( { color: 0xf0f0f0 } );
        const points = [];
        for (let i=0; i<wirePath.length; i++) {
            points.push( new THREE.Vector3( wirePath[i][0], wirePath[i][1], wirePath[i][2] ) );
        }
        // console.log('points');console.log(points);
        const geometry = new THREE.BufferGeometry().setFromPoints( points );
        // const line = new THREE.Line( geometry, material );
        super(geometry, material);

        //<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<clean up the helpers, some are not needed
    }



}

export {Wire};