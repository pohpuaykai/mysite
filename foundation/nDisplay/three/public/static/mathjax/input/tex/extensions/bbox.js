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

/***/ 133:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BboxConfiguration = exports.BboxMethods = void 0;
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var TexError_js_1 = __importDefault(__webpack_require__(402));
exports.BboxMethods = {};
exports.BboxMethods.BBox = function (parser, name) {
    var bbox = parser.GetBrackets(name, '');
    var math = parser.ParseArg(name);
    var parts = bbox.split(/,/);
    var def, background, style;
    for (var i = 0, m = parts.length; i < m; i++) {
        var part = parts[i].trim();
        var match = part.match(/^(\.\d+|\d+(\.\d*)?)(pt|em|ex|mu|px|in|cm|mm)$/);
        if (match) {
            if (def) {
                throw new TexError_js_1.default('MultipleBBoxProperty', '%1 specified twice in %2', 'Padding', name);
            }
            var pad = BBoxPadding(match[1] + match[3]);
            if (pad) {
                def = {
                    height: '+' + pad,
                    depth: '+' + pad,
                    lspace: pad,
                    width: '+' + (2 * parseInt(match[1], 10)) + match[3]
                };
            }
        }
        else if (part.match(/^([a-z0-9]+|\#[0-9a-f]{6}|\#[0-9a-f]{3})$/i)) {
            if (background) {
                throw new TexError_js_1.default('MultipleBBoxProperty', '%1 specified twice in %2', 'Background', name);
            }
            background = part;
        }
        else if (part.match(/^[-a-z]+:/i)) {
            if (style) {
                throw new TexError_js_1.default('MultipleBBoxProperty', '%1 specified twice in %2', 'Style', name);
            }
            style = BBoxStyle(part);
        }
        else if (part !== '') {
            throw new TexError_js_1.default('InvalidBBoxProperty', '"%1" doesn\'t look like a color, a padding dimension, or a style', part);
        }
    }
    if (def) {
        math = parser.create('node', 'mpadded', [math], def);
    }
    if (background || style) {
        def = {};
        if (background) {
            Object.assign(def, { mathbackground: background });
        }
        if (style) {
            Object.assign(def, { style: style });
        }
        math = parser.create('node', 'mstyle', [math], def);
    }
    parser.Push(math);
};
var BBoxStyle = function (styles) {
    return styles;
};
var BBoxPadding = function (pad) {
    return pad;
};
new SymbolMap_js_1.CommandMap('bbox', { bbox: 'BBox' }, exports.BboxMethods);
exports.BboxConfiguration = Configuration_js_1.Configuration.create('bbox', { handler: { macro: ['bbox'] } });
//# sourceMappingURL=BboxConfiguration.js.map

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/bbox/BboxConfiguration.js
var BboxConfiguration = __webpack_require__(133);
;// CONCATENATED MODULE: ./lib/bbox.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/bbox', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        bbox: {
          BboxConfiguration: BboxConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./bbox.js

}();
/******/ })()
;