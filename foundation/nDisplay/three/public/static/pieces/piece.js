import * as THREE from '../three/three.module.js';

import {Animation} from '../custom/Animation.js';
import {LatexMeshCreator} from '../custom/LatexMeshCreater.js'
import {asyncCreateTextMesh} from '../custom/TextMeshCreater.js'

class Piece {
    
    /**
     * 
     * **/
    constructor(scene, camera, renderer, controls, meshes) {

        this.scene = scene;
        this.camera = camera;
        this.renderer = renderer;
        this.controls = controls;
        this.meshUUID__mesh = {};//TODO do we still need this if everything goes to the scene directly?
        // console.log(meshes);
        meshes.forEach(mesh => {this.meshUUID__mesh[mesh.uuid] = mesh});

        this.latexMeshCreator = new LatexMeshCreator();


        this.textStr__textMeshUUID = {};//store all the detailed of the textStrMesh, associates each letter of the textStr to a MeshUUID

        this.animationScheduler = new Animation(scene, camera, renderer);
    }

    highlight({meshUUID, redMag=0.23, greenMag=0.23, blueMag=0.23}) {
        // const actor = this.meshUUID__mesh[meshUUID];
        const actor = this.scene.getObjectByProperty('uuid', meshUUID);//TODO delegate highlight to Actor
        actor.highlight(redMag, greenMag, blueMag);
        this.render();
        // this.meshUUID__mesh[meshUUID] = actor;
        // console.log('highlighted: ', actor)
    }

