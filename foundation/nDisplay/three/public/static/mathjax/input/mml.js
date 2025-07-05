/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 306:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;

__webpack_unused_export__ = ({ value: true });
exports.q = void 0;
exports.q = '3.2.2';
//# sourceMappingURL=version.js.map

/***/ }),

/***/ 236:
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
exports.MathML = void 0;
var InputJax_js_1 = __webpack_require__(309);
var Options_js_1 = __webpack_require__(77);
var FunctionList_js_1 = __webpack_require__(898);
var FindMathML_js_1 = __webpack_require__(794);
var MathMLCompile_js_1 = __webpack_require__(332);
var MathML = (function (_super) {
    __extends(MathML, _super);
    function MathML(options) {
        if (options === void 0) { options = {}; }
        var _this = this;
        var _a = __read((0, Options_js_1.separateOptions)(options, FindMathML_js_1.FindMathML.OPTIONS, MathMLCompile_js_1.MathMLCompile.OPTIONS), 3), mml = _a[0], find = _a[1], compile = _a[2];
        _this = _super.call(this, mml) || this;
        _this.findMathML = _this.options['FindMathML'] || new FindMathML_js_1.FindMathML(find);
        _this.mathml = _this.options['MathMLCompile'] || new MathMLCompile_js_1.MathMLCompile(compile);
        _this.mmlFilters = new FunctionList_js_1.FunctionList();
        return _this;
    }
    MathML.prototype.setAdaptor = function (adaptor) {
        _super.prototype.setAdaptor.call(this, adaptor);
        this.findMathML.adaptor = adaptor;
        this.mathml.adaptor = adaptor;
    };
    MathML.prototype.setMmlFactory = function (mmlFactory) {
        _super.prototype.setMmlFactory.call(this, mmlFactory);
        this.mathml.setMmlFactory(mmlFactory);
    };
    Object.defineProperty(MathML.prototype, "processStrings", {
        get: function () {
            return false;
        },
        enumerable: false,
        configurable: true
    });
    MathML.prototype.compile = function (math, document) {
        var mml = math.start.node;
        if (!mml || !math.end.node || this.options['forceReparse'] || this.adaptor.kind(mml) === '#text') {
            var mathml = this.executeFilters(this.preFilters, math, document, (math.math || '<math></math>').trim());
            var doc = this.checkForErrors(this.adaptor.parse(mathml, 'text/' + this.options['parseAs']));
            var body = this.adaptor.body(doc);
            if (this.adaptor.childNodes(body).length !== 1) {
                this.error('MathML must consist of a single element');
            }
            mml = this.adaptor.remove(this.adaptor.firstChild(body));
            if (this.adaptor.kind(mml).replace(/^[a-z]+:/, '') !== 'math') {
                this.error('MathML must be formed by a <math> element, not <' + this.adaptor.kind(mml) + '>');
            }
        }
        mml = this.executeFilters(this.mmlFilters, math, document, mml);
        return this.executeFilters(this.postFilters, math, document, this.mathml.compile(mml));
    };
    MathML.prototype.checkForErrors = function (doc) {
        var err = this.adaptor.tags(this.adaptor.body(doc), 'parsererror')[0];
        if (err) {
            if (this.adaptor.textContent(err) === '') {
                this.error('Error processing MathML');
            }
            this.options['parseError'].call(this, err);
        }
        return doc;
    };
    MathML.prototype.error = function (message) {
        throw new Error(message);
    };
    MathML.prototype.findMath = function (node) {
        return this.findMathML.findMath(node);
    };
    MathML.NAME = 'MathML';
    MathML.OPTIONS = (0, Options_js_1.defaultOptions)({
        parseAs: 'html',
        forceReparse: false,
        FindMathML: null,
        MathMLCompile: null,
        parseError: function (node) {
            this.error(this.adaptor.textContent(node).replace(/\n.*/g, ''));
        }
    }, InputJax_js_1.AbstractInputJax.OPTIONS);
    return MathML;
}(InputJax_js_1.AbstractInputJax));
exports.MathML = MathML;
//# sourceMappingURL=mathml.js.map

/***/ }),

