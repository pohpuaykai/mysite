
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
        this.scene.add(resistor0); this.render();

        const battery0 = new ComponentBattery({x:0, y:0, z:10});
        this.scene.add(battery0); this.render();

        const resistor1 = new ComponentResistor({x:15, y:0, z:-20});
        this.scene.add(resistor1); this.render();

        const wireBetween01 = this.wire(resistor0, battery0, 1.024);

        const wireBetween10 = this.wire(resistor0, resistor1, 1.024, 1, 0);

        const wireBetween11 = this.wire(battery0, resistor1, 1.024, 1, 1);

        // console.log(this.wiring);
        // const self = this; 
        //get Equations and solving steps:
        // function CALLBACK__getAllEquationsAndASolvingStep(listOfEquations_latexStrs, solvingSteps){
        //     console.log('solvingSteps');
        //     console.log(solvingSteps);
        //     const YSize = 30;
        //     const startYCoordinate = -listOfEquations_latexStrs.length* YSize/2;
        //     function CALLBACK__createLatexMeshes(meshIdx, mesh) {
        //         mesh.position.set(-64, startYCoordinate+YSize*meshIdx, 100);
        //         self.scene.add(mesh);
        //         // console.log(meshIdx, mesh);
        //         self.animationAggregator.appendAction((function(mesh){
        //             return function() {
        //                 if (mesh.position.y > 120) {
        //                     mesh.visible = false;
        //                 } else {
        //                     mesh.position.y += 0.1;
        //                 }
        //             }
        //         })(mesh));
        //         self.render();
        //         self.animationAggregator.restartAnimation();
        //         // renderer.setAnimationLoop( animate );
        //     }
        //     self.createLatexMeshes(listOfEquations_latexStrs, CALLBACK__createLatexMeshes);
        // }
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
            }
        }
        this.animate_getAllEquationsAndASolvingStep(meshToAnimation, dependentUUID, list_independentUUID, dependentVarType, list_independentVarType);

        // this.getAllEquationsAndASolvingStep(CALLBACK__getAllEquationsAndASolvingStep, dependentUUID, list_independentUUID, dependentVarType, list_independentVarType);
        // this.listOfEquations_latexStrs;
        // this.solvingSteps;


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
            //     'wireBetween11':wireBetween11
            // },
            // 'animate':animate// This will be set within the piece, no need to return this anymore
        }

    }
    
}

export {DCTwoResistorSeries};