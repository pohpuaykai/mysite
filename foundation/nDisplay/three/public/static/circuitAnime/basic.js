import {Recorder} from '../mediaRecorder/recorder.js';

class CircuitAnime {
    constructor(animationName, circuit, variableSelector, ticketing, simplify, record) {
        const self = this;
        this.circuit = circuit;// this is a circuit.js is a piece.js
        this.variableSelector = variableSelector;// it is a function that uses a list_equationNetworkInfoDict, but takes a circuit
        this.ticketing = ticketing;
        this.simplify = simplify;
        this.animationName = animationName;
        this.currentPositionInAnimation = {'idx':0}; //a dictionary that contains information about where the animation is in
        this.updateCurrentPositionInAnimation = function(state) {
            self.currentPositionInAnimation['idx'] += 1
            self.currentPositionInAnimation['state'] = state;
        }
        this.currentPositionInAudio = {'idx':0};//a dictionary that contains information about where the animation is in
        this.updateCurrentPositionInAudio = function(state) {
            self.currentPositionInAudio['idx'] += 1
            self.currentPositionInAudio['state'] = state
        }

        this.isAudioVideoInSync = function() {
            //what to check here? need to check currentPositionInAnimation&currentPositionInAudio<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            console.log('*****************************')
            console.log("videoFrame:", self.currentPositionInAnimation['idx'], "audioFrame:", self.currentPositionInAudio['idx'])
            // console.log("videoState:", self.currentPositionInAnimation['state'])
            // console.log("audioState:", self.currentPositionInAudio['state']['listOfWordLocationLengthElapsedTime'])
            console.log('*****************************')
            return self.currentPositionInAnimation['idx'] == self.currentPositionInAudio['idx']
        }

        //camera positions
        const cameraPosition = this.circuit.camera.position;
        this.facingCoordinate = {x:6*cameraPosition.x, y:6*cameraPosition.y, z:6*cameraPosition.z};
        this.vorPosition = {x:3*cameraPosition.x, y:3*cameraPosition.y, z:3*cameraPosition.z};
        this.hinPosition = {x:3*cameraPosition.x, y:3*cameraPosition.y, z:3*cameraPosition.z};

        //highlight colours
        this.componentHighlightColour = {r:0.6, g:0.1, b:0.1};
        this.componentVariableHighlightColour = {r:-0.1, g:-0.6, b:-0.1};
        this.variableHighlightColour = {r:-0.1, g:-0.6, b:-0.1}

        //pauses
        this.pauseBetweenEachVorHinDisplay = 4000;//milliseconds //this is now a minimum pause, so even if audio and video are in sync there will be this pause
        this.pauseAfterRevealingEquation = 4000;//milliseconds
        this.pauseBetweenEachVariableHighlight = 4000;//milliseconds
        // this.pauseBetweenEachComponentHighlight = 4000;//milliseconds// this is not used anymore<<<<<<<<<<<<<<<<<<<<<
        this.videoMinPauseTime_introduction_findEquation = 0;
        this.videoMinPauseTime_conclusion_findEquation = 0;
        this.videoMinPauseTime_introduction_solveEquation = 0;
        this.videoMinPauseTime_conclusion_solveEquation = 0;
        this.audioMinPauseTime_findEquations = 0;
        this.audioMinPauseTime_solveEquations = 0;


        //
        // this.audioPlayer_findEquations = null;
        // this.audioPlayer_solveEquations = null;

        //displayEquationsRelativeEquations
        this.vorHinEquationRelativePositions = 'up_down'; //the other one is left_right //this one looks prettier

        //
        this.record = record; 
        if (record) {
            this.permissionGiven = false;
            function permissionGivenCallback() {
                self.permissionGiven = true;
                console.log('self.permissionGiven: ', self.permissionGiven)
            }
            this.recorder = new Recorder(permissionGivenCallback, this.circuit.renderer.domElement);//this.circuit.renderer.domElement is the canvas of THREE?
        }
        this.loadedDatei_findEquations = false;//flag to make sure we finished loading datei for findEquation
        this.loadedDatei_solveEquations = false;//flag to make sure we finished loading datei for solveEquation
        this.gotAudio_findEquations = false;//flag to make sure we got audio
        this.gotAudio_solveEquations = false;//flag to make sure we got audio
    }

