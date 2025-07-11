/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 7306:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;

__webpack_unused_export__ = ({ value: true });
exports.q = void 0;
exports.q = '3.2.2';
//# sourceMappingURL=version.js.map

/***/ }),

/***/ 9250:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.FontData = exports.NOSTRETCH = exports.H = exports.V = void 0;
var Options_js_1 = __webpack_require__(9077);
exports.V = 1;
exports.H = 2;
exports.NOSTRETCH = { dir: 0 };
var FontData = (function () {
    function FontData(options) {
        var e_1, _a, e_2, _b;
        if (options === void 0) { options = null; }
        this.variant = {};
        this.delimiters = {};
        this.cssFontMap = {};
        this.remapChars = {};
        this.skewIcFactor = .75;
        var CLASS = this.constructor;
        this.options = (0, Options_js_1.userOptions)((0, Options_js_1.defaultOptions)({}, CLASS.OPTIONS), options);
        this.params = __assign({}, CLASS.defaultParams);
        this.sizeVariants = __spreadArray([], __read(CLASS.defaultSizeVariants), false);
        this.stretchVariants = __spreadArray([], __read(CLASS.defaultStretchVariants), false);
        this.cssFontMap = __assign({}, CLASS.defaultCssFonts);
        try {
            for (var _c = __values(Object.keys(this.cssFontMap)), _d = _c.next(); !_d.done; _d = _c.next()) {
                var name_1 = _d.value;
                if (this.cssFontMap[name_1][0] === 'unknown') {
                    this.cssFontMap[name_1][0] = this.options.unknownFamily;
                }
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_1) throw e_1.error; }
        }
        this.cssFamilyPrefix = CLASS.defaultCssFamilyPrefix;
        this.createVariants(CLASS.defaultVariants);
        this.defineDelimiters(CLASS.defaultDelimiters);
        try {
            for (var _e = __values(Object.keys(CLASS.defaultChars)), _f = _e.next(); !_f.done; _f = _e.next()) {
                var name_2 = _f.value;
                this.defineChars(name_2, CLASS.defaultChars[name_2]);
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_f && !_f.done && (_b = _e.return)) _b.call(_e);
            }
            finally { if (e_2) throw e_2.error; }
        }
        this.defineRemap('accent', CLASS.defaultAccentMap);
        this.defineRemap('mo', CLASS.defaultMoMap);
        this.defineRemap('mn', CLASS.defaultMnMap);
    }
    FontData.charOptions = function (font, n) {
        var char = font[n];
        if (char.length === 3) {
            char[3] = {};
        }
        return char[3];
    };
    Object.defineProperty(FontData.prototype, "styles", {
        get: function () {
            return this._styles;
        },
        set: function (style) {
            this._styles = style;
        },
        enumerable: false,
        configurable: true
    });
    FontData.prototype.createVariant = function (name, inherit, link) {
        if (inherit === void 0) { inherit = null; }
        if (link === void 0) { link = null; }
        var variant = {
            linked: [],
            chars: (inherit ? Object.create(this.variant[inherit].chars) : {})
        };
        if (link && this.variant[link]) {
            Object.assign(variant.chars, this.variant[link].chars);
            this.variant[link].linked.push(variant.chars);
            variant.chars = Object.create(variant.chars);
        }
        this.remapSmpChars(variant.chars, name);
        this.variant[name] = variant;
    };
    FontData.prototype.remapSmpChars = function (chars, name) {
        var e_3, _a, e_4, _b;
        var CLASS = this.constructor;
        if (CLASS.VariantSmp[name]) {
            var SmpRemap = CLASS.SmpRemap;
            var SmpGreek = [null, null, CLASS.SmpRemapGreekU, CLASS.SmpRemapGreekL];
            try {
                for (var _c = __values(CLASS.SmpRanges), _d = _c.next(); !_d.done; _d = _c.next()) {
                    var _e = __read(_d.value, 3), i = _e[0], lo = _e[1], hi = _e[2];
                    var base = CLASS.VariantSmp[name][i];
                    if (!base)
                        continue;
                    for (var n = lo; n <= hi; n++) {
                        if (n === 0x3A2)
                            continue;
                        var smp = base + n - lo;
                        chars[n] = this.smpChar(SmpRemap[smp] || smp);
                    }
                    if (SmpGreek[i]) {
                        try {
                            for (var _f = (e_4 = void 0, __values(Object.keys(SmpGreek[i]).map(function (x) { return parseInt(x); }))), _g = _f.next(); !_g.done; _g = _f.next()) {
                                var n = _g.value;
                                chars[n] = this.smpChar(base + SmpGreek[i][n]);
                            }
                        }
                        catch (e_4_1) { e_4 = { error: e_4_1 }; }
                        finally {
                            try {
                                if (_g && !_g.done && (_b = _f.return)) _b.call(_f);
                            }
                            finally { if (e_4) throw e_4.error; }
                        }
                    }
                }
            }
            catch (e_3_1) { e_3 = { error: e_3_1 }; }
            finally {
                try {
                    if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
                }
                finally { if (e_3) throw e_3.error; }
            }
        }
        if (name === 'bold') {
            chars[0x3DC] = this.smpChar(0x1D7CA);
            chars[0x3DD] = this.smpChar(0x1D7CB);
        }
    };
    FontData.prototype.smpChar = function (n) {
        return [, , , { smp: n }];
    };
    FontData.prototype.createVariants = function (variants) {
        var e_5, _a;
        try {
            for (var variants_1 = __values(variants), variants_1_1 = variants_1.next(); !variants_1_1.done; variants_1_1 = variants_1.next()) {
                var variant = variants_1_1.value;
                this.createVariant(variant[0], variant[1], variant[2]);
            }
        }
        catch (e_5_1) { e_5 = { error: e_5_1 }; }
        finally {
            try {
                if (variants_1_1 && !variants_1_1.done && (_a = variants_1.return)) _a.call(variants_1);
            }
            finally { if (e_5) throw e_5.error; }
        }
    };
    FontData.prototype.defineChars = function (name, chars) {
        var e_6, _a;
        var variant = this.variant[name];
        Object.assign(variant.chars, chars);
        try {
            for (var _b = __values(variant.linked), _c = _b.next(); !_c.done; _c = _b.next()) {
                var link = _c.value;
                Object.assign(link, chars);
            }
        }
        catch (e_6_1) { e_6 = { error: e_6_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_6) throw e_6.error; }
        }
    };
    FontData.prototype.defineDelimiters = function (delims) {
        Object.assign(this.delimiters, delims);
    };
    FontData.prototype.defineRemap = function (name, remap) {
        if (!this.remapChars.hasOwnProperty(name)) {
            this.remapChars[name] = {};
        }
        Object.assign(this.remapChars[name], remap);
    };
    FontData.prototype.getDelimiter = function (n) {
        return this.delimiters[n];
    };
    FontData.prototype.getSizeVariant = function (n, i) {
        if (this.delimiters[n].variants) {
            i = this.delimiters[n].variants[i];
        }
        return this.sizeVariants[i];
    };
    FontData.prototype.getStretchVariant = function (n, i) {
        return this.stretchVariants[this.delimiters[n].stretchv ? this.delimiters[n].stretchv[i] : 0];
    };
    FontData.prototype.getChar = function (name, n) {
        return this.variant[name].chars[n];
    };
    FontData.prototype.getVariant = function (name) {
        return this.variant[name];
    };
    FontData.prototype.getCssFont = function (variant) {
        return this.cssFontMap[variant] || ['serif', false, false];
    };
    FontData.prototype.getFamily = function (family) {
        return (this.cssFamilyPrefix ? this.cssFamilyPrefix + ', ' + family : family);
    };
    FontData.prototype.getRemappedChar = function (name, c) {
        var map = this.remapChars[name] || {};
        return map[c];
    };
    FontData.OPTIONS = {
        unknownFamily: 'serif'
    };
    FontData.JAX = 'common';
    FontData.NAME = '';
    FontData.defaultVariants = [
        ['normal'],
        ['bold', 'normal'],
        ['italic', 'normal'],
        ['bold-italic', 'italic', 'bold'],
        ['double-struck', 'bold'],
        ['fraktur', 'normal'],
        ['bold-fraktur', 'bold', 'fraktur'],
        ['script', 'italic'],
        ['bold-script', 'bold-italic', 'script'],
        ['sans-serif', 'normal'],
        ['bold-sans-serif', 'bold', 'sans-serif'],
        ['sans-serif-italic', 'italic', 'sans-serif'],
        ['sans-serif-bold-italic', 'bold-italic', 'bold-sans-serif'],
        ['monospace', 'normal']
    ];
    FontData.defaultCssFonts = {
        normal: ['unknown', false, false],
        bold: ['unknown', false, true],
        italic: ['unknown', true, false],
        'bold-italic': ['unknown', true, true],
        'double-struck': ['unknown', false, true],
        fraktur: ['unknown', false, false],
        'bold-fraktur': ['unknown', false, true],
        script: ['cursive', false, false],
        'bold-script': ['cursive', false, true],
        'sans-serif': ['sans-serif', false, false],
        'bold-sans-serif': ['sans-serif', false, true],
        'sans-serif-italic': ['sans-serif', true, false],
        'sans-serif-bold-italic': ['sans-serif', true, true],
        monospace: ['monospace', false, false]
    };
    FontData.defaultCssFamilyPrefix = '';
    FontData.VariantSmp = {
        bold: [0x1D400, 0x1D41A, 0x1D6A8, 0x1D6C2, 0x1D7CE],
        italic: [0x1D434, 0x1D44E, 0x1D6E2, 0x1D6FC],
        'bold-italic': [0x1D468, 0x1D482, 0x1D71C, 0x1D736],
        script: [0x1D49C, 0x1D4B6],
        'bold-script': [0x1D4D0, 0x1D4EA],
        fraktur: [0x1D504, 0x1D51E],
        'double-struck': [0x1D538, 0x1D552, , , 0x1D7D8],
        'bold-fraktur': [0x1D56C, 0x1D586],
        'sans-serif': [0x1D5A0, 0x1D5BA, , , 0x1D7E2],
        'bold-sans-serif': [0x1D5D4, 0x1D5EE, 0x1D756, 0x1D770, 0x1D7EC],
        'sans-serif-italic': [0x1D608, 0x1D622],
        'sans-serif-bold-italic': [0x1D63C, 0x1D656, 0x1D790, 0x1D7AA],
        'monospace': [0x1D670, 0x1D68A, , , 0x1D7F6]
    };
    FontData.SmpRanges = [
        [0, 0x41, 0x5A],
        [1, 0x61, 0x7A],
        [2, 0x391, 0x3A9],
        [3, 0x3B1, 0x3C9],
        [4, 0x30, 0x39]
    ];
    FontData.SmpRemap = {
        0x1D455: 0x210E,
        0x1D49D: 0x212C,
        0x1D4A0: 0x2130,
        0x1D4A1: 0x2131,
        0x1D4A3: 0x210B,
        0x1D4A4: 0x2110,
        0x1D4A7: 0x2112,
        0x1D4A8: 0x2133,
        0x1D4AD: 0x211B,
        0x1D4BA: 0x212F,
        0x1D4BC: 0x210A,
        0x1D4C4: 0x2134,
        0x1D506: 0x212D,
        0x1D50B: 0x210C,
        0x1D50C: 0x2111,
        0x1D515: 0x211C,
        0x1D51D: 0x2128,
        0x1D53A: 0x2102,
        0x1D53F: 0x210D,
        0x1D545: 0x2115,
        0x1D547: 0x2119,
        0x1D548: 0x211A,
        0x1D549: 0x211D,
        0x1D551: 0x2124,
    };
    FontData.SmpRemapGreekU = {
        0x2207: 0x19,
        0x03F4: 0x11
    };
    FontData.SmpRemapGreekL = {
        0x3D1: 0x1B,
        0x3D5: 0x1D,
        0x3D6: 0x1F,
        0x3F0: 0x1C,
        0x3F1: 0x1E,
        0x3F5: 0x1A,
        0x2202: 0x19
    };
    FontData.defaultAccentMap = {
        0x0300: '\u02CB',
        0x0301: '\u02CA',
        0x0302: '\u02C6',
        0x0303: '\u02DC',
        0x0304: '\u02C9',
        0x0306: '\u02D8',
        0x0307: '\u02D9',
        0x0308: '\u00A8',
        0x030A: '\u02DA',
        0x030C: '\u02C7',
        0x2192: '\u20D7',
        0x2032: '\'',
        0x2033: '\'\'',
        0x2034: '\'\'\'',
        0x2035: '`',
        0x2036: '``',
        0x2037: '```',
        0x2057: '\'\'\'\'',
        0x20D0: '\u21BC',
        0x20D1: '\u21C0',
        0x20D6: '\u2190',
        0x20E1: '\u2194',
        0x20F0: '*',
        0x20DB: '...',
        0x20DC: '....',
        0x20EC: '\u21C1',
        0x20ED: '\u21BD',
        0x20EE: '\u2190',
        0x20EF: '\u2192'
    };
    FontData.defaultMoMap = {
        0x002D: '\u2212'
    };
    FontData.defaultMnMap = {
        0x002D: '\u2212'
    };
    FontData.defaultParams = {
        x_height: .442,
        quad: 1,
        num1: .676,
        num2: .394,
        num3: .444,
        denom1: .686,
        denom2: .345,
        sup1: .413,
        sup2: .363,
        sup3: .289,
        sub1: .15,
        sub2: .247,
        sup_drop: .386,
        sub_drop: .05,
        delim1: 2.39,
        delim2: 1.0,
        axis_height: .25,
        rule_thickness: .06,
        big_op_spacing1: .111,
        big_op_spacing2: .167,
        big_op_spacing3: .2,
        big_op_spacing4: .6,
        big_op_spacing5: .1,
        surd_height: .075,
        scriptspace: .05,
        nulldelimiterspace: .12,
        delimiterfactor: 901,
        delimitershortfall: .3,
        min_rule_thickness: 1.25,
        separation_factor: 1.75,
        extra_ic: .033
    };
    FontData.defaultDelimiters = {};
    FontData.defaultChars = {};
    FontData.defaultSizeVariants = [];
    FontData.defaultStretchVariants = [];
    return FontData;
}());
exports.FontData = FontData;
//# sourceMappingURL=FontData.js.map

/***/ }),

/***/ 5373:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonArrow = exports.CommonDiagonalArrow = exports.CommonDiagonalStrike = exports.CommonBorder2 = exports.CommonBorder = exports.arrowBBox = exports.diagonalArrowDef = exports.arrowDef = exports.arrowBBoxW = exports.arrowBBoxHD = exports.arrowHead = exports.fullBorder = exports.fullPadding = exports.fullBBox = exports.sideNames = exports.sideIndex = exports.SOLID = exports.PADDING = exports.THICKNESS = exports.ARROWY = exports.ARROWDX = exports.ARROWX = void 0;
exports.ARROWX = 4, exports.ARROWDX = 1, exports.ARROWY = 2;
exports.THICKNESS = .067;
exports.PADDING = .2;
exports.SOLID = exports.THICKNESS + 'em solid';
exports.sideIndex = { top: 0, right: 1, bottom: 2, left: 3 };
exports.sideNames = Object.keys(exports.sideIndex);
exports.fullBBox = (function (node) { return new Array(4).fill(node.thickness + node.padding); });
exports.fullPadding = (function (node) { return new Array(4).fill(node.padding); });
exports.fullBorder = (function (node) { return new Array(4).fill(node.thickness); });
var arrowHead = function (node) {
    return Math.max(node.padding, node.thickness * (node.arrowhead.x + node.arrowhead.dx + 1));
};
exports.arrowHead = arrowHead;
var arrowBBoxHD = function (node, TRBL) {
    if (node.childNodes[0]) {
        var _a = node.childNodes[0].getBBox(), h = _a.h, d = _a.d;
        TRBL[0] = TRBL[2] = Math.max(0, node.thickness * node.arrowhead.y - (h + d) / 2);
    }
    return TRBL;
};
exports.arrowBBoxHD = arrowBBoxHD;
var arrowBBoxW = function (node, TRBL) {
    if (node.childNodes[0]) {
        var w = node.childNodes[0].getBBox().w;
        TRBL[1] = TRBL[3] = Math.max(0, node.thickness * node.arrowhead.y - w / 2);
    }
    return TRBL;
};
exports.arrowBBoxW = arrowBBoxW;
exports.arrowDef = {
    up: [-Math.PI / 2, false, true, 'verticalstrike'],
    down: [Math.PI / 2, false, true, 'verticakstrike'],
    right: [0, false, false, 'horizontalstrike'],
    left: [Math.PI, false, false, 'horizontalstrike'],
    updown: [Math.PI / 2, true, true, 'verticalstrike uparrow downarrow'],
    leftright: [0, true, false, 'horizontalstrike leftarrow rightarrow']
};
exports.diagonalArrowDef = {
    updiagonal: [-1, 0, false, 'updiagonalstrike northeastarrow'],
    northeast: [-1, 0, false, 'updiagonalstrike updiagonalarrow'],
    southeast: [1, 0, false, 'downdiagonalstrike'],
    northwest: [1, Math.PI, false, 'downdiagonalstrike'],
    southwest: [-1, Math.PI, false, 'updiagonalstrike'],
    northeastsouthwest: [-1, 0, true, 'updiagonalstrike northeastarrow updiagonalarrow southwestarrow'],
    northwestsoutheast: [1, 0, true, 'downdiagonalstrike northwestarrow southeastarrow']
};
exports.arrowBBox = {
    up: function (node) { return (0, exports.arrowBBoxW)(node, [(0, exports.arrowHead)(node), 0, node.padding, 0]); },
    down: function (node) { return (0, exports.arrowBBoxW)(node, [node.padding, 0, (0, exports.arrowHead)(node), 0]); },
    right: function (node) { return (0, exports.arrowBBoxHD)(node, [0, (0, exports.arrowHead)(node), 0, node.padding]); },
    left: function (node) { return (0, exports.arrowBBoxHD)(node, [0, node.padding, 0, (0, exports.arrowHead)(node)]); },
    updown: function (node) { return (0, exports.arrowBBoxW)(node, [(0, exports.arrowHead)(node), 0, (0, exports.arrowHead)(node), 0]); },
    leftright: function (node) { return (0, exports.arrowBBoxHD)(node, [0, (0, exports.arrowHead)(node), 0, (0, exports.arrowHead)(node)]); }
};
var CommonBorder = function (render) {
    return function (side) {
        var i = exports.sideIndex[side];
        return [side, {
                renderer: render,
                bbox: function (node) {
                    var bbox = [0, 0, 0, 0];
                    bbox[i] = node.thickness + node.padding;
                    return bbox;
                },
                border: function (node) {
                    var bbox = [0, 0, 0, 0];
                    bbox[i] = node.thickness;
                    return bbox;
                }
            }];
    };
};
exports.CommonBorder = CommonBorder;
var CommonBorder2 = function (render) {
    return function (name, side1, side2) {
        var i1 = exports.sideIndex[side1];
        var i2 = exports.sideIndex[side2];
        return [name, {
                renderer: render,
                bbox: function (node) {
                    var t = node.thickness + node.padding;
                    var bbox = [0, 0, 0, 0];
                    bbox[i1] = bbox[i2] = t;
                    return bbox;
                },
                border: function (node) {
                    var bbox = [0, 0, 0, 0];
                    bbox[i1] = bbox[i2] = node.thickness;
                    return bbox;
                },
                remove: side1 + ' ' + side2
            }];
    };
};
exports.CommonBorder2 = CommonBorder2;
var CommonDiagonalStrike = function (render) {
    return function (name) {
        var cname = 'mjx-' + name.charAt(0) + 'strike';
        return [name + 'diagonalstrike', {
                renderer: render(cname),
                bbox: exports.fullBBox
            }];
    };
};
exports.CommonDiagonalStrike = CommonDiagonalStrike;
var CommonDiagonalArrow = function (render) {
    return function (name) {
        var _a = __read(exports.diagonalArrowDef[name], 4), c = _a[0], pi = _a[1], double = _a[2], remove = _a[3];
        return [name + 'arrow', {
                renderer: function (node, _child) {
                    var _a = __read(node.arrowAW(), 2), a = _a[0], W = _a[1];
                    var arrow = node.arrow(W, c * (a - pi), double);
                    render(node, arrow);
                },
                bbox: function (node) {
                    var _a = node.arrowData(), a = _a.a, x = _a.x, y = _a.y;
                    var _b = __read([node.arrowhead.x, node.arrowhead.y, node.arrowhead.dx], 3), ax = _b[0], ay = _b[1], adx = _b[2];
                    var _c = __read(node.getArgMod(ax + adx, ay), 2), b = _c[0], ar = _c[1];
                    var dy = y + (b > a ? node.thickness * ar * Math.sin(b - a) : 0);
                    var dx = x + (b > Math.PI / 2 - a ? node.thickness * ar * Math.sin(b + a - Math.PI / 2) : 0);
                    return [dy, dx, dy, dx];
                },
                remove: remove
            }];
    };
};
exports.CommonDiagonalArrow = CommonDiagonalArrow;
var CommonArrow = function (render) {
    return function (name) {
        var _a = __read(exports.arrowDef[name], 4), angle = _a[0], double = _a[1], isVertical = _a[2], remove = _a[3];
        return [name + 'arrow', {
                renderer: function (node, _child) {
                    var _a = node.getBBox(), w = _a.w, h = _a.h, d = _a.d;
                    var _b = __read((isVertical ? [h + d, 'X'] : [w, 'Y']), 2), W = _b[0], offset = _b[1];
                    var dd = node.getOffset(offset);
                    var arrow = node.arrow(W, angle, double, offset, dd);
                    render(node, arrow);
                },
                bbox: exports.arrowBBox[name],
                remove: remove
            }];
    };
};
exports.CommonArrow = CommonArrow;
//# sourceMappingURL=Notation.js.map

/***/ }),

/***/ 716:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonOutputJax = void 0;
var OutputJax_js_1 = __webpack_require__(3985);
var MathItem_js_1 = __webpack_require__(4769);
var Options_js_1 = __webpack_require__(9077);
var lengths_js_1 = __webpack_require__(6914);
var Styles_js_1 = __webpack_require__(5878);
var StyleList_js_1 = __webpack_require__(5888);
var CommonOutputJax = (function (_super) {
    __extends(CommonOutputJax, _super);
    function CommonOutputJax(options, defaultFactory, defaultFont) {
        if (options === void 0) { options = null; }
        if (defaultFactory === void 0) { defaultFactory = null; }
        if (defaultFont === void 0) { defaultFont = null; }
        var _this = this;
        var _a = __read((0, Options_js_1.separateOptions)(options, defaultFont.OPTIONS), 2), jaxOptions = _a[0], fontOptions = _a[1];
        _this = _super.call(this, jaxOptions) || this;
        _this.factory = _this.options.wrapperFactory ||
            new defaultFactory();
        _this.factory.jax = _this;
        _this.cssStyles = _this.options.cssStyles || new StyleList_js_1.CssStyles();
        _this.font = _this.options.font || new defaultFont(fontOptions);
        _this.unknownCache = new Map();
        return _this;
    }
    CommonOutputJax.prototype.typeset = function (math, html) {
        this.setDocument(html);
        var node = this.createNode();
        this.toDOM(math, node, html);
        return node;
    };
    CommonOutputJax.prototype.createNode = function () {
        var jax = this.constructor.NAME;
        return this.html('mjx-container', { 'class': 'MathJax', jax: jax });
    };
    CommonOutputJax.prototype.setScale = function (node) {
        var scale = this.math.metrics.scale * this.options.scale;
        if (scale !== 1) {
            this.adaptor.setStyle(node, 'fontSize', (0, lengths_js_1.percent)(scale));
        }
    };
    CommonOutputJax.prototype.toDOM = function (math, node, html) {
        if (html === void 0) { html = null; }
        this.setDocument(html);
        this.math = math;
        this.pxPerEm = math.metrics.ex / this.font.params.x_height;
        math.root.setTeXclass(null);
        this.setScale(node);
        this.nodeMap = new Map();
        this.container = node;
        this.processMath(math.root, node);
        this.nodeMap = null;
        this.executeFilters(this.postFilters, math, html, node);
    };
    CommonOutputJax.prototype.getBBox = function (math, html) {
        this.setDocument(html);
        this.math = math;
        math.root.setTeXclass(null);
        this.nodeMap = new Map();
        var bbox = this.factory.wrap(math.root).getOuterBBox();
        this.nodeMap = null;
        return bbox;
    };
    CommonOutputJax.prototype.getMetrics = function (html) {
        var e_1, _a;
        this.setDocument(html);
        var adaptor = this.adaptor;
        var maps = this.getMetricMaps(html);
        try {
            for (var _b = __values(html.math), _c = _b.next(); !_c.done; _c = _b.next()) {
                var math = _c.value;
                var parent_1 = adaptor.parent(math.start.node);
                if (math.state() < MathItem_js_1.STATE.METRICS && parent_1) {
                    var map = maps[math.display ? 1 : 0];
                    var _d = map.get(parent_1), em = _d.em, ex = _d.ex, containerWidth = _d.containerWidth, lineWidth = _d.lineWidth, scale = _d.scale, family = _d.family;
                    math.setMetrics(em, ex, containerWidth, lineWidth, scale);
                    if (this.options.mtextInheritFont) {
                        math.outputData.mtextFamily = family;
                    }
                    if (this.options.merrorInheritFont) {
                        math.outputData.merrorFamily = family;
                    }
                    math.state(MathItem_js_1.STATE.METRICS);
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
    };
    CommonOutputJax.prototype.getMetricsFor = function (node, display) {
        var getFamily = (this.options.mtextInheritFont || this.options.merrorInheritFont);
        var test = this.getTestElement(node, display);
        var metrics = this.measureMetrics(test, getFamily);
        this.adaptor.remove(test);
        return metrics;
    };
    CommonOutputJax.prototype.getMetricMaps = function (html) {
        var e_2, _a, e_3, _b, e_4, _c, e_5, _d, e_6, _e;
        var adaptor = this.adaptor;
        var domMaps = [new Map(), new Map()];
        try {
            for (var _f = __values(html.math), _g = _f.next(); !_g.done; _g = _f.next()) {
                var math = _g.value;
                var node = adaptor.parent(math.start.node);
                if (node && math.state() < MathItem_js_1.STATE.METRICS) {
                    var map = domMaps[math.display ? 1 : 0];
                    if (!map.has(node)) {
                        map.set(node, this.getTestElement(node, math.display));
                    }
                }
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_g && !_g.done && (_a = _f.return)) _a.call(_f);
            }
            finally { if (e_2) throw e_2.error; }
        }
        var getFamily = this.options.mtextInheritFont || this.options.merrorInheritFont;
        var maps = [new Map(), new Map()];
        try {
            for (var _h = __values(maps.keys()), _j = _h.next(); !_j.done; _j = _h.next()) {
                var i = _j.value;
                try {
                    for (var _k = (e_4 = void 0, __values(domMaps[i].keys())), _l = _k.next(); !_l.done; _l = _k.next()) {
                        var node = _l.value;
                        maps[i].set(node, this.measureMetrics(domMaps[i].get(node), getFamily));
                    }
                }
                catch (e_4_1) { e_4 = { error: e_4_1 }; }
                finally {
                    try {
                        if (_l && !_l.done && (_c = _k.return)) _c.call(_k);
                    }
                    finally { if (e_4) throw e_4.error; }
                }
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (_j && !_j.done && (_b = _h.return)) _b.call(_h);
            }
            finally { if (e_3) throw e_3.error; }
        }
        try {
            for (var _m = __values(maps.keys()), _o = _m.next(); !_o.done; _o = _m.next()) {
                var i = _o.value;
                try {
                    for (var _p = (e_6 = void 0, __values(domMaps[i].values())), _q = _p.next(); !_q.done; _q = _p.next()) {
                        var node = _q.value;
                        adaptor.remove(node);
                    }
                }
                catch (e_6_1) { e_6 = { error: e_6_1 }; }
                finally {
                    try {
                        if (_q && !_q.done && (_e = _p.return)) _e.call(_p);
                    }
                    finally { if (e_6) throw e_6.error; }
                }
            }
        }
        catch (e_5_1) { e_5 = { error: e_5_1 }; }
        finally {
            try {
                if (_o && !_o.done && (_d = _m.return)) _d.call(_m);
            }
            finally { if (e_5) throw e_5.error; }
        }
        return maps;
    };
    CommonOutputJax.prototype.getTestElement = function (node, display) {
        var adaptor = this.adaptor;
        if (!this.testInline) {
            this.testInline = this.html('mjx-test', { style: {
                    display: 'inline-block',
                    width: '100%',
                    'font-style': 'normal',
                    'font-weight': 'normal',
                    'font-size': '100%',
                    'font-size-adjust': 'none',
                    'text-indent': 0,
                    'text-transform': 'none',
                    'letter-spacing': 'normal',
                    'word-spacing': 'normal',
                    overflow: 'hidden',
                    height: '1px',
                    'margin-right': '-1px'
                } }, [
                this.html('mjx-left-box', { style: {
                        display: 'inline-block',
                        width: 0,
                        'float': 'left'
                    } }),
                this.html('mjx-ex-box', { style: {
                        position: 'absolute',
                        overflow: 'hidden',
                        width: '1px', height: '60ex'
                    } }),
                this.html('mjx-right-box', { style: {
                        display: 'inline-block',
                        width: 0,
                        'float': 'right'
                    } })
            ]);
            this.testDisplay = adaptor.clone(this.testInline);
            adaptor.setStyle(this.testDisplay, 'display', 'table');
            adaptor.setStyle(this.testDisplay, 'margin-right', '');
            adaptor.setStyle(adaptor.firstChild(this.testDisplay), 'display', 'none');
            var right = adaptor.lastChild(this.testDisplay);
            adaptor.setStyle(right, 'display', 'table-cell');
            adaptor.setStyle(right, 'width', '10000em');
            adaptor.setStyle(right, 'float', '');
        }
        return adaptor.append(node, adaptor.clone(display ? this.testDisplay : this.testInline));
    };
    CommonOutputJax.prototype.measureMetrics = function (node, getFamily) {
        var adaptor = this.adaptor;
        var family = (getFamily ? adaptor.fontFamily(node) : '');
        var em = adaptor.fontSize(node);
        var _a = __read(adaptor.nodeSize(adaptor.childNode(node, 1)), 2), w = _a[0], h = _a[1];
        var ex = (w ? h / 60 : em * this.options.exFactor);
        var containerWidth = (!w ? 1000000 : adaptor.getStyle(node, 'display') === 'table' ?
            adaptor.nodeSize(adaptor.lastChild(node))[0] - 1 :
            adaptor.nodeBBox(adaptor.lastChild(node)).left -
                adaptor.nodeBBox(adaptor.firstChild(node)).left - 2);
        var scale = Math.max(this.options.minScale, this.options.matchFontHeight ? ex / this.font.params.x_height / em : 1);
        var lineWidth = 1000000;
        return { em: em, ex: ex, containerWidth: containerWidth, lineWidth: lineWidth, scale: scale, family: family };
    };
    CommonOutputJax.prototype.styleSheet = function (html) {
        var e_7, _a;
        this.setDocument(html);
        this.cssStyles.clear();
        this.cssStyles.addStyles(this.constructor.commonStyles);
        if ('getStyles' in html) {
            try {
                for (var _b = __values(html.getStyles()), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var styles = _c.value;
                    this.cssStyles.addStyles(styles);
                }
            }
            catch (e_7_1) { e_7 = { error: e_7_1 }; }
            finally {
                try {
                    if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
                }
                finally { if (e_7) throw e_7.error; }
            }
        }
        this.addWrapperStyles(this.cssStyles);
        this.addFontStyles(this.cssStyles);
        var sheet = this.html('style', { id: 'MJX-styles' }, [this.text('\n' + this.cssStyles.cssText + '\n')]);
        return sheet;
    };
    CommonOutputJax.prototype.addFontStyles = function (styles) {
        styles.addStyles(this.font.styles);
    };
    CommonOutputJax.prototype.addWrapperStyles = function (styles) {
        var e_8, _a;
        try {
            for (var _b = __values(this.factory.getKinds()), _c = _b.next(); !_c.done; _c = _b.next()) {
                var kind = _c.value;
                this.addClassStyles(this.factory.getNodeClass(kind), styles);
            }
        }
        catch (e_8_1) { e_8 = { error: e_8_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_8) throw e_8.error; }
        }
    };
    CommonOutputJax.prototype.addClassStyles = function (CLASS, styles) {
        styles.addStyles(CLASS.styles);
    };
    CommonOutputJax.prototype.setDocument = function (html) {
        if (html) {
            this.document = html;
            this.adaptor.document = html.document;
        }
    };
    CommonOutputJax.prototype.html = function (type, def, content, ns) {
        if (def === void 0) { def = {}; }
        if (content === void 0) { content = []; }
        return this.adaptor.node(type, def, content, ns);
    };
    CommonOutputJax.prototype.text = function (text) {
        return this.adaptor.text(text);
    };
    CommonOutputJax.prototype.fixed = function (m, n) {
        if (n === void 0) { n = 3; }
        if (Math.abs(m) < .0006) {
            return '0';
        }
        return m.toFixed(n).replace(/\.?0+$/, '');
    };
    CommonOutputJax.prototype.measureText = function (text, variant, font) {
        if (font === void 0) { font = ['', false, false]; }
        var node = this.unknownText(text, variant);
        if (variant === '-explicitFont') {
            var styles = this.cssFontStyles(font);
            this.adaptor.setAttributes(node, { style: styles });
        }
        return this.measureTextNodeWithCache(node, text, variant, font);
    };
    CommonOutputJax.prototype.measureTextNodeWithCache = function (text, chars, variant, font) {
        if (font === void 0) { font = ['', false, false]; }
        if (variant === '-explicitFont') {
            variant = [font[0], font[1] ? 'T' : 'F', font[2] ? 'T' : 'F', ''].join('-');
        }
        if (!this.unknownCache.has(variant)) {
            this.unknownCache.set(variant, new Map());
        }
        var map = this.unknownCache.get(variant);
        var cached = map.get(chars);
        if (cached)
            return cached;
        var bbox = this.measureTextNode(text);
        map.set(chars, bbox);
        return bbox;
    };
    CommonOutputJax.prototype.measureXMLnode = function (xml) {
        var adaptor = this.adaptor;
        var content = this.html('mjx-xml-block', { style: { display: 'inline-block' } }, [adaptor.clone(xml)]);
        var base = this.html('mjx-baseline', { style: { display: 'inline-block', width: 0, height: 0 } });
        var style = {
            position: 'absolute',
            display: 'inline-block',
            'font-family': 'initial',
            'line-height': 'normal'
        };
        var node = this.html('mjx-measure-xml', { style: style }, [base, content]);
        adaptor.append(adaptor.parent(this.math.start.node), this.container);
        adaptor.append(this.container, node);
        var em = this.math.metrics.em * this.math.metrics.scale;
        var _a = adaptor.nodeBBox(content), left = _a.left, right = _a.right, bottom = _a.bottom, top = _a.top;
        var w = (right - left) / em;
        var h = (adaptor.nodeBBox(base).top - top) / em;
        var d = (bottom - top) / em - h;
        adaptor.remove(this.container);
        adaptor.remove(node);
        return { w: w, h: h, d: d };
    };
    CommonOutputJax.prototype.cssFontStyles = function (font, styles) {
        if (styles === void 0) { styles = {}; }
        var _a = __read(font, 3), family = _a[0], italic = _a[1], bold = _a[2];
        styles['font-family'] = this.font.getFamily(family);
        if (italic)
            styles['font-style'] = 'italic';
        if (bold)
            styles['font-weight'] = 'bold';
        return styles;
    };
    CommonOutputJax.prototype.getFontData = function (styles) {
        if (!styles) {
            styles = new Styles_js_1.Styles();
        }
        return [this.font.getFamily(styles.get('font-family')),
            styles.get('font-style') === 'italic',
            styles.get('font-weight') === 'bold'];
    };
    CommonOutputJax.NAME = 'Common';
    CommonOutputJax.OPTIONS = __assign(__assign({}, OutputJax_js_1.AbstractOutputJax.OPTIONS), { scale: 1, minScale: .5, mtextInheritFont: false, merrorInheritFont: false, mtextFont: '', merrorFont: 'serif', mathmlSpacing: false, skipAttributes: {}, exFactor: .5, displayAlign: 'center', displayIndent: '0', wrapperFactory: null, font: null, cssStyles: null });
    CommonOutputJax.commonStyles = {};
    return CommonOutputJax;
}(OutputJax_js_1.AbstractOutputJax));
exports.CommonOutputJax = CommonOutputJax;
//# sourceMappingURL=OutputJax.js.map

/***/ }),

