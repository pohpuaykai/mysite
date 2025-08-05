

class Piece {
    
    /**
     * NEED to move all the things only relevant to circuit, to circuit.js<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<TODO
     * **/
    constructor(scene, camera, renderer, meshes) {

        this.scene = scene;
        this.camera = camera;
        this.renderer = renderer;
        this.meshes = meshes;

        
        // this.wiring = [];
        // // this.wiringSansWires = [];//originally for rcclorthogonallayout, but to differentiate parallel_circuit from series_circuit, we need wire nodes. so... this is defunked for now
        // this.uuid__type = {};
        // this.uuid__positiveLeadsDirections = {};
        // this.edgeUUID__solderableIndices = {};
        // this.edge__solderableIndices = {};

        // this.type__boundingBox = {};//<<<<<<<<<<<<<put into one endpoint, then query

        // //getBBox of each schematic size
        // function getBBoxFromSVGString(svgString) {

        //     // Parse the SVG string
        //     const parser = new DOMParser();
        //     const svgDoc = parser.parseFromString(svgString, "image/svg+xml");
        //     const svgElement = svgDoc.documentElement;

        //     // Append to DOM (hidden)
        //     svgElement.style.position = "absolute";
        //     svgElement.style.visibility = "hidden";
        //     svgElement.style.pointerEvents = "none";
        //     svgElement.style.width = "auto";
        //     svgElement.style.height = "auto";
        //     document.body.appendChild(svgElement);

        //     // Now getBBox
        //     const bbox = svgElement.getBBox();
        //     console.log(bbox);

        //     // Optional: clean up
        //     svgElement.remove();
        //     return bbox;

        // }
        // let componenttypeSVGFilepath_ajax = new XMLHttpRequest(); this.componentType__boundingBox = {}; const self = this;
        // componenttypeSVGFilepath_ajax.addEventListener("load", function() {
        //     const componenttype__svgfilepath___str = componenttypeSVGFilepath_ajax.responseText;
        //     const COMPONENTTYPE__SVGFILEPATH___entries = Object.entries(JSON.parse(componenttype__svgfilepath___str));
        //     console.log(COMPONENTTYPE__SVGFILEPATH___entries);
        //     let componentType; let svgFilepath;let absolutePath;
        //     for (let i=0; i<COMPONENTTYPE__SVGFILEPATH___entries.length; i++) {
        //         // if (COMPONENTTYPE__SVGFILEPATH___entries[i] != undefined) { //https://developer.mozilla.org/en-US/docs/Web/API/SVGGraphicsElement/getBBox
        //             [componentType, svgFilepath] = COMPONENTTYPE__SVGFILEPATH___entries[i];
        //             absolutePath = '/public/static/'+svgFilepath;
        //             let ajax = new XMLHttpRequest();
        //             ajax.addEventListener("load", function(componentType) {
        //                 return function () {
        //                     // console.log(ajax.responseText);
        //                     let svgString = ajax.responseText;
        //                     let svgBBox = getBBoxFromSVGString(svgString);
        //                     console.log(componentType, svgBBox);
        //                     // self.componentType__boundingBox[componentType] = svgBBox;
        //                     self.componentType__boundingBox[componentType] = {'width':svgBBox.width, 'height':svgBBox.height};
        //                     // console.log('componentType__boundingBox', JSON.stringify(self.componentType__boundingBox));
        //                 }
        //             }(componentType));
        //             console.log(componentType, absolutePath);
        //             ajax.open("GET", absolutePath);
        //             ajax.send();
        //     }
        // });
        // componenttypeSVGFilepath_ajax.open("GET", "/public/static/settings/ComponentType__SVGFilepath.json");//hide this link?<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        // componenttypeSVGFilepath_ajax.send();
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