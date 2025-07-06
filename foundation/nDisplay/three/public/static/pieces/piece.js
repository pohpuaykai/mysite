
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
        this.uuid__type = {};
        this.uuid__positiveLeadsDirections = {};
        this.edgeUUID__solderableIndices = {};
        this.edge__solderableIndices = {};
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
        this.wiring.push([component0.uuid, wireBetween.uuid, solderableLeadIdx0]);
        this.wiring.push([component1.uuid, wireBetween.uuid, solderableLeadIdx1]);
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
        console.log('this.edgeUUID__solderableIndices', this.edgeUUID__solderableIndices);
        const edgeUUID__solderableIndicesEntries = Object.entries(this.edgeUUID__solderableIndices); let uuidDelimitedByComma; let component0_uuid; let component1_uuid; let solderableLeadIdx0; let solderableLeadIdx1;
        console.log('edgeUUID__solderableIndicesEntries', edgeUUID__solderableIndicesEntries)
        for (let i=0; i<edgeUUID__solderableIndicesEntries.length; i++) {
            [uuidDelimitedByComma, [solderableLeadIdx0, solderableLeadIdx1]] = edgeUUID__solderableIndicesEntries[i];
            [component0_uuid, component1_uuid] = uuidDelimitedByComma.split(',');
            console.log('uuidDelimitedByComma', uuidDelimitedByComma, 'solderableLeadIdx0', solderableLeadIdx0, 'solderableLeadIdx1', solderableLeadIdx1);
            this.edge__solderableIndices[this.uuid__id[component0_uuid]+","+this.uuid__id[component1_uuid]] = [solderableLeadIdx0, solderableLeadIdx1]
        }
        console.log('this.edge__solderableIndices', this.edge__solderableIndices);

        // console.log(this.uuid__id); console.log(this.id__uuid);
        let networkGraph = {}; let idNetworkGraph = {}; let id__type = {};
        // let component0_uuid; let component1_uuid; 
        let component0_solderableIdx;//component1 is the wire
        for (let i=0; i<this.wiring.length; i++) {
            [component0_uuid, component1_uuid, component0_solderableIdx] = this.wiring[i];
            //
            let existingNeighbours = networkGraph[this.uuid__id[component0_uuid].toString()];
            if (existingNeighbours===undefined) {
                existingNeighbours = [];
            }
            existingNeighbours.push(this.uuid__id[component1_uuid].toString());
            networkGraph[this.uuid__id[component0_uuid]] = existingNeighbours;
            //
            //
            existingNeighbours = networkGraph[this.uuid__id[component1_uuid].toString()];
            if (existingNeighbours===undefined) {
                existingNeighbours = [];
            }
            existingNeighbours.push(this.uuid__id[component0_uuid].toString());
            networkGraph[this.uuid__id[component1_uuid].toString()] = existingNeighbours;
            //
        }
        return networkGraph;
    }
}

export {Piece};