/***/ 1541:
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
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonWrapper = void 0;
var Wrapper_js_1 = __webpack_require__(9879);
var MmlNode_js_1 = __webpack_require__(8921);
var string_js_1 = __webpack_require__(6720);
var LENGTHS = __importStar(__webpack_require__(6914));
var Styles_js_1 = __webpack_require__(5878);
var BBox_js_1 = __webpack_require__(3717);
var FontData_js_1 = __webpack_require__(9250);
var SMALLSIZE = 2 / 18;
function MathMLSpace(script, size) {
    return (script ? size < SMALLSIZE ? 0 : SMALLSIZE : size);
}
var CommonWrapper = (function (_super) {
    __extends(CommonWrapper, _super);
    function CommonWrapper(factory, node, parent) {
        if (parent === void 0) { parent = null; }
        var _this = _super.call(this, factory, node) || this;
        _this.parent = null;
        _this.removedStyles = null;
        _this.styles = null;
        _this.variant = '';
        _this.bboxComputed = false;
        _this.stretch = FontData_js_1.NOSTRETCH;
        _this.font = null;
        _this.parent = parent;
        _this.font = factory.jax.font;
        _this.bbox = BBox_js_1.BBox.zero();
        _this.getStyles();
        _this.getVariant();
        _this.getScale();
        _this.getSpace();
        _this.childNodes = node.childNodes.map(function (child) {
            var wrapped = _this.wrap(child);
            if (wrapped.bbox.pwidth && (node.notParent || node.isKind('math'))) {
                _this.bbox.pwidth = BBox_js_1.BBox.fullWidth;
            }
            return wrapped;
        });
        return _this;
    }
    Object.defineProperty(CommonWrapper.prototype, "jax", {
        get: function () {
            return this.factory.jax;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(CommonWrapper.prototype, "adaptor", {
        get: function () {
            return this.factory.jax.adaptor;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(CommonWrapper.prototype, "metrics", {
        get: function () {
            return this.factory.jax.math.metrics;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(CommonWrapper.prototype, "fixesPWidth", {
        get: function () {
            return !this.node.notParent && !this.node.isToken;
        },
        enumerable: false,
        configurable: true
    });
    CommonWrapper.prototype.wrap = function (node, parent) {
        if (parent === void 0) { parent = null; }
        var wrapped = this.factory.wrap(node, parent || this);
        if (parent) {
            parent.childNodes.push(wrapped);
        }
        this.jax.nodeMap.set(node, wrapped);
        return wrapped;
    };
    CommonWrapper.prototype.getBBox = function (save) {
        if (save === void 0) { save = true; }
        if (this.bboxComputed) {
            return this.bbox;
        }
        var bbox = (save ? this.bbox : BBox_js_1.BBox.zero());
        this.computeBBox(bbox);
        this.bboxComputed = save;
        return bbox;
    };
    CommonWrapper.prototype.getOuterBBox = function (save) {
        var e_1, _a;
        if (save === void 0) { save = true; }
        var bbox = this.getBBox(save);
        if (!this.styles)
            return bbox;
        var obox = new BBox_js_1.BBox();
        Object.assign(obox, bbox);
        try {
            for (var _b = __values(BBox_js_1.BBox.StyleAdjust), _c = _b.next(); !_c.done; _c = _b.next()) {
                var _d = __read(_c.value, 2), name_1 = _d[0], side = _d[1];
                var x = this.styles.get(name_1);
                if (x) {
                    obox[side] += this.length2em(x, 1, obox.rscale);
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
        return obox;
    };
    CommonWrapper.prototype.computeBBox = function (bbox, recompute) {
        var e_2, _a;
        if (recompute === void 0) { recompute = false; }
        bbox.empty();
        try {
            for (var _b = __values(this.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                var child = _c.value;
                bbox.append(child.getOuterBBox());
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_2) throw e_2.error; }
        }
        bbox.clean();
        if (this.fixesPWidth && this.setChildPWidths(recompute)) {
            this.computeBBox(bbox, true);
        }
    };
    CommonWrapper.prototype.setChildPWidths = function (recompute, w, clear) {
        var e_3, _a;
        if (w === void 0) { w = null; }
        if (clear === void 0) { clear = true; }
        if (recompute) {
            return false;
        }
        if (clear) {
            this.bbox.pwidth = '';
        }
        var changed = false;
        try {
            for (var _b = __values(this.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                var child = _c.value;
                var cbox = child.getOuterBBox();
                if (cbox.pwidth && child.setChildPWidths(recompute, w === null ? cbox.w : w, clear)) {
                    changed = true;
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
        return changed;
    };
    CommonWrapper.prototype.invalidateBBox = function () {
        if (this.bboxComputed) {
            this.bboxComputed = false;
            if (this.parent) {
                this.parent.invalidateBBox();
            }
        }
    };
    CommonWrapper.prototype.copySkewIC = function (bbox) {
        var first = this.childNodes[0];
        if (first === null || first === void 0 ? void 0 : first.bbox.sk) {
            bbox.sk = first.bbox.sk;
        }
        if (first === null || first === void 0 ? void 0 : first.bbox.dx) {
            bbox.dx = first.bbox.dx;
        }
        var last = this.childNodes[this.childNodes.length - 1];
        if (last === null || last === void 0 ? void 0 : last.bbox.ic) {
            bbox.ic = last.bbox.ic;
            bbox.w += bbox.ic;
        }
    };
    CommonWrapper.prototype.getStyles = function () {
        var styleString = this.node.attributes.getExplicit('style');
        if (!styleString)
            return;
        var style = this.styles = new Styles_js_1.Styles(styleString);
        for (var i = 0, m = CommonWrapper.removeStyles.length; i < m; i++) {
            var id = CommonWrapper.removeStyles[i];
            if (style.get(id)) {
                if (!this.removedStyles)
                    this.removedStyles = {};
                this.removedStyles[id] = style.get(id);
                style.set(id, '');
            }
        }
    };
    CommonWrapper.prototype.getVariant = function () {
        if (!this.node.isToken)
            return;
        var attributes = this.node.attributes;
        var variant = attributes.get('mathvariant');
        if (!attributes.getExplicit('mathvariant')) {
            var values = attributes.getList('fontfamily', 'fontweight', 'fontstyle');
            if (this.removedStyles) {
                var style = this.removedStyles;
                if (style.fontFamily)
                    values.family = style.fontFamily;
                if (style.fontWeight)
                    values.weight = style.fontWeight;
                if (style.fontStyle)
                    values.style = style.fontStyle;
            }
            if (values.fontfamily)
                values.family = values.fontfamily;
            if (values.fontweight)
                values.weight = values.fontweight;
            if (values.fontstyle)
                values.style = values.fontstyle;
            if (values.weight && values.weight.match(/^\d+$/)) {
                values.weight = (parseInt(values.weight) > 600 ? 'bold' : 'normal');
            }
            if (values.family) {
                variant = this.explicitVariant(values.family, values.weight, values.style);
            }
            else {
                if (this.node.getProperty('variantForm'))
                    variant = '-tex-variant';
                variant = (CommonWrapper.BOLDVARIANTS[values.weight] || {})[variant] || variant;
                variant = (CommonWrapper.ITALICVARIANTS[values.style] || {})[variant] || variant;
            }
        }
        this.variant = variant;
    };
    CommonWrapper.prototype.explicitVariant = function (fontFamily, fontWeight, fontStyle) {
        var style = this.styles;
        if (!style)
            style = this.styles = new Styles_js_1.Styles();
        style.set('fontFamily', fontFamily);
        if (fontWeight)
            style.set('fontWeight', fontWeight);
        if (fontStyle)
            style.set('fontStyle', fontStyle);
        return '-explicitFont';
    };
    CommonWrapper.prototype.getScale = function () {
        var scale = 1, parent = this.parent;
        var pscale = (parent ? parent.bbox.scale : 1);
        var attributes = this.node.attributes;
        var scriptlevel = Math.min(attributes.get('scriptlevel'), 2);
        var fontsize = attributes.get('fontsize');
        var mathsize = (this.node.isToken || this.node.isKind('mstyle') ?
            attributes.get('mathsize') : attributes.getInherited('mathsize'));
        if (scriptlevel !== 0) {
            scale = Math.pow(attributes.get('scriptsizemultiplier'), scriptlevel);
            var scriptminsize = this.length2em(attributes.get('scriptminsize'), .8, 1);
            if (scale < scriptminsize)
                scale = scriptminsize;
        }
        if (this.removedStyles && this.removedStyles.fontSize && !fontsize) {
            fontsize = this.removedStyles.fontSize;
        }
        if (fontsize && !attributes.getExplicit('mathsize')) {
            mathsize = fontsize;
        }
        if (mathsize !== '1') {
            scale *= this.length2em(mathsize, 1, 1);
        }
        this.bbox.scale = scale;
        this.bbox.rscale = scale / pscale;
    };
    CommonWrapper.prototype.getSpace = function () {
        var isTop = this.isTopEmbellished();
        var hasSpacing = this.node.hasSpacingAttributes();
        if (this.jax.options.mathmlSpacing || hasSpacing) {
            isTop && this.getMathMLSpacing();
        }
        else {
            this.getTeXSpacing(isTop, hasSpacing);
        }
    };
    CommonWrapper.prototype.getMathMLSpacing = function () {
        var node = this.node.coreMO();
        var child = node.coreParent();
        var parent = child.parent;
        if (!parent || !parent.isKind('mrow') || parent.childNodes.length === 1)
            return;
        var attributes = node.attributes;
        var isScript = (attributes.get('scriptlevel') > 0);
        this.bbox.L = (attributes.isSet('lspace') ?
            Math.max(0, this.length2em(attributes.get('lspace'))) :
            MathMLSpace(isScript, node.lspace));
        this.bbox.R = (attributes.isSet('rspace') ?
            Math.max(0, this.length2em(attributes.get('rspace'))) :
            MathMLSpace(isScript, node.rspace));
        var n = parent.childIndex(child);
        if (n === 0)
            return;
        var prev = parent.childNodes[n - 1];
        if (!prev.isEmbellished)
            return;
        var bbox = this.jax.nodeMap.get(prev).getBBox();
        if (bbox.R) {
            this.bbox.L = Math.max(0, this.bbox.L - bbox.R);
        }
    };
    CommonWrapper.prototype.getTeXSpacing = function (isTop, hasSpacing) {
        if (!hasSpacing) {
            var space = this.node.texSpacing();
            if (space) {
                this.bbox.L = this.length2em(space);
            }
        }
        if (isTop || hasSpacing) {
            var attributes = this.node.coreMO().attributes;
            if (attributes.isSet('lspace')) {
                this.bbox.L = Math.max(0, this.length2em(attributes.get('lspace')));
            }
            if (attributes.isSet('rspace')) {
                this.bbox.R = Math.max(0, this.length2em(attributes.get('rspace')));
            }
        }
    };
    CommonWrapper.prototype.isTopEmbellished = function () {
        return (this.node.isEmbellished &&
            !(this.node.parent && this.node.parent.isEmbellished));
    };
    CommonWrapper.prototype.core = function () {
        return this.jax.nodeMap.get(this.node.core());
    };
    CommonWrapper.prototype.coreMO = function () {
        return this.jax.nodeMap.get(this.node.coreMO());
    };
    CommonWrapper.prototype.getText = function () {
        var e_4, _a;
        var text = '';
        if (this.node.isToken) {
            try {
                for (var _b = __values(this.node.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var child = _c.value;
                    if (child instanceof MmlNode_js_1.TextNode) {
                        text += child.getText();
                    }
                }
            }
            catch (e_4_1) { e_4 = { error: e_4_1 }; }
            finally {
                try {
                    if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
                }
                finally { if (e_4) throw e_4.error; }
            }
        }
        return text;
    };
    CommonWrapper.prototype.canStretch = function (direction) {
        this.stretch = FontData_js_1.NOSTRETCH;
        if (this.node.isEmbellished) {
            var core = this.core();
            if (core && core.node !== this.node) {
                if (core.canStretch(direction)) {
                    this.stretch = core.stretch;
                }
            }
        }
        return this.stretch.dir !== 0;
    };
    CommonWrapper.prototype.getAlignShift = function () {
        var _a;
        var _b = (_a = this.node.attributes).getList.apply(_a, __spreadArray([], __read(MmlNode_js_1.indentAttributes), false)), indentalign = _b.indentalign, indentshift = _b.indentshift, indentalignfirst = _b.indentalignfirst, indentshiftfirst = _b.indentshiftfirst;
        if (indentalignfirst !== 'indentalign') {
            indentalign = indentalignfirst;
        }
        if (indentalign === 'auto') {
            indentalign = this.jax.options.displayAlign;
        }
        if (indentshiftfirst !== 'indentshift') {
            indentshift = indentshiftfirst;
        }
        if (indentshift === 'auto') {
            indentshift = this.jax.options.displayIndent;
            if (indentalign === 'right' && !indentshift.match(/^\s*0[a-z]*\s*$/)) {
                indentshift = ('-' + indentshift.trim()).replace(/^--/, '');
            }
        }
        var shift = this.length2em(indentshift, this.metrics.containerWidth);
        return [indentalign, shift];
    };
    CommonWrapper.prototype.getAlignX = function (W, bbox, align) {
        return (align === 'right' ? W - (bbox.w + bbox.R) * bbox.rscale :
            align === 'left' ? bbox.L * bbox.rscale :
                (W - bbox.w * bbox.rscale) / 2);
    };
    CommonWrapper.prototype.getAlignY = function (H, D, h, d, align) {
        return (align === 'top' ? H - h :
            align === 'bottom' ? d - D :
                align === 'center' ? ((H - h) - (D - d)) / 2 :
                    0);
    };
    CommonWrapper.prototype.getWrapWidth = function (i) {
        return this.childNodes[i].getBBox().w;
    };
    CommonWrapper.prototype.getChildAlign = function (_i) {
        return 'left';
    };
    CommonWrapper.prototype.percent = function (m) {
        return LENGTHS.percent(m);
    };
    CommonWrapper.prototype.em = function (m) {
        return LENGTHS.em(m);
    };
    CommonWrapper.prototype.px = function (m, M) {
        if (M === void 0) { M = -LENGTHS.BIGDIMEN; }
        return LENGTHS.px(m, M, this.metrics.em);
    };
    CommonWrapper.prototype.length2em = function (length, size, scale) {
        if (size === void 0) { size = 1; }
        if (scale === void 0) { scale = null; }
        if (scale === null) {
            scale = this.bbox.scale;
        }
        return LENGTHS.length2em(length, size, scale, this.jax.pxPerEm);
    };
    CommonWrapper.prototype.unicodeChars = function (text, name) {
        if (name === void 0) { name = this.variant; }
        var chars = (0, string_js_1.unicodeChars)(text);
        var variant = this.font.getVariant(name);
        if (variant && variant.chars) {
            var map_1 = variant.chars;
            chars = chars.map(function (n) { return ((map_1[n] || [])[3] || {}).smp || n; });
        }
        return chars;
    };
    CommonWrapper.prototype.remapChars = function (chars) {
        return chars;
    };
    CommonWrapper.prototype.mmlText = function (text) {
        return this.node.factory.create('text').setText(text);
    };
    CommonWrapper.prototype.mmlNode = function (kind, properties, children) {
        if (properties === void 0) { properties = {}; }
        if (children === void 0) { children = []; }
        return this.node.factory.create(kind, properties, children);
    };
    CommonWrapper.prototype.createMo = function (text) {
        var mmlFactory = this.node.factory;
        var textNode = mmlFactory.create('text').setText(text);
        var mml = mmlFactory.create('mo', { stretchy: true }, [textNode]);
        mml.inheritAttributesFrom(this.node);
        var node = this.wrap(mml);
        node.parent = this;
        return node;
    };
    CommonWrapper.prototype.getVariantChar = function (variant, n) {
        var char = this.font.getChar(variant, n) || [0, 0, 0, { unknown: true }];
        if (char.length === 3) {
            char[3] = {};
        }
        return char;
    };
    CommonWrapper.kind = 'unknown';
    CommonWrapper.styles = {};
    CommonWrapper.removeStyles = [
        'fontSize', 'fontFamily', 'fontWeight',
        'fontStyle', 'fontVariant', 'font'
    ];
    CommonWrapper.skipAttributes = {
        fontfamily: true, fontsize: true, fontweight: true, fontstyle: true,
        color: true, background: true,
        'class': true, href: true, style: true,
        xmlns: true
    };
    CommonWrapper.BOLDVARIANTS = {
        bold: {
            normal: 'bold',
            italic: 'bold-italic',
            fraktur: 'bold-fraktur',
            script: 'bold-script',
            'sans-serif': 'bold-sans-serif',
            'sans-serif-italic': 'sans-serif-bold-italic'
        },
        normal: {
            bold: 'normal',
            'bold-italic': 'italic',
            'bold-fraktur': 'fraktur',
            'bold-script': 'script',
            'bold-sans-serif': 'sans-serif',
            'sans-serif-bold-italic': 'sans-serif-italic'
        }
    };
    CommonWrapper.ITALICVARIANTS = {
        italic: {
            normal: 'italic',
            bold: 'bold-italic',
            'sans-serif': 'sans-serif-italic',
            'bold-sans-serif': 'sans-serif-bold-italic'
        },
        normal: {
            italic: 'normal',
            'bold-italic': 'bold',
            'sans-serif-italic': 'sans-serif',
            'sans-serif-bold-italic': 'bold-sans-serif'
        }
    };
    return CommonWrapper;
}(Wrapper_js_1.AbstractWrapper));
exports.CommonWrapper = CommonWrapper;
//# sourceMappingURL=Wrapper.js.map

/***/ }),

/***/ 1475:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonWrapperFactory = void 0;
var WrapperFactory_js_1 = __webpack_require__(2506);
var CommonWrapperFactory = (function (_super) {
    __extends(CommonWrapperFactory, _super);
    function CommonWrapperFactory() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.jax = null;
        return _this;
    }
    Object.defineProperty(CommonWrapperFactory.prototype, "Wrappers", {
        get: function () {
            return this.node;
        },
        enumerable: false,
        configurable: true
    });
    CommonWrapperFactory.defaultNodes = {};
    return CommonWrapperFactory;
}(WrapperFactory_js_1.AbstractWrapperFactory));
exports.CommonWrapperFactory = CommonWrapperFactory;
//# sourceMappingURL=WrapperFactory.js.map

/***/ }),

/***/ 3438:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonTeXAtomMixin = void 0;
var MmlNode_js_1 = __webpack_require__(8921);
function CommonTeXAtomMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.computeBBox = function (bbox, recompute) {
            if (recompute === void 0) { recompute = false; }
            _super.prototype.computeBBox.call(this, bbox, recompute);
            if (this.childNodes[0] && this.childNodes[0].bbox.ic) {
                bbox.ic = this.childNodes[0].bbox.ic;
            }
            if (this.node.texClass === MmlNode_js_1.TEXCLASS.VCENTER) {
                var h = bbox.h, d = bbox.d;
                var a = this.font.params.axis_height;
                var dh = ((h + d) / 2 + a) - h;
                bbox.h += dh;
                bbox.d -= dh;
            }
        };
        return class_1;
    }(Base));
}
exports.CommonTeXAtomMixin = CommonTeXAtomMixin;
//# sourceMappingURL=TeXAtom.js.map

/***/ }),

/***/ 555:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonTextNodeMixin = void 0;
function CommonTextNodeMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.computeBBox = function (bbox, _recompute) {
            var e_1, _a;
            if (_recompute === void 0) { _recompute = false; }
            var variant = this.parent.variant;
            var text = this.node.getText();
            if (variant === '-explicitFont') {
                var font = this.jax.getFontData(this.parent.styles);
                var _b = this.jax.measureText(text, variant, font), w = _b.w, h = _b.h, d = _b.d;
                bbox.h = h;
                bbox.d = d;
                bbox.w = w;
            }
            else {
                var chars = this.remappedText(text, variant);
                bbox.empty();
                try {
                    for (var chars_1 = __values(chars), chars_1_1 = chars_1.next(); !chars_1_1.done; chars_1_1 = chars_1.next()) {
                        var char = chars_1_1.value;
                        var _c = __read(this.getVariantChar(variant, char), 4), h = _c[0], d = _c[1], w = _c[2], data = _c[3];
                        if (data.unknown) {
                            var cbox = this.jax.measureText(String.fromCodePoint(char), variant);
                            w = cbox.w;
                            h = cbox.h;
                            d = cbox.d;
                        }
                        bbox.w += w;
                        if (h > bbox.h)
                            bbox.h = h;
                        if (d > bbox.d)
                            bbox.d = d;
                        bbox.ic = data.ic || 0;
                        bbox.sk = data.sk || 0;
                        bbox.dx = data.dx || 0;
                    }
                }
                catch (e_1_1) { e_1 = { error: e_1_1 }; }
                finally {
                    try {
                        if (chars_1_1 && !chars_1_1.done && (_a = chars_1.return)) _a.call(chars_1);
                    }
                    finally { if (e_1) throw e_1.error; }
                }
                if (chars.length > 1) {
                    bbox.sk = 0;
                }
                bbox.clean();
            }
        };
        class_1.prototype.remappedText = function (text, variant) {
            var c = this.parent.stretch.c;
            return (c ? [c] : this.parent.remapChars(this.unicodeChars(text, variant)));
        };
        class_1.prototype.getStyles = function () { };
        class_1.prototype.getVariant = function () { };
        class_1.prototype.getScale = function () { };
        class_1.prototype.getSpace = function () { };
        return class_1;
    }(Base));
}
exports.CommonTextNodeMixin = CommonTextNodeMixin;
//# sourceMappingURL=TextNode.js.map

/***/ }),

/***/ 3345:
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
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMactionMixin = exports.TooltipData = void 0;
var string_js_1 = __webpack_require__(6720);
exports.TooltipData = {
    dx: '.2em',
    dy: '.1em',
    postDelay: 600,
    clearDelay: 100,
    hoverTimer: new Map(),
    clearTimer: new Map(),
    stopTimers: function (node, data) {
        if (data.clearTimer.has(node)) {
            clearTimeout(data.clearTimer.get(node));
            data.clearTimer.delete(node);
        }
        if (data.hoverTimer.has(node)) {
            clearTimeout(data.hoverTimer.get(node));
            data.hoverTimer.delete(node);
        }
    }
};
function CommonMactionMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            var actions = _this.constructor.actions;
            var action = _this.node.attributes.get('actiontype');
            var _a = __read(actions.get(action) || [(function (_node, _data) { }), {}], 2), handler = _a[0], data = _a[1];
            _this.action = handler;
            _this.data = data;
            _this.getParameters();
            return _this;
        }
        Object.defineProperty(class_1.prototype, "selected", {
            get: function () {
                var selection = this.node.attributes.get('selection');
                var i = Math.max(1, Math.min(this.childNodes.length, selection)) - 1;
                return this.childNodes[i] || this.wrap(this.node.selected);
            },
            enumerable: false,
            configurable: true
        });
        class_1.prototype.getParameters = function () {
            var offsets = this.node.attributes.get('data-offsets');
            var _a = __read((0, string_js_1.split)(offsets || ''), 2), dx = _a[0], dy = _a[1];
            this.dx = this.length2em(dx || exports.TooltipData.dx);
            this.dy = this.length2em(dy || exports.TooltipData.dy);
        };
        class_1.prototype.computeBBox = function (bbox, recompute) {
            if (recompute === void 0) { recompute = false; }
            bbox.updateFrom(this.selected.getOuterBBox());
            this.selected.setChildPWidths(recompute);
        };
        return class_1;
    }(Base));
}
exports.CommonMactionMixin = CommonMactionMixin;
//# sourceMappingURL=maction.js.map

/***/ }),

/***/ 2057:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMathMixin = void 0;
function CommonMathMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.getWrapWidth = function (_i) {
            return (this.parent ? this.getBBox().w : this.metrics.containerWidth / this.jax.pxPerEm);
        };
        return class_1;
    }(Base));
}
exports.CommonMathMixin = CommonMathMixin;
//# sourceMappingURL=math.js.map

/***/ }),

/***/ 6200:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMencloseMixin = void 0;
var Notation = __importStar(__webpack_require__(5373));
var string_js_1 = __webpack_require__(6720);
function CommonMencloseMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.notations = {};
            _this.renderChild = null;
            _this.msqrt = null;
            _this.padding = Notation.PADDING;
            _this.thickness = Notation.THICKNESS;
            _this.arrowhead = { x: Notation.ARROWX, y: Notation.ARROWY, dx: Notation.ARROWDX };
            _this.TRBL = [0, 0, 0, 0];
            _this.getParameters();
            _this.getNotations();
            _this.removeRedundantNotations();
            _this.initializeNotations();
            _this.TRBL = _this.getBBoxExtenders();
            return _this;
        }
        class_1.prototype.getParameters = function () {
            var attributes = this.node.attributes;
            var padding = attributes.get('data-padding');
            if (padding !== undefined) {
                this.padding = this.length2em(padding, Notation.PADDING);
            }
            var thickness = attributes.get('data-thickness');
            if (thickness !== undefined) {
                this.thickness = this.length2em(thickness, Notation.THICKNESS);
            }
            var arrowhead = attributes.get('data-arrowhead');
            if (arrowhead !== undefined) {
                var _b = __read((0, string_js_1.split)(arrowhead), 3), x = _b[0], y = _b[1], dx = _b[2];
                this.arrowhead = {
                    x: (x ? parseFloat(x) : Notation.ARROWX),
                    y: (y ? parseFloat(y) : Notation.ARROWY),
                    dx: (dx ? parseFloat(dx) : Notation.ARROWDX)
                };
            }
        };
        class_1.prototype.getNotations = function () {
            var e_1, _b;
            var Notations = this.constructor.notations;
            try {
                for (var _c = __values((0, string_js_1.split)(this.node.attributes.get('notation'))), _d = _c.next(); !_d.done; _d = _c.next()) {
                    var name_1 = _d.value;
                    var notation = Notations.get(name_1);
                    if (notation) {
                        this.notations[name_1] = notation;
                        if (notation.renderChild) {
                            this.renderChild = notation.renderer;
                        }
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
        };
        class_1.prototype.removeRedundantNotations = function () {
            var e_2, _b, e_3, _c;
            try {
                for (var _d = __values(Object.keys(this.notations)), _e = _d.next(); !_e.done; _e = _d.next()) {
                    var name_2 = _e.value;
                    if (this.notations[name_2]) {
                        var remove = this.notations[name_2].remove || '';
                        try {
                            for (var _f = (e_3 = void 0, __values(remove.split(/ /))), _g = _f.next(); !_g.done; _g = _f.next()) {
                                var notation = _g.value;
                                delete this.notations[notation];
                            }
                        }
                        catch (e_3_1) { e_3 = { error: e_3_1 }; }
                        finally {
                            try {
                                if (_g && !_g.done && (_c = _f.return)) _c.call(_f);
                            }
                            finally { if (e_3) throw e_3.error; }
                        }
                    }
                }
            }
            catch (e_2_1) { e_2 = { error: e_2_1 }; }
            finally {
                try {
                    if (_e && !_e.done && (_b = _d.return)) _b.call(_d);
                }
                finally { if (e_2) throw e_2.error; }
            }
        };
        class_1.prototype.initializeNotations = function () {
            var e_4, _b;
            try {
                for (var _c = __values(Object.keys(this.notations)), _d = _c.next(); !_d.done; _d = _c.next()) {
                    var name_3 = _d.value;
                    var init = this.notations[name_3].init;
                    init && init(this);
                }
            }
            catch (e_4_1) { e_4 = { error: e_4_1 }; }
            finally {
                try {
                    if (_d && !_d.done && (_b = _c.return)) _b.call(_c);
                }
                finally { if (e_4) throw e_4.error; }
            }
        };
        class_1.prototype.computeBBox = function (bbox, recompute) {
            if (recompute === void 0) { recompute = false; }
            var _b = __read(this.TRBL, 4), T = _b[0], R = _b[1], B = _b[2], L = _b[3];
            var child = this.childNodes[0].getBBox();
            bbox.combine(child, L, 0);
            bbox.h += T;
            bbox.d += B;
            bbox.w += R;
            this.setChildPWidths(recompute);
        };
        class_1.prototype.getBBoxExtenders = function () {
            var e_5, _b;
            var TRBL = [0, 0, 0, 0];
            try {
                for (var _c = __values(Object.keys(this.notations)), _d = _c.next(); !_d.done; _d = _c.next()) {
                    var name_4 = _d.value;
                    this.maximizeEntries(TRBL, this.notations[name_4].bbox(this));
                }
            }
            catch (e_5_1) { e_5 = { error: e_5_1 }; }
            finally {
                try {
                    if (_d && !_d.done && (_b = _c.return)) _b.call(_c);
                }
                finally { if (e_5) throw e_5.error; }
            }
            return TRBL;
        };
        class_1.prototype.getPadding = function () {
            var e_6, _b;
            var _this = this;
            var BTRBL = [0, 0, 0, 0];
            try {
                for (var _c = __values(Object.keys(this.notations)), _d = _c.next(); !_d.done; _d = _c.next()) {
                    var name_5 = _d.value;
                    var border = this.notations[name_5].border;
                    if (border) {
                        this.maximizeEntries(BTRBL, border(this));
                    }
                }
            }
            catch (e_6_1) { e_6 = { error: e_6_1 }; }
            finally {
                try {
                    if (_d && !_d.done && (_b = _c.return)) _b.call(_c);
                }
                finally { if (e_6) throw e_6.error; }
            }
            return [0, 1, 2, 3].map(function (i) { return _this.TRBL[i] - BTRBL[i]; });
        };
        class_1.prototype.maximizeEntries = function (X, Y) {
            for (var i = 0; i < X.length; i++) {
                if (X[i] < Y[i]) {
                    X[i] = Y[i];
                }
            }
        };
        class_1.prototype.getOffset = function (direction) {
            var _b = __read(this.TRBL, 4), T = _b[0], R = _b[1], B = _b[2], L = _b[3];
            var d = (direction === 'X' ? R - L : B - T) / 2;
            return (Math.abs(d) > .001 ? d : 0);
        };
        class_1.prototype.getArgMod = function (w, h) {
            return [Math.atan2(h, w), Math.sqrt(w * w + h * h)];
        };
        class_1.prototype.arrow = function (_w, _a, _double, _offset, _dist) {
            if (_offset === void 0) { _offset = ''; }
            if (_dist === void 0) { _dist = 0; }
            return null;
        };
        class_1.prototype.arrowData = function () {
            var _b = __read([this.padding, this.thickness], 2), p = _b[0], t = _b[1];
            var r = t * (this.arrowhead.x + Math.max(1, this.arrowhead.dx));
            var _c = this.childNodes[0].getBBox(), h = _c.h, d = _c.d, w = _c.w;
            var H = h + d;
            var R = Math.sqrt(H * H + w * w);
            var x = Math.max(p, r * w / R);
            var y = Math.max(p, r * H / R);
            var _d = __read(this.getArgMod(w + 2 * x, H + 2 * y), 2), a = _d[0], W = _d[1];
            return { a: a, W: W, x: x, y: y };
        };
        class_1.prototype.arrowAW = function () {
            var _b = this.childNodes[0].getBBox(), h = _b.h, d = _b.d, w = _b.w;
            var _c = __read(this.TRBL, 4), T = _c[0], R = _c[1], B = _c[2], L = _c[3];
            return this.getArgMod(L + w + R, T + h + d + B);
        };
        class_1.prototype.createMsqrt = function (child) {
            var mmlFactory = this.node.factory;
            var mml = mmlFactory.create('msqrt');
            mml.inheritAttributesFrom(this.node);
            mml.childNodes[0] = child.node;
            var node = this.wrap(mml);
            node.parent = this;
            return node;
        };
        class_1.prototype.sqrtTRBL = function () {
            var bbox = this.msqrt.getBBox();
            var cbox = this.msqrt.childNodes[0].getBBox();
            return [bbox.h - cbox.h, 0, bbox.d - cbox.d, bbox.w - cbox.w];
        };
        return class_1;
    }(Base));
}
exports.CommonMencloseMixin = CommonMencloseMixin;
//# sourceMappingURL=menclose.js.map

/***/ }),

