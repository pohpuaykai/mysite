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

/***/ 530:
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
var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CasesConfiguration = exports.CasesMethods = exports.CasesTags = exports.CasesBeginItem = void 0;
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var BaseMethods_js_1 = __importDefault(__webpack_require__(360));
var TexError_js_1 = __importDefault(__webpack_require__(402));
var BaseItems_js_1 = __webpack_require__(935);
var AmsConfiguration_js_1 = __webpack_require__(379);
var EmpheqUtil_js_1 = __webpack_require__(446);
var CasesBeginItem = (function (_super) {
    __extends(CasesBeginItem, _super);
    function CasesBeginItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(CasesBeginItem.prototype, "kind", {
        get: function () {
            return 'cases-begin';
        },
        enumerable: false,
        configurable: true
    });
    CasesBeginItem.prototype.checkItem = function (item) {
        if (item.isKind('end') && item.getName() === this.getName()) {
            if (this.getProperty('end')) {
                this.setProperty('end', false);
                return [[], true];
            }
        }
        return _super.prototype.checkItem.call(this, item);
    };
    return CasesBeginItem;
}(BaseItems_js_1.BeginItem));
exports.CasesBeginItem = CasesBeginItem;
var CasesTags = (function (_super) {
    __extends(CasesTags, _super);
    function CasesTags() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.subcounter = 0;
        return _this;
    }
    CasesTags.prototype.start = function (env, taggable, defaultTags) {
        this.subcounter = 0;
        _super.prototype.start.call(this, env, taggable, defaultTags);
    };
    CasesTags.prototype.autoTag = function () {
        if (this.currentTag.tag != null)
            return;
        if (this.currentTag.env === 'subnumcases') {
            if (this.subcounter === 0)
                this.counter++;
            this.subcounter++;
            this.tag(this.formatNumber(this.counter, this.subcounter), false);
        }
        else {
            if (this.subcounter === 0 || this.currentTag.env !== 'numcases-left')
                this.counter++;
            this.tag(this.formatNumber(this.counter), false);
        }
    };
    CasesTags.prototype.formatNumber = function (n, m) {
        if (m === void 0) { m = null; }
        return n.toString() + (m === null ? '' : String.fromCharCode(0x60 + m));
    };
    return CasesTags;
}(AmsConfiguration_js_1.AmsTags));
exports.CasesTags = CasesTags;
exports.CasesMethods = {
    NumCases: function (parser, begin) {
        if (parser.stack.env.closing === begin.getName()) {
            delete parser.stack.env.closing;
            parser.Push(parser.itemFactory.create('end').setProperty('name', begin.getName()));
            var cases = parser.stack.Top();
            var table = cases.Last;
            var original = ParseUtil_js_1.default.copyNode(table, parser);
            var left = cases.getProperty('left');
            EmpheqUtil_js_1.EmpheqUtil.left(table, original, left + '\\empheqlbrace\\,', parser, 'numcases-left');
            parser.Push(parser.itemFactory.create('end').setProperty('name', begin.getName()));
            return null;
        }
        else {
            var left = parser.GetArgument('\\begin{' + begin.getName() + '}');
            begin.setProperty('left', left);
            var array = BaseMethods_js_1.default.EqnArray(parser, begin, true, true, 'll');
            array.arraydef.displaystyle = false;
            array.arraydef.rowspacing = '.2em';
            array.setProperty('numCases', true);
            parser.Push(begin);
            return array;
        }
    },
    Entry: function (parser, name) {
        if (!parser.stack.Top().getProperty('numCases')) {
            return BaseMethods_js_1.default.Entry(parser, name);
        }
        parser.Push(parser.itemFactory.create('cell').setProperties({ isEntry: true, name: name }));
        var tex = parser.string;
        var braces = 0, i = parser.i, m = tex.length;
        while (i < m) {
            var c = tex.charAt(i);
            if (c === '{') {
                braces++;
                i++;
            }
            else if (c === '}') {
                if (braces === 0) {
                    break;
                }
                else {
                    braces--;
                    i++;
                }
            }
            else if (c === '&' && braces === 0) {
                throw new TexError_js_1.default('ExtraCasesAlignTab', 'Extra alignment tab in text for numcase environment');
            }
            else if (c === '\\' && braces === 0) {
                var cs = (tex.slice(i + 1).match(/^[a-z]+|./i) || [])[0];
                if (cs === '\\' || cs === 'cr' || cs === 'end' || cs === 'label') {
                    break;
                }
                else {
                    i += cs.length;
                }
            }
            else {
                i++;
            }
        }
        var text = tex.substr(parser.i, i - parser.i).replace(/^\s*/, '');
        parser.PushAll(ParseUtil_js_1.default.internalMath(parser, text, 0));
        parser.i = i;
    }
};
new SymbolMap_js_1.EnvironmentMap('cases-env', EmpheqUtil_js_1.EmpheqUtil.environment, {
    numcases: ['NumCases', 'cases'],
    subnumcases: ['NumCases', 'cases']
}, exports.CasesMethods);
new SymbolMap_js_1.MacroMap('cases-macros', {
    '&': 'Entry'
}, exports.CasesMethods);
exports.CasesConfiguration = Configuration_js_1.Configuration.create('cases', {
    handler: {
        environment: ['cases-env'],
        character: ['cases-macros']
    },
    items: (_a = {},
        _a[CasesBeginItem.prototype.kind] = CasesBeginItem,
        _a),
    tags: { 'cases': CasesTags }
});
//# sourceMappingURL=CasesConfiguration.js.map

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

