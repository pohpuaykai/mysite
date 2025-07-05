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

/***/ 769:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AmsCdConfiguration = void 0;
var Configuration_js_1 = __webpack_require__(251);
__webpack_require__(704);
exports.AmsCdConfiguration = Configuration_js_1.Configuration.create('amscd', {
    handler: {
        character: ['amscd_special'],
        macro: ['amscd_macros'],
        environment: ['amscd_environment']
    },
    options: {
        amscd: {
            colspace: '5pt',
            rowspace: '5pt',
            harrowsize: '2.75em',
            varrowsize: '1.75em',
            hideHorizontalLabels: false
        }
    }
});
//# sourceMappingURL=AmsCdConfiguration.js.map

/***/ }),

/***/ 704:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var sm = __importStar(__webpack_require__(871));
var ParseMethods_js_1 = __importDefault(__webpack_require__(945));
var AmsCdMethods_js_1 = __importDefault(__webpack_require__(834));
new sm.EnvironmentMap('amscd_environment', ParseMethods_js_1.default.environment, { CD: 'CD' }, AmsCdMethods_js_1.default);
new sm.CommandMap('amscd_macros', {
    minCDarrowwidth: 'minCDarrowwidth',
    minCDarrowheight: 'minCDarrowheight',
}, AmsCdMethods_js_1.default);
new sm.MacroMap('amscd_special', { '@': 'arrow' }, AmsCdMethods_js_1.default);
//# sourceMappingURL=AmsCdMappings.js.map

/***/ }),

/***/ 834:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var TexParser_js_1 = __importDefault(__webpack_require__(193));
var BaseConfiguration_js_1 = __webpack_require__(379);
var MmlNode_js_1 = __webpack_require__(801);
var NodeUtil_js_1 = __importDefault(__webpack_require__(748));
var AmsCdMethods = {};
AmsCdMethods.CD = function (parser, begin) {
    parser.Push(begin);
    var item = parser.itemFactory.create('array');
    var options = parser.configuration.options.amscd;
    item.setProperties({
        minw: parser.stack.env.CD_minw || options.harrowsize,
        minh: parser.stack.env.CD_minh || options.varrowsize
    });
    item.arraydef = {
        columnalign: 'center',
        columnspacing: options.colspace,
        rowspacing: options.rowspace,
        displaystyle: true
    };
    return item;
};
AmsCdMethods.arrow = function (parser, name) {
    var c = parser.string.charAt(parser.i);
    if (!c.match(/[><VA.|=]/)) {
        return (0, BaseConfiguration_js_1.Other)(parser, name);
    }
    else {
        parser.i++;
    }
    var first = parser.stack.Top();
    if (!first.isKind('array') || first.Size()) {
        AmsCdMethods.cell(parser, name);
        first = parser.stack.Top();
    }
    var top = first;
    var arrowRow = ((top.table.length % 2) === 1);
    var n = (top.row.length + (arrowRow ? 0 : 1)) % 2;
    while (n) {
        AmsCdMethods.cell(parser, name);
        n--;
    }
    var mml;
    var hdef = { minsize: top.getProperty('minw'), stretchy: true }, vdef = { minsize: top.getProperty('minh'),
        stretchy: true, symmetric: true, lspace: 0, rspace: 0 };
    if (c === '.') {
    }
    else if (c === '|') {
        mml = parser.create('token', 'mo', vdef, '\u2225');
    }
    else if (c === '=') {
        mml = parser.create('token', 'mo', hdef, '=');
    }
    else {
        var arrow = {
            '>': '\u2192', '<': '\u2190', 'V': '\u2193', 'A': '\u2191'
        }[c];
        var a = parser.GetUpTo(name + c, c);
        var b = parser.GetUpTo(name + c, c);
        if (c === '>' || c === '<') {
            mml = parser.create('token', 'mo', hdef, arrow);
            if (!a) {
                a = '\\kern ' + top.getProperty('minw');
            }
            if (a || b) {
                var pad = { width: '+.67em', lspace: '.33em' };
                mml = parser.create('node', 'munderover', [mml]);
                if (a) {
                    var nodeA = new TexParser_js_1.default(a, parser.stack.env, parser.configuration).mml();
                    var mpadded = parser.create('node', 'mpadded', [nodeA], pad);
                    NodeUtil_js_1.default.setAttribute(mpadded, 'voffset', '.1em');
                    NodeUtil_js_1.default.setChild(mml, mml.over, mpadded);
                }
                if (b) {
                    var nodeB = new TexParser_js_1.default(b, parser.stack.env, parser.configuration).mml();
                    NodeUtil_js_1.default.setChild(mml, mml.under, parser.create('node', 'mpadded', [nodeB], pad));
                }
                if (parser.configuration.options.amscd.hideHorizontalLabels) {
                    mml = parser.create('node', 'mpadded', mml, { depth: 0, height: '.67em' });
                }
            }
        }
        else {
            var arrowNode = parser.create('token', 'mo', vdef, arrow);
            mml = arrowNode;
            if (a || b) {
                mml = parser.create('node', 'mrow');
                if (a) {
                    NodeUtil_js_1.default.appendChildren(mml, [new TexParser_js_1.default('\\scriptstyle\\llap{' + a + '}', parser.stack.env, parser.configuration).mml()]);
                }
                arrowNode.texClass = MmlNode_js_1.TEXCLASS.ORD;
                NodeUtil_js_1.default.appendChildren(mml, [arrowNode]);
                if (b) {
                    NodeUtil_js_1.default.appendChildren(mml, [new TexParser_js_1.default('\\scriptstyle\\rlap{' + b + '}', parser.stack.env, parser.configuration).mml()]);
                }
            }
        }
    }
    if (mml) {
        parser.Push(mml);
    }
    AmsCdMethods.cell(parser, name);
};
AmsCdMethods.cell = function (parser, name) {
    var top = parser.stack.Top();
    if ((top.table || []).length % 2 === 0 && (top.row || []).length === 0) {
        parser.Push(parser.create('node', 'mpadded', [], { height: '8.5pt', depth: '2pt' }));
    }
    parser.Push(parser.itemFactory.create('cell').setProperties({ isEntry: true, name: name }));
};
AmsCdMethods.minCDarrowwidth = function (parser, name) {
    parser.stack.env.CD_minw = parser.GetDimen(name);
};
AmsCdMethods.minCDarrowheight = function (parser, name) {
    parser.stack.env.CD_minh = parser.GetDimen(name);
};
exports["default"] = AmsCdMethods;
//# sourceMappingURL=AmsCdMethods.js.map

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