/***/ 1346:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMfencedMixin = void 0;
function CommonMfencedMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.mrow = null;
            _this.createMrow();
            _this.addMrowChildren();
            return _this;
        }
        class_1.prototype.createMrow = function () {
            var mmlFactory = this.node.factory;
            var mrow = mmlFactory.create('inferredMrow');
            mrow.inheritAttributesFrom(this.node);
            this.mrow = this.wrap(mrow);
            this.mrow.parent = this;
        };
        class_1.prototype.addMrowChildren = function () {
            var e_1, _a;
            var mfenced = this.node;
            var mrow = this.mrow;
            this.addMo(mfenced.open);
            if (this.childNodes.length) {
                mrow.childNodes.push(this.childNodes[0]);
            }
            var i = 0;
            try {
                for (var _b = __values(this.childNodes.slice(1)), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var child = _c.value;
                    this.addMo(mfenced.separators[i++]);
                    mrow.childNodes.push(child);
                }
            }
            catch (e_1_1) { e_1 = { error: e_1_1 }; }
            finally {
                try {
                    if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
                }
                finally { if (e_1) throw e_1.error; }
            }
            this.addMo(mfenced.close);
            mrow.stretchChildren();
        };
        class_1.prototype.addMo = function (node) {
            if (!node)
                return;
            var mo = this.wrap(node);
            this.mrow.childNodes.push(mo);
            mo.parent = this.mrow;
        };
        class_1.prototype.computeBBox = function (bbox, recompute) {
            if (recompute === void 0) { recompute = false; }
            bbox.updateFrom(this.mrow.getOuterBBox());
            this.setChildPWidths(recompute);
        };
        return class_1;
    }(Base));
}
exports.CommonMfencedMixin = CommonMfencedMixin;
//# sourceMappingURL=mfenced.js.map

/***/ }),

/***/ 5705:
/***/ (function(__unused_webpack_module, exports) {


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
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMfracMixin = void 0;
function CommonMfracMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.bevel = null;
            _this.pad = (_this.node.getProperty('withDelims') ? 0 : _this.font.params.nulldelimiterspace);
            if (_this.node.attributes.get('bevelled')) {
                var H = _this.getBevelData(_this.isDisplay()).H;
                var bevel = _this.bevel = _this.createMo('/');
                bevel.node.attributes.set('symmetric', true);
                bevel.canStretch(1);
                bevel.getStretchedVariant([H], true);
            }
            return _this;
        }
        class_1.prototype.computeBBox = function (bbox, recompute) {
            if (recompute === void 0) { recompute = false; }
            bbox.empty();
            var _a = this.node.attributes.getList('linethickness', 'bevelled'), linethickness = _a.linethickness, bevelled = _a.bevelled;
            var display = this.isDisplay();
            var w = null;
            if (bevelled) {
                this.getBevelledBBox(bbox, display);
            }
            else {
                var thickness = this.length2em(String(linethickness), .06);
                w = -2 * this.pad;
                if (thickness === 0) {
                    this.getAtopBBox(bbox, display);
                }
                else {
                    this.getFractionBBox(bbox, display, thickness);
                    w -= .2;
                }
                w += bbox.w;
            }
            bbox.clean();
            this.setChildPWidths(recompute, w);
        };
        class_1.prototype.getFractionBBox = function (bbox, display, t) {
            var nbox = this.childNodes[0].getOuterBBox();
            var dbox = this.childNodes[1].getOuterBBox();
            var tex = this.font.params;
            var a = tex.axis_height;
            var _a = this.getTUV(display, t), T = _a.T, u = _a.u, v = _a.v;
            bbox.combine(nbox, 0, a + T + Math.max(nbox.d * nbox.rscale, u));
            bbox.combine(dbox, 0, a - T - Math.max(dbox.h * dbox.rscale, v));
            bbox.w += 2 * this.pad + .2;
        };
        class_1.prototype.getTUV = function (display, t) {
            var tex = this.font.params;
            var a = tex.axis_height;
            var T = (display ? 3.5 : 1.5) * t;
            return { T: (display ? 3.5 : 1.5) * t,
                u: (display ? tex.num1 : tex.num2) - a - T,
                v: (display ? tex.denom1 : tex.denom2) + a - T };
        };
        class_1.prototype.getAtopBBox = function (bbox, display) {
            var _a = this.getUVQ(display), u = _a.u, v = _a.v, nbox = _a.nbox, dbox = _a.dbox;
            bbox.combine(nbox, 0, u);
            bbox.combine(dbox, 0, -v);
            bbox.w += 2 * this.pad;
        };
        class_1.prototype.getUVQ = function (display) {
            var nbox = this.childNodes[0].getOuterBBox();
            var dbox = this.childNodes[1].getOuterBBox();
            var tex = this.font.params;
            var _a = __read((display ? [tex.num1, tex.denom1] : [tex.num3, tex.denom2]), 2), u = _a[0], v = _a[1];
            var p = (display ? 7 : 3) * tex.rule_thickness;
            var q = (u - nbox.d * nbox.scale) - (dbox.h * dbox.scale - v);
            if (q < p) {
                u += (p - q) / 2;
                v += (p - q) / 2;
                q = p;
            }
            return { u: u, v: v, q: q, nbox: nbox, dbox: dbox };
        };
        class_1.prototype.getBevelledBBox = function (bbox, display) {
            var _a = this.getBevelData(display), u = _a.u, v = _a.v, delta = _a.delta, nbox = _a.nbox, dbox = _a.dbox;
            var lbox = this.bevel.getOuterBBox();
            bbox.combine(nbox, 0, u);
            bbox.combine(lbox, bbox.w - delta / 2, 0);
            bbox.combine(dbox, bbox.w - delta / 2, v);
        };
        class_1.prototype.getBevelData = function (display) {
            var nbox = this.childNodes[0].getOuterBBox();
            var dbox = this.childNodes[1].getOuterBBox();
            var delta = (display ? .4 : .15);
            var H = Math.max(nbox.scale * (nbox.h + nbox.d), dbox.scale * (dbox.h + dbox.d)) + 2 * delta;
            var a = this.font.params.axis_height;
            var u = nbox.scale * (nbox.d - nbox.h) / 2 + a + delta;
            var v = dbox.scale * (dbox.d - dbox.h) / 2 + a - delta;
            return { H: H, delta: delta, u: u, v: v, nbox: nbox, dbox: dbox };
        };
        class_1.prototype.canStretch = function (_direction) {
            return false;
        };
        class_1.prototype.isDisplay = function () {
            var _a = this.node.attributes.getList('displaystyle', 'scriptlevel'), displaystyle = _a.displaystyle, scriptlevel = _a.scriptlevel;
            return displaystyle && scriptlevel === 0;
        };
        class_1.prototype.getWrapWidth = function (i) {
            var attributes = this.node.attributes;
            if (attributes.get('bevelled')) {
                return this.childNodes[i].getOuterBBox().w;
            }
            var w = this.getBBox().w;
            var thickness = this.length2em(attributes.get('linethickness'));
            return w - (thickness ? .2 : 0) - 2 * this.pad;
        };
        class_1.prototype.getChildAlign = function (i) {
            var attributes = this.node.attributes;
            return (attributes.get('bevelled') ? 'left' : attributes.get(['numalign', 'denomalign'][i]));
        };
        return class_1;
    }(Base));
}
exports.CommonMfracMixin = CommonMfracMixin;
//# sourceMappingURL=mfrac.js.map

/***/ }),

/***/ 7969:
/***/ (function(__unused_webpack_module, exports) {


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
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMglyphMixin = void 0;
function CommonMglyphMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.getParameters();
            return _this;
        }
        class_1.prototype.getParameters = function () {
            var _a = this.node.attributes.getList('width', 'height', 'valign', 'src', 'index'), width = _a.width, height = _a.height, valign = _a.valign, src = _a.src, index = _a.index;
            if (src) {
                this.width = (width === 'auto' ? 1 : this.length2em(width));
                this.height = (height === 'auto' ? 1 : this.length2em(height));
                this.valign = this.length2em(valign || '0');
            }
            else {
                var text = String.fromCodePoint(parseInt(index));
                var mmlFactory = this.node.factory;
                this.charWrapper = this.wrap(mmlFactory.create('text').setText(text));
                this.charWrapper.parent = this;
            }
        };
        class_1.prototype.computeBBox = function (bbox, _recompute) {
            if (_recompute === void 0) { _recompute = false; }
            if (this.charWrapper) {
                bbox.updateFrom(this.charWrapper.getBBox());
            }
            else {
                bbox.w = this.width;
                bbox.h = this.height + this.valign;
                bbox.d = -this.valign;
            }
        };
        return class_1;
    }(Base));
}
exports.CommonMglyphMixin = CommonMglyphMixin;
//# sourceMappingURL=mglyph.js.map

/***/ }),

/***/ 1419:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMiMixin = void 0;
function CommonMiMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.computeBBox = function (bbox, _recompute) {
            if (_recompute === void 0) { _recompute = false; }
            _super.prototype.computeBBox.call(this, bbox);
            this.copySkewIC(bbox);
        };
        return class_1;
    }(Base));
}
exports.CommonMiMixin = CommonMiMixin;
//# sourceMappingURL=mi.js.map

/***/ }),

/***/ 9906:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMmultiscriptsMixin = exports.ScriptNames = exports.NextScript = void 0;
var BBox_js_1 = __webpack_require__(3717);
exports.NextScript = {
    base: 'subList',
    subList: 'supList',
    supList: 'subList',
    psubList: 'psupList',
    psupList: 'psubList',
};
exports.ScriptNames = ['sup', 'sup', 'psup', 'psub'];
function CommonMmultiscriptsMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.scriptData = null;
            _this.firstPrescript = 0;
            _this.getScriptData();
            return _this;
        }
        class_1.prototype.combinePrePost = function (pre, post) {
            var bbox = new BBox_js_1.BBox(pre);
            bbox.combine(post, 0, 0);
            return bbox;
        };
        class_1.prototype.computeBBox = function (bbox, recompute) {
            if (recompute === void 0) { recompute = false; }
            var scriptspace = this.font.params.scriptspace;
            var data = this.scriptData;
            var sub = this.combinePrePost(data.sub, data.psub);
            var sup = this.combinePrePost(data.sup, data.psup);
            var _a = __read(this.getUVQ(sub, sup), 2), u = _a[0], v = _a[1];
            bbox.empty();
            if (data.numPrescripts) {
                bbox.combine(data.psup, scriptspace, u);
                bbox.combine(data.psub, scriptspace, v);
            }
            bbox.append(data.base);
            if (data.numScripts) {
                var w = bbox.w;
                bbox.combine(data.sup, w, u);
                bbox.combine(data.sub, w, v);
                bbox.w += scriptspace;
            }
            bbox.clean();
            this.setChildPWidths(recompute);
        };
        class_1.prototype.getScriptData = function () {
            var data = this.scriptData = {
                base: null, sub: BBox_js_1.BBox.empty(), sup: BBox_js_1.BBox.empty(), psub: BBox_js_1.BBox.empty(), psup: BBox_js_1.BBox.empty(),
                numPrescripts: 0, numScripts: 0
            };
            var lists = this.getScriptBBoxLists();
            this.combineBBoxLists(data.sub, data.sup, lists.subList, lists.supList);
            this.combineBBoxLists(data.psub, data.psup, lists.psubList, lists.psupList);
            data.base = lists.base[0];
            data.numPrescripts = lists.psubList.length;
            data.numScripts = lists.subList.length;
        };
        class_1.prototype.getScriptBBoxLists = function () {
            var e_1, _a;
            var lists = {
                base: [], subList: [], supList: [], psubList: [], psupList: []
            };
            var script = 'base';
            try {
                for (var _b = __values(this.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var child = _c.value;
                    if (child.node.isKind('mprescripts')) {
                        script = 'psubList';
                    }
                    else {
                        lists[script].push(child.getOuterBBox());
                        script = exports.NextScript[script];
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
            this.firstPrescript = lists.subList.length + lists.supList.length + 2;
            this.padLists(lists.subList, lists.supList);
            this.padLists(lists.psubList, lists.psupList);
            return lists;
        };
        class_1.prototype.padLists = function (list1, list2) {
            if (list1.length > list2.length) {
                list2.push(BBox_js_1.BBox.empty());
            }
        };
        class_1.prototype.combineBBoxLists = function (bbox1, bbox2, list1, list2) {
            for (var i = 0; i < list1.length; i++) {
                var _a = __read(this.getScaledWHD(list1[i]), 3), w1 = _a[0], h1 = _a[1], d1 = _a[2];
                var _b = __read(this.getScaledWHD(list2[i]), 3), w2 = _b[0], h2 = _b[1], d2 = _b[2];
                var w = Math.max(w1, w2);
                bbox1.w += w;
                bbox2.w += w;
                if (h1 > bbox1.h)
                    bbox1.h = h1;
                if (d1 > bbox1.d)
                    bbox1.d = d1;
                if (h2 > bbox2.h)
                    bbox2.h = h2;
                if (d2 > bbox2.d)
                    bbox2.d = d2;
            }
        };
        class_1.prototype.getScaledWHD = function (bbox) {
            var w = bbox.w, h = bbox.h, d = bbox.d, rscale = bbox.rscale;
            return [w * rscale, h * rscale, d * rscale];
        };
        class_1.prototype.getUVQ = function (subbox, supbox) {
            var _a;
            if (!this.UVQ) {
                var _b = __read([0, 0, 0], 3), u = _b[0], v = _b[1], q = _b[2];
                if (subbox.h === 0 && subbox.d === 0) {
                    u = this.getU();
                }
                else if (supbox.h === 0 && supbox.d === 0) {
                    u = -this.getV();
                }
                else {
                    _a = __read(_super.prototype.getUVQ.call(this, subbox, supbox), 3), u = _a[0], v = _a[1], q = _a[2];
                }
                this.UVQ = [u, v, q];
            }
            return this.UVQ;
        };
        return class_1;
    }(Base));
}
exports.CommonMmultiscriptsMixin = CommonMmultiscriptsMixin;
//# sourceMappingURL=mmultiscripts.js.map

/***/ }),

/***/ 2304:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMnMixin = void 0;
function CommonMnMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.remapChars = function (chars) {
            if (chars.length) {
                var text = this.font.getRemappedChar('mn', chars[0]);
                if (text) {
                    var c = this.unicodeChars(text, this.variant);
                    if (c.length === 1) {
                        chars[0] = c[0];
                    }
                    else {
                        chars = c.concat(chars.slice(1));
                    }
                }
            }
            return chars;
        };
        return class_1;
    }(Base));
}
exports.CommonMnMixin = CommonMnMixin;
//# sourceMappingURL=mn.js.map

/***/ }),

/***/ 437:
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
var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMoMixin = exports.DirectionVH = void 0;
var BBox_js_1 = __webpack_require__(3717);
var string_js_1 = __webpack_require__(6720);
var FontData_js_1 = __webpack_require__(9250);
exports.DirectionVH = (_a = {},
    _a[1] = 'v',
    _a[2] = 'h',
    _a);
function CommonMoMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.size = null;
            _this.isAccent = _this.node.isAccent;
            return _this;
        }
        class_1.prototype.computeBBox = function (bbox, _recompute) {
            if (_recompute === void 0) { _recompute = false; }
            this.protoBBox(bbox);
            if (this.node.attributes.get('symmetric') &&
                this.stretch.dir !== 2) {
                var d = this.getCenterOffset(bbox);
                bbox.h += d;
                bbox.d -= d;
            }
            if (this.node.getProperty('mathaccent') &&
                (this.stretch.dir === 0 || this.size >= 0)) {
                bbox.w = 0;
            }
        };
        class_1.prototype.protoBBox = function (bbox) {
            var stretchy = (this.stretch.dir !== 0);
            if (stretchy && this.size === null) {
                this.getStretchedVariant([0]);
            }
            if (stretchy && this.size < 0)
                return;
            _super.prototype.computeBBox.call(this, bbox);
            this.copySkewIC(bbox);
        };
        class_1.prototype.getAccentOffset = function () {
            var bbox = BBox_js_1.BBox.empty();
            this.protoBBox(bbox);
            return -bbox.w / 2;
        };
        class_1.prototype.getCenterOffset = function (bbox) {
            if (bbox === void 0) { bbox = null; }
            if (!bbox) {
                bbox = BBox_js_1.BBox.empty();
                _super.prototype.computeBBox.call(this, bbox);
            }
            return ((bbox.h + bbox.d) / 2 + this.font.params.axis_height) - bbox.h;
        };
        class_1.prototype.getVariant = function () {
            if (this.node.attributes.get('largeop')) {
                this.variant = (this.node.attributes.get('displaystyle') ? '-largeop' : '-smallop');
                return;
            }
            if (!this.node.attributes.getExplicit('mathvariant') &&
                this.node.getProperty('pseudoscript') === false) {
                this.variant = '-tex-variant';
                return;
            }
            _super.prototype.getVariant.call(this);
        };
        class_1.prototype.canStretch = function (direction) {
            if (this.stretch.dir !== 0) {
                return this.stretch.dir === direction;
            }
            var attributes = this.node.attributes;
            if (!attributes.get('stretchy'))
                return false;
            var c = this.getText();
            if (Array.from(c).length !== 1)
                return false;
            var delim = this.font.getDelimiter(c.codePointAt(0));
            this.stretch = (delim && delim.dir === direction ? delim : FontData_js_1.NOSTRETCH);
            return this.stretch.dir !== 0;
        };
        class_1.prototype.getStretchedVariant = function (WH, exact) {
            var e_1, _a;
            if (exact === void 0) { exact = false; }
            if (this.stretch.dir !== 0) {
                var D = this.getWH(WH);
                var min = this.getSize('minsize', 0);
                var max = this.getSize('maxsize', Infinity);
                var mathaccent = this.node.getProperty('mathaccent');
                D = Math.max(min, Math.min(max, D));
                var df = this.font.params.delimiterfactor / 1000;
                var ds = this.font.params.delimitershortfall;
                var m = (min || exact ? D : mathaccent ? Math.min(D / df, D + ds) : Math.max(D * df, D - ds));
                var delim = this.stretch;
                var c = delim.c || this.getText().codePointAt(0);
                var i = 0;
                if (delim.sizes) {
                    try {
                        for (var _b = __values(delim.sizes), _c = _b.next(); !_c.done; _c = _b.next()) {
                            var d = _c.value;
                            if (d >= m) {
                                if (mathaccent && i) {
                                    i--;
                                }
                                this.variant = this.font.getSizeVariant(c, i);
                                this.size = i;
                                if (delim.schar && delim.schar[i]) {
                                    this.stretch = __assign(__assign({}, this.stretch), { c: delim.schar[i] });
                                }
                                return;
                            }
                            i++;
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
                if (delim.stretch) {
                    this.size = -1;
                    this.invalidateBBox();
                    this.getStretchBBox(WH, this.checkExtendedHeight(D, delim), delim);
                }
                else {
                    this.variant = this.font.getSizeVariant(c, i - 1);
                    this.size = i - 1;
                }
            }
        };
        class_1.prototype.getSize = function (name, value) {
            var attributes = this.node.attributes;
            if (attributes.isSet(name)) {
                value = this.length2em(attributes.get(name), 1, 1);
            }
            return value;
        };
        class_1.prototype.getWH = function (WH) {
            if (WH.length === 0)
                return 0;
            if (WH.length === 1)
                return WH[0];
            var _a = __read(WH, 2), H = _a[0], D = _a[1];
            var a = this.font.params.axis_height;
            return (this.node.attributes.get('symmetric') ? 2 * Math.max(H - a, D + a) : H + D);
        };
        class_1.prototype.getStretchBBox = function (WHD, D, C) {
            var _a;
            if (C.hasOwnProperty('min') && C.min > D) {
                D = C.min;
            }
            var _b = __read(C.HDW, 3), h = _b[0], d = _b[1], w = _b[2];
            if (this.stretch.dir === 1) {
                _a = __read(this.getBaseline(WHD, D, C), 2), h = _a[0], d = _a[1];
            }
            else {
                w = D;
            }
            this.bbox.h = h;
            this.bbox.d = d;
            this.bbox.w = w;
        };
        class_1.prototype.getBaseline = function (WHD, HD, C) {
            var hasWHD = (WHD.length === 2 && WHD[0] + WHD[1] === HD);
            var symmetric = this.node.attributes.get('symmetric');
            var _a = __read((hasWHD ? WHD : [HD, 0]), 2), H = _a[0], D = _a[1];
            var _b = __read([H + D, 0], 2), h = _b[0], d = _b[1];
            if (symmetric) {
                var a = this.font.params.axis_height;
                if (hasWHD) {
                    h = 2 * Math.max(H - a, D + a);
                }
                d = h / 2 - a;
            }
            else if (hasWHD) {
                d = D;
            }
            else {
                var _c = __read((C.HDW || [.75, .25]), 2), ch = _c[0], cd = _c[1];
                d = cd * (h / (ch + cd));
            }
            return [h - d, d];
        };
        class_1.prototype.checkExtendedHeight = function (D, C) {
            if (C.fullExt) {
                var _a = __read(C.fullExt, 2), extSize = _a[0], endSize = _a[1];
                var n = Math.ceil(Math.max(0, D - endSize) / extSize);
                D = endSize + n * extSize;
            }
            return D;
        };
        class_1.prototype.remapChars = function (chars) {
            var primes = this.node.getProperty('primes');
            if (primes) {
                return (0, string_js_1.unicodeChars)(primes);
            }
            if (chars.length === 1) {
                var parent_1 = this.node.coreParent().parent;
                var isAccent = this.isAccent && !parent_1.isKind('mrow');
                var map = (isAccent ? 'accent' : 'mo');
                var text = this.font.getRemappedChar(map, chars[0]);
                if (text) {
                    chars = this.unicodeChars(text, this.variant);
                }
            }
            return chars;
        };
        return class_1;
    }(Base));
}
exports.CommonMoMixin = CommonMoMixin;
//# sourceMappingURL=mo.js.map

/***/ }),

/***/ 7481:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMpaddedMixin = void 0;
function CommonMpaddedMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.getDimens = function () {
            var values = this.node.attributes.getList('width', 'height', 'depth', 'lspace', 'voffset');
            var bbox = this.childNodes[0].getBBox();
            var w = bbox.w, h = bbox.h, d = bbox.d;
            var W = w, H = h, D = d, x = 0, y = 0, dx = 0;
            if (values.width !== '')
                w = this.dimen(values.width, bbox, 'w', 0);
            if (values.height !== '')
                h = this.dimen(values.height, bbox, 'h', 0);
            if (values.depth !== '')
                d = this.dimen(values.depth, bbox, 'd', 0);
            if (values.voffset !== '')
                y = this.dimen(values.voffset, bbox);
            if (values.lspace !== '')
                x = this.dimen(values.lspace, bbox);
            var align = this.node.attributes.get('data-align');
            if (align) {
                dx = this.getAlignX(w, bbox, align);
            }
            return [H, D, W, h - H, d - D, w - W, x, y, dx];
        };
        class_1.prototype.dimen = function (length, bbox, d, m) {
            if (d === void 0) { d = ''; }
            if (m === void 0) { m = null; }
            length = String(length);
            var match = length.match(/width|height|depth/);
            var size = (match ? bbox[match[0].charAt(0)] :
                (d ? bbox[d] : 0));
            var dimen = (this.length2em(length, size) || 0);
            if (length.match(/^[-+]/) && d) {
                dimen += size;
            }
            if (m != null) {
                dimen = Math.max(m, dimen);
            }
            return dimen;
        };
        class_1.prototype.computeBBox = function (bbox, recompute) {
            if (recompute === void 0) { recompute = false; }
            var _a = __read(this.getDimens(), 6), H = _a[0], D = _a[1], W = _a[2], dh = _a[3], dd = _a[4], dw = _a[5];
            bbox.w = W + dw;
            bbox.h = H + dh;
            bbox.d = D + dd;
            this.setChildPWidths(recompute, bbox.w);
        };
        class_1.prototype.getWrapWidth = function (_i) {
            return this.getBBox().w;
        };
        class_1.prototype.getChildAlign = function (_i) {
            return this.node.attributes.get('data-align') || 'left';
        };
        return class_1;
    }(Base));
}
exports.CommonMpaddedMixin = CommonMpaddedMixin;
//# sourceMappingURL=mpadded.js.map

/***/ }),

/***/ 5997:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMrootMixin = void 0;
function CommonMrootMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        Object.defineProperty(class_1.prototype, "surd", {
            get: function () {
                return 2;
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_1.prototype, "root", {
            get: function () {
                return 1;
            },
            enumerable: false,
            configurable: true
        });
        class_1.prototype.combineRootBBox = function (BBOX, sbox, H) {
            var bbox = this.childNodes[this.root].getOuterBBox();
            var h = this.getRootDimens(sbox, H)[1];
            BBOX.combine(bbox, 0, h);
        };
        class_1.prototype.getRootDimens = function (sbox, H) {
            var surd = this.childNodes[this.surd];
            var bbox = this.childNodes[this.root].getOuterBBox();
            var offset = (surd.size < 0 ? .5 : .6) * sbox.w;
            var w = bbox.w, rscale = bbox.rscale;
            var W = Math.max(w, offset / rscale);
            var dx = Math.max(0, W - w);
            var h = this.rootHeight(bbox, sbox, surd.size, H);
            var x = W * rscale - offset;
            return [x, h, dx];
        };
        class_1.prototype.rootHeight = function (rbox, sbox, size, H) {
            var h = sbox.h + sbox.d;
            var b = (size < 0 ? 1.9 : .55 * h) - (h - H);
            return b + Math.max(0, rbox.d * rbox.rscale);
        };
        return class_1;
    }(Base));
}
exports.CommonMrootMixin = CommonMrootMixin;
//# sourceMappingURL=mroot.js.map

/***/ }),

/***/ 9323:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonInferredMrowMixin = exports.CommonMrowMixin = void 0;
var BBox_js_1 = __webpack_require__(3717);
function CommonMrowMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var e_1, _a;
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.stretchChildren();
            try {
                for (var _b = __values(_this.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var child = _c.value;
                    if (child.bbox.pwidth) {
                        _this.bbox.pwidth = BBox_js_1.BBox.fullWidth;
                        break;
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
            return _this;
        }
        Object.defineProperty(class_1.prototype, "fixesPWidth", {
            get: function () {
                return false;
            },
            enumerable: false,
            configurable: true
        });
        class_1.prototype.stretchChildren = function () {
            var e_2, _a, e_3, _b, e_4, _c;
            var stretchy = [];
            try {
                for (var _d = __values(this.childNodes), _e = _d.next(); !_e.done; _e = _d.next()) {
                    var child = _e.value;
                    if (child.canStretch(1)) {
                        stretchy.push(child);
                    }
                }
            }
            catch (e_2_1) { e_2 = { error: e_2_1 }; }
            finally {
                try {
                    if (_e && !_e.done && (_a = _d.return)) _a.call(_d);
                }
                finally { if (e_2) throw e_2.error; }
            }
            var count = stretchy.length;
            var nodeCount = this.childNodes.length;
            if (count && nodeCount > 1) {
                var H = 0, D = 0;
                var all = (count > 1 && count === nodeCount);
                try {
                    for (var _f = __values(this.childNodes), _g = _f.next(); !_g.done; _g = _f.next()) {
                        var child = _g.value;
                        var noStretch = (child.stretch.dir === 0);
                        if (all || noStretch) {
                            var _h = child.getOuterBBox(noStretch), h = _h.h, d = _h.d, rscale = _h.rscale;
                            h *= rscale;
                            d *= rscale;
                            if (h > H)
                                H = h;
                            if (d > D)
                                D = d;
                        }
                    }
                }
                catch (e_3_1) { e_3 = { error: e_3_1 }; }
                finally {
                    try {
                        if (_g && !_g.done && (_b = _f.return)) _b.call(_f);
                    }
                    finally { if (e_3) throw e_3.error; }
                }
                try {
                    for (var stretchy_1 = __values(stretchy), stretchy_1_1 = stretchy_1.next(); !stretchy_1_1.done; stretchy_1_1 = stretchy_1.next()) {
                        var child = stretchy_1_1.value;
                        child.coreMO().getStretchedVariant([H, D]);
                    }
                }
                catch (e_4_1) { e_4 = { error: e_4_1 }; }
                finally {
                    try {
                        if (stretchy_1_1 && !stretchy_1_1.done && (_c = stretchy_1.return)) _c.call(stretchy_1);
                    }
                    finally { if (e_4) throw e_4.error; }
                }
            }
        };
        return class_1;
    }(Base));
}
exports.CommonMrowMixin = CommonMrowMixin;
function CommonInferredMrowMixin(Base) {
    return (function (_super) {
        __extends(class_2, _super);
        function class_2() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_2.prototype.getScale = function () {
            this.bbox.scale = this.parent.bbox.scale;
            this.bbox.rscale = 1;
        };
        return class_2;
    }(Base));
}
exports.CommonInferredMrowMixin = CommonInferredMrowMixin;
//# sourceMappingURL=mrow.js.map

/***/ }),

/***/ 6920:
/***/ (function(__unused_webpack_module, exports) {


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
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMsMixin = void 0;
function CommonMsMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            var attributes = _this.node.attributes;
            var quotes = attributes.getList('lquote', 'rquote');
            if (_this.variant !== 'monospace') {
                if (!attributes.isSet('lquote') && quotes.lquote === '"')
                    quotes.lquote = '\u201C';
                if (!attributes.isSet('rquote') && quotes.rquote === '"')
                    quotes.rquote = '\u201D';
            }
            _this.childNodes.unshift(_this.createText(quotes.lquote));
            _this.childNodes.push(_this.createText(quotes.rquote));
            return _this;
        }
        class_1.prototype.createText = function (text) {
            var node = this.wrap(this.mmlText(text));
            node.parent = this;
            return node;
        };
        return class_1;
    }(Base));
}
exports.CommonMsMixin = CommonMsMixin;
//# sourceMappingURL=ms.js.map

/***/ }),

/***/ 37:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMspaceMixin = void 0;
function CommonMspaceMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.computeBBox = function (bbox, _recompute) {
            if (_recompute === void 0) { _recompute = false; }
            var attributes = this.node.attributes;
            bbox.w = this.length2em(attributes.get('width'), 0);
            bbox.h = this.length2em(attributes.get('height'), 0);
            bbox.d = this.length2em(attributes.get('depth'), 0);
        };
        class_1.prototype.handleVariant = function () {
        };
        return class_1;
    }(Base));
}
exports.CommonMspaceMixin = CommonMspaceMixin;
//# sourceMappingURL=mspace.js.map

/***/ }),

/***/ 222:
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
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMsqrtMixin = void 0;
var BBox_js_1 = __webpack_require__(3717);
function CommonMsqrtMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            var surd = _this.createMo('\u221A');
            surd.canStretch(1);
            var _a = _this.childNodes[_this.base].getOuterBBox(), h = _a.h, d = _a.d;
            var t = _this.font.params.rule_thickness;
            var p = (_this.node.attributes.get('displaystyle') ? _this.font.params.x_height : t);
            _this.surdH = h + d + 2 * t + p / 4;
            surd.getStretchedVariant([_this.surdH - d, d], true);
            return _this;
        }
        Object.defineProperty(class_1.prototype, "base", {
            get: function () {
                return 0;
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_1.prototype, "surd", {
            get: function () {
                return 1;
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_1.prototype, "root", {
            get: function () {
                return null;
            },
            enumerable: false,
            configurable: true
        });
        class_1.prototype.createMo = function (text) {
            var node = _super.prototype.createMo.call(this, text);
            this.childNodes.push(node);
            return node;
        };
        class_1.prototype.computeBBox = function (bbox, recompute) {
            if (recompute === void 0) { recompute = false; }
            var surdbox = this.childNodes[this.surd].getBBox();
            var basebox = new BBox_js_1.BBox(this.childNodes[this.base].getOuterBBox());
            var q = this.getPQ(surdbox)[1];
            var t = this.font.params.rule_thickness;
            var H = basebox.h + q + t;
            var _a = __read(this.getRootDimens(surdbox, H), 1), x = _a[0];
            bbox.h = H + t;
            this.combineRootBBox(bbox, surdbox, H);
            bbox.combine(surdbox, x, H - surdbox.h);
            bbox.combine(basebox, x + surdbox.w, 0);
            bbox.clean();
            this.setChildPWidths(recompute);
        };
        class_1.prototype.combineRootBBox = function (_bbox, _sbox, _H) {
        };
        class_1.prototype.getPQ = function (sbox) {
            var t = this.font.params.rule_thickness;
            var p = (this.node.attributes.get('displaystyle') ? this.font.params.x_height : t);
            var q = (sbox.h + sbox.d > this.surdH ?
                ((sbox.h + sbox.d) - (this.surdH - 2 * t - p / 2)) / 2 :
                t + p / 4);
            return [p, q];
        };
        class_1.prototype.getRootDimens = function (_sbox, _H) {
            return [0, 0, 0, 0];
        };
        return class_1;
    }(Base));
}
exports.CommonMsqrtMixin = CommonMsqrtMixin;
//# sourceMappingURL=msqrt.js.map

/***/ }),

/***/ 3069:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMsubsupMixin = exports.CommonMsupMixin = exports.CommonMsubMixin = void 0;
function CommonMsubMixin(Base) {
    var _a;
    return _a = (function (_super) {
            __extends(class_1, _super);
            function class_1() {
                return _super !== null && _super.apply(this, arguments) || this;
            }
            Object.defineProperty(class_1.prototype, "scriptChild", {
                get: function () {
                    return this.childNodes[this.node.sub];
                },
                enumerable: false,
                configurable: true
            });
            class_1.prototype.getOffset = function () {
                return [0, -this.getV()];
            };
            return class_1;
        }(Base)),
        _a.useIC = false,
        _a;
}
exports.CommonMsubMixin = CommonMsubMixin;
function CommonMsupMixin(Base) {
    return (function (_super) {
        __extends(class_2, _super);
        function class_2() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        Object.defineProperty(class_2.prototype, "scriptChild", {
            get: function () {
                return this.childNodes[this.node.sup];
            },
            enumerable: false,
            configurable: true
        });
        class_2.prototype.getOffset = function () {
            var x = this.getAdjustedIc() - (this.baseRemoveIc ? 0 : this.baseIc);
            return [x, this.getU()];
        };
        return class_2;
    }(Base));
}
exports.CommonMsupMixin = CommonMsupMixin;
function CommonMsubsupMixin(Base) {
    var _a;
    return _a = (function (_super) {
            __extends(class_3, _super);
            function class_3() {
                var _this = _super !== null && _super.apply(this, arguments) || this;
                _this.UVQ = null;
                return _this;
            }
            Object.defineProperty(class_3.prototype, "subChild", {
                get: function () {
                    return this.childNodes[this.node.sub];
                },
                enumerable: false,
                configurable: true
            });
            Object.defineProperty(class_3.prototype, "supChild", {
                get: function () {
                    return this.childNodes[this.node.sup];
                },
                enumerable: false,
                configurable: true
            });
            class_3.prototype.computeBBox = function (bbox, recompute) {
                if (recompute === void 0) { recompute = false; }
                var basebox = this.baseChild.getOuterBBox();
                var _a = __read([this.subChild.getOuterBBox(), this.supChild.getOuterBBox()], 2), subbox = _a[0], supbox = _a[1];
                bbox.empty();
                bbox.append(basebox);
                var w = this.getBaseWidth();
                var x = this.getAdjustedIc();
                var _b = __read(this.getUVQ(), 2), u = _b[0], v = _b[1];
                bbox.combine(subbox, w, v);
                bbox.combine(supbox, w + x, u);
                bbox.w += this.font.params.scriptspace;
                bbox.clean();
                this.setChildPWidths(recompute);
            };
            class_3.prototype.getUVQ = function (subbox, supbox) {
                if (subbox === void 0) { subbox = this.subChild.getOuterBBox(); }
                if (supbox === void 0) { supbox = this.supChild.getOuterBBox(); }
                var basebox = this.baseCore.getOuterBBox();
                if (this.UVQ)
                    return this.UVQ;
                var tex = this.font.params;
                var t = 3 * tex.rule_thickness;
                var subscriptshift = this.length2em(this.node.attributes.get('subscriptshift'), tex.sub2);
                var drop = this.baseCharZero(basebox.d * this.baseScale + tex.sub_drop * subbox.rscale);
                var _a = __read([this.getU(), Math.max(drop, subscriptshift)], 2), u = _a[0], v = _a[1];
                var q = (u - supbox.d * supbox.rscale) - (subbox.h * subbox.rscale - v);
                if (q < t) {
                    v += t - q;
                    var p = (4 / 5) * tex.x_height - (u - supbox.d * supbox.rscale);
                    if (p > 0) {
                        u += p;
                        v -= p;
                    }
                }
                u = Math.max(this.length2em(this.node.attributes.get('superscriptshift'), u), u);
                v = Math.max(this.length2em(this.node.attributes.get('subscriptshift'), v), v);
                q = (u - supbox.d * supbox.rscale) - (subbox.h * subbox.rscale - v);
                this.UVQ = [u, -v, q];
                return this.UVQ;
            };
            return class_3;
        }(Base)),
        _a.useIC = false,
        _a;
}
exports.CommonMsubsupMixin = CommonMsubsupMixin;
//# sourceMappingURL=msubsup.js.map

