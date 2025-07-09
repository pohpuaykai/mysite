import * as THREE from '../three/three.module.js';
import {SVGLoader} from '../three/SVGLoader.js';


async function asyncCreateLatexMesh(scene, renderer, camera, listOfEquations_latexStrs) {
//(message, position, color, materialName, fontSize, onMeshReady) {

    //test out SVG=>THREE.js setup Courtesy of ChatGPT
    function getCleanSVG(math) {
      const svgNode = MathJax.tex2svg(math, {display: true});
      const svg = svgNode.querySelector("svg");

      // Clean style to avoid CSS inheritance issues
      svg.removeAttribute("style");

      // Serialize to string
      return new XMLSerializer().serializeToString(svg);
    }
    const YSize = 30;
    const startYCoordinate = -listOfEquations_latexStrs.length* YSize/2;
    for (let i=0; i<listOfEquations_latexStrs.length; i++) {
        let latexStr = listOfEquations_latexStrs[i]; //console.log(latexStr);

        const svgString = getCleanSVG(latexStr);
        const blob = new Blob([svgString], {type: "image/svg+xml"});
        const url = URL.createObjectURL(blob);

        const loader = new SVGLoader();

        loader.load(url, (data) => {
          const paths = data.paths;
          const group = new THREE.Group();

          for (const path of paths) {
            const material = new THREE.MeshBasicMaterial({
              color: path.color,
              side: THREE.DoubleSide,
              depthWrite: false
            });

            const shapes = path.toShapes(true);
            for (const shape of shapes) {
              const geometry = new THREE.ShapeGeometry(shape);
              const mesh = new THREE.Mesh(geometry, material);
              mesh.position.set(0, startYCoordinate+YSize*i, 100);
              mesh.scale.set(0.01, 0.01, 0.01);
              mesh.rotation.set(0, 0, Math.PI)
              group.add(mesh);
            }
          }
          // group.position.set(0, 0, -100);
          console.log('svg position: ', group.position);

          scene.add(group); renderer.render(scene, camera);
        });
    }


    // const svgString = getCleanSVG("x^2 + y^2 = z^2");
    // const blob = new Blob([svgString], {type: "image/svg+xml"});
    // const url = URL.createObjectURL(blob);

    // const loader = new SVGLoader();

    // loader.load(url, (data) => {
    //   const paths = data.paths;
    //   const group = new THREE.Group();

    //   for (const path of paths) {
    //     const material = new THREE.MeshBasicMaterial({
    //       color: path.color,
    //       side: THREE.DoubleSide,
    //       depthWrite: false
    //     });

    //     const shapes = path.toShapes(true);
    //     for (const shape of shapes) {
    //       const geometry = new THREE.ShapeGeometry(shape);
    //       const mesh = new THREE.Mesh(geometry, material);
    //       mesh.position.set(0, 0, 100);
    //       mesh.scale.set(0.01, 0.01, 0.01);
    //       mesh.rotation.set(0, 0, Math.PI)
    //       group.add(mesh);
    //     }
    //   }
    //   // group.position.set(0, 0, -100);
    //   console.log('svg position: ', group.position);

    //   scene.add(group); renderer.render(scene, camera);
    // });
    //
}

export {asyncCreateLatexMesh};