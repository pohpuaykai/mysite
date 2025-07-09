import {Wire} from '../meshes/Wire.js';

class Piece {
    
    /**
     * 
     * **/
    constructor(scene, camera, renderer, meshes) {

        this.scene = scene;
        this.camera = camera;
        this.renderer = renderer;
        this.meshes = meshes;
        this.wiring = [];
        this.wiringSansWires = [];
        this.uuid__type = {};
        this.uuid__positiveLeadsDirections = {};
        this.edgeUUID__solderableIndices = {};
        this.edge__solderableIndices = {};

        this.type__boundingBox = {};//<<<<<<<<<<<<<put into one endpoint, then query

        //getBBox of each schematic size
        function getBBoxFromSVGString(svgString) {

            // Parse the SVG string
            const parser = new DOMParser();
            const svgDoc = parser.parseFromString(svgString, "image/svg+xml");
            const svgElement = svgDoc.documentElement;

            // Append to DOM (hidden)
            svgElement.style.position = "absolute";
            svgElement.style.visibility = "hidden";
            svgElement.style.pointerEvents = "none";
            svgElement.style.width = "auto";
            svgElement.style.height = "auto";
            document.body.appendChild(svgElement);

            // Now getBBox
            const bbox = svgElement.getBBox();
            console.log(bbox);

            // Optional: clean up
            svgElement.remove();
            return bbox;

        }
        let componenttypeSVGFilepath_ajax = new XMLHttpRequest(); this.componentType__boundingBox = {}; const self = this;
        componenttypeSVGFilepath_ajax.addEventListener("load", function() {
            const componenttype__svgfilepath___str = componenttypeSVGFilepath_ajax.responseText;
            const COMPONENTTYPE__SVGFILEPATH___entries = Object.entries(JSON.parse(componenttype__svgfilepath___str));
            console.log(COMPONENTTYPE__SVGFILEPATH___entries);
            let componentType; let svgFilepath;let absolutePath;
            for (let i=0; i<COMPONENTTYPE__SVGFILEPATH___entries.length; i++) {
                // if (COMPONENTTYPE__SVGFILEPATH___entries[i] != undefined) { //https://developer.mozilla.org/en-US/docs/Web/API/SVGGraphicsElement/getBBox
                    [componentType, svgFilepath] = COMPONENTTYPE__SVGFILEPATH___entries[i];
                    absolutePath = '/public/static/'+svgFilepath;
                    let ajax = new XMLHttpRequest();
                    ajax.addEventListener("load", function(componentType) {
                        return function () {
                            // console.log(ajax.responseText);
                            let svgString = ajax.responseText;
                            let svgBBox = getBBoxFromSVGString(svgString);
                            console.log(componentType, svgBBox);
                            // self.componentType__boundingBox[componentType] = svgBBox;
                            self.componentType__boundingBox[componentType] = {'width':svgBBox.width, 'height':svgBBox.height};
                            // console.log('componentType__boundingBox', JSON.stringify(self.componentType__boundingBox));
                        }
                    }(componentType));
                    console.log(componentType, absolutePath);
                    ajax.open("GET", absolutePath);
                    ajax.send();
            }
        });
        componenttypeSVGFilepath_ajax.open("GET", "/public/static/settings/ComponentType__SVGFilepath.json");//hide this link?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        componenttypeSVGFilepath_ajax.send();
    }

    /**
     * 
     * @abstract
     * @return a dictionary mapping from localFunction variable_names to variables (
     *  scene
     *  camera
     *  renderer
     *  meshes - a dictionary of variables_names to variables (meshes)
     *  animate - function for renderer.setAnimationLoop on main.js
     * )
     * **/
    act() {
        console.warn( ': .act() not implemented.' );
    }

    render() {
        this.renderer.render(this.scene, this.camera);

    }

