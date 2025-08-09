
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

        //the actors coming in one-by-one, could be an animation too. :D

        //actors in this piece
        const battery0 = new ComponentBattery({x:0, y:0, z:0});
        this.scene.add(battery0); battery0.setAllTouchingBoxVisibility(false);//this.render();

        const resistor__2Ohm__parallel = new ComponentResistor({x:0, y:5, z:-20});
        this.scene.add(resistor__2Ohm__parallel); resistor__2Ohm__parallel.setAllTouchingBoxVisibility(false);//this.render();
        console.log('2OhmParallel'); console.log(resistor__2Ohm__parallel.uuid);

        const resistor__3Ohm__parallel = new ComponentResistor({x:0, y:0, z:-20});
        this.scene.add(resistor__3Ohm__parallel); resistor__3Ohm__parallel.setAllTouchingBoxVisibility(false);//this.render();
        console.log('3OhmParallel'); console.log(resistor__3Ohm__parallel.uuid);

        const resistor__6Ohm__parallel = new ComponentResistor({x:0, y:-5, z:-20});
        this.scene.add(resistor__6Ohm__parallel); resistor__6Ohm__parallel.setAllTouchingBoxVisibility(false);//this.render();
        console.log('6OhmParallel'); console.log(resistor__6Ohm__parallel.uuid);

        const a = new Wire({'x':30, 'y':0, 'z':-20, 'radius': 0.644/2}); //point a on diagram
        a.setAllTouchingBoxVisibility(false);
        this.scene.add(a);

        const c = new Wire({'x': 10, 'y': 0, 'z':-20, 'radius': 0.644/2});//point c on the diagram
        c.setAllTouchingBoxVisibility(false);
        this.scene.add(c);

        const d = new Wire({'x': -10, 'y': 0, 'z':-20, 'radius': 0.644/2});//point d on the diagram
        d.setAllTouchingBoxVisibility(false);
        this.scene.add(d);

        const e = new Wire({'x': -30, 'y': 0, 'z':-20, 'radius': 0.644/2});//point e on the diagram
        e.setAllTouchingBoxVisibility(false);
        this.scene.add(e);

        const resistor__1Ohm__series = new ComponentResistor({x:20, y:0, z:-20});
        this.scene.add(resistor__1Ohm__series); resistor__1Ohm__series.setAllTouchingBoxVisibility(false);//this.render();
        console.log('1OhmSeries'); console.log(resistor__1Ohm__series.uuid);

        const resistor__6Ohm__series = new ComponentResistor({x:-20, y:0, z:-20});
        this.scene.add(resistor__6Ohm__series); resistor__6Ohm__series.setAllTouchingBoxVisibility(false);//this.render();
        console.log('6OhmSeries'); console.log(resistor__6Ohm__series.uuid);

        const resistor__8Ohm__parallel = new ComponentResistor({x:0, y:-10, z:-20});
        this.scene.add(resistor__8Ohm__parallel); resistor__8Ohm__parallel.setAllTouchingBoxVisibility(false);//this.render();
        console.log('8OhmParallel'); console.log(resistor__8Ohm__parallel.uuid);

        const resistor__16Ohm__series = new ComponentResistor({x:-40, y:0, z:-20});
        this.scene.add(resistor__16Ohm__series); resistor__16Ohm__series.setAllTouchingBoxVisibility(false);this.render();
        console.log('16OhmSeries'); console.log(resistor__16Ohm__series.uuid);

        //make the wire connections
        const wire_c_2OhmParallel_L = this.wire(resistor__2Ohm__parallel, c, 0.644/2, 1);
        wire_c_2OhmParallel_L.setAllTouchingBoxVisibility(false);
        const wire_c_3OhmParallel_L = this.wire(resistor__3Ohm__parallel, c, 0.644/2, 1);
        wire_c_3OhmParallel_L.setAllTouchingBoxVisibility(false);
        const wire_c_6OhmParallel_L = this.wire(resistor__6Ohm__parallel, c, 0.644/2, 1);
        wire_c_6OhmParallel_L.setAllTouchingBoxVisibility(false);

        const wire_d_2OhmParallel_R = this.wire(resistor__2Ohm__parallel, d, 0.644/2, 0);
        wire_d_2OhmParallel_R.setAllTouchingBoxVisibility(false);
        const wire_d_3OhmParallel_R = this.wire(resistor__3Ohm__parallel, d, 0.644/2, 0);
        wire_d_3OhmParallel_R.setAllTouchingBoxVisibility(false);
        const wire_d_6OhmParallel_R = this.wire(resistor__6Ohm__parallel, d, 0.644/2, 0);
        wire_d_6OhmParallel_R.setAllTouchingBoxVisibility(false);

        const wire_d_6OhmSeries_L = this.wire(resistor__6Ohm__series, d, 0.644/2, 1);//TODO please fix: if you specify a solderableLead to WireComponent, it goes to CASE3 and BREAKs!
        wire_d_6OhmSeries_L.setAllTouchingBoxVisibility(false);
        const wire_e_6OhmSeries_R = this.wire(resistor__6Ohm__series, e, 0.644/2, 0);
        wire_e_6OhmSeries_R.setAllTouchingBoxVisibility(false);

        const wire_c_1OhmSeries_R = this.wire(resistor__1Ohm__series, c, 0.644/2, 0);
        wire_c_1OhmSeries_R.setAllTouchingBoxVisibility(false);
        const wire_a_1OhmSeries_L = this.wire(resistor__1Ohm__series, a, 0.644/2, 1);
        wire_a_1OhmSeries_L.setAllTouchingBoxVisibility(false);
        
        const wire_a_8hmParallel_L = this.wire(resistor__8Ohm__parallel, a, 0.644/2, 1);
        wire_a_8hmParallel_L.setAllTouchingBoxVisibility(false);

        const wire_8OhmParallel_e_R = this.wire(resistor__8Ohm__parallel, e, 0.644/2, 0);
        wire_8OhmParallel_e_R.setAllTouchingBoxVisibility(false);

        const wire_16OhmSeries_e_L = this.wire(resistor__16Ohm__series, e, 0.644/2, 1);
        wire_16OhmSeries_e_L.setAllTouchingBoxVisibility(false);

        const wire_battery_b = this.wire(battery0, resistor__16Ohm__series, 0.644/2, 0, 0);
        wire_battery_b.setAllTouchingBoxVisibility(false);
        const wire_battery_a = this.wire(battery0, a, 0.644/2, 1);
        wire_battery_a.setAllTouchingBoxVisibility(false);


        //this question needs to get the sum of 3 components, not just each component
        //get Equations and solving steps:
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
            //
            //find the equation that contains R of resistor__16Ohm__series, since total must contain it, set as E
            const theEquationStr = Object.keys(equationStr__variables).filter(function(s){return onlySubString(s, self.uuid__id[resistor__16Ohm__series.uuid])})[0];
            //remove all the variables that contains ids from self.id__type, from equationStr__variables[E]
            const ids = Object.keys(self.id__type);
            const variablesLeft = equationStr__variables[theEquationStr].filter(function(s){
                for(let i=0; i<ids; i++) {
                    if (s.includes('{'+ids[i]+'}')) {
                        return false;
                    }
                }
                return true;
            });
            console.log('variablesLeft: ');
            console.log(variablesLeft);
            //the variable left, will be the total_resistance variable.
            const dependentVarStr = variablesLeft[0];
            console.log('dependentVarStr: ');
            console.log(dependentVarStr)
            //
            // let dependentVarStr = ;//take the resistance of total_resistance_of_the_entire_circuit
            const list_independentVarStr = [
                componentId__list_variables[self.uuid__id[resistor__2Ohm__parallel.uuid]].filter(function(s){return onlySubString(s, 'R_{R')})[0],//take the resistance of resistor__2Ohm__parallel
                componentId__list_variables[self.uuid__id[resistor__3Ohm__parallel.uuid]].filter(function(s){return onlySubString(s, 'R_{R')})[0], //take the resistance of resistor__3Ohm__parallel
                componentId__list_variables[self.uuid__id[resistor__6Ohm__parallel.uuid]].filter(function(s){return onlySubString(s, 'R_{R')})[0],//take the resistance of resistor__6Ohm__parallel
                componentId__list_variables[self.uuid__id[resistor__1Ohm__series.uuid]].filter(function(s){return onlySubString(s, 'R_{R')})[0], //take the resistance of resistor__1Ohm__series
                componentId__list_variables[self.uuid__id[resistor__6Ohm__series.uuid]].filter(function(s){return onlySubString(s, 'R_{R')})[0],//take the resistance of resistor__6Ohm__series
                componentId__list_variables[self.uuid__id[resistor__8Ohm__parallel.uuid]].filter(function(s){return onlySubString(s, 'R_{R')})[0], //take the resistance of resistor__8Ohm__parallel
                componentId__list_variables[self.uuid__id[resistor__16Ohm__series.uuid]].filter(function(s){return onlySubString(s, 'R_{R')})[0] //take the resistance of resistor__16Ohm__series
            ];
            console.log('list_independentVarStr', list_independentVarStr);
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
        // this.animate_findEquations(meshToAnimation, solvingCallback);

        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }
    
}

export {Q3_21__P18};