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

/***/ 286:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __values = (this && this.__values) || function(o) {
    var s = typeof Symbol === "function" && Symbol.iterator, m = s && o[s], i = 0;
    if (m) return m.call(o);
    if (o && typeof o.length === "number") return {
        next: function () {
            if (o && i >= o.length) o = void 0;
            return { value: o && o[i++], done: !o };
        }
    };
    throw new TypeError(s ? "Object is not iterable." : "Symbol.iterator is not defined.");
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CenternotConfiguration = exports.filterCenterOver = void 0;
var Configuration_js_1 = __webpack_require__(251);
var TexParser_js_1 = __importDefault(__webpack_require__(193));
var NodeUtil_js_1 = __importDefault(__webpack_require__(748));
var SymbolMap_js_1 = __webpack_require__(871);
var BaseMethods_js_1 = __importDefault(__webpack_require__(360));
new SymbolMap_js_1.CommandMap('centernot', {
    centerOver: 'CenterOver',
    centernot: ['Macro', '\\centerOver{#1}{{\u29F8}}', 1]
}, {
    CenterOver: function (parser, name) {
        var arg = '{' + parser.GetArgument(name) + '}';
        var over = parser.ParseArg(name);
        var base = new TexParser_js_1.default(arg, parser.stack.env, parser.configuration).mml();
        var mml = parser.create('node', 'TeXAtom', [
            new TexParser_js_1.default(arg, parser.stack.env, parser.configuration).mml(),
            parser.create('node', 'mpadded', [
                parser.create('node', 'mpadded', [over], { width: 0, lspace: '-.5width' }),
                parser.create('node', 'mphantom', [base])
            ], { width: 0, lspace: '-.5width' })
        ]);
        parser.configuration.addNode('centerOver', base);
        parser.Push(mml);
    },
    Macro: BaseMethods_js_1.default.Macro
});
function filterCenterOver(_a) {
    var e_1, _b;
    var data = _a.data;
    try {
        for (var _c = __values(data.getList('centerOver')), _d = _c.next(); !_d.done; _d = _c.next()) {
            var base = _d.value;
            var texClass = NodeUtil_js_1.default.getTexClass(base.childNodes[0].childNodes[0]);
            if (texClass !== null) {
                NodeUtil_js_1.default.setProperties(base.parent.parent.parent.parent.parent.parent, { texClass: texClass });
            }
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (_d && !_d.done && (_b = _c.return)) _b.call(_c);
        }
        finally { if (e_1) throw e_1.error; }
    }
}
exports.filterCenterOver = filterCenterOver;
exports.CenternotConfiguration = Configuration_js_1.Configuration.create('centernot', {
    handler: { macro: ['centernot'] },
    postprocessors: [filterCenterOver]
});
//# sourceMappingURL=CenternotConfiguration.js.map

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

/***/ 748:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.NodeUtil["default"];

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

/***/ 193:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.TexParser["default"];

/***/ }),

/***/ 360:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.base.BaseMethods["default"];

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/centernot/CenternotConfiguration.js
var CenternotConfiguration = __webpack_require__(286);
;// CONCATENATED MODULE: ./lib/centernot.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/centernot', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        centernot: {
          CenternotConfiguration: CenternotConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./centernot.js

}();
/******/ })()
;