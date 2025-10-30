
import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {Circuit} from './circuit.js';
import {Wire} from '../meshes/Wire.js';
// import {CircuitAnime} from '../circuitAnime/basic.js';
import {CircuitAnime} from '../circuitAnime/basicNoAudio.js';

class ACTwoCapacitorParallel extends Circuit {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, audioContext, controls, meshes) {
        super(scene, camera, renderer, audioContext, controls, meshes);
        this.circuitName = ''//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        this.language_introduction_findEquations = {//This will be read out at the beginning of the animation_findEquations
            'en-US':'',
            'zh-CN':'',
            'ja-JP':'',
            'de-DE':'',
            'fr-FR':'',
            'ru-RU':''
        }

        this.language_conclusion_findEquations = {//This will be read out at the end of the animation_findEquations
            'en-US':'',
            'zh-CN':'',
            'ja-JP':'',
            'de-DE':'',
            'fr-FR':'',
            'ru-RU':''
        }

        this.language_introduction_solvingSteps = {//This will be read out at the beginning of the animation_solvingSteps
            'en-US':'',
            'zh-CN':'',
            'ja-JP':'',
            'de-DE':'',
            'fr-FR':'',
            'ru-RU':''
        }

        this.language_conclusion_solvingSteps = {//This will be read out at the end of the animation_solvingSteps
            'en-US':'',
            'zh-CN':'',
            'ja-JP':'',
            'de-DE':'',
            'fr-FR':"",
            'ru-RU':''
        }

        this.audioLanguage = 'ja-JP';
    }

    act() {
        this.camera.position.set( 0, 30, -120 );

        const sigGen = this.createComponent({componentName:'acSignalGenerator', position:{x:0, y:5, z:100}});
        this.enter(sigGen.uuid);
        sigGen.setAllTouchingBoxVisibility(false);//this.render();

        const capacitor0 = this.createComponent({componentName:'capacitor', position:{x:0, y:20, z:-15}});
        this.enter(capacitor0.uuid);
        capacitor0.setAllTouchingBoxVisibility(false);//this.render();

        const capacitor1 = this.createComponent({componentName:'capacitor', position:{x:0, y:-20, z:-25}, rotation:{x:Math.PI, y:0, z:0}});
        this.enter(capacitor1.uuid);
        capacitor1.setAllTouchingBoxVisibility(false);//this.render();

        const c = this.createComponent({componentName:'wire', position:{'x': 15, 'y': 0, 'z':-20}, additionalInfo:{'radius': 0.644/2}})
        this.enter(c.uuid);
        // this.scene.add(c);
        c.setAllTouchingBoxVisibility(false);
        // console.log('c', c);

        const d = this.createComponent({componentName:'wire', position:{'x': -15, 'y': 0, 'z':-20}, additionalInfo:{'radius': 0.644/2}})
        this.enter(d.uuid);
        // this.scene.add(d);
        d.setAllTouchingBoxVisibility(false);
        // console.log('d', d);


        //network|connection information
        const wire_c_capacitor0 = this.wire(capacitor0, c, 0.644/2, 1);
        wire_c_capacitor0.setAllTouchingBoxVisibility(false);
        const wire_c_capacitor1 = this.wire(capacitor1, c, 0.644/2, 1);
        wire_c_capacitor1.setAllTouchingBoxVisibility(false);
        const wire_d_capacitor0 = this.wire(capacitor0, d, 0.644/2, 0);
        wire_d_capacitor0.setAllTouchingBoxVisibility(false);
        const wire_d_capacitor1 = this.wire(capacitor1, d, 0.644/2, 0);
        wire_d_capacitor1.setAllTouchingBoxVisibility(false);
        const wireBetween11 = this.wire(sigGen, d, 0.644/2, 0);
        wireBetween11.setAllTouchingBoxVisibility(false);
        const wireBetween00 = this.wire(sigGen, c, 0.644/2, 1);
        wireBetween00.setAllTouchingBoxVisibility(false);


        //get Equations and solving steps:
        const dependentUUID = battery0.uuid;
        const list_independentUUID = [resistor0.uuid, resistor1.uuid];
        const dependentVarType = 'capacitance';
        const list_independentVarType = ['capacitance', 'capacitance'];

        function variableSelect(self) {
            function onlySubString(s, subString){return s.includes(subString)}
            const list_equationLatexStr = []; let dependentVarStr=undefined; const list_independentVarStr = [];
            self.list_equationNetworkInfoDict.forEach(equationNetworkInfoDict => {
                list_equationLatexStr.push(equationNetworkInfoDict['equation']);
                Object.entries(equationNetworkInfoDict['variableInfos']).forEach(([nodeId, list_variableStr]) => {
                    //capture the dependentVarStr: resistance of resistor0
                    if(parseInt(nodeId) == self.uuid__id[battery0.uuid]) {//we only want to set dependentVarStr once
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'C_{')})[0];//TODO some hard coding here, to get rid of it, server need to have an endpoint to get variable_name given the description
                        // console.log('varString: ', varString, 'dependentVarStr')
                        // if (varString !== undefined) {
                            dependentVarStr = varString;
                        // }
                    }
                    //capture the first element of list_independentVarStr
                    if(parseInt(nodeId) == self.uuid__id[resistor0.uuid]) {
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'C_{C')})[0];
                        if (varString !== undefined && !(list_independentVarStr.includes(varString))) {
                            list_independentVarStr.push(varString)
                        }
                        // list_independentVarStr.push(); //TODO some hard coding here, to get rid of it, server need to have an endpoint to get variable_name given the description
                    }
                    //capture the first element of list_independentVarStr
                    if(parseInt(nodeId) == self.uuid__id[resistor1.uuid]) {
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'C_{C')})[0];
                        if (varString !== undefined && !(list_independentVarStr.includes(varString))) {
                            list_independentVarStr.push(varString)
                        }
                    }
                });
            });
            return [list_equationLatexStr, dependentVarStr, list_independentVarStr]
        }

        const simplify = true; const record = true; const ticketing = true; const recordSubtitles = true;
        (new CircuitAnime(this.circuitName, this, variableSelect, ticketing, simplify, record, recordSubtitles)).play();

        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }

    
}

export {ACTwoCapacitorParallel};