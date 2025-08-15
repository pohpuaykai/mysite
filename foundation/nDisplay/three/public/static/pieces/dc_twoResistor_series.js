
// import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {Animation} from '../custom/Animation.js';
import {Circuit} from './circuit.js';
import {Wire} from '../meshes/Wire.js';

class DCTwoResistorSeries extends Circuit {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, controls, meshes) {
        super(scene, camera, renderer, controls, meshes);
    }

    act() {

        // console.log(this.renderer.getContext())
        // console.log(this.renderer.xr)


        
        const resistor0 = this.createComponent({componentName:'resistor', position:{x:0, y:0, z:-20}});
        this.enter(resistor0.uuid); 
        resistor0.setAllTouchingBoxVisibility(false); //this.render();
        console.log('resistor0'); console.log(resistor0.uuid);

        const battery0 = this.createComponent({componentName:'battery', position:{x:0, y:0, z:10}});
        this.enter(battery0.uuid);
        battery0.setAllTouchingBoxVisibility(false); //this.render();
        console.log('battery0'); console.log(battery0.uuid);

        const resistor1 = this.createComponent({componentName:'resistor', position:{x:15, y:0, z:-20}})
        this.enter(resistor1.uuid)
        resistor1.setAllTouchingBoxVisibility(false); this.render();
        console.log('resistor1'); console.log(resistor1.uuid);

        const wireBetween01 = this.wire(resistor0, battery0, 0.644/2, 0, 0, '241');
        wireBetween01.setAllTouchingBoxVisibility(false);

        const wireBetween10 = this.wire(resistor0, resistor1, 0.644/2, 1, 0);
        wireBetween10.setAllTouchingBoxVisibility(false);

        const wireBetween11 = this.wire(battery0, resistor1, 0.644/2, 1, 1, '142');
        wireBetween11.setAllTouchingBoxVisibility(false);


        //set the dependent and independent variables
        const dependentUUID = resistor0.uuid;
        const list_independentUUID = [battery0.uuid, resistor1.uuid];
        const dependentVarType = 'voltage';
        const list_independentVarType = ['voltage', 'voltage'];
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
        // function solvingCallback(list_equationNetworkInfoDict) {
            
        //     let dependentVarStr = componentId__list_variables[self.uuid__id[resistor0.uuid]].filter(function(s){return onlySubString(s, 'V')})[0];//take the voltage of resistor0
        //     let list_independentVarStr = [
        //         componentId__list_variables[self.uuid__id[battery0.uuid]].filter(function(s){return onlySubString(s, 'V')})[0],//take the voltage of battery0
        //         componentId__list_variables[self.uuid__id[resistor1.uuid]].filter(function(s){return onlySubString(s, 'V')})[0] //take the voltage of resistor1
        //     ];
        //     // self.animate_solveEquations(meshToAnimation_solve, Object.keys(equationStr__variables), dependentVarStr, list_independentVarStr)
        // }
        function solveEquation___readyCallback() {

            function solveEquation___functionGen(

            ) {
                return function() {
                    /**
                     * We have :
                     * self.solvingSteps
                     * self.branchedStepsIdx__latexStrs
                     * self.runningStepsIdx__branchedStepsIdx
                     * 
                     * also the latexMeshes from LatexMeshCreater.js
                     *  self.textStr__textMeshUUID
                     *  self.meshUUID__mesh
                     * **/
                    const cameraPosition = self.camera.position;
                    console.log(cameraPosition)
                    // debugger

                    console.log('running solveEquation animation is running')
                    // look back.
                    const facingCoordinate = {x:6*cameraPosition.x, y:6*cameraPosition.y, z:6*cameraPosition.z};
                    self.smoothLookAt(facingCoordinate.x, facingCoordinate.y, facingCoordinate.z, function(){
                    // self.smoothMoveCameraPosition(facingCoordinate.x, facingCoordinate.y, facingCoordinate.z ,function() {
                        console.log('finished looking back'); let previousEquationType = 'vor'; let lastDidNotHideMeshUUID = null;
                        function equationReveal(theList, theList___idx) {
                            if (theList___idx >= theList.length) {
                                self.animationScheduler.pause(); 
                                console.log('animationScheduler.pause DONE')
                                // self.removeMeshesByRequestingAnimation('solveEquations');
                                // console.log('removed ')
                                return
                            }
                            let runningStepsIdx; let branchedStepsIdx;
                            [runningStepsIdx, branchedStepsIdx] = theList[theList___idx]
                            // console.log("self.textStr__textMeshUUID", self.textStr__textMeshUUID)
                            const latexStrMeshUUID = self.textStr__textMeshUUID[self.branchedStepsIdx__latexStrs[branchedStepsIdx]]['meshUUID'];
                            const equationDimensions = self.getDimensions(latexStrMeshUUID);
                            self.setRotation(latexStrMeshUUID, 0, Math.PI, 0)
                            if (branchedStepsIdx[1] == 'vor') {//put it slightly to the left
                                self.setPosition(latexStrMeshUUID, facingCoordinate.x-equationDimensions.xLen, facingCoordinate.y, facingCoordinate.z);
                            } else {
                                self.setPosition(latexStrMeshUUID, facingCoordinate.x+equationDimensions.xLen, facingCoordinate.y, facingCoordinate.z);
                            }
                            self.reveal(latexStrMeshUUID); 
                            console.log('revealed: ', self.branchedStepsIdx__latexStrs[branchedStepsIdx], branchedStepsIdx)
                            self.pause(()=>{
                                //hide the previous according to whether branchedStepsIdx, branchedStepsIdx<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
                                if (previousEquationType == branchedStepsIdx[1]) {
                                    self.hide(latexStrMeshUUID);
                                    previousEquationType = branchedStepsIdx[1];
                                } else {
                                    if (lastDidNotHideMeshUUID !== null) {
                                        self.hide(lastDidNotHideMeshUUID)
                                    }
                                    lastDidNotHideMeshUUID = latexStrMeshUUID;
                                }
                                equationReveal(theList, theList___idx+1);
                            }, 4000)

                        }
                        equationReveal(Object.entries(self.runningStepsIdx__branchedStepsIdx), 0)
                        // debugger;
                    });
                }
            }


            //schedule animation
            self.scheduleAnimation(solveEquation___functionGen(), 1, 'solveEquation');//1 so that it will run after the findEquationAnimation
            self.play(function() {
                return self.animationScheduler.animationHoldingPen.length >=2;//check that all the animation is in before playing
            }, false);
        }

        function findEquations___readyCallback() {//when the latexEquationStrs has been converted to meshes, and we have str__uuid in the piece.js, list_equationNetworkInfoDict is ready also
            // //making the parameters need for animate__solveEquations
            const list_equationLatexStr = []; let dependentVarStr; const list_independentVarStr = [];
            self.list_equationNetworkInfoDict.forEach(equationNetworkInfoDict => {
                list_equationLatexStr.push(equationNetworkInfoDict['equation']);
                Object.entries(equationNetworkInfoDict['variableInfos']).forEach(([nodeId, list_variableStr]) => {
                    //capture the dependentVarStr: voltage of resistor0
                    if(parseInt(nodeId) == self.uuid__id[resistor0.uuid]) {
                        dependentVarStr = list_variableStr.filter(function(s){return onlySubString(s, 'V')})[0];//TODO some hard coding here....
                    }
                    //capture the first element of list_independentVarStr
                    if(parseInt(nodeId) == self.uuid__id[battery0.uuid]) {
                        list_independentVarStr.push(list_variableStr.filter(function(s){return onlySubString(s, 'V')})[0]); //TODO some hard coding here...
                    }
                    //capture the first element of list_independentVarStr
                    if(parseInt(nodeId) == self.uuid__id[resistor1.uuid]) {
                        list_independentVarStr.push(list_variableStr.filter(function(s){return onlySubString(s, 'V')})[0]); //TODO some hard coding here...
                    }
                });
            });
            console.log('list_equationLatexStr', list_equationLatexStr);
            console.log('dependentVarStr', dependentVarStr);
            console.log('list_independentVarStr', list_independentVarStr);
            self.animate_solveEquations(solveEquation___readyCallback, list_equationLatexStr, dependentVarStr, list_independentVarStr);//this will just schedule the animation...

            function findEquationAnimation___functionGen(// is the parametrisation neccessary, what about using self.?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO?

                ) {
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
                            // self.animationScheduler.pause(); 
                            console.log('finished Animation equationDisplay$$$$$$$$$$$')
                            //TODO maybe... remove all the latexStrings on the scene? But there are latexStrings that in solveEquation animation that are the same as in findEquation, and they will be cleared too.
                            self.removeMeshesByRequestingAnimation('findEquations');
                            // here is where you should run the next animation.
                            self.animationScheduler.playNextAnimation()
                            return;
                        }
                        const graphInfoD = list_equationNetworkInfoDict[list_equationNetworkInfoDict___idx];
// console.log('equationIdx: ', list_equationNetworkInfoDict___idx, graphInfoD['equation'], '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        
                        //[2]
                        graphInfoD['list_list_networkNodeIds'].forEach(list_nodeId => {
                            // console.log('highlighting list_nodeId: ', graphInfoD['list_list_networkNodeIds'], '<<<HL<<')
                            const visited = []; // nodeId might be repeated
                            list_nodeId.forEach(nodeId => {
                                // console.log('highlight nodeId', nodeId, ' type: ', id__type[nodeId], ' meshId: ', id__uuid[nodeId]); 
                                if (visited.indexOf(nodeId) <0) {
                                    visited.push(nodeId)
                                    self.highlight({meshUUID:self.id__uuid[nodeId], redMag:0.6, greenMag:0.1, blueMag:0.1})

                                }
                            })
                        });
                        // console.log('highlighted nodes', window.performance.now())

                        //[3]
                        const equationMeshUUID = self.textStr__textMeshUUID[graphInfoD['equation']]['meshUUID']
                        const equationDimensions = self.getDimensions(equationMeshUUID);
                        // console.log('getting dimensions: ', equationDimensions);
                        // self.highlight({meshUUID:equationMeshUUID, redMag:0.6, greenMag:0.1, blueMag:0.1}); //this group does not even have attributes and cannot be highlighted this way
                        self.setPosition(equationMeshUUID, equationDimensions.xLen/2, equationDimensions.yLen/2, equationDimensions.zLen+50);
                        self.reveal(equationMeshUUID); //self.renderer.render(self.scene, self.camera);

                        // console.log('revealed equations', graphInfoD['equation'], ' ', window.performance.now());
                        // debugger;


                        // console.log('pausing for 8 seconds 0', window.performance.now())

                        self.pause(()=>{
                            // console.log('finished pausing 0', window.performance.now())

                            // debugger;
                            //[4] unhighlight network
                            // self.unhighlight(equationMeshUUID);
                            graphInfoD['list_list_networkNodeIds'].forEach(list_nodeId => {
                            // console.log('UNhighlighting list_nodeId: ', graphInfoD['list_list_networkNodeIds'], '<<<UN<<')

                                const visited = [];
                                list_nodeId.forEach(nodeId => {
                                    if (visited.indexOf(nodeId) <0) {
                                        // console.log('unhightlight nodeId', nodeId, ' type: ', id__type[nodeId]); 
                                        self.unhighlight(self.id__uuid[nodeId])
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

                                        // console.log('hid equations', graphInfoD['equation'], window.performance.now());
                                        //call the next equation animation
                                        equationDisplay(list_equationNetworkInfoDict, list_equationNetworkInfoDict___idx+1);
                                        return;
                                    }
                                    const variableInfoD = list_variableInfoD[list_variableInfoD___idx]

                                    const variableStr = variableInfoD['variableStr'];

                                    //[7]
                                    //highlight variableComponent
                                    const componentMeshUUID = self.id__uuid[graphInfoD['variableStr__nodeId'][variableStr]]
                                    self.highlight({meshUUID: componentMeshUUID, redMag:-0.1, greenMag:-0.6, blueMag:-0.1})
                                    // console.log('highlighted variableNodes', window.performance.now())


                                    //[8] each chaStr is only a part of the variable, so we want them to light up togehter
                                    variableInfoD['info'].forEach(([chaStr, charMeshUUID]) => {
                                        self.highlight({meshUUID:charMeshUUID, redMag:-0.1, greenMag:-0.6, blueMag:-0.1});
                                        // console.log('highlighted: ', chaStr, ' uuid: ', charMeshUUID, '<<<<<<<<<<<<<<<<<<<<<<<variable highlighting????????????????????????????????????????????????????')
                                    })


                                    // console.log('highlighted variable', window.performance.now())
                                    // console.log('pausing for 8 seconds 1', window.performance.now())
                                    self.pause(()=>{
                                        // console.log('finish pausing 1', window.performance.now())
                                        //[9]
                                        self.unhighlight(self.id__uuid[graphInfoD['variableStr__nodeId'][variableStr]])
                                        // console.log('unhighlight variableNode', window.performance.now())
                                        //[10]
                                        variableInfoD['info'].forEach(([chaStr, charMeshUUID]) => {
                                            // console.log('chaStr', chaStr, 'charMeshUUID', charMeshUUID)
                                            self.unhighlight(charMeshUUID)
                                        })
                                        // console.log('unhighlight variable', window.performance.now())

                                        variableDisplay(list_variableInfoD, list_variableInfoD___idx+1);
                                    }, 4000);// pause for 8 seconds, then unhighlight relevant_component and relevant_variable

                                }
                                variableDisplay(self.textStr__textMeshUUID[graphInfoD['equation']]['info'], 0);


                            }, 4000);



                        }, 4000);

                    }
                    equationDisplay(self.list_equationNetworkInfoDict, 0);

                }
            }
            //schedule animation
            self.scheduleAnimation(findEquationAnimation___functionGen(), 0, 'findEquation');
            self.play(function() {
                return self.animationScheduler.animationHoldingPen.length >=2;//check that all the animation is in before playing
            }, false);
        }
        this.animate_findEquations(findEquations___readyCallback);



        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }
    
}

export {DCTwoResistorSeries};