
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

        const c = new Wire({'x': 15, 'y': 0, 'z':-20, 'radius': 1.024});//point c on the diagram
        this.scene.add(c);
        console.log(c);

        const d = new Wire({'x': -15, 'y': 0, 'z':-20, 'radius': 1.024});//point d on the diagram
        this.scene.add(d);


        //network|connection information
        const wire_c_resistor0 = this.wire(resistor0, c, 1.024, 1);
        const wire_c_resistor1 = this.wire(resistor1, c, 1.024, 1);
        const wire_d_resistor0 = this.wire(resistor0, d, 1.024, 0);
        const wire_d_resistor1 = this.wire(resistor1, d, 1.024, 0);
        const wireBetween11 = this.wire(battery0, d, 1.024, 0);
        const wireBetween00 = this.wire(battery0, c, 1.024, 1);



        // const wireBetween01 = this.wire(resistor0, resistor1, 1.024);

        // const wireBetween10 = this.wire(resistor0, resistor1, 1.024, 1, 1);

        // const wireBetween11 = this.wire(battery0, wireBetween10, 1.024, 1);

        // const wireBetween00 = this.wire(battery0, wireBetween01, 1.024, 0);

        //get Equations and solving steps:
        const dependentUUID = resistor0.uuid;
        const list_independentUUID = [battery0.uuid, resistor1.uuid];
        const dependentVarType = 'current';
        const list_independentVarType = ['current', 'current'];
        function meshToAnimation(mesh) {
            return function() {
                if (mesh.position.y > 120) {
                    mesh.visible = false;
                } else {
                    mesh.position.y += 0.1;
                }
            }
        }
        function onlySubString(s, subString){return s.includes(subString)}
        const self = this;
        function solvingCallback(equationStr__variables, componentId__list_variables) {
            
            let dependentVarStr = componentId__list_variables[self.uuid__id[resistor0.uuid]].filter(function(s){return onlySubString(s, 'V')})[0];//take the voltage of resistor0
            let list_independentVarStr = [
                componentId__list_variables[self.uuid__id[battery0.uuid]].filter(function(s){return onlySubString(s, 'V')})[0],//take the voltage of battery0
                componentId__list_variables[self.uuid__id[resistor1.uuid]].filter(function(s){return onlySubString(s, 'V')})[0] //take the voltage of resistor1
            ];
            function meshToAnimation_solve(mesh) {
                return function() {
                    if (mesh.position.y > 120) {
                        mesh.visible = false;
                    } else {
                        mesh.position.y += 0.1;
                    }
                }
                
            }
            self.animate_solveEquations(meshToAnimation_solve, Object.keys(equationStr__variables), dependentVarStr, list_independentVarStr)
        }
        this.animate_findEquations(meshToAnimation, solvingCallback);
        
        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }

    
}

export {DCTwoResistorParallel};