/***/ 398:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.ParseUtil["default"];

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

/***/ 935:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.StartItem = MathJax._.input.tex.base.BaseItems.StartItem;
exports.StopItem = MathJax._.input.tex.base.BaseItems.StopItem;
exports.OpenItem = MathJax._.input.tex.base.BaseItems.OpenItem;
exports.CloseItem = MathJax._.input.tex.base.BaseItems.CloseItem;
exports.PrimeItem = MathJax._.input.tex.base.BaseItems.PrimeItem;
exports.SubsupItem = MathJax._.input.tex.base.BaseItems.SubsupItem;
exports.OverItem = MathJax._.input.tex.base.BaseItems.OverItem;
exports.LeftItem = MathJax._.input.tex.base.BaseItems.LeftItem;
exports.Middle = MathJax._.input.tex.base.BaseItems.Middle;
exports.RightItem = MathJax._.input.tex.base.BaseItems.RightItem;
exports.BeginItem = MathJax._.input.tex.base.BaseItems.BeginItem;
exports.EndItem = MathJax._.input.tex.base.BaseItems.EndItem;
exports.StyleItem = MathJax._.input.tex.base.BaseItems.StyleItem;
exports.PositionItem = MathJax._.input.tex.base.BaseItems.PositionItem;
exports.CellItem = MathJax._.input.tex.base.BaseItems.CellItem;
exports.MmlItem = MathJax._.input.tex.base.BaseItems.MmlItem;
exports.FnItem = MathJax._.input.tex.base.BaseItems.FnItem;
exports.NotItem = MathJax._.input.tex.base.BaseItems.NotItem;
exports.NonscriptItem = MathJax._.input.tex.base.BaseItems.NonscriptItem;
exports.DotsItem = MathJax._.input.tex.base.BaseItems.DotsItem;
exports.ArrayItem = MathJax._.input.tex.base.BaseItems.ArrayItem;
exports.EqnArrayItem = MathJax._.input.tex.base.BaseItems.EqnArrayItem;
exports.EquationItem = MathJax._.input.tex.base.BaseItems.EquationItem;

/***/ }),

/***/ 360:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.base.BaseMethods["default"];

/***/ }),

/***/ 379:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AmsTags = MathJax._.input.tex.ams.AmsConfiguration.AmsTags;
exports.AmsConfiguration = MathJax._.input.tex.ams.AmsConfiguration.AmsConfiguration;

/***/ }),

/***/ 446:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.EmpheqUtil = MathJax._.input.tex.empheq.EmpheqUtil.EmpheqUtil;

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/cases/CasesConfiguration.js
var CasesConfiguration = __webpack_require__(530);
;// CONCATENATED MODULE: ./lib/cases.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/cases', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        cases: {
          CasesConfiguration: CasesConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./cases.js

}();
/******/ })()
;