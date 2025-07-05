/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 18:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.setA11yOption = exports.setA11yOptions = exports.ExplorerHandler = exports.ExplorerMathDocumentMixin = exports.ExplorerMathItemMixin = void 0;
var MathItem_js_1 = __webpack_require__(769);
var semantic_enrich_js_1 = __webpack_require__(511);
var Options_js_1 = __webpack_require__(77);
var SerializedMmlVisitor_js_1 = __webpack_require__(433);
var MJContextMenu_js_1 = __webpack_require__(850);
var ke = __importStar(__webpack_require__(269));
var me = __importStar(__webpack_require__(85));
var TreeExplorer_js_1 = __webpack_require__(854);
var Region_js_1 = __webpack_require__(367);
var sre_js_1 = __importDefault(__webpack_require__(712));
(0, MathItem_js_1.newState)('EXPLORER', 160);
function ExplorerMathItemMixin(BaseMathItem, toMathML) {
    return (function (_super) {
        __extends(class_1, _super);
        function class_1() {
            var _this = _super !== null && _super.apply(this, arguments) || this;
            _this.explorers = {};
            _this.attached = [];
            _this.restart = [];
            _this.refocus = false;
            _this.savedId = null;
            return _this;
        }
        class_1.prototype.explorable = function (document, force) {
            if (force === void 0) { force = false; }
            if (this.state() >= MathItem_js_1.STATE.EXPLORER)
                return;
            if (!this.isEscaped && (document.options.enableExplorer || force)) {
                var node = this.typesetRoot;
                var mml = toMathML(this.root);
                if (this.savedId) {
                    this.typesetRoot.setAttribute('sre-explorer-id', this.savedId);
                    this.savedId = null;
                }
                this.explorers = initExplorers(document, node, mml);
                this.attachExplorers(document);
            }
            this.state(MathItem_js_1.STATE.EXPLORER);
        };
        class_1.prototype.attachExplorers = function (document) {
            var e_1, _a, e_2, _b;
            this.attached = [];
            var keyExplorers = [];
            try {
                for (var _c = __values(Object.keys(this.explorers)), _d = _c.next(); !_d.done; _d = _c.next()) {
                    var key = _d.value;
                    var explorer = this.explorers[key];
                    if (explorer instanceof ke.AbstractKeyExplorer) {
                        explorer.AddEvents();
                        explorer.stoppable = false;
                        keyExplorers.unshift(explorer);
                    }
                    if (document.options.a11y[key]) {
                        explorer.Attach();
                        this.attached.push(key);
                    }
                    else {
                        explorer.Detach();
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
            try {
                for (var keyExplorers_1 = __values(keyExplorers), keyExplorers_1_1 = keyExplorers_1.next(); !keyExplorers_1_1.done; keyExplorers_1_1 = keyExplorers_1.next()) {
                    var explorer = keyExplorers_1_1.value;
                    if (explorer.attached) {
                        explorer.stoppable = true;
                        break;
                    }
                }
            }
            catch (e_2_1) { e_2 = { error: e_2_1 }; }
            finally {
                try {
                    if (keyExplorers_1_1 && !keyExplorers_1_1.done && (_b = keyExplorers_1.return)) _b.call(keyExplorers_1);
                }
                finally { if (e_2) throw e_2.error; }
            }
        };
        class_1.prototype.rerender = function (document, start) {
            var e_3, _a;
            if (start === void 0) { start = MathItem_js_1.STATE.RERENDER; }
            this.savedId = this.typesetRoot.getAttribute('sre-explorer-id');
            this.refocus = (window.document.activeElement === this.typesetRoot);
            try {
                for (var _b = __values(this.attached), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var key = _c.value;
                    var explorer = this.explorers[key];
                    if (explorer.active) {
                        this.restart.push(key);
                        explorer.Stop();
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
            _super.prototype.rerender.call(this, document, start);
        };
        class_1.prototype.updateDocument = function (document) {
            var _this = this;
            _super.prototype.updateDocument.call(this, document);
            this.refocus && this.typesetRoot.focus();
            this.restart.forEach(function (x) { return _this.explorers[x].Start(); });
            this.restart = [];
            this.refocus = false;
        };
        return class_1;
    }(BaseMathItem));
}
exports.ExplorerMathItemMixin = ExplorerMathItemMixin;
function ExplorerMathDocumentMixin(BaseDocument) {
    var _a;
    return _a = (function (_super) {
            __extends(class_2, _super);
            function class_2() {
                var args = [];
                for (var _i = 0; _i < arguments.length; _i++) {
                    args[_i] = arguments[_i];
                }
                var _this = _super.apply(this, __spreadArray([], __read(args), false)) || this;
                var ProcessBits = _this.constructor.ProcessBits;
                if (!ProcessBits.has('explorer')) {
                    ProcessBits.allocate('explorer');
                }
                var visitor = new SerializedMmlVisitor_js_1.SerializedMmlVisitor(_this.mmlFactory);
                var toMathML = (function (node) { return visitor.visitTree(node); });
                _this.options.MathItem = ExplorerMathItemMixin(_this.options.MathItem, toMathML);
                _this.explorerRegions = initExplorerRegions(_this);
                return _this;
            }
            class_2.prototype.explorable = function () {
                var e_4, _a;
                if (!this.processed.isSet('explorer')) {
                    if (this.options.enableExplorer) {
                        try {
                            for (var _b = __values(this.math), _c = _b.next(); !_c.done; _c = _b.next()) {
                                var math = _c.value;
                                math.explorable(this);
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
                    this.processed.set('explorer');
                }
                return this;
            };
            class_2.prototype.state = function (state, restore) {
                if (restore === void 0) { restore = false; }
                _super.prototype.state.call(this, state, restore);
                if (state < MathItem_js_1.STATE.EXPLORER) {
                    this.processed.clear('explorer');
                }
                return this;
            };
            return class_2;
        }(BaseDocument)),
        _a.OPTIONS = __assign(__assign({}, BaseDocument.OPTIONS), { enableExplorer: true, renderActions: (0, Options_js_1.expandable)(__assign(__assign({}, BaseDocument.OPTIONS.renderActions), { explorable: [MathItem_js_1.STATE.EXPLORER] })), sre: (0, Options_js_1.expandable)(__assign(__assign({}, BaseDocument.OPTIONS.sre), { speech: 'shallow' })), a11y: {
                align: 'top',
                backgroundColor: 'Blue',
                backgroundOpacity: 20,
                braille: false,
                flame: false,
                foregroundColor: 'Black',
                foregroundOpacity: 100,
                highlight: 'None',
                hover: false,
                infoPrefix: false,
                infoRole: false,
                infoType: false,
                keyMagnifier: false,
                magnification: 'None',
                magnify: '400%',
                mouseMagnifier: false,
                speech: true,
                subtitles: true,
                treeColoring: false,
                viewBraille: false
            } }),
        _a;
}
exports.ExplorerMathDocumentMixin = ExplorerMathDocumentMixin;
function ExplorerHandler(handler, MmlJax) {
    if (MmlJax === void 0) { MmlJax = null; }
    if (!handler.documentClass.prototype.enrich && MmlJax) {
        handler = (0, semantic_enrich_js_1.EnrichHandler)(handler, MmlJax);
    }
    handler.documentClass = ExplorerMathDocumentMixin(handler.documentClass);
    return handler;
}
exports.ExplorerHandler = ExplorerHandler;
function initExplorerRegions(document) {
    return {
        speechRegion: new Region_js_1.LiveRegion(document),
        brailleRegion: new Region_js_1.LiveRegion(document),
        magnifier: new Region_js_1.HoverRegion(document),
        tooltip1: new Region_js_1.ToolTip(document),
        tooltip2: new Region_js_1.ToolTip(document),
        tooltip3: new Region_js_1.ToolTip(document)
    };
}
var allExplorers = {
    speech: function (doc, node) {
        var _a;
        var rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            rest[_i - 2] = arguments[_i];
        }
        var explorer = (_a = ke.SpeechExplorer).create.apply(_a, __spreadArray([doc, doc.explorerRegions.speechRegion, node], __read(rest), false));
        explorer.speechGenerator.setOptions({
            locale: doc.options.sre.locale, domain: doc.options.sre.domain,
            style: doc.options.sre.style, modality: 'speech'
        });
        var locale = explorer.speechGenerator.getOptions().locale;
        if (locale !== sre_js_1.default.engineSetup().locale) {
            doc.options.sre.locale = sre_js_1.default.engineSetup().locale;
            explorer.speechGenerator.setOptions({ locale: doc.options.sre.locale });
        }
        explorer.showRegion = 'subtitles';
        return explorer;
    },
    braille: function (doc, node) {
        var _a;
        var rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            rest[_i - 2] = arguments[_i];
        }
        var explorer = (_a = ke.SpeechExplorer).create.apply(_a, __spreadArray([doc, doc.explorerRegions.brailleRegion, node], __read(rest), false));
        explorer.speechGenerator.setOptions({ locale: 'nemeth', domain: 'default',
            style: 'default', modality: 'braille' });
        explorer.showRegion = 'viewBraille';
        return explorer;
    },
    keyMagnifier: function (doc, node) {
        var _a;
        var rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            rest[_i - 2] = arguments[_i];
        }
        return (_a = ke.Magnifier).create.apply(_a, __spreadArray([doc, doc.explorerRegions.magnifier, node], __read(rest), false));
    },
    mouseMagnifier: function (doc, node) {
        var _rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            _rest[_i - 2] = arguments[_i];
        }
        return me.ContentHoverer.create(doc, doc.explorerRegions.magnifier, node, function (x) { return x.hasAttribute('data-semantic-type'); }, function (x) { return x; });
    },
    hover: function (doc, node) {
        var _rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            _rest[_i - 2] = arguments[_i];
        }
        return me.FlameHoverer.create(doc, null, node);
    },
    infoType: function (doc, node) {
        var _rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            _rest[_i - 2] = arguments[_i];
        }
        return me.ValueHoverer.create(doc, doc.explorerRegions.tooltip1, node, function (x) { return x.hasAttribute('data-semantic-type'); }, function (x) { return x.getAttribute('data-semantic-type'); });
    },
    infoRole: function (doc, node) {
        var _rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            _rest[_i - 2] = arguments[_i];
        }
        return me.ValueHoverer.create(doc, doc.explorerRegions.tooltip2, node, function (x) { return x.hasAttribute('data-semantic-role'); }, function (x) { return x.getAttribute('data-semantic-role'); });
    },
    infoPrefix: function (doc, node) {
        var _rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            _rest[_i - 2] = arguments[_i];
        }
        return me.ValueHoverer.create(doc, doc.explorerRegions.tooltip3, node, function (x) { return x.hasAttribute('data-semantic-prefix'); }, function (x) { return x.getAttribute('data-semantic-prefix'); });
    },
    flame: function (doc, node) {
        var _rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            _rest[_i - 2] = arguments[_i];
        }
        return TreeExplorer_js_1.FlameColorer.create(doc, null, node);
    },
    treeColoring: function (doc, node) {
        var rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            rest[_i - 2] = arguments[_i];
        }
        return TreeExplorer_js_1.TreeColorer.create.apply(TreeExplorer_js_1.TreeColorer, __spreadArray([doc, null, node], __read(rest), false));
    }
};
function initExplorers(document, node, mml) {
    var e_5, _a;
    var explorers = {};
    try {
        for (var _b = __values(Object.keys(allExplorers)), _c = _b.next(); !_c.done; _c = _b.next()) {
            var key = _c.value;
            explorers[key] = allExplorers[key](document, node, mml);
        }
    }
    catch (e_5_1) { e_5 = { error: e_5_1 }; }
    finally {
        try {
            if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
        }
        finally { if (e_5) throw e_5.error; }
    }
    return explorers;
}
function setA11yOptions(document, options) {
    var e_6, _a;
    var sreOptions = sre_js_1.default.engineSetup();
    for (var key in options) {
        if (document.options.a11y[key] !== undefined) {
            setA11yOption(document, key, options[key]);
            if (key === 'locale') {
                document.options.sre[key] = options[key];
            }
            continue;
        }
        if (sreOptions[key] !== undefined) {
            document.options.sre[key] = options[key];
        }
    }
    try {
        for (var _b = __values(document.math), _c = _b.next(); !_c.done; _c = _b.next()) {
            var item = _c.value;
            item.attachExplorers(document);
        }
    }
    catch (e_6_1) { e_6 = { error: e_6_1 }; }
    finally {
        try {
            if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
        }
        finally { if (e_6) throw e_6.error; }
    }
}
exports.setA11yOptions = setA11yOptions;
function setA11yOption(document, option, value) {
    switch (option) {
        case 'magnification':
            switch (value) {
                case 'None':
                    document.options.a11y.magnification = value;
                    document.options.a11y.keyMagnifier = false;
                    document.options.a11y.mouseMagnifier = false;
                    break;
                case 'Keyboard':
                    document.options.a11y.magnification = value;
                    document.options.a11y.keyMagnifier = true;
                    document.options.a11y.mouseMagnifier = false;
                    break;
                case 'Mouse':
                    document.options.a11y.magnification = value;
                    document.options.a11y.keyMagnifier = false;
                    document.options.a11y.mouseMagnifier = true;
                    break;
            }
            break;
        case 'highlight':
            switch (value) {
                case 'None':
                    document.options.a11y.highlight = value;
                    document.options.a11y.hover = false;
                    document.options.a11y.flame = false;
                    break;
                case 'Hover':
                    document.options.a11y.highlight = value;
                    document.options.a11y.hover = true;
                    document.options.a11y.flame = false;
                    break;
                case 'Flame':
                    document.options.a11y.highlight = value;
                    document.options.a11y.hover = false;
                    document.options.a11y.flame = true;
                    break;
            }
            break;
        default:
            document.options.a11y[option] = value;
    }
}
exports.setA11yOption = setA11yOption;
var csPrefsSetting = {};
var csPrefsVariables = function (menu, prefs) {
    var e_7, _a;
    var srVariable = menu.pool.lookup('speechRules');
    var _loop_1 = function (pref) {
        if (csPrefsSetting[pref])
            return "continue";
        menu.factory.get('variable')(menu.factory, {
            name: 'csprf_' + pref,
            setter: function (value) {
                csPrefsSetting[pref] = value;
                srVariable.setValue('clearspeak-' +
                    sre_js_1.default.clearspeakPreferences.addPreference(sre_js_1.default.clearspeakStyle(), pref, value));
            },
            getter: function () { return csPrefsSetting[pref] || 'Auto'; }
        }, menu.pool);
    };
    try {
        for (var prefs_1 = __values(prefs), prefs_1_1 = prefs_1.next(); !prefs_1_1.done; prefs_1_1 = prefs_1.next()) {
            var pref = prefs_1_1.value;
            _loop_1(pref);
        }
    }
    catch (e_7_1) { e_7 = { error: e_7_1 }; }
    finally {
        try {
            if (prefs_1_1 && !prefs_1_1.done && (_a = prefs_1.return)) _a.call(prefs_1);
        }
        finally { if (e_7) throw e_7.error; }
    }
};
var csSelectionBox = function (menu, locale) {
    var e_8, _a;
    var prefs = sre_js_1.default.clearspeakPreferences.getLocalePreferences();
    var props = prefs[locale];
    if (!props) {
        var csEntry = menu.findID('Accessibility', 'Speech', 'Clearspeak');
        if (csEntry) {
            csEntry.disable();
        }
        return null;
    }
    csPrefsVariables(menu, Object.keys(props));
    var items = [];
    var _loop_2 = function (prop) {
        items.push({
            'title': prop,
            'values': props[prop].map(function (x) { return x.replace(RegExp('^' + prop + '_'), ''); }),
            'variable': 'csprf_' + prop
        });
    };
    try {
        for (var _b = __values(Object.getOwnPropertyNames(props)), _c = _b.next(); !_c.done; _c = _b.next()) {
            var prop = _c.value;
            _loop_2(prop);
        }
    }
    catch (e_8_1) { e_8 = { error: e_8_1 }; }
    finally {
        try {
            if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
        }
        finally { if (e_8) throw e_8.error; }
    }
    var sb = menu.factory.get('selectionBox')(menu.factory, {
        'title': 'Clearspeak Preferences',
        'signature': '',
        'order': 'alphabetic',
        'grid': 'square',
        'selections': items
    }, menu);
    return { 'type': 'command',
        'id': 'ClearspeakPreferences',
        'content': 'Select Preferences',
        'action': function () { return sb.post(0, 0); } };
};
var csMenu = function (menu, sub) {
    var locale = menu.pool.lookup('locale').getValue();
    var box = csSelectionBox(menu, locale);
    var items = [];
    try {
        items = sre_js_1.default.clearspeakPreferences.smartPreferences(menu.mathItem, locale);
    }
    catch (e) {
        console.log(e);
    }
    if (box) {
        items.splice(2, 0, box);
    }
    return menu.factory.get('subMenu')(menu.factory, {
        items: items,
        id: 'Clearspeak'
    }, sub);
};
MJContextMenu_js_1.MJContextMenu.DynamicSubmenus.set('Clearspeak', csMenu);
var language = function (menu, sub) {
    var e_9, _a;
    var radios = [];
    try {
        for (var _b = __values(sre_js_1.default.locales.keys()), _c = _b.next(); !_c.done; _c = _b.next()) {
            var lang = _c.value;
            if (lang === 'nemeth')
                continue;
            radios.push({ type: 'radio', id: lang,
                content: sre_js_1.default.locales.get(lang) || lang, variable: 'locale' });
        }
    }
    catch (e_9_1) { e_9 = { error: e_9_1 }; }
    finally {
        try {
            if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
        }
        finally { if (e_9) throw e_9.error; }
    }
    radios.sort(function (x, y) { return x.content.localeCompare(y.content, 'en'); });
    return menu.factory.get('subMenu')(menu.factory, {
        items: radios, id: 'Language'
    }, sub);
};
MJContextMenu_js_1.MJContextMenu.DynamicSubmenus.set('A11yLanguage', language);
//# sourceMappingURL=explorer.js.map

