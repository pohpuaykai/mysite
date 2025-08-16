

class CircuitAnime {
    constructor(circuit, variableSelector) {
        this.circuit = circuit;// this is a circuit.js
        this.variableSelector = variableSelector;// it is a function that uses a list_equationNetworkInfoDict, but takes a circuit
    }

    play() {
        const self = this.circuit;
        const animeSelf = this;

        function solveEquation___readyCallback() {

            function solveEquation___functionGen(
                /**
                 * 
                 * At the last of each list of subSteps, hold the 
                 * 
                 * 
                 * you can know if it is the last of subSteps, by using
                 * self.solvingSteps
                 * &&
                 * branchedStepsIdx
                 * **/

            ) {
                return function() {
                    /**
                     * We have :
                     * self.steps
                     * self.branchedStepsIdx__latexStrs
                     * self.runningStepsIdx__branchedStepsIdx
                     * self.list_runningIdx__toClearAll
                     * self.list_runningIdx__toKeep
                     * 
                     * also the latexMeshes from LatexMeshCreater.js
                     *  self.textStr__textMeshUUID
                     *  self.meshUUID__mesh
                     * **/
                    console.log('self.branchedStepsIdx__latexStrs', self.branchedStepsIdx__latexStrs)
                    console.log('self.runningStepsIdx__branchedStepsIdx', self.runningStepsIdx__branchedStepsIdx)
                    console.log('self.list_runningIdx__toClearAll', self.list_runningIdx__toClearAll)
                    console.log('self.list_runningIdx__toKeep', self.list_runningIdx__toKeep)
                    // debugger

                    const cameraPosition = self.camera.position;
                    console.log(cameraPosition)
                    // debugger

                    console.log('running solveEquation animation is running')
                    // look back.
                    const facingCoordinate = {x:6*cameraPosition.x, y:6*cameraPosition.y, z:6*cameraPosition.z};
                    self.smoothLookAt(facingCoordinate.x, facingCoordinate.y, facingCoordinate.z, function(){
                    // self.smoothMoveCameraPosition(facingCoordinate.x, facingCoordinate.y, facingCoordinate.z ,function() {
                        console.log('finished looking back'); let previousEquationType = 'vor'; 
                        let lastDidNotHideMeshUUID___vor = null; let lastDidNotHideMeshUUID___hin = null;
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
                            if (branchedStepsIdx[1] == 'vor') {//put it slightly to the left, the running_equation
                                self.setPosition(latexStrMeshUUID, facingCoordinate.x-equationDimensions.xLen, facingCoordinate.y, facingCoordinate.z);
                            } else {//hin always introduce new equations
                                self.setPosition(latexStrMeshUUID, facingCoordinate.x+equationDimensions.xLen, facingCoordinate.y, facingCoordinate.z);
                            }


                            if (self.list_runningIdx__toClearAll.includes(parseInt(runningStepsIdx)) && lastDidNotHideMeshUUID___hin !== null && lastDidNotHideMeshUUID___vor !== null) { //hide both, previous, or running_equation don't hide
                                console.log('going to clear screen')
                                // debugger;
                                self.hide(lastDidNotHideMeshUUID___hin)
                                self.hide(lastDidNotHideMeshUUID___vor)
                            }


                            self.reveal(latexStrMeshUUID); 
                            console.log('revealed: ', self.branchedStepsIdx__latexStrs[branchedStepsIdx], branchedStepsIdx)
                            self.pause(()=>{
                                /**
                                 * branchedStepsIdx = [stepIdx, 'vor', subStepIdx, 'vor__subSteps']; 
                                 * 
                                 * 
                                 * **/
                                // console.log('runningStepsIdx', runningStepsIdx, 'list_runningIdx__toKeep', self.list_runningIdx__toKeep, ' in? ', self.list_runningIdx__toKeep.includes(parseInt(runningStepsIdx))); debugger;
                                if (self.list_runningIdx__toKeep.includes(parseInt(runningStepsIdx))) {
                                    if (branchedStepsIdx[1] === 'vor') {
                                        lastDidNotHideMeshUUID___vor = latexStrMeshUUID
                                    } else if (branchedStepsIdx[1] === 'hin') {
                                        lastDidNotHideMeshUUID___hin = latexStrMeshUUID
                                    }
                                } else {
                                    self.hide(latexStrMeshUUID)
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
            let list_equationLatexStr; let dependentVarStr; let list_independentVarStr;
            [list_equationLatexStr, dependentVarStr, list_independentVarStr] = animeSelf.variableSelector(self)

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
        self.animate_findEquations(findEquations___readyCallback);



    }
}

export {CircuitAnime}