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

/***/ 79:
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
var __read = (this && this.__read) || function (o, n) {
    var m = typeof Symbol === "function" && o[Symbol.iterator];
    if (!m) return o;
    var i = m.call(o), r, ar = [], e;
    try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) ar.push(r.value);
    }
    catch (error) { e = { error: error }; }
    finally {
        try {
            if (r && !r.done && (m = i["return"])) m.call(i);
        }
        finally { if (e) throw e.error; }
    }
    return ar;
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.EmpheqConfiguration = exports.EmpheqMethods = exports.EmpheqBeginItem = void 0;
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var TexError_js_1 = __importDefault(__webpack_require__(402));
var BaseItems_js_1 = __webpack_require__(935);
var EmpheqUtil_js_1 = __webpack_require__(301);
var EmpheqBeginItem = (function (_super) {
    __extends(EmpheqBeginItem, _super);
    function EmpheqBeginItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(EmpheqBeginItem.prototype, "kind", {
        get: function () {
            return 'empheq-begin';
        },
        enumerable: false,
        configurable: true
    });
    EmpheqBeginItem.prototype.checkItem = function (item) {
        if (item.isKind('end') && item.getName() === this.getName()) {
            this.setProperty('end', false);
        }
        return _super.prototype.checkItem.call(this, item);
    };
    return EmpheqBeginItem;
}(BaseItems_js_1.BeginItem));
exports.EmpheqBeginItem = EmpheqBeginItem;
exports.EmpheqMethods = {
    Empheq: function (parser, begin) {
        if (parser.stack.env.closing === begin.getName()) {
            delete parser.stack.env.closing;
            parser.Push(parser.itemFactory.create('end').setProperty('name', parser.stack.global.empheq));
            parser.stack.global.empheq = '';
            var empheq = parser.stack.Top();
            EmpheqUtil_js_1.EmpheqUtil.adjustTable(empheq, parser);
            parser.Push(parser.itemFactory.create('end').setProperty('name', 'empheq'));
        }
        else {
            ParseUtil_js_1.default.checkEqnEnv(parser);
            delete parser.stack.global.eqnenv;
            var opts = parser.GetBrackets('\\begin{' + begin.getName() + '}') || '';
            var _a = __read((parser.GetArgument('\\begin{' + begin.getName() + '}') || '').split(/=/), 2), env = _a[0], n = _a[1];
            if (!EmpheqUtil_js_1.EmpheqUtil.checkEnv(env)) {
                throw new TexError_js_1.default('UnknownEnv', 'Unknown environment "%1"', env);
            }
            if (opts) {
                begin.setProperties(EmpheqUtil_js_1.EmpheqUtil.splitOptions(opts, { left: 1, right: 1 }));
            }
            parser.stack.global.empheq = env;
            parser.string = '\\begin{' + env + '}' + (n ? '{' + n + '}' : '') + parser.string.slice(parser.i);
            parser.i = 0;
            parser.Push(begin);
        }
    },
    EmpheqMO: function (parser, _name, c) {
        parser.Push(parser.create('token', 'mo', {}, c));
    },
    EmpheqDelim: function (parser, name) {
        var c = parser.GetDelimiter(name);
        parser.Push(parser.create('token', 'mo', { stretchy: true, symmetric: true }, c));
    }
};
new SymbolMap_js_1.EnvironmentMap('empheq-env', EmpheqUtil_js_1.EmpheqUtil.environment, {
    empheq: ['Empheq', 'empheq'],
}, exports.EmpheqMethods);
new SymbolMap_js_1.CommandMap('empheq-macros', {
    empheqlbrace: ['EmpheqMO', '{'],
    empheqrbrace: ['EmpheqMO', '}'],
    empheqlbrack: ['EmpheqMO', '['],
    empheqrbrack: ['EmpheqMO', ']'],
    empheqlangle: ['EmpheqMO', '\u27E8'],
    empheqrangle: ['EmpheqMO', '\u27E9'],
    empheqlparen: ['EmpheqMO', '('],
    empheqrparen: ['EmpheqMO', ')'],
    empheqlvert: ['EmpheqMO', '|'],
    empheqrvert: ['EmpheqMO', '|'],
    empheqlVert: ['EmpheqMO', '\u2016'],
    empheqrVert: ['EmpheqMO', '\u2016'],
    empheqlfloor: ['EmpheqMO', '\u230A'],
    empheqrfloor: ['EmpheqMO', '\u230B'],
    empheqlceil: ['EmpheqMO', '\u2308'],
    empheqrceil: ['EmpheqMO', '\u2309'],
    empheqbiglbrace: ['EmpheqMO', '{'],
    empheqbigrbrace: ['EmpheqMO', '}'],
    empheqbiglbrack: ['EmpheqMO', '['],
    empheqbigrbrack: ['EmpheqMO', ']'],
    empheqbiglangle: ['EmpheqMO', '\u27E8'],
    empheqbigrangle: ['EmpheqMO', '\u27E9'],
    empheqbiglparen: ['EmpheqMO', '('],
    empheqbigrparen: ['EmpheqMO', ')'],
    empheqbiglvert: ['EmpheqMO', '|'],
    empheqbigrvert: ['EmpheqMO', '|'],
    empheqbiglVert: ['EmpheqMO', '\u2016'],
    empheqbigrVert: ['EmpheqMO', '\u2016'],
    empheqbiglfloor: ['EmpheqMO', '\u230A'],
    empheqbigrfloor: ['EmpheqMO', '\u230B'],
    empheqbiglceil: ['EmpheqMO', '\u2308'],
    empheqbigrceil: ['EmpheqMO', '\u2309'],
    empheql: 'EmpheqDelim',
    empheqr: 'EmpheqDelim',
    empheqbigl: 'EmpheqDelim',
    empheqbigr: 'EmpheqDelim'
}, exports.EmpheqMethods);
exports.EmpheqConfiguration = Configuration_js_1.Configuration.create('empheq', {
    handler: {
        macro: ['empheq-macros'],
        environment: ['empheq-env'],
    },
    items: (_a = {},
        _a[EmpheqBeginItem.prototype.kind] = EmpheqBeginItem,
        _a)
});
//# sourceMappingURL=EmpheqConfiguration.js.map

