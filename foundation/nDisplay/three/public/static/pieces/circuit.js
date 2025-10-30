import {Wire} from '../meshes/Wire.js';
import {Piece} from './piece.js';
import {Animation} from '../custom/Animation.js';

//all the components
import {ComponentBattery} from '../meshes/ComponentBattery.js';
import {ComponentACSignalGenerator} from '../meshes/ComponentACSignalGenerator.js';
import {ComponentResistor} from '../meshes/ComponentResistor.js';
import {ComponentDiode} from '../meshes/ComponentDiode.js';
import {ComponentCapacitor} from '../meshes/ComponentCapacitor.js';
import {ComponentInductor} from '../meshes/ComponentInductor.js';
import {ComponentTransistor} from '../meshes/ComponentTransistor.js';
import {ComponentOscillator} from '../meshes/ComponentOscillator.js'

class Circuit extends Piece{
    
    constructor(scene, camera, renderer, audioContext, controls, meshes) {
        super(scene, camera, renderer, audioContext, controls, meshes);

        this.animationAggregator = new Animation(scene, camera, renderer);
        
        this.wiring = [];
        // this.wiringSansWires = [];//originally for rcclorthogonallayout, but to differentiate parallel_circuit from series_circuit, we need wire nodes. so... this is defunked for now
        this.uuid__type = {};
        this.uuid__positiveLeadsDirections = {};
        this.edgeUUID__solderableIndices = {};
        this.edge__solderableIndices = {};

        this.type__boundingBox = {};//<<<<<<<<<<<<<put into one endpoint, then query

        //getBBox of each schematic size
        function getBBoxFromSVGString(svgString) {

            // Parse the SVG string
            const parser = new DOMParser();
            const svgDoc = parser.parseFromString(svgString, "image/svg+xml");
            const svgElement = svgDoc.documentElement;

            // Append to DOM (hidden)
            svgElement.style.position = "absolute";
            svgElement.style.visibility = "hidden";
            svgElement.style.pointerEvents = "none";
            svgElement.style.width = "auto";
            svgElement.style.height = "auto";
            document.body.appendChild(svgElement);

            // Now getBBox
            const bbox = svgElement.getBBox();
            // console.log(bbox);

            // Optional: clean up
            svgElement.remove();
            return bbox;

        }

        //TODO this is currently not being used, maybe a new Genre of Anime, can have the schematic included<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // let componenttypeSVGFilepath_ajax = new XMLHttpRequest(); this.componentType__boundingBox = {}; const self = this;
        // componenttypeSVGFilepath_ajax.addEventListener("load", function() {
        //     const componenttype__svgfilepath___str = componenttypeSVGFilepath_ajax.responseText;
        //     const COMPONENTTYPE__SVGFILEPATH___entries = Object.entries(JSON.parse(componenttype__svgfilepath___str));
        //     // console.log(COMPONENTTYPE__SVGFILEPATH___entries);
        //     let componentType; let svgFilepath;let absolutePath;
        //     for (let i=0; i<COMPONENTTYPE__SVGFILEPATH___entries.length; i++) {
        //         // if (COMPONENTTYPE__SVGFILEPATH___entries[i] != undefined) { //https://developer.mozilla.org/en-US/docs/Web/API/SVGGraphicsElement/getBBox
        //             [componentType, svgFilepath] = COMPONENTTYPE__SVGFILEPATH___entries[i];
        //             absolutePath = '/public/static/'+svgFilepath;
        //             let ajax = new XMLHttpRequest();
        //             ajax.addEventListener("load", function(componentType) {
        //                 return function () {
        //                     // console.log(ajax.responseText);
        //                     let svgString = ajax.responseText;
        //                     let svgBBox = getBBoxFromSVGString(svgString);
        //                     // console.log(componentType, svgBBox);
        //                     // self.componentType__boundingBox[componentType] = svgBBox;
        //                     self.componentType__boundingBox[componentType] = {'width':svgBBox.width, 'height':svgBBox.height};
        //                     // console.log('componentType__boundingBox', JSON.stringify(self.componentType__boundingBox));
        //                 }
        //             }(componentType));
        //             // console.log(componentType, absolutePath);
        //             ajax.open("GET", absolutePath);
        //             ajax.send();
        //     }
        // });
        // componenttypeSVGFilepath_ajax.open("GET", "/public/static/settings/ComponentType__SVGFilepath.json");//hide this link?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // componenttypeSVGFilepath_ajax.send();
    }


