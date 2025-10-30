
import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {Circuit} from './circuit.js';
import {Wire} from '../meshes/Wire.js';
import {CircuitAnime} from '../circuitAnime/basic.js';

class ACTwoCapacitorSeries extends Circuit {

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
        const sigGen = this.createComponent({componentName:'acSignalGenerator', position:{x:0, y:10, z:100}});
        this.enter(sigGen.uuid);
        sigGen.setAllTouchingBoxVisibility(false);//this.render();

        const capacitor0 = this.createComponent({componentName:'capacitor', position:{x:-15, y:0, z:-20}});
        this.enter(capacitor0.uuid);
        capacitor0.setAllTouchingBoxVisibility(false);//this.render();

        const capacitor1 = this.createComponent({componentName:'capacitor', position:{x:15, y:0, z:-20}});
        this.enter(capacitor1.uuid);
        capacitor1.setAllTouchingBoxVisibility(false);//this.render();

        const wireBetween01 = this.wire(capacitor0, sigGen, 0.644/2, 0, 0, '124');
        wireBetween01.setAllTouchingBoxVisibility(false);

        const wireBetween10 = this.wire(capacitor0, capacitor1, 0.644/2, 1, 0);
        wireBetween10.setAllTouchingBoxVisibility(false);

        const wireBetween11 = this.wire(sigGen, capacitor1, 0.644/2, 1, 1, '142');
        wireBetween11.setAllTouchingBoxVisibility(false);


        // //get Equations and solving steps:
        // const dependentUUID = battery0.uuid;
        // const list_independentUUID = [resistor0.uuid, resistor1.uuid];
        // const dependentVarType = 'resistance';
        // const list_independentVarType = ['resistance', 'resistance'];

        // function variableSelect(self) {
        //     function onlySubString(s, subString){return s.includes(subString)}
        //     const list_equationLatexStr = []; let dependentVarStr=undefined; const list_independentVarStr = [];
        //     self.list_equationNetworkInfoDict.forEach(equationNetworkInfoDict => {
        //         list_equationLatexStr.push(equationNetworkInfoDict['equation']);
        //         Object.entries(equationNetworkInfoDict['variableInfos']).forEach(([nodeId, list_variableStr]) => {
        //             //capture the dependentVarStr: resistance of resistor0
        //             if(parseInt(nodeId) == self.uuid__id[battery0.uuid]) {//we only want to set dependentVarStr once
        //                 const varString = list_variableStr.filter(function(s){return onlySubString(s, 'R_{')})[0];//TODO some hard coding here, to get rid of it, server need to have an endpoint to get variable_name given the description
        //                 // console.log('varString: ', varString, 'dependentVarStr')
        //                 // if (varString !== undefined) {
        //                     dependentVarStr = varString;
        //                 // }
        //             }
        //             //capture the first element of list_independentVarStr
        //             if(parseInt(nodeId) == self.uuid__id[resistor0.uuid]) {
        //                 const varString = list_variableStr.filter(function(s){return onlySubString(s, 'R_{R')})[0];
        //                 if (varString !== undefined && !(list_independentVarStr.includes(varString))) {
        //                     list_independentVarStr.push(varString)
        //                 }
        //                 // list_independentVarStr.push(); //TODO some hard coding here, to get rid of it, server need to have an endpoint to get variable_name given the description
        //             }
        //             //capture the first element of list_independentVarStr
        //             if(parseInt(nodeId) == self.uuid__id[resistor1.uuid]) {
        //                 const varString = list_variableStr.filter(function(s){return onlySubString(s, 'R_{R')})[0];
        //                 if (varString !== undefined && !(list_independentVarStr.includes(varString))) {
        //                     list_independentVarStr.push(varString)
        //                 }
        //             }
        //         });
        //     });
        //     return [list_equationLatexStr, dependentVarStr, list_independentVarStr]
        // }

        // const simplify = true; const record = true; const ticketing = true; const recordSubtitles = true;
        // (new CircuitAnime(this.circuitName, this, variableSelect, ticketing, simplify, record, recordSubtitles)).play();

        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }

    
}

export {ACTwoCapacitorSeries};