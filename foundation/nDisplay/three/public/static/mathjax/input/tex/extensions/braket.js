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

/***/ 243:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BraketConfiguration = void 0;
var Configuration_js_1 = __webpack_require__(251);
var BraketItems_js_1 = __webpack_require__(519);
__webpack_require__(299);
exports.BraketConfiguration = Configuration_js_1.Configuration.create('braket', {
    handler: {
        character: ['Braket-characters'],
        macro: ['Braket-macros']
    },
    items: (_a = {},
        _a[BraketItems_js_1.BraketItem.prototype.kind] = BraketItems_js_1.BraketItem,
        _a)
});
//# sourceMappingURL=BraketConfiguration.js.map

/***/ }),

/***/ 519:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BraketItem = void 0;
var StackItem_js_1 = __webpack_require__(76);
var MmlNode_js_1 = __webpack_require__(801);
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var BraketItem = (function (_super) {
    __extends(BraketItem, _super);
    function BraketItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(BraketItem.prototype, "kind", {
        get: function () {
            return 'braket';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(BraketItem.prototype, "isOpen", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    BraketItem.prototype.checkItem = function (item) {
        if (item.isKind('close')) {
            return [[this.factory.create('mml', this.toMml())], true];
        }
        if (item.isKind('mml')) {
            this.Push(item.toMml());
            if (this.getProperty('single')) {
                return [[this.toMml()], true];
            }
            return StackItem_js_1.BaseItem.fail;
        }
        return _super.prototype.checkItem.call(this, item);
    };
    BraketItem.prototype.toMml = function () {
        var inner = _super.prototype.toMml.call(this);
        var open = this.getProperty('open');
        var close = this.getProperty('close');
        if (this.getProperty('stretchy')) {
            return ParseUtil_js_1.default.fenced(this.factory.configuration, open, inner, close);
        }
        var attrs = { fence: true, stretchy: false, symmetric: true, texClass: MmlNode_js_1.TEXCLASS.OPEN };
        var openNode = this.create('token', 'mo', attrs, open);
        attrs.texClass = MmlNode_js_1.TEXCLASS.CLOSE;
        var closeNode = this.create('token', 'mo', attrs, close);
        var mrow = this.create('node', 'mrow', [openNode, inner, closeNode], { open: open, close: close, texClass: MmlNode_js_1.TEXCLASS.INNER });
        return mrow;
    };
    return BraketItem;
}(StackItem_js_1.BaseItem));
exports.BraketItem = BraketItem;
//# sourceMappingURL=BraketItems.js.map

/***/ }),

/***/ 299:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var SymbolMap_js_1 = __webpack_require__(871);
var BraketMethods_js_1 = __importDefault(__webpack_require__(277));
new SymbolMap_js_1.CommandMap('Braket-macros', {
    bra: ['Macro', '{\\langle {#1} \\vert}', 1],
    ket: ['Macro', '{\\vert {#1} \\rangle}', 1],
    braket: ['Braket', '\u27E8', '\u27E9', false, Infinity],
    'set': ['Braket', '{', '}', false, 1],
    Bra: ['Macro', '{\\left\\langle {#1} \\right\\vert}', 1],
    Ket: ['Macro', '{\\left\\vert {#1} \\right\\rangle}', 1],
    Braket: ['Braket', '\u27E8', '\u27E9', true, Infinity],
    Set: ['Braket', '{', '}', true, 1],
    ketbra: ['Macro', '{\\vert {#1} \\rangle\\langle {#2} \\vert}', 2],
    Ketbra: ['Macro', '{\\left\\vert {#1} \\right\\rangle\\left\\langle {#2} \\right\\vert}', 2],
    '|': 'Bar'
}, BraketMethods_js_1.default);
new SymbolMap_js_1.MacroMap('Braket-characters', {
    '|': 'Bar'
}, BraketMethods_js_1.default);
//# sourceMappingURL=BraketMappings.js.map

/***/ }),

/***/ 277:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var BaseMethods_js_1 = __importDefault(__webpack_require__(360));
var MmlNode_js_1 = __webpack_require__(801);
var TexError_js_1 = __importDefault(__webpack_require__(402));
var BraketMethods = {};
BraketMethods.Macro = BaseMethods_js_1.default.Macro;
BraketMethods.Braket = function (parser, _name, open, close, stretchy, barmax) {
    var next = parser.GetNext();
    if (next === '') {
        throw new TexError_js_1.default('MissingArgFor', 'Missing argument for %1', parser.currentCS);
    }
    var single = true;
    if (next === '{') {
        parser.i++;
        single = false;
    }
    parser.Push(parser.itemFactory.create('braket')
        .setProperties({ barmax: barmax, barcount: 0, open: open,
        close: close, stretchy: stretchy, single: single }));
};
BraketMethods.Bar = function (parser, name) {
    var c = name === '|' ? '|' : '\u2225';
    var top = parser.stack.Top();
    if (top.kind !== 'braket' ||
        top.getProperty('barcount') >= top.getProperty('barmax')) {
        var mml = parser.create('token', 'mo', { texClass: MmlNode_js_1.TEXCLASS.ORD, stretchy: false }, c);
        parser.Push(mml);
        return;
    }
    if (c === '|' && parser.GetNext() === '|') {
        parser.i++;
        c = '\u2225';
    }
    var stretchy = top.getProperty('stretchy');
    if (!stretchy) {
        var node_1 = parser.create('token', 'mo', { stretchy: false, braketbar: true }, c);
        parser.Push(node_1);
        return;
    }
    var node = parser.create('node', 'TeXAtom', [], { texClass: MmlNode_js_1.TEXCLASS.CLOSE });
    parser.Push(node);
    top.setProperty('barcount', top.getProperty('barcount') + 1);
    node = parser.create('token', 'mo', { stretchy: true, braketbar: true }, c);
    parser.Push(node);
    node = parser.create('node', 'TeXAtom', [], { texClass: MmlNode_js_1.TEXCLASS.OPEN });
    parser.Push(node);
};
exports["default"] = BraketMethods;
//# sourceMappingURL=BraketMethods.js.map

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

/***/ 398:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.ParseUtil["default"];

/***/ }),

/***/ 76:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlStack = MathJax._.input.tex.StackItem.MmlStack;
exports.BaseItem = MathJax._.input.tex.StackItem.BaseItem;

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/braket/BraketConfiguration.js
var BraketConfiguration = __webpack_require__(243);
// EXTERNAL MODULE: ../../../../../../js/input/tex/braket/BraketItems.js
var BraketItems = __webpack_require__(519);
// EXTERNAL MODULE: ../../../../../../js/input/tex/braket/BraketMethods.js
var BraketMethods = __webpack_require__(277);
;// CONCATENATED MODULE: ./lib/braket.js






if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/braket', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        braket: {
          BraketConfiguration: BraketConfiguration,
          BraketItems: BraketItems,
          BraketMethods: BraketMethods
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./braket.js

}();
/******/ })()
;