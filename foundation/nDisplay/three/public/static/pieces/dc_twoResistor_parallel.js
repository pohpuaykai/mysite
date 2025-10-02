
import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {Circuit} from './circuit.js';
import {Wire} from '../meshes/Wire.js';
import {CircuitAnime} from '../circuitAnime/basic.js';

class DCTwoResistorParallel extends Circuit {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, controls, meshes) {
        super(scene, camera, renderer, controls, meshes);

        this.language_introduction_findEquations = {//This will be read out at the beginning of the animation_findEquations
            'en-US':'This is a circuit with two resistors connected in parallel, lets find all the equations related to the components of this circuit',
            'zh-CN':'我们求，此二电阻器并联电路内，所有方程式。',
            'ja-JP':'こちらは、並列に接続されている抵抗が二つである。その並列回路の素子においての公式を、全て見つけましょう',
            'de-DE':'Die folgende Stromkreise ist in der ParallelSchaltung. Versuch wir jetzt, allen Gleichungen dieser Stromkreise der Bauelemente aufzuschreiben', //check with ChatGPT
            'fr-FR':'',
            'ru-RU':''
        }

        this.language_conclusion_findEquations = {//This will be read out at the end of the animation_findEquations
            'en-US':'We have found all the equations relating to the two resistors and their parallel connectivity.',
            'zh-CN':'现阶段，我们以求获所有相关的方程式。',
            'ja-JP':'今まで、その並列回路の素子においての公式を、求めました。',
            'de-DE':'Wir haben allen Gleichungen dieser Stromkreise der Bauelemente gefunden,', //check with ChatGPT
            'fr-FR':'',
            'ru-RU':''
        }

        this.language_introduction_solvingSteps = {//This will be read out at the beginning of the animation_solvingSteps
            'en-US':'Lets try to find the resistance of the battery in terms of the two resistors!',
            'zh-CN':'然后，我们利用之前取获的方程式，推出总电阻。',
            'ja-JP':'それから、求めました公式を使って、その回路は、合成抵抗が、求めましょう！',
            'de-DE':'damit lassen wir, der Gesamtwiderstand dieser Stromkreise zu berechnen.', //check with ChatGPT
            'fr-FR':'',
            'ru-RU':''
        }

        this.language_conclusion_solvingSteps = {//This will be read out at the end of the animation_solvingSteps
            'en-US':'And thats it! However, there are many redundant steps, can you find a more elegant solution? Leave your solution in the comments below!',
            'zh-CN':'可是，之前的解题步骤有一点繁琐，您能找到更简易的解题步骤吗？请在讨论区留下您的雅论。',
            'ja-JP':'通りですけど、無駄な手順がいっぱいあります。表した手順より、きれいな解き方を求めることができますか？ぜひ、解き方と考えが、コメント欄に、書いて下さい。',
            'de-DE':'Und das ist so! Aber, es gibt viele überflüssig Rechnengen, davor motiviert uns, eine elegante Antworte zu suchen. Schreib uns ihre Antworte in der Commentaire!', //check with ChatGPT
            'fr-FR':'',
            'ru-RU':''
        }

    }

    act() {

        const resistor0 = this.createComponent({componentName:'resistor', position:{x:0, y:-5, z:-20}});
        this.enter(resistor0.uuid); 
        // this.scene.add(resistor0); 
        resistor0.setAllTouchingBoxVisibility(false);//this.render();
        console.log('resistor0'); console.log(resistor0.uuid);

        const battery0 = this.createComponent({componentName:'battery', position:{x:0, y:0, z:10}});
        this.enter(battery0.uuid);
        // this.scene.add(battery0); 
        battery0.setAllTouchingBoxVisibility(false);//this.render();
        console.log('battery0'); console.log(battery0.uuid);

        const resistor1 = this.createComponent({componentName:'resistor', position:{x:0, y:5, z:-20}})
        this.enter(resistor1.uuid)
        // this.scene.add(resistor1); 
        resistor1.setAllTouchingBoxVisibility(false); this.render();
        console.log('resistor1'); console.log(resistor1.uuid);

        const c = this.createComponent({componentName:'wire', position:{'x': 15, 'y': 0, 'z':-20}, additionalInfo:{'radius': 0.644/2}})
        this.enter(c.uuid);
        // this.scene.add(c);
        c.setAllTouchingBoxVisibility(false);
        console.log('c', c);

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
        const dependentUUID = battery0.uuid;
        const list_independentUUID = [resistor0.uuid, resistor1.uuid];
        const dependentVarType = 'resistance';
        const list_independentVarType = ['resistance', 'resistance'];

        function variableSelect(self) {
            function onlySubString(s, subString){return s.includes(subString)}
            const list_equationLatexStr = []; let dependentVarStr=undefined; const list_independentVarStr = [];
            self.list_equationNetworkInfoDict.forEach(equationNetworkInfoDict => {
                list_equationLatexStr.push(equationNetworkInfoDict['equation']);
                Object.entries(equationNetworkInfoDict['variableInfos']).forEach(([nodeId, list_variableStr]) => {
                    //capture the dependentVarStr: resistance of resistor0
                    if(parseInt(nodeId) == self.uuid__id[battery0.uuid]) {//we only want to set dependentVarStr once
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'R_{')})[0];//TODO some hard coding here, to get rid of it, server need to have an endpoint to get variable_name given the description
                        // console.log('varString: ', varString, 'dependentVarStr')
                        // if (varString !== undefined) {
                            dependentVarStr = varString;
                        // }
                    }
                    //capture the first element of list_independentVarStr
                    if(parseInt(nodeId) == self.uuid__id[resistor0.uuid]) {
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'R_{R')})[0];
                        if (varString !== undefined && !(list_independentVarStr.includes(varString))) {
                            list_independentVarStr.push(varString)
                        }
                        // list_independentVarStr.push(); //TODO some hard coding here, to get rid of it, server need to have an endpoint to get variable_name given the description
                    }
                    //capture the first element of list_independentVarStr
                    if(parseInt(nodeId) == self.uuid__id[resistor1.uuid]) {
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'R_{R')})[0];
                        if (varString !== undefined && !(list_independentVarStr.includes(varString))) {
                            list_independentVarStr.push(varString)
                        }
                    }
                });
            });
            console.log('copy this to subtitles: ')
            console.log('list_equationLatexStr', list_equationLatexStr);
            console.log('dependentVarStr', dependentVarStr);
            console.log('list_independentVarStr', list_independentVarStr);
            debugger;
            return [list_equationLatexStr, dependentVarStr, list_independentVarStr]
        }
        const simplify = true; const record = false; const ticketing = true;
        (new CircuitAnime('dc_twoResistor_parallel', this, variableSelect, ticketing, simplify, record)).play();

        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }

    
}

export {DCTwoResistorParallel};