/***/ }),

/***/ 724:
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
exports.AbstractExplorer = void 0;
var sre_js_1 = __importDefault(__webpack_require__(712));
var AbstractExplorer = (function () {
    function AbstractExplorer(document, region, node) {
        var _rest = [];
        for (var _i = 3; _i < arguments.length; _i++) {
            _rest[_i - 3] = arguments[_i];
        }
        this.document = document;
        this.region = region;
        this.node = node;
        this.stoppable = true;
        this.events = [];
        this.highlighter = this.getHighlighter();
        this._active = false;
    }
    AbstractExplorer.stopEvent = function (event) {
        if (event.preventDefault) {
            event.preventDefault();
        }
        else {
            event.returnValue = false;
        }
        if (event.stopImmediatePropagation) {
            event.stopImmediatePropagation();
        }
        else if (event.stopPropagation) {
            event.stopPropagation();
        }
        event.cancelBubble = true;
    };
    AbstractExplorer.create = function (document, region, node) {
        var rest = [];
        for (var _i = 3; _i < arguments.length; _i++) {
            rest[_i - 3] = arguments[_i];
        }
        var explorer = new (this.bind.apply(this, __spreadArray([void 0, document, region, node], __read(rest), false)))();
        return explorer;
    };
    AbstractExplorer.prototype.Events = function () {
        return this.events;
    };
    Object.defineProperty(AbstractExplorer.prototype, "active", {
        get: function () {
            return this._active;
        },
        set: function (flag) {
            this._active = flag;
        },
        enumerable: false,
        configurable: true
    });
    AbstractExplorer.prototype.Attach = function () {
        this.AddEvents();
    };
    AbstractExplorer.prototype.Detach = function () {
        this.RemoveEvents();
    };
    AbstractExplorer.prototype.Start = function () {
        this.highlighter = this.getHighlighter();
        this.active = true;
    };
    AbstractExplorer.prototype.Stop = function () {
        if (this.active) {
            this.region.Clear();
            this.region.Hide();
            this.active = false;
        }
    };
    AbstractExplorer.prototype.AddEvents = function () {
        var e_1, _a;
        try {
            for (var _b = __values(this.events), _c = _b.next(); !_c.done; _c = _b.next()) {
                var _d = __read(_c.value, 2), eventkind = _d[0], eventfunc = _d[1];
                this.node.addEventListener(eventkind, eventfunc);
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
    AbstractExplorer.prototype.RemoveEvents = function () {
        var e_2, _a;
        try {
            for (var _b = __values(this.events), _c = _b.next(); !_c.done; _c = _b.next()) {
                var _d = __read(_c.value, 2), eventkind = _d[0], eventfunc = _d[1];
                this.node.removeEventListener(eventkind, eventfunc);
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
    AbstractExplorer.prototype.Update = function (force) {
        if (force === void 0) { force = false; }
    };
    AbstractExplorer.prototype.getHighlighter = function () {
        var opts = this.document.options.a11y;
        var foreground = { color: opts.foregroundColor.toLowerCase(),
            alpha: opts.foregroundOpacity / 100 };
        var background = { color: opts.backgroundColor.toLowerCase(),
            alpha: opts.backgroundOpacity / 100 };
        return sre_js_1.default.getHighlighter(background, foreground, { renderer: this.document.outputJax.name, browser: 'v3' });
    };
    AbstractExplorer.prototype.stopEvent = function (event) {
        if (this.stoppable) {
            AbstractExplorer.stopEvent(event);
        }
    };
    return AbstractExplorer;
}());
exports.AbstractExplorer = AbstractExplorer;
//# sourceMappingURL=Explorer.js.map

/***/ }),

/***/ 269:
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
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Magnifier = exports.SpeechExplorer = exports.AbstractKeyExplorer = void 0;
var Explorer_js_1 = __webpack_require__(724);
var sre_js_1 = __importDefault(__webpack_require__(712));
var AbstractKeyExplorer = (function (_super) {
    __extends(AbstractKeyExplorer, _super);
    function AbstractKeyExplorer() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.attached = false;
        _this.eventsAttached = false;
        _this.events = _super.prototype.Events.call(_this).concat([['keydown', _this.KeyDown.bind(_this)],
            ['focusin', _this.FocusIn.bind(_this)],
            ['focusout', _this.FocusOut.bind(_this)]]);
        _this.oldIndex = null;
        return _this;
    }
    AbstractKeyExplorer.prototype.FocusIn = function (_event) {
    };
    AbstractKeyExplorer.prototype.FocusOut = function (_event) {
        this.Stop();
    };
    AbstractKeyExplorer.prototype.Update = function (force) {
        if (force === void 0) { force = false; }
        if (!this.active && !force)
            return;
        this.highlighter.unhighlight();
        var nodes = this.walker.getFocus(true).getNodes();
        if (!nodes.length) {
            this.walker.refocus();
            nodes = this.walker.getFocus().getNodes();
        }
        this.highlighter.highlight(nodes);
    };
    AbstractKeyExplorer.prototype.Attach = function () {
        _super.prototype.Attach.call(this);
        this.attached = true;
        this.oldIndex = this.node.tabIndex;
        this.node.tabIndex = 1;
        this.node.setAttribute('role', 'application');
    };
    AbstractKeyExplorer.prototype.AddEvents = function () {
        if (!this.eventsAttached) {
            _super.prototype.AddEvents.call(this);
            this.eventsAttached = true;
        }
    };
    AbstractKeyExplorer.prototype.Detach = function () {
        if (this.active) {
            this.node.tabIndex = this.oldIndex;
            this.oldIndex = null;
            this.node.removeAttribute('role');
        }
        this.attached = false;
    };
    AbstractKeyExplorer.prototype.Stop = function () {
        if (this.active) {
            this.highlighter.unhighlight();
            this.walker.deactivate();
        }
        _super.prototype.Stop.call(this);
    };
    return AbstractKeyExplorer;
}(Explorer_js_1.AbstractExplorer));
exports.AbstractKeyExplorer = AbstractKeyExplorer;
var SpeechExplorer = (function (_super) {
    __extends(SpeechExplorer, _super);
    function SpeechExplorer(document, region, node, mml) {
        var _this = _super.call(this, document, region, node) || this;
        _this.document = document;
        _this.region = region;
        _this.node = node;
        _this.mml = mml;
        _this.showRegion = 'subtitles';
        _this.init = false;
        _this.restarted = false;
        _this.initWalker();
        return _this;
    }
    SpeechExplorer.prototype.Start = function () {
        var _this = this;
        if (!this.attached)
            return;
        var options = this.getOptions();
        if (!this.init) {
            this.init = true;
            SpeechExplorer.updatePromise = SpeechExplorer.updatePromise.then(function () { return __awaiter(_this, void 0, void 0, function () {
                var _this = this;
                return __generator(this, function (_a) {
                    return [2, sre_js_1.default.sreReady()
                            .then(function () { return sre_js_1.default.setupEngine({ locale: options.locale }); })
                            .then(function () {
                            _this.Speech(_this.walker);
                            _this.Start();
                        })];
                });
            }); })
                .catch(function (error) { return console.log(error.message); });
            return;
        }
        _super.prototype.Start.call(this);
        this.speechGenerator = sre_js_1.default.getSpeechGenerator('Direct');
        this.speechGenerator.setOptions(options);
        this.walker = sre_js_1.default.getWalker('table', this.node, this.speechGenerator, this.highlighter, this.mml);
        this.walker.activate();
        this.Update();
        if (this.document.options.a11y[this.showRegion]) {
            SpeechExplorer.updatePromise.then(function () { return _this.region.Show(_this.node, _this.highlighter); });
        }
        this.restarted = true;
    };
    SpeechExplorer.prototype.Update = function (force) {
        var _this = this;
        if (force === void 0) { force = false; }
        _super.prototype.Update.call(this, force);
        var options = this.speechGenerator.getOptions();
        if (options.modality === 'speech') {
            this.document.options.sre.domain = options.domain;
            this.document.options.sre.style = options.style;
            this.document.options.a11y.speechRules =
                options.domain + '-' + options.style;
        }
        SpeechExplorer.updatePromise = SpeechExplorer.updatePromise.then(function () { return __awaiter(_this, void 0, void 0, function () {
            var _this = this;
            return __generator(this, function (_a) {
                return [2, sre_js_1.default.sreReady()
                        .then(function () { return sre_js_1.default.setupEngine({ modality: options.modality,
                        locale: options.locale }); })
                        .then(function () { return _this.region.Update(_this.walker.speech()); })];
            });
        }); });
    };
    SpeechExplorer.prototype.Speech = function (walker) {
        var _this = this;
        SpeechExplorer.updatePromise.then(function () {
            walker.speech();
            _this.node.setAttribute('hasspeech', 'true');
            _this.Update();
            if (_this.restarted && _this.document.options.a11y[_this.showRegion]) {
                _this.region.Show(_this.node, _this.highlighter);
            }
        });
    };
    SpeechExplorer.prototype.KeyDown = function (event) {
        var code = event.keyCode;
        this.walker.modifier = event.shiftKey;
        if (code === 27) {
            this.Stop();
            this.stopEvent(event);
            return;
        }
        if (this.active) {
            this.Move(code);
            if (this.triggerLink(code))
                return;
            this.stopEvent(event);
            return;
        }
        if (code === 32 && event.shiftKey || code === 13) {
            this.Start();
            this.stopEvent(event);
        }
    };
    SpeechExplorer.prototype.triggerLink = function (code) {
        var _a, _b;
        if (code !== 13) {
            return false;
        }
        var node = (_a = this.walker.getFocus().getNodes()) === null || _a === void 0 ? void 0 : _a[0];
        var focus = (_b = node === null || node === void 0 ? void 0 : node.getAttribute('data-semantic-postfix')) === null || _b === void 0 ? void 0 : _b.match(/(^| )link($| )/);
        if (focus) {
            node.parentNode.dispatchEvent(new MouseEvent('click'));
            return true;
        }
        return false;
    };
    SpeechExplorer.prototype.Move = function (key) {
        this.walker.move(key);
        this.Update();
    };
    SpeechExplorer.prototype.initWalker = function () {
        this.speechGenerator = sre_js_1.default.getSpeechGenerator('Tree');
        var dummy = sre_js_1.default.getWalker('dummy', this.node, this.speechGenerator, this.highlighter, this.mml);
        this.walker = dummy;
    };
    SpeechExplorer.prototype.getOptions = function () {
        var options = this.speechGenerator.getOptions();
        var sreOptions = this.document.options.sre;
        if (options.modality === 'speech' &&
            (options.locale !== sreOptions.locale ||
                options.domain !== sreOptions.domain ||
                options.style !== sreOptions.style)) {
            options.domain = sreOptions.domain;
            options.style = sreOptions.style;
            options.locale = sreOptions.locale;
            this.walker.update(options);
        }
        return options;
    };
    SpeechExplorer.updatePromise = Promise.resolve();
    return SpeechExplorer;
}(AbstractKeyExplorer));
exports.SpeechExplorer = SpeechExplorer;
var Magnifier = (function (_super) {
    __extends(Magnifier, _super);
    function Magnifier(document, region, node, mml) {
        var _this = _super.call(this, document, region, node) || this;
        _this.document = document;
        _this.region = region;
        _this.node = node;
        _this.mml = mml;
        _this.walker = sre_js_1.default.getWalker('table', _this.node, sre_js_1.default.getSpeechGenerator('Dummy'), _this.highlighter, _this.mml);
        return _this;
    }
    Magnifier.prototype.Update = function (force) {
        if (force === void 0) { force = false; }
        _super.prototype.Update.call(this, force);
        this.showFocus();
    };
    Magnifier.prototype.Start = function () {
        _super.prototype.Start.call(this);
        if (!this.attached)
            return;
        this.region.Show(this.node, this.highlighter);
        this.walker.activate();
        this.Update();
    };
    Magnifier.prototype.showFocus = function () {
        var node = this.walker.getFocus().getNodes()[0];
        this.region.Show(node, this.highlighter);
    };
    Magnifier.prototype.Move = function (key) {
        var result = this.walker.move(key);
        if (result) {
            this.Update();
        }
    };
    Magnifier.prototype.KeyDown = function (event) {
        var code = event.keyCode;
        this.walker.modifier = event.shiftKey;
        if (code === 27) {
            this.Stop();
            this.stopEvent(event);
            return;
        }
        if (this.active && code !== 13) {
            this.Move(code);
            this.stopEvent(event);
            return;
        }
        if (code === 32 && event.shiftKey || code === 13) {
            this.Start();
            this.stopEvent(event);
        }
    };
    return Magnifier;
}(AbstractKeyExplorer));
exports.Magnifier = Magnifier;
//# sourceMappingURL=KeyExplorer.js.map

/***/ }),

/***/ 85:
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
exports.FlameHoverer = exports.ContentHoverer = exports.ValueHoverer = exports.Hoverer = exports.AbstractMouseExplorer = void 0;
var Region_js_1 = __webpack_require__(367);
var Explorer_js_1 = __webpack_require__(724);
__webpack_require__(712);
var AbstractMouseExplorer = (function (_super) {
    __extends(AbstractMouseExplorer, _super);
    function AbstractMouseExplorer() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.events = _super.prototype.Events.call(_this).concat([
            ['mouseover', _this.MouseOver.bind(_this)],
            ['mouseout', _this.MouseOut.bind(_this)]
        ]);
        return _this;
    }
    AbstractMouseExplorer.prototype.MouseOver = function (_event) {
        this.Start();
    };
    AbstractMouseExplorer.prototype.MouseOut = function (_event) {
        this.Stop();
    };
    return AbstractMouseExplorer;
}(Explorer_js_1.AbstractExplorer));
exports.AbstractMouseExplorer = AbstractMouseExplorer;
var Hoverer = (function (_super) {
    __extends(Hoverer, _super);
    function Hoverer(document, region, node, nodeQuery, nodeAccess) {
        var _this = _super.call(this, document, region, node) || this;
        _this.document = document;
        _this.region = region;
        _this.node = node;
        _this.nodeQuery = nodeQuery;
        _this.nodeAccess = nodeAccess;
        return _this;
    }
    Hoverer.prototype.MouseOut = function (event) {
        if (event.clientX === this.coord[0] &&
            event.clientY === this.coord[1]) {
            return;
        }
        this.highlighter.unhighlight();
        this.region.Hide();
        _super.prototype.MouseOut.call(this, event);
    };
    Hoverer.prototype.MouseOver = function (event) {
        _super.prototype.MouseOver.call(this, event);
        var target = event.target;
        this.coord = [event.clientX, event.clientY];
        var _a = __read(this.getNode(target), 2), node = _a[0], kind = _a[1];
        if (!node) {
            return;
        }
        this.highlighter.unhighlight();
        this.highlighter.highlight([node]);
        this.region.Update(kind);
        this.region.Show(node, this.highlighter);
    };
    Hoverer.prototype.getNode = function (node) {
        var original = node;
        while (node && node !== this.node) {
            if (this.nodeQuery(node)) {
                return [node, this.nodeAccess(node)];
            }
            node = node.parentNode;
        }
        node = original;
        while (node) {
            if (this.nodeQuery(node)) {
                return [node, this.nodeAccess(node)];
            }
            var child = node.childNodes[0];
            node = (child && child.tagName === 'defs') ?
                node.childNodes[1] : child;
        }
        return [null, null];
    };
    return Hoverer;
}(AbstractMouseExplorer));
exports.Hoverer = Hoverer;
var ValueHoverer = (function (_super) {
    __extends(ValueHoverer, _super);
    function ValueHoverer() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return ValueHoverer;
}(Hoverer));
exports.ValueHoverer = ValueHoverer;
var ContentHoverer = (function (_super) {
    __extends(ContentHoverer, _super);
    function ContentHoverer() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return ContentHoverer;
}(Hoverer));
exports.ContentHoverer = ContentHoverer;
var FlameHoverer = (function (_super) {
    __extends(FlameHoverer, _super);
    function FlameHoverer(document, _ignore, node) {
        var _this = _super.call(this, document, new Region_js_1.DummyRegion(document), node, function (x) { return _this.highlighter.isMactionNode(x); }, function () { }) || this;
        _this.document = document;
        _this.node = node;
        return _this;
    }
    return FlameHoverer;
}(Hoverer));
exports.FlameHoverer = FlameHoverer;
//# sourceMappingURL=MouseExplorer.js.map

