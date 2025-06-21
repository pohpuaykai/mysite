import * as THREE from '../three/three.module.js';
import {kDTree} from '../common/kDTree.js';

/**
 *
 * connects 2 components together with this wire
 * 0. find tB0=touchingBox0 of component0 and tB1=touchingBox1 of component1 with smallest distance apart
 * 1. wB = THREE.Box3().setFromPoints(corners(tB0)+corners(tB1))
 * 2. Use component0.insertVector from midPoint of touchingBox0(tB0) to touch wB at face F0, closest to the corners of tB0
 * 3. Use component1.insertVector from midPoint of touchingBox1(tB1) to touch wB at face F1, closest to the corners of tB1
 * 4. Find C0=corner of F0 closest to tB0, Find tBC0=corner of tB0 closest to any face of wB
 * 5. Find C1=corner of F1 closest to tB1, Find tBC1=corner of tB1 closest to any face of WB
 * 6. Find path_of_wire, we expect the path_of_wire to be shortest distance between C0 and C1, following the edges of wB
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
 * just take one corner for each touchingBoxes of component0, to make kDTree T,
 * 
 * then take one corner for each touchingBoxes of component1, to do nearestNeighbourSeach in T
 * **/

        //0: THIS is better done with OctTree<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<2 OctTrees, one for each component
        let cornerCoordinates__d_touchingBox_insertVector = {}
        const cornersOfTouchingBoxes0 = kDTree();
        const solderableLeads0 = component0.getAllTouchingBoxesAndInsertVectors();
        for (let i0=0; i0<solderableLeads0.length; i0++) {
            const solderableLead0 = solderableLeads0[i0];
            for (let j0=0; j0<solderableLead0.length; j0++) {
                const touchingBox0 = solderableLead0[j0]['touchingBox'];//three.Mesh has exactly 8 vertices for a cuboid
                const insertVector0 = solderableLead0[j0]['insertVector'];

                const cornerCoordinates = threeFloatsToAPoint(touchingBox0.geometry.getAttribute('position'))[0];//first corner, vertices is a flat list

                cornersOfTouchingBoxes0.insert(cornerCoordinates);
                cornerCoordinates__d_touchingBox_insertVector[cornerCoordinates] = {
                    'touchingBox':touchingBox0, 'insertVector':insertVector0
                }
            }
        }

        let minimumDistanceofComponents = Number.MAX_VALUE;
        let tB0 = null;
        let iV0 = null;
        let tB1 = null;
        let iV1 = null;
        const solderableLeads1 = component1.getAllTouchingBoxesAndInsertVectors();
        for (let i1=0; i1<solderableLeads1.length; i1++) {
            const solderableLead1 = solderableLeads1[i1];
            for (let j1=0; j1<solderableLead1.length; j1++) {
                const touchingBox1 = solderablelead1[j1]['touchingBox'];//three.Mesh has exactly 8 vertices for a cuboid
                const insertVector1 = solderableLead1[j1]['insertVector'];

                const cornerCoordinates = threeFloatsToAPoint(touchingBox1.geometry.getAttribute('position'));

                const nearestNeighbourInfoDict = cornersOfTouchingBoxes0.nearestNeighbour(cornerCoordinates);
                const nearestNeighbour = nearestNeighbourInfoDict['nearestNeighbour'];
                const nearestNeighbourDistance = nearestNeighbourInfoDict['nearestNeighbourDistance'];
                if (minimumDistanceofComponents > nearestNeighbourDistance) {
                    minimumDistanceofComponents = nearestNeighbourDistance;
                    d_touchingBox_insertVector = cornerCoordinates__d_touchingBox_insertVector[cornerCoordinates];
                    tB0Mesh = d_touchingBox_insertVector['touchingBox'];
                    tB0 = threeFloatsToAPoint(tB0Mesh.geometry.getAttribute('position')); // this is just a list of cornerCoordinates
                    iV0 = d_touchingBox_insertVector['insertVector'];
                    tB1Mesh = touchingBox1;
                    tB1 = threeFloatsToAPoint(tB1Mesh.geometry.getAttribute('position')); // this is just a list of cornerCoordinates
                    iV1 = insertVector1;
                }
            }
        }



        //1
        const wBTHREEBox = THREE.Box3();
        wBTHREEBox.setFromPoints(tB0+tB1);
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

        //2
        const F0Indices = this.findFaceOfWireBoxFromMidPointOfTouchingBoxWithInsertVector(tB0, iV0, wB);
        //

        //3 Repeat 2 for tB1
        const F1Indices = this.findFaceOfWireBoxFromMidPointOfTouchingBoxWithInsertVector(tB1, iV1, wB);


        //4 
        let C0; let C0IndexOfwB; let tbC0;
        [C0, C0IndexOfwB, tbC0] = this.findClosestCornerOfWireBoxAndCornerOfTouchingBox(F0Indices, wB, tB0)


        //5 Repeat 4 for tB1
        let C1; let C1IndexOfwB; let tbC1;
        [C1, C1IndexOfwB, tbC1] = this.findClosestCornerOfWireBoxAndCornerOfTouchingBox(F1Indices, wB, tB1)


        //6  connect them all together

        //
        const wirePath = [tbC0];
        //6.1.0
        const OG__HammingCode = {0:0, 1:1, 2:5, 3:4, 4:2, 5:3, 6:7, 7:6};
        //
        const HammingCode__OG = {}
        for (var OG in OG__HammingCode) {
            const hammingCode = OG__HammingCode[OG]; HammingCode__OG[hammingCode] = OG;
        }
        //
        const C0hIndexOfwB = OG__HammingCode[C0IndexOfwB]; const C1hIndexOfwB = OG__HammingCode[C1IndexOfwB];
        const difference_number = (C0hIndexOfwB ^ C1hIndexOfwB).toString(2); //^ is XOR, toString(2) is to change it to binaryString
        wirePath.push(tbC0);wirePath.push(C0);
        let lastVertexIdx = C0hIndexOfwB.toString(2);
        for (let digitNum=0; digitNum<difference_number.length; digitNum++) {
            if (difference_number[digitNum] == '1') {
                if (lastVertexIdx[digitNum] == '1') {
                    let newVertexIdx = lastVertexIdx;//in hIndex
                    newVertexIdx[digitNum] = '0';//flip the bit on digitNum
                } else if (lastVertexIdx[digitNum] == '0') {
                    let newVertexIdx = lastVertexIdx;//in hIndex
                    newVertexIdx[digitNum] = '1';//flip the bit on digitNum
                } else {
                    throw new Error("")
                }
                wirePath.push(wB[HammingCode__OG[parseInt(newVertexIdx, 2)]]); //convert newVertexIdx back to coordinates of wB, and push onto wirePath
                lastVertexIdx = newVertexIdx;
            }
        }
        wirePath.push(tbC1);


        //TODO  try to add thickness (FOR MAXWELL!) to it, by replacing it with CylinderGeometry, and the bends with ShapeGeometry (bezierCurve) or TubeGeometry, maybe use a quadratic_curve to make the bend shape<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        const material = new THREE.LineBasicMaterial( { color: 0x0000ff } );
        const points = [];
        for (let i=0; i<wirePath.length; i++) {
            points.push( new THREE.Vector3( wirePath[i][0], wirePath[i][1], wirePath[i][2] ) );
        }
        const geometry = new THREE.BufferGeometry().setFromPoints( points );
        // const line = new THREE.Line( geometry, material );
        super(geometry, material);
    }

    /**
     * 
     * **/
    findClosestCornerOfWireBoxAndCornerOfTouchingBox(FIndices, wB, tB) {
        let C = null; let CIndexOfwB = null; let closestDistanceTotB = Number.MAX_VALUE; let tbC = null;
        for (let i=0; i<FIndices.length; i++) {
            const corner = wB[FIndices[i]]; const closesttBCorner = null; const closestDistanceToCorner = Number.MAX_VALUE;
            for (let j=0; j<tB.length; j++) {
                const distance = this.distance(corner, tB[j]);
                if (distance < closestDistanceToCorner) {
                    closestDistanceToCorner = distance; closesttBCorner = tB[j];
                }
            }
            if (closestDistanceToCorner < closestDistanceTotB) {
                closestDistanceTotB = closestDistanceToCorner; C = corner; CIndexOfwB = F0Indices[i]; tbC = closesttBCorner;
            }
        }
        return [C, CIndexOfwB, tbC];//C is corner of wireBox, CIndexOfwB is index of C on wireBox, tbC is the corner closest to C on touchingBox
    }


    /**
     * Take midpoint of tB and the directional vector iV to form a line L.
     * This line L intersects with the faces of wB as farplanes.
     * Of the faces of wB that intersect with L, find the closest to tB
     * **/
    findFaceOfWireBoxFromMidPointOfTouchingBoxWithInsertVector(tB, iV, wB) {

        const touchingBoxFacesVertexIndices = [
            [0, 1, 2, 3], //top face
            [0, 3, 7, 4], //left face
            [1, 0, 4, 5], //back face
            [2, 1, 5, 6], //right face
            [3, 2, 6, 7], //front face
            [7, 6, 5, 4], //bottom face
        ]

        const midPoint = [0, 0, 0]; //average of the corners of tB
        for (let i=0; i<tB.length; i++) {
            midPoint[0] += tB[0];midPoint[1] += tB[1];midPoint[2] += tB[2];
        }
        midPoint[0]/=tB.length; midPoint[1]/=tB.length; midPoint[2]/=tB.length;

        const wBFacesThatIntersectWithiV = []; const indices_touchingBoxFacesVertexIndices = [];
        for (let i=0; i<touchingBoxFacesVertexIndices.length; i++) {
            const faceIndices = touchingBoxFacesVertexIndices[i];
            const topLeft = wB[faceIndices[0]]; const topRight = wB[faceIndices[1]]; const bottomRight = wB[faceIndices[2]]; const bottomLeft = wB[faceIndices[3]];
            const lambdaX = (topLeft[0] - midPoint[0])/iV[0];//could have been topRight, or bottomRight, or bottomLeft
            const lambdaY = (topLeft[1] - midPoint[1])/iV[1];//could have been topRight, or bottomRight, or bottomLeft
            const lambdaZ = (topLeft[2] - midPoint[2])/iV[2];//could have been topRight, or bottomRight, or bottomLeft
            if (this.aEquals(lambdaX, lambdaY) && this.aEquals(lambdaX, lambdaZ) && this.aEquals(lambdaY, lambdaZ)) {//insertVectorWithMidPoint intersects faceIndices as farplane
                const intersectionPoint = [midPoint[0]+lambdaX*iV[0], midPoint[1]+lambdaX*iV[1], midPoint[2]+lambdaX*iV[2]];//intersectionPoint on face as farplane
                if (this.isPointInRectangleOnTheSameFarplane(intersectionPoint, topLeft, topRight, bottomRight, bottomLeft)) {//rectPoints have to go topLeft, topRight, bottomRight, bottomLeft
                    //iVWithMidPoint intersect at this_face_of_wB
                    wBFacesThatIntersectWithiV.push(faceIndices);
                    indices_touchingBoxFacesVertexIndices.push(i);
                }
            }
        }
        //find the closest intersecting face with tB
        let shortestDistanceFromPointToFace = Number.MAX_VALUE; const FIndices = null;
        for (let i=0; i<wBFacesThatIntersectWithiV.length; i++) {
            const faceIndices = wBFacesThatIntersectWithiV[i];
            const topLeft = tB[faceIndices[0]]; const topRight = tB[faceIndices[1]]; const bottomRight = tB[faceIndices[2]]; const bottomLeft = tB[faceIndices[3]];
            const distance = shortestFarplaneDistanceofPointAndThreeCoplanarPoints(point, topLeft, topRight, bottomLeft);
            if (shortestDistanceFromPointToFace > distance) {
                shortestDistanceFromPointToFace = distance;
                FIndices = faceIndices;//Got F0
            }
        }
        return FIndices;
    }

    /**
     * A list of floats, whose amount is divisible by 3. Rearrange every 3 floats into a coordinate point.
     * **/
    threeFloatsToAPoint(coordinates) {
        const points = []; const point = [];
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
     * rectPoints go clockwise, 
     * topLeft rectPoint0
     * topRight rectPoint1
     * bottomRight rectPoint2
     * bottomLeft rectPoint3
     * 
     * find the shortest(perpendicular)_distance from point to each of the 4 lineSegments of the Rectangle, topSegment, rightSegment, bottomSegment, leftSegment.
     * shortest_distance_from_point_to_topSegment+shortest_distance_from_point_to_bottomSegment=rightSegment.length (or leftSegment.length) &&
     * shortest_distance_from_point_to_leftSegment+shortest_distance_from_point_to_rightSegment=topSegment.length (or bottomSegment.length)
     * 
     * ELSE, the point is not in this rectangle.
     * **/
    isPointInRectangleOnTheSameFarplane(point, rectPoint0, rectPoint1, rectPoint2, rectPoint3) {
        const shortestDistanceFromTopSegment = this.shortestDistance(rectPoint0, rectPoint1, point);
        const shortestDistanceFromBottomSegment = this.shortestDistance(rectPoint2, rectPoint3, point);
        const shortestDistanceFromLeftSegment = this.shortestDistance(rectPoint0, rectPoint3, point);
        const shortestDistanceFromRightSegment = this.shortestDistance(rectPoint1, rectPoint2, point);
        const rightSegment = [rectPoint1[0]-rectPoint2[0], rectPoint1[1]-rectPoint2[1], rectPoint1[2]-rectPoint2[2]];
        const topSegment = [rectPoint0[0]-rectPoint1[0], rectPoint0[1]-rectPoint1[1], rectPoint0[2]-rectPoint1[2]];
        const rightSegmentLength = this.vectorLength(rightSegment);
        const topSegmentLength = this.vectorLength(topSegment);
        return this.aEquals(shortestDistanceFromTopSegment+shortestDistanceFromBottomSegment, rightSegmentLength) && this.aEquals(shortestDistanceFromLeftSegment+shortestDistanceFromRightSegment, topSegmentLength);
    }


    /**
     * (P0P1 . P0P) / |P0P1|
     * **/
    shortestDistanceFromPointToLine(linePoint0, linePoint1, point) {
        const p0p1 = [linePoint1[0]-linePoint0[0], linePoint1[1]-linePoint0[1], linePoint1[2]-linePoint0[2]];
        const p0p = [linePoint1[0]-point[0], linePoint1[1]-point[1], linePoint1[2]-point[2]];
        const shortestDistance = (p0p1[0]*p0p[0]+p0p1[1]*p0p[1]+p0p1[2]*p0p[2])/this.vectorLength(p0p1);
        return shortestDistance;
    }


    shortestFarplaneDistanceofPointAndThreeCoplanarPoints(point, coplanarPoint0, coplanarPoint1, coplanarPoint2) {
        const normalVectorOfFarplane = [//result of cross_product between (coplanarPoint1-coplanarPoint0) (coplanarPoint2-coplanarPoint0)
            coplanarPoint0[1]*(coplanarPoint1[2]-coplanarPoint2[2])+coplanarPoint1[1]*(coplanarPoint2[2]-coplanarPoint0[2])+coplanarPoint2[1]*(coplanarPoint0[2]-coplanarPoint1[2]),
            coplanarPoint0[2]*(coplanarPoint1[0]-coplanarPoint2[0])+coplanarPoint1[2]*(coplanarPoint2[0]-coplanarPoint0[0])+coplanarPoint2[2]*(coplanarPoint0[0]-coplanarPoint1[0]),
            coplanarPoint0[0]*(coplanarPoint1[1]-coplanarPoint2[1])+coplanarPoint1[0]*(coplanarPoint2[1]-coplanarPoint0[1])+coplanarPoint2[0]*(coplanarPoint0[1]-coplanarPoint1[1]),

        ];
        return this.shortestDistanceFromPointToFarplane(point, coplanarPoint0, normalVectorOfFarplane);
    }
    /**
     * point is an array of 3 floats, (x, y, z)
     * pointOnFarplane is an array of 3 floats, (x, y, z)
     * normalVectorOfFarplane is an array of 3 floats, (x, y, z)
     * **/
    shortestDistanceFromPointToFarplane(point, pointOnFarplane, normalVectorOfFarplane) {
        //normal_projection of point on farplane
        const lambdaX = (point[0] - pointOnFarplane[0])/normalVectorOfFarplane[0];
        const lambdaY = (point[1] - pointOnFarplane[1])/normalVectorOfFarplane[1];
        const lambdaZ = (point[2] - pointOnFarplane[2])/normalVectorOfFarplane[2];

        if (this.aEquals(lambdaX, lambdaY) && this.aEquals(lambdaX, lambdaZ) && this.aEquals(lambdaY, lambdaZ)) {
            const shortestDistance = lambdaX*this.vectorLength(normalVectorOfFarplane);//we choose lambdaX, but it could have been any other
            return shortestDistance
        }
        return null;
    }

    /**
     * linePoint is an array of 3 floats, (x, y, z)
     * lineVector is an array of 3 floats, (x, y, z)
     * pointOnFarplane is an array of 3 floats, (x, y, z)
     * **/
    doesLineTouchFarplane(linePoint, lineVector, pointOnFarplane) {
        const lambdaX = (pointOnFarplane[0] - linePoint[0]) / lineVector[0];
        const lambdaY = (pointOnFarplane[1] - linePoint[1]) / lineVector[1];
        const lambdaZ = (pointOnFarplane[2] - linePoint[2]) / lineVector[2];
        return this.aEquals(lambdaX, lambdaY) && this.aEquals(lambdaX, lambdaZ) && this.aEquals(lambdaY, lambdaZ);
    }

    /**
     * Euclidean Distance
     * **/
    vectorLength(v) {
        return Math.sqrt((v[0]*v[0])+(v[1]*v[1])+(v[2]*v[2]));
    }

    distance(v0, v1) {
        const v = [v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2]];
        return this.vectorLength(v);
    }


    /**
     * 
     * equals within certain bound
     * **/
    aEquals(number0, number1) {
        const boundWidth = 0.0001;
        return number0-boundWidth <= number1 and number1 <= number0+boundWidth;
    }
}

export {Wire};