    animate_findEquations(readyCallback, animationName) {//TODO meshToAnimation, should take a 
        const self = this;
        function CALLBACK__findEquations(list_equationNetworkInfoDict){
            self.list_equationNetworkInfoDict = list_equationNetworkInfoDict;
            let latexStrs = [];
            for(let i=0; i<list_equationNetworkInfoDict.length; i++) {
                latexStrs.push([list_equationNetworkInfoDict[i]['equation'], list_equationNetworkInfoDict[i]['variables']]);
            }
            latexStrs = [...new Set(latexStrs)];
            self.makeLatexMesh(latexStrs, readyCallback, 'findEquations'); // also give latexStr to variables mapping
        }

        this.findEquations(CALLBACK__findEquations);
        
    }

    findEquations(callback) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();
        const self = this;
        xhr.onreadystatechange = function(){

            function handleResponseText(responseText) {
                const list_equationNetworkInfoDict = JSON.parse(responseText);
                callback(list_equationNetworkInfoDict);
            }

            if (this.readyState == 4 && this.status == 200) {
              if (isNaN(parseInt(this.responseText))) {//not a ticket, its the actual
                handleResponseText(this.responseText);
              } else if(this.responseText.length > 0) {//is a ticketNum
                const ticketNum = this.responseText;
                function ticketCallback(responseText) {
                    handleResponseText(responseText);
                }
                self.pollForTicket(ticketNum, ticketCallback);
              }
            }
        }
        // xhr.onerror = function(){}
        xhr.open('POST', findEquations_url);
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        // xhr.setRequestHeader('Content-Type', 'application/json');
        self.getNetworkGraph();
        // console.log('this.id__type', this.id__type); debugger;

