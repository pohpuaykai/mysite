/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 433:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.EnrichHandler = exports.EnrichedMathDocumentMixin = exports.EnrichedMathItemMixin = void 0;
var mathjax_js_1 = __webpack_require__(184);
var MathItem_js_1 = __webpack_require__(769);
var SerializedMmlVisitor_js_1 = __webpack_require__(758);
var Options_js_1 = __webpack_require__(77);
var sre_js_1 = __importDefault(__webpack_require__(712));
var currentSpeech = 'none';
(0, MathItem_js_1.newState)('ENRICHED', 30);
(0, MathItem_js_1.newState)('ATTACHSPEECH', 155);
function EnrichedMathItemMixin(BaseMathItem, MmlJax, toMathML) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.serializeMml = function (node) {
            if ('outerHTML' in node) {
                return node.outerHTML;
            }
            if (typeof Element !== 'undefined' && typeof window !== 'undefined' && node instanceof Element) {
                var div = window.document.createElement('div');
                div.appendChild(node);
                return div.innerHTML;
            }
            return node.toString();
        };
        class_1.prototype.enrich = function (document, force) {
            if (force === void 0) { force = false; }
            if (this.state() >= MathItem_js_1.STATE.ENRICHED)
                return;
            if (!this.isEscaped && (document.options.enableEnrichment || force)) {
                if (document.options.sre.speech !== currentSpeech) {
                    currentSpeech = document.options.sre.speech;
                    mathjax_js_1.mathjax.retryAfter(sre_js_1.default.setupEngine(document.options.sre).then(function () { return sre_js_1.default.sreReady(); }));
                }
                var math = new document.options.MathItem('', MmlJax);
                try {
                    var mml = this.inputData.originalMml = toMathML(this.root);
                    math.math = this.serializeMml(sre_js_1.default.toEnriched(mml));
                    math.display = this.display;
                    math.compile(document);
                    this.root = math.root;
                    this.inputData.enrichedMml = math.math;
                }
                catch (err) {
                    document.options.enrichError(document, this, err);
                }
            }
            this.state(MathItem_js_1.STATE.ENRICHED);
        };
        class_1.prototype.attachSpeech = function (document) {
            var e_1, _a;
            if (this.state() >= MathItem_js_1.STATE.ATTACHSPEECH)
                return;
            var attributes = this.root.attributes;
            var speech = (attributes.get('aria-label') ||
                this.getSpeech(this.root));
            if (speech) {
                var adaptor = document.adaptor;
                var node = this.typesetRoot;
                adaptor.setAttribute(node, 'aria-label', speech);
                try {
                    for (var _b = __values(adaptor.childNodes(node)), _c = _b.next(); !_c.done; _c = _b.next()) {
                        var child = _c.value;
                        adaptor.setAttribute(child, 'aria-hidden', 'true');
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
            this.state(MathItem_js_1.STATE.ATTACHSPEECH);
        };
        class_1.prototype.getSpeech = function (node) {
            var e_2, _a;
            var attributes = node.attributes;
            if (!attributes)
                return '';
            var speech = attributes.getExplicit('data-semantic-speech');
            if (!attributes.getExplicit('data-semantic-parent') && speech) {
                return speech;
            }
            try {
                for (var _b = __values(node.childNodes), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var child = _c.value;
                    var value = this.getSpeech(child);
                    if (value != null) {
                        return value;
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
            return '';
        };
        return class_1;
    }(BaseMathItem));
}
exports.EnrichedMathItemMixin = EnrichedMathItemMixin;
function EnrichedMathDocumentMixin(BaseDocument, MmlJax) {
    var _a;
    return _a = (function (_super) {
            __extends(class_2, _super);
            function class_2() {
                var args = [];
                for (var _i = 0; _i < arguments.length; _i++) {
                    args[_i] = arguments[_i];
                }
                var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
                MmlJax.setMmlFactory(_this.mmlFactory);
                var ProcessBits = _this.constructor.ProcessBits;
                if (!ProcessBits.has('enriched')) {
                    ProcessBits.allocate('enriched');
                    ProcessBits.allocate('attach-speech');
                }
                var visitor = new SerializedMmlVisitor_js_1.SerializedMmlVisitor(_this.mmlFactory);
                var toMathML = (function (node) { return visitor.visitTree(node); });
                _this.options.MathItem =
                    EnrichedMathItemMixin(_this.options.MathItem, MmlJax, toMathML);
                return _this;
            }
            class_2.prototype.attachSpeech = function () {
                var e_3, _a;
                if (!this.processed.isSet('attach-speech')) {
                    try {
                        for (var _b = __values(this.math), _c = _b.next(); !_c.done; _c = _b.next()) {
                            var math = _c.value;
                            math.attachSpeech(this);
                        }
                    }
                    catch (e_3_1) { e_3 = { error: e_3_1 }; }
                    finally {
                        try {
                            if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
                        }
                        finally { if (e_3) throw e_3.error; }
                    }
                    this.processed.set('attach-speech');
                }
                return this;
            };
            class_2.prototype.enrich = function () {
                var e_4, _a;
                if (!this.processed.isSet('enriched')) {
                    if (this.options.enableEnrichment) {
                        try {
                            for (var _b = __values(this.math), _c = _b.next(); !_c.done; _c = _b.next()) {
                                var math = _c.value;
                                math.enrich(this);
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
                    this.processed.set('enriched');
                }
                return this;
            };
            class_2.prototype.enrichError = function (_doc, _math, err) {
                console.warn('Enrichment error:', err);
            };
            class_2.prototype.state = function (state, restore) {
                if (restore === void 0) { restore = false; }
                _super.prototype.state.call(this, state, restore);
                if (state < MathItem_js_1.STATE.ENRICHED) {
                    this.processed.clear('enriched');
                }
                return this;
            };
            return class_2;
        }(BaseDocument)),
        _a.OPTIONS = __assign(__assign({}, BaseDocument.OPTIONS), { enableEnrichment: true, enrichError: function (doc, math, err) { return doc.enrichError(doc, math, err); }, renderActions: (0, Options_js_1.expandable)(__assign(__assign({}, BaseDocument.OPTIONS.renderActions), { enrich: [MathItem_js_1.STATE.ENRICHED], attachSpeech: [MathItem_js_1.STATE.ATTACHSPEECH] })), sre: (0, Options_js_1.expandable)({
                speech: 'none',
                domain: 'mathspeak',
                style: 'default',
                locale: 'en'
            }) }),
        _a;
}
exports.EnrichedMathDocumentMixin = EnrichedMathDocumentMixin;
function EnrichHandler(handler, MmlJax) {
    MmlJax.setAdaptor(handler.adaptor);
    handler.documentClass =
        EnrichedMathDocumentMixin(handler.documentClass, MmlJax);
    return handler;
}
exports.EnrichHandler = EnrichHandler;
//# sourceMappingURL=semantic-enrich.js.map

/***/ }),

/***/ 306:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;

__webpack_unused_export__ = ({ value: true });
exports.q = void 0;
exports.q = '3.2.2';
//# sourceMappingURL=version.js.map

/***/ }),

/***/ 712:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Sre = MathJax._.a11y.sre.Sre;
exports.sreReady = MathJax._.a11y.sre.sreReady;
exports["default"] = MathJax._.a11y.sre["default"];

/***/ }),

