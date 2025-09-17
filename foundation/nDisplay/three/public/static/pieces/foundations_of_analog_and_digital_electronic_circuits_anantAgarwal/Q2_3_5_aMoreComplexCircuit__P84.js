
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

        const battery0 = this.createComponent({componentName:'battery', position:{x:0, y:0, z:50}, rotation:{x:0, y:0, z:-Math.PI/2}});
        this.enter(battery0.uuid);
        // this.scene.add(battery0); 
        battery0.setAllTouchingBoxVisibility(false);//this.render();
        console.log('battery0', ); //console.log(battery0.uuid);

        const battery0_dimensions = battery0.getDimensions()


        const resistor1 = this.createComponent({componentName:'resistor', position:{x:-(battery0_dimensions.xLen/2), y:(battery0_dimensions.yLen/2), z:50}});
        this.enter(resistor1.uuid); 
        // this.scene.add(resistor1); 
        resistor1.setAllTouchingBoxVisibility(false);//this.render();
        console.log('resistor1'); console.log(resistor1.uuid);
        
        const resistor2 = this.createComponent({componentName:'resistor', position:{x:-(battery0_dimensions.xLen/2)-10, y:0, z:50}, rotation:{x:0, y:0, z:-Math.PI/2}});
        this.enter(resistor2.uuid); 
        // this.scene.add(resistor2); 
        resistor2.setAllTouchingBoxVisibility(false);//this.render();
        console.log('resistor2'); console.log(resistor2.uuid);
        
        const resistor3 = this.createComponent({componentName:'resistor', position:{x:-(battery0_dimensions.xLen)-10, y:(battery0_dimensions.yLen/2), z:50}});
        this.enter(resistor3.uuid); 
        // this.scene.add(resistor3); 
        resistor3.setAllTouchingBoxVisibility(false);//this.render();
        console.log('resistor3'); console.log(resistor3.uuid);
        
        const resistor4 = this.createComponent({componentName:'resistor', position:{x:-(battery0_dimensions.xLen)-20, y:0, z:50}, rotation:{x:0, y:0, z:-Math.PI/2}});
        this.enter(resistor4.uuid); 
        // this.scene.add(resistor4); 
        resistor4.setAllTouchingBoxVisibility(false);//this.render();
        console.log('resistor4'); console.log(resistor4.uuid);
        


        const c = this.createComponent({componentName:'wire', position:{'x': resistor2.position.x, 'y': resistor1.position.y, 'z':50}, additionalInfo:{'radius': 0.644/2}})
        this.enter(c.uuid);
        // this.scene.add(c);
        c.setAllTouchingBoxVisibility(false);
        console.log('c', c);


        const d = this.createComponent({componentName:'wire', position:{'x': resistor2.position.x, 'y': -resistor1.position.y, 'z':50}, additionalInfo:{'radius': 0.644/2}})
        this.enter(d.uuid);
        // this.scene.add(d);
        d.setAllTouchingBoxVisibility(false);
        console.log('d', d);

        this.render();

        //network|connection information
        const wire_battery0_resistor1 = this.wire(battery0, resistor1, 0.644/2, 0, 1);
        wire_battery0_resistor1.setAllTouchingBoxVisibility(false);


        const wire_resistor1_c = this.wire(resistor1, c, 0.644/2, 0);
        wire_resistor1_c.setAllTouchingBoxVisibility(false);

        const wire_battery0_d = this.wire(battery0, d, 0.644/2, 1);
        wire_battery0_d.setAllTouchingBoxVisibility(false);


        const wire_resistor2_c = this.wire(resistor2, c, 0.644/2, 0);
        wire_resistor2_c.setAllTouchingBoxVisibility(false);

        const wire_resistor2_d = this.wire(resistor2, d, 0.644/2, 1);
        wire_resistor2_d.setAllTouchingBoxVisibility(false);


        const wire_resistor3_c = this.wire(resistor3, c, 0.644/2, 1);
        wire_resistor3_c.setAllTouchingBoxVisibility(false);

        const wire_resistor3_resistor4 = this.wire(resistor3, resistor4, 0.644/2, 0, 0);
        wire_resistor3_resistor4.setAllTouchingBoxVisibility(false);

        const wire_resistor4_d = this.wire(resistor4, d, 0.644/2, 1, 0, '124');
        wire_resistor4_d.setAllTouchingBoxVisibility(false);

        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }
    
}

export {Q2_3_5_aMoreComplexCircuit__P84};