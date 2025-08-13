import {Wire} from '../meshes/Wire.js';
import {Piece} from './piece.js';
import {Animation} from '../custom/Animation.js';

//all the components
import {ComponentResistor} from '../meshes/ComponentResistor.js';
import {ComponentBattery} from '../meshes/ComponentBattery.js';

class Circuit extends Piece{
    
    constructor(scene, camera, renderer, meshes) {
        super(scene, camera, renderer, meshes);

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
        let componenttypeSVGFilepath_ajax = new XMLHttpRequest(); this.componentType__boundingBox = {}; const self = this;
        componenttypeSVGFilepath_ajax.addEventListener("load", function() {
            const componenttype__svgfilepath___str = componenttypeSVGFilepath_ajax.responseText;
            const COMPONENTTYPE__SVGFILEPATH___entries = Object.entries(JSON.parse(componenttype__svgfilepath___str));
            // console.log(COMPONENTTYPE__SVGFILEPATH___entries);
            let componentType; let svgFilepath;let absolutePath;
            for (let i=0; i<COMPONENTTYPE__SVGFILEPATH___entries.length; i++) {
                // if (COMPONENTTYPE__SVGFILEPATH___entries[i] != undefined) { //https://developer.mozilla.org/en-US/docs/Web/API/SVGGraphicsElement/getBBox
                    [componentType, svgFilepath] = COMPONENTTYPE__SVGFILEPATH___entries[i];
                    absolutePath = '/public/static/'+svgFilepath;
                    let ajax = new XMLHttpRequest();
                    ajax.addEventListener("load", function(componentType) {
                        return function () {
                            // console.log(ajax.responseText);
                            let svgString = ajax.responseText;
                            let svgBBox = getBBoxFromSVGString(svgString);
                            // console.log(componentType, svgBBox);
                            // self.componentType__boundingBox[componentType] = svgBBox;
                            self.componentType__boundingBox[componentType] = {'width':svgBBox.width, 'height':svgBBox.height};
                            // console.log('componentType__boundingBox', JSON.stringify(self.componentType__boundingBox));
                        }
                    }(componentType));
                    // console.log(componentType, absolutePath);
                    ajax.open("GET", absolutePath);
                    ajax.send();
            }
        });
        componenttypeSVGFilepath_ajax.open("GET", "/public/static/settings/ComponentType__SVGFilepath.json");//hide this link?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        componenttypeSVGFilepath_ajax.send();
    }


    animate_findEquations(solvingCallback, readyCallback) {//TODO meshToAnimation, should take a 
        const self = this;
        function CALLBACK__findEquations(list_equationNetworkInfoDict){
            // console.log("equationStr__variables"); console.log(equationStr__variables)
            // console.log("componentId__list_variables"); console.log(componentId__list_variables)
            self.list_equationNetworkInfoDict = list_equationNetworkInfoDict;

            solvingCallback(list_equationNetworkInfoDict);
            // const findEquationAnimation = findEquationAnimation___functionGen(list_equationNetworkInfoDict);
            // self.scheduleAnimation(findEquationAnimation, 0);//0 is a priority, lower number gets animated first.
            let latexStrs = [];
            for(let i=0; i<list_equationNetworkInfoDict.length; i++) {
                latexStrs.push([list_equationNetworkInfoDict[i]['equation'], list_equationNetworkInfoDict[i]['variables']]);
            }
            console.log('list_equationNetworkInfoDict', list_equationNetworkInfoDict)
            latexStrs = [...new Set(latexStrs)];
            self.makeLatexMesh(latexStrs, readyCallback); // also give latexStr to variables







            // let listOfEquations_latexStrs = Object.keys(equationStr__variables);
            // const YSize = 30;
            // const startYCoordinate = -listOfEquations_latexStrs.length* YSize/2;
            // self.animationAggregator.resetAggregatedAnimations();
            // function CALLBACK__createLatexMeshes(meshIdx, mesh) {
            //     mesh.position.set(-64, startYCoordinate+YSize*meshIdx, 100);// here we are fixing the position....<<<<<<<<<<<<<<<
            //     self.scene.add(mesh);
            //     self.animationAggregator.appendAction(meshToAnimation(mesh));
            //     self.render();
            //     self.animationAggregator.restartAnimation();
            // }
            // self.createLatexMeshes(listOfEquations_latexStrs, CALLBACK__createLatexMeshes);
        }

        this.findEquations(CALLBACK__findEquations);
        
    }

