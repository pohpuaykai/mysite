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

/***/ 205:
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
var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MathtoolsConfiguration = exports.fixPrescripts = exports.PAIREDDELIMS = void 0;
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var NodeUtil_js_1 = __importDefault(__webpack_require__(748));
var Options_js_1 = __webpack_require__(74);
__webpack_require__(926);
var MathtoolsUtil_js_1 = __webpack_require__(262);
var MathtoolsTags_js_1 = __webpack_require__(298);
var MathtoolsItems_js_1 = __webpack_require__(144);
exports.PAIREDDELIMS = 'mathtools-paired-delims';
function initMathtools(config) {
    new SymbolMap_js_1.CommandMap(exports.PAIREDDELIMS, {}, {});
    config.append(Configuration_js_1.Configuration.local({ handler: { macro: [exports.PAIREDDELIMS] }, priority: -5 }));
}
function configMathtools(config, jax) {
    var e_1, _a;
    var parser = jax.parseOptions;
    var pairedDelims = parser.options.mathtools.pairedDelimiters;
    try {
        for (var _b = __values(Object.keys(pairedDelims)), _c = _b.next(); !_c.done; _c = _b.next()) {
            var cs = _c.value;
            MathtoolsUtil_js_1.MathtoolsUtil.addPairedDelims(parser, cs, pairedDelims[cs]);
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
        }
        finally { if (e_1) throw e_1.error; }
    }
    (0, MathtoolsTags_js_1.MathtoolsTagFormat)(config, jax);
}
function fixPrescripts(_a) {
    var e_2, _b, e_3, _c, e_4, _d;
    var data = _a.data;
    try {
        for (var _e = __values(data.getList('mmultiscripts')), _f = _e.next(); !_f.done; _f = _e.next()) {
            var node = _f.value;
            if (!node.getProperty('fixPrescript'))
                continue;
            var childNodes = NodeUtil_js_1.default.getChildren(node);
            var n = 0;
            try {
                for (var _g = (e_3 = void 0, __values([1, 2])), _h = _g.next(); !_h.done; _h = _g.next()) {
                    var i = _h.value;
                    if (!childNodes[i]) {
                        NodeUtil_js_1.default.setChild(node, i, data.nodeFactory.create('node', 'none'));
                        n++;
                    }
                }
            }
            catch (e_3_1) { e_3 = { error: e_3_1 }; }
            finally {
                try {
                    if (_h && !_h.done && (_c = _g.return)) _c.call(_g);
                }
                finally { if (e_3) throw e_3.error; }
            }
            try {
                for (var _j = (e_4 = void 0, __values([4, 5])), _k = _j.next(); !_k.done; _k = _j.next()) {
                    var i = _k.value;
                    if (NodeUtil_js_1.default.isType(childNodes[i], 'mrow') && NodeUtil_js_1.default.getChildren(childNodes[i]).length === 0) {
                        NodeUtil_js_1.default.setChild(node, i, data.nodeFactory.create('node', 'none'));
                    }
                }
            }
            catch (e_4_1) { e_4 = { error: e_4_1 }; }
            finally {
                try {
                    if (_k && !_k.done && (_d = _j.return)) _d.call(_j);
                }
                finally { if (e_4) throw e_4.error; }
            }
            if (n === 2) {
                childNodes.splice(1, 2);
            }
        }
    }
    catch (e_2_1) { e_2 = { error: e_2_1 }; }
    finally {
        try {
            if (_f && !_f.done && (_b = _e.return)) _b.call(_e);
        }
        finally { if (e_2) throw e_2.error; }
    }
}
exports.fixPrescripts = fixPrescripts;
exports.MathtoolsConfiguration = Configuration_js_1.Configuration.create('mathtools', {
    handler: {
        macro: ['mathtools-macros', 'mathtools-delimiters'],
        environment: ['mathtools-environments'],
        delimiter: ['mathtools-delimiters'],
        character: ['mathtools-characters']
    },
    items: (_a = {},
        _a[MathtoolsItems_js_1.MultlinedItem.prototype.kind] = MathtoolsItems_js_1.MultlinedItem,
        _a),
    init: initMathtools,
    config: configMathtools,
    postprocessors: [[fixPrescripts, -6]],
    options: {
        mathtools: {
            'multlinegap': '1em',
            'multlined-pos': 'c',
            'firstline-afterskip': '',
            'lastline-preskip': '',
            'smallmatrix-align': 'c',
            'shortvdotsadjustabove': '.2em',
            'shortvdotsadjustbelow': '.2em',
            'centercolon': false,
            'centercolon-offset': '.04em',
            'thincolon-dx': '-.04em',
            'thincolon-dw': '-.08em',
            'use-unicode': false,
            'prescript-sub-format': '',
            'prescript-sup-format': '',
            'prescript-arg-format': '',
            'allow-mathtoolsset': true,
            pairedDelimiters: (0, Options_js_1.expandable)({}),
            tagforms: (0, Options_js_1.expandable)({}),
        }
    }
});
//# sourceMappingURL=MathtoolsConfiguration.js.map

/***/ }),