/***/ }),

/***/ 367:
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
var _a, _b, _c;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.HoverRegion = exports.LiveRegion = exports.ToolTip = exports.StringRegion = exports.DummyRegion = exports.AbstractRegion = void 0;
var StyleList_js_1 = __webpack_require__(888);
var AbstractRegion = (function () {
    function AbstractRegion(document) {
        this.document = document;
        this.CLASS = this.constructor;
        this.AddStyles();
        this.AddElement();
    }
    AbstractRegion.prototype.AddStyles = function () {
        if (this.CLASS.styleAdded) {
            return;
        }
        var node = this.document.adaptor.node('style');
        node.innerHTML = this.CLASS.style.cssText;
        this.document.adaptor.head(this.document.adaptor.document).
            appendChild(node);
        this.CLASS.styleAdded = true;
    };
    AbstractRegion.prototype.AddElement = function () {
        var element = this.document.adaptor.node('div');
        element.classList.add(this.CLASS.className);
        element.style.backgroundColor = 'white';
        this.div = element;
        this.inner = this.document.adaptor.node('div');
        this.div.appendChild(this.inner);
        this.document.adaptor.
            body(this.document.adaptor.document).
            appendChild(this.div);
    };
    AbstractRegion.prototype.Show = function (node, highlighter) {
        this.position(node);
        this.highlight(highlighter);
        this.div.classList.add(this.CLASS.className + '_Show');
    };
    AbstractRegion.prototype.Hide = function () {
        this.div.classList.remove(this.CLASS.className + '_Show');
    };
    AbstractRegion.prototype.stackRegions = function (node) {
        var rect = node.getBoundingClientRect();
        var baseBottom = 0;
        var baseLeft = Number.POSITIVE_INFINITY;
        var regions = this.document.adaptor.document.getElementsByClassName(this.CLASS.className + '_Show');
        for (var i = 0, region = void 0; region = regions[i]; i++) {
            if (region !== this.div) {
                baseBottom = Math.max(region.getBoundingClientRect().bottom, baseBottom);
                baseLeft = Math.min(region.getBoundingClientRect().left, baseLeft);
            }
        }
        var bot = (baseBottom ? baseBottom : rect.bottom + 10) + window.pageYOffset;
        var left = (baseLeft < Number.POSITIVE_INFINITY ? baseLeft : rect.left) + window.pageXOffset;
        this.div.style.top = bot + 'px';
        this.div.style.left = left + 'px';
    };
    AbstractRegion.styleAdded = false;
    return AbstractRegion;
}());
exports.AbstractRegion = AbstractRegion;
var DummyRegion = (function (_super) {
    __extends(DummyRegion, _super);
    function DummyRegion() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    DummyRegion.prototype.Clear = function () { };
    DummyRegion.prototype.Update = function () { };
    DummyRegion.prototype.Hide = function () { };
    DummyRegion.prototype.Show = function () { };
    DummyRegion.prototype.AddElement = function () { };
    DummyRegion.prototype.AddStyles = function () { };
    DummyRegion.prototype.position = function () { };
    DummyRegion.prototype.highlight = function (_highlighter) { };
    return DummyRegion;
}(AbstractRegion));
exports.DummyRegion = DummyRegion;
var StringRegion = (function (_super) {
    __extends(StringRegion, _super);
    function StringRegion() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    StringRegion.prototype.Clear = function () {
        this.Update('');
        this.inner.style.top = '';
        this.inner.style.backgroundColor = '';
    };
    StringRegion.prototype.Update = function (speech) {
        this.inner.textContent = '';
        this.inner.textContent = speech;
    };
    StringRegion.prototype.position = function (node) {
        this.stackRegions(node);
    };
    StringRegion.prototype.highlight = function (highlighter) {
        var color = highlighter.colorString();
        this.inner.style.backgroundColor = color.background;
        this.inner.style.color = color.foreground;
    };
    return StringRegion;
}(AbstractRegion));
exports.StringRegion = StringRegion;
var ToolTip = (function (_super) {
    __extends(ToolTip, _super);
    function ToolTip() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    ToolTip.className = 'MJX_ToolTip';
    ToolTip.style = new StyleList_js_1.CssStyles((_a = {},
        _a['.' + ToolTip.className] = {
            position: 'absolute', display: 'inline-block',
            height: '1px', width: '1px'
        },
        _a['.' + ToolTip.className + '_Show'] = {
            width: 'auto', height: 'auto', opacity: 1, 'text-align': 'center',
            'border-radius': '6px', padding: '0px 0px',
            'border-bottom': '1px dotted black', position: 'absolute',
            'z-index': 202
        },
        _a));
    return ToolTip;
}(StringRegion));
exports.ToolTip = ToolTip;
var LiveRegion = (function (_super) {
    __extends(LiveRegion, _super);
    function LiveRegion(document) {
        var _this = _super.call(this, document) || this;
        _this.document = document;
        _this.div.setAttribute('aria-live', 'assertive');
        return _this;
    }
    LiveRegion.className = 'MJX_LiveRegion';
    LiveRegion.style = new StyleList_js_1.CssStyles((_b = {},
        _b['.' + LiveRegion.className] = {
            position: 'absolute', top: '0', height: '1px', width: '1px',
            padding: '1px', overflow: 'hidden'
        },
        _b['.' + LiveRegion.className + '_Show'] = {
            top: '0', position: 'absolute', width: 'auto', height: 'auto',
            padding: '0px 0px', opacity: 1, 'z-index': '202',
            left: 0, right: 0, 'margin': '0 auto',
            'background-color': 'rgba(0, 0, 255, 0.2)', 'box-shadow': '0px 10px 20px #888',
            border: '2px solid #CCCCCC'
        },
        _b));
    return LiveRegion;
}(StringRegion));
exports.LiveRegion = LiveRegion;
var HoverRegion = (function (_super) {
    __extends(HoverRegion, _super);
    function HoverRegion(document) {
        var _this = _super.call(this, document) || this;
        _this.document = document;
        _this.inner.style.lineHeight = '0';
        return _this;
    }
    HoverRegion.prototype.position = function (node) {
        var nodeRect = node.getBoundingClientRect();
        var divRect = this.div.getBoundingClientRect();
        var xCenter = nodeRect.left + (nodeRect.width / 2);
        var left = xCenter - (divRect.width / 2);
        left = (left < 0) ? 0 : left;
        left = left + window.pageXOffset;
        var top;
        switch (this.document.options.a11y.align) {
            case 'top':
                top = nodeRect.top - divRect.height - 10;
                break;
            case 'bottom':
                top = nodeRect.bottom + 10;
                break;
            case 'center':
            default:
                var yCenter = nodeRect.top + (nodeRect.height / 2);
                top = yCenter - (divRect.height / 2);
        }
        top = top + window.pageYOffset;
        top = (top < 0) ? 0 : top;
        this.div.style.top = top + 'px';
        this.div.style.left = left + 'px';
    };
    HoverRegion.prototype.highlight = function (highlighter) {
        if (this.inner.firstChild &&
            !this.inner.firstChild.hasAttribute('sre-highlight')) {
            return;
        }
        var color = highlighter.colorString();
        this.inner.style.backgroundColor = color.background;
        this.inner.style.color = color.foreground;
    };
    HoverRegion.prototype.Show = function (node, highlighter) {
        this.div.style.fontSize = this.document.options.a11y.magnify;
        this.Update(node);
        _super.prototype.Show.call(this, node, highlighter);
    };
    HoverRegion.prototype.Clear = function () {
        this.inner.textContent = '';
        this.inner.style.top = '';
        this.inner.style.backgroundColor = '';
    };
    HoverRegion.prototype.Update = function (node) {
        this.Clear();
        var mjx = this.cloneNode(node);
        this.inner.appendChild(mjx);
    };
    HoverRegion.prototype.cloneNode = function (node) {
        var mjx = node.cloneNode(true);
        if (mjx.nodeName !== 'MJX-CONTAINER') {
            if (mjx.nodeName !== 'g') {
                mjx.style.marginLeft = mjx.style.marginRight = '0';
            }
            var container = node;
            while (container && container.nodeName !== 'MJX-CONTAINER') {
                container = container.parentNode;
            }
            if (mjx.nodeName !== 'MJX-MATH' && mjx.nodeName !== 'svg') {
                var child = container.firstChild;
                mjx = child.cloneNode(false).appendChild(mjx).parentNode;
                if (mjx.nodeName === 'svg') {
                    mjx.firstChild.setAttribute('transform', 'matrix(1 0 0 -1 0 0)');
                    var W = parseFloat(mjx.getAttribute('viewBox').split(/ /)[2]);
                    var w = parseFloat(mjx.getAttribute('width'));
                    var _a = node.getBBox(), x = _a.x, y = _a.y, width = _a.width, height = _a.height;
                    mjx.setAttribute('viewBox', [x, -(y + height), width, height].join(' '));
                    mjx.removeAttribute('style');
                    mjx.setAttribute('width', (w / W * width) + 'ex');
                    mjx.setAttribute('height', (w / W * height) + 'ex');
                    container.setAttribute('sre-highlight', 'false');
                }
            }
            mjx = container.cloneNode(false).appendChild(mjx).parentNode;
            mjx.style.margin = '0';
        }
        return mjx;
    };
    HoverRegion.className = 'MJX_HoverRegion';
    HoverRegion.style = new StyleList_js_1.CssStyles((_c = {},
        _c['.' + HoverRegion.className] = {
            position: 'absolute', height: '1px', width: '1px',
            padding: '1px', overflow: 'hidden'
        },
        _c['.' + HoverRegion.className + '_Show'] = {
            position: 'absolute', width: 'max-content', height: 'auto',
            padding: '0px 0px', opacity: 1, 'z-index': '202', 'margin': '0 auto',
            'background-color': 'rgba(0, 0, 255, 0.2)',
            'box-shadow': '0px 10px 20px #888', border: '2px solid #CCCCCC'
        },
        _c));
    return HoverRegion;
}(AbstractRegion));
exports.HoverRegion = HoverRegion;
//# sourceMappingURL=Region.js.map

