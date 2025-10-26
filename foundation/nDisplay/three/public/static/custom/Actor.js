import * as THREE from '../three/three.module.js';

class Actor extends THREE.Group{
    
    constructor() {
        super();
        this.mainMeshUUID = [];
        this.requestingAnimationName = null;
    }

    addMainMesh(meshUUID) {
        this.mainMeshUUID.push(meshUUID);
    }

    setType(type) {
        this.type = type;// cannot set in constructor because ~Component.js sets this as rawAttribute of this class <<<<<TODO
    }

    setRequestingAnimation(animationName) {
        this.requestingAnimationName = animationName;
    }


    /**
     * Get all disjoint mainMeshes
     * **/
    getAllMainMeshes() {
        const disjointMainMeshes = []; let disjointMesh;
        this.mainMeshUUID.forEach(meshUUID => {
            disjointMesh = this.getObjectByProperty('uuid', meshUUID);
            disjointMainMeshes.push(disjointMesh)
        })
        return disjointMainMeshes
    }

    getDimensions() {
        const boundingBox = new THREE.Box3();
        boundingBox.setFromObject(this);
        // console.log(boundingBox)
        return {
            xLen:boundingBox.max.x-boundingBox.min.x,
            yLen:boundingBox.max.y-boundingBox.min.y,
            zLen:boundingBox.max.z-boundingBox.min.z,
        }
    }


    cacheOGColors() {
        const meshes = this.getAllMainMeshes();
        for(let i=0; i<meshes.length; i++) {
            // console.log(meshes[i].geometry.attributes.color, ' ===undefined ', meshes[i].geometry.attributes.color === undefined)//some colors like Wire and LatexMesh does not have array
            if (meshes[i].geometry.attributes.color === undefined) { // some colors like Wire and LatexTextMesh's color is not in geometry.attributes, but in material.color
                // meshes[i].userData['OGColorArray'] = meshes[i].material.color;
                meshes[i].userData['OGColorArray'] = {r:meshes[i].material.color.r, g:meshes[i].material.color.g, b:meshes[i].material.color.b}
            } else{
                meshes[i].userData['OGColorArray'] = meshes[i].geometry.attributes.color.array;
            }
            // console.log('OG meshIdx: ', i, ' OG color: ', meshes[i].userData['OGColorArray'], '########')
        }

    }
    /**
     * Changes the color of this meshUUID, and stores the original color
     * 
     * Checks if this color is a light|dark color,
     * if this color is a light color, then we turn it dark by user_assigned_percentage
     * if this color is a dark color, then we turn it light by user_assigned_percentage
     * 
     * user_assigned_percentage is a decimal from 0 to 1
     * **/
    contrast(contrast_percentage) {
        function rgbToInt(r, g, b) {
          // Convert each component to a hexadecimal string
          const hexR = r.toString(16).padStart(2, 0);
          const hexG = g.toString(16).padStart(2, 0);
          const hexB = b.toString(16).padStart(2, 0);


          // Concatenate the hexadecimal values with a '#' prefix
          const hexStr = hexR + hexG + hexB
          return parseInt(hexStr, 16) //convert to decimal(10) on base 16
        }

        function getComplementColor(colorInt) {
            const maxNum = 256 * 256 * 256 // the maxColor// could be higher to prevent unneccessary_reinitialisation
            return maxNum - colorInt
        }
        function isDarkColor(r, g, b) {
            const colorInt = rgbToInt(r, g, b)
            const complementColorInt = getComplementColor(colorInt);//complementColor is a number
            return complementColorInt > colorInt;
        }



        this.cacheOGColors();
        this.updateColor(
            function(OGred, OGgreen, OGblue){//geometryCallback
                let isDark = isDarkColor(OGred, OGgreen, OGblue)
                let signed_contrast_percentage
                if (isDark) {
                    signed_contrast_percentage = contrast_percentage;//make it light, bigger number
                } else {
                    signed_contrast_percentage = 1 - contrast_percentage;//make it dark, smaller number
                }
                return [
                    Math.max(0.0, Math.min(1.0, OGred*signed_contrast_percentage)), 
                    Math.max(0.0, Math.min(1.0, OGgreen*signed_contrast_percentage)), 
                    Math.max(0.0, Math.min(1.0, OGblue*signed_contrast_percentage))
                ];
            },
            function(colorCoordinate, colorFlag){//arrayCallback
                let signed_contrast_percentage
                if (colorCoordinate < 0.5) {//dark color
                    signed_contrast_percentage = contrast_percentage;//make it light, bigger number
                } else {
                    signed_contrast_percentage = 1 - contrast_percentage;//make it dark, smaller number
                }
                switch (colorFlag) {
                    case 'r':
                        return Math.max(0.0, Math.min(1.0, colorCoordinate*signed_contrast_percentage));
                    case 'g':
                        return Math.max(0.0, Math.min(1.0, colorCoordinate*signed_contrast_percentage));
                    case 'b':
                        return Math.max(0.0, Math.min(1.0, colorCoordinate*signed_contrast_percentage));
                }
            }
        );
    }


