class Animation {
    
    constructor(scene, camera, renderer){
        this.scene = scene; this.camera = camera; this.renderer = renderer;
        this.aggregatedAnimations = function(){}; // this does not contain the 'this.renderer.render(this.scene, this.camera)'
        this.animation = function(){};
    }

    appendAction(action){//action aggregator
        //Copied from ChatGPT

        //Capture the current animation function in a local variable
        const oldAnimation = this.aggregatedAnimations.bind(this);

        this.aggregatedAnimations = function() {
            oldAnimation(); action();
        }
        const self = this;
        this.animation = function(){
            self.aggregatedAnimations(); 
            self.renderer.render(self.scene, self.camera);
        }
    };

    resetAggregatedAnimations() {this.aggregatedAnimations = function(){};}

    restartAnimation(){
        this.renderer.setAnimationLoop(this.animation)
    }
}

export {Animation};