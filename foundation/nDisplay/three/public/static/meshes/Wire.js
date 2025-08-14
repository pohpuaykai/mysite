import * as THREE from '../three/three.module.js';
import {Actor} from '../custom/Actor.js';

import {kDTree} from '../common/kDTree.js';
import {RayIntersectBox} from '../common/RayIntersectBox.js';
/**
 * 
 * @param radius {Number} - we follow the American_wire_gauge from this source: https://en.wikipedia.org/wiki/American_wire_gauge#Tables_of_AWG_wire_sizes
 * Here is a reproduction of 2 columns in millimetres:
 * AWG|Diameter(mm)
 * 0000(4/0)|11.684
 * 000 (3/0)|10.405
 * 00 (2/0)|9.266
 * 0 (1/0)|8.251
 * 1|7.348
 * 2|6.544
 * 3|5.827
 * 4|5.189
 * 5|4.621
 * 6|4.115
 * 7|3.665
 * 8|3.264
 * 9|2.906
 * 10|2.588
 * 11|2.305
 * 12|2.053
 * 13|1.828
 * 14|1.628
 * 15|1.450
 * 16|1.291
 * 17|1.150
 * 18|1.024
 * 19|0.912
 * 20|0.812
 * 21|0.723
 * 22|0.644
 * 23|0.573
 * 24|0.511
 * 25|0.455
 * 26|0.405
 * 27|0.361
 * 28|0.321
 * 29|0.286
 * 30|0.255
 * 31|0.227
 * 32|0.202
 * 33|0.180
 * 34|0.160
 * 35|0.143
 * 36|0.127
 * 37|0.113
 * 38|0.101
 * 39|0.0897
 * 40|0.0799
 * 
 */
class Wire extends Actor {// extends THREE.Object3D {//THREE.Line {
    /**
     * 
     * **/
    // constructor(component0, component1, radius, solderableLeadIdx0=null, solderableLeadIdx1=null) {
    constructor(config) {
        super();
        this.type = 'wire';
        this.wireColor = 0x99d6ff;
        //overloading
        if (typeof config === "object" && config != null) {
            if ('x' in config && 'y' in config && 'z' in config && 'radius' in config) {
                let x; let y; let z; let radius;
                ({x, y, z, radius}=config);
                this.constructor__fakeNode(x, y, z, radius);
            } else if ('component0' in config && 'component1' in config && 'radius' in config) {// maybe check type of component0, component1 and radius
                let component0; let component1; let radius; let solderableLeadIdx0; let solderableLeadIdx1; let hamming3Idx;
                ({component0, component1, radius, solderableLeadIdx0=null, solderableLeadIdx1=null, hamming3Idx='214'}=config);
                this.constructor__connection(component0, component1, radius, solderableLeadIdx0, solderableLeadIdx1, hamming3Idx);//making connection between component0 and component1
            }
        } else {
            throw Exception()
        }

    }