/***/ }),

/***/ 8589:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMtableMixin = void 0;
var BBox_js_1 = __webpack_require__(3717);
var string_js_1 = __webpack_require__(6720);
var numeric_js_1 = __webpack_require__(1490);
function CommonMtableMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.numCols = 0;
            _this.numRows = 0;
            _this.data = null;
            _this.pwidthCells = [];
            _this.pWidth = 0;
            _this.numCols = (0, numeric_js_1.max)(_this.tableRows.map(function (row) { return row.numCells; }));
            _this.numRows = _this.childNodes.length;
            _this.hasLabels = _this.childNodes.reduce(function (value, row) { return value || row.node.isKind('mlabeledtr'); }, false);
            _this.findContainer();
            _this.isTop = !_this.container || (_this.container.node.isKind('math') && !_this.container.parent);
            if (_this.isTop) {
                _this.jax.table = _this;
            }
            _this.getPercentageWidth();
            var attributes = _this.node.attributes;
            _this.frame = attributes.get('frame') !== 'none';
            _this.fLine = (_this.frame && attributes.get('frame') ? .07 : 0);
            _this.fSpace = (_this.frame ? _this.convertLengths(_this.getAttributeArray('framespacing')) : [0, 0]);
            _this.cSpace = _this.convertLengths(_this.getColumnAttributes('columnspacing'));
            _this.rSpace = _this.convertLengths(_this.getRowAttributes('rowspacing'));
            _this.cLines = _this.getColumnAttributes('columnlines').map(function (x) { return (x === 'none' ? 0 : .07); });
            _this.rLines = _this.getRowAttributes('rowlines').map(function (x) { return (x === 'none' ? 0 : .07); });
            _this.cWidths = _this.getColumnWidths();
            _this.stretchRows();
            _this.stretchColumns();
            return _this;
        }
        Object.defineProperty(class_1.prototype, "tableRows", {
            get: function () {
                return this.childNodes;
            },
            enumerable: false,
            configurable: true
        });
        class_1.prototype.findContainer = function () {
            var node = this;
            var parent = node.parent;
            while (parent && (parent.node.notParent || parent.node.isKind('mrow'))) {
                node = parent;
                parent = parent.parent;
            }
            this.container = parent;
            this.containerI = node.node.childPosition();
        };
        class_1.prototype.getPercentageWidth = function () {
            if (this.hasLabels) {
                this.bbox.pwidth = BBox_js_1.BBox.fullWidth;
            }
            else {
                var width = this.node.attributes.get('width');
                if ((0, string_js_1.isPercent)(width)) {
                    this.bbox.pwidth = width;
                }
            }
        };
        class_1.prototype.stretchRows = function () {
            var equal = this.node.attributes.get('equalrows');
            var HD = (equal ? this.getEqualRowHeight() : 0);
            var _a = (equal ? this.getTableData() : { H: [0], D: [0] }), H = _a.H, D = _a.D;
            var rows = this.tableRows;
            for (var i = 0; i < this.numRows; i++) {
                var hd = (equal ? [(HD + H[i] - D[i]) / 2, (HD - H[i] + D[i]) / 2] : null);
                rows[i].stretchChildren(hd);
            }
        };
        class_1.prototype.stretchColumns = function () {
            for (var i = 0; i < this.numCols; i++) {
                var width = (typeof this.cWidths[i] === 'number' ? this.cWidths[i] : null);
                this.stretchColumn(i, width);
            }
        };
        class_1.prototype.stretchColumn = function (i, W) {
            var e_1, _a, e_2, _b, e_3, _c;
            var stretchy = [];
            try {
                for (var _d = __values(this.tableRows), _e = _d.next(); !_e.done; _e = _d.next()) {
                    var row = _e.value;
                    var cell = row.getChild(i);
                    if (cell) {
                        var child = cell.childNodes[0];
                        if (child.stretch.dir === 0 &&
                            child.canStretch(2)) {
                            stretchy.push(child);
                        }
                    }
                }
            }
            catch (e_1_1) { e_1 = { error: e_1_1 }; }
            finally {
                try {
                    if (_e && !_e.done && (_a = _d.return)) _a.call(_d);
                }
                finally { if (e_1) throw e_1.error; }
            }
            var count = stretchy.length;
            var nodeCount = this.childNodes.length;
            if (count && nodeCount > 1) {
                if (W === null) {
                    W = 0;
                    var all = (count > 1 && count === nodeCount);
                    try {
                        for (var _f = __values(this.tableRows), _g = _f.next(); !_g.done; _g = _f.next()) {
                            var row = _g.value;
                            var cell = row.getChild(i);
                            if (cell) {
                                var child = cell.childNodes[0];
                                var noStretch = (child.stretch.dir === 0);
                                if (all || noStretch) {
                                    var w = child.getBBox(noStretch).w;
                                    if (w > W) {
                                        W = w;
                                    }
                                }
                            }
                        }
                    }
                    catch (e_2_1) { e_2 = { error: e_2_1 }; }
                    finally {
                        try {
                            if (_g && !_g.done && (_b = _f.return)) _b.call(_f);
                        }
                        finally { if (e_2) throw e_2.error; }
                    }
                }
                try {
                    for (var stretchy_1 = __values(stretchy), stretchy_1_1 = stretchy_1.next(); !stretchy_1_1.done; stretchy_1_1 = stretchy_1.next()) {
                        var child = stretchy_1_1.value;
                        child.coreMO().getStretchedVariant([W]);
                    }
                }
                catch (e_3_1) { e_3 = { error: e_3_1 }; }
                finally {
                    try {
                        if (stretchy_1_1 && !stretchy_1_1.done && (_c = stretchy_1.return)) _c.call(stretchy_1);
                    }
                    finally { if (e_3) throw e_3.error; }
                }
            }
        };
        class_1.prototype.getTableData = function () {
            if (this.data) {
                return this.data;
            }
            var H = new Array(this.numRows).fill(0);
            var D = new Array(this.numRows).fill(0);
            var W = new Array(this.numCols).fill(0);
            var NH = new Array(this.numRows);
            var ND = new Array(this.numRows);
            var LW = [0];
            var rows = this.tableRows;
            for (var j = 0; j < rows.length; j++) {
                var M = 0;
                var row = rows[j];
                var align = row.node.attributes.get('rowalign');
                for (var i = 0; i < row.numCells; i++) {
                    var cell = row.getChild(i);
                    M = this.updateHDW(cell, i, j, align, H, D, W, M);
                    this.recordPWidthCell(cell, i);
                }
                NH[j] = H[j];
                ND[j] = D[j];
                if (row.labeled) {
                    M = this.updateHDW(row.childNodes[0], 0, j, align, H, D, LW, M);
                }
                this.extendHD(j, H, D, M);
                this.extendHD(j, NH, ND, M);
            }
            var L = LW[0];
            this.data = { H: H, D: D, W: W, NH: NH, ND: ND, L: L };
            return this.data;
        };
        class_1.prototype.updateHDW = function (cell, i, j, align, H, D, W, M) {
            var _a = cell.getBBox(), h = _a.h, d = _a.d, w = _a.w;
            var scale = cell.parent.bbox.rscale;
            if (cell.parent.bbox.rscale !== 1) {
                h *= scale;
                d *= scale;
                w *= scale;
            }
            if (this.node.getProperty('useHeight')) {
                if (h < .75)
                    h = .75;
                if (d < .25)
                    d = .25;
            }
            var m = 0;
            align = cell.node.attributes.get('rowalign') || align;
            if (align !== 'baseline' && align !== 'axis') {
                m = h + d;
                h = d = 0;
            }
            if (h > H[j])
                H[j] = h;
            if (d > D[j])
                D[j] = d;
            if (m > M)
                M = m;
            if (W && w > W[i])
                W[i] = w;
            return M;
        };
        class_1.prototype.extendHD = function (i, H, D, M) {
            var d = (M - (H[i] + D[i])) / 2;
            if (d < .00001)
                return;
            H[i] += d;
            D[i] += d;
        };
        class_1.prototype.recordPWidthCell = function (cell, i) {
            if (cell.childNodes[0] && cell.childNodes[0].getBBox().pwidth) {
                this.pwidthCells.push([cell, i]);
            }
        };
        class_1.prototype.computeBBox = function (bbox, _recompute) {
            if (_recompute === void 0) { _recompute = false; }
            var _a = this.getTableData(), H = _a.H, D = _a.D;
            var height, width;
            if (this.node.attributes.get('equalrows')) {
                var HD = this.getEqualRowHeight();
                height = (0, numeric_js_1.sum)([].concat(this.rLines, this.rSpace)) + HD * this.numRows;
            }
            else {
                height = (0, numeric_js_1.sum)(H.concat(D, this.rLines, this.rSpace));
            }
            height += 2 * (this.fLine + this.fSpace[1]);
            var CW = this.getComputedWidths();
            width = (0, numeric_js_1.sum)(CW.concat(this.cLines, this.cSpace)) + 2 * (this.fLine + this.fSpace[0]);
            var w = this.node.attributes.get('width');
            if (w !== 'auto') {
                width = Math.max(this.length2em(w, 0) + 2 * this.fLine, width);
            }
            var _b = __read(this.getBBoxHD(height), 2), h = _b[0], d = _b[1];
            bbox.h = h;
            bbox.d = d;
            bbox.w = width;
            var _c = __read(this.getBBoxLR(), 2), L = _c[0], R = _c[1];
            bbox.L = L;
            bbox.R = R;
            if (!(0, string_js_1.isPercent)(w)) {
                this.setColumnPWidths();
            }
        };
        class_1.prototype.setChildPWidths = function (_recompute, cwidth, _clear) {
            var width = this.node.attributes.get('width');
            if (!(0, string_js_1.isPercent)(width))
                return false;
            if (!this.hasLabels) {
                this.bbox.pwidth = '';
                this.container.bbox.pwidth = '';
            }
            var _a = this.bbox, w = _a.w, L = _a.L, R = _a.R;
            var labelInWidth = this.node.attributes.get('data-width-includes-label');
            var W = Math.max(w, this.length2em(width, Math.max(cwidth, L + w + R))) - (labelInWidth ? L + R : 0);
            var cols = (this.node.attributes.get('equalcolumns') ?
                Array(this.numCols).fill(this.percent(1 / Math.max(1, this.numCols))) :
                this.getColumnAttributes('columnwidth', 0));
            this.cWidths = this.getColumnWidthsFixed(cols, W);
            var CW = this.getComputedWidths();
            this.pWidth = (0, numeric_js_1.sum)(CW.concat(this.cLines, this.cSpace)) + 2 * (this.fLine + this.fSpace[0]);
            if (this.isTop) {
                this.bbox.w = this.pWidth;
            }
            this.setColumnPWidths();
            if (this.pWidth !== w) {
                this.parent.invalidateBBox();
            }
            return this.pWidth !== w;
        };
        class_1.prototype.setColumnPWidths = function () {
            var e_4, _a;
            var W = this.cWidths;
            try {
                for (var _b = __values(this.pwidthCells), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var _d = __read(_c.value, 2), cell = _d[0], i = _d[1];
                    if (cell.setChildPWidths(false, W[i])) {
                        cell.invalidateBBox();
                        cell.getBBox();
                    }
                }
            }
            catch (e_4_1) { e_4 = { error: e_4_1 }; }
            finally {
                try {
                    if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
                }
                finally { if (e_4) throw e_4.error; }
            }
        };
        class_1.prototype.getBBoxHD = function (height) {
            var _a = __read(this.getAlignmentRow(), 2), align = _a[0], row = _a[1];
            if (row === null) {
                var a = this.font.params.axis_height;
                var h2 = height / 2;
                var HD = {
                    top: [0, height],
                    center: [h2, h2],
                    bottom: [height, 0],
                    baseline: [h2, h2],
                    axis: [h2 + a, h2 - a]
                };
                return HD[align] || [h2, h2];
            }
            else {
                var y = this.getVerticalPosition(row, align);
                return [y, height - y];
            }
        };
        class_1.prototype.getBBoxLR = function () {
            if (this.hasLabels) {
                var attributes = this.node.attributes;
                var side = attributes.get('side');
                var _a = __read(this.getPadAlignShift(side), 2), pad = _a[0], align = _a[1];
                var labels = this.hasLabels && !!attributes.get('data-width-includes-label');
                if (labels && this.frame && this.fSpace[0]) {
                    pad -= this.fSpace[0];
                }
                return (align === 'center' && !labels ? [pad, pad] :
                    side === 'left' ? [pad, 0] : [0, pad]);
            }
            return [0, 0];
        };
        class_1.prototype.getPadAlignShift = function (side) {
            var L = this.getTableData().L;
            var sep = this.length2em(this.node.attributes.get('minlabelspacing'));
            var pad = L + sep;
            var _a = __read((this.styles == null ? ['', ''] :
                [this.styles.get('padding-left'), this.styles.get('padding-right')]), 2), lpad = _a[0], rpad = _a[1];
            if (lpad || rpad) {
                pad = Math.max(pad, this.length2em(lpad || '0'), this.length2em(rpad || '0'));
            }
            var _b = __read(this.getAlignShift(), 2), align = _b[0], shift = _b[1];
            if (align === side) {
                shift = (side === 'left' ? Math.max(pad, shift) - pad : Math.min(-pad, shift) + pad);
            }
            return [pad, align, shift];
        };
        class_1.prototype.getAlignShift = function () {
            return (this.isTop ? _super.prototype.getAlignShift.call(this) :
                [this.container.getChildAlign(this.containerI), 0]);
        };
        class_1.prototype.getWidth = function () {
            return this.pWidth || this.getBBox().w;
        };
        class_1.prototype.getEqualRowHeight = function () {
            var _a = this.getTableData(), H = _a.H, D = _a.D;
            var HD = Array.from(H.keys()).map(function (i) { return H[i] + D[i]; });
            return Math.max.apply(Math, HD);
        };
        class_1.prototype.getComputedWidths = function () {
            var _this = this;
            var W = this.getTableData().W;
            var CW = Array.from(W.keys()).map(function (i) {
                return (typeof _this.cWidths[i] === 'number' ? _this.cWidths[i] : W[i]);
            });
            if (this.node.attributes.get('equalcolumns')) {
                CW = Array(CW.length).fill((0, numeric_js_1.max)(CW));
            }
            return CW;
        };
        class_1.prototype.getColumnWidths = function () {
            var width = this.node.attributes.get('width');
            if (this.node.attributes.get('equalcolumns')) {
                return this.getEqualColumns(width);
            }
            var swidths = this.getColumnAttributes('columnwidth', 0);
            if (width === 'auto') {
                return this.getColumnWidthsAuto(swidths);
            }
            if ((0, string_js_1.isPercent)(width)) {
                return this.getColumnWidthsPercent(swidths);
            }
            return this.getColumnWidthsFixed(swidths, this.length2em(width));
        };
        class_1.prototype.getEqualColumns = function (width) {
            var n = Math.max(1, this.numCols);
            var cwidth;
            if (width === 'auto') {
                var W = this.getTableData().W;
                cwidth = (0, numeric_js_1.max)(W);
            }
            else if ((0, string_js_1.isPercent)(width)) {
                cwidth = this.percent(1 / n);
            }
            else {
                var w = (0, numeric_js_1.sum)([].concat(this.cLines, this.cSpace)) + 2 * this.fSpace[0];
                cwidth = Math.max(0, this.length2em(width) - w) / n;
            }
            return Array(this.numCols).fill(cwidth);
        };
        class_1.prototype.getColumnWidthsAuto = function (swidths) {
            var _this = this;
            return swidths.map(function (x) {
                if (x === 'auto' || x === 'fit')
                    return null;
                if ((0, string_js_1.isPercent)(x))
                    return x;
                return _this.length2em(x);
            });
        };
        class_1.prototype.getColumnWidthsPercent = function (swidths) {
            var _this = this;
            var hasFit = swidths.indexOf('fit') >= 0;
            var W = (hasFit ? this.getTableData() : { W: null }).W;
            return Array.from(swidths.keys()).map(function (i) {
                var x = swidths[i];
                if (x === 'fit')
                    return null;
                if (x === 'auto')
                    return (hasFit ? W[i] : null);
                if ((0, string_js_1.isPercent)(x))
                    return x;
                return _this.length2em(x);
            });
        };
        class_1.prototype.getColumnWidthsFixed = function (swidths, width) {
            var _this = this;
            var indices = Array.from(swidths.keys());
            var fit = indices.filter(function (i) { return swidths[i] === 'fit'; });
            var auto = indices.filter(function (i) { return swidths[i] === 'auto'; });
            var n = fit.length || auto.length;
            var W = (n ? this.getTableData() : { W: null }).W;
            var cwidth = width - (0, numeric_js_1.sum)([].concat(this.cLines, this.cSpace)) - 2 * this.fSpace[0];
            var dw = cwidth;
            indices.forEach(function (i) {
                var x = swidths[i];
                dw -= (x === 'fit' || x === 'auto' ? W[i] : _this.length2em(x, cwidth));
            });
            var fw = (n && dw > 0 ? dw / n : 0);
            return indices.map(function (i) {
                var x = swidths[i];
                if (x === 'fit')
                    return W[i] + fw;
                if (x === 'auto')
                    return W[i] + (fit.length === 0 ? fw : 0);
                return _this.length2em(x, cwidth);
            });
        };
        class_1.prototype.getVerticalPosition = function (i, align) {
            var equal = this.node.attributes.get('equalrows');
            var _a = this.getTableData(), H = _a.H, D = _a.D;
            var HD = (equal ? this.getEqualRowHeight() : 0);
            var space = this.getRowHalfSpacing();
            var y = this.fLine;
            for (var j = 0; j < i; j++) {
                y += space[j] + (equal ? HD : H[j] + D[j]) + space[j + 1] + this.rLines[j];
            }
            var _b = __read((equal ? [(HD + H[i] - D[i]) / 2, (HD - H[i] + D[i]) / 2] : [H[i], D[i]]), 2), h = _b[0], d = _b[1];
            var offset = {
                top: 0,
                center: space[i] + (h + d) / 2,
                bottom: space[i] + h + d + space[i + 1],
                baseline: space[i] + h,
                axis: space[i] + h - .25
            };
            y += offset[align] || 0;
            return y;
        };
        class_1.prototype.getEmHalfSpacing = function (fspace, space, scale) {
            if (scale === void 0) { scale = 1; }
            var fspaceEm = this.em(fspace * scale);
            var spaceEm = this.addEm(space, 2 / scale);
            spaceEm.unshift(fspaceEm);
            spaceEm.push(fspaceEm);
            return spaceEm;
        };
        class_1.prototype.getRowHalfSpacing = function () {
            var space = this.rSpace.map(function (x) { return x / 2; });
            space.unshift(this.fSpace[1]);
            space.push(this.fSpace[1]);
            return space;
        };
        class_1.prototype.getColumnHalfSpacing = function () {
            var space = this.cSpace.map(function (x) { return x / 2; });
            space.unshift(this.fSpace[0]);
            space.push(this.fSpace[0]);
            return space;
        };
        class_1.prototype.getAlignmentRow = function () {
            var _a = __read((0, string_js_1.split)(this.node.attributes.get('align')), 2), align = _a[0], row = _a[1];
            if (row == null)
                return [align, null];
            var i = parseInt(row);
            if (i < 0)
                i += this.numRows + 1;
            return [align, i < 1 || i > this.numRows ? null : i - 1];
        };
        class_1.prototype.getColumnAttributes = function (name, i) {
            if (i === void 0) { i = 1; }
            var n = this.numCols - i;
            var columns = this.getAttributeArray(name);
            if (columns.length === 0)
                return null;
            while (columns.length < n) {
                columns.push(columns[columns.length - 1]);
            }
            if (columns.length > n) {
                columns.splice(n);
            }
            return columns;
        };
        class_1.prototype.getRowAttributes = function (name, i) {
            if (i === void 0) { i = 1; }
            var n = this.numRows - i;
            var rows = this.getAttributeArray(name);
            if (rows.length === 0)
                return null;
            while (rows.length < n) {
                rows.push(rows[rows.length - 1]);
            }
            if (rows.length > n) {
                rows.splice(n);
            }
            return rows;
        };
        class_1.prototype.getAttributeArray = function (name) {
            var value = this.node.attributes.get(name);
            if (!value)
                return [this.node.attributes.getDefault(name)];
            return (0, string_js_1.split)(value);
        };
        class_1.prototype.addEm = function (list, n) {
            var _this = this;
            if (n === void 0) { n = 1; }
            if (!list)
                return null;
            return list.map(function (x) { return _this.em(x / n); });
        };
        class_1.prototype.convertLengths = function (list) {
            var _this = this;
            if (!list)
                return null;
            return list.map(function (x) { return _this.length2em(x); });
        };
        return class_1;
    }(Base));
}
exports.CommonMtableMixin = CommonMtableMixin;
//# sourceMappingURL=mtable.js.map

/***/ }),

/***/ 7805:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMtdMixin = void 0;
function CommonMtdMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        Object.defineProperty(class_1.prototype, "fixesPWidth", {
            get: function () {
                return false;
            },
            enumerable: false,
            configurable: true
        });
        class_1.prototype.invalidateBBox = function () {
            this.bboxComputed = false;
        };
        class_1.prototype.getWrapWidth = function (_j) {
            var table = this.parent.parent;
            var row = this.parent;
            var i = this.node.childPosition() - (row.labeled ? 1 : 0);
            return (typeof (table.cWidths[i]) === 'number' ? table.cWidths[i] : table.getTableData().W[i]);
        };
        class_1.prototype.getChildAlign = function (_i) {
            return this.node.attributes.get('columnalign');
        };
        return class_1;
    }(Base));
}
exports.CommonMtdMixin = CommonMtdMixin;
//# sourceMappingURL=mtd.js.map

/***/ }),

/***/ 8325:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMtextMixin = void 0;
function CommonMtextMixin(Base) {
    var _a;
    return _a = (function (_super) {
            __extends(class_1, _super);
            function class_1() {
                return _super !== null && _super.apply(this, arguments) || this;
            }
            class_1.prototype.getVariant = function () {
                var options = this.jax.options;
                var data = this.jax.math.outputData;
                var merror = ((!!data.merrorFamily || !!options.merrorFont) && this.node.Parent.isKind('merror'));
                if (!!data.mtextFamily || !!options.mtextFont || merror) {
                    var variant = this.node.attributes.get('mathvariant');
                    var font = this.constructor.INHERITFONTS[variant] || this.jax.font.getCssFont(variant);
                    var family = font[0] || (merror ? data.merrorFamily || options.merrorFont :
                        data.mtextFamily || options.mtextFont);
                    this.variant = this.explicitVariant(family, font[2] ? 'bold' : '', font[1] ? 'italic' : '');
                    return;
                }
                _super.prototype.getVariant.call(this);
            };
            return class_1;
        }(Base)),
        _a.INHERITFONTS = {
            normal: ['', false, false],
            bold: ['', false, true],
            italic: ['', true, false],
            'bold-italic': ['', true, true]
        },
        _a;
}
exports.CommonMtextMixin = CommonMtextMixin;
//# sourceMappingURL=mtext.js.map

/***/ }),

