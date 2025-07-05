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

/***/ 986:
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
exports.BoldsymbolConfiguration = exports.rewriteBoldTokens = exports.createBoldToken = exports.BoldsymbolMethods = void 0;
var Configuration_js_1 = __webpack_require__(251);
var NodeUtil_js_1 = __importDefault(__webpack_require__(748));
var TexConstants_js_1 = __webpack_require__(108);
var SymbolMap_js_1 = __webpack_require__(871);
var NodeFactory_js_1 = __webpack_require__(348);
var BOLDVARIANT = {};
BOLDVARIANT[TexConstants_js_1.TexConstant.Variant.NORMAL] = TexConstants_js_1.TexConstant.Variant.BOLD;
BOLDVARIANT[TexConstants_js_1.TexConstant.Variant.ITALIC] = TexConstants_js_1.TexConstant.Variant.BOLDITALIC;
BOLDVARIANT[TexConstants_js_1.TexConstant.Variant.FRAKTUR] = TexConstants_js_1.TexConstant.Variant.BOLDFRAKTUR;
BOLDVARIANT[TexConstants_js_1.TexConstant.Variant.SCRIPT] = TexConstants_js_1.TexConstant.Variant.BOLDSCRIPT;
BOLDVARIANT[TexConstants_js_1.TexConstant.Variant.SANSSERIF] = TexConstants_js_1.TexConstant.Variant.BOLDSANSSERIF;
BOLDVARIANT['-tex-calligraphic'] = '-tex-bold-calligraphic';
BOLDVARIANT['-tex-oldstyle'] = '-tex-bold-oldstyle';
BOLDVARIANT['-tex-mathit'] = TexConstants_js_1.TexConstant.Variant.BOLDITALIC;
exports.BoldsymbolMethods = {};
exports.BoldsymbolMethods.Boldsymbol = function (parser, name) {
    var boldsymbol = parser.stack.env['boldsymbol'];
    parser.stack.env['boldsymbol'] = true;
    var mml = parser.ParseArg(name);
    parser.stack.env['boldsymbol'] = boldsymbol;
    parser.Push(mml);
};
new SymbolMap_js_1.CommandMap('boldsymbol', { boldsymbol: 'Boldsymbol' }, exports.BoldsymbolMethods);
function createBoldToken(factory, kind, def, text) {
    var token = NodeFactory_js_1.NodeFactory.createToken(factory, kind, def, text);
    if (kind !== 'mtext' &&
        factory.configuration.parser.stack.env['boldsymbol']) {
        NodeUtil_js_1.default.setProperty(token, 'fixBold', true);
        factory.configuration.addNode('fixBold', token);
    }
    return token;
}
exports.createBoldToken = createBoldToken;
function rewriteBoldTokens(arg) {
    var e_1, _a;
    try {
        for (var _b = __values(arg.data.getList('fixBold')), _c = _b.next(); !_c.done; _c = _b.next()) {
            var node = _c.value;
            if (NodeUtil_js_1.default.getProperty(node, 'fixBold')) {
                var variant = NodeUtil_js_1.default.getAttribute(node, 'mathvariant');
                if (variant == null) {
                    NodeUtil_js_1.default.setAttribute(node, 'mathvariant', TexConstants_js_1.TexConstant.Variant.BOLD);
                }
                else {
                    NodeUtil_js_1.default.setAttribute(node, 'mathvariant', BOLDVARIANT[variant] || variant);
                }
                NodeUtil_js_1.default.removeProperties(node, 'fixBold');
            }
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
        }
        finally { if (e_1) throw e_1.error; }
    }
}
exports.rewriteBoldTokens = rewriteBoldTokens;
exports.BoldsymbolConfiguration = Configuration_js_1.Configuration.create('boldsymbol', {
    handler: { macro: ['boldsymbol'] },
    nodes: { 'token': createBoldToken },
    postprocessors: [rewriteBoldTokens]
});
//# sourceMappingURL=BoldsymbolConfiguration.js.map

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

/***/ 348:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.NodeFactory = MathJax._.input.tex.NodeFactory.NodeFactory;

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/boldsymbol/BoldsymbolConfiguration.js
var BoldsymbolConfiguration = __webpack_require__(986);
;// CONCATENATED MODULE: ./lib/boldsymbol.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/boldsymbol', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        boldsymbol: {
          BoldsymbolConfiguration: BoldsymbolConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./boldsymbol.js

}();
/******/ })()
;