    play() {
        /* Workflow: piece.js schedule thread0...thread1
        thread0:
        - reveal equation
        - highlight component
        - unhighlight component
        - highligh component&variable
        - unhighlight component&variable

        thread1:
        - reveal vor solvingStep
        - hide vor solvingStep
        - reveal vor subSolvingStep
        - hide vor subSolvingStep
        - reveal hin solvingStep
        - hide hin solvingStep
        - reveal hin subSolvingStep
        - hide hin subSolvingStep
        */
        const self = this.circuit;
        const animeSelf = this;
        animeSelf.noop = function(...any) {}


        function solveEquation___readyCallback(){// this will be ran second...
            //load solveEquation audio

            // console.log('self.solvingSteps.length (should be 7)', self.solvingSteps.length); debugger
            self.getAudioUrls_solveEquations(
                function(list_tuple_word_location_length_elapsedTime, pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime, filename){
                    animeSelf.list_tuple_word_location_length_elapsedTime=list_tuple_word_location_length_elapsedTime; 
                    animeSelf.filename_solvingSteps = filename;
                    const entries_pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = Object.entries(pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime)
                    entries_pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime.sort((a, b)=>a[0]-b[0])
                    const pauseTimings = entries_pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime.map(([pauseIdx, d]) => {return d['endTime']})//list of timings to pause
                    // console.log(pausedTimings)
                    // debugger;
                    self.getWavFile(
                        function(audioBuffer){
                            animeSelf.audioPlayer_solveEquations = self.makeWavPlayer(audioBuffer, pauseTimings, 
                                function playerPausedCallback(pauseIdx, actualPausedTiming, plannedPausedTiming){
                                    // self.pauseUntilCallback(function(){//continue
                                    //     self.audioPlayer_solveEquations.playAudio();
                                    // }, function(){//until
                                    //     return animeSelf.isAudioVideoInSync()
                                    // }, function() {
                                    //     return animeSelf.audioMinPauseTime_solveEquations;
                                    // }());


                                    // animeSelf.updateCurrentPositionInAudio();
                                    animeSelf.updateCurrentPositionInAudio(pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[pauseIdx]);//this is more for debugging, the state is not need
                                }, 
                                function playerResumedCallback(pausedIdx, actualPausedTiming, plannedPausedTiming){

                                },
                                function readyCallback(){
                                    console.log('solvingEquation audio is in>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                    animeSelf.gotAudio_solveEquations = true
                                },
                                animeSelf.isAudioVideoInSync);
                        }, filename);
                }, 
                self.solvingSteps,
                self.runningStepsIdx__branchedStepsIdx,
                self.language_introduction_solvingSteps, 
                self.language_conclusion_solvingSteps
            );
            //
            // console.log('self.runningStepsIdx__branchedStepsIdx'); console.log(self.runningStepsIdx__branchedStepsIdx); debugger;
            let datum1 = [
                {
                    '<<>>':'introduction',
                    'introduction':''
                }
            ]

            datum1.push.apply(datum1 ,Object.entries(self.runningStepsIdx__branchedStepsIdx).map(([runningStepsIdx, branchedStepsIdx], idx)=>{
                const tag = 'eq'+idx.toString()
                const data = {
                    '<<>>':tag
                }
                data[tag] = [runningStepsIdx, branchedStepsIdx]
                return data
            }));

            datum1.push({
                '<<>>':'conclusion',
                'conclusion':''
            })

            let lastDidNotHideMeshUUID___vor = null; let lastDidNotHideMeshUUID___hin = null;
            function positionAndRevealSolvingStep(runningStepsIdx, branchedStepsIdx) {
                const latexStrMeshUUID = self.textStr__textMeshUUID[self.branchedStepsIdx__latexStrs[branchedStepsIdx]]['meshUUID'];
                const equationDimensions = self.getDimensions(latexStrMeshUUID);
                self.setRotation(latexStrMeshUUID, 0, Math.PI, 0)
                if (animeSelf.vorHinEquationRelativePositions == 'left_right') {
                    if (branchedStepsIdx[1] == 'vor') {//put it slightly to the left, the running_equation
                        //center the y
                        self.setPosition(latexStrMeshUUID, animeSelf.vorPosition.x-equationDimensions.xLen, animeSelf.vorPosition.y-(equationDimensions.yLen/2), animeSelf.vorPosition.z)
                    } else {//hin always introduce new equations
                        self.setPosition(latexStrMeshUUID, animeSelf.hinPosition.x+equationDimensions.xLen, animeSelf.hinPosition.y-(equationDimensions.yLen/2), animeSelf.hinPosition.z);
                    }
                } else if (animeSelf.vorHinEquationRelativePositions == 'up_down') {
                    if (branchedStepsIdx[1] == 'vor') {//put it slightly to the left, the running_equation
                        //center the x
                        self.setPosition(latexStrMeshUUID, animeSelf.vorPosition.x-(equationDimensions.xLen/2), animeSelf.vorPosition.y-equationDimensions.yLen, animeSelf.vorPosition.z)
                    } else {//hin always introduce new equations
                        self.setPosition(latexStrMeshUUID, animeSelf.hinPosition.x-(equationDimensions.xLen/2), animeSelf.hinPosition.y+equationDimensions.yLen, animeSelf.hinPosition.z)
                    }
                }

                //although it is a standard reveal, we still want to hide the previous, RENAME this function?
                if (self.list_runningIdx__toClearAll.includes(parseInt(runningStepsIdx)) && lastDidNotHideMeshUUID___hin !== null && lastDidNotHideMeshUUID___vor !== null) { //hide both, previous, or running_equation don't hide
                    self.hide(lastDidNotHideMeshUUID___hin)
                    self.hide(lastDidNotHideMeshUUID___vor)
                }

                self.reveal(latexStrMeshUUID);
            }

            function standardRevealSolvingStep(threadSelf, rIdx, preCalInfoDict) {
                const line = preCalInfoDict['line'];const data = line[rIdx];
                let runningStepsIdx//seems like this is not needed
                let branchedStepsIdx
                [runningStepsIdx, branchedStepsIdx] = data
                positionAndRevealSolvingStep(runningStepsIdx, branchedStepsIdx)
            }

            function standardHideSolvingStep(threadSelf, rIdx, preCalInfoDict) {
                const line = preCalInfoDict['line'];const data = line[rIdx]; // we want to hide the previous, so -1?
                let runningStepsIdx
                let branchedStepsIdx
                [runningStepsIdx, branchedStepsIdx] = data
                const latexStrMeshUUID = self.textStr__textMeshUUID[self.branchedStepsIdx__latexStrs[branchedStepsIdx]]['meshUUID'];
                if (self.list_runningIdx__toKeep.includes(parseInt(runningStepsIdx))) {
                    if (branchedStepsIdx[1] === 'vor') {
                        lastDidNotHideMeshUUID___vor = latexStrMeshUUID
                    } else if (branchedStepsIdx[1] === 'hin') {
                        lastDidNotHideMeshUUID___hin = latexStrMeshUUID
                    }
                } else {
                    self.hide(latexStrMeshUUID)
                }
            }

            const callbacks1 = {
                'introduction':{
                    'continue_recursor':function(threadSelf, rIdx, preCalInfoDict){
                        animeSelf.updateCurrentPositionInAnimation('solvingStep:introduction')//actually the state is not needed, but good for debugging
                        // animeSelf.updateCurrentPositionInAudio()
                        animeSelf.audioPlayer_solveEquations.playAudio()
                        //nothing just wait for audio to finish playing
                    },
                    'until_recursor':function(threadSelf, rIdx, preCalInfoDict){
                        return animeSelf.isAudioVideoInSync();
                    },
                    'minWaitTime_recursor':function(threadSelf, rIdx, preCalInfoDict){
                        return animeSelf.videoMinPauseTime_introduction_solveEquation
                    }
                },
                'eq0':{
                    'until_continueRecursor':function(threadSelf, rIdx, preCalInfoDict){
                        // return true
                        return animeSelf.isAudioVideoInSync();
                    },//templates can be add in Animation.js as a guide, no need to put it here?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    'minWaitTime_continueRecursor':function(threadSelf, rIdx, preCalInfoDict){
                        return animeSelf.pauseBetweenEachVorHinDisplay;
                    },
                    //'finish_recursor':function(threadSelf, rIdx, preCalInfoDict){},
                    'continue_recursor':function(threadSelf, rIdx, preCalInfoDict){
                        const facingCoordinate = animeSelf.facingCoordinate;
                        self.smoothLookAt(facingCoordinate.x, facingCoordinate.y, facingCoordinate.z, function(){
                            // console.log('**7**'); debugger
                        });
                    },
                    'continueCallbacks_recursor':[
                        function(threadSelf, rIdx, preCalInfoDict){
                            const line = preCalInfoDict['line'];
                            const data = line[rIdx];
                            let runningStepsIdx//seems like this is not needed
                            let branchedStepsIdx
                            [runningStepsIdx, branchedStepsIdx] = data
                            positionAndRevealSolvingStep(runningStepsIdx, branchedStepsIdx)
                        },
                        // animeSelf.noop,
                        standardHideSolvingStep
                    ],
                    'until_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        // return true;
                        return animeSelf.isAudioVideoInSync();
                    },
                    'minWaitTime_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        return animeSelf.pauseBetweenEachVorHinDisplay;
                    }//put in all the correct timings and then test<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                }
            }
            //add a callback for every data in 
            // for(let i=1; i<datum1.length; i++) {
            for(let i=2; i<datum1.length-1; i++) {//first one is the introduction_audio_frame, second one is the first_step. -1 for the conclusion
                callbacks1['eq'+i.toString()] = {
                    'minWaitTime_continueRecursor':function(threadSelf,rIdx, preCalInfoDict){
                        return animeSelf.pauseBetweenEachVorHinDisplay;
                    },
                    'continue_recursor':function(threadSelf, rIdx, preCalInfoDict) {
                        //hide previous eq
                        standardHideSolvingStep(threadSelf, rIdx-1, preCalInfoDict)
                        animeSelf.updateCurrentPositionInAnimation('solvingSteps:eq'+i.toString()+':hide')//actually the state is not needed, but good for debugging
                    },
                    'continueCallbacks_recursor':[standardRevealSolvingStep],
                    'until_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        // return true;
                        return animeSelf.isAudioVideoInSync();
                    },
                    'minWaitTime_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        return animeSelf.pauseBetweenEachVorHinDisplay;
                    }
                };
            }
            //add the clean up and stopRecording
            callbacks1['eq'+(datum1.length-2).toString()]['finish_recursor'] = function(threadSelf, rIdx, preCalInfoDict) {//-2 because -1 is the conclusion
                standardHideSolvingStep(threadSelf, rIdx, preCalInfoDict);// hide this equation
                // self.animationScheduler.pause(); //nessercity?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                console.log('animationScheduler.pause DONE')
                self.removeMeshesByRequestingAnimation('solveEquations', function() {//could this be a frame? like in Adobe Flash?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    //animeSelf.updateCurrentPositionInAnimation()
                    if (animeSelf.record) {
                        console.log('stopped recording')
                        self.pause(function() {

                            animeSelf.recorder.stopRecording();//maybe pause until THREE has cleared all the actors then stop? STILL MISSING a few frames at the back
                            animeSelf.recorder.sendVideoToBackend(animeSelf.formatDateTime(new Date()));
                        }, 8000)// pause for 8 seconds to make sure we get the last few frames.
                    }
                });
            }
            callbacks1['conclusion'] = {
                'continue_recursor':function(threadSelf, rIdx, preCalInfoDict) {
                    animeSelf.updateCurrentPositionInAnimation('solvingSteps:conclusion')//actually the state is not needed, but good for debugging
                },
                'until_recursor':function(threadSelf, rIdx, preCalInfoDict) {
                    return animeSelf.isAudioVideoInSync();
                },
                'minWaitTime_recursor':function(threadSelf, rIdx, preCalInfoDict) {
                    return animeSelf.videoMinPauseTime_conclusion_findEquation
                }
            }

            const thread1 = self.animeTemplate(datum1, callbacks1);
            console.log('solvingSteps init completed<<<<<<<<<<<<<<<<<<<<<<')

            self.scheduleAnimation(thread1, 1, 'solveEquation', function(){animeSelf.loadedDatei_solveEquations=true});//1 so that it will run after the findEquationAnimation

            self.start(function() {//actually why not set 2 flag for data loading of findEquations and solveEquations too?
                console.log('loadedDatei_findEquations: ', animeSelf.loadedDatei_findEquations, 'loadedDatei_solveEquations: ', animeSelf.loadedDatei_solveEquations, 'gotAudio_findEquations: ', animeSelf.gotAudio_findEquations, 'gotAudio_solveEquations: ', animeSelf.gotAudio_solveEquations)
                return animeSelf.loadedDatei_findEquations && animeSelf.loadedDatei_solveEquations && animeSelf.gotAudio_findEquations && animeSelf.gotAudio_solveEquations;//check that all the animation is in before playing, needs to let the animations signal the animationScheduler before playing<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            }, false);
        }



        function findEquations___readyCallback(){// this will be ran first.
            //once ready call for the equations to be solved first..., or this should be a Frame?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            let list_equationLatexStr; let dependentVarStr; let list_independentVarStr;
            [list_equationLatexStr, dependentVarStr, list_independentVarStr] = animeSelf.variableSelector(self)

            self.animate_solveEquations(
                solveEquation___readyCallback, 
                list_equationLatexStr, dependentVarStr, list_independentVarStr, animeSelf.animationName, animeSelf.simplify);//this will just schedule the animation...

            //audio
            // console.log('self.list_equationNetworkInfoDict', self.list_equationNetworkInfoDict);
            // console.log('self.textStr__textMeshUUID', self.textStr__textMeshUUID);
            // console.log('self.id__type', self.id__type)
            // console.log('self.language_introduction_findEquations', self.language_introduction_findEquations);
            // console.log('self.language_conclusion_findEquations', self.language_conclusion_findEquations);
            // debugger
            self.getAudioUrls_findEquations(
                function(list_tuple_word_location_length_elapsedTime, pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime, filename){
                    // animeSelf.subtitles_findEquations = subtitles; 
                    animeSelf.list_tuple_word_location_length_elapsedTime=list_tuple_word_location_length_elapsedTime; 
                    animeSelf.filename_findEquations = filename;
                    animeSelf.gotAudio_findEquations = true;
                    const entries_pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = Object.entries(pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime)
                    entries_pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime.sort((a, b)=>a[0]-b[0])
                    const pauseTimings = entries_pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime.map(([pauseIdx, d]) => {return d['endTime']})//list of timings to pause
                    // console.log(pauseTimings)
                    // debugger;
                    self.getWavFile(function(audioBuffer){
                        animeSelf.audioPlayer_findEquations = self.makeWavPlayer(audioBuffer, pauseTimings, 
                        function playerPausedCallback(pauseIdx, actualPausedTiming, plannedPausedTiming){ //need a currentPointer to the timing in animation
                            
                            // self.pauseUntilCallback(function(){//continue
                            //     self.audioPlayer_findEquations.playAudio();
                            // }, function(){//until
                            //     return animeSelf.isAudioVideoInSync()
                            // }, function() {
                            //     return animeSelf.audioMinPauseTime_findEquations;
                            // }())
                            // animeSelf.updateCurrentPositionInAudio();
                            animeSelf.updateCurrentPositionInAudio(pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[pauseIdx]);//this is not neccessary, more for debugging, the state is not needed.
                        }, 
                        function playerResumedCallback(pausedIdx, actualPausedTiming, plannedPausedTiming){
                        }, 
                        function readyCallback() {
                            console.log('made findEquation Wave player>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                            animeSelf.gotAudio_findEquations = true
                        },
                        animeSelf.isAudioVideoInSync)
                    }, filename);
                }, 
                self.list_equationNetworkInfoDict, 
                self.textStr__textMeshUUID, 
                self.id__type, 
                self.language_introduction_findEquations, 
                self.language_conclusion_findEquations
            );
            //
        //

            /*
            each item in datum0 is 
            {
              '<<>>':'eq{i}',
              'data': {
                'list_list_networkNodeIds':list_equationNetworkInfoDict[i]['list_list_networkNodeIds'],//for highlight the components used to derive equation
                'equationMeshUUID':self.textStr__textMeshUUID[list_equationNetworkInfoDict[i]['equation']]['meshUUID'] // to reveal the equation
              },
              'varComponentId':[
                  {
                    '<<>>':'eq{i}VarCId{j}',
                    'data':{
                      'componentMeshUUID': self.id__uuid[list_equationNetworkInfoDict[i]['variableStr__nodeId'][self.textStr__textMeshUUID[graphInfoD['equation']]['info'][j]['variableStr']]],//for component un|highlighting
                      'list_varChaStr,chaMeshUUID':self.textStr__textMeshUUID[list_equationNetworkInfoDict[i]['equation']]['info'][j]['info'],//for variable un|highlighting
                    }
                  },

              ]
            }
            */
            let datum0 = []; let callbacks0 = {}; let startInCallbackIdx = 1;//the extra 1 is for the introduction

            if (animeSelf.record) {
                const recordingTag = 'startRecording';
                datum0 = [{
                    'startRecording':{},
                    '<<>>':recordingTag
                }];
                callbacks0[recordingTag] = {
                    'continue_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        console.log('started recording in anime')
                        animeSelf.recorder.startRecording();
                        // threadSelf();//this is thread0
                    },
                    'until_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        console.log('checking if flag: animeSelf.permissionGiven is true: ', animeSelf.permissionGiven)
                        return animeSelf.permissionGiven
                    },
                    'minWaitTime_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        return 0;
                    }//no minWait time for recording
                };
                startInCallbackIdx = 2//the extra 1 is for the introduction
            }

            datum0.push({
                '<<>>':'introduction',
                'introduction':''
            });


            for (let i=0; i<self.list_equationNetworkInfoDict.length; i++) {
                const equationNetworkInfoDict = self.list_equationNetworkInfoDict[i];
                const key0 = 'eq'+i.toString()
                const item = {
                    '<<>>':key0,
                    'varComponentId':[]
                }
                item[key0] = {
                    'list_list_networkNodeIds':equationNetworkInfoDict['list_list_networkNodeIds'],//for highlight the components used to derive equation
                    'equationMeshUUID':self.textStr__textMeshUUID[equationNetworkInfoDict['equation']]['meshUUID'] // to reveal the equation
                }
                const list_list_variableStr__nodeId = Object.entries(equationNetworkInfoDict['variableStr__nodeId']);
                const variableInfoD = self.textStr__textMeshUUID[equationNetworkInfoDict['equation']]['info'];
                //console.log("self.textStr__textMeshUUID[equationNetworkInfoDict['equation']]", self.textStr__textMeshUUID[equationNetworkInfoDict['equation']])
                for(let j=0; j<variableInfoD.length; j++) {
                    const key1 = key0+'VarCId'+j.toString()
                    const item0 = {
                        '<<>>':key1,
                    }
                    item0[key1] = {
                      'componentMeshUUID': self.id__uuid[equationNetworkInfoDict['variableStr__nodeId'][variableInfoD[j]['variableStr']]],//for component un|highlighting
                      'list_varChaStr,chaMeshUUID':self.textStr__textMeshUUID[equationNetworkInfoDict['equation']]['info'][j]['info'],//for variable un|highlighting
                    }
                    item['varComponentId'].push(item0)
                }
                datum0.push(item);
            }

            datum0.push({
                '<<>>':'conclusion',
                'conclusion':''
            });

            // const waitTime = 1000;//change to the standard here<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            const componentDisplay = function(list_list_networkNodeIds){
                //[2]
                //graphInfoD['list_list_networkNodeIds']
                list_list_networkNodeIds.forEach(list_nodeId => {
                    // console.log('highlighting list_nodeId: ', graphInfoD['list_list_networkNodeIds'], '<<<HL<<')
                    const visited = []; // nodeId might be repeated
                    list_nodeId.forEach(nodeId => {
                        // console.log('highlight nodeId', nodeId, ' type: ', id__type[nodeId], ' meshId: ', id__uuid[nodeId]); 
                        if (visited.indexOf(nodeId) <0) {
                            visited.push(nodeId)
                            self.highlight({meshUUID:self.id__uuid[nodeId], redMag:animeSelf.componentHighlightColour.r, greenMag:animeSelf.componentHighlightColour.g, blueMag:animeSelf.componentHighlightColour.b})

                        }
                    })
                });
            }
            const formulaDisplay = function(equationMeshUUID){
                //[3]
                //const equationMeshUUID = self.textStr__textMeshUUID[graphInfoD['equation']]['meshUUID']
                const equationDimensions = self.getDimensions(equationMeshUUID);
                // console.log('getting dimensions: ', equationDimensions);
                // self.highlight({meshUUID:equationMeshUUID, redMag:0.6, greenMag:0.1, blueMag:0.1}); //this group does not even have attributes and cannot be highlighted this way
                self.setPosition(equationMeshUUID, equationDimensions.xLen/2, equationDimensions.yLen/2, equationDimensions.zLen+50);
                self.reveal(equationMeshUUID); //self.renderer.render(self.scene, self.camera);
            }
            const componentHide = function(list_list_networkNodeIds){
                //[4] unhighlight network
                // self.unhighlight(equationMeshUUID);
                //graphInfoD['list_list_networkNodeIds']
                list_list_networkNodeIds.forEach(list_nodeId => {
                // console.log('UNhighlighting list_nodeId: ', graphInfoD['list_list_networkNodeIds'], '<<<UN<<')
                    const visited = [];
                    list_nodeId.forEach(nodeId => {
                        if (visited.indexOf(nodeId) <0) {
                            // console.log('unhightlight nodeId', nodeId, ' type: ', id__type[nodeId]); 
                            self.unhighlight(self.id__uuid[nodeId])
                        }
                    })
                });
            }
            const formulaHide = function(equationMeshUUID){
                //const equationMeshUUID = self.textStr__textMeshUUID[graphInfoD['equation']]['meshUUID']
                self.hide(equationMeshUUID); //self.renderer.render(self.scene, self.camera);
            }
            const highlightVarComponent = function(componentMeshUUID, list_varChaStr__chaMeshUUID) {
                //const variableInfoD = list_variableInfoD[list_variableInfoD___idx]
                //const variableStr = variableInfoD['variableStr'];
                //[7]
                //highlight variableComponent
                //const componentMeshUUID = self.id__uuid[graphInfoD['variableStr__nodeId'][variableStr]]
                self.highlight({meshUUID: componentMeshUUID, redMag:animeSelf.componentVariableHighlightColour.r, greenMag:animeSelf.componentVariableHighlightColour.g, blueMag:animeSelf.componentVariableHighlightColour.b})
                // console.log('highlighted variableNodes', window.performance.now())
                //[8] each chaStr is only a part of the variable, so we want them to light up togehter
                // variableInfoD['info'].
                list_varChaStr__chaMeshUUID.forEach(([chaStr, charMeshUUID]) => {
                    self.highlight({meshUUID:charMeshUUID, redMag:animeSelf.variableHighlightColour.r, greenMag:animeSelf.variableHighlightColour.g, blueMag:animeSelf.variableHighlightColour.b});
                    // console.log('highlighted: ', chaStr, ' uuid: ', charMeshUUID, '<<<<<<<<<<<<<<<<<<<<<<<variable highlighting????????????????????????????????????????????????????')
                })
            }
            const unhighlightVarComponent = function(componentMeshUUID, list_varChaStr__chaMeshUUID) {
                //const variableInfoD = list_variableInfoD[list_variableInfoD___idx]
                // const variableStr = variableInfoD['variableStr'];
                //[9]
                // self.unhighlight(self.id__uuid[graphInfoD['variableStr__nodeId'][variableStr]])
                self.unhighlight(componentMeshUUID)
                // console.log('unhighlight variableNode', window.performance.now())
                //[10]
                // variableInfoD['info']
                list_varChaStr__chaMeshUUID.forEach(([chaStr, charMeshUUID]) => {
                    // console.log('chaStr', chaStr, 'charMeshUUID', charMeshUUID)
                    self.unhighlight(charMeshUUID)
                })
            }

            callbacks0['introduction'] = {
                'continue_recursor':function(threadSelf, rIdx, preCalInfoDict){
                    animeSelf.audioPlayer_findEquations.playAudio()
                    // animeSelf.updateCurrentPositionInAnimation()
                    animeSelf.updateCurrentPositionInAnimation('findEquations:introduction')//actually the state is not needed, but good for debugging
                    // animeSelf.updateCurrentPositionInAudio()//only advance when the audio pause, to stop the video, this is done in wavePlayer
                    //nothing just wait for audio to finish playing
                },
                'until_recursor':function(threadSelf, rIdx, preCalInfoDict){
                    return animeSelf.isAudioVideoInSync();
                },
                'minWaitTime_recursor':function(threadSelf, rIdx, preCalInfoDict){
                    return animeSelf.videoMinPauseTime_introduction_findEquation
                }

            }

            //only the first callback and last callback are different

            let tagIdOffset = -1 * startInCallbackIdx
            let variableStr; let nodeId
            for(let i=startInCallbackIdx; i<datum0.length-1; i++) {//-1 for the conclusion
                callbacks0['eq'+(i+tagIdOffset).toString()]={//eq0
                    'until_continueRecursor':function(threadSelf,rIdx, preCalInfoDict){
                        return animeSelf.isAudioVideoInSync();
                        // return true;
                    },
                    'minWaitTime_continueRecursor':function(threadSelf,rIdx, preCalInfoDict){
                        return 0;//no pause for hiding Component?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    },
                    'continue_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        const line = preCalInfoDict['line'];
                        const list_list_networkNodeIds = line[rIdx]['list_list_networkNodeIds'];
                        const equationMeshUUID = line[rIdx]['equationMeshUUID'];
                        componentDisplay(list_list_networkNodeIds);
                        formulaDisplay(equationMeshUUID);
                        // animeSelf.updateCurrentPositionInAnimation()
                        animeSelf.updateCurrentPositionInAnimation('findEquations: eq'+(i+tagIdOffset).toString()+':display');//actually the state is not needed, but good for debugging
                    },
                    'continueCallbacks_recursor':[
                        function(threadSelf,rIdx, preCalInfoDict){
                            const line = preCalInfoDict['line'];
                            const list_list_networkNodeIds = line[rIdx]['list_list_networkNodeIds'];
                            componentHide(list_list_networkNodeIds)
                            // animeSelf.updateCurrentPositionInAnimation();//display and hide same data<<<<<<<<? no need to advance
                        }
                    ],
                    'until_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        return animeSelf.isAudioVideoInSync();
                    },//extend to audio later<<<<<<<<<<<<<<<<<<<<
                    'minWaitTime_recursor':function(threadSelf,rIdx, preCalInfoDict){
                        return animeSelf.pauseAfterRevealingEquation;
                    }
                }
                for(let j=0; j<datum0[i]['varComponentId'].length; j++) {
                    const varCallbacks = {//for the variableStrComponentnodeId
                        'until_continueRecursor':function(threadSelf,rIdx, preCalInfoDict){
                            return animeSelf.isAudioVideoInSync();
                            // return true;
                        },
                        'minWaitTime_continueRecursor':function(threadSelf,rIdx, preCalInfoDict){
                            return 0;
                        },
                        //'finish_recursor':function(threadSelf,rIdx, preCalInfoDict){},
                        'continue_recursor':function(threadSelf,rIdx, preCalInfoDict){
                            // console.log('highlightVarComponent')
                            const line = preCalInfoDict['line'];
                            const componentMeshUUID = line[rIdx]['componentMeshUUID'];
                            const list_varChaStr__chaMeshUUID = line[rIdx]['list_varChaStr,chaMeshUUID']
                            highlightVarComponent(componentMeshUUID, list_varChaStr__chaMeshUUID);
                        },
                        'continueCallbacks_recursor':[
                        ],
                        'until_recursor':function(threadSelf,rIdx, preCalInfoDict){
                            return animeSelf.isAudioVideoInSync();
                        },
                        'minWaitTime_recursor':function(threadSelf,rIdx, preCalInfoDict){
                            return animeSelf.pauseBetweenEachVariableHighlight;
                        }
                    };
                    if (j == datum0[i]['varComponentId'].length-1) {
                        varCallbacks['continueCallbacks_recursor'].push(function(threadSelf, rIdx, preCalInfoDict) {
                            const line = preCalInfoDict['line'];
                            const componentMeshUUID = line[rIdx]['componentMeshUUID'];
                            const list_varChaStr__chaMeshUUID = line[rIdx]['list_varChaStr,chaMeshUUID']
                            unhighlightVarComponent(componentMeshUUID, list_varChaStr__chaMeshUUID);
                            // animeSelf.updateCurrentPositionInAnimation()
                            // animeSelf.updateCurrentPositionInAnimation('findEquations: eq'+(i+tagIdOffset).toString()+'VarCId'+j.toString()+':highlightVarComponent');//actually the state is not needed, but good for debugging
                        });
                        varCallbacks['continueCallbacks_recursor'].push(animeSelf.noop);
                        varCallbacks['continueCallbacks_recursor'].push(
                            function(threadSelf, rIdx, preCalInfoDict) {
                                const taggedWidthDepthIdx__tagName = preCalInfoDict['taggedWidthDepthIdx__tagName'];
                                const dataLinearIdx__widthDepthIdx = preCalInfoDict['dataLinearIdx__widthDepthIdx'];
                                const tagName = taggedWidthDepthIdx__tagName[dataLinearIdx__widthDepthIdx[rIdx]]
                                const eqName = tagName.split('VarCId')[0]
                                const line = preCalInfoDict['line'];
                                const tagName__taggedWidthDepthIdx = preCalInfoDict['tagName__taggedWidthDepthIdx'];
                                const widthDepthIdx__dataLinearIdx = preCalInfoDict['widthDepthIdx__dataLinearIdx'];
                                const equationMeshUUID = line[parseInt(widthDepthIdx__dataLinearIdx[tagName__taggedWidthDepthIdx[eqName]])]['equationMeshUUID']
                                formulaHide(equationMeshUUID)
                                animeSelf.updateCurrentPositionInAnimation('findEquations: eq'+(i+tagIdOffset).toString()+'VarCId'+j.toString()+':highlightVarComponent');//actually the state is not needed, but good for debugging
                            });

                    } else {
                        varCallbacks['continueCallbacks_recursor'].push(function(threadSelf, rIdx, preCalInfoDict) {
                            const line = preCalInfoDict['line'];
                            const componentMeshUUID = line[rIdx]['componentMeshUUID'];
                            const list_varChaStr__chaMeshUUID = line[rIdx]['list_varChaStr,chaMeshUUID']
                            unhighlightVarComponent(componentMeshUUID, list_varChaStr__chaMeshUUID);
                            // animeSelf.updateCurrentPositionInAnimation()
                            animeSelf.updateCurrentPositionInAnimation('findEquations: eq'+(i+tagIdOffset).toString()+'VarCId'+j.toString()+':highlightVarComponent');//actually the state is not needed, but good for debugging
                        });
                    }
                    callbacks0['eq'+(i+tagIdOffset).toString()+'VarCId'+j.toString()] = varCallbacks
                }

            }
            // debugger;
            //-2 for the conclusion
            callbacks0['eq'+(datum0.length-2+tagIdOffset).toString()+'VarCId'+(datum0[datum0.length-2+tagIdOffset]['varComponentId'].length-1).toString()]['finish_recursor'] = function(threadSelf,rIdx, preCalInfoDict){
                self.removeMeshesByRequestingAnimation('findEquations', function(){});
                self.animationScheduler.playNextAnimation()
            }
            callbacks0['conclusion'] = {
                'continue_recursor':function(threadSelf, rIdx, preCalInfoDict){
                    // animeSelf.updateCurrentPositionInAnimation()
                    animeSelf.updateCurrentPositionInAnimation('findEquations:conclusion');//actually the state is not needed, but good for debugging
                    //nothing just wait for audio to finish playing
                },
                'until_recursor':function(threadSelf, rIdx, preCalInfoDict){
                    return animeSelf.isAudioVideoInSync();
                },
                'minWaitTime_recursor':function(threadSelf, rIdx, preCalInfoDict){
                    return animeSelf.videoMinPauseTime_conclusion_findEquation
                }
            }
            //
            // console.log('datum0', datum0);
            // console.log('callbacks0', callbacks0); 
            // debugger
            const thread0 = self.animeTemplate(datum0, callbacks0);

            self.scheduleAnimation(thread0, 0, 'findEquation', function(){animeSelf.loadedDatei_findEquations=true;});
            console.log('findEquations init completed<<<<<<<<<<<<<<<<<<<<<<<<<<')

        }


        self.animate_findEquations(findEquations___readyCallback, animeSelf.animationName);//within animate_findEquations, calls animate_solveEquations
    }




    formatDateTime(date) {
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0'); // Months are 0-indexed
      const day = String(date.getDate()).padStart(2, '0');
      const hours = String(date.getHours()).padStart(2, '0');
      const minutes = String(date.getMinutes()).padStart(2, '0');
      const seconds = String(date.getSeconds()).padStart(2, '0');

      // return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
      return `${year}${month}${day}${hours}${minutes}${seconds}`;
    }
}

export {CircuitAnime}