/***/ 4818:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMlabeledtrMixin = exports.CommonMtrMixin = void 0;
function CommonMtrMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        Object.defineProperty(class_1.prototype, "fixesPWidth", {
            get: function () {
                return false;
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_1.prototype, "numCells", {
            get: function () {
                return this.childNodes.length;
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_1.prototype, "labeled", {
            get: function () {
                return false;
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_1.prototype, "tableCells", {
            get: function () {
                return this.childNodes;
            },
            enumerable: false,
            configurable: true
        });
        class_1.prototype.getChild = function (i) {
            return this.childNodes[i];
        };
        class_1.prototype.getChildBBoxes = function () {
            return this.childNodes.map(function (cell) { return cell.getBBox(); });
        };
        class_1.prototype.stretchChildren = function (HD) {
            var e_1, _a, e_2, _b, e_3, _c;
            if (HD === void 0) { HD = null; }
            var stretchy = [];
            var children = (this.labeled ? this.childNodes.slice(1) : this.childNodes);
            try {
                for (var children_1 = __values(children), children_1_1 = children_1.next(); !children_1_1.done; children_1_1 = children_1.next()) {
                    var mtd = children_1_1.value;
                    var child = mtd.childNodes[0];
                    if (child.canStretch(1)) {
                        stretchy.push(child);
                    }
                }
            }
            catch (e_1_1) { e_1 = { error: e_1_1 }; }
            finally {
                try {
                    if (children_1_1 && !children_1_1.done && (_a = children_1.return)) _a.call(children_1);
                }
                finally { if (e_1) throw e_1.error; }
            }
            var count = stretchy.length;
            var nodeCount = this.childNodes.length;
            if (count && nodeCount > 1) {
                if (HD === null) {
                    var H = 0, D = 0;
                    var all = (count > 1 && count === nodeCount);
                    try {
                        for (var children_2 = __values(children), children_2_1 = children_2.next(); !children_2_1.done; children_2_1 = children_2.next()) {
                            var mtd = children_2_1.value;
                            var child = mtd.childNodes[0];
                            var noStretch = (child.stretch.dir === 0);
                            if (all || noStretch) {
                                var _d = child.getBBox(noStretch), h = _d.h, d = _d.d;
                                if (h > H) {
                                    H = h;
                                }
                                if (d > D) {
                                    D = d;
                                }
                            }
                        }
                    }
                    catch (e_2_1) { e_2 = { error: e_2_1 }; }
                    finally {
                        try {
                            if (children_2_1 && !children_2_1.done && (_b = children_2.return)) _b.call(children_2);
                        }
                        finally { if (e_2) throw e_2.error; }
                    }
                    HD = [H, D];
                }
                try {
                    for (var stretchy_1 = __values(stretchy), stretchy_1_1 = stretchy_1.next(); !stretchy_1_1.done; stretchy_1_1 = stretchy_1.next()) {
                        var child = stretchy_1_1.value;
                        child.coreMO().getStretchedVariant(HD);
                    }
                }
                catch (e_3_1) { e_3 = { error: e_3_1 }; }
                finally {
                    try {
                        if (stretchy_1_1 && !stretchy_1_1.done && (_c = stretchy_1.return)) _c.call(stretchy_1);
                    }
                    finally { if (e_3) throw e_3.error; }
                }
            }
        };
        return class_1;
    }(Base));
}
exports.CommonMtrMixin = CommonMtrMixin;
function CommonMlabeledtrMixin(Base) {
    return (function (_super) {
        __extends(class_2, _super);
        function class_2() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        Object.defineProperty(class_2.prototype, "numCells", {
            get: function () {
                return Math.max(0, this.childNodes.length - 1);
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_2.prototype, "labeled", {
            get: function () {
                return true;
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_2.prototype, "tableCells", {
            get: function () {
                return this.childNodes.slice(1);
            },
            enumerable: false,
            configurable: true
        });
        class_2.prototype.getChild = function (i) {
            return this.childNodes[i + 1];
        };
        class_2.prototype.getChildBBoxes = function () {
            return this.childNodes.slice(1).map(function (cell) { return cell.getBBox(); });
        };
        return class_2;
    }(Base));
}
exports.CommonMlabeledtrMixin = CommonMlabeledtrMixin;
//# sourceMappingURL=mtr.js.map

/***/ }),

/***/ 9690:
/***/ (function(__unused_webpack_module, exports) {


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
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonMunderoverMixin = exports.CommonMoverMixin = exports.CommonMunderMixin = void 0;
function CommonMunderMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.stretchChildren();
            return _this;
        }
        Object.defineProperty(class_1.prototype, "scriptChild", {
            get: function () {
                return this.childNodes[this.node.under];
            },
            enumerable: false,
            configurable: true
        });
        class_1.prototype.computeBBox = function (bbox, recompute) {
            if (recompute === void 0) { recompute = false; }
            if (this.hasMovableLimits()) {
                _super.prototype.computeBBox.call(this, bbox, recompute);
                return;
            }
            bbox.empty();
            var basebox = this.baseChild.getOuterBBox();
            var underbox = this.scriptChild.getOuterBBox();
            var v = this.getUnderKV(basebox, underbox)[1];
            var delta = (this.isLineBelow ? 0 : this.getDelta(true));
            var _a = __read(this.getDeltaW([basebox, underbox], [0, -delta]), 2), bw = _a[0], uw = _a[1];
            bbox.combine(basebox, bw, 0);
            bbox.combine(underbox, uw, v);
            bbox.d += this.font.params.big_op_spacing5;
            bbox.clean();
            this.setChildPWidths(recompute);
        };
        return class_1;
    }(Base));
}
exports.CommonMunderMixin = CommonMunderMixin;
function CommonMoverMixin(Base) {
    return (function (_super) {
        __extends(class_2, _super);
        function class_2() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.stretchChildren();
            return _this;
        }
        Object.defineProperty(class_2.prototype, "scriptChild", {
            get: function () {
                return this.childNodes[this.node.over];
            },
            enumerable: false,
            configurable: true
        });
        class_2.prototype.computeBBox = function (bbox) {
            if (this.hasMovableLimits()) {
                _super.prototype.computeBBox.call(this, bbox);
                return;
            }
            bbox.empty();
            var basebox = this.baseChild.getOuterBBox();
            var overbox = this.scriptChild.getOuterBBox();
            if (this.node.attributes.get('accent')) {
                basebox.h = Math.max(basebox.h, this.font.params.x_height * basebox.scale);
            }
            var u = this.getOverKU(basebox, overbox)[1];
            var delta = (this.isLineAbove ? 0 : this.getDelta());
            var _a = __read(this.getDeltaW([basebox, overbox], [0, delta]), 2), bw = _a[0], ow = _a[1];
            bbox.combine(basebox, bw, 0);
            bbox.combine(overbox, ow, u);
            bbox.h += this.font.params.big_op_spacing5;
            bbox.clean();
        };
        return class_2;
    }(Base));
}
exports.CommonMoverMixin = CommonMoverMixin;
function CommonMunderoverMixin(Base) {
    return (function (_super) {
        __extends(class_3, _super);
        function class_3() {
            var args = [];
            for (var _i = 0; _i < arguments.length; _i++) {
                args[_i] = arguments[_i];
            }
            var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
            _this.stretchChildren();
            return _this;
        }
        Object.defineProperty(class_3.prototype, "underChild", {
            get: function () {
                return this.childNodes[this.node.under];
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_3.prototype, "overChild", {
            get: function () {
                return this.childNodes[this.node.over];
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_3.prototype, "subChild", {
            get: function () {
                return this.underChild;
            },
            enumerable: false,
            configurable: true
        });
        Object.defineProperty(class_3.prototype, "supChild", {
            get: function () {
                return this.overChild;
            },
            enumerable: false,
            configurable: true
        });
        class_3.prototype.computeBBox = function (bbox) {
            if (this.hasMovableLimits()) {
                _super.prototype.computeBBox.call(this, bbox);
                return;
            }
            bbox.empty();
            var overbox = this.overChild.getOuterBBox();
            var basebox = this.baseChild.getOuterBBox();
            var underbox = this.underChild.getOuterBBox();
            if (this.node.attributes.get('accent')) {
                basebox.h = Math.max(basebox.h, this.font.params.x_height * basebox.scale);
            }
            var u = this.getOverKU(basebox, overbox)[1];
            var v = this.getUnderKV(basebox, underbox)[1];
            var delta = this.getDelta();
            var _a = __read(this.getDeltaW([basebox, underbox, overbox], [0, this.isLineBelow ? 0 : -delta, this.isLineAbove ? 0 : delta]), 3), bw = _a[0], uw = _a[1], ow = _a[2];
            bbox.combine(basebox, bw, 0);
            bbox.combine(overbox, ow, u);
            bbox.combine(underbox, uw, v);
            var z = this.font.params.big_op_spacing5;
            bbox.h += z;
            bbox.d += z;
            bbox.clean();
        };
        return class_3;
    }(Base));
}
exports.CommonMunderoverMixin = CommonMunderoverMixin;
//# sourceMappingURL=munderover.js.map

/***/ }),

/***/ 7091:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonScriptbaseMixin = void 0;
var MmlNode_js_1 = __webpack_require__(8921);
function CommonScriptbaseMixin(Base) {
    var _a;
    return _a = (function (_super) {
            __extends(class_1, _super);
            function class_1() {
                var args = [];
                for (var _i = 0; _i < arguments.length; _i++) {
                    args[_i] = arguments[_i];
                }
                var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
                _this.baseScale = 1;
                _this.baseIc = 0;
                _this.baseRemoveIc = false;
                _this.baseIsChar = false;
                _this.baseHasAccentOver = null;
                _this.baseHasAccentUnder = null;
                _this.isLineAbove = false;
                _this.isLineBelow = false;
                _this.isMathAccent = false;
                var core = _this.baseCore = _this.getBaseCore();
                if (!core)
                    return _this;
                _this.setBaseAccentsFor(core);
                _this.baseScale = _this.getBaseScale();
                _this.baseIc = _this.getBaseIc();
                _this.baseIsChar = _this.isCharBase();
                _this.isMathAccent = _this.baseIsChar &&
                    (_this.scriptChild && !!_this.scriptChild.coreMO().node.getProperty('mathaccent'));
                _this.checkLineAccents();
                _this.baseRemoveIc = !_this.isLineAbove && !_this.isLineBelow &&
                    (!_this.constructor.useIC || _this.isMathAccent);
                return _this;
            }
            Object.defineProperty(class_1.prototype, "baseChild", {
                get: function () {
                    return this.childNodes[this.node.base];
                },
                enumerable: false,
                configurable: true
            });
            Object.defineProperty(class_1.prototype, "scriptChild", {
                get: function () {
                    return this.childNodes[1];
                },
                enumerable: false,
                configurable: true
            });
            class_1.prototype.getBaseCore = function () {
                var core = this.getSemanticBase() || this.childNodes[0];
                while (core &&
                    ((core.childNodes.length === 1 &&
                        (core.node.isKind('mrow') ||
                            (core.node.isKind('TeXAtom') && core.node.texClass !== MmlNode_js_1.TEXCLASS.VCENTER) ||
                            core.node.isKind('mstyle') || core.node.isKind('mpadded') ||
                            core.node.isKind('mphantom') || core.node.isKind('semantics'))) ||
                        (core.node.isKind('munderover') && core.isMathAccent))) {
                    this.setBaseAccentsFor(core);
                    core = core.childNodes[0];
                }
                if (!core) {
                    this.baseHasAccentOver = this.baseHasAccentUnder = false;
                }
                return core || this.childNodes[0];
            };
            class_1.prototype.setBaseAccentsFor = function (core) {
                if (core.node.isKind('munderover')) {
                    if (this.baseHasAccentOver === null) {
                        this.baseHasAccentOver = !!core.node.attributes.get('accent');
                    }
                    if (this.baseHasAccentUnder === null) {
                        this.baseHasAccentUnder = !!core.node.attributes.get('accentunder');
                    }
                }
            };
            class_1.prototype.getSemanticBase = function () {
                var fence = this.node.attributes.getExplicit('data-semantic-fencepointer');
                return this.getBaseFence(this.baseChild, fence);
            };
            class_1.prototype.getBaseFence = function (fence, id) {
                var e_1, _a;
                if (!fence || !fence.node.attributes || !id) {
                    return null;
                }
                if (fence.node.attributes.getExplicit('data-semantic-id') === id) {
                    return fence;
                }
                try {
                    for (var _b = __values(fence.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                        var child = _c.value;
                        var result = this.getBaseFence(child, id);
                        if (result) {
                            return result;
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
                return null;
            };
            class_1.prototype.getBaseScale = function () {
                var child = this.baseCore;
                var scale = 1;
                while (child && child !== this) {
                    var bbox = child.getOuterBBox();
                    scale *= bbox.rscale;
                    child = child.parent;
                }
                return scale;
            };
            class_1.prototype.getBaseIc = function () {
                return this.baseCore.getOuterBBox().ic * this.baseScale;
            };
            class_1.prototype.getAdjustedIc = function () {
                var bbox = this.baseCore.getOuterBBox();
                return (bbox.ic ? 1.05 * bbox.ic + .05 : 0) * this.baseScale;
            };
            class_1.prototype.isCharBase = function () {
                var base = this.baseCore;
                return (((base.node.isKind('mo') && base.size === null) ||
                    base.node.isKind('mi') || base.node.isKind('mn')) &&
                    base.bbox.rscale === 1 && Array.from(base.getText()).length === 1);
            };
            class_1.prototype.checkLineAccents = function () {
                if (!this.node.isKind('munderover'))
                    return;
                if (this.node.isKind('mover')) {
                    this.isLineAbove = this.isLineAccent(this.scriptChild);
                }
                else if (this.node.isKind('munder')) {
                    this.isLineBelow = this.isLineAccent(this.scriptChild);
                }
                else {
                    var mml = this;
                    this.isLineAbove = this.isLineAccent(mml.overChild);
                    this.isLineBelow = this.isLineAccent(mml.underChild);
                }
            };
            class_1.prototype.isLineAccent = function (script) {
                var node = script.coreMO().node;
                return (node.isToken && node.getText() === '\u2015');
            };
            class_1.prototype.getBaseWidth = function () {
                var bbox = this.baseChild.getOuterBBox();
                return bbox.w * bbox.rscale - (this.baseRemoveIc ? this.baseIc : 0) + this.font.params.extra_ic;
            };
            class_1.prototype.computeBBox = function (bbox, recompute) {
                if (recompute === void 0) { recompute = false; }
                var w = this.getBaseWidth();
                var _a = __read(this.getOffset(), 2), x = _a[0], y = _a[1];
                bbox.append(this.baseChild.getOuterBBox());
                bbox.combine(this.scriptChild.getOuterBBox(), w + x, y);
                bbox.w += this.font.params.scriptspace;
                bbox.clean();
                this.setChildPWidths(recompute);
            };
            class_1.prototype.getOffset = function () {
                return [0, 0];
            };
            class_1.prototype.baseCharZero = function (n) {
                var largeop = !!this.baseCore.node.attributes.get('largeop');
                var scale = this.baseScale;
                return (this.baseIsChar && !largeop && scale === 1 ? 0 : n);
            };
            class_1.prototype.getV = function () {
                var bbox = this.baseCore.getOuterBBox();
                var sbox = this.scriptChild.getOuterBBox();
                var tex = this.font.params;
                var subscriptshift = this.length2em(this.node.attributes.get('subscriptshift'), tex.sub1);
                return Math.max(this.baseCharZero(bbox.d * this.baseScale + tex.sub_drop * sbox.rscale), subscriptshift, sbox.h * sbox.rscale - (4 / 5) * tex.x_height);
            };
            class_1.prototype.getU = function () {
                var bbox = this.baseCore.getOuterBBox();
                var sbox = this.scriptChild.getOuterBBox();
                var tex = this.font.params;
                var attr = this.node.attributes.getList('displaystyle', 'superscriptshift');
                var prime = this.node.getProperty('texprimestyle');
                var p = prime ? tex.sup3 : (attr.displaystyle ? tex.sup1 : tex.sup2);
                var superscriptshift = this.length2em(attr.superscriptshift, p);
                return Math.max(this.baseCharZero(bbox.h * this.baseScale - tex.sup_drop * sbox.rscale), superscriptshift, sbox.d * sbox.rscale + (1 / 4) * tex.x_height);
            };
            class_1.prototype.hasMovableLimits = function () {
                var display = this.node.attributes.get('displaystyle');
                var mo = this.baseChild.coreMO().node;
                return (!display && !!mo.attributes.get('movablelimits'));
            };
            class_1.prototype.getOverKU = function (basebox, overbox) {
                var accent = this.node.attributes.get('accent');
                var tex = this.font.params;
                var d = overbox.d * overbox.rscale;
                var t = tex.rule_thickness * tex.separation_factor;
                var delta = (this.baseHasAccentOver ? t : 0);
                var T = (this.isLineAbove ? 3 * tex.rule_thickness : t);
                var k = (accent ? T : Math.max(tex.big_op_spacing1, tex.big_op_spacing3 - Math.max(0, d))) - delta;
                return [k, basebox.h * basebox.rscale + k + d];
            };
            class_1.prototype.getUnderKV = function (basebox, underbox) {
                var accent = this.node.attributes.get('accentunder');
                var tex = this.font.params;
                var h = underbox.h * underbox.rscale;
                var t = tex.rule_thickness * tex.separation_factor;
                var delta = (this.baseHasAccentUnder ? t : 0);
                var T = (this.isLineBelow ? 3 * tex.rule_thickness : t);
                var k = (accent ? T : Math.max(tex.big_op_spacing2, tex.big_op_spacing4 - h)) - delta;
                return [k, -(basebox.d * basebox.rscale + k + h)];
            };
            class_1.prototype.getDeltaW = function (boxes, delta) {
                var e_2, _a, e_3, _b;
                if (delta === void 0) { delta = [0, 0, 0]; }
                var align = this.node.attributes.get('align');
                var widths = boxes.map(function (box) { return box.w * box.rscale; });
                widths[0] -= (this.baseRemoveIc && !this.baseCore.node.attributes.get('largeop') ? this.baseIc : 0);
                var w = Math.max.apply(Math, __spreadArray([], __read(widths), false));
                var dw = [];
                var m = 0;
                try {
                    for (var _c = __values(widths.keys()), _d = _c.next(); !_d.done; _d = _c.next()) {
                        var i = _d.value;
                        dw[i] = (align === 'center' ? (w - widths[i]) / 2 :
                            align === 'right' ? w - widths[i] : 0) + delta[i];
                        if (dw[i] < m) {
                            m = -dw[i];
                        }
                    }
                }
                catch (e_2_1) { e_2 = { error: e_2_1 }; }
                finally {
                    try {
                        if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
                    }
                    finally { if (e_2) throw e_2.error; }
                }
                if (m) {
                    try {
                        for (var _e = __values(dw.keys()), _f = _e.next(); !_f.done; _f = _e.next()) {
                            var i = _f.value;
                            dw[i] += m;
                        }
                    }
                    catch (e_3_1) { e_3 = { error: e_3_1 }; }
                    finally {
                        try {
                            if (_f && !_f.done && (_b = _e.return)) _b.call(_e);
                        }
                        finally { if (e_3) throw e_3.error; }
                    }
                }
                [1, 2].map(function (i) { return dw[i] += (boxes[i] ? boxes[i].dx * boxes[0].scale : 0); });
                return dw;
            };
            class_1.prototype.getDelta = function (noskew) {
                if (noskew === void 0) { noskew = false; }
                var accent = this.node.attributes.get('accent');
                var _a = this.baseCore.getOuterBBox(), sk = _a.sk, ic = _a.ic;
                return ((accent && !noskew ? sk : 0) + this.font.skewIcFactor * ic) * this.baseScale;
            };
            class_1.prototype.stretchChildren = function () {
                var e_4, _a, e_5, _b, e_6, _c;
                var stretchy = [];
                try {
                    for (var _d = __values(this.childNodes), _e = _d.next(); !_e.done; _e = _d.next()) {
                        var child = _e.value;
                        if (child.canStretch(2)) {
                            stretchy.push(child);
                        }
                    }
                }
                catch (e_4_1) { e_4 = { error: e_4_1 }; }
                finally {
                    try {
                        if (_e && !_e.done && (_a = _d.return)) _a.call(_d);
                    }
                    finally { if (e_4) throw e_4.error; }
                }
                var count = stretchy.length;
                var nodeCount = this.childNodes.length;
                if (count && nodeCount > 1) {
                    var W = 0;
                    var all = (count > 1 && count === nodeCount);
                    try {
                        for (var _f = __values(this.childNodes), _g = _f.next(); !_g.done; _g = _f.next()) {
                            var child = _g.value;
                            var noStretch = (child.stretch.dir === 0);
                            if (all || noStretch) {
                                var _h = child.getOuterBBox(noStretch), w = _h.w, rscale = _h.rscale;
                                if (w * rscale > W)
                                    W = w * rscale;
                            }
                        }
                    }
                    catch (e_5_1) { e_5 = { error: e_5_1 }; }
                    finally {
                        try {
                            if (_g && !_g.done && (_b = _f.return)) _b.call(_f);
                        }
                        finally { if (e_5) throw e_5.error; }
                    }
                    try {
                        for (var stretchy_1 = __values(stretchy), stretchy_1_1 = stretchy_1.next(); !stretchy_1_1.done; stretchy_1_1 = stretchy_1.next()) {
                            var child = stretchy_1_1.value;
                            child.coreMO().getStretchedVariant([W / child.bbox.rscale]);
                        }
                    }
                    catch (e_6_1) { e_6 = { error: e_6_1 }; }
                    finally {
                        try {
                            if (stretchy_1_1 && !stretchy_1_1.done && (_c = stretchy_1.return)) _c.call(stretchy_1);
                        }
                        finally { if (e_6) throw e_6.error; }
                    }
                }
            };
            return class_1;
        }(Base)),
        _a.useIC = true,
        _a;
}
exports.CommonScriptbaseMixin = CommonScriptbaseMixin;
//# sourceMappingURL=scriptbase.js.map

/***/ }),

/***/ 3191:
/***/ (function(__unused_webpack_module, exports) {


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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CommonSemanticsMixin = void 0;
function CommonSemanticsMixin(Base) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.computeBBox = function (bbox, _recompute) {
            if (_recompute === void 0) { _recompute = false; }
            if (this.childNodes.length) {
                var _a = this.childNodes[0].getBBox(), w = _a.w, h = _a.h, d = _a.d;
                bbox.w = w;
                bbox.h = h;
                bbox.d = d;
            }
        };
        return class_1;
    }(Base));
}
exports.CommonSemanticsMixin = CommonSemanticsMixin;
//# sourceMappingURL=semantics.js.map

/***/ }),

/***/ 6582:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVG = exports.XLINKNS = exports.SVGNS = void 0;
var OutputJax_js_1 = __webpack_require__(716);
var WrapperFactory_js_1 = __webpack_require__(9416);
var tex_js_1 = __webpack_require__(4142);
var FontCache_js_1 = __webpack_require__(4129);
var string_js_1 = __webpack_require__(6720);
var lengths_js_1 = __webpack_require__(6914);
exports.SVGNS = 'http://www.w3.org/2000/svg';
exports.XLINKNS = 'http://www.w3.org/1999/xlink';
var SVG = (function (_super) {
    __extends(SVG, _super);
    function SVG(options) {
        if (options === void 0) { options = null; }
        var _this = _super.call(this, options, WrapperFactory_js_1.SVGWrapperFactory, tex_js_1.TeXFont) || this;
        _this.minwidth = 0;
        _this.shift = 0;
        _this.container = null;
        _this.svgStyles = null;
        _this.fontCache = new FontCache_js_1.FontCache(_this);
        return _this;
    }
    SVG.prototype.initialize = function () {
        if (this.options.fontCache === 'global') {
            this.fontCache.clearCache();
        }
    };
    SVG.prototype.clearFontCache = function () {
        this.fontCache.clearCache();
    };
    SVG.prototype.reset = function () {
        this.clearFontCache();
    };
    SVG.prototype.setScale = function (node) {
        if (this.options.scale !== 1) {
            this.adaptor.setStyle(node, 'fontSize', (0, lengths_js_1.percent)(this.options.scale));
        }
    };
    SVG.prototype.escaped = function (math, html) {
        this.setDocument(html);
        return this.html('span', {}, [this.text(math.math)]);
    };
    SVG.prototype.styleSheet = function (html) {
        if (this.svgStyles) {
            return this.svgStyles;
        }
        var sheet = this.svgStyles = _super.prototype.styleSheet.call(this, html);
        this.adaptor.setAttribute(sheet, 'id', SVG.STYLESHEETID);
        return sheet;
    };
    SVG.prototype.pageElements = function (html) {
        if (this.options.fontCache === 'global' && !this.findCache(html)) {
            return this.svg('svg', { id: SVG.FONTCACHEID, style: { display: 'none' } }, [this.fontCache.getCache()]);
        }
        return null;
    };
    SVG.prototype.findCache = function (html) {
        var adaptor = this.adaptor;
        var svgs = adaptor.tags(adaptor.body(html.document), 'svg');
        for (var i = svgs.length - 1; i >= 0; i--) {
            if (this.adaptor.getAttribute(svgs[i], 'id') === SVG.FONTCACHEID) {
                return true;
            }
        }
        return false;
    };
    SVG.prototype.processMath = function (math, parent) {
        var container = this.container;
        this.container = parent;
        var wrapper = this.factory.wrap(math);
        var _a = __read(this.createRoot(wrapper), 2), svg = _a[0], g = _a[1];
        this.typesetSVG(wrapper, svg, g);
        this.container = container;
    };
    SVG.prototype.createRoot = function (wrapper) {
        var _a = wrapper.getOuterBBox(), w = _a.w, h = _a.h, d = _a.d, pwidth = _a.pwidth;
        var px = wrapper.metrics.em / 1000;
        var W = Math.max(w, px);
        var H = Math.max(h + d, px);
        var g = this.svg('g', {
            stroke: 'currentColor', fill: 'currentColor',
            'stroke-width': 0, transform: 'scale(1,-1)'
        });
        var adaptor = this.adaptor;
        var svg = adaptor.append(this.container, this.svg('svg', {
            xmlns: exports.SVGNS,
            width: this.ex(W), height: this.ex(H),
            role: 'img', focusable: false,
            style: { 'vertical-align': this.ex(-d) },
            viewBox: [0, this.fixed(-h * 1000, 1), this.fixed(W * 1000, 1), this.fixed(H * 1000, 1)].join(' ')
        }, [g]));
        if (W === .001) {
            adaptor.setAttribute(svg, 'preserveAspectRatio', 'xMidYMid slice');
            if (w < 0) {
                adaptor.setStyle(this.container, 'margin-right', this.ex(w));
            }
        }
        if (pwidth) {
            adaptor.setStyle(svg, 'min-width', this.ex(W));
            adaptor.setAttribute(svg, 'width', pwidth);
            adaptor.removeAttribute(svg, 'viewBox');
            var scale = this.fixed(wrapper.metrics.ex / (this.font.params.x_height * 1000), 6);
            adaptor.setAttribute(g, 'transform', "scale(".concat(scale, ",-").concat(scale, ") translate(0, ").concat(this.fixed(-h * 1000, 1), ")"));
        }
        if (this.options.fontCache !== 'none') {
            adaptor.setAttribute(svg, 'xmlns:xlink', exports.XLINKNS);
        }
        return [svg, g];
    };
    SVG.prototype.typesetSVG = function (wrapper, svg, g) {
        var adaptor = this.adaptor;
        this.minwidth = this.shift = 0;
        if (this.options.fontCache === 'local') {
            this.fontCache.clearCache();
            this.fontCache.useLocalID(this.options.localID);
            adaptor.insert(this.fontCache.getCache(), g);
        }
        wrapper.toSVG(g);
        this.fontCache.clearLocalID();
        if (this.minwidth) {
            adaptor.setStyle(svg, 'minWidth', this.ex(this.minwidth));
            adaptor.setStyle(this.container, 'minWidth', this.ex(this.minwidth));
        }
        else if (this.shift) {
            var align = adaptor.getAttribute(this.container, 'justify') || 'center';
            this.setIndent(svg, align, this.shift);
        }
    };
    SVG.prototype.setIndent = function (svg, align, shift) {
        if (align === 'center' || align === 'left') {
            this.adaptor.setStyle(svg, 'margin-left', this.ex(shift));
        }
        if (align === 'center' || align === 'right') {
            this.adaptor.setStyle(svg, 'margin-right', this.ex(-shift));
        }
    };
    SVG.prototype.ex = function (m) {
        m /= this.font.params.x_height;
        return (Math.abs(m) < .001 ? '0' : m.toFixed(3).replace(/\.?0+$/, '') + 'ex');
    };
    SVG.prototype.svg = function (kind, properties, children) {
        if (properties === void 0) { properties = {}; }
        if (children === void 0) { children = []; }
        return this.html(kind, properties, children, exports.SVGNS);
    };
    SVG.prototype.unknownText = function (text, variant) {
        var metrics = this.math.metrics;
        var scale = this.font.params.x_height / metrics.ex * metrics.em * 1000;
        var svg = this.svg('text', {
            'data-variant': variant,
            transform: 'scale(1,-1)', 'font-size': this.fixed(scale, 1) + 'px'
        }, [this.text(text)]);
        var adaptor = this.adaptor;
        if (variant !== '-explicitFont') {
            var c = (0, string_js_1.unicodeChars)(text);
            if (c.length !== 1 || c[0] < 0x1D400 || c[0] > 0x1D7FF) {
                var _a = __read(this.font.getCssFont(variant), 3), family = _a[0], italic = _a[1], bold = _a[2];
                adaptor.setAttribute(svg, 'font-family', family);
                if (italic) {
                    adaptor.setAttribute(svg, 'font-style', 'italic');
                }
                if (bold) {
                    adaptor.setAttribute(svg, 'font-weight', 'bold');
                }
            }
        }
        return svg;
    };
    SVG.prototype.measureTextNode = function (text) {
        var adaptor = this.adaptor;
        text = adaptor.clone(text);
        adaptor.removeAttribute(text, 'transform');
        var ex = this.fixed(this.font.params.x_height * 1000, 1);
        var svg = this.svg('svg', {
            position: 'absolute', visibility: 'hidden',
            width: '1ex', height: '1ex',
            viewBox: [0, 0, ex, ex].join(' ')
        }, [text]);
        adaptor.append(adaptor.body(adaptor.document), svg);
        var w = adaptor.nodeSize(text, 1000, true)[0];
        adaptor.remove(svg);
        return { w: w, h: .75, d: .2 };
    };
    SVG.NAME = 'SVG';
    SVG.OPTIONS = __assign(__assign({}, OutputJax_js_1.CommonOutputJax.OPTIONS), { internalSpeechTitles: true, titleID: 0, fontCache: 'local', localID: null });
    SVG.commonStyles = {
        'mjx-container[jax="SVG"]': {
            direction: 'ltr'
        },
        'mjx-container[jax="SVG"] > svg': {
            overflow: 'visible',
            'min-height': '1px',
            'min-width': '1px'
        },
        'mjx-container[jax="SVG"] > svg a': {
            fill: 'blue', stroke: 'blue'
        }
    };
    SVG.FONTCACHEID = 'MJX-SVG-global-cache';
    SVG.STYLESHEETID = 'MJX-SVG-styles';
    return SVG;
}(OutputJax_js_1.CommonOutputJax));
exports.SVG = SVG;
//# sourceMappingURL=svg.js.map

/***/ }),

/***/ 4129:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.FontCache = void 0;
var FontCache = (function () {
    function FontCache(jax) {
        this.cache = new Map();
        this.defs = null;
        this.localID = '';
        this.nextID = 0;
        this.jax = jax;
    }
    FontCache.prototype.cachePath = function (variant, C, path) {
        var id = 'MJX-' + this.localID + (this.jax.font.getVariant(variant).cacheID || '') + '-' + C;
        if (!this.cache.has(id)) {
            this.cache.set(id, path);
            this.jax.adaptor.append(this.defs, this.jax.svg('path', { id: id, d: path }));
        }
        return id;
    };
    FontCache.prototype.clearLocalID = function () {
        this.localID = '';
    };
    FontCache.prototype.useLocalID = function (id) {
        if (id === void 0) { id = null; }
        this.localID = (id == null ? ++this.nextID : id) + (id === '' ? '' : '-');
    };
    FontCache.prototype.clearCache = function () {
        this.cache = new Map();
        this.defs = this.jax.svg('defs');
    };
    FontCache.prototype.getCache = function () {
        return this.defs;
    };
    return FontCache;
}());
exports.FontCache = FontCache;
//# sourceMappingURL=FontCache.js.map

/***/ }),

/***/ 9708:
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
var __exportStar = (this && this.__exportStar) || function(m, exports) {
    for (var p in m) if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AddPaths = exports.SVGFontData = void 0;
var FontData_js_1 = __webpack_require__(9250);
__exportStar(__webpack_require__(9250), exports);
var SVGFontData = (function (_super) {
    __extends(SVGFontData, _super);
    function SVGFontData() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGFontData.charOptions = function (font, n) {
        return _super.charOptions.call(this, font, n);
    };
    SVGFontData.OPTIONS = __assign(__assign({}, FontData_js_1.FontData.OPTIONS), { dynamicPrefix: './output/svg/fonts' });
    SVGFontData.JAX = 'SVG';
    return SVGFontData;
}(FontData_js_1.FontData));
exports.SVGFontData = SVGFontData;
function AddPaths(font, paths, content) {
    var e_1, _a, e_2, _b;
    try {
        for (var _c = __values(Object.keys(paths)), _d = _c.next(); !_d.done; _d = _c.next()) {
            var c = _d.value;
            var n = parseInt(c);
            SVGFontData.charOptions(font, n).p = paths[n];
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
        }
        finally { if (e_1) throw e_1.error; }
    }
    try {
        for (var _e = __values(Object.keys(content)), _f = _e.next(); !_f.done; _f = _e.next()) {
            var c = _f.value;
            var n = parseInt(c);
            SVGFontData.charOptions(font, n).c = content[n];
        }
    }
    catch (e_2_1) { e_2 = { error: e_2_1 }; }
    finally {
        try {
            if (_f && !_f.done && (_b = _e.return)) _b.call(_e);
        }
        finally { if (e_2) throw e_2.error; }
    }
    return font;
}
exports.AddPaths = AddPaths;
//# sourceMappingURL=FontData.js.map

/***/ }),

/***/ 9737:
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
var __exportStar = (this && this.__exportStar) || function(m, exports) {
    for (var p in m) if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Arrow = exports.DiagonalArrow = exports.DiagonalStrike = exports.Border2 = exports.Border = exports.RenderLine = exports.lineOffset = exports.lineData = exports.computeLineData = void 0;
var Notation = __importStar(__webpack_require__(5373));
__exportStar(__webpack_require__(5373), exports);
exports.computeLineData = {
    top: function (h, _d, w, t) { return [0, h - t, w, h - t]; },
    right: function (h, d, w, t) { return [w - t, -d, w - t, h]; },
    bottom: function (_h, d, w, t) { return [0, t - d, w, t - d]; },
    left: function (h, d, _w, t) { return [t, -d, t, h]; },
    vertical: function (h, d, w, _t) { return [w / 2, h, w / 2, -d]; },
    horizontal: function (h, d, w, _t) { return [0, (h - d) / 2, w, (h - d) / 2]; },
    up: function (h, d, w, t) { return [t, t - d, w - t, h - t]; },
    down: function (h, d, w, t) { return [t, h - t, w - t, t - d]; }
};
var lineData = function (node, kind, offset) {
    if (offset === void 0) { offset = ''; }
    var _a = node.getBBox(), h = _a.h, d = _a.d, w = _a.w;
    var t = node.thickness / 2;
    return (0, exports.lineOffset)(exports.computeLineData[kind](h, d, w, t), node, offset);
};
exports.lineData = lineData;
var lineOffset = function (data, node, offset) {
    if (offset) {
        var d = node.getOffset(offset);
        if (d) {
            if (offset === 'X') {
                data[0] -= d;
                data[2] -= d;
            }
            else {
                data[1] -= d;
                data[3] -= d;
            }
        }
    }
    return data;
};
exports.lineOffset = lineOffset;
var RenderLine = function (line, offset) {
    if (offset === void 0) { offset = ''; }
    return (function (node, _child) {
        var L = node.line((0, exports.lineData)(node, line, offset));
        node.adaptor.append(node.element, L);
    });
};
exports.RenderLine = RenderLine;
var Border = function (side) {
    return Notation.CommonBorder(function (node, _child) {
        node.adaptor.append(node.element, node.line((0, exports.lineData)(node, side)));
    })(side);
};
exports.Border = Border;
var Border2 = function (name, side1, side2) {
    return Notation.CommonBorder2(function (node, _child) {
        node.adaptor.append(node.element, node.line((0, exports.lineData)(node, side1)));
        node.adaptor.append(node.element, node.line((0, exports.lineData)(node, side2)));
    })(name, side1, side2);
};
exports.Border2 = Border2;
var DiagonalStrike = function (name) {
    return Notation.CommonDiagonalStrike(function (_cname) { return function (node, _child) {
        node.adaptor.append(node.element, node.line((0, exports.lineData)(node, name)));
    }; })(name);
};
exports.DiagonalStrike = DiagonalStrike;
var DiagonalArrow = function (name) {
    return Notation.CommonDiagonalArrow(function (node, arrow) {
        node.adaptor.append(node.element, arrow);
    })(name);
};
exports.DiagonalArrow = DiagonalArrow;
var Arrow = function (name) {
    return Notation.CommonArrow(function (node, arrow) {
        node.adaptor.append(node.element, arrow);
    })(name);
};
exports.Arrow = Arrow;
//# sourceMappingURL=Notation.js.map

/***/ }),

