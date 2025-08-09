
// import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {Animation} from '../custom/Animation.js';
import {ComponentResistor} from '../meshes/ComponentResistor.js';
import {ComponentBattery} from '../meshes/ComponentBattery.js';
import {Circuit} from './circuit.js';
import {Wire} from '../meshes/Wire.js';

class DCTwoResistorSeries extends Circuit {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, meshes) {
        super(scene, camera, renderer, meshes);
    }

    act() {

        const resistor0 = new ComponentResistor({x:0, y:0, z:-20});
        this.scene.add(resistor0); resistor0.setAllTouchingBoxVisibility(false); //this.render();
        console.log('resistor0'); console.log(resistor0.uuid);

        const battery0 = new ComponentBattery({x:0, y:0, z:10});
        this.scene.add(battery0); battery0.setAllTouchingBoxVisibility(false); //this.render();
        console.log('battery0'); console.log(battery0.uuid);

        const resistor1 = new ComponentResistor({x:15, y:0, z:-20});
        this.scene.add(resistor1); resistor1.setAllTouchingBoxVisibility(false); this.render();
        console.log('resistor1'); console.log(resistor1.uuid);

        const wireBetween01 = this.wire(resistor0, battery0, 1.024, 0, 0, '241');
        wireBetween01.setAllTouchingBoxVisibility(false);

        const wireBetween10 = this.wire(resistor0, resistor1, 1.024, 1, 0);
        wireBetween10.setAllTouchingBoxVisibility(false);

        const wireBetween11 = this.wire(battery0, resistor1, 1.024, 1, 1, '142');
        wireBetween11.setAllTouchingBoxVisibility(false);

        //set the dependent and independent variables
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
            }//TODO refactor this<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<, this animation will end... if you do not aggregate it to the solving animation.....
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
                }//TODO refactor this<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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

export {DCTwoResistorSeries};