/***/ }),

/***/ 854:
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
exports.TreeColorer = exports.FlameColorer = exports.AbstractTreeExplorer = void 0;
var Explorer_js_1 = __webpack_require__(724);
var sre_js_1 = __importDefault(__webpack_require__(712));
var AbstractTreeExplorer = (function (_super) {
    __extends(AbstractTreeExplorer, _super);
    function AbstractTreeExplorer(document, region, node, mml) {
        var _this = _super.call(this, document, null, node) || this;
        _this.document = document;
        _this.region = region;
        _this.node = node;
        _this.mml = mml;
        _this.stoppable = false;
        return _this;
    }
    AbstractTreeExplorer.prototype.Attach = function () {
        _super.prototype.Attach.call(this);
        this.Start();
    };
    AbstractTreeExplorer.prototype.Detach = function () {
        this.Stop();
        _super.prototype.Detach.call(this);
    };
    return AbstractTreeExplorer;
}(Explorer_js_1.AbstractExplorer));
exports.AbstractTreeExplorer = AbstractTreeExplorer;
var FlameColorer = (function (_super) {
    __extends(FlameColorer, _super);
    function FlameColorer() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    FlameColorer.prototype.Start = function () {
        if (this.active)
            return;
        this.active = true;
        this.highlighter.highlightAll(this.node);
    };
    FlameColorer.prototype.Stop = function () {
        if (this.active) {
            this.highlighter.unhighlightAll();
        }
        this.active = false;
    };
    return FlameColorer;
}(AbstractTreeExplorer));
exports.FlameColorer = FlameColorer;
var TreeColorer = (function (_super) {
    __extends(TreeColorer, _super);
    function TreeColorer() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    TreeColorer.prototype.Start = function () {
        if (this.active)
            return;
        this.active = true;
        var generator = sre_js_1.default.getSpeechGenerator('Color');
        if (!this.node.hasAttribute('hasforegroundcolor')) {
            generator.generateSpeech(this.node, this.mml);
            this.node.setAttribute('hasforegroundcolor', 'true');
        }
        this.highlighter.colorizeAll(this.node);
    };
    TreeColorer.prototype.Stop = function () {
        if (this.active) {
            this.highlighter.uncolorizeAll(this.node);
        }
        this.active = false;
    };
    return TreeColorer;
}(AbstractTreeExplorer));
exports.TreeColorer = TreeColorer;
//# sourceMappingURL=TreeExplorer.js.map