/***/ 9321:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGWrapper = void 0;
var BBox_js_1 = __webpack_require__(3717);
var Wrapper_js_1 = __webpack_require__(1541);
var svg_js_1 = __webpack_require__(6582);
var SVGWrapper = (function (_super) {
    __extends(SVGWrapper, _super);
    function SVGWrapper() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.element = null;
        _this.dx = 0;
        return _this;
    }
    SVGWrapper.prototype.toSVG = function (parent) {
        this.addChildren(this.standardSVGnode(parent));
    };
    SVGWrapper.prototype.addChildren = function (parent) {
        var e_1, _a;
        var x = 0;
        try {
            for (var _b = __values(this.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                var child = _c.value;
                child.toSVG(parent);
                var bbox = child.getOuterBBox();
                if (child.element) {
                    child.place(x + bbox.L * bbox.rscale, 0);
                }
                x += (bbox.L + bbox.w + bbox.R) * bbox.rscale;
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_1) throw e_1.error; }
        }
    };
    SVGWrapper.prototype.standardSVGnode = function (parent) {
        var svg = this.createSVGnode(parent);
        this.handleStyles();
        this.handleScale();
        this.handleBorder();
        this.handleColor();
        this.handleAttributes();
        return svg;
    };
    SVGWrapper.prototype.createSVGnode = function (parent) {
        this.element = this.svg('g', { 'data-mml-node': this.node.kind });
        var href = this.node.attributes.get('href');
        if (href) {
            parent = this.adaptor.append(parent, this.svg('a', { href: href }));
            var _a = this.getOuterBBox(), h = _a.h, d = _a.d, w = _a.w;
            this.adaptor.append(this.element, this.svg('rect', {
                'data-hitbox': true, fill: 'none', stroke: 'none', 'pointer-events': 'all',
                width: this.fixed(w), height: this.fixed(h + d), y: this.fixed(-d)
            }));
        }
        this.adaptor.append(parent, this.element);
        return this.element;
    };
    SVGWrapper.prototype.handleStyles = function () {
        var _this = this;
        if (!this.styles)
            return;
        var styles = this.styles.cssText;
        if (styles) {
            this.adaptor.setAttribute(this.element, 'style', styles);
        }
        BBox_js_1.BBox.StyleAdjust.forEach(function (_a) {
            var _b = __read(_a, 3), name = _b[0], lr = _b[2];
            if (lr !== 0)
                return;
            var x = _this.styles.get(name);
            if (x) {
                _this.dx += _this.length2em(x, 1, _this.bbox.rscale);
            }
        });
    };
    SVGWrapper.prototype.handleScale = function () {
        if (this.bbox.rscale !== 1) {
            var scale = 'scale(' + this.fixed(this.bbox.rscale / 1000, 3) + ')';
            this.adaptor.setAttribute(this.element, 'transform', scale);
        }
    };
    SVGWrapper.prototype.handleColor = function () {
        var _a;
        var adaptor = this.adaptor;
        var attributes = this.node.attributes;
        var mathcolor = attributes.getExplicit('mathcolor');
        var color = attributes.getExplicit('color');
        var mathbackground = attributes.getExplicit('mathbackground');
        var background = attributes.getExplicit('background');
        var bgcolor = (((_a = this.styles) === null || _a === void 0 ? void 0 : _a.get('background-color')) || '');
        if (mathcolor || color) {
            adaptor.setAttribute(this.element, 'fill', mathcolor || color);
            adaptor.setAttribute(this.element, 'stroke', mathcolor || color);
        }
        if (mathbackground || background || bgcolor) {
            var _b = this.getOuterBBox(), h = _b.h, d = _b.d, w = _b.w;
            var rect = this.svg('rect', {
                fill: mathbackground || background || bgcolor,
                x: this.fixed(-this.dx), y: this.fixed(-d),
                width: this.fixed(w),
                height: this.fixed(h + d),
                'data-bgcolor': true
            });
            var child = adaptor.firstChild(this.element);
            if (child) {
                adaptor.insert(rect, child);
            }
            else {
                adaptor.append(this.element, rect);
            }
        }
    };
    SVGWrapper.prototype.handleBorder = function () {
        var e_2, _a, e_3, _b;
        if (!this.styles)
            return;
        var width = Array(4).fill(0);
        var style = Array(4);
        var color = Array(4);
        try {
            for (var _c = __values([['Top', 0], ['Right', 1], ['Bottom', 2], ['Left', 3]]), _d = _c.next(); !_d.done; _d = _c.next()) {
                var _e = __read(_d.value, 2), name_1 = _e[0], i = _e[1];
                var key = 'border' + name_1;
                var w_1 = this.styles.get(key + 'Width');
                if (!w_1)
                    continue;
                width[i] = Math.max(0, this.length2em(w_1, 1, this.bbox.rscale));
                style[i] = this.styles.get(key + 'Style') || 'solid';
                color[i] = this.styles.get(key + 'Color') || 'currentColor';
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_2) throw e_2.error; }
        }
        var f = SVGWrapper.borderFuzz;
        var bbox = this.getOuterBBox();
        var _f = __read([bbox.h + f, bbox.d + f, bbox.w + f], 3), h = _f[0], d = _f[1], w = _f[2];
        var outerRT = [w, h];
        var outerLT = [-f, h];
        var outerRB = [w, -d];
        var outerLB = [-f, -d];
        var innerRT = [w - width[1], h - width[0]];
        var innerLT = [-f + width[3], h - width[0]];
        var innerRB = [w - width[1], -d + width[2]];
        var innerLB = [-f + width[3], -d + width[2]];
        var paths = [
            [outerLT, outerRT, innerRT, innerLT],
            [outerRB, outerRT, innerRT, innerRB],
            [outerLB, outerRB, innerRB, innerLB],
            [outerLB, outerLT, innerLT, innerLB]
        ];
        var adaptor = this.adaptor;
        var child = adaptor.firstChild(this.element);
        try {
            for (var _g = __values([0, 1, 2, 3]), _h = _g.next(); !_h.done; _h = _g.next()) {
                var i = _h.value;
                if (!width[i])
                    continue;
                var path = paths[i];
                if (style[i] === 'dashed' || style[i] === 'dotted') {
                    this.addBorderBroken(path, color[i], style[i], width[i], i);
                }
                else {
                    this.addBorderSolid(path, color[i], child);
                }
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (_h && !_h.done && (_b = _g.return)) _b.call(_g);
            }
            finally { if (e_3) throw e_3.error; }
        }
    };
    SVGWrapper.prototype.addBorderSolid = function (path, color, child) {
        var _this = this;
        var border = this.svg('polygon', {
            points: path.map(function (_a) {
                var _b = __read(_a, 2), x = _b[0], y = _b[1];
                return "".concat(_this.fixed(x - _this.dx), ",").concat(_this.fixed(y));
            }).join(' '),
            stroke: 'none',
            fill: color
        });
        if (child) {
            this.adaptor.insert(border, child);
        }
        else {
            this.adaptor.append(this.element, border);
        }
    };
    SVGWrapper.prototype.addBorderBroken = function (path, color, style, t, i) {
        var dot = (style === 'dotted');
        var t2 = t / 2;
        var _a = __read([[t2, -t2, -t2, -t2], [-t2, t2, -t2, -t2], [t2, t2, -t2, t2], [t2, t2, t2, -t2]][i], 4), tx1 = _a[0], ty1 = _a[1], tx2 = _a[2], ty2 = _a[3];
        var _b = __read(path, 2), A = _b[0], B = _b[1];
        var x1 = A[0] + tx1 - this.dx, y1 = A[1] + ty1;
        var x2 = B[0] + tx2 - this.dx, y2 = B[1] + ty2;
        var W = Math.abs(i % 2 ? y2 - y1 : x2 - x1);
        var n = (dot ? Math.ceil(W / (2 * t)) : Math.ceil((W - t) / (4 * t)));
        var m = W / (4 * n + 1);
        var line = this.svg('line', {
            x1: this.fixed(x1), y1: this.fixed(y1),
            x2: this.fixed(x2), y2: this.fixed(y2),
            'stroke-width': this.fixed(t), stroke: color, 'stroke-linecap': dot ? 'round' : 'square',
            'stroke-dasharray': dot ? [1, this.fixed(W / n - .002)].join(' ') : [this.fixed(m), this.fixed(3 * m)].join(' ')
        });
        var adaptor = this.adaptor;
        var child = adaptor.firstChild(this.element);
        if (child) {
            adaptor.insert(line, child);
        }
        else {
            adaptor.append(this.element, line);
        }
    };
    SVGWrapper.prototype.handleAttributes = function () {
        var e_4, _a, e_5, _b;
        var attributes = this.node.attributes;
        var defaults = attributes.getAllDefaults();
        var skip = SVGWrapper.skipAttributes;
        try {
            for (var _c = __values(attributes.getExplicitNames()), _d = _c.next(); !_d.done; _d = _c.next()) {
                var name_2 = _d.value;
                if (skip[name_2] === false || (!(name_2 in defaults) && !skip[name_2] &&
                    !this.adaptor.hasAttribute(this.element, name_2))) {
                    this.adaptor.setAttribute(this.element, name_2, attributes.getExplicit(name_2));
                }
            }
        }
        catch (e_4_1) { e_4 = { error: e_4_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_4) throw e_4.error; }
        }
        if (attributes.get('class')) {
            var names = attributes.get('class').trim().split(/ +/);
            try {
                for (var names_1 = __values(names), names_1_1 = names_1.next(); !names_1_1.done; names_1_1 = names_1.next()) {
                    var name_3 = names_1_1.value;
                    this.adaptor.addClass(this.element, name_3);
                }
            }
            catch (e_5_1) { e_5 = { error: e_5_1 }; }
            finally {
                try {
                    if (names_1_1 && !names_1_1.done && (_b = names_1.return)) _b.call(names_1);
                }
                finally { if (e_5) throw e_5.error; }
            }
        }
    };
    SVGWrapper.prototype.place = function (x, y, element) {
        if (element === void 0) { element = null; }
        x += this.dx;
        if (!(x || y))
            return;
        if (!element) {
            element = this.element;
            y = this.handleId(y);
        }
        var translate = "translate(".concat(this.fixed(x), ",").concat(this.fixed(y), ")");
        var transform = this.adaptor.getAttribute(element, 'transform') || '';
        this.adaptor.setAttribute(element, 'transform', translate + (transform ? ' ' + transform : ''));
    };
    SVGWrapper.prototype.handleId = function (y) {
        if (!this.node.attributes || !this.node.attributes.get('id')) {
            return y;
        }
        var adaptor = this.adaptor;
        var h = this.getBBox().h;
        var children = adaptor.childNodes(this.element);
        children.forEach(function (child) { return adaptor.remove(child); });
        var g = this.svg('g', { 'data-idbox': true, transform: "translate(0,".concat(this.fixed(-h), ")") }, children);
        adaptor.append(this.element, this.svg('text', { 'data-id-align': true }, [this.text('')]));
        adaptor.append(this.element, g);
        return y + h;
    };
    SVGWrapper.prototype.firstChild = function () {
        var adaptor = this.adaptor;
        var child = adaptor.firstChild(this.element);
        if (child && adaptor.kind(child) === 'text' && adaptor.getAttribute(child, 'data-id-align')) {
            child = adaptor.firstChild(adaptor.next(child));
        }
        if (child && adaptor.kind(child) === 'rect' && adaptor.getAttribute(child, 'data-hitbox')) {
            child = adaptor.next(child);
        }
        return child;
    };
    SVGWrapper.prototype.placeChar = function (n, x, y, parent, variant) {
        var e_6, _a;
        if (variant === void 0) { variant = null; }
        if (variant === null) {
            variant = this.variant;
        }
        var C = n.toString(16).toUpperCase();
        var _b = __read(this.getVariantChar(variant, n), 4), w = _b[2], data = _b[3];
        if ('p' in data) {
            var path = (data.p ? 'M' + data.p + 'Z' : '');
            this.place(x, y, this.adaptor.append(parent, this.charNode(variant, C, path)));
        }
        else if ('c' in data) {
            var g = this.adaptor.append(parent, this.svg('g', { 'data-c': C }));
            this.place(x, y, g);
            x = 0;
            try {
                for (var _c = __values(this.unicodeChars(data.c, variant)), _d = _c.next(); !_d.done; _d = _c.next()) {
                    var n_1 = _d.value;
                    x += this.placeChar(n_1, x, y, g, variant);
                }
            }
            catch (e_6_1) { e_6 = { error: e_6_1 }; }
            finally {
                try {
                    if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
                }
                finally { if (e_6) throw e_6.error; }
            }
        }
        else if (data.unknown) {
            var char = String.fromCodePoint(n);
            var text = this.adaptor.append(parent, this.jax.unknownText(char, variant));
            this.place(x, y, text);
            return this.jax.measureTextNodeWithCache(text, char, variant).w;
        }
        return w;
    };
    SVGWrapper.prototype.charNode = function (variant, C, path) {
        var cache = this.jax.options.fontCache;
        return (cache !== 'none' ? this.useNode(variant, C, path) : this.pathNode(C, path));
    };
    SVGWrapper.prototype.pathNode = function (C, path) {
        return this.svg('path', { 'data-c': C, d: path });
    };
    SVGWrapper.prototype.useNode = function (variant, C, path) {
        var use = this.svg('use', { 'data-c': C });
        var id = '#' + this.jax.fontCache.cachePath(variant, C, path);
        this.adaptor.setAttribute(use, 'href', id, svg_js_1.XLINKNS);
        return use;
    };
    SVGWrapper.prototype.drawBBox = function () {
        var _a = this.getBBox(), w = _a.w, h = _a.h, d = _a.d;
        var box = this.svg('g', { style: {
                opacity: .25
            } }, [
            this.svg('rect', {
                fill: 'red',
                height: this.fixed(h),
                width: this.fixed(w)
            }),
            this.svg('rect', {
                fill: 'green',
                height: this.fixed(d),
                width: this.fixed(w),
                y: this.fixed(-d)
            })
        ]);
        var node = this.element || this.parent.element;
        this.adaptor.append(node, box);
    };
    SVGWrapper.prototype.html = function (type, def, content) {
        if (def === void 0) { def = {}; }
        if (content === void 0) { content = []; }
        return this.jax.html(type, def, content);
    };
    SVGWrapper.prototype.svg = function (type, def, content) {
        if (def === void 0) { def = {}; }
        if (content === void 0) { content = []; }
        return this.jax.svg(type, def, content);
    };
    SVGWrapper.prototype.text = function (text) {
        return this.jax.text(text);
    };
    SVGWrapper.prototype.fixed = function (x, n) {
        if (n === void 0) { n = 1; }
        return this.jax.fixed(x * 1000, n);
    };
    SVGWrapper.kind = 'unknown';
    SVGWrapper.borderFuzz = 0.005;
    return SVGWrapper;
}(Wrapper_js_1.CommonWrapper));
exports.SVGWrapper = SVGWrapper;
//# sourceMappingURL=Wrapper.js.map

/***/ }),

/***/ 9416:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGWrapperFactory = void 0;
var WrapperFactory_js_1 = __webpack_require__(1475);
var Wrappers_js_1 = __webpack_require__(4687);
var SVGWrapperFactory = (function (_super) {
    __extends(SVGWrapperFactory, _super);
    function SVGWrapperFactory() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.jax = null;
        return _this;
    }
    SVGWrapperFactory.defaultNodes = Wrappers_js_1.SVGWrappers;
    return SVGWrapperFactory;
}(WrapperFactory_js_1.CommonWrapperFactory));
exports.SVGWrapperFactory = SVGWrapperFactory;
//# sourceMappingURL=WrapperFactory.js.map

/***/ }),

/***/ 4687:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGWrappers = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var math_js_1 = __webpack_require__(1211);
var mrow_js_1 = __webpack_require__(322);
var mi_js_1 = __webpack_require__(2983);
var mo_js_1 = __webpack_require__(6760);
var mn_js_1 = __webpack_require__(9810);
var ms_js_1 = __webpack_require__(3677);
var mtext_js_1 = __webpack_require__(1941);
var merror_js_1 = __webpack_require__(3007);
var mspace_js_1 = __webpack_require__(2458);
var mpadded_js_1 = __webpack_require__(4539);
var mphantom_js_1 = __webpack_require__(438);
var mfrac_js_1 = __webpack_require__(9295);
var msqrt_js_1 = __webpack_require__(9948);
var mroot_js_1 = __webpack_require__(8798);
var mfenced_js_1 = __webpack_require__(5258);
var msubsup_js_1 = __webpack_require__(7522);
var munderover_js_1 = __webpack_require__(4299);
var mmultiscripts_js_1 = __webpack_require__(4750);
var mtable_js_1 = __webpack_require__(451);
var mtr_js_1 = __webpack_require__(4682);
var mtd_js_1 = __webpack_require__(2673);
var maction_js_1 = __webpack_require__(4601);
var menclose_js_1 = __webpack_require__(144);
var semantics_js_1 = __webpack_require__(6965);
var mglyph_js_1 = __webpack_require__(4916);
var TeXAtom_js_1 = __webpack_require__(484);
var TextNode_js_1 = __webpack_require__(7455);
exports.SVGWrappers = (_a = {},
    _a[math_js_1.SVGmath.kind] = math_js_1.SVGmath,
    _a[mrow_js_1.SVGmrow.kind] = mrow_js_1.SVGmrow,
    _a[mrow_js_1.SVGinferredMrow.kind] = mrow_js_1.SVGinferredMrow,
    _a[mi_js_1.SVGmi.kind] = mi_js_1.SVGmi,
    _a[mo_js_1.SVGmo.kind] = mo_js_1.SVGmo,
    _a[mn_js_1.SVGmn.kind] = mn_js_1.SVGmn,
    _a[ms_js_1.SVGms.kind] = ms_js_1.SVGms,
    _a[mtext_js_1.SVGmtext.kind] = mtext_js_1.SVGmtext,
    _a[merror_js_1.SVGmerror.kind] = merror_js_1.SVGmerror,
    _a[mspace_js_1.SVGmspace.kind] = mspace_js_1.SVGmspace,
    _a[mpadded_js_1.SVGmpadded.kind] = mpadded_js_1.SVGmpadded,
    _a[mphantom_js_1.SVGmphantom.kind] = mphantom_js_1.SVGmphantom,
    _a[mfrac_js_1.SVGmfrac.kind] = mfrac_js_1.SVGmfrac,
    _a[msqrt_js_1.SVGmsqrt.kind] = msqrt_js_1.SVGmsqrt,
    _a[mroot_js_1.SVGmroot.kind] = mroot_js_1.SVGmroot,
    _a[mfenced_js_1.SVGmfenced.kind] = mfenced_js_1.SVGmfenced,
    _a[msubsup_js_1.SVGmsub.kind] = msubsup_js_1.SVGmsub,
    _a[msubsup_js_1.SVGmsup.kind] = msubsup_js_1.SVGmsup,
    _a[msubsup_js_1.SVGmsubsup.kind] = msubsup_js_1.SVGmsubsup,
    _a[munderover_js_1.SVGmunder.kind] = munderover_js_1.SVGmunder,
    _a[munderover_js_1.SVGmover.kind] = munderover_js_1.SVGmover,
    _a[munderover_js_1.SVGmunderover.kind] = munderover_js_1.SVGmunderover,
    _a[mmultiscripts_js_1.SVGmmultiscripts.kind] = mmultiscripts_js_1.SVGmmultiscripts,
    _a[mtable_js_1.SVGmtable.kind] = mtable_js_1.SVGmtable,
    _a[mtr_js_1.SVGmtr.kind] = mtr_js_1.SVGmtr,
    _a[mtr_js_1.SVGmlabeledtr.kind] = mtr_js_1.SVGmlabeledtr,
    _a[mtd_js_1.SVGmtd.kind] = mtd_js_1.SVGmtd,
    _a[maction_js_1.SVGmaction.kind] = maction_js_1.SVGmaction,
    _a[menclose_js_1.SVGmenclose.kind] = menclose_js_1.SVGmenclose,
    _a[semantics_js_1.SVGsemantics.kind] = semantics_js_1.SVGsemantics,
    _a[semantics_js_1.SVGannotation.kind] = semantics_js_1.SVGannotation,
    _a[semantics_js_1.SVGannotationXML.kind] = semantics_js_1.SVGannotationXML,
    _a[semantics_js_1.SVGxml.kind] = semantics_js_1.SVGxml,
    _a[mglyph_js_1.SVGmglyph.kind] = mglyph_js_1.SVGmglyph,
    _a[TeXAtom_js_1.SVGTeXAtom.kind] = TeXAtom_js_1.SVGTeXAtom,
    _a[TextNode_js_1.SVGTextNode.kind] = TextNode_js_1.SVGTextNode,
    _a[Wrapper_js_1.SVGWrapper.kind] = Wrapper_js_1.SVGWrapper,
    _a);
//# sourceMappingURL=Wrappers.js.map

/***/ }),