    unhighlight(meshUUID) {
        // console.log('unhighlight: ', meshUUID)
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


    makeLatexMesh(list_latexStr, readyCallback, requestingAnimationName) {
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
                // console.log('piece.js is calling the readyCallback')
                readyCallback();
                // console.log('this.textStr__textMeshUUID', self.textStr__textMeshUUID);
                // console.log('self.meshUUID__mesh', self.meshUUID__mesh)
            }
        }
        this.latexMeshCreator.getMeshes(list_latexStr, equationMeshCallback, readyCallback, this.textStr__textMeshUUID, requestingAnimationName);
    }

    scheduleAnimation(animation, priority, animationName) {
        this.animationScheduler.animationHoldingPen.push({'animation':animation, 'priority':priority, 'name':animationName});//
    }


    removeMeshesByRequestingAnimation(animationName, completionCallback) {
        const meshUUID__mesh___new = {}; const self = this;
        Object.keys(this.meshUUID__mesh).forEach(meshUUID => {
            if (self.meshUUID__mesh[meshUUID].requestingAnimationName !== animationName) {
                meshUUID__mesh___new[meshUUID] = this.meshUUID__mesh[meshUUID]; //keep
            } else {
                this.scene.remove(this.meshUUID__mesh[meshUUID]);
                // console.log('remove: ', meshUUID)
            }
        })
        this.meshUUID__mesh = meshUUID__mesh___new;
        completionCallback();
    }

    play(playIfTrue) {
        if(playIfTrue() && !this.animationScheduler.playing) {
            this.animationScheduler.playNextAnimation()
        }
    }

    pause(continueFunction, milliseconds) {
        const self = this;
        self.animationScheduler.pause();// if i am not using requestAnimationFrame, how is this still useful?
        const timeoutId = setTimeout(afterPause, milliseconds);
        function afterPause() {
            continueFunction();
            clearTimeout(timeoutId);
        }
    }

    pauseUntilCallback(continueFunction, untilCallBack) {

        const self = this;
        self.animationScheduler.pause();// if i am not using requestAnimationFrame, how is this still useful?
        const intervalId = setInterval(afterPause, 1000);//check every second?
        function afterPause() {
            if (untilCallBack()) {//must be true
                continueFunction();
                clearTimeout(intervalId);

            }
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
        // console.log('in piece.js: ', meshUUID, ', ', this.meshUUID__mesh[meshUUID])
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

    setRotation(meshUUID, angleAboutX, angleAboutY, angleAboutZ) {
        // const q = new THREE.Quaternion(); q.setFromEuler(new THREE.Euler(angleAboutX, angleAboutY, angleAboutZ))
        // this.scene.getObjectByProperty('uuid', meshUUID).setRotationFromQuaternion(q);
        this.scene.getObjectByProperty('uuid', meshUUID).rotation.set(angleAboutX, angleAboutY, angleAboutZ)
    }

    setRequestingAnimation(meshUUID, requestAnimationName) {
        this.scene.getObjectByProperty('uuid', meshUUID).setRequestingAnimation(requestAnimationName);
        this.meshUUID__mesh[meshUUID].setRequestingAnimation(requestAnimationName)
    }

    //remove mesh from scene by uuid
    exit(meshUUID) {
        this.scene.remove(this.meshUUID__mesh[meshUUID]); this.render();
    }

    smoothOrbit(theta, phi, readyCallback) {
        /**
         * theta && phi are in radians
         * 
         * rotates about the object in scene?
         * 
         * **/
        // const fromQuarternion = new THREE.Quaternion().copy(this.camera.quarternion);
        // this.camera.lookAt(new THREE.Vector3(x, y, z));
        // const toQuarternion = new THREE.Quaternion().copy(this.camera.quarternion);
        // this.camera.copy(fromQuarternion); //Restore original quarternion

        const self = this;
        function turnCamera() {
            // self.camera.quarternion.slerp(toQuarternion, 0.1); //0.1 is the speed of rotation
            // self.renderer.render(self.scene, self.camera);


            let currentTheta = 0; let currentPhi = 0; const thetaSpeed = 0.01; const phiSpeed = 0.01;

            function turnCamera___recursion(currentTheta, currentPhi) {

                if (currentTheta >= theta && currentPhi >= phi) {
                    readyCallback();
                    return 
                }
                if(currentTheta < theta) {
                    self.controls._rotateLeft(thetaSpeed); 
                    currentTheta += thetaSpeed
                }
                if(currentPhi < phi) {
                    self.controls._rotateUp(phiSpeed);
                    currentPhi += phiSpeed
                }

                self.controls.update()
                // self.pause(()=>{turnCamera___recursion(currentTheta, currentPhi);}, 1)
                window.requestAnimationFrame(()=>{turnCamera___recursion(currentTheta, currentPhi);})
                
            }
            turnCamera___recursion(currentTheta, currentPhi)


            // self.camera.lookAt(2*self.camera.x, 2*self.camera.y, 2*self.camera.z);
            // self.render()
        }

        turnCamera();
    }


    smoothMoveCameraPosition(x, y, z, readyCallback) {
        const cameraPosition = this.camera.position;
        // console.log(cameraPosition);
        // console.log('x',x, 'y', y, 'z', z);
        // debugger;
        function closeTo(val, tar, precision) {
            return Math.abs(tar-val)<2*Math.abs(precision)
        }

        const self = this; 
        function moveCamera() {
            const moveSpeed = 0.01; let xMoveSpeed; let yMoveSpeed; let zMoveSpeed;
            if (x == cameraPosition.x) {
                xMoveSpeed = 0.001;
            } else {
                xMoveSpeed = (x-cameraPosition.x)*moveSpeed; 
            }
            if (y == cameraPosition.y) {
                yMoveSpeed = 0.001;
            } else {
                yMoveSpeed = (y-cameraPosition.y)*moveSpeed; 
            }
            
            if (z == cameraPosition.z) {
                zMoveSpeed = 0.001;
            } else {
                zMoveSpeed = (z-cameraPosition.z)*moveSpeed; 
            }
            
            // console.log('xMoveSpeed', xMoveSpeed);console.log('yMoveSpeed', yMoveSpeed);console.log('zMoveSpeed', zMoveSpeed);
            // console.log(xMoveSpeed); console.log(yMoveSpeed); console.log(zMoveSpeed)
            function moveCamera___recursion(currentX, currentY, currentZ) {
                if (closeTo(currentX, x, xMoveSpeed) && closeTo(currentY, y, yMoveSpeed) && closeTo(currentZ, z, zMoveSpeed)) {
                    readyCallback(); return
                }

                if(!closeTo(currentX, x, xMoveSpeed)) {
                    currentX += xMoveSpeed
                }


                if(!closeTo(currentY, y, yMoveSpeed)) {
                    currentY += yMoveSpeed
                }


                if(!closeTo(currentZ, z, zMoveSpeed)) {
                    currentZ += zMoveSpeed
                }

                self.camera.position.set(currentX, currentY, currentZ);
                self.render();
                console.log(self.camera.position)
                window.requestAnimationFrame(()=>{moveCamera___recursion(currentX, currentY, currentZ);})
            }
            moveCamera___recursion(cameraPosition.x, cameraPosition.y, cameraPosition.z);
        }
        moveCamera()
    }

    smoothLookAt(x, y, z, readyCallback) {
        /**
         * turns Camera to face x, y, z
         * set the controls.target to camera.position
         * **/
        const target = new THREE.Vector3(x, y, z)
        const cTarget = new THREE.Vector3(this.controls.target.x, this.controls.target.y, this.controls.target.z)
        cTarget.sub(this.camera.position)
        const currentLookSph = new THREE.Spherical()
        currentLookSph.setFromCartesianCoords(cTarget.x, cTarget.y, cTarget.z)
        target.sub(this.camera.position);
        const endingLookSph = new THREE.Spherical()
        endingLookSph.setFromCartesianCoords(target.x, target.y, target.z)
        const theta = endingLookSph.theta - currentLookSph.theta;
        const phi = endingLookSph.phi - currentLookSph.phi;
        const cameraPosition = this.camera.position

        const self = this;

        //set OrbitTarget to within_an_inch(cTarget.x/1000, cTarget.y/1000, cTarget.z/1000) of camera but still face the camera towards cTarget
        self.controls.target.set(cameraPosition.x+(cTarget.x/1000), cameraPosition.y+(cTarget.y/1000), cameraPosition.z+(cTarget.z/1000))
        self.controls.update()
        //and then orbit around that within_an_inch point, with theta and phi
        self.smoothOrbit(theta, phi, function() {
            //at the end, just set self.controls.target to target
            self.controls.target.set(target.x, target.y, target.z);
            self.controls.update()
            readyCallback();
        })
    }

    pollForTicket(ticketNum, ticketCallback) {
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const self = this;
        let hadReturned = false; const timeOutIds = [];

        function poll() {//recursive polling no need to setInterval and then clear interval

            const formData = new FormData();
            formData.append('ticketNum', ticketNum)
            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function(){
                if (this.readyState == 4 && this.status == 200) {
                    if (this.responseText.length > 0) {//if the ticket is not ready, backend will send a length zero string
                        ticketCallback(this.responseText);
                        hadReturned = true;
                        timeOutIds.forEach((timeOutId) => {
                            clearTimeout(timeOutId)
                        })
                    } else if(!hadReturned) {
                        const timeOutId = setTimeout(poll, 1000); // wait 1s before next poll
                        timeOutIds.push(timeOutId)
                    }
                }
            }
            xhr.open('POST', pollable_url);
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
            xhr.send(formData);
        }
        poll();
    }

}

export {Piece};