/***/ 794:
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
exports.FindMathML = void 0;
var FindMath_js_1 = __webpack_require__(649);
var NAMESPACE = 'http://www.w3.org/1998/Math/MathML';
var FindMathML = (function (_super) {
    __extends(FindMathML, _super);
    function FindMathML() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    FindMathML.prototype.findMath = function (node) {
        var set = new Set();
        this.findMathNodes(node, set);
        this.findMathPrefixed(node, set);
        var html = this.adaptor.root(this.adaptor.document);
        if (this.adaptor.kind(html) === 'html' && set.size === 0) {
            this.findMathNS(node, set);
        }
        return this.processMath(set);
    };
    FindMathML.prototype.findMathNodes = function (node, set) {
        var e_1, _a;
        try {
            for (var _b = __values(this.adaptor.tags(node, 'math')), _c = _b.next(); !_c.done; _c = _b.next()) {
                var math = _c.value;
                set.add(math);
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
    FindMathML.prototype.findMathPrefixed = function (node, set) {
        var e_2, _a, e_3, _b;
        var html = this.adaptor.root(this.adaptor.document);
        try {
            for (var _c = __values(this.adaptor.allAttributes(html)), _d = _c.next(); !_d.done; _d = _c.next()) {
                var attr = _d.value;
                if (attr.name.substr(0, 6) === 'xmlns:' && attr.value === NAMESPACE) {
                    var prefix = attr.name.substr(6);
                    try {
                        for (var _e = (e_3 = void 0, __values(this.adaptor.tags(node, prefix + ':math'))), _f = _e.next(); !_f.done; _f = _e.next()) {
                            var math = _f.value;
                            set.add(math);
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
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_2) throw e_2.error; }
        }
    };
    FindMathML.prototype.findMathNS = function (node, set) {
        var e_4, _a;
        try {
            for (var _b = __values(this.adaptor.tags(node, 'math', NAMESPACE)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var math = _c.value;
                set.add(math);
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
    FindMathML.prototype.processMath = function (set) {
        var e_5, _a;
        var math = [];
        try {
            for (var _b = __values(Array.from(set)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var mml = _c.value;
                var display = (this.adaptor.getAttribute(mml, 'display') === 'block' ||
                    this.adaptor.getAttribute(mml, 'mode') === 'display');
                var start = { node: mml, n: 0, delim: '' };
                var end = { node: mml, n: 0, delim: '' };
                math.push({ math: this.adaptor.outerHTML(mml), start: start, end: end, display: display });
            }
        }
        catch (e_5_1) { e_5 = { error: e_5_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_5) throw e_5.error; }
        }
        return math;
    };
    FindMathML.OPTIONS = {};
    return FindMathML;
}(FindMath_js_1.AbstractFindMath));
exports.FindMathML = FindMathML;
//# sourceMappingURL=FindMathML.js.map

/***/ }),

/***/ 332:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MathMLCompile = void 0;
var MmlNode_js_1 = __webpack_require__(921);
var Options_js_1 = __webpack_require__(77);
var Entities = __importStar(__webpack_require__(29));
var MathMLCompile = (function () {
    function MathMLCompile(options) {
        if (options === void 0) { options = {}; }
        var Class = this.constructor;
        this.options = (0, Options_js_1.userOptions)((0, Options_js_1.defaultOptions)({}, Class.OPTIONS), options);
    }
    MathMLCompile.prototype.setMmlFactory = function (mmlFactory) {
        this.factory = mmlFactory;
    };
    MathMLCompile.prototype.compile = function (node) {
        var mml = this.makeNode(node);
        mml.verifyTree(this.options['verify']);
        mml.setInheritedAttributes({}, false, 0, false);
        mml.walkTree(this.markMrows);
        return mml;
    };
    MathMLCompile.prototype.makeNode = function (node) {
        var e_1, _a;
        var adaptor = this.adaptor;
        var limits = false;
        var kind = adaptor.kind(node).replace(/^.*:/, '');
        var texClass = adaptor.getAttribute(node, 'data-mjx-texclass') || '';
        if (texClass) {
            texClass = this.filterAttribute('data-mjx-texclass', texClass) || '';
        }
        var type = texClass && kind === 'mrow' ? 'TeXAtom' : kind;
        try {
            for (var _b = __values(this.filterClassList(adaptor.allClasses(node))), _c = _b.next(); !_c.done; _c = _b.next()) {
                var name_1 = _c.value;
                if (name_1.match(/^MJX-TeXAtom-/) && kind === 'mrow') {
                    texClass = name_1.substr(12);
                    type = 'TeXAtom';
                }
                else if (name_1 === 'MJX-fixedlimits') {
                    limits = true;
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
        this.factory.getNodeClass(type) || this.error('Unknown node type "' + type + '"');
        var mml = this.factory.create(type);
        if (type === 'TeXAtom' && texClass === 'OP' && !limits) {
            mml.setProperty('movesupsub', true);
            mml.attributes.setInherited('movablelimits', true);
        }
        if (texClass) {
            mml.texClass = MmlNode_js_1.TEXCLASS[texClass];
            mml.setProperty('texClass', mml.texClass);
        }
        this.addAttributes(mml, node);
        this.checkClass(mml, node);
        this.addChildren(mml, node);
        return mml;
    };
    MathMLCompile.prototype.addAttributes = function (mml, node) {
        var e_2, _a;
        var ignoreVariant = false;
        try {
            for (var _b = __values(this.adaptor.allAttributes(node)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var attr = _c.value;
                var name_2 = attr.name;
                var value = this.filterAttribute(name_2, attr.value);
                if (value === null || name_2 === 'xmlns') {
                    continue;
                }
                if (name_2.substr(0, 9) === 'data-mjx-') {
                    switch (name_2.substr(9)) {
                        case 'alternate':
                            mml.setProperty('variantForm', true);
                            break;
                        case 'variant':
                            mml.attributes.set('mathvariant', value);
                            ignoreVariant = true;
                            break;
                        case 'smallmatrix':
                            mml.setProperty('scriptlevel', 1);
                            mml.setProperty('useHeight', false);
                            break;
                        case 'accent':
                            mml.setProperty('mathaccent', value === 'true');
                            break;
                        case 'auto-op':
                            mml.setProperty('autoOP', value === 'true');
                            break;
                        case 'script-align':
                            mml.setProperty('scriptalign', value);
                            break;
                    }
                }
                else if (name_2 !== 'class') {
                    var val = value.toLowerCase();
                    if (val === 'true' || val === 'false') {
                        mml.attributes.set(name_2, val === 'true');
                    }
                    else if (!ignoreVariant || name_2 !== 'mathvariant') {
                        mml.attributes.set(name_2, value);
                    }
                }
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_2) throw e_2.error; }
        }
    };
    MathMLCompile.prototype.filterAttribute = function (_name, value) {
        return value;
    };
    MathMLCompile.prototype.filterClassList = function (list) {
        return list;
    };
    MathMLCompile.prototype.addChildren = function (mml, node) {
        var e_3, _a;
        if (mml.arity === 0) {
            return;
        }
        var adaptor = this.adaptor;
        try {
            for (var _b = __values(adaptor.childNodes(node)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var child = _c.value;
                var name_3 = adaptor.kind(child);
                if (name_3 === '#comment') {
                    continue;
                }
                if (name_3 === '#text') {
                    this.addText(mml, child);
                }
                else if (mml.isKind('annotation-xml')) {
                    mml.appendChild(this.factory.create('XML').setXML(child, adaptor));
                }
                else {
                    var childMml = mml.appendChild(this.makeNode(child));
                    if (childMml.arity === 0 && adaptor.childNodes(child).length) {
                        if (this.options['fixMisplacedChildren']) {
                            this.addChildren(mml, child);
                        }
                        else {
                            childMml.mError('There should not be children for ' + childMml.kind + ' nodes', this.options['verify'], true);
                        }
                    }
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
    };
    MathMLCompile.prototype.addText = function (mml, child) {
        var text = this.adaptor.value(child);
        if ((mml.isToken || mml.getProperty('isChars')) && mml.arity) {
            if (mml.isToken) {
                text = Entities.translate(text);
                text = this.trimSpace(text);
            }
            mml.appendChild(this.factory.create('text').setText(text));
        }
        else if (text.match(/\S/)) {
            this.error('Unexpected text node "' + text + '"');
        }
    };
    MathMLCompile.prototype.checkClass = function (mml, node) {
        var e_4, _a;
        var classList = [];
        try {
            for (var _b = __values(this.filterClassList(this.adaptor.allClasses(node))), _c = _b.next(); !_c.done; _c = _b.next()) {
                var name_4 = _c.value;
                if (name_4.substr(0, 4) === 'MJX-') {
                    if (name_4 === 'MJX-variant') {
                        mml.setProperty('variantForm', true);
                    }
                    else if (name_4.substr(0, 11) !== 'MJX-TeXAtom') {
                        mml.attributes.set('mathvariant', this.fixCalligraphic(name_4.substr(3)));
                    }
                }
                else {
                    classList.push(name_4);
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
        if (classList.length) {
            mml.attributes.set('class', classList.join(' '));
        }
    };
    MathMLCompile.prototype.fixCalligraphic = function (variant) {
        return variant.replace(/caligraphic/, 'calligraphic');
    };
    MathMLCompile.prototype.markMrows = function (mml) {
        if (mml.isKind('mrow') && !mml.isInferred && mml.childNodes.length >= 2) {
            var first = mml.childNodes[0];
            var last = mml.childNodes[mml.childNodes.length - 1];
            if (first.isKind('mo') && first.attributes.get('fence') && first.attributes.get('stretchy') &&
                last.isKind('mo') && last.attributes.get('fence') && last.attributes.get('stretchy')) {
                if (first.childNodes.length) {
                    mml.setProperty('open', first.getText());
                }
                if (last.childNodes.length) {
                    mml.setProperty('close', last.getText());
                }
            }
        }
    };
    MathMLCompile.prototype.trimSpace = function (text) {
        return text.replace(/[\t\n\r]/g, ' ')
            .replace(/^ +/, '')
            .replace(/ +$/, '')
            .replace(/  +/g, ' ');
    };
    MathMLCompile.prototype.error = function (message) {
        throw new Error(message);
    };
    MathMLCompile.OPTIONS = {
        MmlFactory: null,
        fixMisplacedChildren: true,
        verify: __assign({}, MmlNode_js_1.AbstractMmlNode.verifyDefaults),
        translateEntities: true
    };
    return MathMLCompile;
}());
exports.MathMLCompile = MathMLCompile;
//# sourceMappingURL=MathMLCompile.js.map

/***/ }),

/***/ 723:
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

/***/ 649:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AbstractFindMath = MathJax._.core.FindMath.AbstractFindMath;

/***/ }),

/***/ 309:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AbstractInputJax = MathJax._.core.InputJax.AbstractInputJax;

/***/ }),

/***/ 921:
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

/***/ 29:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.options = MathJax._.util.Entities.options;
exports.entities = MathJax._.util.Entities.entities;
exports.add = MathJax._.util.Entities.add;
exports.remove = MathJax._.util.Entities.remove;
exports.translate = MathJax._.util.Entities.translate;
exports.numeric = MathJax._.util.Entities.numeric;

/***/ }),

/***/ 898:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.FunctionList = MathJax._.util.FunctionList.FunctionList;

/***/ }),

/***/ 77:
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

// EXTERNAL MODULE: ../../core/lib/components/global.js
var global = __webpack_require__(723);
// EXTERNAL MODULE: ../../../../js/components/version.js
var version = __webpack_require__(306);
// EXTERNAL MODULE: ../../../../js/input/mathml.js
var mathml = __webpack_require__(236);
// EXTERNAL MODULE: ../../../../js/input/mathml/FindMathML.js
var FindMathML = __webpack_require__(794);
// EXTERNAL MODULE: ../../../../js/input/mathml/MathMLCompile.js
var MathMLCompile = __webpack_require__(332);
;// CONCATENATED MODULE: ./lib/mml.js






if (MathJax.loader) {
  MathJax.loader.checkVersion('input/mml', version/* VERSION */.q, 'input');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      mathml_ts: mathml,
      mathml: {
        FindMathML: FindMathML,
        MathMLCompile: MathMLCompile
      }
    }
  }
});
;// CONCATENATED MODULE: ./mml.js



if (MathJax.startup) {
  MathJax.startup.registerConstructor('mml', mathml.MathML);
  MathJax.startup.useInput('mml');
}

if (MathJax.loader) {
  //
  // Install a path-filter to cause loading of an entity file to load all entities,
  //   since the individual files don't have individual components.
  //
  MathJax.loader.pathFilters.add(function (data) {
    data.name = data.name.replace(/\/util\/entities\/.*?\.js/, '/input/mml/entities.js');
    return true;
  });
}
}();
/******/ })()
;