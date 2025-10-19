class Animation {
    
    constructor(scene, camera, renderer){
        this.scene = scene; this.camera = camera; this.renderer = renderer;
        //Player functionalities like run, pause... (Courtesy of ChatGPT)
        this.requestId = null; this.running = false; this.lastTime = 0;


        this.animationHoldingPen = [];
        this.lastAnimationPlayedId = null;
        this.playing = false;

        //for sticking animations together in a timeline, TODO please remove this does not work any more
        // this.aggregatedAnimations = function(){}; // this does not contain the 'this.renderer.render(this.scene, this.camera)'
        // this.animation = function(){};
        // this.clock = new THREE.Clock();
        // this.delta = this.clock.getDelta();//time since last frame (Courtesy of ChatGPT)
    }

    // appendAction(action, name){//this does not work, since it will still run all the animations in parallel, you have to use recursion
    //     //Copied from ChatGPT

    //     //Capture the current animation function in a local variable
    //     const oldAnimation = this.aggregatedAnimations.bind(this);

    //     this.aggregatedAnimations = function() {
    //         oldAnimation(); 
    //         console.log('running: ', name);
    //         action();
    //     }
    //     // const self = this;
    //     this.animation = this.aggregatedAnimations
    // };

    scheduleAnimation(animation, priority, animationName, callback) {
        this.animationHoldingPen.push({'animation':animation, 'priority':priority, 'name':animationName});//
        callback();
    }

    playNextAnimation() {
        if(this.lastAnimationPlayedId === null) {
            this.playing = true
            this.animationHoldingPen.sort((a, b) => a['priority'] - b['priority']);//ascending order
            // this.animationHoldingPen.sort((a, b) => b['priority'] - a['priority']);//descending order
            const animationInfoDict = this.animationHoldingPen[0];// play this first one
            console.log('playing animation: ', animationInfoDict['name'])
            animationInfoDict['animation']();
            this.lastAnimationPlayedId = 0; 
        } else if (this.lastAnimationPlayedId >= this.animationHoldingPen.length) {// for non looping animations
            this.pause();this.playing = false;
        } else {
            this.lastAnimationPlayedId += 1;
            this.animationHoldingPen.sort((a, b) => a['priority'] - b['priority']);//ascending order
            // this.animationHoldingPen.sort((a, b) => b['priority'] - a['priority']);//descending order
            const animationInfoDict = this.animationHoldingPen[this.lastAnimationPlayedId];// play this first one
            console.log('playing animation: ', animationInfoDict['name']);
            // debugger;
            animationInfoDict['animation']();
            this.playing = true
        }
    }

    resetAggregatedAnimations() {this.aggregatedAnimations = function(){};}

    // restartAnimation(){
    //     if (! this.running) {
    //         this.running = true;
    //         this.lastTime = performance.now(); // reset timing
    //         const self = this;
    //         function renderLoop() {
    //             const now = performance.now();
    //             const delta = (now - self.lastTime) / 1000;
    //             self.lastTime = now;

    //             self.animation();
    //             self.renderer.render(self.scene, self.camera);

    //             if (self.running) {
    //                 self.requestId = window.requestAnimationFrame(renderLoop)
    //             }

    //         }
    //         self.requestId = window.requestAnimationFrame(renderLoop);
    //     }
    // }

    pause() {
        this.running = false;
        if (this.requestId != null) {
            // console.log('cancelled Animation Frame<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            window.cancelAnimationFrame(this.requestId);
            this.requestId = null;
        }
    }

    // start() {//shorthand
    //     this.restartAnimation();
    // }
}


export {Animation};