/***/ }),

/***/ 306:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;

__webpack_unused_export__ = ({ value: true });
exports.q = void 0;
exports.q = '3.2.2';
//# sourceMappingURL=version.js.map

/***/ }),

/***/ 511:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.EnrichedMathItemMixin = MathJax._.a11y['semantic-enrich'].EnrichedMathItemMixin;
exports.EnrichedMathDocumentMixin = MathJax._.a11y['semantic-enrich'].EnrichedMathDocumentMixin;
exports.EnrichHandler = MathJax._.a11y['semantic-enrich'].EnrichHandler;

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

/***/ }),

/***/ 888:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.CssStyles = MathJax._.util.StyleList.CssStyles;

/***/ }),

/***/ 850:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MJContextMenu = MathJax._.ui.menu.MJContextMenu.MJContextMenu;

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
// EXTERNAL MODULE: ../../../../js/a11y/explorer.js
var explorer = __webpack_require__(18);
// EXTERNAL MODULE: ../../../../js/a11y/explorer/Explorer.js
var Explorer = __webpack_require__(724);
// EXTERNAL MODULE: ../../../../js/a11y/explorer/KeyExplorer.js
var KeyExplorer = __webpack_require__(269);
// EXTERNAL MODULE: ../../../../js/a11y/explorer/MouseExplorer.js
var MouseExplorer = __webpack_require__(85);
// EXTERNAL MODULE: ../../../../js/a11y/explorer/Region.js
var Region = __webpack_require__(367);
// EXTERNAL MODULE: ../../../../js/a11y/explorer/TreeExplorer.js
var TreeExplorer = __webpack_require__(854);
;// CONCATENATED MODULE: ./lib/explorer.js









if (MathJax.loader) {
  MathJax.loader.checkVersion('a11y/explorer', version/* VERSION */.q, 'a11y');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    a11y: {
      explorer_ts: explorer,
      explorer: {
        Explorer: Explorer,
        KeyExplorer: KeyExplorer,
        MouseExplorer: MouseExplorer,
        Region: Region,
        TreeExplorer: TreeExplorer
      }
    }
  }
});
;// CONCATENATED MODULE: ./explorer.js




if (MathJax.startup) {
  MathJax.startup.extendHandler(function (handler) {
    return (0,explorer.ExplorerHandler)(handler);
  });
}
}();
/******/ })()
;