/***/ 484:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGTeXAtom = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var TeXAtom_js_1 = __webpack_require__(3438);
var TeXAtom_js_2 = __webpack_require__(4282);
var MmlNode_js_1 = __webpack_require__(8921);
var SVGTeXAtom = (function (_super) {
    __extends(SVGTeXAtom, _super);
    function SVGTeXAtom() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGTeXAtom.prototype.toSVG = function (parent) {
        _super.prototype.toSVG.call(this, parent);
        this.adaptor.setAttribute(this.element, 'data-mjx-texclass', MmlNode_js_1.TEXCLASSNAMES[this.node.texClass]);
        if (this.node.texClass === MmlNode_js_1.TEXCLASS.VCENTER) {
            var bbox = this.childNodes[0].getBBox();
            var h = bbox.h, d = bbox.d;
            var a = this.font.params.axis_height;
            var dh = ((h + d) / 2 + a) - h;
            var translate = 'translate(0 ' + this.fixed(dh) + ')';
            this.adaptor.setAttribute(this.element, 'transform', translate);
        }
    };
    SVGTeXAtom.kind = TeXAtom_js_2.TeXAtom.prototype.kind;
    return SVGTeXAtom;
}((0, TeXAtom_js_1.CommonTeXAtomMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGTeXAtom = SVGTeXAtom;
//# sourceMappingURL=TeXAtom.js.map

/***/ }),

/***/ 7455:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGTextNode = void 0;
var MmlNode_js_1 = __webpack_require__(8921);
var Wrapper_js_1 = __webpack_require__(9321);
var TextNode_js_1 = __webpack_require__(555);
var SVGTextNode = (function (_super) {
    __extends(SVGTextNode, _super);
    function SVGTextNode() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGTextNode.prototype.toSVG = function (parent) {
        var e_1, _a;
        var text = this.node.getText();
        var variant = this.parent.variant;
        if (text.length === 0)
            return;
        if (variant === '-explicitFont') {
            this.element = this.adaptor.append(parent, this.jax.unknownText(text, variant));
        }
        else {
            var chars = this.remappedText(text, variant);
            if (this.parent.childNodes.length > 1) {
                parent = this.element = this.adaptor.append(parent, this.svg('g', { 'data-mml-node': 'text' }));
            }
            var x = 0;
            try {
                for (var chars_1 = __values(chars), chars_1_1 = chars_1.next(); !chars_1_1.done; chars_1_1 = chars_1.next()) {
                    var n = chars_1_1.value;
                    x += this.placeChar(n, x, 0, parent, variant);
                }
            }
            catch (e_1_1) { e_1 = { error: e_1_1 }; }
            finally {
                try {
                    if (chars_1_1 && !chars_1_1.done && (_a = chars_1.return)) _a.call(chars_1);
                }
                finally { if (e_1) throw e_1.error; }
            }
        }
    };
    SVGTextNode.kind = MmlNode_js_1.TextNode.prototype.kind;
    SVGTextNode.styles = {
        'mjx-container[jax="SVG"] path[data-c], mjx-container[jax="SVG"] use[data-c]': {
            'stroke-width': 3
        }
    };
    return SVGTextNode;
}((0, TextNode_js_1.CommonTextNodeMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGTextNode = SVGTextNode;
//# sourceMappingURL=TextNode.js.map

/***/ }),

/***/ 4601:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmaction = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var maction_js_1 = __webpack_require__(3345);
var maction_js_2 = __webpack_require__(3345);
var maction_js_3 = __webpack_require__(3969);
var SVGmaction = (function (_super) {
    __extends(SVGmaction, _super);
    function SVGmaction() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmaction.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        var child = this.selected;
        var _a = child.getOuterBBox(), h = _a.h, d = _a.d, w = _a.w;
        this.adaptor.append(this.element, this.svg('rect', {
            width: this.fixed(w), height: this.fixed(h + d), y: this.fixed(-d),
            fill: 'none', 'pointer-events': 'all'
        }));
        child.toSVG(svg);
        var bbox = child.getOuterBBox();
        if (child.element) {
            child.place(bbox.L * bbox.rscale, 0);
        }
        this.action(this, this.data);
    };
    SVGmaction.prototype.setEventHandler = function (type, handler) {
        this.element.addEventListener(type, handler);
    };
    SVGmaction.kind = maction_js_3.MmlMaction.prototype.kind;
    SVGmaction.styles = {
        '[jax="SVG"] mjx-tool': {
            display: 'inline-block',
            position: 'relative',
            width: 0, height: 0
        },
        '[jax="SVG"] mjx-tool > mjx-tip': {
            position: 'absolute',
            top: 0, left: 0
        },
        'mjx-tool > mjx-tip': {
            display: 'inline-block',
            padding: '.2em',
            border: '1px solid #888',
            'font-size': '70%',
            'background-color': '#F8F8F8',
            color: 'black',
            'box-shadow': '2px 2px 5px #AAAAAA'
        },
        'g[data-mml-node="maction"][data-toggle]': {
            cursor: 'pointer'
        },
        'mjx-status': {
            display: 'block',
            position: 'fixed',
            left: '1em',
            bottom: '1em',
            'min-width': '25%',
            padding: '.2em .4em',
            border: '1px solid #888',
            'font-size': '90%',
            'background-color': '#F8F8F8',
            color: 'black'
        }
    };
    SVGmaction.actions = new Map([
        ['toggle', [function (node, _data) {
                    node.adaptor.setAttribute(node.element, 'data-toggle', node.node.attributes.get('selection'));
                    var math = node.factory.jax.math;
                    var document = node.factory.jax.document;
                    var mml = node.node;
                    node.setEventHandler('click', function (event) {
                        if (!math.end.node) {
                            math.start.node = math.end.node = math.typesetRoot;
                            math.start.n = math.end.n = 0;
                        }
                        mml.nextToggleSelection();
                        math.rerender(document);
                        event.stopPropagation();
                    });
                }, {}]],
        ['tooltip', [function (node, data) {
                    var tip = node.childNodes[1];
                    if (!tip)
                        return;
                    var rect = node.firstChild();
                    if (tip.node.isKind('mtext')) {
                        var text = tip.node.getText();
                        node.adaptor.insert(node.svg('title', {}, [node.text(text)]), rect);
                    }
                    else {
                        var adaptor_1 = node.adaptor;
                        var container_1 = node.jax.container;
                        var math = node.node.factory.create('math', {}, [node.childNodes[1].node]);
                        var tool_1 = node.html('mjx-tool', {}, [node.html('mjx-tip')]);
                        var hidden_1 = adaptor_1.append(rect, node.svg('foreignObject', { style: { display: 'none' } }, [tool_1]));
                        node.jax.processMath(math, adaptor_1.firstChild(tool_1));
                        node.childNodes[1].node.parent = node.node;
                        node.setEventHandler('mouseover', function (event) {
                            data.stopTimers(node, data);
                            data.hoverTimer.set(node, setTimeout(function () {
                                adaptor_1.setStyle(tool_1, 'left', '0');
                                adaptor_1.setStyle(tool_1, 'top', '0');
                                adaptor_1.append(container_1, tool_1);
                                var tbox = adaptor_1.nodeBBox(tool_1);
                                var nbox = adaptor_1.nodeBBox(node.element);
                                var dx = (nbox.right - tbox.left) / node.metrics.em + node.dx;
                                var dy = (nbox.bottom - tbox.bottom) / node.metrics.em + node.dy;
                                adaptor_1.setStyle(tool_1, 'left', node.px(dx));
                                adaptor_1.setStyle(tool_1, 'top', node.px(dy));
                            }, data.postDelay));
                            event.stopPropagation();
                        });
                        node.setEventHandler('mouseout', function (event) {
                            data.stopTimers(node, data);
                            var timer = setTimeout(function () { return adaptor_1.append(hidden_1, tool_1); }, data.clearDelay);
                            data.clearTimer.set(node, timer);
                            event.stopPropagation();
                        });
                    }
                }, maction_js_2.TooltipData]],
        ['statusline', [function (node, data) {
                    var tip = node.childNodes[1];
                    if (!tip)
                        return;
                    if (tip.node.isKind('mtext')) {
                        var adaptor_2 = node.adaptor;
                        var text_1 = tip.node.getText();
                        adaptor_2.setAttribute(node.element, 'data-statusline', text_1);
                        node.setEventHandler('mouseover', function (event) {
                            if (data.status === null) {
                                var body = adaptor_2.body(adaptor_2.document);
                                data.status = adaptor_2.append(body, node.html('mjx-status', {}, [node.text(text_1)]));
                            }
                            event.stopPropagation();
                        });
                        node.setEventHandler('mouseout', function (event) {
                            if (data.status) {
                                adaptor_2.remove(data.status);
                                data.status = null;
                            }
                            event.stopPropagation();
                        });
                    }
                }, {
                    status: null
                }]]
    ]);
    return SVGmaction;
}((0, maction_js_1.CommonMactionMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmaction = SVGmaction;
//# sourceMappingURL=maction.js.map

/***/ }),

/***/ 1211:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmath = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var math_js_1 = __webpack_require__(2057);
var math_js_2 = __webpack_require__(304);
var BBox_js_1 = __webpack_require__(3717);
var SVGmath = (function (_super) {
    __extends(SVGmath, _super);
    function SVGmath() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmath.prototype.toSVG = function (parent) {
        _super.prototype.toSVG.call(this, parent);
        var adaptor = this.adaptor;
        var display = (this.node.attributes.get('display') === 'block');
        if (display) {
            adaptor.setAttribute(this.jax.container, 'display', 'true');
            this.handleDisplay();
        }
        if (this.jax.document.options.internalSpeechTitles) {
            this.handleSpeech();
        }
    };
    SVGmath.prototype.handleDisplay = function () {
        var _a = __read(this.getAlignShift(), 2), align = _a[0], shift = _a[1];
        if (align !== 'center') {
            this.adaptor.setAttribute(this.jax.container, 'justify', align);
        }
        if (this.bbox.pwidth === BBox_js_1.BBox.fullWidth) {
            this.adaptor.setAttribute(this.jax.container, 'width', 'full');
            if (this.jax.table) {
                var _b = this.jax.table.getOuterBBox(), L = _b.L, w = _b.w, R = _b.R;
                if (align === 'right') {
                    R = Math.max(R || -shift, -shift);
                }
                else if (align === 'left') {
                    L = Math.max(L || shift, shift);
                }
                else if (align === 'center') {
                    w += 2 * Math.abs(shift);
                }
                this.jax.minwidth = Math.max(0, L + w + R);
            }
        }
        else {
            this.jax.shift = shift;
        }
    };
    SVGmath.prototype.handleSpeech = function () {
        var e_1, _a;
        var adaptor = this.adaptor;
        var attributes = this.node.attributes;
        var speech = (attributes.get('aria-label') || attributes.get('data-semantic-speech'));
        if (speech) {
            var id = this.getTitleID();
            var label = this.svg('title', { id: id }, [this.text(speech)]);
            adaptor.insert(label, adaptor.firstChild(this.element));
            adaptor.setAttribute(this.element, 'aria-labeledby', id);
            adaptor.removeAttribute(this.element, 'aria-label');
            try {
                for (var _b = __values(this.childNodes[0].childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var child = _c.value;
                    adaptor.setAttribute(child.element, 'aria-hidden', 'true');
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
    };
    SVGmath.prototype.getTitleID = function () {
        return 'mjx-svg-title-' + String(this.jax.options.titleID++);
    };
    SVGmath.prototype.setChildPWidths = function (recompute, w, _clear) {
        if (w === void 0) { w = null; }
        if (_clear === void 0) { _clear = true; }
        return _super.prototype.setChildPWidths.call(this, recompute, this.parent ? w : this.metrics.containerWidth / this.jax.pxPerEm, false);
    };
    SVGmath.kind = math_js_2.MmlMath.prototype.kind;
    SVGmath.styles = {
        'mjx-container[jax="SVG"][display="true"]': {
            display: 'block',
            'text-align': 'center',
            margin: '1em 0'
        },
        'mjx-container[jax="SVG"][display="true"][width="full"]': {
            display: 'flex'
        },
        'mjx-container[jax="SVG"][justify="left"]': {
            'text-align': 'left'
        },
        'mjx-container[jax="SVG"][justify="right"]': {
            'text-align': 'right'
        }
    };
    return SVGmath;
}((0, math_js_1.CommonMathMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmath = SVGmath;
//# sourceMappingURL=math.js.map

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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmenclose = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var menclose_js_1 = __webpack_require__(6200);
var Notation = __importStar(__webpack_require__(9737));
var menclose_js_2 = __webpack_require__(4374);
var SVGmenclose = (function (_super) {
    __extends(SVGmenclose, _super);
    function SVGmenclose() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmenclose.prototype.toSVG = function (parent) {
        var e_1, _a;
        var svg = this.standardSVGnode(parent);
        var left = this.getBBoxExtenders()[3];
        var def = {};
        if (left > 0) {
            def.transform = 'translate(' + this.fixed(left) + ', 0)';
        }
        var block = this.adaptor.append(svg, this.svg('g', def));
        if (this.renderChild) {
            this.renderChild(this, block);
        }
        else {
            this.childNodes[0].toSVG(block);
        }
        try {
            for (var _b = __values(Object.keys(this.notations)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var name_1 = _c.value;
                var notation = this.notations[name_1];
                !notation.renderChild && notation.renderer(this, svg);
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_1) throw e_1.error; }
        }
    };
    SVGmenclose.prototype.arrow = function (W, a, double, offset, dist) {
        if (offset === void 0) { offset = ''; }
        if (dist === void 0) { dist = 0; }
        var _a = this.getBBox(), w = _a.w, h = _a.h, d = _a.d;
        var dw = (W - w) / 2;
        var m = (h - d) / 2;
        var t = this.thickness;
        var t2 = t / 2;
        var _b = __read([t * this.arrowhead.x, t * this.arrowhead.y, t * this.arrowhead.dx], 3), x = _b[0], y = _b[1], dx = _b[2];
        var arrow = (double ?
            this.fill('M', w + dw, m, 'l', -(x + dx), y, 'l', dx, t2 - y, 'L', x - dw, m + t2, 'l', dx, y - t2, 'l', -(x + dx), -y, 'l', x + dx, -y, 'l', -dx, y - t2, 'L', w + dw - x, m - t2, 'l', -dx, t2 - y, 'Z') :
            this.fill('M', w + dw, m, 'l', -(x + dx), y, 'l', dx, t2 - y, 'L', -dw, m + t2, 'l', 0, -t, 'L', w + dw - x, m - t2, 'l', -dx, t2 - y, 'Z'));
        var transform = [];
        if (dist) {
            transform.push(offset === 'X' ? "translate(".concat(this.fixed(-dist), " 0)") : "translate(0 ".concat(this.fixed(dist), ")"));
        }
        if (a) {
            var A = this.jax.fixed(-a * 180 / Math.PI);
            transform.push("rotate(".concat(A, " ").concat(this.fixed(w / 2), " ").concat(this.fixed(m), ")"));
        }
        if (transform.length) {
            this.adaptor.setAttribute(arrow, 'transform', transform.join(' '));
        }
        return arrow;
    };
    SVGmenclose.prototype.line = function (pq) {
        var _a = __read(pq, 4), x1 = _a[0], y1 = _a[1], x2 = _a[2], y2 = _a[3];
        return this.svg('line', {
            x1: this.fixed(x1), y1: this.fixed(y1),
            x2: this.fixed(x2), y2: this.fixed(y2),
            'stroke-width': this.fixed(this.thickness)
        });
    };
    SVGmenclose.prototype.box = function (w, h, d, r) {
        if (r === void 0) { r = 0; }
        var t = this.thickness;
        var def = {
            x: this.fixed(t / 2), y: this.fixed(t / 2 - d),
            width: this.fixed(w - t), height: this.fixed(h + d - t),
            fill: 'none', 'stroke-width': this.fixed(t)
        };
        if (r) {
            def.rx = this.fixed(r);
        }
        return this.svg('rect', def);
    };
    SVGmenclose.prototype.ellipse = function (w, h, d) {
        var t = this.thickness;
        return this.svg('ellipse', {
            rx: this.fixed((w - t) / 2), ry: this.fixed((h + d - t) / 2),
            cx: this.fixed(w / 2), cy: this.fixed((h - d) / 2),
            'fill': 'none', 'stroke-width': this.fixed(t)
        });
    };
    SVGmenclose.prototype.path = function (join) {
        var _this = this;
        var P = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            P[_i - 1] = arguments[_i];
        }
        return this.svg('path', {
            d: P.map(function (x) { return (typeof x === 'string' ? x : _this.fixed(x)); }).join(' '),
            style: { 'stroke-width': this.fixed(this.thickness) },
            'stroke-linecap': 'round', 'stroke-linejoin': join,
            fill: 'none'
        });
    };
    SVGmenclose.prototype.fill = function () {
        var _this = this;
        var P = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            P[_i] = arguments[_i];
        }
        return this.svg('path', {
            d: P.map(function (x) { return (typeof x === 'string' ? x : _this.fixed(x)); }).join(' ')
        });
    };
    SVGmenclose.kind = menclose_js_2.MmlMenclose.prototype.kind;
    SVGmenclose.notations = new Map([
        Notation.Border('top'),
        Notation.Border('right'),
        Notation.Border('bottom'),
        Notation.Border('left'),
        Notation.Border2('actuarial', 'top', 'right'),
        Notation.Border2('madruwb', 'bottom', 'right'),
        Notation.DiagonalStrike('up'),
        Notation.DiagonalStrike('down'),
        ['horizontalstrike', {
                renderer: Notation.RenderLine('horizontal', 'Y'),
                bbox: function (node) { return [0, node.padding, 0, node.padding]; }
            }],
        ['verticalstrike', {
                renderer: Notation.RenderLine('vertical', 'X'),
                bbox: function (node) { return [node.padding, 0, node.padding, 0]; }
            }],
        ['box', {
                renderer: function (node, _child) {
                    var _a = node.getBBox(), w = _a.w, h = _a.h, d = _a.d;
                    node.adaptor.append(node.element, node.box(w, h, d));
                },
                bbox: Notation.fullBBox,
                border: Notation.fullBorder,
                remove: 'left right top bottom'
            }],
        ['roundedbox', {
                renderer: function (node, _child) {
                    var _a = node.getBBox(), w = _a.w, h = _a.h, d = _a.d;
                    var r = node.thickness + node.padding;
                    node.adaptor.append(node.element, node.box(w, h, d, r));
                },
                bbox: Notation.fullBBox
            }],
        ['circle', {
                renderer: function (node, _child) {
                    var _a = node.getBBox(), w = _a.w, h = _a.h, d = _a.d;
                    node.adaptor.append(node.element, node.ellipse(w, h, d));
                },
                bbox: Notation.fullBBox
            }],
        ['phasorangle', {
                renderer: function (node, _child) {
                    var _a = node.getBBox(), w = _a.w, h = _a.h, d = _a.d;
                    var a = node.getArgMod(1.75 * node.padding, h + d)[0];
                    var t = node.thickness / 2;
                    var HD = h + d;
                    var cos = Math.cos(a);
                    node.adaptor.append(node.element, node.path('mitre', 'M', w, t - d, 'L', t + cos * t, t - d, 'L', cos * HD + t, HD - d - t));
                },
                bbox: function (node) {
                    var p = node.padding / 2;
                    var t = node.thickness;
                    return [2 * p, p, p + t, 3 * p + t];
                },
                border: function (node) { return [0, 0, node.thickness, 0]; },
                remove: 'bottom'
            }],
        Notation.Arrow('up'),
        Notation.Arrow('down'),
        Notation.Arrow('left'),
        Notation.Arrow('right'),
        Notation.Arrow('updown'),
        Notation.Arrow('leftright'),
        Notation.DiagonalArrow('updiagonal'),
        Notation.DiagonalArrow('northeast'),
        Notation.DiagonalArrow('southeast'),
        Notation.DiagonalArrow('northwest'),
        Notation.DiagonalArrow('southwest'),
        Notation.DiagonalArrow('northeastsouthwest'),
        Notation.DiagonalArrow('northwestsoutheast'),
        ['longdiv', {
                renderer: function (node, _child) {
                    var _a = node.getBBox(), w = _a.w, h = _a.h, d = _a.d;
                    var t = node.thickness / 2;
                    var p = node.padding;
                    node.adaptor.append(node.element, node.path('round', 'M', t, t - d, 'a', p - t / 2, (h + d) / 2 - 4 * t, 0, '0,1', 0, h + d - 2 * t, 'L', w - t, h - t));
                },
                bbox: function (node) {
                    var p = node.padding;
                    var t = node.thickness;
                    return [p + t, p, p, 2 * p + t / 2];
                }
            }],
        ['radical', {
                renderer: function (node, child) {
                    node.msqrt.toSVG(child);
                    var left = node.sqrtTRBL()[3];
                    node.place(-left, 0, child);
                },
                init: function (node) {
                    node.msqrt = node.createMsqrt(node.childNodes[0]);
                },
                bbox: function (node) { return node.sqrtTRBL(); },
                renderChild: true
            }]
    ]);
    return SVGmenclose;
}((0, menclose_js_1.CommonMencloseMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmenclose = SVGmenclose;
//# sourceMappingURL=menclose.js.map

/***/ }),

/***/ 3007:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmerror = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var merror_js_1 = __webpack_require__(8078);
var SVGmerror = (function (_super) {
    __extends(SVGmerror, _super);
    function SVGmerror() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmerror.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        var _a = this.getBBox(), h = _a.h, d = _a.d, w = _a.w;
        this.adaptor.append(this.element, this.svg('rect', {
            'data-background': true,
            width: this.fixed(w), height: this.fixed(h + d), y: this.fixed(-d)
        }));
        var title = this.node.attributes.get('title');
        if (title) {
            this.adaptor.append(this.element, this.svg('title', {}, [this.adaptor.text(title)]));
        }
        this.addChildren(svg);
    };
    SVGmerror.kind = merror_js_1.MmlMerror.prototype.kind;
    SVGmerror.styles = {
        'g[data-mml-node="merror"] > g': {
            fill: 'red',
            stroke: 'red'
        },
        'g[data-mml-node="merror"] > rect[data-background]': {
            fill: 'yellow',
            stroke: 'none'
        }
    };
    return SVGmerror;
}(Wrapper_js_1.SVGWrapper));
exports.SVGmerror = SVGmerror;
//# sourceMappingURL=merror.js.map

/***/ }),

/***/ 5258:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmfenced = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mfenced_js_1 = __webpack_require__(1346);
var mfenced_js_2 = __webpack_require__(7451);
var SVGmfenced = (function (_super) {
    __extends(SVGmfenced, _super);
    function SVGmfenced() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmfenced.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        this.setChildrenParent(this.mrow);
        this.mrow.toSVG(svg);
        this.setChildrenParent(this);
    };
    SVGmfenced.prototype.setChildrenParent = function (parent) {
        var e_1, _a;
        try {
            for (var _b = __values(this.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                var child = _c.value;
                child.parent = parent;
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_1) throw e_1.error; }
        }
    };
    SVGmfenced.kind = mfenced_js_2.MmlMfenced.prototype.kind;
    return SVGmfenced;
}((0, mfenced_js_1.CommonMfencedMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmfenced = SVGmfenced;
//# sourceMappingURL=mfenced.js.map

/***/ }),

/***/ 9295:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmfrac = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mfrac_js_1 = __webpack_require__(5705);
var mfrac_js_2 = __webpack_require__(848);
var SVGmfrac = (function (_super) {
    __extends(SVGmfrac, _super);
    function SVGmfrac() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmfrac.prototype.toSVG = function (parent) {
        this.standardSVGnode(parent);
        var _a = this.node.attributes.getList('linethickness', 'bevelled'), linethickness = _a.linethickness, bevelled = _a.bevelled;
        var display = this.isDisplay();
        if (bevelled) {
            this.makeBevelled(display);
        }
        else {
            var thickness = this.length2em(String(linethickness), .06);
            if (thickness === 0) {
                this.makeAtop(display);
            }
            else {
                this.makeFraction(display, thickness);
            }
        }
    };
    SVGmfrac.prototype.makeFraction = function (display, t) {
        var svg = this.element;
        var _a = this.node.attributes.getList('numalign', 'denomalign'), numalign = _a.numalign, denomalign = _a.denomalign;
        var _b = __read(this.childNodes, 2), num = _b[0], den = _b[1];
        var nbox = num.getOuterBBox();
        var dbox = den.getOuterBBox();
        var tex = this.font.params;
        var a = tex.axis_height;
        var d = .1;
        var pad = (this.node.getProperty('withDelims') ? 0 : tex.nulldelimiterspace);
        var W = Math.max((nbox.L + nbox.w + nbox.R) * nbox.rscale, (dbox.L + dbox.w + dbox.R) * dbox.rscale);
        var nx = this.getAlignX(W, nbox, numalign) + d + pad;
        var dx = this.getAlignX(W, dbox, denomalign) + d + pad;
        var _c = this.getTUV(display, t), T = _c.T, u = _c.u, v = _c.v;
        num.toSVG(svg);
        num.place(nx, a + T + Math.max(nbox.d * nbox.rscale, u));
        den.toSVG(svg);
        den.place(dx, a - T - Math.max(dbox.h * dbox.rscale, v));
        this.adaptor.append(svg, this.svg('rect', {
            width: this.fixed(W + 2 * d), height: this.fixed(t),
            x: this.fixed(pad), y: this.fixed(a - t / 2)
        }));
    };
    SVGmfrac.prototype.makeAtop = function (display) {
        var svg = this.element;
        var _a = this.node.attributes.getList('numalign', 'denomalign'), numalign = _a.numalign, denomalign = _a.denomalign;
        var _b = __read(this.childNodes, 2), num = _b[0], den = _b[1];
        var nbox = num.getOuterBBox();
        var dbox = den.getOuterBBox();
        var tex = this.font.params;
        var pad = (this.node.getProperty('withDelims') ? 0 : tex.nulldelimiterspace);
        var W = Math.max((nbox.L + nbox.w + nbox.R) * nbox.rscale, (dbox.L + dbox.w + dbox.R) * dbox.rscale);
        var nx = this.getAlignX(W, nbox, numalign) + pad;
        var dx = this.getAlignX(W, dbox, denomalign) + pad;
        var _c = this.getUVQ(display), u = _c.u, v = _c.v;
        num.toSVG(svg);
        num.place(nx, u);
        den.toSVG(svg);
        den.place(dx, -v);
    };
    SVGmfrac.prototype.makeBevelled = function (display) {
        var svg = this.element;
        var _a = __read(this.childNodes, 2), num = _a[0], den = _a[1];
        var _b = this.getBevelData(display), u = _b.u, v = _b.v, delta = _b.delta, nbox = _b.nbox, dbox = _b.dbox;
        var w = (nbox.L + nbox.w + nbox.R) * nbox.rscale;
        num.toSVG(svg);
        this.bevel.toSVG(svg);
        den.toSVG(svg);
        num.place(nbox.L * nbox.rscale, u);
        this.bevel.place(w - delta / 2, 0);
        den.place(w + this.bevel.getOuterBBox().w + dbox.L * dbox.rscale - delta, v);
    };
    SVGmfrac.kind = mfrac_js_2.MmlMfrac.prototype.kind;
    return SVGmfrac;
}((0, mfrac_js_1.CommonMfracMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmfrac = SVGmfrac;
//# sourceMappingURL=mfrac.js.map

/***/ }),

/***/ 4916:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmglyph = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mglyph_js_1 = __webpack_require__(7969);
var mglyph_js_2 = __webpack_require__(910);
var SVGmglyph = (function (_super) {
    __extends(SVGmglyph, _super);
    function SVGmglyph() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmglyph.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        if (this.charWrapper) {
            this.charWrapper.toSVG(svg);
            return;
        }
        var _a = this.node.attributes.getList('src', 'alt'), src = _a.src, alt = _a.alt;
        var h = this.fixed(this.height);
        var w = this.fixed(this.width);
        var y = this.fixed(this.height + (this.valign || 0));
        var properties = {
            width: w, height: h,
            transform: 'translate(0 ' + y + ') matrix(1 0 0 -1 0 0)',
            preserveAspectRatio: 'none',
            'aria-label': alt,
            href: src
        };
        var img = this.svg('image', properties);
        this.adaptor.append(svg, img);
    };
    SVGmglyph.kind = mglyph_js_2.MmlMglyph.prototype.kind;
    return SVGmglyph;
}((0, mglyph_js_1.CommonMglyphMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmglyph = SVGmglyph;
//# sourceMappingURL=mglyph.js.map

/***/ }),

/***/ 2983:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmi = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mi_js_1 = __webpack_require__(1419);
var mi_js_2 = __webpack_require__(7754);
var SVGmi = (function (_super) {
    __extends(SVGmi, _super);
    function SVGmi() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmi.kind = mi_js_2.MmlMi.prototype.kind;
    return SVGmi;
}((0, mi_js_1.CommonMiMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmi = SVGmi;
//# sourceMappingURL=mi.js.map

/***/ }),

/***/ 4750:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmmultiscripts = exports.AlignX = void 0;
var msubsup_js_1 = __webpack_require__(7522);
var mmultiscripts_js_1 = __webpack_require__(9906);
var mmultiscripts_js_2 = __webpack_require__(7764);
var string_js_1 = __webpack_require__(6720);
function AlignX(align) {
    return {
        left: function (_w, _W) { return 0; },
        center: function (w, W) { return (W - w) / 2; },
        right: function (w, W) { return W - w; }
    }[align] || (function (_w, _W) { return 0; });
}
exports.AlignX = AlignX;
var SVGmmultiscripts = (function (_super) {
    __extends(SVGmmultiscripts, _super);
    function SVGmmultiscripts() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmmultiscripts.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        var data = this.scriptData;
        var scriptalign = this.node.getProperty('scriptalign') || 'right left';
        var _a = __read((0, string_js_1.split)(scriptalign + ' ' + scriptalign), 2), preAlign = _a[0], postAlign = _a[1];
        var sub = this.combinePrePost(data.sub, data.psub);
        var sup = this.combinePrePost(data.sup, data.psup);
        var _b = __read(this.getUVQ(sub, sup), 2), u = _b[0], v = _b[1];
        var x = 0;
        if (data.numPrescripts) {
            x = this.addScripts(.05, u, v, this.firstPrescript, data.numPrescripts, preAlign);
        }
        var base = this.baseChild;
        base.toSVG(svg);
        base.place(x, 0);
        x += base.getOuterBBox().w;
        if (data.numScripts) {
            this.addScripts(x, u, v, 1, data.numScripts, postAlign);
        }
    };
    SVGmmultiscripts.prototype.addScripts = function (x, u, v, i, n, align) {
        var adaptor = this.adaptor;
        var alignX = AlignX(align);
        var supRow = adaptor.append(this.element, this.svg('g'));
        var subRow = adaptor.append(this.element, this.svg('g'));
        this.place(x, u, supRow);
        this.place(x, v, subRow);
        var m = i + 2 * n;
        var dx = 0;
        while (i < m) {
            var _a = __read([this.childNodes[i++], this.childNodes[i++]], 2), sub = _a[0], sup = _a[1];
            var _b = __read([sub.getOuterBBox(), sup.getOuterBBox()], 2), subbox = _b[0], supbox = _b[1];
            var _c = __read([subbox.rscale, supbox.rscale], 2), subr = _c[0], supr = _c[1];
            var w = Math.max(subbox.w * subr, supbox.w * supr);
            sub.toSVG(subRow);
            sup.toSVG(supRow);
            sub.place(dx + alignX(subbox.w * subr, w), 0);
            sup.place(dx + alignX(supbox.w * supr, w), 0);
            dx += w;
        }
        return x + dx;
    };
    SVGmmultiscripts.kind = mmultiscripts_js_2.MmlMmultiscripts.prototype.kind;
    return SVGmmultiscripts;
}((0, mmultiscripts_js_1.CommonMmultiscriptsMixin)(msubsup_js_1.SVGmsubsup)));
exports.SVGmmultiscripts = SVGmmultiscripts;
//# sourceMappingURL=mmultiscripts.js.map

/***/ }),

/***/ 9810:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmn = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mn_js_1 = __webpack_require__(2304);
var mn_js_2 = __webpack_require__(3235);
var SVGmn = (function (_super) {
    __extends(SVGmn, _super);
    function SVGmn() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmn.kind = mn_js_2.MmlMn.prototype.kind;
    return SVGmn;
}((0, mn_js_1.CommonMnMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmn = SVGmn;
//# sourceMappingURL=mn.js.map

/***/ }),

/***/ 6760:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmo = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mo_js_1 = __webpack_require__(437);
var mo_js_2 = __webpack_require__(9946);
var VFUZZ = 0.1;
var HFUZZ = 0.1;
var SVGmo = (function (_super) {
    __extends(SVGmo, _super);
    function SVGmo() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmo.prototype.toSVG = function (parent) {
        var attributes = this.node.attributes;
        var symmetric = attributes.get('symmetric') && this.stretch.dir !== 2;
        var stretchy = this.stretch.dir !== 0;
        if (stretchy && this.size === null) {
            this.getStretchedVariant([]);
        }
        var svg = this.standardSVGnode(parent);
        if (stretchy && this.size < 0) {
            this.stretchSVG();
        }
        else {
            var u = (symmetric || attributes.get('largeop') ? this.fixed(this.getCenterOffset()) : '0');
            var v = (this.node.getProperty('mathaccent') ? this.fixed(this.getAccentOffset()) : '0');
            if (u !== '0' || v !== '0') {
                this.adaptor.setAttribute(svg, 'transform', "translate(".concat(v, " ").concat(u, ")"));
            }
            this.addChildren(svg);
        }
    };
    SVGmo.prototype.stretchSVG = function () {
        var stretch = this.stretch.stretch;
        var variants = this.getStretchVariants();
        var bbox = this.getBBox();
        if (this.stretch.dir === 1) {
            this.stretchVertical(stretch, variants, bbox);
        }
        else {
            this.stretchHorizontal(stretch, variants, bbox);
        }
    };
    SVGmo.prototype.getStretchVariants = function () {
        var e_1, _a;
        var c = this.stretch.c || this.getText().codePointAt(0);
        var variants = [];
        try {
            for (var _b = __values(this.stretch.stretch.keys()), _c = _b.next(); !_c.done; _c = _b.next()) {
                var i = _c.value;
                variants[i] = this.font.getStretchVariant(c, i);
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_1) throw e_1.error; }
        }
        return variants;
    };
    SVGmo.prototype.stretchVertical = function (stretch, variant, bbox) {
        var h = bbox.h, d = bbox.d, w = bbox.w;
        var T = this.addTop(stretch[0], variant[0], h, w);
        var B = this.addBot(stretch[2], variant[2], d, w);
        if (stretch.length === 4) {
            var _a = __read(this.addMidV(stretch[3], variant[3], w), 2), H = _a[0], D = _a[1];
            this.addExtV(stretch[1], variant[1], h, 0, T, H, w);
            this.addExtV(stretch[1], variant[1], 0, d, D, B, w);
        }
        else {
            this.addExtV(stretch[1], variant[1], h, d, T, B, w);
        }
    };
    SVGmo.prototype.stretchHorizontal = function (stretch, variant, bbox) {
        var w = bbox.w;
        var L = this.addLeft(stretch[0], variant[0]);
        var R = this.addRight(stretch[2], variant[2], w);
        if (stretch.length === 4) {
            var _a = __read(this.addMidH(stretch[3], variant[3], w), 2), x1 = _a[0], x2 = _a[1];
            var w2 = w / 2;
            this.addExtH(stretch[1], variant[1], w2, L, w2 - x1);
            this.addExtH(stretch[1], variant[1], w2, x2 - w2, R, w2);
        }
        else {
            this.addExtH(stretch[1], variant[1], w, L, R);
        }
    };
    SVGmo.prototype.getChar = function (n, variant) {
        var char = this.font.getChar(variant, n) || [0, 0, 0, null];
        return [char[0], char[1], char[2], char[3] || {}];
    };
    SVGmo.prototype.addGlyph = function (n, variant, x, y, parent) {
        if (parent === void 0) { parent = null; }
        return this.placeChar(n, x, y, parent || this.element, variant);
    };
    SVGmo.prototype.addTop = function (n, v, H, W) {
        if (!n)
            return 0;
        var _a = __read(this.getChar(n, v), 3), h = _a[0], d = _a[1], w = _a[2];
        this.addGlyph(n, v, (W - w) / 2, H - h);
        return h + d;
    };
    SVGmo.prototype.addExtV = function (n, v, H, D, T, B, W) {
        var _this = this;
        if (!n)
            return;
        T = Math.max(0, T - VFUZZ);
        B = Math.max(0, B - VFUZZ);
        var adaptor = this.adaptor;
        var _a = __read(this.getChar(n, v), 3), h = _a[0], d = _a[1], w = _a[2];
        var Y = H + D - T - B;
        var s = 1.5 * Y / (h + d);
        var y = (s * (h - d) - Y) / 2;
        if (Y <= 0)
            return;
        var svg = this.svg('svg', {
            width: this.fixed(w), height: this.fixed(Y),
            y: this.fixed(B - D), x: this.fixed((W - w) / 2),
            viewBox: [0, y, w, Y].map(function (x) { return _this.fixed(x); }).join(' ')
        });
        this.addGlyph(n, v, 0, 0, svg);
        var glyph = adaptor.lastChild(svg);
        adaptor.setAttribute(glyph, 'transform', "scale(1,".concat(this.jax.fixed(s), ")"));
        adaptor.append(this.element, svg);
    };
    SVGmo.prototype.addBot = function (n, v, D, W) {
        if (!n)
            return 0;
        var _a = __read(this.getChar(n, v), 3), h = _a[0], d = _a[1], w = _a[2];
        this.addGlyph(n, v, (W - w) / 2, d - D);
        return h + d;
    };
    SVGmo.prototype.addMidV = function (n, v, W) {
        if (!n)
            return [0, 0];
        var _a = __read(this.getChar(n, v), 3), h = _a[0], d = _a[1], w = _a[2];
        var y = (d - h) / 2 + this.font.params.axis_height;
        this.addGlyph(n, v, (W - w) / 2, y);
        return [h + y, d - y];
    };
    SVGmo.prototype.addLeft = function (n, v) {
        return (n ? this.addGlyph(n, v, 0, 0) : 0);
    };
    SVGmo.prototype.addExtH = function (n, v, W, L, R, x) {
        var _this = this;
        if (x === void 0) { x = 0; }
        if (!n)
            return;
        R = Math.max(0, R - HFUZZ);
        L = Math.max(0, L - HFUZZ);
        var adaptor = this.adaptor;
        var _a = __read(this.getChar(n, v), 3), h = _a[0], d = _a[1], w = _a[2];
        var X = W - L - R;
        var Y = h + d + 2 * VFUZZ;
        var s = 1.5 * (X / w);
        var D = -(d + VFUZZ);
        if (X <= 0)
            return;
        var svg = this.svg('svg', {
            width: this.fixed(X), height: this.fixed(Y),
            x: this.fixed(x + L), y: this.fixed(D),
            viewBox: [(s * w - X) / 2, D, X, Y].map(function (x) { return _this.fixed(x); }).join(' ')
        });
        this.addGlyph(n, v, 0, 0, svg);
        var glyph = adaptor.lastChild(svg);
        adaptor.setAttribute(glyph, 'transform', 'scale(' + this.jax.fixed(s) + ',1)');
        adaptor.append(this.element, svg);
    };
    SVGmo.prototype.addRight = function (n, v, W) {
        if (!n)
            return 0;
        var w = this.getChar(n, v)[2];
        return this.addGlyph(n, v, W - w, 0);
    };
    SVGmo.prototype.addMidH = function (n, v, W) {
        if (!n)
            return [0, 0];
        var w = this.getChar(n, v)[2];
        this.addGlyph(n, v, (W - w) / 2, 0);
        return [(W - w) / 2, (W + w) / 2];
    };
    SVGmo.kind = mo_js_2.MmlMo.prototype.kind;
    return SVGmo;
}((0, mo_js_1.CommonMoMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmo = SVGmo;
//# sourceMappingURL=mo.js.map

/***/ }),

/***/ 4539:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmpadded = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mpadded_js_1 = __webpack_require__(7481);
var mpadded_js_2 = __webpack_require__(189);
var SVGmpadded = (function (_super) {
    __extends(SVGmpadded, _super);
    function SVGmpadded() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmpadded.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        var _a = __read(this.getDimens(), 9), dw = _a[5], x = _a[6], y = _a[7], dx = _a[8];
        var align = this.node.attributes.get('data-align') || 'left';
        var X = x + dx - (dw < 0 && align !== 'left' ? align === 'center' ? dw / 2 : dw : 0);
        if (X || y) {
            svg = this.adaptor.append(svg, this.svg('g'));
            this.place(X, y, svg);
        }
        this.addChildren(svg);
    };
    SVGmpadded.kind = mpadded_js_2.MmlMpadded.prototype.kind;
    return SVGmpadded;
}((0, mpadded_js_1.CommonMpaddedMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmpadded = SVGmpadded;
//# sourceMappingURL=mpadded.js.map

/***/ }),

/***/ 438:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmphantom = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mphantom_js_1 = __webpack_require__(7988);
var SVGmphantom = (function (_super) {
    __extends(SVGmphantom, _super);
    function SVGmphantom() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmphantom.prototype.toSVG = function (parent) {
        this.standardSVGnode(parent);
    };
    SVGmphantom.kind = mphantom_js_1.MmlMphantom.prototype.kind;
    return SVGmphantom;
}(Wrapper_js_1.SVGWrapper));
exports.SVGmphantom = SVGmphantom;
//# sourceMappingURL=mphantom.js.map

/***/ }),

/***/ 8798:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmroot = void 0;
var msqrt_js_1 = __webpack_require__(9948);
var mroot_js_1 = __webpack_require__(5997);
var mroot_js_2 = __webpack_require__(4664);
var SVGmroot = (function (_super) {
    __extends(SVGmroot, _super);
    function SVGmroot() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmroot.prototype.addRoot = function (ROOT, root, sbox, H) {
        root.toSVG(ROOT);
        var _a = __read(this.getRootDimens(sbox, H), 3), x = _a[0], h = _a[1], dx = _a[2];
        var bbox = root.getOuterBBox();
        root.place(dx * bbox.rscale, h);
        this.dx = x;
    };
    SVGmroot.kind = mroot_js_2.MmlMroot.prototype.kind;
    return SVGmroot;
}((0, mroot_js_1.CommonMrootMixin)(msqrt_js_1.SVGmsqrt)));
exports.SVGmroot = SVGmroot;
//# sourceMappingURL=mroot.js.map

/***/ }),

/***/ 322:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGinferredMrow = exports.SVGmrow = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mrow_js_1 = __webpack_require__(9323);
var mrow_js_2 = __webpack_require__(9323);
var mrow_js_3 = __webpack_require__(1691);
var SVGmrow = (function (_super) {
    __extends(SVGmrow, _super);
    function SVGmrow() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmrow.prototype.toSVG = function (parent) {
        var svg = (this.node.isInferred ? (this.element = parent) : this.standardSVGnode(parent));
        this.addChildren(svg);
    };
    SVGmrow.kind = mrow_js_3.MmlMrow.prototype.kind;
    return SVGmrow;
}((0, mrow_js_1.CommonMrowMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmrow = SVGmrow;
var SVGinferredMrow = (function (_super) {
    __extends(SVGinferredMrow, _super);
    function SVGinferredMrow() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGinferredMrow.kind = mrow_js_3.MmlInferredMrow.prototype.kind;
    return SVGinferredMrow;
}((0, mrow_js_2.CommonInferredMrowMixin)(SVGmrow)));
exports.SVGinferredMrow = SVGinferredMrow;
//# sourceMappingURL=mrow.js.map

/***/ }),

/***/ 3677:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGms = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var ms_js_1 = __webpack_require__(6920);
var ms_js_2 = __webpack_require__(4042);
var SVGms = (function (_super) {
    __extends(SVGms, _super);
    function SVGms() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGms.kind = ms_js_2.MmlMs.prototype.kind;
    return SVGms;
}((0, ms_js_1.CommonMsMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGms = SVGms;
//# sourceMappingURL=ms.js.map

/***/ }),

/***/ 2458:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmspace = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mspace_js_1 = __webpack_require__(37);
var mspace_js_2 = __webpack_require__(1465);
var SVGmspace = (function (_super) {
    __extends(SVGmspace, _super);
    function SVGmspace() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmspace.kind = mspace_js_2.MmlMspace.prototype.kind;
    return SVGmspace;
}((0, mspace_js_1.CommonMspaceMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmspace = SVGmspace;
//# sourceMappingURL=mspace.js.map

/***/ }),

/***/ 9948:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmsqrt = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var msqrt_js_1 = __webpack_require__(222);
var msqrt_js_2 = __webpack_require__(4655);
var SVGmsqrt = (function (_super) {
    __extends(SVGmsqrt, _super);
    function SVGmsqrt() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.dx = 0;
        return _this;
    }
    SVGmsqrt.prototype.toSVG = function (parent) {
        var surd = this.childNodes[this.surd];
        var base = this.childNodes[this.base];
        var root = (this.root ? this.childNodes[this.root] : null);
        var sbox = surd.getBBox();
        var bbox = base.getOuterBBox();
        var q = this.getPQ(sbox)[1];
        var t = this.font.params.rule_thickness * this.bbox.scale;
        var H = bbox.h + q + t;
        var SVG = this.standardSVGnode(parent);
        var BASE = this.adaptor.append(SVG, this.svg('g'));
        this.addRoot(SVG, root, sbox, H);
        surd.toSVG(SVG);
        surd.place(this.dx, H - sbox.h);
        base.toSVG(BASE);
        base.place(this.dx + sbox.w, 0);
        this.adaptor.append(SVG, this.svg('rect', {
            width: this.fixed(bbox.w), height: this.fixed(t),
            x: this.fixed(this.dx + sbox.w), y: this.fixed(H - t)
        }));
    };
    SVGmsqrt.prototype.addRoot = function (_ROOT, _root, _sbox, _H) {
    };
    SVGmsqrt.kind = msqrt_js_2.MmlMsqrt.prototype.kind;
    return SVGmsqrt;
}((0, msqrt_js_1.CommonMsqrtMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmsqrt = SVGmsqrt;
//# sourceMappingURL=msqrt.js.map

/***/ }),

/***/ 7522:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmsubsup = exports.SVGmsup = exports.SVGmsub = void 0;
var scriptbase_js_1 = __webpack_require__(1269);
var msubsup_js_1 = __webpack_require__(3069);
var msubsup_js_2 = __webpack_require__(3069);
var msubsup_js_3 = __webpack_require__(3069);
var msubsup_js_4 = __webpack_require__(5857);
var SVGmsub = (function (_super) {
    __extends(SVGmsub, _super);
    function SVGmsub() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmsub.kind = msubsup_js_4.MmlMsub.prototype.kind;
    return SVGmsub;
}((0, msubsup_js_1.CommonMsubMixin)(scriptbase_js_1.SVGscriptbase)));
exports.SVGmsub = SVGmsub;
var SVGmsup = (function (_super) {
    __extends(SVGmsup, _super);
    function SVGmsup() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmsup.kind = msubsup_js_4.MmlMsup.prototype.kind;
    return SVGmsup;
}((0, msubsup_js_2.CommonMsupMixin)(scriptbase_js_1.SVGscriptbase)));
exports.SVGmsup = SVGmsup;
var SVGmsubsup = (function (_super) {
    __extends(SVGmsubsup, _super);
    function SVGmsubsup() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmsubsup.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        var _a = __read([this.baseChild, this.supChild, this.subChild], 3), base = _a[0], sup = _a[1], sub = _a[2];
        var w = this.getBaseWidth();
        var x = this.getAdjustedIc();
        var _b = __read(this.getUVQ(), 2), u = _b[0], v = _b[1];
        base.toSVG(svg);
        sup.toSVG(svg);
        sub.toSVG(svg);
        sub.place(w, v);
        sup.place(w + x, u);
    };
    SVGmsubsup.kind = msubsup_js_4.MmlMsubsup.prototype.kind;
    return SVGmsubsup;
}((0, msubsup_js_3.CommonMsubsupMixin)(scriptbase_js_1.SVGscriptbase)));
exports.SVGmsubsup = SVGmsubsup;
//# sourceMappingURL=msubsup.js.map

/***/ }),

/***/ 451:
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
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmtable = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mtable_js_1 = __webpack_require__(8589);
var mtable_js_2 = __webpack_require__(4859);
var CLASSPREFIX = 'mjx-';
var SVGmtable = (function (_super) {
    __extends(SVGmtable, _super);
    function SVGmtable(factory, node, parent) {
        if (parent === void 0) { parent = null; }
        var _this = _super.call(this, factory, node, parent) || this;
        var def = { 'data-labels': true };
        if (_this.isTop) {
            def.transform = 'matrix(1 0 0 -1 0 0)';
        }
        _this.labels = _this.svg('g', def);
        return _this;
    }
    SVGmtable.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        this.placeRows(svg);
        this.handleColumnLines(svg);
        this.handleRowLines(svg);
        this.handleFrame(svg);
        var dx = this.handlePWidth(svg);
        this.handleLabels(svg, parent, dx);
    };
    SVGmtable.prototype.placeRows = function (svg) {
        var _a, _b, _c;
        var equal = this.node.attributes.get('equalrows');
        var _d = this.getTableData(), H = _d.H, D = _d.D;
        var HD = this.getEqualRowHeight();
        var rSpace = this.getRowHalfSpacing();
        var rLines = __spreadArray(__spreadArray([this.fLine], __read(this.rLines), false), [this.fLine], false);
        var y = this.getBBox().h - rLines[0];
        for (var i = 0; i < this.numRows; i++) {
            var row = this.childNodes[i];
            _a = __read(this.getRowHD(equal, HD, H[i], D[i]), 2), row.H = _a[0], row.D = _a[1];
            _b = __read([rSpace[i], rSpace[i + 1]], 2), row.tSpace = _b[0], row.bSpace = _b[1];
            _c = __read([rLines[i], rLines[i + 1]], 2), row.tLine = _c[0], row.bLine = _c[1];
            row.toSVG(svg);
            row.place(0, y - rSpace[i] - row.H);
            y -= rSpace[i] + row.H + row.D + rSpace[i + 1] + rLines[i + 1];
        }
    };
    SVGmtable.prototype.getRowHD = function (equal, HD, H, D) {
        return (equal ? [(HD + H - D) / 2, (HD - H + D) / 2] : [H, D]);
    };
    SVGmtable.prototype.handleColor = function () {
        _super.prototype.handleColor.call(this);
        var rect = this.firstChild();
        if (rect) {
            this.adaptor.setAttribute(rect, 'width', this.fixed(this.getWidth()));
        }
    };
    SVGmtable.prototype.handleColumnLines = function (svg) {
        if (this.node.attributes.get('columnlines') === 'none')
            return;
        var lines = this.getColumnAttributes('columnlines');
        if (!lines)
            return;
        var cSpace = this.getColumnHalfSpacing();
        var cLines = this.cLines;
        var cWidth = this.getComputedWidths();
        var x = this.fLine;
        for (var i = 0; i < lines.length; i++) {
            x += cSpace[i] + cWidth[i] + cSpace[i + 1];
            if (lines[i] !== 'none') {
                this.adaptor.append(svg, this.makeVLine(x, lines[i], cLines[i]));
            }
            x += cLines[i];
        }
    };
    SVGmtable.prototype.handleRowLines = function (svg) {
        if (this.node.attributes.get('rowlines') === 'none')
            return;
        var lines = this.getRowAttributes('rowlines');
        if (!lines)
            return;
        var equal = this.node.attributes.get('equalrows');
        var _a = this.getTableData(), H = _a.H, D = _a.D;
        var HD = this.getEqualRowHeight();
        var rSpace = this.getRowHalfSpacing();
        var rLines = this.rLines;
        var y = this.getBBox().h - this.fLine;
        for (var i = 0; i < lines.length; i++) {
            var _b = __read(this.getRowHD(equal, HD, H[i], D[i]), 2), rH = _b[0], rD = _b[1];
            y -= rSpace[i] + rH + rD + rSpace[i + 1];
            if (lines[i] !== 'none') {
                this.adaptor.append(svg, this.makeHLine(y, lines[i], rLines[i]));
            }
            y -= rLines[i];
        }
    };
    SVGmtable.prototype.handleFrame = function (svg) {
        if (this.frame && this.fLine) {
            var _a = this.getBBox(), h = _a.h, d = _a.d, w = _a.w;
            var style = this.node.attributes.get('frame');
            this.adaptor.append(svg, this.makeFrame(w, h, d, style));
        }
    };
    SVGmtable.prototype.handlePWidth = function (svg) {
        if (!this.pWidth) {
            return 0;
        }
        var _a = this.getBBox(), w = _a.w, L = _a.L, R = _a.R;
        var W = L + this.pWidth + R;
        var align = this.getAlignShift()[0];
        var CW = Math.max(this.isTop ? W : 0, this.container.getWrapWidth(this.containerI)) - L - R;
        var dw = w - (this.pWidth > CW ? CW : this.pWidth);
        var dx = (align === 'left' ? 0 : align === 'right' ? dw : dw / 2);
        if (dx) {
            var table = this.svg('g', {}, this.adaptor.childNodes(svg));
            this.place(dx, 0, table);
            this.adaptor.append(svg, table);
        }
        return dx;
    };
    SVGmtable.prototype.lineClass = function (style) {
        return CLASSPREFIX + style;
    };
    SVGmtable.prototype.makeFrame = function (w, h, d, style) {
        var t = this.fLine;
        return this.svg('rect', this.setLineThickness(t, style, {
            'data-frame': true, 'class': this.lineClass(style),
            width: this.fixed(w - t), height: this.fixed(h + d - t),
            x: this.fixed(t / 2), y: this.fixed(t / 2 - d)
        }));
    };
    SVGmtable.prototype.makeVLine = function (x, style, t) {
        var _a = this.getBBox(), h = _a.h, d = _a.d;
        var dt = (style === 'dotted' ? t / 2 : 0);
        var X = this.fixed(x + t / 2);
        return this.svg('line', this.setLineThickness(t, style, {
            'data-line': 'v', 'class': this.lineClass(style),
            x1: X, y1: this.fixed(dt - d), x2: X, y2: this.fixed(h - dt)
        }));
    };
    SVGmtable.prototype.makeHLine = function (y, style, t) {
        var w = this.getBBox().w;
        var dt = (style === 'dotted' ? t / 2 : 0);
        var Y = this.fixed(y - t / 2);
        return this.svg('line', this.setLineThickness(t, style, {
            'data-line': 'h', 'class': this.lineClass(style),
            x1: this.fixed(dt), y1: Y, x2: this.fixed(w - dt), y2: Y
        }));
    };
    SVGmtable.prototype.setLineThickness = function (t, style, properties) {
        if (t !== .07) {
            properties['stroke-thickness'] = this.fixed(t);
            if (style !== 'solid') {
                properties['stroke-dasharray'] = (style === 'dotted' ? '0,' : '') + this.fixed(2 * t);
            }
        }
        return properties;
    };
    SVGmtable.prototype.handleLabels = function (svg, _parent, dx) {
        if (!this.hasLabels)
            return;
        var labels = this.labels;
        var attributes = this.node.attributes;
        var side = attributes.get('side');
        this.spaceLabels();
        this.isTop ? this.topTable(svg, labels, side) : this.subTable(svg, labels, side, dx);
    };
    SVGmtable.prototype.spaceLabels = function () {
        var adaptor = this.adaptor;
        var h = this.getBBox().h;
        var L = this.getTableData().L;
        var space = this.getRowHalfSpacing();
        var y = h - this.fLine;
        var current = adaptor.firstChild(this.labels);
        for (var i = 0; i < this.numRows; i++) {
            var row = this.childNodes[i];
            if (row.node.isKind('mlabeledtr')) {
                var cell = row.childNodes[0];
                y -= space[i] + row.H;
                row.placeCell(cell, { x: 0, y: y, w: L, lSpace: 0, rSpace: 0, lLine: 0, rLine: 0 });
                y -= row.D + space[i + 1] + this.rLines[i];
                current = adaptor.next(current);
            }
            else {
                y -= space[i] + row.H + row.D + space[i + 1] + this.rLines[i];
            }
        }
    };
    SVGmtable.prototype.topTable = function (svg, labels, side) {
        var adaptor = this.adaptor;
        var _a = this.getBBox(), h = _a.h, d = _a.d, w = _a.w, L = _a.L, R = _a.R;
        var W = L + (this.pWidth || w) + R;
        var LW = this.getTableData().L;
        var _b = __read(this.getPadAlignShift(side), 3), align = _b[1], shift = _b[2];
        var dx = shift + (align === 'right' ? -W : align === 'center' ? -W / 2 : 0) + L;
        var matrix = 'matrix(1 0 0 -1 0 0)';
        var scale = "scale(".concat(this.jax.fixed((this.font.params.x_height * 1000) / this.metrics.ex, 2), ")");
        var transform = "translate(0 ".concat(this.fixed(h), ") ").concat(matrix, " ").concat(scale);
        var table = this.svg('svg', {
            'data-table': true,
            preserveAspectRatio: (align === 'left' ? 'xMinYMid' : align === 'right' ? 'xMaxYMid' : 'xMidYMid'),
            viewBox: [this.fixed(-dx), this.fixed(-h), 1, this.fixed(h + d)].join(' ')
        }, [
            this.svg('g', { transform: matrix }, adaptor.childNodes(svg))
        ]);
        labels = this.svg('svg', {
            'data-labels': true,
            preserveAspectRatio: (side === 'left' ? 'xMinYMid' : 'xMaxYMid'),
            viewBox: [side === 'left' ? 0 : this.fixed(LW), this.fixed(-h), 1, this.fixed(h + d)].join(' ')
        }, [labels]);
        adaptor.append(svg, this.svg('g', { transform: transform }, [table, labels]));
        this.place(-L, 0, svg);
    };
    SVGmtable.prototype.subTable = function (svg, labels, side, dx) {
        var adaptor = this.adaptor;
        var _a = this.getBBox(), w = _a.w, L = _a.L, R = _a.R;
        var W = L + (this.pWidth || w) + R;
        var labelW = this.getTableData().L;
        var align = this.getAlignShift()[0];
        var CW = Math.max(W, this.container.getWrapWidth(this.containerI));
        this.place(side === 'left' ?
            (align === 'left' ? 0 : align === 'right' ? W - CW + dx : (W - CW) / 2 + dx) - L :
            (align === 'left' ? CW : align === 'right' ? W + dx : (CW + W) / 2 + dx) - L - labelW, 0, labels);
        adaptor.append(svg, labels);
    };
    SVGmtable.kind = mtable_js_2.MmlMtable.prototype.kind;
    SVGmtable.styles = {
        'g[data-mml-node="mtable"] > line[data-line], svg[data-table] > g > line[data-line]': {
            'stroke-width': '70px',
            fill: 'none'
        },
        'g[data-mml-node="mtable"] > rect[data-frame], svg[data-table] > g > rect[data-frame]': {
            'stroke-width': '70px',
            fill: 'none'
        },
        'g[data-mml-node="mtable"] > .mjx-dashed, svg[data-table] > g > .mjx-dashed': {
            'stroke-dasharray': '140'
        },
        'g[data-mml-node="mtable"] > .mjx-dotted, svg[data-table] > g > .mjx-dotted': {
            'stroke-linecap': 'round',
            'stroke-dasharray': '0,140'
        },
        'g[data-mml-node="mtable"] > g > svg': {
            overflow: 'visible'
        }
    };
    return SVGmtable;
}((0, mtable_js_1.CommonMtableMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmtable = SVGmtable;
//# sourceMappingURL=mtable.js.map

/***/ }),

/***/ 2673:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmtd = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mtd_js_1 = __webpack_require__(7805);
var mtd_js_2 = __webpack_require__(2321);
var SVGmtd = (function (_super) {
    __extends(SVGmtd, _super);
    function SVGmtd() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmtd.prototype.placeCell = function (x, y, W, H, D) {
        var bbox = this.getBBox();
        var h = Math.max(bbox.h, .75);
        var d = Math.max(bbox.d, .25);
        var calign = this.node.attributes.get('columnalign');
        var ralign = this.node.attributes.get('rowalign');
        var alignX = this.getAlignX(W, bbox, calign);
        var alignY = this.getAlignY(H, D, h, d, ralign);
        this.place(x + alignX, y + alignY);
        return [alignX, alignY];
    };
    SVGmtd.prototype.placeColor = function (x, y, W, H) {
        var adaptor = this.adaptor;
        var child = this.firstChild();
        if (child && adaptor.kind(child) === 'rect' && adaptor.getAttribute(child, 'data-bgcolor')) {
            adaptor.setAttribute(child, 'x', this.fixed(x));
            adaptor.setAttribute(child, 'y', this.fixed(y));
            adaptor.setAttribute(child, 'width', this.fixed(W));
            adaptor.setAttribute(child, 'height', this.fixed(H));
        }
    };
    SVGmtd.kind = mtd_js_2.MmlMtd.prototype.kind;
    return SVGmtd;
}((0, mtd_js_1.CommonMtdMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmtd = SVGmtd;
//# sourceMappingURL=mtd.js.map

/***/ }),

/***/ 1941:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmtext = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mtext_js_1 = __webpack_require__(8325);
var mtext_js_2 = __webpack_require__(6277);
var SVGmtext = (function (_super) {
    __extends(SVGmtext, _super);
    function SVGmtext() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmtext.kind = mtext_js_2.MmlMtext.prototype.kind;
    return SVGmtext;
}((0, mtext_js_1.CommonMtextMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmtext = SVGmtext;
//# sourceMappingURL=mtext.js.map

/***/ }),

/***/ 4682:
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
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmlabeledtr = exports.SVGmtr = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var mtr_js_1 = __webpack_require__(4818);
var mtr_js_2 = __webpack_require__(4818);
var mtr_js_3 = __webpack_require__(4393);
var SVGmtr = (function (_super) {
    __extends(SVGmtr, _super);
    function SVGmtr() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmtr.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        this.placeCells(svg);
        this.placeColor();
    };
    SVGmtr.prototype.placeCells = function (svg) {
        var cSpace = this.parent.getColumnHalfSpacing();
        var cLines = __spreadArray(__spreadArray([this.parent.fLine], __read(this.parent.cLines), false), [this.parent.fLine], false);
        var cWidth = this.parent.getComputedWidths();
        var scale = 1 / this.getBBox().rscale;
        var x = cLines[0];
        for (var i = 0; i < this.numCells; i++) {
            var child = this.getChild(i);
            child.toSVG(svg);
            x += this.placeCell(child, {
                x: x, y: 0, lSpace: cSpace[i] * scale, rSpace: cSpace[i + 1] * scale, w: cWidth[i] * scale,
                lLine: cLines[i] * scale, rLine: cLines[i + 1] * scale
            });
        }
    };
    SVGmtr.prototype.placeCell = function (cell, sizes) {
        var x = sizes.x, y = sizes.y, lSpace = sizes.lSpace, w = sizes.w, rSpace = sizes.rSpace, lLine = sizes.lLine, rLine = sizes.rLine;
        var scale = 1 / this.getBBox().rscale;
        var _a = __read([this.H * scale, this.D * scale], 2), h = _a[0], d = _a[1];
        var _b = __read([this.tSpace * scale, this.bSpace * scale], 2), t = _b[0], b = _b[1];
        var _c = __read(cell.placeCell(x + lSpace, y, w, h, d), 2), dx = _c[0], dy = _c[1];
        var W = lSpace + w + rSpace;
        cell.placeColor(-(dx + lSpace + lLine / 2), -(d + b + dy), W + (lLine + rLine) / 2, h + d + t + b);
        return W + rLine;
    };
    SVGmtr.prototype.placeColor = function () {
        var scale = 1 / this.getBBox().rscale;
        var adaptor = this.adaptor;
        var child = this.firstChild();
        if (child && adaptor.kind(child) === 'rect' && adaptor.getAttribute(child, 'data-bgcolor')) {
            var _a = __read([(this.tLine / 2) * scale, (this.bLine / 2) * scale], 2), TL = _a[0], BL = _a[1];
            var _b = __read([this.tSpace * scale, this.bSpace * scale], 2), TS = _b[0], BS = _b[1];
            var _c = __read([this.H * scale, this.D * scale], 2), H = _c[0], D = _c[1];
            adaptor.setAttribute(child, 'y', this.fixed(-(D + BS + BL)));
            adaptor.setAttribute(child, 'width', this.fixed(this.parent.getWidth() * scale));
            adaptor.setAttribute(child, 'height', this.fixed(TL + TS + H + D + BS + BL));
        }
    };
    SVGmtr.kind = mtr_js_3.MmlMtr.prototype.kind;
    return SVGmtr;
}((0, mtr_js_1.CommonMtrMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGmtr = SVGmtr;
var SVGmlabeledtr = (function (_super) {
    __extends(SVGmlabeledtr, _super);
    function SVGmlabeledtr() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmlabeledtr.prototype.toSVG = function (parent) {
        _super.prototype.toSVG.call(this, parent);
        var child = this.childNodes[0];
        if (child) {
            child.toSVG(this.parent.labels);
        }
    };
    SVGmlabeledtr.kind = mtr_js_3.MmlMlabeledtr.prototype.kind;
    return SVGmlabeledtr;
}((0, mtr_js_2.CommonMlabeledtrMixin)(SVGmtr)));
exports.SVGmlabeledtr = SVGmlabeledtr;
//# sourceMappingURL=mtr.js.map

/***/ }),

/***/ 4299:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGmunderover = exports.SVGmover = exports.SVGmunder = void 0;
var msubsup_js_1 = __webpack_require__(7522);
var munderover_js_1 = __webpack_require__(9690);
var munderover_js_2 = __webpack_require__(9690);
var munderover_js_3 = __webpack_require__(9690);
var munderover_js_4 = __webpack_require__(3102);
var SVGmunder = (function (_super) {
    __extends(SVGmunder, _super);
    function SVGmunder() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmunder.prototype.toSVG = function (parent) {
        if (this.hasMovableLimits()) {
            _super.prototype.toSVG.call(this, parent);
            return;
        }
        var svg = this.standardSVGnode(parent);
        var _a = __read([this.baseChild, this.scriptChild], 2), base = _a[0], script = _a[1];
        var _b = __read([base.getOuterBBox(), script.getOuterBBox()], 2), bbox = _b[0], sbox = _b[1];
        base.toSVG(svg);
        script.toSVG(svg);
        var delta = (this.isLineBelow ? 0 : this.getDelta(true));
        var v = this.getUnderKV(bbox, sbox)[1];
        var _c = __read(this.getDeltaW([bbox, sbox], [0, -delta]), 2), bx = _c[0], sx = _c[1];
        base.place(bx, 0);
        script.place(sx, v);
    };
    SVGmunder.kind = munderover_js_4.MmlMunder.prototype.kind;
    return SVGmunder;
}((0, munderover_js_1.CommonMunderMixin)(msubsup_js_1.SVGmsub)));
exports.SVGmunder = SVGmunder;
var SVGmover = (function (_super) {
    __extends(SVGmover, _super);
    function SVGmover() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmover.prototype.toSVG = function (parent) {
        if (this.hasMovableLimits()) {
            _super.prototype.toSVG.call(this, parent);
            return;
        }
        var svg = this.standardSVGnode(parent);
        var _a = __read([this.baseChild, this.scriptChild], 2), base = _a[0], script = _a[1];
        var _b = __read([base.getOuterBBox(), script.getOuterBBox()], 2), bbox = _b[0], sbox = _b[1];
        base.toSVG(svg);
        script.toSVG(svg);
        var delta = (this.isLineAbove ? 0 : this.getDelta());
        var u = this.getOverKU(bbox, sbox)[1];
        var _c = __read(this.getDeltaW([bbox, sbox], [0, delta]), 2), bx = _c[0], sx = _c[1];
        base.place(bx, 0);
        script.place(sx, u);
    };
    SVGmover.kind = munderover_js_4.MmlMover.prototype.kind;
    return SVGmover;
}((0, munderover_js_2.CommonMoverMixin)(msubsup_js_1.SVGmsup)));
exports.SVGmover = SVGmover;
var SVGmunderover = (function (_super) {
    __extends(SVGmunderover, _super);
    function SVGmunderover() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGmunderover.prototype.toSVG = function (parent) {
        if (this.hasMovableLimits()) {
            _super.prototype.toSVG.call(this, parent);
            return;
        }
        var svg = this.standardSVGnode(parent);
        var _a = __read([this.baseChild, this.overChild, this.underChild], 3), base = _a[0], over = _a[1], under = _a[2];
        var _b = __read([base.getOuterBBox(), over.getOuterBBox(), under.getOuterBBox()], 3), bbox = _b[0], obox = _b[1], ubox = _b[2];
        base.toSVG(svg);
        under.toSVG(svg);
        over.toSVG(svg);
        var delta = this.getDelta();
        var u = this.getOverKU(bbox, obox)[1];
        var v = this.getUnderKV(bbox, ubox)[1];
        var _c = __read(this.getDeltaW([bbox, ubox, obox], [0, this.isLineBelow ? 0 : -delta, this.isLineAbove ? 0 : delta]), 3), bx = _c[0], ux = _c[1], ox = _c[2];
        base.place(bx, 0);
        under.place(ux, v);
        over.place(ox, u);
    };
    SVGmunderover.kind = munderover_js_4.MmlMunderover.prototype.kind;
    return SVGmunderover;
}((0, munderover_js_3.CommonMunderoverMixin)(msubsup_js_1.SVGmsubsup)));
exports.SVGmunderover = SVGmunderover;
//# sourceMappingURL=munderover.js.map

/***/ }),

/***/ 1269:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGscriptbase = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var scriptbase_js_1 = __webpack_require__(7091);
var SVGscriptbase = (function (_super) {
    __extends(SVGscriptbase, _super);
    function SVGscriptbase() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGscriptbase.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        var w = this.getBaseWidth();
        var _a = __read(this.getOffset(), 2), x = _a[0], v = _a[1];
        this.baseChild.toSVG(svg);
        this.scriptChild.toSVG(svg);
        this.scriptChild.place(w + x, v);
    };
    SVGscriptbase.kind = 'scriptbase';
    return SVGscriptbase;
}((0, scriptbase_js_1.CommonScriptbaseMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGscriptbase = SVGscriptbase;
//# sourceMappingURL=scriptbase.js.map

/***/ }),

/***/ 6965:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SVGxml = exports.SVGannotationXML = exports.SVGannotation = exports.SVGsemantics = void 0;
var Wrapper_js_1 = __webpack_require__(9321);
var semantics_js_1 = __webpack_require__(3191);
var semantics_js_2 = __webpack_require__(9167);
var MmlNode_js_1 = __webpack_require__(8921);
var SVGsemantics = (function (_super) {
    __extends(SVGsemantics, _super);
    function SVGsemantics() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGsemantics.prototype.toSVG = function (parent) {
        var svg = this.standardSVGnode(parent);
        if (this.childNodes.length) {
            this.childNodes[0].toSVG(svg);
        }
    };
    SVGsemantics.kind = semantics_js_2.MmlSemantics.prototype.kind;
    return SVGsemantics;
}((0, semantics_js_1.CommonSemanticsMixin)(Wrapper_js_1.SVGWrapper)));
exports.SVGsemantics = SVGsemantics;
var SVGannotation = (function (_super) {
    __extends(SVGannotation, _super);
    function SVGannotation() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGannotation.prototype.toSVG = function (parent) {
        _super.prototype.toSVG.call(this, parent);
    };
    SVGannotation.prototype.computeBBox = function () {
        return this.bbox;
    };
    SVGannotation.kind = semantics_js_2.MmlAnnotation.prototype.kind;
    return SVGannotation;
}(Wrapper_js_1.SVGWrapper));
exports.SVGannotation = SVGannotation;
var SVGannotationXML = (function (_super) {
    __extends(SVGannotationXML, _super);
    function SVGannotationXML() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGannotationXML.kind = semantics_js_2.MmlAnnotationXML.prototype.kind;
    SVGannotationXML.styles = {
        'foreignObject[data-mjx-xml]': {
            'font-family': 'initial',
            'line-height': 'normal',
            overflow: 'visible'
        }
    };
    return SVGannotationXML;
}(Wrapper_js_1.SVGWrapper));
exports.SVGannotationXML = SVGannotationXML;
var SVGxml = (function (_super) {
    __extends(SVGxml, _super);
    function SVGxml() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    SVGxml.prototype.toSVG = function (parent) {
        var xml = this.adaptor.clone(this.node.getXML());
        var em = this.jax.math.metrics.em * this.jax.math.metrics.scale;
        var scale = this.fixed(1 / em);
        var _a = this.getBBox(), w = _a.w, h = _a.h, d = _a.d;
        this.element = this.adaptor.append(parent, this.svg('foreignObject', {
            'data-mjx-xml': true,
            y: this.jax.fixed(-h * em) + 'px',
            width: this.jax.fixed(w * em) + 'px',
            height: this.jax.fixed((h + d) * em) + 'px',
            transform: "scale(".concat(scale, ") matrix(1 0 0 -1 0 0)")
        }, [xml]));
    };
    SVGxml.prototype.computeBBox = function (bbox, _recompute) {
        if (_recompute === void 0) { _recompute = false; }
        var _a = this.jax.measureXMLnode(this.node.getXML()), w = _a.w, h = _a.h, d = _a.d;
        bbox.w = w;
        bbox.h = h;
        bbox.d = d;
    };
    SVGxml.prototype.getStyles = function () { };
    SVGxml.prototype.getScale = function () { };
    SVGxml.prototype.getVariant = function () { };
    SVGxml.kind = MmlNode_js_1.XMLNode.prototype.kind;
    SVGxml.autoStyle = false;
    return SVGxml;
}(Wrapper_js_1.SVGWrapper));
exports.SVGxml = SVGxml;
//# sourceMappingURL=semantics.js.map

/***/ }),