/***/ 144:
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
exports.MultlinedItem = void 0;
var AmsItems_js_1 = __webpack_require__(927);
var NodeUtil_js_1 = __importDefault(__webpack_require__(748));
var TexConstants_js_1 = __webpack_require__(108);
var MultlinedItem = (function (_super) {
    __extends(MultlinedItem, _super);
    function MultlinedItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(MultlinedItem.prototype, "kind", {
        get: function () {
            return 'multlined';
        },
        enumerable: false,
        configurable: true
    });
    MultlinedItem.prototype.EndTable = function () {
        if (this.Size() || this.row.length) {
            this.EndEntry();
            this.EndRow();
        }
        if (this.table.length > 1) {
            var options = this.factory.configuration.options.mathtools;
            var gap = options.multlinegap;
            var firstskip = options['firstline-afterskip'] || gap;
            var lastskip = options['lastline-preskip'] || gap;
            var first = NodeUtil_js_1.default.getChildren(this.table[0])[0];
            if (NodeUtil_js_1.default.getAttribute(first, 'columnalign') !== TexConstants_js_1.TexConstant.Align.RIGHT) {
                first.appendChild(this.create('node', 'mspace', [], { width: firstskip }));
            }
            var last = NodeUtil_js_1.default.getChildren(this.table[this.table.length - 1])[0];
            if (NodeUtil_js_1.default.getAttribute(last, 'columnalign') !== TexConstants_js_1.TexConstant.Align.LEFT) {
                var top_1 = NodeUtil_js_1.default.getChildren(last)[0];
                top_1.childNodes.unshift(null);
                var space = this.create('node', 'mspace', [], { width: lastskip });
                NodeUtil_js_1.default.setChild(top_1, 0, space);
            }
        }
        _super.prototype.EndTable.call(this);
    };
    return MultlinedItem;
}(AmsItems_js_1.MultlineItem));
exports.MultlinedItem = MultlinedItem;
//# sourceMappingURL=MathtoolsItems.js.map

/***/ }),

/***/ 926:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var ParseMethods_js_1 = __importDefault(__webpack_require__(945));
var SymbolMap_js_1 = __webpack_require__(871);
var TexConstants_js_1 = __webpack_require__(108);
var MathtoolsMethods_js_1 = __webpack_require__(178);
new SymbolMap_js_1.CommandMap('mathtools-macros', {
    shoveleft: ['HandleShove', TexConstants_js_1.TexConstant.Align.LEFT],
    shoveright: ['HandleShove', TexConstants_js_1.TexConstant.Align.RIGHT],
    xleftrightarrow: ['xArrow', 0x2194, 10, 10],
    xLeftarrow: ['xArrow', 0x21D0, 12, 7],
    xRightarrow: ['xArrow', 0x21D2, 7, 12],
    xLeftrightarrow: ['xArrow', 0x21D4, 12, 12],
    xhookleftarrow: ['xArrow', 0x21A9, 10, 5],
    xhookrightarrow: ['xArrow', 0x21AA, 5, 10],
    xmapsto: ['xArrow', 0x21A6, 10, 10],
    xrightharpoondown: ['xArrow', 0x21C1, 5, 10],
    xleftharpoondown: ['xArrow', 0x21BD, 10, 5],
    xrightleftharpoons: ['xArrow', 0x21CC, 10, 10],
    xrightharpoonup: ['xArrow', 0x21C0, 5, 10],
    xleftharpoonup: ['xArrow', 0x21BC, 10, 5],
    xleftrightharpoons: ['xArrow', 0x21CB, 10, 10],
    mathllap: ['MathLap', 'l', false],
    mathrlap: ['MathLap', 'r', false],
    mathclap: ['MathLap', 'c', false],
    clap: ['MtLap', 'c'],
    textllap: ['MtLap', 'l'],
    textrlap: ['MtLap', 'r'],
    textclap: ['MtLap', 'c'],
    cramped: 'Cramped',
    crampedllap: ['MathLap', 'l', true],
    crampedrlap: ['MathLap', 'r', true],
    crampedclap: ['MathLap', 'c', true],
    crampedsubstack: ['Macro', '\\begin{crampedsubarray}{c}#1\\end{crampedsubarray}', 1],
    mathmbox: 'MathMBox',
    mathmakebox: 'MathMakeBox',
    overbracket: 'UnderOverBracket',
    underbracket: 'UnderOverBracket',
    refeq: 'HandleRef',
    MoveEqLeft: ['Macro', '\\hspace{#1em}&\\hspace{-#1em}', 1, '2'],
    Aboxed: 'Aboxed',
    ArrowBetweenLines: 'ArrowBetweenLines',
    vdotswithin: 'VDotsWithin',
    shortvdotswithin: 'ShortVDotsWithin',
    MTFlushSpaceAbove: 'FlushSpaceAbove',
    MTFlushSpaceBelow: 'FlushSpaceBelow',
    DeclarePairedDelimiter: 'DeclarePairedDelimiter',
    DeclarePairedDelimiterX: 'DeclarePairedDelimiterX',
    DeclarePairedDelimiterXPP: 'DeclarePairedDelimiterXPP',
    DeclarePairedDelimiters: 'DeclarePairedDelimiter',
    DeclarePairedDelimitersX: 'DeclarePairedDelimiterX',
    DeclarePairedDelimitersXPP: 'DeclarePairedDelimiterXPP',
    centercolon: ['CenterColon', true, true],
    ordinarycolon: ['CenterColon', false],
    MTThinColon: ['CenterColon', true, true, true],
    coloneqq: ['Relation', ':=', '\u2254'],
    Coloneqq: ['Relation', '::=', '\u2A74'],
    coloneq: ['Relation', ':-'],
    Coloneq: ['Relation', '::-'],
    eqqcolon: ['Relation', '=:', '\u2255'],
    Eqqcolon: ['Relation', '=::'],
    eqcolon: ['Relation', '-:', '\u2239'],
    Eqcolon: ['Relation', '-::'],
    colonapprox: ['Relation', ':\\approx'],
    Colonapprox: ['Relation', '::\\approx'],
    colonsim: ['Relation', ':\\sim'],
    Colonsim: ['Relation', '::\\sim'],
    dblcolon: ['Relation', '::', '\u2237'],
    nuparrow: ['NArrow', '\u2191', '.06em'],
    ndownarrow: ['NArrow', '\u2193', '.25em'],
    bigtimes: ['Macro', '\\mathop{\\Large\\kern-.1em\\boldsymbol{\\times}\\kern-.1em}'],
    splitfrac: ['SplitFrac', false],
    splitdfrac: ['SplitFrac', true],
    xmathstrut: 'XMathStrut',
    prescript: 'Prescript',
    newtagform: ['NewTagForm', false],
    renewtagform: ['NewTagForm', true],
    usetagform: 'UseTagForm',
    adjustlimits: [
        'MacroWithTemplate',
        '\\mathop{{#1}\\vphantom{{#3}}}_{{#2}\\vphantom{{#4}}}\\mathop{{#3}\\vphantom{{#1}}}_{{#4}\\vphantom{{#2}}}',
        4, , '_', , '_'
    ],
    mathtoolsset: 'SetOptions'
}, MathtoolsMethods_js_1.MathtoolsMethods);
new SymbolMap_js_1.EnvironmentMap('mathtools-environments', ParseMethods_js_1.default.environment, {
    dcases: ['Array', null, '\\{', '', 'll', null, '.2em', 'D'],
    rcases: ['Array', null, '', '\\}', 'll', null, '.2em'],
    drcases: ['Array', null, '', '\\}', 'll', null, '.2em', 'D'],
    'dcases*': ['Cases', null, '{', '', 'D'],
    'rcases*': ['Cases', null, '', '}'],
    'drcases*': ['Cases', null, '', '}', 'D'],
    'cases*': ['Cases', null, '{', ''],
    'matrix*': ['MtMatrix', null, null, null],
    'pmatrix*': ['MtMatrix', null, '(', ')'],
    'bmatrix*': ['MtMatrix', null, '[', ']'],
    'Bmatrix*': ['MtMatrix', null, '\\{', '\\}'],
    'vmatrix*': ['MtMatrix', null, '\\vert', '\\vert'],
    'Vmatrix*': ['MtMatrix', null, '\\Vert', '\\Vert'],
    'smallmatrix*': ['MtSmallMatrix', null, null, null],
    psmallmatrix: ['MtSmallMatrix', null, '(', ')', 'c'],
    'psmallmatrix*': ['MtSmallMatrix', null, '(', ')'],
    bsmallmatrix: ['MtSmallMatrix', null, '[', ']', 'c'],
    'bsmallmatrix*': ['MtSmallMatrix', null, '[', ']'],
    Bsmallmatrix: ['MtSmallMatrix', null, '\\{', '\\}', 'c'],
    'Bsmallmatrix*': ['MtSmallMatrix', null, '\\{', '\\}'],
    vsmallmatrix: ['MtSmallMatrix', null, '\\vert', '\\vert', 'c'],
    'vsmallmatrix*': ['MtSmallMatrix', null, '\\vert', '\\vert'],
    Vsmallmatrix: ['MtSmallMatrix', null, '\\Vert', '\\Vert', 'c'],
    'Vsmallmatrix*': ['MtSmallMatrix', null, '\\Vert', '\\Vert'],
    crampedsubarray: ['Array', null, null, null, null, '0em', '0.1em', 'S\'', 1],
    multlined: 'MtMultlined',
    spreadlines: ['SpreadLines', true],
    lgathered: ['AmsEqnArray', null, null, null, 'l', null, '.5em', 'D'],
    rgathered: ['AmsEqnArray', null, null, null, 'r', null, '.5em', 'D'],
}, MathtoolsMethods_js_1.MathtoolsMethods);
new SymbolMap_js_1.DelimiterMap('mathtools-delimiters', ParseMethods_js_1.default.delimiter, {
    '\\lparen': '(',
    '\\rparen': ')'
});
new SymbolMap_js_1.CommandMap('mathtools-characters', {
    ':': ['CenterColon', true]
}, MathtoolsMethods_js_1.MathtoolsMethods);
//# sourceMappingURL=MathtoolsMappings.js.map

