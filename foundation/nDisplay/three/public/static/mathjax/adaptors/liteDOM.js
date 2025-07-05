/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 244:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.NodeMixin = exports.NodeMixinOptions = void 0;
var Options_js_1 = __webpack_require__(77);
exports.NodeMixinOptions = {
    badCSS: true,
    badSizes: true,
};
function NodeMixin(Base, options) {
    var _a;
    if (options === void 0) { options = {}; }
    options = (0, Options_js_1.userOptions)((0, Options_js_1.defaultOptions)({}, exports.NodeMixinOptions), options);
    return _a = (function (_super) {
            __extends(NodeAdaptor, _super);
            function NodeAdaptor() {
                var args = [];
                for (var _i = 0; _i < arguments.length; _i++) {
                    args[_i] = arguments[_i];
                }
                var _this = _super.call(this, args[0]) || this;
                var CLASS = _this.constructor;
                _this.options = (0, Options_js_1.userOptions)((0, Options_js_1.defaultOptions)({}, CLASS.OPTIONS), args[1]);
                return _this;
            }
            NodeAdaptor.prototype.fontSize = function (node) {
                return (options.badCSS ? this.options.fontSize : _super.prototype.fontSize.call(this, node));
            };
            NodeAdaptor.prototype.fontFamily = function (node) {
                return (options.badCSS ? this.options.fontFamily : _super.prototype.fontFamily.call(this, node));
            };
            NodeAdaptor.prototype.nodeSize = function (node, em, local) {
                if (em === void 0) { em = 1; }
                if (local === void 0) { local = null; }
                if (!options.badSizes) {
                    return _super.prototype.nodeSize.call(this, node, em, local);
                }
                var text = this.textContent(node);
                var non = Array.from(text.replace(NodeAdaptor.cjkPattern, '')).length;
                var CJK = Array.from(text).length - non;
                return [
                    CJK * this.options.cjkCharWidth + non * this.options.unknownCharWidth,
                    this.options.unknownCharHeight
                ];
            };
            NodeAdaptor.prototype.nodeBBox = function (node) {
                return (options.badSizes ? { left: 0, right: 0, top: 0, bottom: 0 } : _super.prototype.nodeBBox.call(this, node));
            };
            return NodeAdaptor;
        }(Base)),
        _a.OPTIONS = __assign(__assign({}, (options.badCSS ? {
            fontSize: 16,
            fontFamily: 'Times',
        } : {})), (options.badSizes ? {
            cjkCharWidth: 1,
            unknownCharWidth: .6,
            unknownCharHeight: .8,
        } : {})),
        _a.cjkPattern = new RegExp([
            '[',
            '\u1100-\u115F',
            '\u2329\u232A',
            '\u2E80-\u303E',
            '\u3040-\u3247',
            '\u3250-\u4DBF',
            '\u4E00-\uA4C6',
            '\uA960-\uA97C',
            '\uAC00-\uD7A3',
            '\uF900-\uFAFF',
            '\uFE10-\uFE19',
            '\uFE30-\uFE6B',
            '\uFF01-\uFF60\uFFE0-\uFFE6',
            "\uD82C\uDC00-\uD82C\uDC01",
            "\uD83C\uDE00-\uD83C\uDE51",
            "\uD840\uDC00-\uD8BF\uDFFD",
            ']'
        ].join(''), 'gu'),
        _a;
}
exports.NodeMixin = NodeMixin;
//# sourceMappingURL=NodeMixin.js.map

/***/ }),

/***/ 877:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.LiteDocument = void 0;
var Element_js_1 = __webpack_require__(946);
var LiteDocument = (function () {
    function LiteDocument() {
        this.root = new Element_js_1.LiteElement('html', {}, [
            this.head = new Element_js_1.LiteElement('head'),
            this.body = new Element_js_1.LiteElement('body')
        ]);
        this.type = '';
    }
    Object.defineProperty(LiteDocument.prototype, "kind", {
        get: function () {
            return '#document';
        },
        enumerable: false,
        configurable: true
    });
    return LiteDocument;
}());
exports.LiteDocument = LiteDocument;
//# sourceMappingURL=Document.js.map