/***/ 8723:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;


__webpack_unused_export__ = ({
  value: true
});
__webpack_unused_export__ = MathJax._.components.global.isObject;
__webpack_unused_export__ = MathJax._.components.global.combineConfig;
exports.PV = MathJax._.components.global.combineDefaults;
exports.r8 = MathJax._.components.global.combineWithMathJax;
__webpack_unused_export__ = MathJax._.components.global.MathJax;

/***/ }),

/***/ 4769:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.protoItem = MathJax._.core.MathItem.protoItem;
exports.AbstractMathItem = MathJax._.core.MathItem.AbstractMathItem;
exports.STATE = MathJax._.core.MathItem.STATE;
exports.newState = MathJax._.core.MathItem.newState;

/***/ }),

/***/ 8921:
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

/***/ 4282:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.TeXAtom = MathJax._.core.MmlTree.MmlNodes.TeXAtom.TeXAtom;

/***/ }),

/***/ 3969:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMaction = MathJax._.core.MmlTree.MmlNodes.maction.MmlMaction;

/***/ }),

/***/ 304:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMath = MathJax._.core.MmlTree.MmlNodes.math.MmlMath;

/***/ }),

/***/ 4374:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMenclose = MathJax._.core.MmlTree.MmlNodes.menclose.MmlMenclose;

/***/ }),

/***/ 8078:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMerror = MathJax._.core.MmlTree.MmlNodes.merror.MmlMerror;

/***/ }),

/***/ 7451:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMfenced = MathJax._.core.MmlTree.MmlNodes.mfenced.MmlMfenced;

/***/ }),

/***/ 848:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMfrac = MathJax._.core.MmlTree.MmlNodes.mfrac.MmlMfrac;

/***/ }),

/***/ 910:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMglyph = MathJax._.core.MmlTree.MmlNodes.mglyph.MmlMglyph;

/***/ }),

/***/ 7754:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMi = MathJax._.core.MmlTree.MmlNodes.mi.MmlMi;

/***/ }),

/***/ 7764:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMmultiscripts = MathJax._.core.MmlTree.MmlNodes.mmultiscripts.MmlMmultiscripts;
exports.MmlMprescripts = MathJax._.core.MmlTree.MmlNodes.mmultiscripts.MmlMprescripts;
exports.MmlNone = MathJax._.core.MmlTree.MmlNodes.mmultiscripts.MmlNone;

/***/ }),

/***/ 3235:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMn = MathJax._.core.MmlTree.MmlNodes.mn.MmlMn;

/***/ }),

/***/ 9946:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMo = MathJax._.core.MmlTree.MmlNodes.mo.MmlMo;

/***/ }),

/***/ 189:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMpadded = MathJax._.core.MmlTree.MmlNodes.mpadded.MmlMpadded;

/***/ }),

/***/ 7988:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMphantom = MathJax._.core.MmlTree.MmlNodes.mphantom.MmlMphantom;

/***/ }),

/***/ 4664:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMroot = MathJax._.core.MmlTree.MmlNodes.mroot.MmlMroot;

/***/ }),

/***/ 1691:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMrow = MathJax._.core.MmlTree.MmlNodes.mrow.MmlMrow;
exports.MmlInferredMrow = MathJax._.core.MmlTree.MmlNodes.mrow.MmlInferredMrow;

/***/ }),

/***/ 4042:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMs = MathJax._.core.MmlTree.MmlNodes.ms.MmlMs;

/***/ }),

/***/ 1465:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMspace = MathJax._.core.MmlTree.MmlNodes.mspace.MmlMspace;

/***/ }),

/***/ 4655:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMsqrt = MathJax._.core.MmlTree.MmlNodes.msqrt.MmlMsqrt;

/***/ }),

/***/ 5857:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMsubsup = MathJax._.core.MmlTree.MmlNodes.msubsup.MmlMsubsup;
exports.MmlMsub = MathJax._.core.MmlTree.MmlNodes.msubsup.MmlMsub;
exports.MmlMsup = MathJax._.core.MmlTree.MmlNodes.msubsup.MmlMsup;

/***/ }),

/***/ 4859:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMtable = MathJax._.core.MmlTree.MmlNodes.mtable.MmlMtable;

/***/ }),

/***/ 2321:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMtd = MathJax._.core.MmlTree.MmlNodes.mtd.MmlMtd;

/***/ }),

/***/ 6277:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMtext = MathJax._.core.MmlTree.MmlNodes.mtext.MmlMtext;

/***/ }),

/***/ 4393:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMtr = MathJax._.core.MmlTree.MmlNodes.mtr.MmlMtr;
exports.MmlMlabeledtr = MathJax._.core.MmlTree.MmlNodes.mtr.MmlMlabeledtr;

/***/ }),

/***/ 3102:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMunderover = MathJax._.core.MmlTree.MmlNodes.munderover.MmlMunderover;
exports.MmlMunder = MathJax._.core.MmlTree.MmlNodes.munderover.MmlMunder;
exports.MmlMover = MathJax._.core.MmlTree.MmlNodes.munderover.MmlMover;

/***/ }),

/***/ 9167:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlSemantics = MathJax._.core.MmlTree.MmlNodes.semantics.MmlSemantics;
exports.MmlAnnotationXML = MathJax._.core.MmlTree.MmlNodes.semantics.MmlAnnotationXML;
exports.MmlAnnotation = MathJax._.core.MmlTree.MmlNodes.semantics.MmlAnnotation;

/***/ }),

/***/ 3985:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AbstractOutputJax = MathJax._.core.OutputJax.AbstractOutputJax;

/***/ }),

/***/ 9879:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AbstractWrapper = MathJax._.core.Tree.Wrapper.AbstractWrapper;

/***/ }),

/***/ 2506:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AbstractWrapperFactory = MathJax._.core.Tree.WrapperFactory.AbstractWrapperFactory;

/***/ }),

/***/ 3717:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.BBox = MathJax._.util.BBox.BBox;

/***/ }),

/***/ 9077:
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

/***/ 5888:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.CssStyles = MathJax._.util.StyleList.CssStyles;

/***/ }),

/***/ 5878:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Styles = MathJax._.util.Styles.Styles;

/***/ }),

/***/ 6914:
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

/***/ 1490:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.sum = MathJax._.util.numeric.sum;
exports.max = MathJax._.util.numeric.max;

/***/ }),

/***/ 6720:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.sortLength = MathJax._.util.string.sortLength;
exports.quotePattern = MathJax._.util.string.quotePattern;
exports.unicodeChars = MathJax._.util.string.unicodeChars;
exports.unicodeString = MathJax._.util.string.unicodeString;
exports.isPercent = MathJax._.util.string.isPercent;
exports.split = MathJax._.util.string.split;

/***/ }),

/***/ 4142:
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TeXFont": function() { return /* binding */ TeXFont; }
/* harmony export */ });
/* harmony import */ var _js_output_svg_FontData_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(9708);
/* harmony import */ var _js_output_svg_FontData_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_js_output_svg_FontData_js__WEBPACK_IMPORTED_MODULE_0__);
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }

function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf || function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }

function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }

function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }

function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }

function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }

function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }


var TeXFont = /*#__PURE__*/function (_FontData) {
  _inherits(TeXFont, _FontData);

  var _super = _createSuper(TeXFont);

  function TeXFont() {
    _classCallCheck(this, TeXFont);

    return _super.apply(this, arguments);
  }

  return _createClass(TeXFont);
}(_js_output_svg_FontData_js__WEBPACK_IMPORTED_MODULE_0__.FontData);
;
TeXFont.OPTIONS = {
  fontURL: '.'
};

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
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	!function() {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = function(module) {
/******/ 			var getter = module && module.__esModule ?
/******/ 				function() { return module['default']; } :
/******/ 				function() { return module; };
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	}();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	!function() {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = function(exports, definition) {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	}();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	!function() {
/******/ 		__webpack_require__.o = function(obj, prop) { return Object.prototype.hasOwnProperty.call(obj, prop); }
/******/ 	}();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	!function() {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = function(exports) {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	}();
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
!function() {

// EXTERNAL MODULE: ../../core/lib/components/global.js
var global = __webpack_require__(8723);
// EXTERNAL MODULE: ../../../../js/components/version.js
var version = __webpack_require__(7306);
// EXTERNAL MODULE: ../../../../js/output/common/FontData.js
var FontData = __webpack_require__(9250);
// EXTERNAL MODULE: ../../../../js/output/common/Notation.js
var Notation = __webpack_require__(5373);
// EXTERNAL MODULE: ../../../../js/output/common/OutputJax.js
var OutputJax = __webpack_require__(716);
// EXTERNAL MODULE: ../../../../js/output/common/Wrapper.js
var Wrapper = __webpack_require__(1541);
// EXTERNAL MODULE: ../../../../js/output/common/WrapperFactory.js
var WrapperFactory = __webpack_require__(1475);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/TeXAtom.js
var TeXAtom = __webpack_require__(3438);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/TextNode.js
var TextNode = __webpack_require__(555);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/maction.js
var maction = __webpack_require__(3345);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/math.js
var math = __webpack_require__(2057);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/menclose.js
var menclose = __webpack_require__(6200);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mfenced.js
var mfenced = __webpack_require__(1346);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mfrac.js
var mfrac = __webpack_require__(5705);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mglyph.js
var mglyph = __webpack_require__(7969);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mi.js
var mi = __webpack_require__(1419);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mmultiscripts.js
var mmultiscripts = __webpack_require__(9906);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mn.js
var mn = __webpack_require__(2304);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mo.js
var mo = __webpack_require__(437);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mpadded.js
var mpadded = __webpack_require__(7481);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mroot.js
var mroot = __webpack_require__(5997);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mrow.js
var mrow = __webpack_require__(9323);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/ms.js
var ms = __webpack_require__(6920);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mspace.js
var mspace = __webpack_require__(37);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/msqrt.js
var msqrt = __webpack_require__(222);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/msubsup.js
var msubsup = __webpack_require__(3069);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mtable.js
var mtable = __webpack_require__(8589);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mtd.js
var mtd = __webpack_require__(7805);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mtext.js
var mtext = __webpack_require__(8325);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/mtr.js
var mtr = __webpack_require__(4818);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/munderover.js
var munderover = __webpack_require__(9690);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/scriptbase.js
var scriptbase = __webpack_require__(7091);
// EXTERNAL MODULE: ../../../../js/output/common/Wrappers/semantics.js
var semantics = __webpack_require__(3191);
// EXTERNAL MODULE: ../../../../js/output/svg.js
var svg = __webpack_require__(6582);
// EXTERNAL MODULE: ../../../../js/output/svg/FontCache.js
var FontCache = __webpack_require__(4129);
// EXTERNAL MODULE: ../../../../js/output/svg/FontData.js
var svg_FontData = __webpack_require__(9708);
// EXTERNAL MODULE: ../../../../js/output/svg/Notation.js
var svg_Notation = __webpack_require__(9737);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrapper.js
var svg_Wrapper = __webpack_require__(9321);
// EXTERNAL MODULE: ../../../../js/output/svg/WrapperFactory.js
var svg_WrapperFactory = __webpack_require__(9416);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers.js
var Wrappers = __webpack_require__(4687);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/TeXAtom.js
var Wrappers_TeXAtom = __webpack_require__(484);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/TextNode.js
var Wrappers_TextNode = __webpack_require__(7455);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/maction.js
var Wrappers_maction = __webpack_require__(4601);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/math.js
var Wrappers_math = __webpack_require__(1211);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/menclose.js
var Wrappers_menclose = __webpack_require__(144);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/merror.js
var merror = __webpack_require__(3007);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mfenced.js
var Wrappers_mfenced = __webpack_require__(5258);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mfrac.js
var Wrappers_mfrac = __webpack_require__(9295);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mglyph.js
var Wrappers_mglyph = __webpack_require__(4916);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mi.js
var Wrappers_mi = __webpack_require__(2983);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mmultiscripts.js
var Wrappers_mmultiscripts = __webpack_require__(4750);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mn.js
var Wrappers_mn = __webpack_require__(9810);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mo.js
var Wrappers_mo = __webpack_require__(6760);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mpadded.js
var Wrappers_mpadded = __webpack_require__(4539);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mphantom.js
var mphantom = __webpack_require__(438);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mroot.js
var Wrappers_mroot = __webpack_require__(8798);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mrow.js
var Wrappers_mrow = __webpack_require__(322);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/ms.js
var Wrappers_ms = __webpack_require__(3677);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mspace.js
var Wrappers_mspace = __webpack_require__(2458);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/msqrt.js
var Wrappers_msqrt = __webpack_require__(9948);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/msubsup.js
var Wrappers_msubsup = __webpack_require__(7522);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mtable.js
var Wrappers_mtable = __webpack_require__(451);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mtd.js
var Wrappers_mtd = __webpack_require__(2673);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mtext.js
var Wrappers_mtext = __webpack_require__(1941);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/mtr.js
var Wrappers_mtr = __webpack_require__(4682);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/munderover.js
var Wrappers_munderover = __webpack_require__(4299);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/scriptbase.js
var Wrappers_scriptbase = __webpack_require__(1269);
// EXTERNAL MODULE: ../../../../js/output/svg/Wrappers/semantics.js
var Wrappers_semantics = __webpack_require__(6965);
;// CONCATENATED MODULE: ./lib/svg.js





































































if (MathJax.loader) {
  MathJax.loader.checkVersion('output/svg', version/* VERSION */.q, 'output');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    output: {
      common: {
        FontData: FontData,
        Notation: Notation,
        OutputJax: OutputJax,
        Wrapper: Wrapper,
        WrapperFactory: WrapperFactory,
        Wrappers: {
          TeXAtom: TeXAtom,
          TextNode: TextNode,
          maction: maction,
          math: math,
          menclose: menclose,
          mfenced: mfenced,
          mfrac: mfrac,
          mglyph: mglyph,
          mi: mi,
          mmultiscripts: mmultiscripts,
          mn: mn,
          mo: mo,
          mpadded: mpadded,
          mroot: mroot,
          mrow: mrow,
          ms: ms,
          mspace: mspace,
          msqrt: msqrt,
          msubsup: msubsup,
          mtable: mtable,
          mtd: mtd,
          mtext: mtext,
          mtr: mtr,
          munderover: munderover,
          scriptbase: scriptbase,
          semantics: semantics
        }
      },
      svg_ts: svg,
      svg: {
        FontCache: FontCache,
        FontData: svg_FontData,
        Notation: svg_Notation,
        Wrapper: svg_Wrapper,
        WrapperFactory: svg_WrapperFactory,
        Wrappers_ts: Wrappers,
        Wrappers: {
          TeXAtom: Wrappers_TeXAtom,
          TextNode: Wrappers_TextNode,
          maction: Wrappers_maction,
          math: Wrappers_math,
          menclose: Wrappers_menclose,
          merror: merror,
          mfenced: Wrappers_mfenced,
          mfrac: Wrappers_mfrac,
          mglyph: Wrappers_mglyph,
          mi: Wrappers_mi,
          mmultiscripts: Wrappers_mmultiscripts,
          mn: Wrappers_mn,
          mo: Wrappers_mo,
          mpadded: Wrappers_mpadded,
          mphantom: mphantom,
          mroot: Wrappers_mroot,
          mrow: Wrappers_mrow,
          ms: Wrappers_ms,
          mspace: Wrappers_mspace,
          msqrt: Wrappers_msqrt,
          msubsup: Wrappers_msubsup,
          mtable: Wrappers_mtable,
          mtd: Wrappers_mtd,
          mtext: Wrappers_mtext,
          mtr: Wrappers_mtr,
          munderover: Wrappers_munderover,
          scriptbase: Wrappers_scriptbase,
          semantics: Wrappers_semantics
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./svg.js




if (MathJax.loader) {
  (0,global/* combineDefaults */.PV)(MathJax.config.loader, 'output/svg', {
    checkReady: function checkReady() {
      return MathJax.loader.load("output/svg/fonts/tex");
    }
  });
}

if (MathJax.startup) {
  MathJax.startup.registerConstructor('svg', svg.SVG);
  MathJax.startup.useOutput('svg');
}
}();
/******/ })()
;