/***/ }),

/***/ 178:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
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
exports.MathtoolsMethods = void 0;
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var AmsMethods_js_1 = __webpack_require__(939);
var BaseMethods_js_1 = __importDefault(__webpack_require__(360));
var TexParser_js_1 = __importDefault(__webpack_require__(193));
var TexError_js_1 = __importDefault(__webpack_require__(402));
var NodeUtil_js_1 = __importDefault(__webpack_require__(748));
var MmlNode_js_1 = __webpack_require__(801);
var lengths_js_1 = __webpack_require__(230);
var Options_js_1 = __webpack_require__(74);
var NewcommandUtil_js_1 = __importDefault(__webpack_require__(892));
var NewcommandMethods_js_1 = __importDefault(__webpack_require__(432));
var MathtoolsUtil_js_1 = __webpack_require__(262);
exports.MathtoolsMethods = {
    MtMatrix: function (parser, begin, open, close) {
        var align = parser.GetBrackets("\\begin{".concat(begin.getName(), "}"), 'c');
        return exports.MathtoolsMethods.Array(parser, begin, open, close, align);
    },
    MtSmallMatrix: function (parser, begin, open, close, align) {
        if (!align) {
            align = parser.GetBrackets("\\begin{".concat(begin.getName(), "}"), parser.options.mathtools['smallmatrix-align']);
        }
        return exports.MathtoolsMethods.Array(parser, begin, open, close, align, ParseUtil_js_1.default.Em(1 / 3), '.2em', 'S', 1);
    },
    MtMultlined: function (parser, begin) {
        var _a;
        var name = "\\begin{".concat(begin.getName(), "}");
        var pos = parser.GetBrackets(name, parser.options.mathtools['multlined-pos'] || 'c');
        var width = pos ? parser.GetBrackets(name, '') : '';
        if (pos && !pos.match(/^[cbt]$/)) {
            _a = __read([pos, width], 2), width = _a[0], pos = _a[1];
        }
        parser.Push(begin);
        var item = parser.itemFactory.create('multlined', parser, begin);
        item.arraydef = {
            displaystyle: true,
            rowspacing: '.5em',
            width: width || 'auto',
            columnwidth: '100%',
        };
        return ParseUtil_js_1.default.setArrayAlign(item, pos || 'c');
    },
    HandleShove: function (parser, name, shove) {
        var top = parser.stack.Top();
        if (top.kind !== 'multline' && top.kind !== 'multlined') {
            throw new TexError_js_1.default('CommandInMultlined', '%1 can only appear within the multline or multlined environments', name);
        }
        if (top.Size()) {
            throw new TexError_js_1.default('CommandAtTheBeginingOfLine', '%1 must come at the beginning of the line', name);
        }
        top.setProperty('shove', shove);
        var shift = parser.GetBrackets(name);
        var mml = parser.ParseArg(name);
        if (shift) {
            var mrow = parser.create('node', 'mrow', []);
            var mspace = parser.create('node', 'mspace', [], { width: shift });
            if (shove === 'left') {
                mrow.appendChild(mspace);
                mrow.appendChild(mml);
            }
            else {
                mrow.appendChild(mml);
                mrow.appendChild(mspace);
            }
            mml = mrow;
        }
        parser.Push(mml);
    },
    SpreadLines: function (parser, begin) {
        var e_1, _a;
        if (parser.stack.env.closing === begin.getName()) {
            delete parser.stack.env.closing;
            var top_1 = parser.stack.Pop();
            var mml = top_1.toMml();
            var spread = top_1.getProperty('spread');
            if (mml.isInferred) {
                try {
                    for (var _b = __values(NodeUtil_js_1.default.getChildren(mml)), _c = _b.next(); !_c.done; _c = _b.next()) {
                        var child = _c.value;
                        MathtoolsUtil_js_1.MathtoolsUtil.spreadLines(child, spread);
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
            else {
                MathtoolsUtil_js_1.MathtoolsUtil.spreadLines(mml, spread);
            }
            parser.Push(mml);
        }
        else {
            var spread = parser.GetDimen("\\begin{".concat(begin.getName(), "}"));
            begin.setProperty('spread', spread);
            parser.Push(begin);
        }
    },
    Cases: function (parser, begin, open, close, style) {
        var array = parser.itemFactory.create('array').setProperty('casesEnv', begin.getName());
        array.arraydef = {
            rowspacing: '.2em',
            columnspacing: '1em',
            columnalign: 'left'
        };
        if (style === 'D') {
            array.arraydef.displaystyle = true;
        }
        array.setProperties({ open: open, close: close });
        parser.Push(begin);
        return array;
    },
    MathLap: function (parser, name, pos, cramped) {
        var style = parser.GetBrackets(name, '').trim();
        var mml = parser.create('node', 'mstyle', [
            parser.create('node', 'mpadded', [parser.ParseArg(name)], __assign({ width: 0 }, (pos === 'r' ? {} : { lspace: (pos === 'l' ? '-1width' : '-.5width') })))
        ], { 'data-cramped': cramped });
        MathtoolsUtil_js_1.MathtoolsUtil.setDisplayLevel(mml, style);
        parser.Push(parser.create('node', 'TeXAtom', [mml]));
    },
    Cramped: function (parser, name) {
        var style = parser.GetBrackets(name, '').trim();
        var arg = parser.ParseArg(name);
        var mml = parser.create('node', 'mstyle', [arg], { 'data-cramped': true });
        MathtoolsUtil_js_1.MathtoolsUtil.setDisplayLevel(mml, style);
        parser.Push(mml);
    },
    MtLap: function (parser, name, pos) {
        var content = ParseUtil_js_1.default.internalMath(parser, parser.GetArgument(name), 0);
        var mml = parser.create('node', 'mpadded', content, { width: 0 });
        if (pos !== 'r') {
            NodeUtil_js_1.default.setAttribute(mml, 'lspace', pos === 'l' ? '-1width' : '-.5width');
        }
        parser.Push(mml);
    },
    MathMakeBox: function (parser, name) {
        var width = parser.GetBrackets(name);
        var pos = parser.GetBrackets(name, 'c');
        var mml = parser.create('node', 'mpadded', [parser.ParseArg(name)]);
        if (width) {
            NodeUtil_js_1.default.setAttribute(mml, 'width', width);
        }
        var align = (0, Options_js_1.lookup)(pos, { c: 'center', r: 'right' }, '');
        if (align) {
            NodeUtil_js_1.default.setAttribute(mml, 'data-align', align);
        }
        parser.Push(mml);
    },
    MathMBox: function (parser, name) {
        parser.Push(parser.create('node', 'mrow', [parser.ParseArg(name)]));
    },
    UnderOverBracket: function (parser, name) {
        var thickness = (0, lengths_js_1.length2em)(parser.GetBrackets(name, '.1em'), .1);
        var height = parser.GetBrackets(name, '.2em');
        var arg = parser.GetArgument(name);
        var _a = __read((name.charAt(1) === 'o' ?
            ['over', 'accent', 'bottom'] :
            ['under', 'accentunder', 'top']), 3), pos = _a[0], accent = _a[1], border = _a[2];
        var t = (0, lengths_js_1.em)(thickness);
        var base = new TexParser_js_1.default(arg, parser.stack.env, parser.configuration).mml();
        var copy = new TexParser_js_1.default(arg, parser.stack.env, parser.configuration).mml();
        var script = parser.create('node', 'mpadded', [
            parser.create('node', 'mphantom', [copy])
        ], {
            style: "border: ".concat(t, " solid; border-").concat(border, ": none"),
            height: height,
            depth: 0
        });
        var node = ParseUtil_js_1.default.underOver(parser, base, script, pos, true);
        var munderover = NodeUtil_js_1.default.getChildAt(NodeUtil_js_1.default.getChildAt(node, 0), 0);
        NodeUtil_js_1.default.setAttribute(munderover, accent, true);
        parser.Push(node);
    },
    Aboxed: function (parser, name) {
        var top = MathtoolsUtil_js_1.MathtoolsUtil.checkAlignment(parser, name);
        if (top.row.length % 2 === 1) {
            top.row.push(parser.create('node', 'mtd', []));
        }
        var arg = parser.GetArgument(name);
        var rest = parser.string.substr(parser.i);
        parser.string = arg + '&&\\endAboxed';
        parser.i = 0;
        var left = parser.GetUpTo(name, '&');
        var right = parser.GetUpTo(name, '&');
        parser.GetUpTo(name, '\\endAboxed');
        var tex = ParseUtil_js_1.default.substituteArgs(parser, [left, right], '\\rlap{\\boxed{#1{}#2}}\\kern.267em\\phantom{#1}&\\phantom{{}#2}\\kern.267em');
        parser.string = tex + rest;
        parser.i = 0;
    },
    ArrowBetweenLines: function (parser, name) {
        var top = MathtoolsUtil_js_1.MathtoolsUtil.checkAlignment(parser, name);
        if (top.Size() || top.row.length) {
            throw new TexError_js_1.default('BetweenLines', '%1 must be on a row by itself', name);
        }
        var star = parser.GetStar();
        var symbol = parser.GetBrackets(name, '\\Updownarrow');
        if (star) {
            top.EndEntry();
            top.EndEntry();
        }
        var tex = (star ? '\\quad' + symbol : symbol + '\\quad');
        var mml = new TexParser_js_1.default(tex, parser.stack.env, parser.configuration).mml();
        parser.Push(mml);
        top.EndEntry();
        top.EndRow();
    },
    VDotsWithin: function (parser, name) {
        var top = parser.stack.Top();
        var isFlush = (top.getProperty('flushspaceabove') === top.table.length);
        var arg = '\\mmlToken{mi}{}' + parser.GetArgument(name) + '\\mmlToken{mi}{}';
        var base = new TexParser_js_1.default(arg, parser.stack.env, parser.configuration).mml();
        var mml = parser.create('node', 'mpadded', [
            parser.create('node', 'mpadded', [
                parser.create('node', 'mo', [
                    parser.create('text', '\u22EE')
                ])
            ], __assign({ width: 0, lspace: '-.5width' }, (isFlush ? { height: '-.6em', voffset: '-.18em' } : {}))),
            parser.create('node', 'mphantom', [base])
        ], {
            lspace: '.5width'
        });
        parser.Push(mml);
    },
    ShortVDotsWithin: function (parser, _name) {
        var top = parser.stack.Top();
        var star = parser.GetStar();
        exports.MathtoolsMethods.FlushSpaceAbove(parser, '\\MTFlushSpaceAbove');
        !star && top.EndEntry();
        exports.MathtoolsMethods.VDotsWithin(parser, '\\vdotswithin');
        star && top.EndEntry();
        exports.MathtoolsMethods.FlushSpaceBelow(parser, '\\MTFlushSpaceBelow');
    },
    FlushSpaceAbove: function (parser, name) {
        var top = MathtoolsUtil_js_1.MathtoolsUtil.checkAlignment(parser, name);
        top.setProperty('flushspaceabove', top.table.length);
        top.addRowSpacing('-' + parser.options.mathtools['shortvdotsadjustabove']);
    },
    FlushSpaceBelow: function (parser, name) {
        var top = MathtoolsUtil_js_1.MathtoolsUtil.checkAlignment(parser, name);
        top.Size() && top.EndEntry();
        top.EndRow();
        top.addRowSpacing('-' + parser.options.mathtools['shortvdotsadjustbelow']);
    },
    PairedDelimiters: function (parser, name, open, close, body, n, pre, post) {
        if (body === void 0) { body = '#1'; }
        if (n === void 0) { n = 1; }
        if (pre === void 0) { pre = ''; }
        if (post === void 0) { post = ''; }
        var star = parser.GetStar();
        var size = (star ? '' : parser.GetBrackets(name));
        var _a = __read((star ? ['\\left', '\\right'] : size ? [size + 'l', size + 'r'] : ['', '']), 2), left = _a[0], right = _a[1];
        var delim = (star ? '\\middle' : size || '');
        if (n) {
            var args = [];
            for (var i = args.length; i < n; i++) {
                args.push(parser.GetArgument(name));
            }
            pre = ParseUtil_js_1.default.substituteArgs(parser, args, pre);
            body = ParseUtil_js_1.default.substituteArgs(parser, args, body);
            post = ParseUtil_js_1.default.substituteArgs(parser, args, post);
        }
        body = body.replace(/\\delimsize/g, delim);
        parser.string = [pre, left, open, body, right, close, post, parser.string.substr(parser.i)]
            .reduce(function (s, part) { return ParseUtil_js_1.default.addArgs(parser, s, part); }, '');
        parser.i = 0;
        ParseUtil_js_1.default.checkMaxMacros(parser);
    },
    DeclarePairedDelimiter: function (parser, name) {
        var cs = NewcommandUtil_js_1.default.GetCsNameArgument(parser, name);
        var open = parser.GetArgument(name);
        var close = parser.GetArgument(name);
        MathtoolsUtil_js_1.MathtoolsUtil.addPairedDelims(parser.configuration, cs, [open, close]);
    },
    DeclarePairedDelimiterX: function (parser, name) {
        var cs = NewcommandUtil_js_1.default.GetCsNameArgument(parser, name);
        var n = NewcommandUtil_js_1.default.GetArgCount(parser, name);
        var open = parser.GetArgument(name);
        var close = parser.GetArgument(name);
        var body = parser.GetArgument(name);
        MathtoolsUtil_js_1.MathtoolsUtil.addPairedDelims(parser.configuration, cs, [open, close, body, n]);
    },
    DeclarePairedDelimiterXPP: function (parser, name) {
        var cs = NewcommandUtil_js_1.default.GetCsNameArgument(parser, name);
        var n = NewcommandUtil_js_1.default.GetArgCount(parser, name);
        var pre = parser.GetArgument(name);
        var open = parser.GetArgument(name);
        var close = parser.GetArgument(name);
        var post = parser.GetArgument(name);
        var body = parser.GetArgument(name);
        MathtoolsUtil_js_1.MathtoolsUtil.addPairedDelims(parser.configuration, cs, [open, close, body, n, pre, post]);
    },
    CenterColon: function (parser, _name, center, force, thin) {
        if (force === void 0) { force = false; }
        if (thin === void 0) { thin = false; }
        var options = parser.options.mathtools;
        var mml = parser.create('token', 'mo', {}, ':');
        if (center && (options['centercolon'] || force)) {
            var dy = options['centercolon-offset'];
            mml = parser.create('node', 'mpadded', [mml], __assign({ voffset: dy, height: "+".concat(dy), depth: "-".concat(dy) }, (thin ? { width: options['thincolon-dw'], lspace: options['thincolon-dx'] } : {})));
        }
        parser.Push(mml);
    },
    Relation: function (parser, _name, tex, unicode) {
        var options = parser.options.mathtools;
        if (options['use-unicode'] && unicode) {
            parser.Push(parser.create('token', 'mo', { texClass: MmlNode_js_1.TEXCLASS.REL }, unicode));
        }
        else {
            tex = '\\mathrel{' + tex.replace(/:/g, '\\MTThinColon').replace(/-/g, '\\mathrel{-}') + '}';
            parser.string = ParseUtil_js_1.default.addArgs(parser, tex, parser.string.substr(parser.i));
            parser.i = 0;
        }
    },
    NArrow: function (parser, _name, c, dy) {
        parser.Push(parser.create('node', 'TeXAtom', [
            parser.create('token', 'mtext', {}, c),
            parser.create('node', 'mpadded', [
                parser.create('node', 'mpadded', [
                    parser.create('node', 'menclose', [
                        parser.create('node', 'mspace', [], { height: '.2em', depth: 0, width: '.4em' })
                    ], { notation: 'updiagonalstrike', 'data-thickness': '.05em', 'data-padding': 0 })
                ], { width: 0, lspace: '-.5width', voffset: dy }),
                parser.create('node', 'mphantom', [
                    parser.create('token', 'mtext', {}, c)
                ])
            ], { width: 0, lspace: '-.5width' })
        ], { texClass: MmlNode_js_1.TEXCLASS.REL }));
    },
    SplitFrac: function (parser, name, display) {
        var num = parser.ParseArg(name);
        var den = parser.ParseArg(name);
        parser.Push(parser.create('node', 'mstyle', [
            parser.create('node', 'mfrac', [
                parser.create('node', 'mstyle', [
                    num,
                    parser.create('token', 'mi'),
                    parser.create('token', 'mspace', { width: '1em' })
                ], { scriptlevel: 0 }),
                parser.create('node', 'mstyle', [
                    parser.create('token', 'mspace', { width: '1em' }),
                    parser.create('token', 'mi'),
                    den
                ], { scriptlevel: 0 })
            ], { linethickness: 0, numalign: 'left', denomalign: 'right' })
        ], { displaystyle: display, scriptlevel: 0 }));
    },
    XMathStrut: function (parser, name) {
        var dd = parser.GetBrackets(name);
        var dh = parser.GetArgument(name);
        dh = MathtoolsUtil_js_1.MathtoolsUtil.plusOrMinus(name, dh);
        dd = MathtoolsUtil_js_1.MathtoolsUtil.plusOrMinus(name, dd || dh);
        parser.Push(parser.create('node', 'TeXAtom', [
            parser.create('node', 'mpadded', [
                parser.create('node', 'mphantom', [
                    parser.create('token', 'mo', { stretchy: false }, '(')
                ])
            ], { width: 0, height: dh + 'height', depth: dd + 'depth' })
        ], { texClass: MmlNode_js_1.TEXCLASS.ORD }));
    },
    Prescript: function (parser, name) {
        var sup = MathtoolsUtil_js_1.MathtoolsUtil.getScript(parser, name, 'sup');
        var sub = MathtoolsUtil_js_1.MathtoolsUtil.getScript(parser, name, 'sub');
        var base = MathtoolsUtil_js_1.MathtoolsUtil.getScript(parser, name, 'arg');
        if (NodeUtil_js_1.default.isType(sup, 'none') && NodeUtil_js_1.default.isType(sub, 'none')) {
            parser.Push(base);
            return;
        }
        var mml = parser.create('node', 'mmultiscripts', [base]);
        NodeUtil_js_1.default.getChildren(mml).push(null, null);
        NodeUtil_js_1.default.appendChildren(mml, [parser.create('node', 'mprescripts'), sub, sup]);
        mml.setProperty('fixPrescript', true);
        parser.Push(mml);
    },
    NewTagForm: function (parser, name, renew) {
        if (renew === void 0) { renew = false; }
        var tags = parser.tags;
        if (!('mtFormats' in tags)) {
            throw new TexError_js_1.default('TagsNotMT', '%1 can only be used with ams or mathtools tags', name);
        }
        var id = parser.GetArgument(name).trim();
        if (!id) {
            throw new TexError_js_1.default('InvalidTagFormID', 'Tag form name can\'t be empty');
        }
        var format = parser.GetBrackets(name, '');
        var left = parser.GetArgument(name);
        var right = parser.GetArgument(name);
        if (!renew && tags.mtFormats.has(id)) {
            throw new TexError_js_1.default('DuplicateTagForm', 'Duplicate tag form: %1', id);
        }
        tags.mtFormats.set(id, [left, right, format]);
    },
    UseTagForm: function (parser, name) {
        var tags = parser.tags;
        if (!('mtFormats' in tags)) {
            throw new TexError_js_1.default('TagsNotMT', '%1 can only be used with ams or mathtools tags', name);
        }
        var id = parser.GetArgument(name).trim();
        if (!id) {
            tags.mtCurrent = null;
            return;
        }
        if (!tags.mtFormats.has(id)) {
            throw new TexError_js_1.default('UndefinedTagForm', 'Undefined tag form: %1', id);
        }
        tags.mtCurrent = tags.mtFormats.get(id);
    },
    SetOptions: function (parser, name) {
        var e_2, _a;
        var options = parser.options.mathtools;
        if (!options['allow-mathtoolsset']) {
            throw new TexError_js_1.default('ForbiddenMathtoolsSet', '%1 is disabled', name);
        }
        var allowed = {};
        Object.keys(options).forEach(function (id) {
            if (id !== 'pariedDelimiters' && id !== 'tagforms' && id !== 'allow-mathtoolsset') {
                allowed[id] = 1;
            }
        });
        var args = parser.GetArgument(name);
        var keys = ParseUtil_js_1.default.keyvalOptions(args, allowed, true);
        try {
            for (var _b = __values(Object.keys(keys)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var id = _c.value;
                options[id] = keys[id];
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_2) throw e_2.error; }
        }
    },
    Array: BaseMethods_js_1.default.Array,
    Macro: BaseMethods_js_1.default.Macro,
    xArrow: AmsMethods_js_1.AmsMethods.xArrow,
    HandleRef: AmsMethods_js_1.AmsMethods.HandleRef,
    AmsEqnArray: AmsMethods_js_1.AmsMethods.AmsEqnArray,
    MacroWithTemplate: NewcommandMethods_js_1.default.MacroWithTemplate,
};
//# sourceMappingURL=MathtoolsMethods.js.map

/***/ }),

/***/ 298:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MathtoolsTagFormat = void 0;
var TexError_js_1 = __importDefault(__webpack_require__(402));
var Tags_js_1 = __webpack_require__(680);
var tagID = 0;
function MathtoolsTagFormat(config, jax) {
    var tags = jax.parseOptions.options.tags;
    if (tags !== 'base' && config.tags.hasOwnProperty(tags)) {
        Tags_js_1.TagsFactory.add(tags, config.tags[tags]);
    }
    var TagClass = Tags_js_1.TagsFactory.create(jax.parseOptions.options.tags).constructor;
    var TagFormat = (function (_super) {
        __extends(TagFormat, _super);
        function TagFormat() {
            var e_1, _a;
            var _this = _super.call(this) || this;
            _this.mtFormats = new Map();
            _this.mtCurrent = null;
            var forms = jax.parseOptions.options.mathtools.tagforms;
            try {
                for (var _b = __values(Object.keys(forms)), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var form = _c.value;
                    if (!Array.isArray(forms[form]) || forms[form].length !== 3) {
                        throw new TexError_js_1.default('InvalidTagFormDef', 'The tag form definition for "%1" should be an array fo three strings', form);
                    }
                    _this.mtFormats.set(form, forms[form]);
                }
            }
            catch (e_1_1) { e_1 = { error: e_1_1 }; }
            finally {
                try {
                    if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
                }
                finally { if (e_1) throw e_1.error; }
            }
            return _this;
        }
        TagFormat.prototype.formatTag = function (tag) {
            if (this.mtCurrent) {
                var _a = __read(this.mtCurrent, 3), left = _a[0], right = _a[1], format = _a[2];
                return (format ? "".concat(left).concat(format, "{").concat(tag, "}").concat(right) : "".concat(left).concat(tag).concat(right));
            }
            return _super.prototype.formatTag.call(this, tag);
        };
        return TagFormat;
    }(TagClass));
    tagID++;
    var tagName = 'MathtoolsTags-' + tagID;
    Tags_js_1.TagsFactory.add(tagName, TagFormat);
    jax.parseOptions.options.tags = tagName;
}
exports.MathtoolsTagFormat = MathtoolsTagFormat;
//# sourceMappingURL=MathtoolsTags.js.map

/***/ }),