    /**
     * Changes the color of this meshUUID, and stores the original color
     * 
     * TODO for latexEquation, where the letter are in a THREE.Group, you need to traverse
     * 
     * this.traverse(function(child) {highlight(child)});
     * **/
    highlight(redMag, greenMag, blueMag) {
        this.userData['highlight'] = [redMag, greenMag, blueMag];
        // console.log(actor.userData)
        // const meshes = this.getAllMainMeshes();
        // for(let i=0; i<meshes.length; i++) {
        //     // console.log(meshes[i].geometry.attributes.color, ' ===undefined ', meshes[i].geometry.attributes.color === undefined)//some colors like Wire and LatexMesh does not have array
        //     if (meshes[i].geometry.attributes.color === undefined) { // some colors like Wire and LatexTextMesh's color is not in geometry.attributes, but in material.color
        //         // meshes[i].userData['OGColorArray'] = meshes[i].material.color;
        //         meshes[i].userData['OGColorArray'] = {r:meshes[i].material.color.r, g:meshes[i].material.color.g, b:meshes[i].material.color.b}
        //     } else{
        //         meshes[i].userData['OGColorArray'] = meshes[i].geometry.attributes.color.array;
        //     }
        //     // console.log('OG meshIdx: ', i, ' OG color: ', meshes[i].userData['OGColorArray'], '########')
        // }
        this.cacheOGColors();

        // const meshes = this.getAllMainMeshes();
        // meshes.forEach(mesh => {
        //     if (mesh.geometry.attributes.color === undefined) {// some colors like Wire and LatexTextMesh's color is not in geometry.attributes, but in material.color

        //         mesh.material.color.set(
        //             Math.max(0.0, Math.min(1.0, mesh.material.color.r+redMag)), 
        //             Math.max(0.0, Math.min(1.0, mesh.material.color.g+greenMag)), 
        //             Math.max(0.0, Math.min(1.0, mesh.material.color.b+blueMag))
        //         )

        //     } else {

        //         const colorArray = [];
        //         mesh.geometry.attributes.color.array.forEach((colorCoordinate, idx) => {
        //             if (idx %3 == 0) {//red
        //                 colorCoordinate = Math.max(0.0, Math.min(1.0, colorCoordinate+redMag));// the maximum whiteness is 1.0
        //             } else if (idx%3 == 1) {//green
        //                 colorCoordinate = Math.max(0.0, Math.min(1.0, colorCoordinate+greenMag));// the maximum whiteness is 1.0
        //             } else {//blue
        //                 colorCoordinate = Math.max(0.0, Math.min(1.0, colorCoordinate+blueMag));// the maximum whiteness is 1.0
        //             }
        //             colorArray.push(colorCoordinate)
        //         })
        //         mesh.geometry.setAttribute('color', new THREE.BufferAttribute(new Float32Array(colorArray), 3));
        //     }
        // })
        this.updateColor(
            function(OGred, OGgreen, OGblue){//geometryCallback
                return [
                    Math.max(0.0, Math.min(1.0, OGred+redMag)), 
                    Math.max(0.0, Math.min(1.0, OGgreen+greenMag)), 
                    Math.max(0.0, Math.min(1.0, OGblue+blueMag))
                ];
            },
            function(colorCoordinate, colorFlag){//arrayCallback
                switch (colorFlag) {
                    case 'r':
                        return Math.max(0.0, Math.min(1.0, colorCoordinate+redMag));
                    case 'g':
                        return Math.max(0.0, Math.min(1.0, colorCoordinate+greenMag));
                    case 'b':
                        return Math.max(0.0, Math.min(1.0, colorCoordinate+blueMag));
                }
            }
        );
    }