    /**
     * This constructor is used to make a fakeNode (sphere in space) like a component with 1_solderableLead, in contrast with the other constructor which is used to make connection between components
     * **/
    constructor__fakeNode(x, y, z, radius) {
        /**
         * Constructor Parameters for THREE.SphereGeometry
         * 
         * radius — sphere radius. Default is 1.<<<<< we are only using this, 
            widthSegments — number of horizontal segments. Minimum value is 3, and the default is 32.
            heightSegments — number of vertical segments. Minimum value is 2, and the default is 16.
            phiStart — specify horizontal starting angle. Default is 0.
            phiLength — specify horizontal sweep angle size. Default is Math.PI * 2.
            thetaStart — specify vertical starting angle. Default is 0.
            thetaLength — specify vertical sweep angle size. Default is Math.PI.
         * **/
        const geometry = new THREE.SphereGeometry(radius);
        const material = new THREE.MeshBasicMaterial({color: this.wireColor})
        const sphere = new THREE.Mesh(geometry, material);
        this.add(sphere);
        // this.mainMeshUUID = [sphere.uuid];
        this.addMainMesh(sphere.uuid)
        // super(geometry, material);
        this.position.set(x, y, z);

        // console.log('x', x, 'y', y, 'z', z);
        //below is the attributes needed to use this Wire as a Component
        this.positiveLeadsDirections = [[0, 0]]; //only one sphere
        const touchPointsOfSolderableLeads = [];

        const bufferLength = 0;
        const left=x-radius-bufferLength; //-x 
        const right=x+radius+bufferLength;//+x
        const down=y-radius-bufferLength;//-y
        const up=y+radius+bufferLength;//+y
        const out=z-radius-bufferLength;//-z
        const inx=z+radius+bufferLength;//+z
        // const left=-radius-bufferLength; //-x
        // const right=radius+bufferLength;//+x
        // const down=-radius-bufferLength;//-y
        // const up=radius+bufferLength;//+y
        // const out=-radius-bufferLength;//-z
        // const inx=radius+bufferLength;//+z
        // console.log('left: ', left);
        // console.log('right: ', right);
        
        // console.log('down: ', down);
        
        // console.log('up: ', up);
        
        // console.log('out: ', out);
        
        // console.log('inx: ', inx);
        

        const coordinates = [
            [left, up, inx],
            [right, up, inx],
            [right, up, out],
            [left, up, out],
            [left, down, inx],
            [right, down, inx],
            [right, down, out],
            [left, down, out]
        ]
        let solderableLeads = [];
        //take center of each segment
        touchPointsOfSolderableLeads.push([
            (left+right)/2, (up+down)/2, (inx+out)/2
        ]);
        solderableLeads.push([
            {//topFace
                'touchingFaceCoordinates':[
                    coordinates[0][0], coordinates[0][1], coordinates[0][2], 
                    coordinates[1][0], coordinates[1][1], coordinates[1][2], 
                    coordinates[2][0], coordinates[2][1], coordinates[2][2], 
                    coordinates[3][0], coordinates[3][1], coordinates[3][2],
                ]
            },
            {//leftFace; rightFace
                'touchingFaceCoordinates':[
                    coordinates[0][0], coordinates[0][1], coordinates[0][2], 
                    coordinates[3][0], coordinates[3][1], coordinates[3][2], 
                    coordinates[7][0], coordinates[7][1], coordinates[7][2], 
                    coordinates[4][0], coordinates[4][1], coordinates[4][2], 
                ]
            },
            {//rightFace; leftFace
                'touchingFaceCoordinates':[
                    coordinates[1][0], coordinates[1][1], coordinates[1][2], 
                    coordinates[2][0], coordinates[2][1], coordinates[2][2], 
                    coordinates[6][0], coordinates[6][1], coordinates[6][2], 
                    coordinates[5][0], coordinates[5][1], coordinates[5][2], 
                ]
            },
            {//inxFace
                'touchingFaceCoordinates':[
                    coordinates[0][0], coordinates[0][1], coordinates[0][2], 
                    coordinates[1][0], coordinates[1][1], coordinates[1][2], 
                    coordinates[5][0], coordinates[5][1], coordinates[5][2], 
                    coordinates[4][0], coordinates[4][1], coordinates[4][2], 
                ]
            },
            {//outFace
                'touchingFaceCoordinates':[
                    coordinates[3][0], coordinates[3][1], coordinates[3][2], 
                    coordinates[2][0], coordinates[2][1], coordinates[2][2], 
                    coordinates[6][0], coordinates[6][1], coordinates[6][2], 
                    coordinates[7][0], coordinates[7][1], coordinates[7][2], 
                ]
            },
            {//downFace
                'touchingFaceCoordinates':[
                    coordinates[4][0], coordinates[4][1], coordinates[4][2], 
                    coordinates[5][0], coordinates[5][1], coordinates[5][2], 
                    coordinates[6][0], coordinates[6][1], coordinates[6][2], 
                    coordinates[7][0], coordinates[7][1], coordinates[7][2], 
                ]
            },
        ]);// we do a cube around the sphere, only one solderableLead
        this.touchPointsOfSolderableLeads = touchPointsOfSolderableLeads;

        const uuid__type = {}; this.solderableIdx__touchPointUUID = {}
        this.touchPointsOfSolderableLeads = touchPointsOfSolderableLeads;
        for (let i=0; i<touchPointsOfSolderableLeads.length; i++) {
            let touchPoint = touchPointsOfSolderableLeads[i];

            const geometry = new THREE.BufferGeometry();
            geometry.setAttribute('position', new THREE.Float32BufferAttribute(touchPoint, 3));

            const material = new THREE.PointsMaterial({ color: this.wireColor, size: 0.1 });
            const point = new THREE.Points(geometry, material);
            this.attach(point); // scene or any Object3D

            uuid__type[point.uuid] = 'TOUCH_POINT';
            this.solderableIdx__touchPointUUID[i] = point.uuid;
        }
        this.solderableLeads = solderableLeads;


        // console.log("solderableLeads", solderableLeads);
        const solderableLeadsIdx_touchingBoxesIdx__attachmentId = {}; const attachmentId__solderableLeadsIdx_touchingBoxesIdx = {};
        for ( let i = 0; i<solderableLeads.length; i++) {
            let touchingFaces = solderableLeads[i];
            // console.log('touchingFaces', touchingFaces);
            for(let j = 0; j<touchingFaces.length; j++) {
                const touchingFaceCoordinates = new Float32Array(touchingFaces[j]['touchingFaceCoordinates']);//this needs to be flat...
                // console.log(touchingFaceCoordinates);
                // console.log('touchingFaceCoordinates', touchingFaceCoordinates)
                const touchingFaceGeometry = new THREE.BufferGeometry();
                touchingFaceGeometry.setAttribute('position', new THREE.BufferAttribute(touchingFaceCoordinates, 3));
                const touchingFaceColors = new Float32Array([//2 triangles per face,  each row is R G B, R G B, R G B,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                ]);
                touchingFaceGeometry.setAttribute('color', new THREE.BufferAttribute(touchingFaceColors, 3));
                const touchingFaceIndices = new Uint16Array([
                    0, 1, 3, 2, 3, 1, //top face
                ]);
                touchingFaceGeometry.setIndex(new THREE.BufferAttribute(touchingFaceIndices, 1));
                const touchingFaceMaterial = new THREE.MeshBasicMaterial({
                    vertexColors: true,
                    // flatShading: true, // this disables vertex interpolation, also known as Blending Does not exist in our version of THREE
                    side: THREE.DoubleSide //ensure backface shows color too
                });
                const touchingFace = new THREE.Line(touchingFaceGeometry, touchingFaceMaterial);
                // this.add(touchingFace); // this make solderableLeads position relative to this wire
                this.attach(touchingFace); // this make solderableLeads position relative to this wire
                uuid__type[touchingFace.uuid] = 'TOUCHING_BOX';
                solderableLeadsIdx_touchingBoxesIdx__attachmentId[[i, j]] = touchingFace.uuid;
                attachmentId__solderableLeadsIdx_touchingBoxesIdx[touchingFace.uuid] = [i, j];
            }
        }
        this.solderableLeadsIdx_touchingBoxesIdx__attachmentId = solderableLeadsIdx_touchingBoxesIdx__attachmentId;
        this.attachmentId__solderableLeadsIdx_touchingBoxesIdx = attachmentId__solderableLeadsIdx_touchingBoxesIdx;
        this.uuid__type = uuid__type;
    }



    /**
     * This constructor is used to make connection between components, in contrast with the other constructor which forms a fakeNode (sphere in space)
     * ConnectionConstructor
     * 
     * 
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
     * 
     * **/
    constructor__connection(component0, component1, radius, solderableLeadIdx0=null, solderableLeadIdx1=null, hamming3Idx='214') {

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

        // console.log('solderableLeadIdx0', solderableLeadIdx0); console.log('solderableLeadIdx1', solderableLeadIdx1); console.log(solderableLeadIdx0 === null && solderableLeadIdx1 === null)
        let tF0 = null;
        let tF1 = null;
        let tF0Idx = null; let tF1Idx = null;
        if (solderableLeadIdx0 === null && solderableLeadIdx1 === null) {
            // console.log('CASE0<<<<<');
            //0
            let cornerCoordinates__solderableLeadIdx = {};
            let cornerCoordinates__faceIdx = {};
            let cornerCoordinates__d_touchingBox_insertVector = {}
            const cornersOfTouchingBoxes0 = new kDTree();
            const solderableLeads0 = component0.getAllTouchingBoxesAndInsertVectors();
            for (let i0=0; i0<solderableLeads0.length; i0++) {
                const solderableLead0 = solderableLeads0[i0];
                for (let j0=0; j0<solderableLead0.length; j0++) {
                    const touchingBox0 = solderableLead0[j0]['touchingBox'];//THREE.Line
                    const cornerCoordinates = touchingBox0[0];//first corner, vertices is a flat list

                    cornersOfTouchingBoxes0.insert(cornerCoordinates);
                    cornerCoordinates__d_touchingBox_insertVector[cornerCoordinates] = {
                        'touchingBox':touchingBox0//, 'insertVector':insertVector0
                    }

                    cornerCoordinates__solderableLeadIdx[cornerCoordinates] = i0;
                    cornerCoordinates__faceIdx[cornerCoordinates] = j0;
                }
            }

            let minimumDistanceofComponents = Number.MAX_VALUE;
            // let tF0 = null;
            // let tF1 = null;
            // console.log('****');console.log(cornersOfTouchingBoxes0);console.log(cornerCoordinates__d_touchingBox_insertVector);console.log('****');
            const solderableLeads1 = component1.getAllTouchingBoxesAndInsertVectors();
            for (let i1=0; i1<solderableLeads1.length; i1++) {
                const solderableLead1 = solderableLeads1[i1];
                for (let j1=0; j1<solderableLead1.length; j1++) {
                    const touchingBox1 = solderableLead1[j1]['touchingBox'];//three.Mesh has exactly 8 vertices for a cuboid
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
                            solderableLeadIdx0 = cornerCoordinates__solderableLeadIdx[nearestNeighbour];
                            solderableLeadIdx1 = i1;
                            tF0Idx = cornerCoordinates__faceIdx[nearestNeighbour]; 
                            tF1Idx = j1;
                        }
                    }
                }
            }
            // console.log(tF0); console.log(tF1);

        } else if (solderableLeadIdx0 != null && solderableLeadIdx1 === null) {//assume !=null means its a valid index

            // console.log('CASE1<<<<<');
            //0
            let cornerCoordinates__solderableLeadIdx = {};
            let cornerCoordinates__faceIdx = {};
            let cornerCoordinates__d_touchingBox_insertVector = {}
            const cornersOfTouchingBoxes1 = new kDTree();
            const solderableLeads1 = component1.getAllTouchingBoxesAndInsertVectors();
            for (let i1=0; i1<solderableLeads1.length; i1++) {
                const solderableLead1 = solderableLeads1[i1];
                for (let j1=0; j1<solderableLead1.length; j1++) {
                    const touchingBox1 = solderableLead1[j1]['touchingBox'];
                    const cornerCoordinates = touchingBox1[0];//first corner, vertices is a flat list

                    cornersOfTouchingBoxes1.insert(cornerCoordinates);
                    cornerCoordinates__d_touchingBox_insertVector[cornerCoordinates] = {
                        'touchingBox':touchingBox1
                    }

                    cornerCoordinates__solderableLeadIdx[cornerCoordinates] = i1;
                    cornerCoordinates__faceIdx[cornerCoordinates] = j1;
                }
            }

            let minimumDistanceofComponents = Number.MAX_VALUE;
            const solderableLeads0 = component0.getAllTouchingBoxesAndInsertVectors();
            const solderableLead0 = solderableLeads0[solderableLeadIdx0];
            for (let j0=0; j0<solderableLead0.length; j0++) {
                const touchingBox0 = solderableLead0[j0]['touchingBox'];//three.Mesh has exactly 8 vertices for a cuboid
                const cornerCoordinates = touchingBox0;
                for (let k0=0; k0<cornerCoordinates.length; k0++) {
                    const cornerCoordinate = cornerCoordinates[k0];
                    const nearestNeighbourInfoDict = cornersOfTouchingBoxes1.nearestNeighbour(cornerCoordinate);//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    const nearestNeighbour = nearestNeighbourInfoDict['nearestNeighbour'];
                    const nearestNeighbourDistance = nearestNeighbourInfoDict['nearestNeighbourDistance'];
                    if (minimumDistanceofComponents > nearestNeighbourDistance) {
                        minimumDistanceofComponents = nearestNeighbourDistance;

                        let d_touchingBox_insertVector = cornerCoordinates__d_touchingBox_insertVector[nearestNeighbour];
                        tF0 = touchingBox0;
                        tF1 = d_touchingBox_insertVector['touchingBox'];
                        solderableLeadIdx1 = cornerCoordinates__solderableLeadIdx[nearestNeighbour];
                        tF1Idx = cornerCoordinates__faceIdx[nearestNeighbour]; 
                        tF0Idx = j0;
                    }
                }
            }

        } else if (solderableLeadIdx0 === null && solderableLeadIdx1 != null) {//assume !=null means its a valid index

            // console.log('CASE2<<<<<');
            //0
            let cornerCoordinates__solderableLeadIdx = {};
            let cornerCoordinates__faceIdx = {};
            let cornerCoordinates__d_touchingBox_insertVector = {}
            const cornersOfTouchingBoxes0 = new kDTree();
            const solderableLeads0 = component0.getAllTouchingBoxesAndInsertVectors();
            for (let i0=0; i0<solderableLeads0.length; i0++) {
                const solderableLead0 = solderableLeads0[i0];
                for (let j0=0; j0<solderableLead0.length; j0++) {
                    const touchingBox0 = solderableLead0[j0]['touchingBox'];
                    const cornerCoordinates = touchingBox0[0];//first corner, vertices is a flat list

                    cornersOfTouchingBoxes0.insert(cornerCoordinates);
                    cornerCoordinates__d_touchingBox_insertVector[cornerCoordinates] = {
                        'touchingBox':touchingBox0
                    }

                    cornerCoordinates__solderableLeadIdx[cornerCoordinates] = i0;
                    cornerCoordinates__faceIdx[cornerCoordinates] = j0;
                }
            }

            let minimumDistanceofComponents = Number.MAX_VALUE;
            const solderableLeads1 = component1.getAllTouchingBoxesAndInsertVectors();
            const solderableLead1 = solderableLeads1[solderableLeadIdx1];
            for (let j1=0; j1<solderableLead1.length; j1++) {
                const touchingBox1 = solderableLead1[j1]['touchingBox'];//three.Mesh has exactly 8 vertices for a cuboid
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
                        solderableLeadIdx0 = cornerCoordinates__solderableLeadIdx[nearestNeighbour];
                        tF0Idx = cornerCoordinates__faceIdx[nearestNeighbour]; 
                        tF1Idx = j1;
                    }
                }
            }

        } else { // we have both solderableLead0 && solderableLead1

            // console.log('CASE3<<<<<');
            const solderableLeads0 = component0.getAllTouchingBoxesAndInsertVectors();
            const solderableLead0 = solderableLeads0[solderableLeadIdx0];
            const solderableLeads1 = component1.getAllTouchingBoxesAndInsertVectors();
            const solderableLead1 = solderableLeads1[solderableLeadIdx1];
            let minimumDistanceofComponents = Number.MAX_VALUE;
            for (let i0=0; i0<solderableLead0.length; i0++) {
                const touchingBox0 = solderableLead0[i0]['touchingBox'];
                for(let j0=0; j0<touchingBox0.length; j0++) {
                    const cornerCoordinate0 = touchingBox0[j0];
                    for(let i1=0; i1<solderableLead1.length; i1++) {
                        const touchingBox1 = solderableLead1[i1]['touchingBox'];
                        for(let j1=0; j1<touchingBox1.length; j1++) {
                            const cornerCoordinate1 = touchingBox1[j1];
                            const d = distance(cornerCoordinate0, cornerCoordinate1);
                            if (minimumDistanceofComponents > d) {
                                minimumDistanceofComponents = d;

                                tF0 = touchingBox0;
                                tF1 = touchingBox1;
                                tF0Idx = i0; tF1Idx = i1;
                            }
                        }
                    }
                }
            }
        }

        // console.log(tF0); console.log(tF1);
