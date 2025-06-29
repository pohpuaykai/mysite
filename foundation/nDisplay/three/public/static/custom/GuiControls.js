/**
 * AddsOn Gui to OrbitControls.js
 * **/
import {
    Controls,
    MOUSE,
    Quaternion,
    Spherical,
    TOUCH,
    Vector2,
    Vector3,
    Plane,
    Ray,
    Raycaster,
    MathUtils
} from '../three/three.module.js';
import {OrbitControls} from '../three/OrbitControls.js';
import {RayIntersectBox} from '../common/RayIntersectBox.js';


/**
 * Fires when the camera has been transformed by the controls.
 *
 * @event OrbitControls#change
 * @type {Object}
 */
const _changeEvent = { type: 'change' };

/**
 * Fires when an interaction was initiated.
 *
 * @event OrbitControls#start
 * @type {Object}
 */
const _startEvent = { type: 'start' };

/**
 * Fires when an interaction has finished.
 *
 * @event OrbitControls#end
 * @type {Object}
 */
const _endEvent = { type: 'end' };

const _ray = new Ray();
const _plane = new Plane();
const _TILT_LIMIT = Math.cos( 70 * MathUtils.DEG2RAD );

const _v = new Vector3();
const _twoPI = 2 * Math.PI;

const _STATE = {
    NONE: - 1,
    ROTATE: 0,
    DOLLY: 1,
    PAN: 2,
    TOUCH_ROTATE: 3,
    TOUCH_PAN: 4,
    TOUCH_DOLLY_PAN: 5,
    TOUCH_DOLLY_ROTATE: 6,
    // ALTLEFT_DOWN: 7
};
const _EPS = 0.000001;


class GuiControls extends OrbitControls {

    constructor(camera, scene, domElement=null) {
        super(camera, domElement);
        this.keys = { LEFT: 'ArrowLeft', UP: 'ArrowUp', RIGHT: 'ArrowRight', BOTTOM: 'ArrowDown', ALTLEFT: 'AltLeft' };

        this._onMouseDown = onMouseDown.bind( this );
        this._onKeyDown = onKeyDown.bind( this );
        this.listenToKeyEvents(window);
        this.camera = camera; this.scene = scene;
    }


    _handleRayCast(event) {
        console.log('raycast start');
        // example from https://threejs.org/docs/#api/en/core/Raycaster
        //calculate pointer position in normalized device coordinates
        const pointer = new Vector2();
        pointer.x = (event.clientX / window.innerWidth) * 2 - 1;
        pointer.y = (event.clientY / window.innerWidth) * 2 + 1;

        //update the picking ray with the camera and pointer position
        const raycaster = new Raycaster();
        raycaster.setFromCamera(pointer, this.camera);

        //calculate objects intersecting the picking ray
        console.log('this.scene.children: ', this.scene.children);
        const intersects = [];
        raycaster.intersectObjects(this.scene.children, true, intersects);//TODO use kDTree.js for Large number of objects
        // intersects is empty, might be the layers
        console.log('intersects:', intersects);
        for (let i=0; i<intersects.length; i++) {
            // intersects[i].object.material.color.set(0xff0000);//highlight as bright_RED
            console.log('intersected object.material.color: ', intersects[i].object.material.color);
        }
    }
}


