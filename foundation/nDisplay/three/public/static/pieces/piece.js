import * as THREE from '../three/three.module.js';

import {Animation} from '../custom/Animation.js';
import {LatexMeshCreator} from '../custom/LatexMeshCreater.js'
import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js'

class Piece {
    
    /**
     * NEED to move all the things only relevant to circuit, to circuit.js<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
     * **/
    constructor(scene, camera, renderer, meshes) {

        this.scene = scene;
        this.camera = camera;
        this.renderer = renderer;
        this.meshUUID__mesh = {};//TODO do we still need this if everything goes to the scene directly?
        console.log(meshes);
        meshes.forEach(mesh => {this.meshUUID__mesh[mesh.uuid] = mesh});

        this.latexMeshCreator = new LatexMeshCreator();


        this.textStr__textMeshUUID = {};//store all the detailed of the textStrMesh, associates each letter of the textStr to a MeshUUID

        this.animationHoldingPen = [];
        this.animationScheduler = new Animation(scene, camera, renderer);
    }

    highlight({meshUUID, redMag=0.23, greenMag=0.23, blueMag=0.23}) {
        // const actor = this.meshUUID__mesh[meshUUID];
        const actor = this.scene.getObjectByProperty('uuid', meshUUID);//TODO delegate highlight to Actor
        actor.highlight(redMag, greenMag, blueMag);
        this.render();
        // this.meshUUID__mesh[meshUUID] = actor;
        console.log('highlighted: ', actor)
    }

    unhighlight(meshUUID) {
        console.log('unhighlight: ', meshUUID)
        // const actor = this.meshUUID__mesh[meshUUID];

        const actor = this.scene.getObjectByProperty('uuid', meshUUID);//TODO delegate unhighlight to Actor
        // console.log('unhighlight actor: ', actor)
        // console.log('unhighligh actor.userData: ', actor.userData)
        // console.log(actor.userData['highlight'])
        if (actor.userData['highlight'] !== undefined) {
            actor.unhighlight()
            this.render();
        }
    }

    getDimensions(meshUUID) {

        const actor = this.scene.getObjectByProperty('uuid', meshUUID);//TODO delegate to Actor
        return actor.getDimensions()
    }


    makeLatexMesh(list_latexStr, readyCallback) {
        const self = this;
        const indices = new Set();

        function equationMeshCallback(latexStrIdx, textMeshInformation, meshUUID__mesh, latexStrMeshUUID) {
            self.textStr__textMeshUUID[list_latexStr[latexStrIdx][0]] = {'info':textMeshInformation, 'type':'latex', 'meshUUID':latexStrMeshUUID};
            self.meshUUID__mesh = Object.assign({}, meshUUID__mesh, self.meshUUID__mesh);
            meshUUID__mesh[latexStrMeshUUID].visible = false;
            meshUUID__mesh[latexStrMeshUUID].position.set(0, 0, 0);//default position, will be changed in the circuit itself.
            self.enter(latexStrMeshUUID)
            //check if all the list_latexStr's meshes are prepared by idx, then call the readyCallback
            indices.add(latexStrIdx);
            console.log(indices.size, list_latexStr.length, indices.length == list_latexStr.length)
            if (indices.size == list_latexStr.length) { // all the meshes are ready in textStr__textMeshUUID
                console.log('piece.js is calling the readyCallback')
                readyCallback();
                console.log('this.textStr__textMeshUUID', self.textStr__textMeshUUID);
                console.log('self.meshUUID__mesh', self.meshUUID__mesh)
            }
        }
        this.latexMeshCreator.getMeshes(list_latexStr, equationMeshCallback, readyCallback);
    }

    scheduleAnimation(animation, priority) {
        this.animationHoldingPen.push({'animation':animation, 'priority':priority});//
    }

    play() {
        this.animationScheduler.resetAggregatedAnimations();
        this.animationHoldingPen.sort((a, b) => a['priority'] - b['priority']);//ascending order
        for(let i=0; i<this.animationHoldingPen.length; i++) {
            this.animationScheduler.appendAction(this.animationHoldingPen[i]['animation']);
        }
        this.animationScheduler.restartAnimation();//also starts the animations appended in the forloop earlier
    }

    pause(continueFunction, milliseconds) {
        const self = this;
        self.animationScheduler.pause()
        const timeoutId = setTimeout(afterPause, milliseconds);
        function afterPause() {
            self.animationScheduler.start();
            console.log('afterPause')
            continueFunction();
            clearTimeout(timeoutId);
        }
    }

    /**
     * 
     * @abstract
     * @return a dictionary mapping from localFunction variable_names to variables (
     *  scene
     *  camera
     *  renderer
     *  meshes - a dictionary of variables_names to variables (meshes)
     *  animate - function for renderer.setAnimationLoop on main.js
     * )
     * **/
    act() {
        console.warn( ': .act() not implemented.' );
    }

    render() {
        this.renderer.render(this.scene, this.camera);

    }

    enter(meshUUID) {
        console.log('in piece.js: ', meshUUID, ', ', this.meshUUID__mesh[meshUUID])
        this.scene.add(this.meshUUID__mesh[meshUUID]); this.render();
    }

    reveal(meshUUID) {
        this.scene.getObjectByProperty('uuid', meshUUID).visible = true;
        this.render();
    }

    hide(meshUUID) {
        this.scene.getObjectByProperty('uuid', meshUUID).visible = false;
        this.render();
    }

    setPosition(meshUUID, x, y, z) {
        this.scene.getObjectByProperty('uuid', meshUUID).position.set(x, y, z);
    }

    //remove mesh from scene by uuid
    exit(meshUUID) {
        this.scene.remove(this.meshUUID__mesh[meshUUID]); this.render();
    }


}

export {Piece};