        xhr.send(JSON.stringify({
            'circuitName':self.circuitName,
            'networkGraph':self.networkGraph, //circuit.networkGraph,
            'id__type':self.id__type,//circuit.id__type,
            'id__positiveLeadsDirections':self.id__positiveLeadsDirections,//circuit.id__positiveLeadsDirections,
            'edge__solderableIndices':self.edge__solderableIndices,//circuit.edge__solderableIndices
            'wantsTicket':true
        }));
    }

    animate_solveEquations(readyCallback, list_equationStr, dependentVarStr, list_independentVarStr, animationName, simplify) {
        //
    // list_equationStr
    // id__type
    // dependentVarStr
    // list_independentVarStr
        const self = this;
        function CALLBACK__solveEquations(steps, latexStrs) {
            self.makeLatexMesh(latexStrs, readyCallback, 'solveEquations');
            // console.log('step.length (should be 7)', steps.length); debugger
            self.solvingSteps = steps;//<<<<<<<<<<<<<<<<<<<not very elegant?
            // console.log('self.solvingSteps.length (should be 7)', self.solvingSteps.length); debugger
        }
        this.solveEquations(CALLBACK__solveEquations, list_equationStr, dependentVarStr, list_independentVarStr, simplify)
    }

    solveEquations(callback, list_equationStr, dependentVarStr, list_independentVarStr, simplify) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();
        const self = this;
        xhr.onreadystatechange  = function(){

            function handleResponseText(responseText) {
              const responseDict = JSON.parse(responseText);
              const steps = responseDict['steps']// this is solving step, you can call getAudio here...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
              // console.log('step.length (should be 7)', steps.length); debugger
              const branchedStepsIdxs = responseDict['branchedStepsIdxs']
              const latexStrs = responseDict['latexStrs']// not needed: list_tuple_latexStrVariableStr
              const list_tuple_latexStrVariableStr = responseDict['list_tuple_latexStrVariableStr']
              const list_runningIdx__toClearAll = responseDict['list_runningIdx__toClearAll']
              const list_runningIdx__toKeep = responseDict['list_runningIdx__toKeep']

              const branchedStepsIdx__latexStrs = {}; let branchedStepsIdx; let latexStr;
              for(let i=0; i<branchedStepsIdxs.length; i++) {
                branchedStepsIdx = branchedStepsIdxs[i]; latexStr = latexStrs[i];
                branchedStepsIdx__latexStrs[branchedStepsIdx] = latexStr
              }
              const runningStepsIdx__branchedStepsIdx = responseDict['runningStepsIdx__branchedStepsIdx']
              self.steps = steps;
              // console.log('step.length (should be 7)', self.steps.length); debugger
              self.branchedStepsIdx__latexStrs = branchedStepsIdx__latexStrs;
              self.runningStepsIdx__branchedStepsIdx = runningStepsIdx__branchedStepsIdx;
              self.list_runningIdx__toClearAll = list_runningIdx__toClearAll;
              self.list_runningIdx__toKeep = list_runningIdx__toKeep;
              callback(steps, list_tuple_latexStrVariableStr);

            }

            if (this.readyState == 4 && this.status == 200) {
              if (isNaN(parseInt(this.responseText))) {//not a ticket, its the actual
                handleResponseText(this.responseText);
              } else if(this.responseText.length > 0) {//is a ticketNum
                const ticketNum = this.responseText;
                function ticketCallback(responseText) {
                    handleResponseText(responseText);
                }
                self.pollForTicket(ticketNum, ticketCallback);
              }
              // asyncCreateLatexMesh(scene, renderer, camera, listOfEquations_latexStrs);
            }
        }
        // xhr.onerror = function(){}
        xhr.open('POST', solveEquations_url);
        xhr.setRequestHeader('X-CSRFToken', csrftoken);

        xhr.send(JSON.stringify({
            'circuitName':self.circuitName,
            'list_equationStr':list_equationStr,
            'id__type':self.id__type,
            'dependentVarStr':dependentVarStr,
            'list_independentVarStr':list_independentVarStr,
            'simplify':simplify, //<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO test
            'wantsTicket':true
        }));

    }

    //[start] animeAudio
    getAudioUrls_findEquations(
        callback, 
        list_equationNetworkInfoDict, 
        textStr__textMeshUUID, 
        id__type, 
        language_introduction_findEquations, 
        language_conclusion_findEquations
    ) {

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();
        const self = this;
        xhr.onreadystatechange  = function(){

            function handleResponseText(responseText) {
              const responseDict = JSON.parse(responseText);

              self.tag__getAudioUrls_findEquations = responseDict['tag']
              callback(responseDict['language__filepaths'][self.audioLanguage])

            }

            if (this.readyState == 4 && this.status == 200) {
              if (isNaN(parseInt(this.responseText))) {//not a ticket, its the actual
                handleResponseText(this.responseText);
              } else if(this.responseText.length > 0) {//is a ticketNum
                const ticketNum = this.responseText;
                function ticketCallback(responseText) {
                    handleResponseText(responseText);
                }
                self.pollForTicket(ticketNum, ticketCallback);
              }
              // asyncCreateLatexMesh(scene, renderer, camera, listOfEquations_latexStrs);
            }
        }
        // xhr.onerror = function(){}
        xhr.open('POST', basic_findEquations_audioFiles_url);
        xhr.setRequestHeader('X-CSRFToken', csrftoken);


        xhr.send(JSON.stringify({
            'circuitName':self.circuitName,
            'list_equationNetworkInfoDict':list_equationNetworkInfoDict,
            'textStr__textMeshUUID':textStr__textMeshUUID,
            'id__type':id__type,
            'language':self.audioLanguage,
            'introduction_findEquations':language_introduction_findEquations[self.audioLanguage],
            'conclusion_findEquations':language_conclusion_findEquations[self.audioLanguage],
            // 'wantsTicket':true// this is always ticketed
        }));
    }
    getAudioUrls_solveEquations(
        callback, 
        solvingSteps, 
        runningStepsIdx__branchedStepsIdx, 
        language_introduction_solvingSteps, 
        language_conclusion_solvingSteps
    ) {

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();
        const self = this;
        xhr.onreadystatechange = function(){

            function handleResponseText(responseText) {
              const responseDict = JSON.parse(responseText);

              self.tag__getAudioUrls_solveEquations = responseDict['tag']
              callback(responseDict['language__filepaths'][self.audioLanguage])

            }

            if (this.readyState == 4 && this.status == 200) {
              if (isNaN(parseInt(this.responseText))) {//not a ticket, its the actual
                handleResponseText(this.responseText);
              } else if(this.responseText.length > 0) {//is a ticketNum
                const ticketNum = this.responseText;
                function ticketCallback(responseText) {
                    handleResponseText(responseText);
                }
                self.pollForTicket(ticketNum, ticketCallback);
              }

            }
        }
        // xhr.onerror = function(){}
        xhr.open('POST', basic_solvingSteps_audioFiles_url);
        xhr.setRequestHeader('X-CSRFToken', csrftoken);

        xhr.send(JSON.stringify({
            'circuitName':self.circuitName,
            'solvingSteps':solvingSteps, 
            'runningStepsIdx__branchedStepsIdx':runningStepsIdx__branchedStepsIdx,
            'language':self.audioLanguage,
            'introduction_solvingSteps':language_introduction_solvingSteps[self.audioLanguage], 
            'conclusion_solvingSteps':language_conclusion_solvingSteps[self.audioLanguage],
            // 'wantsTicket':true// this is always ticketed
        }));
    }
    getWavFile(callback, wavFilename) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'arraybuffer';
        const self = this;
        xhr.onreadystatechange = function(){
            if (this.readyState == 4 && this.status == 200) {
                const audioContext = new (window.AudioContext || window.webkitAudioContext)();//maybe you can just pass this to the makeWavPlayer, so that it is not duplicating work?
                const arrayBuffer = this.response;//this is the arraybuffer
                audioContext.decodeAudioData(arrayBuffer).then(function(audioBuffer){
                    callback(audioBuffer)
                });
            }
        }
        xhr.open('POST', wavFiles_url, true);
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        const formData = new FormData();

        console.log('making formData')
        formData.append('filename', wavFilename)
        console.log('wavFileName: ', wavFilename)
        xhr.send(formData)
        console.log('sent!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    }

    sendSubtitles(list_subtitles_findEquations, list_subtitles_solveEquations) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'arraybuffer';
        const self = this;
        //xhr.onreadystatechange = //no needed for now
        xhr.open('POST', subtitlesTimingRecord_url, true);
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        
        xhr.send(JSON.stringify({
            'circuitName':self.circuitName,
            'list_subtitles_findEquations':list_subtitles_findEquations,
            'tag__getAudioUrls_findEquations':self.tag__getAudioUrls_findEquations,
            'tag__getAudioUrls_solveEquations':self.tag__getAudioUrls_solveEquations,
            'list_subtitles_solveEquations':list_subtitles_solveEquations,
            'language':self.audioLanguage
        }));

    }

    makeWavPlayer(audioBuffer, pauseTimings, playerPausedCallback, playerResumedCallback, readyCallback, checkIfAudioVideoInSync) {//this is not used, maybe rename to something more specific?, this is made to pause at timings, stipulated by the user, but it is not working very well
        //maybe put this in its own file?
        class WavPlayer {
            constructor(audioBuffer, pauseTimings, playerPausedCallback, playerResumedCallback, readyCallback, checkIfAudioVideoInSync) {
                this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
                this.audioBuffer = audioBuffer;
                this.startOffset = 0;
                this.startTime = 0;
                this.source;// = this.audioContext.createBufferSource();
                this.pauseTimings = pauseTimings;
                // console.log('this.pauseTimings: ', this.pauseTimings)
                this.playerPausedCallback = playerPausedCallback;
                this.playerResumedCallback = playerResumedCallback;
                this.checkIfAudioVideoInSync = checkIfAudioVideoInSync;
                this.readyCallback = readyCallback;
                this.paused = true;
                //this.alreadyInitWatcher = false;
                this.pausedTimingLastIndex = 0;
                this.readyCallback()
                //
            }

            initTimingReachedWatcher() {
                const self = this;
                let isProcessingInterval = false;
                const intervalId = setInterval(function(){
                    if (isProcessingInterval) {return}
                    let sliced = self.pauseTimings.slice(self.pausedTimingLastIndex, self.pauseTimings.length);
                    for(let i=0; i<sliced.length; i++) {
                        let pausedTiming = sliced[i];
                        let startOffsetSegment = self.audioContext.currentTime - self.startTime
                        //console.log('startOffsetSegment:', startOffsetSegment, '+self.startOffset:', self.startOffset, '>', pausedTiming);
                        if(startOffsetSegment + self.startOffset > pausedTiming) {
                            // console.log('startOffsetSegment', startOffsetSegment, ' + ', self.startOffset, 'self.startOffset >', pausedTiming, 'pausedTiming');
                            isProcessingInterval = true;
                            self.pausedTimingLastIndex +=1;
                            self.pauseAudio(startOffsetSegment);
                            self.playerPausedCallback(self.pausedTimingLastIndex-1, startOffsetSegment + self.startOffset, pausedTiming);//actual paused timing, planned paused timing?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                            if (self.checkIfAudioVideoInSync()) {
                                self.playAudio(self.audioBuffer);
                                self.playerResumedCallback(self.pausedTimingLastIndex-1, startOffsetSegment + self.startOffset, pausedTiming)
                                isProcessingInterval = false;
                            }
                            break;
                        }
                    }
                }, 500);//every 500 milliseconds
            }

            playAudio() {
                if (this.paused) {
                    this.startTime = this.audioContext.currentTime;
                    this.source = this.audioContext.createBufferSource();
                    this.source.buffer = this.audioBuffer;
                    this.source.connect(this.audioContext.destination);
                    this.source.start(0, this.startOffset);
                    this.paused = false;
                    console.log('played audio')
                    //if (!this.alreadyInitWatcher) {
                    //    this.alreadyInitWatcher = true;
                    //    this.initTimingReachedWatcher()
                    //    console.log('initTimingReachedWatcher')
                    //}
                    this.initTimingReachedWatcher()
                }
            }

            pauseAudio(pausedOffset) {
                if (!this.paused) {
                    this.source.stop();
                    //this.startOffset += this.audioContext.currentTime - this.startTime;
                    this.startOffset += pausedOffset
                    console.log('paused:', this.startOffset);
                    this.paused = true;
                    console.log('paused audio')
                }
            }
        }
        //
        return new WavPlayer(audioBuffer, pauseTimings, playerPausedCallback, playerResumedCallback, readyCallback, checkIfAudioVideoInSync)
    }
    //[end] animeAudio

    createLatexMeshes(listOfLatexStrs, callback) {
        const lmc = new LatexMeshCreator(this.scene, this.renderer, this.camera, listOfLatexStrs);
        lmc.getMeshes(callback);
        // return lmc.generatedMeshes;
    }



    //wiring and network information and methods

    createComponent({componentName, position={x:0, y:0, z:0}, rotation={x:0, y:0, z:0}, additionalInfo={}}) {
        let component;
        // console.log(componentName);
        switch(componentName) {
            case 'resistor':
                component = new ComponentResistor(position, rotation);
                break;
            case 'battery':
                component = new ComponentBattery(position, rotation);
                break;
            case 'acSignalGenerator':
                component = new ComponentACSignalGenerator(position, rotation);
                break;
            case 'diode':
                component = new ComponentDiode(position, rotation);
                break;
            case 'capacitor':
                component = new ComponentCapacitor(position, rotation);
                break;
            case 'inductor':
                component = new ComponentInductor(position, rotation);
                break;
            case 'transistor':
                component = new ComponentTransistor(position, rotation);
                break;
            case 'oscillator':
                component = new ComponentOscillator(position, rotation);
                break;
            case 'wire':
                component = new Wire(Object.assign({}, additionalInfo, position));//merge the additionalInfo and position together TODO
                break;
            default:
                throw new Error();
        }
        this.meshUUID__mesh[component.uuid] = component;
        return component
    }

    wire(component0, component1, wireRadius, solderableLeadIdx0=null, solderableLeadIdx1=null, hamming3Idx='214') {

        // const wireBetween = new Wire({
        //     'component0':component0, 
        //     'component1':component1, 
        //     'radius':wireRadius, 
        //     'solderableLeadIdx0':solderableLeadIdx0, 
        //     'solderableLeadIdx1':solderableLeadIdx1,
        //     'hamming3Idx':hamming3Idx
        // });//AWG18
        const wireBetween = this.createComponent(
            {componentName:'wire', position:{}, additionalInfo:{
            'component0':component0, 
            'component1':component1, 
            'radius':wireRadius, 
            'solderableLeadIdx0':solderableLeadIdx0, 
            'solderableLeadIdx1':solderableLeadIdx1,
            'hamming3Idx':hamming3Idx
            }})
        if (solderableLeadIdx0 === null) {
            solderableLeadIdx0 = wireBetween.solderableLeadIdx0
        }
        if (solderableLeadIdx1 === null) {
            solderableLeadIdx1 = wireBetween.solderableLeadIdx1
        }
        this.enter(wireBetween.uuid);// this.scene.add(wireBetween); this.render();


        this.wiring.push([component0.uuid, wireBetween.uuid]);
        this.wiring.push([component1.uuid, wireBetween.uuid]);
        this.uuid__type[component0.uuid] = component0.type;
        this.uuid__type[component1.uuid] = component1.type;
        this.uuid__type[wireBetween.uuid] = wireBetween.type;
        this.uuid__positiveLeadsDirections[component0.uuid] = component0.positiveLeadsDirections;
        this.uuid__positiveLeadsDirections[component1.uuid] = component1.positiveLeadsDirections;
        this.uuid__positiveLeadsDirections[wireBetween.uuid] = wireBetween.positiveLeadsDirections;
        //edgeUUID, is undirected, so need both sides, solderableLeadIdx is directed, so only one side
        this.edgeUUID__solderableIndices[[component0.uuid, wireBetween.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        this.edgeUUID__solderableIndices[[wireBetween.uuid, component0.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        this.edgeUUID__solderableIndices[[component1.uuid, wireBetween.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        this.edgeUUID__solderableIndices[[wireBetween.uuid, component1.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        // also add the connection without wire for some equationFinders ignore wire.... TODO maybe a seperate dictionary to prevent confusion?
        
        this.edgeUUID__solderableIndices[[component0.uuid, component1.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        this.edgeUUID__solderableIndices[[component1.uuid, component0.uuid]] = [solderableLeadIdx0, solderableLeadIdx1];
        return wireBetween
    }

    getNetworkGraph() {
        //simplify uuid 
        this.uuid__id = {}; this.id__uuid = {}; this.id__type = {}; this.id__positiveLeadsDirections = {};
        const uuid__typeEntries = Object.entries(this.uuid__type);let uuid; let type;
        // console.log(uuid__typeEntries);
        for (let i=0; i<uuid__typeEntries.length; i++) {
            [uuid, type] = uuid__typeEntries[i];
            // console.log(uuid, type)
            this.uuid__id[uuid] = i; this.id__uuid[i] = uuid; this.id__type[i] = this.uuid__type[uuid];
            this.id__positiveLeadsDirections[i] = this.uuid__positiveLeadsDirections[uuid];
        }
        // console.log('this.edgeUUID__solderableIndices', this.edgeUUID__solderableIndices);
        const edgeUUID__solderableIndicesEntries = Object.entries(this.edgeUUID__solderableIndices); let uuidDelimitedByComma; let component0_uuid; let component1_uuid; let solderableLeadIdx0; let solderableLeadIdx1;
        // console.log('edgeUUID__solderableIndicesEntries', edgeUUID__solderableIndicesEntries)
        for (let i=0; i<edgeUUID__solderableIndicesEntries.length; i++) {
            [uuidDelimitedByComma, [solderableLeadIdx0, solderableLeadIdx1]] = edgeUUID__solderableIndicesEntries[i];
            [component0_uuid, component1_uuid] = uuidDelimitedByComma.split(',');
            // console.log('uuidDelimitedByComma', uuidDelimitedByComma, 'solderableLeadIdx0', solderableLeadIdx0, 'solderableLeadIdx1', solderableLeadIdx1);
            this.edge__solderableIndices[this.uuid__id[component0_uuid]+","+this.uuid__id[component1_uuid]] = [solderableLeadIdx0, solderableLeadIdx1]
        }
        // console.log('this.edge__solderableIndices', this.edge__solderableIndices);

        // console.log(this.uuid__id); console.log(this.id__uuid);
        let networkGraph = {}; let idNetworkGraph = {}; let id__type = {};
        // let component0_uuid; let component1_uuid; 
        // let component0_solderableIdx;//component1 is the wire
        for (let i=0; i<this.wiring.length; i++) {
            // [component0_uuid, component1_uuid, component0_solderableIdx] = this.wiring[i];
            [component0_uuid, component1_uuid] = this.wiring[i];
            //
            let existingNeighbours = networkGraph[this.uuid__id[component0_uuid]];
            if (existingNeighbours===undefined) {
                existingNeighbours = [];
            }
            if (existingNeighbours.indexOf(this.uuid__id[component1_uuid]) == -1 ) {
                existingNeighbours.push(this.uuid__id[component1_uuid]);
            }
            networkGraph[this.uuid__id[component0_uuid]] = existingNeighbours;
            //
            //
            existingNeighbours = networkGraph[this.uuid__id[component1_uuid]];
            if (existingNeighbours===undefined) {
                existingNeighbours = [];
            }
            if (existingNeighbours.indexOf(this.uuid__id[component0_uuid]) == -1) {
                existingNeighbours.push(this.uuid__id[component0_uuid]);
            }
            networkGraph[this.uuid__id[component1_uuid]] = existingNeighbours;
            //
        }
        this.networkGraph = networkGraph;
        // console.log('id__uuid: ');console.log(this.id__uuid);
        return networkGraph;
    }
}

export {Circuit};