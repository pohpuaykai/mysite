
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
        const simplify = true; const record = true;
        (new CircuitAnime('dc_twoResistor_parallel', this, variableSelect, simplify, record)).play();

        return {
            'scene':this.scene,
            'camera':this.camera,
            'renderer':this.renderer,
        }

    }

    
}

export {DCTwoResistorParallel};