/***/ 262:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MathtoolsUtil = void 0;
var BaseItems_js_1 = __webpack_require__(935);
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var TexParser_js_1 = __importDefault(__webpack_require__(193));
var TexError_js_1 = __importDefault(__webpack_require__(402));
var Symbol_js_1 = __webpack_require__(924);
var Options_js_1 = __webpack_require__(74);
var MathtoolsMethods_js_1 = __webpack_require__(178);
var MathtoolsConfiguration_js_1 = __webpack_require__(205);
exports.MathtoolsUtil = {
    setDisplayLevel: function (mml, style) {
        if (!style)
            return;
        var _a = __read((0, Options_js_1.lookup)(style, {
            '\\displaystyle': [true, 0],
            '\\textstyle': [false, 0],
            '\\scriptstyle': [false, 1],
            '\\scriptscriptstyle': [false, 2]
        }, [null, null]), 2), display = _a[0], script = _a[1];
        if (display !== null) {
            mml.attributes.set('displaystyle', display);
            mml.attributes.set('scriptlevel', script);
        }
    },
    checkAlignment: function (parser, name) {
        var top = parser.stack.Top();
        if (top.kind !== BaseItems_js_1.EqnArrayItem.prototype.kind) {
            throw new TexError_js_1.default('NotInAlignment', '%1 can only be used in aligment environments', name);
        }
        return top;
    },
    addPairedDelims: function (config, cs, args) {
        var delims = config.handlers.retrieve(MathtoolsConfiguration_js_1.PAIREDDELIMS);
        delims.add(cs, new Symbol_js_1.Macro(cs, MathtoolsMethods_js_1.MathtoolsMethods.PairedDelimiters, args));
    },
    spreadLines: function (mtable, spread) {
        if (!mtable.isKind('mtable'))
            return;
        var rowspacing = mtable.attributes.get('rowspacing');
        if (rowspacing) {
            var add_1 = ParseUtil_js_1.default.dimen2em(spread);
            rowspacing = rowspacing
                .split(/ /)
                .map(function (s) { return ParseUtil_js_1.default.Em(Math.max(0, ParseUtil_js_1.default.dimen2em(s) + add_1)); })
                .join(' ');
        }
        else {
            rowspacing = spread;
        }
        mtable.attributes.set('rowspacing', rowspacing);
    },
    plusOrMinus: function (name, n) {
        n = n.trim();
        if (!n.match(/^[-+]?(?:\d+(?:\.\d*)?|\.\d+)$/)) {
            throw new TexError_js_1.default('NotANumber', 'Argument to %1 is not a number', name);
        }
        return (n.match(/^[-+]/) ? n : '+' + n);
    },
    getScript: function (parser, name, pos) {
        var arg = ParseUtil_js_1.default.trimSpaces(parser.GetArgument(name));
        if (arg === '') {
            return parser.create('node', 'none');
        }
        var format = parser.options.mathtools["prescript-".concat(pos, "-format")];
        format && (arg = "".concat(format, "{").concat(arg, "}"));
        return new TexParser_js_1.default(arg, parser.stack.env, parser.configuration).mml();
    }
};
//# sourceMappingURL=MathtoolsUtil.js.map

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

