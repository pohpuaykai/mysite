class Animation {
    
    constructor(scene, camera, renderer){
        this.scene = scene; this.camera = camera; this.renderer = renderer;
        //Player functionalities like run, pause... (Courtesy of ChatGPT)
        this.requestId = null; this.running = false; this.lastTime = 0;

        //for sticking animations together in a timeline.
        this.aggregatedAnimations = function(){}; // this does not contain the 'this.renderer.render(this.scene, this.camera)'
        this.animation = function(){};
        // this.clock = new THREE.Clock();
        // this.delta = this.clock.getDelta();//time since last frame (Courtesy of ChatGPT)
    }

    appendAction(action){//action aggregator
        //Copied from ChatGPT

        //Capture the current animation function in a local variable
        const oldAnimation = this.aggregatedAnimations.bind(this);

        this.aggregatedAnimations = function() {
            oldAnimation(); action();
        }
        // const self = this;
        this.animation = this.aggregatedAnimations
    };

    resetAggregatedAnimations() {this.aggregatedAnimations = function(){};}

    restartAnimation(){
        if (! this.running) {
            this.running = true;
            this.lastTime = performance.now(); // reset timing
            const self = this;
            function renderLoop() {
                const now = performance.now();
                const delta = (now - self.lastTime) / 1000;
                self.lastTime = now;

                self.animation();
                self.renderer.render(self.scene, self.camera);

                if (self.running) {
                    self.requestId = window.requestAnimationFrame(renderLoop)
                }

            }
            self.requestId = window.requestAnimationFrame(renderLoop);
        }
    }

    pause() {
        this.running = false;
        if (this.requestId != null) {
            // console.log('cancelled Animation Frame<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            window.cancelAnimationFrame(this.requestId);
            this.requestId = null;
        }

    }
    start() {//shorthand
        this.restartAnimation();
    }
}


export {Animation};