    wire(component0, component1, wireRadius, solderableLeadIdx0=null, solderableLeadIdx1=null) {

        const wireBetween = new Wire(component0, component1, wireRadius, solderableLeadIdx0, solderableLeadIdx1);//AWG18
        if (solderableLeadIdx0 === null) {
            solderableLeadIdx0 = wireBetween.solderableLeadIdx0
        }
        if (solderableLeadIdx1 === null) {
            solderableLeadIdx1 = wireBetween.solderableLeadIdx1
        }
        this.scene.add(wireBetween); this.render();
        // this.wiring.push([component0.uuid, wireBetween.uuid, solderableLeadIdx0]);
        // this.wiring.push([component1.uuid, wireBetween.uuid, solderableLeadIdx1]);
        let networkGraph = {};
        if ((component0.type == 'wire') || (component1.type == 'wire')) {
            //construct dictionary_list of this.wiring
            let component0_uuid; let component1_uuid;
            for (let i=0; i<this.wiring.length; i++) {
                // [component0_uuid, component1_uuid, component0_solderableIdx] = this.wiring[i];
                [component0_uuid, component1_uuid] = this.wiring[i];
                //
                let existingNeighbours = networkGraph[component0_uuid];
                if (existingNeighbours===undefined) {
                    existingNeighbours = [];
                }
                existingNeighbours.push(component1_uuid);
                networkGraph[component0_uuid] = existingNeighbours;
                //
                //
                existingNeighbours = networkGraph[component1_uuid];
                if (existingNeighbours===undefined) {
                    existingNeighbours = [];
                }
                existingNeighbours.push(component0_uuid);
                networkGraph[component1_uuid] = existingNeighbours;
                //
            }
            //BFS this.wiring(list_of_edges) from component0, if child is non-wire add to this.wiringSansWires, and do not add to queue
            if (component0.type == 'wire') {
                const queue = [component0.uuid]; const visited = [component0.uuid]; const noWireNeighbours = [];
                while (queue.length > 0) {
                    const current = queue.shift(); const neighbours = networkGraph[current];
                    for (let i=0; i<neighbours.length; i++) {
                        const neighbour = neighbours[i];
                        if (this.uuid__type[neighbour] == 'wire') {
                            if (visited.indexOf(neighbour) == -1) {
                                queue.push(neighbour); visited.push(neighbour);
                            }
                        } else {
                            noWireNeighbours.push(neighbour); visited.push(neighbour);
                        }
                    }
                }
                for (let i=0; i<noWireNeighbours.length; i++) {//component1 is not wire, since cannot be both wires.... <<<<<<<<need to check and throw ?
                    const noWireNeighbour = noWireNeighbours[i];
                    this.wiringSansWires.push([noWireNeighbour, component1.uuid]);
                    this.wiringSansWires.push([component1.uuid, noWireNeighbour]);
                }
            }

            if (component1.type == 'wire') {
                const queue = [component1.uuid]; const visited = [component0.uuid]; const noWireNeighbours = [];
                while(queue.length > 0) {
                    const current = queue.shift(); const neighbours = networkGraph[current];
                    for (let i=0; i<neighbours.length; i++) {
                        const neighbour = neighbours[i];
                        if (this.uuid__type[neighbour] == 'wire') {
                            if (visited.indexOf(neighbour) == -1) {
                                queue.push(neighbour); visited.push(neighbour);
                            }
                        } else {
                            noWireNeighbours.push(neighbour); visited.push(neighbour);
                        }
                    }
                }
                for (let i=0; i<noWireNeighbours.length; i++) {//component0 is not wire, since cannot be both wires.... <<<<<<<<need to check and throw ?
                    const noWireNeighbour = noWireNeighbours[i];
                    this.wiringSansWires.push([noWireNeighbour, component0.uuid]);
                    this.wiringSansWires.push([component0.uuid, noWireNeighbour]);
                }
            }
        } else {
            this.wiringSansWires.push([component0.uuid, component1.uuid]);
        }


        this.wiring.push([component0.uuid, wireBetween.uuid]);
        this.wiring.push([component1.uuid, wireBetween.uuid]);
        this.uuid__type[component0.uuid] = component0.type;
        this.uuid__type[component1.uuid] = component1.type;
        this.uuid__type[wireBetween.uuid] = wireBetween.type;
        this.uuid__positiveLeadsDirections[component0.uuid] = component0.positiveLeadsDirections;
        this.uuid__positiveLeadsDirections[component1.uuid] = component1.positiveLeadsDirections;
        this.uuid__positiveLeadsDirections[wireBetween.uuid] = wireBetween.positiveLeadsDirections;
        //edgeUUID, is undirected, so need both sides, solderableLeadIdx is directed, so only one side
        this.edgeUUID__solderableIndices[[component0.uuid, wireBetween.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        this.edgeUUID__solderableIndices[[wireBetween.uuid, component0.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        this.edgeUUID__solderableIndices[[component1.uuid, wireBetween.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        this.edgeUUID__solderableIndices[[wireBetween.uuid, component1.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        // also add the connection without wire for some equationFinders ignore wire.... TODO maybe a seperate dictionary to prevent confusion?
        
        this.edgeUUID__solderableIndices[[component0.uuid, component1.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        this.edgeUUID__solderableIndices[[component1.uuid, component0.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        return wireBetween
    }

    getNetworkGraph() {
        //simplify uuid 
        this.uuid__id = {}; this.id__uuid = {}; this.id__type = {}; this.id__positiveLeadsDirections = {};
        const uuid__typeEntries = Object.entries(this.uuid__type);let uuid; let type;
        // console.log(uuid__typeEntries);
        for (let i=0; i<uuid__typeEntries.length; i++) {
            [uuid, type] = uuid__typeEntries[i];
            // console.log(uuid, type)
            this.uuid__id[uuid] = i; this.id__uuid[i] = uuid; this.id__type[i] = this.uuid__type[uuid];
            this.id__positiveLeadsDirections[i] = this.uuid__positiveLeadsDirections[uuid];
        }
        // console.log('this.edgeUUID__solderableIndices', this.edgeUUID__solderableIndices);
        const edgeUUID__solderableIndicesEntries = Object.entries(this.edgeUUID__solderableIndices); let uuidDelimitedByComma; let component0_uuid; let component1_uuid; let solderableLeadIdx0; let solderableLeadIdx1;
        // console.log('edgeUUID__solderableIndicesEntries', edgeUUID__solderableIndicesEntries)
        for (let i=0; i<edgeUUID__solderableIndicesEntries.length; i++) {
            [uuidDelimitedByComma, [solderableLeadIdx0, solderableLeadIdx1]] = edgeUUID__solderableIndicesEntries[i];
            [component0_uuid, component1_uuid] = uuidDelimitedByComma.split(',');
            // console.log('uuidDelimitedByComma', uuidDelimitedByComma, 'solderableLeadIdx0', solderableLeadIdx0, 'solderableLeadIdx1', solderableLeadIdx1);
            this.edge__solderableIndices[this.uuid__id[component0_uuid]+","+this.uuid__id[component1_uuid]] = [solderableLeadIdx0, solderableLeadIdx1]
        }
        // console.log('this.edge__solderableIndices', this.edge__solderableIndices);

        //find networkGraphNoWires
        console.log('wiringSansWires:', this.wiringSansWires);
        this.networkGraphNoWires = {};
        for (let i=0; i<this.wiringSansWires.length; i++) {
            [component0_uuid, component1_uuid] = this.wiringSansWires[i];
            console.log(this.uuid__id[component0_uuid], this.uuid__id[component1_uuid]);
            //
            let existingNeighbours = this.networkGraphNoWires[this.uuid__id[component0_uuid]];
            if (existingNeighbours===undefined) {
                existingNeighbours = [];
            }
            if (existingNeighbours.indexOf(this.uuid__id[component1_uuid]) == -1) {
                console.log('parent:', this.uuid__id[component0_uuid], 'existingNeighbours', existingNeighbours, 'adding:', this.uuid__id[component1_uuid]);
                existingNeighbours.push(this.uuid__id[component1_uuid]);
            }
            this.networkGraphNoWires[this.uuid__id[component0_uuid]] = existingNeighbours;
            //
            //
            existingNeighbours = this.networkGraphNoWires[this.uuid__id[component1_uuid]];
            if (existingNeighbours===undefined) {
                existingNeighbours = [];
            }
            if (existingNeighbours.indexOf(this.uuid__id[component0_uuid]) == -1) {
                console.log('parent:', this.uuid__id[component1_uuid], 'existingNeighbours', existingNeighbours, 'adding:', this.uuid__id[component0_uuid]);
                existingNeighbours.push(this.uuid__id[component0_uuid]);
            }
            this.networkGraphNoWires[this.uuid__id[component1_uuid]] = existingNeighbours;
            //
        }
        console.log('this.networkGraphNoWires', this.networkGraphNoWires); console.log('*************************************************')

        // console.log(this.uuid__id); console.log(this.id__uuid);
        let networkGraph = {}; let idNetworkGraph = {}; let id__type = {};
        // let component0_uuid; let component1_uuid; 
        // let component0_solderableIdx;//component1 is the wire
        for (let i=0; i<this.wiring.length; i++) {
            // [component0_uuid, component1_uuid, component0_solderableIdx] = this.wiring[i];
            [component0_uuid, component1_uuid] = this.wiring[i];
            //
            let existingNeighbours = networkGraph[this.uuid__id[component0_uuid]];
            if (existingNeighbours===undefined) {
                existingNeighbours = [];
            }
            if (existingNeighbours.indexOf(this.uuid__id[component1_uuid]) == -1 ) {
                existingNeighbours.push(this.uuid__id[component1_uuid]);
            }
            networkGraph[this.uuid__id[component0_uuid]] = existingNeighbours;
            //
            //
            existingNeighbours = networkGraph[this.uuid__id[component1_uuid]];
            if (existingNeighbours===undefined) {
                existingNeighbours = [];
            }
            if (existingNeighbours.indexOf(this.uuid__id[component0_uuid]) == -1) {
                existingNeighbours.push(this.uuid__id[component0_uuid]);
            }
            networkGraph[this.uuid__id[component1_uuid]] = existingNeighbours;
            //
        }
        this.networkGraph = networkGraph;
        return networkGraph;
    }
}

export {Piece};