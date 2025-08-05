
import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {ComponentResistor} from '../meshes/ComponentResistor.js';
import {ComponentBattery} from '../meshes/ComponentBattery.js';
import {Circuit} from './circuit.js';
import {Wire} from '../meshes/Wire.js';

class DCTwoResistorParallel extends Circuit {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, meshes) {
        super(scene, camera, renderer, meshes);
    }

    act() {

        const resistor0 = new ComponentResistor({x:0, y:-5, z:-20});
        this.scene.add(resistor0); this.render();

        const battery0 = new ComponentBattery({x:0, y:0, z:10});
        this.scene.add(battery0); this.render();

        const resistor1 = new ComponentResistor({x:0, y:5, z:-20});
        this.scene.add(resistor1); this.render();

        /**
         * Wire is also a NODE in summarised graph|network?, then Wire.js must have 
         * getAllTouchingBoxesAndInsertVectors -> Wire.js needs to have diameter and length, albeit in Segments
         * **/

        const wireBetween01 = this.wire(resistor0, resistor1, 1.024);

        const wireBetween10 = this.wire(resistor0, resistor1, 1.024, 1, 1);

        const wireBetween11 = this.wire(battery0, wireBetween10, 1.024, 1);

        const wireBetween00 = this.wire(battery0, wireBetween01, 1.024, 0);

        //get Equations and solving steps:
        const dependentUUID = resistor0.uuid;
        const list_independentUUID = [battery0.uuid, resistor1.uuid];
        const dependentVarType = 'voltage';
        const list_independentVarType = ['voltage', 'voltage'];
        function meshToAnimation(mesh) {
            return function() {
                if (mesh.position.y > 120) {
                    mesh.visible = false;
                } else {
                    mesh.position.y += 0.1;
                }
            }
        }
        this.animate_getAllEquationsAndASolvingStep(meshToAnimation, dependentUUID, list_independentUUID, dependentVarType, list_independentVarType);

        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
            // 'meshes':{
            //     'resistor0':resistor0,
            //     'battery0':battery0,
            //     'resistor1':resistor1,
            //     'wireBetween01':wireBetween01,
            //     'wireBetween10':wireBetween10,
            //     'wireBetween11':wireBetween11,
            //     'wireBetween00':wireBetween00
            // },
            // 'animate':animate
        }

    }

    
}

export {DCTwoResistorParallel};