/***/ }),

/***/ 946:
/***/ (function(__unused_webpack_module, exports) {


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
exports.LiteElement = void 0;
var LiteElement = (function () {
    function LiteElement(kind, attributes, children) {
        var e_1, _a;
        if (attributes === void 0) { attributes = {}; }
        if (children === void 0) { children = []; }
        this.kind = kind;
        this.attributes = __assign({}, attributes);
        this.children = __spreadArray([], __read(children), false);
        try {
            for (var _b = __values(this.children), _c = _b.next(); !_c.done; _c = _b.next()) {
                var child = _c.value;
                child.parent = this;
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_1) throw e_1.error; }
        }
        this.styles = null;
    }
    return LiteElement;
}());
exports.LiteElement = LiteElement;
//# sourceMappingURL=Element.js.map

/***/ }),

/***/ 6:
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
exports.LiteList = void 0;
var LiteList = (function () {
    function LiteList(children) {
        this.nodes = [];
        this.nodes = __spreadArray([], __read(children), false);
    }
    LiteList.prototype.append = function (node) {
        this.nodes.push(node);
    };
    LiteList.prototype[Symbol.iterator] = function () {
        var i = 0;
        return {
            next: function () {
                return (i === this.nodes.length ?
                    { value: null, done: true } :
                    { value: this.nodes[i++], done: false });
            }
        };
    };
    return LiteList;
}());
exports.LiteList = LiteList;
//# sourceMappingURL=List.js.map

/***/ }),