/**
 * just take one corner for each touchingBoxes of component0, to make kDTree T,
 * 
 * then take one corner for each touchingBoxes of component1, to do nearestNeighbourSeach in T
 * **/

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
        // console.log('component0.getTouchPoint(solderableLeadIdx0)', component0.getTouchPoint(solderableLeadIdx0));
        const wirePath = [component0.getTouchPoint(solderableLeadIdx0)];
        // const wirePath = [];
        //6.1.0
        const OG__HammingCode__124 = {0:0, 1:1, 2:5, 3:4, 4:2, 5:3, 6:7, 7:6};
        const OG__HammingCode__142 = {0:0, 1:1, 2:3, 3:2, 4:4, 5:5, 6:7, 7:6};
        const OG__HammingCode__214 = {0:0, 1:2, 2:6, 3:4, 4:1, 5:3, 6:7, 7:5};
        const OG__HammingCode__241 = {0:0, 1:2, 2:3, 3:1, 4:4, 5:6, 6:7, 7:5};
        const OG__HammingCode__412 = {0:0, 1:4, 2:6, 3:2, 4:1, 5:5, 6:7, 7:3};
        const OG__HammingCode__421 = {0:0, 1:4, 2:5, 3:1, 4:2, 5:6, 6:7, 7:3};

        let OG__HammingCode;
        //1 of the 6 possible OG__HammingCode mapping, we should help the user to choose the most pretty..., HOW? <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        switch(hamming3Idx) {
        case '124':
            OG__HammingCode = OG__HammingCode__124;
            break;

        case '142':
            OG__HammingCode = OG__HammingCode__142;
            break;

        case '214':
            OG__HammingCode = OG__HammingCode__214;
            break;

        case '241':
            OG__HammingCode = OG__HammingCode__241;
            break;

        case '412':
            OG__HammingCode = OG__HammingCode__412;
            break;

        case '421':
            OG__HammingCode = OG__HammingCode__421;
            break;

        default:
            OG__HammingCode = OG__HammingCode__214;
        }
        
        
        
        
        
        
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
        // console.log('lastVertexIdx: ', lastVertexIdx);
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
        wirePath.push(component1.getTouchPoint(solderableLeadIdx1));
        
        this.wirePath = wirePath;
        // console.log('wirePath');console.log(wirePath);

        //below is the attributes needed to use this Wire as a Component
        const positiveLeadsDirections = [];
        for(let i=0; i<this.wirePath.length; i++) {
            for(let j=i+1; j<this.wirePath.length; j++) {
                positiveLeadsDirections.push([i, j]);
                positiveLeadsDirections.push([j, i]);
            }
        }
        this.positiveLeadsDirections = positiveLeadsDirections;


        //add touchingFaces to this wire.
        const solderableLeads = []; const offset = radius+0.001; console.log(offset); const touchPointsOfSolderableLeads = [];
        for (let i=0; i<wirePath.length-1; i++) {//number_of_solderableLeads == wirePath.length
            const startCoordinate = wirePath[i]; const endCoordinate = wirePath[i+1];
            // console.log('s', startCoordinate); console.log('e', endCoordinate);
            //find boundingBoxOfThisLine with radius
            let left = null; let right = null; let down = null; let up = null; let out = null; let inx = null;
            if (!aEquals(startCoordinate[0], endCoordinate[0])) {//radius is on 1(y), 2(z)
                left = Math.min(startCoordinate[0], endCoordinate[0]); right = Math.max(startCoordinate[0], endCoordinate[0]); 
                down = startCoordinate[1]-offset; up = endCoordinate[1]+offset; out = startCoordinate[2]-offset; inx = endCoordinate[2]+offset;
                // console.log('facing x-axis');
            } else if (!aEquals(startCoordinate[1], endCoordinate[1])) {//radius is on 0(x), 2(z)
                left = startCoordinate[0]-offset; right = endCoordinate[0]+offset; 
                down = Math.min(startCoordinate[1], endCoordinate[1]); up = Math.max(startCoordinate[1], endCoordinate[1]); 
                out = startCoordinate[2]-offset; inx = endCoordinate[2]+offset;
                // console.log('facing y-axis');console.log('left', left); console.log('right', right);
            } else if (!aEquals(startCoordinate[2], endCoordinate[2])) {//radius is on 0(x), 1(y)
                left = startCoordinate[0]-offset; right = endCoordinate[0]+offset; down = startCoordinate[1]-offset; up = endCoordinate[1]+offset; 
                out = Math.min(startCoordinate[2], endCoordinate[2]); inx = Math.max(startCoordinate[2], endCoordinate[2]);
                // console.log('facing z-axis')
            }
            const coordinates = [
                [left, up, inx],
                [right, up, inx],
                [right, up, out],
                [left, up, out],
                [left, down, inx],
                [right, down, inx],
                [right, down, out],
                [left, down, out]
            ]
            // console.log('coordinates', coordinates);
            //take center of each segment
            touchPointsOfSolderableLeads.push([
                (left+right)/2, (up+down)/2, (inx+out)/2
            ]);
            solderableLeads.push([
                {//topFace
                    'touchingFaceCoordinates':[
                        coordinates[0][0], coordinates[0][1], coordinates[0][2], 
                        coordinates[1][0], coordinates[1][1], coordinates[1][2], 
                        coordinates[2][0], coordinates[2][1], coordinates[2][2], 
                        coordinates[3][0], coordinates[3][1], coordinates[3][2],
                    ]
                },
                {//leftFace
                    'touchingFaceCoordinates':[
                        coordinates[0][0], coordinates[0][1], coordinates[0][2], 
                        coordinates[3][0], coordinates[3][1], coordinates[3][2], 
                        coordinates[7][0], coordinates[7][1], coordinates[7][2], 
                        coordinates[4][0], coordinates[4][1], coordinates[4][2], 
                    ]
                },
                {//rightFace
                    'touchingFaceCoordinates':[
                        coordinates[1][0], coordinates[1][1], coordinates[1][2], 
                        coordinates[2][0], coordinates[2][1], coordinates[2][2], 
                        coordinates[6][0], coordinates[6][1], coordinates[6][2], 
                        coordinates[5][0], coordinates[5][1], coordinates[5][2], 
                    ]
                },
                {//inxFace
                    'touchingFaceCoordinates':[
                        coordinates[0][0], coordinates[0][1], coordinates[0][2], 
                        coordinates[1][0], coordinates[1][1], coordinates[1][2], 
                        coordinates[5][0], coordinates[5][1], coordinates[5][2], 
                        coordinates[4][0], coordinates[4][1], coordinates[4][2], 
                    ]
                },
                {//outFace
                    'touchingFaceCoordinates':[
                        coordinates[3][0], coordinates[3][1], coordinates[3][2], 
                        coordinates[2][0], coordinates[2][1], coordinates[2][2], 
                        coordinates[6][0], coordinates[6][1], coordinates[6][2], 
                        coordinates[7][0], coordinates[7][1], coordinates[7][2], 
                    ]
                },
                {//downFace
                    'touchingFaceCoordinates':[
                        coordinates[4][0], coordinates[4][1], coordinates[4][2], 
                        coordinates[5][0], coordinates[5][1], coordinates[5][2], 
                        coordinates[6][0], coordinates[6][1], coordinates[6][2], 
                        coordinates[7][0], coordinates[7][1], coordinates[7][2], 
                    ]
                },
            ]);
        }

        this.touchPointsOfSolderableLeads = touchPointsOfSolderableLeads;

        const uuid__type = {}; this.solderableIdx__touchPointUUID = {}
        this.touchPointsOfSolderableLeads = touchPointsOfSolderableLeads;
        for (let i=0; i<touchPointsOfSolderableLeads.length; i++) {
            let touchPoint = touchPointsOfSolderableLeads[i];

            const geometry = new THREE.BufferGeometry();
            geometry.setAttribute('position', new THREE.Float32BufferAttribute(touchPoint, 3));

            const material = new THREE.PointsMaterial({ color: this.wireColor, size: 0.1 });
            const point = new THREE.Points(geometry, material);
            this.add(point); // scene or any Object3D

            uuid__type[point.uuid] = 'TOUCH_POINT';
            this.solderableIdx__touchPointUUID[i] = point.uuid;
        }

        this.solderableLeads = solderableLeads;
        // console.log("solderableLeads", solderableLeads);
        const solderableLeadsIdx_touchingBoxesIdx__attachmentId = {}; const attachmentId__solderableLeadsIdx_touchingBoxesIdx = {};
        for ( let i = 0; i<solderableLeads.length; i++) {
            let touchingFaces = solderableLeads[i];
            // console.log('touchingFaces', touchingFaces);
            for(let j = 0; j<touchingFaces.length; j++) {
                const touchingFaceCoordinates = new Float32Array(touchingFaces[j]['touchingFaceCoordinates']);//this needs to be flat...
                // console.log('touchingFaceCoordinates', touchingFaceCoordinates)
                const touchingFaceGeometry = new THREE.BufferGeometry();
                touchingFaceGeometry.setAttribute('position', new THREE.BufferAttribute(touchingFaceCoordinates, 3));
                const touchingFaceColors = new Float32Array([//2 triangles per face,  each row is R G B, R G B, R G B,
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                ]);
                touchingFaceGeometry.setAttribute('color', new THREE.BufferAttribute(touchingFaceColors, 3));
                const touchingFaceIndices = new Uint16Array([
                    0, 1, 3, 2, 3, 1, //top face
                ]);
                touchingFaceGeometry.setIndex(new THREE.BufferAttribute(touchingFaceIndices, 1));
                const touchingFaceMaterial = new THREE.MeshBasicMaterial({
                    vertexColors: true,
                    // flatShading: true, // this disables vertex interpolation, also known as Blending Does not exist in our version of THREE
                    side: THREE.DoubleSide //ensure backface shows color too
                });
                const touchingFace = new THREE.Line(touchingFaceGeometry, touchingFaceMaterial);
                this.add(touchingFace);//this.attach(touchingFace);
                uuid__type[touchingFace.uuid] = 'TOUCHING_BOX';
                solderableLeadsIdx_touchingBoxesIdx__attachmentId[[i, j]] = touchingFace.uuid;
                attachmentId__solderableLeadsIdx_touchingBoxesIdx[touchingFace.uuid] = [i, j];
            }
        }
        this.solderableLeadsIdx_touchingBoxesIdx__attachmentId = solderableLeadsIdx_touchingBoxesIdx__attachmentId;
        this.attachmentId__solderableLeadsIdx_touchingBoxesIdx = attachmentId__solderableLeadsIdx_touchingBoxesIdx;
        this.uuid__type = uuid__type;
        //



        // keep this Line as well
        const material = new THREE.LineBasicMaterial( { color: this.wireColor } );
        const points = [];
        for (let i=0; i<wirePath.length; i++) {
            points.push( new THREE.Vector3( wirePath[i][0], wirePath[i][1], wirePath[i][2] ) );
        }
        // console.log('points');console.log(points);
        const geometry = new THREE.BufferGeometry().setFromPoints( points );
        const line = new THREE.Line( geometry, material );
        this.add(line);
        // super(geometry, material);

        const tubeMaterial = new THREE.MeshBasicMaterial({ color: this.wireColor });
        const wirePathCurve = new WirePathCurve(wirePath);
        wirePathCurve.arcLengthDivisions = 1;
        // wirePathCurve.arcLengthDivisions = wirePath.length-1;
        // console.log('wirePath.length', wirePath.length);
        // const tubeGeometry = new THREE.TubeGeometry(wirePathCurve, wirePath.length-1, radius, 12, false);//not working very well, doesn't draw orthogonally
        const tubeGeometry = new THREE.TubeGeometry(wirePathCurve, 128, radius, 12, false);//TODO adjust 128 accounting to total_length of wirePath.
        
        const tube = new THREE.Mesh(tubeGeometry, tubeMaterial);
        // this.mainMeshUUID = [tube.uuid];
        this.addMainMesh(tube.uuid)
        // console.log('tubeGeometry.vertices: ', tube.geometry.getAttribute('position').array);
        this.add(tube);


        
        this.tF0 = tF0; this.tF1 = tF1; this.solderableLeadIdx0 = solderableLeadIdx0; this.solderableLeadIdx1 = solderableLeadIdx1;
    }


    /**
     * Get all disjoint mainMeshes
     * **/
    getAllMainMeshes() {
        const disjointMainMeshes = []; let disjointMesh;
        this.mainMeshUUID.forEach(meshUUID => {
            disjointMesh = this.getObjectByProperty('uuid', meshUUID);
            disjointMainMeshes.push(disjointMesh)
        })
        return disjointMainMeshes
    }
    /**
     * get all touchingBoxes
     * 
     * used by ConnectionConstructor
     * **/
    getAllTouchingBoxesAndInsertVectors() {
        let updatedSolderableLeads = [];
        for ( let i = 0; i < this.solderableLeads.length; i ++ ) {
            let touchingBoxes = this.solderableLeads[i];
            let updatedSolderableLead = [];
            for ( let j = 0; j < touchingBoxes.length; j ++ ) {
                let touchingBoxAttachmentId = this.solderableLeadsIdx_touchingBoxesIdx__attachmentId[[i, j]];
                let touchingBox = this.getObjectByProperty('uuid', touchingBoxAttachmentId);//is THREE.Line
                updatedSolderableLead.push({
                    'touchingBox':this.updateListOfCoordinates(touchingBox)
                });
            }
            updatedSolderableLeads.push(updatedSolderableLead);
        }
        return updatedSolderableLeads;
    }


    /**
     * get touchPoint of solderableIdx, in javascript array [x, y, z]
     * **/
    getTouchPoint(solderableIdx) {
        let point = this.getObjectByProperty('uuid', this.solderableIdx__touchPointUUID[solderableIdx]);
        return this.updateListOfCoordinates(point)[0];
    }


    /**
     * hides the touchingBoxes
     * **/
    setAllTouchingBoxVisibility(visible) {
        for ( let i = 0; i < this.solderableLeads.length; i ++ ) {
            let touchingBoxes = this.solderableLeads[i];
            let updatedSolderableLead = [];
            for ( let j = 0; j < touchingBoxes.length; j ++ ) {
                let touchingBoxAttachmentId = this.solderableLeadsIdx_touchingBoxesIdx__attachmentId[[i, j]];
                let touchingBox = this.getObjectByProperty('uuid', touchingBoxAttachmentId);//is THREE.Line
                touchingBox.visible=visible;
            }
        }
    }

    /**
     * Converts THREE.Object3D.geometry.position.array to a Javascript.Array of [x, y, z]; where x, y, z are Javascript floats
     * 
     * used by ConnectionConstructor
     * **/
    updateListOfCoordinates(threeObject3D) {
        threeObject3D.geometry.computeBoundingBox(); threeObject3D.updateMatrixWorld(true);
        const pointsList = this.threeFloatsToAPoint(threeObject3D.geometry.getAttribute('position').array);
        const updatedPoints = [];
        for(let i=0; i<pointsList.length; i++) {
            const oldPoint = new THREE.Vector3(pointsList[i][0], pointsList[i][1],pointsList[i][2]);
            const updatedPoint = oldPoint.clone().applyMatrix4(threeObject3D.matrixWorld);
            updatedPoints.push([updatedPoint.x, updatedPoint.y, updatedPoint.z]);
        }
        return updatedPoints;
    }
    /**
     * A list of floats, whose amount is divisible by 3. Rearrange every 3 floats into a coordinate point.
     * 
     * used by ConnectionConstructor
     * **/
    threeFloatsToAPoint(coordinates) {
        const points = []; let point = [];
        for (let i=0; i<coordinates.length; i++) {
            point.push(coordinates[i]);
            if (i%3 == 2) {
                points.push(point); point = [];
            }
        }
        return points;
    }


}

