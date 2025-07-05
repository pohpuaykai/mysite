/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 667:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;

__webpack_unused_export__ = ({ value: true });
exports.q = void 0;
exports.q = '3.2.2';
//# sourceMappingURL=version.js.map

/***/ }),

/***/ 927:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.UpgreekConfiguration = void 0;
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var TexConstants_js_1 = __webpack_require__(108);
function mathchar0miNormal(parser, mchar) {
    var def = mchar.attributes || {};
    def.mathvariant = TexConstants_js_1.TexConstant.Variant.NORMAL;
    var node = parser.create('token', 'mi', def, mchar.char);
    parser.Push(node);
}
new SymbolMap_js_1.CharacterMap('upgreek', mathchar0miNormal, {
    upalpha: '\u03B1',
    upbeta: '\u03B2',
    upgamma: '\u03B3',
    updelta: '\u03B4',
    upepsilon: '\u03F5',
    upzeta: '\u03B6',
    upeta: '\u03B7',
    uptheta: '\u03B8',
    upiota: '\u03B9',
    upkappa: '\u03BA',
    uplambda: '\u03BB',
    upmu: '\u03BC',
    upnu: '\u03BD',
    upxi: '\u03BE',
    upomicron: '\u03BF',
    uppi: '\u03C0',
    uprho: '\u03C1',
    upsigma: '\u03C3',
    uptau: '\u03C4',
    upupsilon: '\u03C5',
    upphi: '\u03D5',
    upchi: '\u03C7',
    uppsi: '\u03C8',
    upomega: '\u03C9',
    upvarepsilon: '\u03B5',
    upvartheta: '\u03D1',
    upvarpi: '\u03D6',
    upvarrho: '\u03F1',
    upvarsigma: '\u03C2',
    upvarphi: '\u03C6',
    Upgamma: '\u0393',
    Updelta: '\u0394',
    Uptheta: '\u0398',
    Uplambda: '\u039B',
    Upxi: '\u039E',
    Uppi: '\u03A0',
    Upsigma: '\u03A3',
    Upupsilon: '\u03A5',
    Upphi: '\u03A6',
    Uppsi: '\u03A8',
    Upomega: '\u03A9'
});
exports.UpgreekConfiguration = Configuration_js_1.Configuration.create('upgreek', {
    handler: { macro: ['upgreek'] },
});
//# sourceMappingURL=UpgreekConfiguration.js.map

/***/ }),

/***/ 955:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;


__webpack_unused_export__ = ({
  value: true
});
__webpack_unused_export__ = MathJax._.components.global.isObject;
__webpack_unused_export__ = MathJax._.components.global.combineConfig;
__webpack_unused_export__ = MathJax._.components.global.combineDefaults;
exports.r8 = MathJax._.components.global.combineWithMathJax;
__webpack_unused_export__ = MathJax._.components.global.MathJax;

/***/ }),

/***/ 251:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Configuration = MathJax._.input.tex.Configuration.Configuration;
exports.ConfigurationHandler = MathJax._.input.tex.Configuration.ConfigurationHandler;
exports.ParserConfiguration = MathJax._.input.tex.Configuration.ParserConfiguration;

/***/ }),

/***/ 871:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.parseResult = MathJax._.input.tex.SymbolMap.parseResult;
exports.AbstractSymbolMap = MathJax._.input.tex.SymbolMap.AbstractSymbolMap;
exports.RegExpMap = MathJax._.input.tex.SymbolMap.RegExpMap;
exports.AbstractParseMap = MathJax._.input.tex.SymbolMap.AbstractParseMap;
exports.CharacterMap = MathJax._.input.tex.SymbolMap.CharacterMap;
exports.DelimiterMap = MathJax._.input.tex.SymbolMap.DelimiterMap;
exports.MacroMap = MathJax._.input.tex.SymbolMap.MacroMap;
exports.CommandMap = MathJax._.input.tex.SymbolMap.CommandMap;
exports.EnvironmentMap = MathJax._.input.tex.SymbolMap.EnvironmentMap;

/***/ }),

/***/ 108:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.TexConstant = MathJax._.input.tex.TexConstants.TexConstant;

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
!function() {

// EXTERNAL MODULE: ../../../../core/lib/components/global.js
var global = __webpack_require__(955);
// EXTERNAL MODULE: ../../../../../../js/components/version.js
var version = __webpack_require__(667);
// EXTERNAL MODULE: ../../../../../../js/input/tex/upgreek/UpgreekConfiguration.js
var UpgreekConfiguration = __webpack_require__(927);
;// CONCATENATED MODULE: ./lib/upgreek.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/upgreek', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        upgreek: {
          UpgreekConfiguration: UpgreekConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./upgreek.js

}();
/******/ })()
;