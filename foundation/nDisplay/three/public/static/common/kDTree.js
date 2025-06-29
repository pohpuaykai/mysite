class kDTree {
    
    constructor(listOfPoints=[]) {
        if (listOfPoints.length > 0) {
            this.D = listOfPoints[0].length;
            this.rootNode = new Node(listOfPoints[0], 0);
            //TODO the order could be better to make this tree more balanced.
            for (let i=0; i<listOfPoints.length; i++) {
                const point = listOfPoints[i];
                this.rootNode.insert(point)
            }
        } else {
            this.D = null; this.rootNode = null;
        }

        //
        this.nearestNeighbourDistance = Number.MAX_VALUE;
        this.nearestNeighbourElement = null;
    }

    insert(point) {
        if (this.D == null) {
            this.D = point.length;
            this.rootNode = new Node(point, 0);
        } else {
            this.rootNode.insert(point);
        }
    }

    nearestNeighbour(searchPoint) {
        let nearestNeighbourElement; let nearestNeighbourDistance;
        [nearestNeighbourElement, nearestNeighbourDistance] = this._rNearestNeighbour(this.rootNode, searchPoint);
        return {'nearestNeighbour':nearestNeighbourElement.data, 'nearestNeighbourDistance':Math.sqrt(nearestNeighbourDistance)};
    }

    _rNearestNeighbour(root, searchPoint) {
        //Courtesy of Stable Sort of Youtube
        if (root == null) {
            return [null, Number.MAX_VALUE];
        }
        let nextBranch
        let otherBranch
        if (searchPoint[root.dIdx] < root[root.dIdx]) {
            nextBranch = root.leftNode;
            otherBranch = root.rightNode;
        } else {
            nextBranch = root.rightNode;
            otherBranch = root.leftNode;
        }

        let tempNode; let radiusSquaredTemp;
        [tempNode, radiusSquaredTemp] = this._rNearestNeighbour(nextBranch, searchPoint);
        if (tempNode != null) {
            // let radiusSquaredTemp = 0;//tempNode versus searchPoint
            let radiusSquaredRoot = 0;//root versus searchPoint
            // console.log('tempNode:', tempNode.data);
            // for (let i=0; i<this.D; i++) {
            //     radiusSquaredTemp += (tempNode.data[i]-searchPoint[i])*(tempNode.data[i]-searchPoint[i]);
            // }
            for (let i=0; i<this.D; i++) {
                radiusSquaredRoot += (root.data[i]-searchPoint[i])*(root.data[i]-searchPoint[i]);
            }
            //
            let bestNode; let bestDistanceSquared;
            if (radiusSquaredTemp < radiusSquaredRoot) {
                bestNode = tempNode; bestDistanceSquared = radiusSquaredTemp
            } else {
                bestNode = root; bestDistanceSquared = radiusSquaredRoot;
            }
            //

            const dimensionDistance = Math.abs(tempNode[root.dIdx]-searchPoint[root.dIdx]);

            if (bestDistanceSquared >= dimensionDistance * dimensionDistance) {
                let tempNode; let radiusSquaredTemp;
                [tempNode, radiusSquaredTemp] = this._rNearestNeighbour(otherBranch, searchPoint);
                if (tempNode != null) {
                    // let radiusSquaredTemp = 0;//tempNode versus searchPoint
                    let radiusSquaredRoot = 0;//root versus searchPoint
                    // for (let i=0; i<this.D; i++) {
                    //     radiusSquaredTemp += (tempNode.data[i]-searchPoint[i])*(tempNode.data[i]-searchPoint[i]);
                    // }
                    for (let i=0; i<this.D; i++) {
                        radiusSquaredRoot += (root.data[i]-searchPoint[i])*(root.data[i]-searchPoint[i]);
                    }
                    //
                    let bestNode; let bestDistanceSquared;
                    if (radiusSquaredTemp < radiusSquaredRoot) {
                        bestNode = tempNode; bestDistanceSquared = radiusSquaredTemp
                    } else {
                        bestNode = root; bestDistanceSquared = radiusSquaredRoot;
                    }
                }
            }
            // console.log('bestNode'); console.log(bestNode.data, bestDistanceSquared);
            return [bestNode, bestDistanceSquared];
        } else {

            let radiusSquaredRoot = 0;//root versus searchPoint
            for (let i=0; i<this.D; i++) {
                radiusSquaredRoot += (root.data[i]-searchPoint[i])*(root.data[i]-searchPoint[i]);
            }
            // console.log('best is root'); console.log(root.data, radiusSquaredRoot);
            return [root, radiusSquaredRoot];
        }
    }
}


class Node {
    
    constructor(data, dIdx) {
        this.data = data;
        this.dIdx = dIdx;
        this.leftNode = null;
        this.rightNode = null;
    }

    insert(data) {
        if (data[this.dIdx] < this.data[this.dIdx]) {
            if (this.leftNode == null) {
                this.leftNode = new Node(data, (this.dIdx+1)%data.length);
            } else {
                this.leftNode.insert(data);
            }
        } else {
            if (this.rightNode == null) {
                this.rightNode = new Node(data, (this.dIdx+1)%data.length);
            } else {
                this.rightNode.insert(data);
            }
        }
    }
}

export {kDTree};