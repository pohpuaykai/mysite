
import {asyncCreateTextMesh} from '../../custom/TextMeshCreater.js';
import {Circuit} from '../circuit.js';
import {Wire} from '../../meshes/Wire.js';

class Q2_3_5_aMoreComplexCircuit__P84 extends Circuit {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, controls, meshes) {
        super(scene, camera, renderer, controls, meshes);
    }

    act() {

        const battery0 = this.createComponent({componentName:'battery', position:{x:0, y:0, z:10}});
        this.enter(battery0.uuid);
        // this.scene.add(battery0); 
        battery0.setAllTouchingBoxVisibility(false);//this.render();
        console.log('battery0'); console.log(battery0.uuid);


        
        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }
    
}

export {Q3_21__P18};