/***/ 801:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.TEXCLASS = MathJax._.core.MmlTree.MmlNode.TEXCLASS;
exports.TEXCLASSNAMES = MathJax._.core.MmlTree.MmlNode.TEXCLASSNAMES;
exports.indentAttributes = MathJax._.core.MmlTree.MmlNode.indentAttributes;
exports.AbstractMmlNode = MathJax._.core.MmlTree.MmlNode.AbstractMmlNode;
exports.AbstractMmlTokenNode = MathJax._.core.MmlTree.MmlNode.AbstractMmlTokenNode;
exports.AbstractMmlLayoutNode = MathJax._.core.MmlTree.MmlNode.AbstractMmlLayoutNode;
exports.AbstractMmlBaseNode = MathJax._.core.MmlTree.MmlNode.AbstractMmlBaseNode;
exports.AbstractMmlEmptyNode = MathJax._.core.MmlTree.MmlNode.AbstractMmlEmptyNode;
exports.TextNode = MathJax._.core.MmlTree.MmlNode.TextNode;
exports.XMLNode = MathJax._.core.MmlTree.MmlNode.XMLNode;

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

/***/ 945:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.ParseMethods["default"];

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

/***/ 379:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Other = MathJax._.input.tex.base.BaseConfiguration.Other;
exports.BaseTags = MathJax._.input.tex.base.BaseConfiguration.BaseTags;
exports.BaseConfiguration = MathJax._.input.tex.base.BaseConfiguration.BaseConfiguration;

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/amscd/AmsCdConfiguration.js
var AmsCdConfiguration = __webpack_require__(769);
// EXTERNAL MODULE: ../../../../../../js/input/tex/amscd/AmsCdMethods.js
var AmsCdMethods = __webpack_require__(834);
;// CONCATENATED MODULE: ./lib/amscd.js





if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/amscd', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        amscd: {
          AmsCdConfiguration: AmsCdConfiguration,
          AmsCdMethods: AmsCdMethods
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./amscd.js

}();
/******/ })()
;