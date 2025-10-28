
// import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js';
import {Animation} from '../custom/Animation.js';
import {Circuit} from './circuit.js';
import {Wire} from '../meshes/Wire.js';
import {CircuitAnime} from '../circuitAnime/basic.js';

class DCTwoResistorSeries extends Circuit {

    /**
     * 
     * **/
    constructor(scene, camera, renderer, audioContext, controls, meshes) {
        super(scene, camera, renderer, audioContext, controls, meshes);
        this.circuitName = 'dcTwoResistorSeries'
        //This is just copy and paste from dc_twoResistor_parallel, not updated yet<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        this.language_introduction_findEquations = {//This will be read out at the beginning of the animation_findEquations
            'en-US':'This is a circuit with two resistors connected in series, lets find all the equations related to the components of this circuit',
            'zh-CN':'我们求，此二电阻器串联电路内，所有方程式。',
            'ja-JP':'こちらは、並列に接続されている抵抗が二つである。その直列回路の素子においての公式を、全て見つけましょう',
            'de-DE':'Der folgende Stromkreis ist eine ReihenSchaltung. Versuchen wir jetzt, alle Gleichungen der Bauelemente dieses Stromkreises aufzuschreiben',
            'fr-FR':'Nous avons deux résistances en série et nous allons trouver toutes les équations relatives à ses composants.',
            'ru-RU':'У нас есть два последовательно соединенных резистора, и нам нужно найти все уравнения, связанные с их компонентами.'
        }

        this.language_conclusion_findEquations = {//This will be read out at the end of the animation_findEquations
            'en-US':'We have found all the equations relating to the two resistors and their series connectivity.',
            'zh-CN':'现阶段，我们以求获所有相关的方程式。',
            'ja-JP':'今まで、その直列回路の素子においての公式を、求めました。',
            'de-DE':'Wir haben alle Gleichungen der Bauelemente dieses Stromkreises gefunden,',
            'fr-FR':'Nous avons trouvé toutes les équations relatives à ses composants.',
            'ru-RU':'Мы нашли все уравнения, касающиеся его компонентов.'
        }

        this.language_introduction_solvingSteps = {//This will be read out at the beginning of the animation_solvingSteps
            'en-US':'Lets try to find the resistance of the battery in terms of the two resistors!',
            'zh-CN':'然后，我们利用之前取获的方程式，推出总电阻。',
            'ja-JP':'それから、求めました公式を使って、その回路は、合成抵抗が、求めましょう！',
            'de-DE':'Damit können wir den Gesamtwiderstand dieses Stromkreises berechnen.',
            'fr-FR':'Calculons la résistance équivalente aux réseaux ci-dessous.',
            'ru-RU':'Рассчитаем эквивалентное сопротивление сетей ниже.'
        }

        this.language_conclusion_solvingSteps = {//This will be read out at the end of the animation_solvingSteps
            'en-US':'And thats it! However, there are many redundant steps, can you find a more elegant solution? Leave your solution in the comments below!',
            'zh-CN':'可是，之前的解题步骤有一点繁琐，您能找到更简易的解题步骤吗？请在讨论区留下您的雅论。',
            'ja-JP':'通りですけど、無駄な手順がいっぱいあります。表した手順より、きれいな解き方を求めることができますか？ぜひ、解き方と考えが、コメント欄に、書いて下さい。',
            'de-DE':'Und so ist es! Aber es gibt viele überflüssige Rechnengen, und das motiviert uns, nach einer eleganten Antwort zu suchen. Schreib uns deine elegante Antworte in die Commentare!',
            'fr-FR':"C'est exact, mais il y a beaucoup d'étapes inutiles. Pouvez-vous trouver une solution plus élégante que celles que j'ai présentées ? N'hésitez pas à partager votre solution et vos réflexions dans les commentaires.",
            'ru-RU':'Это верно, но есть много лишних шагов. Можете ли вы найти более элегантное решение, чем те, что я предложил? Не стесняйтесь делиться своими решениями и мыслями в комментариях.'
        }

        this.audioLanguage = 'zh-CN';

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
        const dependentUUID = battery0.uuid;
        const list_independentUUID = [resistor0.uuid, resistor1.uuid];
        const dependentVarType = 'resistance';
        const list_independentVarType = ['resistance', 'resistance'];


        function variableSelect(self) {
            function onlySubString(s, subString){return s.includes(subString)}
            const list_equationLatexStr = []; let dependentVarStr; const list_independentVarStr = [];
            self.list_equationNetworkInfoDict.forEach(equationNetworkInfoDict => {
                list_equationLatexStr.push(equationNetworkInfoDict['equation']);
                Object.entries(equationNetworkInfoDict['variableInfos']).forEach(([nodeId, list_variableStr]) => {
                    //capture the dependentVarStr: resistance of resistor0
                    if(parseInt(nodeId) == self.uuid__id[battery0.uuid]) {//we only want to set dependentVarStr once
                        const varString = list_variableStr.filter(function(s){return onlySubString(s, 'R_{')})[0];//TODO some hard coding here, to get rid of it, server need to have an endpoint to get variable_name given the description
                        console.log('varString: ', varString, 'dependentVarStr')
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
            console.log('list_equationLatexStr', list_equationLatexStr);
            console.log('dependentVarStr', dependentVarStr);
            console.log('list_independentVarStr', list_independentVarStr);
            return [list_equationLatexStr, dependentVarStr, list_independentVarStr]
        }
        const simplify = true; const record = true; const ticketing = true; const recordSubtitles = true;
        (new CircuitAnime('dc_twoResistor_series', this, variableSelect, ticketing, simplify, record, recordSubtitles)).play();


        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }
    
}

export {DCTwoResistorSeries};