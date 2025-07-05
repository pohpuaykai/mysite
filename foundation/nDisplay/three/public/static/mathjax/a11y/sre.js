/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 706:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
var MathMaps = new Map();
exports["default"] = MathMaps;
//# sourceMappingURL=mathmaps.js.map

/***/ }),

/***/ 8905:
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
exports.sreReady = exports.Sre = void 0;
var Api = __importStar(__webpack_require__(9037));
var WalkerFactory = __importStar(__webpack_require__(907));
var SpeechGeneratorFactory = __importStar(__webpack_require__(7317));
var EngineConst = __importStar(__webpack_require__(4998));
var engine_js_1 = __importDefault(__webpack_require__(4886));
var clearspeak_preferences_js_1 = __webpack_require__(3955);
var HighlighterFactory = __importStar(__webpack_require__(9009));
var variables_js_1 = __webpack_require__(4513);
var mathmaps_js_1 = __importDefault(__webpack_require__(706));
var Sre;
(function (Sre) {
    Sre.locales = variables_js_1.Variables.LOCALES;
    Sre.sreReady = Api.engineReady;
    Sre.setupEngine = Api.setupEngine;
    Sre.engineSetup = Api.engineSetup;
    Sre.toEnriched = Api.toEnriched;
    Sre.toSpeech = Api.toSpeech;
    Sre.clearspeakPreferences = clearspeak_preferences_js_1.ClearspeakPreferences;
    Sre.getHighlighter = HighlighterFactory.highlighter;
    Sre.getSpeechGenerator = SpeechGeneratorFactory.generator;
    Sre.getWalker = WalkerFactory.walker;
    Sre.clearspeakStyle = function () {
        return EngineConst.DOMAIN_TO_STYLES['clearspeak'];
    };
    Sre.preloadLocales = function (locale) {
        return __awaiter(this, void 0, void 0, function () {
            var json;
            return __generator(this, function (_a) {
                json = mathmaps_js_1.default.get(locale);
                return [2, json ? new Promise(function (res, _rej) { return res(JSON.stringify(json)); }) :
                        Api.localeLoader()(locale)];
            });
        });
    };
})(Sre = exports.Sre || (exports.Sre = {}));
exports.sreReady = Sre.sreReady;
engine_js_1.default.getInstance().delay = true;
exports["default"] = Sre;
//# sourceMappingURL=sre.js.map

/***/ }),

/***/ 7306:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;

__webpack_unused_export__ = ({ value: true });
exports.q = void 0;
exports.q = '3.2.2';
//# sourceMappingURL=version.js.map

/***/ }),

/***/ 8723:
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

/***/ 1993:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;


__webpack_unused_export__ = ({
  value: true
});
__webpack_unused_export__ = MathJax._.components["package"].PackageError;
exports.GL = MathJax._.components["package"].Package;

/***/ }),

/***/ 7086:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AbstractAudioRenderer = void 0;
const engine_1 = __webpack_require__(4886);
class AbstractAudioRenderer {
    constructor() {
        this.separator_ = ' ';
    }
    setSeparator(sep) {
        this.separator_ = sep;
    }
    getSeparator() {
        return engine_1.default.getInstance().modality === 'braille' ? '' : this.separator_;
    }
    error(_key) {
        return null;
    }
    merge(spans) {
        let str = '';
        const len = spans.length - 1;
        for (let i = 0, span; (span = spans[i]); i++) {
            str += span.speech;
            if (i < len) {
                const sep = span.attributes['separator'];
                str += sep !== undefined ? sep : this.getSeparator();
            }
        }
        return str;
    }
    finalize(str) {
        return str;
    }
    pauseValue(value) {
        let numeric;
        switch (value) {
            case 'long':
                numeric = 750;
                break;
            case 'medium':
                numeric = 500;
                break;
            case 'short':
                numeric = 250;
                break;
            default:
                numeric = parseInt(value, 10);
        }
        return Math.floor((numeric * engine_1.default.getInstance().getRate()) / 100);
    }
}
exports.AbstractAudioRenderer = AbstractAudioRenderer;


/***/ }),

/***/ 9202:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AcssRenderer = void 0;
const EngineConst = __webpack_require__(4998);
const EventUtil = __webpack_require__(6988);
const AudioUtil = __webpack_require__(2599);
const markup_renderer_1 = __webpack_require__(9610);
class AcssRenderer extends markup_renderer_1.MarkupRenderer {
    markup(descrs) {
        this.setScaleFunction(-2, 2, 0, 10, 0);
        const markup = AudioUtil.personalityMarkup(descrs);
        const result = [];
        const currentPers = { open: [] };
        let pause = null;
        let isString = false;
        for (let i = 0, descr; (descr = markup[i]); i++) {
            if (AudioUtil.isMarkupElement(descr)) {
                AudioUtil.mergeMarkup(currentPers, descr);
                continue;
            }
            if (AudioUtil.isPauseElement(descr)) {
                if (isString) {
                    pause = AudioUtil.mergePause(pause, descr, Math.max);
                }
                continue;
            }
            const str = '"' + this.merge(descr.span) + '"';
            isString = true;
            if (pause) {
                result.push(this.pause(pause));
                pause = null;
            }
            const prosody = this.prosody_(currentPers);
            result.push(prosody ? '(text (' + prosody + ') ' + str + ')' : str);
        }
        return '(exp ' + result.join(' ') + ')';
    }
    error(key) {
        return '(error "' + EventUtil.Move.get(key) + '")';
    }
    prosodyElement(key, value) {
        value = this.applyScaleFunction(value);
        switch (key) {
            case EngineConst.personalityProps.RATE:
                return '(richness . ' + value + ')';
            case EngineConst.personalityProps.PITCH:
                return '(average-pitch . ' + value + ')';
            case EngineConst.personalityProps.VOLUME:
                return '(stress . ' + value + ')';
        }
        return '(value . ' + value + ')';
    }
    pause(pause) {
        return ('(pause . ' +
            this.pauseValue(pause[EngineConst.personalityProps.PAUSE]) +
            ')');
    }
    prosody_(pros) {
        const keys = pros.open;
        const result = [];
        for (let i = 0, key; (key = keys[i]); i++) {
            result.push(this.prosodyElement(key, pros[key]));
        }
        return result.join(' ');
    }
}
exports.AcssRenderer = AcssRenderer;


/***/ }),

/***/ 2599:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.isSpanElement = exports.isPauseElement = exports.isMarkupElement = exports.personalityMarkup = exports.sortClose = exports.mergeMarkup = exports.mergePause = void 0;
const base_util_1 = __webpack_require__(1426);
const EngineConst = __webpack_require__(4998);
const span_1 = __webpack_require__(1930);
function mergePause(oldPause, newPause, opt_merge) {
    if (!oldPause) {
        return newPause;
    }
    return { pause: mergePause_(oldPause.pause, newPause.pause, opt_merge) };
}
exports.mergePause = mergePause;
function mergePause_(oldPause, newPause, opt_merge) {
    const merge = opt_merge ||
        function (x, y) {
            if (typeof x === 'number' && typeof y === 'number') {
                return x + y;
            }
            if (typeof x === 'number') {
                return y;
            }
            if (typeof y === 'number') {
                return x;
            }
            return [oldPause, newPause].sort()[0];
        };
    return merge.call(null, oldPause, newPause);
}
function mergeMarkup(oldPers, newPers) {
    delete oldPers.open;
    newPers.close.forEach((x) => delete oldPers[x]);
    newPers.open.forEach((x) => (oldPers[x] = newPers[x]));
    const keys = Object.keys(oldPers);
    oldPers.open = keys;
}
exports.mergeMarkup = mergeMarkup;
function sortClose(open, descrs) {
    if (open.length <= 1) {
        return open;
    }
    const result = [];
    for (let i = 0, descr; (descr = descrs[i]), open.length; i++) {
        if (!descr.close || !descr.close.length) {
            continue;
        }
        descr.close.forEach(function (x) {
            const index = open.indexOf(x);
            if (index !== -1) {
                result.unshift(x);
                open.splice(index, 1);
            }
        });
    }
    return result;
}
exports.sortClose = sortClose;
let PersonalityRanges_ = {};
let LastOpen_ = [];
function personalityMarkup(descrs) {
    PersonalityRanges_ = {};
    LastOpen_ = [];
    let result = [];
    const currentPers = {};
    for (let i = 0, descr; (descr = descrs[i]); i++) {
        let pause = null;
        const span = descr.descriptionSpan();
        const pers = descr.personality;
        const join = pers[EngineConst.personalityProps.JOIN];
        delete pers[EngineConst.personalityProps.JOIN];
        if (typeof pers[EngineConst.personalityProps.PAUSE] !== 'undefined') {
            pause = {
                [EngineConst.personalityProps.PAUSE]: pers[EngineConst.personalityProps.PAUSE]
            };
            delete pers[EngineConst.personalityProps.PAUSE];
        }
        const diff = personalityDiff_(pers, currentPers);
        appendMarkup_(result, span, diff, join, pause, true);
    }
    result = result.concat(finaliseMarkup_());
    result = simplifyMarkup_(result);
    return result;
}
exports.personalityMarkup = personalityMarkup;
function appendElement_(markup, element) {
    const last = markup[markup.length - 1];
    if (!last) {
        markup.push(element);
        return;
    }
    if (isSpanElement(element) && isSpanElement(last)) {
        if (typeof last.join === 'undefined') {
            last.span = last.span.concat(element.span);
            return;
        }
        const lstr = last['span'].pop();
        const fstr = element['span'].shift();
        last['span'].push(lstr + last.join + fstr);
        last['span'] = last['span'].concat(element.span);
        last.join = element.join;
        return;
    }
    if (isPauseElement(element) && isPauseElement(last)) {
        last.pause = mergePause_(last.pause, element.pause);
        return;
    }
    markup.push(element);
}
function simplifyMarkup_(markup) {
    const lastPers = {};
    const result = [];
    for (let i = 0, element; (element = markup[i]); i++) {
        if (!isMarkupElement(element)) {
            appendElement_(result, element);
            continue;
        }
        if (!element.close || element.close.length !== 1 || element.open.length) {
            copyValues_(element, lastPers);
            result.push(element);
            continue;
        }
        let nextElement = markup[i + 1];
        if (!nextElement || isSpanElement(nextElement)) {
            copyValues_(element, lastPers);
            result.push(element);
            continue;
        }
        const pauseElement = isPauseElement(nextElement) ? nextElement : null;
        if (pauseElement) {
            nextElement = markup[i + 2];
        }
        if (nextElement &&
            isMarkupElement(nextElement) &&
            nextElement.open[0] === element.close[0] &&
            !nextElement.close.length &&
            nextElement[nextElement.open[0]] === lastPers[nextElement.open[0]]) {
            if (pauseElement) {
                appendElement_(result, pauseElement);
                i = i + 2;
            }
            else {
                i = i + 1;
            }
        }
        else {
            copyValues_(element, lastPers);
            result.push(element);
        }
    }
    return result;
}
function copyValues_(from, to) {
    if (from['rate']) {
        to['rate'] = from['rate'];
    }
    if (from['pitch']) {
        to['pitch'] = from['pitch'];
    }
    if (from['volume']) {
        to['volume'] = from['volume'];
    }
}
function finaliseMarkup_() {
    const final = [];
    for (let i = LastOpen_.length - 1; i >= 0; i--) {
        const pers = LastOpen_[i];
        if (pers.length) {
            const markup = { open: [], close: [] };
            for (let j = 0; j < pers.length; j++) {
                const per = pers[j];
                markup.close.push(per);
                markup[per] = 0;
            }
            final.push(markup);
        }
    }
    return final;
}
function isMarkupElement(element) {
    return typeof element === 'object' && element.open;
}
exports.isMarkupElement = isMarkupElement;
function isPauseElement(element) {
    return (typeof element === 'object' &&
        Object.keys(element).length === 1 &&
        Object.keys(element)[0] === EngineConst.personalityProps.PAUSE);
}
exports.isPauseElement = isPauseElement;
function isSpanElement(element) {
    const keys = Object.keys(element);
    return (typeof element === 'object' &&
        ((keys.length === 1 && keys[0] === 'span') ||
            (keys.length === 2 &&
                ((keys[0] === 'span' && keys[1] === 'join') ||
                    (keys[1] === 'span' && keys[0] === 'join')))));
}
exports.isSpanElement = isSpanElement;
function appendMarkup_(markup, span, pers, join, pause, merge = false) {
    if (merge) {
        const last = markup[markup.length - 1];
        let oldJoin;
        if (last) {
            oldJoin = last[EngineConst.personalityProps.JOIN];
        }
        if (last && !span.speech && pause && isPauseElement(last)) {
            const pauseProp = EngineConst.personalityProps.PAUSE;
            last[pauseProp] = mergePause_(last[pauseProp], pause[pauseProp]);
            pause = null;
        }
        if (last &&
            span.speech &&
            Object.keys(pers).length === 0 &&
            isSpanElement(last)) {
            if (typeof oldJoin !== 'undefined') {
                const lastSpan = last['span'].pop();
                span = new span_1.Span(lastSpan.speech + oldJoin + span.speech, lastSpan.attributes);
            }
            last['span'].push(span);
            span = new span_1.Span('', {});
            last[EngineConst.personalityProps.JOIN] = join;
        }
    }
    if (Object.keys(pers).length !== 0) {
        markup.push(pers);
    }
    if (span.speech) {
        markup.push({ span: [span], join: join });
    }
    if (pause) {
        markup.push(pause);
    }
}
function personalityDiff_(current, old) {
    if (!old) {
        return current;
    }
    const result = {};
    for (const prop of EngineConst.personalityPropList) {
        const currentValue = current[prop];
        const oldValue = old[prop];
        if ((!currentValue && !oldValue) ||
            (currentValue && oldValue && currentValue === oldValue)) {
            continue;
        }
        const value = currentValue || 0;
        if (!isMarkupElement(result)) {
            result.open = [];
            result.close = [];
        }
        if (!currentValue) {
            result.close.push(prop);
        }
        if (!oldValue) {
            result.open.push(prop);
        }
        if (oldValue && currentValue) {
            result.close.push(prop);
            result.open.push(prop);
        }
        old[prop] = value;
        result[prop] = value;
        PersonalityRanges_[prop]
            ? PersonalityRanges_[prop].push(value)
            : (PersonalityRanges_[prop] = [value]);
    }
    if (isMarkupElement(result)) {
        let c = result.close.slice();
        while (c.length > 0) {
            let lo = LastOpen_.pop();
            const loNew = (0, base_util_1.setdifference)(lo, c);
            c = (0, base_util_1.setdifference)(c, lo);
            lo = loNew;
            if (c.length === 0) {
                if (lo.length !== 0) {
                    LastOpen_.push(lo);
                }
                continue;
            }
            if (lo.length === 0) {
                continue;
            }
            result.close = result.close.concat(lo);
            result.open = result.open.concat(lo);
            for (let i = 0, open; (open = lo[i]); i++) {
                result[open] = old[open];
            }
        }
        LastOpen_.push(result.open);
    }
    return result;
}


/***/ }),

/***/ 4148:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AuditoryDescription = void 0;
const grammar_1 = __webpack_require__(1058);
const span_1 = __webpack_require__(1930);
class AuditoryDescription {
    constructor({ context, text, userValue, annotation, attributes, personality, layout }) {
        this.context = context || '';
        this.text = text || '';
        this.userValue = userValue || '';
        this.annotation = annotation || '';
        this.attributes = attributes || {};
        this.personality = personality || {};
        this.layout = layout || '';
    }
    static create(args, flags = {}) {
        args.text = grammar_1.Grammar.getInstance().apply(args.text, flags);
        return new AuditoryDescription(args);
    }
    isEmpty() {
        return (this.context.length === 0 &&
            this.text.length === 0 &&
            this.userValue.length === 0 &&
            this.annotation.length === 0);
    }
    clone() {
        let personality;
        if (this.personality) {
            personality = {};
            for (const key in this.personality) {
                personality[key] = this.personality[key];
            }
        }
        let attributes;
        if (this.attributes) {
            attributes = {};
            for (const key in this.attributes) {
                attributes[key] = this.attributes[key];
            }
        }
        return new AuditoryDescription({
            context: this.context,
            text: this.text,
            userValue: this.userValue,
            annotation: this.annotation,
            personality: personality,
            attributes: attributes,
            layout: this.layout
        });
    }
    toString() {
        return ('AuditoryDescription(context="' +
            this.context +
            '" ' +
            ' text="' +
            this.text +
            '" ' +
            ' userValue="' +
            this.userValue +
            '" ' +
            ' annotation="' +
            this.annotation +
            '")');
    }
    descriptionString() {
        return this.context && this.text
            ? this.context + ' ' + this.text
            : this.context || this.text;
    }
    descriptionSpan() {
        return new span_1.Span(this.descriptionString(), this.attributes);
    }
    equals(that) {
        return (this.context === that.context &&
            this.text === that.text &&
            this.userValue === that.userValue &&
            this.annotation === that.annotation);
    }
}
exports.AuditoryDescription = AuditoryDescription;


/***/ }),

/***/ 4253:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.isXml = exports.registerRenderer = exports.error = exports.finalize = exports.merge = exports.markup = exports.getSeparator = exports.setSeparator = void 0;
const engine_1 = __webpack_require__(4886);
const EngineConst = __webpack_require__(4998);
const acss_renderer_1 = __webpack_require__(9202);
const layout_renderer_1 = __webpack_require__(1292);
const punctuation_renderer_1 = __webpack_require__(1674);
const sable_renderer_1 = __webpack_require__(8078);
const span_1 = __webpack_require__(1930);
const ssml_renderer_1 = __webpack_require__(4115);
const ssml_step_renderer_1 = __webpack_require__(6123);
const string_renderer_1 = __webpack_require__(8244);
const xml_renderer_1 = __webpack_require__(4708);
const xmlInstance = new ssml_renderer_1.SsmlRenderer();
const renderers = new Map([
    [EngineConst.Markup.NONE, new string_renderer_1.StringRenderer()],
    [EngineConst.Markup.PUNCTUATION, new punctuation_renderer_1.PunctuationRenderer()],
    [EngineConst.Markup.LAYOUT, new layout_renderer_1.LayoutRenderer()],
    [EngineConst.Markup.ACSS, new acss_renderer_1.AcssRenderer()],
    [EngineConst.Markup.SABLE, new sable_renderer_1.SableRenderer()],
    [EngineConst.Markup.VOICEXML, xmlInstance],
    [EngineConst.Markup.SSML, xmlInstance],
    [EngineConst.Markup.SSML_STEP, new ssml_step_renderer_1.SsmlStepRenderer()]
]);
function setSeparator(sep) {
    const renderer = renderers.get(engine_1.default.getInstance().markup);
    if (renderer) {
        renderer.setSeparator(sep);
    }
}
exports.setSeparator = setSeparator;
function getSeparator() {
    const renderer = renderers.get(engine_1.default.getInstance().markup);
    return renderer ? renderer.getSeparator() : '';
}
exports.getSeparator = getSeparator;
function markup(descrs) {
    const renderer = renderers.get(engine_1.default.getInstance().markup);
    if (!renderer) {
        return '';
    }
    return renderer.markup(descrs);
}
exports.markup = markup;
function merge(strs) {
    const span = strs.map((s) => {
        return typeof s === 'string' ? new span_1.Span(s, {}) : s;
    });
    const renderer = renderers.get(engine_1.default.getInstance().markup);
    if (!renderer) {
        return strs.join();
    }
    return renderer.merge(span);
}
exports.merge = merge;
function finalize(str) {
    const renderer = renderers.get(engine_1.default.getInstance().markup);
    if (!renderer) {
        return str;
    }
    return renderer.finalize(str);
}
exports.finalize = finalize;
function error(key) {
    const renderer = renderers.get(engine_1.default.getInstance().markup);
    if (!renderer) {
        return '';
    }
    return renderer.error(key);
}
exports.error = error;
function registerRenderer(type, renderer) {
    renderers.set(type, renderer);
}
exports.registerRenderer = registerRenderer;
function isXml() {
    return renderers.get(engine_1.default.getInstance().markup) instanceof xml_renderer_1.XmlRenderer;
}
exports.isXml = isXml;


/***/ }),

/***/ 1292:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.LayoutRenderer = void 0;
const debugger_1 = __webpack_require__(1984);
const DomUtil = __webpack_require__(6671);
const EngineConst = __webpack_require__(4998);
const AudioUtil = __webpack_require__(2599);
const xml_renderer_1 = __webpack_require__(4708);
class LayoutRenderer extends xml_renderer_1.XmlRenderer {
    finalize(str) {
        return setTwoDim(str);
    }
    pause(_pause) {
        return '';
    }
    prosodyElement(attr, value) {
        return attr === EngineConst.personalityProps.LAYOUT ? `<${value}>` : '';
    }
    closeTag(tag) {
        return `</${tag}>`;
    }
    markup(descrs) {
        const result = [];
        let content = [];
        for (const descr of descrs) {
            if (!descr.layout) {
                content.push(descr);
                continue;
            }
            result.push(this.processContent(content));
            content = [];
            const value = descr.layout;
            if (value.match(/^begin/)) {
                result.push('<' + value.replace(/^begin/, '') + '>');
                continue;
            }
            if (value.match(/^end/)) {
                result.push('</' + value.replace(/^end/, '') + '>');
                continue;
            }
            console.warn('Something went wrong with layout markup: ' + value);
        }
        result.push(this.processContent(content));
        return result.join('');
    }
    processContent(content) {
        const result = [];
        const markup = AudioUtil.personalityMarkup(content);
        for (let i = 0, descr; (descr = markup[i]); i++) {
            if (descr.span) {
                result.push(this.merge(descr.span));
                continue;
            }
            if (AudioUtil.isPauseElement(descr)) {
                continue;
            }
        }
        return result.join('');
    }
}
exports.LayoutRenderer = LayoutRenderer;
let twodExpr = '';
const handlers = {
    TABLE: handleTable,
    CASES: handleCases,
    CAYLEY: handleCayley,
    MATRIX: handleMatrix,
    CELL: recurseTree,
    FENCE: recurseTree,
    ROW: recurseTree,
    FRACTION: handleFraction,
    NUMERATOR: handleFractionPart,
    DENOMINATOR: handleFractionPart
};
function applyHandler(element) {
    const tag = DomUtil.tagName(element);
    const handler = handlers[tag];
    return handler ? handler(element) : element.textContent;
}
function setTwoDim(str) {
    twodExpr = '';
    const dom = DomUtil.parseInput(`<all>${str}</all>`);
    debugger_1.Debugger.getInstance().output(DomUtil.formatXml(dom.toString()));
    twodExpr = recurseTree(dom);
    return twodExpr;
}
function combineContent(str1, str2) {
    if (!str1 || !str2) {
        return str1 + str2;
    }
    const height1 = strHeight(str1);
    const height2 = strHeight(str2);
    const diff = height1 - height2;
    str1 = diff < 0 ? padCell(str1, height2, strWidth(str1)) : str1;
    str2 = diff > 0 ? padCell(str2, height1, strWidth(str2)) : str2;
    const lines1 = str1.split(/\r\n|\r|\n/);
    const lines2 = str2.split(/\r\n|\r|\n/);
    const result = [];
    for (let i = 0; i < lines1.length; i++) {
        result.push(lines1[i] + lines2[i]);
    }
    return result.join('\n');
}
function recurseTree(dom) {
    let result = '';
    for (const child of Array.from(dom.childNodes)) {
        if (child.nodeType === DomUtil.NodeType.TEXT_NODE) {
            result = combineContent(result, child.textContent);
            continue;
        }
        result = combineContent(result, applyHandler(child));
    }
    return result;
}
function strHeight(str) {
    return str.split(/\r\n|\r|\n/).length;
}
function strWidth(str) {
    return str.split(/\r\n|\r|\n/).reduce((max, x) => Math.max(x.length, max), 0);
}
function padHeight(str, height) {
    const padding = height - strHeight(str);
    return str + (padding > 0 ? new Array(padding + 1).join('\n') : '');
}
function padWidth(str, width) {
    const lines = str.split(/\r\n|\r|\n/);
    const result = [];
    for (const line of lines) {
        const padding = width - line.length;
        result.push(line + (padding > 0 ? new Array(padding + 1).join('⠀') : ''));
    }
    return result.join('\n');
}
function padCell(str, height, width) {
    str = padHeight(str, height);
    return padWidth(str, width);
}
function assembleRows(matrix) {
    const children = Array.from(matrix.childNodes);
    const mat = [];
    for (const row of children) {
        if (row.nodeType !== DomUtil.NodeType.ELEMENT_NODE) {
            continue;
        }
        mat.push(handleRow(row));
    }
    return mat;
}
function getMaxParameters(mat) {
    const maxHeight = mat.reduce((max, x) => Math.max(x.height, max), 0);
    const maxWidth = [];
    for (let i = 0; i < mat[0].width.length; i++) {
        maxWidth.push(mat.map((x) => x.width[i]).reduce((max, x) => Math.max(max, x), 0));
    }
    return [maxHeight, maxWidth];
}
function combineCells(mat, maxWidth) {
    const newMat = [];
    for (const row of mat) {
        if (row.height === 0) {
            continue;
        }
        const newCells = [];
        for (let i = 0; i < row.cells.length; i++) {
            newCells.push(padCell(row.cells[i], row.height, maxWidth[i]));
        }
        row.cells = newCells;
        newMat.push(row);
    }
    return newMat;
}
function combineRows(mat, maxHeight) {
    if (maxHeight === 1) {
        return mat
            .map((row) => row.lfence + row.cells.join(row.sep) + row.rfence)
            .join('\n');
    }
    const result = [];
    for (const row of mat) {
        const sep = verticalArrange(row.sep, row.height);
        let str = row.cells.shift();
        while (row.cells.length) {
            str = combineContent(str, sep);
            str = combineContent(str, row.cells.shift());
        }
        str = combineContent(verticalArrange(row.lfence, row.height), str);
        str = combineContent(str, verticalArrange(row.rfence, row.height));
        result.push(str);
        result.push(row.lfence + new Array(strWidth(str) - 3).join(row.sep) + row.rfence);
    }
    return result.slice(0, -1).join('\n');
}
function verticalArrange(char, height) {
    let str = '';
    while (height) {
        str += char + '\n';
        height--;
    }
    return str.slice(0, -1);
}
function getFence(node) {
    if (node.nodeType === DomUtil.NodeType.ELEMENT_NODE &&
        DomUtil.tagName(node) === 'FENCE') {
        return applyHandler(node);
    }
    return '';
}
function handleMatrix(matrix) {
    let mat = assembleRows(matrix);
    const [maxHeight, maxWidth] = getMaxParameters(mat);
    mat = combineCells(mat, maxWidth);
    return combineRows(mat, maxHeight);
}
function handleTable(table) {
    let mat = assembleRows(table);
    mat.forEach((row) => {
        row.cells = row.cells.slice(1).slice(0, -1);
        row.width = row.width.slice(1).slice(0, -1);
    });
    const [maxHeight, maxWidth] = getMaxParameters(mat);
    mat = combineCells(mat, maxWidth);
    return combineRows(mat, maxHeight);
}
function handleCases(cases) {
    let mat = assembleRows(cases);
    mat.forEach((row) => {
        row.cells = row.cells.slice(0, -1);
        row.width = row.width.slice(0, -1);
    });
    const [maxHeight, maxWidth] = getMaxParameters(mat);
    mat = combineCells(mat, maxWidth);
    return combineRows(mat, maxHeight);
}
function handleCayley(cayley) {
    let mat = assembleRows(cayley);
    mat.forEach((row) => {
        row.cells = row.cells.slice(1).slice(0, -1);
        row.width = row.width.slice(1).slice(0, -1);
        row.sep = row.sep + row.sep;
    });
    const [maxHeight, maxWidth] = getMaxParameters(mat);
    const bar = {
        lfence: '',
        rfence: '',
        cells: maxWidth.map((x) => '⠐' + new Array(x).join('⠒')),
        width: maxWidth,
        height: 1,
        sep: mat[0].sep
    };
    mat.splice(1, 0, bar);
    mat = combineCells(mat, maxWidth);
    return combineRows(mat, maxHeight);
}
function handleRow(row) {
    const children = Array.from(row.childNodes);
    const lfence = getFence(children[0]);
    const rfence = getFence(children[children.length - 1]);
    if (lfence) {
        children.shift();
    }
    if (rfence) {
        children.pop();
    }
    let sep = '';
    const cells = [];
    for (const child of children) {
        if (child.nodeType === DomUtil.NodeType.TEXT_NODE) {
            sep = child.textContent;
            continue;
        }
        const result = applyHandler(child);
        cells.push(result);
    }
    return {
        lfence: lfence,
        rfence: rfence,
        sep: sep,
        cells: cells,
        height: cells.reduce((max, x) => Math.max(strHeight(x), max), 0),
        width: cells.map(strWidth)
    };
}
function centerCell(cell, width) {
    const cw = strWidth(cell);
    const center = (width - cw) / 2;
    const [lpad, rpad] = Math.floor(center) === center
        ? [center, center]
        : [Math.floor(center), Math.ceil(center)];
    const lines = cell.split(/\r\n|\r|\n/);
    const result = [];
    const [lstr, rstr] = [
        new Array(lpad + 1).join('⠀'),
        new Array(rpad + 1).join('⠀')
    ];
    for (const line of lines) {
        result.push(lstr + line + rstr);
    }
    return result.join('\n');
}
function handleFraction(frac) {
    const [open, num, , den, close] = Array.from(frac.childNodes);
    const numerator = applyHandler(num);
    const denominator = applyHandler(den);
    const nwidth = strWidth(numerator);
    const dwidth = strWidth(denominator);
    let maxWidth = Math.max(nwidth, dwidth);
    const bar = open + new Array(maxWidth + 1).join('⠒') + close;
    maxWidth = bar.length;
    return (`${centerCell(numerator, maxWidth)}\n${bar}\n` +
        `${centerCell(denominator, maxWidth)}`);
}
function handleFractionPart(prt) {
    const fchild = prt.firstChild;
    const content = recurseTree(prt);
    if (fchild && fchild.nodeType === DomUtil.NodeType.ELEMENT_NODE) {
        if (DomUtil.tagName(fchild) === 'ENGLISH') {
            return '⠰' + content;
        }
        if (DomUtil.tagName(fchild) === 'NUMBER') {
            return '⠼' + content;
        }
    }
    return content;
}


/***/ }),

/***/ 9610:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MarkupRenderer = void 0;
const EngineConst = __webpack_require__(4998);
const abstract_audio_renderer_1 = __webpack_require__(7086);
class MarkupRenderer extends abstract_audio_renderer_1.AbstractAudioRenderer {
    constructor() {
        super(...arguments);
        this.ignoreElements = [EngineConst.personalityProps.LAYOUT];
        this.scaleFunction = null;
    }
    setScaleFunction(a, b, c, d, decimals = 0) {
        this.scaleFunction = (x) => {
            const delta = (x - a) / (b - a);
            const num = c * (1 - delta) + d * delta;
            return +(Math.round((num + 'e+' + decimals)) +
                'e-' +
                decimals);
        };
    }
    applyScaleFunction(value) {
        return this.scaleFunction ? this.scaleFunction(value) : value;
    }
    ignoreElement(key) {
        return this.ignoreElements.indexOf(key) !== -1;
    }
}
exports.MarkupRenderer = MarkupRenderer;


/***/ }),

/***/ 1674:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.PunctuationRenderer = void 0;
const EngineConst = __webpack_require__(4998);
const abstract_audio_renderer_1 = __webpack_require__(7086);
const AudioUtil = __webpack_require__(2599);
class PunctuationRenderer extends abstract_audio_renderer_1.AbstractAudioRenderer {
    markup(descrs) {
        const markup = AudioUtil.personalityMarkup(descrs);
        let str = '';
        let pause = null;
        let span = false;
        for (let i = 0, descr; (descr = markup[i]); i++) {
            if (AudioUtil.isMarkupElement(descr)) {
                continue;
            }
            if (AudioUtil.isPauseElement(descr)) {
                if (span) {
                    pause = AudioUtil.mergePause(pause, descr, Math.max);
                }
                continue;
            }
            if (pause) {
                str += this.pause(pause[EngineConst.personalityProps.PAUSE]);
                pause = null;
            }
            str += (span ? this.getSeparator() : '') + this.merge(descr.span);
            span = true;
        }
        return str;
    }
    pause(pause) {
        let newPause;
        if (typeof pause === 'number') {
            if (pause <= 250) {
                newPause = 'short';
            }
            else if (pause <= 500) {
                newPause = 'medium';
            }
            else {
                newPause = 'long';
            }
        }
        else {
            newPause = pause;
        }
        return PunctuationRenderer.PAUSE_PUNCTUATION.get(newPause) || '';
    }
}
exports.PunctuationRenderer = PunctuationRenderer;
PunctuationRenderer.PAUSE_PUNCTUATION = new Map([
    ['short', ','],
    ['medium', ';'],
    ['long', '.']
]);


/***/ }),

/***/ 8078:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SableRenderer = void 0;
const EngineConst = __webpack_require__(4998);
const xml_renderer_1 = __webpack_require__(4708);
class SableRenderer extends xml_renderer_1.XmlRenderer {
    finalize(str) {
        return ('<?xml version="1.0"?>' +
            '<!DOCTYPE SABLE PUBLIC "-//SABLE//DTD SABLE speech mark up//EN"' +
            ' "Sable.v0_2.dtd" []><SABLE>' +
            this.getSeparator() +
            str +
            this.getSeparator() +
            '</SABLE>');
    }
    pause(pause) {
        return ('<BREAK ' +
            'MSEC="' +
            this.pauseValue(pause[EngineConst.personalityProps.PAUSE]) +
            '"/>');
    }
    prosodyElement(tag, value) {
        value = this.applyScaleFunction(value);
        switch (tag) {
            case EngineConst.personalityProps.PITCH:
                return '<PITCH RANGE="' + value + '%">';
            case EngineConst.personalityProps.RATE:
                return '<RATE SPEED="' + value + '%">';
            case EngineConst.personalityProps.VOLUME:
                return '<VOLUME LEVEL="' + value + '%">';
            default:
                return '<' + tag.toUpperCase() + ' VALUE="' + value + '">';
        }
    }
    closeTag(tag) {
        return '</' + tag.toUpperCase() + '>';
    }
}
exports.SableRenderer = SableRenderer;


/***/ }),

/***/ 1930:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Span = void 0;
class Span {
    constructor(speech, attributes) {
        this.speech = speech;
        this.attributes = attributes;
    }
}
exports.Span = Span;


/***/ }),

/***/ 4115:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SsmlRenderer = void 0;
const engine_1 = __webpack_require__(4886);
const EngineConst = __webpack_require__(4998);
const xml_renderer_1 = __webpack_require__(4708);
class SsmlRenderer extends xml_renderer_1.XmlRenderer {
    finalize(str) {
        return ('<?xml version="1.0"?><speak version="1.1"' +
            ' xmlns="http://www.w3.org/2001/10/synthesis">' +
            '<prosody rate="' +
            engine_1.default.getInstance().getRate() +
            '%">' +
            this.getSeparator() +
            str +
            this.getSeparator() +
            '</prosody></speak>');
    }
    pause(pause) {
        return ('<break ' +
            'time="' +
            this.pauseValue(pause[EngineConst.personalityProps.PAUSE]) +
            'ms"/>');
    }
    prosodyElement(attr, value) {
        value = Math.floor(this.applyScaleFunction(value));
        const valueStr = value < 0 ? value.toString() : '+' + value.toString();
        return ('<prosody ' +
            attr.toLowerCase() +
            '="' +
            valueStr +
            (attr === EngineConst.personalityProps.VOLUME ? '>' : '%">'));
    }
    closeTag(_tag) {
        return '</prosody>';
    }
}
exports.SsmlRenderer = SsmlRenderer;


/***/ }),

/***/ 6123:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SsmlStepRenderer = void 0;
const ssml_renderer_1 = __webpack_require__(4115);
class SsmlStepRenderer extends ssml_renderer_1.SsmlRenderer {
    markup(descrs) {
        SsmlStepRenderer.MARKS = {};
        return super.markup(descrs);
    }
    merge(spans) {
        const result = [];
        for (let i = 0; i < spans.length; i++) {
            const span = spans[i];
            const id = span.attributes['extid'];
            if (id && !SsmlStepRenderer.MARKS[id]) {
                result.push('<mark name="' + id + '"/>');
                SsmlStepRenderer.MARKS[id] = true;
            }
            if (span.speech.length === 1 && span.speech.match(/[a-zA-Z]/)) {
                result.push('<say-as interpret-as="' +
                    SsmlStepRenderer.CHARACTER_ATTR +
                    '">' +
                    span.speech +
                    '</say-as>');
            }
            else {
                result.push(span.speech);
            }
        }
        return result.join(this.getSeparator());
    }
}
exports.SsmlStepRenderer = SsmlStepRenderer;
SsmlStepRenderer.CHARACTER_ATTR = 'character';
SsmlStepRenderer.MARKS = {};


/***/ }),

/***/ 8244:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.StringRenderer = void 0;
const abstract_audio_renderer_1 = __webpack_require__(7086);
const audio_util_1 = __webpack_require__(2599);
class StringRenderer extends abstract_audio_renderer_1.AbstractAudioRenderer {
    markup(descrs) {
        let str = '';
        const markup = (0, audio_util_1.personalityMarkup)(descrs);
        const clean = markup.filter((x) => x.span);
        if (!clean.length) {
            return str;
        }
        const len = clean.length - 1;
        for (let i = 0, descr; (descr = clean[i]); i++) {
            if (descr.span) {
                str += this.merge(descr.span);
            }
            if (i >= len) {
                continue;
            }
            const join = descr.join;
            str += typeof join === 'undefined' ? this.getSeparator() : join;
        }
        return str;
    }
}
exports.StringRenderer = StringRenderer;


/***/ }),

/***/ 4708:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.XmlRenderer = void 0;
const engine_1 = __webpack_require__(4886);
const AudioUtil = __webpack_require__(2599);
const markup_renderer_1 = __webpack_require__(9610);
class XmlRenderer extends markup_renderer_1.MarkupRenderer {
    markup(descrs) {
        this.setScaleFunction(-2, 2, -100, 100, 2);
        const markup = AudioUtil.personalityMarkup(descrs);
        const result = [];
        const currentOpen = [];
        for (let i = 0, descr; (descr = markup[i]); i++) {
            if (descr.span) {
                result.push(this.merge(descr.span));
                continue;
            }
            if (AudioUtil.isPauseElement(descr)) {
                result.push(this.pause(descr));
                continue;
            }
            if (descr.close.length) {
                for (let j = 0; j < descr.close.length; j++) {
                    const last = currentOpen.pop();
                    if (descr.close.indexOf(last) === -1) {
                        throw new engine_1.SREError('Unknown closing markup element: ' + last);
                    }
                    result.push(this.closeTag(last));
                }
            }
            if (descr.open.length) {
                const open = AudioUtil.sortClose(descr.open.slice(), markup.slice(i + 1));
                open.forEach((o) => {
                    result.push(this.prosodyElement(o, descr[o]));
                    currentOpen.push(o);
                });
            }
        }
        return result.join(' ');
    }
}
exports.XmlRenderer = XmlRenderer;


/***/ }),

/***/ 1426:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.union = exports.setdifference = exports.interleaveLists = exports.removeEmpty = void 0;
function removeEmpty(strs) {
    return strs.filter((str) => str);
}
exports.removeEmpty = removeEmpty;
function interleaveLists(list1, list2) {
    const result = [];
    while (list1.length || list2.length) {
        list1.length && result.push(list1.shift());
        list2.length && result.push(list2.shift());
    }
    return result;
}
exports.interleaveLists = interleaveLists;
function setdifference(a, b) {
    if (!a) {
        return [];
    }
    if (!b) {
        return a;
    }
    return a.filter((x) => b.indexOf(x) < 0);
}
exports.setdifference = setdifference;
function union(a, b) {
    if (!a || !b) {
        return a || b || [];
    }
    return a.concat(setdifference(b, a));
}
exports.union = union;


/***/ }),

/***/ 9501:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.loadScript = exports.loadMapsForIE_ = exports.installWGXpath_ = exports.loadWGXpath_ = exports.mapsForIE = exports.detectEdge = exports.detectIE = void 0;
const system_external_1 = __webpack_require__(4755);
const xpath_util_1 = __webpack_require__(5024);
function detectIE() {
    const isIE = typeof window !== 'undefined' &&
        'ActiveXObject' in window &&
        'clipboardData' in window;
    if (!isIE) {
        return false;
    }
    loadMapsForIE_();
    loadWGXpath_();
    return true;
}
exports.detectIE = detectIE;
function detectEdge() {
    var _a;
    const isEdge = typeof window !== 'undefined' &&
        'MSGestureEvent' in window &&
        ((_a = window.chrome) === null || _a === void 0 ? void 0 : _a.loadTimes) === null;
    if (!isEdge) {
        return false;
    }
    document.evaluate = null;
    loadWGXpath_(true);
    return true;
}
exports.detectEdge = detectEdge;
exports.mapsForIE = null;
function loadWGXpath_(opt_isEdge) {
    loadScript(system_external_1.default.WGXpath);
    installWGXpath_(opt_isEdge);
}
exports.loadWGXpath_ = loadWGXpath_;
function installWGXpath_(opt_isEdge, opt_count) {
    let count = opt_count || 1;
    if (typeof wgxpath === 'undefined' && count < 10) {
        setTimeout(function () {
            installWGXpath_(opt_isEdge, count++);
        }, 200);
        return;
    }
    if (count >= 10) {
        return;
    }
    system_external_1.default.wgxpath = wgxpath;
    opt_isEdge
        ? system_external_1.default.wgxpath.install({ document: document })
        : system_external_1.default.wgxpath.install();
    xpath_util_1.xpath.evaluate = document.evaluate;
    xpath_util_1.xpath.result = XPathResult;
    xpath_util_1.xpath.createNSResolver = document.createNSResolver;
}
exports.installWGXpath_ = installWGXpath_;
function loadMapsForIE_() {
    loadScript(system_external_1.default.mathmapsIePath);
}
exports.loadMapsForIE_ = loadMapsForIE_;
function loadScript(src) {
    const scr = system_external_1.default.document.createElement('script');
    scr.type = 'text/javascript';
    scr.src = src;
    system_external_1.default.document.head
        ? system_external_1.default.document.head.appendChild(scr)
        : system_external_1.default.document.body.appendChild(scr);
}
exports.loadScript = loadScript;


/***/ }),

/***/ 1984:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Debugger = void 0;
const system_external_1 = __webpack_require__(4755);
class Debugger {
    constructor() {
        this.isActive_ = false;
        this.outputFunction_ = console.info;
        this.stream_ = null;
    }
    static getInstance() {
        Debugger.instance = Debugger.instance || new Debugger();
        return Debugger.instance;
    }
    init(opt_file) {
        if (opt_file) {
            this.startDebugFile_(opt_file);
        }
        this.isActive_ = true;
    }
    output(...args) {
        if (this.isActive_) {
            this.output_(args);
        }
    }
    generateOutput(func) {
        if (this.isActive_) {
            this.output_(func.apply(func, []));
        }
    }
    exit(callback = () => { }) {
        if (this.isActive_ && this.stream_) {
            this.stream_.end('', '', callback);
        }
    }
    startDebugFile_(filename) {
        this.stream_ = system_external_1.default.fs.createWriteStream(filename);
        this.outputFunction_ = function (...args) {
            this.stream_.write(args.join(' '));
            this.stream_.write('\n');
        }.bind(this);
        this.stream_.on('error', function (_error) {
            console.info('Invalid log file. Debug information sent to console.');
            this.outputFunction_ = console.info;
        }.bind(this));
        this.stream_.on('finish', function () {
            console.info('Finalizing debug file.');
        });
    }
    output_(outputList) {
        this.outputFunction_.apply(console.info === this.outputFunction_ ? console : this.outputFunction_, ['Speech Rule Engine Debugger:'].concat(outputList));
    }
}
exports.Debugger = Debugger;


/***/ }),

/***/ 6671:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.serializeXml = exports.cloneNode = exports.tagName = exports.querySelectorAll = exports.querySelectorAllByAttrValue = exports.querySelectorAllByAttr = exports.formatXml = exports.createTextNode = exports.createElementNS = exports.createElement = exports.replaceNode = exports.NodeType = exports.parseInput = exports.XML_ENTITIES = exports.trimInput_ = exports.toArray = void 0;
const engine_1 = __webpack_require__(4886);
const EngineConst = __webpack_require__(4998);
const system_external_1 = __webpack_require__(4755);
const XpathUtil = __webpack_require__(5024);
function toArray(nodeList) {
    const nodeArray = [];
    for (let i = 0, m = nodeList.length; i < m; i++) {
        nodeArray.push(nodeList[i]);
    }
    return nodeArray;
}
exports.toArray = toArray;
function trimInput_(input) {
    input = input.replace(/&nbsp;/g, ' ');
    return input.replace(/>[ \f\n\r\t\v\u200b]+</g, '><').trim();
}
exports.trimInput_ = trimInput_;
exports.XML_ENTITIES = {
    '&lt;': true,
    '&gt;': true,
    '&amp;': true,
    '&quot;': true,
    '&apos;': true
};
function parseInput(input) {
    const dp = new system_external_1.default.xmldom.DOMParser();
    const clean_input = trimInput_(input);
    const allValues = clean_input.match(/&(?!lt|gt|amp|quot|apos)\w+;/g);
    const html = !!allValues;
    if (!clean_input) {
        throw new Error('Empty input!');
    }
    try {
        const doc = dp.parseFromString(clean_input, html ? 'text/html' : 'text/xml');
        if (engine_1.default.getInstance().mode === EngineConst.Mode.HTTP) {
            XpathUtil.xpath.currentDocument = doc;
            return html ? doc.body.childNodes[0] : doc.documentElement;
        }
        return doc.documentElement;
    }
    catch (err) {
        throw new engine_1.SREError('Illegal input: ' + err.message);
    }
}
exports.parseInput = parseInput;
var NodeType;
(function (NodeType) {
    NodeType[NodeType["ELEMENT_NODE"] = 1] = "ELEMENT_NODE";
    NodeType[NodeType["ATTRIBUTE_NODE"] = 2] = "ATTRIBUTE_NODE";
    NodeType[NodeType["TEXT_NODE"] = 3] = "TEXT_NODE";
    NodeType[NodeType["CDATA_SECTION_NODE"] = 4] = "CDATA_SECTION_NODE";
    NodeType[NodeType["ENTITY_REFERENCE_NODE"] = 5] = "ENTITY_REFERENCE_NODE";
    NodeType[NodeType["ENTITY_NODE"] = 6] = "ENTITY_NODE";
    NodeType[NodeType["PROCESSING_INSTRUCTION_NODE"] = 7] = "PROCESSING_INSTRUCTION_NODE";
    NodeType[NodeType["COMMENT_NODE"] = 8] = "COMMENT_NODE";
    NodeType[NodeType["DOCUMENT_NODE"] = 9] = "DOCUMENT_NODE";
    NodeType[NodeType["DOCUMENT_TYPE_NODE"] = 10] = "DOCUMENT_TYPE_NODE";
    NodeType[NodeType["DOCUMENT_FRAGMENT_NODE"] = 11] = "DOCUMENT_FRAGMENT_NODE";
    NodeType[NodeType["NOTATION_NODE"] = 12] = "NOTATION_NODE";
})(NodeType = exports.NodeType || (exports.NodeType = {}));
function replaceNode(oldNode, newNode) {
    if (!oldNode.parentNode) {
        return;
    }
    oldNode.parentNode.insertBefore(newNode, oldNode);
    oldNode.parentNode.removeChild(oldNode);
}
exports.replaceNode = replaceNode;
function createElement(tag) {
    return system_external_1.default.document.createElement(tag);
}
exports.createElement = createElement;
function createElementNS(url, tag) {
    return system_external_1.default.document.createElementNS(url, tag);
}
exports.createElementNS = createElementNS;
function createTextNode(content) {
    return system_external_1.default.document.createTextNode(content);
}
exports.createTextNode = createTextNode;
function formatXml(xml) {
    let formatted = '';
    let reg = /(>)(<)(\/*)/g;
    xml = xml.replace(reg, '$1\r\n$2$3');
    let pad = 0;
    let split = xml.split('\r\n');
    reg = /(\.)*(<)(\/*)/g;
    split = split
        .map((x) => x.replace(reg, '$1\r\n$2$3').split('\r\n'))
        .reduce((x, y) => x.concat(y), []);
    while (split.length) {
        let node = split.shift();
        if (!node) {
            continue;
        }
        let indent = 0;
        if (node.match(/^<\w[^>/]*>[^>]+$/)) {
            const match = matchingStartEnd(node, split[0]);
            if (match[0]) {
                if (match[1]) {
                    node = node + split.shift().slice(0, -match[1].length);
                    if (match[1].trim()) {
                        split.unshift(match[1]);
                    }
                }
                else {
                    node = node + split.shift();
                }
            }
            else {
                indent = 1;
            }
        }
        else if (node.match(/^<\/\w/)) {
            if (pad !== 0) {
                pad -= 1;
            }
        }
        else if (node.match(/^<\w[^>]*[^/]>.*$/)) {
            indent = 1;
        }
        else if (node.match(/^<\w[^>]*\/>.+$/)) {
            const position = node.indexOf('>') + 1;
            const rest = node.slice(position);
            if (rest.trim()) {
                split.unshift();
            }
            node = node.slice(0, position);
        }
        else {
            indent = 0;
        }
        formatted += new Array(pad + 1).join('  ') + node + '\r\n';
        pad += indent;
    }
    return formatted;
}
exports.formatXml = formatXml;
function matchingStartEnd(start, end) {
    if (!end) {
        return [false, ''];
    }
    const tag1 = start.match(/^<([^> ]+).*>/);
    const tag2 = end.match(/^<\/([^>]+)>(.*)/);
    return tag1 && tag2 && tag1[1] === tag2[1] ? [true, tag2[2]] : [false, ''];
}
function querySelectorAllByAttr(node, attr) {
    return node.querySelectorAll
        ? toArray(node.querySelectorAll(`[${attr}]`))
        : XpathUtil.evalXPath(`.//*[@${attr}]`, node);
}
exports.querySelectorAllByAttr = querySelectorAllByAttr;
function querySelectorAllByAttrValue(node, attr, value) {
    return node.querySelectorAll
        ? toArray(node.querySelectorAll(`[${attr}="${value}"]`))
        : XpathUtil.evalXPath(`.//*[@${attr}="${value}"]`, node);
}
exports.querySelectorAllByAttrValue = querySelectorAllByAttrValue;
function querySelectorAll(node, tag) {
    return node.querySelectorAll
        ? toArray(node.querySelectorAll(tag))
        : XpathUtil.evalXPath(`.//${tag}`, node);
}
exports.querySelectorAll = querySelectorAll;
function tagName(node) {
    return node.tagName.toUpperCase();
}
exports.tagName = tagName;
function cloneNode(node) {
    return node.cloneNode(true);
}
exports.cloneNode = cloneNode;
function serializeXml(node) {
    const xmls = new system_external_1.default.xmldom.XMLSerializer();
    return xmls.serializeToString(node);
}
exports.serializeXml = serializeXml;


/***/ }),

/***/ 4886:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.EnginePromise = exports.SREError = void 0;
const Dcstr = __webpack_require__(8310);
const EngineConst = __webpack_require__(4998);
const debugger_1 = __webpack_require__(1984);
const variables_1 = __webpack_require__(4513);
class SREError extends Error {
    constructor(message = '') {
        super();
        this.message = message;
        this.name = 'SRE Error';
    }
}
exports.SREError = SREError;
class Engine {
    constructor() {
        this.customLoader = null;
        this.parsers = {};
        this.comparator = null;
        this.mode = EngineConst.Mode.SYNC;
        this.init = true;
        this.delay = false;
        this.comparators = {};
        this.domain = 'mathspeak';
        this.style = Dcstr.DynamicCstr.DEFAULT_VALUES[Dcstr.Axis.STYLE];
        this._defaultLocale = Dcstr.DynamicCstr.DEFAULT_VALUES[Dcstr.Axis.LOCALE];
        this.locale = this.defaultLocale;
        this.subiso = '';
        this.modality = Dcstr.DynamicCstr.DEFAULT_VALUES[Dcstr.Axis.MODALITY];
        this.speech = EngineConst.Speech.NONE;
        this.markup = EngineConst.Markup.NONE;
        this.walker = 'Table';
        this.structure = false;
        this.ruleSets = [];
        this.strict = false;
        this.isIE = false;
        this.isEdge = false;
        this.rate = '100';
        this.pprint = false;
        this.config = false;
        this.rules = '';
        this.prune = '';
        this.evaluator = Engine.defaultEvaluator;
        this.defaultParser = new Dcstr.DynamicCstrParser(Dcstr.DynamicCstr.DEFAULT_ORDER);
        this.parser = this.defaultParser;
        this.dynamicCstr = Dcstr.DynamicCstr.defaultCstr();
    }
    set defaultLocale(loc) {
        this._defaultLocale = variables_1.Variables.ensureLocale(loc, this._defaultLocale);
    }
    get defaultLocale() {
        return this._defaultLocale;
    }
    static getInstance() {
        Engine.instance = Engine.instance || new Engine();
        return Engine.instance;
    }
    static defaultEvaluator(str, _cstr) {
        return str;
    }
    static evaluateNode(node) {
        return Engine.nodeEvaluator(node);
    }
    getRate() {
        const numeric = parseInt(this.rate, 10);
        return isNaN(numeric) ? 100 : numeric;
    }
    setDynamicCstr(opt_dynamic) {
        if (this.defaultLocale) {
            Dcstr.DynamicCstr.DEFAULT_VALUES[Dcstr.Axis.LOCALE] = this.defaultLocale;
        }
        if (opt_dynamic) {
            const keys = Object.keys(opt_dynamic);
            for (let i = 0; i < keys.length; i++) {
                const feature = keys[i];
                if (Dcstr.DynamicCstr.DEFAULT_ORDER.indexOf(feature) !== -1) {
                    const value = opt_dynamic[feature];
                    this[feature] = value;
                }
            }
        }
        EngineConst.DOMAIN_TO_STYLES[this.domain] = this.style;
        const dynamic = [this.locale, this.modality, this.domain, this.style].join('.');
        const fallback = Dcstr.DynamicProperties.createProp([Dcstr.DynamicCstr.DEFAULT_VALUES[Dcstr.Axis.LOCALE]], [Dcstr.DynamicCstr.DEFAULT_VALUES[Dcstr.Axis.MODALITY]], [Dcstr.DynamicCstr.DEFAULT_VALUES[Dcstr.Axis.DOMAIN]], [Dcstr.DynamicCstr.DEFAULT_VALUES[Dcstr.Axis.STYLE]]);
        const comparator = this.comparators[this.domain];
        const parser = this.parsers[this.domain];
        this.parser = parser ? parser : this.defaultParser;
        this.dynamicCstr = this.parser.parse(dynamic);
        this.dynamicCstr.updateProperties(fallback.getProperties());
        this.comparator = comparator
            ? comparator()
            : new Dcstr.DefaultComparator(this.dynamicCstr);
    }
    configurate(feature) {
        if (this.mode === EngineConst.Mode.HTTP && !this.config) {
            configBlocks(feature);
            this.config = true;
        }
        configFeature(feature);
    }
    setCustomLoader(fn) {
        if (fn) {
            this.customLoader = fn;
        }
    }
}
exports["default"] = Engine;
Engine.BINARY_FEATURES = ['strict', 'structure', 'pprint'];
Engine.STRING_FEATURES = [
    'markup',
    'style',
    'domain',
    'speech',
    'walker',
    'defaultLocale',
    'locale',
    'delay',
    'modality',
    'rate',
    'rules',
    'subiso',
    'prune'
];
Engine.nodeEvaluator = function (_node) {
    return [];
};
function configFeature(feature) {
    if (typeof SREfeature !== 'undefined') {
        for (const [name, feat] of Object.entries(SREfeature)) {
            feature[name] = feat;
        }
    }
}
function configBlocks(feature) {
    const scripts = document.documentElement.querySelectorAll('script[type="text/x-sre-config"]');
    for (let i = 0, m = scripts.length; i < m; i++) {
        let inner;
        try {
            inner = scripts[i].innerHTML;
            const config = JSON.parse(inner);
            for (const f in config) {
                feature[f] = config[f];
            }
        }
        catch (err) {
            debugger_1.Debugger.getInstance().output('Illegal configuration ', inner);
        }
    }
}
class EnginePromise {
    static get(locale = Engine.getInstance().locale) {
        return EnginePromise.promises[locale] || Promise.resolve('');
    }
    static getall() {
        return Promise.all(Object.values(EnginePromise.promises));
    }
}
exports.EnginePromise = EnginePromise;
EnginePromise.loaded = {};
EnginePromise.promises = {};


/***/ }),

/***/ 4998:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DOMAIN_TO_STYLES = exports.Markup = exports.Speech = exports.personalityPropList = exports.personalityProps = exports.Mode = void 0;
var Mode;
(function (Mode) {
    Mode["SYNC"] = "sync";
    Mode["ASYNC"] = "async";
    Mode["HTTP"] = "http";
})(Mode = exports.Mode || (exports.Mode = {}));
var personalityProps;
(function (personalityProps) {
    personalityProps["PITCH"] = "pitch";
    personalityProps["RATE"] = "rate";
    personalityProps["VOLUME"] = "volume";
    personalityProps["PAUSE"] = "pause";
    personalityProps["JOIN"] = "join";
    personalityProps["LAYOUT"] = "layout";
})(personalityProps = exports.personalityProps || (exports.personalityProps = {}));
exports.personalityPropList = [
    personalityProps.PITCH,
    personalityProps.RATE,
    personalityProps.VOLUME,
    personalityProps.PAUSE,
    personalityProps.JOIN
];
var Speech;
(function (Speech) {
    Speech["NONE"] = "none";
    Speech["SHALLOW"] = "shallow";
    Speech["DEEP"] = "deep";
})(Speech = exports.Speech || (exports.Speech = {}));
var Markup;
(function (Markup) {
    Markup["NONE"] = "none";
    Markup["LAYOUT"] = "layout";
    Markup["PUNCTUATION"] = "punctuation";
    Markup["SSML"] = "ssml";
    Markup["SSML_STEP"] = "ssml_step";
    Markup["ACSS"] = "acss";
    Markup["SABLE"] = "sable";
    Markup["VOICEXML"] = "voicexml";
})(Markup = exports.Markup || (exports.Markup = {}));
exports.DOMAIN_TO_STYLES = {
    mathspeak: 'default',
    clearspeak: 'default'
};


/***/ }),

/***/ 985:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.setup = void 0;
const L10n = __webpack_require__(2371);
const MathMap = __webpack_require__(5659);
const BrowserUtil = __webpack_require__(9501);
const engine_1 = __webpack_require__(4886);
const FileUtil = __webpack_require__(7129);
const system_external_1 = __webpack_require__(4755);
function setup(feature) {
    return __awaiter(this, void 0, void 0, function* () {
        const engine = engine_1.default.getInstance();
        if (feature.domain === 'default' &&
            (feature.modality === 'speech' ||
                !feature.modality ||
                engine.modality === 'speech')) {
            feature.domain = 'mathspeak';
        }
        const setIf = (feat) => {
            if (typeof feature[feat] !== 'undefined') {
                engine[feat] = !!feature[feat];
            }
        };
        const setMulti = (feat) => {
            if (typeof feature[feat] !== 'undefined') {
                engine[feat] = feature[feat];
            }
        };
        setMulti('mode');
        engine.configurate(feature);
        engine_1.default.BINARY_FEATURES.forEach(setIf);
        engine_1.default.STRING_FEATURES.forEach(setMulti);
        if (feature.json) {
            system_external_1.default.jsonPath = FileUtil.makePath(feature.json);
        }
        if (feature.xpath) {
            system_external_1.default.WGXpath = feature.xpath;
        }
        engine.setCustomLoader(feature.custom);
        setupBrowsers(engine);
        L10n.setLocale();
        engine.setDynamicCstr();
        if (engine.init) {
            engine_1.EnginePromise.promises['init'] = new Promise((res, _rej) => {
                setTimeout(() => {
                    res('init');
                }, 10);
            });
            engine.init = false;
            return engine_1.EnginePromise.get();
        }
        if (engine.delay) {
            engine.delay = false;
            return engine_1.EnginePromise.get();
        }
        return MathMap.loadLocale();
    });
}
exports.setup = setup;
function setupBrowsers(engine) {
    engine.isIE = BrowserUtil.detectIE();
    engine.isEdge = BrowserUtil.detectEdge();
}


/***/ }),

/***/ 6988:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Event = exports.EventType = exports.Move = exports.KeyCode = void 0;
var KeyCode;
(function (KeyCode) {
    KeyCode[KeyCode["ENTER"] = 13] = "ENTER";
    KeyCode[KeyCode["ESC"] = 27] = "ESC";
    KeyCode[KeyCode["SPACE"] = 32] = "SPACE";
    KeyCode[KeyCode["PAGE_UP"] = 33] = "PAGE_UP";
    KeyCode[KeyCode["PAGE_DOWN"] = 34] = "PAGE_DOWN";
    KeyCode[KeyCode["END"] = 35] = "END";
    KeyCode[KeyCode["HOME"] = 36] = "HOME";
    KeyCode[KeyCode["LEFT"] = 37] = "LEFT";
    KeyCode[KeyCode["UP"] = 38] = "UP";
    KeyCode[KeyCode["RIGHT"] = 39] = "RIGHT";
    KeyCode[KeyCode["DOWN"] = 40] = "DOWN";
    KeyCode[KeyCode["TAB"] = 9] = "TAB";
    KeyCode[KeyCode["LESS"] = 188] = "LESS";
    KeyCode[KeyCode["GREATER"] = 190] = "GREATER";
    KeyCode[KeyCode["DASH"] = 189] = "DASH";
    KeyCode[KeyCode["ZERO"] = 48] = "ZERO";
    KeyCode[KeyCode["ONE"] = 49] = "ONE";
    KeyCode[KeyCode["TWO"] = 50] = "TWO";
    KeyCode[KeyCode["THREE"] = 51] = "THREE";
    KeyCode[KeyCode["FOUR"] = 52] = "FOUR";
    KeyCode[KeyCode["FIVE"] = 53] = "FIVE";
    KeyCode[KeyCode["SIX"] = 54] = "SIX";
    KeyCode[KeyCode["SEVEN"] = 55] = "SEVEN";
    KeyCode[KeyCode["EIGHT"] = 56] = "EIGHT";
    KeyCode[KeyCode["NINE"] = 57] = "NINE";
    KeyCode[KeyCode["A"] = 65] = "A";
    KeyCode[KeyCode["B"] = 66] = "B";
    KeyCode[KeyCode["C"] = 67] = "C";
    KeyCode[KeyCode["D"] = 68] = "D";
    KeyCode[KeyCode["E"] = 69] = "E";
    KeyCode[KeyCode["F"] = 70] = "F";
    KeyCode[KeyCode["G"] = 71] = "G";
    KeyCode[KeyCode["H"] = 72] = "H";
    KeyCode[KeyCode["I"] = 73] = "I";
    KeyCode[KeyCode["J"] = 74] = "J";
    KeyCode[KeyCode["K"] = 75] = "K";
    KeyCode[KeyCode["L"] = 76] = "L";
    KeyCode[KeyCode["M"] = 77] = "M";
    KeyCode[KeyCode["N"] = 78] = "N";
    KeyCode[KeyCode["O"] = 79] = "O";
    KeyCode[KeyCode["P"] = 80] = "P";
    KeyCode[KeyCode["Q"] = 81] = "Q";
    KeyCode[KeyCode["R"] = 82] = "R";
    KeyCode[KeyCode["S"] = 83] = "S";
    KeyCode[KeyCode["T"] = 84] = "T";
    KeyCode[KeyCode["U"] = 85] = "U";
    KeyCode[KeyCode["V"] = 86] = "V";
    KeyCode[KeyCode["W"] = 87] = "W";
    KeyCode[KeyCode["X"] = 88] = "X";
    KeyCode[KeyCode["Y"] = 89] = "Y";
    KeyCode[KeyCode["Z"] = 90] = "Z";
})(KeyCode = exports.KeyCode || (exports.KeyCode = {}));
exports.Move = new Map([
    [13, 'ENTER'],
    [27, 'ESC'],
    [32, 'SPACE'],
    [33, 'PAGE_UP'],
    [34, 'PAGE_DOWN'],
    [35, 'END'],
    [36, 'HOME'],
    [37, 'LEFT'],
    [38, 'UP'],
    [39, 'RIGHT'],
    [40, 'DOWN'],
    [9, 'TAB'],
    [188, 'LESS'],
    [190, 'GREATER'],
    [189, 'DASH'],
    [48, 'ZERO'],
    [49, 'ONE'],
    [50, 'TWO'],
    [51, 'THREE'],
    [52, 'FOUR'],
    [53, 'FIVE'],
    [54, 'SIX'],
    [55, 'SEVEN'],
    [56, 'EIGHT'],
    [57, 'NINE'],
    [65, 'A'],
    [66, 'B'],
    [67, 'C'],
    [68, 'D'],
    [69, 'E'],
    [70, 'F'],
    [71, 'G'],
    [72, 'H'],
    [73, 'I'],
    [74, 'J'],
    [75, 'K'],
    [76, 'L'],
    [77, 'M'],
    [78, 'N'],
    [79, 'O'],
    [80, 'P'],
    [81, 'Q'],
    [82, 'R'],
    [83, 'S'],
    [84, 'T'],
    [85, 'U'],
    [86, 'V'],
    [87, 'W'],
    [88, 'X'],
    [89, 'Y'],
    [90, 'Z']
]);
var EventType;
(function (EventType) {
    EventType["CLICK"] = "click";
    EventType["DBLCLICK"] = "dblclick";
    EventType["MOUSEDOWN"] = "mousedown";
    EventType["MOUSEUP"] = "mouseup";
    EventType["MOUSEOVER"] = "mouseover";
    EventType["MOUSEOUT"] = "mouseout";
    EventType["MOUSEMOVE"] = "mousemove";
    EventType["SELECTSTART"] = "selectstart";
    EventType["KEYPRESS"] = "keypress";
    EventType["KEYDOWN"] = "keydown";
    EventType["KEYUP"] = "keyup";
    EventType["TOUCHSTART"] = "touchstart";
    EventType["TOUCHMOVE"] = "touchmove";
    EventType["TOUCHEND"] = "touchend";
    EventType["TOUCHCANCEL"] = "touchcancel";
})(EventType = exports.EventType || (exports.EventType = {}));
class Event {
    constructor(src, type, callback) {
        this.src = src;
        this.type = type;
        this.callback = callback;
    }
    add() {
        this.src.addEventListener(this.type, this.callback);
    }
    remove() {
        this.src.removeEventListener(this.type, this.callback);
    }
}
exports.Event = Event;


/***/ }),

/***/ 7129:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.localePath = exports.makePath = void 0;
const system_external_1 = __webpack_require__(4755);
function makePath(path) {
    return path.match('/$') ? path : path + '/';
}
exports.makePath = makePath;
function localePath(locale, ext = 'json') {
    return (makePath(system_external_1.default.jsonPath) +
        locale +
        (ext.match(/^\./) ? ext : '.' + ext));
}
exports.localePath = localePath;


/***/ }),

/***/ 3539:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.KeyProcessor = exports.Processor = void 0;
const event_util_1 = __webpack_require__(6988);
class Processor {
    constructor(name, methods) {
        this.name = name;
        this.process = methods.processor;
        this.postprocess =
            methods.postprocessor || ((x, _y) => x);
        this.processor = this.postprocess
            ? function (x) {
                return this.postprocess(this.process(x), x);
            }
            : this.process;
        this.print = methods.print || Processor.stringify_;
        this.pprint = methods.pprint || this.print;
    }
    static stringify_(x) {
        return x ? x.toString() : x;
    }
}
exports.Processor = Processor;
Processor.LocalState = { walker: null, speechGenerator: null, highlighter: null };
class KeyProcessor extends Processor {
    constructor(name, methods) {
        super(name, methods);
        this.key = methods.key || KeyProcessor.getKey_;
    }
    static getKey_(key) {
        return typeof key === 'string'
            ?
                event_util_1.KeyCode[key.toUpperCase()]
            : key;
    }
}
exports.KeyProcessor = KeyProcessor;


/***/ }),

/***/ 9615:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.keypress = exports.output = exports.print = exports.process = exports.set = void 0;
const AuralRendering = __webpack_require__(4253);
const Enrich = __webpack_require__(7450);
const HighlighterFactory = __webpack_require__(9009);
const locale_1 = __webpack_require__(4524);
const Semantic = __webpack_require__(1939);
const SpeechGeneratorFactory = __webpack_require__(7317);
const SpeechGeneratorUtil = __webpack_require__(144);
const WalkerFactory = __webpack_require__(907);
const WalkerUtil = __webpack_require__(8835);
const DomUtil = __webpack_require__(6671);
const engine_1 = __webpack_require__(4886);
const EngineConst = __webpack_require__(4998);
const processor_1 = __webpack_require__(3539);
const XpathUtil = __webpack_require__(5024);
const PROCESSORS = new Map();
function set(processor) {
    PROCESSORS.set(processor.name, processor);
}
exports.set = set;
function get_(name) {
    const processor = PROCESSORS.get(name);
    if (!processor) {
        throw new engine_1.SREError('Unknown processor ' + name);
    }
    return processor;
}
function process(name, expr) {
    const processor = get_(name);
    try {
        return processor.processor(expr);
    }
    catch (_e) {
        throw new engine_1.SREError('Processing error for expression ' + expr);
    }
}
exports.process = process;
function print(name, data) {
    const processor = get_(name);
    return engine_1.default.getInstance().pprint
        ? processor.pprint(data)
        : processor.print(data);
}
exports.print = print;
function output(name, expr) {
    const processor = get_(name);
    try {
        const data = processor.processor(expr);
        return engine_1.default.getInstance().pprint
            ? processor.pprint(data)
            : processor.print(data);
    }
    catch (_e) {
        throw new engine_1.SREError('Processing error for expression ' + expr);
    }
}
exports.output = output;
function keypress(name, expr) {
    const processor = get_(name);
    const key = processor instanceof processor_1.KeyProcessor ? processor.key(expr) : expr;
    const data = processor.processor(key);
    return engine_1.default.getInstance().pprint
        ? processor.pprint(data)
        : processor.print(data);
}
exports.keypress = keypress;
set(new processor_1.Processor('semantic', {
    processor: function (expr) {
        const mml = DomUtil.parseInput(expr);
        return Semantic.xmlTree(mml);
    },
    postprocessor: function (xml, _expr) {
        const setting = engine_1.default.getInstance().speech;
        if (setting === EngineConst.Speech.NONE) {
            return xml;
        }
        const clone = DomUtil.cloneNode(xml);
        let speech = SpeechGeneratorUtil.computeMarkup(clone);
        if (setting === EngineConst.Speech.SHALLOW) {
            xml.setAttribute('speech', AuralRendering.finalize(speech));
            return xml;
        }
        const nodesXml = XpathUtil.evalXPath('.//*[@id]', xml);
        const nodesClone = XpathUtil.evalXPath('.//*[@id]', clone);
        for (let i = 0, orig, node; (orig = nodesXml[i]), (node = nodesClone[i]); i++) {
            speech = SpeechGeneratorUtil.computeMarkup(node);
            orig.setAttribute('speech', AuralRendering.finalize(speech));
        }
        return xml;
    },
    pprint: function (tree) {
        return DomUtil.formatXml(tree.toString());
    }
}));
set(new processor_1.Processor('speech', {
    processor: function (expr) {
        const mml = DomUtil.parseInput(expr);
        const xml = Semantic.xmlTree(mml);
        const descrs = SpeechGeneratorUtil.computeSpeech(xml);
        return AuralRendering.finalize(AuralRendering.markup(descrs));
    },
    pprint: function (speech) {
        const str = speech.toString();
        return AuralRendering.isXml() ? DomUtil.formatXml(str) : str;
    }
}));
set(new processor_1.Processor('json', {
    processor: function (expr) {
        const mml = DomUtil.parseInput(expr);
        const stree = Semantic.getTree(mml);
        return stree.toJson();
    },
    postprocessor: function (json, expr) {
        const setting = engine_1.default.getInstance().speech;
        if (setting === EngineConst.Speech.NONE) {
            return json;
        }
        const mml = DomUtil.parseInput(expr);
        const xml = Semantic.xmlTree(mml);
        const speech = SpeechGeneratorUtil.computeMarkup(xml);
        if (setting === EngineConst.Speech.SHALLOW) {
            json.stree.speech = AuralRendering.finalize(speech);
            return json;
        }
        const addRec = (json) => {
            const node = XpathUtil.evalXPath(`.//*[@id=${json.id}]`, xml)[0];
            const speech = SpeechGeneratorUtil.computeMarkup(node);
            json.speech = AuralRendering.finalize(speech);
            if (json.children) {
                json.children.forEach(addRec);
            }
        };
        addRec(json.stree);
        return json;
    },
    print: function (json) {
        return JSON.stringify(json);
    },
    pprint: function (json) {
        return JSON.stringify(json, null, 2);
    }
}));
set(new processor_1.Processor('description', {
    processor: function (expr) {
        const mml = DomUtil.parseInput(expr);
        const xml = Semantic.xmlTree(mml);
        const descrs = SpeechGeneratorUtil.computeSpeech(xml);
        return descrs;
    },
    print: function (descrs) {
        return JSON.stringify(descrs);
    },
    pprint: function (descrs) {
        return JSON.stringify(descrs, null, 2);
    }
}));
set(new processor_1.Processor('enriched', {
    processor: function (expr) {
        return Enrich.semanticMathmlSync(expr);
    },
    postprocessor: function (enr, _expr) {
        const root = WalkerUtil.getSemanticRoot(enr);
        let generator;
        switch (engine_1.default.getInstance().speech) {
            case EngineConst.Speech.NONE:
                break;
            case EngineConst.Speech.SHALLOW:
                generator = SpeechGeneratorFactory.generator('Adhoc');
                generator.getSpeech(root, enr);
                break;
            case EngineConst.Speech.DEEP:
                generator = SpeechGeneratorFactory.generator('Tree');
                generator.getSpeech(enr, enr);
                break;
            default:
                break;
        }
        return enr;
    },
    pprint: function (tree) {
        return DomUtil.formatXml(tree.toString());
    }
}));
set(new processor_1.Processor('walker', {
    processor: function (expr) {
        const generator = SpeechGeneratorFactory.generator('Node');
        processor_1.Processor.LocalState.speechGenerator = generator;
        generator.setOptions({
            modality: engine_1.default.getInstance().modality,
            locale: engine_1.default.getInstance().locale,
            domain: engine_1.default.getInstance().domain,
            style: engine_1.default.getInstance().style
        });
        processor_1.Processor.LocalState.highlighter = HighlighterFactory.highlighter({ color: 'black' }, { color: 'white' }, { renderer: 'NativeMML' });
        const node = process('enriched', expr);
        const eml = print('enriched', node);
        processor_1.Processor.LocalState.walker = WalkerFactory.walker(engine_1.default.getInstance().walker, node, generator, processor_1.Processor.LocalState.highlighter, eml);
        return processor_1.Processor.LocalState.walker;
    },
    print: function (_walker) {
        return processor_1.Processor.LocalState.walker.speech();
    }
}));
set(new processor_1.KeyProcessor('move', {
    processor: function (direction) {
        if (!processor_1.Processor.LocalState.walker) {
            return null;
        }
        const move = processor_1.Processor.LocalState.walker.move(direction);
        return move === false
            ? AuralRendering.error(direction)
            : processor_1.Processor.LocalState.walker.speech();
    }
}));
set(new processor_1.Processor('number', {
    processor: function (numb) {
        const num = parseInt(numb, 10);
        return isNaN(num) ? '' : locale_1.LOCALE.NUMBERS.numberToWords(num);
    }
}));
set(new processor_1.Processor('ordinal', {
    processor: function (numb) {
        const num = parseInt(numb, 10);
        return isNaN(num) ? '' : locale_1.LOCALE.NUMBERS.wordOrdinal(num);
    }
}));
set(new processor_1.Processor('numericOrdinal', {
    processor: function (numb) {
        const num = parseInt(numb, 10);
        return isNaN(num) ? '' : locale_1.LOCALE.NUMBERS.numericOrdinal(num);
    }
}));
set(new processor_1.Processor('vulgar', {
    processor: function (numb) {
        const [en, den] = numb.split('/').map((x) => parseInt(x, 10));
        return isNaN(en) || isNaN(den)
            ? ''
            : process('speech', `<mfrac><mn>${en}</mn><mn>${den}</mn></mfrac>`);
    }
}));


/***/ }),

/***/ 9037:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.localePath = exports.exit = exports.move = exports.walk = exports.processFile = exports.file = exports.vulgar = exports.numericOrdinal = exports.ordinal = exports.number = exports.toEnriched = exports.toDescription = exports.toJson = exports.toSemantic = exports.toSpeech = exports.localeLoader = exports.engineReady = exports.engineSetup = exports.setupEngine = exports.version = void 0;
const engine_1 = __webpack_require__(4886);
const engine_setup_1 = __webpack_require__(985);
const EngineConst = __webpack_require__(4998);
const FileUtil = __webpack_require__(7129);
const ProcessorFactory = __webpack_require__(9615);
const system_external_1 = __webpack_require__(4755);
const variables_1 = __webpack_require__(4513);
const math_map_1 = __webpack_require__(5659);
exports.version = variables_1.Variables.VERSION;
function setupEngine(feature) {
    return __awaiter(this, void 0, void 0, function* () {
        return (0, engine_setup_1.setup)(feature);
    });
}
exports.setupEngine = setupEngine;
function engineSetup() {
    const engineFeatures = ['mode'].concat(engine_1.default.STRING_FEATURES, engine_1.default.BINARY_FEATURES);
    const engine = engine_1.default.getInstance();
    const features = {};
    engineFeatures.forEach(function (x) {
        features[x] = engine[x];
    });
    features.json = system_external_1.default.jsonPath;
    features.xpath = system_external_1.default.WGXpath;
    features.rules = engine.ruleSets.slice();
    return features;
}
exports.engineSetup = engineSetup;
function engineReady() {
    return __awaiter(this, void 0, void 0, function* () {
        return setupEngine({}).then(() => engine_1.EnginePromise.getall());
    });
}
exports.engineReady = engineReady;
exports.localeLoader = math_map_1.standardLoader;
function toSpeech(expr) {
    return processString('speech', expr);
}
exports.toSpeech = toSpeech;
function toSemantic(expr) {
    return processString('semantic', expr);
}
exports.toSemantic = toSemantic;
function toJson(expr) {
    return processString('json', expr);
}
exports.toJson = toJson;
function toDescription(expr) {
    return processString('description', expr);
}
exports.toDescription = toDescription;
function toEnriched(expr) {
    return processString('enriched', expr);
}
exports.toEnriched = toEnriched;
function number(expr) {
    return processString('number', expr);
}
exports.number = number;
function ordinal(expr) {
    return processString('ordinal', expr);
}
exports.ordinal = ordinal;
function numericOrdinal(expr) {
    return processString('numericOrdinal', expr);
}
exports.numericOrdinal = numericOrdinal;
function vulgar(expr) {
    return processString('vulgar', expr);
}
exports.vulgar = vulgar;
function processString(processor, input) {
    return ProcessorFactory.process(processor, input);
}
exports.file = {};
exports.file.toSpeech = function (input, opt_output) {
    return processFile('speech', input, opt_output);
};
exports.file.toSemantic = function (input, opt_output) {
    return processFile('semantic', input, opt_output);
};
exports.file.toJson = function (input, opt_output) {
    return processFile('json', input, opt_output);
};
exports.file.toDescription = function (input, opt_output) {
    return processFile('description', input, opt_output);
};
exports.file.toEnriched = function (input, opt_output) {
    return processFile('enriched', input, opt_output);
};
function processFile(processor, input, opt_output) {
    switch (engine_1.default.getInstance().mode) {
        case EngineConst.Mode.ASYNC:
            return processFileAsync(processor, input, opt_output);
        case EngineConst.Mode.SYNC:
            return processFileSync(processor, input, opt_output);
        default:
            throw new engine_1.SREError(`Can process files in ${engine_1.default.getInstance().mode} mode`);
    }
}
exports.processFile = processFile;
function processFileSync(processor, input, opt_output) {
    const expr = inputFileSync_(input);
    const result = ProcessorFactory.output(processor, expr);
    if (opt_output) {
        try {
            system_external_1.default.fs.writeFileSync(opt_output, result);
        }
        catch (err) {
            throw new engine_1.SREError('Can not write to file: ' + opt_output);
        }
    }
    return result;
}
function inputFileSync_(file) {
    let expr;
    try {
        expr = system_external_1.default.fs.readFileSync(file, { encoding: 'utf8' });
    }
    catch (err) {
        throw new engine_1.SREError('Can not open file: ' + file);
    }
    return expr;
}
function processFileAsync(processor, file, output) {
    return __awaiter(this, void 0, void 0, function* () {
        const expr = yield system_external_1.default.fs.promises.readFile(file, {
            encoding: 'utf8'
        });
        const result = ProcessorFactory.output(processor, expr);
        if (output) {
            try {
                system_external_1.default.fs.promises.writeFile(output, result);
            }
            catch (_err) {
                throw new engine_1.SREError('Can not write to file: ' + output);
            }
        }
        return result;
    });
}
function walk(expr) {
    return ProcessorFactory.output('walker', expr);
}
exports.walk = walk;
function move(direction) {
    return ProcessorFactory.keypress('move', direction);
}
exports.move = move;
function exit(opt_value) {
    const value = opt_value || 0;
    engine_1.EnginePromise.getall().then(() => process.exit(value));
}
exports.exit = exit;
exports.localePath = FileUtil.localePath;
if (system_external_1.default.documentSupported) {
    setupEngine({ mode: EngineConst.Mode.HTTP }).then(() => setupEngine({}));
}
else {
    setupEngine({ mode: EngineConst.Mode.SYNC }).then(() => setupEngine({ mode: EngineConst.Mode.ASYNC }));
}


/***/ }),

/***/ 4755:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

var __dirname = "/";

Object.defineProperty(exports, "__esModule", ({ value: true }));
const variables_1 = __webpack_require__(4513);
class SystemExternal {
    static extRequire(library) {
        if (typeof process !== 'undefined' && "function" !== 'undefined') {
            const nodeRequire = eval('require');
            return nodeRequire(library);
        }
        return null;
    }
}
exports["default"] = SystemExternal;
SystemExternal.windowSupported = (() => !(typeof window === 'undefined'))();
SystemExternal.documentSupported = (() => SystemExternal.windowSupported &&
    !(typeof window.document === 'undefined'))();
SystemExternal.xmldom = SystemExternal.documentSupported
    ? window
    : SystemExternal.extRequire('xmldom-sre');
SystemExternal.document = SystemExternal.documentSupported
    ? window.document
    : new SystemExternal.xmldom.DOMImplementation().createDocument('', '', 0);
SystemExternal.xpath = SystemExternal.documentSupported
    ? document
    : (function () {
        const window = { document: {}, XPathResult: {} };
        const wgx = SystemExternal.extRequire('wicked-good-xpath');
        wgx.install(window);
        window.document.XPathResult = window.XPathResult;
        return window.document;
    })();
SystemExternal.mathmapsIePath = 'https://cdn.jsdelivr.net/npm/sre-mathmaps-ie@' +
    variables_1.Variables.VERSION +
    'mathmaps_ie.js';
SystemExternal.commander = SystemExternal.documentSupported
    ? null
    : SystemExternal.extRequire('commander');
SystemExternal.fs = SystemExternal.documentSupported
    ? null
    : SystemExternal.extRequire('fs');
SystemExternal.url = variables_1.Variables.url;
SystemExternal.jsonPath = (function () {
    return ((SystemExternal.documentSupported
        ? SystemExternal.url
        : process.env.SRE_JSON_PATH ||
            __webpack_require__.g.SRE_JSON_PATH ||
            ( true
                ? __dirname + '/mathmaps'
                : 0)) + '/');
})();
SystemExternal.WGXpath = variables_1.Variables.WGXpath;
SystemExternal.wgxpath = null;


/***/ }),

/***/ 4513:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Variables = void 0;
class Variables {
    static ensureLocale(loc, def) {
        if (!Variables.LOCALES.get(loc)) {
            console.error(`Locale ${loc} does not exist! Using` +
                ` ${Variables.LOCALES.get(def)} instead.`);
            return def;
        }
        return loc;
    }
}
exports.Variables = Variables;
Variables.VERSION = '4.0.6';
Variables.LOCALES = new Map([
    ['ca', 'Catalan'],
    ['da', 'Danish'],
    ['de', 'German'],
    ['en', 'English'],
    ['es', 'Spanish'],
    ['fr', 'French'],
    ['hi', 'Hindi'],
    ['it', 'Italian'],
    ['nb', 'Bokmål'],
    ['nn', 'Nynorsk'],
    ['sv', 'Swedish'],
    ['nemeth', 'Nemeth']
]);
Variables.mathjaxVersion = '3.2.1';
Variables.url = 'https://cdn.jsdelivr.net/npm/speech-rule-engine@' +
    Variables.VERSION +
    '/lib/mathmaps';
Variables.WGXpath = 'https://cdn.jsdelivr.net/npm/wicked-good-xpath@1.3.0/dist/wgxpath.install.js';


/***/ }),

/***/ 5024:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.updateEvaluator = exports.evaluateString = exports.evaluateBoolean = exports.getLeafNodes = exports.evalXPath = exports.resolveNameSpace = exports.xpath = void 0;
const engine_1 = __webpack_require__(4886);
const EngineConst = __webpack_require__(4998);
const system_external_1 = __webpack_require__(4755);
function xpathSupported() {
    if (typeof XPathResult === 'undefined') {
        return false;
    }
    return true;
}
exports.xpath = {
    currentDocument: null,
    evaluate: xpathSupported()
        ? document.evaluate
        : system_external_1.default.xpath.evaluate,
    result: xpathSupported() ? XPathResult : system_external_1.default.xpath.XPathResult,
    createNSResolver: xpathSupported()
        ? document.createNSResolver
        : system_external_1.default.xpath.createNSResolver
};
const nameSpaces = {
    xhtml: 'http://www.w3.org/1999/xhtml',
    mathml: 'http://www.w3.org/1998/Math/MathML',
    mml: 'http://www.w3.org/1998/Math/MathML',
    svg: 'http://www.w3.org/2000/svg'
};
function resolveNameSpace(prefix) {
    return nameSpaces[prefix] || null;
}
exports.resolveNameSpace = resolveNameSpace;
class Resolver {
    constructor() {
        this.lookupNamespaceURI = resolveNameSpace;
    }
}
function evaluateXpath(expression, rootNode, type) {
    return engine_1.default.getInstance().mode === EngineConst.Mode.HTTP &&
        !engine_1.default.getInstance().isIE &&
        !engine_1.default.getInstance().isEdge
        ? exports.xpath.currentDocument.evaluate(expression, rootNode, resolveNameSpace, type, null)
        : exports.xpath.evaluate(expression, rootNode, new Resolver(), type, null);
}
function evalXPath(expression, rootNode) {
    let iterator;
    try {
        iterator = evaluateXpath(expression, rootNode, exports.xpath.result.ORDERED_NODE_ITERATOR_TYPE);
    }
    catch (err) {
        return [];
    }
    const results = [];
    for (let xpathNode = iterator.iterateNext(); xpathNode; xpathNode = iterator.iterateNext()) {
        results.push(xpathNode);
    }
    return results;
}
exports.evalXPath = evalXPath;
function getLeafNodes(rootNode) {
    return evalXPath('.//*[count(*)=0]', rootNode);
}
exports.getLeafNodes = getLeafNodes;
function evaluateBoolean(expression, rootNode) {
    let result;
    try {
        result = evaluateXpath(expression, rootNode, exports.xpath.result.BOOLEAN_TYPE);
    }
    catch (err) {
        return false;
    }
    return result.booleanValue;
}
exports.evaluateBoolean = evaluateBoolean;
function evaluateString(expression, rootNode) {
    let result;
    try {
        result = evaluateXpath(expression, rootNode, exports.xpath.result.STRING_TYPE);
    }
    catch (err) {
        return '';
    }
    return result.stringValue;
}
exports.evaluateString = evaluateString;
function updateEvaluator(node) {
    if (engine_1.default.getInstance().mode !== EngineConst.Mode.HTTP)
        return;
    let parent = node;
    while (parent && !parent.evaluate) {
        parent = parent.parentNode;
    }
    if (parent && parent.evaluate) {
        exports.xpath.currentDocument = parent;
    }
    else if (node.ownerDocument) {
        exports.xpath.currentDocument = node.ownerDocument;
    }
}
exports.updateEvaluator = updateEvaluator;


/***/ }),

/***/ 9341:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AbstractEnrichCase = void 0;
class AbstractEnrichCase {
    constructor(semantic) {
        this.semantic = semantic;
    }
}
exports.AbstractEnrichCase = AbstractEnrichCase;


/***/ }),

/***/ 4306:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseBinomial = void 0;
const DomUtil = __webpack_require__(6671);
const abstract_enrich_case_1 = __webpack_require__(9341);
const enrich_mathml_1 = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseBinomial extends abstract_enrich_case_1.AbstractEnrichCase {
    constructor(semantic) {
        super(semantic);
        this.mml = semantic.mathmlTree;
    }
    static test(semantic) {
        return (!semantic.mathmlTree &&
            semantic.type === "line" &&
            semantic.role === "binomial");
    }
    getMathml() {
        if (!this.semantic.childNodes.length) {
            return this.mml;
        }
        const child = this.semantic.childNodes[0];
        this.mml = (0, enrich_mathml_1.walkTree)(child);
        if (this.mml.hasAttribute(enrich_attr_1.Attribute.TYPE)) {
            const mrow = DomUtil.createElement('mrow');
            mrow.setAttribute(enrich_attr_1.Attribute.ADDED, 'true');
            DomUtil.replaceNode(this.mml, mrow);
            mrow.appendChild(this.mml);
            this.mml = mrow;
        }
        (0, enrich_attr_1.setAttributes)(this.mml, this.semantic);
        return this.mml;
    }
}
exports.CaseBinomial = CaseBinomial;


/***/ }),

/***/ 8871:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseDoubleScript = void 0;
const DomUtil = __webpack_require__(6671);
const abstract_enrich_case_1 = __webpack_require__(9341);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseDoubleScript extends abstract_enrich_case_1.AbstractEnrichCase {
    constructor(semantic) {
        super(semantic);
        this.mml = semantic.mathmlTree;
    }
    static test(semantic) {
        if (!semantic.mathmlTree || !semantic.childNodes.length) {
            return false;
        }
        const mmlTag = DomUtil.tagName(semantic.mathmlTree);
        const role = semantic.childNodes[0].role;
        return ((mmlTag === 'MSUBSUP' && role === "subsup") ||
            (mmlTag === 'MUNDEROVER' && role === "underover"));
    }
    getMathml() {
        const ignore = this.semantic.childNodes[0];
        const baseSem = ignore.childNodes[0];
        const supSem = this.semantic.childNodes[1];
        const subSem = ignore.childNodes[1];
        const supMml = EnrichMathml.walkTree(supSem);
        const baseMml = EnrichMathml.walkTree(baseSem);
        const subMml = EnrichMathml.walkTree(subSem);
        (0, enrich_attr_1.setAttributes)(this.mml, this.semantic);
        this.mml.setAttribute(enrich_attr_1.Attribute.CHILDREN, (0, enrich_attr_1.makeIdList)([baseSem, subSem, supSem]));
        [baseMml, subMml, supMml].forEach((child) => EnrichMathml.getInnerNode(child).setAttribute(enrich_attr_1.Attribute.PARENT, this.mml.getAttribute(enrich_attr_1.Attribute.ID)));
        this.mml.setAttribute(enrich_attr_1.Attribute.TYPE, ignore.role);
        EnrichMathml.addCollapsedAttribute(this.mml, [
            this.semantic.id,
            [ignore.id, baseSem.id, subSem.id],
            supSem.id
        ]);
        return this.mml;
    }
}
exports.CaseDoubleScript = CaseDoubleScript;


/***/ }),

/***/ 928:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseEmbellished = void 0;
const DomUtil = __webpack_require__(6671);
const semantic_node_1 = __webpack_require__(9444);
const abstract_enrich_case_1 = __webpack_require__(9341);
const case_double_script_1 = __webpack_require__(8871);
const case_multiscripts_1 = __webpack_require__(4308);
const case_tensor_1 = __webpack_require__(439);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseEmbellished extends abstract_enrich_case_1.AbstractEnrichCase {
    constructor(semantic) {
        super(semantic);
        this.fenced = null;
        this.fencedMml = null;
        this.fencedMmlNodes = [];
        this.ofence = null;
        this.ofenceMml = null;
        this.ofenceMap = {};
        this.cfence = null;
        this.cfenceMml = null;
        this.cfenceMap = {};
        this.parentCleanup = [];
    }
    static test(semantic) {
        return !!(semantic.mathmlTree &&
            semantic.fencePointer &&
            !semantic.mathmlTree.getAttribute('data-semantic-type'));
    }
    static makeEmptyNode_(id) {
        const mrow = DomUtil.createElement('mrow');
        const empty = new semantic_node_1.SemanticNode(id);
        empty.type = "empty";
        empty.mathmlTree = mrow;
        return empty;
    }
    static fencedMap_(fence, ids) {
        ids[fence.id] = fence.mathmlTree;
        if (!fence.embellished) {
            return;
        }
        CaseEmbellished.fencedMap_(fence.childNodes[0], ids);
    }
    getMathml() {
        this.getFenced_();
        this.fencedMml = EnrichMathml.walkTree(this.fenced);
        this.getFencesMml_();
        if (this.fenced.type === "empty" && !this.fencedMml.parentNode) {
            this.fencedMml.setAttribute(enrich_attr_1.Attribute.ADDED, 'true');
            this.cfenceMml.parentNode.insertBefore(this.fencedMml, this.cfenceMml);
        }
        this.getFencedMml_();
        const rewrite = this.rewrite_();
        return rewrite;
    }
    fencedElement(node) {
        return (node.type === "fenced" ||
            node.type === "matrix" ||
            node.type === "vector");
    }
    getFenced_() {
        let currentNode = this.semantic;
        while (!this.fencedElement(currentNode)) {
            currentNode = currentNode.childNodes[0];
        }
        this.fenced = currentNode.childNodes[0];
        this.ofence = currentNode.contentNodes[0];
        this.cfence = currentNode.contentNodes[1];
        CaseEmbellished.fencedMap_(this.ofence, this.ofenceMap);
        CaseEmbellished.fencedMap_(this.cfence, this.cfenceMap);
    }
    getFencedMml_() {
        let sibling = this.ofenceMml.nextSibling;
        sibling = sibling === this.fencedMml ? sibling : this.fencedMml;
        while (sibling && sibling !== this.cfenceMml) {
            this.fencedMmlNodes.push(sibling);
            sibling = sibling.nextSibling;
        }
    }
    getFencesMml_() {
        let currentNode = this.semantic;
        const ofenceIds = Object.keys(this.ofenceMap);
        const cfenceIds = Object.keys(this.cfenceMap);
        while ((!this.ofenceMml || !this.cfenceMml) &&
            currentNode !== this.fenced) {
            if (ofenceIds.indexOf(currentNode.fencePointer) !== -1 &&
                !this.ofenceMml) {
                this.ofenceMml = currentNode.mathmlTree;
            }
            if (cfenceIds.indexOf(currentNode.fencePointer) !== -1 &&
                !this.cfenceMml) {
                this.cfenceMml = currentNode.mathmlTree;
            }
            currentNode = currentNode.childNodes[0];
        }
        if (!this.ofenceMml) {
            this.ofenceMml = this.ofence.mathmlTree;
        }
        if (!this.cfenceMml) {
            this.cfenceMml = this.cfence.mathmlTree;
        }
        if (this.ofenceMml) {
            this.ofenceMml = EnrichMathml.ascendNewNode(this.ofenceMml);
        }
        if (this.cfenceMml) {
            this.cfenceMml = EnrichMathml.ascendNewNode(this.cfenceMml);
        }
    }
    rewrite_() {
        let currentNode = this.semantic;
        let result = null;
        const newNode = this.introduceNewLayer_();
        (0, enrich_attr_1.setAttributes)(newNode, this.fenced.parent);
        while (!this.fencedElement(currentNode)) {
            const mml = currentNode.mathmlTree;
            const specialCase = this.specialCase_(currentNode, mml);
            if (specialCase) {
                currentNode = specialCase;
            }
            else {
                (0, enrich_attr_1.setAttributes)(mml, currentNode);
                const mmlChildren = [];
                for (let i = 1, child; (child = currentNode.childNodes[i]); i++) {
                    mmlChildren.push(EnrichMathml.walkTree(child));
                }
                currentNode = currentNode.childNodes[0];
            }
            const dummy = DomUtil.createElement('dummy');
            const saveChild = mml.childNodes[0];
            DomUtil.replaceNode(mml, dummy);
            DomUtil.replaceNode(newNode, mml);
            DomUtil.replaceNode(mml.childNodes[0], newNode);
            DomUtil.replaceNode(dummy, saveChild);
            if (!result) {
                result = mml;
            }
        }
        EnrichMathml.walkTree(this.ofence);
        EnrichMathml.walkTree(this.cfence);
        this.cleanupParents_();
        return result || newNode;
    }
    specialCase_(semantic, mml) {
        const mmlTag = DomUtil.tagName(mml);
        let parent = null;
        let caller;
        if (mmlTag === 'MSUBSUP') {
            parent = semantic.childNodes[0];
            caller = case_double_script_1.CaseDoubleScript;
        }
        else if (mmlTag === 'MMULTISCRIPTS') {
            if (semantic.type === "superscript" ||
                semantic.type === "subscript") {
                caller = case_multiscripts_1.CaseMultiscripts;
            }
            else if (semantic.type === "tensor") {
                caller = case_tensor_1.CaseTensor;
            }
            if (caller &&
                semantic.childNodes[0] &&
                semantic.childNodes[0].role === "subsup") {
                parent = semantic.childNodes[0];
            }
            else {
                parent = semantic;
            }
        }
        if (!parent) {
            return null;
        }
        const base = parent.childNodes[0];
        const empty = CaseEmbellished.makeEmptyNode_(base.id);
        parent.childNodes[0] = empty;
        mml = new caller(semantic).getMathml();
        parent.childNodes[0] = base;
        this.parentCleanup.push(mml);
        return parent.childNodes[0];
    }
    introduceNewLayer_() {
        const fullOfence = this.fullFence(this.ofenceMml);
        const fullCfence = this.fullFence(this.cfenceMml);
        let newNode = DomUtil.createElement('mrow');
        DomUtil.replaceNode(this.fencedMml, newNode);
        this.fencedMmlNodes.forEach((node) => newNode.appendChild(node));
        newNode.insertBefore(fullOfence, this.fencedMml);
        newNode.appendChild(fullCfence);
        if (!newNode.parentNode) {
            const mrow = DomUtil.createElement('mrow');
            while (newNode.childNodes.length > 0) {
                mrow.appendChild(newNode.childNodes[0]);
            }
            newNode.appendChild(mrow);
            newNode = mrow;
        }
        return newNode;
    }
    fullFence(fence) {
        const parent = this.fencedMml.parentNode;
        let currentFence = fence;
        while (currentFence.parentNode && currentFence.parentNode !== parent) {
            currentFence = currentFence.parentNode;
        }
        return currentFence;
    }
    cleanupParents_() {
        this.parentCleanup.forEach(function (x) {
            const parent = x.childNodes[1].getAttribute(enrich_attr_1.Attribute.PARENT);
            x.childNodes[0].setAttribute(enrich_attr_1.Attribute.PARENT, parent);
        });
    }
}
exports.CaseEmbellished = CaseEmbellished;


/***/ }),

/***/ 9763:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseLimit = void 0;
const DomUtil = __webpack_require__(6671);
const abstract_enrich_case_1 = __webpack_require__(9341);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseLimit extends abstract_enrich_case_1.AbstractEnrichCase {
    constructor(semantic) {
        super(semantic);
        this.mml = semantic.mathmlTree;
    }
    static test(semantic) {
        if (!semantic.mathmlTree || !semantic.childNodes.length) {
            return false;
        }
        const mmlTag = DomUtil.tagName(semantic.mathmlTree);
        const type = semantic.type;
        return (((type === "limupper" || type === "limlower") &&
            (mmlTag === 'MSUBSUP' || mmlTag === 'MUNDEROVER')) ||
            (type === "limboth" &&
                (mmlTag === 'MSUB' ||
                    mmlTag === 'MUNDER' ||
                    mmlTag === 'MSUP' ||
                    mmlTag === 'MOVER')));
    }
    static walkTree_(node) {
        if (node) {
            EnrichMathml.walkTree(node);
        }
    }
    getMathml() {
        const children = this.semantic.childNodes;
        if (this.semantic.type !== "limboth" &&
            this.mml.childNodes.length >= 3) {
            this.mml = EnrichMathml.introduceNewLayer([this.mml], this.semantic);
        }
        (0, enrich_attr_1.setAttributes)(this.mml, this.semantic);
        if (!children[0].mathmlTree) {
            children[0].mathmlTree = this.semantic.mathmlTree;
        }
        children.forEach(CaseLimit.walkTree_);
        return this.mml;
    }
}
exports.CaseLimit = CaseLimit;


/***/ }),

/***/ 7978:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseLine = void 0;
const abstract_enrich_case_1 = __webpack_require__(9341);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseLine extends abstract_enrich_case_1.AbstractEnrichCase {
    constructor(semantic) {
        super(semantic);
        this.mml = semantic.mathmlTree;
    }
    static test(semantic) {
        return !!semantic.mathmlTree && semantic.type === "line";
    }
    getMathml() {
        if (this.semantic.contentNodes.length) {
            EnrichMathml.walkTree(this.semantic.contentNodes[0]);
        }
        if (this.semantic.childNodes.length) {
            EnrichMathml.walkTree(this.semantic.childNodes[0]);
        }
        (0, enrich_attr_1.setAttributes)(this.mml, this.semantic);
        return this.mml;
    }
}
exports.CaseLine = CaseLine;


/***/ }),

/***/ 2124:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseMultiindex = void 0;
const DomUtil = __webpack_require__(6671);
const abstract_enrich_case_1 = __webpack_require__(9341);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseMultiindex extends abstract_enrich_case_1.AbstractEnrichCase {
    constructor(semantic) {
        super(semantic);
        this.mml = semantic.mathmlTree;
    }
    static multiscriptIndex(index) {
        if (index.type === "punctuated" &&
            index.contentNodes[0].role === "dummy") {
            return EnrichMathml.collapsePunctuated(index);
        }
        EnrichMathml.walkTree(index);
        return index.id;
    }
    static createNone_(semantic) {
        const newNode = DomUtil.createElement('none');
        if (semantic) {
            (0, enrich_attr_1.setAttributes)(newNode, semantic);
        }
        newNode.setAttribute(enrich_attr_1.Attribute.ADDED, 'true');
        return newNode;
    }
    completeMultiscript(rightIndices, leftIndices) {
        const children = DomUtil.toArray(this.mml.childNodes).slice(1);
        let childCounter = 0;
        const completeIndices = (indices) => {
            for (let i = 0, index; (index = indices[i]); i++) {
                const child = children[childCounter];
                if (!child ||
                    index !==
                        parseInt(EnrichMathml.getInnerNode(child).getAttribute(enrich_attr_1.Attribute.ID))) {
                    const query = this.semantic.querySelectorAll((x) => x.id === index);
                    this.mml.insertBefore(CaseMultiindex.createNone_(query[0]), child || null);
                }
                else {
                    EnrichMathml.getInnerNode(child).setAttribute(enrich_attr_1.Attribute.PARENT, this.semantic.id.toString());
                    childCounter++;
                }
            }
        };
        completeIndices(rightIndices);
        if (children[childCounter] &&
            DomUtil.tagName(children[childCounter]) !== 'MPRESCRIPTS') {
            this.mml.insertBefore(children[childCounter], DomUtil.createElement('mprescripts'));
        }
        else {
            childCounter++;
        }
        completeIndices(leftIndices);
    }
}
exports.CaseMultiindex = CaseMultiindex;


/***/ }),

/***/ 4308:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseMultiscripts = void 0;
const DomUtil = __webpack_require__(6671);
const semantic_skeleton_1 = __webpack_require__(7984);
const case_multiindex_1 = __webpack_require__(2124);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseMultiscripts extends case_multiindex_1.CaseMultiindex {
    static test(semantic) {
        if (!semantic.mathmlTree) {
            return false;
        }
        const mmlTag = DomUtil.tagName(semantic.mathmlTree);
        return (mmlTag === 'MMULTISCRIPTS' &&
            (semantic.type === "superscript" ||
                semantic.type === "subscript"));
    }
    constructor(semantic) {
        super(semantic);
    }
    getMathml() {
        (0, enrich_attr_1.setAttributes)(this.mml, this.semantic);
        let baseSem, rsup, rsub;
        if (this.semantic.childNodes[0] &&
            this.semantic.childNodes[0].role === "subsup") {
            const ignore = this.semantic.childNodes[0];
            baseSem = ignore.childNodes[0];
            rsup = case_multiindex_1.CaseMultiindex.multiscriptIndex(this.semantic.childNodes[1]);
            rsub = case_multiindex_1.CaseMultiindex.multiscriptIndex(ignore.childNodes[1]);
            const collapsed = [this.semantic.id, [ignore.id, baseSem.id, rsub], rsup];
            EnrichMathml.addCollapsedAttribute(this.mml, collapsed);
            this.mml.setAttribute(enrich_attr_1.Attribute.TYPE, ignore.role);
            this.completeMultiscript(semantic_skeleton_1.SemanticSkeleton.interleaveIds(rsub, rsup), []);
        }
        else {
            baseSem = this.semantic.childNodes[0];
            rsup = case_multiindex_1.CaseMultiindex.multiscriptIndex(this.semantic.childNodes[1]);
            const collapsed = [this.semantic.id, baseSem.id, rsup];
            EnrichMathml.addCollapsedAttribute(this.mml, collapsed);
        }
        const childIds = semantic_skeleton_1.SemanticSkeleton.collapsedLeafs(rsub || [], rsup);
        const base = EnrichMathml.walkTree(baseSem);
        EnrichMathml.getInnerNode(base).setAttribute(enrich_attr_1.Attribute.PARENT, this.semantic.id.toString());
        childIds.unshift(baseSem.id);
        this.mml.setAttribute(enrich_attr_1.Attribute.CHILDREN, childIds.join(','));
        return this.mml;
    }
}
exports.CaseMultiscripts = CaseMultiscripts;


/***/ }),

/***/ 5326:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseProof = void 0;
const abstract_enrich_case_1 = __webpack_require__(9341);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseProof extends abstract_enrich_case_1.AbstractEnrichCase {
    constructor(semantic) {
        super(semantic);
        this.mml = semantic.mathmlTree;
    }
    static test(semantic) {
        return (!!semantic.mathmlTree &&
            (semantic.type === "inference" ||
                semantic.type === "premises"));
    }
    getMathml() {
        if (!this.semantic.childNodes.length) {
            return this.mml;
        }
        this.semantic.contentNodes.forEach(function (x) {
            EnrichMathml.walkTree(x);
            (0, enrich_attr_1.setAttributes)(x.mathmlTree, x);
        });
        this.semantic.childNodes.forEach(function (x) {
            EnrichMathml.walkTree(x);
        });
        (0, enrich_attr_1.setAttributes)(this.mml, this.semantic);
        if (this.mml.getAttribute('data-semantic-id') ===
            this.mml.getAttribute('data-semantic-parent')) {
            this.mml.removeAttribute('data-semantic-parent');
        }
        return this.mml;
    }
}
exports.CaseProof = CaseProof;


/***/ }),

/***/ 6998:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseTable = void 0;
const DomUtil = __webpack_require__(6671);
const abstract_enrich_case_1 = __webpack_require__(9341);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseTable extends abstract_enrich_case_1.AbstractEnrichCase {
    constructor(semantic) {
        super(semantic);
        this.inner = [];
        this.mml = semantic.mathmlTree;
    }
    static test(semantic) {
        return (semantic.type === "matrix" ||
            semantic.type === "vector" ||
            semantic.type === "cases");
    }
    getMathml() {
        const lfence = EnrichMathml.cloneContentNode(this.semantic.contentNodes[0]);
        const rfence = this.semantic.contentNodes[1]
            ? EnrichMathml.cloneContentNode(this.semantic.contentNodes[1])
            : null;
        this.inner = this.semantic.childNodes.map(EnrichMathml.walkTree);
        if (!this.mml) {
            this.mml = EnrichMathml.introduceNewLayer([lfence].concat(this.inner, [rfence]), this.semantic);
        }
        else if (DomUtil.tagName(this.mml) === 'MFENCED') {
            const children = this.mml.childNodes;
            this.mml.insertBefore(lfence, children[0] || null);
            rfence && this.mml.appendChild(rfence);
            this.mml = EnrichMathml.rewriteMfenced(this.mml);
        }
        else {
            const newChildren = [lfence, this.mml];
            rfence && newChildren.push(rfence);
            this.mml = EnrichMathml.introduceNewLayer(newChildren, this.semantic);
        }
        (0, enrich_attr_1.setAttributes)(this.mml, this.semantic);
        return this.mml;
    }
}
exports.CaseTable = CaseTable;


/***/ }),

/***/ 439:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseTensor = void 0;
const semantic_skeleton_1 = __webpack_require__(7984);
const case_multiindex_1 = __webpack_require__(2124);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseTensor extends case_multiindex_1.CaseMultiindex {
    static test(semantic) {
        return !!semantic.mathmlTree && semantic.type === "tensor";
    }
    constructor(semantic) {
        super(semantic);
    }
    getMathml() {
        EnrichMathml.walkTree(this.semantic.childNodes[0]);
        const lsub = case_multiindex_1.CaseMultiindex.multiscriptIndex(this.semantic.childNodes[1]);
        const lsup = case_multiindex_1.CaseMultiindex.multiscriptIndex(this.semantic.childNodes[2]);
        const rsub = case_multiindex_1.CaseMultiindex.multiscriptIndex(this.semantic.childNodes[3]);
        const rsup = case_multiindex_1.CaseMultiindex.multiscriptIndex(this.semantic.childNodes[4]);
        (0, enrich_attr_1.setAttributes)(this.mml, this.semantic);
        const collapsed = [
            this.semantic.id,
            this.semantic.childNodes[0].id,
            lsub,
            lsup,
            rsub,
            rsup
        ];
        EnrichMathml.addCollapsedAttribute(this.mml, collapsed);
        const childIds = semantic_skeleton_1.SemanticSkeleton.collapsedLeafs(lsub, lsup, rsub, rsup);
        childIds.unshift(this.semantic.childNodes[0].id);
        this.mml.setAttribute(enrich_attr_1.Attribute.CHILDREN, childIds.join(','));
        this.completeMultiscript(semantic_skeleton_1.SemanticSkeleton.interleaveIds(rsub, rsup), semantic_skeleton_1.SemanticSkeleton.interleaveIds(lsub, lsup));
        return this.mml;
    }
}
exports.CaseTensor = CaseTensor;


/***/ }),

/***/ 598:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CaseText = void 0;
const abstract_enrich_case_1 = __webpack_require__(9341);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
class CaseText extends abstract_enrich_case_1.AbstractEnrichCase {
    constructor(semantic) {
        super(semantic);
        this.mml = semantic.mathmlTree;
    }
    static test(semantic) {
        return (semantic.type === "punctuated" &&
            (semantic.role === "text" ||
                semantic.contentNodes.every((x) => x.role === "dummy")));
    }
    getMathml() {
        const children = [];
        const collapsed = EnrichMathml.collapsePunctuated(this.semantic, children);
        this.mml = EnrichMathml.introduceNewLayer(children, this.semantic);
        (0, enrich_attr_1.setAttributes)(this.mml, this.semantic);
        this.mml.removeAttribute(enrich_attr_1.Attribute.CONTENT);
        EnrichMathml.addCollapsedAttribute(this.mml, collapsed);
        return this.mml;
    }
}
exports.CaseText = CaseText;


/***/ }),

/***/ 7450:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.prepareMmlString = exports.testTranslation__ = exports.semanticMathml = exports.semanticMathmlSync = exports.semanticMathmlNode = void 0;
const debugger_1 = __webpack_require__(1984);
const DomUtil = __webpack_require__(6671);
const engine_1 = __webpack_require__(4886);
const Semantic = __webpack_require__(1939);
const EnrichMathml = __webpack_require__(8672);
const enrich_attr_1 = __webpack_require__(8171);
__webpack_require__(7813);
function semanticMathmlNode(mml) {
    const clone = DomUtil.cloneNode(mml);
    const tree = Semantic.getTree(clone);
    return EnrichMathml.enrich(clone, tree);
}
exports.semanticMathmlNode = semanticMathmlNode;
function semanticMathmlSync(expr) {
    const mml = DomUtil.parseInput(expr);
    return semanticMathmlNode(mml);
}
exports.semanticMathmlSync = semanticMathmlSync;
function semanticMathml(expr, callback) {
    engine_1.EnginePromise.getall().then(() => {
        const mml = DomUtil.parseInput(expr);
        callback(semanticMathmlNode(mml));
    });
}
exports.semanticMathml = semanticMathml;
function testTranslation__(expr) {
    debugger_1.Debugger.getInstance().init();
    const mml = semanticMathmlSync(prepareMmlString(expr)).toString();
    (0, enrich_attr_1.removeAttributePrefix)(mml);
    debugger_1.Debugger.getInstance().exit();
    return mml;
}
exports.testTranslation__ = testTranslation__;
function prepareMmlString(expr) {
    if (!expr.match(/^<math/)) {
        expr = '<math>' + expr;
    }
    if (!expr.match(/\/math>$/)) {
        expr += '</math>';
    }
    return expr;
}
exports.prepareMmlString = prepareMmlString;


/***/ }),

/***/ 8171:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.addPrefix = exports.removeAttributePrefix = exports.setPostfix = exports.setAttributes = exports.makeIdList = exports.EnrichAttributes = exports.Attribute = exports.Prefix = void 0;
exports.Prefix = 'data-semantic-';
var Attribute;
(function (Attribute) {
    Attribute["ADDED"] = "data-semantic-added";
    Attribute["ALTERNATIVE"] = "data-semantic-alternative";
    Attribute["CHILDREN"] = "data-semantic-children";
    Attribute["COLLAPSED"] = "data-semantic-collapsed";
    Attribute["CONTENT"] = "data-semantic-content";
    Attribute["EMBELLISHED"] = "data-semantic-embellished";
    Attribute["FENCEPOINTER"] = "data-semantic-fencepointer";
    Attribute["FONT"] = "data-semantic-font";
    Attribute["ID"] = "data-semantic-id";
    Attribute["ANNOTATION"] = "data-semantic-annotation";
    Attribute["OPERATOR"] = "data-semantic-operator";
    Attribute["OWNS"] = "data-semantic-owns";
    Attribute["PARENT"] = "data-semantic-parent";
    Attribute["POSTFIX"] = "data-semantic-postfix";
    Attribute["PREFIX"] = "data-semantic-prefix";
    Attribute["ROLE"] = "data-semantic-role";
    Attribute["SPEECH"] = "data-semantic-speech";
    Attribute["STRUCTURE"] = "data-semantic-structure";
    Attribute["TYPE"] = "data-semantic-type";
})(Attribute = exports.Attribute || (exports.Attribute = {}));
exports.EnrichAttributes = [
    Attribute.ADDED,
    Attribute.ALTERNATIVE,
    Attribute.CHILDREN,
    Attribute.COLLAPSED,
    Attribute.CONTENT,
    Attribute.EMBELLISHED,
    Attribute.FENCEPOINTER,
    Attribute.FONT,
    Attribute.ID,
    Attribute.ANNOTATION,
    Attribute.OPERATOR,
    Attribute.OWNS,
    Attribute.PARENT,
    Attribute.POSTFIX,
    Attribute.PREFIX,
    Attribute.ROLE,
    Attribute.SPEECH,
    Attribute.STRUCTURE,
    Attribute.TYPE
];
function makeIdList(nodes) {
    return nodes
        .map(function (node) {
        return node.id;
    })
        .join(',');
}
exports.makeIdList = makeIdList;
function setAttributes(mml, semantic) {
    mml.setAttribute(Attribute.TYPE, semantic.type);
    const attributes = semantic.allAttributes();
    for (let i = 0, attr; (attr = attributes[i]); i++) {
        mml.setAttribute(exports.Prefix + attr[0].toLowerCase(), attr[1]);
    }
    if (semantic.childNodes.length) {
        mml.setAttribute(Attribute.CHILDREN, makeIdList(semantic.childNodes));
    }
    if (semantic.contentNodes.length) {
        mml.setAttribute(Attribute.CONTENT, makeIdList(semantic.contentNodes));
    }
    if (semantic.parent) {
        mml.setAttribute(Attribute.PARENT, semantic.parent.id.toString());
    }
    setPostfix(mml, semantic);
}
exports.setAttributes = setAttributes;
function setPostfix(mml, semantic) {
    const postfix = [];
    if (semantic.role === "mglyph") {
        postfix.push('image');
    }
    if (semantic.attributes['href']) {
        postfix.push('link');
    }
    if (postfix.length) {
        mml.setAttribute(Attribute.POSTFIX, postfix.join(' '));
    }
}
exports.setPostfix = setPostfix;
function removeAttributePrefix(mml) {
    return mml.toString().replace(new RegExp(exports.Prefix, 'g'), '');
}
exports.removeAttributePrefix = removeAttributePrefix;
function addPrefix(attr) {
    return (exports.Prefix + attr);
}
exports.addPrefix = addPrefix;


/***/ }),

/***/ 9775:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.factory = exports.getCase = void 0;
function getCase(node) {
    for (let i = 0, enrich; (enrich = exports.factory[i]); i++) {
        if (enrich.test(node)) {
            return enrich.constr(node);
        }
    }
    return null;
}
exports.getCase = getCase;
exports.factory = [];


/***/ }),

/***/ 7813:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const case_binomial_1 = __webpack_require__(4306);
const case_double_script_1 = __webpack_require__(8871);
const case_embellished_1 = __webpack_require__(928);
const case_limit_1 = __webpack_require__(9763);
const case_line_1 = __webpack_require__(7978);
const case_multiscripts_1 = __webpack_require__(4308);
const case_proof_1 = __webpack_require__(5326);
const case_table_1 = __webpack_require__(6998);
const case_tensor_1 = __webpack_require__(439);
const case_text_1 = __webpack_require__(598);
const enrich_case_1 = __webpack_require__(9775);
enrich_case_1.factory.push(...[
    {
        test: case_limit_1.CaseLimit.test,
        constr: (node) => new case_limit_1.CaseLimit(node)
    },
    {
        test: case_embellished_1.CaseEmbellished.test,
        constr: (node) => new case_embellished_1.CaseEmbellished(node)
    },
    {
        test: case_double_script_1.CaseDoubleScript.test,
        constr: (node) => new case_double_script_1.CaseDoubleScript(node)
    },
    {
        test: case_tensor_1.CaseTensor.test,
        constr: (node) => new case_tensor_1.CaseTensor(node)
    },
    {
        test: case_multiscripts_1.CaseMultiscripts.test,
        constr: (node) => new case_multiscripts_1.CaseMultiscripts(node)
    },
    { test: case_line_1.CaseLine.test, constr: (node) => new case_line_1.CaseLine(node) },
    {
        test: case_binomial_1.CaseBinomial.test,
        constr: (node) => new case_binomial_1.CaseBinomial(node)
    },
    {
        test: case_proof_1.CaseProof.test,
        constr: (node) => new case_proof_1.CaseProof(node)
    },
    {
        test: case_table_1.CaseTable.test,
        constr: (node) => new case_table_1.CaseTable(node)
    },
    { test: case_text_1.CaseText.test, constr: (node) => new case_text_1.CaseText(node) }
]);


/***/ }),

/***/ 8672:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.printNodeList__ = exports.collapsePunctuated = exports.formattedOutput_ = exports.formattedOutput = exports.getInnerNode = exports.setOperatorAttribute_ = exports.createInvisibleOperator_ = exports.rewriteMfenced = exports.cloneContentNode = exports.addCollapsedAttribute = exports.parentNode_ = exports.isIgnorable_ = exports.unitChild_ = exports.descendNode_ = exports.ascendNewNode = exports.validLca_ = exports.pathToRoot_ = exports.attachedElement_ = exports.prunePath_ = exports.mathmlLca_ = exports.lcaType = exports.functionApplication_ = exports.isDescendant_ = exports.insertNewChild_ = exports.mergeChildren_ = exports.collectChildNodes_ = exports.collateChildNodes_ = exports.childrenSubset_ = exports.moveSemanticAttributes_ = exports.introduceLayerAboveLca = exports.introduceNewLayer = exports.walkTree = exports.enrich = exports.SETTINGS = void 0;
const debugger_1 = __webpack_require__(1984);
const DomUtil = __webpack_require__(6671);
const engine_1 = __webpack_require__(4886);
const SemanticAttr = __webpack_require__(4020);
const SemanticHeuristics = __webpack_require__(2721);
const semantic_skeleton_1 = __webpack_require__(7984);
const SemanticUtil = __webpack_require__(8901);
const EnrichAttr = __webpack_require__(8171);
const enrich_case_1 = __webpack_require__(9775);
exports.SETTINGS = {
    collapsed: true,
    implicit: true
};
function enrich(mml, semantic) {
    const oldMml = DomUtil.cloneNode(mml);
    walkTree(semantic.root);
    if (engine_1.default.getInstance().structure) {
        mml.setAttribute(EnrichAttr.Attribute.STRUCTURE, semantic_skeleton_1.SemanticSkeleton.fromStructure(mml, semantic).toString());
    }
    debugger_1.Debugger.getInstance().generateOutput(function () {
        formattedOutput(oldMml, mml, semantic, true);
        return [];
    });
    return mml;
}
exports.enrich = enrich;
function walkTree(semantic) {
    const specialCase = (0, enrich_case_1.getCase)(semantic);
    let newNode;
    if (specialCase) {
        newNode = specialCase.getMathml();
        return ascendNewNode(newNode);
    }
    if (semantic.mathml.length === 1) {
        debugger_1.Debugger.getInstance().output('Walktree Case 0');
        newNode = semantic.mathml[0];
        EnrichAttr.setAttributes(newNode, semantic);
        if (semantic.childNodes.length) {
            debugger_1.Debugger.getInstance().output('Walktree Case 0.1');
            semantic.childNodes.forEach(function (child) {
                if (child.type === "empty") {
                    newNode.appendChild(walkTree(child));
                }
            });
        }
        return ascendNewNode(newNode);
    }
    const newContent = semantic.contentNodes.map(cloneContentNode);
    setOperatorAttribute_(semantic, newContent);
    const newChildren = semantic.childNodes.map(walkTree);
    const childrenList = semantic_skeleton_1.SemanticSkeleton.combineContentChildren(semantic, newContent, newChildren);
    newNode = semantic.mathmlTree;
    if (newNode === null) {
        debugger_1.Debugger.getInstance().output('Walktree Case 1');
        newNode = introduceNewLayer(childrenList, semantic);
    }
    else {
        const attached = attachedElement_(childrenList);
        debugger_1.Debugger.getInstance().output('Walktree Case 2');
        if (attached) {
            debugger_1.Debugger.getInstance().output('Walktree Case 2.1');
            newNode = attached.parentNode;
        }
        else {
            debugger_1.Debugger.getInstance().output('Walktree Case 2.2');
            newNode = getInnerNode(newNode);
        }
    }
    newNode = rewriteMfenced(newNode);
    mergeChildren_(newNode, childrenList, semantic);
    EnrichAttr.setAttributes(newNode, semantic);
    return ascendNewNode(newNode);
}
exports.walkTree = walkTree;
function introduceNewLayer(children, semantic) {
    const lca = mathmlLca_(children);
    let newNode = lca.node;
    const info = lca.type;
    if (info !== lcaType.VALID || !SemanticUtil.hasEmptyTag(newNode)) {
        debugger_1.Debugger.getInstance().output('Walktree Case 1.1');
        newNode = DomUtil.createElement('mrow');
        if (info === lcaType.PRUNED) {
            debugger_1.Debugger.getInstance().output('Walktree Case 1.1.0');
            newNode = introduceLayerAboveLca(newNode, lca.node, children);
        }
        else if (children[0]) {
            debugger_1.Debugger.getInstance().output('Walktree Case 1.1.1');
            const node = attachedElement_(children);
            const oldChildren = childrenSubset_(node.parentNode, children);
            DomUtil.replaceNode(node, newNode);
            oldChildren.forEach(function (x) {
                newNode.appendChild(x);
            });
        }
    }
    if (!semantic.mathmlTree) {
        semantic.mathmlTree = newNode;
    }
    return newNode;
}
exports.introduceNewLayer = introduceNewLayer;
function introduceLayerAboveLca(mrow, lca, children) {
    let innerNode = descendNode_(lca);
    if (SemanticUtil.hasMathTag(innerNode)) {
        debugger_1.Debugger.getInstance().output('Walktree Case 1.1.0.0');
        moveSemanticAttributes_(innerNode, mrow);
        DomUtil.toArray(innerNode.childNodes).forEach(function (x) {
            mrow.appendChild(x);
        });
        const auxNode = mrow;
        mrow = innerNode;
        innerNode = auxNode;
    }
    const index = children.indexOf(lca);
    children[index] = innerNode;
    DomUtil.replaceNode(innerNode, mrow);
    mrow.appendChild(innerNode);
    children.forEach(function (x) {
        mrow.appendChild(x);
    });
    return mrow;
}
exports.introduceLayerAboveLca = introduceLayerAboveLca;
function moveSemanticAttributes_(oldNode, newNode) {
    for (const attr of EnrichAttr.EnrichAttributes) {
        if (oldNode.hasAttribute(attr)) {
            newNode.setAttribute(attr, oldNode.getAttribute(attr));
            oldNode.removeAttribute(attr);
        }
    }
}
exports.moveSemanticAttributes_ = moveSemanticAttributes_;
function childrenSubset_(node, newChildren) {
    const oldChildren = DomUtil.toArray(node.childNodes);
    let leftIndex = +Infinity;
    let rightIndex = -Infinity;
    newChildren.forEach(function (child) {
        const index = oldChildren.indexOf(child);
        if (index !== -1) {
            leftIndex = Math.min(leftIndex, index);
            rightIndex = Math.max(rightIndex, index);
        }
    });
    return oldChildren.slice(leftIndex, rightIndex + 1);
}
exports.childrenSubset_ = childrenSubset_;
function collateChildNodes_(node, children, semantic) {
    const oldChildren = [];
    let newChildren = DomUtil.toArray(node.childNodes);
    let notFirst = false;
    while (newChildren.length) {
        const child = newChildren.shift();
        if (child.hasAttribute(EnrichAttr.Attribute.TYPE)) {
            oldChildren.push(child);
            continue;
        }
        const collect = collectChildNodes_(child);
        if (collect.length === 0) {
            continue;
        }
        if (collect.length === 1) {
            oldChildren.push(child);
            continue;
        }
        if (notFirst) {
            child.setAttribute('AuxiliaryImplicit', true);
        }
        else {
            notFirst = true;
        }
        newChildren = collect.concat(newChildren);
    }
    const rear = [];
    const semChildren = semantic.childNodes.map(function (x) {
        return x.mathmlTree;
    });
    while (semChildren.length) {
        const schild = semChildren.pop();
        if (!schild) {
            continue;
        }
        if (oldChildren.indexOf(schild) !== -1) {
            break;
        }
        if (children.indexOf(schild) !== -1) {
            rear.unshift(schild);
        }
    }
    return oldChildren.concat(rear);
}
exports.collateChildNodes_ = collateChildNodes_;
function collectChildNodes_(node) {
    const collect = [];
    let newChildren = DomUtil.toArray(node.childNodes);
    while (newChildren.length) {
        const child = newChildren.shift();
        if (child.nodeType !== DomUtil.NodeType.ELEMENT_NODE) {
            continue;
        }
        if (child.hasAttribute(EnrichAttr.Attribute.TYPE)) {
            collect.push(child);
            continue;
        }
        newChildren = DomUtil.toArray(child.childNodes).concat(newChildren);
    }
    return collect;
}
exports.collectChildNodes_ = collectChildNodes_;
function mergeChildren_(node, newChildren, semantic) {
    const oldChildren = semantic.role === "implicit" &&
        SemanticHeuristics.flags.combine_juxtaposition
        ? collateChildNodes_(node, newChildren, semantic)
        : DomUtil.toArray(node.childNodes);
    if (!oldChildren.length) {
        newChildren.forEach(function (x) {
            node.appendChild(x);
        });
        return;
    }
    let oldCounter = 0;
    while (newChildren.length) {
        const newChild = newChildren[0];
        if (oldChildren[oldCounter] === newChild ||
            functionApplication_(oldChildren[oldCounter], newChild)) {
            newChildren.shift();
            oldCounter++;
            continue;
        }
        if (oldChildren[oldCounter] &&
            newChildren.indexOf(oldChildren[oldCounter]) === -1) {
            oldCounter++;
            continue;
        }
        if (isDescendant_(newChild, node)) {
            newChildren.shift();
            continue;
        }
        insertNewChild_(node, oldChildren[oldCounter], newChild);
        newChildren.shift();
    }
}
exports.mergeChildren_ = mergeChildren_;
function insertNewChild_(node, oldChild, newChild) {
    if (!oldChild) {
        node.insertBefore(newChild, null);
        return;
    }
    let parent = oldChild;
    let next = parentNode_(parent);
    while (next &&
        next.firstChild === parent &&
        !parent.hasAttribute('AuxiliaryImplicit') &&
        next !== node) {
        parent = next;
        next = parentNode_(parent);
    }
    if (next) {
        next.insertBefore(newChild, parent);
        parent.removeAttribute('AuxiliaryImplicit');
    }
}
exports.insertNewChild_ = insertNewChild_;
function isDescendant_(child, node) {
    if (!child) {
        return false;
    }
    do {
        child = child.parentNode;
        if (child === node) {
            return true;
        }
    } while (child);
    return false;
}
exports.isDescendant_ = isDescendant_;
function functionApplication_(oldNode, newNode) {
    const appl = SemanticAttr.functionApplication();
    if (oldNode &&
        newNode &&
        oldNode.textContent &&
        newNode.textContent &&
        oldNode.textContent === appl &&
        newNode.textContent === appl &&
        newNode.getAttribute(EnrichAttr.Attribute.ADDED) === 'true') {
        for (let i = 0, attr; (attr = oldNode.attributes[i]); i++) {
            if (!newNode.hasAttribute(attr.nodeName)) {
                newNode.setAttribute(attr.nodeName, attr.nodeValue);
            }
        }
        DomUtil.replaceNode(oldNode, newNode);
        return true;
    }
    return false;
}
exports.functionApplication_ = functionApplication_;
var lcaType;
(function (lcaType) {
    lcaType["VALID"] = "valid";
    lcaType["INVALID"] = "invalid";
    lcaType["PRUNED"] = "pruned";
})(lcaType = exports.lcaType || (exports.lcaType = {}));
function mathmlLca_(children) {
    const leftMost = attachedElement_(children);
    if (!leftMost) {
        return { type: lcaType.INVALID, node: null };
    }
    const rightMost = attachedElement_(children.slice().reverse());
    if (leftMost === rightMost) {
        return { type: lcaType.VALID, node: leftMost };
    }
    const leftPath = pathToRoot_(leftMost);
    const newLeftPath = prunePath_(leftPath, children);
    const rightPath = pathToRoot_(rightMost, function (x) {
        return newLeftPath.indexOf(x) !== -1;
    });
    const lca = rightPath[0];
    const lIndex = newLeftPath.indexOf(lca);
    if (lIndex === -1) {
        return { type: lcaType.INVALID, node: null };
    }
    return {
        type: newLeftPath.length !== leftPath.length
            ? lcaType.PRUNED
            : validLca_(newLeftPath[lIndex + 1], rightPath[1])
                ? lcaType.VALID
                : lcaType.INVALID,
        node: lca
    };
}
exports.mathmlLca_ = mathmlLca_;
function prunePath_(path, children) {
    let i = 0;
    while (path[i] && children.indexOf(path[i]) === -1) {
        i++;
    }
    return path.slice(0, i + 1);
}
exports.prunePath_ = prunePath_;
function attachedElement_(nodes) {
    let count = 0;
    let attached = null;
    while (!attached && count < nodes.length) {
        if (nodes[count].parentNode) {
            attached = nodes[count];
        }
        count++;
    }
    return attached;
}
exports.attachedElement_ = attachedElement_;
function pathToRoot_(node, opt_test) {
    const test = opt_test || ((_x) => false);
    const path = [node];
    while (!test(node) && !SemanticUtil.hasMathTag(node) && node.parentNode) {
        node = parentNode_(node);
        path.unshift(node);
    }
    return path;
}
exports.pathToRoot_ = pathToRoot_;
function validLca_(left, right) {
    return !!(left && right && !left.previousSibling && !right.nextSibling);
}
exports.validLca_ = validLca_;
function ascendNewNode(newNode) {
    while (!SemanticUtil.hasMathTag(newNode) && unitChild_(newNode)) {
        newNode = parentNode_(newNode);
    }
    return newNode;
}
exports.ascendNewNode = ascendNewNode;
function descendNode_(node) {
    const children = DomUtil.toArray(node.childNodes);
    if (!children) {
        return node;
    }
    const remainder = children.filter(function (child) {
        return (child.nodeType === DomUtil.NodeType.ELEMENT_NODE &&
            !SemanticUtil.hasIgnoreTag(child));
    });
    if (remainder.length === 1 &&
        SemanticUtil.hasEmptyTag(remainder[0]) &&
        !remainder[0].hasAttribute(EnrichAttr.Attribute.TYPE)) {
        return descendNode_(remainder[0]);
    }
    return node;
}
exports.descendNode_ = descendNode_;
function unitChild_(node) {
    const parent = parentNode_(node);
    if (!parent || !SemanticUtil.hasEmptyTag(parent)) {
        return false;
    }
    return DomUtil.toArray(parent.childNodes).every(function (child) {
        return child === node || isIgnorable_(child);
    });
}
exports.unitChild_ = unitChild_;
function isIgnorable_(node) {
    if (node.nodeType !== DomUtil.NodeType.ELEMENT_NODE) {
        return true;
    }
    if (!node || SemanticUtil.hasIgnoreTag(node)) {
        return true;
    }
    const children = DomUtil.toArray(node.childNodes);
    if ((!SemanticUtil.hasEmptyTag(node) && children.length) ||
        SemanticUtil.hasDisplayTag(node) ||
        node.hasAttribute(EnrichAttr.Attribute.TYPE) ||
        SemanticUtil.isOrphanedGlyph(node)) {
        return false;
    }
    return DomUtil.toArray(node.childNodes).every(isIgnorable_);
}
exports.isIgnorable_ = isIgnorable_;
function parentNode_(element) {
    return element.parentNode;
}
exports.parentNode_ = parentNode_;
function addCollapsedAttribute(node, collapsed) {
    const skeleton = new semantic_skeleton_1.SemanticSkeleton(collapsed);
    node.setAttribute(EnrichAttr.Attribute.COLLAPSED, skeleton.toString());
}
exports.addCollapsedAttribute = addCollapsedAttribute;
function cloneContentNode(content) {
    if (content.mathml.length) {
        return walkTree(content);
    }
    const clone = exports.SETTINGS.implicit
        ? createInvisibleOperator_(content)
        : DomUtil.createElement('mrow');
    content.mathml = [clone];
    return clone;
}
exports.cloneContentNode = cloneContentNode;
function rewriteMfenced(mml) {
    if (DomUtil.tagName(mml) !== 'MFENCED') {
        return mml;
    }
    const newNode = DomUtil.createElement('mrow');
    for (let i = 0, attr; (attr = mml.attributes[i]); i++) {
        if (['open', 'close', 'separators'].indexOf(attr.name) === -1) {
            newNode.setAttribute(attr.name, attr.value);
        }
    }
    DomUtil.toArray(mml.childNodes).forEach(function (x) {
        newNode.appendChild(x);
    });
    DomUtil.replaceNode(mml, newNode);
    return newNode;
}
exports.rewriteMfenced = rewriteMfenced;
function createInvisibleOperator_(operator) {
    const moNode = DomUtil.createElement('mo');
    const text = DomUtil.createTextNode(operator.textContent);
    moNode.appendChild(text);
    EnrichAttr.setAttributes(moNode, operator);
    moNode.setAttribute(EnrichAttr.Attribute.ADDED, 'true');
    return moNode;
}
exports.createInvisibleOperator_ = createInvisibleOperator_;
function setOperatorAttribute_(semantic, content) {
    const operator = semantic.type + (semantic.textContent ? ',' + semantic.textContent : '');
    content.forEach(function (c) {
        getInnerNode(c).setAttribute(EnrichAttr.Attribute.OPERATOR, operator);
    });
}
exports.setOperatorAttribute_ = setOperatorAttribute_;
function getInnerNode(node) {
    const children = DomUtil.toArray(node.childNodes);
    if (!children) {
        return node;
    }
    const remainder = children.filter(function (child) {
        return !isIgnorable_(child);
    });
    const result = [];
    for (let i = 0, remain; (remain = remainder[i]); i++) {
        if (SemanticUtil.hasEmptyTag(remain)) {
            const nextInner = getInnerNode(remain);
            if (nextInner && nextInner !== remain) {
                result.push(nextInner);
            }
        }
        else {
            result.push(remain);
        }
    }
    if (result.length === 1) {
        return result[0];
    }
    return node;
}
exports.getInnerNode = getInnerNode;
function formattedOutput(mml, expr, tree, opt_wiki) {
    const wiki = opt_wiki || false;
    formattedOutput_(mml, 'Original MathML', wiki);
    formattedOutput_(tree, 'Semantic Tree', wiki);
    formattedOutput_(expr, 'Semantically enriched MathML', wiki);
}
exports.formattedOutput = formattedOutput;
function formattedOutput_(element, name, wiki) {
    const output = DomUtil.formatXml(element.toString());
    if (!wiki) {
        console.info(output);
        return;
    }
    console.info(name + ':\n```html\n' + EnrichAttr.removeAttributePrefix(output) + '\n```\n');
}
exports.formattedOutput_ = formattedOutput_;
function collapsePunctuated(semantic, opt_children) {
    const optional = !!opt_children;
    const children = opt_children || [];
    const parent = semantic.parent;
    const contentIds = semantic.contentNodes.map(function (x) {
        return x.id;
    });
    contentIds.unshift('c');
    const childIds = [semantic.id, contentIds];
    for (let i = 0, child; (child = semantic.childNodes[i]); i++) {
        const mmlChild = walkTree(child);
        children.push(mmlChild);
        const innerNode = getInnerNode(mmlChild);
        if (parent && !optional) {
            innerNode.setAttribute(EnrichAttr.Attribute.PARENT, parent.id.toString());
        }
        childIds.push(child.id);
    }
    return childIds;
}
exports.collapsePunctuated = collapsePunctuated;
function printNodeList__(title, nodes) {
    console.info(title);
    DomUtil.toArray(nodes).forEach(function (x) {
        console.info(x.toString());
    });
    console.info('<<<<<<<<<<<<<<<<<');
}
exports.printNodeList__ = printNodeList__;


/***/ }),

/***/ 7228:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AbstractHighlighter = void 0;
const XpathUtil = __webpack_require__(5024);
const enrich_attr_1 = __webpack_require__(8171);
class AbstractHighlighter {
    constructor() {
        this.color = null;
        this.mactionName = '';
        this.currentHighlights = [];
    }
    highlight(nodes) {
        this.currentHighlights.push(nodes.map((node) => {
            const info = this.highlightNode(node);
            this.setHighlighted(node);
            return info;
        }));
    }
    highlightAll(node) {
        const mactions = this.getMactionNodes(node);
        for (let i = 0, maction; (maction = mactions[i]); i++) {
            this.highlight([maction]);
        }
    }
    unhighlight() {
        const nodes = this.currentHighlights.pop();
        if (!nodes) {
            return;
        }
        nodes.forEach((highlight) => {
            if (this.isHighlighted(highlight.node)) {
                this.unhighlightNode(highlight);
                this.unsetHighlighted(highlight.node);
            }
        });
    }
    unhighlightAll() {
        while (this.currentHighlights.length > 0) {
            this.unhighlight();
        }
    }
    setColor(color) {
        this.color = color;
    }
    colorString() {
        return this.color.rgba();
    }
    addEvents(node, events) {
        const mactions = this.getMactionNodes(node);
        for (let i = 0, maction; (maction = mactions[i]); i++) {
            for (const event in events) {
                maction.addEventListener(event, events[event]);
            }
        }
    }
    getMactionNodes(node) {
        return Array.from(node.getElementsByClassName(this.mactionName));
    }
    isMactionNode(node) {
        const className = node.className || node.getAttribute('class');
        return className ? !!className.match(new RegExp(this.mactionName)) : false;
    }
    isHighlighted(node) {
        return node.hasAttribute(AbstractHighlighter.ATTR);
    }
    setHighlighted(node) {
        node.setAttribute(AbstractHighlighter.ATTR, 'true');
    }
    unsetHighlighted(node) {
        node.removeAttribute(AbstractHighlighter.ATTR);
    }
    colorizeAll(node) {
        const allNodes = XpathUtil.evalXPath(`.//*[@${enrich_attr_1.Attribute.ID}]`, node);
        allNodes.forEach((x) => this.colorize(x));
    }
    uncolorizeAll(node) {
        const allNodes = XpathUtil.evalXPath(`.//*[@${enrich_attr_1.Attribute.ID}]`, node);
        allNodes.forEach((x) => this.uncolorize(x));
    }
    colorize(node) {
        const fore = (0, enrich_attr_1.addPrefix)('foreground');
        if (node.hasAttribute(fore)) {
            node.setAttribute(fore + '-old', node.style.color);
            node.style.color = node.getAttribute(fore);
        }
    }
    uncolorize(node) {
        const fore = (0, enrich_attr_1.addPrefix)('foreground') + '-old';
        if (node.hasAttribute(fore)) {
            node.style.color = node.getAttribute(fore);
        }
    }
}
exports.AbstractHighlighter = AbstractHighlighter;
AbstractHighlighter.ATTR = 'sre-highlight';


/***/ }),

/***/ 7567:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ChtmlHighlighter = void 0;
const css_highlighter_1 = __webpack_require__(9400);
class ChtmlHighlighter extends css_highlighter_1.CssHighlighter {
    constructor() {
        super();
    }
    isMactionNode(node) {
        return node.tagName.toUpperCase() === this.mactionName.toUpperCase();
    }
    getMactionNodes(node) {
        return Array.from(node.getElementsByTagName(this.mactionName));
    }
}
exports.ChtmlHighlighter = ChtmlHighlighter;


/***/ }),

/***/ 1123:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ContrastPicker = exports.ColorPicker = void 0;
const namedColors = {
    red: { red: 255, green: 0, blue: 0 },
    green: { red: 0, green: 255, blue: 0 },
    blue: { red: 0, green: 0, blue: 255 },
    yellow: { red: 255, green: 255, blue: 0 },
    cyan: { red: 0, green: 255, blue: 255 },
    magenta: { red: 255, green: 0, blue: 255 },
    white: { red: 255, green: 255, blue: 255 },
    black: { red: 0, green: 0, blue: 0 }
};
function getChannelColor(color, deflt) {
    const col = color || { color: deflt };
    let channel = Object.prototype.hasOwnProperty.call(col, 'color')
        ? namedColors[col.color]
        : col;
    if (!channel) {
        channel = namedColors[deflt];
    }
    channel.alpha = Object.prototype.hasOwnProperty.call(col, 'alpha')
        ? col.alpha
        : 1;
    return normalizeColor(channel);
}
function normalizeColor(color) {
    const normalizeCol = (col) => {
        col = Math.max(col, 0);
        col = Math.min(255, col);
        return Math.round(col);
    };
    color.red = normalizeCol(color.red);
    color.green = normalizeCol(color.green);
    color.blue = normalizeCol(color.blue);
    color.alpha = Math.max(color.alpha, 0);
    color.alpha = Math.min(1, color.alpha);
    return color;
}
class ColorPicker {
    constructor(background, foreground) {
        this.foreground = getChannelColor(foreground, ColorPicker.DEFAULT_FOREGROUND_);
        this.background = getChannelColor(background, ColorPicker.DEFAULT_BACKGROUND_);
    }
    static toHex(num) {
        const hex = num.toString(16);
        return hex.length === 1 ? '0' + hex : hex;
    }
    rgba() {
        const rgba = function (col) {
            return ('rgba(' +
                col.red +
                ',' +
                col.green +
                ',' +
                col.blue +
                ',' +
                col.alpha +
                ')');
        };
        return {
            background: rgba(this.background),
            foreground: rgba(this.foreground)
        };
    }
    rgb() {
        const rgb = function (col) {
            return 'rgb(' + col.red + ',' + col.green + ',' + col.blue + ')';
        };
        return {
            background: rgb(this.background),
            alphaback: this.background.alpha.toString(),
            foreground: rgb(this.foreground),
            alphafore: this.foreground.alpha.toString()
        };
    }
    hex() {
        const hex = function (col) {
            return ('#' +
                ColorPicker.toHex(col.red) +
                ColorPicker.toHex(col.green) +
                ColorPicker.toHex(col.blue));
        };
        return {
            background: hex(this.background),
            alphaback: this.background.alpha.toString(),
            foreground: hex(this.foreground),
            alphafore: this.foreground.alpha.toString()
        };
    }
}
exports.ColorPicker = ColorPicker;
ColorPicker.DEFAULT_BACKGROUND_ = 'blue';
ColorPicker.DEFAULT_FOREGROUND_ = 'black';
function hsl2rgb(h, s, l) {
    s = s > 1 ? s / 100 : s;
    l = l > 1 ? l / 100 : l;
    const c = (1 - Math.abs(2 * l - 1)) * s;
    const x = c * (1 - Math.abs(((h / 60) % 2) - 1));
    const m = l - c / 2;
    let r = 0, g = 0, b = 0;
    if (0 <= h && h < 60) {
        [r, g, b] = [c, x, 0];
    }
    else if (60 <= h && h < 120) {
        [r, g, b] = [x, c, 0];
    }
    else if (120 <= h && h < 180) {
        [r, g, b] = [0, c, x];
    }
    else if (180 <= h && h < 240) {
        [r, g, b] = [0, x, c];
    }
    else if (240 <= h && h < 300) {
        [r, g, b] = [x, 0, c];
    }
    else if (300 <= h && h < 360) {
        [r, g, b] = [c, 0, x];
    }
    return { red: r + m, green: g + m, blue: b + m };
}
function rgb2RGB(rgb) {
    return {
        red: Math.round(255 * rgb.red),
        green: Math.round(255 * rgb.green),
        blue: Math.round(255 * rgb.blue)
    };
}
function RGB2hex(col) {
    return 'rgb(' + col.red + ',' + col.green + ',' + col.blue + ')';
}
class ContrastPicker {
    constructor() {
        this.hue = 10;
        this.sat = 100;
        this.light = 50;
        this.incr = 50;
    }
    generate() {
        return RGB2hex(rgb2RGB(hsl2rgb(this.hue, this.sat, this.light)));
    }
    increment() {
        this.hue = (this.hue + this.incr) % 360;
    }
}
exports.ContrastPicker = ContrastPicker;


/***/ }),

/***/ 9400:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CssHighlighter = void 0;
const abstract_highlighter_1 = __webpack_require__(7228);
class CssHighlighter extends abstract_highlighter_1.AbstractHighlighter {
    constructor() {
        super();
        this.mactionName = 'mjx-maction';
    }
    highlightNode(node) {
        const info = {
            node: node,
            background: node.style.backgroundColor,
            foreground: node.style.color
        };
        const color = this.colorString();
        node.style.backgroundColor = color.background;
        node.style.color = color.foreground;
        return info;
    }
    unhighlightNode(info) {
        info.node.style.backgroundColor = info.background;
        info.node.style.color = info.foreground;
    }
}
exports.CssHighlighter = CssHighlighter;


/***/ }),

/***/ 9009:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.highlighterMapping_ = exports.addEvents = exports.highlighter = void 0;
const chtml_highlighter_1 = __webpack_require__(7567);
const color_picker_1 = __webpack_require__(1123);
const css_highlighter_1 = __webpack_require__(9400);
const html_highlighter_1 = __webpack_require__(7872);
const mml_css_highlighter_1 = __webpack_require__(3711);
const mml_highlighter_1 = __webpack_require__(4662);
const svg_highlighter_1 = __webpack_require__(3507);
const svg_v3_highlighter_1 = __webpack_require__(280);
function highlighter(back, fore, rendererInfo) {
    const colorPicker = new color_picker_1.ColorPicker(back, fore);
    const renderer = rendererInfo.renderer === 'NativeMML' && rendererInfo.browser === 'Safari'
        ? 'MML-CSS'
        : rendererInfo.renderer === 'SVG' && rendererInfo.browser === 'v3'
            ? 'SVG-V3'
            : rendererInfo.renderer;
    const highlighter = new (exports.highlighterMapping_[renderer] ||
        exports.highlighterMapping_['NativeMML'])();
    highlighter.setColor(colorPicker);
    return highlighter;
}
exports.highlighter = highlighter;
function addEvents(node, events, rendererInfo) {
    const highlight = exports.highlighterMapping_[rendererInfo.renderer];
    if (highlight) {
        new highlight().addEvents(node, events);
    }
}
exports.addEvents = addEvents;
exports.highlighterMapping_ = {
    SVG: svg_highlighter_1.SvgHighlighter,
    'SVG-V3': svg_v3_highlighter_1.SvgV3Highlighter,
    NativeMML: mml_highlighter_1.MmlHighlighter,
    'HTML-CSS': html_highlighter_1.HtmlHighlighter,
    'MML-CSS': mml_css_highlighter_1.MmlCssHighlighter,
    CommonHTML: css_highlighter_1.CssHighlighter,
    CHTML: chtml_highlighter_1.ChtmlHighlighter
};


/***/ }),

/***/ 7872:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.HtmlHighlighter = void 0;
const DomUtil = __webpack_require__(6671);
const abstract_highlighter_1 = __webpack_require__(7228);
class HtmlHighlighter extends abstract_highlighter_1.AbstractHighlighter {
    constructor() {
        super();
        this.mactionName = 'maction';
    }
    highlightNode(node) {
        const info = {
            node: node,
            foreground: node.style.color,
            position: node.style.position
        };
        const color = this.color.rgb();
        node.style.color = color.foreground;
        node.style.position = 'relative';
        const bbox = node.bbox;
        if (bbox && bbox.w) {
            const vpad = 0.05;
            const hpad = 0;
            const span = DomUtil.createElement('span');
            const left = parseFloat(node.style.paddingLeft || '0');
            span.style.backgroundColor = color.background;
            span.style.opacity = color.alphaback.toString();
            span.style.display = 'inline-block';
            span.style.height = bbox.h + bbox.d + 2 * vpad + 'em';
            span.style.verticalAlign = -bbox.d + 'em';
            span.style.marginTop = span.style.marginBottom = -vpad + 'em';
            span.style.width = bbox.w + 2 * hpad + 'em';
            span.style.marginLeft = left - hpad + 'em';
            span.style.marginRight = -bbox.w - hpad - left + 'em';
            node.parentNode.insertBefore(span, node);
            info.box = span;
        }
        return info;
    }
    unhighlightNode(info) {
        const node = info.node;
        node.style.color = info.foreground;
        node.style.position = info.position;
        if (info.box) {
            info.box.parentNode.removeChild(info.box);
        }
    }
}
exports.HtmlHighlighter = HtmlHighlighter;


/***/ }),

/***/ 3711:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MmlCssHighlighter = void 0;
const css_highlighter_1 = __webpack_require__(9400);
class MmlCssHighlighter extends css_highlighter_1.CssHighlighter {
    constructor() {
        super();
        this.mactionName = 'maction';
    }
    getMactionNodes(node) {
        return Array.from(node.getElementsByTagName(this.mactionName));
    }
    isMactionNode(node) {
        return node.tagName === this.mactionName;
    }
}
exports.MmlCssHighlighter = MmlCssHighlighter;


/***/ }),

/***/ 4662:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MmlHighlighter = void 0;
const abstract_highlighter_1 = __webpack_require__(7228);
class MmlHighlighter extends abstract_highlighter_1.AbstractHighlighter {
    constructor() {
        super();
        this.mactionName = 'maction';
    }
    highlightNode(node) {
        let style = node.getAttribute('style');
        style += ';background-color: ' + this.colorString().background;
        style += ';color: ' + this.colorString().foreground;
        node.setAttribute('style', style);
        return { node: node };
    }
    unhighlightNode(info) {
        let style = info.node.getAttribute('style');
        style = style.replace(';background-color: ' + this.colorString().background, '');
        style = style.replace(';color: ' + this.colorString().foreground, '');
        info.node.setAttribute('style', style);
    }
    colorString() {
        return this.color.rgba();
    }
    getMactionNodes(node) {
        return Array.from(node.getElementsByTagName(this.mactionName));
    }
    isMactionNode(node) {
        return node.tagName === this.mactionName;
    }
}
exports.MmlHighlighter = MmlHighlighter;


/***/ }),

/***/ 3507:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SvgHighlighter = void 0;
const DomUtil = __webpack_require__(6671);
const abstract_highlighter_1 = __webpack_require__(7228);
class SvgHighlighter extends abstract_highlighter_1.AbstractHighlighter {
    constructor() {
        super();
        this.mactionName = 'mjx-svg-maction';
    }
    highlightNode(node) {
        let info;
        if (this.isHighlighted(node)) {
            info = {
                node: node.previousSibling || node,
                background: node.style.backgroundColor,
                foreground: node.style.color
            };
            return info;
        }
        if (node.tagName === 'svg') {
            const info = {
                node: node,
                background: node.style.backgroundColor,
                foreground: node.style.color
            };
            node.style.backgroundColor = this.colorString().background;
            node.style.color = this.colorString().foreground;
            return info;
        }
        const rect = DomUtil.createElementNS('http://www.w3.org/2000/svg', 'rect');
        const padding = 40;
        let bbox;
        if (node.nodeName === 'use') {
            const g = DomUtil.createElementNS('http://www.w3.org/2000/svg', 'g');
            node.parentNode.insertBefore(g, node);
            g.appendChild(node);
            bbox = g.getBBox();
            g.parentNode.replaceChild(node, g);
        }
        else {
            bbox = node.getBBox();
        }
        rect.setAttribute('x', (bbox.x - padding).toString());
        rect.setAttribute('y', (bbox.y - padding).toString());
        rect.setAttribute('width', (bbox.width + 2 * padding).toString());
        rect.setAttribute('height', (bbox.height + 2 * padding).toString());
        const transform = node.getAttribute('transform');
        if (transform) {
            rect.setAttribute('transform', transform);
        }
        rect.setAttribute('fill', this.colorString().background);
        rect.setAttribute(abstract_highlighter_1.AbstractHighlighter.ATTR, 'true');
        node.parentNode.insertBefore(rect, node);
        info = { node: rect, foreground: node.getAttribute('fill') };
        node.setAttribute('fill', this.colorString().foreground);
        return info;
    }
    setHighlighted(node) {
        if (node.tagName === 'svg') {
            super.setHighlighted(node);
        }
    }
    unhighlightNode(info) {
        if ('background' in info) {
            info.node.style.backgroundColor = info.background;
            info.node.style.color = info.foreground;
            return;
        }
        info.foreground
            ? info.node.nextSibling.setAttribute('fill', info.foreground)
            : info.node.nextSibling.removeAttribute('fill');
        info.node.parentNode.removeChild(info.node);
    }
    isMactionNode(node) {
        let className = node.className || node.getAttribute('class');
        className =
            className.baseVal !== undefined
                ? className.baseVal
                : className;
        return className ? !!className.match(new RegExp(this.mactionName)) : false;
    }
}
exports.SvgHighlighter = SvgHighlighter;


/***/ }),

/***/ 280:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SvgV3Highlighter = void 0;
const DomUtil = __webpack_require__(6671);
const XpathUtil = __webpack_require__(5024);
const abstract_highlighter_1 = __webpack_require__(7228);
const color_picker_1 = __webpack_require__(1123);
const svg_highlighter_1 = __webpack_require__(3507);
class SvgV3Highlighter extends svg_highlighter_1.SvgHighlighter {
    constructor() {
        super();
        this.mactionName = 'maction';
    }
    highlightNode(node) {
        let info;
        if (this.isHighlighted(node)) {
            info = {
                node: node,
                background: this.colorString().background,
                foreground: this.colorString().foreground
            };
            return info;
        }
        if (node.tagName === 'svg' || node.tagName === 'MJX-CONTAINER') {
            info = {
                node: node,
                background: node.style.backgroundColor,
                foreground: node.style.color
            };
            node.style.backgroundColor = this.colorString().background;
            node.style.color = this.colorString().foreground;
            return info;
        }
        const rect = DomUtil.createElementNS('http://www.w3.org/2000/svg', 'rect');
        rect.setAttribute('sre-highlighter-added', 'true');
        const padding = 40;
        const bbox = node.getBBox();
        rect.setAttribute('x', (bbox.x - padding).toString());
        rect.setAttribute('y', (bbox.y - padding).toString());
        rect.setAttribute('width', (bbox.width + 2 * padding).toString());
        rect.setAttribute('height', (bbox.height + 2 * padding).toString());
        const transform = node.getAttribute('transform');
        if (transform) {
            rect.setAttribute('transform', transform);
        }
        rect.setAttribute('fill', this.colorString().background);
        node.setAttribute(abstract_highlighter_1.AbstractHighlighter.ATTR, 'true');
        node.parentNode.insertBefore(rect, node);
        info = { node: node, foreground: node.getAttribute('fill') };
        if (node.nodeName === 'rect') {
            const picker = new color_picker_1.ColorPicker({ alpha: 0, color: 'black' });
            node.setAttribute('fill', picker.rgba().foreground);
        }
        else {
            node.setAttribute('fill', this.colorString().foreground);
        }
        return info;
    }
    unhighlightNode(info) {
        const previous = info.node.previousSibling;
        if (previous && previous.hasAttribute('sre-highlighter-added')) {
            info.foreground
                ? info.node.setAttribute('fill', info.foreground)
                : info.node.removeAttribute('fill');
            info.node.parentNode.removeChild(previous);
            return;
        }
        info.node.style.backgroundColor = info.background;
        info.node.style.color = info.foreground;
    }
    isMactionNode(node) {
        return node.getAttribute('data-mml-node') === this.mactionName;
    }
    getMactionNodes(node) {
        return Array.from(XpathUtil.evalXPath(`.//*[@data-mml-node="${this.mactionName}"]`, node));
    }
}
exports.SvgV3Highlighter = SvgV3Highlighter;


/***/ }),

/***/ 1473:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.StaticTrieNode = exports.AbstractTrieNode = void 0;
const debugger_1 = __webpack_require__(1984);
const trie_node_1 = __webpack_require__(9259);
class AbstractTrieNode {
    constructor(constraint, test) {
        this.constraint = constraint;
        this.test = test;
        this.children_ = {};
        this.kind = trie_node_1.TrieNodeKind.ROOT;
    }
    getConstraint() {
        return this.constraint;
    }
    getKind() {
        return this.kind;
    }
    applyTest(object) {
        return this.test(object);
    }
    addChild(node) {
        const constraint = node.getConstraint();
        const child = this.children_[constraint];
        this.children_[constraint] = node;
        return child;
    }
    getChild(constraint) {
        return this.children_[constraint];
    }
    getChildren() {
        const children = [];
        for (const key in this.children_) {
            children.push(this.children_[key]);
        }
        return children;
    }
    findChildren(object) {
        const children = [];
        for (const key in this.children_) {
            const child = this.children_[key];
            if (child.applyTest(object)) {
                children.push(child);
            }
        }
        return children;
    }
    removeChild(constraint) {
        delete this.children_[constraint];
    }
    toString() {
        return this.constraint;
    }
}
exports.AbstractTrieNode = AbstractTrieNode;
class StaticTrieNode extends AbstractTrieNode {
    constructor(constraint, test) {
        super(constraint, test);
        this.rule_ = null;
        this.kind = trie_node_1.TrieNodeKind.STATIC;
    }
    getRule() {
        return this.rule_;
    }
    setRule(rule) {
        if (this.rule_) {
            debugger_1.Debugger.getInstance().output('Replacing rule ' + this.rule_ + ' with ' + rule);
        }
        this.rule_ = rule;
    }
    toString() {
        const rule = this.getRule();
        return rule
            ? this.constraint + '\n' + '==> ' + this.getRule().action
            : this.constraint;
    }
}
exports.StaticTrieNode = StaticTrieNode;


/***/ }),

/***/ 2803:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Trie = void 0;
const trie_node_1 = __webpack_require__(9259);
const trie_node_factory_1 = __webpack_require__(9146);
class Trie {
    constructor() {
        this.root = (0, trie_node_factory_1.getNode)(trie_node_1.TrieNodeKind.ROOT, '', null);
    }
    static collectRules_(root) {
        const rules = [];
        let explore = [root];
        while (explore.length) {
            const node = explore.shift();
            if (node.getKind() === trie_node_1.TrieNodeKind.QUERY ||
                node.getKind() === trie_node_1.TrieNodeKind.BOOLEAN) {
                const rule = node.getRule();
                if (rule) {
                    rules.unshift(rule);
                }
            }
            explore = explore.concat(node.getChildren());
        }
        return rules;
    }
    static printWithDepth_(node, depth, str) {
        const prefix = new Array(depth + 2).join(depth.toString()) + ': ';
        str += prefix + node.toString() + '\n';
        const children = node.getChildren();
        for (let i = 0, child; (child = children[i]); i++) {
            str = Trie.printWithDepth_(child, depth + 1, str);
        }
        return str;
    }
    static order_(node) {
        const children = node.getChildren();
        if (!children.length) {
            return 0;
        }
        const max = Math.max.apply(null, children.map(Trie.order_));
        return Math.max(children.length, max);
    }
    addRule(rule) {
        let node = this.root;
        const context = rule.context;
        const dynamicCstr = rule.dynamicCstr.getValues();
        for (let i = 0, l = dynamicCstr.length; i < l; i++) {
            node = this.addNode_(node, dynamicCstr[i], trie_node_1.TrieNodeKind.DYNAMIC, context);
        }
        node = this.addNode_(node, rule.precondition.query, trie_node_1.TrieNodeKind.QUERY, context);
        const booleans = rule.precondition.constraints;
        for (let i = 0, l = booleans.length; i < l; i++) {
            node = this.addNode_(node, booleans[i], trie_node_1.TrieNodeKind.BOOLEAN, context);
        }
        node.setRule(rule);
    }
    lookupRules(xml, dynamic) {
        let nodes = [this.root];
        const rules = [];
        while (dynamic.length) {
            const dynamicSet = dynamic.shift();
            const newNodes = [];
            while (nodes.length) {
                const node = nodes.shift();
                const children = node.getChildren();
                children.forEach((child) => {
                    if (child.getKind() !== trie_node_1.TrieNodeKind.DYNAMIC ||
                        dynamicSet.indexOf(child.getConstraint()) !== -1) {
                        newNodes.push(child);
                    }
                });
            }
            nodes = newNodes.slice();
        }
        while (nodes.length) {
            const node = nodes.shift();
            if (node.getRule) {
                const rule = node.getRule();
                if (rule) {
                    rules.push(rule);
                }
            }
            const children = node.findChildren(xml);
            nodes = nodes.concat(children);
        }
        return rules;
    }
    hasSubtrie(cstrs) {
        let subtrie = this.root;
        for (let i = 0, l = cstrs.length; i < l; i++) {
            const cstr = cstrs[i];
            subtrie = subtrie.getChild(cstr);
            if (!subtrie) {
                return false;
            }
        }
        return true;
    }
    toString() {
        return Trie.printWithDepth_(this.root, 0, '');
    }
    collectRules() {
        return Trie.collectRules_(this.root);
    }
    order() {
        return Trie.order_(this.root);
    }
    enumerate(opt_info) {
        return this.enumerate_(this.root, opt_info);
    }
    byConstraint(constraint) {
        let node = this.root;
        while (constraint.length && node) {
            const cstr = constraint.shift();
            node = node.getChild(cstr);
        }
        return node || null;
    }
    enumerate_(node, info) {
        info = info || {};
        const children = node.getChildren();
        for (let i = 0, child; (child = children[i]); i++) {
            if (child.kind !== trie_node_1.TrieNodeKind.DYNAMIC) {
                continue;
            }
            info[child.getConstraint()] = this.enumerate_(child, info[child.getConstraint()]);
        }
        return info;
    }
    addNode_(node, constraint, kind, context) {
        let nextNode = node.getChild(constraint);
        if (!nextNode) {
            nextNode = (0, trie_node_factory_1.getNode)(kind, constraint, context);
            node.addChild(nextNode);
        }
        return nextNode;
    }
}
exports.Trie = Trie;


/***/ }),

/***/ 9259:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TrieNodeKind = void 0;
var TrieNodeKind;
(function (TrieNodeKind) {
    TrieNodeKind["ROOT"] = "root";
    TrieNodeKind["DYNAMIC"] = "dynamic";
    TrieNodeKind["QUERY"] = "query";
    TrieNodeKind["BOOLEAN"] = "boolean";
    TrieNodeKind["STATIC"] = "static";
})(TrieNodeKind = exports.TrieNodeKind || (exports.TrieNodeKind = {}));


/***/ }),

/***/ 9146:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BooleanTrieNode = exports.QueryTrieNode = exports.constraintTest_ = exports.DynamicTrieNode = exports.RootTrieNode = exports.getNode = void 0;
const DomUtil = __webpack_require__(6671);
const XpathUtil = __webpack_require__(5024);
const grammar_1 = __webpack_require__(1058);
const MathCompoundStore = __webpack_require__(4161);
const abstract_trie_node_1 = __webpack_require__(1473);
const abstract_trie_node_2 = __webpack_require__(1473);
const trie_node_1 = __webpack_require__(9259);
function getNode(kind, constraint, context) {
    switch (kind) {
        case trie_node_1.TrieNodeKind.ROOT:
            return new RootTrieNode();
        case trie_node_1.TrieNodeKind.DYNAMIC:
            return new DynamicTrieNode(constraint);
        case trie_node_1.TrieNodeKind.QUERY:
            return new QueryTrieNode(constraint, context);
        case trie_node_1.TrieNodeKind.BOOLEAN:
            return new BooleanTrieNode(constraint, context);
        default:
            return null;
    }
}
exports.getNode = getNode;
class RootTrieNode extends abstract_trie_node_1.AbstractTrieNode {
    constructor() {
        super('', () => true);
        this.kind = trie_node_1.TrieNodeKind.ROOT;
    }
}
exports.RootTrieNode = RootTrieNode;
class DynamicTrieNode extends abstract_trie_node_1.AbstractTrieNode {
    constructor(constraint) {
        super(constraint, (axis) => axis === constraint);
        this.kind = trie_node_1.TrieNodeKind.DYNAMIC;
    }
}
exports.DynamicTrieNode = DynamicTrieNode;
const comparator = {
    '=': (x, y) => x === y,
    '!=': (x, y) => x !== y,
    '<': (x, y) => x < y,
    '>': (x, y) => x > y,
    '<=': (x, y) => x <= y,
    '>=': (x, y) => x >= y
};
function constraintTest_(constraint) {
    if (constraint.match(/^self::\*$/)) {
        return (_node) => true;
    }
    if (constraint.match(/^self::\w+$/)) {
        const tag = constraint.slice(6).toUpperCase();
        return (node) => node.tagName && DomUtil.tagName(node) === tag;
    }
    if (constraint.match(/^self::\w+:\w+$/)) {
        const inter = constraint.split(':');
        const namespace = XpathUtil.resolveNameSpace(inter[2]);
        if (!namespace) {
            return null;
        }
        const tag = inter[3].toUpperCase();
        return (node) => node.localName &&
            node.localName.toUpperCase() === tag &&
            node.namespaceURI === namespace;
    }
    if (constraint.match(/^@\w+$/)) {
        const attr = constraint.slice(1);
        return (node) => node.hasAttribute && node.hasAttribute(attr);
    }
    if (constraint.match(/^@\w+="[\w\d ]+"$/)) {
        const split = constraint.split('=');
        const attr = split[0].slice(1);
        const value = split[1].slice(1, -1);
        return (node) => node.hasAttribute &&
            node.hasAttribute(attr) &&
            node.getAttribute(attr) === value;
    }
    if (constraint.match(/^@\w+!="[\w\d ]+"$/)) {
        const split = constraint.split('!=');
        const attr = split[0].slice(1);
        const value = split[1].slice(1, -1);
        return (node) => !node.hasAttribute ||
            !node.hasAttribute(attr) ||
            node.getAttribute(attr) !== value;
    }
    if (constraint.match(/^contains\(\s*@grammar\s*,\s*"[\w\d ]+"\s*\)$/)) {
        const split = constraint.split('"');
        const value = split[1];
        return (_node) => !!grammar_1.Grammar.getInstance().getParameter(value);
    }
    if (constraint.match(/^not\(\s*contains\(\s*@grammar\s*,\s*"[\w\d ]+"\s*\)\s*\)$/)) {
        const split = constraint.split('"');
        const value = split[1];
        return (_node) => !grammar_1.Grammar.getInstance().getParameter(value);
    }
    if (constraint.match(/^name\(\.\.\/\.\.\)="\w+"$/)) {
        const split = constraint.split('"');
        const tag = split[1].toUpperCase();
        return (node) => {
            var _a, _b;
            return ((_b = (_a = node.parentNode) === null || _a === void 0 ? void 0 : _a.parentNode) === null || _b === void 0 ? void 0 : _b.tagName) &&
                DomUtil.tagName(node.parentNode.parentNode) === tag;
        };
    }
    if (constraint.match(/^count\(preceding-sibling::\*\)=\d+$/)) {
        const split = constraint.split('=');
        const num = parseInt(split[1], 10);
        return (node) => { var _a; return ((_a = node.parentNode) === null || _a === void 0 ? void 0 : _a.childNodes[num]) === node; };
    }
    if (constraint.match(/^.+\[@category!?=".+"\]$/)) {
        let [, query, equality, category] = constraint.match(/^(.+)\[@category(!?=)"(.+)"\]$/);
        const unit = category.match(/^unit:(.+)$/);
        let add = '';
        if (unit) {
            category = unit[1];
            add = ':unit';
        }
        return (node) => {
            const xpath = XpathUtil.evalXPath(query, node)[0];
            if (xpath) {
                const result = MathCompoundStore.lookupCategory(xpath.textContent + add);
                return equality === '=' ? result === category : result !== category;
            }
            return false;
        };
    }
    if (constraint.match(/^string-length\(.+\)\W+\d+/)) {
        const [, select, comp, count] = constraint.match(/^string-length\((.+)\)(\W+)(\d+)/);
        const func = comparator[comp] || comparator['='];
        const numb = parseInt(count, 10);
        return (node) => {
            const xpath = XpathUtil.evalXPath(select, node)[0];
            if (!xpath) {
                return false;
            }
            return func(Array.from(xpath.textContent).length, numb);
        };
    }
    return null;
}
exports.constraintTest_ = constraintTest_;
class QueryTrieNode extends abstract_trie_node_2.StaticTrieNode {
    constructor(constraint, context) {
        super(constraint, constraintTest_(constraint));
        this.context = context;
        this.kind = trie_node_1.TrieNodeKind.QUERY;
    }
    applyTest(object) {
        return this.test
            ? this.test(object)
            : this.context.applyQuery(object, this.constraint) === object;
    }
}
exports.QueryTrieNode = QueryTrieNode;
class BooleanTrieNode extends abstract_trie_node_2.StaticTrieNode {
    constructor(constraint, context) {
        super(constraint, constraintTest_(constraint));
        this.context = context;
        this.kind = trie_node_1.TrieNodeKind.BOOLEAN;
    }
    applyTest(object) {
        return this.test
            ? this.test(object)
            : this.context.applyConstraint(object, this.constraint);
    }
}
exports.BooleanTrieNode = BooleanTrieNode;


/***/ }),

/***/ 2371:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.completeLocale = exports.getLocale = exports.setLocale = exports.locales = void 0;
const engine_1 = __webpack_require__(4886);
const variables_1 = __webpack_require__(4513);
const grammar_1 = __webpack_require__(1058);
const locale_ca_1 = __webpack_require__(8597);
const locale_da_1 = __webpack_require__(9883);
const locale_de_1 = __webpack_require__(2523);
const locale_en_1 = __webpack_require__(3938);
const locale_es_1 = __webpack_require__(9139);
const locale_fr_1 = __webpack_require__(1547);
const locale_hi_1 = __webpack_require__(346);
const locale_it_1 = __webpack_require__(13);
const locale_nb_1 = __webpack_require__(6238);
const locale_nemeth_1 = __webpack_require__(2913);
const locale_nn_1 = __webpack_require__(3305);
const locale_sv_1 = __webpack_require__(9770);
const locale_1 = __webpack_require__(4524);
exports.locales = {
    ca: locale_ca_1.ca,
    da: locale_da_1.da,
    de: locale_de_1.de,
    en: locale_en_1.en,
    es: locale_es_1.es,
    fr: locale_fr_1.fr,
    hi: locale_hi_1.hi,
    it: locale_it_1.it,
    nb: locale_nb_1.nb,
    nn: locale_nn_1.nn,
    sv: locale_sv_1.sv,
    nemeth: locale_nemeth_1.nemeth
};
function setLocale() {
    const msgs = getLocale();
    setSubiso(msgs);
    if (msgs) {
        for (const key of Object.getOwnPropertyNames(msgs)) {
            locale_1.LOCALE[key] = msgs[key];
        }
        for (const [key, func] of Object.entries(msgs.CORRECTIONS)) {
            grammar_1.Grammar.getInstance().setCorrection(key, func);
        }
    }
}
exports.setLocale = setLocale;
function setSubiso(msg) {
    const subiso = engine_1.default.getInstance().subiso;
    if (msg.SUBISO.all.indexOf(subiso) === -1) {
        engine_1.default.getInstance().subiso = msg.SUBISO.default;
    }
    msg.SUBISO.current = engine_1.default.getInstance().subiso;
}
function getLocale() {
    const locale = variables_1.Variables.ensureLocale(engine_1.default.getInstance().locale, engine_1.default.getInstance().defaultLocale);
    engine_1.default.getInstance().locale = locale;
    return exports.locales[locale]();
}
exports.getLocale = getLocale;
function completeLocale(json) {
    const locale = exports.locales[json.locale];
    if (!locale) {
        console.error('Locale ' + json.locale + ' does not exist!');
        return;
    }
    const kind = json.kind.toUpperCase();
    const messages = json.messages;
    if (!messages)
        return;
    const loc = locale();
    for (const [key, value] of Object.entries(messages)) {
        loc[kind][key] = value;
    }
}
exports.completeLocale = completeLocale;


/***/ }),

/***/ 4524:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.createLocale = exports.LOCALE = void 0;
const messages_1 = __webpack_require__(4277);
exports.LOCALE = createLocale();
function createLocale() {
    return {
        FUNCTIONS: (0, messages_1.FUNCTIONS)(),
        MESSAGES: (0, messages_1.MESSAGES)(),
        ALPHABETS: (0, messages_1.ALPHABETS)(),
        NUMBERS: (0, messages_1.NUMBERS)(),
        COMBINERS: {},
        CORRECTIONS: {},
        SUBISO: (0, messages_1.SUBISO)()
    };
}
exports.createLocale = createLocale;


/***/ }),

/***/ 3319:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.localeFontCombiner = exports.extractString = exports.localEnclose = exports.localRole = exports.localFont = exports.combinePostfixIndex = exports.nestingToString = void 0;
const locale_1 = __webpack_require__(4524);
const transformers_1 = __webpack_require__(9385);
function nestingToString(count) {
    switch (count) {
        case 1:
            return locale_1.LOCALE.MESSAGES.MS.ONCE || '';
        case 2:
            return locale_1.LOCALE.MESSAGES.MS.TWICE;
        default:
            return count.toString();
    }
}
exports.nestingToString = nestingToString;
function combinePostfixIndex(postfix, index) {
    return postfix === locale_1.LOCALE.MESSAGES.MS.ROOTINDEX ||
        postfix === locale_1.LOCALE.MESSAGES.MS.INDEX
        ? postfix
        : postfix + ' ' + index;
}
exports.combinePostfixIndex = combinePostfixIndex;
function localFont(font) {
    return extractString(locale_1.LOCALE.MESSAGES.font[font], font);
}
exports.localFont = localFont;
function localRole(role) {
    return extractString(locale_1.LOCALE.MESSAGES.role[role], role);
}
exports.localRole = localRole;
function localEnclose(enclose) {
    return extractString(locale_1.LOCALE.MESSAGES.enclose[enclose], enclose);
}
exports.localEnclose = localEnclose;
function extractString(combiner, fallback) {
    if (combiner === undefined) {
        return fallback;
    }
    return typeof combiner === 'string' ? combiner : combiner[0];
}
exports.extractString = extractString;
function localeFontCombiner(font) {
    return typeof font === 'string'
        ? { font: font, combiner: locale_1.LOCALE.ALPHABETS.combiner }
        : {
            font: font[0],
            combiner: locale_1.LOCALE.COMBINERS[font[1]] ||
                transformers_1.Combiners[font[1]] ||
                locale_1.LOCALE.ALPHABETS.combiner
        };
}
exports.localeFontCombiner = localeFontCombiner;


/***/ }),

/***/ 8597:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ca = void 0;
const locale_1 = __webpack_require__(4524);
const locale_util_1 = __webpack_require__(3319);
const numbers_ca_1 = __webpack_require__(165);
const transformers_1 = __webpack_require__(9385);
const sansserifCombiner = function (letter, font, cap) {
    letter = 'sans serif ' + (cap ? cap + ' ' + letter : letter);
    return font ? letter + ' ' + font : letter;
};
let locale = null;
function ca() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.ca = ca;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_ca_1.default;
    loc.COMBINERS['sansserif'] = sansserifCombiner;
    loc.FUNCTIONS.fracNestDepth = (_node) => false;
    (loc.FUNCTIONS.combineRootIndex = locale_util_1.combinePostfixIndex),
        (loc.FUNCTIONS.combineNestedRadical = (a, _b, c) => a + c);
    loc.FUNCTIONS.fontRegexp = (font) => RegExp('^' + font + ' ');
    (loc.FUNCTIONS.plural = (unit) => {
        if (/.*os$/.test(unit)) {
            return unit + 'sos';
        }
        if (/.*s$/.test(unit)) {
            return unit + 'os';
        }
        if (/.*ga$/.test(unit)) {
            return unit.slice(0, -2) + 'gues';
        }
        if (/.*ça$/.test(unit)) {
            return unit.slice(0, -2) + 'ces';
        }
        if (/.*ca$/.test(unit)) {
            return unit.slice(0, -2) + 'ques';
        }
        if (/.*ja$/.test(unit)) {
            return unit.slice(0, -2) + 'ges';
        }
        if (/.*qua$/.test(unit)) {
            return unit.slice(0, -3) + 'qües';
        }
        if (/.*a$/.test(unit)) {
            return unit.slice(0, -1) + 'es';
        }
        if (/.*(e|i)$/.test(unit)) {
            return unit + 'ns';
        }
        if (/.*í$/.test(unit)) {
            return unit.slice(0, -1) + 'ins';
        }
        return unit + 's';
    }),
        (loc.FUNCTIONS.si = (prefix, unit) => {
            if (unit.match(/^metre/)) {
                prefix = prefix
                    .replace(/a$/, 'à')
                    .replace(/o$/, 'ò')
                    .replace(/i$/, 'í');
            }
            return prefix + unit;
        });
    loc.ALPHABETS.combiner = transformers_1.Combiners.prefixCombiner;
    return loc;
}


/***/ }),

/***/ 9883:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.da = void 0;
const locale_1 = __webpack_require__(4524);
const locale_util_1 = __webpack_require__(3319);
const numbers_da_1 = __webpack_require__(5571);
const tr = __webpack_require__(9385);
let locale = null;
function da() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.da = da;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_da_1.default;
    loc.FUNCTIONS.radicalNestDepth = locale_util_1.nestingToString;
    loc.FUNCTIONS.fontRegexp = (font) => {
        return font === loc.ALPHABETS.capPrefix['default']
            ? RegExp('^' + font + ' ')
            : RegExp(' ' + font + '$');
    };
    loc.ALPHABETS.combiner = tr.Combiners.postfixCombiner;
    loc.ALPHABETS.digitTrans.default = numbers_da_1.default.numberToWords;
    return loc;
}


/***/ }),

/***/ 2523:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.de = void 0;
const grammar_1 = __webpack_require__(1058);
const locale_util_1 = __webpack_require__(3319);
const locale_1 = __webpack_require__(4524);
const numbers_de_1 = __webpack_require__(757);
const germanPrefixCombiner = function (letter, font, cap) {
    if (cap === 's') {
        font = font
            .split(' ')
            .map(function (x) {
            return x.replace(/s$/, '');
        })
            .join(' ');
        cap = '';
    }
    letter = cap ? cap + ' ' + letter : letter;
    return font ? font + ' ' + letter : letter;
};
const germanPostfixCombiner = function (letter, font, cap) {
    letter = !cap || cap === 's' ? letter : cap + ' ' + letter;
    return font ? letter + ' ' + font : letter;
};
let locale = null;
function de() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.de = de;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_de_1.default;
    loc.COMBINERS['germanPostfix'] = germanPostfixCombiner;
    loc.ALPHABETS.combiner = germanPrefixCombiner;
    loc.FUNCTIONS.radicalNestDepth = (x) => {
        return x > 1 ? loc.NUMBERS.numberToWords(x) + 'fach' : '';
    };
    loc.FUNCTIONS.combineRootIndex = (postfix, index) => {
        const root = index ? index + 'wurzel' : '';
        return postfix.replace('Wurzel', root);
    };
    loc.FUNCTIONS.combineNestedRadical = (a, b, c) => {
        a = c.match(/exponent$/) ? a + 'r' : a;
        const count = (b ? b + ' ' : '') + a;
        return c.match(/ /) ? c.replace(/ /, ' ' + count + ' ') : count + ' ' + c;
    };
    loc.FUNCTIONS.fontRegexp = function (font) {
        font = font
            .split(' ')
            .map(function (x) {
            return x.replace(/s$/, '(|s)');
        })
            .join(' ');
        return new RegExp('((^' + font + ' )|( ' + font + '$))');
    };
    loc.CORRECTIONS.correctOne = (num) => num.replace(/^eins$/, 'ein');
    loc.CORRECTIONS.localFontNumber = (font) => {
        const realFont = (0, locale_util_1.localFont)(font);
        return realFont
            .split(' ')
            .map(function (x) {
            return x.replace(/s$/, '');
        })
            .join(' ');
    };
    loc.CORRECTIONS.lowercase = (name) => name.toLowerCase();
    loc.CORRECTIONS.article = (name) => {
        const decl = grammar_1.Grammar.getInstance().getParameter('case');
        const plural = grammar_1.Grammar.getInstance().getParameter('plural');
        if (decl === 'dative') {
            return { der: 'dem', die: plural ? 'den' : 'der', das: 'dem' }[name];
        }
        return name;
    };
    loc.CORRECTIONS.masculine = (name) => {
        const decl = grammar_1.Grammar.getInstance().getParameter('case');
        if (decl === 'dative') {
            return name + 'n';
        }
        return name;
    };
    return loc;
}


/***/ }),

/***/ 3938:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.en = void 0;
const grammar_1 = __webpack_require__(1058);
const locale_1 = __webpack_require__(4524);
const locale_util_1 = __webpack_require__(3319);
const numbers_en_1 = __webpack_require__(166);
const tr = __webpack_require__(9385);
let locale = null;
function en() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.en = en;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_en_1.default;
    loc.FUNCTIONS.radicalNestDepth = locale_util_1.nestingToString;
    loc.FUNCTIONS.plural = (unit) => {
        return /.*s$/.test(unit) ? unit : unit + 's';
    };
    loc.ALPHABETS.combiner = tr.Combiners.prefixCombiner;
    loc.ALPHABETS.digitTrans.default = numbers_en_1.default.numberToWords;
    loc.CORRECTIONS.article = (name) => {
        return grammar_1.Grammar.getInstance().getParameter('noArticle') ? '' : name;
    };
    return loc;
}


/***/ }),

/***/ 9139:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.es = void 0;
const locale_1 = __webpack_require__(4524);
const locale_util_1 = __webpack_require__(3319);
const numbers_es_1 = __webpack_require__(6154);
const transformers_1 = __webpack_require__(9385);
const sansserifCombiner = function (letter, font, cap) {
    letter = 'sans serif ' + (cap ? cap + ' ' + letter : letter);
    return font ? letter + ' ' + font : letter;
};
let locale = null;
function es() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.es = es;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_es_1.default;
    loc.COMBINERS['sansserif'] = sansserifCombiner;
    loc.FUNCTIONS.fracNestDepth = (_node) => false;
    (loc.FUNCTIONS.combineRootIndex = locale_util_1.combinePostfixIndex),
        (loc.FUNCTIONS.combineNestedRadical = (a, _b, c) => a + c);
    loc.FUNCTIONS.fontRegexp = (font) => RegExp('^' + font + ' ');
    (loc.FUNCTIONS.plural = (unit) => {
        if (/.*(a|e|i|o|u)$/.test(unit)) {
            return unit + 's';
        }
        if (/.*z$/.test(unit)) {
            return unit.slice(0, -1) + 'ces';
        }
        if (/.*c$/.test(unit)) {
            return unit.slice(0, -1) + 'ques';
        }
        if (/.*g$/.test(unit)) {
            return unit + 'ues';
        }
        if (/.*\u00f3n$/.test(unit)) {
            return unit.slice(0, -2) + 'ones';
        }
        return unit + 'es';
    }),
        (loc.FUNCTIONS.si = (prefix, unit) => {
            if (unit.match(/^metro/)) {
                prefix = prefix
                    .replace(/a$/, 'á')
                    .replace(/o$/, 'ó')
                    .replace(/i$/, 'í');
            }
            return prefix + unit;
        });
    loc.ALPHABETS.combiner = transformers_1.Combiners.prefixCombiner;
    return loc;
}


/***/ }),

/***/ 1547:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.fr = void 0;
const grammar_1 = __webpack_require__(1058);
const locale_1 = __webpack_require__(4524);
const locale_util_1 = __webpack_require__(3319);
const numbers_fr_1 = __webpack_require__(4394);
const transformers_1 = __webpack_require__(9385);
let locale = null;
function fr() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.fr = fr;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_fr_1.default;
    loc.FUNCTIONS.radicalNestDepth = locale_util_1.nestingToString;
    loc.FUNCTIONS.combineRootIndex = locale_util_1.combinePostfixIndex;
    loc.FUNCTIONS.combineNestedFraction = (a, b, c) => c.replace(/ $/g, '') + b + a;
    loc.FUNCTIONS.combineNestedRadical = (a, _b, c) => c + ' ' + a;
    loc.FUNCTIONS.fontRegexp = (font) => RegExp(' (en |)' + font + '$');
    loc.FUNCTIONS.plural = (unit) => {
        return /.*s$/.test(unit) ? unit : unit + 's';
    };
    loc.CORRECTIONS.article = (name) => {
        return grammar_1.Grammar.getInstance().getParameter('noArticle') ? '' : name;
    };
    loc.ALPHABETS.combiner = transformers_1.Combiners.romanceCombiner;
    loc.SUBISO = {
        default: 'fr',
        current: 'fr',
        all: ['fr', 'be', 'ch']
    };
    return loc;
}


/***/ }),

/***/ 346:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.hi = void 0;
const locale_1 = __webpack_require__(4524);
const numbers_hi_1 = __webpack_require__(1779);
const transformers_1 = __webpack_require__(9385);
const locale_util_1 = __webpack_require__(3319);
let locale = null;
function hi() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.hi = hi;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_hi_1.default;
    loc.ALPHABETS.combiner = transformers_1.Combiners.prefixCombiner;
    loc.FUNCTIONS.radicalNestDepth = locale_util_1.nestingToString;
    return loc;
}


/***/ }),

/***/ 13:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.it = void 0;
const locale_util_1 = __webpack_require__(3319);
const locale_1 = __webpack_require__(4524);
const numbers_it_1 = __webpack_require__(5952);
const transformers_1 = __webpack_require__(9385);
const italianPostfixCombiner = function (letter, font, cap) {
    if (letter.match(/^[a-zA-Z]$/)) {
        font = font.replace('cerchiato', 'cerchiata');
    }
    letter = cap ? letter + ' ' + cap : letter;
    return font ? letter + ' ' + font : letter;
};
let locale = null;
function it() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.it = it;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_it_1.default;
    loc.COMBINERS['italianPostfix'] = italianPostfixCombiner;
    loc.FUNCTIONS.radicalNestDepth = locale_util_1.nestingToString;
    loc.FUNCTIONS.combineRootIndex = locale_util_1.combinePostfixIndex;
    loc.FUNCTIONS.combineNestedFraction = (a, b, c) => c.replace(/ $/g, '') + b + a;
    loc.FUNCTIONS.combineNestedRadical = (a, _b, c) => c + ' ' + a;
    loc.FUNCTIONS.fontRegexp = (font) => RegExp(' (en |)' + font + '$');
    loc.ALPHABETS.combiner = transformers_1.Combiners.romanceCombiner;
    return loc;
}


/***/ }),

/***/ 6238:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.nb = void 0;
const locale_1 = __webpack_require__(4524);
const locale_util_1 = __webpack_require__(3319);
const numbers_nn_1 = __webpack_require__(984);
const tr = __webpack_require__(9385);
let locale = null;
function nb() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.nb = nb;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_nn_1.default;
    loc.ALPHABETS.combiner = tr.Combiners.prefixCombiner;
    loc.ALPHABETS.digitTrans.default = numbers_nn_1.default.numberToWords;
    loc.FUNCTIONS.radicalNestDepth = locale_util_1.nestingToString;
    return loc;
}


/***/ }),

/***/ 2913:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.nemeth = void 0;
const locale_1 = __webpack_require__(4524);
const numbers_nemeth_1 = __webpack_require__(3669);
const transformers_1 = __webpack_require__(9385);
const simpleEnglish = function (letter) {
    return letter.match(RegExp('^' + locale.ALPHABETS.languagePrefix.english))
        ? letter.slice(1)
        : letter;
};
const postfixCombiner = function (letter, font, _number) {
    letter = simpleEnglish(letter);
    return font ? letter + font : letter;
};
const germanCombiner = function (letter, font, _cap) {
    return font + simpleEnglish(letter);
};
const embellishCombiner = function (letter, font, num) {
    letter = simpleEnglish(letter);
    return font + (num ? num : '') + letter + '⠻';
};
const doubleEmbellishCombiner = function (letter, font, num) {
    letter = simpleEnglish(letter);
    return font + (num ? num : '') + letter + '⠻⠻';
};
const parensCombiner = function (letter, font, _number) {
    letter = simpleEnglish(letter);
    return font + letter + '⠾';
};
let locale = null;
function nemeth() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.nemeth = nemeth;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_nemeth_1.default;
    loc.COMBINERS = {
        postfixCombiner: postfixCombiner,
        germanCombiner: germanCombiner,
        embellishCombiner: embellishCombiner,
        doubleEmbellishCombiner: doubleEmbellishCombiner,
        parensCombiner: parensCombiner
    };
    loc.FUNCTIONS.fracNestDepth = (_node) => false;
    loc.FUNCTIONS.fontRegexp = (font) => RegExp('^' + font);
    (loc.FUNCTIONS.si = transformers_1.identityTransformer),
        (loc.ALPHABETS.combiner = (letter, font, num) => {
            return font ? font + num + letter : simpleEnglish(letter);
        });
    loc.ALPHABETS.digitTrans = { default: numbers_nemeth_1.default.numberToWords };
    return loc;
}


/***/ }),

/***/ 3305:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.nn = void 0;
const locale_1 = __webpack_require__(4524);
const locale_util_1 = __webpack_require__(3319);
const numbers_nn_1 = __webpack_require__(984);
const tr = __webpack_require__(9385);
let locale = null;
function nn() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.nn = nn;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_nn_1.default;
    loc.ALPHABETS.combiner = tr.Combiners.prefixCombiner;
    loc.ALPHABETS.digitTrans.default = numbers_nn_1.default.numberToWords;
    loc.FUNCTIONS.radicalNestDepth = locale_util_1.nestingToString;
    loc.SUBISO = {
        default: '',
        current: '',
        all: ['', 'alt']
    };
    return loc;
}


/***/ }),

/***/ 9770:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.sv = void 0;
const locale_1 = __webpack_require__(4524);
const locale_util_1 = __webpack_require__(3319);
const numbers_sv_1 = __webpack_require__(6416);
const tr = __webpack_require__(9385);
let locale = null;
function sv() {
    if (!locale) {
        locale = create();
    }
    return locale;
}
exports.sv = sv;
function create() {
    const loc = (0, locale_1.createLocale)();
    loc.NUMBERS = numbers_sv_1.default;
    loc.FUNCTIONS.radicalNestDepth = locale_util_1.nestingToString;
    loc.FUNCTIONS.fontRegexp = function (font) {
        return new RegExp('((^' + font + ' )|( ' + font + '$))');
    };
    loc.ALPHABETS.combiner = tr.Combiners.prefixCombiner;
    loc.ALPHABETS.digitTrans.default = numbers_sv_1.default.numberToWords;
    loc.CORRECTIONS.correctOne = (num) => num.replace(/^ett$/, 'en');
    return loc;
}


/***/ }),

/***/ 4277:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SUBISO = exports.FUNCTIONS = exports.ALPHABETS = exports.NUMBERS = exports.MESSAGES = void 0;
const tr = __webpack_require__(9385);
function MESSAGES() {
    return {
        MS: {},
        MSroots: {},
        font: {},
        embellish: {},
        role: {},
        enclose: {},
        navigate: {},
        regexp: {},
        unitTimes: ''
    };
}
exports.MESSAGES = MESSAGES;
function NUMBERS() {
    return {
        zero: 'zero',
        ones: [],
        tens: [],
        large: [],
        special: {},
        wordOrdinal: tr.identityTransformer,
        numericOrdinal: tr.identityTransformer,
        numberToWords: tr.identityTransformer,
        numberToOrdinal: tr.pluralCase,
        vulgarSep: ' ',
        numSep: ' '
    };
}
exports.NUMBERS = NUMBERS;
function ALPHABETS() {
    return {
        latinSmall: [],
        latinCap: [],
        greekSmall: [],
        greekCap: [],
        capPrefix: { default: '' },
        smallPrefix: { default: '' },
        digitPrefix: { default: '' },
        languagePrefix: {},
        digitTrans: {
            default: tr.identityTransformer,
            mathspeak: tr.identityTransformer,
            clearspeak: tr.identityTransformer
        },
        letterTrans: { default: tr.identityTransformer },
        combiner: (letter, _font, _cap) => {
            return letter;
        }
    };
}
exports.ALPHABETS = ALPHABETS;
function FUNCTIONS() {
    return {
        fracNestDepth: (n) => tr.vulgarFractionSmall(n, 10, 100),
        radicalNestDepth: (_count) => '',
        combineRootIndex: function (postfix, _index) {
            return postfix;
        },
        combineNestedFraction: tr.Combiners.identityCombiner,
        combineNestedRadical: tr.Combiners.identityCombiner,
        fontRegexp: function (font) {
            return new RegExp('^' + font.split(/ |-/).join('( |-)') + '( |-)');
        },
        si: tr.siCombiner,
        plural: tr.identityTransformer
    };
}
exports.FUNCTIONS = FUNCTIONS;
function SUBISO() {
    return {
        default: '',
        current: '',
        all: []
    };
}
exports.SUBISO = SUBISO;


/***/ }),

/***/ 165:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const grammar_1 = __webpack_require__(1058);
const messages_1 = __webpack_require__(4277);
function tensToWords_(num) {
    const n = num % 100;
    if (n < 20) {
        return NUMBERS.ones[n];
    }
    const ten = Math.floor(n / 10);
    const tens = NUMBERS.tens[ten];
    const ones = NUMBERS.ones[n % 10];
    return tens && ones ? tens + (ten === 2 ? '-i-' : '-') + ones : tens || ones;
}
function hundredsToWords_(num) {
    const n = num % 1000;
    const hundred = Math.floor(n / 100);
    const hundreds = hundred
        ? hundred === 1
            ? 'cent'
            : NUMBERS.ones[hundred] + '-cents'
        : '';
    const tens = tensToWords_(n % 100);
    return hundreds && tens ? hundreds + NUMBERS.numSep + tens : hundreds || tens;
}
function numberToWords(num) {
    if (num === 0) {
        return NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % (pos > 1 ? 1000000 : 1000);
        if (hundreds) {
            let large = NUMBERS.large[pos];
            if (!pos) {
                str = hundredsToWords_(hundreds);
            }
            else if (pos === 1) {
                str =
                    (hundreds === 1 ? '' : hundredsToWords_(hundreds) + NUMBERS.numSep) +
                        large +
                        (str ? NUMBERS.numSep + str : '');
            }
            else {
                const thousands = numberToWords(hundreds);
                large = hundreds === 1 ? large : large.replace(/\u00f3$/, 'ons');
                str =
                    thousands +
                        NUMBERS.numSep +
                        large +
                        (str ? NUMBERS.numSep + str : '');
            }
        }
        num = Math.floor(num / (pos > 1 ? 1000000 : 1000));
        pos++;
    }
    return str;
}
function numberToOrdinal(num, _plural) {
    if (num > 1999) {
        return numericOrdinal(num);
    }
    if (num <= 10) {
        return NUMBERS.special.onesOrdinals[num - 1];
    }
    const result = numberToWords(num);
    if (result.match(/mil$/)) {
        return result.replace(/mil$/, 'mil·lèsima');
    }
    if (result.match(/u$/)) {
        return result.replace(/u$/, 'vena');
    }
    if (result.match(/a$/)) {
        return result.replace(/a$/, 'ena');
    }
    return result + (result.match(/e$/) ? 'na' : 'ena');
}
function numericOrdinal(num) {
    const gender = grammar_1.Grammar.getInstance().getParameter('gender');
    return num.toString() + (gender === 'f' ? 'a' : 'n');
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;


/***/ }),

/***/ 5571:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const messages_1 = __webpack_require__(4277);
function onePrefix_(num, mill = false) {
    return num === NUMBERS.ones[1] ? (mill ? 'et' : 'en') : num;
}
function hundredsToWords_(num, ordinal = false) {
    let n = num % 1000;
    let str = '';
    let ones = NUMBERS.ones[Math.floor(n / 100)];
    str += ones ? onePrefix_(ones, true) + ' hundrede' : '';
    n = n % 100;
    if (n) {
        str += str ? ' og ' : '';
        ones = ordinal ? NUMBERS.special.smallOrdinals[n] : NUMBERS.ones[n];
        if (ones) {
            str += ones;
        }
        else {
            const tens = ordinal
                ? NUMBERS.special.tensOrdinals[Math.floor(n / 10)]
                : NUMBERS.tens[Math.floor(n / 10)];
            ones = NUMBERS.ones[n % 10];
            str += ones ? onePrefix_(ones) + 'og' + tens : tens;
        }
    }
    return str;
}
function numberToWords(num, ordinal = false) {
    if (num === 0) {
        return NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % 1000;
        if (hundreds) {
            const hund = hundredsToWords_(hundreds, ordinal && !pos);
            if (pos) {
                const large = NUMBERS.large[pos];
                const plural = hundreds > 1 ? 'er' : '';
                str =
                    onePrefix_(hund, pos <= 1) +
                        ' ' +
                        large +
                        plural +
                        (str ? ' og ' : '') +
                        str;
            }
            else {
                str = onePrefix_(hund) + str;
            }
        }
        num = Math.floor(num / 1000);
        pos++;
    }
    return str;
}
function numberToOrdinal(num, plural) {
    if (num === 1) {
        return plural ? 'hel' : 'hele';
    }
    if (num === 2) {
        return plural ? 'halv' : 'halve';
    }
    return wordOrdinal(num) + (plural ? 'dele' : 'del');
}
function wordOrdinal(num) {
    if (num % 100) {
        return numberToWords(num, true);
    }
    const ordinal = numberToWords(num);
    return ordinal.match(/e$/) ? ordinal : ordinal + 'e';
}
function numericOrdinal(num) {
    return num.toString() + '.';
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.wordOrdinal = wordOrdinal;
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;


/***/ }),

/***/ 757:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const messages_1 = __webpack_require__(4277);
function onePrefix_(num, mill = false) {
    return num === NUMBERS.ones[1] ? (mill ? 'eine' : 'ein') : num;
}
function hundredsToWords_(num) {
    let n = num % 1000;
    let str = '';
    let ones = NUMBERS.ones[Math.floor(n / 100)];
    str += ones ? onePrefix_(ones) + 'hundert' : '';
    n = n % 100;
    if (n) {
        str += str ? NUMBERS.numSep : '';
        ones = NUMBERS.ones[n];
        if (ones) {
            str += ones;
        }
        else {
            const tens = NUMBERS.tens[Math.floor(n / 10)];
            ones = NUMBERS.ones[n % 10];
            str += ones ? onePrefix_(ones) + 'und' + tens : tens;
        }
    }
    return str;
}
function numberToWords(num) {
    if (num === 0) {
        return NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % 1000;
        if (hundreds) {
            const hund = hundredsToWords_(num % 1000);
            if (pos) {
                const large = NUMBERS.large[pos];
                const plural = pos > 1 && hundreds > 1 ? (large.match(/e$/) ? 'n' : 'en') : '';
                str = onePrefix_(hund, pos > 1) + large + plural + str;
            }
            else {
                str = onePrefix_(hund, pos > 1) + str;
            }
        }
        num = Math.floor(num / 1000);
        pos++;
    }
    return str.replace(/ein$/, 'eins');
}
function numberToOrdinal(num, plural) {
    if (num === 1) {
        return 'eintel';
    }
    if (num === 2) {
        return plural ? 'halbe' : 'halb';
    }
    return wordOrdinal(num) + 'l';
}
function wordOrdinal(num) {
    if (num === 1) {
        return 'erste';
    }
    if (num === 3) {
        return 'dritte';
    }
    if (num === 7) {
        return 'siebte';
    }
    if (num === 8) {
        return 'achte';
    }
    const ordinal = numberToWords(num);
    return ordinal + (num < 19 ? 'te' : 'ste');
}
function numericOrdinal(num) {
    return num.toString() + '.';
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.wordOrdinal = wordOrdinal;
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;


/***/ }),

/***/ 166:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const messages_1 = __webpack_require__(4277);
function hundredsToWords_(num) {
    let n = num % 1000;
    let str = '';
    str += NUMBERS.ones[Math.floor(n / 100)]
        ? NUMBERS.ones[Math.floor(n / 100)] + NUMBERS.numSep + 'hundred'
        : '';
    n = n % 100;
    if (n) {
        str += str ? NUMBERS.numSep : '';
        str +=
            NUMBERS.ones[n] ||
                NUMBERS.tens[Math.floor(n / 10)] +
                    (n % 10 ? NUMBERS.numSep + NUMBERS.ones[n % 10] : '');
    }
    return str;
}
function numberToWords(num) {
    if (num === 0) {
        return NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % 1000;
        if (hundreds) {
            str =
                hundredsToWords_(num % 1000) +
                    (pos ? '-' + NUMBERS.large[pos] + '-' : '') +
                    str;
        }
        num = Math.floor(num / 1000);
        pos++;
    }
    return str.replace(/-$/, '');
}
function numberToOrdinal(num, plural) {
    if (num === 1) {
        return plural ? 'oneths' : 'oneth';
    }
    if (num === 2) {
        return plural ? 'halves' : 'half';
    }
    const ordinal = wordOrdinal(num);
    return plural ? ordinal + 's' : ordinal;
}
function wordOrdinal(num) {
    let ordinal = numberToWords(num);
    if (ordinal.match(/one$/)) {
        ordinal = ordinal.slice(0, -3) + 'first';
    }
    else if (ordinal.match(/two$/)) {
        ordinal = ordinal.slice(0, -3) + 'second';
    }
    else if (ordinal.match(/three$/)) {
        ordinal = ordinal.slice(0, -5) + 'third';
    }
    else if (ordinal.match(/five$/)) {
        ordinal = ordinal.slice(0, -4) + 'fifth';
    }
    else if (ordinal.match(/eight$/)) {
        ordinal = ordinal.slice(0, -5) + 'eighth';
    }
    else if (ordinal.match(/nine$/)) {
        ordinal = ordinal.slice(0, -4) + 'ninth';
    }
    else if (ordinal.match(/twelve$/)) {
        ordinal = ordinal.slice(0, -6) + 'twelfth';
    }
    else if (ordinal.match(/ty$/)) {
        ordinal = ordinal.slice(0, -2) + 'tieth';
    }
    else {
        ordinal = ordinal + 'th';
    }
    return ordinal;
}
function numericOrdinal(num) {
    const tens = num % 100;
    const numStr = num.toString();
    if (tens > 10 && tens < 20) {
        return numStr + 'th';
    }
    switch (num % 10) {
        case 1:
            return numStr + 'st';
        case 2:
            return numStr + 'nd';
        case 3:
            return numStr + 'rd';
        default:
            return numStr + 'th';
    }
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.wordOrdinal = wordOrdinal;
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;


/***/ }),

/***/ 6154:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const grammar_1 = __webpack_require__(1058);
const messages_1 = __webpack_require__(4277);
function tensToWords_(num) {
    const n = num % 100;
    if (n < 30) {
        return NUMBERS.ones[n];
    }
    const tens = NUMBERS.tens[Math.floor(n / 10)];
    const ones = NUMBERS.ones[n % 10];
    return tens && ones ? tens + ' y ' + ones : tens || ones;
}
function hundredsToWords_(num) {
    const n = num % 1000;
    const hundred = Math.floor(n / 100);
    const hundreds = NUMBERS.special.hundreds[hundred];
    const tens = tensToWords_(n % 100);
    if (hundred === 1) {
        if (!tens) {
            return hundreds;
        }
        return hundreds + 'to' + ' ' + tens;
    }
    return hundreds && tens ? hundreds + ' ' + tens : hundreds || tens;
}
function numberToWords(num) {
    if (num === 0) {
        return NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % 1000;
        if (hundreds) {
            let large = NUMBERS.large[pos];
            const huns = hundredsToWords_(hundreds);
            if (!pos) {
                str = huns;
            }
            else if (hundreds === 1) {
                large = large.match('/^mil( |$)/') ? large : 'un ' + large;
                str = large + (str ? ' ' + str : '');
            }
            else {
                large = large.replace(/\u00f3n$/, 'ones');
                str = hundredsToWords_(hundreds) + ' ' + large + (str ? ' ' + str : '');
            }
        }
        num = Math.floor(num / 1000);
        pos++;
    }
    return str;
}
function numberToOrdinal(num, _plural) {
    if (num > 1999) {
        return num.toString() + 'a';
    }
    if (num <= 12) {
        return NUMBERS.special.onesOrdinals[num - 1];
    }
    const result = [];
    if (num >= 1000) {
        num = num - 1000;
        result.push('milésima');
    }
    if (!num) {
        return result.join(' ');
    }
    let pos = 0;
    pos = Math.floor(num / 100);
    if (pos > 0) {
        result.push(NUMBERS.special.hundredsOrdinals[pos - 1]);
        num = num % 100;
    }
    if (num <= 12) {
        result.push(NUMBERS.special.onesOrdinals[num - 1]);
    }
    else {
        pos = Math.floor(num / 10);
        if (pos > 0) {
            result.push(NUMBERS.special.tensOrdinals[pos - 1]);
            num = num % 10;
        }
        if (num > 0) {
            result.push(NUMBERS.special.onesOrdinals[num - 1]);
        }
    }
    return result.join(' ');
}
function numericOrdinal(num) {
    const gender = grammar_1.Grammar.getInstance().getParameter('gender');
    return num.toString() + (gender === 'f' ? 'a' : 'o');
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;


/***/ }),

/***/ 4394:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const engine_1 = __webpack_require__(4886);
const grammar_1 = __webpack_require__(1058);
const messages_1 = __webpack_require__(4277);
function hundredsToWords_(num) {
    let n = num % 1000;
    let str = '';
    str += NUMBERS.ones[Math.floor(n / 100)]
        ? NUMBERS.ones[Math.floor(n / 100)] + '-cent'
        : '';
    n = n % 100;
    if (n) {
        str += str ? '-' : '';
        let ones = NUMBERS.ones[n];
        if (ones) {
            str += ones;
        }
        else {
            const tens = NUMBERS.tens[Math.floor(n / 10)];
            if (tens.match(/-dix$/)) {
                ones = NUMBERS.ones[(n % 10) + 10];
                str += tens.replace(/-dix$/, '') + '-' + ones;
            }
            else {
                str += tens + (n % 10 ? '-' + NUMBERS.ones[n % 10] : '');
            }
        }
    }
    const match = str.match(/s-\w+$/);
    return match
        ? str.replace(/s-\w+$/, match[0].slice(1))
        : str.replace(/-un$/, '-et-un');
}
function numberToWords(num) {
    if (num === 0) {
        return NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    if (NUMBERS.special['tens-' + engine_1.default.getInstance().subiso]) {
        NUMBERS.tens = NUMBERS.special['tens-' + engine_1.default.getInstance().subiso];
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % 1000;
        if (hundreds) {
            let large = NUMBERS.large[pos];
            const huns = hundredsToWords_(hundreds);
            if (large && large.match(/^mille /)) {
                const rest = large.replace(/^mille /, '');
                if (str.match(RegExp(rest))) {
                    str = huns + (pos ? '-mille-' : '') + str;
                }
                else if (str.match(RegExp(rest.replace(/s$/, '')))) {
                    str =
                        huns +
                            (pos ? '-mille-' : '') +
                            str.replace(rest.replace(/s$/, ''), rest);
                }
                else {
                    str = huns + (pos ? '-' + large + '-' : '') + str;
                }
            }
            else {
                large = hundreds === 1 && large ? large.replace(/s$/, '') : large;
                str = huns + (pos ? '-' + large + '-' : '') + str;
            }
        }
        num = Math.floor(num / 1000);
        pos++;
    }
    return str.replace(/-$/, '');
}
const SMALL_ORDINAL = {
    1: 'unième',
    2: 'demi',
    3: 'tiers',
    4: 'quart'
};
function numberToOrdinal(num, plural) {
    const ordinal = SMALL_ORDINAL[num] || wordOrdinal(num);
    return num === 3 ? ordinal : plural ? ordinal + 's' : ordinal;
}
function wordOrdinal(num) {
    if (num === 1) {
        return 'première';
    }
    let ordinal = numberToWords(num);
    if (ordinal.match(/^neuf$/)) {
        ordinal = ordinal.slice(0, -1) + 'v';
    }
    else if (ordinal.match(/cinq$/)) {
        ordinal = ordinal + 'u';
    }
    else if (ordinal.match(/trois$/)) {
        ordinal = ordinal + '';
    }
    else if (ordinal.match(/e$/) || ordinal.match(/s$/)) {
        ordinal = ordinal.slice(0, -1);
    }
    ordinal = ordinal + 'ième';
    return ordinal;
}
function numericOrdinal(num) {
    const gender = grammar_1.Grammar.getInstance().getParameter('gender');
    return num === 1
        ? num.toString() + (gender === 'm' ? 'er' : 're')
        : num.toString() + 'e';
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.wordOrdinal = wordOrdinal;
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;


/***/ }),

/***/ 1779:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const grammar_1 = __webpack_require__(1058);
const messages_1 = __webpack_require__(4277);
function hundredsToWords_(num) {
    let n = num % 1000;
    let str = '';
    str += NUMBERS.ones[Math.floor(n / 100)]
        ? NUMBERS.ones[Math.floor(n / 100)] +
            NUMBERS.numSep +
            NUMBERS.special.hundred
        : '';
    n = n % 100;
    if (n) {
        str += str ? NUMBERS.numSep : '';
        str += NUMBERS.ones[n];
    }
    return str;
}
function numberToWords(num) {
    if (num === 0) {
        return NUMBERS.zero;
    }
    if (num >= Math.pow(10, 32)) {
        return num.toString();
    }
    let pos = 0;
    let str = '';
    const hundreds = num % 1000;
    const hundredsWords = hundredsToWords_(hundreds);
    num = Math.floor(num / 1000);
    if (!num) {
        return hundredsWords;
    }
    while (num > 0) {
        const thousands = num % 100;
        if (thousands) {
            str =
                NUMBERS.ones[thousands] +
                    NUMBERS.numSep +
                    NUMBERS.large[pos] +
                    (str ? NUMBERS.numSep + str : '');
        }
        num = Math.floor(num / 100);
        pos++;
    }
    return hundredsWords ? str + NUMBERS.numSep + hundredsWords : str;
}
function numberToOrdinal(num, _plural) {
    if (num <= 10) {
        return NUMBERS.special.smallDenominators[num];
    }
    return wordOrdinal(num) + ' अंश';
}
function wordOrdinal(num) {
    const gender = grammar_1.Grammar.getInstance().getParameter('gender');
    if (num <= 0) {
        return num.toString();
    }
    if (num < 10) {
        return gender === 'f'
            ? NUMBERS.special.ordinalsFeminine[num]
            : NUMBERS.special.ordinalsMasculine[num];
    }
    const ordinal = numberToWords(num);
    return ordinal + (gender === 'f' ? 'वीं' : 'वाँ');
}
function numericOrdinal(num) {
    const gender = grammar_1.Grammar.getInstance().getParameter('gender');
    if (num > 0 && num < 10) {
        return gender === 'f'
            ? NUMBERS.special.simpleSmallOrdinalsFeminine[num]
            : NUMBERS.special.simpleSmallOrdinalsMasculine[num];
    }
    const ordinal = num
        .toString()
        .split('')
        .map(function (x) {
        const num = parseInt(x, 10);
        return isNaN(num) ? '' : NUMBERS.special.simpleNumbers[num];
    })
        .join('');
    return ordinal + (gender === 'f' ? 'वीं' : 'वाँ');
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.wordOrdinal = wordOrdinal;
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;


/***/ }),

/***/ 5952:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const grammar_1 = __webpack_require__(1058);
const messages_1 = __webpack_require__(4277);
function hundredsToWords_(num) {
    let n = num % 1000;
    let str = '';
    str += NUMBERS.ones[Math.floor(n / 100)]
        ? NUMBERS.ones[Math.floor(n / 100)] + NUMBERS.numSep + 'cento'
        : '';
    n = n % 100;
    if (n) {
        str += str ? NUMBERS.numSep : '';
        const ones = NUMBERS.ones[n];
        if (ones) {
            str += ones;
        }
        else {
            let tens = NUMBERS.tens[Math.floor(n / 10)];
            const rest = n % 10;
            if (rest === 1 || rest === 8) {
                tens = tens.slice(0, -1);
            }
            str += tens;
            str += rest ? NUMBERS.numSep + NUMBERS.ones[n % 10] : '';
        }
    }
    return str;
}
function numberToWords(num) {
    if (num === 0) {
        return NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    if (num === 1 && grammar_1.Grammar.getInstance().getParameter('fraction')) {
        return 'un';
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % 1000;
        if (hundreds) {
            str =
                hundredsToWords_(num % 1000) +
                    (pos ? '-' + NUMBERS.large[pos] + '-' : '') +
                    str;
        }
        num = Math.floor(num / 1000);
        pos++;
    }
    return str.replace(/-$/, '');
}
function numberToOrdinal(num, plural) {
    if (num === 2) {
        return plural ? 'mezzi' : 'mezzo';
    }
    const ordinal = wordOrdinal(num);
    if (!plural) {
        return ordinal;
    }
    const gender = ordinal.match(/o$/) ? 'i' : 'e';
    return ordinal.slice(0, -1) + gender;
}
function wordOrdinal(num) {
    const gender = grammar_1.Grammar.getInstance().getParameter('gender');
    const postfix = gender === 'm' ? 'o' : 'a';
    let ordinal = NUMBERS.special.onesOrdinals[num];
    if (ordinal) {
        return ordinal.slice(0, -1) + postfix;
    }
    ordinal = numberToWords(num);
    return ordinal.slice(0, -1) + 'esim' + postfix;
}
function numericOrdinal(num) {
    const gender = grammar_1.Grammar.getInstance().getParameter('gender');
    return num.toString() + (gender === 'm' ? 'o' : 'a');
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.wordOrdinal = wordOrdinal;
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;


/***/ }),

/***/ 3669:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const messages_1 = __webpack_require__(4277);
function numberToWords(num) {
    const digits = num.toString().split('');
    return digits
        .map(function (digit) {
        return NUMBERS.ones[parseInt(digit, 10)];
    })
        .join('');
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToWords;
exports["default"] = NUMBERS;


/***/ }),

/***/ 984:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const engine_1 = __webpack_require__(4886);
const messages_1 = __webpack_require__(4277);
function hundredsToWordsRo_(num, ordinal = false) {
    let n = num % 1000;
    let str = '';
    const count = Math.floor(n / 100);
    const ones = NUMBERS.ones[count];
    str += ones ? (count === 1 ? '' : ones) + 'hundre' : '';
    n = n % 100;
    if (n) {
        str += str ? 'og' : '';
        if (ordinal) {
            const ord = NUMBERS.special.smallOrdinals[n];
            if (ord) {
                return str + ord;
            }
            if (n % 10) {
                return (str +
                    NUMBERS.tens[Math.floor(n / 10)] +
                    NUMBERS.special.smallOrdinals[n % 10]);
            }
        }
        str +=
            NUMBERS.ones[n] ||
                NUMBERS.tens[Math.floor(n / 10)] + (n % 10 ? NUMBERS.ones[n % 10] : '');
    }
    return ordinal ? replaceOrdinal(str) : str;
}
function numberToWordsRo(num, ordinal = false) {
    if (num === 0) {
        return ordinal ? NUMBERS.special.smallOrdinals[0] : NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % 1000;
        if (hundreds) {
            const hund = hundredsToWordsRo_(num % 1000, pos ? false : ordinal);
            if (!pos && ordinal) {
                ordinal = !ordinal;
            }
            str =
                hund +
                    (pos
                        ? ' ' +
                            (NUMBERS.large[pos] + (pos > 1 && hundreds > 1 ? 'er' : '')) +
                            (str ? ' ' : '')
                        : '') +
                    str;
        }
        num = Math.floor(num / 1000);
        pos++;
    }
    return ordinal ? str + (str.match(/tusen$/) ? 'de' : 'te') : str;
}
function numberToOrdinal(num, _plural) {
    return wordOrdinal(num);
}
function replaceOrdinal(str) {
    const letOne = NUMBERS.special.endOrdinal[0];
    if (letOne === 'a' && str.match(/en$/)) {
        return str.slice(0, -2) + NUMBERS.special.endOrdinal;
    }
    if (str.match(/(d|n)$/) || str.match(/hundre$/)) {
        return str + 'de';
    }
    if (str.match(/i$/)) {
        return str + NUMBERS.special.endOrdinal;
    }
    if (letOne === 'a' && str.match(/e$/)) {
        return str.slice(0, -1) + NUMBERS.special.endOrdinal;
    }
    if (str.match(/e$/)) {
        return str + 'nde';
    }
    return str + 'nde';
}
function wordOrdinal(num) {
    const ordinal = numberToWords(num, true);
    return ordinal;
}
function numericOrdinal(num) {
    return num.toString() + '.';
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.wordOrdinal = wordOrdinal;
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;
function onePrefix_(num, thd = false) {
    const numOne = NUMBERS.ones[1];
    return num === numOne ? (num === 'ein' ? 'eitt ' : thd ? 'et' : 'ett') : num;
}
function hundredsToWordsGe_(num, ordinal = false) {
    let n = num % 1000;
    let str = '';
    let ones = NUMBERS.ones[Math.floor(n / 100)];
    str += ones ? onePrefix_(ones) + 'hundre' : '';
    n = n % 100;
    if (n) {
        str += str ? 'og' : '';
        if (ordinal) {
            const ord = NUMBERS.special.smallOrdinals[n];
            if (ord) {
                return (str += ord);
            }
        }
        ones = NUMBERS.ones[n];
        if (ones) {
            str += ones;
        }
        else {
            const tens = NUMBERS.tens[Math.floor(n / 10)];
            ones = NUMBERS.ones[n % 10];
            str += ones ? ones + 'og' + tens : tens;
        }
    }
    return ordinal ? replaceOrdinal(str) : str;
}
function numberToWordsGe(num, ordinal = false) {
    if (num === 0) {
        return ordinal ? NUMBERS.special.smallOrdinals[0] : NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % 1000;
        if (hundreds) {
            const hund = hundredsToWordsGe_(num % 1000, pos ? false : ordinal);
            if (!pos && ordinal) {
                ordinal = !ordinal;
            }
            str =
                (pos === 1 ? onePrefix_(hund, true) : hund) +
                    (pos > 1 ? NUMBERS.numSep : '') +
                    (pos
                        ?
                            NUMBERS.large[pos] + (pos > 1 && hundreds > 1 ? 'er' : '')
                        : '') +
                    (pos > 1 && str ? NUMBERS.numSep : '') +
                    str;
        }
        num = Math.floor(num / 1000);
        pos++;
    }
    return ordinal ? str + (str.match(/tusen$/) ? 'de' : 'te') : str;
}
function numberToWords(num, ordinal = false) {
    const word = engine_1.default.getInstance().subiso === 'alt'
        ? numberToWordsGe(num, ordinal)
        : numberToWordsRo(num, ordinal);
    return word;
}


/***/ }),

/***/ 6416:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const messages_1 = __webpack_require__(4277);
function hundredsToWords_(num) {
    let n = num % 1000;
    let str = '';
    const hundreds = Math.floor(n / 100);
    str += NUMBERS.ones[hundreds]
        ? (hundreds === 1 ? '' : NUMBERS.ones[hundreds] + NUMBERS.numSep) + 'hundra'
        : '';
    n = n % 100;
    if (n) {
        str += str ? NUMBERS.numSep : '';
        str +=
            NUMBERS.ones[n] ||
                NUMBERS.tens[Math.floor(n / 10)] +
                    (n % 10 ? NUMBERS.numSep + NUMBERS.ones[n % 10] : '');
    }
    return str;
}
function numberToWords(num, ordinal = false) {
    if (num === 0) {
        return NUMBERS.zero;
    }
    if (num >= Math.pow(10, 36)) {
        return num.toString();
    }
    let pos = 0;
    let str = '';
    while (num > 0) {
        const hundreds = num % 1000;
        if (hundreds) {
            const large = NUMBERS.large[pos];
            const plural = hundreds > 1 && pos > 1 && !ordinal ? 'er' : '';
            str =
                (pos === 1 && hundreds === 1
                    ? ''
                    : (pos > 1 && hundreds === 1 ? 'en' : hundredsToWords_(num % 1000)) +
                        (pos > 1 ? ' ' : '')) +
                    (pos ? large + plural + (pos > 1 ? ' ' : '') : '') +
                    str;
        }
        num = Math.floor(num / 1000);
        pos++;
    }
    return str.replace(/ $/, '');
}
function numberToOrdinal(num, plural) {
    if (num === 1) {
        return plural ? 'hel' : 'hel';
    }
    if (num === 2) {
        return plural ? 'halva' : 'halv';
    }
    let ordinal = wordOrdinal(num);
    ordinal = ordinal.match(/de$/) ? ordinal.replace(/de$/, '') : ordinal;
    return ordinal + (plural ? 'delar' : 'del');
}
function wordOrdinal(num) {
    let ordinal = numberToWords(num, true);
    if (ordinal.match(/^noll$/)) {
        ordinal = 'nollte';
    }
    else if (ordinal.match(/ett$/)) {
        ordinal = ordinal.replace(/ett$/, 'första');
    }
    else if (ordinal.match(/två$/)) {
        ordinal = ordinal.replace(/två$/, 'andra');
    }
    else if (ordinal.match(/tre$/)) {
        ordinal = ordinal.replace(/tre$/, 'tredje');
    }
    else if (ordinal.match(/fyra$/)) {
        ordinal = ordinal.replace(/fyra$/, 'fjärde');
    }
    else if (ordinal.match(/fem$/)) {
        ordinal = ordinal.replace(/fem$/, 'femte');
    }
    else if (ordinal.match(/sex$/)) {
        ordinal = ordinal.replace(/sex$/, 'sjätte');
    }
    else if (ordinal.match(/sju$/)) {
        ordinal = ordinal.replace(/sju$/, 'sjunde');
    }
    else if (ordinal.match(/åtta$/)) {
        ordinal = ordinal.replace(/åtta$/, 'åttonde');
    }
    else if (ordinal.match(/nio$/)) {
        ordinal = ordinal.replace(/nio$/, 'nionde');
    }
    else if (ordinal.match(/tio$/)) {
        ordinal = ordinal.replace(/tio$/, 'tionde');
    }
    else if (ordinal.match(/elva$/)) {
        ordinal = ordinal.replace(/elva$/, 'elfte');
    }
    else if (ordinal.match(/tolv$/)) {
        ordinal = ordinal.replace(/tolv$/, 'tolfte');
    }
    else if (ordinal.match(/tusen$/)) {
        ordinal = ordinal.replace(/tusen$/, 'tusonde');
    }
    else if (ordinal.match(/jard$/) || ordinal.match(/jon$/)) {
        ordinal = ordinal + 'te';
    }
    else {
        ordinal = ordinal + 'de';
    }
    return ordinal;
}
function numericOrdinal(num) {
    const str = num.toString();
    if (str.match(/11$|12$/)) {
        return str + ':e';
    }
    return str + (str.match(/1$|2$/) ? ':a' : ':e');
}
const NUMBERS = (0, messages_1.NUMBERS)();
NUMBERS.wordOrdinal = wordOrdinal;
NUMBERS.numericOrdinal = numericOrdinal;
NUMBERS.numberToWords = numberToWords;
NUMBERS.numberToOrdinal = numberToOrdinal;
exports["default"] = NUMBERS;


/***/ }),

/***/ 9385:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.vulgarFractionSmall = exports.convertVulgarFraction = exports.Combiners = exports.siCombiner = exports.identityTransformer = exports.pluralCase = void 0;
function pluralCase(num, _plural) {
    return num.toString();
}
exports.pluralCase = pluralCase;
function identityTransformer(input) {
    return input.toString();
}
exports.identityTransformer = identityTransformer;
function siCombiner(prefix, unit) {
    return prefix + unit.toLowerCase();
}
exports.siCombiner = siCombiner;
exports.Combiners = {};
exports.Combiners.identityCombiner = function (a, b, c) {
    return a + b + c;
};
exports.Combiners.prefixCombiner = function (letter, font, cap) {
    letter = cap ? cap + ' ' + letter : letter;
    return font ? font + ' ' + letter : letter;
};
exports.Combiners.postfixCombiner = function (letter, font, cap) {
    letter = cap ? cap + ' ' + letter : letter;
    return font ? letter + ' ' + font : letter;
};
exports.Combiners.romanceCombiner = function (letter, font, cap) {
    letter = cap ? letter + ' ' + cap : letter;
    return font ? letter + ' ' + font : letter;
};
function convertVulgarFraction(node, over = '') {
    if (!node.childNodes ||
        !node.childNodes[0] ||
        !node.childNodes[0].childNodes ||
        node.childNodes[0].childNodes.length < 2 ||
        node.childNodes[0].childNodes[0].tagName !==
            "number" ||
        node.childNodes[0].childNodes[0].getAttribute('role') !==
            "integer" ||
        node.childNodes[0].childNodes[1].tagName !==
            "number" ||
        node.childNodes[0].childNodes[1].getAttribute('role') !==
            "integer") {
        return { convertible: false, content: node.textContent };
    }
    const denStr = node.childNodes[0].childNodes[1].textContent;
    const enumStr = node.childNodes[0].childNodes[0].textContent;
    const denominator = Number(denStr);
    const enumerator = Number(enumStr);
    if (isNaN(denominator) || isNaN(enumerator)) {
        return {
            convertible: false,
            content: `${enumStr} ${over} ${denStr}`
        };
    }
    return {
        convertible: true,
        enumerator: enumerator,
        denominator: denominator
    };
}
exports.convertVulgarFraction = convertVulgarFraction;
function vulgarFractionSmall(node, enumer, denom) {
    const conversion = convertVulgarFraction(node);
    if (conversion.convertible) {
        const enumerator = conversion.enumerator;
        const denominator = conversion.denominator;
        return (enumerator > 0 &&
            enumerator < enumer &&
            denominator > 0 &&
            denominator < denom);
    }
    return false;
}
exports.vulgarFractionSmall = vulgarFractionSmall;


/***/ }),

/***/ 1970:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Condition = exports.BaseRuleStore = void 0;
const auditory_description_1 = __webpack_require__(4148);
const dynamic_cstr_1 = __webpack_require__(8310);
const speech_rule_1 = __webpack_require__(7039);
const speech_rule_context_1 = __webpack_require__(443);
class BaseRuleStore {
    constructor() {
        this.context = new speech_rule_context_1.SpeechRuleContext();
        this.parseOrder = dynamic_cstr_1.DynamicCstr.DEFAULT_ORDER;
        this.parser = new dynamic_cstr_1.DynamicCstrParser(this.parseOrder);
        this.locale = dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.LOCALE];
        this.modality = dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.MODALITY];
        this.domain = '';
        this.initialized = false;
        this.inherits = null;
        this.kind = 'standard';
        this.customTranscriptions = {};
        this.preconditions = new Map();
        this.speechRules_ = [];
        this.rank = 0;
        this.parseMethods = {
            Rule: this.defineRule,
            Generator: this.generateRules,
            Action: this.defineAction,
            Precondition: this.definePrecondition,
            Ignore: this.ignoreRules
        };
    }
    static compareStaticConstraints_(cstr1, cstr2) {
        if (cstr1.length !== cstr2.length) {
            return false;
        }
        for (let i = 0, cstr; (cstr = cstr1[i]); i++) {
            if (cstr2.indexOf(cstr) === -1) {
                return false;
            }
        }
        return true;
    }
    static comparePreconditions_(rule1, rule2) {
        const prec1 = rule1.precondition;
        const prec2 = rule2.precondition;
        if (prec1.query !== prec2.query) {
            return false;
        }
        return BaseRuleStore.compareStaticConstraints_(prec1.constraints, prec2.constraints);
    }
    defineRule(name, dynamic, action, prec, ...args) {
        const postc = this.parseAction(action);
        const fullPrec = this.parsePrecondition(prec, args);
        const dynamicCstr = this.parseCstr(dynamic);
        if (!(postc && fullPrec && dynamicCstr)) {
            console.error(`Rule Error: ${prec}, (${dynamic}): ${action}`);
            return null;
        }
        const rule = new speech_rule_1.SpeechRule(name, dynamicCstr, fullPrec, postc);
        rule.precondition.rank = this.rank++;
        this.addRule(rule);
        return rule;
    }
    addRule(rule) {
        rule.context = this.context;
        this.speechRules_.unshift(rule);
    }
    deleteRule(rule) {
        const index = this.speechRules_.indexOf(rule);
        if (index !== -1) {
            this.speechRules_.splice(index, 1);
        }
    }
    findRule(pred) {
        for (let i = 0, rule; (rule = this.speechRules_[i]); i++) {
            if (pred(rule)) {
                return rule;
            }
        }
        return null;
    }
    findAllRules(pred) {
        return this.speechRules_.filter(pred);
    }
    evaluateDefault(node) {
        const rest = node.textContent.slice(0);
        if (rest.match(/^\s+$/)) {
            return this.evaluateWhitespace(rest);
        }
        return this.evaluateString(rest);
    }
    evaluateWhitespace(_str) {
        return [];
    }
    evaluateCustom(str) {
        const trans = this.customTranscriptions[str];
        return trans !== undefined
            ? auditory_description_1.AuditoryDescription.create({ text: trans }, { adjust: true, translate: false })
            : null;
    }
    evaluateCharacter(str) {
        return (this.evaluateCustom(str) ||
            auditory_description_1.AuditoryDescription.create({ text: str }, { adjust: true, translate: true }));
    }
    removeDuplicates(rule) {
        for (let i = this.speechRules_.length - 1, oldRule; (oldRule = this.speechRules_[i]); i--) {
            if (oldRule !== rule &&
                rule.dynamicCstr.equal(oldRule.dynamicCstr) &&
                BaseRuleStore.comparePreconditions_(oldRule, rule)) {
                this.speechRules_.splice(i, 1);
            }
        }
    }
    getSpeechRules() {
        return this.speechRules_;
    }
    setSpeechRules(rules) {
        this.speechRules_ = rules;
    }
    getPreconditions() {
        return this.preconditions;
    }
    parseCstr(cstr) {
        try {
            return this.parser.parse(this.locale +
                '.' +
                this.modality +
                (this.domain ? '.' + this.domain : '') +
                '.' +
                cstr);
        }
        catch (err) {
            if (err.name === 'RuleError') {
                console.error('Rule Error ', `Illegal Dynamic Constraint: ${cstr}.`, err.message);
                return null;
            }
            else {
                throw err;
            }
        }
    }
    parsePrecondition(query, rest) {
        try {
            const queryCstr = this.parsePrecondition_(query);
            query = queryCstr[0];
            let restCstr = queryCstr.slice(1);
            for (const cstr of rest) {
                restCstr = restCstr.concat(this.parsePrecondition_(cstr));
            }
            return new speech_rule_1.Precondition(query, ...restCstr);
        }
        catch (err) {
            if (err.name === 'RuleError') {
                console.error('Rule Error ', `Illegal preconditions: ${query}, ${rest}.`, err.message);
                return null;
            }
            else {
                throw err;
            }
        }
    }
    parseAction(action) {
        try {
            return speech_rule_1.Action.fromString(action);
        }
        catch (err) {
            if (err.name === 'RuleError') {
                console.error('Rule Error ', `Illegal action: ${action}.`, err.message);
                return null;
            }
            else {
                throw err;
            }
        }
    }
    parse(ruleSet) {
        this.modality = ruleSet.modality || this.modality;
        this.locale = ruleSet.locale || this.locale;
        this.domain = ruleSet.domain || this.domain;
        this.context.parse(ruleSet.functions || []);
        if (ruleSet.kind !== 'actions') {
            this.kind = ruleSet.kind || this.kind;
            this.inheritRules();
        }
        this.parseRules(ruleSet.rules || []);
    }
    parseRules(rules) {
        for (let i = 0, rule; (rule = rules[i]); i++) {
            const type = rule[0];
            const method = this.parseMethods[type];
            if (type && method) {
                method.apply(this, rule.slice(1));
            }
        }
    }
    generateRules(generator) {
        const method = this.context.customGenerators.lookup(generator);
        if (method) {
            method(this);
        }
    }
    defineAction(name, action) {
        let postc;
        try {
            postc = speech_rule_1.Action.fromString(action);
        }
        catch (err) {
            if (err.name === 'RuleError') {
                console.error('Action Error ', action, err.message);
                return;
            }
            else {
                throw err;
            }
        }
        const prec = this.getFullPreconditions(name);
        if (!prec) {
            console.error(`Action Error: No precondition for action ${name}`);
            return;
        }
        this.ignoreRules(name);
        const regexp = new RegExp('^\\w+\\.\\w+\\.' + (this.domain ? '\\w+\\.' : ''));
        prec.conditions.forEach(([dynamic, prec]) => {
            const newDynamic = this.parseCstr(dynamic.toString().replace(regexp, ''));
            this.addRule(new speech_rule_1.SpeechRule(name, newDynamic, prec, postc));
        });
    }
    getFullPreconditions(name) {
        const prec = this.preconditions.get(name);
        if (prec || !this.inherits) {
            return prec;
        }
        return this.inherits.getFullPreconditions(name);
    }
    definePrecondition(name, dynamic, prec, ...args) {
        const fullPrec = this.parsePrecondition(prec, args);
        const dynamicCstr = this.parseCstr(dynamic);
        if (!(fullPrec && dynamicCstr)) {
            console.error(`Precondition Error: ${prec}, (${dynamic})`);
            return;
        }
        fullPrec.rank = this.rank++;
        this.preconditions.set(name, new Condition(dynamicCstr, fullPrec));
    }
    inheritRules() {
        if (!this.inherits || !this.inherits.getSpeechRules().length) {
            return;
        }
        const regexp = new RegExp('^\\w+\\.\\w+\\.' + (this.domain ? '\\w+\\.' : ''));
        this.inherits.getSpeechRules().forEach((rule) => {
            const newDynamic = this.parseCstr(rule.dynamicCstr.toString().replace(regexp, ''));
            this.addRule(new speech_rule_1.SpeechRule(rule.name, newDynamic, rule.precondition, rule.action));
        });
    }
    ignoreRules(name, ...cstrs) {
        let rules = this.findAllRules((r) => r.name === name);
        if (!cstrs.length) {
            rules.forEach(this.deleteRule.bind(this));
            return;
        }
        let rest = [];
        for (const cstr of cstrs) {
            const dynamic = this.parseCstr(cstr);
            for (const rule of rules) {
                if (dynamic.equal(rule.dynamicCstr)) {
                    this.deleteRule(rule);
                }
                else {
                    rest.push(rule);
                }
            }
            rules = rest;
            rest = [];
        }
    }
    parsePrecondition_(cstr) {
        const generator = this.context.customGenerators.lookup(cstr);
        return generator ? generator() : [cstr];
    }
}
exports.BaseRuleStore = BaseRuleStore;
class Condition {
    constructor(base, condition) {
        this.base = base;
        this._conditions = [];
        this.constraints = [];
        this.allCstr = {};
        this.constraints.push(base);
        this.addCondition(base, condition);
    }
    get conditions() {
        return this._conditions;
    }
    addConstraint(dynamic) {
        if (this.constraints.filter((cstr) => cstr.equal(dynamic)).length) {
            return;
        }
        this.constraints.push(dynamic);
        const newConds = [];
        for (const [dyn, pre] of this.conditions) {
            if (this.base.equal(dyn)) {
                newConds.push([dynamic, pre]);
            }
        }
        this._conditions = this._conditions.concat(newConds);
    }
    addBaseCondition(cond) {
        this.addCondition(this.base, cond);
    }
    addFullCondition(cond) {
        this.constraints.forEach((cstr) => this.addCondition(cstr, cond));
    }
    addCondition(dynamic, cond) {
        const condStr = dynamic.toString() + ' ' + cond.toString();
        if (this.allCstr.condStr) {
            return;
        }
        this.allCstr[condStr] = true;
        this._conditions.push([dynamic, cond]);
    }
}
exports.Condition = Condition;


/***/ }),

/***/ 1462:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BrailleStore = void 0;
const semantic_annotations_1 = __webpack_require__(4036);
const math_store_1 = __webpack_require__(7478);
class BrailleStore extends math_store_1.MathStore {
    constructor() {
        super(...arguments);
        this.modality = 'braille';
        this.customTranscriptions = { '\u22ca': '⠈⠡⠳' };
    }
    evaluateString(str) {
        const descs = [];
        const text = Array.from(str);
        for (let i = 0; i < text.length; i++) {
            descs.push(this.evaluateCharacter(text[i]));
        }
        return descs;
    }
    annotations() {
        for (let i = 0, annotator; (annotator = this.annotators[i]); i++) {
            (0, semantic_annotations_1.activate)(this.locale, annotator);
        }
    }
}
exports.BrailleStore = BrailleStore;


/***/ }),

/***/ 8310:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DefaultComparator = exports.DynamicCstrParser = exports.DynamicCstr = exports.DynamicProperties = exports.Axis = void 0;
var Axis;
(function (Axis) {
    Axis["DOMAIN"] = "domain";
    Axis["STYLE"] = "style";
    Axis["LOCALE"] = "locale";
    Axis["TOPIC"] = "topic";
    Axis["MODALITY"] = "modality";
})(Axis = exports.Axis || (exports.Axis = {}));
class DynamicProperties {
    constructor(properties, order = Object.keys(properties)) {
        this.properties = properties;
        this.order = order;
    }
    static createProp(...cstrList) {
        const axes = DynamicCstr.DEFAULT_ORDER;
        const dynamicCstr = {};
        for (let i = 0, l = cstrList.length, k = axes.length; i < l && i < k; i++) {
            dynamicCstr[axes[i]] = cstrList[i];
        }
        return new DynamicProperties(dynamicCstr);
    }
    getProperties() {
        return this.properties;
    }
    getOrder() {
        return this.order;
    }
    getAxes() {
        return this.order;
    }
    getProperty(key) {
        return this.properties[key];
    }
    updateProperties(props) {
        this.properties = props;
    }
    allProperties() {
        const propLists = [];
        this.order.forEach((key) => propLists.push(this.getProperty(key).slice()));
        return propLists;
    }
    toString() {
        const cstrStrings = [];
        this.order.forEach((key) => cstrStrings.push(key + ': ' + this.getProperty(key).toString()));
        return cstrStrings.join('\n');
    }
}
exports.DynamicProperties = DynamicProperties;
class DynamicCstr extends DynamicProperties {
    constructor(components_, order) {
        const properties = {};
        for (const [key, value] of Object.entries(components_)) {
            properties[key] = [value];
        }
        super(properties, order);
        this.components = components_;
    }
    static createCstr(...cstrList) {
        const axes = DynamicCstr.DEFAULT_ORDER;
        const dynamicCstr = {};
        for (let i = 0, l = cstrList.length, k = axes.length; i < l && i < k; i++) {
            dynamicCstr[axes[i]] = cstrList[i];
        }
        return new DynamicCstr(dynamicCstr);
    }
    static defaultCstr() {
        return DynamicCstr.createCstr.apply(null, DynamicCstr.DEFAULT_ORDER.map(function (x) {
            return DynamicCstr.DEFAULT_VALUES[x];
        }));
    }
    static validOrder(order) {
        const axes = DynamicCstr.DEFAULT_ORDER.slice();
        return order.every((x) => {
            const index = axes.indexOf(x);
            return index !== -1 && axes.splice(index, 1);
        });
    }
    getComponents() {
        return this.components;
    }
    getValue(key) {
        return this.components[key];
    }
    getValues() {
        return this.order.map((key) => this.getValue(key));
    }
    allProperties() {
        const propLists = super.allProperties();
        for (let i = 0, props, key; (props = propLists[i]), (key = this.order[i]); i++) {
            const value = this.getValue(key);
            if (props.indexOf(value) === -1) {
                props.unshift(value);
            }
        }
        return propLists;
    }
    toString() {
        return this.getValues().join('.');
    }
    equal(cstr) {
        const keys1 = cstr.getAxes();
        if (this.order.length !== keys1.length) {
            return false;
        }
        for (let j = 0, key; (key = keys1[j]); j++) {
            const comp2 = this.getValue(key);
            if (!comp2 || cstr.getValue(key) !== comp2) {
                return false;
            }
        }
        return true;
    }
}
exports.DynamicCstr = DynamicCstr;
DynamicCstr.DEFAULT_ORDER = [
    Axis.LOCALE,
    Axis.MODALITY,
    Axis.DOMAIN,
    Axis.STYLE,
    Axis.TOPIC
];
DynamicCstr.BASE_LOCALE = 'base';
DynamicCstr.DEFAULT_VALUE = 'default';
DynamicCstr.DEFAULT_VALUES = {
    [Axis.LOCALE]: 'en',
    [Axis.DOMAIN]: DynamicCstr.DEFAULT_VALUE,
    [Axis.STYLE]: DynamicCstr.DEFAULT_VALUE,
    [Axis.TOPIC]: DynamicCstr.DEFAULT_VALUE,
    [Axis.MODALITY]: 'speech'
};
class DynamicCstrParser {
    constructor(order) {
        this.order = order;
    }
    parse(str) {
        const order = str.split('.');
        const cstr = {};
        if (order.length > this.order.length) {
            throw new Error('Invalid dynamic constraint: ' + cstr);
        }
        let j = 0;
        for (let i = 0, key; (key = this.order[i]), order.length; i++, j++) {
            const value = order.shift();
            cstr[key] = value;
        }
        return new DynamicCstr(cstr, this.order.slice(0, j));
    }
}
exports.DynamicCstrParser = DynamicCstrParser;
class DefaultComparator {
    constructor(reference, fallback = new DynamicProperties(reference.getProperties(), reference.getOrder())) {
        this.reference = reference;
        this.fallback = fallback;
        this.order = this.reference.getOrder();
    }
    getReference() {
        return this.reference;
    }
    setReference(cstr, props) {
        this.reference = cstr;
        this.fallback =
            props || new DynamicProperties(cstr.getProperties(), cstr.getOrder());
        this.order = this.reference.getOrder();
    }
    match(cstr) {
        const keys1 = cstr.getAxes();
        return (keys1.length === this.reference.getAxes().length &&
            keys1.every((key) => {
                const value = cstr.getValue(key);
                return (value === this.reference.getValue(key) ||
                    this.fallback.getProperty(key).indexOf(value) !== -1);
            }));
    }
    compare(cstr1, cstr2) {
        let ignore = false;
        for (let i = 0, key; (key = this.order[i]); i++) {
            const value1 = cstr1.getValue(key);
            const value2 = cstr2.getValue(key);
            if (!ignore) {
                const ref = this.reference.getValue(key);
                if (ref === value1 && ref !== value2) {
                    return -1;
                }
                if (ref === value2 && ref !== value1) {
                    return 1;
                }
                if (ref === value1 && ref === value2) {
                    continue;
                }
                if (ref !== value1 && ref !== value2) {
                    ignore = true;
                }
            }
            const prop = this.fallback.getProperty(key);
            const index1 = prop.indexOf(value1);
            const index2 = prop.indexOf(value2);
            if (index1 < index2) {
                return -1;
            }
            if (index2 < index1) {
                return 1;
            }
        }
        return 0;
    }
    toString() {
        return this.reference.toString() + '\n' + this.fallback.toString();
    }
}
exports.DefaultComparator = DefaultComparator;


/***/ }),

/***/ 1058:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.numbersToAlpha = exports.Grammar = exports.ATTRIBUTE = void 0;
const DomUtil = __webpack_require__(6671);
const engine_1 = __webpack_require__(4886);
const LocaleUtil = __webpack_require__(3319);
const locale_1 = __webpack_require__(4524);
exports.ATTRIBUTE = 'grammar';
class Grammar {
    constructor() {
        this.currentFlags = {};
        this.parameters_ = {};
        this.corrections_ = {};
        this.preprocessors_ = {};
        this.stateStack_ = [];
    }
    static getInstance() {
        Grammar.instance = Grammar.instance || new Grammar();
        return Grammar.instance;
    }
    static parseInput(grammar) {
        const attributes = {};
        const components = grammar.split(':');
        for (let i = 0, l = components.length; i < l; i++) {
            const comp = components[i].split('=');
            const key = comp[0].trim();
            if (comp[1]) {
                attributes[key] = comp[1].trim();
                continue;
            }
            key.match(/^!/)
                ? (attributes[key.slice(1)] = false)
                : (attributes[key] = true);
        }
        return attributes;
    }
    static parseState(stateStr) {
        const state = {};
        const corrections = stateStr.split(' ');
        for (let i = 0, l = corrections.length; i < l; i++) {
            const corr = corrections[i].split(':');
            const key = corr[0];
            const value = corr[1];
            state[key] = value ? value : true;
        }
        return state;
    }
    static translateString_(text) {
        if (text.match(/:unit$/)) {
            return Grammar.translateUnit_(text);
        }
        const engine = engine_1.default.getInstance();
        let result = engine.evaluator(text, engine.dynamicCstr);
        result = result === null ? text : result;
        if (Grammar.getInstance().getParameter('plural')) {
            result = locale_1.LOCALE.FUNCTIONS.plural(result);
        }
        return result;
    }
    static translateUnit_(text) {
        text = Grammar.prepareUnit_(text);
        const engine = engine_1.default.getInstance();
        const plural = Grammar.getInstance().getParameter('plural');
        const strict = engine.strict;
        const baseCstr = `${engine.locale}.${engine.modality}.default`;
        engine.strict = true;
        let cstr;
        let result;
        if (plural) {
            cstr = engine.defaultParser.parse(baseCstr + '.plural');
            result = engine.evaluator(text, cstr);
        }
        if (result) {
            engine.strict = strict;
            return result;
        }
        cstr = engine.defaultParser.parse(baseCstr + '.default');
        result = engine.evaluator(text, cstr);
        engine.strict = strict;
        if (!result) {
            return Grammar.cleanUnit_(text);
        }
        if (plural) {
            result = locale_1.LOCALE.FUNCTIONS.plural(result);
        }
        return result;
    }
    static prepareUnit_(text) {
        const match = text.match(/:unit$/);
        return match
            ? text.slice(0, match.index).replace(/\s+/g, ' ') +
                text.slice(match.index)
            : text;
    }
    static cleanUnit_(text) {
        if (text.match(/:unit$/)) {
            return text.replace(/:unit$/, '');
        }
        return text;
    }
    clear() {
        this.parameters_ = {};
        this.stateStack_ = [];
    }
    setParameter(parameter, value) {
        const oldValue = this.parameters_[parameter];
        value
            ? (this.parameters_[parameter] = value)
            : delete this.parameters_[parameter];
        return oldValue;
    }
    getParameter(parameter) {
        return this.parameters_[parameter];
    }
    setCorrection(correction, func) {
        this.corrections_[correction] = func;
    }
    setPreprocessor(preprocessor, func) {
        this.preprocessors_[preprocessor] = func;
    }
    getCorrection(correction) {
        return this.corrections_[correction];
    }
    getState() {
        const pairs = [];
        for (const key in this.parameters_) {
            const value = this.parameters_[key];
            pairs.push(typeof value === 'string' ? key + ':' + value : key);
        }
        return pairs.join(' ');
    }
    pushState(assignment) {
        for (const key in assignment) {
            assignment[key] = this.setParameter(key, assignment[key]);
        }
        this.stateStack_.push(assignment);
    }
    popState() {
        const assignment = this.stateStack_.pop();
        for (const key in assignment) {
            this.setParameter(key, assignment[key]);
        }
    }
    setAttribute(node) {
        if (node && node.nodeType === DomUtil.NodeType.ELEMENT_NODE) {
            const state = this.getState();
            if (state) {
                node.setAttribute(exports.ATTRIBUTE, state);
            }
        }
    }
    preprocess(text) {
        return this.runProcessors_(text, this.preprocessors_);
    }
    correct(text) {
        return this.runProcessors_(text, this.corrections_);
    }
    apply(text, opt_flags) {
        this.currentFlags = opt_flags || {};
        text =
            this.currentFlags.adjust || this.currentFlags.preprocess
                ? Grammar.getInstance().preprocess(text)
                : text;
        if (this.parameters_['translate'] || this.currentFlags.translate) {
            text = Grammar.translateString_(text);
        }
        text =
            this.currentFlags.adjust || this.currentFlags.correct
                ? Grammar.getInstance().correct(text)
                : text;
        this.currentFlags = {};
        return text;
    }
    runProcessors_(text, funcs) {
        for (const key in this.parameters_) {
            const func = funcs[key];
            if (!func) {
                continue;
            }
            const value = this.parameters_[key];
            text = value === true ? func(text) : func(text, value);
        }
        return text;
    }
}
exports.Grammar = Grammar;
function correctFont_(text, correction) {
    if (!correction || !text) {
        return text;
    }
    const regexp = locale_1.LOCALE.FUNCTIONS.fontRegexp(LocaleUtil.localFont(correction));
    return text.replace(regexp, '');
}
function correctCaps_(text) {
    let cap = locale_1.LOCALE.ALPHABETS.capPrefix[engine_1.default.getInstance().domain];
    if (typeof cap === 'undefined') {
        cap = locale_1.LOCALE.ALPHABETS.capPrefix['default'];
    }
    return correctFont_(text, cap);
}
function addAnnotation_(text, annotation) {
    return text + ':' + annotation;
}
function numbersToAlpha(text) {
    return text.match(/\d+/)
        ? locale_1.LOCALE.NUMBERS.numberToWords(parseInt(text, 10))
        : text;
}
exports.numbersToAlpha = numbersToAlpha;
function noTranslateText_(text) {
    if (text.match(new RegExp('^[' + locale_1.LOCALE.MESSAGES.regexp.TEXT + ']+$'))) {
        Grammar.getInstance().currentFlags['translate'] = false;
    }
    return text;
}
Grammar.getInstance().setCorrection('localFont', LocaleUtil.localFont);
Grammar.getInstance().setCorrection('localRole', LocaleUtil.localRole);
Grammar.getInstance().setCorrection('localEnclose', LocaleUtil.localEnclose);
Grammar.getInstance().setCorrection('ignoreFont', correctFont_);
Grammar.getInstance().setPreprocessor('annotation', addAnnotation_);
Grammar.getInstance().setPreprocessor('noTranslateText', noTranslateText_);
Grammar.getInstance().setCorrection('ignoreCaps', correctCaps_);
Grammar.getInstance().setPreprocessor('numbers2alpha', numbersToAlpha);


/***/ }),

/***/ 4161:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.enumerate = exports.lookupString = exports.lookupCategory = exports.lookupRule = exports.addSiUnitRules = exports.addUnitRules = exports.addFunctionRules = exports.addSymbolRules = exports.defineRule = exports.defineRules = exports.setSiPrefixes = void 0;
const debugger_1 = __webpack_require__(1984);
const engine_1 = __webpack_require__(4886);
const l10n_1 = __webpack_require__(2371);
const math_simple_store_1 = __webpack_require__(4974);
const dynamic_cstr_1 = __webpack_require__(8310);
let locale = dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.LOCALE];
let modality = dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.MODALITY];
let siPrefixes = {};
function setSiPrefixes(prefixes) {
    siPrefixes = prefixes;
}
exports.setSiPrefixes = setSiPrefixes;
const subStores_ = {};
function defineRules(name, str, cat, mappings) {
    const store = getSubStore_(str);
    setupStore_(store, cat);
    store.defineRulesFromMappings(name, locale, modality, str, mappings);
}
exports.defineRules = defineRules;
function defineRule(name, domain, style, cat, str, content) {
    const store = getSubStore_(str);
    setupStore_(store, cat);
    store.defineRuleFromStrings(name, locale, modality, domain, style, str, content);
}
exports.defineRule = defineRule;
function addSymbolRules(json) {
    if (changeLocale_(json)) {
        return;
    }
    const key = math_simple_store_1.MathSimpleStore.parseUnicode(json['key']);
    defineRules(json['key'], key, json['category'], json['mappings']);
}
exports.addSymbolRules = addSymbolRules;
function addFunctionRules(json) {
    if (changeLocale_(json)) {
        return;
    }
    const names = json['names'];
    const mappings = json['mappings'];
    const category = json['category'];
    for (let j = 0, name; (name = names[j]); j++) {
        defineRules(name, name, category, mappings);
    }
}
exports.addFunctionRules = addFunctionRules;
function addUnitRules(json) {
    if (changeLocale_(json)) {
        return;
    }
    if (json['si']) {
        addSiUnitRules(json);
        return;
    }
    addUnitRules_(json);
}
exports.addUnitRules = addUnitRules;
function addSiUnitRules(json) {
    for (const key of Object.keys(siPrefixes)) {
        const newJson = Object.assign({}, json);
        newJson.mappings = {};
        const prefix = siPrefixes[key];
        newJson['key'] = key + newJson['key'];
        newJson['names'] = newJson['names'].map(function (name) {
            return key + name;
        });
        for (const domain of Object.keys(json['mappings'])) {
            newJson.mappings[domain] = {};
            for (const style of Object.keys(json['mappings'][domain])) {
                newJson['mappings'][domain][style] = l10n_1.locales[locale]().FUNCTIONS.si(prefix, json['mappings'][domain][style]);
            }
        }
        addUnitRules_(newJson);
    }
    addUnitRules_(json);
}
exports.addSiUnitRules = addSiUnitRules;
function lookupRule(node, dynamic) {
    const store = subStores_[node];
    return store ? store.lookupRule(null, dynamic) : null;
}
exports.lookupRule = lookupRule;
function lookupCategory(character) {
    const store = subStores_[character];
    return store ? store.category : '';
}
exports.lookupCategory = lookupCategory;
function lookupString(text, dynamic) {
    const rule = lookupRule(text, dynamic);
    if (!rule) {
        return null;
    }
    return rule.action;
}
exports.lookupString = lookupString;
engine_1.default.getInstance().evaluator = lookupString;
function enumerate(info = {}) {
    for (const store of Object.values(subStores_)) {
        for (const [, rules] of store.rules.entries()) {
            for (const { cstr: dynamic } of rules) {
                info = enumerate_(dynamic.getValues(), info);
            }
        }
    }
    return info;
}
exports.enumerate = enumerate;
function enumerate_(dynamic, info) {
    info = info || {};
    if (!dynamic.length) {
        return info;
    }
    info[dynamic[0]] = enumerate_(dynamic.slice(1), info[dynamic[0]]);
    return info;
}
function addUnitRules_(json) {
    const names = json['names'];
    if (names) {
        json['names'] = names.map(function (name) {
            return name + ':' + 'unit';
        });
    }
    addFunctionRules(json);
}
function changeLocale_(json) {
    if (!json['locale'] && !json['modality']) {
        return false;
    }
    locale = json['locale'] || locale;
    modality = json['modality'] || modality;
    return true;
}
function getSubStore_(key) {
    let store = subStores_[key];
    if (store) {
        debugger_1.Debugger.getInstance().output('Store exists! ' + key);
        return store;
    }
    store = new math_simple_store_1.MathSimpleStore();
    subStores_[key] = store;
    return store;
}
function setupStore_(store, opt_cat) {
    if (opt_cat) {
        store.category = opt_cat;
    }
}


/***/ }),

/***/ 4974:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MathSimpleStore = void 0;
const engine_1 = __webpack_require__(4886);
const dynamic_cstr_1 = __webpack_require__(8310);
class MathSimpleStore {
    constructor() {
        this.category = '';
        this.rules = new Map();
    }
    static parseUnicode(num) {
        const keyValue = parseInt(num, 16);
        return String.fromCodePoint(keyValue);
    }
    static testDynamicConstraints_(dynamic, rule) {
        if (engine_1.default.getInstance().strict) {
            return rule.cstr.equal(dynamic);
        }
        return engine_1.default.getInstance().comparator.match(rule.cstr);
    }
    defineRulesFromMappings(name, locale, modality, str, mapping) {
        for (const domain in mapping) {
            for (const style in mapping[domain]) {
                const content = mapping[domain][style];
                this.defineRuleFromStrings(name, locale, modality, domain, style, str, content);
            }
        }
    }
    getRules(key) {
        let store = this.rules.get(key);
        if (!store) {
            store = [];
            this.rules.set(key, store);
        }
        return store;
    }
    defineRuleFromStrings(_name, locale, modality, domain, style, _str, content) {
        let store = this.getRules(locale);
        const parser = engine_1.default.getInstance().parsers[domain] ||
            engine_1.default.getInstance().defaultParser;
        const comp = engine_1.default.getInstance().comparators[domain];
        const cstr = `${locale}.${modality}.${domain}.${style}`;
        const dynamic = parser.parse(cstr);
        const comparator = comp ? comp() : engine_1.default.getInstance().comparator;
        const oldCstr = comparator.getReference();
        comparator.setReference(dynamic);
        const rule = { cstr: dynamic, action: content };
        store = store.filter((r) => !dynamic.equal(r.cstr));
        store.push(rule);
        this.rules.set(locale, store);
        comparator.setReference(oldCstr);
    }
    lookupRule(_node, dynamic) {
        let rules = this.getRules(dynamic.getValue(dynamic_cstr_1.Axis.LOCALE));
        rules = rules.filter(function (rule) {
            return MathSimpleStore.testDynamicConstraints_(dynamic, rule);
        });
        if (rules.length === 1) {
            return rules[0];
        }
        return rules.length
            ? rules.sort((r1, r2) => engine_1.default.getInstance().comparator.compare(r1.cstr, r2.cstr))[0]
            : null;
    }
}
exports.MathSimpleStore = MathSimpleStore;


/***/ }),

/***/ 7478:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MathStore = void 0;
const BaseUtil = __webpack_require__(1426);
const locale_1 = __webpack_require__(4524);
const semantic_annotations_1 = __webpack_require__(4036);
const base_rule_store_1 = __webpack_require__(1970);
const speech_rule_1 = __webpack_require__(7039);
class MathStore extends base_rule_store_1.BaseRuleStore {
    constructor() {
        super();
        this.annotators = [];
        this.parseMethods['Alias'] = this.defineAlias;
        this.parseMethods['SpecializedRule'] = this.defineSpecializedRule;
        this.parseMethods['Specialized'] = this.defineSpecialized;
    }
    initialize() {
        if (this.initialized) {
            return;
        }
        this.annotations();
        this.initialized = true;
    }
    annotations() {
        for (let i = 0, annotator; (annotator = this.annotators[i]); i++) {
            (0, semantic_annotations_1.activate)(this.domain, annotator);
        }
    }
    defineAlias(name, prec, ...args) {
        const fullPrec = this.parsePrecondition(prec, args);
        if (!fullPrec) {
            console.error(`Precondition Error: ${prec} ${args}`);
            return;
        }
        const condition = this.preconditions.get(name);
        if (!condition) {
            console.error(`Alias Error: No precondition by the name of ${name}`);
            return;
        }
        condition.addFullCondition(fullPrec);
    }
    defineRulesAlias(name, query, ...args) {
        const rules = this.findAllRules(function (rule) {
            return rule.name === name;
        });
        if (rules.length === 0) {
            throw new speech_rule_1.OutputError('Rule with name ' + name + ' does not exist.');
        }
        const keep = [];
        const findKeep = (rule) => {
            const cstr = rule.dynamicCstr.toString();
            const action = rule.action.toString();
            for (let i = 0, k; (k = keep[i]); i++) {
                if (k.action === action && k.cstr === cstr) {
                    return false;
                }
            }
            keep.push({ cstr: cstr, action: action });
            return true;
        };
        rules.forEach((rule) => {
            if (findKeep(rule)) {
                this.addAlias_(rule, query, args);
            }
        });
    }
    defineSpecializedRule(name, oldDynamic, newDynamic, opt_action) {
        const dynamicCstr = this.parseCstr(oldDynamic);
        const rule = this.findRule((rule) => rule.name === name && dynamicCstr.equal(rule.dynamicCstr));
        const newCstr = this.parseCstr(newDynamic);
        if (!rule && opt_action) {
            throw new speech_rule_1.OutputError('Rule named ' + name + ' with style ' + oldDynamic + ' does not exist.');
        }
        const action = opt_action ? speech_rule_1.Action.fromString(opt_action) : rule.action;
        const newRule = new speech_rule_1.SpeechRule(rule.name, newCstr, rule.precondition, action);
        this.addRule(newRule);
    }
    defineSpecialized(name, _old, dynamic) {
        const cstr = this.parseCstr(dynamic);
        if (!cstr) {
            console.error(`Dynamic Constraint Error: ${dynamic}`);
            return;
        }
        const condition = this.preconditions.get(name);
        if (!condition) {
            console.error(`Alias Error: No precondition by the name of ${name}`);
            return;
        }
        condition.addConstraint(cstr);
    }
    evaluateString(str) {
        const descs = [];
        if (str.match(/^\s+$/)) {
            return descs;
        }
        let num = this.matchNumber_(str);
        if (num && num.length === str.length) {
            descs.push(this.evaluateCharacter(num.number));
            return descs;
        }
        const split = BaseUtil.removeEmpty(str.replace(/\s/g, ' ').split(' '));
        for (let i = 0, s; (s = split[i]); i++) {
            if (s.length === 1) {
                descs.push(this.evaluateCharacter(s));
            }
            else if (s.match(new RegExp('^[' + locale_1.LOCALE.MESSAGES.regexp.TEXT + ']+$'))) {
                descs.push(this.evaluateCharacter(s));
            }
            else {
                let rest = s;
                while (rest) {
                    num = this.matchNumber_(rest);
                    const alpha = rest.match(new RegExp('^[' + locale_1.LOCALE.MESSAGES.regexp.TEXT + ']+'));
                    if (num) {
                        descs.push(this.evaluateCharacter(num.number));
                        rest = rest.substring(num.length);
                    }
                    else if (alpha) {
                        descs.push(this.evaluateCharacter(alpha[0]));
                        rest = rest.substring(alpha[0].length);
                    }
                    else {
                        const chars = Array.from(rest);
                        const chr = chars[0];
                        descs.push(this.evaluateCharacter(chr));
                        rest = chars.slice(1).join('');
                    }
                }
            }
        }
        return descs;
    }
    parse(ruleSet) {
        super.parse(ruleSet);
        this.annotators = ruleSet['annotators'] || [];
    }
    addAlias_(rule, query, cstrList) {
        const prec = this.parsePrecondition(query, cstrList);
        const newRule = new speech_rule_1.SpeechRule(rule.name, rule.dynamicCstr, prec, rule.action);
        newRule.name = rule.name;
        this.addRule(newRule);
    }
    matchNumber_(str) {
        const locNum = str.match(new RegExp('^' + locale_1.LOCALE.MESSAGES.regexp.NUMBER));
        const enNum = str.match(new RegExp('^' + MathStore.regexp.NUMBER));
        if (!locNum && !enNum) {
            return null;
        }
        const isEn = enNum && enNum[0] === str;
        const isLoc = (locNum && locNum[0] === str) || !isEn;
        if (isLoc) {
            return locNum ? { number: locNum[0], length: locNum[0].length } : null;
        }
        const num = enNum[0]
            .replace(new RegExp(MathStore.regexp.DIGIT_GROUP, 'g'), 'X')
            .replace(new RegExp(MathStore.regexp.DECIMAL_MARK, 'g'), locale_1.LOCALE.MESSAGES.regexp.DECIMAL_MARK)
            .replace(/X/g, locale_1.LOCALE.MESSAGES.regexp.DIGIT_GROUP.replace(/\\/g, ''));
        return { number: num, length: enNum[0].length };
    }
}
exports.MathStore = MathStore;
MathStore.regexp = {
    NUMBER: '((\\d{1,3})(?=(,| ))((,| )\\d{3})*(\\.\\d+)?)|^\\d*\\.\\d+|^\\d+',
    DECIMAL_MARK: '\\.',
    DIGIT_GROUP: ','
};


/***/ }),

/***/ 7039:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.OutputError = exports.Precondition = exports.Action = exports.Component = exports.ActionType = exports.SpeechRule = void 0;
const engine_1 = __webpack_require__(4886);
const Grammar = __webpack_require__(1058);
class SpeechRule {
    constructor(name, dynamicCstr, precondition, action) {
        this.name = name;
        this.dynamicCstr = dynamicCstr;
        this.precondition = precondition;
        this.action = action;
        this.context = null;
    }
    toString() {
        return (this.name +
            ' | ' +
            this.dynamicCstr.toString() +
            ' | ' +
            this.precondition.toString() +
            ' ==> ' +
            this.action.toString());
    }
}
exports.SpeechRule = SpeechRule;
var ActionType;
(function (ActionType) {
    ActionType["NODE"] = "NODE";
    ActionType["MULTI"] = "MULTI";
    ActionType["TEXT"] = "TEXT";
    ActionType["PERSONALITY"] = "PERSONALITY";
})(ActionType = exports.ActionType || (exports.ActionType = {}));
function actionFromString(str) {
    switch (str) {
        case '[n]':
            return ActionType.NODE;
        case '[m]':
            return ActionType.MULTI;
        case '[t]':
            return ActionType.TEXT;
        case '[p]':
            return ActionType.PERSONALITY;
        default:
            throw 'Parse error: ' + str;
    }
}
function actionToString(speechType) {
    switch (speechType) {
        case ActionType.NODE:
            return '[n]';
        case ActionType.MULTI:
            return '[m]';
        case ActionType.TEXT:
            return '[t]';
        case ActionType.PERSONALITY:
            return '[p]';
        default:
            throw 'Unknown type error: ' + speechType;
    }
}
class Component {
    constructor({ type, content, attributes, grammar }) {
        this.type = type;
        this.content = content;
        this.attributes = attributes;
        this.grammar = grammar;
    }
    static grammarFromString(grammar) {
        return Grammar.Grammar.parseInput(grammar);
    }
    static fromString(input) {
        const output = {
            type: actionFromString(input.substring(0, 3))
        };
        let rest = input.slice(3).trim();
        if (!rest) {
            throw new OutputError('Missing content.');
        }
        switch (output.type) {
            case ActionType.TEXT:
                if (rest[0] === '"') {
                    const quotedString = splitString(rest, '\\(')[0].trim();
                    if (quotedString.slice(-1) !== '"') {
                        throw new OutputError('Invalid string syntax.');
                    }
                    output.content = quotedString;
                    rest = rest.slice(quotedString.length).trim();
                    if (rest.indexOf('(') === -1) {
                        rest = '';
                    }
                    break;
                }
            case ActionType.NODE:
            case ActionType.MULTI:
                {
                    const bracket = rest.indexOf(' (');
                    if (bracket === -1) {
                        output.content = rest.trim();
                        rest = '';
                        break;
                    }
                    output.content = rest.substring(0, bracket).trim();
                    rest = rest.slice(bracket).trim();
                }
                break;
        }
        if (rest) {
            const attributes = Component.attributesFromString(rest);
            if (attributes.grammar) {
                output.grammar = attributes.grammar;
                delete attributes.grammar;
            }
            if (Object.keys(attributes).length) {
                output.attributes = attributes;
            }
        }
        return new Component(output);
    }
    static attributesFromString(attrs) {
        if (attrs[0] !== '(' || attrs.slice(-1) !== ')') {
            throw new OutputError('Invalid attribute expression: ' + attrs);
        }
        const attributes = {};
        const attribs = splitString(attrs.slice(1, -1), ',');
        for (let i = 0, m = attribs.length; i < m; i++) {
            const attr = attribs[i];
            const colon = attr.indexOf(':');
            if (colon === -1) {
                attributes[attr.trim()] = 'true';
            }
            else {
                const key = attr.substring(0, colon).trim();
                const value = attr.slice(colon + 1).trim();
                attributes[key] =
                    key === Grammar.ATTRIBUTE
                        ? Component.grammarFromString(value)
                        : value;
            }
        }
        return attributes;
    }
    toString() {
        let strs = '';
        strs += actionToString(this.type);
        strs += this.content ? ' ' + this.content : '';
        const attrs = this.attributesToString();
        strs += attrs ? ' ' + attrs : '';
        return strs;
    }
    grammarToString() {
        return this.getGrammar().join(':');
    }
    getGrammar() {
        const attribs = [];
        for (const key in this.grammar) {
            if (this.grammar[key] === true) {
                attribs.push(key);
            }
            else if (this.grammar[key] === false) {
                attribs.push('!' + key);
            }
            else {
                attribs.push(key + '=' + this.grammar[key]);
            }
        }
        return attribs;
    }
    attributesToString() {
        const attribs = this.getAttributes();
        const grammar = this.grammarToString();
        if (grammar) {
            attribs.push('grammar:' + grammar);
        }
        return attribs.length > 0 ? '(' + attribs.join(', ') + ')' : '';
    }
    getAttributes() {
        const attribs = [];
        for (const key in this.attributes) {
            const value = this.attributes[key];
            value === 'true' ? attribs.push(key) : attribs.push(key + ':' + value);
        }
        return attribs;
    }
}
exports.Component = Component;
class Action {
    constructor(components) {
        this.components = components;
    }
    static fromString(input) {
        const comps = splitString(input, ';')
            .filter(function (x) {
            return x.match(/\S/);
        })
            .map(function (x) {
            return x.trim();
        });
        const newComps = [];
        for (let i = 0, m = comps.length; i < m; i++) {
            const comp = Component.fromString(comps[i]);
            if (comp) {
                newComps.push(comp);
            }
        }
        return new Action(newComps);
    }
    toString() {
        const comps = this.components.map(function (c) {
            return c.toString();
        });
        return comps.join('; ');
    }
}
exports.Action = Action;
class Precondition {
    constructor(query, ...cstr) {
        this.query = query;
        this.constraints = cstr;
        const [exists, user] = this.presetPriority();
        this.priority = exists ? user : this.calculatePriority();
    }
    static constraintValue(constr, priorities) {
        for (let i = 0, regexp; (regexp = priorities[i]); i++) {
            if (constr.match(regexp)) {
                return ++i;
            }
        }
        return 0;
    }
    toString() {
        const constrs = this.constraints.join(', ');
        return `${this.query}, ${constrs} (${this.priority}, ${this.rank})`;
    }
    calculatePriority() {
        const query = Precondition.constraintValue(this.query, Precondition.queryPriorities);
        if (!query) {
            return 0;
        }
        const inner = this.query.match(/^self::.+\[(.+)\]/)[1];
        const attr = Precondition.constraintValue(inner, Precondition.attributePriorities);
        return query * 100 + attr * 10;
    }
    presetPriority() {
        if (!this.constraints.length) {
            return [false, 0];
        }
        const last = this.constraints[this.constraints.length - 1].match(/^priority=(.*$)/);
        if (!last) {
            return [false, 0];
        }
        this.constraints.pop();
        const numb = parseFloat(last[1]);
        return [true, isNaN(numb) ? 0 : numb];
    }
}
exports.Precondition = Precondition;
Precondition.queryPriorities = [
    /^self::\*\[.+\]$/,
    /^self::[\w-]+\[.+\]$/
];
Precondition.attributePriorities = [
    /^@[\w-]+$/,
    /^@[\w-]+!=".+"$/,
    /^not\(contains\(@[\w-]+,\s*".+"\)\)$/,
    /^contains\(@[\w-]+,".+"\)$/,
    /^@[\w-]+=".+"$/
];
class OutputError extends engine_1.SREError {
    constructor(msg) {
        super(msg);
        this.name = 'RuleError';
    }
}
exports.OutputError = OutputError;
function splitString(str, sep) {
    const strList = [];
    let prefix = '';
    while (str !== '') {
        const sepPos = str.search(sep);
        if (sepPos === -1) {
            if ((str.match(/"/g) || []).length % 2 !== 0) {
                throw new OutputError('Invalid string in expression: ' + str);
            }
            strList.push(prefix + str);
            prefix = '';
            str = '';
        }
        else if ((str.substring(0, sepPos).match(/"/g) || []).length % 2 === 0) {
            strList.push(prefix + str.substring(0, sepPos));
            prefix = '';
            str = str.substring(sepPos + 1);
        }
        else {
            const nextQuot = str.substring(sepPos).search('"');
            if (nextQuot === -1) {
                throw new OutputError('Invalid string in expression: ' + str);
            }
            else {
                prefix = prefix + str.substring(0, sepPos + nextQuot + 1);
                str = str.substring(sepPos + nextQuot + 1);
            }
        }
    }
    if (prefix) {
        strList.push(prefix);
    }
    return strList;
}


/***/ }),

/***/ 443:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SpeechRuleContext = void 0;
const XpathUtil = __webpack_require__(5024);
const srf = __webpack_require__(3686);
class SpeechRuleContext {
    constructor() {
        this.customQueries = new srf.CustomQueries();
        this.customStrings = new srf.CustomStrings();
        this.contextFunctions = new srf.ContextFunctions();
        this.customGenerators = new srf.CustomGenerators();
    }
    applyCustomQuery(node, funcName) {
        const func = this.customQueries.lookup(funcName);
        return func ? func(node) : null;
    }
    applySelector(node, expr) {
        const result = this.applyCustomQuery(node, expr);
        return result || XpathUtil.evalXPath(expr, node);
    }
    applyQuery(node, expr) {
        const results = this.applySelector(node, expr);
        if (results.length > 0) {
            return results[0];
        }
        return null;
    }
    applyConstraint(node, expr) {
        const result = this.applyQuery(node, expr);
        return !!result || XpathUtil.evaluateBoolean(expr, node);
    }
    constructString(node, expr) {
        if (!expr) {
            return '';
        }
        if (expr.charAt(0) === '"') {
            return expr.slice(1, -1);
        }
        const func = this.customStrings.lookup(expr);
        if (func) {
            return func(node);
        }
        return XpathUtil.evaluateString(expr, node);
    }
    parse(functions) {
        const functs = Array.isArray(functions)
            ? functions
            : Object.entries(functions);
        for (let i = 0, func; (func = functs[i]); i++) {
            const kind = func[0].slice(0, 3);
            switch (kind) {
                case 'CQF':
                    this.customQueries.add(func[0], func[1]);
                    break;
                case 'CSF':
                    this.customStrings.add(func[0], func[1]);
                    break;
                case 'CTF':
                    this.contextFunctions.add(func[0], func[1]);
                    break;
                case 'CGF':
                    this.customGenerators.add(func[0], func[1]);
                    break;
                default:
                    console.error('FunctionError: Invalid function name ' + func[0]);
            }
        }
    }
}
exports.SpeechRuleContext = SpeechRuleContext;


/***/ }),

/***/ 6060:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.storeFactory = exports.SpeechRuleEngine = void 0;
const auditory_description_1 = __webpack_require__(4148);
const debugger_1 = __webpack_require__(1984);
const DomUtil = __webpack_require__(6671);
const engine_1 = __webpack_require__(4886);
const EngineConst = __webpack_require__(4998);
const xpath_util_1 = __webpack_require__(5024);
const SpeechRules = __webpack_require__(7278);
const SpeechRuleStores = __webpack_require__(9805);
const braille_store_1 = __webpack_require__(1462);
const dynamic_cstr_1 = __webpack_require__(8310);
const grammar_1 = __webpack_require__(1058);
const math_store_1 = __webpack_require__(7478);
const speech_rule_1 = __webpack_require__(7039);
const trie_1 = __webpack_require__(2803);
class SpeechRuleEngine {
    constructor() {
        this.trie = null;
        this.evaluators_ = {};
        this.trie = new trie_1.Trie();
    }
    static getInstance() {
        SpeechRuleEngine.instance =
            SpeechRuleEngine.instance || new SpeechRuleEngine();
        return SpeechRuleEngine.instance;
    }
    static debugSpeechRule(rule, node) {
        const prec = rule.precondition;
        const queryResult = rule.context.applyQuery(node, prec.query);
        debugger_1.Debugger.getInstance().output(prec.query, queryResult ? queryResult.toString() : queryResult);
        prec.constraints.forEach((cstr) => debugger_1.Debugger.getInstance().output(cstr, rule.context.applyConstraint(node, cstr)));
    }
    static debugNamedSpeechRule(name, node) {
        const rules = SpeechRuleEngine.getInstance().trie.collectRules();
        const allRules = rules.filter((rule) => rule.name == name);
        for (let i = 0, rule; (rule = allRules[i]); i++) {
            debugger_1.Debugger.getInstance().output('Rule', name, 'DynamicCstr:', rule.dynamicCstr.toString(), 'number', i);
            SpeechRuleEngine.debugSpeechRule(rule, node);
        }
    }
    evaluateNode(node) {
        (0, xpath_util_1.updateEvaluator)(node);
        const timeIn = new Date().getTime();
        let result = [];
        try {
            result = this.evaluateNode_(node);
        }
        catch (err) {
            console.error('Something went wrong computing speech.');
            debugger_1.Debugger.getInstance().output(err);
        }
        const timeOut = new Date().getTime();
        debugger_1.Debugger.getInstance().output('Time:', timeOut - timeIn);
        return result;
    }
    toString() {
        const allRules = this.trie.collectRules();
        return allRules.map((rule) => rule.toString()).join('\n');
    }
    runInSetting(settings, callback) {
        const engine = engine_1.default.getInstance();
        const save = {};
        for (const key in settings) {
            save[key] = engine[key];
            engine[key] = settings[key];
        }
        engine.setDynamicCstr();
        const result = callback();
        for (const key in save) {
            engine[key] = save[key];
        }
        engine.setDynamicCstr();
        return result;
    }
    addStore(set) {
        const store = storeFactory(set);
        if (store.kind !== 'abstract') {
            store.getSpeechRules().forEach((x) => this.trie.addRule(x));
        }
        this.addEvaluator(store);
    }
    processGrammar(context, node, grammar) {
        const assignment = {};
        for (const key in grammar) {
            const value = grammar[key];
            assignment[key] =
                typeof value === 'string'
                    ?
                        context.constructString(node, value)
                    : value;
        }
        grammar_1.Grammar.getInstance().pushState(assignment);
    }
    addEvaluator(store) {
        const fun = store.evaluateDefault.bind(store);
        const loc = this.evaluators_[store.locale];
        if (loc) {
            loc[store.modality] = fun;
            return;
        }
        const mod = {};
        mod[store.modality] = fun;
        this.evaluators_[store.locale] = mod;
    }
    getEvaluator(locale, modality) {
        const loc = this.evaluators_[locale] ||
            this.evaluators_[dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.LOCALE]];
        return loc[modality] || loc[dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.MODALITY]];
    }
    enumerate(opt_info) {
        return this.trie.enumerate(opt_info);
    }
    evaluateNode_(node) {
        if (!node) {
            return [];
        }
        this.updateConstraint_();
        return this.evaluateTree_(node);
    }
    evaluateTree_(node) {
        const engine = engine_1.default.getInstance();
        let result;
        debugger_1.Debugger.getInstance().output(engine.mode !== EngineConst.Mode.HTTP ? node.toString() : node);
        grammar_1.Grammar.getInstance().setAttribute(node);
        const rule = this.lookupRule(node, engine.dynamicCstr);
        if (!rule) {
            if (engine.strict) {
                return [];
            }
            result = this.getEvaluator(engine.locale, engine.modality)(node);
            if (node.attributes) {
                this.addPersonality_(result, {}, false, node);
            }
            return result;
        }
        debugger_1.Debugger.getInstance().generateOutput(() => [
            'Apply Rule:',
            rule.name,
            rule.dynamicCstr.toString(),
            (engine.mode !== EngineConst.Mode.HTTP ? node : node).toString()
        ]);
        const context = rule.context;
        const components = rule.action.components;
        result = [];
        for (let i = 0, component; (component = components[i]); i++) {
            let descrs = [];
            const content = component.content || '';
            const attributes = component.attributes || {};
            let multi = false;
            if (component.grammar) {
                this.processGrammar(context, node, component.grammar);
            }
            let saveEngine = null;
            if (attributes.engine) {
                saveEngine = engine_1.default.getInstance().dynamicCstr.getComponents();
                const features = grammar_1.Grammar.parseInput(attributes.engine);
                engine_1.default.getInstance().setDynamicCstr(features);
            }
            switch (component.type) {
                case speech_rule_1.ActionType.NODE:
                    {
                        const selected = context.applyQuery(node, content);
                        if (selected) {
                            descrs = this.evaluateTree_(selected);
                        }
                    }
                    break;
                case speech_rule_1.ActionType.MULTI:
                    {
                        multi = true;
                        const selects = context.applySelector(node, content);
                        if (selects.length > 0) {
                            descrs = this.evaluateNodeList_(context, selects, attributes['sepFunc'], context.constructString(node, attributes['separator']), attributes['ctxtFunc'], context.constructString(node, attributes['context']));
                        }
                    }
                    break;
                case speech_rule_1.ActionType.TEXT:
                    {
                        const xpath = attributes['span'];
                        const attrs = {};
                        if (xpath) {
                            const nodes = (0, xpath_util_1.evalXPath)(xpath, node);
                            if (nodes.length) {
                                attrs.extid = nodes[0].getAttribute('extid');
                            }
                        }
                        const str = context.constructString(node, content);
                        if (str || str === '') {
                            if (Array.isArray(str)) {
                                descrs = str.map(function (span) {
                                    return auditory_description_1.AuditoryDescription.create({ text: span.speech, attributes: span.attributes }, { adjust: true });
                                });
                            }
                            else {
                                descrs = [
                                    auditory_description_1.AuditoryDescription.create({ text: str, attributes: attrs }, { adjust: true })
                                ];
                            }
                        }
                    }
                    break;
                case speech_rule_1.ActionType.PERSONALITY:
                default:
                    descrs = [auditory_description_1.AuditoryDescription.create({ text: content })];
            }
            if (descrs[0] && !multi) {
                if (attributes['context']) {
                    descrs[0]['context'] =
                        context.constructString(node, attributes['context']) +
                            (descrs[0]['context'] || '');
                }
                if (attributes['annotation']) {
                    descrs[0]['annotation'] = attributes['annotation'];
                }
            }
            this.addLayout(descrs, attributes, multi);
            if (component.grammar) {
                grammar_1.Grammar.getInstance().popState();
            }
            result = result.concat(this.addPersonality_(descrs, attributes, multi, node));
            if (saveEngine) {
                engine_1.default.getInstance().setDynamicCstr(saveEngine);
            }
        }
        return result;
    }
    evaluateNodeList_(context, nodes, sepFunc, sepStr, ctxtFunc, ctxtStr) {
        if (!nodes.length) {
            return [];
        }
        const sep = sepStr || '';
        const cont = ctxtStr || '';
        const cFunc = context.contextFunctions.lookup(ctxtFunc);
        const ctxtClosure = cFunc
            ? cFunc(nodes, cont)
            : function () {
                return cont;
            };
        const sFunc = context.contextFunctions.lookup(sepFunc);
        const sepClosure = sFunc
            ? sFunc(nodes, sep)
            : function () {
                return [
                    auditory_description_1.AuditoryDescription.create({ text: sep }, { translate: true })
                ];
            };
        let result = [];
        for (let i = 0, node; (node = nodes[i]); i++) {
            const descrs = this.evaluateTree_(node);
            if (descrs.length > 0) {
                descrs[0]['context'] = ctxtClosure() + (descrs[0]['context'] || '');
                result = result.concat(descrs);
                if (i < nodes.length - 1) {
                    const text = sepClosure();
                    result = result.concat(text);
                }
            }
        }
        return result;
    }
    addLayout(descrs, props, _multi) {
        const layout = props.layout;
        if (!layout) {
            return;
        }
        if (layout.match(/^begin/)) {
            descrs.unshift(new auditory_description_1.AuditoryDescription({ text: '', layout: layout }));
            return;
        }
        if (layout.match(/^end/)) {
            descrs.push(new auditory_description_1.AuditoryDescription({ text: '', layout: layout }));
            return;
        }
        descrs.unshift(new auditory_description_1.AuditoryDescription({ text: '', layout: `begin${layout}` }));
        descrs.push(new auditory_description_1.AuditoryDescription({ text: '', layout: `end${layout}` }));
    }
    addPersonality_(descrs, props, multi, node) {
        const personality = {};
        let pause = null;
        for (const key of EngineConst.personalityPropList) {
            const value = props[key];
            if (typeof value === 'undefined') {
                continue;
            }
            const numeral = parseFloat(value);
            const realValue = isNaN(numeral)
                ? value.charAt(0) === '"'
                    ? value.slice(1, -1)
                    : value
                : numeral;
            if (key === EngineConst.personalityProps.PAUSE) {
                pause = realValue;
            }
            else {
                personality[key] = realValue;
            }
        }
        for (let i = 0, descr; (descr = descrs[i]); i++) {
            this.addRelativePersonality_(descr, personality);
            this.addExternalAttributes_(descr, node);
        }
        if (multi && descrs.length) {
            delete descrs[descrs.length - 1].personality[EngineConst.personalityProps.JOIN];
        }
        if (pause && descrs.length) {
            const last = descrs[descrs.length - 1];
            if (last.text || Object.keys(last.personality).length) {
                descrs.push(auditory_description_1.AuditoryDescription.create({
                    text: '',
                    personality: { pause: pause }
                }));
            }
            else {
                last.personality[EngineConst.personalityProps.PAUSE] = pause;
            }
        }
        return descrs;
    }
    addExternalAttributes_(descr, node) {
        if (node.hasAttributes()) {
            const attrs = node.attributes;
            for (let i = attrs.length - 1; i >= 0; i--) {
                const key = attrs[i].name;
                if (!descr.attributes[key] && key.match(/^ext/)) {
                    descr.attributes[key] = attrs[i].value;
                }
            }
        }
    }
    addRelativePersonality_(descr, personality) {
        if (!descr['personality']) {
            descr['personality'] = personality;
            return descr;
        }
        const descrPersonality = descr['personality'];
        for (const p in personality) {
            if (descrPersonality[p] &&
                typeof descrPersonality[p] == 'number' &&
                typeof personality[p] == 'number') {
                descrPersonality[p] = descrPersonality[p] + personality[p];
            }
            else if (!descrPersonality[p]) {
                descrPersonality[p] = personality[p];
            }
        }
        return descr;
    }
    updateConstraint_() {
        const dynamic = engine_1.default.getInstance().dynamicCstr;
        const strict = engine_1.default.getInstance().strict;
        const trie = this.trie;
        const props = {};
        let locale = dynamic.getValue(dynamic_cstr_1.Axis.LOCALE);
        let modality = dynamic.getValue(dynamic_cstr_1.Axis.MODALITY);
        let domain = dynamic.getValue(dynamic_cstr_1.Axis.DOMAIN);
        if (!trie.hasSubtrie([locale, modality, domain])) {
            domain = dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.DOMAIN];
            if (!trie.hasSubtrie([locale, modality, domain])) {
                modality = dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.MODALITY];
                if (!trie.hasSubtrie([locale, modality, domain])) {
                    locale = dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.LOCALE];
                }
            }
        }
        props[dynamic_cstr_1.Axis.LOCALE] = [locale];
        props[dynamic_cstr_1.Axis.MODALITY] = [
            modality !== 'summary'
                ? modality
                : dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.MODALITY]
        ];
        props[dynamic_cstr_1.Axis.DOMAIN] = [
            modality !== 'speech' ? dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.DOMAIN] : domain
        ];
        const order = dynamic.getOrder();
        for (let i = 0, axis; (axis = order[i]); i++) {
            if (!props[axis]) {
                const value = dynamic.getValue(axis);
                const valueSet = this.makeSet_(value, dynamic.preference);
                const def = dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[axis];
                if (!strict && value !== def) {
                    valueSet.push(def);
                }
                props[axis] = valueSet;
            }
        }
        dynamic.updateProperties(props);
    }
    makeSet_(value, preferences) {
        if (!preferences || !Object.keys(preferences).length) {
            return [value];
        }
        return value.split(':');
    }
    lookupRule(node, dynamic) {
        if (!node ||
            (node.nodeType !== DomUtil.NodeType.ELEMENT_NODE &&
                node.nodeType !== DomUtil.NodeType.TEXT_NODE)) {
            return null;
        }
        const matchingRules = this.lookupRules(node, dynamic);
        return matchingRules.length > 0
            ? this.pickMostConstraint_(dynamic, matchingRules)
            : null;
    }
    lookupRules(node, dynamic) {
        return this.trie.lookupRules(node, dynamic.allProperties());
    }
    pickMostConstraint_(_dynamic, rules) {
        const comparator = engine_1.default.getInstance().comparator;
        rules.sort(function (r1, r2) {
            return (comparator.compare(r1.dynamicCstr, r2.dynamicCstr) ||
                r2.precondition.priority - r1.precondition.priority ||
                r2.precondition.constraints.length -
                    r1.precondition.constraints.length ||
                r2.precondition.rank - r1.precondition.rank);
        });
        debugger_1.Debugger.getInstance().generateOutput((() => {
            return rules.map((x) => x.name + '(' + x.dynamicCstr.toString() + ')');
        }).bind(this));
        return rules[0];
    }
}
exports.SpeechRuleEngine = SpeechRuleEngine;
const stores = new Map();
function getStore(modality) {
    if (modality === 'braille') {
        return new braille_store_1.BrailleStore();
    }
    return new math_store_1.MathStore();
}
function storeFactory(set) {
    const name = `${set.locale}.${set.modality}.${set.domain}`;
    if (set.kind === 'actions') {
        const store = stores.get(name);
        store.parse(set);
        return store;
    }
    SpeechRuleStores.init();
    if (set && !set.functions) {
        set.functions = SpeechRules.getStore(set.locale, set.modality, set.domain);
    }
    const store = getStore(set.modality);
    stores.set(name, store);
    if (set.inherits) {
        store.inherits = stores.get(`${set.inherits}.${set.modality}.${set.domain}`);
    }
    store.parse(set);
    store.initialize();
    return store;
}
exports.storeFactory = storeFactory;
engine_1.default.nodeEvaluator = SpeechRuleEngine.getInstance().evaluateNode.bind(SpeechRuleEngine.getInstance());


/***/ }),

/***/ 3686:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CustomGenerators = exports.ContextFunctions = exports.CustomStrings = exports.CustomQueries = void 0;
class FunctionsStore {
    constructor(prefix, store) {
        this.prefix = prefix;
        this.store = store;
    }
    add(name, func) {
        if (this.checkCustomFunctionSyntax_(name)) {
            this.store[name] = func;
        }
    }
    addStore(store) {
        const keys = Object.keys(store.store);
        for (let i = 0, key; (key = keys[i]); i++) {
            this.add(key, store.store[key]);
        }
    }
    lookup(name) {
        return this.store[name];
    }
    checkCustomFunctionSyntax_(name) {
        const reg = new RegExp('^' + this.prefix);
        if (!name.match(reg)) {
            console.error('FunctionError: Invalid function name. Expected prefix ' + this.prefix);
            return false;
        }
        return true;
    }
}
class CustomQueries extends FunctionsStore {
    constructor() {
        const store = {};
        super('CQF', store);
    }
}
exports.CustomQueries = CustomQueries;
class CustomStrings extends FunctionsStore {
    constructor() {
        const store = {};
        super('CSF', store);
    }
}
exports.CustomStrings = CustomStrings;
class ContextFunctions extends FunctionsStore {
    constructor() {
        const store = {};
        super('CTF', store);
    }
}
exports.ContextFunctions = ContextFunctions;
class CustomGenerators extends FunctionsStore {
    constructor() {
        const store = {};
        super('CGF', store);
    }
}
exports.CustomGenerators = CustomGenerators;


/***/ }),

/***/ 931:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.contentIterator = exports.pauseSeparator = exports.nodeCounter = void 0;
const auditory_description_1 = __webpack_require__(4148);
const XpathUtil = __webpack_require__(5024);
const engine_1 = __webpack_require__(4886);
function nodeCounter(nodes, context) {
    const localLength = nodes.length;
    let localCounter = 0;
    let localContext = context;
    if (!context) {
        localContext = '';
    }
    return function () {
        if (localCounter < localLength) {
            localCounter += 1;
        }
        return localContext + ' ' + localCounter;
    };
}
exports.nodeCounter = nodeCounter;
function pauseSeparator(_nodes, context) {
    const numeral = parseFloat(context);
    const value = isNaN(numeral) ? context : numeral;
    return function () {
        return [
            auditory_description_1.AuditoryDescription.create({
                text: '',
                personality: { pause: value }
            })
        ];
    };
}
exports.pauseSeparator = pauseSeparator;
function contentIterator(nodes, context) {
    let contentNodes;
    if (nodes.length > 0) {
        contentNodes = XpathUtil.evalXPath('../../content/*', nodes[0]);
    }
    else {
        contentNodes = [];
    }
    return function () {
        const content = contentNodes.shift();
        const contextDescr = context
            ? [auditory_description_1.AuditoryDescription.create({ text: context }, { translate: true })]
            : [];
        if (!content) {
            return contextDescr;
        }
        const descrs = engine_1.default.evaluateNode(content);
        return contextDescr.concat(descrs);
    };
}
exports.contentIterator = contentIterator;


/***/ }),

/***/ 1939:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.getTreeFromString = exports.getTree = exports.xmlTree = void 0;
const DomUtil = __webpack_require__(6671);
const semantic_tree_1 = __webpack_require__(1784);
function xmlTree(mml) {
    return getTree(mml).xml();
}
exports.xmlTree = xmlTree;
function getTree(mml) {
    return new semantic_tree_1.SemanticTree(mml);
}
exports.getTree = getTree;
function getTreeFromString(expr) {
    const mml = DomUtil.parseInput(expr);
    return getTree(mml);
}
exports.getTreeFromString = getTreeFromString;


/***/ }),

/***/ 4036:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.annotate = exports.activate = exports.register = exports.visitors = exports.annotators = void 0;
const semantic_annotator_1 = __webpack_require__(241);
exports.annotators = new Map();
exports.visitors = new Map();
function register(annotator) {
    const name = annotator.domain + ':' + annotator.name;
    annotator instanceof semantic_annotator_1.SemanticAnnotator
        ? exports.annotators.set(name, annotator)
        : exports.visitors.set(name, annotator);
}
exports.register = register;
function activate(domain, name) {
    const key = domain + ':' + name;
    const annotator = exports.annotators.get(key) || exports.visitors.get(key);
    if (annotator) {
        annotator.active = true;
    }
}
exports.activate = activate;
function annotate(node) {
    for (const annotator of exports.annotators.values()) {
        if (annotator.active) {
            annotator.annotate(node);
        }
    }
    for (const visitor of exports.visitors.values()) {
        if (visitor.active) {
            visitor.visit(node, Object.assign({}, visitor.def));
        }
    }
}
exports.annotate = annotate;


/***/ }),

/***/ 241:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticVisitor = exports.SemanticAnnotator = void 0;
class SemanticAnnotator {
    constructor(domain, name, func) {
        this.domain = domain;
        this.name = name;
        this.func = func;
        this.active = false;
    }
    annotate(node) {
        node.childNodes.forEach(this.annotate.bind(this));
        node.addAnnotation(this.domain, this.func(node));
    }
}
exports.SemanticAnnotator = SemanticAnnotator;
class SemanticVisitor {
    constructor(domain, name, func, def = {}) {
        this.domain = domain;
        this.name = name;
        this.func = func;
        this.def = def;
        this.active = false;
    }
    visit(node, info) {
        let result = this.func(node, info);
        node.addAnnotation(this.domain, result[0]);
        for (let i = 0, child; (child = node.childNodes[i]); i++) {
            result = this.visit(child, result[1]);
        }
        return result;
    }
}
exports.SemanticVisitor = SemanticVisitor;


/***/ }),

/***/ 4020:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.lookupSecondary = exports.isEmbellishedType = exports.isMatchingFence = exports.functionApplication = exports.invisibleComma = exports.invisiblePlus = exports.invisibleTimes = exports.lookupMeaning = exports.lookupRole = exports.lookupType = exports.equal = exports.allLettersRegExp = void 0;
const generalPunctuations = [
    '!',
    '"',
    '#',
    '%',
    '&',
    ';',
    '?',
    '@',
    '\\',
    '¡',
    '§',
    '¶',
    '¿',
    '‗',
    '†',
    '‡',
    '•',
    '‣',
    '․',
    '‥',
    '‧',
    '‰',
    '‱',
    '‸',
    '※',
    '‼',
    '‽',
    '‾',
    '⁁',
    '⁂',
    '⁃',
    '⁇',
    '⁈',
    '⁉',
    '⁋',
    '⁌',
    '⁍',
    '⁎',
    '⁏',
    '⁐',
    '⁑',
    '⁓',
    '⁕',
    '⁖',
    '⁘',
    '⁙',
    '⁚',
    '⁛',
    '⁜',
    '⁝',
    '⁞',
    '︐',
    '︔',
    '︕',
    '︖',
    '︰',
    '﹅',
    '﹆',
    '﹉',
    '﹊',
    '﹋',
    '﹌',
    '﹔',
    '﹖',
    '﹗',
    '﹟',
    '﹠',
    '﹡',
    '﹨',
    '﹪',
    '﹫',
    '！',
    '＂',
    '＃',
    '％',
    '＆',
    '＇',
    '＊',
    '／',
    '；',
    '？',
    '＠',
    '＼'
];
const colons = ['︓', ':', '：', '﹕'];
const invisibleComma_ = String.fromCodePoint(0x2063);
const commas = ['，', '﹐', ',', invisibleComma_];
const ellipses = ['…', '⋮', '⋯', '⋰', '⋱', '︙'];
const fullStops = ['.', '﹒', '．'];
const dashes = [
    '¯',
    '‒',
    '–',
    '—',
    '―',
    '﹘',
    '-',
    '⁻',
    '₋',
    '−',
    '➖',
    '﹣',
    '－',
    '‐',
    '‑',
    '‾',
    '_'
];
const tildes = ['~', '̃', '∼', '˜', '∽', '˷', '̴', '̰'];
const primes = ["'", '′', '″', '‴', '‵', '‶', '‷', '⁗', 'ʹ', 'ʺ'];
const degrees = ['°'];
const openClosePairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '\u2045': '⁆',
    '\u2329': '〉',
    '\u2768': '❩',
    '\u276a': '❫',
    '\u276c': '❭',
    '\u276e': '❯',
    '\u2770': '❱',
    '\u2772': '❳',
    '\u2774': '❵',
    '\u27c5': '⟆',
    '\u27e6': '⟧',
    '\u27e8': '⟩',
    '\u27ea': '⟫',
    '\u27ec': '⟭',
    '\u27ee': '⟯',
    '\u2983': '⦄',
    '\u2985': '⦆',
    '\u2987': '⦈',
    '\u2989': '⦊',
    '\u298b': '⦌',
    '\u298d': '⦎',
    '\u298f': '⦐',
    '\u2991': '⦒',
    '\u2993': '⦔',
    '\u2995': '⦖',
    '\u2997': '⦘',
    '\u29d8': '⧙',
    '\u29da': '⧛',
    '\u29fc': '⧽',
    '\u2e22': '⸣',
    '\u2e24': '⸥',
    '\u2e26': '⸧',
    '\u2e28': '⸩',
    '\u3008': '〉',
    '\u300a': '》',
    '\u300c': '」',
    '\u300e': '』',
    '\u3010': '】',
    '\u3014': '〕',
    '\u3016': '〗',
    '\u3018': '〙',
    '\u301a': '〛',
    '\u301d': '〞',
    '\ufd3e': '﴿',
    '\ufe17': '︘',
    '\ufe59': '﹚',
    '\ufe5b': '﹜',
    '\ufe5d': '﹞',
    '\uff08': '）',
    '\uff3b': '］',
    '\uff5b': '｝',
    '\uff5f': '｠',
    '\uff62': '｣',
    '\u2308': '⌉',
    '\u230a': '⌋',
    '\u230c': '⌍',
    '\u230e': '⌏',
    '\u231c': '⌝',
    '\u231e': '⌟',
    '\u239b': '⎞',
    '\u239c': '⎟',
    '\u239d': '⎠',
    '\u23a1': '⎤',
    '\u23a2': '⎥',
    '\u23a3': '⎦',
    '\u23a7': '⎫',
    '\u23a8': '⎬',
    '\u23a9': '⎭',
    '\u23b0': '⎱',
    '\u23b8': '⎹'
};
const topBottomPairs = {
    '\u23b4': '⎵',
    '\u23dc': '⏝',
    '\u23de': '⏟',
    '\u23e0': '⏡',
    '\ufe35': '︶',
    '\ufe37': '︸',
    '\ufe39': '︺',
    '\ufe3b': '︼',
    '\ufe3d': '︾',
    '\ufe3f': '﹀',
    '\ufe41': '﹂',
    '\ufe43': '﹄',
    '\ufe47': '﹈'
};
const leftFences = Object.keys(openClosePairs);
const rightFences = Object.values(openClosePairs);
rightFences.push('〟');
const topFences = Object.keys(topBottomPairs);
const bottomFences = Object.values(topBottomPairs);
const neutralFences = [
    '|',
    '¦',
    '∣',
    '⏐',
    '⎸',
    '⎹',
    '❘',
    '｜',
    '￤',
    '︱',
    '︲'
];
const metricFences = ['‖', '∥', '⦀', '⫴'];
const capitalLatin = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
];
const smallLatin = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    'ı',
    'ȷ'
];
const capitalLatinFullWidth = [
    'Ａ',
    'Ｂ',
    'Ｃ',
    'Ｄ',
    'Ｅ',
    'Ｆ',
    'Ｇ',
    'Ｈ',
    'Ｉ',
    'Ｊ',
    'Ｋ',
    'Ｌ',
    'Ｍ',
    'Ｎ',
    'Ｏ',
    'Ｐ',
    'Ｑ',
    'Ｒ',
    'Ｓ',
    'Ｔ',
    'Ｕ',
    'Ｖ',
    'Ｗ',
    'Ｘ',
    'Ｙ',
    'Ｚ'
];
const smallLatinFullWidth = [
    'ａ',
    'ｂ',
    'ｃ',
    'ｄ',
    'ｅ',
    'ｆ',
    'ｇ',
    'ｈ',
    'ｉ',
    'ｊ',
    'ｋ',
    'ｌ',
    'ｍ',
    'ｎ',
    'ｏ',
    'ｐ',
    'ｑ',
    'ｒ',
    'ｓ',
    'ｔ',
    'ｕ',
    'ｖ',
    'ｗ',
    'ｘ',
    'ｙ',
    'ｚ'
];
const capitalLatinBold = [
    '𝐀',
    '𝐁',
    '𝐂',
    '𝐃',
    '𝐄',
    '𝐅',
    '𝐆',
    '𝐇',
    '𝐈',
    '𝐉',
    '𝐊',
    '𝐋',
    '𝐌',
    '𝐍',
    '𝐎',
    '𝐏',
    '𝐐',
    '𝐑',
    '𝐒',
    '𝐓',
    '𝐔',
    '𝐕',
    '𝐖',
    '𝐗',
    '𝐘',
    '𝐙'
];
const smallLatinBold = [
    '𝐚',
    '𝐛',
    '𝐜',
    '𝐝',
    '𝐞',
    '𝐟',
    '𝐠',
    '𝐡',
    '𝐢',
    '𝐣',
    '𝐤',
    '𝐥',
    '𝐦',
    '𝐧',
    '𝐨',
    '𝐩',
    '𝐪',
    '𝐫',
    '𝐬',
    '𝐭',
    '𝐮',
    '𝐯',
    '𝐰',
    '𝐱',
    '𝐲',
    '𝐳'
];
const capitalLatinItalic = [
    '𝐴',
    '𝐵',
    '𝐶',
    '𝐷',
    '𝐸',
    '𝐹',
    '𝐺',
    '𝐻',
    '𝐼',
    '𝐽',
    '𝐾',
    '𝐿',
    '𝑀',
    '𝑁',
    '𝑂',
    '𝑃',
    '𝑄',
    '𝑅',
    '𝑆',
    '𝑇',
    '𝑈',
    '𝑉',
    '𝑊',
    '𝑋',
    '𝑌',
    '𝑍'
];
const smallLatinItalic = [
    '𝑎',
    '𝑏',
    '𝑐',
    '𝑑',
    '𝑒',
    '𝑓',
    '𝑔',
    'ℎ',
    '𝑖',
    '𝑗',
    '𝑘',
    '𝑙',
    '𝑚',
    '𝑛',
    '𝑜',
    '𝑝',
    '𝑞',
    '𝑟',
    '𝑠',
    '𝑡',
    '𝑢',
    '𝑣',
    '𝑤',
    '𝑥',
    '𝑦',
    '𝑧',
    '𝚤',
    '𝚥'
];
const capitalLatinBoldItalic = [
    '𝑨',
    '𝑩',
    '𝑪',
    '𝑫',
    '𝑬',
    '𝑭',
    '𝑮',
    '𝑯',
    '𝑰',
    '𝑱',
    '𝑲',
    '𝑳',
    '𝑴',
    '𝑵',
    '𝑶',
    '𝑷',
    '𝑸',
    '𝑹',
    '𝑺',
    '𝑻',
    '𝑼',
    '𝑽',
    '𝑾',
    '𝑿',
    '𝒀',
    '𝒁'
];
const smallLatinBoldItalic = [
    '𝒂',
    '𝒃',
    '𝒄',
    '𝒅',
    '𝒆',
    '𝒇',
    '𝒈',
    '𝒉',
    '𝒊',
    '𝒋',
    '𝒌',
    '𝒍',
    '𝒎',
    '𝒏',
    '𝒐',
    '𝒑',
    '𝒒',
    '𝒓',
    '𝒔',
    '𝒕',
    '𝒖',
    '𝒗',
    '𝒘',
    '𝒙',
    '𝒚',
    '𝒛'
];
const capitalLatinScript = [
    '𝒜',
    'ℬ',
    '𝒞',
    '𝒟',
    'ℰ',
    'ℱ',
    '𝒢',
    'ℋ',
    'ℐ',
    '𝒥',
    '𝒦',
    'ℒ',
    'ℳ',
    '𝒩',
    '𝒪',
    '𝒫',
    '𝒬',
    'ℛ',
    '𝒮',
    '𝒯',
    '𝒰',
    '𝒱',
    '𝒲',
    '𝒳',
    '𝒴',
    '𝒵',
    '℘'
];
const smallLatinScript = [
    '𝒶',
    '𝒷',
    '𝒸',
    '𝒹',
    'ℯ',
    '𝒻',
    'ℊ',
    '𝒽',
    '𝒾',
    '𝒿',
    '𝓀',
    '𝓁',
    '𝓂',
    '𝓃',
    'ℴ',
    '𝓅',
    '𝓆',
    '𝓇',
    '𝓈',
    '𝓉',
    '𝓊',
    '𝓋',
    '𝓌',
    '𝓍',
    '𝓎',
    '𝓏',
    'ℓ'
];
const capitalLatinBoldScript = [
    '𝓐',
    '𝓑',
    '𝓒',
    '𝓓',
    '𝓔',
    '𝓕',
    '𝓖',
    '𝓗',
    '𝓘',
    '𝓙',
    '𝓚',
    '𝓛',
    '𝓜',
    '𝓝',
    '𝓞',
    '𝓟',
    '𝓠',
    '𝓡',
    '𝓢',
    '𝓣',
    '𝓤',
    '𝓥',
    '𝓦',
    '𝓧',
    '𝓨',
    '𝓩'
];
const smallLatinBoldScript = [
    '𝓪',
    '𝓫',
    '𝓬',
    '𝓭',
    '𝓮',
    '𝓯',
    '𝓰',
    '𝓱',
    '𝓲',
    '𝓳',
    '𝓴',
    '𝓵',
    '𝓶',
    '𝓷',
    '𝓸',
    '𝓹',
    '𝓺',
    '𝓻',
    '𝓼',
    '𝓽',
    '𝓾',
    '𝓿',
    '𝔀',
    '𝔁',
    '𝔂',
    '𝔃'
];
const capitalLatinFraktur = [
    '𝔄',
    '𝔅',
    'ℭ',
    '𝔇',
    '𝔈',
    '𝔉',
    '𝔊',
    'ℌ',
    'ℑ',
    '𝔍',
    '𝔎',
    '𝔏',
    '𝔐',
    '𝔑',
    '𝔒',
    '𝔓',
    '𝔔',
    'ℜ',
    '𝔖',
    '𝔗',
    '𝔘',
    '𝔙',
    '𝔚',
    '𝔛',
    '𝔜',
    'ℨ'
];
const smallLatinFraktur = [
    '𝔞',
    '𝔟',
    '𝔠',
    '𝔡',
    '𝔢',
    '𝔣',
    '𝔤',
    '𝔥',
    '𝔦',
    '𝔧',
    '𝔨',
    '𝔩',
    '𝔪',
    '𝔫',
    '𝔬',
    '𝔭',
    '𝔮',
    '𝔯',
    '𝔰',
    '𝔱',
    '𝔲',
    '𝔳',
    '𝔴',
    '𝔵',
    '𝔶',
    '𝔷'
];
const capitalLatinDoubleStruck = [
    '𝔸',
    '𝔹',
    'ℂ',
    '𝔻',
    '𝔼',
    '𝔽',
    '𝔾',
    'ℍ',
    '𝕀',
    '𝕁',
    '𝕂',
    '𝕃',
    '𝕄',
    'ℕ',
    '𝕆',
    'ℙ',
    'ℚ',
    'ℝ',
    '𝕊',
    '𝕋',
    '𝕌',
    '𝕍',
    '𝕎',
    '𝕏',
    '𝕐',
    'ℤ'
];
const smallLatinDoubleStruck = [
    '𝕒',
    '𝕓',
    '𝕔',
    '𝕕',
    '𝕖',
    '𝕗',
    '𝕘',
    '𝕙',
    '𝕚',
    '𝕛',
    '𝕜',
    '𝕝',
    '𝕞',
    '𝕟',
    '𝕠',
    '𝕡',
    '𝕢',
    '𝕣',
    '𝕤',
    '𝕥',
    '𝕦',
    '𝕧',
    '𝕨',
    '𝕩',
    '𝕪',
    '𝕫'
];
const capitalLatinBoldFraktur = [
    '𝕬',
    '𝕭',
    '𝕮',
    '𝕯',
    '𝕰',
    '𝕱',
    '𝕲',
    '𝕳',
    '𝕴',
    '𝕵',
    '𝕶',
    '𝕷',
    '𝕸',
    '𝕹',
    '𝕺',
    '𝕻',
    '𝕼',
    '𝕽',
    '𝕾',
    '𝕿',
    '𝖀',
    '𝖁',
    '𝖂',
    '𝖃',
    '𝖄',
    '𝖅'
];
const smallLatinBoldFraktur = [
    '𝖆',
    '𝖇',
    '𝖈',
    '𝖉',
    '𝖊',
    '𝖋',
    '𝖌',
    '𝖍',
    '𝖎',
    '𝖏',
    '𝖐',
    '𝖑',
    '𝖒',
    '𝖓',
    '𝖔',
    '𝖕',
    '𝖖',
    '𝖗',
    '𝖘',
    '𝖙',
    '𝖚',
    '𝖛',
    '𝖜',
    '𝖝',
    '𝖞',
    '𝖟'
];
const capitalLatinSansSerif = [
    '𝖠',
    '𝖡',
    '𝖢',
    '𝖣',
    '𝖤',
    '𝖥',
    '𝖦',
    '𝖧',
    '𝖨',
    '𝖩',
    '𝖪',
    '𝖫',
    '𝖬',
    '𝖭',
    '𝖮',
    '𝖯',
    '𝖰',
    '𝖱',
    '𝖲',
    '𝖳',
    '𝖴',
    '𝖵',
    '𝖶',
    '𝖷',
    '𝖸',
    '𝖹'
];
const smallLatinSansSerif = [
    '𝖺',
    '𝖻',
    '𝖼',
    '𝖽',
    '𝖾',
    '𝖿',
    '𝗀',
    '𝗁',
    '𝗂',
    '𝗃',
    '𝗄',
    '𝗅',
    '𝗆',
    '𝗇',
    '𝗈',
    '𝗉',
    '𝗊',
    '𝗋',
    '𝗌',
    '𝗍',
    '𝗎',
    '𝗏',
    '𝗐',
    '𝗑',
    '𝗒',
    '𝗓'
];
const capitalLatinSansSerifBold = [
    '𝗔',
    '𝗕',
    '𝗖',
    '𝗗',
    '𝗘',
    '𝗙',
    '𝗚',
    '𝗛',
    '𝗜',
    '𝗝',
    '𝗞',
    '𝗟',
    '𝗠',
    '𝗡',
    '𝗢',
    '𝗣',
    '𝗤',
    '𝗥',
    '𝗦',
    '𝗧',
    '𝗨',
    '𝗩',
    '𝗪',
    '𝗫',
    '𝗬',
    '𝗭'
];
const smallLatinSansSerifBold = [
    '𝗮',
    '𝗯',
    '𝗰',
    '𝗱',
    '𝗲',
    '𝗳',
    '𝗴',
    '𝗵',
    '𝗶',
    '𝗷',
    '𝗸',
    '𝗹',
    '𝗺',
    '𝗻',
    '𝗼',
    '𝗽',
    '𝗾',
    '𝗿',
    '𝘀',
    '𝘁',
    '𝘂',
    '𝘃',
    '𝘄',
    '𝘅',
    '𝘆',
    '𝘇'
];
const capitalLatinSansSerifItalic = [
    '𝘈',
    '𝘉',
    '𝘊',
    '𝘋',
    '𝘌',
    '𝘍',
    '𝘎',
    '𝘏',
    '𝘐',
    '𝘑',
    '𝘒',
    '𝘓',
    '𝘔',
    '𝘕',
    '𝘖',
    '𝘗',
    '𝘘',
    '𝘙',
    '𝘚',
    '𝘛',
    '𝘜',
    '𝘝',
    '𝘞',
    '𝘟',
    '𝘠',
    '𝘡'
];
const smallLatinSansSerifItalic = [
    '𝘢',
    '𝘣',
    '𝘤',
    '𝘥',
    '𝘦',
    '𝘧',
    '𝘨',
    '𝘩',
    '𝘪',
    '𝘫',
    '𝘬',
    '𝘭',
    '𝘮',
    '𝘯',
    '𝘰',
    '𝘱',
    '𝘲',
    '𝘳',
    '𝘴',
    '𝘵',
    '𝘶',
    '𝘷',
    '𝘸',
    '𝘹',
    '𝘺',
    '𝘻'
];
const capitalLatinSansSerifBoldItalic = [
    '𝘼',
    '𝘽',
    '𝘾',
    '𝘿',
    '𝙀',
    '𝙁',
    '𝙂',
    '𝙃',
    '𝙄',
    '𝙅',
    '𝙆',
    '𝙇',
    '𝙈',
    '𝙉',
    '𝙊',
    '𝙋',
    '𝙌',
    '𝙍',
    '𝙎',
    '𝙏',
    '𝙐',
    '𝙑',
    '𝙒',
    '𝙓',
    '𝙔',
    '𝙕'
];
const smallLatinSansSerifBoldItalic = [
    '𝙖',
    '𝙗',
    '𝙘',
    '𝙙',
    '𝙚',
    '𝙛',
    '𝙜',
    '𝙝',
    '𝙞',
    '𝙟',
    '𝙠',
    '𝙡',
    '𝙢',
    '𝙣',
    '𝙤',
    '𝙥',
    '𝙦',
    '𝙧',
    '𝙨',
    '𝙩',
    '𝙪',
    '𝙫',
    '𝙬',
    '𝙭',
    '𝙮',
    '𝙯'
];
const capitalLatinMonospace = [
    '𝙰',
    '𝙱',
    '𝙲',
    '𝙳',
    '𝙴',
    '𝙵',
    '𝙶',
    '𝙷',
    '𝙸',
    '𝙹',
    '𝙺',
    '𝙻',
    '𝙼',
    '𝙽',
    '𝙾',
    '𝙿',
    '𝚀',
    '𝚁',
    '𝚂',
    '𝚃',
    '𝚄',
    '𝚅',
    '𝚆',
    '𝚇',
    '𝚈',
    '𝚉'
];
const smallLatinMonospace = [
    '𝚊',
    '𝚋',
    '𝚌',
    '𝚍',
    '𝚎',
    '𝚏',
    '𝚐',
    '𝚑',
    '𝚒',
    '𝚓',
    '𝚔',
    '𝚕',
    '𝚖',
    '𝚗',
    '𝚘',
    '𝚙',
    '𝚚',
    '𝚛',
    '𝚜',
    '𝚝',
    '𝚞',
    '𝚟',
    '𝚠',
    '𝚡',
    '𝚢',
    '𝚣'
];
const latinDoubleStruckItalic = ['ⅅ', 'ⅆ', 'ⅇ', 'ⅈ', 'ⅉ'];
const capitalGreek = [
    'Α',
    'Β',
    'Γ',
    'Δ',
    'Ε',
    'Ζ',
    'Η',
    'Θ',
    'Ι',
    'Κ',
    'Λ',
    'Μ',
    'Ν',
    'Ξ',
    'Ο',
    'Π',
    'Ρ',
    'Σ',
    'Τ',
    'Υ',
    'Φ',
    'Χ',
    'Ψ',
    'Ω'
];
const smallGreek = [
    'α',
    'β',
    'γ',
    'δ',
    'ε',
    'ζ',
    'η',
    'θ',
    'ι',
    'κ',
    'λ',
    'μ',
    'ν',
    'ξ',
    'ο',
    'π',
    'ρ',
    'ς',
    'σ',
    'τ',
    'υ',
    'φ',
    'χ',
    'ψ',
    'ω'
];
const capitalGreekBold = [
    '𝚨',
    '𝚩',
    '𝚪',
    '𝚫',
    '𝚬',
    '𝚭',
    '𝚮',
    '𝚯',
    '𝚰',
    '𝚱',
    '𝚲',
    '𝚳',
    '𝚴',
    '𝚵',
    '𝚶',
    '𝚷',
    '𝚸',
    '𝚺',
    '𝚻',
    '𝚼',
    '𝚽',
    '𝚾',
    '𝚿',
    '𝛀'
];
const smallGreekBold = [
    '𝛂',
    '𝛃',
    '𝛄',
    '𝛅',
    '𝛆',
    '𝛇',
    '𝛈',
    '𝛉',
    '𝛊',
    '𝛋',
    '𝛌',
    '𝛍',
    '𝛎',
    '𝛏',
    '𝛐',
    '𝛑',
    '𝛒',
    '𝛓',
    '𝛔',
    '𝛕',
    '𝛖',
    '𝛗',
    '𝛘',
    '𝛙',
    '𝛚'
];
const capitalGreekItalic = [
    '𝛢',
    '𝛣',
    '𝛤',
    '𝛥',
    '𝛦',
    '𝛧',
    '𝛨',
    '𝛩',
    '𝛪',
    '𝛫',
    '𝛬',
    '𝛭',
    '𝛮',
    '𝛯',
    '𝛰',
    '𝛱',
    '𝛲',
    '𝛴',
    '𝛵',
    '𝛶',
    '𝛷',
    '𝛸',
    '𝛹',
    '𝛺'
];
const smallGreekItalic = [
    '𝛼',
    '𝛽',
    '𝛾',
    '𝛿',
    '𝜀',
    '𝜁',
    '𝜂',
    '𝜃',
    '𝜄',
    '𝜅',
    '𝜆',
    '𝜇',
    '𝜈',
    '𝜉',
    '𝜊',
    '𝜋',
    '𝜌',
    '𝜍',
    '𝜎',
    '𝜏',
    '𝜐',
    '𝜑',
    '𝜒',
    '𝜓',
    '𝜔'
];
const capitalGreekBoldItalic = [
    '𝜜',
    '𝜝',
    '𝜞',
    '𝜟',
    '𝜠',
    '𝜡',
    '𝜢',
    '𝜣',
    '𝜤',
    '𝜥',
    '𝜦',
    '𝜧',
    '𝜨',
    '𝜩',
    '𝜪',
    '𝜫',
    '𝜬',
    '𝜮',
    '𝜯',
    '𝜰',
    '𝜱',
    '𝜲',
    '𝜳',
    '𝜴'
];
const smallGreekBoldItalic = [
    '𝜶',
    '𝜷',
    '𝜸',
    '𝜹',
    '𝜺',
    '𝜻',
    '𝜼',
    '𝜽',
    '𝜾',
    '𝜿',
    '𝝀',
    '𝝁',
    '𝝂',
    '𝝃',
    '𝝄',
    '𝝅',
    '𝝆',
    '𝝇',
    '𝝈',
    '𝝉',
    '𝝊',
    '𝝋',
    '𝝌',
    '𝝍',
    '𝝎'
];
const capitalGreekSansSerifBold = [
    '𝝖',
    '𝝗',
    '𝝘',
    '𝝙',
    '𝝚',
    '𝝛',
    '𝝜',
    '𝝝',
    '𝝞',
    '𝝟',
    '𝝠',
    '𝝡',
    '𝝢',
    '𝝣',
    '𝝤',
    '𝝥',
    '𝝦',
    '𝝨',
    '𝝩',
    '𝝪',
    '𝝫',
    '𝝬',
    '𝝭',
    '𝝮'
];
const smallGreekSansSerifBold = [
    '𝝰',
    '𝝱',
    '𝝲',
    '𝝳',
    '𝝴',
    '𝝵',
    '𝝶',
    '𝝷',
    '𝝸',
    '𝝹',
    '𝝺',
    '𝝻',
    '𝝼',
    '𝝽',
    '𝝾',
    '𝝿',
    '𝞀',
    '𝞁',
    '𝞂',
    '𝞃',
    '𝞄',
    '𝞅',
    '𝞆',
    '𝞇',
    '𝞈'
];
const capitalGreekSansSerifBoldItalic = [
    '𝞐',
    '𝞑',
    '𝞒',
    '𝞓',
    '𝞔',
    '𝞕',
    '𝞖',
    '𝞗',
    '𝞘',
    '𝞙',
    '𝞚',
    '𝞛',
    '𝞜',
    '𝞝',
    '𝞞',
    '𝞟',
    '𝞠',
    '𝞢',
    '𝞣',
    '𝞤',
    '𝞥',
    '𝞦',
    '𝞧',
    '𝞨'
];
const smallGreekSansSerifBoldItalic = [
    '𝞪',
    '𝞫',
    '𝞬',
    '𝞭',
    '𝞮',
    '𝞯',
    '𝞰',
    '𝞱',
    '𝞲',
    '𝞳',
    '𝞴',
    '𝞵',
    '𝞶',
    '𝞷',
    '𝞸',
    '𝞹',
    '𝞺',
    '𝞻',
    '𝞼',
    '𝞽',
    '𝞾',
    '𝞿',
    '𝟀',
    '𝟁',
    '𝟂'
];
const greekDoubleStruck = ['ℼ', 'ℽ', 'ℾ', 'ℿ'];
const greekSpecial = [
    'ϐ',
    'ϑ',
    'ϕ',
    'ϖ',
    'ϗ',
    'ϰ',
    'ϱ',
    'ϵ',
    '϶',
    'ϴ'
];
const greekSpecialBold = ['𝛜', '𝛝', '𝛞', '𝛟', '𝛠', '𝛡'];
const greekSpecialItalic = ['𝜖', '𝜗', '𝜘', '𝜙', '𝜚', '𝜛'];
const greekSpecialSansSerifBold = ['𝞊', '𝞋', '𝞌', '𝞍', '𝞎', '𝞏'];
const hebrewLetters = ['ℵ', 'ℶ', 'ℷ', 'ℸ'];
const allLetters = capitalLatin.concat(smallLatin, capitalLatinFullWidth, smallLatinFullWidth, capitalLatinBold, smallLatinBold, capitalLatinItalic, capitalLatinBoldItalic, smallLatinBoldItalic, smallLatinItalic, capitalLatinScript, smallLatinScript, capitalLatinBoldScript, smallLatinBoldScript, capitalLatinFraktur, smallLatinFraktur, capitalLatinDoubleStruck, smallLatinDoubleStruck, capitalLatinBoldFraktur, smallLatinBoldFraktur, capitalLatinSansSerif, smallLatinSansSerif, capitalLatinSansSerifBold, smallLatinSansSerifBold, capitalLatinSansSerifItalic, smallLatinSansSerifItalic, capitalLatinSansSerifBoldItalic, smallLatinSansSerifBoldItalic, capitalLatinMonospace, smallLatinMonospace, latinDoubleStruckItalic, capitalGreek, smallGreek, capitalGreekBold, smallGreekBold, capitalGreekItalic, smallGreekItalic, capitalGreekBoldItalic, smallGreekBoldItalic, capitalGreekSansSerifBold, smallGreekSansSerifBold, greekDoubleStruck, greekSpecial, capitalGreekSansSerifBoldItalic, smallGreekSansSerifBoldItalic, greekSpecialBold, greekSpecialItalic, greekSpecialSansSerifBold, hebrewLetters);
exports.allLettersRegExp = new RegExp(allLetters.join('|'));
const additions = [
    '+',
    '±',
    '∓',
    '∔',
    '∧',
    '∨',
    '∩',
    '∪',
    '⊌',
    '⊍',
    '⊎',
    '⊓',
    '⊔',
    '⊝',
    '⊞',
    '⊤',
    '⊥',
    '⊺',
    '⊻',
    '⊼',
    '⋄',
    '⋎',
    '⋏',
    '⋒',
    '⋓',
    '⩞',
    '⊕',
    '⋔'
];
const invisiblePlus_ = String.fromCodePoint(0x2064);
additions.push(invisiblePlus_);
const multiplications = [
    '†',
    '‡',
    '∐',
    '∗',
    '∘',
    '∙',
    '≀',
    '⊚',
    '⊛',
    '⊠',
    '⊡',
    '⋅',
    '⋆',
    '⋇',
    '⋈',
    '⋉',
    '⋊',
    '⋋',
    '⋌',
    '○',
    '·',
    '*',
    '⊗',
    '⊙'
];
const invisibleTimes_ = String.fromCodePoint(0x2062);
multiplications.push(invisibleTimes_);
const subtractions = [
    '¯',
    '-',
    '⁒',
    '⁻',
    '₋',
    '−',
    '∖',
    '∸',
    '≂',
    '⊖',
    '⊟',
    '➖',
    '⨩',
    '⨪',
    '⨫',
    '⨬',
    '⨺',
    '⩁',
    '﹣',
    '－',
    '‐',
    '‑'
];
const divisions = ['/', '÷', '⁄', '∕', '⊘', '⟌', '⦼', '⨸'];
const functionApplication_ = String.fromCodePoint(0x2061);
const equalities = [
    '=',
    '~',
    '⁼',
    '₌',
    '∼',
    '∽',
    '≃',
    '≅',
    '≈',
    '≊',
    '≋',
    '≌',
    '≍',
    '≎',
    '≑',
    '≒',
    '≓',
    '≔',
    '≕',
    '≖',
    '≗',
    '≘',
    '≙',
    '≚',
    '≛',
    '≜',
    '≝',
    '≞',
    '≟',
    '≡',
    '≣',
    '⧤',
    '⩦',
    '⩮',
    '⩯',
    '⩰',
    '⩱',
    '⩲',
    '⩳',
    '⩴',
    '⩵',
    '⩶',
    '⩷',
    '⩸',
    '⋕',
    '⩭',
    '⩪',
    '⩫',
    '⩬',
    '﹦',
    '＝',
    '⩬',
    '⊜',
    '∷'
];
const inequalities = [
    '<',
    '>',
    '≁',
    '≂',
    '≄',
    '≆',
    '≇',
    '≉',
    '≏',
    '≐',
    '≠',
    '≢',
    '≤',
    '≥',
    '≦',
    '≧',
    '≨',
    '≩',
    '≪',
    '≫',
    '≬',
    '≭',
    '≮',
    '≯',
    '≰',
    '≱',
    '≲',
    '≳',
    '≴',
    '≵',
    '≶',
    '≷',
    '≸',
    '≹',
    '≺',
    '≻',
    '≼',
    '≽',
    '≾',
    '≿',
    '⊀',
    '⊁',
    '⋖',
    '⋗',
    '⋘',
    '⋙',
    '⋚',
    '⋛',
    '⋜',
    '⋝',
    '⋞',
    '⋟',
    '⋠',
    '⋡',
    '⋦',
    '⋧',
    '⋨',
    '⋩',
    '⩹',
    '⩺',
    '⩻',
    '⩼',
    '⩽',
    '⩾',
    '⩿',
    '⪀',
    '⪁',
    '⪂',
    '⪃',
    '⪄',
    '⪅',
    '⪆',
    '⪇',
    '⪈',
    '⪉',
    '⪊',
    '⪋',
    '⪌',
    '⪍',
    '⪎',
    '⪏',
    '⪐',
    '⪑',
    '⪒',
    '⪓',
    '⪔',
    '⪕',
    '⪖',
    '⪗',
    '⪘',
    '⪙',
    '⪚',
    '⪛',
    '⪜',
    '⪝',
    '⪞',
    '⪟',
    '⪠',
    '⪡',
    '⪢',
    '⪣',
    '⪤',
    '⪥',
    '⪦',
    '⪧',
    '⪨',
    '⪩',
    '⪪',
    '⪫',
    '⪬',
    '⪭',
    '⪮',
    '⪯',
    '⪰',
    '⪱',
    '⪲',
    '⪳',
    '⪴',
    '⪵',
    '⪶',
    '⪷',
    '⪸',
    '⪹',
    '⪺',
    '⪻',
    '⪼',
    '⫷',
    '⫸',
    '⫹',
    '⫺',
    '⧀',
    '⧁',
    '﹤',
    '﹥',
    '＜',
    '＞'
];
const setRelations = [
    '⋢',
    '⋣',
    '⋤',
    '⋥',
    '⊂',
    '⊃',
    '⊄',
    '⊅',
    '⊆',
    '⊇',
    '⊈',
    '⊉',
    '⊊',
    '⊋',
    '⊏',
    '⊐',
    '⊑',
    '⊒',
    '⪽',
    '⪾',
    '⪿',
    '⫀',
    '⫁',
    '⫂',
    '⫃',
    '⫄',
    '⫅',
    '⫆',
    '⫇',
    '⫈',
    '⫉',
    '⫊',
    '⫋',
    '⫌',
    '⫍',
    '⫎',
    '⫏',
    '⫐',
    '⫑',
    '⫒',
    '⫓',
    '⫔',
    '⫕',
    '⫖',
    '⫗',
    '⫘',
    '⋐',
    '⋑',
    '⋪',
    '⋫',
    '⋬',
    '⋭',
    '⊲',
    '⊳',
    '⊴',
    '⊵'
];
const elementRelations = [
    '∈',
    '∊',
    '⋲',
    '⋳',
    '⋴',
    '⋵',
    '⋶',
    '⋷',
    '⋸',
    '⋹',
    '⋿'
];
const nonelementRelations = ['∉'];
const reelementRelations = ['∋', '∍', '⋺', '⋻', '⋼', '⋽', '⋾'];
const renonelementRelations = ['∌'];
const relations = [
    '⊢',
    '⊣',
    '⊦',
    '⊧',
    '⊨',
    '⊩',
    '⊪',
    '⊫',
    '⊬',
    '⊭',
    '⊮',
    '⊯',
    '⫞',
    '⫟',
    '⫠',
    '⫡',
    '⫢',
    '⫣',
    '⫤',
    '⫥',
    '⫦',
    '⫧',
    '⫨',
    '⫩',
    '⫪',
    '⫫',
    '⫬',
    '⫭'
];
const arrows = [
    '←',
    '↑',
    '→',
    '↓',
    '↔',
    '↕',
    '↖',
    '↗',
    '↘',
    '↙',
    '↚',
    '↛',
    '↜',
    '↝',
    '↞',
    '↟',
    '↠',
    '↡',
    '↢',
    '↣',
    '↤',
    '↥',
    '↦',
    '↧',
    '↨',
    '↩',
    '↪',
    '↫',
    '↬',
    '↭',
    '↮',
    '↯',
    '↰',
    '↱',
    '↲',
    '↳',
    '↴',
    '↵',
    '↶',
    '↷',
    '↸',
    '↹',
    '↺',
    '↻',
    '⇄',
    '⇅',
    '⇆',
    '⇇',
    '⇈',
    '⇉',
    '⇊',
    '⇍',
    '⇎',
    '⇏',
    '⇐',
    '⇑',
    '⇒',
    '⇓',
    '⇔',
    '⇕',
    '⇖',
    '⇗',
    '⇘',
    '⇙',
    '⇚',
    '⇛',
    '⇜',
    '⇝',
    '⇞',
    '⇟',
    '⇠',
    '⇡',
    '⇢',
    '⇣',
    '⇤',
    '⇥',
    '⇦',
    '⇧',
    '⇨',
    '⇩',
    '⇪',
    '⇫',
    '⇬',
    '⇭',
    '⇮',
    '⇯',
    '⇰',
    '⇱',
    '⇲',
    '⇳',
    '⇴',
    '⇵',
    '⇶',
    '⇷',
    '⇸',
    '⇹',
    '⇺',
    '⇻',
    '⇼',
    '⇽',
    '⇾',
    '⇿',
    '⌁',
    '⌃',
    '⌄',
    '⌤',
    '⎋',
    '➔',
    '➘',
    '➙',
    '➚',
    '➛',
    '➜',
    '➝',
    '➞',
    '➟',
    '➠',
    '➡',
    '➢',
    '➣',
    '➤',
    '➥',
    '➦',
    '➧',
    '➨',
    '➩',
    '➪',
    '➫',
    '➬',
    '➭',
    '➮',
    '➯',
    '➱',
    '➲',
    '➳',
    '➴',
    '➵',
    '➶',
    '➷',
    '➸',
    '➹',
    '➺',
    '➻',
    '➼',
    '➽',
    '➾',
    '⟰',
    '⟱',
    '⟲',
    '⟳',
    '⟴',
    '⟵',
    '⟶',
    '⟷',
    '⟸',
    '⟹',
    '⟺',
    '⟻',
    '⟼',
    '⟽',
    '⟾',
    '⟿',
    '⤀',
    '⤁',
    '⤂',
    '⤃',
    '⤄',
    '⤅',
    '⤆',
    '⤇',
    '⤈',
    '⤉',
    '⤊',
    '⤋',
    '⤌',
    '⤍',
    '⤎',
    '⤏',
    '⤐',
    '⤑',
    '⤒',
    '⤓',
    '⤔',
    '⤕',
    '⤖',
    '⤗',
    '⤘',
    '⤙',
    '⤚',
    '⤛',
    '⤜',
    '⤝',
    '⤞',
    '⤟',
    '⤠',
    '⤡',
    '⤢',
    '⤣',
    '⤤',
    '⤥',
    '⤦',
    '⤧',
    '⤨',
    '⤩',
    '⤪',
    '⤭',
    '⤮',
    '⤯',
    '⤰',
    '⤱',
    '⤲',
    '⤳',
    '⤴',
    '⤵',
    '⤶',
    '⤷',
    '⤸',
    '⤹',
    '⤺',
    '⤻',
    '⤼',
    '⤽',
    '⤾',
    '⤿',
    '⥀',
    '⥁',
    '⥂',
    '⥃',
    '⥄',
    '⥅',
    '⥆',
    '⥇',
    '⥈',
    '⥉',
    '⥰',
    '⥱',
    '⥲',
    '⥳',
    '⥴',
    '⥵',
    '⥶',
    '⥷',
    '⥸',
    '⥹',
    '⥺',
    '⥻',
    '⦳',
    '⦴',
    '⦽',
    '⧪',
    '⧬',
    '⧭',
    '⨗',
    '⬀',
    '⬁',
    '⬂',
    '⬃',
    '⬄',
    '⬅',
    '⬆',
    '⬇',
    '⬈',
    '⬉',
    '⬊',
    '⬋',
    '⬌',
    '⬍',
    '⬎',
    '⬏',
    '⬐',
    '⬑',
    '⬰',
    '⬱',
    '⬲',
    '⬳',
    '⬴',
    '⬵',
    '⬶',
    '⬷',
    '⬸',
    '⬹',
    '⬺',
    '⬻',
    '⬼',
    '⬽',
    '⬾',
    '⬿',
    '⭀',
    '⭁',
    '⭂',
    '⭃',
    '⭄',
    '⭅',
    '⭆',
    '⭇',
    '⭈',
    '⭉',
    '⭊',
    '⭋',
    '⭌',
    '￩',
    '￪',
    '￫',
    '￬',
    '↼',
    '↽',
    '↾',
    '↿',
    '⇀',
    '⇁',
    '⇂',
    '⇃',
    '⇋',
    '⇌',
    '⥊',
    '⥋',
    '⥌',
    '⥍',
    '⥎',
    '⥏',
    '⥐',
    '⥑',
    '⥒',
    '⥓',
    '⥔',
    '⥕',
    '⥖',
    '⥗',
    '⥘',
    '⥙',
    '⥚',
    '⥛',
    '⥜',
    '⥝',
    '⥞',
    '⥟',
    '⥠',
    '⥡',
    '⥢',
    '⥣',
    '⥤',
    '⥥',
    '⥦',
    '⥧',
    '⥨',
    '⥩',
    '⥪',
    '⥫',
    '⥬',
    '⥭',
    '⥮',
    '⥯',
    '⥼',
    '⥽',
    '⥾',
    '⥿'
];
const sumOps = [
    '⅀',
    '∏',
    '∐',
    '∑',
    '⋀',
    '⋁',
    '⋂',
    '⋃',
    '⨀',
    '⨁',
    '⨂',
    '⨃',
    '⨄',
    '⨅',
    '⨆',
    '⨇',
    '⨈',
    '⨉',
    '⨊',
    '⨋',
    '⫼',
    '⫿'
];
const intOps = [
    '∫',
    '∬',
    '∭',
    '∮',
    '∯',
    '∰',
    '∱',
    '∲',
    '∳',
    '⨌',
    '⨍',
    '⨎',
    '⨏',
    '⨐',
    '⨑',
    '⨒',
    '⨓',
    '⨔',
    '⨕',
    '⨖',
    '⨗',
    '⨘',
    '⨙',
    '⨚',
    '⨛',
    '⨜'
];
const geometryOps = [
    '∟',
    '∠',
    '∡',
    '∢',
    '⊾',
    '⊿',
    '△',
    '▷',
    '▽',
    '◁'
];
const prefixOps = ['∀', '∃', '∆', '∇', '∂', '∁', '∄'];
const prefixOpsBold = ['𝛁', '𝛛', '𝟊', '𝟋'];
const prefixOpsItalic = ['𝛻', '𝜕'];
const prefixOpsSansSerifBold = ['𝝯', '𝞉'];
const digitsNormal = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
];
const digitsFullWidth = [
    '０',
    '１',
    '２',
    '３',
    '４',
    '５',
    '６',
    '７',
    '８',
    '９'
];
const digitsBold = ['𝟎', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗'];
const digitsDoubleStruck = [
    '𝟘',
    '𝟙',
    '𝟚',
    '𝟛',
    '𝟜',
    '𝟝',
    '𝟞',
    '𝟟',
    '𝟠',
    '𝟡'
];
const digitsSansSerif = [
    '𝟢',
    '𝟣',
    '𝟤',
    '𝟥',
    '𝟦',
    '𝟧',
    '𝟨',
    '𝟩',
    '𝟪',
    '𝟫'
];
const digitsSansSerifBold = [
    '𝟬',
    '𝟭',
    '𝟮',
    '𝟯',
    '𝟰',
    '𝟱',
    '𝟲',
    '𝟳',
    '𝟴',
    '𝟵'
];
const digitsMonospace = [
    '𝟶',
    '𝟷',
    '𝟸',
    '𝟹',
    '𝟺',
    '𝟻',
    '𝟼',
    '𝟽',
    '𝟾',
    '𝟿'
];
const digitsSuperscript = [
    '²',
    '³',
    '¹',
    '⁰',
    '⁴',
    '⁵',
    '⁶',
    '⁷',
    '⁸',
    '⁹'
];
const digitsSubscript = [
    '₀',
    '₁',
    '₂',
    '₃',
    '₄',
    '₅',
    '₆',
    '₇',
    '₈',
    '₉'
];
const fractions = [
    '¼',
    '½',
    '¾',
    '⅐',
    '⅑',
    '⅒',
    '⅓',
    '⅔',
    '⅕',
    '⅖',
    '⅗',
    '⅘',
    '⅙',
    '⅚',
    '⅛',
    '⅜',
    '⅝',
    '⅞',
    '⅟',
    '↉'
];
const enclosedNumbers = [
    '①',
    '②',
    '③',
    '④',
    '⑤',
    '⑥',
    '⑦',
    '⑧',
    '⑨',
    '⑩',
    '⑪',
    '⑫',
    '⑬',
    '⑭',
    '⑮',
    '⑯',
    '⑰',
    '⑱',
    '⑲',
    '⑳',
    '⓪',
    '⓫',
    '⓬',
    '⓭',
    '⓮',
    '⓯',
    '⓰',
    '⓱',
    '⓲',
    '⓳',
    '⓴',
    '⓵',
    '⓶',
    '⓷',
    '⓸',
    '⓹',
    '⓺',
    '⓻',
    '⓼',
    '⓽',
    '⓾',
    '⓿',
    '❶',
    '❷',
    '❸',
    '❹',
    '❺',
    '❻',
    '❼',
    '❽',
    '❾',
    '❿',
    '➀',
    '➁',
    '➂',
    '➃',
    '➄',
    '➅',
    '➆',
    '➇',
    '➈',
    '➉',
    '➊',
    '➋',
    '➌',
    '➍',
    '➎',
    '➏',
    '➐',
    '➑',
    '➒',
    '➓',
    '㉈',
    '㉉',
    '㉊',
    '㉋',
    '㉌',
    '㉍',
    '㉎',
    '㉏',
    '㉑',
    '㉒',
    '㉓',
    '㉔',
    '㉕',
    '㉖',
    '㉗',
    '㉘',
    '㉙',
    '㉚',
    '㉛',
    '㉜',
    '㉝',
    '㉞',
    '㉟',
    '㊱',
    '㊲',
    '㊳',
    '㊴',
    '㊵',
    '㊶',
    '㊷',
    '㊸',
    '㊹',
    '㊺',
    '㊻',
    '㊼',
    '㊽',
    '㊾',
    '㊿'
];
const fencedNumbers = [
    '⑴',
    '⑵',
    '⑶',
    '⑷',
    '⑸',
    '⑹',
    '⑺',
    '⑻',
    '⑼',
    '⑽',
    '⑾',
    '⑿',
    '⒀',
    '⒁',
    '⒂',
    '⒃',
    '⒄',
    '⒅',
    '⒆',
    '⒇'
];
const punctuatedNumbers = [
    '⒈',
    '⒉',
    '⒊',
    '⒋',
    '⒌',
    '⒍',
    '⒎',
    '⒏',
    '⒐',
    '⒑',
    '⒒',
    '⒓',
    '⒔',
    '⒕',
    '⒖',
    '⒗',
    '⒘',
    '⒙',
    '⒚',
    '⒛',
    '🄀',
    '🄁',
    '🄂',
    '🄃',
    '🄄',
    '🄅',
    '🄆',
    '🄇',
    '🄈',
    '🄉',
    '🄊'
];
const numbers = fractions;
const otherNumbers = digitsSuperscript.concat(digitsSubscript, enclosedNumbers, fencedNumbers, punctuatedNumbers);
const trigonometricFunctions = [
    'cos',
    'cot',
    'csc',
    'sec',
    'sin',
    'tan',
    'arccos',
    'arccot',
    'arccsc',
    'arcsec',
    'arcsin',
    'arctan',
    'arc cos',
    'arc cot',
    'arc csc',
    'arc sec',
    'arc sin',
    'arc tan'
];
const hyperbolicFunctions = [
    'cosh',
    'coth',
    'csch',
    'sech',
    'sinh',
    'tanh',
    'arcosh',
    'arcoth',
    'arcsch',
    'arsech',
    'arsinh',
    'artanh',
    'arccosh',
    'arccoth',
    'arccsch',
    'arcsech',
    'arcsinh',
    'arctanh'
];
const algebraicFunctions = [
    'deg',
    'det',
    'dim',
    'hom',
    'ker',
    'Tr',
    'tr'
];
const elementaryFunctions = [
    'log',
    'ln',
    'lg',
    'exp',
    'expt',
    'gcd',
    'gcd',
    'arg',
    'im',
    're',
    'Pr'
];
const prefixFunctions = trigonometricFunctions.concat(hyperbolicFunctions, algebraicFunctions, elementaryFunctions);
const limitFunctions = [
    'inf',
    'lim',
    'liminf',
    'limsup',
    'max',
    'min',
    'sup',
    'injlim',
    'projlim',
    'inj lim',
    'proj lim'
];
const infixFunctions = ['mod', 'rem'];
const symbolSetToSemantic_ = [
    {
        set: generalPunctuations,
        type: "punctuation",
        role: "unknown"
    },
    {
        set: colons,
        type: "punctuation",
        role: "colon"
    },
    {
        set: commas,
        type: "punctuation",
        role: "comma"
    },
    {
        set: ellipses,
        type: "punctuation",
        role: "ellipsis"
    },
    {
        set: fullStops,
        type: "punctuation",
        role: "fullstop"
    },
    {
        set: dashes,
        type: "operator",
        role: "dash"
    },
    {
        set: tildes,
        type: "operator",
        role: "tilde"
    },
    {
        set: primes,
        type: "punctuation",
        role: "prime"
    },
    {
        set: degrees,
        type: "punctuation",
        role: "degree"
    },
    {
        set: leftFences,
        type: "fence",
        role: "open"
    },
    {
        set: rightFences,
        type: "fence",
        role: "close"
    },
    {
        set: topFences,
        type: "fence",
        role: "top"
    },
    {
        set: bottomFences,
        type: "fence",
        role: "bottom"
    },
    {
        set: neutralFences,
        type: "fence",
        role: "neutral"
    },
    {
        set: metricFences,
        type: "fence",
        role: "metric"
    },
    {
        set: smallLatin,
        type: "identifier",
        role: "latinletter",
        font: "normal"
    },
    {
        set: capitalLatin,
        type: "identifier",
        role: "latinletter",
        font: "normal"
    },
    {
        set: smallLatinFullWidth,
        type: "identifier",
        role: "latinletter",
        font: "normal"
    },
    {
        set: capitalLatinFullWidth,
        type: "identifier",
        role: "latinletter",
        font: "normal"
    },
    {
        set: smallLatinBold,
        type: "identifier",
        role: "latinletter",
        font: "bold"
    },
    {
        set: capitalLatinBold,
        type: "identifier",
        role: "latinletter",
        font: "bold"
    },
    {
        set: smallLatinItalic,
        type: "identifier",
        role: "latinletter",
        font: "italic"
    },
    {
        set: capitalLatinItalic,
        type: "identifier",
        role: "latinletter",
        font: "italic"
    },
    {
        set: smallLatinBoldItalic,
        type: "identifier",
        role: "latinletter",
        font: "bold-italic"
    },
    {
        set: capitalLatinBoldItalic,
        type: "identifier",
        role: "latinletter",
        font: "bold-italic"
    },
    {
        set: smallLatinScript,
        type: "identifier",
        role: "latinletter",
        font: "script"
    },
    {
        set: capitalLatinScript,
        type: "identifier",
        role: "latinletter",
        font: "script"
    },
    {
        set: smallLatinBoldScript,
        type: "identifier",
        role: "latinletter",
        font: "bold-script"
    },
    {
        set: capitalLatinBoldScript,
        type: "identifier",
        role: "latinletter",
        font: "bold-script"
    },
    {
        set: smallLatinFraktur,
        type: "identifier",
        role: "latinletter",
        font: "fraktur"
    },
    {
        set: capitalLatinFraktur,
        type: "identifier",
        role: "latinletter",
        font: "fraktur"
    },
    {
        set: smallLatinDoubleStruck,
        type: "identifier",
        role: "latinletter",
        font: "double-struck"
    },
    {
        set: capitalLatinDoubleStruck,
        type: "identifier",
        role: "latinletter",
        font: "double-struck"
    },
    {
        set: smallLatinBoldFraktur,
        type: "identifier",
        role: "latinletter",
        font: "bold-fraktur"
    },
    {
        set: capitalLatinBoldFraktur,
        type: "identifier",
        role: "latinletter",
        font: "bold-fraktur"
    },
    {
        set: smallLatinSansSerif,
        type: "identifier",
        role: "latinletter",
        font: "sans-serif"
    },
    {
        set: capitalLatinSansSerif,
        type: "identifier",
        role: "latinletter",
        font: "sans-serif"
    },
    {
        set: smallLatinSansSerifBold,
        type: "identifier",
        role: "latinletter",
        font: "sans-serif-bold"
    },
    {
        set: capitalLatinSansSerifBold,
        type: "identifier",
        role: "latinletter",
        font: "sans-serif-bold"
    },
    {
        set: smallLatinSansSerifItalic,
        type: "identifier",
        role: "latinletter",
        font: "sans-serif-italic"
    },
    {
        set: capitalLatinSansSerifItalic,
        type: "identifier",
        role: "latinletter",
        font: "sans-serif-italic"
    },
    {
        set: smallLatinSansSerifBoldItalic,
        type: "identifier",
        role: "latinletter",
        font: "sans-serif-bold-italic"
    },
    {
        set: capitalLatinSansSerifBoldItalic,
        type: "identifier",
        role: "latinletter",
        font: "sans-serif-bold-italic"
    },
    {
        set: smallLatinMonospace,
        type: "identifier",
        role: "latinletter",
        font: "monospace"
    },
    {
        set: capitalLatinMonospace,
        type: "identifier",
        role: "latinletter",
        font: "monospace"
    },
    {
        set: latinDoubleStruckItalic,
        type: "identifier",
        role: "latinletter",
        font: "double-struck-italic"
    },
    {
        set: smallGreek,
        type: "identifier",
        role: "greekletter",
        font: "normal"
    },
    {
        set: capitalGreek,
        type: "identifier",
        role: "greekletter",
        font: "normal"
    },
    {
        set: smallGreekBold,
        type: "identifier",
        role: "greekletter",
        font: "bold"
    },
    {
        set: capitalGreekBold,
        type: "identifier",
        role: "greekletter",
        font: "bold"
    },
    {
        set: smallGreekItalic,
        type: "identifier",
        role: "greekletter",
        font: "italic"
    },
    {
        set: capitalGreekItalic,
        type: "identifier",
        role: "greekletter",
        font: "italic"
    },
    {
        set: smallGreekBoldItalic,
        type: "identifier",
        role: "greekletter",
        font: "bold-italic"
    },
    {
        set: capitalGreekBoldItalic,
        type: "identifier",
        role: "greekletter",
        font: "bold-italic"
    },
    {
        set: smallGreekSansSerifBold,
        type: "identifier",
        role: "greekletter",
        font: "sans-serif-bold"
    },
    {
        set: capitalGreekSansSerifBold,
        type: "identifier",
        role: "greekletter",
        font: "sans-serif-bold"
    },
    {
        set: capitalGreekSansSerifBoldItalic,
        type: "identifier",
        role: "greekletter",
        font: "sans-serif-bold-italic"
    },
    {
        set: smallGreekSansSerifBoldItalic,
        type: "identifier",
        role: "greekletter",
        font: "sans-serif-bold-italic"
    },
    {
        set: greekDoubleStruck,
        type: "identifier",
        role: "greekletter",
        font: "double-struck"
    },
    {
        set: greekSpecial,
        type: "identifier",
        role: "greekletter",
        font: "normal"
    },
    {
        set: greekSpecialBold,
        type: "identifier",
        role: "greekletter",
        font: "bold"
    },
    {
        set: greekSpecialItalic,
        type: "identifier",
        role: "greekletter",
        font: "italic"
    },
    {
        set: greekSpecialSansSerifBold,
        type: "identifier",
        role: "greekletter",
        font: "sans-serif-bold"
    },
    {
        set: hebrewLetters,
        type: "identifier",
        role: "otherletter",
        font: "normal"
    },
    {
        set: digitsNormal,
        type: "number",
        role: "integer",
        font: "normal"
    },
    {
        set: digitsFullWidth,
        type: "number",
        role: "integer",
        font: "normal"
    },
    {
        set: digitsBold,
        type: "number",
        role: "integer",
        font: "bold"
    },
    {
        set: digitsDoubleStruck,
        type: "number",
        role: "integer",
        font: "double-struck"
    },
    {
        set: digitsSansSerif,
        type: "number",
        role: "integer",
        font: "sans-serif"
    },
    {
        set: digitsSansSerifBold,
        type: "number",
        role: "integer",
        font: "sans-serif-bold"
    },
    {
        set: digitsMonospace,
        type: "number",
        role: "integer",
        font: "monospace"
    },
    {
        set: numbers,
        type: "number",
        role: "float"
    },
    {
        set: otherNumbers,
        type: "number",
        role: "othernumber"
    },
    {
        set: additions,
        type: "operator",
        role: "addition"
    },
    {
        set: multiplications,
        type: "operator",
        role: "multiplication"
    },
    {
        set: subtractions,
        type: "operator",
        role: "subtraction"
    },
    {
        set: divisions,
        type: "operator",
        role: "division"
    },
    {
        set: prefixOps,
        type: "operator",
        role: "prefix operator"
    },
    {
        set: prefixOpsBold,
        type: "operator",
        role: "prefix operator",
        font: "bold"
    },
    {
        set: prefixOpsItalic,
        type: "operator",
        role: "prefix operator",
        font: "italic"
    },
    {
        set: prefixOpsSansSerifBold,
        type: "operator",
        role: "prefix operator",
        font: "sans-serif-bold"
    },
    {
        set: equalities,
        type: "relation",
        role: "equality"
    },
    {
        set: inequalities,
        type: "relation",
        role: "inequality"
    },
    {
        set: setRelations,
        type: "relation",
        role: "set"
    },
    {
        set: relations,
        type: "relation",
        role: "unknown"
    },
    {
        set: arrows,
        type: "relation",
        role: "arrow"
    },
    {
        set: elementRelations,
        type: "operator",
        role: "element"
    },
    {
        set: nonelementRelations,
        type: "operator",
        role: "nonelement"
    },
    {
        set: reelementRelations,
        type: "operator",
        role: "reelement"
    },
    {
        set: renonelementRelations,
        type: "operator",
        role: "renonelement"
    },
    {
        set: sumOps,
        type: "largeop",
        role: "sum"
    },
    {
        set: intOps,
        type: "largeop",
        role: "integral"
    },
    {
        set: geometryOps,
        type: "operator",
        role: "geometry"
    },
    {
        set: limitFunctions,
        type: "function",
        role: "limit function"
    },
    {
        set: prefixFunctions,
        type: "function",
        role: "prefix function"
    },
    {
        set: infixFunctions,
        type: "operator",
        role: "prefix function"
    }
];
const meaning_ = (function () {
    const result = {};
    for (let i = 0, st; (st = symbolSetToSemantic_[i]); i++) {
        st.set.forEach(function (symbol) {
            result[symbol] = {
                role: st.role || "unknown",
                type: st.type || "unknown",
                font: st.font || "unknown"
            };
        });
    }
    return result;
})();
function equal(meaning1, meaning2) {
    return (meaning1.type === meaning2.type &&
        meaning1.role === meaning2.role &&
        meaning1.font === meaning2.font);
}
exports.equal = equal;
function lookupType(symbol) {
    var _a;
    return ((_a = meaning_[symbol]) === null || _a === void 0 ? void 0 : _a.type) || "unknown";
}
exports.lookupType = lookupType;
function lookupRole(symbol) {
    var _a;
    return ((_a = meaning_[symbol]) === null || _a === void 0 ? void 0 : _a.role) || "unknown";
}
exports.lookupRole = lookupRole;
function lookupMeaning(symbol) {
    return (meaning_[symbol] || {
        role: "unknown",
        type: "unknown",
        font: "unknown"
    });
}
exports.lookupMeaning = lookupMeaning;
function invisibleTimes() {
    return invisibleTimes_;
}
exports.invisibleTimes = invisibleTimes;
function invisiblePlus() {
    return invisiblePlus_;
}
exports.invisiblePlus = invisiblePlus;
function invisibleComma() {
    return invisibleComma_;
}
exports.invisibleComma = invisibleComma;
function functionApplication() {
    return functionApplication_;
}
exports.functionApplication = functionApplication;
function isMatchingFence(open, close) {
    if (neutralFences.indexOf(open) !== -1 || metricFences.indexOf(open) !== -1) {
        return open === close;
    }
    return openClosePairs[open] === close || topBottomPairs[open] === close;
}
exports.isMatchingFence = isMatchingFence;
function isEmbellishedType(type) {
    return (type === "operator" ||
        type === "relation" ||
        type === "fence" ||
        type === "punctuation");
}
exports.isEmbellishedType = isEmbellishedType;
const secondary_ = new Map();
function secKey(kind, char) {
    return `${kind} ${char}`;
}
function addSecondary_(kind, chars, annotation = '') {
    for (const char of chars) {
        secondary_.set(secKey(kind, char), annotation || kind);
    }
}
addSecondary_('d', [
    'd',
    'ⅆ',
    'ｄ',
    '𝐝',
    '𝑑',
    '𝒹',
    '𝓭',
    '𝔡',
    '𝕕',
    '𝖉',
    '𝖽',
    '𝗱',
    '𝘥',
    '𝚍'
]);
addSecondary_('bar', dashes);
addSecondary_('tilde', tildes);
function lookupSecondary(kind, char) {
    return secondary_.get(secKey(kind, char));
}
exports.lookupSecondary = lookupSecondary;


/***/ }),

/***/ 7405:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticMeaningCollator = exports.SemanticNodeCollator = exports.SemanticDefault = void 0;
const SemanticAttr = __webpack_require__(4020);
const semantic_ordering_1 = __webpack_require__(178);
class SemanticDefault {
    constructor() {
        this.map = {};
    }
    static key(symbol, font) {
        return font ? symbol + ':' + font : symbol;
    }
    add(symbol, meaning) {
        this.map[SemanticDefault.key(symbol, meaning.font)] = meaning;
    }
    addNode(node) {
        this.add(node.textContent, node.meaning());
    }
    retrieve(symbol, font) {
        return this.map[SemanticDefault.key(symbol, font)];
    }
    retrieveNode(node) {
        return this.retrieve(node.textContent, node.font);
    }
    size() {
        return Object.keys(this.map).length;
    }
}
exports.SemanticDefault = SemanticDefault;
class SemanticCollator {
    constructor() {
        this.map = {};
    }
    add(symbol, entry) {
        const list = this.map[symbol];
        if (list) {
            list.push(entry);
        }
        else {
            this.map[symbol] = [entry];
        }
    }
    retrieve(symbol, font) {
        return this.map[SemanticDefault.key(symbol, font)];
    }
    retrieveNode(node) {
        return this.retrieve(node.textContent, node.font);
    }
    copy() {
        const collator = this.copyCollator();
        for (const key in this.map) {
            collator.map[key] = this.map[key];
        }
        return collator;
    }
    minimize() {
        for (const key in this.map) {
            if (this.map[key].length === 1) {
                delete this.map[key];
            }
        }
    }
    minimalCollator() {
        const collator = this.copy();
        for (const key in collator.map) {
            if (collator.map[key].length === 1) {
                delete collator.map[key];
            }
        }
        return collator;
    }
    isMultiValued() {
        for (const key in this.map) {
            if (this.map[key].length > 1) {
                return true;
            }
        }
        return false;
    }
    isEmpty() {
        return !Object.keys(this.map).length;
    }
}
class SemanticNodeCollator extends SemanticCollator {
    copyCollator() {
        return new SemanticNodeCollator();
    }
    add(symbol, entry) {
        const key = SemanticDefault.key(symbol, entry.font);
        super.add(key, entry);
    }
    addNode(node) {
        this.add(node.textContent, node);
    }
    toString() {
        const outer = [];
        for (const key in this.map) {
            const length = Array(key.length + 3).join(' ');
            const nodes = this.map[key];
            const inner = [];
            for (let i = 0, node; (node = nodes[i]); i++) {
                inner.push(node.toString());
            }
            outer.push(key + ': ' + inner.join('\n' + length));
        }
        return outer.join('\n');
    }
    collateMeaning() {
        const collator = new SemanticMeaningCollator();
        for (const key in this.map) {
            collator.map[key] = this.map[key].map(function (node) {
                return node.meaning();
            });
        }
        return collator;
    }
}
exports.SemanticNodeCollator = SemanticNodeCollator;
class SemanticMeaningCollator extends SemanticCollator {
    copyCollator() {
        return new SemanticMeaningCollator();
    }
    add(symbol, entry) {
        const list = this.retrieve(symbol, entry.font);
        if (!list ||
            !list.find(function (x) {
                return SemanticAttr.equal(x, entry);
            })) {
            const key = SemanticDefault.key(symbol, entry.font);
            super.add(key, entry);
        }
    }
    addNode(node) {
        this.add(node.textContent, node.meaning());
    }
    toString() {
        const outer = [];
        for (const key in this.map) {
            const length = Array(key.length + 3).join(' ');
            const nodes = this.map[key];
            const inner = [];
            for (let i = 0, node; (node = nodes[i]); i++) {
                inner.push('{type: ' +
                    node.type +
                    ', role: ' +
                    node.role +
                    ', font: ' +
                    node.font +
                    '}');
            }
            outer.push(key + ': ' + inner.join('\n' + length));
        }
        return outer.join('\n');
    }
    reduce() {
        for (const key in this.map) {
            if (this.map[key].length !== 1) {
                this.map[key] = (0, semantic_ordering_1.reduce)(this.map[key]);
            }
        }
    }
    default() {
        const def = new SemanticDefault();
        for (const key in this.map) {
            if (this.map[key].length === 1) {
                def.map[key] = this.map[key][0];
            }
        }
        return def;
    }
    newDefault() {
        const oldDefault = this.default();
        this.reduce();
        const newDefault = this.default();
        return oldDefault.size() !== newDefault.size() ? newDefault : null;
    }
}
exports.SemanticMeaningCollator = SemanticMeaningCollator;


/***/ }),

/***/ 5958:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticMultiHeuristic = exports.SemanticTreeHeuristic = exports.SemanticAbstractHeuristic = void 0;
class SemanticAbstractHeuristic {
    constructor(name, method, predicate = (_x) => false) {
        this.name = name;
        this.apply = method;
        this.applicable = predicate;
    }
}
exports.SemanticAbstractHeuristic = SemanticAbstractHeuristic;
class SemanticTreeHeuristic extends SemanticAbstractHeuristic {
}
exports.SemanticTreeHeuristic = SemanticTreeHeuristic;
class SemanticMultiHeuristic extends SemanticAbstractHeuristic {
}
exports.SemanticMultiHeuristic = SemanticMultiHeuristic;


/***/ }),

/***/ 2721:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.lookup = exports.run = exports.add = exports.blacklist = exports.flags = exports.updateFactory = exports.factory = void 0;
exports.factory = null;
function updateFactory(nodeFactory) {
    exports.factory = nodeFactory;
}
exports.updateFactory = updateFactory;
const heuristics = new Map();
exports.flags = {
    combine_juxtaposition: true,
    convert_juxtaposition: true,
    multioperator: true
};
exports.blacklist = {};
function add(heuristic) {
    const name = heuristic.name;
    heuristics.set(name, heuristic);
    if (!exports.flags[name]) {
        exports.flags[name] = false;
    }
}
exports.add = add;
function run(name, root, opt_alternative) {
    const heuristic = lookup(name);
    return heuristic &&
        !exports.blacklist[name] &&
        (exports.flags[name] || heuristic.applicable(root))
        ? heuristic.apply(root)
        : opt_alternative
            ? opt_alternative(root)
            : root;
}
exports.run = run;
function lookup(name) {
    return heuristics.get(name);
}
exports.lookup = lookup;


/***/ }),

/***/ 7103:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const debugger_1 = __webpack_require__(1984);
const engine_1 = __webpack_require__(4886);
const SemanticAttr = __webpack_require__(4020);
const SemanticHeuristics = __webpack_require__(2721);
const semantic_heuristic_1 = __webpack_require__(5958);
const SemanticPred = __webpack_require__(6161);
const semantic_processor_1 = __webpack_require__(7793);
const SemanticUtil = __webpack_require__(8901);
SemanticHeuristics.add(new semantic_heuristic_1.SemanticTreeHeuristic('combine_juxtaposition', combineJuxtaposition));
function combineJuxtaposition(root) {
    for (let i = root.childNodes.length - 1, child; (child = root.childNodes[i]); i--) {
        if (!SemanticPred.isImplicitOp(child) || child.nobreaking) {
            continue;
        }
        root.childNodes.splice(i, 1, ...child.childNodes);
        root.contentNodes.splice(i, 0, ...child.contentNodes);
        child.childNodes.concat(child.contentNodes).forEach(function (x) {
            x.parent = root;
        });
        root.addMathmlNodes(child.mathml);
    }
    return root;
}
SemanticHeuristics.add(new semantic_heuristic_1.SemanticTreeHeuristic('propagateSimpleFunction', (node) => {
    if ((node.type === "infixop" ||
        node.type === "fraction") &&
        node.childNodes.every(SemanticPred.isSimpleFunction)) {
        node.role = "composed function";
    }
    return node;
}, (_node) => engine_1.default.getInstance().domain === 'clearspeak'));
SemanticHeuristics.add(new semantic_heuristic_1.SemanticTreeHeuristic('simpleNamedFunction', (node) => {
    const specialFunctions = ['f', 'g', 'h', 'F', 'G', 'H'];
    if (node.role !== "unit" &&
        specialFunctions.indexOf(node.textContent) !== -1) {
        node.role = "simple function";
    }
    return node;
}, (_node) => engine_1.default.getInstance().domain === 'clearspeak'));
SemanticHeuristics.add(new semantic_heuristic_1.SemanticTreeHeuristic('propagateComposedFunction', (node) => {
    if (node.type === "fenced" &&
        node.childNodes[0].role === "composed function") {
        node.role = "composed function";
    }
    return node;
}, (_node) => engine_1.default.getInstance().domain === 'clearspeak'));
SemanticHeuristics.add(new semantic_heuristic_1.SemanticTreeHeuristic('multioperator', (node) => {
    if (node.role !== "unknown" || node.textContent.length <= 1) {
        return;
    }
    const content = [...node.textContent];
    const meaning = content.map(SemanticAttr.lookupMeaning);
    const singleRole = meaning.reduce(function (prev, curr) {
        if (!prev ||
            !curr.role ||
            curr.role === "unknown" ||
            curr.role === prev) {
            return prev;
        }
        if (prev === "unknown") {
            return curr.role;
        }
        return null;
    }, "unknown");
    if (singleRole) {
        node.role = singleRole;
    }
}));
SemanticHeuristics.add(new semantic_heuristic_1.SemanticMultiHeuristic('convert_juxtaposition', (nodes) => {
    let partition = SemanticUtil.partitionNodes(nodes, function (x) {
        return (x.textContent === SemanticAttr.invisibleTimes() &&
            x.type === "operator");
    });
    partition = partition.rel.length
        ? juxtapositionPrePost(partition)
        : partition;
    nodes = partition.comp[0];
    for (let i = 1, c, r; (c = partition.comp[i]), (r = partition.rel[i - 1]); i++) {
        nodes.push(r);
        nodes = nodes.concat(c);
    }
    partition = SemanticUtil.partitionNodes(nodes, function (x) {
        return (x.textContent === SemanticAttr.invisibleTimes() &&
            (x.type === "operator" || x.type === "infixop"));
    });
    if (!partition.rel.length) {
        return nodes;
    }
    return recurseJuxtaposition(partition.comp.shift(), partition.rel, partition.comp);
}));
SemanticHeuristics.add(new semantic_heuristic_1.SemanticTreeHeuristic('simple2prefix', (node) => {
    if (node.textContent.length > 1 &&
        !node.textContent[0].match(/[A-Z]/)) {
        node.role = "prefix function";
    }
    return node;
}, (node) => engine_1.default.getInstance().modality === 'braille' &&
    node.type === "identifier"));
SemanticHeuristics.add(new semantic_heuristic_1.SemanticTreeHeuristic('detect_cycle', (node) => {
    node.type = "matrix";
    node.role = "cycle";
    const row = node.childNodes[0];
    row.type = "row";
    row.role = "cycle";
    row.textContent = '';
    row.contentNodes = [];
    return node;
}, (node) => node.type === "fenced" &&
    node.childNodes[0].type === "infixop" &&
    node.childNodes[0].role === "implicit" &&
    node.childNodes[0].childNodes.every(function (x) {
        return x.type === "number";
    }) &&
    node.childNodes[0].contentNodes.every(function (x) {
        return x.role === "space";
    })));
function juxtapositionPrePost(partition) {
    const rels = [];
    const comps = [];
    let next = partition.comp.shift();
    let rel = null;
    let collect = [];
    while (partition.comp.length) {
        collect = [];
        if (next.length) {
            if (rel) {
                rels.push(rel);
            }
            comps.push(next);
            rel = partition.rel.shift();
            next = partition.comp.shift();
            continue;
        }
        if (rel) {
            collect.push(rel);
        }
        while (!next.length && partition.comp.length) {
            next = partition.comp.shift();
            collect.push(partition.rel.shift());
        }
        rel = convertPrePost(collect, next, comps);
    }
    if (!collect.length && !next.length) {
        collect.push(rel);
        convertPrePost(collect, next, comps);
    }
    else {
        rels.push(rel);
        comps.push(next);
    }
    return { rel: rels, comp: comps };
}
function convertPrePost(collect, next, comps) {
    let rel = null;
    if (!collect.length) {
        return rel;
    }
    const prev = comps[comps.length - 1];
    const prevExists = prev && prev.length;
    const nextExists = next && next.length;
    const processor = semantic_processor_1.default.getInstance();
    if (prevExists && nextExists) {
        if (next[0].type === "infixop" &&
            next[0].role === "implicit") {
            rel = collect.pop();
            prev.push(processor['postfixNode_'](prev.pop(), collect));
            return rel;
        }
        rel = collect.shift();
        const result = processor['prefixNode_'](next.shift(), collect);
        next.unshift(result);
        return rel;
    }
    if (prevExists) {
        prev.push(processor['postfixNode_'](prev.pop(), collect));
        return rel;
    }
    if (nextExists) {
        next.unshift(processor['prefixNode_'](next.shift(), collect));
    }
    return rel;
}
function recurseJuxtaposition(acc, ops, elements) {
    if (!ops.length) {
        return acc;
    }
    const left = acc.pop();
    const op = ops.shift();
    const first = elements.shift();
    if (SemanticPred.isImplicitOp(op)) {
        debugger_1.Debugger.getInstance().output('Juxta Heuristic Case 2');
        const right = (left ? [left, op] : [op]).concat(first);
        return recurseJuxtaposition(acc.concat(right), ops, elements);
    }
    if (!left) {
        debugger_1.Debugger.getInstance().output('Juxta Heuristic Case 3');
        return recurseJuxtaposition([op].concat(first), ops, elements);
    }
    const right = first.shift();
    if (!right) {
        debugger_1.Debugger.getInstance().output('Juxta Heuristic Case 9');
        const newOp = SemanticHeuristics.factory.makeBranchNode("infixop", [left, ops.shift()], [op], op.textContent);
        newOp.role = "implicit";
        SemanticHeuristics.run('combine_juxtaposition', newOp);
        ops.unshift(newOp);
        return recurseJuxtaposition(acc, ops, elements);
    }
    if (SemanticPred.isOperator(left) || SemanticPred.isOperator(right)) {
        debugger_1.Debugger.getInstance().output('Juxta Heuristic Case 4');
        return recurseJuxtaposition(acc.concat([left, op, right]).concat(first), ops, elements);
    }
    let result = null;
    if (SemanticPred.isImplicitOp(left) && SemanticPred.isImplicitOp(right)) {
        debugger_1.Debugger.getInstance().output('Juxta Heuristic Case 5');
        left.contentNodes.push(op);
        left.contentNodes = left.contentNodes.concat(right.contentNodes);
        left.childNodes.push(right);
        left.childNodes = left.childNodes.concat(right.childNodes);
        right.childNodes.forEach((x) => (x.parent = left));
        op.parent = left;
        left.addMathmlNodes(op.mathml);
        left.addMathmlNodes(right.mathml);
        result = left;
    }
    else if (SemanticPred.isImplicitOp(left)) {
        debugger_1.Debugger.getInstance().output('Juxta Heuristic Case 6');
        left.contentNodes.push(op);
        left.childNodes.push(right);
        right.parent = left;
        op.parent = left;
        left.addMathmlNodes(op.mathml);
        left.addMathmlNodes(right.mathml);
        result = left;
    }
    else if (SemanticPred.isImplicitOp(right)) {
        debugger_1.Debugger.getInstance().output('Juxta Heuristic Case 7');
        right.contentNodes.unshift(op);
        right.childNodes.unshift(left);
        left.parent = right;
        op.parent = right;
        right.addMathmlNodes(op.mathml);
        right.addMathmlNodes(left.mathml);
        result = right;
    }
    else {
        debugger_1.Debugger.getInstance().output('Juxta Heuristic Case 8');
        result = SemanticHeuristics.factory.makeBranchNode("infixop", [left, right], [op], op.textContent);
        result.role = "implicit";
    }
    acc.push(result);
    return recurseJuxtaposition(acc.concat(first), ops, elements);
}


/***/ }),

/***/ 8122:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticMathml = void 0;
const DomUtil = __webpack_require__(6671);
const semantic_parser_1 = __webpack_require__(6098);
const SemanticPred = __webpack_require__(6161);
const semantic_processor_1 = __webpack_require__(7793);
const SemanticUtil = __webpack_require__(8901);
class SemanticMathml extends semantic_parser_1.SemanticAbstractParser {
    constructor() {
        super('MathML');
        this.parseMap_ = {
            SEMANTICS: this.semantics_.bind(this),
            MATH: this.rows_.bind(this),
            MROW: this.rows_.bind(this),
            MPADDED: this.rows_.bind(this),
            MSTYLE: this.rows_.bind(this),
            MFRAC: this.fraction_.bind(this),
            MSUB: this.limits_.bind(this),
            MSUP: this.limits_.bind(this),
            MSUBSUP: this.limits_.bind(this),
            MOVER: this.limits_.bind(this),
            MUNDER: this.limits_.bind(this),
            MUNDEROVER: this.limits_.bind(this),
            MROOT: this.root_.bind(this),
            MSQRT: this.sqrt_.bind(this),
            MTABLE: this.table_.bind(this),
            MLABELEDTR: this.tableLabeledRow_.bind(this),
            MTR: this.tableRow_.bind(this),
            MTD: this.tableCell_.bind(this),
            MS: this.text_.bind(this),
            MTEXT: this.text_.bind(this),
            MSPACE: this.space_.bind(this),
            'ANNOTATION-XML': this.text_.bind(this),
            MI: this.identifier_.bind(this),
            MN: this.number_.bind(this),
            MO: this.operator_.bind(this),
            MFENCED: this.fenced_.bind(this),
            MENCLOSE: this.enclosed_.bind(this),
            MMULTISCRIPTS: this.multiscripts_.bind(this),
            ANNOTATION: this.empty_.bind(this),
            NONE: this.empty_.bind(this),
            MACTION: this.action_.bind(this)
        };
        const meaning = {
            type: "identifier",
            role: "numbersetletter",
            font: "double-struck"
        };
        [
            'C',
            'H',
            'N',
            'P',
            'Q',
            'R',
            'Z',
            'ℂ',
            'ℍ',
            'ℕ',
            'ℙ',
            'ℚ',
            'ℝ',
            'ℤ'
        ].forEach(((x) => this.getFactory().defaultMap.add(x, meaning)).bind(this));
    }
    static getAttribute_(node, attr, def) {
        if (!node.hasAttribute(attr)) {
            return def;
        }
        const value = node.getAttribute(attr);
        if (value.match(/^\s*$/)) {
            return null;
        }
        return value;
    }
    parse(mml) {
        semantic_processor_1.default.getInstance().setNodeFactory(this.getFactory());
        const children = DomUtil.toArray(mml.childNodes);
        const tag = DomUtil.tagName(mml);
        const func = this.parseMap_[tag];
        const newNode = (func ? func : this.dummy_.bind(this))(mml, children);
        SemanticUtil.addAttributes(newNode, mml);
        if (['MATH', 'MROW', 'MPADDED', 'MSTYLE', 'SEMANTICS'].indexOf(tag) !== -1) {
            return newNode;
        }
        newNode.mathml.unshift(mml);
        newNode.mathmlTree = mml;
        return newNode;
    }
    semantics_(_node, children) {
        return children.length
            ? this.parse(children[0])
            : this.getFactory().makeEmptyNode();
    }
    rows_(node, children) {
        const semantics = node.getAttribute('semantics');
        if (semantics && semantics.match('bspr_')) {
            return semantic_processor_1.default.proof(node, semantics, this.parseList.bind(this));
        }
        children = SemanticUtil.purgeNodes(children);
        let newNode;
        if (children.length === 1) {
            newNode = this.parse(children[0]);
            if (newNode.type === "empty" && !newNode.mathmlTree) {
                newNode.mathmlTree = node;
            }
        }
        else {
            newNode = semantic_processor_1.default.getInstance().row(this.parseList(children));
        }
        newNode.mathml.unshift(node);
        return newNode;
    }
    fraction_(node, children) {
        if (!children.length) {
            return this.getFactory().makeEmptyNode();
        }
        const upper = this.parse(children[0]);
        const lower = children[1]
            ? this.parse(children[1])
            : this.getFactory().makeEmptyNode();
        const sem = semantic_processor_1.default.getInstance().fractionLikeNode(upper, lower, node.getAttribute('linethickness'), node.getAttribute('bevelled') === 'true');
        return sem;
    }
    limits_(node, children) {
        return semantic_processor_1.default.getInstance().limitNode(DomUtil.tagName(node), this.parseList(children));
    }
    root_(node, children) {
        if (!children[1]) {
            return this.sqrt_(node, children);
        }
        return this.getFactory().makeBranchNode("root", [this.parse(children[1]), this.parse(children[0])], []);
    }
    sqrt_(_node, children) {
        const semNodes = this.parseList(SemanticUtil.purgeNodes(children));
        return this.getFactory().makeBranchNode("sqrt", [semantic_processor_1.default.getInstance().row(semNodes)], []);
    }
    table_(node, children) {
        const semantics = node.getAttribute('semantics');
        if (semantics && semantics.match('bspr_')) {
            return semantic_processor_1.default.proof(node, semantics, this.parseList.bind(this));
        }
        const newNode = this.getFactory().makeBranchNode("table", this.parseList(children), []);
        newNode.mathmlTree = node;
        semantic_processor_1.default.tableToMultiline(newNode);
        return newNode;
    }
    tableRow_(_node, children) {
        const newNode = this.getFactory().makeBranchNode("row", this.parseList(children), []);
        newNode.role = "table";
        return newNode;
    }
    tableLabeledRow_(node, children) {
        if (!children.length) {
            return this.tableRow_(node, children);
        }
        const label = this.parse(children[0]);
        label.role = "label";
        const newNode = this.getFactory().makeBranchNode("row", this.parseList(children.slice(1)), [label]);
        newNode.role = "table";
        return newNode;
    }
    tableCell_(_node, children) {
        const semNodes = this.parseList(SemanticUtil.purgeNodes(children));
        let childNodes;
        if (!semNodes.length) {
            childNodes = [];
        }
        else if (semNodes.length === 1 &&
            SemanticPred.isType(semNodes[0], "empty")) {
            childNodes = semNodes;
        }
        else {
            childNodes = [semantic_processor_1.default.getInstance().row(semNodes)];
        }
        const newNode = this.getFactory().makeBranchNode("cell", childNodes, []);
        newNode.role = "table";
        return newNode;
    }
    space_(node, children) {
        const width = node.getAttribute('width');
        const match = width && width.match(/[a-z]*$/);
        if (!match) {
            return this.empty_(node, children);
        }
        const sizes = {
            cm: 0.4,
            pc: 0.5,
            em: 0.5,
            ex: 1,
            in: 0.15,
            pt: 5,
            mm: 5
        };
        const unit = match[0];
        const measure = parseFloat(width.slice(0, match.index));
        const size = sizes[unit];
        if (!size || isNaN(measure) || measure < size) {
            return this.empty_(node, children);
        }
        const newNode = this.getFactory().makeUnprocessed(node);
        return semantic_processor_1.default.getInstance().text(newNode, DomUtil.tagName(node));
    }
    text_(node, children) {
        const newNode = this.leaf_(node, children);
        if (!node.textContent) {
            return newNode;
        }
        newNode.updateContent(node.textContent, true);
        return semantic_processor_1.default.getInstance().text(newNode, DomUtil.tagName(node));
    }
    identifier_(node, children) {
        const newNode = this.leaf_(node, children);
        return semantic_processor_1.default.getInstance().identifierNode(newNode, semantic_processor_1.default.getInstance().font(node.getAttribute('mathvariant')), node.getAttribute('class'));
    }
    number_(node, children) {
        const newNode = this.leaf_(node, children);
        semantic_processor_1.default.number(newNode);
        return newNode;
    }
    operator_(node, children) {
        const newNode = this.leaf_(node, children);
        semantic_processor_1.default.getInstance().operatorNode(newNode);
        return newNode;
    }
    fenced_(node, children) {
        const semNodes = this.parseList(SemanticUtil.purgeNodes(children));
        const sepValue = SemanticMathml.getAttribute_(node, 'separators', ',');
        const open = SemanticMathml.getAttribute_(node, 'open', '(');
        const close = SemanticMathml.getAttribute_(node, 'close', ')');
        const newNode = semantic_processor_1.default.getInstance().mfenced(open, close, sepValue, semNodes);
        const nodes = semantic_processor_1.default.getInstance().tablesInRow([newNode]);
        return nodes[0];
    }
    enclosed_(node, children) {
        const semNodes = this.parseList(SemanticUtil.purgeNodes(children));
        const newNode = this.getFactory().makeBranchNode("enclose", [semantic_processor_1.default.getInstance().row(semNodes)], []);
        newNode.role =
            node.getAttribute('notation') || "unknown";
        return newNode;
    }
    multiscripts_(_node, children) {
        if (!children.length) {
            return this.getFactory().makeEmptyNode();
        }
        const base = this.parse(children.shift());
        if (!children.length) {
            return base;
        }
        const lsup = [];
        const lsub = [];
        const rsup = [];
        const rsub = [];
        let prescripts = false;
        let scriptcount = 0;
        for (let i = 0, child; (child = children[i]); i++) {
            if (DomUtil.tagName(child) === 'MPRESCRIPTS') {
                prescripts = true;
                scriptcount = 0;
                continue;
            }
            prescripts
                ? scriptcount & 1
                    ? lsup.push(child)
                    : lsub.push(child)
                : scriptcount & 1
                    ? rsup.push(child)
                    : rsub.push(child);
            scriptcount++;
        }
        if (!SemanticUtil.purgeNodes(lsup).length &&
            !SemanticUtil.purgeNodes(lsub).length) {
            return semantic_processor_1.default.getInstance().pseudoTensor(base, this.parseList(rsub), this.parseList(rsup));
        }
        return semantic_processor_1.default.getInstance().tensor(base, this.parseList(lsub), this.parseList(lsup), this.parseList(rsub), this.parseList(rsup));
    }
    empty_(_node, _children) {
        return this.getFactory().makeEmptyNode();
    }
    action_(node, children) {
        return children.length > 1
            ? this.parse(children[1])
            : this.getFactory().makeUnprocessed(node);
    }
    dummy_(node, _children) {
        const unknown = this.getFactory().makeUnprocessed(node);
        unknown.role = node.tagName;
        unknown.textContent = node.textContent;
        return unknown;
    }
    leaf_(mml, children) {
        if (children.length === 1 &&
            children[0].nodeType !== DomUtil.NodeType.TEXT_NODE) {
            const node = this.getFactory().makeUnprocessed(mml);
            node.role = children[0].tagName;
            SemanticUtil.addAttributes(node, children[0]);
            return node;
        }
        return this.getFactory().makeLeafNode(mml.textContent, semantic_processor_1.default.getInstance().font(mml.getAttribute('mathvariant')));
    }
}
exports.SemanticMathml = SemanticMathml;


/***/ }),

/***/ 9444:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticNode = void 0;
const DomUtil = __webpack_require__(6671);
const semantic_attr_1 = __webpack_require__(4020);
const SemanticUtil = __webpack_require__(8901);
class SemanticNode {
    constructor(id) {
        this.id = id;
        this.mathml = [];
        this.parent = null;
        this.type = "unknown";
        this.role = "unknown";
        this.font = "unknown";
        this.embellished = null;
        this.fencePointer = '';
        this.childNodes = [];
        this.textContent = '';
        this.mathmlTree = null;
        this.contentNodes = [];
        this.annotation = {};
        this.attributes = {};
        this.nobreaking = false;
    }
    static fromXml(xml) {
        const id = parseInt(xml.getAttribute('id'), 10);
        const node = new SemanticNode(id);
        node.type = xml.tagName;
        SemanticNode.setAttribute(node, xml, 'role');
        SemanticNode.setAttribute(node, xml, 'font');
        SemanticNode.setAttribute(node, xml, 'embellished');
        SemanticNode.setAttribute(node, xml, 'fencepointer', 'fencePointer');
        if (xml.getAttribute('annotation')) {
            node.parseAnnotation(xml.getAttribute('annotation'));
        }
        SemanticUtil.addAttributes(node, xml);
        SemanticNode.processChildren(node, xml);
        return node;
    }
    static setAttribute(node, xml, attribute, opt_name) {
        opt_name = opt_name || attribute;
        const value = xml.getAttribute(attribute);
        if (value) {
            node[opt_name] = value;
        }
    }
    static processChildren(node, xml) {
        for (const child of DomUtil.toArray(xml.childNodes)) {
            if (child.nodeType === DomUtil.NodeType.TEXT_NODE) {
                node.textContent = child.textContent;
                continue;
            }
            const children = DomUtil.toArray(child.childNodes).map(SemanticNode.fromXml);
            children.forEach((x) => (x.parent = node));
            if (DomUtil.tagName(child) === 'CONTENT') {
                node.contentNodes = children;
            }
            else {
                node.childNodes = children;
            }
        }
    }
    querySelectorAll(pred) {
        let result = [];
        for (let i = 0, child; (child = this.childNodes[i]); i++) {
            result = result.concat(child.querySelectorAll(pred));
        }
        for (let i = 0, content; (content = this.contentNodes[i]); i++) {
            result = result.concat(content.querySelectorAll(pred));
        }
        if (pred(this)) {
            result.unshift(this);
        }
        return result;
    }
    xml(xml, brief) {
        const xmlNodeList = function (tag, nodes) {
            const xmlNodes = nodes.map(function (x) {
                return x.xml(xml, brief);
            });
            const tagNode = xml.createElementNS('', tag);
            for (let i = 0, child; (child = xmlNodes[i]); i++) {
                tagNode.appendChild(child);
            }
            return tagNode;
        };
        const node = xml.createElementNS('', this.type);
        if (!brief) {
            this.xmlAttributes(node);
        }
        node.textContent = this.textContent;
        if (this.contentNodes.length > 0) {
            node.appendChild(xmlNodeList("content", this.contentNodes));
        }
        if (this.childNodes.length > 0) {
            node.appendChild(xmlNodeList("children", this.childNodes));
        }
        return node;
    }
    toString(brief = false) {
        const xml = DomUtil.parseInput('<snode/>');
        return DomUtil.serializeXml(this.xml(xml, brief));
    }
    allAttributes() {
        const attributes = [];
        attributes.push(["role", this.role]);
        if (this.font !== "unknown") {
            attributes.push(["font", this.font]);
        }
        if (Object.keys(this.annotation).length) {
            attributes.push(["annotation", this.xmlAnnotation()]);
        }
        if (this.embellished) {
            attributes.push(["embellished", this.embellished]);
        }
        if (this.fencePointer) {
            attributes.push(["fencepointer", this.fencePointer]);
        }
        attributes.push(["id", this.id.toString()]);
        return attributes;
    }
    xmlAnnotation() {
        const result = [];
        for (const key in this.annotation) {
            this.annotation[key].forEach(function (mean) {
                result.push(key + ':' + mean);
            });
        }
        return result.join(';');
    }
    toJson() {
        const json = {};
        json["type"] = this.type;
        const attributes = this.allAttributes();
        for (let i = 0, attr; (attr = attributes[i]); i++) {
            json[attr[0]] = attr[1].toString();
        }
        if (this.textContent) {
            json["$t"] = this.textContent;
        }
        if (this.childNodes.length) {
            json["children"] = this.childNodes.map(function (child) {
                return child.toJson();
            });
        }
        if (this.contentNodes.length) {
            json["content"] = this.contentNodes.map(function (child) {
                return child.toJson();
            });
        }
        return json;
    }
    updateContent(content, text) {
        const newContent = text
            ? content
                .replace(/^[ \f\n\r\t\v\u200b]*/, '')
                .replace(/[ \f\n\r\t\v\u200b]*$/, '')
            : content.trim();
        content = content && !newContent ? content : newContent;
        if (this.textContent === content) {
            return;
        }
        const meaning = (0, semantic_attr_1.lookupMeaning)(content);
        this.textContent = content;
        this.role = meaning.role;
        this.type = meaning.type;
        this.font = meaning.font;
    }
    addMathmlNodes(mmlNodes) {
        for (let i = 0, mml; (mml = mmlNodes[i]); i++) {
            if (this.mathml.indexOf(mml) === -1) {
                this.mathml.push(mml);
            }
        }
    }
    appendChild(child) {
        this.childNodes.push(child);
        this.addMathmlNodes(child.mathml);
        child.parent = this;
    }
    replaceChild(oldNode, newNode) {
        const index = this.childNodes.indexOf(oldNode);
        if (index === -1) {
            return;
        }
        oldNode.parent = null;
        newNode.parent = this;
        this.childNodes[index] = newNode;
        const removeMathml = oldNode.mathml.filter(function (x) {
            return newNode.mathml.indexOf(x) === -1;
        });
        const addMathml = newNode.mathml.filter(function (x) {
            return oldNode.mathml.indexOf(x) === -1;
        });
        this.removeMathmlNodes(removeMathml);
        this.addMathmlNodes(addMathml);
    }
    appendContentNode(node) {
        if (node) {
            this.contentNodes.push(node);
            this.addMathmlNodes(node.mathml);
            node.parent = this;
        }
    }
    removeContentNode(node) {
        if (node) {
            const index = this.contentNodes.indexOf(node);
            if (index !== -1) {
                this.contentNodes.slice(index, 1);
            }
        }
    }
    equals(node) {
        if (!node) {
            return false;
        }
        if (this.type !== node.type ||
            this.role !== node.role ||
            this.textContent !== node.textContent ||
            this.childNodes.length !== node.childNodes.length ||
            this.contentNodes.length !== node.contentNodes.length) {
            return false;
        }
        for (let i = 0, node1, node2; (node1 = this.childNodes[i]), (node2 = node.childNodes[i]); i++) {
            if (!node1.equals(node2)) {
                return false;
            }
        }
        for (let i = 0, node1, node2; (node1 = this.contentNodes[i]), (node2 = node.contentNodes[i]); i++) {
            if (!node1.equals(node2)) {
                return false;
            }
        }
        return true;
    }
    displayTree() {
        console.info(this.displayTree_(0));
    }
    addAnnotation(domain, annotation) {
        if (annotation) {
            this.addAnnotation_(domain, annotation);
        }
    }
    getAnnotation(domain) {
        const content = this.annotation[domain];
        return content ? content : [];
    }
    hasAnnotation(domain, annotation) {
        const content = this.annotation[domain];
        if (!content) {
            return false;
        }
        return content.indexOf(annotation) !== -1;
    }
    parseAnnotation(stateStr) {
        const annotations = stateStr.split(';');
        for (let i = 0, l = annotations.length; i < l; i++) {
            const annotation = annotations[i].split(':');
            this.addAnnotation(annotation[0], annotation[1]);
        }
    }
    meaning() {
        return { type: this.type, role: this.role, font: this.font };
    }
    xmlAttributes(node) {
        const attributes = this.allAttributes();
        for (let i = 0, attr; (attr = attributes[i]); i++) {
            node.setAttribute(attr[0], attr[1]);
        }
        this.addExternalAttributes(node);
    }
    addExternalAttributes(node) {
        for (const attr in this.attributes) {
            node.setAttribute(attr, this.attributes[attr]);
        }
    }
    removeMathmlNodes(mmlNodes) {
        const mmlList = this.mathml;
        for (let i = 0, mml; (mml = mmlNodes[i]); i++) {
            const index = mmlList.indexOf(mml);
            if (index !== -1) {
                mmlList.splice(index, 1);
            }
        }
        this.mathml = mmlList;
    }
    displayTree_(depth) {
        depth++;
        const depthString = Array(depth).join('  ');
        let result = '';
        result += '\n' + depthString + this.toString();
        result += '\n' + depthString + 'MathmlTree:';
        result += '\n' + depthString + this.mathmlTreeString();
        result += '\n' + depthString + 'MathML:';
        for (let i = 0, mml; (mml = this.mathml[i]); i++) {
            result += '\n' + depthString + mml.toString();
        }
        result += '\n' + depthString + 'Begin Content';
        this.contentNodes.forEach(function (x) {
            result += x.displayTree_(depth);
        });
        result += '\n' + depthString + 'End Content';
        result += '\n' + depthString + 'Begin Children';
        this.childNodes.forEach(function (x) {
            result += x.displayTree_(depth);
        });
        result += '\n' + depthString + 'End Children';
        return result;
    }
    mathmlTreeString() {
        return this.mathmlTree ? this.mathmlTree.toString() : 'EMPTY';
    }
    addAnnotation_(domain, annotation) {
        const content = this.annotation[domain];
        if (content) {
            content.push(annotation);
        }
        else {
            this.annotation[domain] = [annotation];
        }
    }
}
exports.SemanticNode = SemanticNode;


/***/ }),

/***/ 4790:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticNodeFactory = void 0;
const semantic_default_1 = __webpack_require__(7405);
const semantic_default_2 = __webpack_require__(7405);
const semantic_node_1 = __webpack_require__(9444);
class SemanticNodeFactory {
    constructor() {
        this.leafMap = new semantic_default_2.SemanticNodeCollator();
        this.defaultMap = new semantic_default_1.SemanticDefault();
        this.idCounter_ = -1;
    }
    makeNode(id) {
        return this.createNode_(id);
    }
    makeUnprocessed(mml) {
        const node = this.createNode_();
        node.mathml = [mml];
        node.mathmlTree = mml;
        return node;
    }
    makeEmptyNode() {
        const node = this.createNode_();
        node.type = "empty";
        return node;
    }
    makeContentNode(content) {
        const node = this.createNode_();
        node.updateContent(content);
        return node;
    }
    makeMultipleContentNodes(num, content) {
        const nodes = [];
        for (let i = 0; i < num; i++) {
            nodes.push(this.makeContentNode(content));
        }
        return nodes;
    }
    makeLeafNode(content, font) {
        if (!content) {
            return this.makeEmptyNode();
        }
        const node = this.makeContentNode(content);
        node.font = font || node.font;
        const meaning = this.defaultMap.retrieveNode(node);
        if (meaning) {
            node.type = meaning.type;
            node.role = meaning.role;
            node.font = meaning.font;
        }
        this.leafMap.addNode(node);
        return node;
    }
    makeBranchNode(type, children, contentNodes, opt_content) {
        const node = this.createNode_();
        if (opt_content) {
            node.updateContent(opt_content);
        }
        node.type = type;
        node.childNodes = children;
        node.contentNodes = contentNodes;
        children.concat(contentNodes).forEach(function (x) {
            x.parent = node;
            node.addMathmlNodes(x.mathml);
        });
        return node;
    }
    createNode_(id) {
        if (typeof id !== 'undefined') {
            this.idCounter_ = Math.max(this.idCounter_, id);
        }
        else {
            id = ++this.idCounter_;
        }
        return new semantic_node_1.SemanticNode(id);
    }
}
exports.SemanticNodeFactory = SemanticNodeFactory;


/***/ }),

/***/ 178:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticComparator = exports.reduce = exports.sort = exports.apply = exports.add = void 0;
const comparators = [];
function add(comparator) {
    comparators.push(comparator);
}
exports.add = add;
function apply(meaning1, meaning2) {
    for (let i = 0, comparator; (comparator = comparators[i]); i++) {
        const result = comparator.compare(meaning1, meaning2);
        if (result !== 0) {
            return result;
        }
    }
    return 0;
}
exports.apply = apply;
function sort(meanings) {
    meanings.sort(apply);
}
exports.sort = sort;
function reduce(meanings) {
    if (meanings.length <= 1) {
        return meanings;
    }
    const copy = meanings.slice();
    sort(copy);
    const result = [];
    let last;
    do {
        last = copy.pop();
        result.push(last);
    } while (last && copy.length && apply(copy[copy.length - 1], last) === 0);
    return result;
}
exports.reduce = reduce;
class SemanticComparator {
    constructor(comparator, type = null) {
        this.comparator = comparator;
        this.type = type;
        add(this);
    }
    compare(meaning1, meaning2) {
        return this.type &&
            this.type === meaning1.type &&
            this.type === meaning2.type
            ? this.comparator(meaning1, meaning2)
            : 0;
    }
}
exports.SemanticComparator = SemanticComparator;
function simpleFunction(meaning1, meaning2) {
    if (meaning1.role === "simple function") {
        return 1;
    }
    if (meaning2.role === "simple function") {
        return -1;
    }
    return 0;
}
new SemanticComparator(simpleFunction, "identifier");


/***/ }),

/***/ 6098:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticAbstractParser = void 0;
const semantic_node_factory_1 = __webpack_require__(4790);
class SemanticAbstractParser {
    constructor(type) {
        this.type = type;
        this.factory_ = new semantic_node_factory_1.SemanticNodeFactory();
    }
    getFactory() {
        return this.factory_;
    }
    setFactory(factory) {
        this.factory_ = factory;
    }
    getType() {
        return this.type;
    }
    parseList(list) {
        const result = [];
        for (let i = 0, element; (element = list[i]); i++) {
            result.push(this.parse(element));
        }
        return result;
    }
}
exports.SemanticAbstractParser = SemanticAbstractParser;


/***/ }),

/***/ 6161:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.isMembership = exports.elligibleRightNeutral = exports.elligibleLeftNeutral = exports.compareNeutralFences = exports.isNeutralFence = exports.isImplicitOp = exports.isImplicit = exports.isPureUnit = exports.isUnitCounter = exports.isNumber = exports.isSingletonSetContent = exports.scriptedElement_ = exports.illegalSingleton_ = exports.isSetNode = exports.isRightBrace = exports.isLeftBrace = exports.isSimpleFunction = exports.singlePunctAtPosition = exports.isSimpleFunctionHead = exports.isLimitBase = exports.isBinomial = exports.lineIsLabelled = exports.tableIsMultiline = exports.tableIsCases = exports.isFencedElement = exports.tableIsMatrixOrVector = exports.isTableOrMultiline = exports.isElligibleEmbellishedFence = exports.isFence = exports.isPunctuation = exports.isRelation = exports.isOperator = exports.isEmbellished = exports.isGeneralFunctionBoundary = exports.isIntegralDxBoundarySingle = exports.isIntegralDxBoundary = exports.isBigOpBoundary = exports.isPrefixFunctionBoundary = exports.isSimpleFunctionScope = exports.isAccent = exports.isRole = exports.embellishedType = exports.isType = void 0;
const SemanticAttr = __webpack_require__(4020);
const semantic_util_1 = __webpack_require__(8901);
function isType(node, attr) {
    return node.type === attr;
}
exports.isType = isType;
function embellishedType(node, attr) {
    return node.embellished === attr;
}
exports.embellishedType = embellishedType;
function isRole(node, attr) {
    return node.role === attr;
}
exports.isRole = isRole;
function isAccent(node) {
    const inftyReg = new RegExp('∞|᪲');
    return (isType(node, "fence") ||
        isType(node, "punctuation") ||
        (isType(node, "operator") &&
            !node.textContent.match(inftyReg)) ||
        isType(node, "relation") ||
        (isType(node, "identifier") &&
            isRole(node, "unknown") &&
            !node.textContent.match(SemanticAttr.allLettersRegExp) &&
            !node.textContent.match(inftyReg)));
}
exports.isAccent = isAccent;
function isSimpleFunctionScope(node) {
    const children = node.childNodes;
    if (children.length === 0) {
        return true;
    }
    if (children.length > 1) {
        return false;
    }
    const child = children[0];
    if (child.type === "infixop") {
        if (child.role !== "implicit") {
            return false;
        }
        if (child.childNodes.some((x) => isType(x, "infixop"))) {
            return false;
        }
    }
    return true;
}
exports.isSimpleFunctionScope = isSimpleFunctionScope;
function isPrefixFunctionBoundary(node) {
    return ((isOperator(node) && !isRole(node, "division")) ||
        isType(node, "appl") ||
        isGeneralFunctionBoundary(node));
}
exports.isPrefixFunctionBoundary = isPrefixFunctionBoundary;
function isBigOpBoundary(node) {
    return isOperator(node) || isGeneralFunctionBoundary(node);
}
exports.isBigOpBoundary = isBigOpBoundary;
function isIntegralDxBoundary(firstNode, secondNode) {
    return (!!secondNode &&
        isType(secondNode, "identifier") &&
        SemanticAttr.lookupSecondary('d', firstNode.textContent));
}
exports.isIntegralDxBoundary = isIntegralDxBoundary;
function isIntegralDxBoundarySingle(node) {
    if (isType(node, "identifier")) {
        const firstChar = node.textContent[0];
        return (firstChar &&
            node.textContent[1] &&
            SemanticAttr.lookupSecondary('d', firstChar));
    }
    return false;
}
exports.isIntegralDxBoundarySingle = isIntegralDxBoundarySingle;
function isGeneralFunctionBoundary(node) {
    return isRelation(node) || isPunctuation(node);
}
exports.isGeneralFunctionBoundary = isGeneralFunctionBoundary;
function isEmbellished(node) {
    if (node.embellished) {
        return node.embellished;
    }
    if (SemanticAttr.isEmbellishedType(node.type)) {
        return node.type;
    }
    return null;
}
exports.isEmbellished = isEmbellished;
function isOperator(node) {
    return (isType(node, "operator") ||
        embellishedType(node, "operator"));
}
exports.isOperator = isOperator;
function isRelation(node) {
    return (isType(node, "relation") ||
        embellishedType(node, "relation"));
}
exports.isRelation = isRelation;
function isPunctuation(node) {
    return (isType(node, "punctuation") ||
        embellishedType(node, "punctuation"));
}
exports.isPunctuation = isPunctuation;
function isFence(node) {
    return (isType(node, "fence") ||
        embellishedType(node, "fence"));
}
exports.isFence = isFence;
function isElligibleEmbellishedFence(node) {
    if (!node || !isFence(node)) {
        return false;
    }
    if (!node.embellished) {
        return true;
    }
    return recurseBaseNode(node);
}
exports.isElligibleEmbellishedFence = isElligibleEmbellishedFence;
function bothSide(node) {
    return (isType(node, "tensor") &&
        (!isType(node.childNodes[1], "empty") ||
            !isType(node.childNodes[2], "empty")) &&
        (!isType(node.childNodes[3], "empty") ||
            !isType(node.childNodes[4], "empty")));
}
function recurseBaseNode(node) {
    if (!node.embellished) {
        return true;
    }
    if (bothSide(node)) {
        return false;
    }
    if (isRole(node, "close") && isType(node, "tensor")) {
        return false;
    }
    if (isRole(node, "open") &&
        (isType(node, "subscript") ||
            isType(node, "superscript"))) {
        return false;
    }
    return recurseBaseNode(node.childNodes[0]);
}
function isTableOrMultiline(node) {
    return (!!node &&
        (isType(node, "table") || isType(node, "multiline")));
}
exports.isTableOrMultiline = isTableOrMultiline;
function tableIsMatrixOrVector(node) {
    return (!!node && isFencedElement(node) && isTableOrMultiline(node.childNodes[0]));
}
exports.tableIsMatrixOrVector = tableIsMatrixOrVector;
function isFencedElement(node) {
    return (!!node &&
        isType(node, "fenced") &&
        (isRole(node, "leftright") || isNeutralFence(node)) &&
        node.childNodes.length === 1);
}
exports.isFencedElement = isFencedElement;
function tableIsCases(_table, prevNodes) {
    return (prevNodes.length > 0 &&
        isRole(prevNodes[prevNodes.length - 1], "openfence"));
}
exports.tableIsCases = tableIsCases;
function tableIsMultiline(table) {
    return table.childNodes.every(function (row) {
        const length = row.childNodes.length;
        return length <= 1;
    });
}
exports.tableIsMultiline = tableIsMultiline;
function lineIsLabelled(line) {
    return (isType(line, "line") &&
        line.contentNodes.length &&
        isRole(line.contentNodes[0], "label"));
}
exports.lineIsLabelled = lineIsLabelled;
function isBinomial(table) {
    return table.childNodes.length === 2;
}
exports.isBinomial = isBinomial;
function isLimitBase(node) {
    return (isType(node, "largeop") ||
        isType(node, "limboth") ||
        isType(node, "limlower") ||
        isType(node, "limupper") ||
        (isType(node, "function") &&
            isRole(node, "limit function")) ||
        ((isType(node, "overscore") ||
            isType(node, "underscore")) &&
            isLimitBase(node.childNodes[0])));
}
exports.isLimitBase = isLimitBase;
function isSimpleFunctionHead(node) {
    return (node.type === "identifier" ||
        node.role === "latinletter" ||
        node.role === "greekletter" ||
        node.role === "otherletter");
}
exports.isSimpleFunctionHead = isSimpleFunctionHead;
function singlePunctAtPosition(nodes, puncts, position) {
    return (puncts.length === 1 &&
        (nodes[position].type === "punctuation" ||
            nodes[position].embellished === "punctuation") &&
        nodes[position] === puncts[0]);
}
exports.singlePunctAtPosition = singlePunctAtPosition;
function isSimpleFunction(node) {
    return (isType(node, "identifier") &&
        isRole(node, "simple function"));
}
exports.isSimpleFunction = isSimpleFunction;
function isLeftBrace(node) {
    const leftBrace = ['{', '﹛', '｛'];
    return !!node && leftBrace.indexOf(node.textContent) !== -1;
}
exports.isLeftBrace = isLeftBrace;
function isRightBrace(node) {
    const rightBrace = ['}', '﹜', '｝'];
    return !!node && rightBrace.indexOf(node.textContent) !== -1;
}
exports.isRightBrace = isRightBrace;
function isSetNode(node) {
    return (isLeftBrace(node.contentNodes[0]) && isRightBrace(node.contentNodes[1]));
}
exports.isSetNode = isSetNode;
exports.illegalSingleton_ = [
    "punctuation",
    "punctuated",
    "relseq",
    "multirel",
    "table",
    "multiline",
    "cases",
    "inference"
];
exports.scriptedElement_ = [
    "limupper",
    "limlower",
    "limboth",
    "subscript",
    "superscript",
    "underscore",
    "overscore",
    "tensor"
];
function isSingletonSetContent(node) {
    const type = node.type;
    if (exports.illegalSingleton_.indexOf(type) !== -1 ||
        (type === "infixop" && node.role !== "implicit")) {
        return false;
    }
    if (type === "fenced") {
        return node.role === "leftright"
            ? isSingletonSetContent(node.childNodes[0])
            : true;
    }
    if (exports.scriptedElement_.indexOf(type) !== -1) {
        return isSingletonSetContent(node.childNodes[0]);
    }
    return true;
}
exports.isSingletonSetContent = isSingletonSetContent;
function isNumber(node) {
    return (node.type === "number" &&
        (node.role === "integer" || node.role === "float"));
}
exports.isNumber = isNumber;
function isUnitCounter(node) {
    return (isNumber(node) ||
        node.role === "vulgar" ||
        node.role === "mixed");
}
exports.isUnitCounter = isUnitCounter;
function isPureUnit(node) {
    const children = node.childNodes;
    return (node.role === "unit" &&
        (!children.length || children[0].role === "unit"));
}
exports.isPureUnit = isPureUnit;
function isImplicit(node) {
    return (node.role === "implicit" ||
        (node.role === "unit" &&
            !!node.contentNodes.length &&
            node.contentNodes[0].textContent === SemanticAttr.invisibleTimes()));
}
exports.isImplicit = isImplicit;
function isImplicitOp(node) {
    return (node.type === "infixop" && node.role === "implicit");
}
exports.isImplicitOp = isImplicitOp;
function isNeutralFence(fence) {
    return (fence.role === "neutral" || fence.role === "metric");
}
exports.isNeutralFence = isNeutralFence;
function compareNeutralFences(fence1, fence2) {
    return (isNeutralFence(fence1) &&
        isNeutralFence(fence2) &&
        (0, semantic_util_1.getEmbellishedInner)(fence1).textContent ===
            (0, semantic_util_1.getEmbellishedInner)(fence2).textContent);
}
exports.compareNeutralFences = compareNeutralFences;
function elligibleLeftNeutral(fence) {
    if (!isNeutralFence(fence)) {
        return false;
    }
    if (!fence.embellished) {
        return true;
    }
    if (fence.type === "superscript" ||
        fence.type === "subscript") {
        return false;
    }
    if (fence.type === "tensor" &&
        (fence.childNodes[3].type !== "empty" ||
            fence.childNodes[4].type !== "empty")) {
        return false;
    }
    return true;
}
exports.elligibleLeftNeutral = elligibleLeftNeutral;
function elligibleRightNeutral(fence) {
    if (!isNeutralFence(fence)) {
        return false;
    }
    if (!fence.embellished) {
        return true;
    }
    if (fence.type === "tensor" &&
        (fence.childNodes[1].type !== "empty" ||
            fence.childNodes[2].type !== "empty")) {
        return false;
    }
    return true;
}
exports.elligibleRightNeutral = elligibleRightNeutral;
function isMembership(element) {
    return [
        "element",
        "nonelement",
        "reelement",
        "renonelement"
    ].includes(element.role);
}
exports.isMembership = isMembership;


/***/ }),

/***/ 7793:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const DomUtil = __webpack_require__(6671);
const SemanticAttr = __webpack_require__(4020);
const SemanticHeuristics = __webpack_require__(2721);
const semantic_node_factory_1 = __webpack_require__(4790);
const SemanticPred = __webpack_require__(6161);
const SemanticUtil = __webpack_require__(8901);
class SemanticProcessor {
    constructor() {
        this.funcAppls = {};
        this.factory_ = new semantic_node_factory_1.SemanticNodeFactory();
        SemanticHeuristics.updateFactory(this.factory_);
    }
    static getInstance() {
        SemanticProcessor.instance =
            SemanticProcessor.instance || new SemanticProcessor();
        return SemanticProcessor.instance;
    }
    static tableToMultiline(table) {
        if (!SemanticPred.tableIsMultiline(table)) {
            SemanticProcessor.classifyTable(table);
            return;
        }
        table.type = "multiline";
        for (let i = 0, row; (row = table.childNodes[i]); i++) {
            SemanticProcessor.rowToLine_(row, "multiline");
        }
        if (table.childNodes.length === 1 &&
            !SemanticPred.lineIsLabelled(table.childNodes[0]) &&
            SemanticPred.isFencedElement(table.childNodes[0].childNodes[0])) {
            SemanticProcessor.tableToMatrixOrVector_(SemanticProcessor.rewriteFencedLine_(table));
        }
        SemanticProcessor.binomialForm_(table);
        SemanticProcessor.classifyMultiline(table);
    }
    static number(node) {
        if (node.type === "unknown" ||
            node.type === "identifier") {
            node.type = "number";
        }
        SemanticProcessor.numberRole_(node);
        SemanticProcessor.exprFont_(node);
    }
    static classifyMultiline(multiline) {
        let index = 0;
        const length = multiline.childNodes.length;
        let line;
        while (index < length &&
            (!(line = multiline.childNodes[index]) || !line.childNodes.length)) {
            index++;
        }
        if (index >= length) {
            return;
        }
        const firstRole = line.childNodes[0].role;
        if (firstRole !== "unknown" &&
            multiline.childNodes.every(function (x) {
                const cell = x.childNodes[0];
                return (!cell ||
                    (cell.role === firstRole &&
                        (SemanticPred.isType(cell, "relation") ||
                            SemanticPred.isType(cell, "relseq"))));
            })) {
            multiline.role = firstRole;
        }
    }
    static classifyTable(table) {
        const columns = SemanticProcessor.computeColumns_(table);
        SemanticProcessor.classifyByColumns_(table, columns, "equality") ||
            SemanticProcessor.classifyByColumns_(table, columns, "inequality", ["equality"]) ||
            SemanticProcessor.classifyByColumns_(table, columns, "arrow") ||
            SemanticProcessor.detectCaleyTable(table);
    }
    static detectCaleyTable(table) {
        if (!table.mathmlTree) {
            return false;
        }
        const tree = table.mathmlTree;
        const cl = tree.getAttribute('columnlines');
        const rl = tree.getAttribute('rowlines');
        if (!cl || !rl) {
            return false;
        }
        if (SemanticProcessor.cayleySpacing(cl) &&
            SemanticProcessor.cayleySpacing(rl)) {
            table.role = "cayley";
            return true;
        }
        return false;
    }
    static cayleySpacing(lines) {
        const list = lines.split(' ');
        return ((list[0] === 'solid' || list[0] === 'dashed') &&
            list.slice(1).every((x) => x === 'none'));
    }
    static proof(node, semantics, parse) {
        const attrs = SemanticProcessor.separateSemantics(semantics);
        return SemanticProcessor.getInstance().proof(node, attrs, parse);
    }
    static findSemantics(node, attr, opt_value) {
        const value = opt_value == null ? null : opt_value;
        const semantics = SemanticProcessor.getSemantics(node);
        if (!semantics) {
            return false;
        }
        if (!semantics[attr]) {
            return false;
        }
        return value == null ? true : semantics[attr] === value;
    }
    static getSemantics(node) {
        const semantics = node.getAttribute('semantics');
        if (!semantics) {
            return null;
        }
        return SemanticProcessor.separateSemantics(semantics);
    }
    static removePrefix(name) {
        const [, ...rest] = name.split('_');
        return rest.join('_');
    }
    static separateSemantics(attr) {
        const result = {};
        attr.split(';').forEach(function (x) {
            const [name, value] = x.split(':');
            result[SemanticProcessor.removePrefix(name)] = value;
        });
        return result;
    }
    static matchSpaces_(nodes, ops) {
        for (let i = 0, op; (op = ops[i]); i++) {
            const node = nodes[i];
            const mt1 = node.mathmlTree;
            const mt2 = nodes[i + 1].mathmlTree;
            if (!mt1 || !mt2) {
                continue;
            }
            const sibling = mt1.nextSibling;
            if (!sibling || sibling === mt2) {
                continue;
            }
            const spacer = SemanticProcessor.getSpacer_(sibling);
            if (spacer) {
                op.mathml.push(spacer);
                op.mathmlTree = spacer;
                op.role = "space";
            }
        }
    }
    static getSpacer_(node) {
        if (DomUtil.tagName(node) === 'MSPACE') {
            return node;
        }
        while (SemanticUtil.hasEmptyTag(node) && node.childNodes.length === 1) {
            node = node.childNodes[0];
            if (DomUtil.tagName(node) === 'MSPACE') {
                return node;
            }
        }
        return null;
    }
    static fenceToPunct_(fence) {
        const newRole = SemanticProcessor.FENCE_TO_PUNCT_[fence.role];
        if (!newRole) {
            return;
        }
        while (fence.embellished) {
            fence.embellished = "punctuation";
            if (!(SemanticPred.isRole(fence, "subsup") ||
                SemanticPred.isRole(fence, "underover"))) {
                fence.role = newRole;
            }
            fence = fence.childNodes[0];
        }
        fence.type = "punctuation";
        fence.role = newRole;
    }
    static classifyFunction_(funcNode, restNodes) {
        if (funcNode.type === "appl" ||
            funcNode.type === "bigop" ||
            funcNode.type === "integral") {
            return '';
        }
        if (restNodes[0] &&
            restNodes[0].textContent === SemanticAttr.functionApplication()) {
            SemanticProcessor.getInstance().funcAppls[funcNode.id] =
                restNodes.shift();
            let role = "simple function";
            SemanticHeuristics.run('simple2prefix', funcNode);
            if (funcNode.role === "prefix function" ||
                funcNode.role === "limit function") {
                role = funcNode.role;
            }
            SemanticProcessor.propagateFunctionRole_(funcNode, role);
            return 'prefix';
        }
        const kind = SemanticProcessor.CLASSIFY_FUNCTION_[funcNode.role];
        return kind
            ? kind
            : SemanticPred.isSimpleFunctionHead(funcNode)
                ? 'simple'
                : '';
    }
    static propagateFunctionRole_(funcNode, tag) {
        if (funcNode) {
            if (funcNode.type === "infixop") {
                return;
            }
            if (!(SemanticPred.isRole(funcNode, "subsup") ||
                SemanticPred.isRole(funcNode, "underover"))) {
                funcNode.role = tag;
            }
            SemanticProcessor.propagateFunctionRole_(funcNode.childNodes[0], tag);
        }
    }
    static getFunctionOp_(tree, pred) {
        if (pred(tree)) {
            return tree;
        }
        for (let i = 0, child; (child = tree.childNodes[i]); i++) {
            const op = SemanticProcessor.getFunctionOp_(child, pred);
            if (op) {
                return op;
            }
        }
        return null;
    }
    static tableToMatrixOrVector_(node) {
        const matrix = node.childNodes[0];
        SemanticPred.isType(matrix, "multiline")
            ? SemanticProcessor.tableToVector_(node)
            : SemanticProcessor.tableToMatrix_(node);
        node.contentNodes.forEach(matrix.appendContentNode.bind(matrix));
        for (let i = 0, row; (row = matrix.childNodes[i]); i++) {
            SemanticProcessor.assignRoleToRow_(row, SemanticProcessor.getComponentRoles_(matrix));
        }
        matrix.parent = null;
        return matrix;
    }
    static tableToVector_(node) {
        const vector = node.childNodes[0];
        vector.type = "vector";
        if (vector.childNodes.length === 1) {
            SemanticProcessor.tableToSquare_(node);
            return;
        }
        SemanticProcessor.binomialForm_(vector);
    }
    static binomialForm_(node) {
        if (SemanticPred.isBinomial(node)) {
            node.role = "binomial";
            node.childNodes[0].role = "binomial";
            node.childNodes[1].role = "binomial";
        }
    }
    static tableToMatrix_(node) {
        const matrix = node.childNodes[0];
        matrix.type = "matrix";
        if (matrix.childNodes &&
            matrix.childNodes.length > 0 &&
            matrix.childNodes[0].childNodes &&
            matrix.childNodes.length === matrix.childNodes[0].childNodes.length) {
            SemanticProcessor.tableToSquare_(node);
            return;
        }
        if (matrix.childNodes && matrix.childNodes.length === 1) {
            matrix.role = "rowvector";
        }
    }
    static tableToSquare_(node) {
        const matrix = node.childNodes[0];
        if (SemanticPred.isNeutralFence(node)) {
            matrix.role = "determinant";
            return;
        }
        matrix.role = "squarematrix";
    }
    static getComponentRoles_(node) {
        const role = node.role;
        if (role && role !== "unknown") {
            return role;
        }
        return node.type.toLowerCase() || "unknown";
    }
    static tableToCases_(table, openFence) {
        for (let i = 0, row; (row = table.childNodes[i]); i++) {
            SemanticProcessor.assignRoleToRow_(row, "cases");
        }
        table.type = "cases";
        table.appendContentNode(openFence);
        if (SemanticPred.tableIsMultiline(table)) {
            SemanticProcessor.binomialForm_(table);
        }
        return table;
    }
    static rewriteFencedLine_(table) {
        const line = table.childNodes[0];
        const fenced = table.childNodes[0].childNodes[0];
        const element = table.childNodes[0].childNodes[0].childNodes[0];
        fenced.parent = table.parent;
        table.parent = fenced;
        element.parent = line;
        fenced.childNodes = [table];
        line.childNodes = [element];
        return fenced;
    }
    static rowToLine_(row, opt_role) {
        const role = opt_role || "unknown";
        if (SemanticPred.isType(row, "row")) {
            row.type = "line";
            row.role = role;
            if (row.childNodes.length === 1 &&
                SemanticPred.isType(row.childNodes[0], "cell")) {
                row.childNodes = row.childNodes[0].childNodes;
                row.childNodes.forEach(function (x) {
                    x.parent = row;
                });
            }
        }
    }
    static assignRoleToRow_(row, role) {
        if (SemanticPred.isType(row, "line")) {
            row.role = role;
            return;
        }
        if (SemanticPred.isType(row, "row")) {
            row.role = role;
            row.childNodes.forEach(function (cell) {
                if (SemanticPred.isType(cell, "cell")) {
                    cell.role = role;
                }
            });
        }
    }
    static nextSeparatorFunction_(separators) {
        let sepList;
        if (separators) {
            if (separators.match(/^\s+$/)) {
                return null;
            }
            else {
                sepList = separators
                    .replace(/\s/g, '')
                    .split('')
                    .filter(function (x) {
                    return x;
                });
            }
        }
        else {
            sepList = [','];
        }
        return function () {
            if (sepList.length > 1) {
                return sepList.shift();
            }
            return sepList[0];
        };
    }
    static numberRole_(node) {
        if (node.role !== "unknown") {
            return;
        }
        const content = [...node.textContent].filter((x) => x.match(/[^\s]/));
        const meaning = content.map(SemanticAttr.lookupMeaning);
        if (meaning.every(function (x) {
            return ((x.type === "number" && x.role === "integer") ||
                (x.type === "punctuation" && x.role === "comma"));
        })) {
            node.role = "integer";
            if (content[0] === '0') {
                node.addAnnotation('general', 'basenumber');
            }
            return;
        }
        if (meaning.every(function (x) {
            return ((x.type === "number" && x.role === "integer") ||
                x.type === "punctuation");
        })) {
            node.role = "float";
            return;
        }
        node.role = "othernumber";
    }
    static exprFont_(node) {
        if (node.font !== "unknown") {
            return;
        }
        const content = [...node.textContent];
        const meaning = content.map(SemanticAttr.lookupMeaning);
        const singleFont = meaning.reduce(function (prev, curr) {
            if (!prev ||
                !curr.font ||
                curr.font === "unknown" ||
                curr.font === prev) {
                return prev;
            }
            if (prev === "unknown") {
                return curr.font;
            }
            return null;
        }, "unknown");
        if (singleFont) {
            node.font = singleFont;
        }
    }
    static purgeFences_(partition) {
        const rel = partition.rel;
        const comp = partition.comp;
        const newRel = [];
        const newComp = [];
        while (rel.length > 0) {
            const currentRel = rel.shift();
            let currentComp = comp.shift();
            if (SemanticPred.isElligibleEmbellishedFence(currentRel)) {
                newRel.push(currentRel);
                newComp.push(currentComp);
                continue;
            }
            SemanticProcessor.fenceToPunct_(currentRel);
            currentComp.push(currentRel);
            currentComp = currentComp.concat(comp.shift());
            comp.unshift(currentComp);
        }
        newComp.push(comp.shift());
        return { rel: newRel, comp: newComp };
    }
    static rewriteFencedNode_(fenced) {
        const ofence = fenced.contentNodes[0];
        const cfence = fenced.contentNodes[1];
        let rewritten = SemanticProcessor.rewriteFence_(fenced, ofence);
        fenced.contentNodes[0] = rewritten.fence;
        rewritten = SemanticProcessor.rewriteFence_(rewritten.node, cfence);
        fenced.contentNodes[1] = rewritten.fence;
        fenced.contentNodes[0].parent = fenced;
        fenced.contentNodes[1].parent = fenced;
        rewritten.node.parent = null;
        return rewritten.node;
    }
    static rewriteFence_(node, fence) {
        if (!fence.embellished) {
            return { node: node, fence: fence };
        }
        const newFence = fence.childNodes[0];
        const rewritten = SemanticProcessor.rewriteFence_(node, newFence);
        if (SemanticPred.isType(fence, "superscript") ||
            SemanticPred.isType(fence, "subscript") ||
            SemanticPred.isType(fence, "tensor")) {
            if (!SemanticPred.isRole(fence, "subsup")) {
                fence.role = node.role;
            }
            if (newFence !== rewritten.node) {
                fence.replaceChild(newFence, rewritten.node);
                newFence.parent = node;
            }
            SemanticProcessor.propagateFencePointer_(fence, newFence);
            return { node: fence, fence: rewritten.fence };
        }
        fence.replaceChild(newFence, rewritten.fence);
        if (fence.mathmlTree && fence.mathml.indexOf(fence.mathmlTree) === -1) {
            fence.mathml.push(fence.mathmlTree);
        }
        return { node: rewritten.node, fence: fence };
    }
    static propagateFencePointer_(oldNode, newNode) {
        oldNode.fencePointer = newNode.fencePointer || newNode.id.toString();
        oldNode.embellished = null;
    }
    static classifyByColumns_(table, columns, relation, _alternatives) {
        const test1 = (x) => SemanticProcessor.isPureRelation_(x, relation);
        const test2 = (x) => SemanticProcessor.isEndRelation_(x, relation) ||
            SemanticProcessor.isPureRelation_(x, relation);
        const test3 = (x) => SemanticProcessor.isEndRelation_(x, relation, true) ||
            SemanticProcessor.isPureRelation_(x, relation);
        if ((columns.length === 3 &&
            SemanticProcessor.testColumns_(columns, 1, test1)) ||
            (columns.length === 2 &&
                (SemanticProcessor.testColumns_(columns, 1, test2) ||
                    SemanticProcessor.testColumns_(columns, 0, test3)))) {
            table.role = relation;
            return true;
        }
        return false;
    }
    static isEndRelation_(node, relation, opt_right) {
        const position = opt_right ? node.childNodes.length - 1 : 0;
        return (SemanticPred.isType(node, "relseq") &&
            SemanticPred.isRole(node, relation) &&
            SemanticPred.isType(node.childNodes[position], "empty"));
    }
    static isPureRelation_(node, relation) {
        return (SemanticPred.isType(node, "relation") &&
            SemanticPred.isRole(node, relation));
    }
    static computeColumns_(table) {
        const columns = [];
        for (let i = 0, row; (row = table.childNodes[i]); i++) {
            for (let j = 0, cell; (cell = row.childNodes[j]); j++) {
                const column = columns[j];
                column ? columns[j].push(cell) : (columns[j] = [cell]);
            }
        }
        return columns;
    }
    static testColumns_(columns, index, pred) {
        const column = columns[index];
        return column
            ? column.some(function (cell) {
                return (cell.childNodes.length && pred(cell.childNodes[0]));
            }) &&
                column.every(function (cell) {
                    return (!cell.childNodes.length ||
                        pred(cell.childNodes[0]));
                })
            : false;
    }
    setNodeFactory(factory) {
        SemanticProcessor.getInstance().factory_ = factory;
        SemanticHeuristics.updateFactory(SemanticProcessor.getInstance().factory_);
    }
    getNodeFactory() {
        return SemanticProcessor.getInstance().factory_;
    }
    identifierNode(leaf, font, unit) {
        if (unit === 'MathML-Unit') {
            leaf.type = "identifier";
            leaf.role = "unit";
        }
        else if (!font &&
            leaf.textContent.length === 1 &&
            (leaf.role === "integer" ||
                leaf.role === "latinletter" ||
                leaf.role === "greekletter") &&
            leaf.font === "normal") {
            leaf.font = "italic";
            return SemanticHeuristics.run('simpleNamedFunction', leaf);
        }
        if (leaf.type === "unknown") {
            leaf.type = "identifier";
        }
        SemanticProcessor.exprFont_(leaf);
        return SemanticHeuristics.run('simpleNamedFunction', leaf);
    }
    implicitNode(nodes) {
        nodes = SemanticProcessor.getInstance().getMixedNumbers_(nodes);
        nodes = SemanticProcessor.getInstance().combineUnits_(nodes);
        if (nodes.length === 1) {
            return nodes[0];
        }
        const node = SemanticProcessor.getInstance().implicitNode_(nodes);
        return SemanticHeuristics.run('combine_juxtaposition', node);
    }
    text(leaf, type) {
        SemanticProcessor.exprFont_(leaf);
        leaf.type = "text";
        if (type === 'MS') {
            leaf.role = "string";
            return leaf;
        }
        if (type === 'MSPACE' || leaf.textContent.match(/^\s*$/)) {
            leaf.role = "space";
            return leaf;
        }
        return leaf;
    }
    row(nodes) {
        nodes = nodes.filter(function (x) {
            return !SemanticPred.isType(x, "empty");
        });
        if (nodes.length === 0) {
            return SemanticProcessor.getInstance().factory_.makeEmptyNode();
        }
        nodes = SemanticProcessor.getInstance().getFencesInRow_(nodes);
        nodes = SemanticProcessor.getInstance().tablesInRow(nodes);
        nodes = SemanticProcessor.getInstance().getPunctuationInRow_(nodes);
        nodes = SemanticProcessor.getInstance().getTextInRow_(nodes);
        nodes = SemanticProcessor.getInstance().getFunctionsInRow_(nodes);
        return SemanticProcessor.getInstance().relationsInRow_(nodes);
    }
    limitNode(mmlTag, children) {
        if (!children.length) {
            return SemanticProcessor.getInstance().factory_.makeEmptyNode();
        }
        let center = children[0];
        let type = "unknown";
        if (!children[1]) {
            return center;
        }
        let result;
        if (SemanticPred.isLimitBase(center)) {
            result = SemanticProcessor.MML_TO_LIMIT_[mmlTag];
            const length = result.length;
            type = result.type;
            children = children.slice(0, result.length + 1);
            if ((length === 1 && SemanticPred.isAccent(children[1])) ||
                (length === 2 &&
                    SemanticPred.isAccent(children[1]) &&
                    SemanticPred.isAccent(children[2]))) {
                result = SemanticProcessor.MML_TO_BOUNDS_[mmlTag];
                return SemanticProcessor.getInstance().accentNode_(center, children, result.type, result.length, result.accent);
            }
            if (length === 2) {
                if (SemanticPred.isAccent(children[1])) {
                    center = SemanticProcessor.getInstance().accentNode_(center, [center, children[1]], {
                        MSUBSUP: "subscript",
                        MUNDEROVER: "underscore"
                    }[mmlTag], 1, true);
                    return !children[2]
                        ? center
                        : SemanticProcessor.getInstance().makeLimitNode_(center, [center, children[2]], null, "limupper");
                }
                if (children[2] && SemanticPred.isAccent(children[2])) {
                    center = SemanticProcessor.getInstance().accentNode_(center, [center, children[2]], {
                        MSUBSUP: "superscript",
                        MUNDEROVER: "overscore"
                    }[mmlTag], 1, true);
                    return SemanticProcessor.getInstance().makeLimitNode_(center, [center, children[1]], null, "limlower");
                }
                if (!children[length]) {
                    type = "limlower";
                }
            }
            return SemanticProcessor.getInstance().makeLimitNode_(center, children, null, type);
        }
        result = SemanticProcessor.MML_TO_BOUNDS_[mmlTag];
        return SemanticProcessor.getInstance().accentNode_(center, children, result.type, result.length, result.accent);
    }
    tablesInRow(nodes) {
        let partition = SemanticUtil.partitionNodes(nodes, SemanticPred.tableIsMatrixOrVector);
        let result = [];
        for (let i = 0, matrix; (matrix = partition.rel[i]); i++) {
            result = result.concat(partition.comp.shift());
            result.push(SemanticProcessor.tableToMatrixOrVector_(matrix));
        }
        result = result.concat(partition.comp.shift());
        partition = SemanticUtil.partitionNodes(result, SemanticPred.isTableOrMultiline);
        result = [];
        for (let i = 0, table; (table = partition.rel[i]); i++) {
            const prevNodes = partition.comp.shift();
            if (SemanticPred.tableIsCases(table, prevNodes)) {
                SemanticProcessor.tableToCases_(table, prevNodes.pop());
            }
            result = result.concat(prevNodes);
            result.push(table);
        }
        return result.concat(partition.comp.shift());
    }
    mfenced(open, close, sepValue, children) {
        if (sepValue && children.length > 0) {
            const separators = SemanticProcessor.nextSeparatorFunction_(sepValue);
            const newChildren = [children.shift()];
            children.forEach((child) => {
                newChildren.push(SemanticProcessor.getInstance().factory_.makeContentNode(separators()));
                newChildren.push(child);
            });
            children = newChildren;
        }
        if (open && close) {
            return SemanticProcessor.getInstance().horizontalFencedNode_(SemanticProcessor.getInstance().factory_.makeContentNode(open), SemanticProcessor.getInstance().factory_.makeContentNode(close), children);
        }
        if (open) {
            children.unshift(SemanticProcessor.getInstance().factory_.makeContentNode(open));
        }
        if (close) {
            children.push(SemanticProcessor.getInstance().factory_.makeContentNode(close));
        }
        return SemanticProcessor.getInstance().row(children);
    }
    fractionLikeNode(denom, enume, linethickness, bevelled) {
        let node;
        if (!bevelled && SemanticUtil.isZeroLength(linethickness)) {
            const child0 = SemanticProcessor.getInstance().factory_.makeBranchNode("line", [denom], []);
            const child1 = SemanticProcessor.getInstance().factory_.makeBranchNode("line", [enume], []);
            node = SemanticProcessor.getInstance().factory_.makeBranchNode("multiline", [child0, child1], []);
            SemanticProcessor.binomialForm_(node);
            SemanticProcessor.classifyMultiline(node);
            return node;
        }
        else {
            node = SemanticProcessor.getInstance().fractionNode_(denom, enume);
            if (bevelled) {
                node.addAnnotation('general', 'bevelled');
            }
            return node;
        }
    }
    tensor(base, lsub, lsup, rsub, rsup) {
        const newNode = SemanticProcessor.getInstance().factory_.makeBranchNode("tensor", [
            base,
            SemanticProcessor.getInstance().scriptNode_(lsub, "leftsub"),
            SemanticProcessor.getInstance().scriptNode_(lsup, "leftsuper"),
            SemanticProcessor.getInstance().scriptNode_(rsub, "rightsub"),
            SemanticProcessor.getInstance().scriptNode_(rsup, "rightsuper")
        ], []);
        newNode.role = base.role;
        newNode.embellished = SemanticPred.isEmbellished(base);
        return newNode;
    }
    pseudoTensor(base, sub, sup) {
        const isEmpty = (x) => !SemanticPred.isType(x, "empty");
        const nonEmptySub = sub.filter(isEmpty).length;
        const nonEmptySup = sup.filter(isEmpty).length;
        if (!nonEmptySub && !nonEmptySup) {
            return base;
        }
        const mmlTag = nonEmptySub ? (nonEmptySup ? 'MSUBSUP' : 'MSUB') : 'MSUP';
        const mmlchild = [base];
        if (nonEmptySub) {
            mmlchild.push(SemanticProcessor.getInstance().scriptNode_(sub, "rightsub", true));
        }
        if (nonEmptySup) {
            mmlchild.push(SemanticProcessor.getInstance().scriptNode_(sup, "rightsuper", true));
        }
        return SemanticProcessor.getInstance().limitNode(mmlTag, mmlchild);
    }
    font(font) {
        const mathjaxFont = SemanticProcessor.MATHJAX_FONTS[font];
        return mathjaxFont ? mathjaxFont : font;
    }
    proof(node, semantics, parse) {
        if (!semantics['inference'] && !semantics['axiom']) {
            console.log('Noise');
        }
        if (semantics['axiom']) {
            const cleaned = SemanticProcessor.getInstance().cleanInference(node.childNodes);
            const axiom = cleaned.length
                ? SemanticProcessor.getInstance().factory_.makeBranchNode("inference", parse(cleaned), [])
                : SemanticProcessor.getInstance().factory_.makeEmptyNode();
            axiom.role = "axiom";
            axiom.mathmlTree = node;
            return axiom;
        }
        const inference = SemanticProcessor.getInstance().inference(node, semantics, parse);
        if (semantics['proof']) {
            inference.role = "proof";
            inference.childNodes[0].role = "final";
        }
        return inference;
    }
    inference(node, semantics, parse) {
        if (semantics['inferenceRule']) {
            const formulas = SemanticProcessor.getInstance().getFormulas(node, [], parse);
            const inference = SemanticProcessor.getInstance().factory_.makeBranchNode("inference", [formulas.conclusion, formulas.premises], []);
            return inference;
        }
        const label = semantics['labelledRule'];
        const children = DomUtil.toArray(node.childNodes);
        const content = [];
        if (label === 'left' || label === 'both') {
            content.push(SemanticProcessor.getInstance().getLabel(node, children, parse, "left"));
        }
        if (label === 'right' || label === 'both') {
            content.push(SemanticProcessor.getInstance().getLabel(node, children, parse, "right"));
        }
        const formulas = SemanticProcessor.getInstance().getFormulas(node, children, parse);
        const inference = SemanticProcessor.getInstance().factory_.makeBranchNode("inference", [formulas.conclusion, formulas.premises], content);
        inference.mathmlTree = node;
        return inference;
    }
    getLabel(_node, children, parse, side) {
        const label = SemanticProcessor.getInstance().findNestedRow(children, 'prooflabel', side);
        const sem = SemanticProcessor.getInstance().factory_.makeBranchNode("rulelabel", parse(DomUtil.toArray(label.childNodes)), []);
        sem.role = side;
        sem.mathmlTree = label;
        return sem;
    }
    getFormulas(node, children, parse) {
        const inf = children.length
            ? SemanticProcessor.getInstance().findNestedRow(children, 'inferenceRule')
            : node;
        const up = SemanticProcessor.getSemantics(inf)['inferenceRule'] === 'up';
        const premRow = up ? inf.childNodes[1] : inf.childNodes[0];
        const concRow = up ? inf.childNodes[0] : inf.childNodes[1];
        const premTable = premRow.childNodes[0].childNodes[0];
        const topRow = DomUtil.toArray(premTable.childNodes[0].childNodes);
        const premNodes = [];
        let i = 1;
        for (const cell of topRow) {
            if (i % 2) {
                premNodes.push(cell.childNodes[0]);
            }
            i++;
        }
        const premises = parse(premNodes);
        const conclusion = parse(DomUtil.toArray(concRow.childNodes[0].childNodes))[0];
        const prem = SemanticProcessor.getInstance().factory_.makeBranchNode("premises", premises, []);
        prem.mathmlTree = premTable;
        const conc = SemanticProcessor.getInstance().factory_.makeBranchNode("conclusion", [conclusion], []);
        conc.mathmlTree = concRow.childNodes[0].childNodes[0];
        return { conclusion: conc, premises: prem };
    }
    findNestedRow(nodes, semantic, opt_value) {
        return SemanticProcessor.getInstance().findNestedRow_(nodes, semantic, 0, opt_value);
    }
    cleanInference(nodes) {
        return DomUtil.toArray(nodes).filter(function (x) {
            return DomUtil.tagName(x) !== 'MSPACE';
        });
    }
    operatorNode(node) {
        if (node.type === "unknown") {
            node.type = "operator";
        }
        return SemanticHeuristics.run('multioperator', node);
    }
    implicitNode_(nodes) {
        const operators = SemanticProcessor.getInstance().factory_.makeMultipleContentNodes(nodes.length - 1, SemanticAttr.invisibleTimes());
        SemanticProcessor.matchSpaces_(nodes, operators);
        const newNode = SemanticProcessor.getInstance().infixNode_(nodes, operators[0]);
        newNode.role = "implicit";
        operators.forEach(function (op) {
            op.parent = newNode;
        });
        newNode.contentNodes = operators;
        return newNode;
    }
    infixNode_(children, opNode) {
        const node = SemanticProcessor.getInstance().factory_.makeBranchNode("infixop", children, [opNode], SemanticUtil.getEmbellishedInner(opNode).textContent);
        node.role = opNode.role;
        return SemanticHeuristics.run('propagateSimpleFunction', node);
    }
    explicitMixed_(nodes) {
        const partition = SemanticUtil.partitionNodes(nodes, function (x) {
            return x.textContent === SemanticAttr.invisiblePlus();
        });
        if (!partition.rel.length) {
            return nodes;
        }
        let result = [];
        for (let i = 0, rel; (rel = partition.rel[i]); i++) {
            const prev = partition.comp[i];
            const next = partition.comp[i + 1];
            const last = prev.length - 1;
            if (prev[last] &&
                next[0] &&
                SemanticPred.isType(prev[last], "number") &&
                !SemanticPred.isRole(prev[last], "mixed") &&
                SemanticPred.isType(next[0], "fraction")) {
                const newNode = SemanticProcessor.getInstance().factory_.makeBranchNode("number", [prev[last], next[0]], []);
                newNode.role = "mixed";
                result = result.concat(prev.slice(0, last));
                result.push(newNode);
                next.shift();
            }
            else {
                result = result.concat(prev);
                result.push(rel);
            }
        }
        return result.concat(partition.comp[partition.comp.length - 1]);
    }
    concatNode_(inner, nodeList, type) {
        if (nodeList.length === 0) {
            return inner;
        }
        const content = nodeList
            .map(function (x) {
            return SemanticUtil.getEmbellishedInner(x).textContent;
        })
            .join(' ');
        const newNode = SemanticProcessor.getInstance().factory_.makeBranchNode(type, [inner], nodeList, content);
        if (nodeList.length > 1) {
            newNode.role = "multiop";
        }
        return newNode;
    }
    prefixNode_(node, prefixes) {
        const negatives = SemanticUtil.partitionNodes(prefixes, (x) => SemanticPred.isRole(x, "subtraction"));
        let newNode = SemanticProcessor.getInstance().concatNode_(node, negatives.comp.pop(), "prefixop");
        if (newNode.contentNodes.length === 1 &&
            newNode.contentNodes[0].role === "addition" &&
            newNode.contentNodes[0].textContent === '+') {
            newNode.role = "positive";
        }
        while (negatives.rel.length > 0) {
            newNode = SemanticProcessor.getInstance().concatNode_(newNode, [negatives.rel.pop()], "prefixop");
            newNode.role = "negative";
            newNode = SemanticProcessor.getInstance().concatNode_(newNode, negatives.comp.pop(), "prefixop");
        }
        return newNode;
    }
    postfixNode_(node, postfixes) {
        if (!postfixes.length) {
            return node;
        }
        return SemanticProcessor.getInstance().concatNode_(node, postfixes, "postfixop");
    }
    combineUnits_(nodes) {
        const partition = SemanticUtil.partitionNodes(nodes, function (x) {
            return !SemanticPred.isRole(x, "unit");
        });
        if (nodes.length === partition.rel.length) {
            return partition.rel;
        }
        const result = [];
        let rel;
        let last;
        do {
            const comp = partition.comp.shift();
            rel = partition.rel.shift();
            let unitNode = null;
            last = result.pop();
            if (last) {
                if (!comp.length || !SemanticPred.isUnitCounter(last)) {
                    result.push(last);
                }
                else {
                    comp.unshift(last);
                }
            }
            if (comp.length === 1) {
                unitNode = comp.pop();
            }
            if (comp.length > 1) {
                unitNode = SemanticProcessor.getInstance().implicitNode_(comp);
                unitNode.role = "unit";
            }
            if (unitNode) {
                result.push(unitNode);
            }
            if (rel) {
                result.push(rel);
            }
        } while (rel);
        return result;
    }
    getMixedNumbers_(nodes) {
        const partition = SemanticUtil.partitionNodes(nodes, function (x) {
            return (SemanticPred.isType(x, "fraction") &&
                SemanticPred.isRole(x, "vulgar"));
        });
        if (!partition.rel.length) {
            return nodes;
        }
        let result = [];
        for (let i = 0, rel; (rel = partition.rel[i]); i++) {
            const comp = partition.comp[i];
            const last = comp.length - 1;
            if (comp[last] &&
                SemanticPred.isType(comp[last], "number") &&
                (SemanticPred.isRole(comp[last], "integer") ||
                    SemanticPred.isRole(comp[last], "float"))) {
                const newNode = SemanticProcessor.getInstance().factory_.makeBranchNode("number", [comp[last], rel], []);
                newNode.role = "mixed";
                result = result.concat(comp.slice(0, last));
                result.push(newNode);
            }
            else {
                result = result.concat(comp);
                result.push(rel);
            }
        }
        return result.concat(partition.comp[partition.comp.length - 1]);
    }
    getTextInRow_(nodes) {
        if (nodes.length <= 1) {
            return nodes;
        }
        const partition = SemanticUtil.partitionNodes(nodes, (x) => SemanticPred.isType(x, "text"));
        if (partition.rel.length === 0) {
            return nodes;
        }
        const result = [];
        let nextComp = partition.comp[0];
        if (nextComp.length > 0) {
            result.push(SemanticProcessor.getInstance().row(nextComp));
        }
        for (let i = 0, text; (text = partition.rel[i]); i++) {
            result.push(text);
            nextComp = partition.comp[i + 1];
            if (nextComp.length > 0) {
                result.push(SemanticProcessor.getInstance().row(nextComp));
            }
        }
        return [SemanticProcessor.getInstance().dummyNode_(result)];
    }
    relationsInRow_(nodes) {
        const partition = SemanticUtil.partitionNodes(nodes, SemanticPred.isRelation);
        const firstRel = partition.rel[0];
        if (!firstRel) {
            return SemanticProcessor.getInstance().operationsInRow_(nodes);
        }
        if (nodes.length === 1) {
            return nodes[0];
        }
        const children = partition.comp.map(SemanticProcessor.getInstance().operationsInRow_);
        let node;
        if (partition.rel.some(function (x) {
            return !x.equals(firstRel);
        })) {
            node = SemanticProcessor.getInstance().factory_.makeBranchNode("multirel", children, partition.rel);
            if (partition.rel.every(function (x) {
                return x.role === firstRel.role;
            })) {
                node.role = firstRel.role;
            }
            return node;
        }
        node = SemanticProcessor.getInstance().factory_.makeBranchNode("relseq", children, partition.rel, SemanticUtil.getEmbellishedInner(firstRel).textContent);
        node.role = firstRel.role;
        return node;
    }
    operationsInRow_(nodes) {
        if (nodes.length === 0) {
            return SemanticProcessor.getInstance().factory_.makeEmptyNode();
        }
        nodes = SemanticProcessor.getInstance().explicitMixed_(nodes);
        if (nodes.length === 1) {
            return nodes[0];
        }
        const prefix = [];
        while (nodes.length > 0 && SemanticPred.isOperator(nodes[0])) {
            prefix.push(nodes.shift());
        }
        if (nodes.length === 0) {
            return SemanticProcessor.getInstance().prefixNode_(prefix.pop(), prefix);
        }
        if (nodes.length === 1) {
            return SemanticProcessor.getInstance().prefixNode_(nodes[0], prefix);
        }
        nodes = SemanticHeuristics.run('convert_juxtaposition', nodes);
        const split = SemanticUtil.sliceNodes(nodes, SemanticPred.isOperator);
        const node = SemanticProcessor.getInstance().prefixNode_(SemanticProcessor.getInstance().implicitNode(split.head), prefix);
        if (!split.div) {
            return node;
        }
        return SemanticProcessor.getInstance().operationsTree_(split.tail, node, split.div);
    }
    operationsTree_(nodes, root, lastop, opt_prefixes) {
        const prefixes = opt_prefixes || [];
        if (nodes.length === 0) {
            prefixes.unshift(lastop);
            if (root.type === "infixop") {
                const node = SemanticProcessor.getInstance().postfixNode_(root.childNodes.pop(), prefixes);
                root.appendChild(node);
                return root;
            }
            return SemanticProcessor.getInstance().postfixNode_(root, prefixes);
        }
        const split = SemanticUtil.sliceNodes(nodes, SemanticPred.isOperator);
        if (split.head.length === 0) {
            prefixes.push(split.div);
            return SemanticProcessor.getInstance().operationsTree_(split.tail, root, lastop, prefixes);
        }
        const node = SemanticProcessor.getInstance().prefixNode_(SemanticProcessor.getInstance().implicitNode(split.head), prefixes);
        const newNode = SemanticProcessor.getInstance().appendOperand_(root, lastop, node);
        if (!split.div) {
            return newNode;
        }
        return SemanticProcessor.getInstance().operationsTree_(split.tail, newNode, split.div, []);
    }
    appendOperand_(root, op, node) {
        if (root.type !== "infixop") {
            return SemanticProcessor.getInstance().infixNode_([root, node], op);
        }
        const division = SemanticProcessor.getInstance().appendDivisionOp_(root, op, node);
        if (division) {
            return division;
        }
        if (SemanticProcessor.getInstance().appendExistingOperator_(root, op, node)) {
            return root;
        }
        return op.role === "multiplication"
            ? SemanticProcessor.getInstance().appendMultiplicativeOp_(root, op, node)
            : SemanticProcessor.getInstance().appendAdditiveOp_(root, op, node);
    }
    appendDivisionOp_(root, op, node) {
        if (op.role === "division") {
            if (SemanticPred.isImplicit(root)) {
                return SemanticProcessor.getInstance().infixNode_([root, node], op);
            }
            return SemanticProcessor.getInstance().appendLastOperand_(root, op, node);
        }
        return root.role === "division"
            ? SemanticProcessor.getInstance().infixNode_([root, node], op)
            : null;
    }
    appendLastOperand_(root, op, node) {
        let lastRoot = root;
        let lastChild = root.childNodes[root.childNodes.length - 1];
        while (lastChild &&
            lastChild.type === "infixop" &&
            !SemanticPred.isImplicit(lastChild)) {
            lastRoot = lastChild;
            lastChild = lastRoot.childNodes[root.childNodes.length - 1];
        }
        const newNode = SemanticProcessor.getInstance().infixNode_([lastRoot.childNodes.pop(), node], op);
        lastRoot.appendChild(newNode);
        return root;
    }
    appendMultiplicativeOp_(root, op, node) {
        if (SemanticPred.isImplicit(root)) {
            return SemanticProcessor.getInstance().infixNode_([root, node], op);
        }
        let lastRoot = root;
        let lastChild = root.childNodes[root.childNodes.length - 1];
        while (lastChild &&
            lastChild.type === "infixop" &&
            !SemanticPred.isImplicit(lastChild)) {
            lastRoot = lastChild;
            lastChild = lastRoot.childNodes[root.childNodes.length - 1];
        }
        const newNode = SemanticProcessor.getInstance().infixNode_([lastRoot.childNodes.pop(), node], op);
        lastRoot.appendChild(newNode);
        return root;
    }
    appendAdditiveOp_(root, op, node) {
        return SemanticProcessor.getInstance().infixNode_([root, node], op);
    }
    appendExistingOperator_(root, op, node) {
        if (!root ||
            root.type !== "infixop" ||
            SemanticPred.isImplicit(root)) {
            return false;
        }
        if (root.contentNodes[0].equals(op)) {
            root.appendContentNode(op);
            root.appendChild(node);
            return true;
        }
        return SemanticProcessor.getInstance().appendExistingOperator_(root.childNodes[root.childNodes.length - 1], op, node);
    }
    getFencesInRow_(nodes) {
        let partition = SemanticUtil.partitionNodes(nodes, SemanticPred.isFence);
        partition = SemanticProcessor.purgeFences_(partition);
        const felem = partition.comp.shift();
        return SemanticProcessor.getInstance().fences_(partition.rel, partition.comp, [], [felem]);
    }
    fences_(fences, content, openStack, contentStack) {
        if (fences.length === 0 && openStack.length === 0) {
            return contentStack[0];
        }
        const openPred = (x) => SemanticPred.isRole(x, "open");
        if (fences.length === 0) {
            const result = contentStack.shift();
            while (openStack.length > 0) {
                if (openPred(openStack[0])) {
                    const firstOpen = openStack.shift();
                    SemanticProcessor.fenceToPunct_(firstOpen);
                    result.push(firstOpen);
                }
                else {
                    const split = SemanticUtil.sliceNodes(openStack, openPred);
                    const cutLength = split.head.length - 1;
                    const innerNodes = SemanticProcessor.getInstance().neutralFences_(split.head, contentStack.slice(0, cutLength));
                    contentStack = contentStack.slice(cutLength);
                    result.push(...innerNodes);
                    if (split.div) {
                        split.tail.unshift(split.div);
                    }
                    openStack = split.tail;
                }
                result.push(...contentStack.shift());
            }
            return result;
        }
        const lastOpen = openStack[openStack.length - 1];
        const firstRole = fences[0].role;
        if (firstRole === "open" ||
            (SemanticPred.isNeutralFence(fences[0]) &&
                !(lastOpen && SemanticPred.compareNeutralFences(fences[0], lastOpen)))) {
            openStack.push(fences.shift());
            const cont = content.shift();
            if (cont) {
                contentStack.push(cont);
            }
            return SemanticProcessor.getInstance().fences_(fences, content, openStack, contentStack);
        }
        if (lastOpen &&
            firstRole === "close" &&
            lastOpen.role === "open") {
            const fenced = SemanticProcessor.getInstance().horizontalFencedNode_(openStack.pop(), fences.shift(), contentStack.pop());
            contentStack.push(contentStack.pop().concat([fenced], content.shift()));
            return SemanticProcessor.getInstance().fences_(fences, content, openStack, contentStack);
        }
        if (lastOpen &&
            SemanticPred.compareNeutralFences(fences[0], lastOpen)) {
            if (!SemanticPred.elligibleLeftNeutral(lastOpen) ||
                !SemanticPred.elligibleRightNeutral(fences[0])) {
                openStack.push(fences.shift());
                const cont = content.shift();
                if (cont) {
                    contentStack.push(cont);
                }
                return SemanticProcessor.getInstance().fences_(fences, content, openStack, contentStack);
            }
            const fenced = SemanticProcessor.getInstance().horizontalFencedNode_(openStack.pop(), fences.shift(), contentStack.pop());
            contentStack.push(contentStack.pop().concat([fenced], content.shift()));
            return SemanticProcessor.getInstance().fences_(fences, content, openStack, contentStack);
        }
        if (lastOpen &&
            firstRole === "close" &&
            SemanticPred.isNeutralFence(lastOpen) &&
            openStack.some(openPred)) {
            const split = SemanticUtil.sliceNodes(openStack, openPred, true);
            const rightContent = contentStack.pop();
            const cutLength = contentStack.length - split.tail.length + 1;
            const innerNodes = SemanticProcessor.getInstance().neutralFences_(split.tail, contentStack.slice(cutLength));
            contentStack = contentStack.slice(0, cutLength);
            const fenced = SemanticProcessor.getInstance().horizontalFencedNode_(split.div, fences.shift(), contentStack.pop().concat(innerNodes, rightContent));
            contentStack.push(contentStack.pop().concat([fenced], content.shift()));
            return SemanticProcessor.getInstance().fences_(fences, content, split.head, contentStack);
        }
        const fenced = fences.shift();
        SemanticProcessor.fenceToPunct_(fenced);
        contentStack.push(contentStack.pop().concat([fenced], content.shift()));
        return SemanticProcessor.getInstance().fences_(fences, content, openStack, contentStack);
    }
    neutralFences_(fences, content) {
        if (fences.length === 0) {
            return fences;
        }
        if (fences.length === 1) {
            SemanticProcessor.fenceToPunct_(fences[0]);
            return fences;
        }
        const firstFence = fences.shift();
        if (!SemanticPred.elligibleLeftNeutral(firstFence)) {
            SemanticProcessor.fenceToPunct_(firstFence);
            const restContent = content.shift();
            restContent.unshift(firstFence);
            return restContent.concat(SemanticProcessor.getInstance().neutralFences_(fences, content));
        }
        const split = SemanticUtil.sliceNodes(fences, function (x) {
            return SemanticPred.compareNeutralFences(x, firstFence);
        });
        if (!split.div) {
            SemanticProcessor.fenceToPunct_(firstFence);
            const restContent = content.shift();
            restContent.unshift(firstFence);
            return restContent.concat(SemanticProcessor.getInstance().neutralFences_(fences, content));
        }
        if (!SemanticPred.elligibleRightNeutral(split.div)) {
            SemanticProcessor.fenceToPunct_(split.div);
            fences.unshift(firstFence);
            return SemanticProcessor.getInstance().neutralFences_(fences, content);
        }
        const newContent = SemanticProcessor.getInstance().combineFencedContent_(firstFence, split.div, split.head, content);
        if (split.tail.length > 0) {
            const leftContent = newContent.shift();
            const result = SemanticProcessor.getInstance().neutralFences_(split.tail, newContent);
            return leftContent.concat(result);
        }
        return newContent[0];
    }
    combineFencedContent_(leftFence, rightFence, midFences, content) {
        if (midFences.length === 0) {
            const fenced = SemanticProcessor.getInstance().horizontalFencedNode_(leftFence, rightFence, content.shift());
            if (content.length > 0) {
                content[0].unshift(fenced);
            }
            else {
                content = [[fenced]];
            }
            return content;
        }
        const leftContent = content.shift();
        const cutLength = midFences.length - 1;
        const midContent = content.slice(0, cutLength);
        content = content.slice(cutLength);
        const rightContent = content.shift();
        const innerNodes = SemanticProcessor.getInstance().neutralFences_(midFences, midContent);
        leftContent.push(...innerNodes);
        leftContent.push(...rightContent);
        const fenced = SemanticProcessor.getInstance().horizontalFencedNode_(leftFence, rightFence, leftContent);
        if (content.length > 0) {
            content[0].unshift(fenced);
        }
        else {
            content = [[fenced]];
        }
        return content;
    }
    horizontalFencedNode_(ofence, cfence, content) {
        const childNode = SemanticProcessor.getInstance().row(content);
        let newNode = SemanticProcessor.getInstance().factory_.makeBranchNode("fenced", [childNode], [ofence, cfence]);
        if (ofence.role === "open") {
            SemanticProcessor.getInstance().classifyHorizontalFence_(newNode);
            newNode = SemanticHeuristics.run('propagateComposedFunction', newNode);
        }
        else {
            newNode.role = ofence.role;
        }
        newNode = SemanticHeuristics.run('detect_cycle', newNode);
        return SemanticProcessor.rewriteFencedNode_(newNode);
    }
    classifyHorizontalFence_(node) {
        node.role = "leftright";
        const children = node.childNodes;
        if (!SemanticPred.isSetNode(node) || children.length > 1) {
            return;
        }
        if (children.length === 0 || children[0].type === "empty") {
            node.role = "set empty";
            return;
        }
        const type = children[0].type;
        if (children.length === 1 &&
            SemanticPred.isSingletonSetContent(children[0])) {
            node.role = "set singleton";
            return;
        }
        const role = children[0].role;
        if (type !== "punctuated" || role !== "sequence") {
            return;
        }
        if (children[0].contentNodes[0].role === "comma") {
            node.role = "set collection";
            return;
        }
        if (children[0].contentNodes.length === 1 &&
            (children[0].contentNodes[0].role === "vbar" ||
                children[0].contentNodes[0].role === "colon")) {
            node.role = "set extended";
            SemanticProcessor.getInstance().setExtension_(node);
            return;
        }
    }
    setExtension_(set) {
        const extender = set.childNodes[0].childNodes[0];
        if (extender &&
            extender.type === "infixop" &&
            extender.contentNodes.length === 1 &&
            SemanticPred.isMembership(extender.contentNodes[0])) {
            extender.addAnnotation('set', 'intensional');
            extender.contentNodes[0].addAnnotation('set', 'intensional');
        }
    }
    getPunctuationInRow_(nodes) {
        if (nodes.length <= 1) {
            return nodes;
        }
        const allowedType = (x) => {
            const type = x.type;
            return (type === 'punctuation' ||
                type === 'text' ||
                type === 'operator' ||
                type === 'relation');
        };
        const partition = SemanticUtil.partitionNodes(nodes, function (x) {
            if (!SemanticPred.isPunctuation(x)) {
                return false;
            }
            if (SemanticPred.isPunctuation(x) &&
                !SemanticPred.isRole(x, "ellipsis")) {
                return true;
            }
            const index = nodes.indexOf(x);
            if (index === 0) {
                if (nodes[1] && allowedType(nodes[1])) {
                    return false;
                }
                return true;
            }
            const prev = nodes[index - 1];
            if (index === nodes.length - 1) {
                if (allowedType(prev)) {
                    return false;
                }
                return true;
            }
            const next = nodes[index + 1];
            if (allowedType(prev) && allowedType(next)) {
                return false;
            }
            return true;
        });
        if (partition.rel.length === 0) {
            return nodes;
        }
        const newNodes = [];
        let firstComp = partition.comp.shift();
        if (firstComp.length > 0) {
            newNodes.push(SemanticProcessor.getInstance().row(firstComp));
        }
        let relCounter = 0;
        while (partition.comp.length > 0) {
            newNodes.push(partition.rel[relCounter++]);
            firstComp = partition.comp.shift();
            if (firstComp.length > 0) {
                newNodes.push(SemanticProcessor.getInstance().row(firstComp));
            }
        }
        return [
            SemanticProcessor.getInstance().punctuatedNode_(newNodes, partition.rel)
        ];
    }
    punctuatedNode_(nodes, punctuations) {
        const newNode = SemanticProcessor.getInstance().factory_.makeBranchNode("punctuated", nodes, punctuations);
        if (punctuations.length === nodes.length) {
            const firstRole = punctuations[0].role;
            if (firstRole !== "unknown" &&
                punctuations.every(function (punct) {
                    return punct.role === firstRole;
                })) {
                newNode.role = firstRole;
                return newNode;
            }
        }
        if (SemanticPred.singlePunctAtPosition(nodes, punctuations, 0)) {
            newNode.role = "startpunct";
        }
        else if (SemanticPred.singlePunctAtPosition(nodes, punctuations, nodes.length - 1)) {
            newNode.role = "endpunct";
        }
        else if (punctuations.every((x) => SemanticPred.isRole(x, "dummy"))) {
            newNode.role = "text";
        }
        else if (punctuations.every((x) => SemanticPred.isRole(x, "space"))) {
            newNode.role = "space";
        }
        else {
            newNode.role = "sequence";
        }
        return newNode;
    }
    dummyNode_(children) {
        const commata = SemanticProcessor.getInstance().factory_.makeMultipleContentNodes(children.length - 1, SemanticAttr.invisibleComma());
        commata.forEach(function (comma) {
            comma.role = "dummy";
        });
        return SemanticProcessor.getInstance().punctuatedNode_(children, commata);
    }
    accentRole_(node, type) {
        if (!SemanticPred.isAccent(node)) {
            return false;
        }
        const content = node.textContent;
        const role = SemanticAttr.lookupSecondary('bar', content) ||
            SemanticAttr.lookupSecondary('tilde', content) ||
            node.role;
        node.role =
            type === "underscore"
                ? "underaccent"
                : "overaccent";
        node.addAnnotation('accent', role);
        return true;
    }
    accentNode_(center, children, type, length, accent) {
        children = children.slice(0, length + 1);
        const child1 = children[1];
        const child2 = children[2];
        let innerNode;
        if (!accent && child2) {
            innerNode = SemanticProcessor.getInstance().factory_.makeBranchNode("subscript", [center, child1], []);
            innerNode.role = "subsup";
            children = [innerNode, child2];
            type = "superscript";
        }
        if (accent) {
            const underAccent = SemanticProcessor.getInstance().accentRole_(child1, type);
            if (child2) {
                const overAccent = SemanticProcessor.getInstance().accentRole_(child2, "overscore");
                if (overAccent && !underAccent) {
                    innerNode = SemanticProcessor.getInstance().factory_.makeBranchNode("overscore", [center, child2], []);
                    children = [innerNode, child1];
                    type = "underscore";
                }
                else {
                    innerNode = SemanticProcessor.getInstance().factory_.makeBranchNode("underscore", [center, child1], []);
                    children = [innerNode, child2];
                    type = "overscore";
                }
                innerNode.role = "underover";
            }
        }
        return SemanticProcessor.getInstance().makeLimitNode_(center, children, innerNode, type);
    }
    makeLimitNode_(center, children, innerNode, type) {
        if (type === "limupper" &&
            center.type === "limlower") {
            center.childNodes.push(children[1]);
            children[1].parent = center;
            center.type = "limboth";
            return center;
        }
        if (type === "limlower" &&
            center.type === "limupper") {
            center.childNodes.splice(1, -1, children[1]);
            children[1].parent = center;
            center.type = "limboth";
            return center;
        }
        const newNode = SemanticProcessor.getInstance().factory_.makeBranchNode(type, children, []);
        const embellished = SemanticPred.isEmbellished(center);
        if (innerNode) {
            innerNode.embellished = embellished;
        }
        newNode.embellished = embellished;
        newNode.role = center.role;
        return newNode;
    }
    getFunctionsInRow_(restNodes, opt_result) {
        const result = opt_result || [];
        if (restNodes.length === 0) {
            return result;
        }
        const firstNode = restNodes.shift();
        const heuristic = SemanticProcessor.classifyFunction_(firstNode, restNodes);
        if (!heuristic) {
            result.push(firstNode);
            return SemanticProcessor.getInstance().getFunctionsInRow_(restNodes, result);
        }
        const processedRest = SemanticProcessor.getInstance().getFunctionsInRow_(restNodes, []);
        const newRest = SemanticProcessor.getInstance().getFunctionArgs_(firstNode, processedRest, heuristic);
        return result.concat(newRest);
    }
    getFunctionArgs_(func, rest, heuristic) {
        let partition, arg, funcNode;
        switch (heuristic) {
            case 'integral': {
                const components = SemanticProcessor.getInstance().getIntegralArgs_(rest);
                if (!components.intvar && !components.integrand.length) {
                    components.rest.unshift(func);
                    return components.rest;
                }
                const integrand = SemanticProcessor.getInstance().row(components.integrand);
                funcNode = SemanticProcessor.getInstance().integralNode_(func, integrand, components.intvar);
                components.rest.unshift(funcNode);
                return components.rest;
            }
            case 'prefix': {
                if (rest[0] && rest[0].type === "fenced") {
                    const arg = rest.shift();
                    if (!SemanticPred.isNeutralFence(arg)) {
                        arg.role = "leftright";
                    }
                    funcNode = SemanticProcessor.getInstance().functionNode_(func, arg);
                    rest.unshift(funcNode);
                    return rest;
                }
                partition = SemanticUtil.sliceNodes(rest, SemanticPred.isPrefixFunctionBoundary);
                if (!partition.head.length) {
                    if (!partition.div ||
                        !SemanticPred.isType(partition.div, "appl")) {
                        rest.unshift(func);
                        return rest;
                    }
                    arg = partition.div;
                }
                else {
                    arg = SemanticProcessor.getInstance().row(partition.head);
                    if (partition.div) {
                        partition.tail.unshift(partition.div);
                    }
                }
                funcNode = SemanticProcessor.getInstance().functionNode_(func, arg);
                partition.tail.unshift(funcNode);
                return partition.tail;
            }
            case 'bigop': {
                partition = SemanticUtil.sliceNodes(rest, SemanticPred.isBigOpBoundary);
                if (!partition.head.length) {
                    rest.unshift(func);
                    return rest;
                }
                arg = SemanticProcessor.getInstance().row(partition.head);
                funcNode = SemanticProcessor.getInstance().bigOpNode_(func, arg);
                if (partition.div) {
                    partition.tail.unshift(partition.div);
                }
                partition.tail.unshift(funcNode);
                return partition.tail;
            }
            case 'simple':
            default: {
                if (rest.length === 0) {
                    return [func];
                }
                const firstArg = rest[0];
                if (firstArg.type === "fenced" &&
                    !SemanticPred.isNeutralFence(firstArg) &&
                    SemanticPred.isSimpleFunctionScope(firstArg)) {
                    firstArg.role = "leftright";
                    SemanticProcessor.propagateFunctionRole_(func, "simple function");
                    funcNode = SemanticProcessor.getInstance().functionNode_(func, rest.shift());
                    rest.unshift(funcNode);
                    return rest;
                }
                rest.unshift(func);
                return rest;
            }
        }
    }
    getIntegralArgs_(nodes, args = []) {
        if (nodes.length === 0) {
            return { integrand: args, intvar: null, rest: nodes };
        }
        const firstNode = nodes[0];
        if (SemanticPred.isGeneralFunctionBoundary(firstNode)) {
            return { integrand: args, intvar: null, rest: nodes };
        }
        if (SemanticPred.isIntegralDxBoundarySingle(firstNode)) {
            firstNode.role = "integral";
            return { integrand: args, intvar: firstNode, rest: nodes.slice(1) };
        }
        if (nodes[1] && SemanticPred.isIntegralDxBoundary(firstNode, nodes[1])) {
            const intvar = SemanticProcessor.getInstance().prefixNode_(nodes[1], [firstNode]);
            intvar.role = "integral";
            return { integrand: args, intvar: intvar, rest: nodes.slice(2) };
        }
        args.push(nodes.shift());
        return SemanticProcessor.getInstance().getIntegralArgs_(nodes, args);
    }
    functionNode_(func, arg) {
        const applNode = SemanticProcessor.getInstance().factory_.makeContentNode(SemanticAttr.functionApplication());
        const appl = SemanticProcessor.getInstance().funcAppls[func.id];
        if (appl) {
            applNode.mathmlTree = appl.mathmlTree;
            applNode.mathml = appl.mathml;
            applNode.annotation = appl.annotation;
            applNode.attributes = appl.attributes;
            delete SemanticProcessor.getInstance().funcAppls[func.id];
        }
        applNode.type = "punctuation";
        applNode.role = "application";
        const funcop = SemanticProcessor.getFunctionOp_(func, function (node) {
            return (SemanticPred.isType(node, "function") ||
                (SemanticPred.isType(node, "identifier") &&
                    SemanticPred.isRole(node, "simple function")));
        });
        return SemanticProcessor.getInstance().functionalNode_("appl", [func, arg], funcop, [applNode]);
    }
    bigOpNode_(bigOp, arg) {
        const largeop = SemanticProcessor.getFunctionOp_(bigOp, (x) => SemanticPred.isType(x, "largeop"));
        return SemanticProcessor.getInstance().functionalNode_("bigop", [bigOp, arg], largeop, []);
    }
    integralNode_(integral, integrand, intvar) {
        integrand =
            integrand || SemanticProcessor.getInstance().factory_.makeEmptyNode();
        intvar = intvar || SemanticProcessor.getInstance().factory_.makeEmptyNode();
        const largeop = SemanticProcessor.getFunctionOp_(integral, (x) => SemanticPred.isType(x, "largeop"));
        return SemanticProcessor.getInstance().functionalNode_("integral", [integral, integrand, intvar], largeop, []);
    }
    functionalNode_(type, children, operator, content) {
        const funcop = children[0];
        let oldParent;
        if (operator) {
            oldParent = operator.parent;
            content.push(operator);
        }
        const newNode = SemanticProcessor.getInstance().factory_.makeBranchNode(type, children, content);
        newNode.role = funcop.role;
        if (oldParent) {
            operator.parent = oldParent;
        }
        return newNode;
    }
    fractionNode_(denom, enume) {
        const newNode = SemanticProcessor.getInstance().factory_.makeBranchNode("fraction", [denom, enume], []);
        newNode.role = newNode.childNodes.every(function (x) {
            return (SemanticPred.isType(x, "number") &&
                SemanticPred.isRole(x, "integer"));
        })
            ? "vulgar"
            : newNode.childNodes.every(SemanticPred.isPureUnit)
                ? "unit"
                : "division";
        return SemanticHeuristics.run('propagateSimpleFunction', newNode);
    }
    scriptNode_(nodes, role, opt_noSingle) {
        let newNode;
        switch (nodes.length) {
            case 0:
                newNode = SemanticProcessor.getInstance().factory_.makeEmptyNode();
                break;
            case 1:
                newNode = nodes[0];
                if (opt_noSingle) {
                    return newNode;
                }
                break;
            default:
                newNode = SemanticProcessor.getInstance().dummyNode_(nodes);
        }
        newNode.role = role;
        return newNode;
    }
    findNestedRow_(nodes, semantic, level, value) {
        if (level > 3) {
            return null;
        }
        for (let i = 0, node; (node = nodes[i]); i++) {
            const tag = DomUtil.tagName(node);
            if (tag !== 'MSPACE') {
                if (tag === 'MROW') {
                    return SemanticProcessor.getInstance().findNestedRow_(DomUtil.toArray(node.childNodes), semantic, level + 1, value);
                }
                if (SemanticProcessor.findSemantics(node, semantic, value)) {
                    return node;
                }
            }
        }
        return null;
    }
}
exports["default"] = SemanticProcessor;
SemanticProcessor.FENCE_TO_PUNCT_ = {
    ["metric"]: "metric",
    ["neutral"]: "vbar",
    ["open"]: "openfence",
    ["close"]: "closefence"
};
SemanticProcessor.MML_TO_LIMIT_ = {
    MSUB: { type: "limlower", length: 1 },
    MUNDER: { type: "limlower", length: 1 },
    MSUP: { type: "limupper", length: 1 },
    MOVER: { type: "limupper", length: 1 },
    MSUBSUP: { type: "limboth", length: 2 },
    MUNDEROVER: { type: "limboth", length: 2 }
};
SemanticProcessor.MML_TO_BOUNDS_ = {
    MSUB: { type: "subscript", length: 1, accent: false },
    MSUP: { type: "superscript", length: 1, accent: false },
    MSUBSUP: { type: "subscript", length: 2, accent: false },
    MUNDER: { type: "underscore", length: 1, accent: true },
    MOVER: { type: "overscore", length: 1, accent: true },
    MUNDEROVER: { type: "underscore", length: 2, accent: true }
};
SemanticProcessor.CLASSIFY_FUNCTION_ = {
    ["integral"]: 'integral',
    ["sum"]: 'bigop',
    ["prefix function"]: 'prefix',
    ["limit function"]: 'prefix',
    ["simple function"]: 'prefix',
    ["composed function"]: 'prefix'
};
SemanticProcessor.MATHJAX_FONTS = {
    '-tex-caligraphic': "caligraphic",
    '-tex-caligraphic-bold': "caligraphic-bold",
    '-tex-calligraphic': "caligraphic",
    '-tex-calligraphic-bold': "caligraphic-bold",
    '-tex-oldstyle': "oldstyle",
    '-tex-oldstyle-bold': "oldstyle-bold",
    '-tex-mathit': "italic"
};


/***/ }),

/***/ 7984:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticSkeleton = void 0;
const BaseUtil = __webpack_require__(1426);
const XpathUtil = __webpack_require__(5024);
const enrich_attr_1 = __webpack_require__(8171);
class SemanticSkeleton {
    constructor(skeleton) {
        this.parents = null;
        this.levelsMap = null;
        skeleton = skeleton === 0 ? skeleton : skeleton || [];
        this.array = skeleton;
    }
    static fromTree(tree) {
        return SemanticSkeleton.fromNode(tree.root);
    }
    static fromNode(node) {
        return new SemanticSkeleton(SemanticSkeleton.fromNode_(node));
    }
    static fromString(skel) {
        return new SemanticSkeleton(SemanticSkeleton.fromString_(skel));
    }
    static simpleCollapseStructure(strct) {
        return typeof strct === 'number';
    }
    static contentCollapseStructure(strct) {
        return (!!strct &&
            !SemanticSkeleton.simpleCollapseStructure(strct) &&
            strct[0] === 'c');
    }
    static interleaveIds(first, second) {
        return BaseUtil.interleaveLists(SemanticSkeleton.collapsedLeafs(first), SemanticSkeleton.collapsedLeafs(second));
    }
    static collapsedLeafs(...args) {
        const collapseStructure = (coll) => {
            if (SemanticSkeleton.simpleCollapseStructure(coll)) {
                return [coll];
            }
            coll = coll;
            return SemanticSkeleton.contentCollapseStructure(coll[1])
                ? coll.slice(2)
                : coll.slice(1);
        };
        return args.reduce((x, y) => x.concat(collapseStructure(y)), []);
    }
    static fromStructure(mml, tree) {
        return new SemanticSkeleton(SemanticSkeleton.tree_(mml, tree.root));
    }
    static combineContentChildren(semantic, content, children) {
        switch (semantic.type) {
            case "relseq":
            case "infixop":
            case "multirel":
                return BaseUtil.interleaveLists(children, content);
            case "prefixop":
                return content.concat(children);
            case "postfixop":
                return children.concat(content);
            case "fenced":
                children.unshift(content[0]);
                children.push(content[1]);
                return children;
            case "appl":
                return [children[0], content[0], children[1]];
            case "root":
                return [children[1], children[0]];
            case "row":
            case "line":
                if (content.length) {
                    children.unshift(content[0]);
                }
                return children;
            default:
                return children;
        }
    }
    static makeSexp_(struct) {
        if (SemanticSkeleton.simpleCollapseStructure(struct)) {
            return struct.toString();
        }
        if (SemanticSkeleton.contentCollapseStructure(struct)) {
            return ('(' +
                'c ' +
                struct.slice(1).map(SemanticSkeleton.makeSexp_).join(' ') +
                ')');
        }
        return ('(' + struct.map(SemanticSkeleton.makeSexp_).join(' ') + ')');
    }
    static fromString_(skeleton) {
        let str = skeleton.replace(/\(/g, '[');
        str = str.replace(/\)/g, ']');
        str = str.replace(/ /g, ',');
        str = str.replace(/c/g, '"c"');
        return JSON.parse(str);
    }
    static fromNode_(node) {
        if (!node) {
            return [];
        }
        const content = node.contentNodes;
        let contentStructure;
        if (content.length) {
            contentStructure = content.map(SemanticSkeleton.fromNode_);
            contentStructure.unshift('c');
        }
        const children = node.childNodes;
        if (!children.length) {
            return content.length ? [node.id, contentStructure] : node.id;
        }
        const structure = children.map(SemanticSkeleton.fromNode_);
        if (content.length) {
            structure.unshift(contentStructure);
        }
        structure.unshift(node.id);
        return structure;
    }
    static tree_(mml, node) {
        if (!node) {
            return [];
        }
        if (!node.childNodes.length) {
            return node.id;
        }
        const id = node.id;
        const skeleton = [id];
        const mmlChild = XpathUtil.evalXPath(`.//self::*[@${enrich_attr_1.Attribute.ID}=${id}]`, mml)[0];
        const children = SemanticSkeleton.combineContentChildren(node, node.contentNodes.map(function (x) {
            return x;
        }), node.childNodes.map(function (x) {
            return x;
        }));
        if (mmlChild) {
            SemanticSkeleton.addOwns_(mmlChild, children);
        }
        for (let i = 0, child; (child = children[i]); i++) {
            skeleton.push(SemanticSkeleton.tree_(mml, child));
        }
        return skeleton;
    }
    static addOwns_(node, children) {
        const collapsed = node.getAttribute(enrich_attr_1.Attribute.COLLAPSED);
        const leafs = collapsed
            ? SemanticSkeleton.realLeafs_(SemanticSkeleton.fromString(collapsed).array)
            : children.map((x) => x.id);
        node.setAttribute(enrich_attr_1.Attribute.OWNS, leafs.join(' '));
    }
    static realLeafs_(sexp) {
        if (SemanticSkeleton.simpleCollapseStructure(sexp)) {
            return [sexp];
        }
        if (SemanticSkeleton.contentCollapseStructure(sexp)) {
            return [];
        }
        sexp = sexp;
        let result = [];
        for (let i = 1; i < sexp.length; i++) {
            result = result.concat(SemanticSkeleton.realLeafs_(sexp[i]));
        }
        return result;
    }
    populate() {
        if (this.parents && this.levelsMap) {
            return;
        }
        this.parents = {};
        this.levelsMap = {};
        this.populate_(this.array, this.array, []);
    }
    toString() {
        return SemanticSkeleton.makeSexp_(this.array);
    }
    populate_(element, layer, parents) {
        if (SemanticSkeleton.simpleCollapseStructure(element)) {
            element = element;
            this.levelsMap[element] = layer;
            this.parents[element] =
                element === parents[0] ? parents.slice(1) : parents;
            return;
        }
        const newElement = SemanticSkeleton.contentCollapseStructure(element)
            ? element.slice(1)
            : element;
        const newParents = [newElement[0]].concat(parents);
        for (let i = 0, l = newElement.length; i < l; i++) {
            const current = newElement[i];
            this.populate_(current, element, newParents);
        }
    }
    isRoot(id) {
        const level = this.levelsMap[id];
        return id === level[0];
    }
    directChildren(id) {
        if (!this.isRoot(id)) {
            return [];
        }
        const level = this.levelsMap[id];
        return level.slice(1).map((child) => {
            if (SemanticSkeleton.simpleCollapseStructure(child)) {
                return child;
            }
            if (SemanticSkeleton.contentCollapseStructure(child)) {
                return child[1];
            }
            return child[0];
        });
    }
    subtreeNodes(id) {
        if (!this.isRoot(id)) {
            return [];
        }
        const subtreeNodes_ = (tree, nodes) => {
            if (SemanticSkeleton.simpleCollapseStructure(tree)) {
                nodes.push(tree);
                return;
            }
            tree = tree;
            if (SemanticSkeleton.contentCollapseStructure(tree)) {
                tree = tree.slice(1);
            }
            tree.forEach((x) => subtreeNodes_(x, nodes));
        };
        const level = this.levelsMap[id];
        const subtree = [];
        subtreeNodes_(level.slice(1), subtree);
        return subtree;
    }
}
exports.SemanticSkeleton = SemanticSkeleton;


/***/ }),

/***/ 1784:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticTree = void 0;
const DomUtil = __webpack_require__(6671);
const semantic_annotations_1 = __webpack_require__(4036);
const semantic_annotator_1 = __webpack_require__(241);
const semantic_mathml_1 = __webpack_require__(8122);
const semantic_node_1 = __webpack_require__(9444);
const SemanticPred = __webpack_require__(6161);
__webpack_require__(7103);
class SemanticTree {
    constructor(mathml) {
        this.mathml = mathml;
        this.parser = new semantic_mathml_1.SemanticMathml();
        this.root = this.parser.parse(mathml);
        this.collator = this.parser.getFactory().leafMap.collateMeaning();
        const newDefault = this.collator.newDefault();
        if (newDefault) {
            this.parser = new semantic_mathml_1.SemanticMathml();
            this.parser.getFactory().defaultMap = newDefault;
            this.root = this.parser.parse(mathml);
        }
        unitVisitor.visit(this.root, {});
        (0, semantic_annotations_1.annotate)(this.root);
    }
    static empty() {
        const empty = DomUtil.parseInput('<math/>');
        const stree = new SemanticTree(empty);
        stree.mathml = empty;
        return stree;
    }
    static fromNode(semantic, opt_mathml) {
        const stree = SemanticTree.empty();
        stree.root = semantic;
        if (opt_mathml) {
            stree.mathml = opt_mathml;
        }
        return stree;
    }
    static fromRoot(semantic, opt_mathml) {
        let root = semantic;
        while (root.parent) {
            root = root.parent;
        }
        const stree = SemanticTree.fromNode(root);
        if (opt_mathml) {
            stree.mathml = opt_mathml;
        }
        return stree;
    }
    static fromXml(xml) {
        const stree = SemanticTree.empty();
        if (xml.childNodes[0]) {
            stree.root = semantic_node_1.SemanticNode.fromXml(xml.childNodes[0]);
        }
        return stree;
    }
    xml(opt_brief) {
        const xml = DomUtil.parseInput('<stree></stree>');
        const xmlRoot = this.root.xml(xml.ownerDocument, opt_brief);
        xml.appendChild(xmlRoot);
        return xml;
    }
    toString(opt_brief) {
        return DomUtil.serializeXml(this.xml(opt_brief));
    }
    formatXml(opt_brief) {
        const xml = this.toString(opt_brief);
        return DomUtil.formatXml(xml);
    }
    displayTree() {
        this.root.displayTree();
    }
    replaceNode(oldNode, newNode) {
        const parent = oldNode.parent;
        if (!parent) {
            this.root = newNode;
            return;
        }
        parent.replaceChild(oldNode, newNode);
    }
    toJson() {
        const json = {};
        json['stree'] = this.root.toJson();
        return json;
    }
}
exports.SemanticTree = SemanticTree;
const unitVisitor = new semantic_annotator_1.SemanticVisitor('general', 'unit', (node, _info) => {
    if (node.type === "infixop" &&
        (node.role === "multiplication" ||
            node.role === "implicit")) {
        const children = node.childNodes;
        if (children.length &&
            (SemanticPred.isPureUnit(children[0]) ||
                SemanticPred.isUnitCounter(children[0])) &&
            node.childNodes.slice(1).every(SemanticPred.isPureUnit)) {
            node.role = "unit";
        }
    }
    return false;
});


/***/ }),

/***/ 8901:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.partitionNodes = exports.sliceNodes = exports.getEmbellishedInner = exports.addAttributes = exports.isZeroLength = exports.purgeNodes = exports.isOrphanedGlyph = exports.hasDisplayTag = exports.hasEmptyTag = exports.hasIgnoreTag = exports.hasLeafTag = exports.hasMathTag = exports.directSpeechKeys = exports.DISPLAYTAGS = exports.EMPTYTAGS = exports.IGNORETAGS = exports.LEAFTAGS = void 0;
const DomUtil = __webpack_require__(6671);
exports.LEAFTAGS = ['MO', 'MI', 'MN', 'MTEXT', 'MS', 'MSPACE'];
exports.IGNORETAGS = [
    'MERROR',
    'MPHANTOM',
    'MALIGNGROUP',
    'MALIGNMARK',
    'MPRESCRIPTS',
    'ANNOTATION',
    'ANNOTATION-XML'
];
exports.EMPTYTAGS = [
    'MATH',
    'MROW',
    'MPADDED',
    'MACTION',
    'NONE',
    'MSTYLE',
    'SEMANTICS'
];
exports.DISPLAYTAGS = ['MROOT', 'MSQRT'];
exports.directSpeechKeys = ['aria-label', 'exact-speech', 'alt'];
function hasMathTag(node) {
    return !!node && DomUtil.tagName(node) === 'MATH';
}
exports.hasMathTag = hasMathTag;
function hasLeafTag(node) {
    return !!node && exports.LEAFTAGS.indexOf(DomUtil.tagName(node)) !== -1;
}
exports.hasLeafTag = hasLeafTag;
function hasIgnoreTag(node) {
    return !!node && exports.IGNORETAGS.indexOf(DomUtil.tagName(node)) !== -1;
}
exports.hasIgnoreTag = hasIgnoreTag;
function hasEmptyTag(node) {
    return !!node && exports.EMPTYTAGS.indexOf(DomUtil.tagName(node)) !== -1;
}
exports.hasEmptyTag = hasEmptyTag;
function hasDisplayTag(node) {
    return !!node && exports.DISPLAYTAGS.indexOf(DomUtil.tagName(node)) !== -1;
}
exports.hasDisplayTag = hasDisplayTag;
function isOrphanedGlyph(node) {
    return (!!node &&
        DomUtil.tagName(node) === 'MGLYPH' &&
        !hasLeafTag(node.parentNode));
}
exports.isOrphanedGlyph = isOrphanedGlyph;
function purgeNodes(nodes) {
    const nodeArray = [];
    for (let i = 0, node; (node = nodes[i]); i++) {
        if (node.nodeType !== DomUtil.NodeType.ELEMENT_NODE) {
            continue;
        }
        const tagName = DomUtil.tagName(node);
        if (exports.IGNORETAGS.indexOf(tagName) !== -1) {
            continue;
        }
        if (exports.EMPTYTAGS.indexOf(tagName) !== -1 && node.childNodes.length === 0) {
            continue;
        }
        nodeArray.push(node);
    }
    return nodeArray;
}
exports.purgeNodes = purgeNodes;
function isZeroLength(length) {
    if (!length) {
        return false;
    }
    const negativeNamedSpaces = [
        'negativeveryverythinmathspace',
        'negativeverythinmathspace',
        'negativethinmathspace',
        'negativemediummathspace',
        'negativethickmathspace',
        'negativeverythickmathspace',
        'negativeveryverythickmathspace'
    ];
    if (negativeNamedSpaces.indexOf(length) !== -1) {
        return true;
    }
    const value = length.match(/[0-9.]+/);
    if (!value) {
        return false;
    }
    return parseFloat(value[0]) === 0;
}
exports.isZeroLength = isZeroLength;
function addAttributes(to, from) {
    if (from.hasAttributes()) {
        const attrs = from.attributes;
        for (let i = attrs.length - 1; i >= 0; i--) {
            const key = attrs[i].name;
            if (key.match(/^ext/)) {
                to.attributes[key] = attrs[i].value;
                to.nobreaking = true;
            }
            if (exports.directSpeechKeys.indexOf(key) !== -1) {
                to.attributes['ext-speech'] = attrs[i].value;
                to.nobreaking = true;
            }
            if (key.match(/texclass$/)) {
                to.attributes['texclass'] = attrs[i].value;
            }
            if (key === 'href') {
                to.attributes['href'] = attrs[i].value;
                to.nobreaking = true;
            }
        }
    }
}
exports.addAttributes = addAttributes;
function getEmbellishedInner(node) {
    if (node && node.embellished && node.childNodes.length > 0) {
        return getEmbellishedInner(node.childNodes[0]);
    }
    return node;
}
exports.getEmbellishedInner = getEmbellishedInner;
function sliceNodes(nodes, pred, opt_reverse) {
    if (opt_reverse) {
        nodes.reverse();
    }
    const head = [];
    for (let i = 0, node; (node = nodes[i]); i++) {
        if (pred(node)) {
            if (opt_reverse) {
                return {
                    head: nodes.slice(i + 1).reverse(),
                    div: node,
                    tail: head.reverse()
                };
            }
            return { head: head, div: node, tail: nodes.slice(i + 1) };
        }
        head.push(node);
    }
    if (opt_reverse) {
        return { head: [], div: null, tail: head.reverse() };
    }
    return { head: head, div: null, tail: [] };
}
exports.sliceNodes = sliceNodes;
function partitionNodes(nodes, pred) {
    let restNodes = nodes;
    const rel = [];
    const comp = [];
    let result = null;
    do {
        result = sliceNodes(restNodes, pred);
        comp.push(result.head);
        rel.push(result.div);
        restNodes = result.tail;
    } while (result.div);
    rel.pop();
    return { rel: rel, comp: comp };
}
exports.partitionNodes = partitionNodes;


/***/ }),

/***/ 9135:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AbstractSpeechGenerator = void 0;
const engine_setup_1 = __webpack_require__(985);
const EnrichAttr = __webpack_require__(8171);
const rebuild_stree_1 = __webpack_require__(1848);
const SpeechGeneratorUtil = __webpack_require__(144);
class AbstractSpeechGenerator {
    constructor() {
        this.modality = EnrichAttr.addPrefix('speech');
        this.rebuilt_ = null;
        this.options_ = {};
    }
    getRebuilt() {
        return this.rebuilt_;
    }
    setRebuilt(rebuilt) {
        this.rebuilt_ = rebuilt;
    }
    setOptions(options) {
        this.options_ = options || {};
        this.modality = EnrichAttr.addPrefix(this.options_.modality || 'speech');
    }
    getOptions() {
        return this.options_;
    }
    start() { }
    end() { }
    generateSpeech(_node, xml) {
        if (!this.rebuilt_) {
            this.rebuilt_ = new rebuild_stree_1.RebuildStree(xml);
        }
        (0, engine_setup_1.setup)(this.options_);
        return SpeechGeneratorUtil.computeMarkup(this.getRebuilt().xml);
    }
}
exports.AbstractSpeechGenerator = AbstractSpeechGenerator;


/***/ }),

/***/ 3153:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AdhocSpeechGenerator = void 0;
const abstract_speech_generator_1 = __webpack_require__(9135);
class AdhocSpeechGenerator extends abstract_speech_generator_1.AbstractSpeechGenerator {
    getSpeech(node, xml) {
        const speech = this.generateSpeech(node, xml);
        node.setAttribute(this.modality, speech);
        return speech;
    }
}
exports.AdhocSpeechGenerator = AdhocSpeechGenerator;


/***/ }),

/***/ 6281:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ColorGenerator = void 0;
const enrich_attr_1 = __webpack_require__(8171);
const color_picker_1 = __webpack_require__(1123);
const rebuild_stree_1 = __webpack_require__(1848);
const WalkerUtil = __webpack_require__(8835);
const abstract_speech_generator_1 = __webpack_require__(9135);
class ColorGenerator extends abstract_speech_generator_1.AbstractSpeechGenerator {
    constructor() {
        super(...arguments);
        this.modality = (0, enrich_attr_1.addPrefix)('foreground');
        this.contrast = new color_picker_1.ContrastPicker();
    }
    static visitStree_(tree, leaves, ignore) {
        if (!tree.childNodes.length) {
            if (!ignore[tree.id]) {
                leaves.push(tree.id);
            }
            return;
        }
        if (tree.contentNodes.length) {
            if (tree.type === 'punctuated') {
                tree.contentNodes.forEach((x) => (ignore[x.id] = true));
            }
            if (tree.role !== 'implicit') {
                leaves.push(tree.contentNodes.map((x) => x.id));
            }
        }
        if (tree.childNodes.length) {
            if (tree.role === 'implicit') {
                const factors = [];
                let rest = [];
                for (const child of tree.childNodes) {
                    const tt = [];
                    ColorGenerator.visitStree_(child, tt, ignore);
                    if (tt.length <= 2) {
                        factors.push(tt.shift());
                    }
                    rest = rest.concat(tt);
                }
                leaves.push(factors);
                rest.forEach((x) => leaves.push(x));
                return;
            }
            tree.childNodes.forEach((x) => ColorGenerator.visitStree_(x, leaves, ignore));
        }
    }
    getSpeech(node, _xml) {
        return WalkerUtil.getAttribute(node, this.modality);
    }
    generateSpeech(node, _xml) {
        if (!this.getRebuilt()) {
            this.setRebuilt(new rebuild_stree_1.RebuildStree(node));
        }
        this.colorLeaves_(node);
        return WalkerUtil.getAttribute(node, this.modality);
    }
    colorLeaves_(node) {
        const leaves = [];
        ColorGenerator.visitStree_(this.getRebuilt().streeRoot, leaves, {});
        for (const id of leaves) {
            const color = this.contrast.generate();
            let success = false;
            if (Array.isArray(id)) {
                success = id
                    .map((x) => this.colorLeave_(node, x, color))
                    .reduce((x, y) => x || y, false);
            }
            else {
                success = this.colorLeave_(node, id.toString(), color);
            }
            if (success) {
                this.contrast.increment();
            }
        }
    }
    colorLeave_(node, id, color) {
        const aux = WalkerUtil.getBySemanticId(node, id);
        if (aux) {
            aux.setAttribute(this.modality, color);
            return true;
        }
        return false;
    }
}
exports.ColorGenerator = ColorGenerator;


/***/ }),

/***/ 1565:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DirectSpeechGenerator = void 0;
const WalkerUtil = __webpack_require__(8835);
const abstract_speech_generator_1 = __webpack_require__(9135);
class DirectSpeechGenerator extends abstract_speech_generator_1.AbstractSpeechGenerator {
    getSpeech(node, _xml) {
        return WalkerUtil.getAttribute(node, this.modality);
    }
}
exports.DirectSpeechGenerator = DirectSpeechGenerator;


/***/ }),

/***/ 7721:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DummySpeechGenerator = void 0;
const abstract_speech_generator_1 = __webpack_require__(9135);
class DummySpeechGenerator extends abstract_speech_generator_1.AbstractSpeechGenerator {
    getSpeech(_node, _xml) {
        return '';
    }
}
exports.DummySpeechGenerator = DummySpeechGenerator;


/***/ }),

/***/ 1558:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.NodeSpeechGenerator = void 0;
const WalkerUtil = __webpack_require__(8835);
const tree_speech_generator_1 = __webpack_require__(7486);
class NodeSpeechGenerator extends tree_speech_generator_1.TreeSpeechGenerator {
    getSpeech(node, _xml) {
        super.getSpeech(node, _xml);
        return WalkerUtil.getAttribute(node, this.modality);
    }
}
exports.NodeSpeechGenerator = NodeSpeechGenerator;


/***/ }),

/***/ 7317:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.generatorMapping_ = exports.generator = void 0;
const adhoc_speech_generator_1 = __webpack_require__(3153);
const color_generator_1 = __webpack_require__(6281);
const direct_speech_generator_1 = __webpack_require__(1565);
const dummy_speech_generator_1 = __webpack_require__(7721);
const node_speech_generator_1 = __webpack_require__(1558);
const summary_speech_generator_1 = __webpack_require__(5778);
const tree_speech_generator_1 = __webpack_require__(7486);
function generator(type) {
    const constructor = exports.generatorMapping_[type] || exports.generatorMapping_.Direct;
    return constructor();
}
exports.generator = generator;
exports.generatorMapping_ = {
    Adhoc: () => new adhoc_speech_generator_1.AdhocSpeechGenerator(),
    Color: () => new color_generator_1.ColorGenerator(),
    Direct: () => new direct_speech_generator_1.DirectSpeechGenerator(),
    Dummy: () => new dummy_speech_generator_1.DummySpeechGenerator(),
    Node: () => new node_speech_generator_1.NodeSpeechGenerator(),
    Summary: () => new summary_speech_generator_1.SummarySpeechGenerator(),
    Tree: () => new tree_speech_generator_1.TreeSpeechGenerator()
};


/***/ }),

/***/ 144:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.computeSummary_ = exports.retrieveSummary = exports.connectAllMactions = exports.connectMactions = exports.nodeAtPosition_ = exports.computePrefix_ = exports.retrievePrefix = exports.addPrefix = exports.addModality = exports.addSpeech = exports.recomputeMarkup = exports.computeMarkup = exports.recomputeSpeech = exports.computeSpeech = void 0;
const AuralRendering = __webpack_require__(4253);
const DomUtil = __webpack_require__(6671);
const XpathUtil = __webpack_require__(5024);
const enrich_attr_1 = __webpack_require__(8171);
const speech_rule_engine_1 = __webpack_require__(6060);
const semantic_tree_1 = __webpack_require__(1784);
const WalkerUtil = __webpack_require__(8835);
function computeSpeech(xml) {
    return speech_rule_engine_1.SpeechRuleEngine.getInstance().evaluateNode(xml);
}
exports.computeSpeech = computeSpeech;
function recomputeSpeech(semantic) {
    const tree = semantic_tree_1.SemanticTree.fromNode(semantic);
    return computeSpeech(tree.xml());
}
exports.recomputeSpeech = recomputeSpeech;
function computeMarkup(tree) {
    const descrs = computeSpeech(tree);
    return AuralRendering.markup(descrs);
}
exports.computeMarkup = computeMarkup;
function recomputeMarkup(semantic) {
    const descrs = recomputeSpeech(semantic);
    return AuralRendering.markup(descrs);
}
exports.recomputeMarkup = recomputeMarkup;
function addSpeech(mml, semantic, snode) {
    const sxml = DomUtil.querySelectorAllByAttrValue(snode, 'id', semantic.id.toString())[0];
    const speech = sxml
        ? AuralRendering.markup(computeSpeech(sxml))
        : recomputeMarkup(semantic);
    mml.setAttribute(enrich_attr_1.Attribute.SPEECH, speech);
}
exports.addSpeech = addSpeech;
function addModality(mml, semantic, modality) {
    const markup = recomputeMarkup(semantic);
    mml.setAttribute(modality, markup);
}
exports.addModality = addModality;
function addPrefix(mml, semantic) {
    const speech = retrievePrefix(semantic);
    if (speech) {
        mml.setAttribute(enrich_attr_1.Attribute.PREFIX, speech);
    }
}
exports.addPrefix = addPrefix;
function retrievePrefix(semantic) {
    const descrs = computePrefix_(semantic);
    return AuralRendering.markup(descrs);
}
exports.retrievePrefix = retrievePrefix;
function computePrefix_(semantic) {
    const tree = semantic_tree_1.SemanticTree.fromRoot(semantic);
    const nodes = XpathUtil.evalXPath('.//*[@id="' + semantic.id + '"]', tree.xml());
    let node = nodes[0];
    if (nodes.length > 1) {
        node = nodeAtPosition_(semantic, nodes) || node;
    }
    return node
        ? speech_rule_engine_1.SpeechRuleEngine.getInstance().runInSetting({
            modality: 'prefix',
            domain: 'default',
            style: 'default',
            strict: true,
            speech: true
        }, function () {
            return speech_rule_engine_1.SpeechRuleEngine.getInstance().evaluateNode(node);
        })
        : [];
}
exports.computePrefix_ = computePrefix_;
function nodeAtPosition_(semantic, nodes) {
    const node = nodes[0];
    if (!semantic.parent) {
        return node;
    }
    const path = [];
    while (semantic) {
        path.push(semantic.id);
        semantic = semantic.parent;
    }
    const pathEquals = function (xml, path) {
        while (path.length &&
            path.shift().toString() === xml.getAttribute('id') &&
            xml.parentNode &&
            xml.parentNode.parentNode) {
            xml = xml.parentNode.parentNode;
        }
        return !path.length;
    };
    for (let i = 0, xml; (xml = nodes[i]); i++) {
        if (pathEquals(xml, path.slice())) {
            return xml;
        }
    }
    return node;
}
exports.nodeAtPosition_ = nodeAtPosition_;
function connectMactions(node, mml, stree) {
    const mactions = DomUtil.querySelectorAll(mml, 'maction');
    for (let i = 0, maction; (maction = mactions[i]); i++) {
        const aid = maction.getAttribute('id');
        const span = DomUtil.querySelectorAllByAttrValue(node, 'id', aid)[0];
        if (!span) {
            continue;
        }
        const lchild = maction.childNodes[1];
        const mid = lchild.getAttribute(enrich_attr_1.Attribute.ID);
        let cspan = WalkerUtil.getBySemanticId(node, mid);
        if (cspan && cspan.getAttribute(enrich_attr_1.Attribute.TYPE) !== 'dummy') {
            continue;
        }
        cspan = span.childNodes[0];
        if (cspan.getAttribute('sre-highlighter-added')) {
            continue;
        }
        const pid = lchild.getAttribute(enrich_attr_1.Attribute.PARENT);
        if (pid) {
            cspan.setAttribute(enrich_attr_1.Attribute.PARENT, pid);
        }
        cspan.setAttribute(enrich_attr_1.Attribute.TYPE, 'dummy');
        cspan.setAttribute(enrich_attr_1.Attribute.ID, mid);
        const cst = DomUtil.querySelectorAllByAttrValue(stree, 'id', mid)[0];
        cst.setAttribute('alternative', mid);
    }
}
exports.connectMactions = connectMactions;
function connectAllMactions(mml, stree) {
    const mactions = DomUtil.querySelectorAll(mml, 'maction');
    for (let i = 0, maction; (maction = mactions[i]); i++) {
        const lchild = maction.childNodes[1];
        const mid = lchild.getAttribute(enrich_attr_1.Attribute.ID);
        const cst = DomUtil.querySelectorAllByAttrValue(stree, 'id', mid)[0];
        cst.setAttribute('alternative', mid);
    }
}
exports.connectAllMactions = connectAllMactions;
function retrieveSummary(node) {
    const descrs = computeSummary_(node);
    return AuralRendering.markup(descrs);
}
exports.retrieveSummary = retrieveSummary;
function computeSummary_(node) {
    return node
        ? speech_rule_engine_1.SpeechRuleEngine.getInstance().runInSetting({ modality: 'summary', strict: false, speech: true }, function () {
            return speech_rule_engine_1.SpeechRuleEngine.getInstance().evaluateNode(node);
        })
        : [];
}
exports.computeSummary_ = computeSummary_;


/***/ }),

/***/ 5778:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SummarySpeechGenerator = void 0;
const abstract_speech_generator_1 = __webpack_require__(9135);
const SpeechGeneratorUtil = __webpack_require__(144);
class SummarySpeechGenerator extends abstract_speech_generator_1.AbstractSpeechGenerator {
    getSpeech(node, xml) {
        SpeechGeneratorUtil.connectAllMactions(xml, this.getRebuilt().xml);
        return this.generateSpeech(node, xml);
    }
}
exports.SummarySpeechGenerator = SummarySpeechGenerator;


/***/ }),

/***/ 7486:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TreeSpeechGenerator = void 0;
const enrich_attr_1 = __webpack_require__(8171);
const WalkerUtil = __webpack_require__(8835);
const abstract_speech_generator_1 = __webpack_require__(9135);
const SpeechGeneratorUtil = __webpack_require__(144);
class TreeSpeechGenerator extends abstract_speech_generator_1.AbstractSpeechGenerator {
    getSpeech(node, xml) {
        const speech = this.generateSpeech(node, xml);
        const nodes = this.getRebuilt().nodeDict;
        for (const key in nodes) {
            const snode = nodes[key];
            const innerMml = WalkerUtil.getBySemanticId(xml, key);
            const innerNode = WalkerUtil.getBySemanticId(node, key);
            if (!innerMml || !innerNode) {
                continue;
            }
            if (!this.modality || this.modality === enrich_attr_1.Attribute.SPEECH) {
                SpeechGeneratorUtil.addSpeech(innerNode, snode, this.getRebuilt().xml);
            }
            else {
                SpeechGeneratorUtil.addModality(innerNode, snode, this.modality);
            }
            if (this.modality === enrich_attr_1.Attribute.SPEECH) {
                SpeechGeneratorUtil.addPrefix(innerNode, snode);
            }
        }
        return speech;
    }
}
exports.TreeSpeechGenerator = TreeSpeechGenerator;


/***/ }),

/***/ 650:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.INTERVALS = exports.makeLetter = exports.numberRules = exports.alphabetRules = exports.getFont = exports.makeInterval = exports.generate = exports.makeDomains_ = exports.Domains_ = exports.Base = exports.Embellish = exports.Font = void 0;
const engine_1 = __webpack_require__(4886);
const L10n = __webpack_require__(2371);
const locale_1 = __webpack_require__(4524);
const locale_util_1 = __webpack_require__(3319);
const MathCompoundStore = __webpack_require__(4161);
var Font;
(function (Font) {
    Font["BOLD"] = "bold";
    Font["BOLDFRAKTUR"] = "bold-fraktur";
    Font["BOLDITALIC"] = "bold-italic";
    Font["BOLDSCRIPT"] = "bold-script";
    Font["DOUBLESTRUCK"] = "double-struck";
    Font["FULLWIDTH"] = "fullwidth";
    Font["FRAKTUR"] = "fraktur";
    Font["ITALIC"] = "italic";
    Font["MONOSPACE"] = "monospace";
    Font["NORMAL"] = "normal";
    Font["SCRIPT"] = "script";
    Font["SANSSERIF"] = "sans-serif";
    Font["SANSSERIFITALIC"] = "sans-serif-italic";
    Font["SANSSERIFBOLD"] = "sans-serif-bold";
    Font["SANSSERIFBOLDITALIC"] = "sans-serif-bold-italic";
})(Font = exports.Font || (exports.Font = {}));
var Embellish;
(function (Embellish) {
    Embellish["SUPER"] = "super";
    Embellish["SUB"] = "sub";
    Embellish["CIRCLED"] = "circled";
    Embellish["PARENTHESIZED"] = "parenthesized";
    Embellish["PERIOD"] = "period";
    Embellish["NEGATIVECIRCLED"] = "negative-circled";
    Embellish["DOUBLECIRCLED"] = "double-circled";
    Embellish["CIRCLEDSANSSERIF"] = "circled-sans-serif";
    Embellish["NEGATIVECIRCLEDSANSSERIF"] = "negative-circled-sans-serif";
    Embellish["COMMA"] = "comma";
    Embellish["SQUARED"] = "squared";
    Embellish["NEGATIVESQUARED"] = "negative-squared";
})(Embellish = exports.Embellish || (exports.Embellish = {}));
var Base;
(function (Base) {
    Base["LATINCAP"] = "latinCap";
    Base["LATINSMALL"] = "latinSmall";
    Base["GREEKCAP"] = "greekCap";
    Base["GREEKSMALL"] = "greekSmall";
    Base["DIGIT"] = "digit";
})(Base = exports.Base || (exports.Base = {}));
exports.Domains_ = {
    small: ['default'],
    capital: ['default'],
    digit: ['default']
};
function makeDomains_() {
    const alph = locale_1.LOCALE.ALPHABETS;
    const combineKeys = (obj1, obj2) => {
        const result = {};
        Object.keys(obj1).forEach((k) => (result[k] = true));
        Object.keys(obj2).forEach((k) => (result[k] = true));
        return Object.keys(result);
    };
    exports.Domains_.small = combineKeys(alph.smallPrefix, alph.letterTrans);
    exports.Domains_.capital = combineKeys(alph.capPrefix, alph.letterTrans);
    exports.Domains_.digit = combineKeys(alph.digitPrefix, alph.digitTrans);
}
exports.makeDomains_ = makeDomains_;
function generate(locale) {
    const oldLocale = engine_1.default.getInstance().locale;
    engine_1.default.getInstance().locale = locale;
    L10n.setLocale();
    MathCompoundStore.addSymbolRules({ locale: locale });
    makeDomains_();
    const intervals = exports.INTERVALS;
    for (let i = 0, int; (int = intervals[i]); i++) {
        const keys = makeInterval(int.interval, int.subst);
        const letters = keys.map(function (x) {
            return String.fromCodePoint(parseInt(x, 16));
        });
        if ('offset' in int) {
            numberRules(keys, letters, int.font, int.category, int.offset || 0);
        }
        else {
            const alphabet = locale_1.LOCALE.ALPHABETS[int.base];
            alphabetRules(keys, letters, alphabet, int.font, int.category, !!int.capital);
        }
    }
    engine_1.default.getInstance().locale = oldLocale;
    L10n.setLocale();
}
exports.generate = generate;
function num2str(num) {
    const str = num.toString(16).toUpperCase();
    return str.length > 3 ? str : ('000' + str).slice(-4);
}
function makeInterval([a, b], subst) {
    const start = parseInt(a, 16);
    const end = parseInt(b, 16);
    const result = [];
    for (let i = start; i <= end; i++) {
        let key = num2str(i);
        const sub = subst[key];
        if (sub === false) {
            continue;
        }
        key = subst[key] || key;
        result.push(key);
    }
    return result;
}
exports.makeInterval = makeInterval;
function getFont(font) {
    const realFont = font === 'normal' || font === 'fullwidth'
        ? ''
        : locale_1.LOCALE.MESSAGES.font[font] || locale_1.LOCALE.MESSAGES.embellish[font] || '';
    return (0, locale_util_1.localeFontCombiner)(realFont);
}
exports.getFont = getFont;
function alphabetRules(keys, unicodes, letters, font, category, cap) {
    const realFont = getFont(font);
    for (let i = 0, key, unicode, letter; (key = keys[i]), (unicode = unicodes[i]), (letter = letters[i]); i++) {
        const prefixes = cap
            ? locale_1.LOCALE.ALPHABETS.capPrefix
            : locale_1.LOCALE.ALPHABETS.smallPrefix;
        const domains = cap ? exports.Domains_.capital : exports.Domains_.small;
        makeLetter(realFont.combiner, key, unicode, letter, realFont.font, prefixes, category, locale_1.LOCALE.ALPHABETS.letterTrans, domains);
    }
}
exports.alphabetRules = alphabetRules;
function numberRules(keys, unicodes, font, category, offset) {
    const realFont = getFont(font);
    for (let i = 0, key, unicode; (key = keys[i]), (unicode = unicodes[i]); i++) {
        const prefixes = locale_1.LOCALE.ALPHABETS.digitPrefix;
        const num = i + offset;
        makeLetter(realFont.combiner, key, unicode, num, realFont.font, prefixes, category, locale_1.LOCALE.ALPHABETS.digitTrans, exports.Domains_.digit);
    }
}
exports.numberRules = numberRules;
function makeLetter(combiner, key, unicode, letter, font, prefixes, category, transformers, domains) {
    for (let i = 0, domain; (domain = domains[i]); i++) {
        const transformer = domain in transformers ? transformers[domain] : transformers['default'];
        const prefix = domain in prefixes ? prefixes[domain] : prefixes['default'];
        MathCompoundStore.defineRule(key.toString(), domain, 'default', category, unicode, combiner(transformer(letter), font, prefix));
    }
}
exports.makeLetter = makeLetter;
exports.INTERVALS = [
    {
        interval: ['1D400', '1D419'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.BOLD
    },
    {
        interval: ['1D41A', '1D433'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.BOLD
    },
    {
        interval: ['1D56C', '1D585'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.BOLDFRAKTUR
    },
    {
        interval: ['1D586', '1D59F'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.BOLDFRAKTUR
    },
    {
        interval: ['1D468', '1D481'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.BOLDITALIC
    },
    {
        interval: ['1D482', '1D49B'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.BOLDITALIC
    },
    {
        interval: ['1D4D0', '1D4E9'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.BOLDSCRIPT
    },
    {
        interval: ['1D4EA', '1D503'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.BOLDSCRIPT
    },
    {
        interval: ['1D538', '1D551'],
        base: Base.LATINCAP,
        subst: {
            '1D53A': '2102',
            '1D53F': '210D',
            '1D545': '2115',
            '1D547': '2119',
            '1D548': '211A',
            '1D549': '211D',
            '1D551': '2124'
        },
        capital: true,
        category: 'Lu',
        font: Font.DOUBLESTRUCK
    },
    {
        interval: ['1D552', '1D56B'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.DOUBLESTRUCK
    },
    {
        interval: ['1D504', '1D51D'],
        base: Base.LATINCAP,
        subst: {
            '1D506': '212D',
            '1D50B': '210C',
            '1D50C': '2111',
            '1D515': '211C',
            '1D51D': '2128'
        },
        capital: true,
        category: 'Lu',
        font: Font.FRAKTUR
    },
    {
        interval: ['1D51E', '1D537'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.FRAKTUR
    },
    {
        interval: ['FF21', 'FF3A'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.FULLWIDTH
    },
    {
        interval: ['FF41', 'FF5A'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.FULLWIDTH
    },
    {
        interval: ['1D434', '1D44D'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.ITALIC
    },
    {
        interval: ['1D44E', '1D467'],
        base: Base.LATINSMALL,
        subst: { '1D455': '210E' },
        capital: false,
        category: 'Ll',
        font: Font.ITALIC
    },
    {
        interval: ['1D670', '1D689'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.MONOSPACE
    },
    {
        interval: ['1D68A', '1D6A3'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.MONOSPACE
    },
    {
        interval: ['0041', '005A'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.NORMAL
    },
    {
        interval: ['0061', '007A'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.NORMAL
    },
    {
        interval: ['1D49C', '1D4B5'],
        base: Base.LATINCAP,
        subst: {
            '1D49D': '212C',
            '1D4A0': '2130',
            '1D4A1': '2131',
            '1D4A3': '210B',
            '1D4A4': '2110',
            '1D4A7': '2112',
            '1D4A8': '2133',
            '1D4AD': '211B'
        },
        capital: true,
        category: 'Lu',
        font: Font.SCRIPT
    },
    {
        interval: ['1D4B6', '1D4CF'],
        base: Base.LATINSMALL,
        subst: { '1D4BA': '212F', '1D4BC': '210A', '1D4C4': '2134' },
        capital: false,
        category: 'Ll',
        font: Font.SCRIPT
    },
    {
        interval: ['1D5A0', '1D5B9'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.SANSSERIF
    },
    {
        interval: ['1D5BA', '1D5D3'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.SANSSERIF
    },
    {
        interval: ['1D608', '1D621'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.SANSSERIFITALIC
    },
    {
        interval: ['1D622', '1D63B'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.SANSSERIFITALIC
    },
    {
        interval: ['1D5D4', '1D5ED'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.SANSSERIFBOLD
    },
    {
        interval: ['1D5EE', '1D607'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.SANSSERIFBOLD
    },
    {
        interval: ['1D63C', '1D655'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.SANSSERIFBOLDITALIC
    },
    {
        interval: ['1D656', '1D66F'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.SANSSERIFBOLDITALIC
    },
    {
        interval: ['0391', '03A9'],
        base: Base.GREEKCAP,
        subst: { '03A2': '03F4' },
        capital: true,
        category: 'Lu',
        font: Font.NORMAL
    },
    {
        interval: ['03B0', '03D0'],
        base: Base.GREEKSMALL,
        subst: {
            '03B0': '2207',
            '03CA': '2202',
            '03CB': '03F5',
            '03CC': '03D1',
            '03CD': '03F0',
            '03CE': '03D5',
            '03CF': '03F1',
            '03D0': '03D6'
        },
        capital: false,
        category: 'Ll',
        font: Font.NORMAL
    },
    {
        interval: ['1D6A8', '1D6C0'],
        base: Base.GREEKCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.BOLD
    },
    {
        interval: ['1D6C1', '1D6E1'],
        base: Base.GREEKSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.BOLD
    },
    {
        interval: ['1D6E2', '1D6FA'],
        base: Base.GREEKCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.ITALIC
    },
    {
        interval: ['1D6FB', '1D71B'],
        base: Base.GREEKSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.ITALIC
    },
    {
        interval: ['1D71C', '1D734'],
        base: Base.GREEKCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.BOLDITALIC
    },
    {
        interval: ['1D735', '1D755'],
        base: Base.GREEKSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.BOLDITALIC
    },
    {
        interval: ['1D756', '1D76E'],
        base: Base.GREEKCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.SANSSERIFBOLD
    },
    {
        interval: ['1D76F', '1D78F'],
        base: Base.GREEKSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.SANSSERIFBOLD
    },
    {
        interval: ['1D790', '1D7A8'],
        base: Base.GREEKCAP,
        subst: {},
        capital: true,
        category: 'Lu',
        font: Font.SANSSERIFBOLDITALIC
    },
    {
        interval: ['1D7A9', '1D7C9'],
        base: Base.GREEKSMALL,
        subst: {},
        capital: false,
        category: 'Ll',
        font: Font.SANSSERIFBOLDITALIC
    },
    {
        interval: ['0030', '0039'],
        base: Base.DIGIT,
        subst: {},
        offset: 0,
        category: 'Nd',
        font: Font.NORMAL
    },
    {
        interval: ['2070', '2079'],
        base: Base.DIGIT,
        subst: { 2071: '00B9', 2072: '00B2', 2073: '00B3' },
        offset: 0,
        category: 'No',
        font: Embellish.SUPER
    },
    {
        interval: ['2080', '2089'],
        base: Base.DIGIT,
        subst: {},
        offset: 0,
        category: 'No',
        font: Embellish.SUB
    },
    {
        interval: ['245F', '2473'],
        base: Base.DIGIT,
        subst: { '245F': '24EA' },
        offset: 0,
        category: 'No',
        font: Embellish.CIRCLED
    },
    {
        interval: ['3251', '325F'],
        base: Base.DIGIT,
        subst: {},
        offset: 21,
        category: 'No',
        font: Embellish.CIRCLED
    },
    {
        interval: ['32B1', '32BF'],
        base: Base.DIGIT,
        subst: {},
        offset: 36,
        category: 'No',
        font: Embellish.CIRCLED
    },
    {
        interval: ['2474', '2487'],
        base: Base.DIGIT,
        subst: {},
        offset: 1,
        category: 'No',
        font: Embellish.PARENTHESIZED
    },
    {
        interval: ['2487', '249B'],
        base: Base.DIGIT,
        subst: { 2487: '1F100' },
        offset: 0,
        category: 'No',
        font: Embellish.PERIOD
    },
    {
        interval: ['2775', '277F'],
        base: Base.DIGIT,
        subst: { 2775: '24FF' },
        offset: 0,
        category: 'No',
        font: Embellish.NEGATIVECIRCLED
    },
    {
        interval: ['24EB', '24F4'],
        base: Base.DIGIT,
        subst: {},
        offset: 11,
        category: 'No',
        font: Embellish.NEGATIVECIRCLED
    },
    {
        interval: ['24F5', '24FE'],
        base: Base.DIGIT,
        subst: {},
        offset: 1,
        category: 'No',
        font: Embellish.DOUBLECIRCLED
    },
    {
        interval: ['277F', '2789'],
        base: Base.DIGIT,
        subst: { '277F': '1F10B' },
        offset: 0,
        category: 'No',
        font: Embellish.CIRCLEDSANSSERIF
    },
    {
        interval: ['2789', '2793'],
        base: Base.DIGIT,
        subst: { 2789: '1F10C' },
        offset: 0,
        category: 'No',
        font: Embellish.NEGATIVECIRCLEDSANSSERIF
    },
    {
        interval: ['FF10', 'FF19'],
        base: Base.DIGIT,
        subst: {},
        offset: 0,
        category: 'Nd',
        font: Font.FULLWIDTH
    },
    {
        interval: ['1D7CE', '1D7D7'],
        base: Base.DIGIT,
        subst: {},
        offset: 0,
        category: 'Nd',
        font: Font.BOLD
    },
    {
        interval: ['1D7D8', '1D7E1'],
        base: Base.DIGIT,
        subst: {},
        offset: 0,
        category: 'Nd',
        font: Font.DOUBLESTRUCK
    },
    {
        interval: ['1D7E2', '1D7EB'],
        base: Base.DIGIT,
        subst: {},
        offset: 0,
        category: 'Nd',
        font: Font.SANSSERIF
    },
    {
        interval: ['1D7EC', '1D7F5'],
        base: Base.DIGIT,
        subst: {},
        offset: 0,
        category: 'Nd',
        font: Font.SANSSERIFBOLD
    },
    {
        interval: ['1D7F6', '1D7FF'],
        base: Base.DIGIT,
        subst: {},
        offset: 0,
        category: 'Nd',
        font: Font.MONOSPACE
    },
    {
        interval: ['1F101', '1F10A'],
        base: Base.DIGIT,
        subst: {},
        offset: 0,
        category: 'No',
        font: Embellish.COMMA
    },
    {
        interval: ['24B6', '24CF'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'So',
        font: Embellish.CIRCLED
    },
    {
        interval: ['24D0', '24E9'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'So',
        font: Embellish.CIRCLED
    },
    {
        interval: ['1F110', '1F129'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'So',
        font: Embellish.PARENTHESIZED
    },
    {
        interval: ['249C', '24B5'],
        base: Base.LATINSMALL,
        subst: {},
        capital: false,
        category: 'So',
        font: Embellish.PARENTHESIZED
    },
    {
        interval: ['1F130', '1F149'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'So',
        font: Embellish.SQUARED
    },
    {
        interval: ['1F170', '1F189'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'So',
        font: Embellish.NEGATIVESQUARED
    },
    {
        interval: ['1F150', '1F169'],
        base: Base.LATINCAP,
        subst: {},
        capital: true,
        category: 'So',
        font: Embellish.NEGATIVECIRCLED
    }
];


/***/ }),

/***/ 3955:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Parser = exports.Comparator = exports.ClearspeakPreferences = void 0;
const engine_1 = __webpack_require__(4886);
const EngineConst = __webpack_require__(4998);
const dynamic_cstr_1 = __webpack_require__(8310);
const dynamic_cstr_2 = __webpack_require__(8310);
const MathCompoundStore = __webpack_require__(4161);
const speech_rule_engine_1 = __webpack_require__(6060);
class ClearspeakPreferences extends dynamic_cstr_1.DynamicCstr {
    constructor(cstr, preference) {
        super(cstr);
        this.preference = preference;
    }
    static comparator() {
        return new Comparator(engine_1.default.getInstance().dynamicCstr, dynamic_cstr_2.DynamicProperties.createProp([dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_2.Axis.LOCALE]], [dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_2.Axis.MODALITY]], [dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_2.Axis.DOMAIN]], [dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_2.Axis.STYLE]]));
    }
    static fromPreference(pref) {
        const pairs = pref.split(':');
        const preferences = {};
        const properties = PREFERENCES.getProperties();
        const validKeys = Object.keys(properties);
        for (let i = 0, key; (key = pairs[i]); i++) {
            const pair = key.split('_');
            if (validKeys.indexOf(pair[0]) === -1) {
                continue;
            }
            const value = pair[1];
            if (value &&
                value !== ClearspeakPreferences.AUTO &&
                properties[pair[0]].indexOf(value) !== -1) {
                preferences[pair[0]] = pair[1];
            }
        }
        return preferences;
    }
    static toPreference(pref) {
        const keys = Object.keys(pref);
        const str = [];
        for (let i = 0; i < keys.length; i++) {
            str.push(keys[i] + '_' + pref[keys[i]]);
        }
        return str.length ? str.join(':') : dynamic_cstr_1.DynamicCstr.DEFAULT_VALUE;
    }
    static getLocalePreferences(opt_dynamic) {
        const dynamic = opt_dynamic ||
            MathCompoundStore.enumerate(speech_rule_engine_1.SpeechRuleEngine.getInstance().enumerate());
        return ClearspeakPreferences.getLocalePreferences_(dynamic);
    }
    static smartPreferences(item, locale) {
        const prefs = ClearspeakPreferences.getLocalePreferences();
        const loc = prefs[locale];
        if (!loc) {
            return [];
        }
        const explorer = item['explorers']['speech'];
        const smart = ClearspeakPreferences.relevantPreferences(explorer.walker.getFocus().getSemanticPrimary());
        const previous = EngineConst.DOMAIN_TO_STYLES['clearspeak'];
        const items = [
            {
                type: 'radio',
                content: 'No Preferences',
                id: 'clearspeak-default',
                variable: 'speechRules'
            },
            {
                type: 'radio',
                content: 'Current Preferences',
                id: 'clearspeak-' + previous,
                variable: 'speechRules'
            },
            { type: 'rule' },
            { type: 'label', content: 'Preferences for ' + smart },
            { type: 'rule' }
        ];
        return items.concat(loc[smart].map(function (x) {
            const pair = x.split('_');
            return {
                type: 'radio',
                content: pair[1],
                id: 'clearspeak-' +
                    ClearspeakPreferences.addPreference(previous, pair[0], pair[1]),
                variable: 'speechRules'
            };
        }));
    }
    static relevantPreferences(node) {
        const roles = SEMANTIC_MAPPING_[node.type];
        if (!roles) {
            return 'ImpliedTimes';
        }
        return roles[node.role] || roles[''] || 'ImpliedTimes';
    }
    static findPreference(prefs, kind) {
        if (prefs === 'default') {
            return ClearspeakPreferences.AUTO;
        }
        const parsed = ClearspeakPreferences.fromPreference(prefs);
        return parsed[kind] || ClearspeakPreferences.AUTO;
    }
    static addPreference(prefs, kind, value) {
        if (prefs === 'default') {
            return kind + '_' + value;
        }
        const parsed = ClearspeakPreferences.fromPreference(prefs);
        parsed[kind] = value;
        return ClearspeakPreferences.toPreference(parsed);
    }
    static getLocalePreferences_(dynamic) {
        const result = {};
        for (const locale in dynamic) {
            if (!dynamic[locale]['speech'] ||
                !dynamic[locale]['speech']['clearspeak']) {
                continue;
            }
            const locPrefs = Object.keys(dynamic[locale]['speech']['clearspeak']);
            const prefs = (result[locale] = {});
            for (const axis in PREFERENCES.getProperties()) {
                const allSty = PREFERENCES.getProperties()[axis];
                const values = [axis + '_Auto'];
                if (allSty) {
                    for (const sty of allSty) {
                        if (locPrefs.indexOf(axis + '_' + sty) !== -1) {
                            values.push(axis + '_' + sty);
                        }
                    }
                }
                prefs[axis] = values;
            }
        }
        return result;
    }
    equal(cstr) {
        const top = super.equal(cstr);
        if (!top) {
            return false;
        }
        const keys = Object.keys(this.preference);
        const preference = cstr.preference;
        if (keys.length !== Object.keys(preference).length) {
            return false;
        }
        for (let i = 0, key; (key = keys[i]); i++) {
            if (this.preference[key] !== preference[key]) {
                return false;
            }
        }
        return true;
    }
}
exports.ClearspeakPreferences = ClearspeakPreferences;
ClearspeakPreferences.AUTO = 'Auto';
const PREFERENCES = new dynamic_cstr_2.DynamicProperties({
    AbsoluteValue: ['Auto', 'AbsEnd', 'Cardinality', 'Determinant'],
    Bar: ['Auto', 'Conjugate'],
    Caps: ['Auto', 'SayCaps'],
    CombinationPermutation: ['Auto', 'ChoosePermute'],
    Currency: ['Auto', 'Position', 'Prefix'],
    Ellipses: ['Auto', 'AndSoOn'],
    Enclosed: ['Auto', 'EndEnclose'],
    Exponent: [
        'Auto',
        'AfterPower',
        'Ordinal',
        'OrdinalPower',
        'Exponent'
    ],
    Fraction: [
        'Auto',
        'EndFrac',
        'FracOver',
        'General',
        'GeneralEndFrac',
        'Ordinal',
        'Over',
        'OverEndFrac',
        'Per'
    ],
    Functions: [
        'Auto',
        'None',
        'Reciprocal'
    ],
    ImpliedTimes: ['Auto', 'MoreImpliedTimes', 'None'],
    Log: ['Auto', 'LnAsNaturalLog'],
    Matrix: [
        'Auto',
        'Combinatoric',
        'EndMatrix',
        'EndVector',
        'SilentColNum',
        'SpeakColNum',
        'Vector'
    ],
    MultiLineLabel: [
        'Auto',
        'Case',
        'Constraint',
        'Equation',
        'Line',
        'None',
        'Row',
        'Step'
    ],
    MultiLineOverview: ['Auto', 'None'],
    MultiLinePausesBetweenColumns: ['Auto', 'Long', 'Short'],
    MultsymbolDot: ['Auto', 'Dot'],
    MultsymbolX: ['Auto', 'By', 'Cross'],
    Paren: [
        'Auto',
        'CoordPoint',
        'Interval',
        'Silent',
        'Speak',
        'SpeakNestingLevel'
    ],
    Prime: ['Auto', 'Angle', 'Length'],
    Roots: ['Auto', 'PosNegSqRoot', 'PosNegSqRootEnd', 'RootEnd'],
    SetMemberSymbol: ['Auto', 'Belongs', 'Element', 'Member', 'In'],
    Sets: ['Auto', 'SilentBracket', 'woAll'],
    TriangleSymbol: ['Auto', 'Delta'],
    Trig: [
        'Auto',
        'ArcTrig',
        'TrigInverse',
        'Reciprocal'
    ],
    VerticalLine: ['Auto', 'Divides', 'Given', 'SuchThat']
});
class Comparator extends dynamic_cstr_2.DefaultComparator {
    constructor(cstr, props) {
        super(cstr, props);
        this.preference =
            cstr instanceof ClearspeakPreferences ? cstr.preference : {};
    }
    match(cstr) {
        if (!(cstr instanceof ClearspeakPreferences)) {
            return super.match(cstr);
        }
        if (cstr.getComponents()[dynamic_cstr_2.Axis.STYLE] === 'default') {
            return true;
        }
        const keys = Object.keys(cstr.preference);
        for (let i = 0, key; (key = keys[i]); i++) {
            if (this.preference[key] !== cstr.preference[key]) {
                return false;
            }
        }
        return true;
    }
    compare(cstr1, cstr2) {
        const top = super.compare(cstr1, cstr2);
        if (top !== 0) {
            return top;
        }
        const pref1 = cstr1 instanceof ClearspeakPreferences;
        const pref2 = cstr2 instanceof ClearspeakPreferences;
        if (!pref1 && pref2) {
            return 1;
        }
        if (pref1 && !pref2) {
            return -1;
        }
        if (!pref1 && !pref2) {
            return 0;
        }
        const length1 = Object.keys(cstr1.preference).length;
        const length2 = Object.keys(cstr2.preference).length;
        return length1 > length2 ? -1 : length1 < length2 ? 1 : 0;
    }
}
exports.Comparator = Comparator;
class Parser extends dynamic_cstr_2.DynamicCstrParser {
    constructor() {
        super([dynamic_cstr_2.Axis.LOCALE, dynamic_cstr_2.Axis.MODALITY, dynamic_cstr_2.Axis.DOMAIN, dynamic_cstr_2.Axis.STYLE]);
    }
    parse(str) {
        const initial = super.parse(str);
        let style = initial.getValue(dynamic_cstr_2.Axis.STYLE);
        const locale = initial.getValue(dynamic_cstr_2.Axis.LOCALE);
        const modality = initial.getValue(dynamic_cstr_2.Axis.MODALITY);
        let pref = {};
        if (style !== dynamic_cstr_1.DynamicCstr.DEFAULT_VALUE) {
            pref = this.fromPreference(style);
            style = this.toPreference(pref);
        }
        return new ClearspeakPreferences({
            locale: locale,
            modality: modality,
            domain: 'clearspeak',
            style: style
        }, pref);
    }
    fromPreference(pref) {
        return ClearspeakPreferences.fromPreference(pref);
    }
    toPreference(pref) {
        return ClearspeakPreferences.toPreference(pref);
    }
}
exports.Parser = Parser;
const REVERSE_MAPPING = [
    [
        'AbsoluteValue',
        "fenced",
        "neutral",
        "metric"
    ],
    ['Bar', "overscore", "overaccent"],
    ['Caps', "identifier", "latinletter"],
    ['CombinationPermutation', "appl", "unknown"],
    ['Ellipses', "punctuation", "ellipsis"],
    ['Exponent', "superscript", ''],
    ['Fraction', "fraction", ''],
    ['Functions', "appl", "simple function"],
    ['ImpliedTimes', "operator", "implicit"],
    ['Log', "appl", "prefix function"],
    ['Matrix', "matrix", ''],
    ['Matrix', "vector", ''],
    ['MultiLineLabel', "multiline", "label"],
    ['MultiLineOverview', "multiline", "table"],
    ['MultiLinePausesBetweenColumns', "multiline", "table"],
    ['MultiLineLabel', "table", "label"],
    ['MultiLineOverview', "table", "table"],
    ['MultiLinePausesBetweenColumns', "table", "table"],
    ['MultiLineLabel', "cases", "label"],
    ['MultiLineOverview', "cases", "table"],
    ['MultiLinePausesBetweenColumns', "cases", "table"],
    ['MultsymbolDot', "operator", "multiplication"],
    ['MultsymbolX', "operator", "multiplication"],
    ['Paren', "fenced", "leftright"],
    ['Prime', "superscript", "prime"],
    ['Roots', "root", ''],
    ['Roots', "sqrt", ''],
    ['SetMemberSymbol', "relation", "element"],
    ['Sets', "fenced", "set extended"],
    ['TriangleSymbol', "identifier", "greekletter"],
    ['Trig', "appl", "prefix function"],
    ['VerticalLine', "punctuated", "vbar"]
];
const SEMANTIC_MAPPING_ = (function () {
    const result = {};
    for (let i = 0, triple; (triple = REVERSE_MAPPING[i]); i++) {
        const pref = triple[0];
        let role = result[triple[1]];
        if (!role) {
            role = {};
            result[triple[1]] = role;
        }
        role[triple[2]] = pref;
    }
    return result;
})();
engine_1.default.getInstance().comparators['clearspeak'] =
    ClearspeakPreferences.comparator;
engine_1.default.getInstance().parsers['clearspeak'] = new Parser();


/***/ }),

/***/ 127:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ClearspeakRules = void 0;
const dynamic_cstr_1 = __webpack_require__(8310);
const StoreUtil = __webpack_require__(931);
const ClearspeakUtil = __webpack_require__(8662);
const MathspeakUtil = __webpack_require__(3269);
const NumbersUtil = __webpack_require__(2110);
const SpeechRules = __webpack_require__(7278);
function ClearspeakRules() {
    SpeechRules.addStore(dynamic_cstr_1.DynamicCstr.BASE_LOCALE + '.speech.clearspeak', '', {
        CTFpauseSeparator: StoreUtil.pauseSeparator,
        CTFnodeCounter: ClearspeakUtil.nodeCounter,
        CTFcontentIterator: StoreUtil.contentIterator,
        CSFvulgarFraction: NumbersUtil.vulgarFraction,
        CQFvulgarFractionSmall: ClearspeakUtil.isSmallVulgarFraction,
        CQFcellsSimple: ClearspeakUtil.allCellsSimple,
        CSFordinalExponent: ClearspeakUtil.ordinalExponent,
        CSFwordOrdinal: ClearspeakUtil.wordOrdinal,
        CQFmatchingFences: ClearspeakUtil.matchingFences,
        CSFnestingDepth: ClearspeakUtil.nestingDepth,
        CQFfencedArguments: ClearspeakUtil.fencedArguments,
        CQFsimpleArguments: ClearspeakUtil.simpleArguments,
        CQFspaceoutNumber: MathspeakUtil.spaceoutNumber
    });
}
exports.ClearspeakRules = ClearspeakRules;


/***/ }),

/***/ 8662:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.wordOrdinal = exports.layoutFactor_ = exports.fencedFactor_ = exports.simpleFactor_ = exports.simpleArguments = exports.fencedArguments = exports.insertNesting = exports.matchingFences = exports.nestingDepth = exports.NESTING_DEPTH = exports.ordinalExponent = exports.allTextLastContent_ = exports.isUnitExpression = exports.isSmallVulgarFraction = exports.allCellsSimple = exports.allIndices_ = exports.isInteger_ = exports.simpleCell_ = exports.simpleNode = exports.hasPreference = exports.isSimpleFraction_ = exports.isSimpleNumber_ = exports.isNumber_ = exports.isLetter_ = exports.isSimple_ = exports.isSimpleLetters_ = exports.isSimpleDegree_ = exports.isSimpleNegative_ = exports.isSimpleFunction_ = exports.isSimpleExpression = exports.nodeCounter = void 0;
const DomUtil = __webpack_require__(6671);
const engine_1 = __webpack_require__(4886);
const XpathUtil = __webpack_require__(5024);
const locale_1 = __webpack_require__(4524);
const transformers_1 = __webpack_require__(9385);
const grammar_1 = __webpack_require__(1058);
const StoreUtil = __webpack_require__(931);
const semantic_annotations_1 = __webpack_require__(4036);
const semantic_annotator_1 = __webpack_require__(241);
const semantic_attr_1 = __webpack_require__(4020);
function nodeCounter(nodes, context) {
    const split = context.split('-');
    const func = StoreUtil.nodeCounter(nodes, split[0] || '');
    const sep = split[1] || '';
    const init = split[2] || '';
    let first = true;
    return function () {
        const result = func();
        if (first) {
            first = false;
            return init + result + sep;
        }
        else {
            return result + sep;
        }
    };
}
exports.nodeCounter = nodeCounter;
function isSimpleExpression(node) {
    return (isSimpleNumber_(node) ||
        isSimpleLetters_(node) ||
        isSimpleDegree_(node) ||
        isSimpleNegative_(node) ||
        isSimpleFunction_(node));
}
exports.isSimpleExpression = isSimpleExpression;
function isSimpleFunction_(node) {
    return (node.type === "appl" &&
        (node.childNodes[0].role === "prefix function" ||
            node.childNodes[0].role === "simple function") &&
        (isSimple_(node.childNodes[1]) ||
            (node.childNodes[1].type === "fenced" &&
                isSimple_(node.childNodes[1].childNodes[0]))));
}
exports.isSimpleFunction_ = isSimpleFunction_;
function isSimpleNegative_(node) {
    return (node.type === "prefixop" &&
        node.role === "negative" &&
        isSimple_(node.childNodes[0]) &&
        node.childNodes[0].type !== "prefixop" &&
        node.childNodes[0].type !== "appl" &&
        node.childNodes[0].type !== "punctuated");
}
exports.isSimpleNegative_ = isSimpleNegative_;
function isSimpleDegree_(node) {
    return (node.type === "punctuated" &&
        node.role === "endpunct" &&
        node.childNodes.length === 2 &&
        node.childNodes[1].role === "degree" &&
        (isLetter_(node.childNodes[0]) ||
            isNumber_(node.childNodes[0]) ||
            (node.childNodes[0].type === "prefixop" &&
                node.childNodes[0].role === "negative" &&
                (isLetter_(node.childNodes[0].childNodes[0]) ||
                    isNumber_(node.childNodes[0].childNodes[0])))));
}
exports.isSimpleDegree_ = isSimpleDegree_;
function isSimpleLetters_(node) {
    return (isLetter_(node) ||
        (node.type === "infixop" &&
            node.role === "implicit" &&
            ((node.childNodes.length === 2 &&
                (isLetter_(node.childNodes[0]) ||
                    isSimpleNumber_(node.childNodes[0])) &&
                isLetter_(node.childNodes[1])) ||
                (node.childNodes.length === 3 &&
                    isSimpleNumber_(node.childNodes[0]) &&
                    isLetter_(node.childNodes[1]) &&
                    isLetter_(node.childNodes[2])))));
}
exports.isSimpleLetters_ = isSimpleLetters_;
function isSimple_(node) {
    return node.hasAnnotation('clearspeak', 'simple');
}
exports.isSimple_ = isSimple_;
function isLetter_(node) {
    return (node.type === "identifier" &&
        (node.role === "latinletter" ||
            node.role === "greekletter" ||
            node.role === "otherletter" ||
            node.role === "simple function"));
}
exports.isLetter_ = isLetter_;
function isNumber_(node) {
    return (node.type === "number" &&
        (node.role === "integer" || node.role === "float"));
}
exports.isNumber_ = isNumber_;
function isSimpleNumber_(node) {
    return isNumber_(node) || isSimpleFraction_(node);
}
exports.isSimpleNumber_ = isSimpleNumber_;
function isSimpleFraction_(node) {
    if (hasPreference('Fraction_Over') || hasPreference('Fraction_FracOver')) {
        return false;
    }
    if (node.type !== "fraction" ||
        node.role !== "vulgar") {
        return false;
    }
    if (hasPreference('Fraction_Ordinal')) {
        return true;
    }
    const enumerator = parseInt(node.childNodes[0].textContent, 10);
    const denominator = parseInt(node.childNodes[1].textContent, 10);
    return (enumerator > 0 && enumerator < 20 && denominator > 0 && denominator < 11);
}
exports.isSimpleFraction_ = isSimpleFraction_;
function hasPreference(pref) {
    return engine_1.default.getInstance().style === pref;
}
exports.hasPreference = hasPreference;
(0, semantic_annotations_1.register)(new semantic_annotator_1.SemanticAnnotator('clearspeak', 'simple', function (node) {
    return isSimpleExpression(node) ? 'simple' : '';
}));
function simpleNode(node) {
    if (!node.hasAttribute('annotation')) {
        return false;
    }
    const annotation = node.getAttribute('annotation');
    return !!/clearspeak:simple$|clearspeak:simple;/.exec(annotation);
}
exports.simpleNode = simpleNode;
function simpleCell_(node) {
    if (simpleNode(node)) {
        return true;
    }
    if (node.tagName !== "subscript") {
        return false;
    }
    const children = node.childNodes[0].childNodes;
    const index = children[1];
    return (children[0].tagName === "identifier" &&
        (isInteger_(index) ||
            (index.tagName === "infixop" &&
                index.hasAttribute('role') &&
                index.getAttribute('role') === "implicit" &&
                allIndices_(index))));
}
exports.simpleCell_ = simpleCell_;
function isInteger_(node) {
    return (node.tagName === "number" &&
        node.hasAttribute('role') &&
        node.getAttribute('role') === "integer");
}
exports.isInteger_ = isInteger_;
function allIndices_(node) {
    const nodes = XpathUtil.evalXPath('children/*', node);
    return nodes.every((x) => isInteger_(x) || x.tagName === "identifier");
}
exports.allIndices_ = allIndices_;
function allCellsSimple(node) {
    const xpath = node.tagName === "matrix"
        ? 'children/row/children/cell/children/*'
        : 'children/line/children/*';
    const nodes = XpathUtil.evalXPath(xpath, node);
    const result = nodes.every(simpleCell_);
    return result ? [node] : [];
}
exports.allCellsSimple = allCellsSimple;
function isSmallVulgarFraction(node) {
    return (0, transformers_1.vulgarFractionSmall)(node, 20, 11) ? [node] : [];
}
exports.isSmallVulgarFraction = isSmallVulgarFraction;
function isUnitExpression(node) {
    return (node.type === "text" ||
        (node.type === "punctuated" &&
            node.role === "text" &&
            isNumber_(node.childNodes[0]) &&
            allTextLastContent_(node.childNodes.slice(1))) ||
        (node.type === "identifier" &&
            node.role === "unit") ||
        (node.type === "infixop" &&
            (node.role === "implicit" || node.role === "unit")));
}
exports.isUnitExpression = isUnitExpression;
function allTextLastContent_(nodes) {
    for (let i = 0; i < nodes.length - 1; i++) {
        if (!(nodes[i].type === "text" && nodes[i].textContent === '')) {
            return false;
        }
    }
    return nodes[nodes.length - 1].type === "text";
}
exports.allTextLastContent_ = allTextLastContent_;
(0, semantic_annotations_1.register)(new semantic_annotator_1.SemanticAnnotator('clearspeak', 'unit', function (node) {
    return isUnitExpression(node) ? 'unit' : '';
}));
function ordinalExponent(node) {
    const num = parseInt(node.textContent, 10);
    if (isNaN(num)) {
        return node.textContent;
    }
    return num > 10
        ? locale_1.LOCALE.NUMBERS.numericOrdinal(num)
        : locale_1.LOCALE.NUMBERS.wordOrdinal(num);
}
exports.ordinalExponent = ordinalExponent;
exports.NESTING_DEPTH = null;
function nestingDepth(node) {
    let count = 0;
    const fence = node.textContent;
    const index = node.getAttribute('role') === 'open' ? 0 : 1;
    let parent = node.parentNode;
    while (parent) {
        if (parent.tagName === "fenced" &&
            parent.childNodes[0].childNodes[index].textContent === fence) {
            count++;
        }
        parent = parent.parentNode;
    }
    exports.NESTING_DEPTH = count > 1 ? locale_1.LOCALE.NUMBERS.wordOrdinal(count) : '';
    return exports.NESTING_DEPTH;
}
exports.nestingDepth = nestingDepth;
function matchingFences(node) {
    const sibling = node.previousSibling;
    let left, right;
    if (sibling) {
        left = sibling;
        right = node;
    }
    else {
        left = node;
        right = node.nextSibling;
    }
    if (!right) {
        return [];
    }
    return (0, semantic_attr_1.isMatchingFence)(left.textContent, right.textContent) ? [node] : [];
}
exports.matchingFences = matchingFences;
function insertNesting(text, correction) {
    if (!correction || !text) {
        return text;
    }
    const start = text.match(/^(open|close) /);
    if (!start) {
        return correction + ' ' + text;
    }
    return start[0] + correction + ' ' + text.substring(start[0].length);
}
exports.insertNesting = insertNesting;
grammar_1.Grammar.getInstance().setCorrection('insertNesting', insertNesting);
function fencedArguments(node) {
    const content = DomUtil.toArray(node.parentNode.childNodes);
    const children = XpathUtil.evalXPath('../../children/*', node);
    const index = content.indexOf(node);
    return fencedFactor_(children[index]) || fencedFactor_(children[index + 1])
        ? [node]
        : [];
}
exports.fencedArguments = fencedArguments;
function simpleArguments(node) {
    const content = DomUtil.toArray(node.parentNode.childNodes);
    const children = XpathUtil.evalXPath('../../children/*', node);
    const index = content.indexOf(node);
    return simpleFactor_(children[index]) &&
        children[index + 1] &&
        (simpleFactor_(children[index + 1]) ||
            children[index + 1].tagName === "root" ||
            children[index + 1].tagName === "sqrt" ||
            (children[index + 1].tagName === "superscript" &&
                children[index + 1].childNodes[0].childNodes[0] &&
                (children[index + 1].childNodes[0].childNodes[0]
                    .tagName === "number" ||
                    children[index + 1].childNodes[0].childNodes[0]
                        .tagName === "identifier") &&
                (children[index + 1].childNodes[0].childNodes[1].textContent === '2' ||
                    children[index + 1].childNodes[0].childNodes[1].textContent === '3')))
        ? [node]
        : [];
}
exports.simpleArguments = simpleArguments;
function simpleFactor_(node) {
    return (!!node &&
        (node.tagName === "number" ||
            node.tagName === "identifier" ||
            node.tagName === "function" ||
            node.tagName === "appl" ||
            node.tagName === "fraction"));
}
exports.simpleFactor_ = simpleFactor_;
function fencedFactor_(node) {
    return (node &&
        (node.tagName === "fenced" ||
            (node.hasAttribute('role') &&
                node.getAttribute('role') === "leftright") ||
            layoutFactor_(node)));
}
exports.fencedFactor_ = fencedFactor_;
function layoutFactor_(node) {
    return (!!node &&
        (node.tagName === "matrix" ||
            node.tagName === "vector"));
}
exports.layoutFactor_ = layoutFactor_;
function wordOrdinal(node) {
    return locale_1.LOCALE.NUMBERS.wordOrdinal(parseInt(node.textContent, 10));
}
exports.wordOrdinal = wordOrdinal;


/***/ }),

/***/ 5659:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.loadAjax = exports.loadFileSync = exports.loadFile = exports.parseMaps = exports.retrieveFiles = exports.standardLoader = exports.loadLocale = exports.store = void 0;
const BrowserUtil = __webpack_require__(9501);
const engine_1 = __webpack_require__(4886);
const EngineConst = __webpack_require__(4998);
const FileUtil = __webpack_require__(7129);
const system_external_1 = __webpack_require__(4755);
const dynamic_cstr_1 = __webpack_require__(8310);
const MathCompoundStore = __webpack_require__(4161);
const speech_rule_engine_1 = __webpack_require__(6060);
const l10n_1 = __webpack_require__(2371);
const AlphabetGenerator = __webpack_require__(650);
exports.store = MathCompoundStore;
const addSymbols = {
    functions: MathCompoundStore.addFunctionRules,
    symbols: MathCompoundStore.addSymbolRules,
    units: MathCompoundStore.addUnitRules,
    si: MathCompoundStore.setSiPrefixes
};
let _init = false;
function loadLocale(locale = engine_1.default.getInstance().locale) {
    return __awaiter(this, void 0, void 0, function* () {
        if (!_init) {
            _loadLocale(dynamic_cstr_1.DynamicCstr.BASE_LOCALE);
            _init = true;
        }
        return engine_1.EnginePromise.promises[dynamic_cstr_1.DynamicCstr.BASE_LOCALE].then(() => __awaiter(this, void 0, void 0, function* () {
            const defLoc = engine_1.default.getInstance().defaultLocale;
            if (defLoc) {
                _loadLocale(defLoc);
                return engine_1.EnginePromise.promises[defLoc].then(() => __awaiter(this, void 0, void 0, function* () {
                    _loadLocale(locale);
                    return engine_1.EnginePromise.promises[locale];
                }));
            }
            _loadLocale(locale);
            return engine_1.EnginePromise.promises[locale];
        }));
    });
}
exports.loadLocale = loadLocale;
function _loadLocale(locale = engine_1.default.getInstance().locale) {
    if (!engine_1.EnginePromise.loaded[locale]) {
        engine_1.EnginePromise.loaded[locale] = [false, false];
        retrieveMaps(locale);
    }
}
function loadMethod() {
    if (engine_1.default.getInstance().customLoader) {
        return engine_1.default.getInstance().customLoader;
    }
    return standardLoader();
}
function standardLoader() {
    switch (engine_1.default.getInstance().mode) {
        case EngineConst.Mode.ASYNC:
            return loadFile;
        case EngineConst.Mode.HTTP:
            return loadAjax;
        case EngineConst.Mode.SYNC:
        default:
            return loadFileSync;
    }
}
exports.standardLoader = standardLoader;
function retrieveFiles(locale) {
    const loader = loadMethod();
    const promise = new Promise((res) => {
        const inner = loader(locale);
        inner.then((str) => {
            parseMaps(str);
            engine_1.EnginePromise.loaded[locale] = [true, true];
            res(locale);
        }, (_err) => {
            engine_1.EnginePromise.loaded[locale] = [true, false];
            console.error(`Unable to load locale: ${locale}`);
            engine_1.default.getInstance().locale = engine_1.default.getInstance().defaultLocale;
            res(locale);
        });
    });
    engine_1.EnginePromise.promises[locale] = promise;
}
exports.retrieveFiles = retrieveFiles;
function parseMaps(json) {
    const js = JSON.parse(json);
    addMaps(js);
}
exports.parseMaps = parseMaps;
function addMaps(json, opt_locale) {
    let generate = true;
    for (let i = 0, key; (key = Object.keys(json)[i]); i++) {
        const info = key.split('/');
        if (opt_locale && opt_locale !== info[0]) {
            continue;
        }
        if (info[1] === 'rules') {
            speech_rule_engine_1.SpeechRuleEngine.getInstance().addStore(json[key]);
        }
        else if (info[1] === 'messages') {
            (0, l10n_1.completeLocale)(json[key]);
        }
        else {
            if (generate) {
                AlphabetGenerator.generate(info[0]);
                generate = false;
            }
            json[key].forEach(addSymbols[info[1]]);
        }
    }
}
function retrieveMaps(locale) {
    if (engine_1.default.getInstance().isIE &&
        engine_1.default.getInstance().mode === EngineConst.Mode.HTTP) {
        getJsonIE_(locale);
        return;
    }
    retrieveFiles(locale);
}
function getJsonIE_(locale, opt_count) {
    let count = opt_count || 1;
    if (!BrowserUtil.mapsForIE) {
        if (count <= 5) {
            setTimeout((() => getJsonIE_(locale, count++)).bind(this), 300);
        }
        return;
    }
    addMaps(BrowserUtil.mapsForIE, locale);
}
function loadFile(locale) {
    const file = FileUtil.localePath(locale);
    return new Promise((res, rej) => {
        system_external_1.default.fs.readFile(file, 'utf8', (err, json) => {
            if (err) {
                return rej(err);
            }
            res(json);
        });
    });
}
exports.loadFile = loadFile;
function loadFileSync(locale) {
    const file = FileUtil.localePath(locale);
    return new Promise((res, rej) => {
        let str = '{}';
        try {
            str = system_external_1.default.fs.readFileSync(file, 'utf8');
        }
        catch (err) {
            return rej(err);
        }
        res(str);
    });
}
exports.loadFileSync = loadFileSync;
function loadAjax(locale) {
    const file = FileUtil.localePath(locale);
    const httpRequest = new XMLHttpRequest();
    return new Promise((res, rej) => {
        httpRequest.onreadystatechange = function () {
            if (httpRequest.readyState === 4) {
                const status = httpRequest.status;
                if (status === 0 || (status >= 200 && status < 400)) {
                    res(httpRequest.responseText);
                }
                else {
                    rej(status);
                }
            }
        };
        httpRequest.open('GET', file, true);
        httpRequest.send();
    });
}
exports.loadAjax = loadAjax;


/***/ }),

/***/ 3784:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.leftSubscriptBrief = exports.leftSuperscriptBrief = exports.leftSubscriptVerbose = exports.leftSuperscriptVerbose = exports.baselineBrief = exports.baselineVerbose = void 0;
const MathspeakUtil = __webpack_require__(3269);
function baselineVerbose(node) {
    const baseline = MathspeakUtil.baselineVerbose(node);
    return baseline.replace(/-$/, '');
}
exports.baselineVerbose = baselineVerbose;
function baselineBrief(node) {
    const baseline = MathspeakUtil.baselineBrief(node);
    return baseline.replace(/-$/, '');
}
exports.baselineBrief = baselineBrief;
function leftSuperscriptVerbose(node) {
    const leftIndex = MathspeakUtil.superscriptVerbose(node);
    return leftIndex.replace(/^exposant/, 'exposant gauche');
}
exports.leftSuperscriptVerbose = leftSuperscriptVerbose;
function leftSubscriptVerbose(node) {
    const leftIndex = MathspeakUtil.subscriptVerbose(node);
    return leftIndex.replace(/^indice/, 'indice gauche');
}
exports.leftSubscriptVerbose = leftSubscriptVerbose;
function leftSuperscriptBrief(node) {
    const leftIndex = MathspeakUtil.superscriptBrief(node);
    return leftIndex.replace(/^sup/, 'sup gauche');
}
exports.leftSuperscriptBrief = leftSuperscriptBrief;
function leftSubscriptBrief(node) {
    const leftIndex = MathspeakUtil.subscriptBrief(node);
    return leftIndex.replace(/^sub/, 'sub gauche');
}
exports.leftSubscriptBrief = leftSubscriptBrief;


/***/ }),

/***/ 4972:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MathspeakRules = void 0;
const dynamic_cstr_1 = __webpack_require__(8310);
const StoreUtil = __webpack_require__(931);
const MathspeakFrenchUtil = __webpack_require__(3784);
const MathspeakUtil = __webpack_require__(3269);
const NumbersUtil = __webpack_require__(2110);
const SpeechRules = __webpack_require__(7278);
const UnitUtil = __webpack_require__(9771);
function MathspeakRules() {
    SpeechRules.addStore(dynamic_cstr_1.DynamicCstr.BASE_LOCALE + '.speech.mathspeak', '', {
        CQFspaceoutNumber: MathspeakUtil.spaceoutNumber,
        CQFspaceoutIdentifier: MathspeakUtil.spaceoutIdentifier,
        CSFspaceoutText: MathspeakUtil.spaceoutText,
        CSFopenFracVerbose: MathspeakUtil.openingFractionVerbose,
        CSFcloseFracVerbose: MathspeakUtil.closingFractionVerbose,
        CSFoverFracVerbose: MathspeakUtil.overFractionVerbose,
        CSFopenFracBrief: MathspeakUtil.openingFractionBrief,
        CSFcloseFracBrief: MathspeakUtil.closingFractionBrief,
        CSFopenFracSbrief: MathspeakUtil.openingFractionSbrief,
        CSFcloseFracSbrief: MathspeakUtil.closingFractionSbrief,
        CSFoverFracSbrief: MathspeakUtil.overFractionSbrief,
        CSFvulgarFraction: NumbersUtil.vulgarFraction,
        CQFvulgarFractionSmall: MathspeakUtil.isSmallVulgarFraction,
        CSFopenRadicalVerbose: MathspeakUtil.openingRadicalVerbose,
        CSFcloseRadicalVerbose: MathspeakUtil.closingRadicalVerbose,
        CSFindexRadicalVerbose: MathspeakUtil.indexRadicalVerbose,
        CSFopenRadicalBrief: MathspeakUtil.openingRadicalBrief,
        CSFcloseRadicalBrief: MathspeakUtil.closingRadicalBrief,
        CSFindexRadicalBrief: MathspeakUtil.indexRadicalBrief,
        CSFopenRadicalSbrief: MathspeakUtil.openingRadicalSbrief,
        CSFindexRadicalSbrief: MathspeakUtil.indexRadicalSbrief,
        CQFisSmallRoot: MathspeakUtil.smallRoot,
        CSFsuperscriptVerbose: MathspeakUtil.superscriptVerbose,
        CSFsuperscriptBrief: MathspeakUtil.superscriptBrief,
        CSFsubscriptVerbose: MathspeakUtil.subscriptVerbose,
        CSFsubscriptBrief: MathspeakUtil.subscriptBrief,
        CSFbaselineVerbose: MathspeakUtil.baselineVerbose,
        CSFbaselineBrief: MathspeakUtil.baselineBrief,
        CSFleftsuperscriptVerbose: MathspeakUtil.superscriptVerbose,
        CSFleftsubscriptVerbose: MathspeakUtil.subscriptVerbose,
        CSFrightsuperscriptVerbose: MathspeakUtil.superscriptVerbose,
        CSFrightsubscriptVerbose: MathspeakUtil.subscriptVerbose,
        CSFleftsuperscriptBrief: MathspeakUtil.superscriptBrief,
        CSFleftsubscriptBrief: MathspeakUtil.subscriptBrief,
        CSFrightsuperscriptBrief: MathspeakUtil.superscriptBrief,
        CSFrightsubscriptBrief: MathspeakUtil.subscriptBrief,
        CSFunderscript: MathspeakUtil.nestedUnderscript,
        CSFoverscript: MathspeakUtil.nestedOverscript,
        CSFendscripts: MathspeakUtil.endscripts,
        CTFordinalCounter: NumbersUtil.ordinalCounter,
        CTFwordCounter: NumbersUtil.wordCounter,
        CTFcontentIterator: StoreUtil.contentIterator,
        CQFdetIsSimple: MathspeakUtil.determinantIsSimple,
        CSFRemoveParens: MathspeakUtil.removeParens,
        CQFresetNesting: MathspeakUtil.resetNestingDepth,
        CGFbaselineConstraint: MathspeakUtil.generateBaselineConstraint,
        CGFtensorRules: MathspeakUtil.generateTensorRules
    });
    SpeechRules.addStore('es.speech.mathspeak', dynamic_cstr_1.DynamicCstr.BASE_LOCALE + '.speech.mathspeak', {
        CTFunitMultipliers: UnitUtil.unitMultipliers,
        CQFoneLeft: UnitUtil.oneLeft
    });
    SpeechRules.addStore('fr.speech.mathspeak', dynamic_cstr_1.DynamicCstr.BASE_LOCALE + '.speech.mathspeak', {
        CSFbaselineVerbose: MathspeakFrenchUtil.baselineVerbose,
        CSFbaselineBrief: MathspeakFrenchUtil.baselineBrief,
        CSFleftsuperscriptVerbose: MathspeakFrenchUtil.leftSuperscriptVerbose,
        CSFleftsubscriptVerbose: MathspeakFrenchUtil.leftSubscriptVerbose,
        CSFleftsuperscriptBrief: MathspeakFrenchUtil.leftSuperscriptBrief,
        CSFleftsubscriptBrief: MathspeakFrenchUtil.leftSubscriptBrief
    });
}
exports.MathspeakRules = MathspeakRules;


/***/ }),

/***/ 3269:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.smallRoot = exports.generateTensorRules = exports.removeParens = exports.generateBaselineConstraint = exports.determinantIsSimple = exports.nestedOverscript = exports.endscripts = exports.overscoreNestingDepth = exports.nestedUnderscript = exports.underscoreNestingDepth = exports.indexRadicalSbrief = exports.openingRadicalSbrief = exports.indexRadicalBrief = exports.closingRadicalBrief = exports.openingRadicalBrief = exports.indexRadicalVerbose = exports.closingRadicalVerbose = exports.openingRadicalVerbose = exports.getRootIndex = exports.nestedRadical = exports.radicalNestingDepth = exports.baselineBrief = exports.baselineVerbose = exports.superscriptBrief = exports.superscriptVerbose = exports.subscriptBrief = exports.subscriptVerbose = exports.nestedSubSuper = exports.isSmallVulgarFraction = exports.overFractionSbrief = exports.closingFractionSbrief = exports.openingFractionSbrief = exports.closingFractionBrief = exports.openingFractionBrief = exports.overFractionVerbose = exports.closingFractionVerbose = exports.openingFractionVerbose = exports.nestedFraction = exports.fractionNestingDepth = exports.computeNestingDepth_ = exports.containsAttr = exports.getNestingDepth = exports.resetNestingDepth = exports.nestingBarriers = exports.spaceoutIdentifier = exports.spaceoutNumber = exports.spaceoutNodes = exports.spaceoutText = void 0;
const BaseUtil = __webpack_require__(1426);
const DomUtil = __webpack_require__(6671);
const XpathUtil = __webpack_require__(5024);
const locale_1 = __webpack_require__(4524);
const semantic_processor_1 = __webpack_require__(7793);
let nestingDepth = {};
function spaceoutText(node) {
    return Array.from(node.textContent).join(' ');
}
exports.spaceoutText = spaceoutText;
function spaceoutNodes(node, correction) {
    const content = Array.from(node.textContent);
    const result = [];
    const processor = semantic_processor_1.default.getInstance();
    const doc = node.ownerDocument;
    for (let i = 0, chr; (chr = content[i]); i++) {
        const leaf = processor
            .getNodeFactory()
            .makeLeafNode(chr, "unknown");
        const sn = processor.identifierNode(leaf, "unknown", '');
        correction(sn);
        result.push(sn.xml(doc));
    }
    return result;
}
exports.spaceoutNodes = spaceoutNodes;
function spaceoutNumber(node) {
    return spaceoutNodes(node, function (sn) {
        if (!sn.textContent.match(/\W/)) {
            sn.type = "number";
        }
    });
}
exports.spaceoutNumber = spaceoutNumber;
function spaceoutIdentifier(node) {
    return spaceoutNodes(node, function (sn) {
        sn.font = "unknown";
        sn.type = "identifier";
    });
}
exports.spaceoutIdentifier = spaceoutIdentifier;
exports.nestingBarriers = [
    "cases",
    "cell",
    "integral",
    "line",
    "matrix",
    "multiline",
    "overscore",
    "root",
    "row",
    "sqrt",
    "subscript",
    "superscript",
    "table",
    "underscore",
    "vector"
];
function resetNestingDepth(node) {
    nestingDepth = {};
    return [node];
}
exports.resetNestingDepth = resetNestingDepth;
function getNestingDepth(type, node, tags, opt_barrierTags, opt_barrierAttrs, opt_func) {
    opt_barrierTags = opt_barrierTags || exports.nestingBarriers;
    opt_barrierAttrs = opt_barrierAttrs || {};
    opt_func =
        opt_func ||
            function (_node) {
                return false;
            };
    const xmlText = DomUtil.serializeXml(node);
    if (!nestingDepth[type]) {
        nestingDepth[type] = {};
    }
    if (nestingDepth[type][xmlText]) {
        return nestingDepth[type][xmlText];
    }
    if (opt_func(node) || tags.indexOf(node.tagName) < 0) {
        return 0;
    }
    const depth = computeNestingDepth_(node, tags, BaseUtil.setdifference(opt_barrierTags, tags), opt_barrierAttrs, opt_func, 0);
    nestingDepth[type][xmlText] = depth;
    return depth;
}
exports.getNestingDepth = getNestingDepth;
function containsAttr(node, attrs) {
    if (!node.attributes) {
        return false;
    }
    const attributes = DomUtil.toArray(node.attributes);
    for (let i = 0, attr; (attr = attributes[i]); i++) {
        if (attrs[attr.nodeName] === attr.nodeValue) {
            return true;
        }
    }
    return false;
}
exports.containsAttr = containsAttr;
function computeNestingDepth_(node, tags, barriers, attrs, func, depth) {
    if (func(node) ||
        barriers.indexOf(node.tagName) > -1 ||
        containsAttr(node, attrs)) {
        return depth;
    }
    if (tags.indexOf(node.tagName) > -1) {
        depth++;
    }
    if (!node.childNodes || node.childNodes.length === 0) {
        return depth;
    }
    const children = DomUtil.toArray(node.childNodes);
    return Math.max.apply(null, children.map(function (subNode) {
        return computeNestingDepth_(subNode, tags, barriers, attrs, func, depth);
    }));
}
exports.computeNestingDepth_ = computeNestingDepth_;
function fractionNestingDepth(node) {
    return getNestingDepth('fraction', node, ['fraction'], exports.nestingBarriers, {}, locale_1.LOCALE.FUNCTIONS.fracNestDepth);
}
exports.fractionNestingDepth = fractionNestingDepth;
function nestedFraction(node, expr, opt_end) {
    const depth = fractionNestingDepth(node);
    const annotation = Array(depth).fill(expr);
    if (opt_end) {
        annotation.push(opt_end);
    }
    return annotation.join(locale_1.LOCALE.MESSAGES.regexp.JOINER_FRAC);
}
exports.nestedFraction = nestedFraction;
function openingFractionVerbose(node) {
    return nestedFraction(node, locale_1.LOCALE.MESSAGES.MS.START, locale_1.LOCALE.MESSAGES.MS.FRAC_V);
}
exports.openingFractionVerbose = openingFractionVerbose;
function closingFractionVerbose(node) {
    return nestedFraction(node, locale_1.LOCALE.MESSAGES.MS.END, locale_1.LOCALE.MESSAGES.MS.FRAC_V);
}
exports.closingFractionVerbose = closingFractionVerbose;
function overFractionVerbose(node) {
    return nestedFraction(node, locale_1.LOCALE.MESSAGES.MS.FRAC_OVER);
}
exports.overFractionVerbose = overFractionVerbose;
function openingFractionBrief(node) {
    return nestedFraction(node, locale_1.LOCALE.MESSAGES.MS.START, locale_1.LOCALE.MESSAGES.MS.FRAC_B);
}
exports.openingFractionBrief = openingFractionBrief;
function closingFractionBrief(node) {
    return nestedFraction(node, locale_1.LOCALE.MESSAGES.MS.END, locale_1.LOCALE.MESSAGES.MS.FRAC_B);
}
exports.closingFractionBrief = closingFractionBrief;
function openingFractionSbrief(node) {
    const depth = fractionNestingDepth(node);
    if (depth === 1) {
        return locale_1.LOCALE.MESSAGES.MS.FRAC_S;
    }
    return locale_1.LOCALE.FUNCTIONS.combineNestedFraction(locale_1.LOCALE.MESSAGES.MS.NEST_FRAC, locale_1.LOCALE.FUNCTIONS.radicalNestDepth(depth - 1), locale_1.LOCALE.MESSAGES.MS.FRAC_S);
}
exports.openingFractionSbrief = openingFractionSbrief;
function closingFractionSbrief(node) {
    const depth = fractionNestingDepth(node);
    if (depth === 1) {
        return locale_1.LOCALE.MESSAGES.MS.ENDFRAC;
    }
    return locale_1.LOCALE.FUNCTIONS.combineNestedFraction(locale_1.LOCALE.MESSAGES.MS.NEST_FRAC, locale_1.LOCALE.FUNCTIONS.radicalNestDepth(depth - 1), locale_1.LOCALE.MESSAGES.MS.ENDFRAC);
}
exports.closingFractionSbrief = closingFractionSbrief;
function overFractionSbrief(node) {
    const depth = fractionNestingDepth(node);
    if (depth === 1) {
        return locale_1.LOCALE.MESSAGES.MS.FRAC_OVER;
    }
    return locale_1.LOCALE.FUNCTIONS.combineNestedFraction(locale_1.LOCALE.MESSAGES.MS.NEST_FRAC, locale_1.LOCALE.FUNCTIONS.radicalNestDepth(depth - 1), locale_1.LOCALE.MESSAGES.MS.FRAC_OVER);
}
exports.overFractionSbrief = overFractionSbrief;
function isSmallVulgarFraction(node) {
    return locale_1.LOCALE.FUNCTIONS.fracNestDepth(node) ? [node] : [];
}
exports.isSmallVulgarFraction = isSmallVulgarFraction;
function nestedSubSuper(node, init, replace) {
    while (node.parentNode) {
        const children = node.parentNode;
        const parent = children.parentNode;
        if (!parent) {
            break;
        }
        const nodeRole = node.getAttribute && node.getAttribute('role');
        if ((parent.tagName === "subscript" &&
            node === children.childNodes[1]) ||
            (parent.tagName === "tensor" &&
                nodeRole &&
                (nodeRole === "leftsub" ||
                    nodeRole === "rightsub"))) {
            init = replace.sub + locale_1.LOCALE.MESSAGES.regexp.JOINER_SUBSUPER + init;
        }
        if ((parent.tagName === "superscript" &&
            node === children.childNodes[1]) ||
            (parent.tagName === "tensor" &&
                nodeRole &&
                (nodeRole === "leftsuper" ||
                    nodeRole === "rightsuper"))) {
            init = replace.sup + locale_1.LOCALE.MESSAGES.regexp.JOINER_SUBSUPER + init;
        }
        node = parent;
    }
    return init.trim();
}
exports.nestedSubSuper = nestedSubSuper;
function subscriptVerbose(node) {
    return nestedSubSuper(node, locale_1.LOCALE.MESSAGES.MS.SUBSCRIPT, {
        sup: locale_1.LOCALE.MESSAGES.MS.SUPER,
        sub: locale_1.LOCALE.MESSAGES.MS.SUB
    });
}
exports.subscriptVerbose = subscriptVerbose;
function subscriptBrief(node) {
    return nestedSubSuper(node, locale_1.LOCALE.MESSAGES.MS.SUB, {
        sup: locale_1.LOCALE.MESSAGES.MS.SUP,
        sub: locale_1.LOCALE.MESSAGES.MS.SUB
    });
}
exports.subscriptBrief = subscriptBrief;
function superscriptVerbose(node) {
    return nestedSubSuper(node, locale_1.LOCALE.MESSAGES.MS.SUPERSCRIPT, {
        sup: locale_1.LOCALE.MESSAGES.MS.SUPER,
        sub: locale_1.LOCALE.MESSAGES.MS.SUB
    });
}
exports.superscriptVerbose = superscriptVerbose;
function superscriptBrief(node) {
    return nestedSubSuper(node, locale_1.LOCALE.MESSAGES.MS.SUP, {
        sup: locale_1.LOCALE.MESSAGES.MS.SUP,
        sub: locale_1.LOCALE.MESSAGES.MS.SUB
    });
}
exports.superscriptBrief = superscriptBrief;
function baselineVerbose(node) {
    const baseline = nestedSubSuper(node, '', {
        sup: locale_1.LOCALE.MESSAGES.MS.SUPER,
        sub: locale_1.LOCALE.MESSAGES.MS.SUB
    });
    if (!baseline) {
        return locale_1.LOCALE.MESSAGES.MS.BASELINE;
    }
    return baseline
        .replace(new RegExp(locale_1.LOCALE.MESSAGES.MS.SUB + '$'), locale_1.LOCALE.MESSAGES.MS.SUBSCRIPT)
        .replace(new RegExp(locale_1.LOCALE.MESSAGES.MS.SUPER + '$'), locale_1.LOCALE.MESSAGES.MS.SUPERSCRIPT);
}
exports.baselineVerbose = baselineVerbose;
function baselineBrief(node) {
    const baseline = nestedSubSuper(node, '', {
        sup: locale_1.LOCALE.MESSAGES.MS.SUP,
        sub: locale_1.LOCALE.MESSAGES.MS.SUB
    });
    return baseline || locale_1.LOCALE.MESSAGES.MS.BASE;
}
exports.baselineBrief = baselineBrief;
function radicalNestingDepth(node) {
    return getNestingDepth('radical', node, ['sqrt', 'root'], exports.nestingBarriers, {});
}
exports.radicalNestingDepth = radicalNestingDepth;
function nestedRadical(node, prefix, postfix) {
    const depth = radicalNestingDepth(node);
    const index = getRootIndex(node);
    postfix = index ? locale_1.LOCALE.FUNCTIONS.combineRootIndex(postfix, index) : postfix;
    if (depth === 1) {
        return postfix;
    }
    return locale_1.LOCALE.FUNCTIONS.combineNestedRadical(prefix, locale_1.LOCALE.FUNCTIONS.radicalNestDepth(depth - 1), postfix);
}
exports.nestedRadical = nestedRadical;
function getRootIndex(node) {
    const content = node.tagName === 'sqrt'
        ? '2'
        :
            XpathUtil.evalXPath('children/*[1]', node)[0].textContent.trim();
    return locale_1.LOCALE.MESSAGES.MSroots[content] || '';
}
exports.getRootIndex = getRootIndex;
function openingRadicalVerbose(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.NESTED, locale_1.LOCALE.MESSAGES.MS.STARTROOT);
}
exports.openingRadicalVerbose = openingRadicalVerbose;
function closingRadicalVerbose(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.NESTED, locale_1.LOCALE.MESSAGES.MS.ENDROOT);
}
exports.closingRadicalVerbose = closingRadicalVerbose;
function indexRadicalVerbose(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.NESTED, locale_1.LOCALE.MESSAGES.MS.ROOTINDEX);
}
exports.indexRadicalVerbose = indexRadicalVerbose;
function openingRadicalBrief(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.NEST_ROOT, locale_1.LOCALE.MESSAGES.MS.STARTROOT);
}
exports.openingRadicalBrief = openingRadicalBrief;
function closingRadicalBrief(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.NEST_ROOT, locale_1.LOCALE.MESSAGES.MS.ENDROOT);
}
exports.closingRadicalBrief = closingRadicalBrief;
function indexRadicalBrief(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.NEST_ROOT, locale_1.LOCALE.MESSAGES.MS.ROOTINDEX);
}
exports.indexRadicalBrief = indexRadicalBrief;
function openingRadicalSbrief(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.NEST_ROOT, locale_1.LOCALE.MESSAGES.MS.ROOT);
}
exports.openingRadicalSbrief = openingRadicalSbrief;
function indexRadicalSbrief(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.NEST_ROOT, locale_1.LOCALE.MESSAGES.MS.INDEX);
}
exports.indexRadicalSbrief = indexRadicalSbrief;
function underscoreNestingDepth(node) {
    return getNestingDepth('underscore', node, ['underscore'], exports.nestingBarriers, {}, function (node) {
        return (node.tagName &&
            node.tagName === "underscore" &&
            node.childNodes[0].childNodes[1].getAttribute('role') ===
                "underaccent");
    });
}
exports.underscoreNestingDepth = underscoreNestingDepth;
function nestedUnderscript(node) {
    const depth = underscoreNestingDepth(node);
    return (Array(depth).join(locale_1.LOCALE.MESSAGES.MS.UNDER) + locale_1.LOCALE.MESSAGES.MS.UNDERSCRIPT);
}
exports.nestedUnderscript = nestedUnderscript;
function overscoreNestingDepth(node) {
    return getNestingDepth('overscore', node, ['overscore'], exports.nestingBarriers, {}, function (node) {
        return (node.tagName &&
            node.tagName === "overscore" &&
            node.childNodes[0].childNodes[1].getAttribute('role') ===
                "overaccent");
    });
}
exports.overscoreNestingDepth = overscoreNestingDepth;
function endscripts(_node) {
    return locale_1.LOCALE.MESSAGES.MS.ENDSCRIPTS;
}
exports.endscripts = endscripts;
function nestedOverscript(node) {
    const depth = overscoreNestingDepth(node);
    return (Array(depth).join(locale_1.LOCALE.MESSAGES.MS.OVER) + locale_1.LOCALE.MESSAGES.MS.OVERSCRIPT);
}
exports.nestedOverscript = nestedOverscript;
function determinantIsSimple(node) {
    if (node.tagName !== "matrix" ||
        node.getAttribute('role') !== "determinant") {
        return [];
    }
    const cells = XpathUtil.evalXPath('children/row/children/cell/children/*', node);
    for (let i = 0, cell; (cell = cells[i]); i++) {
        if (cell.tagName === "number") {
            continue;
        }
        if (cell.tagName === "identifier") {
            const role = cell.getAttribute('role');
            if (role === "latinletter" ||
                role === "greekletter" ||
                role === "otherletter") {
                continue;
            }
        }
        return [];
    }
    return [node];
}
exports.determinantIsSimple = determinantIsSimple;
function generateBaselineConstraint() {
    const ignoreElems = ['subscript', 'superscript', 'tensor'];
    const mainElems = ['relseq', 'multrel'];
    const breakElems = ['fraction', 'punctuation', 'fenced', 'sqrt', 'root'];
    const ancestrify = (elemList) => elemList.map((elem) => 'ancestor::' + elem);
    const notify = (elem) => 'not(' + elem + ')';
    const prefix = 'ancestor::*/following-sibling::*';
    const middle = notify(ancestrify(ignoreElems).join(' or '));
    const mainList = ancestrify(mainElems);
    const breakList = ancestrify(breakElems);
    let breakCstrs = [];
    for (let i = 0, brk; (brk = breakList[i]); i++) {
        breakCstrs = breakCstrs.concat(mainList.map(function (elem) {
            return brk + '/' + elem;
        }));
    }
    const postfix = notify(breakCstrs.join(' | '));
    return [[prefix, middle, postfix].join(' and ')];
}
exports.generateBaselineConstraint = generateBaselineConstraint;
function removeParens(node) {
    if (!node.childNodes.length ||
        !node.childNodes[0].childNodes.length ||
        !node.childNodes[0].childNodes[0].childNodes.length) {
        return '';
    }
    const content = node.childNodes[0].childNodes[0].childNodes[0].textContent;
    return content.match(/^\(.+\)$/) ? content.slice(1, -1) : content;
}
exports.removeParens = removeParens;
const componentString = new Map([
    [3, 'CSFleftsuperscript'],
    [4, 'CSFleftsubscript'],
    [2, 'CSFbaseline'],
    [1, 'CSFrightsubscript'],
    [0, 'CSFrightsuperscript']
]);
const childNumber = new Map([
    [4, 2],
    [3, 3],
    [2, 1],
    [1, 4],
    [0, 5]
]);
function generateTensorRuleStrings_(constellation) {
    const constraints = [];
    let verbString = '';
    let briefString = '';
    let constel = parseInt(constellation, 2);
    for (let i = 0; i < 5; i++) {
        const childString = 'children/*[' + childNumber.get(i) + ']';
        if (constel & 1) {
            const compString = componentString.get(i % 5);
            verbString =
                '[t] ' + compString + 'Verbose; [n] ' + childString + ';' + verbString;
            briefString =
                '[t] ' + compString + 'Brief; [n] ' + childString + ';' + briefString;
        }
        else {
            constraints.unshift('name(' + childString + ')="empty"');
        }
        constel >>= 1;
    }
    return [constraints, verbString, briefString];
}
function generateTensorRules(store, brief = true) {
    const constellations = [
        '11111',
        '11110',
        '11101',
        '11100',
        '10111',
        '10110',
        '10101',
        '10100',
        '01111',
        '01110',
        '01101',
        '01100'
    ];
    for (let i = 0, constel; (constel = constellations[i]); i++) {
        let name = 'tensor' + constel;
        let [components, verbStr, briefStr] = generateTensorRuleStrings_(constel);
        store.defineRule(name, 'default', verbStr, 'self::tensor', ...components);
        if (brief) {
            store.defineRule(name, 'brief', briefStr, 'self::tensor', ...components);
            store.defineRule(name, 'sbrief', briefStr, 'self::tensor', ...components);
        }
        const baselineStr = componentString.get(2);
        verbStr += '; [t]' + baselineStr + 'Verbose';
        briefStr += '; [t]' + baselineStr + 'Brief';
        name = name + '-baseline';
        const cstr = '((.//*[not(*)])[last()]/@id)!=(((.//ancestor::fraction|' +
            'ancestor::root|ancestor::sqrt|ancestor::cell|ancestor::line|' +
            'ancestor::stree)[1]//*[not(*)])[last()]/@id)';
        store.defineRule(name, 'default', verbStr, 'self::tensor', cstr, ...components);
        if (brief) {
            store.defineRule(name, 'brief', briefStr, 'self::tensor', cstr, ...components);
            store.defineRule(name, 'sbrief', briefStr, 'self::tensor', cstr, ...components);
        }
    }
}
exports.generateTensorRules = generateTensorRules;
function smallRoot(node) {
    let max = Object.keys(locale_1.LOCALE.MESSAGES.MSroots).length;
    if (!max) {
        return [];
    }
    else {
        max++;
    }
    if (!node.childNodes ||
        node.childNodes.length === 0 ||
        !node.childNodes[0].childNodes) {
        return [];
    }
    const index = node.childNodes[0].childNodes[0].textContent;
    if (!/^\d+$/.test(index)) {
        return [];
    }
    const num = parseInt(index, 10);
    return num > 1 && num <= max ? [node] : [];
}
exports.smallRoot = smallRoot;


/***/ }),

/***/ 9570:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.implicitIterator = exports.relationIterator = exports.propagateNumber = exports.checkParent_ = exports.NUMBER_INHIBITORS_ = exports.NUMBER_PROPAGATORS_ = exports.enlargeFence = exports.indexRadical = exports.closingRadical = exports.openingRadical = exports.radicalNestingDepth = exports.nestedRadical = exports.overBevelledFraction = exports.overFraction = exports.closingFraction = exports.openingFraction = void 0;
const auditory_description_1 = __webpack_require__(4148);
const DomUtil = __webpack_require__(6671);
const XpathUtil = __webpack_require__(5024);
const grammar_1 = __webpack_require__(1058);
const engine_1 = __webpack_require__(4886);
const semantic_annotations_1 = __webpack_require__(4036);
const semantic_annotator_1 = __webpack_require__(241);
const locale_1 = __webpack_require__(4524);
const MathspeakUtil = __webpack_require__(3269);
function openingFraction(node) {
    const depth = MathspeakUtil.fractionNestingDepth(node);
    return (new Array(depth).join(locale_1.LOCALE.MESSAGES.MS.FRACTION_REPEAT) +
        locale_1.LOCALE.MESSAGES.MS.FRACTION_START);
}
exports.openingFraction = openingFraction;
function closingFraction(node) {
    const depth = MathspeakUtil.fractionNestingDepth(node);
    return (new Array(depth).join(locale_1.LOCALE.MESSAGES.MS.FRACTION_REPEAT) +
        locale_1.LOCALE.MESSAGES.MS.FRACTION_END);
}
exports.closingFraction = closingFraction;
function overFraction(node) {
    const depth = MathspeakUtil.fractionNestingDepth(node);
    return (new Array(depth).join(locale_1.LOCALE.MESSAGES.MS.FRACTION_REPEAT) +
        locale_1.LOCALE.MESSAGES.MS.FRACTION_OVER);
}
exports.overFraction = overFraction;
function overBevelledFraction(node) {
    const depth = MathspeakUtil.fractionNestingDepth(node);
    return (new Array(depth).join(locale_1.LOCALE.MESSAGES.MS.FRACTION_REPEAT) +
        '⠸' +
        locale_1.LOCALE.MESSAGES.MS.FRACTION_OVER);
}
exports.overBevelledFraction = overBevelledFraction;
function nestedRadical(node, postfix) {
    const depth = radicalNestingDepth(node);
    if (depth === 1) {
        return postfix;
    }
    return new Array(depth).join(locale_1.LOCALE.MESSAGES.MS.NESTED) + postfix;
}
exports.nestedRadical = nestedRadical;
function radicalNestingDepth(node, opt_depth) {
    const depth = opt_depth || 0;
    if (!node.parentNode) {
        return depth;
    }
    return radicalNestingDepth(node.parentNode, node.tagName === 'root' || node.tagName === 'sqrt' ? depth + 1 : depth);
}
exports.radicalNestingDepth = radicalNestingDepth;
function openingRadical(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.STARTROOT);
}
exports.openingRadical = openingRadical;
function closingRadical(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.ENDROOT);
}
exports.closingRadical = closingRadical;
function indexRadical(node) {
    return nestedRadical(node, locale_1.LOCALE.MESSAGES.MS.ROOTINDEX);
}
exports.indexRadical = indexRadical;
function enlargeFence(text) {
    const start = '⠠';
    if (text.length === 1) {
        return start + text;
    }
    const neut = '⠳';
    const split = text.split('');
    if (split.every(function (x) {
        return x === neut;
    })) {
        return start + split.join(start);
    }
    return text.slice(0, -1) + start + text.slice(-1);
}
exports.enlargeFence = enlargeFence;
grammar_1.Grammar.getInstance().setCorrection('enlargeFence', enlargeFence);
exports.NUMBER_PROPAGATORS_ = [
    "multirel",
    "relseq",
    "appl",
    "row",
    "line"
];
exports.NUMBER_INHIBITORS_ = [
    "subscript",
    "superscript",
    "overscore",
    "underscore"
];
function checkParent_(node, info) {
    const parent = node.parent;
    if (!parent) {
        return false;
    }
    const type = parent.type;
    if (exports.NUMBER_PROPAGATORS_.indexOf(type) !== -1 ||
        (type === "prefixop" &&
            parent.role === "negative" &&
            !info.script) ||
        (type === "prefixop" &&
            parent.role === "geometry")) {
        return true;
    }
    if (type === "punctuated") {
        if (!info.enclosed || parent.role === "text") {
            return true;
        }
    }
    return false;
}
exports.checkParent_ = checkParent_;
function propagateNumber(node, info) {
    if (!node.childNodes.length) {
        if (checkParent_(node, info)) {
            info.number = true;
            info.script = false;
            info.enclosed = false;
        }
        return [
            info['number'] ? 'number' : '',
            { number: false, enclosed: info.enclosed, script: info.script }
        ];
    }
    if (exports.NUMBER_INHIBITORS_.indexOf(node.type) !== -1) {
        info.script = true;
    }
    if (node.type === "fenced") {
        info.number = false;
        info.enclosed = true;
        return ['', info];
    }
    if (checkParent_(node, info)) {
        info.number = true;
        info.enclosed = false;
    }
    return ['', info];
}
exports.propagateNumber = propagateNumber;
(0, semantic_annotations_1.register)(new semantic_annotator_1.SemanticVisitor('nemeth', 'number', propagateNumber, { number: true }));
function relationIterator(nodes, context) {
    const childNodes = nodes.slice(0);
    let first = true;
    let contentNodes;
    if (nodes.length > 0) {
        contentNodes = XpathUtil.evalXPath('../../content/*', nodes[0]);
    }
    else {
        contentNodes = [];
    }
    return function () {
        const content = contentNodes.shift();
        const leftChild = childNodes.shift();
        const rightChild = childNodes[0];
        const contextDescr = context
            ? [auditory_description_1.AuditoryDescription.create({ text: context }, { translate: true })]
            : [];
        if (!content) {
            return contextDescr;
        }
        const base = leftChild
            ? MathspeakUtil.nestedSubSuper(leftChild, '', {
                sup: locale_1.LOCALE.MESSAGES.MS.SUPER,
                sub: locale_1.LOCALE.MESSAGES.MS.SUB
            })
            : '';
        const left = (leftChild && DomUtil.tagName(leftChild) !== 'EMPTY') ||
            (first &&
                content.parentNode.parentNode &&
                content.parentNode.parentNode.previousSibling)
            ? [auditory_description_1.AuditoryDescription.create({ text: '⠀' + base }, {})]
            : [];
        const right = (rightChild && DomUtil.tagName(rightChild) !== 'EMPTY') ||
            (!contentNodes.length &&
                content.parentNode.parentNode &&
                content.parentNode.parentNode.nextSibling)
            ? [auditory_description_1.AuditoryDescription.create({ text: '⠀' }, {})]
            : [];
        const descrs = engine_1.default.evaluateNode(content);
        first = false;
        return contextDescr.concat(left, descrs, right);
    };
}
exports.relationIterator = relationIterator;
function implicitIterator(nodes, context) {
    const childNodes = nodes.slice(0);
    let contentNodes;
    if (nodes.length > 0) {
        contentNodes = XpathUtil.evalXPath('../../content/*', nodes[0]);
    }
    else {
        contentNodes = [];
    }
    return function () {
        const leftChild = childNodes.shift();
        const rightChild = childNodes[0];
        const content = contentNodes.shift();
        const contextDescr = context
            ? [auditory_description_1.AuditoryDescription.create({ text: context }, { translate: true })]
            : [];
        if (!content) {
            return contextDescr;
        }
        const left = leftChild && DomUtil.tagName(leftChild) === 'NUMBER';
        const right = rightChild && DomUtil.tagName(rightChild) === 'NUMBER';
        return contextDescr.concat(left && right && content.getAttribute('role') === "space"
            ? [auditory_description_1.AuditoryDescription.create({ text: '⠀' }, {})]
            : []);
    };
}
exports.implicitIterator = implicitIterator;


/***/ }),

/***/ 2110:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ordinalPosition = exports.vulgarFraction = exports.wordCounter = exports.ordinalCounter = void 0;
const span_1 = __webpack_require__(1930);
const DomUtil = __webpack_require__(6671);
const locale_1 = __webpack_require__(4524);
const transformers_1 = __webpack_require__(9385);
function ordinalCounter(_node, context) {
    let counter = 0;
    return function () {
        return locale_1.LOCALE.NUMBERS.numericOrdinal(++counter) + ' ' + context;
    };
}
exports.ordinalCounter = ordinalCounter;
function wordCounter(_node, context) {
    let counter = 0;
    return function () {
        return locale_1.LOCALE.NUMBERS.numberToOrdinal(++counter, false) + ' ' + context;
    };
}
exports.wordCounter = wordCounter;
function vulgarFraction(node) {
    const conversion = (0, transformers_1.convertVulgarFraction)(node, locale_1.LOCALE.MESSAGES.MS.FRAC_OVER);
    if (conversion.convertible &&
        conversion.enumerator &&
        conversion.denominator) {
        return [
            new span_1.Span(locale_1.LOCALE.NUMBERS.numberToWords(conversion.enumerator), {
                extid: node.childNodes[0].childNodes[0].getAttribute('extid'),
                separator: ''
            }),
            new span_1.Span(locale_1.LOCALE.NUMBERS.vulgarSep, { separator: '' }),
            new span_1.Span(locale_1.LOCALE.NUMBERS.numberToOrdinal(conversion.denominator, conversion.enumerator !== 1), {
                extid: node.childNodes[0].childNodes[1].getAttribute('extid')
            })
        ];
    }
    return [
        new span_1.Span(conversion.content || '', { extid: node.getAttribute('extid') })
    ];
}
exports.vulgarFraction = vulgarFraction;
function ordinalPosition(node) {
    const children = DomUtil.toArray(node.parentNode.childNodes);
    return locale_1.LOCALE.NUMBERS.numericOrdinal(children.indexOf(node) + 1).toString();
}
exports.ordinalPosition = ordinalPosition;


/***/ }),

/***/ 3724:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BrailleRules = exports.OtherRules = exports.PrefixRules = void 0;
const dynamic_cstr_1 = __webpack_require__(8310);
const StoreUtil = __webpack_require__(931);
const MathspeakUtil = __webpack_require__(3269);
const NemethUtil = __webpack_require__(9570);
const NumbersUtil = __webpack_require__(2110);
const SpeechRules = __webpack_require__(7278);
function PrefixRules() {
    SpeechRules.addStore('en.prefix.default', '', {
        CSFordinalPosition: NumbersUtil.ordinalPosition
    });
}
exports.PrefixRules = PrefixRules;
function OtherRules() {
    SpeechRules.addStore('en.speech.chromevox', '', {
        CTFnodeCounter: StoreUtil.nodeCounter,
        CTFcontentIterator: StoreUtil.contentIterator
    });
    SpeechRules.addStore('en.speech.emacspeak', 'en.speech.chromevox', {
        CQFvulgarFractionSmall: MathspeakUtil.isSmallVulgarFraction,
        CSFvulgarFraction: NumbersUtil.vulgarFraction
    });
}
exports.OtherRules = OtherRules;
function BrailleRules() {
    SpeechRules.addStore('nemeth.braille.default', dynamic_cstr_1.DynamicCstr.BASE_LOCALE + '.speech.mathspeak', {
        CSFopenFraction: NemethUtil.openingFraction,
        CSFcloseFraction: NemethUtil.closingFraction,
        CSFoverFraction: NemethUtil.overFraction,
        CSFoverBevFraction: NemethUtil.overBevelledFraction,
        CSFopenRadical: NemethUtil.openingRadical,
        CSFcloseRadical: NemethUtil.closingRadical,
        CSFindexRadical: NemethUtil.indexRadical,
        CSFsubscript: MathspeakUtil.subscriptVerbose,
        CSFsuperscript: MathspeakUtil.superscriptVerbose,
        CSFbaseline: MathspeakUtil.baselineVerbose,
        CGFtensorRules: (st) => MathspeakUtil.generateTensorRules(st, false),
        CTFrelationIterator: NemethUtil.relationIterator,
        CTFimplicitIterator: NemethUtil.implicitIterator
    });
}
exports.BrailleRules = BrailleRules;


/***/ }),

/***/ 9805:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.init = exports.INIT_ = void 0;
const clearspeak_rules_1 = __webpack_require__(127);
const mathspeak_rules_1 = __webpack_require__(4972);
const other_rules_1 = __webpack_require__(3724);
exports.INIT_ = false;
function init() {
    if (exports.INIT_) {
        return;
    }
    (0, mathspeak_rules_1.MathspeakRules)();
    (0, clearspeak_rules_1.ClearspeakRules)();
    (0, other_rules_1.PrefixRules)();
    (0, other_rules_1.OtherRules)();
    (0, other_rules_1.BrailleRules)();
    exports.INIT_ = true;
}
exports.init = init;


/***/ }),

/***/ 7278:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.getStore = exports.addStore = exports.funcStore = void 0;
const dynamic_cstr_1 = __webpack_require__(8310);
exports.funcStore = new Map();
function addStore(constr, inherit, store) {
    const values = {};
    if (inherit) {
        const inherits = exports.funcStore.get(inherit) || {};
        Object.assign(values, inherits);
    }
    exports.funcStore.set(constr, Object.assign(values, store));
}
exports.addStore = addStore;
function getStore(locale, modality, domain) {
    return (exports.funcStore.get([locale, modality, domain].join('.')) ||
        exports.funcStore.get([dynamic_cstr_1.DynamicCstr.DEFAULT_VALUES[dynamic_cstr_1.Axis.LOCALE], modality, domain].join('.')) ||
        exports.funcStore.get([dynamic_cstr_1.DynamicCstr.BASE_LOCALE, modality, domain].join('.')) ||
        {});
}
exports.getStore = getStore;


/***/ }),

/***/ 9771:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.oneLeft = exports.leftMostUnit = exports.rightMostUnit = exports.unitMultipliers = void 0;
const auditory_description_1 = __webpack_require__(4148);
const XpathUtil = __webpack_require__(5024);
const locale_1 = __webpack_require__(4524);
function unitMultipliers(nodes, _context) {
    const children = nodes;
    let counter = 0;
    return function () {
        const descr = auditory_description_1.AuditoryDescription.create({
            text: rightMostUnit(children[counter]) &&
                leftMostUnit(children[counter + 1])
                ? locale_1.LOCALE.MESSAGES.unitTimes
                : ''
        }, {});
        counter++;
        return [descr];
    };
}
exports.unitMultipliers = unitMultipliers;
const SCRIPT_ELEMENTS = [
    "superscript",
    "subscript",
    "overscore",
    "underscore"
];
function rightMostUnit(node) {
    while (node) {
        if (node.getAttribute('role') === 'unit') {
            return true;
        }
        const tag = node.tagName;
        const children = XpathUtil.evalXPath('children/*', node);
        node = (SCRIPT_ELEMENTS.indexOf(tag) !== -1
            ? children[0]
            : children[children.length - 1]);
    }
    return false;
}
exports.rightMostUnit = rightMostUnit;
function leftMostUnit(node) {
    while (node) {
        if (node.getAttribute('role') === 'unit') {
            return true;
        }
        const children = XpathUtil.evalXPath('children/*', node);
        node = children[0];
    }
    return false;
}
exports.leftMostUnit = leftMostUnit;
function oneLeft(node) {
    while (node) {
        if (node.tagName === 'number' && node.textContent === '1') {
            return [node];
        }
        if (node.tagName !== 'infixop' ||
            (node.getAttribute('role') !== 'multiplication' &&
                node.getAttribute('role') !== 'implicit')) {
            return [];
        }
        node = XpathUtil.evalXPath('children/*', node)[0];
    }
    return [];
}
exports.oneLeft = oneLeft;


/***/ }),

/***/ 4660:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AbstractWalker = void 0;
const auditory_description_1 = __webpack_require__(4148);
const AuralRendering = __webpack_require__(4253);
const DomUtil = __webpack_require__(6671);
const EngineConst = __webpack_require__(4998);
const engine_setup_1 = __webpack_require__(985);
const event_util_1 = __webpack_require__(6988);
const enrich_attr_1 = __webpack_require__(8171);
const locale_1 = __webpack_require__(4524);
const grammar_1 = __webpack_require__(1058);
const semantic_skeleton_1 = __webpack_require__(7984);
const SpeechGeneratorFactory = __webpack_require__(7317);
const SpeechGeneratorUtil = __webpack_require__(144);
const clearspeak_preferences_1 = __webpack_require__(3955);
const focus_1 = __webpack_require__(5658);
const rebuild_stree_1 = __webpack_require__(1848);
const walker_1 = __webpack_require__(8119);
const WalkerUtil = __webpack_require__(8835);
const XpathUtil = __webpack_require__(5024);
class AbstractWalker {
    constructor(node, generator, highlighter, xml) {
        this.node = node;
        this.generator = generator;
        this.highlighter = highlighter;
        this.modifier = false;
        this.keyMapping = new Map([
            [event_util_1.KeyCode.UP, this.up.bind(this)],
            [event_util_1.KeyCode.DOWN, this.down.bind(this)],
            [event_util_1.KeyCode.RIGHT, this.right.bind(this)],
            [event_util_1.KeyCode.LEFT, this.left.bind(this)],
            [event_util_1.KeyCode.TAB, this.repeat.bind(this)],
            [event_util_1.KeyCode.DASH, this.expand.bind(this)],
            [event_util_1.KeyCode.SPACE, this.depth.bind(this)],
            [event_util_1.KeyCode.HOME, this.home.bind(this)],
            [event_util_1.KeyCode.X, this.summary.bind(this)],
            [event_util_1.KeyCode.Z, this.detail.bind(this)],
            [event_util_1.KeyCode.V, this.virtualize.bind(this)],
            [event_util_1.KeyCode.P, this.previous.bind(this)],
            [event_util_1.KeyCode.U, this.undo.bind(this)],
            [event_util_1.KeyCode.LESS, this.previousRules.bind(this)],
            [event_util_1.KeyCode.GREATER, this.nextRules.bind(this)]
        ]);
        this.cursors = [];
        this.xml_ = null;
        this.rebuilt_ = null;
        this.focus_ = null;
        this.active_ = false;
        if (this.node.id) {
            this.id = this.node.id;
        }
        else if (this.node.hasAttribute(AbstractWalker.SRE_ID_ATTR)) {
            this.id = this.node.getAttribute(AbstractWalker.SRE_ID_ATTR);
        }
        else {
            this.node.setAttribute(AbstractWalker.SRE_ID_ATTR, AbstractWalker.ID_COUNTER.toString());
            this.id = AbstractWalker.ID_COUNTER++;
        }
        this.rootNode = WalkerUtil.getSemanticRoot(node);
        this.rootId = this.rootNode.getAttribute(enrich_attr_1.Attribute.ID);
        this.xmlString_ = xml;
        this.moved = walker_1.WalkerMoves.ENTER;
    }
    getXml() {
        if (!this.xml_) {
            this.xml_ = DomUtil.parseInput(this.xmlString_);
        }
        return this.xml_;
    }
    getRebuilt() {
        if (!this.rebuilt_) {
            this.rebuildStree();
        }
        return this.rebuilt_;
    }
    isActive() {
        return this.active_;
    }
    activate() {
        if (this.isActive()) {
            return;
        }
        this.generator.start();
        this.toggleActive_();
    }
    deactivate() {
        if (!this.isActive()) {
            return;
        }
        walker_1.WalkerState.setState(this.id, this.primaryId());
        this.generator.end();
        this.toggleActive_();
    }
    getFocus(update = false) {
        if (!this.focus_) {
            this.focus_ = this.singletonFocus(this.rootId);
        }
        if (update) {
            this.updateFocus();
        }
        return this.focus_;
    }
    setFocus(focus) {
        this.focus_ = focus;
    }
    getDepth() {
        return this.levels.depth() - 1;
    }
    isSpeech() {
        return this.generator.modality === enrich_attr_1.Attribute.SPEECH;
    }
    focusDomNodes() {
        return this.getFocus().getDomNodes();
    }
    focusSemanticNodes() {
        return this.getFocus().getSemanticNodes();
    }
    speech() {
        const nodes = this.focusDomNodes();
        if (!nodes.length) {
            return '';
        }
        const special = this.specialMove();
        if (special !== null) {
            return special;
        }
        switch (this.moved) {
            case walker_1.WalkerMoves.DEPTH:
                return this.depth_();
            case walker_1.WalkerMoves.SUMMARY:
                return this.summary_();
            case walker_1.WalkerMoves.DETAIL:
                return this.detail_();
            default: {
                const speech = [];
                const snodes = this.focusSemanticNodes();
                for (let i = 0, l = nodes.length; i < l; i++) {
                    const node = nodes[i];
                    const snode = snodes[i];
                    speech.push(node
                        ? this.generator.getSpeech(node, this.getXml())
                        : SpeechGeneratorUtil.recomputeMarkup(snode));
                }
                return this.mergePrefix_(speech);
            }
        }
    }
    move(key) {
        const direction = this.keyMapping.get(key);
        if (!direction) {
            return null;
        }
        const focus = direction();
        if (!focus || focus === this.getFocus()) {
            return false;
        }
        this.setFocus(focus);
        if (this.moved === walker_1.WalkerMoves.HOME) {
            this.levels = this.initLevels();
        }
        return true;
    }
    up() {
        this.moved = walker_1.WalkerMoves.UP;
        return this.getFocus();
    }
    down() {
        this.moved = walker_1.WalkerMoves.DOWN;
        return this.getFocus();
    }
    left() {
        this.moved = walker_1.WalkerMoves.LEFT;
        return this.getFocus();
    }
    right() {
        this.moved = walker_1.WalkerMoves.RIGHT;
        return this.getFocus();
    }
    repeat() {
        this.moved = walker_1.WalkerMoves.REPEAT;
        return this.getFocus().clone();
    }
    depth() {
        this.moved = this.isSpeech() ? walker_1.WalkerMoves.DEPTH : walker_1.WalkerMoves.REPEAT;
        return this.getFocus().clone();
    }
    home() {
        this.moved = walker_1.WalkerMoves.HOME;
        const focus = this.singletonFocus(this.rootId);
        return focus;
    }
    getBySemanticId(id) {
        return WalkerUtil.getBySemanticId(this.node, id);
    }
    primaryId() {
        return this.getFocus().getSemanticPrimary().id.toString();
    }
    expand() {
        const primary = this.getFocus().getDomPrimary();
        const expandable = this.actionable_(primary);
        if (!expandable) {
            return this.getFocus();
        }
        this.moved = walker_1.WalkerMoves.EXPAND;
        expandable.dispatchEvent(new Event('click'));
        return this.getFocus().clone();
    }
    expandable(node) {
        const parent = !!this.actionable_(node);
        return parent && node.childNodes.length === 0;
    }
    collapsible(node) {
        const parent = !!this.actionable_(node);
        return parent && node.childNodes.length > 0;
    }
    restoreState() {
        if (!this.highlighter) {
            return;
        }
        const state = walker_1.WalkerState.getState(this.id);
        if (!state) {
            return;
        }
        let node = this.getRebuilt().nodeDict[state];
        const path = [];
        while (node) {
            path.push(node.id);
            node = node.parent;
        }
        path.pop();
        while (path.length > 0) {
            this.down();
            const id = path.pop();
            const focus = this.findFocusOnLevel(id);
            if (!focus) {
                break;
            }
            this.setFocus(focus);
        }
        this.moved = walker_1.WalkerMoves.ENTER;
    }
    updateFocus() {
        this.setFocus(focus_1.Focus.factory(this.getFocus().getSemanticPrimary().id.toString(), this.getFocus()
            .getSemanticNodes()
            .map((x) => x.id.toString()), this.getRebuilt(), this.node));
    }
    rebuildStree() {
        this.rebuilt_ = new rebuild_stree_1.RebuildStree(this.getXml());
        this.rootId = this.rebuilt_.stree.root.id.toString();
        this.generator.setRebuilt(this.rebuilt_);
        this.skeleton = semantic_skeleton_1.SemanticSkeleton.fromTree(this.rebuilt_.stree);
        this.skeleton.populate();
        this.focus_ = this.singletonFocus(this.rootId);
        this.levels = this.initLevels();
        SpeechGeneratorUtil.connectMactions(this.node, this.getXml(), this.rebuilt_.xml);
    }
    previousLevel() {
        const dnode = this.getFocus().getDomPrimary();
        return dnode
            ? WalkerUtil.getAttribute(dnode, enrich_attr_1.Attribute.PARENT)
            : this.getFocus().getSemanticPrimary().parent.id.toString();
    }
    nextLevel() {
        const dnode = this.getFocus().getDomPrimary();
        let children;
        let content;
        if (dnode) {
            children = WalkerUtil.splitAttribute(WalkerUtil.getAttribute(dnode, enrich_attr_1.Attribute.CHILDREN));
            content = WalkerUtil.splitAttribute(WalkerUtil.getAttribute(dnode, enrich_attr_1.Attribute.CONTENT));
            const type = WalkerUtil.getAttribute(dnode, enrich_attr_1.Attribute.TYPE);
            const role = WalkerUtil.getAttribute(dnode, enrich_attr_1.Attribute.ROLE);
            return this.combineContentChildren(type, role, content, children);
        }
        const toIds = (x) => x.id.toString();
        const snode = this.getRebuilt().nodeDict[this.primaryId()];
        children = snode.childNodes.map(toIds);
        content = snode.contentNodes.map(toIds);
        if (children.length === 0) {
            return [];
        }
        return this.combineContentChildren(snode.type, snode.role, content, children);
    }
    singletonFocus(id) {
        this.getRebuilt();
        const ids = this.retrieveVisuals(id);
        return this.focusFromId(id, ids);
    }
    retrieveVisuals(id) {
        if (!this.skeleton) {
            return [id];
        }
        const num = parseInt(id, 10);
        const semStree = this.skeleton.subtreeNodes(num);
        if (!semStree.length) {
            return [id];
        }
        semStree.unshift(num);
        const mmlStree = {};
        const result = [];
        XpathUtil.updateEvaluator(this.getXml());
        for (const child of semStree) {
            if (mmlStree[child]) {
                continue;
            }
            result.push(child.toString());
            mmlStree[child] = true;
            this.subtreeIds(child, mmlStree);
        }
        return result;
    }
    subtreeIds(id, nodes) {
        const xmlRoot = XpathUtil.evalXPath(`//*[@data-semantic-id="${id}"]`, this.getXml());
        const xpath = XpathUtil.evalXPath('*//@data-semantic-id', xmlRoot[0]);
        xpath.forEach((x) => (nodes[parseInt(x.textContent, 10)] = true));
    }
    focusFromId(id, ids) {
        return focus_1.Focus.factory(id, ids, this.getRebuilt(), this.node);
    }
    summary() {
        this.moved = this.isSpeech() ? walker_1.WalkerMoves.SUMMARY : walker_1.WalkerMoves.REPEAT;
        return this.getFocus().clone();
    }
    detail() {
        this.moved = this.isSpeech() ? walker_1.WalkerMoves.DETAIL : walker_1.WalkerMoves.REPEAT;
        return this.getFocus().clone();
    }
    specialMove() {
        return null;
    }
    virtualize(opt_undo) {
        this.cursors.push({
            focus: this.getFocus(),
            levels: this.levels,
            undo: opt_undo || !this.cursors.length
        });
        this.levels = this.levels.clone();
        return this.getFocus().clone();
    }
    previous() {
        const previous = this.cursors.pop();
        if (!previous) {
            return this.getFocus();
        }
        this.levels = previous.levels;
        return previous.focus;
    }
    undo() {
        let previous;
        do {
            previous = this.cursors.pop();
        } while (previous && !previous.undo);
        if (!previous) {
            return this.getFocus();
        }
        this.levels = previous.levels;
        return previous.focus;
    }
    update(options) {
        this.generator.setOptions(options);
        (0, engine_setup_1.setup)(options).then(() => SpeechGeneratorFactory.generator('Tree').getSpeech(this.node, this.getXml()));
    }
    nextRules() {
        const options = this.generator.getOptions();
        if (options.modality !== 'speech') {
            return this.getFocus();
        }
        EngineConst.DOMAIN_TO_STYLES[options.domain] = options.style;
        options.domain =
            options.domain === 'mathspeak' ? 'clearspeak' : 'mathspeak';
        options.style = EngineConst.DOMAIN_TO_STYLES[options.domain];
        this.update(options);
        this.moved = walker_1.WalkerMoves.REPEAT;
        return this.getFocus().clone();
    }
    nextStyle(domain, style) {
        if (domain === 'mathspeak') {
            const styles = ['default', 'brief', 'sbrief'];
            const index = styles.indexOf(style);
            if (index === -1) {
                return style;
            }
            return index >= styles.length - 1 ? styles[0] : styles[index + 1];
        }
        if (domain === 'clearspeak') {
            const prefs = clearspeak_preferences_1.ClearspeakPreferences.getLocalePreferences();
            const loc = prefs['en'];
            if (!loc) {
                return 'default';
            }
            const smart = clearspeak_preferences_1.ClearspeakPreferences.relevantPreferences(this.getFocus().getSemanticPrimary());
            const current = clearspeak_preferences_1.ClearspeakPreferences.findPreference(style, smart);
            const options = loc[smart].map(function (x) {
                return x.split('_')[1];
            });
            const index = options.indexOf(current);
            if (index === -1) {
                return style;
            }
            const next = index >= options.length - 1 ? options[0] : options[index + 1];
            const result = clearspeak_preferences_1.ClearspeakPreferences.addPreference(style, smart, next);
            return result;
        }
        return style;
    }
    previousRules() {
        const options = this.generator.getOptions();
        if (options.modality !== 'speech') {
            return this.getFocus();
        }
        options.style = this.nextStyle(options.domain, options.style);
        this.update(options);
        this.moved = walker_1.WalkerMoves.REPEAT;
        return this.getFocus().clone();
    }
    refocus() {
        let focus = this.getFocus();
        let last;
        while (!focus.getNodes().length) {
            last = this.levels.peek();
            const up = this.up();
            if (!up) {
                break;
            }
            this.setFocus(up);
            focus = this.getFocus(true);
        }
        this.levels.push(last);
        this.setFocus(focus);
    }
    toggleActive_() {
        this.active_ = !this.active_;
    }
    mergePrefix_(speech, pre = []) {
        const prefix = this.isSpeech() ? this.prefix_() : '';
        if (prefix) {
            speech.unshift(prefix);
        }
        const postfix = this.isSpeech() ? this.postfix_() : '';
        if (postfix) {
            speech.push(postfix);
        }
        return AuralRendering.finalize(AuralRendering.merge(pre.concat(speech)));
    }
    prefix_() {
        const nodes = this.getFocus().getDomNodes();
        const snodes = this.getFocus().getSemanticNodes();
        return nodes[0]
            ? WalkerUtil.getAttribute(nodes[0], enrich_attr_1.Attribute.PREFIX)
            : SpeechGeneratorUtil.retrievePrefix(snodes[0]);
    }
    postfix_() {
        const nodes = this.getFocus().getDomNodes();
        return nodes[0]
            ? WalkerUtil.getAttribute(nodes[0], enrich_attr_1.Attribute.POSTFIX)
            : '';
    }
    depth_() {
        const oldDepth = grammar_1.Grammar.getInstance().getParameter('depth');
        grammar_1.Grammar.getInstance().setParameter('depth', true);
        const primary = this.getFocus().getDomPrimary();
        const expand = this.expandable(primary)
            ? locale_1.LOCALE.MESSAGES.navigate.EXPANDABLE
            : this.collapsible(primary)
                ? locale_1.LOCALE.MESSAGES.navigate.COLLAPSIBLE
                : '';
        const level = locale_1.LOCALE.MESSAGES.navigate.LEVEL + ' ' + this.getDepth();
        const snodes = this.getFocus().getSemanticNodes();
        const prefix = SpeechGeneratorUtil.retrievePrefix(snodes[0]);
        const audio = [
            new auditory_description_1.AuditoryDescription({ text: level, personality: {} }),
            new auditory_description_1.AuditoryDescription({ text: prefix, personality: {} }),
            new auditory_description_1.AuditoryDescription({ text: expand, personality: {} })
        ];
        grammar_1.Grammar.getInstance().setParameter('depth', oldDepth);
        return AuralRendering.finalize(AuralRendering.markup(audio));
    }
    actionable_(node) {
        const parent = node === null || node === void 0 ? void 0 : node.parentNode;
        return parent && this.highlighter.isMactionNode(parent) ? parent : null;
    }
    summary_() {
        const sprimary = this.getFocus().getSemanticPrimary();
        const sid = sprimary.id.toString();
        const snode = this.getRebuilt().xml.getAttribute('id') === sid
            ? this.getRebuilt().xml
            : DomUtil.querySelectorAllByAttrValue(this.getRebuilt().xml, 'id', sid)[0];
        const summary = SpeechGeneratorUtil.retrieveSummary(snode);
        const speech = this.mergePrefix_([summary]);
        return speech;
    }
    detail_() {
        const sprimary = this.getFocus().getSemanticPrimary();
        const sid = sprimary.id.toString();
        const snode = this.getRebuilt().xml.getAttribute('id') === sid
            ? this.getRebuilt().xml
            : DomUtil.querySelectorAllByAttrValue(this.getRebuilt().xml, 'id', sid)[0];
        const oldAlt = snode.getAttribute('alternative');
        snode.removeAttribute('alternative');
        const detail = SpeechGeneratorUtil.computeMarkup(snode);
        const speech = this.mergePrefix_([detail]);
        snode.setAttribute('alternative', oldAlt);
        return speech;
    }
}
exports.AbstractWalker = AbstractWalker;
AbstractWalker.ID_COUNTER = 0;
AbstractWalker.SRE_ID_ATTR = 'sre-explorer-id';


/***/ }),

/***/ 4296:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DummyWalker = void 0;
const abstract_walker_1 = __webpack_require__(4660);
class DummyWalker extends abstract_walker_1.AbstractWalker {
    up() {
        return null;
    }
    down() {
        return null;
    }
    left() {
        return null;
    }
    right() {
        return null;
    }
    repeat() {
        return null;
    }
    depth() {
        return null;
    }
    home() {
        return null;
    }
    getDepth() {
        return 0;
    }
    initLevels() {
        return null;
    }
    combineContentChildren(_type, _role, _content, _children) {
        return [];
    }
    findFocusOnLevel(_id) {
        return null;
    }
}
exports.DummyWalker = DummyWalker;


/***/ }),

/***/ 5658:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Focus = void 0;
const WalkerUtil = __webpack_require__(8835);
class Focus {
    constructor(nodes, primary) {
        this.nodes = nodes;
        this.primary = primary;
        this.domNodes = [];
        this.domPrimary_ = null;
        this.allNodes = [];
    }
    static factory(primaryId, nodeIds, rebuilt, dom) {
        const idFunc = (id) => WalkerUtil.getBySemanticId(dom, id);
        const dict = rebuilt.nodeDict;
        const node = idFunc(primaryId);
        const nodes = nodeIds.map(idFunc);
        const snodes = nodeIds.map(function (primaryId) {
            return dict[primaryId];
        });
        const focus = new Focus(snodes, dict[primaryId]);
        focus.domNodes = nodes;
        focus.domPrimary_ = node;
        focus.allNodes = Focus.generateAllVisibleNodes_(nodeIds, nodes, dict, dom);
        return focus;
    }
    static generateAllVisibleNodes_(ids, nodes, dict, domNode) {
        const idFunc = (id) => WalkerUtil.getBySemanticId(domNode, id);
        let result = [];
        for (let i = 0, l = ids.length; i < l; i++) {
            if (nodes[i]) {
                result.push(nodes[i]);
                continue;
            }
            const virtual = dict[ids[i]];
            if (!virtual) {
                continue;
            }
            const childIds = virtual.childNodes.map(function (x) {
                return x.id.toString();
            });
            const children = childIds.map(idFunc);
            result = result.concat(Focus.generateAllVisibleNodes_(childIds, children, dict, domNode));
        }
        return result;
    }
    getSemanticPrimary() {
        return this.primary;
    }
    getSemanticNodes() {
        return this.nodes;
    }
    getNodes() {
        return this.allNodes;
    }
    getDomNodes() {
        return this.domNodes;
    }
    getDomPrimary() {
        return this.domPrimary_;
    }
    toString() {
        return 'Primary:' + this.domPrimary_ + ' Nodes:' + this.domNodes;
    }
    clone() {
        const focus = new Focus(this.nodes, this.primary);
        focus.domNodes = this.domNodes;
        focus.domPrimary_ = this.domPrimary_;
        focus.allNodes = this.allNodes;
        return focus;
    }
}
exports.Focus = Focus;


/***/ }),

/***/ 1497:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Levels = void 0;
class Levels {
    constructor() {
        this.level_ = [];
    }
    push(level) {
        this.level_.push(level);
    }
    pop() {
        return this.level_.pop();
    }
    peek() {
        return this.level_[this.level_.length - 1] || null;
    }
    indexOf(element) {
        const last = this.peek();
        return !last ? null : last.indexOf(element);
    }
    find(pred) {
        const last = this.peek();
        if (!last) {
            return null;
        }
        for (let i = 0, l = last.length; i < l; i++) {
            if (pred(last[i])) {
                return last[i];
            }
        }
        return null;
    }
    get(index) {
        const last = this.peek();
        return !last || index < 0 || index >= last.length ? null : last[index];
    }
    depth() {
        return this.level_.length;
    }
    clone() {
        const levels = new Levels();
        levels.level_ = this.level_.slice(0);
        return levels;
    }
    toString() {
        let str = '';
        for (let i = 0, level; (level = this.level_[i]); i++) {
            str +=
                '\n' +
                    level.map(function (x) {
                        return x.toString();
                    });
        }
        return str;
    }
}
exports.Levels = Levels;


/***/ }),

/***/ 1848:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.RebuildStree = void 0;
const DomUtil = __webpack_require__(6671);
const enrich_attr_1 = __webpack_require__(8171);
const semantic_attr_1 = __webpack_require__(4020);
const semantic_node_factory_1 = __webpack_require__(4790);
const semantic_processor_1 = __webpack_require__(7793);
const semantic_skeleton_1 = __webpack_require__(7984);
const semantic_tree_1 = __webpack_require__(1784);
const SemanticUtil = __webpack_require__(8901);
const WalkerUtil = __webpack_require__(8835);
class RebuildStree {
    constructor(mathml) {
        this.mathml = mathml;
        this.factory = new semantic_node_factory_1.SemanticNodeFactory();
        this.nodeDict = {};
        this.mmlRoot = WalkerUtil.getSemanticRoot(mathml);
        this.streeRoot = this.assembleTree(this.mmlRoot);
        this.stree = semantic_tree_1.SemanticTree.fromNode(this.streeRoot, this.mathml);
        this.xml = this.stree.xml();
        semantic_processor_1.default.getInstance().setNodeFactory(this.factory);
    }
    static addAttributes(snode, node, leaf) {
        if (leaf &&
            node.childNodes.length === 1 &&
            node.childNodes[0].nodeType !== DomUtil.NodeType.TEXT_NODE) {
            SemanticUtil.addAttributes(snode, node.childNodes[0]);
        }
        SemanticUtil.addAttributes(snode, node);
    }
    static textContent(snode, node, ignore) {
        if (!ignore && node.textContent) {
            snode.textContent = node.textContent;
            return;
        }
        const operator = WalkerUtil.splitAttribute(WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.OPERATOR));
        if (operator.length > 1) {
            snode.textContent = operator[1];
        }
    }
    static isPunctuated(collapsed) {
        return (!semantic_skeleton_1.SemanticSkeleton.simpleCollapseStructure(collapsed) &&
            collapsed[1] &&
            semantic_skeleton_1.SemanticSkeleton.contentCollapseStructure(collapsed[1]));
    }
    getTree() {
        return this.stree;
    }
    assembleTree(node) {
        const snode = this.makeNode(node);
        const children = WalkerUtil.splitAttribute(WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.CHILDREN));
        const content = WalkerUtil.splitAttribute(WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.CONTENT));
        RebuildStree.addAttributes(snode, node, !(children.length || content.length));
        if (content.length === 0 && children.length === 0) {
            RebuildStree.textContent(snode, node);
            return snode;
        }
        if (content.length > 0) {
            const fcontent = WalkerUtil.getBySemanticId(this.mathml, content[0]);
            if (fcontent) {
                RebuildStree.textContent(snode, fcontent, true);
            }
        }
        snode.contentNodes = content.map((id) => this.setParent(id, snode));
        snode.childNodes = children.map((id) => this.setParent(id, snode));
        const collapsed = WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.COLLAPSED);
        return collapsed ? this.postProcess(snode, collapsed) : snode;
    }
    makeNode(node) {
        const type = WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.TYPE);
        const role = WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.ROLE);
        const font = WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.FONT);
        const annotation = WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.ANNOTATION) || '';
        const id = WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.ID);
        const embellished = WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.EMBELLISHED);
        const fencepointer = WalkerUtil.getAttribute(node, enrich_attr_1.Attribute.FENCEPOINTER);
        const snode = this.createNode(parseInt(id, 10));
        snode.type = type;
        snode.role = role;
        snode.font = font ? font : "unknown";
        snode.parseAnnotation(annotation);
        if (fencepointer) {
            snode.fencePointer = fencepointer;
        }
        if (embellished) {
            snode.embellished = embellished;
        }
        return snode;
    }
    makePunctuation(id) {
        const node = this.createNode(id);
        node.updateContent((0, semantic_attr_1.invisibleComma)());
        node.role = "dummy";
        return node;
    }
    makePunctuated(snode, collapsed, role) {
        const punctuated = this.createNode(collapsed[0]);
        punctuated.type = "punctuated";
        punctuated.embellished = snode.embellished;
        punctuated.fencePointer = snode.fencePointer;
        punctuated.role = role;
        const cont = collapsed.splice(1, 1)[0].slice(1);
        punctuated.contentNodes = cont.map(this.makePunctuation.bind(this));
        this.collapsedChildren_(collapsed);
    }
    makeEmpty(snode, collapsed, role) {
        const empty = this.createNode(collapsed);
        empty.type = "empty";
        empty.embellished = snode.embellished;
        empty.fencePointer = snode.fencePointer;
        empty.role = role;
    }
    makeIndex(snode, collapsed, role) {
        if (RebuildStree.isPunctuated(collapsed)) {
            this.makePunctuated(snode, collapsed, role);
            collapsed = collapsed[0];
            return;
        }
        if (semantic_skeleton_1.SemanticSkeleton.simpleCollapseStructure(collapsed) &&
            !this.nodeDict[collapsed.toString()]) {
            this.makeEmpty(snode, collapsed, role);
        }
    }
    postProcess(snode, collapsed) {
        const array = semantic_skeleton_1.SemanticSkeleton.fromString(collapsed).array;
        if (snode.type === "subsup") {
            const subscript = this.createNode(array[1][0]);
            subscript.type = "subscript";
            subscript.role = "subsup";
            snode.type = "superscript";
            subscript.embellished = snode.embellished;
            subscript.fencePointer = snode.fencePointer;
            this.makeIndex(snode, array[1][2], "rightsub");
            this.makeIndex(snode, array[2], "rightsuper");
            this.collapsedChildren_(array);
            return snode;
        }
        if (snode.type === "subscript") {
            this.makeIndex(snode, array[2], "rightsub");
            this.collapsedChildren_(array);
            return snode;
        }
        if (snode.type === "superscript") {
            this.makeIndex(snode, array[2], "rightsuper");
            this.collapsedChildren_(array);
            return snode;
        }
        if (snode.type === "tensor") {
            this.makeIndex(snode, array[2], "leftsub");
            this.makeIndex(snode, array[3], "leftsuper");
            this.makeIndex(snode, array[4], "rightsub");
            this.makeIndex(snode, array[5], "rightsuper");
            this.collapsedChildren_(array);
            return snode;
        }
        if (snode.type === "punctuated") {
            if (RebuildStree.isPunctuated(array)) {
                const cont = array.splice(1, 1)[0].slice(1);
                snode.contentNodes = cont.map(this.makePunctuation.bind(this));
            }
            return snode;
        }
        if (snode.type === "underover") {
            const score = this.createNode(array[1][0]);
            if (snode.childNodes[1].role === "overaccent") {
                score.type = "overscore";
                snode.type = "underscore";
            }
            else {
                score.type = "underscore";
                snode.type = "overscore";
            }
            score.role = "underover";
            score.embellished = snode.embellished;
            score.fencePointer = snode.fencePointer;
            this.collapsedChildren_(array);
            return snode;
        }
        return snode;
    }
    createNode(id) {
        const node = this.factory.makeNode(id);
        this.nodeDict[id.toString()] = node;
        return node;
    }
    collapsedChildren_(collapsed) {
        const recurseCollapsed = (coll) => {
            const parent = this.nodeDict[coll[0]];
            parent.childNodes = [];
            for (let j = 1, l = coll.length; j < l; j++) {
                const id = coll[j];
                parent.childNodes.push(semantic_skeleton_1.SemanticSkeleton.simpleCollapseStructure(id)
                    ? this.nodeDict[id]
                    : recurseCollapsed(id));
            }
            return parent;
        };
        recurseCollapsed(collapsed);
    }
    setParent(id, snode) {
        const mml = WalkerUtil.getBySemanticId(this.mathml, id);
        const sn = this.assembleTree(mml);
        sn.parent = snode;
        return sn;
    }
}
exports.RebuildStree = RebuildStree;


/***/ }),

/***/ 1937:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SemanticWalker = void 0;
const abstract_walker_1 = __webpack_require__(4660);
const levels_1 = __webpack_require__(1497);
class SemanticWalker extends abstract_walker_1.AbstractWalker {
    constructor(node, generator, highlighter, xml) {
        super(node, generator, highlighter, xml);
        this.node = node;
        this.generator = generator;
        this.highlighter = highlighter;
        this.levels = null;
        this.restoreState();
    }
    initLevels() {
        const levels = new levels_1.Levels();
        levels.push([this.getFocus()]);
        return levels;
    }
    up() {
        super.up();
        const parent = this.previousLevel();
        if (!parent) {
            return null;
        }
        this.levels.pop();
        const found = this.levels.find(function (focus) {
            return focus.getSemanticNodes().some(function (node) {
                return node.id.toString() === parent;
            });
        });
        return found;
    }
    down() {
        super.down();
        const children = this.nextLevel();
        if (children.length === 0) {
            return null;
        }
        this.levels.push(children);
        return children[0];
    }
    combineContentChildren(type, role, content, children) {
        switch (type) {
            case "relseq":
            case "infixop":
            case "multirel":
                return this.makePairList(children, content);
            case "prefixop":
                return [this.focusFromId(children[0], content.concat(children))];
            case "postfixop":
                return [this.focusFromId(children[0], children.concat(content))];
            case "matrix":
            case "vector":
            case "fenced":
                return [
                    this.focusFromId(children[0], [content[0], children[0], content[1]])
                ];
            case "cases":
                return [this.focusFromId(children[0], [content[0], children[0]])];
            case "punctuated":
                if (role === "text") {
                    return children.map(this.singletonFocus.bind(this));
                }
                if (children.length === content.length) {
                    return content.map(this.singletonFocus.bind(this));
                }
                return this.combinePunctuations(children, content, [], []);
            case "appl":
                return [
                    this.focusFromId(children[0], [children[0], content[0]]),
                    this.singletonFocus(children[1])
                ];
            case "root":
                return [
                    this.singletonFocus(children[1]),
                    this.singletonFocus(children[0])
                ];
            default:
                return children.map(this.singletonFocus.bind(this));
        }
    }
    combinePunctuations(children, content, prepunct, acc) {
        if (children.length === 0) {
            return acc;
        }
        const child = children.shift();
        const cont = content.shift();
        if (child === cont) {
            prepunct.push(cont);
            return this.combinePunctuations(children, content, prepunct, acc);
        }
        else {
            content.unshift(cont);
            prepunct.push(child);
            if (children.length === content.length) {
                acc.push(this.focusFromId(child, prepunct.concat(content)));
                return acc;
            }
            else {
                acc.push(this.focusFromId(child, prepunct));
                return this.combinePunctuations(children, content, [], acc);
            }
        }
    }
    makePairList(children, content) {
        if (children.length === 0) {
            return [];
        }
        if (children.length === 1) {
            return [this.singletonFocus(children[0])];
        }
        const result = [this.singletonFocus(children.shift())];
        for (let i = 0, l = children.length; i < l; i++) {
            result.push(this.focusFromId(children[i], [content[i], children[i]]));
        }
        return result;
    }
    left() {
        super.left();
        const index = this.levels.indexOf(this.getFocus());
        if (index === null) {
            return null;
        }
        const ids = this.levels.get(index - 1);
        return ids ? ids : null;
    }
    right() {
        super.right();
        const index = this.levels.indexOf(this.getFocus());
        if (index === null) {
            return null;
        }
        const ids = this.levels.get(index + 1);
        return ids ? ids : null;
    }
    findFocusOnLevel(id) {
        const focus = this.levels.find((x) => {
            const pid = x.getSemanticPrimary().id;
            return pid === id;
        });
        return focus;
    }
}
exports.SemanticWalker = SemanticWalker;


/***/ }),

/***/ 3531:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.SyntaxWalker = void 0;
const base_util_1 = __webpack_require__(1426);
const abstract_walker_1 = __webpack_require__(4660);
const levels_1 = __webpack_require__(1497);
class SyntaxWalker extends abstract_walker_1.AbstractWalker {
    constructor(node, generator, highlighter, xml) {
        super(node, generator, highlighter, xml);
        this.node = node;
        this.generator = generator;
        this.highlighter = highlighter;
        this.levels = null;
        this.restoreState();
    }
    initLevels() {
        const levels = new levels_1.Levels();
        levels.push([this.primaryId()]);
        return levels;
    }
    up() {
        super.up();
        const parent = this.previousLevel();
        if (!parent) {
            return null;
        }
        this.levels.pop();
        return this.singletonFocus(parent);
    }
    down() {
        super.down();
        const children = this.nextLevel();
        if (children.length === 0) {
            return null;
        }
        const focus = this.singletonFocus(children[0]);
        if (focus) {
            this.levels.push(children);
        }
        return focus;
    }
    combineContentChildren(type, role, content, children) {
        switch (type) {
            case "relseq":
            case "infixop":
            case "multirel":
                return (0, base_util_1.interleaveLists)(children, content);
            case "prefixop":
                return content.concat(children);
            case "postfixop":
                return children.concat(content);
            case "matrix":
            case "vector":
            case "fenced":
                children.unshift(content[0]);
                children.push(content[1]);
                return children;
            case "cases":
                children.unshift(content[0]);
                return children;
            case "punctuated":
                if (role === "text") {
                    return (0, base_util_1.interleaveLists)(children, content);
                }
                return children;
            case "appl":
                return [children[0], content[0], children[1]];
            case "root":
                return [children[1], children[0]];
            default:
                return children;
        }
    }
    left() {
        super.left();
        const index = this.levels.indexOf(this.primaryId());
        if (index === null) {
            return null;
        }
        const id = this.levels.get(index - 1);
        return id ? this.singletonFocus(id) : null;
    }
    right() {
        super.right();
        const index = this.levels.indexOf(this.primaryId());
        if (index === null) {
            return null;
        }
        const id = this.levels.get(index + 1);
        return id ? this.singletonFocus(id) : null;
    }
    findFocusOnLevel(id) {
        return this.singletonFocus(id.toString());
    }
    focusDomNodes() {
        return [this.getFocus().getDomPrimary()];
    }
    focusSemanticNodes() {
        return [this.getFocus().getSemanticPrimary()];
    }
}
exports.SyntaxWalker = SyntaxWalker;


/***/ }),

/***/ 4051:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TableWalker = void 0;
const DomUtil = __webpack_require__(6671);
const event_util_1 = __webpack_require__(6988);
const syntax_walker_1 = __webpack_require__(3531);
const walker_1 = __webpack_require__(8119);
class TableWalker extends syntax_walker_1.SyntaxWalker {
    constructor(node, generator, highlighter, xml) {
        super(node, generator, highlighter, xml);
        this.node = node;
        this.generator = generator;
        this.highlighter = highlighter;
        this.firstJump = null;
        this.key_ = null;
        this.row_ = 0;
        this.currentTable_ = null;
        this.keyMapping.set(event_util_1.KeyCode.ZERO, this.jumpCell.bind(this));
        this.keyMapping.set(event_util_1.KeyCode.ONE, this.jumpCell.bind(this));
        this.keyMapping.set(event_util_1.KeyCode.TWO, this.jumpCell.bind(this));
        this.keyMapping.set(event_util_1.KeyCode.THREE, this.jumpCell.bind(this));
        this.keyMapping.set(event_util_1.KeyCode.FOUR, this.jumpCell.bind(this));
        this.keyMapping.set(event_util_1.KeyCode.FIVE, this.jumpCell.bind(this));
        this.keyMapping.set(event_util_1.KeyCode.SIX, this.jumpCell.bind(this));
        this.keyMapping.set(event_util_1.KeyCode.SEVEN, this.jumpCell.bind(this));
        this.keyMapping.set(event_util_1.KeyCode.EIGHT, this.jumpCell.bind(this));
        this.keyMapping.set(event_util_1.KeyCode.NINE, this.jumpCell.bind(this));
    }
    move(key) {
        this.key_ = key;
        const result = super.move(key);
        this.modifier = false;
        return result;
    }
    up() {
        this.moved = walker_1.WalkerMoves.UP;
        return this.eligibleCell_() ? this.verticalMove_(false) : super.up();
    }
    down() {
        this.moved = walker_1.WalkerMoves.DOWN;
        return this.eligibleCell_() ? this.verticalMove_(true) : super.down();
    }
    jumpCell() {
        if (!this.isInTable_() || this.key_ === null) {
            return this.getFocus();
        }
        if (this.moved === walker_1.WalkerMoves.ROW) {
            this.moved = walker_1.WalkerMoves.CELL;
            const column = this.key_ - event_util_1.KeyCode.ZERO;
            if (!this.isLegalJump_(this.row_, column)) {
                return this.getFocus();
            }
            return this.jumpCell_(this.row_, column);
        }
        const row = this.key_ - event_util_1.KeyCode.ZERO;
        if (row > this.currentTable_.childNodes.length) {
            return this.getFocus();
        }
        this.row_ = row;
        this.moved = walker_1.WalkerMoves.ROW;
        return this.getFocus().clone();
    }
    undo() {
        const focus = super.undo();
        if (focus === this.firstJump) {
            this.firstJump = null;
        }
        return focus;
    }
    eligibleCell_() {
        const primary = this.getFocus().getSemanticPrimary();
        return (this.modifier &&
            primary.type === "cell" &&
            TableWalker.ELIGIBLE_CELL_ROLES.indexOf(primary.role) !== -1);
    }
    verticalMove_(direction) {
        const parent = this.previousLevel();
        if (!parent) {
            return null;
        }
        const origFocus = this.getFocus();
        const origIndex = this.levels.indexOf(this.primaryId());
        const origLevel = this.levels.pop();
        const parentIndex = this.levels.indexOf(parent);
        const row = this.levels.get(direction ? parentIndex + 1 : parentIndex - 1);
        if (!row) {
            this.levels.push(origLevel);
            return null;
        }
        this.setFocus(this.singletonFocus(row));
        const children = this.nextLevel();
        const newNode = children[origIndex];
        if (!newNode) {
            this.setFocus(origFocus);
            this.levels.push(origLevel);
            return null;
        }
        this.levels.push(children);
        return this.singletonFocus(children[origIndex]);
    }
    jumpCell_(row, column) {
        if (!this.firstJump) {
            this.firstJump = this.getFocus();
            this.virtualize(true);
        }
        else {
            this.virtualize(false);
        }
        const id = this.currentTable_.id.toString();
        let level;
        do {
            level = this.levels.pop();
        } while (level.indexOf(id) === -1);
        this.levels.push(level);
        this.setFocus(this.singletonFocus(id));
        this.levels.push(this.nextLevel());
        const semRow = this.currentTable_.childNodes[row - 1];
        this.setFocus(this.singletonFocus(semRow.id.toString()));
        this.levels.push(this.nextLevel());
        return this.singletonFocus(semRow.childNodes[column - 1].id.toString());
    }
    isLegalJump_(row, column) {
        const xmlTable = DomUtil.querySelectorAllByAttrValue(this.getRebuilt().xml, 'id', this.currentTable_.id.toString())[0];
        if (!xmlTable || xmlTable.hasAttribute('alternative')) {
            return false;
        }
        const rowNode = this.currentTable_.childNodes[row - 1];
        if (!rowNode) {
            return false;
        }
        const xmlRow = DomUtil.querySelectorAllByAttrValue(xmlTable, 'id', rowNode.id.toString())[0];
        if (!xmlRow || xmlRow.hasAttribute('alternative')) {
            return false;
        }
        return !!(rowNode && rowNode.childNodes[column - 1]);
    }
    isInTable_() {
        let snode = this.getFocus().getSemanticPrimary();
        while (snode) {
            if (TableWalker.ELIGIBLE_TABLE_TYPES.indexOf(snode.type) !== -1) {
                this.currentTable_ = snode;
                return true;
            }
            snode = snode.parent;
        }
        return false;
    }
}
exports.TableWalker = TableWalker;
TableWalker.ELIGIBLE_CELL_ROLES = [
    "determinant",
    "rowvector",
    "binomial",
    "squarematrix",
    "multiline",
    "matrix",
    "vector",
    "cases",
    "table"
];
TableWalker.ELIGIBLE_TABLE_TYPES = [
    "multiline",
    "matrix",
    "vector",
    "cases",
    "table"
];


/***/ }),

/***/ 8119:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.WalkerState = exports.WalkerMoves = void 0;
var WalkerMoves;
(function (WalkerMoves) {
    WalkerMoves["UP"] = "up";
    WalkerMoves["DOWN"] = "down";
    WalkerMoves["LEFT"] = "left";
    WalkerMoves["RIGHT"] = "right";
    WalkerMoves["REPEAT"] = "repeat";
    WalkerMoves["DEPTH"] = "depth";
    WalkerMoves["ENTER"] = "enter";
    WalkerMoves["EXPAND"] = "expand";
    WalkerMoves["HOME"] = "home";
    WalkerMoves["SUMMARY"] = "summary";
    WalkerMoves["DETAIL"] = "detail";
    WalkerMoves["ROW"] = "row";
    WalkerMoves["CELL"] = "cell";
})(WalkerMoves = exports.WalkerMoves || (exports.WalkerMoves = {}));
class WalkerState {
    static resetState(id) {
        delete WalkerState.STATE[id];
    }
    static setState(id, value) {
        WalkerState.STATE[id] = value;
    }
    static getState(id) {
        return WalkerState.STATE[id];
    }
}
exports.WalkerState = WalkerState;
WalkerState.STATE = {};


/***/ }),

/***/ 907:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.walkerMapping_ = exports.walker = void 0;
const dummy_walker_1 = __webpack_require__(4296);
const semantic_walker_1 = __webpack_require__(1937);
const syntax_walker_1 = __webpack_require__(3531);
const table_walker_1 = __webpack_require__(4051);
function walker(type, node, generator, highlighter, xml) {
    const constructor = exports.walkerMapping_[type.toLowerCase()] || exports.walkerMapping_['dummy'];
    return constructor(node, generator, highlighter, xml);
}
exports.walker = walker;
exports.walkerMapping_ = {
    dummy: (p1, p2, p3, p4) => new dummy_walker_1.DummyWalker(p1, p2, p3, p4),
    semantic: (p1, p2, p3, p4) => new semantic_walker_1.SemanticWalker(p1, p2, p3, p4),
    syntax: (p1, p2, p3, p4) => new syntax_walker_1.SyntaxWalker(p1, p2, p3, p4),
    table: (p1, p2, p3, p4) => new table_walker_1.TableWalker(p1, p2, p3, p4)
};


/***/ }),

/***/ 8835:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.getBySemanticId = exports.getSemanticRoot = exports.getAttribute = exports.splitAttribute = void 0;
const DomUtil = __webpack_require__(6671);
const enrich_attr_1 = __webpack_require__(8171);
function splitAttribute(attr) {
    return !attr ? [] : attr.split(/,/);
}
exports.splitAttribute = splitAttribute;
function getAttribute(node, attr) {
    return node.getAttribute(attr);
}
exports.getAttribute = getAttribute;
function getSemanticRoot(node) {
    if (node.hasAttribute(enrich_attr_1.Attribute.TYPE) &&
        !node.hasAttribute(enrich_attr_1.Attribute.PARENT)) {
        return node;
    }
    const semanticNodes = DomUtil.querySelectorAllByAttr(node, enrich_attr_1.Attribute.TYPE);
    for (let i = 0, semanticNode; (semanticNode = semanticNodes[i]); i++) {
        if (!semanticNode.hasAttribute(enrich_attr_1.Attribute.PARENT)) {
            return semanticNode;
        }
    }
    return node;
}
exports.getSemanticRoot = getSemanticRoot;
function getBySemanticId(root, id) {
    if (root.getAttribute(enrich_attr_1.Attribute.ID) === id) {
        return root;
    }
    return DomUtil.querySelectorAllByAttrValue(root, enrich_attr_1.Attribute.ID, id)[0];
}
exports.getBySemanticId = getBySemanticId;


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
/******/ 	/* webpack/runtime/global */
/******/ 	!function() {
/******/ 		__webpack_require__.g = (function() {
/******/ 			if (typeof globalThis === 'object') return globalThis;
/******/ 			try {
/******/ 				return this || new Function('return this')();
/******/ 			} catch (e) {
/******/ 				if (typeof window === 'object') return window;
/******/ 			}
/******/ 		})();
/******/ 	}();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	!function() {
/******/ 		__webpack_require__.o = function(obj, prop) { return Object.prototype.hasOwnProperty.call(obj, prop); }
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
// EXTERNAL MODULE: ../../../../js/a11y/sre.js
var sre = __webpack_require__(8905);
var sre_default = /*#__PURE__*/__webpack_require__.n(sre);
;// CONCATENATED MODULE: ./lib/sre.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('a11y/sre', version/* VERSION */.q, 'a11y');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    a11y: {
      sre: sre
    }
  }
});
// EXTERNAL MODULE: ../../startup/lib/components/package.js
var components_package = __webpack_require__(1993);
;// CONCATENATED MODULE: ./sre_config.js

 // This sets up the correct link to the mathmaps files.

if (MathJax.startup) {
  var path = components_package/* Package.resolvePath */.GL.resolvePath('[sre]', false);

  if (typeof window !== 'undefined') {
    window.SREfeature = {
      json: path
    };
  } else {
    // In Node get the absolute path to the mathmaps directory.
    try {
      path = MathJax.config.loader.require.resolve(path + '/base.json').replace(/\/base\.json$/, '');
    } catch (_err) {}

    __webpack_require__.g.SREfeature = {
      json: path
    };
  }
}
;// CONCATENATED MODULE: ./sre.js




if (MathJax.startup) {
  (typeof window !== 'undefined' ? window : __webpack_require__.g).SREfeature.custom = function (loc) {
    return sre_default().preloadLocales(loc);
  };
}
}();
/******/ })()
;