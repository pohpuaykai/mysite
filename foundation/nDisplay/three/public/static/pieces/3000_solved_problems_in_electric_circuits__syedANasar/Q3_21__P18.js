
import {asyncCreateTextMesh} from '../../custom/TextMeshCreater.js';
import {ComponentResistor} from '../../meshes/ComponentResistor.js';
import {ComponentBattery} from '../../meshes/ComponentBattery.js';
import {Circuit} from '../circuit.js';
import {Wire} from '../../meshes/Wire.js';

class Q3_21__P18 extends Circuit {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, meshes) {
        super(scene, camera, renderer, meshes);
    }

    act() {

        //actors in this piece
        const battery0 = new ComponentBattery({x:0, y:0, z:0});
        this.scene.add(battery0); //this.render();

        const resistor__2Ohm__parallel = new ComponentResistor({x:0, y:5, z:-20});
        this.scene.add(resistor__2Ohm__parallel); //this.render();

        const resistor__3Ohm__parallel = new ComponentResistor({x:0, y:0, z:-20});
        this.scene.add(resistor__3Ohm__parallel); //this.render();

        const resistor__6Ohm__parallel = new ComponentResistor({x:0, y:-5, z:-20});
        this.scene.add(resistor__6Ohm__parallel); //this.render();

        const resistor__1Ohm__series = new ComponentResistor({x:15, y:0, z:-20});
        this.scene.add(resistor__1Ohm__series); //this.render();

        const resistor__6Ohm__series = new ComponentResistor({x:-15, y:0, z:-20});
        this.scene.add(resistor__6Ohm__series); //this.render();

        const resistor__8Ohm__parallel = new ComponentResistor({x:0, y:-10, z:-20});
        this.scene.add(resistor__8Ohm__parallel); //this.render();

        const resistor__16Ohm__series = new ComponentResistor({x:-30, y:0, z:-20});
        this.scene.add(resistor__16Ohm__series); this.render();

        //make the wire connections
        const wire_2OhmParallel_3OhmParallel_R = this.wire(resistor__2Ohm__parallel, resistor__3Ohm__parallel, 1.024, 1, 1);//d0 //could be point 'd' on the diagram
        const wire_2OhmParallel_3OhmParallel_L = this.wire(resistor__2Ohm__parallel, resistor__3Ohm__parallel, 1.024, 0, 0);//c0 //could be point 'c' on the diagram

        const wire_3OhmParallel_6OhmParallel_R = this.wire(resistor__3Ohm__parallel, resistor__6Ohm__parallel, 1.024, 1, 1);//d1 //could be point 'd' on the diagram
        const wire_3OhmParallel_6OhmParallel_L = this.wire(resistor__3Ohm__parallel, resistor__6Ohm__parallel, 1.024, 0, 0);//c1 //could be point 'c' on the diagram

        const wire_d0_6OhmSeries_L = this.wire(resistor__6Ohm__series, wire_2OhmParallel_3OhmParallel_R, 1.024, 1);//TODO please fix: if you specify a solderableLead to WireComponent, it goes to CASE3 and BREAKs!

        const wire_c0_1OhmSeries_R = this.wire(resistor__1Ohm__series, wire_2OhmParallel_3OhmParallel_L, 1.024, 0);

        const wire_1OhmSeries_8OhmParallel_L = this.wire(resistor__1Ohm__series, resistor__8Ohm__parallel, 1.024, 1, 1);//a //could be point 'a' on the diagram

        const wire_6OhmSeries_16OhmSeries_L = this.wire(resistor__6Ohm__series, resistor__16Ohm__series, 1.024, 1, 0);//e //could be point 'e' on the diagram
        
        const wire_8OhmParallel_e_R = this.wire(resistor__8Ohm__parallel, wire_6OhmSeries_16OhmSeries_L, 1.024, 0);

        const wire_battery_b = this.wire(battery0, resistor__16Ohm__series, 1.024, 0, 0);
        const wire_battery_a = this.wire(battery0, wire_1OhmSeries_8OhmParallel_L, 1.024, 1);


        //this question needs to get the sum of 3 components, not just each component
        //get Equations and solving steps:
        // const dependentUUID = resistor0.uuid;
        // const list_independentUUID = [battery0.uuid, resistor1.uuid];
        // const dependentVarType = 'voltage';
        // const list_independentVarType = ['voltage', 'voltage'];
        // function meshToAnimation(mesh) {
        //     return function() {
        //         if (mesh.position.y > 120) {
        //             mesh.visible = false;
        //         } else {
        //             mesh.position.y += 0.1;
        //         }
        //     }
        // }
        // this.animate_getAllEquationsAndASolvingStep(meshToAnimation, dependentUUID, list_independentUUID, dependentVarType, list_independentVarType);


        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }
    
}

export {Q3_21__P18};