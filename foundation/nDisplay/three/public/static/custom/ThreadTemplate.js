class ThreadTemplate {
    /*
    This class will store different types of animeTemplateThread like makeAnimeTemplateThread
    */

    pauseUntilCallback(continueFunction, untilCallBack, minimumWaitTime) {
        //console.log('IN pauseUntilCallback')
        //console.log('IN pauseUntilCallback, minimumWaitTime', minimumWaitTime);
        const self = this;
        if (typeof minimumWaitTime == 'number') {
            //console.log('pUC0');
            const timeoutId = setTimeout(function(){
                const intervalId = setInterval(afterPause, 1000);//check every second?
                function afterPause() {
                    if (untilCallBack()) {//must be true
                        continueFunction();
                        clearTimeout(intervalId);
                    }
                }
                clearTimeout(timeoutId);
            }, minimumWaitTime);
        } else {
            const intervalId = setInterval(afterPause, 1000);//check every second?
            function afterPause() {
                if (untilCallBack()) {//must be true
                    continueFunction();
                    clearTimeout(intervalId);

                }
            }
        }
    }
    
    isDictionary(obj) {
        if (obj.__proto__===Object.prototype) {return true}
        return false;
    }
    
    isList(obj) {
        if (obj.__proto__===Array.prototype) {return true}
        return false;
    }
    
    isNonEmptyDictionary(obj) {
        if ( this.isDictionary(obj) && Object.keys(obj).length > 0) { return true}
        return false
    }
    
    isNonEmptyList(obj) {
        if ( this.isList(obj) && obj.length > 0) {return true}
        return false
        
    }
    
    makeAnimeTemplateThread(datum, callbacks) {//note that there are other ways to place the recursion, so that we can get different templates <<<<<<<<<TODO
        /*
        callbacks is a list of 
        {
            //'until_continueRecursor':function(threadSelf,rIdx, preCalInfoDict){},
            'minWaitTime_continueRecursor':function(threadSelf,rIdx, preCalInfoDict){return 10;},
            //'finish_recursor':function(threadSelf,rIdx, preCalInfoDict){},
            // 'continue_recursor':function(threadSelf,rIdx, preCalInfoDict){
            //     const line = preCalInfoDict['line'];
            //     const tagName__taggedWidthDepthIdx = preCalInfoDict['tagName__taggedWidthDepthIdx'];
            //     const widthDepthIdx__dataLinearIdx = preCalInfoDict['widthDepthIdx__dataLinearIdx'];
            //     console.log('hide '+line[widthDepthIdx__dataLinearIdx[tagName__taggedWidthDepthIdx['eq0']]]);//hide previous formula
            //     console.log('display '+line[rIdx]);//show previous formula
            // },
            'continueCallbacks_recursor':[
                standardRevealSolvingStep, 
                // animeSelf.noop, 
                standardHideSolvingStep
            ],
            'until_recursor':function(threadSelf,rIdx, preCalInfoDict){return true;},
            'minWaitTime_recursor':function(threadSelf,rIdx, preCalInfoDict){return 4000;}
        }
        */

        const animeSelf = this; const tagKeyWord = '<<>>';
        const depth__widthOffset = {}; // things on the same level, cannot have the same widthIdx if they are on seperate branches
        //linearise datei and match it to (widthIdx, depthIdx), noting their parent
        //let linearIdx = 0; 
        const line = []; const dataLinearIdx__widthDepthIdx = []; const taggedWidthDepthIdx__tagName = {};
        const stack = [{'key':null, 'value':datum, 'depth':0, 'width':0, 'pDepth':null, 'pWidth':null}];
        function drilldown(sache) {
            let cWidth;
            if (Object.keys(depth__widthOffset).includes(sache['depth'].toString())) {
                cWidth = depth__widthOffset[sache['depth']];
            } else {
                cWidth = 0;
            }
            for (let i=Object.keys(sache['value']).length-1; i>=0; i--) {
                const cKey = Object.keys(sache['value'])[i];
                const cValue = sache['value'][cKey]; const cDepth = sache['depth']+1;
                if ( cKey !== tagKeyWord) {
                    stack.push({'key':cKey, 'value':cValue, 'depth':cDepth, 'width':cWidth, 'pDepth':sache['depth'], 'pWidth':sache['width']})
                }
                cWidth+=1
            }
            depth__widthOffset[sache['depth']] = cWidth
        }
        while (stack.length > 0) {
            const sache = stack.pop();
            // const sache = stack.shift();
            if (animeSelf.isNonEmptyDictionary(sache['value'])) {// only dictionaries can have tagKeyword
                drilldown(sache);//<<<<<<we only keep sache that have tagKeyWord in line?, maybe make drilldown delete all the children tagKeyWord?
                if (tagKeyWord in sache['value']) {// no need to drill down anymore
                    const tagName = sache['value'][tagKeyWord];
                    delete sache['value'][tagKeyWord];
                    taggedWidthDepthIdx__tagName[JSON.stringify([sache['depth'], sache['width']])] = tagName;
                    dataLinearIdx__widthDepthIdx.push(JSON.stringify([sache['depth'], sache['width']]))
                    //keep, but need to remove all children that contains tagKeyWord
                    line.push(sache['value'][tagName]);
                }
                
            } else if (animeSelf.isNonEmptyList(sache['value'])) {
                drilldown(sache);
            }
        }
        const tagName__taggedWidthDepthIdx = Object.fromEntries(Object.entries(taggedWidthDepthIdx__tagName).map(([k, v]) => {return [v, k]}))
        const widthDepthIdx__dataLinearIdx = Object.fromEntries(Object.entries(dataLinearIdx__widthDepthIdx).map(([k, v]) => {return [v, k]}))
        const preCalInfoDict = {
            'line':line, 
            'dataLinearIdx__widthDepthIdx':dataLinearIdx__widthDepthIdx, 
            'taggedWidthDepthIdx__tagName':taggedWidthDepthIdx__tagName,
            'tagName__taggedWidthDepthIdx':tagName__taggedWidthDepthIdx, 
            'widthDepthIdx__dataLinearIdx':widthDepthIdx__dataLinearIdx
        }
        // console.log('preCalInfoDict')
        // console.log(preCalInfoDict)
        // debugger
        //create getCallback to handle defaults when the callback needed is not there
        // console.log('taggedWidthDepthIdx__tagName', taggedWidthDepthIdx__tagName)
        // console.log('dataLinearIdx__widthDepthIdx', dataLinearIdx__widthDepthIdx)
        // debugger
        function getCallback(rIdx, callbackName) {
            const name__callback = callbacks[taggedWidthDepthIdx__tagName[dataLinearIdx__widthDepthIdx[rIdx]]]
            // debugger
            if (name__callback!==undefined && callbackName in name__callback) {
                return name__callback[callbackName]
            } else {
                switch (callbackName) {//for returning blank functions
                    case 'until_continueRecursor':
                        return function(...any){return true;}
                    case 'minWaitTime_continueRecursor':
                        return function(...any){return 0;}
                    case 'finish_recursor':
                        return function(...any){}
                    case 'continue_recursor':
                        return function(...any){}
                    case 'continueCallbacks_recursor':
                        return []
                    case 'until_recursor':
                        return function(...any){return true;}
                    case 'minWaitTime_recursor':
                        return function(...any){return 0;}
                }
            }
        }
        //
        function continueRecursor(threadSelf, cIdx, rIdx, preCalInfoDict, recursorFunction, continueCallbacks) {//like a display and a hide
            if (cIdx >= continueCallbacks.length) {
                // allow to do something else here? beware, it will be async<<<<<<<<<<<<<<<<<<<<<<<<<
                recursorFunction()
                // allow to do something else here? beware, it will be async<<<<<<<<<<<<<<<<<<<<<<<<<
                return
            }
            const continueCallback = continueCallbacks[cIdx]
            continueCallback(threadSelf, rIdx, preCalInfoDict);
            animeSelf.pauseUntilCallback(
                function() {//continue
                    // allow to do something else here? beware, it will be async<<<<<<<<<<<<<<<<<<<<<<<<<
                    continueRecursor(threadSelf, cIdx+1, rIdx, preCalInfoDict, recursorFunction, continueCallbacks);//play each continue function 1 by 1
                    // allow to do something else here? beware, it will be async<<<<<<<<<<<<<<<<<<<<<<<<<
                }, 
                function() {//until
                    return getCallback(cIdx, 'until_continueRecursor')(threadSelf, rIdx, preCalInfoDict);
                },
                getCallback(cIdx, 'minWaitTime_continueRecursor')(threadSelf, rIdx, preCalInfoDict)
            );
            // allow to do something else here? beware, it will be async<<<<<<<<<<<<<<<<<<<<<<<<<
        }
        //the playing of the animation
        function recursor(rIdx, preCalInfoDict) {
            if (rIdx >= line.length) {
                // allow to do something else here? beware, it will be async<<<<<<<<<<<<<<<<<<<<<<<<<
                getCallback(rIdx-1, 'finish_recursor')(this, rIdx-1, preCalInfoDict);//return something
                // allow to do something else here? beware, it will be async<<<<<<<<<<<<<<<<<<<<<<<<<
                return 
            }
            getCallback(rIdx, 'continue_recursor')(this, rIdx, preCalInfoDict);//beware it will run before the pauseUntilCallback.
            animeSelf.pauseUntilCallback(
                function() {//continue
                    const recursorFunction = function(){recursor(rIdx+1, preCalInfoDict)}
                    const continueCallbacks = getCallback(rIdx, 'continueCallbacks_recursor');//there should be many callbacks, and each one requires a pauseUntilCallback?
                    continueRecursor(this, 0, rIdx, preCalInfoDict, recursorFunction, continueCallbacks)
                },
                function() {//until
                    return getCallback(rIdx, 'until_recursor')(this, rIdx, preCalInfoDict);
                },
                getCallback(rIdx, 'minWaitTime_recursor')(this, rIdx, preCalInfoDict)
            );
        }
        return function(){
            //console.log('starting animation')
            recursor(0, preCalInfoDict)
        }
    }
}


export {ThreadTemplate};