import * as THREE from '../three/three.module.js';
import {SVGLoader} from '../three/SVGLoader.js';
import {Actor} from './Actor.js'

class LatexMeshCreator {

    constructor() {
        const stylizedDecCode__Char = {};
        Object.values(MathJaxCHTML._.output.common.fonts.tex).forEach(d0=> {Object.values(d0).forEach(d1 => {
          Object.entries(d1).forEach(([key, value]) => {
            let nV = null;
            if (value[3]) {
              if (value[3].c) {
                nV = value[3].c
              } else {
                nV = value[3].f
              }
            } else if (value.c) {
              nV = String.fromCodePoint(parseInt(value.c.toString(16), 16));//convert to unicode character
            }
            if (nV != null && nV.length > 0) {
              stylizedDecCode__Char[key] =nV
            }
          })
        })})
        this.stylizedDecCode__Char = stylizedDecCode__Char;
    }


    getMeshes(list_latexStr, equationMeshCallback, textStr__textMeshUUID___existing, requestingAnimationName) {
      const meshUUID__mesh = {};
      const self = this; //self.generatedMeshes = [];
      // console.log("this.stylizedDecCode__Char", this.stylizedDecCode__Char)


      // const YSize = 30;
      // const startYCoordinate = -listOfEquations_latexStrs.length* YSize/2;
      console.log(list_latexStr)
      //need to get variable to UUID<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      for(let i=0; i<list_latexStr.length; i++) {
        let latexStr; let variables;
        [latexStr, variables] = list_latexStr[i];
        if (latexStr in textStr__textMeshUUID___existing) { // if already exist there is not need to recreate it, it will still be available in circuit.js (latexStr)
          textStr__textMeshUUID___existing[latexStr].setRequestingAnimation(requestingAnimationName)
          continue
        }
        // console.log('variables', variables, 'latexStr', latexStr)
        const list_startPosEndPosVariableStr = []
        variables.forEach(variableStr => {
          for(const match of latexStr.matchAll(new RegExp(RegExp.escape(variableStr), "g"))) {
            list_startPosEndPosVariableStr.push([match.index, match.index+variableStr.length, variableStr]);
          }
        });
        list_startPosEndPosVariableStr.sort((tupa, tupb)=>tupb[0]-tupa[0]); //sort in descending order
        // console.log('list_startPosEndPosVariableStr', list_startPosEndPosVariableStr)


        const svgString = self.getCleanSVG(latexStr);
        //
        const blob = new Blob([svgString], {type: "image/svg+xml"});
        const url = URL.createObjectURL(blob);

        const loader = new SVGLoader();
        const variablesPos__list_chaMeshUUID = {}; //TODO remove
        const list_variableInfoDict = []
        let startVariableMatching = false;// if this true, then we are within the variable_capturing range of the latexStr
        loader.load(url, (data) => {
          let currentVariableToMatch = list_startPosEndPosVariableStr.pop();//will take the earliest in the latexStr, because we are poping the end of list_startPosEndPosVariableStr, which is ordered in descending
          let variableMatchLeftOver = currentVariableToMatch[2]; let list_variableLetterMeshesUUID = [];
          const paths = data.paths;
          const group = new Actor();// const group = new THREE.Group();
          group.name = latexStr;
          group.setType('latexStr');
          group.setRequestingAnimation(requestingAnimationName)

          for (const path of paths) {
            const xlinkHref = path.userData.node.id;
            const hexCode = xlinkHref.substring(xlinkHref.lastIndexOf('-')+1, xlinkHref.length);
            const decCode = parseInt(hexCode, 16); let chaStr = null;
            if (xlinkHref.includes('TEX-N-')) { // normal font
              chaStr = String.fromCodePoint(decCode)
            } else { // stylised font
              chaStr = self.stylizedDecCode__Char[decCode]
            }
            const material = new THREE.MeshBasicMaterial({
              color: path.color,
              color:new THREE.Color(1.0, 1.0, 1.0),
              side: THREE.DoubleSide,
              depthWrite: false
            });

            const shapes = path.toShapes(true);
            const letter = new Actor();// const letter = new THREE.Group();
            letter.setType('latexLetter');
            letter.setRequestingAnimation(requestingAnimationName)
            letter.name = chaStr;
            // console.log(path, chaStr, '#ofshapes: ', shapes.length);
            for (const shape of shapes) {
              const geometry = new THREE.ShapeGeometry(shape);
              const mesh = new THREE.Mesh(geometry, material);
              // mesh.position.set(0, startYCoordinate+YSize*i, 100);
              mesh.scale.set(0.01, 0.01, 0.01);
              mesh.rotation.set(0, 0, Math.PI);
              // mesh.color.set(1.0, 1.0, 1.0)//mesh.color is undefined
              // group.add(mesh);
              letter.add(mesh);
              letter.addMainMesh(mesh.uuid);
            }
            group.add(letter);
            group.addMainMesh(letter.uuid)

            // console.log(letter.uuid, chaStr);//TODO need to group the letter together to form the variableMesh, and group the 
            if (variableMatchLeftOver.indexOf(chaStr) >= 0) {
              variableMatchLeftOver = variableMatchLeftOver.replace(chaStr, '')
              list_variableLetterMeshesUUID.push([chaStr, letter.uuid]);
              meshUUID__mesh[letter.uuid] = letter;//letterMesh
              startVariableMatching = true;
            } else if (startVariableMatching) {//we can this truc: "variable letters are consecutive in paths, if there is letter that is not part of the variable, then we should not keep it as a variable"
              //keep fully_groupped variable in variablesPos__list_chaMeshUUID
              // variablesPos__list_chaMeshUUID[currentVariableToMatch] = list_variableLetterMeshesUUID;
              startVariableMatching = false;
              list_variableInfoDict.push({
                'variableStr':currentVariableToMatch[2],
                'startPos':currentVariableToMatch[0],
                'endPos':currentVariableToMatch[1],
                'info':list_variableLetterMeshesUUID
              });
              //reset
              list_variableLetterMeshesUUID = [];
              if (list_startPosEndPosVariableStr.length > 0) {
                currentVariableToMatch = list_startPosEndPosVariableStr.pop();//need to match new variable
                variableMatchLeftOver = currentVariableToMatch[2];
                if (variableMatchLeftOver.indexOf(chaStr) >= 0) {
                  variableMatchLeftOver = variableMatchLeftOver.replace(chaStr, '')
                  list_variableLetterMeshesUUID.push([chaStr, letter.uuid]);
                  meshUUID__mesh[letter.uuid] = letter;//letterMesh
                }
              }
            }//else ignore, they are not part of any variable... we do not capture them for now

          }
          meshUUID__mesh[group.uuid] = group; // group is the whole latexStr

          //keep fully_groupped variable in variablesPos__list_chaMeshUUID
          // variablesPos__list_chaMeshUUID[currentVariableToMatch] = list_variableLetterMeshesUUID;
          if (list_variableLetterMeshesUUID.length > 0) {
            list_variableInfoDict.push({
              'variableStr':currentVariableToMatch[2],
              'startPos':currentVariableToMatch[0],
              'endPos':currentVariableToMatch[1],
              'info':list_variableLetterMeshesUUID
            });
            //reset
            list_variableLetterMeshesUUID = [];
            
          }
          // console.log('variablesPos__list_chaMeshUUID', variablesPos__list_chaMeshUUID)
          // self.generatedMeshes.push(group);//each group is an equation

          equationMeshCallback(i, list_variableInfoDict, meshUUID__mesh, group.uuid);
         });

      }

    }

    //test out SVG=>THREE.js setup Courtesy of ChatGPT
    getCleanSVG(math) {
      // const svgNode = MathJax.tex2svg(math, {display: true});
      const svgNode = MathJaxSVG.tex2svg(math, {display: true});
      const svg = svgNode.querySelector("svg");

      // Clean style to avoid CSS inheritance issues
      svg.removeAttribute("style");

      // Serialize to string
      return new XMLSerializer().serializeToString(svg);
    }
}



export {LatexMeshCreator};