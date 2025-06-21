class kDTree {
    
    constructor(listOfPoints) {
        //listOfPoints should not be empty
        this.D = listOfPoints[0].length;
        this.rootNode = Node(listOfPoints[0], 0);
        //TODO the order could be better to make this tree more balanced.
        for (let i=0; i<listOfPoints.length; i++) {
            const point = listOfPoints[i];
            this.rootNode.insert(point)
        }

        //
        this.nearestNeighbourDistance = Number.MAX_VALUE;
        this.nearestNeighbour = null;
    }

    nearestNeighbour(searchPoint) {
        _rNearestNeighbour(this.rootNode, searchPoint);
        return {'nearestNeighbour':this.nearestNeighbour, 'nearestNeighbourDistance':nearestNeighbourDistance};
    }

    _rNearestNeighbour(root, searchPoint) {
        //Courtesy of Stable Sort of Youtube
        let nextBranch
        let otherBranch
        if (searchPoint[root.dIdx] < root[root.dIdx]) {
            nextBranch = root.leftNode;
            otherBranch = root.rightNode;
        } else {
            nextBrach = root.rightNode;
            otherBranch = root.leftNode;
        }

        const tempNode = this.nearestNeighbour(nextBranch, searchPoint);

        const radiusSquared = 0;
        for (let i=0; i<this.D; i++) {
            radiusSquared += (tempNode[i]-searchPoint[i])*(tempNode[i]-searchPoint[i]);
        }
        //
        if (radiusSquared < this.nearestNeighbourDistance) {
            this.nearestNeighbour = tempNode;
        }
        //

        const dimensionDistance = Math.abs(tempNode[root.dIdx]-searchPoint[root.dIdx]);

        if (radiusSquared >= dimensionDistance * dimensionDistance) {
            const tempNode = this.nearestNeighbour(otherBranch, searchPoint);
            const radiusSquared = 0;
            for (let i=0; i<this.D; i++) {
                radiusSquared += (tempNode[i]-searchPoint[i])*(tempNode[i]-searchPoint[i]);
            }
            if (radiusSquared < this.nearestNeighbourDistance) {
                this.nearestNeighbour = tempNode;
            }
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