/***/ }),

/***/ 301:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __read = (this && this.__read) || function (o, n) {
    var m = typeof Symbol === "function" && o[Symbol.iterator];
    if (!m) return o;
    var i = m.call(o), r, ar = [], e;
    try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) ar.push(r.value);
    }
    catch (error) { e = { error: error }; }
    finally {
        try {
            if (r && !r.done && (m = i["return"])) m.call(i);
        }
        finally { if (e) throw e.error; }
    }
    return ar;
};
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
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
exports.EmpheqUtil = void 0;
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var TexParser_js_1 = __importDefault(__webpack_require__(193));
exports.EmpheqUtil = {
    environment: function (parser, env, func, args) {
        var name = args[0];
        var item = parser.itemFactory.create(name + '-begin').setProperties({ name: env, end: name });
        parser.Push(func.apply(void 0, __spreadArray([parser, item], __read(args.slice(1)), false)));
    },
    splitOptions: function (text, allowed) {
        if (allowed === void 0) { allowed = null; }
        return ParseUtil_js_1.default.keyvalOptions(text, allowed, true);
    },
    columnCount: function (table) {
        var e_1, _a;
        var m = 0;
        try {
            for (var _b = __values(table.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                var row = _c.value;
                var n = row.childNodes.length - (row.isKind('mlabeledtr') ? 1 : 0);
                if (n > m)
                    m = n;
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_1) throw e_1.error; }
        }
        return m;
    },
    cellBlock: function (tex, table, parser, env) {
        var e_2, _a;
        var mpadded = parser.create('node', 'mpadded', [], { height: 0, depth: 0, voffset: '-1height' });
        var result = new TexParser_js_1.default(tex, parser.stack.env, parser.configuration);
        var mml = result.mml();
        if (env && result.configuration.tags.label) {
            result.configuration.tags.currentTag.env = env;
            result.configuration.tags.getTag(true);
        }
        try {
            for (var _b = __values((mml.isInferred ? mml.childNodes : [mml])), _c = _b.next(); !_c.done; _c = _b.next()) {
                var child = _c.value;
                mpadded.appendChild(child);
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_2) throw e_2.error; }
        }
        mpadded.appendChild(parser.create('node', 'mphantom', [
            parser.create('node', 'mpadded', [table], { width: 0 })
        ]));
        return mpadded;
    },
    topRowTable: function (original, parser) {
        var table = ParseUtil_js_1.default.copyNode(original, parser);
        table.setChildren(table.childNodes.slice(0, 1));
        table.attributes.set('align', 'baseline 1');
        return original.factory.create('mphantom', {}, [parser.create('node', 'mpadded', [table], { width: 0 })]);
    },
    rowspanCell: function (mtd, tex, table, parser, env) {
        mtd.appendChild(parser.create('node', 'mpadded', [
            this.cellBlock(tex, ParseUtil_js_1.default.copyNode(table, parser), parser, env),
            this.topRowTable(table, parser)
        ], { height: 0, depth: 0, voffset: 'height' }));
    },
    left: function (table, original, left, parser, env) {
        var e_3, _a;
        if (env === void 0) { env = ''; }
        table.attributes.set('columnalign', 'right ' + (table.attributes.get('columnalign') || ''));
        table.attributes.set('columnspacing', '0em ' + (table.attributes.get('columnspacing') || ''));
        var mtd;
        try {
            for (var _b = __values(table.childNodes.slice(0).reverse()), _c = _b.next(); !_c.done; _c = _b.next()) {
                var row = _c.value;
                mtd = parser.create('node', 'mtd');
                row.childNodes.unshift(mtd);
                mtd.parent = row;
                if (row.isKind('mlabeledtr')) {
                    row.childNodes[0] = row.childNodes[1];
                    row.childNodes[1] = mtd;
                }
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_3) throw e_3.error; }
        }
        this.rowspanCell(mtd, left, original, parser, env);
    },
    right: function (table, original, right, parser, env) {
        if (env === void 0) { env = ''; }
        if (table.childNodes.length === 0) {
            table.appendChild(parser.create('node', 'mtr'));
        }
        var m = exports.EmpheqUtil.columnCount(table);
        var row = table.childNodes[0];
        while (row.childNodes.length < m)
            row.appendChild(parser.create('node', 'mtd'));
        var mtd = row.appendChild(parser.create('node', 'mtd'));
        exports.EmpheqUtil.rowspanCell(mtd, right, original, parser, env);
        table.attributes.set('columnalign', (table.attributes.get('columnalign') || '').split(/ /).slice(0, m).join(' ') + ' left');
        table.attributes.set('columnspacing', (table.attributes.get('columnspacing') || '').split(/ /).slice(0, m - 1).join(' ') + ' 0em');
    },
    adjustTable: function (empheq, parser) {
        var left = empheq.getProperty('left');
        var right = empheq.getProperty('right');
        if (left || right) {
            var table = empheq.Last;
            var original = ParseUtil_js_1.default.copyNode(table, parser);
            if (left)
                this.left(table, original, left, parser);
            if (right)
                this.right(table, original, right, parser);
        }
    },
    allowEnv: {
        equation: true,
        align: true,
        gather: true,
        flalign: true,
        alignat: true,
        multline: true
    },
    checkEnv: function (env) {
        return this.allowEnv.hasOwnProperty(env.replace(/\*$/, '')) || false;
    }
};
//# sourceMappingURL=EmpheqUtil.js.map

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

/***/ 193:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.TexParser["default"];

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/empheq/EmpheqConfiguration.js
var EmpheqConfiguration = __webpack_require__(79);
// EXTERNAL MODULE: ../../../../../../js/input/tex/empheq/EmpheqUtil.js
var EmpheqUtil = __webpack_require__(301);
;// CONCATENATED MODULE: ./lib/empheq.js





if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/empheq', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        empheq: {
          EmpheqConfiguration: EmpheqConfiguration,
          EmpheqUtil: EmpheqUtil
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./empheq.js

}();
/******/ })()
;