/***/ 74:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.isObject = MathJax._.util.Options.isObject;
exports.APPEND = MathJax._.util.Options.APPEND;
exports.REMOVE = MathJax._.util.Options.REMOVE;
exports.OPTIONS = MathJax._.util.Options.OPTIONS;
exports.Expandable = MathJax._.util.Options.Expandable;
exports.expandable = MathJax._.util.Options.expandable;
exports.makeArray = MathJax._.util.Options.makeArray;
exports.keys = MathJax._.util.Options.keys;
exports.copy = MathJax._.util.Options.copy;
exports.insert = MathJax._.util.Options.insert;
exports.defaultOptions = MathJax._.util.Options.defaultOptions;
exports.userOptions = MathJax._.util.Options.userOptions;
exports.selectOptions = MathJax._.util.Options.selectOptions;
exports.selectOptionsFromKeys = MathJax._.util.Options.selectOptionsFromKeys;
exports.separateOptions = MathJax._.util.Options.separateOptions;
exports.lookup = MathJax._.util.Options.lookup;

/***/ }),

/***/ 230:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.BIGDIMEN = MathJax._.util.lengths.BIGDIMEN;
exports.UNITS = MathJax._.util.lengths.UNITS;
exports.RELUNITS = MathJax._.util.lengths.RELUNITS;
exports.MATHSPACE = MathJax._.util.lengths.MATHSPACE;
exports.length2em = MathJax._.util.lengths.length2em;
exports.percent = MathJax._.util.lengths.percent;
exports.em = MathJax._.util.lengths.em;
exports.emRounded = MathJax._.util.lengths.emRounded;
exports.px = MathJax._.util.lengths.px;

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