    findEquations(callback) {//TODO allow the child_circuit to choose what dependentVar, and independentVars<<<<<<<<<<<<<<
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();
        const self = this;
        xhr.onreadystatechange  = function(){

            if (this.readyState == 4 && this.status == 200) {
              const list_equationNetworkInfoDict = JSON.parse(this.responseText);
              /**
               * responseDict is a list that contains many:
               *     {
               *        'equation':,#inLatexFormat
               *        'equationFinderDisplayName':,#like "Ohms Law", "Kirchoff Voltage Law"
               *        'list_list_networkNodeIds':,#like for Kirchoff Voltage Law, a list of directedCycles, for Ohms Law, list_list of nodeIds?
               *        'variableInfos':[
               *            {
               *                'variable':,
               *                'networkNodeIds':, # for totals, take a list of networkIds
               *            }
               *        ]
               *    }
               * 
               * **/



              // const equationStr__variables = responseDict['equationStr__variables']
              // self.equationStr__variables = equationStr__variables;
              // const componentId__list_variables = responseDict['componentId__list_variables']
              // self.componentId__list_variables = componentId__list_variables
              // console.log('equationStr__variables', self.equationStr__variables);
              // console.log('componentId__list_variables', self.componentId__list_variables);
              callback(list_equationNetworkInfoDict);
            }
        }
        // xhr.onerror = function(){}
        xhr.open('POST', findEquations_url);
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        // xhr.setRequestHeader('Content-Type', 'application/json');
        self.getNetworkGraph();

        xhr.send(JSON.stringify({
            'networkGraph':self.networkGraph, //circuit.networkGraph,
            'id__type':self.id__type,//circuit.id__type,
            'id__positiveLeadsDirections':self.id__positiveLeadsDirections,//circuit.id__positiveLeadsDirections,
            'edge__solderableIndices':self.edge__solderableIndices,//circuit.edge__solderableIndices
        }));
    }

    animate_solveEquations(meshToAnimation, list_equationStr, dependentVarStr, list_independentVarStr) {
        //
    // list_equationStr
    // id__type
    // dependentVarStr
    // list_independentVarStr
        const self = this;
        function CALLBACK__solveEquations(steps) {
            self.animationAggregator.resetAggregatedAnimations();
            const YSize = 30;
            const startYCoordinate = -list_equationStr.length* YSize/2;
            function CALLBACK__createLatexMeshes(meshIdx, mesh) {
                mesh.position.set(128, startYCoordinate+YSize*meshIdx, 100);
                self.scene.add(mesh);
                self.animationAggregator.appendAction(meshToAnimation(mesh));
                self.render();
                self.animationAggregator.restartAnimation();
            }
            console.log('steps:******'); console.log(steps);
            //flatten steps into a list, for now, we just take the broadSteps, KIV the substeps<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            let list_broadLatexVorStr = steps.map(function(broadStep){
                return broadStep['vor']['latex'];
            });
            self.createLatexMeshes(list_broadLatexVorStr, CALLBACK__createLatexMeshes);
        }
        this.solveEquations(CALLBACK__solveEquations, list_equationStr, dependentVarStr, list_independentVarStr)
    }

    solveEquations(callback, list_equationStr, dependentVarStr, list_independentVarStr) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();
        const self = this;
        xhr.onreadystatechange  = function(){

            if (this.readyState == 4 && this.status == 200) {
              const responseDict = JSON.parse(this.responseText);
              const steps = responseDict['steps']
              self.steps = steps;
              callback(steps);

              // asyncCreateLatexMesh(scene, renderer, camera, listOfEquations_latexStrs);
            }
        }
        // xhr.onerror = function(){}
        xhr.open('POST', solveEquations_url);
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        // xhr.setRequestHeader('Content-Type', 'application/json');
        // circuit.getNetworkGraph();
        self.getNetworkGraph();

        xhr.send(JSON.stringify({
            'list_equationStr':list_equationStr,
            'id__type':self.id__type,
            'dependentVarStr':dependentVarStr,
            'list_independentVarStr':list_independentVarStr
        }));

    }

    createLatexMeshes(listOfLatexStrs, callback) {
        const lmc = new LatexMeshCreator(this.scene, this.renderer, this.camera, listOfLatexStrs);
        lmc.getMeshes(callback);
        // return lmc.generatedMeshes;
    }



    //wiring and network information and methods

    createComponent({componentName, position={x:0, y:0, z:0}, additionalInfo={}}) {
        let component;
        console.log(componentName);
        switch(componentName) {
            case 'resistor':
                component = new ComponentResistor(position);
                break;
            case 'battery':
                component = new ComponentBattery(position);
                break;
            case 'wire':

                component = new Wire(Object.assign({}, additionalInfo, position));//merge the additionalInfo and position together
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