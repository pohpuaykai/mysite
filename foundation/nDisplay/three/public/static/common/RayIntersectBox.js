class RayIntersectBox {
    /**
     * 
     * Coordinate of box has to be in this order:
     * BoxPoint list are in this order (top-square clockwise, and then bottom square, from the same top point, clockwise):
     * (left, up, in), (right, up, in), (right, up, out), (left, up, out),
     * (left, down, in), (right, down, in), (right, down, out), (left, down, out)
     * 
     * 
            const touchingBoxFacesVertexIndices = [
                [0, 1, 2, 3], //top face
                [0, 3, 7, 4], //left face
                [1, 0, 4, 5], //back face
                [2, 1, 5, 6], //right face
                [3, 2, 6, 7], //front face
                [7, 6, 5, 4], //bottom face
            ]
     * **/
    constructor(){}

    /**
     * ray is a THREE.Vector3
     * **/
    facesOfIntersection(boxPointList, origin, ray, faceIntersectionCallback) {//TODO this is not really a ray, because it goes in 2 directions
        // console.log("boxPointList", boxPointList); console.log('origin', origin); console.log('ray', ray);
        const touchingBoxFacesVertexIndices = [
            [0, 1, 2, 3], //top face
            [0, 3, 7, 4], //left face
            [1, 0, 4, 5], //back face
            [2, 1, 5, 6], //right face
            [3, 2, 6, 7], //front face
            [7, 6, 5, 4], //bottom face
        ];
        for (let i=0; i<touchingBoxFacesVertexIndices.length; i++) {
            const faceIndices = touchingBoxFacesVertexIndices[i];
            const topLeft = boxPointList[faceIndices[0]]; const topRight = boxPointList[faceIndices[1]]; const bottomRight = boxPointList[faceIndices[2]]; const bottomLeft = boxPointList[faceIndices[3]];
            const normalVectorOfFaceFarplane = this.normalVector(topLeft, topRight, bottomRight);
            const dotProductOfNormalVectorAndRay = (normalVectorOfFaceFarplane[0]*ray[0])+(normalVectorOfFaceFarplane[1]*ray[1])+(normalVectorOfFaceFarplane[2]*ray[2]);
            if (!this.aEquals(dotProductOfNormalVectorAndRay, 0.0)) {// not perpendicular to normal of farplane, then iV intersects farplane
                console.log('normalVectorOfFaceFarplane', normalVectorOfFaceFarplane); console.log('topLeft:', topLeft);
                const lambda = (normalVectorOfFaceFarplane[0]*(topLeft[0]-origin[0])+normalVectorOfFaceFarplane[1]*(topLeft[1]-origin[1])+normalVectorOfFaceFarplane[2]*(topLeft[2]-origin[2]))/ (normalVectorOfFaceFarplane[0]*ray[0]+normalVectorOfFaceFarplane[1]*ray[1]+normalVectorOfFaceFarplane[2]*ray[2]);
                console.log('lambda',lambda);
                //try calculating lambda with other points, topRight, bottomRight, bottomLeft
                // const lambdaTopRight = (normalVectorOfFaceFarplane[0]*(topRight[0]-origin[0])+normalVectorOfFaceFarplane[1]*(topRight[1]-origin[1])+normalVectorOfFaceFarplane[2]*(topRight[2]-origin[2]))/ (normalVectorOfFaceFarplane[0]*ray[0]+normalVectorOfFaceFarplane[1]*ray[1]+normalVectorOfFaceFarplane[2]*ray[2]);
                // const lambdaBottomRight = (normalVectorOfFaceFarplane[0]*(bottomRight[0]-origin[0])+normalVectorOfFaceFarplane[1]*(bottomRight[1]-origin[1])+normalVectorOfFaceFarplane[2]*(bottomRight[2]-origin[2]))/ (normalVectorOfFaceFarplane[0]*ray[0]+normalVectorOfFaceFarplane[1]*ray[1]+normalVectorOfFaceFarplane[2]*ray[2]);
                // const lambdaBottomLeft = (normalVectorOfFaceFarplane[0]*(bottomLeft[0]-origin[0])+normalVectorOfFaceFarplane[1]*(bottomLeft[1]-origin[1])+normalVectorOfFaceFarplane[2]*(bottomLeft[2]-origin[2]))/ (normalVectorOfFaceFarplane[0]*ray[0]+normalVectorOfFaceFarplane[1]*ray[1]+normalVectorOfFaceFarplane[2]*ray[2]);
                // console.log('lambdaTopRight', lambdaTopRight); //if not all the same, then normal is calculated wrongly
                // console.log('lambdaBottomRight', lambdaBottomRight);
                // console.log('lambdaBottomLeft', lambdaBottomLeft);
                //
                console.log('origin: ', origin); console.log('ray: ', ray);
                const intersectionPoint = [origin[0]+lambda*ray[0], origin[1]+lambda*ray[1], origin[2]+lambda*ray[2]];//intersectionPoint on face as farplane
                console.log("intersectionPoint", intersectionPoint);
                // console.log("intersectionPoint", intersectionPoint); console.log("topLeft", topLeft); console.log("topRight", topRight); console.log("bottomRight", bottomRight); console.log("bottomLeft", bottomLeft);
                if (this.isPointInRectangleOnTheSameFarplane(intersectionPoint, topLeft, topRight, bottomRight, bottomLeft)) {//rectPoints have to go topLeft, topRight, bottomRight, bottomLeft
                    //iVWithMidPoint intersect at this_face_of_wB
                    // wBFacesThatIntersectWithiV.push(faceIndices);
                    // indices_touchingBoxFacesVertexIndices.push(i);
                    console.log('in this rectangle!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!');
                    faceIntersectionCallback(faceIndices);
                }
            }
        }
    }

    normalVector(coplanarPoint0, coplanarPoint1, coplanarPoint2) {
        return [//result of cross_product between (coplanarPoint1-coplanarPoint0) (coplanarPoint2-coplanarPoint0)
            coplanarPoint0[1]*(coplanarPoint1[2]-coplanarPoint2[2])+coplanarPoint1[1]*(coplanarPoint2[2]-coplanarPoint0[2])+coplanarPoint2[1]*(coplanarPoint0[2]-coplanarPoint1[2]),
            coplanarPoint0[2]*(coplanarPoint1[0]-coplanarPoint2[0])+coplanarPoint1[2]*(coplanarPoint2[0]-coplanarPoint0[0])+coplanarPoint2[2]*(coplanarPoint0[0]-coplanarPoint1[0]),
            coplanarPoint0[0]*(coplanarPoint1[1]-coplanarPoint2[1])+coplanarPoint1[0]*(coplanarPoint2[1]-coplanarPoint0[1])+coplanarPoint2[0]*(coplanarPoint0[1]-coplanarPoint1[1]),
        ];
    }

    aEquals(number0, number1) {
        const boundWidth = 0.0001;
        return number0-boundWidth <= number1 && number1 <= number0+boundWidth;
    }

    isPointInRectangleOnTheSameFarplane(point, rectPoint0, rectPoint1, rectPoint2, rectPoint3) {
        const shortestDistanceFromTopSegment = this.shortestDistanceFromPointToLine(rectPoint0, rectPoint1, point);
        const shortestDistanceFromBottomSegment = this.shortestDistanceFromPointToLine(rectPoint2, rectPoint3, point);
        const shortestDistanceFromLeftSegment = this.shortestDistanceFromPointToLine(rectPoint0, rectPoint3, point);
        const shortestDistanceFromRightSegment = this.shortestDistanceFromPointToLine(rectPoint1, rectPoint2, point);
        const rightSegment = [rectPoint1[0]-rectPoint2[0], rectPoint1[1]-rectPoint2[1], rectPoint1[2]-rectPoint2[2]];
        const topSegment = [rectPoint0[0]-rectPoint1[0], rectPoint0[1]-rectPoint1[1], rectPoint0[2]-rectPoint1[2]];
        const rightSegmentLength = this.vectorLength(rightSegment);
        const topSegmentLength = this.vectorLength(topSegment);
        return this.aEquals(shortestDistanceFromTopSegment+shortestDistanceFromBottomSegment, rightSegmentLength) && this.aEquals(shortestDistanceFromLeftSegment+shortestDistanceFromRightSegment, topSegmentLength);
    }

    shortestDistanceFromPointToLine(linePoint0, linePoint1, point) {
        const p0p1 = [linePoint1[0]-linePoint0[0], linePoint1[1]-linePoint0[1], linePoint1[2]-linePoint0[2]];
        const p0p = [linePoint1[0]-point[0], linePoint1[1]-point[1], linePoint1[2]-point[2]];
        const shortestDistance = (p0p1[0]*p0p[0]+p0p1[1]*p0p[1]+p0p1[2]*p0p[2])/this.vectorLength(p0p1);
        return shortestDistance;
    }


    /**
     * Euclidean Distance
     * **/
    vectorLength(v) {
        return Math.sqrt((v[0]*v[0])+(v[1]*v[1])+(v[2]*v[2]));
    }



}

export {RayIntersectBox};