class WirePathCurve extends THREE.Curve {//TODO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<display is not very good yet...., not sure why?
    //Maybe learn how QuadraticBezierCurve3 implements a THREE.Curve ???
    constructor(wirePath) {
        super();
        this.wirePath = wirePath;
        //calculate length of wirePath

        this.totalLenOfWire = 0;
        this.list_minSegmentLen_wirePathIdx = [[0.0, 0]]
        for(let i=0; i<this.wirePath.length-1; i++) {
            this.totalLenOfWire += this.distance(this.wirePath[i], this.wirePath[i+1]);
            this.list_minSegmentLen_wirePathIdx.push([this.totalLenOfWire, i+1])// in increasing order of tup[0]
        }
        // console.log('~~~~~~~~~~~~~~~~~');
        // console.log('this.list_minSegmentLen_wirePathIdx', this.list_minSegmentLen_wirePathIdx);
        // console.log('this.totalLenOfWire', this.totalLenOfWire);
        // console.log('~~~~~~~~~~~~~~~~~');
        // this.numberOfTimesZeroWasCalled = -1;//This is equivalent to SegmentIdx
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

    getRealPosition(t) {
        if(t ==1) { t = t-0.0001}

        const actualT = t * this.totalLenOfWire;
        let startIdx = 0; let endIdx = 1; let minLen = this.list_minSegmentLen_wirePathIdx[0][0]
        for(let i=0; i<this.list_minSegmentLen_wirePathIdx.length; i++) {
            if (actualT<this.list_minSegmentLen_wirePathIdx[i][0]) {
                startIdx = this.list_minSegmentLen_wirePathIdx[i][1]-1; endIdx = this.list_minSegmentLen_wirePathIdx[i][1];
                minLen = this.list_minSegmentLen_wirePathIdx[i-1][0];
                // console.log('GOT!!!!!')
                break
            }
        }
        const startPoint = this.wirePath[startIdx]; const endPoint = this.wirePath[endIdx];
        const segmentLength = this.distance(startPoint, endPoint);
        // const directionalVec = [endPoint[0]-startPoint[0], endPoint[1]-startPoint[1], endPoint[2]-startPoint[2]];
        const s = ((actualT - minLen)/segmentLength);
        const aa = [
            startPoint[0]+s*(endPoint[0]-startPoint[0]),
            startPoint[1]+s*(endPoint[1]-startPoint[1]),
            startPoint[2]+s*(endPoint[2]-startPoint[2]),
        ];
        // console.log('~~~~~~~~~~~~~~~~~~~~');
        // console.log('t', t)
        // console.log('actualT', actualT)
        // console.log('startPoint: ', startPoint);
        // console.log('endPoint: ', endPoint);
        // console.log('directionalVec: ', [(endPoint[0]-startPoint[0]), (endPoint[1]-startPoint[1]), (endPoint[2]-startPoint[2])])
        // console.log('minLen', minLen);
        // console.log('segmentLength: ', segmentLength);
        // console.log('s', s);
        // console.log('aa', aa);
        // console.log('~~~~~~~~~~~~~~~~~~~~')
        return aa
    }

    /**
     * Used by line 37273 three.core.js 
     * 
     * t must be between 0 and 1
     * 
     * TODO we are not doing the bends for now. 
     * For bends, use THREE.ArcCurve to make the bend_shape
     * **/
    getPoint(t, optionalTarget = new THREE.Vector3()) {//line 37273 three.core.js
        const point = optionalTarget;
        const positionArray = this.getRealPosition(t);
        point.set(
            positionArray[0], positionArray[1], positionArray[2]
        );
        return point

    }
}

export {Wire};