function onMouseDown(event) {//NOTE <<this>>==orbitControls
    // console.log('before OrbitControls_OnMouseDown');
    let mouseAction;
    switch ( event.button ) {
        case 0:
            mouseAction = this.mouseButtons.LEFT;
            break;
        case 1:
            mouseAction = this.mouseButtons.MIDDLE;
            break;
        case 2:
            mouseAction = this.mouseButtons.RIGHT;
            break;
        default:
            mouseAction = - 1;
    }
    switch ( mouseAction ) {
        case MOUSE.DOLLY:
            if ( this.enableZoom === false ) return;
            //
            this._handleMouseDownDolly( event );
            this.state = _STATE.DOLLY;
            break;
        case MOUSE.ROTATE://this is my LEFT mouseButtons
            //this is quite ugly
            // console.log('this.mouseButtons.MIDDLE');
            // if ( this.state == _STATE.ALTLEFT_DOWN ) {
            if ( event.altKey ) {
                // console.log('mouseButtons.MIDDLE also _STATE.ALTLEFT_DOWN');
                this._handleRayCast(event);
                this.state = _STATE.DOLLY;// put back old state, although its not
                break
            }
            if ( event.ctrlKey || event.metaKey || event.shiftKey ) {
                if ( this.enablePan === false ) return;
                this._handleMouseDownPan( event );
                this.state = _STATE.PAN;
            } else {
                if ( this.enableRotate === false ) return;
                this._handleMouseDownRotate( event );
                this.state = _STATE.ROTATE;
            }
            break;
        case MOUSE.PAN:
            // console.log('this.mouseButtons.RIGHT');
            if ( event.ctrlKey || event.metaKey || event.shiftKey ) {
                if ( this.enableRotate === false ) return;
                this._handleMouseDownRotate( event );
                this.state = _STATE.ROTATE;
            } else {
                if ( this.enablePan === false ) return;
                this._handleMouseDownPan( event );
                this.state = _STATE.PAN;
            }
            break;
        default:
            this.state = _STATE.NONE;
    }
    if ( this.state !== _STATE.NONE ) {
        this.dispatchEvent( _startEvent );
    }
    // console.log('after OrbitControls_OnMouseDown');
}


function onKeyDown( event ) {
    // console.log('before onKeyDown');
    // if ( this.enabled === false ) return;
    let needsUpdate = false;
    // console.log('keyEventCode: ', event.code);
    switch ( event.code ) {
        case this.keys.UP:
            if ( event.ctrlKey || event.metaKey || event.shiftKey ) {
                if ( this.enableRotate ) {
                    this._rotateUp( _twoPI * this.keyRotateSpeed / this.domElement.clientHeight );
                }
            } else {
                if ( this.enablePan ) {
                    this._pan( 0, this.keyPanSpeed );
                }
            }
            needsUpdate = true;
            break;
        case this.keys.BOTTOM:
            if ( event.ctrlKey || event.metaKey || event.shiftKey ) {
                if ( this.enableRotate ) {
                    this._rotateUp( - _twoPI * this.keyRotateSpeed / this.domElement.clientHeight );
                }
            } else {
                if ( this.enablePan ) {
                    this._pan( 0, - this.keyPanSpeed );
                }
            }
            needsUpdate = true;
            break;
        case this.keys.LEFT:
            if ( event.ctrlKey || event.metaKey || event.shiftKey ) {
                if ( this.enableRotate ) {
                    this._rotateLeft( _twoPI * this.keyRotateSpeed / this.domElement.clientHeight );
                }
            } else {
                if ( this.enablePan ) {
                    this._pan( this.keyPanSpeed, 0 );
                }
            }
            needsUpdate = true;
            break;
        case this.keys.RIGHT:
            if ( event.ctrlKey || event.metaKey || event.shiftKey ) {
                if ( this.enableRotate ) {
                    this._rotateLeft( - _twoPI * this.keyRotateSpeed / this.domElement.clientHeight );
                }
            } else {
                if ( this.enablePan ) {
                    this._pan( - this.keyPanSpeed, 0 );
                }
            }
            needsUpdate = true;
            break;
        // case this.keys.ALTLEFT:
        //     console.log('***', this.keys.ALTLEFT);
        //     this.state = _STATE.ALTLEFT_DOWN;
        //     console.log(this.state);
        //     needsUpdate = false;
        //     break;
    }
    if ( needsUpdate ) {
        // prevent the browser from scrolling on cursor keys
        event.preventDefault();
        this.update();
    }
    // console.log('after onKeyDown');
}

export {GuiControls};