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

/***/ 646:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ExtpfeilConfiguration = exports.ExtpfeilMethods = void 0;
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var AmsMethods_js_1 = __webpack_require__(939);
var NewcommandUtil_js_1 = __importDefault(__webpack_require__(892));
var NewcommandConfiguration_js_1 = __webpack_require__(417);
var TexError_js_1 = __importDefault(__webpack_require__(402));
exports.ExtpfeilMethods = {};
exports.ExtpfeilMethods.xArrow = AmsMethods_js_1.AmsMethods.xArrow;
exports.ExtpfeilMethods.NewExtArrow = function (parser, name) {
    var cs = parser.GetArgument(name);
    var space = parser.GetArgument(name);
    var chr = parser.GetArgument(name);
    if (!cs.match(/^\\([a-z]+|.)$/i)) {
        throw new TexError_js_1.default('NewextarrowArg1', 'First argument to %1 must be a control sequence name', name);
    }
    if (!space.match(/^(\d+),(\d+)$/)) {
        throw new TexError_js_1.default('NewextarrowArg2', 'Second argument to %1 must be two integers separated by a comma', name);
    }
    if (!chr.match(/^(\d+|0x[0-9A-F]+)$/i)) {
        throw new TexError_js_1.default('NewextarrowArg3', 'Third argument to %1 must be a unicode character number', name);
    }
    cs = cs.substr(1);
    var spaces = space.split(',');
    NewcommandUtil_js_1.default.addMacro(parser, cs, exports.ExtpfeilMethods.xArrow, [parseInt(chr), parseInt(spaces[0]), parseInt(spaces[1])]);
};
new SymbolMap_js_1.CommandMap('extpfeil', {
    xtwoheadrightarrow: ['xArrow', 0x21A0, 12, 16],
    xtwoheadleftarrow: ['xArrow', 0x219E, 17, 13],
    xmapsto: ['xArrow', 0x21A6, 6, 7],
    xlongequal: ['xArrow', 0x003D, 7, 7],
    xtofrom: ['xArrow', 0x21C4, 12, 12],
    Newextarrow: 'NewExtArrow'
}, exports.ExtpfeilMethods);
var init = function (config) {
    NewcommandConfiguration_js_1.NewcommandConfiguration.init(config);
};
exports.ExtpfeilConfiguration = Configuration_js_1.Configuration.create('extpfeil', {
    handler: { macro: ['extpfeil'] },
    init: init
});
//# sourceMappingURL=ExtpfeilConfiguration.js.map

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

/***/ 402:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.TexError["default"];

/***/ }),

/***/ 939:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AmsMethods = MathJax._.input.tex.ams.AmsMethods.AmsMethods;
exports.NEW_OPS = MathJax._.input.tex.ams.AmsMethods.NEW_OPS;

/***/ }),

/***/ 417:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.NewcommandConfiguration = MathJax._.input.tex.newcommand.NewcommandConfiguration.NewcommandConfiguration;

/***/ }),

/***/ 892:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.newcommand.NewcommandUtil["default"];

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
/******/ 		__webpack_modules__[moduleId].call(module.exports, module, module.exports, __webpack_require__);
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
// EXTERNAL MODULE: ../../../../../../js/input/tex/extpfeil/ExtpfeilConfiguration.js
var ExtpfeilConfiguration = __webpack_require__(646);
;// CONCATENATED MODULE: ./lib/extpfeil.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/extpfeil', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        extpfeil: {
          ExtpfeilConfiguration: ExtpfeilConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./extpfeil.js

}();
/******/ })()
;