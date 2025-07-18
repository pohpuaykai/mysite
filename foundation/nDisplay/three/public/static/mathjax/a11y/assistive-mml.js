/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 62:
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
exports.AssistiveMmlHandler = exports.AssistiveMmlMathDocumentMixin = exports.AssistiveMmlMathItemMixin = exports.LimitedMmlVisitor = void 0;
var MathItem_js_1 = __webpack_require__(769);
var SerializedMmlVisitor_js_1 = __webpack_require__(433);
var Options_js_1 = __webpack_require__(77);
var LimitedMmlVisitor = (function (_super) {
    __extends(LimitedMmlVisitor, _super);
    function LimitedMmlVisitor() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    LimitedMmlVisitor.prototype.getAttributes = function (node) {
        return _super.prototype.getAttributes.call(this, node).replace(/ ?id=".*?"/, '');
    };
    return LimitedMmlVisitor;
}(SerializedMmlVisitor_js_1.SerializedMmlVisitor));
exports.LimitedMmlVisitor = LimitedMmlVisitor;
(0, MathItem_js_1.newState)('ASSISTIVEMML', 153);
function AssistiveMmlMathItemMixin(BaseMathItem) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        class_1.prototype.assistiveMml = function (document, force) {
            if (force === void 0) { force = false; }
            if (this.state() >= MathItem_js_1.STATE.ASSISTIVEMML)
                return;
            if (!this.isEscaped && (document.options.enableAssistiveMml || force)) {
                var adaptor = document.adaptor;
                var mml = document.toMML(this.root).replace(/\n */g, '').replace(/<!--.*?-->/g, '');
                var mmlNodes = adaptor.firstChild(adaptor.body(adaptor.parse(mml, 'text/html')));
                var node = adaptor.node('mjx-assistive-mml', {
                    unselectable: 'on', display: (this.display ? 'block' : 'inline')
                }, [mmlNodes]);
                adaptor.setAttribute(adaptor.firstChild(this.typesetRoot), 'aria-hidden', 'true');
                adaptor.setStyle(this.typesetRoot, 'position', 'relative');
                adaptor.append(this.typesetRoot, node);
            }
            this.state(MathItem_js_1.STATE.ASSISTIVEMML);
        };
        return class_1;
    }(BaseMathItem));
}
exports.AssistiveMmlMathItemMixin = AssistiveMmlMathItemMixin;
function AssistiveMmlMathDocumentMixin(BaseDocument) {
    var _a;
    return _a = (function (_super) {
            __extends(BaseClass, _super);
            function BaseClass() {
                var args = [];
                for (var _i = 0; _i < arguments.length; _i++) {
                    args[_i] = arguments[_i];
                }
                var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
                var CLASS = _this.constructor;
                var ProcessBits = CLASS.ProcessBits;
                if (!ProcessBits.has('assistive-mml')) {
                    ProcessBits.allocate('assistive-mml');
                }
                _this.visitor = new LimitedMmlVisitor(_this.mmlFactory);
                _this.options.MathItem =
                    AssistiveMmlMathItemMixin(_this.options.MathItem);
                if ('addStyles' in _this) {
                    _this.addStyles(CLASS.assistiveStyles);
                }
                return _this;
            }
            BaseClass.prototype.toMML = function (node) {
                return this.visitor.visitTree(node);
            };
            BaseClass.prototype.assistiveMml = function () {
                var e_1, _a;
                if (!this.processed.isSet('assistive-mml')) {
                    try {
                        for (var _b = __values(this.math), _c = _b.next(); !_c.done; _c = _b.next()) {
                            var math = _c.value;
                            math.assistiveMml(this);
                        }
                    }
                    catch (e_1_1) { e_1 = { error: e_1_1 }; }
                    finally {
                        try {
                            if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
                        }
                        finally { if (e_1) throw e_1.error; }
                    }
                    this.processed.set('assistive-mml');
                }
                return this;
            };
            BaseClass.prototype.state = function (state, restore) {
                if (restore === void 0) { restore = false; }
                _super.prototype.state.call(this, state, restore);
                if (state < MathItem_js_1.STATE.ASSISTIVEMML) {
                    this.processed.clear('assistive-mml');
                }
                return this;
            };
            return BaseClass;
        }(BaseDocument)),
        _a.OPTIONS = __assign(__assign({}, BaseDocument.OPTIONS), { enableAssistiveMml: true, renderActions: (0, Options_js_1.expandable)(__assign(__assign({}, BaseDocument.OPTIONS.renderActions), { assistiveMml: [MathItem_js_1.STATE.ASSISTIVEMML] })) }),
        _a.assistiveStyles = {
            'mjx-assistive-mml': {
                position: 'absolute !important',
                top: '0px', left: '0px',
                clip: 'rect(1px, 1px, 1px, 1px)',
                padding: '1px 0px 0px 0px !important',
                border: '0px !important',
                display: 'block !important',
                width: 'auto !important',
                overflow: 'hidden !important',
                '-webkit-touch-callout': 'none',
                '-webkit-user-select': 'none',
                '-khtml-user-select': 'none',
                '-moz-user-select': 'none',
                '-ms-user-select': 'none',
                'user-select': 'none'
            },
            'mjx-assistive-mml[display="block"]': {
                width: '100% !important'
            }
        },
        _a;
}
exports.AssistiveMmlMathDocumentMixin = AssistiveMmlMathDocumentMixin;
function AssistiveMmlHandler(handler) {
    handler.documentClass =
        AssistiveMmlMathDocumentMixin(handler.documentClass);
    return handler;
}
exports.AssistiveMmlHandler = AssistiveMmlHandler;
//# sourceMappingURL=assistive-mml.js.map

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

/***/ 433:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.DATAMJX = MathJax._.core.MmlTree.SerializedMmlVisitor.DATAMJX;
exports.toEntity = MathJax._.core.MmlTree.SerializedMmlVisitor.toEntity;
exports.SerializedMmlVisitor = MathJax._.core.MmlTree.SerializedMmlVisitor.SerializedMmlVisitor;

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
// EXTERNAL MODULE: ../../../../js/a11y/assistive-mml.js
var assistive_mml = __webpack_require__(62);
;// CONCATENATED MODULE: ./lib/assistive-mml.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('a11y/assistive-mml', version/* VERSION */.q, 'a11y');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    a11y: {
      "assistive-mml": assistive_mml
    }
  }
});
;// CONCATENATED MODULE: ./assistive-mml.js



if (MathJax.startup) {
  MathJax.startup.extendHandler(function (handler) {
    return (0,assistive_mml.AssistiveMmlHandler)(handler);
  });
}
}();
/******/ })()
;