/***/ 723:
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

/***/ 769:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.protoItem = MathJax._.core.MathItem.protoItem;
exports.AbstractMathItem = MathJax._.core.MathItem.AbstractMathItem;
exports.STATE = MathJax._.core.MathItem.STATE;
exports.newState = MathJax._.core.MathItem.newState;

/***/ }),

/***/ 758:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.DATAMJX = MathJax._.core.MmlTree.SerializedMmlVisitor.DATAMJX;
exports.toEntity = MathJax._.core.MmlTree.SerializedMmlVisitor.toEntity;
exports.SerializedMmlVisitor = MathJax._.core.MmlTree.SerializedMmlVisitor.SerializedMmlVisitor;

/***/ }),

/***/ 184:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.mathjax = MathJax._.mathjax.mathjax;

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

/***/ 475:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;


__webpack_unused_export__ = ({
  value: true
});
exports.K = MathJax._.input.mathml_ts.MathML;

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
// EXTERNAL MODULE: ../../../../js/a11y/semantic-enrich.js
var semantic_enrich = __webpack_require__(433);
;// CONCATENATED MODULE: ./lib/semantic-enrich.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('a11y/semantic-enrich', version/* VERSION */.q, 'a11y');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    a11y: {
      "semantic-enrich": semantic_enrich
    }
  }
});
// EXTERNAL MODULE: ../sre/lib/a11y/sre.js
var sre = __webpack_require__(712);
// EXTERNAL MODULE: ../../input/mml/lib/input/mathml.js
var mathml = __webpack_require__(475);
;// CONCATENATED MODULE: ./semantic-enrich.js






if (MathJax.loader) {
  (0,global/* combineDefaults */.PV)(MathJax.config.loader, 'a11y/semantic-enrich', {
    checkReady: function checkReady() {
      return sre["default"].sreReady();
    }
  });
}

if (MathJax.startup) {
  MathJax.startup.extendHandler(function (handler) {
    return (0,semantic_enrich.EnrichHandler)(handler, new mathml/* MathML */.K());
  });
}
}();
/******/ })()
;