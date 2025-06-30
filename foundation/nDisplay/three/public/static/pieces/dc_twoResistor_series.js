
import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {ComponentResistor} from '../meshes/ComponentResistor.js';
import {ComponentBattery} from '../meshes/ComponentBattery.js';
import {Wire} from '../meshes/Wire.js';

class DCTwoResistorSeries {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, meshes) {

        this.scene = scene;
        this.camera = camera;
        this.renderer = renderer;
        this.meshes = meshes;

    }

    act() {

        //
        const self = this;
        function render() {
            self.renderer.render(self.scene, self.camera);
        }
        //

        const resistor0 = new ComponentResistor({x:0, y:0, z:-20});
        this.scene.add(resistor0); render();

        const battery0 = new ComponentBattery({x:0, y:0, z:10});
        this.scene.add(battery0); render();

        const resistor1 = new ComponentResistor({x:15, y:0, z:-20});
        this.scene.add(resistor1); render();

        const wireBetween01 = new Wire(resistor0, battery0, 1.024);//AWG18
        this.scene.add(wireBetween01); render();
        // console.log(wireBetween01.solderableLeadIdx0); console.log(wireBetween01.solderableLeadIdx1);

        const wireBetween10 = new Wire(resistor0, resistor1, 1.024, 1, 0);//AWG18
        this.scene.add(wireBetween10); render();

        const wireBetween11 = new Wire(battery0, resistor1, 1.024, 1, 1);//AWG18
        this.scene.add(wireBetween11); render();

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
                'wireBetween11':wireBetween11
            },
            'animate':animate
        }

    }
    
}

export {DCTwoResistorSeries};