/***/ 398:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.ParseUtil["default"];

/***/ }),

/***/ 924:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Symbol = MathJax._.input.tex.Symbol.Symbol;
exports.Macro = MathJax._.input.tex.Symbol.Macro;

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

/***/ 680:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Label = MathJax._.input.tex.Tags.Label;
exports.TagInfo = MathJax._.input.tex.Tags.TagInfo;
exports.AbstractTags = MathJax._.input.tex.Tags.AbstractTags;
exports.NoTags = MathJax._.input.tex.Tags.NoTags;
exports.AllTags = MathJax._.input.tex.Tags.AllTags;
exports.TagsFactory = MathJax._.input.tex.Tags.TagsFactory;

/***/ }),

/***/ 108:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.TexConstant = MathJax._.input.tex.TexConstants.TexConstant;

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

/***/ }),

/***/ 360:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.base.BaseMethods["default"];

/***/ }),

/***/ 927:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MultlineItem = MathJax._.input.tex.ams.AmsItems.MultlineItem;
exports.FlalignItem = MathJax._.input.tex.ams.AmsItems.FlalignItem;

/***/ }),

/***/ 939:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AmsMethods = MathJax._.input.tex.ams.AmsMethods.AmsMethods;
exports.NEW_OPS = MathJax._.input.tex.ams.AmsMethods.NEW_OPS;

/***/ }),

/***/ 432:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.newcommand.NewcommandMethods["default"];

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/mathtools/MathtoolsConfiguration.js
var MathtoolsConfiguration = __webpack_require__(205);
// EXTERNAL MODULE: ../../../../../../js/input/tex/mathtools/MathtoolsItems.js
var MathtoolsItems = __webpack_require__(144);
// EXTERNAL MODULE: ../../../../../../js/input/tex/mathtools/MathtoolsMethods.js
var MathtoolsMethods = __webpack_require__(178);
// EXTERNAL MODULE: ../../../../../../js/input/tex/mathtools/MathtoolsTags.js
var MathtoolsTags = __webpack_require__(298);
// EXTERNAL MODULE: ../../../../../../js/input/tex/mathtools/MathtoolsUtil.js
var MathtoolsUtil = __webpack_require__(262);
;// CONCATENATED MODULE: ./lib/mathtools.js








if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/mathtools', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        mathtools: {
          MathtoolsConfiguration: MathtoolsConfiguration,
          MathtoolsItems: MathtoolsItems,
          MathtoolsMethods: MathtoolsMethods,
          MathtoolsTags: MathtoolsTags,
          MathtoolsUtil: MathtoolsUtil
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./mathtools.js

}();
/******/ })()
;