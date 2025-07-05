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

/***/ 63:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SafeHandler = exports.SafeMathDocumentMixin = void 0;
var safe_js_1 = __webpack_require__(477);
function SafeMathDocumentMixin(BaseDocument) {
    var _a;
    return _a = (function (_super) {
            __extends(class_1, _super);
            function class_1() {
                var e_1, _a;
                var args = [];
                for (var _i = 0; _i < arguments.length; _i++) {
                    args[_i] = arguments[_i];
                }
                var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
                _this.safe = new _this.options.SafeClass(_this, _this.options.safeOptions);
                var ProcessBits = _this.constructor.ProcessBits;
                if (!ProcessBits.has('safe')) {
                    ProcessBits.allocate('safe');
                }
                try {
                    for (var _b = __values(_this.inputJax), _c = _b.next(); !_c.done; _c = _b.next()) {
                        var jax = _c.value;
                        if (jax.name.match(/MathML/)) {
                            jax.mathml.filterAttribute = _this.safe.mmlAttribute.bind(_this.safe);
                            jax.mathml.filterClassList = _this.safe.mmlClassList.bind(_this.safe);
                        }
                        else if (jax.name.match(/TeX/)) {
                            jax.postFilters.add(_this.sanitize.bind(jax), -5.5);
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
            class_1.prototype.sanitize = function (data) {
                data.math.root = this.parseOptions.root;
                data.document.safe.sanitize(data.math, data.document);
            };
            return class_1;
        }(BaseDocument)),
        _a.OPTIONS = __assign(__assign({}, BaseDocument.OPTIONS), { safeOptions: __assign({}, safe_js_1.Safe.OPTIONS), SafeClass: safe_js_1.Safe }),
        _a;
}
exports.SafeMathDocumentMixin = SafeMathDocumentMixin;
function SafeHandler(handler) {
    handler.documentClass = SafeMathDocumentMixin(handler.documentClass);
    return handler;
}
exports.SafeHandler = SafeHandler;
//# sourceMappingURL=SafeHandler.js.map

/***/ }),

/***/ 509:
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
exports.SafeMethods = void 0;
var lengths_js_1 = __webpack_require__(914);
exports.SafeMethods = {
    filterURL: function (safe, url) {
        var protocol = (url.match(/^\s*([a-z]+):/i) || [null, ''])[1].toLowerCase();
        var allow = safe.allow.URLs;
        return (allow === 'all' || (allow === 'safe' &&
            (safe.options.safeProtocols[protocol] || !protocol))) ? url : null;
    },
    filterClassList: function (safe, list) {
        var _this = this;
        var classes = list.trim().replace(/\s\s+/g, ' ').split(/ /);
        return classes.map(function (name) { return _this.filterClass(safe, name) || ''; }).join(' ').trim().replace(/\s\s+/g, '');
    },
    filterClass: function (safe, CLASS) {
        var allow = safe.allow.classes;
        return (allow === 'all' || (allow === 'safe' && CLASS.match(safe.options.classPattern))) ? CLASS : null;
    },
    filterID: function (safe, id) {
        var allow = safe.allow.cssIDs;
        return (allow === 'all' || (allow === 'safe' && id.match(safe.options.idPattern))) ? id : null;
    },
    filterStyles: function (safe, styles) {
        var e_1, _a, e_2, _b;
        if (safe.allow.styles === 'all')
            return styles;
        if (safe.allow.styles !== 'safe')
            return null;
        var adaptor = safe.adaptor;
        var options = safe.options;
        try {
            var div1 = adaptor.node('div', { style: styles });
            var div2 = adaptor.node('div');
            try {
                for (var _c = __values(Object.keys(options.safeStyles)), _d = _c.next(); !_d.done; _d = _c.next()) {
                    var style = _d.value;
                    if (options.styleParts[style]) {
                        try {
                            for (var _e = (e_2 = void 0, __values(['Top', 'Right', 'Bottom', 'Left'])), _f = _e.next(); !_f.done; _f = _e.next()) {
                                var sufix = _f.value;
                                var name_1 = style + sufix;
                                var value = this.filterStyle(safe, name_1, div1);
                                if (value) {
                                    adaptor.setStyle(div2, name_1, value);
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
                    else {
                        var value = this.filterStyle(safe, style, div1);
                        if (value) {
                            adaptor.setStyle(div2, style, value);
                        }
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
            styles = adaptor.allStyles(div2);
        }
        catch (err) {
            styles = '';
        }
        return styles;
    },
    filterStyle: function (safe, style, div) {
        var value = safe.adaptor.getStyle(div, style);
        if (typeof value !== 'string' || value === '' || value.match(/^\s*calc/) ||
            (value.match(/javascript:/) && !safe.options.safeProtocols.javascript) ||
            (value.match(/data:/) && !safe.options.safeProtocols.data)) {
            return null;
        }
        var name = style.replace(/Top|Right|Left|Bottom/, '');
        if (!safe.options.safeStyles[style] && !safe.options.safeStyles[name]) {
            return null;
        }
        return this.filterStyleValue(safe, style, value, div);
    },
    filterStyleValue: function (safe, style, value, div) {
        var name = safe.options.styleLengths[style];
        if (!name) {
            return value;
        }
        if (typeof name !== 'string') {
            return this.filterStyleLength(safe, style, value);
        }
        var length = this.filterStyleLength(safe, name, safe.adaptor.getStyle(div, name));
        if (!length) {
            return null;
        }
        safe.adaptor.setStyle(div, name, length);
        return safe.adaptor.getStyle(div, style);
    },
    filterStyleLength: function (safe, style, value) {
        if (!value.match(/^(.+)(em|ex|ch|rem|px|mm|cm|in|pt|pc|%)$/))
            return null;
        var em = (0, lengths_js_1.length2em)(value, 1);
        var lengths = safe.options.styleLengths[style];
        var _a = __read((Array.isArray(lengths) ? lengths : [-safe.options.lengthMax, safe.options.lengthMax]), 2), m = _a[0], M = _a[1];
        return (m <= em && em <= M ? value : (em < m ? m : M).toFixed(3).replace(/\.?0+$/, '') + 'em');
    },
    filterFontSize: function (safe, size) {
        return this.filterStyleLength(safe, 'fontSize', size);
    },
    filterSizeMultiplier: function (safe, size) {
        var _a = __read(safe.options.scriptsizemultiplierRange || [-Infinity, Infinity], 2), m = _a[0], M = _a[1];
        return Math.min(M, Math.max(m, parseFloat(size))).toString();
    },
    filterScriptLevel: function (safe, level) {
        var _a = __read(safe.options.scriptlevelRange || [-Infinity, Infinity], 2), m = _a[0], M = _a[1];
        return Math.min(M, Math.max(m, parseInt(level))).toString();
    },
    filterData: function (safe, value, id) {
        return (id.match(safe.options.dataPattern) ? value : null);
    }
};
//# sourceMappingURL=SafeMethods.js.map

/***/ }),

/***/ 477:
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
exports.Safe = void 0;
var Options_js_1 = __webpack_require__(77);
var SafeMethods_js_1 = __webpack_require__(509);
var Safe = (function () {
    function Safe(document, options) {
        this.filterAttributes = new Map([
            ['href', 'filterURL'],
            ['src', 'filterURL'],
            ['altimg', 'filterURL'],
            ['class', 'filterClassList'],
            ['style', 'filterStyles'],
            ['id', 'filterID'],
            ['fontsize', 'filterFontSize'],
            ['mathsize', 'filterFontSize'],
            ['scriptminsize', 'filterFontSize'],
            ['scriptsizemultiplier', 'filterSizeMultiplier'],
            ['scriptlevel', 'filterScriptLevel'],
            ['data-', 'filterData']
        ]);
        this.filterMethods = __assign({}, SafeMethods_js_1.SafeMethods);
        this.adaptor = document.adaptor;
        this.options = options;
        this.allow = this.options.allow;
    }
    Safe.prototype.sanitize = function (math, document) {
        try {
            math.root.walkTree(this.sanitizeNode.bind(this));
        }
        catch (err) {
            document.options.compileError(document, math, err);
        }
    };
    Safe.prototype.sanitizeNode = function (node) {
        var e_1, _a;
        var attributes = node.attributes.getAllAttributes();
        try {
            for (var _b = __values(Object.keys(attributes)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var id = _c.value;
                var method = this.filterAttributes.get(id);
                if (method) {
                    var value = this.filterMethods[method](this, attributes[id]);
                    if (value) {
                        if (value !== (typeof value === 'number' ? parseFloat(attributes[id]) : attributes[id])) {
                            attributes[id] = value;
                        }
                    }
                    else {
                        delete attributes[id];
                    }
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
    Safe.prototype.mmlAttribute = function (id, value) {
        if (id === 'class')
            return null;
        var method = this.filterAttributes.get(id);
        var filter = (method || (id.substr(0, 5) === 'data-' ? this.filterAttributes.get('data-') : null));
        if (!filter) {
            return value;
        }
        var result = this.filterMethods[filter](this, value, id);
        return (typeof result === 'number' || typeof result === 'boolean' ? String(result) : result);
    };
    Safe.prototype.mmlClassList = function (list) {
        var _this = this;
        return list.map(function (name) { return _this.filterMethods.filterClass(_this, name); })
            .filter(function (value) { return value !== null; });
    };
    Safe.OPTIONS = {
        allow: {
            URLs: 'safe',
            classes: 'safe',
            cssIDs: 'safe',
            styles: 'safe'
        },
        lengthMax: 3,
        scriptsizemultiplierRange: [.6, 1],
        scriptlevelRange: [-2, 2],
        classPattern: /^mjx-[-a-zA-Z0-9_.]+$/,
        idPattern: /^mjx-[-a-zA-Z0-9_.]+$/,
        dataPattern: /^data-mjx-/,
        safeProtocols: (0, Options_js_1.expandable)({
            http: true,
            https: true,
            file: true,
            javascript: false,
            data: false
        }),
        safeStyles: (0, Options_js_1.expandable)({
            color: true,
            backgroundColor: true,
            border: true,
            cursor: true,
            margin: true,
            padding: true,
            textShadow: true,
            fontFamily: true,
            fontSize: true,
            fontStyle: true,
            fontWeight: true,
            opacity: true,
            outline: true
        }),
        styleParts: (0, Options_js_1.expandable)({
            border: true,
            padding: true,
            margin: true,
            outline: true
        }),
        styleLengths: (0, Options_js_1.expandable)({
            borderTop: 'borderTopWidth',
            borderRight: 'borderRightWidth',
            borderBottom: 'borderBottomWidth',
            borderLeft: 'borderLeftWidth',
            paddingTop: true,
            paddingRight: true,
            paddingBottom: true,
            paddingLeft: true,
            marginTop: true,
            marginRight: true,
            marginBottom: true,
            marginLeft: true,
            outlineTop: true,
            outlineRight: true,
            outlineBottom: true,
            outlineLeft: true,
            fontSize: [.707, 1.44]
        })
    };
    return Safe;
}());
exports.Safe = Safe;
//# sourceMappingURL=safe.js.map

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

/***/ 914:
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
// EXTERNAL MODULE: ../../../../js/ui/safe/SafeHandler.js
var SafeHandler = __webpack_require__(63);
// EXTERNAL MODULE: ../../../../js/ui/safe/SafeMethods.js
var SafeMethods = __webpack_require__(509);
// EXTERNAL MODULE: ../../../../js/ui/safe/safe.js
var safe = __webpack_require__(477);
;// CONCATENATED MODULE: ./lib/safe.js






if (MathJax.loader) {
  MathJax.loader.checkVersion('ui/safe', version/* VERSION */.q, 'ui');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    ui: {
      safe: {
        SafeHandler: SafeHandler,
        SafeMethods: SafeMethods,
        safe: safe
      }
    }
  }
});
;// CONCATENATED MODULE: ./safe.js



if (MathJax.startup && typeof window !== 'undefined') {
  MathJax.startup.extendHandler(function (handler) {
    return (0,SafeHandler.SafeHandler)(handler);
  });
}
}();
/******/ })()
;