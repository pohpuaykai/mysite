
import {asyncCreateTextMesh} from '../../custom/TextMeshCreater.js';
import {ComponentResistor} from '../../meshes/ComponentResistor.js';
import {ComponentBattery} from '../../meshes/ComponentBattery.js';
import {Piece} from '../piece.js';
import {Wire} from '../../meshes/Wire.js';

class Q3_21__P18 extends Piece {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, meshes) {
        super(scene, camera, renderer, meshes);
    }

    act() {



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
                // 'resistor0':resistor0,
                // 'battery0':battery0,
                // 'resistor1':resistor1,
                // 'wireBetween01':wireBetween01,
                // 'wireBetween10':wireBetween10,
                // 'wireBetween11':wireBetween11
            },
            'animate':animate
        }

    }
    
}

export {Q3_21__P18};