/***/ 246:
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
exports.LiteParser = exports.PATTERNS = void 0;
var Entities = __importStar(__webpack_require__(29));
var Element_js_1 = __webpack_require__(946);
var Text_js_1 = __webpack_require__(735);
var PATTERNS;
(function (PATTERNS) {
    PATTERNS.TAGNAME = '[a-z][^\\s\\n>]*';
    PATTERNS.ATTNAME = '[a-z][^\\s\\n>=]*';
    PATTERNS.VALUE = "(?:'[^']*'|\"[^\"]*\"|[^\\s\\n]+)";
    PATTERNS.VALUESPLIT = "(?:'([^']*)'|\"([^\"]*)\"|([^\\s\\n]+))";
    PATTERNS.SPACE = '(?:\\s|\\n)+';
    PATTERNS.OPTIONALSPACE = '(?:\\s|\\n)*';
    PATTERNS.ATTRIBUTE = PATTERNS.ATTNAME + '(?:' + PATTERNS.OPTIONALSPACE + '=' + PATTERNS.OPTIONALSPACE + PATTERNS.VALUE + ')?';
    PATTERNS.ATTRIBUTESPLIT = '(' + PATTERNS.ATTNAME + ')(?:' + PATTERNS.OPTIONALSPACE + '=' + PATTERNS.OPTIONALSPACE + PATTERNS.VALUESPLIT + ')?';
    PATTERNS.TAG = '(<(?:' + PATTERNS.TAGNAME + '(?:' + PATTERNS.SPACE + PATTERNS.ATTRIBUTE + ')*'
        + PATTERNS.OPTIONALSPACE + '/?|/' + PATTERNS.TAGNAME + '|!--[^]*?--|![^]*?)(?:>|$))';
    PATTERNS.tag = new RegExp(PATTERNS.TAG, 'i');
    PATTERNS.attr = new RegExp(PATTERNS.ATTRIBUTE, 'i');
    PATTERNS.attrsplit = new RegExp(PATTERNS.ATTRIBUTESPLIT, 'i');
})(PATTERNS = exports.PATTERNS || (exports.PATTERNS = {}));
var LiteParser = (function () {
    function LiteParser() {
    }
    LiteParser.prototype.parseFromString = function (text, _format, adaptor) {
        if (_format === void 0) { _format = 'text/html'; }
        if (adaptor === void 0) { adaptor = null; }
        var root = adaptor.createDocument();
        var node = adaptor.body(root);
        var parts = text.replace(/<\?.*?\?>/g, '').split(PATTERNS.tag);
        while (parts.length) {
            var text_1 = parts.shift();
            var tag = parts.shift();
            if (text_1) {
                this.addText(adaptor, node, text_1);
            }
            if (tag && tag.charAt(tag.length - 1) === '>') {
                if (tag.charAt(1) === '!') {
                    this.addComment(adaptor, node, tag);
                }
                else if (tag.charAt(1) === '/') {
                    node = this.closeTag(adaptor, node, tag);
                }
                else {
                    node = this.openTag(adaptor, node, tag, parts);
                }
            }
        }
        this.checkDocument(adaptor, root);
        return root;
    };
    LiteParser.prototype.addText = function (adaptor, node, text) {
        text = Entities.translate(text);
        return adaptor.append(node, adaptor.text(text));
    };
    LiteParser.prototype.addComment = function (adaptor, node, comment) {
        return adaptor.append(node, new Text_js_1.LiteComment(comment));
    };
    LiteParser.prototype.closeTag = function (adaptor, node, tag) {
        var kind = tag.slice(2, tag.length - 1).toLowerCase();
        while (adaptor.parent(node) && adaptor.kind(node) !== kind) {
            node = adaptor.parent(node);
        }
        return adaptor.parent(node);
    };
    LiteParser.prototype.openTag = function (adaptor, node, tag, parts) {
        var PCDATA = this.constructor.PCDATA;
        var SELF_CLOSING = this.constructor.SELF_CLOSING;
        var kind = tag.match(/<(.*?)[\s\n>\/]/)[1].toLowerCase();
        var child = adaptor.node(kind);
        var attributes = tag.replace(/^<.*?[\s\n>]/, '').split(PATTERNS.attrsplit);
        if (attributes.pop().match(/>$/) || attributes.length < 5) {
            this.addAttributes(adaptor, child, attributes);
            adaptor.append(node, child);
            if (!SELF_CLOSING[kind] && !tag.match(/\/>$/)) {
                if (PCDATA[kind]) {
                    this.handlePCDATA(adaptor, child, kind, parts);
                }
                else {
                    node = child;
                }
            }
        }
        return node;
    };
    LiteParser.prototype.addAttributes = function (adaptor, node, attributes) {
        var CDATA_ATTR = this.constructor.CDATA_ATTR;
        while (attributes.length) {
            var _a = __read(attributes.splice(0, 5), 5), name_1 = _a[1], v1 = _a[2], v2 = _a[3], v3 = _a[4];
            var value = v1 || v2 || v3 || '';
            if (!CDATA_ATTR[name_1]) {
                value = Entities.translate(value);
            }
            adaptor.setAttribute(node, name_1, value);
        }
    };
    LiteParser.prototype.handlePCDATA = function (adaptor, node, kind, parts) {
        var pcdata = [];
        var etag = '</' + kind + '>';
        var ptag = '';
        while (parts.length && ptag !== etag) {
            pcdata.push(ptag);
            pcdata.push(parts.shift());
            ptag = parts.shift();
        }
        adaptor.append(node, adaptor.text(pcdata.join('')));
    };
    LiteParser.prototype.checkDocument = function (adaptor, root) {
        var e_1, _a, e_2, _b;
        var node = this.getOnlyChild(adaptor, adaptor.body(root));
        if (!node)
            return;
        try {
            for (var _c = __values(adaptor.childNodes(adaptor.body(root))), _d = _c.next(); !_d.done; _d = _c.next()) {
                var child = _d.value;
                if (child === node) {
                    break;
                }
                if (child instanceof Text_js_1.LiteComment && child.value.match(/^<!DOCTYPE/)) {
                    root.type = child.value;
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
        switch (adaptor.kind(node)) {
            case 'html':
                try {
                    for (var _e = __values(node.children), _f = _e.next(); !_f.done; _f = _e.next()) {
                        var child = _f.value;
                        switch (adaptor.kind(child)) {
                            case 'head':
                                root.head = child;
                                break;
                            case 'body':
                                root.body = child;
                                break;
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
                root.root = node;
                adaptor.remove(node);
                if (adaptor.parent(root.body) !== node) {
                    adaptor.append(node, root.body);
                }
                if (adaptor.parent(root.head) !== node) {
                    adaptor.insert(root.head, root.body);
                }
                break;
            case 'head':
                root.head = adaptor.replace(node, root.head);
                break;
            case 'body':
                root.body = adaptor.replace(node, root.body);
                break;
        }
    };
    LiteParser.prototype.getOnlyChild = function (adaptor, body) {
        var e_3, _a;
        var node = null;
        try {
            for (var _b = __values(adaptor.childNodes(body)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var child = _c.value;
                if (child instanceof Element_js_1.LiteElement) {
                    if (node)
                        return null;
                    node = child;
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
        return node;
    };
    LiteParser.prototype.serialize = function (adaptor, node, xml) {
        var _this = this;
        if (xml === void 0) { xml = false; }
        var SELF_CLOSING = this.constructor.SELF_CLOSING;
        var CDATA = this.constructor.CDATA_ATTR;
        var tag = adaptor.kind(node);
        var attributes = adaptor.allAttributes(node).map(function (x) { return x.name + '="' + (CDATA[x.name] ? x.value : _this.protectAttribute(x.value)) + '"'; }).join(' ');
        var content = this.serializeInner(adaptor, node, xml);
        var html = '<' + tag + (attributes ? ' ' + attributes : '')
            + ((!xml || content) && !SELF_CLOSING[tag] ? ">".concat(content, "</").concat(tag, ">") : xml ? '/>' : '>');
        return html;
    };
    LiteParser.prototype.serializeInner = function (adaptor, node, xml) {
        var _this = this;
        if (xml === void 0) { xml = false; }
        var PCDATA = this.constructor.PCDATA;
        if (PCDATA.hasOwnProperty(node.kind)) {
            return adaptor.childNodes(node).map(function (x) { return adaptor.value(x); }).join('');
        }
        return adaptor.childNodes(node).map(function (x) {
            var kind = adaptor.kind(x);
            return (kind === '#text' ? _this.protectHTML(adaptor.value(x)) :
                kind === '#comment' ? x.value :
                    _this.serialize(adaptor, x, xml));
        }).join('');
    };
    LiteParser.prototype.protectAttribute = function (text) {
        if (typeof text !== 'string') {
            text = String(text);
        }
        return text.replace(/"/g, '&quot;');
    };
    LiteParser.prototype.protectHTML = function (text) {
        return text.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    };
    LiteParser.SELF_CLOSING = {
        area: true,
        base: true,
        br: true,
        col: true,
        command: true,
        embed: true,
        hr: true,
        img: true,
        input: true,
        keygen: true,
        link: true,
        menuitem: true,
        meta: true,
        param: true,
        source: true,
        track: true,
        wbr: true
    };
    LiteParser.PCDATA = {
        option: true,
        textarea: true,
        fieldset: true,
        title: true,
        style: true,
        script: true
    };
    LiteParser.CDATA_ATTR = {
        style: true,
        datafld: true,
        datasrc: true,
        href: true,
        src: true,
        longdesc: true,
        usemap: true,
        cite: true,
        datetime: true,
        action: true,
        axis: true,
        profile: true,
        content: true,
        scheme: true
    };
    return LiteParser;
}());
exports.LiteParser = LiteParser;
//# sourceMappingURL=Parser.js.map

/***/ }),

/***/ 735:
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
exports.LiteComment = exports.LiteText = void 0;
var LiteText = (function () {
    function LiteText(text) {
        if (text === void 0) { text = ''; }
        this.value = text;
    }
    Object.defineProperty(LiteText.prototype, "kind", {
        get: function () {
            return '#text';
        },
        enumerable: false,
        configurable: true
    });
    return LiteText;
}());
exports.LiteText = LiteText;
var LiteComment = (function (_super) {
    __extends(LiteComment, _super);
    function LiteComment() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(LiteComment.prototype, "kind", {
        get: function () {
            return '#comment';
        },
        enumerable: false,
        configurable: true
    });
    return LiteComment;
}(LiteText));
exports.LiteComment = LiteComment;
//# sourceMappingURL=Text.js.map

/***/ }),

/***/ 492:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.LiteWindow = void 0;
var Element_js_1 = __webpack_require__(946);
var Document_js_1 = __webpack_require__(877);
var List_js_1 = __webpack_require__(6);
var Parser_js_1 = __webpack_require__(246);
var LiteWindow = (function () {
    function LiteWindow() {
        this.DOMParser = Parser_js_1.LiteParser;
        this.NodeList = List_js_1.LiteList;
        this.HTMLCollection = List_js_1.LiteList;
        this.HTMLElement = Element_js_1.LiteElement;
        this.DocumentFragment = List_js_1.LiteList;
        this.Document = Document_js_1.LiteDocument;
        this.document = new Document_js_1.LiteDocument();
    }
    return LiteWindow;
}());
exports.LiteWindow = LiteWindow;
//# sourceMappingURL=Window.js.map

/***/ }),

/***/ 250:
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
exports.liteAdaptor = exports.LiteAdaptor = exports.LiteBase = void 0;
var DOMAdaptor_js_1 = __webpack_require__(857);
var NodeMixin_js_1 = __webpack_require__(244);
var Document_js_1 = __webpack_require__(877);
var Element_js_1 = __webpack_require__(946);
var Text_js_1 = __webpack_require__(735);
var Window_js_1 = __webpack_require__(492);
var Parser_js_1 = __webpack_require__(246);
var Styles_js_1 = __webpack_require__(878);
var LiteBase = (function (_super) {
    __extends(LiteBase, _super);
    function LiteBase() {
        var _this = _super.call(this) || this;
        _this.parser = new Parser_js_1.LiteParser();
        _this.window = new Window_js_1.LiteWindow();
        return _this;
    }
    LiteBase.prototype.parse = function (text, format) {
        return this.parser.parseFromString(text, format, this);
    };
    LiteBase.prototype.create = function (kind, _ns) {
        if (_ns === void 0) { _ns = null; }
        return new Element_js_1.LiteElement(kind);
    };
    LiteBase.prototype.text = function (text) {
        return new Text_js_1.LiteText(text);
    };
    LiteBase.prototype.comment = function (text) {
        return new Text_js_1.LiteComment(text);
    };
    LiteBase.prototype.createDocument = function () {
        return new Document_js_1.LiteDocument();
    };
    LiteBase.prototype.head = function (doc) {
        return doc.head;
    };
    LiteBase.prototype.body = function (doc) {
        return doc.body;
    };
    LiteBase.prototype.root = function (doc) {
        return doc.root;
    };
    LiteBase.prototype.doctype = function (doc) {
        return doc.type;
    };
    LiteBase.prototype.tags = function (node, name, ns) {
        if (ns === void 0) { ns = null; }
        var stack = [];
        var tags = [];
        if (ns) {
            return tags;
        }
        var n = node;
        while (n) {
            var kind = n.kind;
            if (kind !== '#text' && kind !== '#comment') {
                n = n;
                if (kind === name) {
                    tags.push(n);
                }
                if (n.children.length) {
                    stack = n.children.concat(stack);
                }
            }
            n = stack.shift();
        }
        return tags;
    };
    LiteBase.prototype.elementById = function (node, id) {
        var stack = [];
        var n = node;
        while (n) {
            if (n.kind !== '#text' && n.kind !== '#comment') {
                n = n;
                if (n.attributes['id'] === id) {
                    return n;
                }
                if (n.children.length) {
                    stack = n.children.concat(stack);
                }
            }
            n = stack.shift();
        }
        return null;
    };
    LiteBase.prototype.elementsByClass = function (node, name) {
        var stack = [];
        var tags = [];
        var n = node;
        while (n) {
            if (n.kind !== '#text' && n.kind !== '#comment') {
                n = n;
                var classes = (n.attributes['class'] || '').trim().split(/ +/);
                if (classes.includes(name)) {
                    tags.push(n);
                }
                if (n.children.length) {
                    stack = n.children.concat(stack);
                }
            }
            n = stack.shift();
        }
        return tags;
    };
    LiteBase.prototype.getElements = function (nodes, document) {
        var e_1, _a;
        var containers = [];
        var body = this.body(document);
        try {
            for (var nodes_1 = __values(nodes), nodes_1_1 = nodes_1.next(); !nodes_1_1.done; nodes_1_1 = nodes_1.next()) {
                var node = nodes_1_1.value;
                if (typeof (node) === 'string') {
                    if (node.charAt(0) === '#') {
                        var n = this.elementById(body, node.slice(1));
                        if (n) {
                            containers.push(n);
                        }
                    }
                    else if (node.charAt(0) === '.') {
                        containers = containers.concat(this.elementsByClass(body, node.slice(1)));
                    }
                    else if (node.match(/^[-a-z][-a-z0-9]*$/i)) {
                        containers = containers.concat(this.tags(body, node));
                    }
                }
                else if (Array.isArray(node)) {
                    containers = containers.concat(node);
                }
                else if (node instanceof this.window.NodeList || node instanceof this.window.HTMLCollection) {
                    containers = containers.concat(node.nodes);
                }
                else {
                    containers.push(node);
                }
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (nodes_1_1 && !nodes_1_1.done && (_a = nodes_1.return)) _a.call(nodes_1);
            }
            finally { if (e_1) throw e_1.error; }
        }
        return containers;
    };
    LiteBase.prototype.contains = function (container, node) {
        while (node && node !== container) {
            node = this.parent(node);
        }
        return !!node;
    };
    LiteBase.prototype.parent = function (node) {
        return node.parent;
    };
    LiteBase.prototype.childIndex = function (node) {
        return (node.parent ? node.parent.children.findIndex(function (n) { return n === node; }) : -1);
    };
    LiteBase.prototype.append = function (node, child) {
        if (child.parent) {
            this.remove(child);
        }
        node.children.push(child);
        child.parent = node;
        return child;
    };
    LiteBase.prototype.insert = function (nchild, ochild) {
        if (nchild.parent) {
            this.remove(nchild);
        }
        if (ochild && ochild.parent) {
            var i = this.childIndex(ochild);
            ochild.parent.children.splice(i, 0, nchild);
            nchild.parent = ochild.parent;
        }
    };
    LiteBase.prototype.remove = function (child) {
        var i = this.childIndex(child);
        if (i >= 0) {
            child.parent.children.splice(i, 1);
        }
        child.parent = null;
        return child;
    };
    LiteBase.prototype.replace = function (nnode, onode) {
        var i = this.childIndex(onode);
        if (i >= 0) {
            onode.parent.children[i] = nnode;
            nnode.parent = onode.parent;
            onode.parent = null;
        }
        return onode;
    };
    LiteBase.prototype.clone = function (node) {
        var _this = this;
        var nnode = new Element_js_1.LiteElement(node.kind);
        nnode.attributes = __assign({}, node.attributes);
        nnode.children = node.children.map(function (n) {
            if (n.kind === '#text') {
                return new Text_js_1.LiteText(n.value);
            }
            else if (n.kind === '#comment') {
                return new Text_js_1.LiteComment(n.value);
            }
            else {
                var m = _this.clone(n);
                m.parent = nnode;
                return m;
            }
        });
        return nnode;
    };
    LiteBase.prototype.split = function (node, n) {
        var text = new Text_js_1.LiteText(node.value.slice(n));
        node.value = node.value.slice(0, n);
        node.parent.children.splice(this.childIndex(node) + 1, 0, text);
        text.parent = node.parent;
        return text;
    };
    LiteBase.prototype.next = function (node) {
        var parent = node.parent;
        if (!parent)
            return null;
        var i = this.childIndex(node) + 1;
        return (i >= 0 && i < parent.children.length ? parent.children[i] : null);
    };
    LiteBase.prototype.previous = function (node) {
        var parent = node.parent;
        if (!parent)
            return null;
        var i = this.childIndex(node) - 1;
        return (i >= 0 ? parent.children[i] : null);
    };
    LiteBase.prototype.firstChild = function (node) {
        return node.children[0];
    };
    LiteBase.prototype.lastChild = function (node) {
        return node.children[node.children.length - 1];
    };
    LiteBase.prototype.childNodes = function (node) {
        return __spreadArray([], __read(node.children), false);
    };
    LiteBase.prototype.childNode = function (node, i) {
        return node.children[i];
    };
    LiteBase.prototype.kind = function (node) {
        return node.kind;
    };
    LiteBase.prototype.value = function (node) {
        return (node.kind === '#text' ? node.value :
            node.kind === '#comment' ? node.value.replace(/^<!(--)?((?:.|\n)*)\1>$/, '$2') : '');
    };
    LiteBase.prototype.textContent = function (node) {
        var _this = this;
        return node.children.reduce(function (s, n) {
            return s + (n.kind === '#text' ? n.value :
                n.kind === '#comment' ? '' : _this.textContent(n));
        }, '');
    };
    LiteBase.prototype.innerHTML = function (node) {
        return this.parser.serializeInner(this, node);
    };
    LiteBase.prototype.outerHTML = function (node) {
        return this.parser.serialize(this, node);
    };
    LiteBase.prototype.serializeXML = function (node) {
        return this.parser.serialize(this, node, true);
    };
    LiteBase.prototype.setAttribute = function (node, name, value, ns) {
        if (ns === void 0) { ns = null; }
        if (typeof value !== 'string') {
            value = String(value);
        }
        if (ns) {
            name = ns.replace(/.*\//, '') + ':' + name.replace(/^.*:/, '');
        }
        node.attributes[name] = value;
        if (name === 'style') {
            node.styles = null;
        }
    };
    LiteBase.prototype.getAttribute = function (node, name) {
        return node.attributes[name];
    };
    LiteBase.prototype.removeAttribute = function (node, name) {
        delete node.attributes[name];
    };
    LiteBase.prototype.hasAttribute = function (node, name) {
        return node.attributes.hasOwnProperty(name);
    };
    LiteBase.prototype.allAttributes = function (node) {
        var e_2, _a;
        var attributes = node.attributes;
        var list = [];
        try {
            for (var _b = __values(Object.keys(attributes)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var name_1 = _c.value;
                list.push({ name: name_1, value: attributes[name_1] });
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_2) throw e_2.error; }
        }
        return list;
    };
    LiteBase.prototype.addClass = function (node, name) {
        var classes = (node.attributes['class'] || '').split(/ /);
        if (!classes.find(function (n) { return n === name; })) {
            classes.push(name);
            node.attributes['class'] = classes.join(' ');
        }
    };
    LiteBase.prototype.removeClass = function (node, name) {
        var classes = (node.attributes['class'] || '').split(/ /);
        var i = classes.findIndex(function (n) { return n === name; });
        if (i >= 0) {
            classes.splice(i, 1);
            node.attributes['class'] = classes.join(' ');
        }
    };
    LiteBase.prototype.hasClass = function (node, name) {
        var classes = (node.attributes['class'] || '').split(/ /);
        return !!classes.find(function (n) { return n === name; });
    };
    LiteBase.prototype.setStyle = function (node, name, value) {
        if (!node.styles) {
            node.styles = new Styles_js_1.Styles(this.getAttribute(node, 'style'));
        }
        node.styles.set(name, value);
        node.attributes['style'] = node.styles.cssText;
    };
    LiteBase.prototype.getStyle = function (node, name) {
        if (!node.styles) {
            var style = this.getAttribute(node, 'style');
            if (!style) {
                return '';
            }
            node.styles = new Styles_js_1.Styles(style);
        }
        return node.styles.get(name);
    };
    LiteBase.prototype.allStyles = function (node) {
        return this.getAttribute(node, 'style');
    };
    LiteBase.prototype.insertRules = function (node, rules) {
        node.children = [this.text(rules.join('\n\n') + '\n\n' + this.textContent(node))];
    };
    LiteBase.prototype.fontSize = function (_node) {
        return 0;
    };
    LiteBase.prototype.fontFamily = function (_node) {
        return '';
    };
    LiteBase.prototype.nodeSize = function (_node, _em, _local) {
        if (_em === void 0) { _em = 1; }
        if (_local === void 0) { _local = null; }
        return [0, 0];
    };
    LiteBase.prototype.nodeBBox = function (_node) {
        return { left: 0, right: 0, top: 0, bottom: 0 };
    };
    return LiteBase;
}(DOMAdaptor_js_1.AbstractDOMAdaptor));
exports.LiteBase = LiteBase;
var LiteAdaptor = (function (_super) {
    __extends(LiteAdaptor, _super);
    function LiteAdaptor() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return LiteAdaptor;
}((0, NodeMixin_js_1.NodeMixin)(LiteBase)));
exports.LiteAdaptor = LiteAdaptor;
function liteAdaptor(options) {
    if (options === void 0) { options = null; }
    return new LiteAdaptor(null, options);
}
exports.liteAdaptor = liteAdaptor;
//# sourceMappingURL=liteAdaptor.js.map

/***/ }),

/***/ 306:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;

__webpack_unused_export__ = ({ value: true });
exports.q = void 0;
exports.q = '3.2.2';
//# sourceMappingURL=version.js.map

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

/***/ 857:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AbstractDOMAdaptor = MathJax._.core.DOMAdaptor.AbstractDOMAdaptor;

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

/***/ }),

/***/ 878:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Styles = MathJax._.util.Styles.Styles;

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
// EXTERNAL MODULE: ../../../../js/adaptors/liteAdaptor.js
var liteAdaptor = __webpack_require__(250);
// EXTERNAL MODULE: ../../../../js/adaptors/lite/Document.js
var Document = __webpack_require__(877);
// EXTERNAL MODULE: ../../../../js/adaptors/lite/Element.js
var Element = __webpack_require__(946);
// EXTERNAL MODULE: ../../../../js/adaptors/lite/List.js
var List = __webpack_require__(6);
// EXTERNAL MODULE: ../../../../js/adaptors/lite/Parser.js
var Parser = __webpack_require__(246);
// EXTERNAL MODULE: ../../../../js/adaptors/lite/Text.js
var Text = __webpack_require__(735);
// EXTERNAL MODULE: ../../../../js/adaptors/lite/Window.js
var Window = __webpack_require__(492);
;// CONCATENATED MODULE: ./lib/liteDOM.js










if (MathJax.loader) {
  MathJax.loader.checkVersion('adaptors/liteDOM', version/* VERSION */.q, 'adaptors');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    adaptors: {
      liteAdaptor: liteAdaptor,
      lite: {
        Document: Document,
        Element: Element,
        List: List,
        Parser: Parser,
        Text: Text,
        Window: Window
      }
    }
  }
});
;// CONCATENATED MODULE: ./liteDOM.js



if (MathJax.startup) {
  MathJax.startup.registerConstructor('liteAdaptor', liteAdaptor.liteAdaptor);
  MathJax.startup.useAdaptor('liteAdaptor', true);
}
}();
/******/ })()
;