
import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {Circuit} from './circuit.js';
import {Wire} from '../meshes/Wire.js';
// import {CircuitAnime} from '../circuitAnime/basic.js';
import {CircuitAnime} from '../circuitAnime/basicNoAudio.js';

class DCTwoDiodeSeries extends Circuit {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, audioContext, controls, meshes) {
        super(scene, camera, renderer, audioContext, controls, meshes);
        this.circuitName = 'dcTwoDiodeSeries'//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

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

        const battery0 = this.createComponent({componentName:'battery', position:{x:0, y:0, z:10}});
        this.enter(battery0.uuid);
        battery0.setAllTouchingBoxVisibility(false);//this.render();

        const diode0 = this.createComponent({componentName:'diode', position:{x:0, y:0, z:-20}});
        this.enter(diode0.uuid);
        diode0.setAllTouchingBoxVisibility(false);//this.render();

        const diode1 = this.createComponent({componentName:'diode', position:{x:15, y:0, z:-20}});
        this.enter(diode1.uuid);
        diode1.setAllTouchingBoxVisibility(false);//this.render();

        const wireBetween01 = this.wire(diode0, battery0, 0.644/2, 0, 0, '241');
        wireBetween01.setAllTouchingBoxVisibility(false);

        const wireBetween10 = this.wire(diode0, diode1, 0.644/2, 1, 0);
        wireBetween10.setAllTouchingBoxVisibility(false);

        const wireBetween11 = this.wire(battery0, diode1, 0.644/2, 1, 1, '142');
        wireBetween11.setAllTouchingBoxVisibility(false);


        // //get Equations and solving steps:
        const dependentUUID = battery0.uuid;
        const list_independentUUID = [diode0.uuid, diode1.uuid];
        const dependentVarType = 'current';
        const list_independentVarType = ['current', 'current'];

        function variableSelect(self) {
            function onlySubString(s, subString){return s.includes(subString)}
            const list_equationLatexStr = []; let dependentVarStr=undefined; const list_independentVarStr = [];
            self.list_equationNetworkInfoDict.forEach(equationNetworkInfoDict => {
                list_equationLatexStr.push(equationNetworkInfoDict['equation']);
                Object.entries(equationNetworkInfoDict['variableInfos']).forEach(([nodeId, list_variableStr]) => {
                    //capture the dependentVarStr: resistance of resistor0
                    if(parseInt(nodeId) == self.uuid__id[battery0.uuid] && dependentVarStr==undefined) {//we only want to set dependentVarStr once
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'I_{')})[0];//TODO some hard coding here, to get rid of it, server need to have an endpoint to get variable_name given the description
                        // console.log('varString: ', varString, 'dependentVarStr')
                        // if (varString !== undefined) {
                            dependentVarStr = varString;
                        // }
                    }
                    //capture the first element of list_independentVarStr
                    if(parseInt(nodeId) == self.uuid__id[diode0.uuid]) {
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'I_{D')})[0];
                        if (varString !== undefined && !(list_independentVarStr.includes(varString))) {
                            list_independentVarStr.push(varString)
                        }
                        // list_independentVarStr.push(); //TODO some hard coding here, to get rid of it, server need to have an endpoint to get variable_name given the description
                    }
                    //capture the first element of list_independentVarStr
                    if(parseInt(nodeId) == self.uuid__id[diode1.uuid]) {
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'I_{D')})[0];
                        if (varString !== undefined && !(list_independentVarStr.includes(varString))) {
                            list_independentVarStr.push(varString)
                        }
                    }
                });
            });
            return [list_equationLatexStr, dependentVarStr, list_independentVarStr]
        }

        const simplify = true; const record = false; const ticketing = true; const recordSubtitles = true;
        (new CircuitAnime(this.circuitName, this, variableSelect, ticketing, simplify, record, recordSubtitles)).play();

        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }

    
}

export {DCTwoDiodeSeries};