

class Piece {
    
    /**
     * NEED to move all the things only relevant to circuit, to circuit.js<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
     * **/
    constructor(scene, camera, renderer, meshes) {

        this.scene = scene;
        this.camera = camera;
        this.renderer = renderer;
        this.meshes = meshes;

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

}

export {Piece};