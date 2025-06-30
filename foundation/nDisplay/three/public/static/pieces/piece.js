
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
        return wireBetween
    }

    getNetworkGraph() {
        let networkGraph = {};
        let component0_uuid; let component1_uuid; let component0_solderableIdx;//component1 is the wire
        for (let i=0; i<this.wiring.length; i++) {
            [component0_uuid, component1_uuid, component0_solderableIdx] = this.wiring[i];
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
        return networkGraph;
    }
}

export {Piece};