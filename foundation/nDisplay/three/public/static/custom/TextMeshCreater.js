import * as THREE from '../three/three.module.js';
import {TextGeometry} from '../three/TextGeometry.js';
import {FontLoader} from '../three/FontLoader.js'



async function asyncCreateTextMesh(message, position, color, materialName, fontSize, onMeshReady) {

    const loader = new FontLoader();
    const font = await loader.loadAsync( 'fonts/helvetiker_regular.typeface.json' );

    const shapes = font.generateShapes( message, fontSize );
    const geometry = new THREE.ShapeGeometry( shapes );
    geometry.computeBoundingBox();
    const xMid = - 0.5 * ( geometry.boundingBox.max.x - geometry.boundingBox.min.x );

    //make material
    let material;
    if (materialName == 'line') {

        material = new THREE.LineBasicMaterial( {
            color: color,
            side: THREE.DoubleSide
        } );


        // make line shape ( N.B. edge view remains visible )
        const holeShapes = [];

        for ( let i = 0; i < shapes.length; i ++ ) {
            const shape = shapes[ i ];
            if ( shape.holes && shape.holes.length > 0 ) {
                for ( let j = 0; j < shape.holes.length; j ++ ) {
                    const hole = shape.holes[ j ];
                    holeShapes.push( hole );
                }
            }
        }

        shapes.push( ...holeShapes );
        const lineText = new THREE.Object3D();
        for ( let i = 0; i < shapes.length; i ++ ) {
            const shape = shapes[ i ];
            const points = shape.getPoints();
            const geometry = new THREE.BufferGeometry().setFromPoints( points );
            geometry.translate( xMid, 0, 0 );
            const lineMesh = new THREE.Line( geometry, material );
            lineText.add( lineMesh );

        }
        // scene.add( lineText );
        onMeshReady(lineText);

    } else if (materialName == 'mesh') {

        material = new THREE.MeshBasicMaterial( {
            color: color,
            transparent: true,
            opacity: 0.4,
            side: THREE.DoubleSide
        } );


        geometry.translate( xMid, 0, 0 );
        // make shape ( N.B. edge view not visible )
        const text = new THREE.Mesh( geometry, material );
        text.position.x = position.x;
        text.position.y = position.y;
        text.position.z = position.z;
        // scene.add( text );
        // return text;
        onMeshReady(text);
    }

}



export {asyncCreateTextMesh};