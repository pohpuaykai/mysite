// import {asyncCreateLatexMesh} from '../custom/LatexMeshCreater.js';
import {LatexMeshCreator} from '../custom/LatexMeshCreater.js'
import {Piece} from './piece.js';

class Circuit extends Piece{
    
    constructor(scene, camera, renderer, meshes) {
        super(scene, camera, renderer, meshes);

    }

    getAllEquationsAndASolvingStep(callback) {//TODO allow the child_circuit to choose what dependentVar, and independentVars<<<<<<<<<<<<<<
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const xhr = new XMLHttpRequest();
        const self = this;
        xhr.onreadystatechange  = function(){

            if (this.readyState == 4 && this.status == 200) {
              const responseDict = JSON.parse(this.responseText);
              const listOfEquations_latexStrs = responseDict['equations'];
              const solvingSteps = responseDict['solvingSteps'];
              self.listOfEquations_latexStrs = listOfEquations_latexStrs;
              self.solvingSteps = solvingSteps;
              // console.log(listOfEquations_latexStrs);
              // console.log('solvingSteps');
              // console.log(solvingSteps);
              callback(listOfEquations_latexStrs, solvingSteps);

              // asyncCreateLatexMesh(scene, renderer, camera, listOfEquations_latexStrs);
            }
        }
        // xhr.onerror = function(){}
        xhr.open('POST', findEquationsAndSolve_url);
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        // xhr.setRequestHeader('Content-Type', 'application/json');
        // circuit.getNetworkGraph();
        self.getNetworkGraph();
        xhr.send(JSON.stringify({
            // 'networkGraph':JSON.stringify(circuit.getNetworkGraph()).replaceAll('"', ''), //because keys gets converted to string internally in javscript, and we want everything to be in integers
            'networkGraph':self.networkGraph, //circuit.networkGraph,
            // 'networkGraphNoWires': circuit.networkGraphNoWires,
            'id__type':self.id__type,//circuit.id__type,
            'id__positiveLeadsDirections':self.id__positiveLeadsDirections,//circuit.id__positiveLeadsDirections,
            'edge__solderableIndices':self.edge__solderableIndices//circuit.edge__solderableIndices
        }));
    }

    createLatexMeshes(listOfLatexStrs, callback) {
        const lmc = new LatexMeshCreator(this.scene, this.renderer, this.camera, listOfLatexStrs);
        lmc.getMeshes(callback);
        // return lmc.generatedMeshes;
    }
}

export {Circuit};