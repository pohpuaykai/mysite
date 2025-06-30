
import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {ComponentResistor} from '../meshes/ComponentResistor.js';
import {ComponentBattery} from '../meshes/ComponentBattery.js';
import {Piece} from './piece.js';
import {Wire} from '../meshes/Wire.js';

class DCTwoResistorParallel extends Piece {

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

        function animate(){

        // let rotatingObject = resistor0;
        // rotatingObject.rotation.x += (Math.PI/(360*6));
        // rotatingObject.rotation.y += (Math.PI/(360*6));
        // rotatingObject.rotation.z += (Math.PI/(360*6));
        // render();
            
        }

        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
            'meshes':{
                'resistor0':resistor0,
                'battery0':battery0,
                'resistor1':resistor1,
                'wireBetween01':wireBetween01,
                'wireBetween10':wireBetween10,
                'wireBetween11':wireBetween11,
                'wireBetween00':wireBetween00
            },
            'animate':animate
        }

    }

    
}

export {DCTwoResistorParallel};