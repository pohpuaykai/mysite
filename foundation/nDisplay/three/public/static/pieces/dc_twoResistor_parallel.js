
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

        // const resistor0 = new ComponentResistor({x:0, y:-5, z:-20});
        const resistor0 = this.createComponent({componentName:'resistor', position:{x:0, y:-5, z:-20}});
        this.enter(resistor0.uuid); 
        // this.scene.add(resistor0); 
        resistor0.setAllTouchingBoxVisibility(false);//this.render();
        console.log('resistor0'); console.log(resistor0.uuid);

        // const battery0 = new ComponentBattery({x:0, y:0, z:10});
        const battery0 = this.createComponent({componentName:'battery', position:{x:0, y:0, z:10}});
        this.enter(battery0.uuid);
        // this.scene.add(battery0); 
        battery0.setAllTouchingBoxVisibility(false);//this.render();
        console.log('battery0'); console.log(battery0.uuid);

        // const resistor1 = new ComponentResistor({x:0, y:5, z:-20});
        const resistor1 = this.createComponent({componentName:'resistor', position:{x:0, y:5, z:-20}})
        this.enter(resistor1.uuid)
        // this.scene.add(resistor1); 
        resistor1.setAllTouchingBoxVisibility(false); this.render();
        console.log('resistor1'); console.log(resistor1.uuid);

        // const c = new Wire({'x': 15, 'y': 0, 'z':-20, 'radius': 0.644/2});//point c on the diagram
        const c = this.createComponent({componentName:'wire', position:{'x': 15, 'y': 0, 'z':-20}, additionalInfo:{'radius': 0.644/2}})
        this.enter(c.uuid);
        // this.scene.add(c);
        c.setAllTouchingBoxVisibility(false);
        console.log('c', c);

        // const d = new Wire({'x': -15, 'y': 0, 'z':-20, 'radius': 0.644/2});//point d on the diagram
        const d = this.createComponent({componentName:'wire', position:{'x': -15, 'y': 0, 'z':-20}, additionalInfo:{'radius': 0.644/2}})
        this.enter(d.uuid);
        // this.scene.add(d);
        d.setAllTouchingBoxVisibility(false);
        console.log('d', d);


        //network|connection information
        const wire_c_resistor0 = this.wire(resistor0, c, 0.644/2, 1);
        wire_c_resistor0.setAllTouchingBoxVisibility(false);
        const wire_c_resistor1 = this.wire(resistor1, c, 0.644/2, 1);
        wire_c_resistor1.setAllTouchingBoxVisibility(false);
        const wire_d_resistor0 = this.wire(resistor0, d, 0.644/2, 0);
        wire_d_resistor0.setAllTouchingBoxVisibility(false);
        const wire_d_resistor1 = this.wire(resistor1, d, 0.644/2, 0);
        wire_d_resistor1.setAllTouchingBoxVisibility(false);
        const wireBetween11 = this.wire(battery0, d, 0.644/2, 0);
        wireBetween11.setAllTouchingBoxVisibility(false);
        const wireBetween00 = this.wire(battery0, c, 0.644/2, 1);
        wireBetween00.setAllTouchingBoxVisibility(false);


        //get Equations and solving steps:
        const dependentUUID = resistor0.uuid;
        const list_independentUUID = [battery0.uuid, resistor1.uuid];
        const dependentVarType = 'current';
        const list_independentVarType = ['current', 'current'];
        // function findEquationAnimation___functionGen(list_equationNetworkInfoDict) {
        //     return function() {
        //         if (mesh.position.y > 120) {
        //             mesh.visible = false;
        //         } else {
        //             mesh.position.y += 0.1;
        //         }
        //     }//TODO refactor this<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<, this animation will end... if you do not aggregate it to the solving animation.....
        // }
        function onlySubString(s, subString){return s.includes(subString)}
        const self = this;
        function solvingCallback(list_equationNetworkInfoDict) {
            
            // let dependentVarStr = componentId__list_variables[self.uuid__id[resistor0.uuid]].filter(function(s){return onlySubString(s, 'V')})[0];//take the voltage of resistor0
            // let list_independentVarStr = [
            //     componentId__list_variables[self.uuid__id[battery0.uuid]].filter(function(s){return onlySubString(s, 'V')})[0],//take the voltage of battery0
            //     componentId__list_variables[self.uuid__id[resistor1.uuid]].filter(function(s){return onlySubString(s, 'V')})[0] //take the voltage of resistor1
            // ];
            // function meshToAnimation_solve(mesh) {
            //     return function() {
            //         if (mesh.position.y > 120) {
            //             mesh.visible = false;
            //         } else {
            //             mesh.position.y += 0.1;
            //         }
            //     }//TODO refactor this<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            // }
            // self.animate_solveEquations(meshToAnimation_solve, Object.keys(equationStr__variables), dependentVarStr, list_independentVarStr)
        }
        function findEquations___readyCallback() {//when the latexEquationStrs has been converted to meshes, and we have str__uuid in the piece.js, list_equationNetworkInfoDict is ready also
            //make the animation here? since here is when we have all the information we need
            //we have 
            // self.list_equationNetworkInfoDict
            // self.textStr__textMeshUUID
            // self.meshUUID__mesh

            function findEquationAnimation___functionGen(// is the parametrisation neccessary, what about using self.?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO?
                list_equationNetworkInfoDict, 
                textStr__textMeshUUID, 
                meshUUID__mesh,
                uuid__id,
                id__uuid,
                id__type,
                id__positiveLeadsDirections,
                edge__solderableIndices,
                networkGraph ) {
                //for animation, we store mesh in meshUUID__mesh, and only when we need the mesh, then we add to the THREE.Scene, as recommended by ChatGPT
                

                //load all the equations to scene, and then only when we need the actors then we set visible=true<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                //need a destroy function to remove actors that we do not need any more from the scene<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                //this is the render loop for animation
                return function() {
                    /**
                     * for relevant_equation:                                                          [1]
                     *   highlight the relevant_circuit                                                [2]
                     *   show the relevant_equation                                                    [3]
                     *   stop highlighting the relevant_circuit                                        [4]
                     *   hide the relevant_equation                                                    [5]
                     *   for (variable, component) in zip(relevant_equation, relevant_circuit):        [6]
                     *     highlight the relevant component                                            [7]
                     *     hightlight the relevant variable in the relevant equation                   [8]
                     *     unhighlight the relevant component                                          [9]
                     *     unhighlight the relevant variable in the relevant equation                  [10]
                     * **/
                    //use recursion to prevent all the Equation meshes from showing up together
                    //[1]
                    function equationDisplay(list_equationNetworkInfoDict, list_equationNetworkInfoDict___idx) {
                        if (list_equationNetworkInfoDict___idx >= list_equationNetworkInfoDict.length) {
                            self.animationScheduler.pause(); 
                            console.log('finished Animation$$$$$$$$$$$')
                            return;
                        }
                        const graphInfoD = list_equationNetworkInfoDict[list_equationNetworkInfoDict___idx];
console.log('equationIdx: ', list_equationNetworkInfoDict___idx, graphInfoD['equation'], '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        
                        //[2]
                        graphInfoD['list_list_networkNodeIds'].forEach(list_nodeId => {
                            // console.log('highlighting list_nodeId: ', graphInfoD['list_list_networkNodeIds'], '<<<HL<<')
                            const visited = []; // nodeId might be repeated
                            list_nodeId.forEach(nodeId => {
                                console.log('highlight nodeId', nodeId, ' type: ', id__type[nodeId], ' meshId: ', id__uuid[nodeId]); 
                                if (visited.indexOf(nodeId) <0) {
                                    visited.push(nodeId)
                                    self.highlight({meshUUID:id__uuid[nodeId], redMag:0.6, greenMag:0.1, blueMag:0.1})

                                }
                            })
                        });
                        console.log('highlighted nodes', window.performance.now())

                        //[3]
                        const equationMeshUUID = textStr__textMeshUUID[graphInfoD['equation']]['meshUUID']
                        const equationDimensions = self.getDimensions(equationMeshUUID);
                        console.log('getting dimensions: ', equationDimensions);
                        // self.highlight({meshUUID:equationMeshUUID, redMag:0.6, greenMag:0.1, blueMag:0.1}); //this group does not even have attributes and cannot be highlighted this way
                        self.setPosition(equationMeshUUID, equationDimensions.xLen/2, equationDimensions.yLen/2, equationDimensions.zLen+50);
                        self.reveal(equationMeshUUID); //self.renderer.render(self.scene, self.camera);

                        console.log('revealed equations', graphInfoD['equation'], ' ', window.performance.now());
                        // debugger;


                        console.log('pausing for 8 seconds 0', window.performance.now())

                        self.pause(()=>{
                            console.log('finished pausing 0', window.performance.now())

                            // debugger;
                            //[4] unhighlight network
                            // self.unhighlight(equationMeshUUID);
                            graphInfoD['list_list_networkNodeIds'].forEach(list_nodeId => {
                            // console.log('UNhighlighting list_nodeId: ', graphInfoD['list_list_networkNodeIds'], '<<<UN<<')

                                const visited = [];
                                list_nodeId.forEach(nodeId => {
                                    if (visited.indexOf(nodeId) <0) {
                                        console.log('unhightlight nodeId', nodeId, ' type: ', id__type[nodeId]); 
                                        self.unhighlight(id__uuid[nodeId])
                                    }
                                })
                            });
                            // debugger;



                            self.pause(()=>{


                                //[6] use recursion to play the variables one by one
                                function variableDisplay(list_variableInfoD, list_variableInfoD___idx) {
                                    if (list_variableInfoD___idx >= list_variableInfoD.length){

                                        //[5]
                                        self.hide(equationMeshUUID);

                                        console.log('hid equations', graphInfoD['equation'], window.performance.now());
                                        //call the next equation animation
                                        equationDisplay(list_equationNetworkInfoDict, list_equationNetworkInfoDict___idx+1);
                                        return;
                                    }
                                    const variableInfoD = list_variableInfoD[list_variableInfoD___idx]

                                    const variableStr = variableInfoD['variableStr'];

                                    //[7]
                                    //highlight variableComponent
                                    const componentMeshUUID = id__uuid[graphInfoD['variableStr__nodeId'][variableStr]]
                                    self.highlight({meshUUID: componentMeshUUID, redMag:-0.1, greenMag:-0.6, blueMag:-0.1})
                                    console.log('highlighted variableNodes', window.performance.now())


                                    //[8] each chaStr is only a part of the variable, so we want them to light up togehter
                                    variableInfoD['info'].forEach(([chaStr, charMeshUUID]) => {
                                        self.highlight({meshUUID:charMeshUUID, redMag:-0.1, greenMag:-0.6, blueMag:-0.1});
                                        console.log('highlighted: ', chaStr, ' uuid: ', charMeshUUID, '<<<<<<<<<<<<<<<<<<<<<<<variable highlighting????????????????????????????????????????????????????')
                                    })


                                    console.log('highlighted variable', window.performance.now())
                                    console.log('pausing for 8 seconds 1', window.performance.now())
                                    self.pause(()=>{
                                        console.log('finish pausing 1', window.performance.now())
                                        //[9]
                                        self.unhighlight(id__uuid[graphInfoD['variableStr__nodeId'][variableStr]])
                                        console.log('unhighlight variableNode', window.performance.now())
                                        //[10]
                                        variableInfoD['info'].forEach(([chaStr, charMeshUUID]) => {
                                            console.log('chaStr', chaStr, 'charMeshUUID', charMeshUUID)
                                            self.unhighlight(charMeshUUID)
                                        })
                                        console.log('unhighlight variable', window.performance.now())

                                        variableDisplay(list_variableInfoD, list_variableInfoD___idx+1);
                                    }, 4000);// pause for 8 seconds, then unhighlight relevant_component and relevant_variable

                                }
                                variableDisplay(textStr__textMeshUUID[graphInfoD['equation']]['info'], 0);


                            }, 4000);



                        }, 4000);

                    }
                    equationDisplay(list_equationNetworkInfoDict, 0);

                }
            }
            //schedule animation
            self.scheduleAnimation(findEquationAnimation___functionGen(
                self.list_equationNetworkInfoDict,
                self.textStr__textMeshUUID,
                self.meshUUID__mesh,
                self.uuid__id,
                self.id__uuid,
                self.id__type,
                self.id__positiveLeadsDirections,
                self.edge__solderableIndices,
                self.networkGraph
            ), 0);
            //this is only for TESTING, after we are done with scheduling solvingEquation_animation, then we call this.play()<<<<<<<<<<<<<<<<<<<<<<
            self.play();
        }
        this.animate_findEquations(solvingCallback, findEquations___readyCallback);




















        // function findEquationAnimation___functionGen(list_equationNetworkInfoDict) {
        //     return function() {
        //         if (mesh.position.y > 120) {
        //             mesh.visible = false;
        //         } else {
        //             mesh.position.y += 0.1;
        //         }
        //     }//TODO refactor this<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<, this animation will end... if you do not aggregate it to the solving animation.....
        // }
        // function onlySubString(s, subString){return s.includes(subString)}
        // const self = this;
        // function solvingCallback(list_equationNetworkInfoDict) {
            
        //     let dependentVarStr = componentId__list_variables[self.uuid__id[resistor0.uuid]].filter(function(s){return onlySubString(s, 'V')})[0];//take the voltage of resistor0
        //     let list_independentVarStr = [
        //         componentId__list_variables[self.uuid__id[battery0.uuid]].filter(function(s){return onlySubString(s, 'V')})[0],//take the voltage of battery0
        //         componentId__list_variables[self.uuid__id[resistor1.uuid]].filter(function(s){return onlySubString(s, 'V')})[0] //take the voltage of resistor1
        //     ];
        //     function meshToAnimation_solve(mesh) {
        //         return function() {
        //             if (mesh.position.y > 120) {
        //                 mesh.visible = false;
        //             } else {
        //                 mesh.position.y += 0.1;
        //             }
        //         }
                
        //     }
        //     self.animate_solveEquations(meshToAnimation_solve, Object.keys(equationStr__variables), dependentVarStr, list_independentVarStr)
        // }
        // this.animate_findEquations(findEquationAnimation___functionGen, solvingCallback);
        
        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }

    
}

export {DCTwoResistorParallel};