    updateColor(geometryCallback, arrayCallback) {
        /**
         * geometryCallback takes OGred, OGgreen, OGblue
         * 
         * arrayCallback takes a number, and string flag {'r', 'g', 'b'}
         * **/

        const meshes = this.getAllMainMeshes();
        let newR, newG, newB;
        meshes.forEach(mesh => {
            if (mesh.geometry.attributes.color === undefined) {// some colors like Wire and LatexTextMesh's color is not in geometry.attributes, but in material.color
                [newR, newG, newB] = geometryCallback(mesh.material.color.r, mesh.material.color.g, mesh.material.color.b)
                mesh.material.color.set(
                    Math.max(0.0, Math.min(1.0, newR)), 
                    Math.max(0.0, Math.min(1.0, newG)), 
                    Math.max(0.0, Math.min(1.0, newB))
                )

            } else {

                const colorArray = [];
                mesh.geometry.attributes.color.array.forEach((colorCoordinate, idx) => {
                    if (idx %3 == 0) {//red
                        newR = arrayCallback(colorCoordinate, 'r')
                        colorCoordinate = newR
                        // colorCoordinate = Math.max(0.0, Math.min(1.0, colorCoordinate+redMag));// the maximum whiteness is 1.0
                    } else if (idx%3 == 1) {//green
                        newG = arrayCallback(colorCoordinate, 'g')
                        colorCoordinate = newG
                        // colorCoordinate = Math.max(0.0, Math.min(1.0, colorCoordinate+greenMag));// the maximum whiteness is 1.0
                    } else {//blue
                        newB = arrayCallback(colorCoordinate, 'b')
                        colorCoordinate = newB
                        // colorCoordinate = Math.max(0.0, Math.min(1.0, colorCoordinate+blueMag));// the maximum whiteness is 1.0
                    }
                    colorArray.push(colorCoordinate)
                })
                mesh.geometry.setAttribute('color', new THREE.BufferAttribute(new Float32Array(colorArray), 3));
            }
        })
    }


    /**
     * Return the mesh to its original color stored in the userData
     * **/
    unhighlight() {
        // console.log('DOING unhighlight: ', meshUUID)
        this.userData['highlight'] = undefined;
        const meshes = this.getAllMainMeshes();
        meshes.forEach((mesh, idx) => {
            if (mesh.geometry.attributes.color === undefined) {// some colors like Wire and LatexTextMesh's color is not in geometry.attributes, but in material.color

                // console.log('set material: ', mesh.userData['OGColorArray'])
                mesh.material.color.set(
                    mesh.userData['OGColorArray'].r, 
                    mesh.userData['OGColorArray'].g, 
                    mesh.userData['OGColorArray'].b
                )
            } else {
                // console.log('set geometry')
                mesh.geometry.setAttribute('color', new THREE.BufferAttribute(mesh.userData['OGColorArray'], 3));
            }
        })
        // console.log('unhighlighted: ', this)
    }
}

export {Actor}