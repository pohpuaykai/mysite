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

/***/ 205:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TeX = void 0;
var InputJax_js_1 = __webpack_require__(309);
var Options_js_1 = __webpack_require__(77);
var FindTeX_js_1 = __webpack_require__(982);
var FilterUtil_js_1 = __importDefault(__webpack_require__(199));
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var TexParser_js_1 = __importDefault(__webpack_require__(810));
var TexError_js_1 = __importDefault(__webpack_require__(466));
var ParseOptions_js_1 = __importDefault(__webpack_require__(394));
var Tags_js_1 = __webpack_require__(251);
var Configuration_js_1 = __webpack_require__(552);
__webpack_require__(606);
var TeX = (function (_super) {
    __extends(TeX, _super);
    function TeX(options) {
        if (options === void 0) { options = {}; }
        var _this = this;
        var _a = __read((0, Options_js_1.separateOptions)(options, TeX.OPTIONS, FindTeX_js_1.FindTeX.OPTIONS), 3), rest = _a[0], tex = _a[1], find = _a[2];
        _this = _super.call(this, tex) || this;
        _this.findTeX = _this.options['FindTeX'] || new FindTeX_js_1.FindTeX(find);
        var packages = _this.options.packages;
        var configuration = _this.configuration = TeX.configure(packages);
        var parseOptions = _this._parseOptions =
            new ParseOptions_js_1.default(configuration, [_this.options, Tags_js_1.TagsFactory.OPTIONS]);
        (0, Options_js_1.userOptions)(parseOptions.options, rest);
        configuration.config(_this);
        TeX.tags(parseOptions, configuration);
        _this.postFilters.add(FilterUtil_js_1.default.cleanSubSup, -6);
        _this.postFilters.add(FilterUtil_js_1.default.setInherited, -5);
        _this.postFilters.add(FilterUtil_js_1.default.moveLimits, -4);
        _this.postFilters.add(FilterUtil_js_1.default.cleanStretchy, -3);
        _this.postFilters.add(FilterUtil_js_1.default.cleanAttributes, -2);
        _this.postFilters.add(FilterUtil_js_1.default.combineRelations, -1);
        return _this;
    }
    TeX.configure = function (packages) {
        var configuration = new Configuration_js_1.ParserConfiguration(packages, ['tex']);
        configuration.init();
        return configuration;
    };
    TeX.tags = function (options, configuration) {
        Tags_js_1.TagsFactory.addTags(configuration.tags);
        Tags_js_1.TagsFactory.setDefault(options.options.tags);
        options.tags = Tags_js_1.TagsFactory.getDefault();
        options.tags.configuration = options;
    };
    TeX.prototype.setMmlFactory = function (mmlFactory) {
        _super.prototype.setMmlFactory.call(this, mmlFactory);
        this._parseOptions.nodeFactory.setMmlFactory(mmlFactory);
    };
    Object.defineProperty(TeX.prototype, "parseOptions", {
        get: function () {
            return this._parseOptions;
        },
        enumerable: false,
        configurable: true
    });
    TeX.prototype.reset = function (tag) {
        if (tag === void 0) { tag = 0; }
        this.parseOptions.tags.reset(tag);
    };
    TeX.prototype.compile = function (math, document) {
        this.parseOptions.clear();
        this.executeFilters(this.preFilters, math, document, this.parseOptions);
        var display = math.display;
        this.latex = math.math;
        var node;
        this.parseOptions.tags.startEquation(math);
        var globalEnv;
        try {
            var parser = new TexParser_js_1.default(this.latex, { display: display, isInner: false }, this.parseOptions);
            node = parser.mml();
            globalEnv = parser.stack.global;
        }
        catch (err) {
            if (!(err instanceof TexError_js_1.default)) {
                throw err;
            }
            this.parseOptions.error = true;
            node = this.options.formatError(this, err);
        }
        node = this.parseOptions.nodeFactory.create('node', 'math', [node]);
        if (globalEnv === null || globalEnv === void 0 ? void 0 : globalEnv.indentalign) {
            NodeUtil_js_1.default.setAttribute(node, 'indentalign', globalEnv.indentalign);
        }
        if (display) {
            NodeUtil_js_1.default.setAttribute(node, 'display', 'block');
        }
        this.parseOptions.tags.finishEquation(math);
        this.parseOptions.root = node;
        this.executeFilters(this.postFilters, math, document, this.parseOptions);
        this.mathNode = this.parseOptions.root;
        return this.mathNode;
    };
    TeX.prototype.findMath = function (strings) {
        return this.findTeX.findMath(strings);
    };
    TeX.prototype.formatError = function (err) {
        var message = err.message.replace(/\n.*/, '');
        return this.parseOptions.nodeFactory.create('error', message, err.id, this.latex);
    };
    TeX.NAME = 'TeX';
    TeX.OPTIONS = __assign(__assign({}, InputJax_js_1.AbstractInputJax.OPTIONS), { FindTeX: null, packages: ['base'], digits: /^(?:[0-9]+(?:\{,\}[0-9]{3})*(?:\.[0-9]*)?|\.[0-9]+)/, maxBuffer: 5 * 1024, formatError: function (jax, err) { return jax.formatError(err); } });
    return TeX;
}(InputJax_js_1.AbstractInputJax));
exports.TeX = TeX;
//# sourceMappingURL=tex.js.map

/***/ }),

/***/ 552:
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
exports.ParserConfiguration = exports.ConfigurationHandler = exports.Configuration = void 0;
var Options_js_1 = __webpack_require__(77);
var MapHandler_js_1 = __webpack_require__(910);
var FunctionList_js_1 = __webpack_require__(898);
var PrioritizedList_js_1 = __webpack_require__(297);
var Tags_js_1 = __webpack_require__(251);
var Configuration = (function () {
    function Configuration(name, handler, fallback, items, tags, options, nodes, preprocessors, postprocessors, initMethod, configMethod, priority, parser) {
        if (handler === void 0) { handler = {}; }
        if (fallback === void 0) { fallback = {}; }
        if (items === void 0) { items = {}; }
        if (tags === void 0) { tags = {}; }
        if (options === void 0) { options = {}; }
        if (nodes === void 0) { nodes = {}; }
        if (preprocessors === void 0) { preprocessors = []; }
        if (postprocessors === void 0) { postprocessors = []; }
        if (initMethod === void 0) { initMethod = null; }
        if (configMethod === void 0) { configMethod = null; }
        this.name = name;
        this.handler = handler;
        this.fallback = fallback;
        this.items = items;
        this.tags = tags;
        this.options = options;
        this.nodes = nodes;
        this.preprocessors = preprocessors;
        this.postprocessors = postprocessors;
        this.initMethod = initMethod;
        this.configMethod = configMethod;
        this.priority = priority;
        this.parser = parser;
        this.handler = Object.assign({ character: [], delimiter: [], macro: [], environment: [] }, handler);
    }
    Configuration.makeProcessor = function (func, priority) {
        return Array.isArray(func) ? func : [func, priority];
    };
    Configuration._create = function (name, config) {
        var _this = this;
        if (config === void 0) { config = {}; }
        var priority = config.priority || PrioritizedList_js_1.PrioritizedList.DEFAULTPRIORITY;
        var init = config.init ? this.makeProcessor(config.init, priority) : null;
        var conf = config.config ? this.makeProcessor(config.config, priority) : null;
        var preprocessors = (config.preprocessors || []).map(function (pre) { return _this.makeProcessor(pre, priority); });
        var postprocessors = (config.postprocessors || []).map(function (post) { return _this.makeProcessor(post, priority); });
        var parser = config.parser || 'tex';
        return new Configuration(name, config.handler || {}, config.fallback || {}, config.items || {}, config.tags || {}, config.options || {}, config.nodes || {}, preprocessors, postprocessors, init, conf, priority, parser);
    };
    Configuration.create = function (name, config) {
        if (config === void 0) { config = {}; }
        var configuration = Configuration._create(name, config);
        ConfigurationHandler.set(name, configuration);
        return configuration;
    };
    Configuration.local = function (config) {
        if (config === void 0) { config = {}; }
        return Configuration._create('', config);
    };
    Object.defineProperty(Configuration.prototype, "init", {
        get: function () {
            return this.initMethod ? this.initMethod[0] : null;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Configuration.prototype, "config", {
        get: function () {
            return this.configMethod ? this.configMethod[0] : null;
        },
        enumerable: false,
        configurable: true
    });
    return Configuration;
}());
exports.Configuration = Configuration;
var ConfigurationHandler;
(function (ConfigurationHandler) {
    var maps = new Map();
    ConfigurationHandler.set = function (name, map) {
        maps.set(name, map);
    };
    ConfigurationHandler.get = function (name) {
        return maps.get(name);
    };
    ConfigurationHandler.keys = function () {
        return maps.keys();
    };
})(ConfigurationHandler = exports.ConfigurationHandler || (exports.ConfigurationHandler = {}));
var ParserConfiguration = (function () {
    function ParserConfiguration(packages, parsers) {
        var e_1, _a, e_2, _b;
        if (parsers === void 0) { parsers = ['tex']; }
        this.initMethod = new FunctionList_js_1.FunctionList();
        this.configMethod = new FunctionList_js_1.FunctionList();
        this.configurations = new PrioritizedList_js_1.PrioritizedList();
        this.parsers = [];
        this.handlers = new MapHandler_js_1.SubHandlers();
        this.items = {};
        this.tags = {};
        this.options = {};
        this.nodes = {};
        this.parsers = parsers;
        try {
            for (var _c = __values(packages.slice().reverse()), _d = _c.next(); !_d.done; _d = _c.next()) {
                var pkg = _d.value;
                this.addPackage(pkg);
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
            for (var _e = __values(this.configurations), _f = _e.next(); !_f.done; _f = _e.next()) {
                var _g = _f.value, config = _g.item, priority = _g.priority;
                this.append(config, priority);
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
    ParserConfiguration.prototype.init = function () {
        this.initMethod.execute(this);
    };
    ParserConfiguration.prototype.config = function (jax) {
        var e_3, _a;
        this.configMethod.execute(this, jax);
        try {
            for (var _b = __values(this.configurations), _c = _b.next(); !_c.done; _c = _b.next()) {
                var config = _c.value;
                this.addFilters(jax, config.item);
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
    ParserConfiguration.prototype.addPackage = function (pkg) {
        var name = typeof pkg === 'string' ? pkg : pkg[0];
        var conf = this.getPackage(name);
        conf && this.configurations.add(conf, typeof pkg === 'string' ? conf.priority : pkg[1]);
    };
    ParserConfiguration.prototype.add = function (name, jax, options) {
        var e_4, _a;
        if (options === void 0) { options = {}; }
        var config = this.getPackage(name);
        this.append(config);
        this.configurations.add(config, config.priority);
        this.init();
        var parser = jax.parseOptions;
        parser.nodeFactory.setCreators(config.nodes);
        try {
            for (var _b = __values(Object.keys(config.items)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var kind = _c.value;
                parser.itemFactory.setNodeClass(kind, config.items[kind]);
            }
        }
        catch (e_4_1) { e_4 = { error: e_4_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_4) throw e_4.error; }
        }
        Tags_js_1.TagsFactory.addTags(config.tags);
        (0, Options_js_1.defaultOptions)(parser.options, config.options);
        (0, Options_js_1.userOptions)(parser.options, options);
        this.addFilters(jax, config);
        if (config.config) {
            config.config(this, jax);
        }
    };
    ParserConfiguration.prototype.getPackage = function (name) {
        var config = ConfigurationHandler.get(name);
        if (config && this.parsers.indexOf(config.parser) < 0) {
            throw Error("Package ".concat(name, " doesn't target the proper parser"));
        }
        return config;
    };
    ParserConfiguration.prototype.append = function (config, priority) {
        priority = priority || config.priority;
        if (config.initMethod) {
            this.initMethod.add(config.initMethod[0], config.initMethod[1]);
        }
        if (config.configMethod) {
            this.configMethod.add(config.configMethod[0], config.configMethod[1]);
        }
        this.handlers.add(config.handler, config.fallback, priority);
        Object.assign(this.items, config.items);
        Object.assign(this.tags, config.tags);
        (0, Options_js_1.defaultOptions)(this.options, config.options);
        Object.assign(this.nodes, config.nodes);
    };
    ParserConfiguration.prototype.addFilters = function (jax, config) {
        var e_5, _a, e_6, _b;
        try {
            for (var _c = __values(config.preprocessors), _d = _c.next(); !_d.done; _d = _c.next()) {
                var _e = __read(_d.value, 2), pre = _e[0], priority = _e[1];
                jax.preFilters.add(pre, priority);
            }
        }
        catch (e_5_1) { e_5 = { error: e_5_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_5) throw e_5.error; }
        }
        try {
            for (var _f = __values(config.postprocessors), _g = _f.next(); !_g.done; _g = _f.next()) {
                var _h = __read(_g.value, 2), post = _h[0], priority = _h[1];
                jax.postFilters.add(post, priority);
            }
        }
        catch (e_6_1) { e_6 = { error: e_6_1 }; }
        finally {
            try {
                if (_g && !_g.done && (_b = _f.return)) _b.call(_f);
            }
            finally { if (e_6) throw e_6.error; }
        }
    };
    return ParserConfiguration;
}());
exports.ParserConfiguration = ParserConfiguration;
//# sourceMappingURL=Configuration.js.map

/***/ }),

/***/ 199:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
var MmlNode_js_1 = __webpack_require__(921);
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var FilterUtil;
(function (FilterUtil) {
    FilterUtil.cleanStretchy = function (arg) {
        var e_1, _a;
        var options = arg.data;
        try {
            for (var _b = __values(options.getList('fixStretchy')), _c = _b.next(); !_c.done; _c = _b.next()) {
                var mo = _c.value;
                if (NodeUtil_js_1.default.getProperty(mo, 'fixStretchy')) {
                    var symbol = NodeUtil_js_1.default.getForm(mo);
                    if (symbol && symbol[3] && symbol[3]['stretchy']) {
                        NodeUtil_js_1.default.setAttribute(mo, 'stretchy', false);
                    }
                    var parent_1 = mo.parent;
                    if (!NodeUtil_js_1.default.getTexClass(mo) && (!symbol || !symbol[2])) {
                        var texAtom = options.nodeFactory.create('node', 'TeXAtom', [mo]);
                        parent_1.replaceChild(texAtom, mo);
                        texAtom.inheritAttributesFrom(mo);
                    }
                    NodeUtil_js_1.default.removeProperties(mo, 'fixStretchy');
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
    FilterUtil.cleanAttributes = function (arg) {
        var node = arg.data.root;
        node.walkTree(function (mml, _d) {
            var e_2, _a;
            var attribs = mml.attributes;
            if (!attribs) {
                return;
            }
            var keep = new Set((attribs.get('mjx-keep-attrs') || '').split(/ /));
            delete (attribs.getAllAttributes())['mjx-keep-attrs'];
            try {
                for (var _b = __values(attribs.getExplicitNames()), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var key = _c.value;
                    if (!keep.has(key) && attribs.attributes[key] === mml.attributes.getInherited(key)) {
                        delete attribs.attributes[key];
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
        }, {});
    };
    FilterUtil.combineRelations = function (arg) {
        var e_3, _a, e_4, _b;
        var remove = [];
        try {
            for (var _c = __values(arg.data.getList('mo')), _e = _c.next(); !_e.done; _e = _c.next()) {
                var mo = _e.value;
                if (mo.getProperty('relationsCombined') || !mo.parent ||
                    (mo.parent && !NodeUtil_js_1.default.isType(mo.parent, 'mrow')) ||
                    NodeUtil_js_1.default.getTexClass(mo) !== MmlNode_js_1.TEXCLASS.REL) {
                    continue;
                }
                var mml = mo.parent;
                var m2 = void 0;
                var children = mml.childNodes;
                var next = children.indexOf(mo) + 1;
                var variantForm = NodeUtil_js_1.default.getProperty(mo, 'variantForm');
                while (next < children.length && (m2 = children[next]) &&
                    NodeUtil_js_1.default.isType(m2, 'mo') &&
                    NodeUtil_js_1.default.getTexClass(m2) === MmlNode_js_1.TEXCLASS.REL) {
                    if (variantForm === NodeUtil_js_1.default.getProperty(m2, 'variantForm') &&
                        _compareExplicit(mo, m2)) {
                        NodeUtil_js_1.default.appendChildren(mo, NodeUtil_js_1.default.getChildren(m2));
                        _copyExplicit(['stretchy', 'rspace'], mo, m2);
                        try {
                            for (var _f = (e_4 = void 0, __values(m2.getPropertyNames())), _g = _f.next(); !_g.done; _g = _f.next()) {
                                var name_1 = _g.value;
                                mo.setProperty(name_1, m2.getProperty(name_1));
                            }
                        }
                        catch (e_4_1) { e_4 = { error: e_4_1 }; }
                        finally {
                            try {
                                if (_g && !_g.done && (_b = _f.return)) _b.call(_f);
                            }
                            finally { if (e_4) throw e_4.error; }
                        }
                        children.splice(next, 1);
                        remove.push(m2);
                        m2.parent = null;
                        m2.setProperty('relationsCombined', true);
                    }
                    else {
                        if (mo.attributes.getExplicit('rspace') == null) {
                            NodeUtil_js_1.default.setAttribute(mo, 'rspace', '0pt');
                        }
                        if (m2.attributes.getExplicit('lspace') == null) {
                            NodeUtil_js_1.default.setAttribute(m2, 'lspace', '0pt');
                        }
                        break;
                    }
                }
                mo.attributes.setInherited('form', mo.getForms()[0]);
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (_e && !_e.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_3) throw e_3.error; }
        }
        arg.data.removeFromList('mo', remove);
    };
    var _copyExplicit = function (attrs, node1, node2) {
        var attr1 = node1.attributes;
        var attr2 = node2.attributes;
        attrs.forEach(function (x) {
            var attr = attr2.getExplicit(x);
            if (attr != null) {
                attr1.set(x, attr);
            }
        });
    };
    var _compareExplicit = function (node1, node2) {
        var e_5, _a;
        var filter = function (attr, space) {
            var exp = attr.getExplicitNames();
            return exp.filter(function (x) {
                return x !== space &&
                    (x !== 'stretchy' ||
                        attr.getExplicit('stretchy'));
            });
        };
        var attr1 = node1.attributes;
        var attr2 = node2.attributes;
        var exp1 = filter(attr1, 'lspace');
        var exp2 = filter(attr2, 'rspace');
        if (exp1.length !== exp2.length) {
            return false;
        }
        try {
            for (var exp1_1 = __values(exp1), exp1_1_1 = exp1_1.next(); !exp1_1_1.done; exp1_1_1 = exp1_1.next()) {
                var name_2 = exp1_1_1.value;
                if (attr1.getExplicit(name_2) !== attr2.getExplicit(name_2)) {
                    return false;
                }
            }
        }
        catch (e_5_1) { e_5 = { error: e_5_1 }; }
        finally {
            try {
                if (exp1_1_1 && !exp1_1_1.done && (_a = exp1_1.return)) _a.call(exp1_1);
            }
            finally { if (e_5) throw e_5.error; }
        }
        return true;
    };
    var _cleanSubSup = function (options, low, up) {
        var e_6, _a;
        var remove = [];
        try {
            for (var _b = __values(options.getList('m' + low + up)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var mml = _c.value;
                var children = mml.childNodes;
                if (children[mml[low]] && children[mml[up]]) {
                    continue;
                }
                var parent_2 = mml.parent;
                var newNode = (children[mml[low]] ?
                    options.nodeFactory.create('node', 'm' + low, [children[mml.base], children[mml[low]]]) :
                    options.nodeFactory.create('node', 'm' + up, [children[mml.base], children[mml[up]]]));
                NodeUtil_js_1.default.copyAttributes(mml, newNode);
                if (parent_2) {
                    parent_2.replaceChild(newNode, mml);
                }
                else {
                    options.root = newNode;
                }
                remove.push(mml);
            }
        }
        catch (e_6_1) { e_6 = { error: e_6_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_6) throw e_6.error; }
        }
        options.removeFromList('m' + low + up, remove);
    };
    FilterUtil.cleanSubSup = function (arg) {
        var options = arg.data;
        if (options.error) {
            return;
        }
        _cleanSubSup(options, 'sub', 'sup');
        _cleanSubSup(options, 'under', 'over');
    };
    var _moveLimits = function (options, underover, subsup) {
        var e_7, _a;
        var remove = [];
        try {
            for (var _b = __values(options.getList(underover)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var mml = _c.value;
                if (mml.attributes.get('displaystyle')) {
                    continue;
                }
                var base = mml.childNodes[mml.base];
                var mo = base.coreMO();
                if (base.getProperty('movablelimits') && !mo.attributes.getExplicit('movablelimits')) {
                    var node = options.nodeFactory.create('node', subsup, mml.childNodes);
                    NodeUtil_js_1.default.copyAttributes(mml, node);
                    if (mml.parent) {
                        mml.parent.replaceChild(node, mml);
                    }
                    else {
                        options.root = node;
                    }
                    remove.push(mml);
                }
            }
        }
        catch (e_7_1) { e_7 = { error: e_7_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_7) throw e_7.error; }
        }
        options.removeFromList(underover, remove);
    };
    FilterUtil.moveLimits = function (arg) {
        var options = arg.data;
        _moveLimits(options, 'munderover', 'msubsup');
        _moveLimits(options, 'munder', 'msub');
        _moveLimits(options, 'mover', 'msup');
    };
    FilterUtil.setInherited = function (arg) {
        arg.data.root.setInheritedAttributes({}, arg.math['display'], 0, false);
    };
})(FilterUtil || (FilterUtil = {}));
exports["default"] = FilterUtil;
//# sourceMappingURL=FilterUtil.js.map

/***/ }),

/***/ 982:
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
exports.FindTeX = void 0;
var FindMath_js_1 = __webpack_require__(649);
var string_js_1 = __webpack_require__(720);
var MathItem_js_1 = __webpack_require__(769);
var FindTeX = (function (_super) {
    __extends(FindTeX, _super);
    function FindTeX(options) {
        var _this = _super.call(this, options) || this;
        _this.getPatterns();
        return _this;
    }
    FindTeX.prototype.getPatterns = function () {
        var _this = this;
        var options = this.options;
        var starts = [], parts = [], subparts = [];
        this.end = {};
        this.env = this.sub = 0;
        var i = 1;
        options['inlineMath'].forEach(function (delims) { return _this.addPattern(starts, delims, false); });
        options['displayMath'].forEach(function (delims) { return _this.addPattern(starts, delims, true); });
        if (starts.length) {
            parts.push(starts.sort(string_js_1.sortLength).join('|'));
        }
        if (options['processEnvironments']) {
            parts.push('\\\\begin\\s*\\{([^}]*)\\}');
            this.env = i;
            i++;
        }
        if (options['processEscapes']) {
            subparts.push('\\\\([\\\\$])');
        }
        if (options['processRefs']) {
            subparts.push('(\\\\(?:eq)?ref\\s*\\{[^}]*\\})');
        }
        if (subparts.length) {
            parts.push('(' + subparts.join('|') + ')');
            this.sub = i;
        }
        this.start = new RegExp(parts.join('|'), 'g');
        this.hasPatterns = (parts.length > 0);
    };
    FindTeX.prototype.addPattern = function (starts, delims, display) {
        var _a = __read(delims, 2), open = _a[0], close = _a[1];
        starts.push((0, string_js_1.quotePattern)(open));
        this.end[open] = [close, display, this.endPattern(close)];
    };
    FindTeX.prototype.endPattern = function (end, endp) {
        return new RegExp((endp || (0, string_js_1.quotePattern)(end)) + '|\\\\(?:[a-zA-Z]|.)|[{}]', 'g');
    };
    FindTeX.prototype.findEnd = function (text, n, start, end) {
        var _a = __read(end, 3), close = _a[0], display = _a[1], pattern = _a[2];
        var i = pattern.lastIndex = start.index + start[0].length;
        var match, braces = 0;
        while ((match = pattern.exec(text))) {
            if ((match[1] || match[0]) === close && braces === 0) {
                return (0, MathItem_js_1.protoItem)(start[0], text.substr(i, match.index - i), match[0], n, start.index, match.index + match[0].length, display);
            }
            else if (match[0] === '{') {
                braces++;
            }
            else if (match[0] === '}' && braces) {
                braces--;
            }
        }
        return null;
    };
    FindTeX.prototype.findMathInString = function (math, n, text) {
        var start, match;
        this.start.lastIndex = 0;
        while ((start = this.start.exec(text))) {
            if (start[this.env] !== undefined && this.env) {
                var end = '\\\\end\\s*(\\{' + (0, string_js_1.quotePattern)(start[this.env]) + '\\})';
                match = this.findEnd(text, n, start, ['{' + start[this.env] + '}', true, this.endPattern(null, end)]);
                if (match) {
                    match.math = match.open + match.math + match.close;
                    match.open = match.close = '';
                }
            }
            else if (start[this.sub] !== undefined && this.sub) {
                var math_1 = start[this.sub];
                var end = start.index + start[this.sub].length;
                if (math_1.length === 2) {
                    match = (0, MathItem_js_1.protoItem)('', math_1.substr(1), '', n, start.index, end);
                }
                else {
                    match = (0, MathItem_js_1.protoItem)('', math_1, '', n, start.index, end, false);
                }
            }
            else {
                match = this.findEnd(text, n, start, this.end[start[0]]);
            }
            if (match) {
                math.push(match);
                this.start.lastIndex = match.end.n;
            }
        }
    };
    FindTeX.prototype.findMath = function (strings) {
        var math = [];
        if (this.hasPatterns) {
            for (var i = 0, m = strings.length; i < m; i++) {
                this.findMathInString(math, i, strings[i]);
            }
        }
        return math;
    };
    FindTeX.OPTIONS = {
        inlineMath: [
            ['\\(', '\\)']
        ],
        displayMath: [
            ['$$', '$$'],
            ['\\[', '\\]']
        ],
        processEscapes: true,
        processEnvironments: true,
        processRefs: true,
    };
    return FindTeX;
}(FindMath_js_1.AbstractFindMath));
exports.FindTeX = FindTeX;
//# sourceMappingURL=FindTeX.js.map

/***/ }),

/***/ 910:
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
exports.SubHandlers = exports.SubHandler = exports.MapHandler = void 0;
var PrioritizedList_js_1 = __webpack_require__(297);
var FunctionList_js_1 = __webpack_require__(898);
var MapHandler;
(function (MapHandler) {
    var maps = new Map();
    MapHandler.register = function (map) {
        maps.set(map.name, map);
    };
    MapHandler.getMap = function (name) {
        return maps.get(name);
    };
})(MapHandler = exports.MapHandler || (exports.MapHandler = {}));
var SubHandler = (function () {
    function SubHandler() {
        this._configuration = new PrioritizedList_js_1.PrioritizedList();
        this._fallback = new FunctionList_js_1.FunctionList();
    }
    SubHandler.prototype.add = function (maps, fallback, priority) {
        var e_1, _a;
        if (priority === void 0) { priority = PrioritizedList_js_1.PrioritizedList.DEFAULTPRIORITY; }
        try {
            for (var _b = __values(maps.slice().reverse()), _c = _b.next(); !_c.done; _c = _b.next()) {
                var name_1 = _c.value;
                var map = MapHandler.getMap(name_1);
                if (!map) {
                    this.warn('Configuration ' + name_1 + ' not found! Omitted.');
                    return;
                }
                this._configuration.add(map, priority);
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_1) throw e_1.error; }
        }
        if (fallback) {
            this._fallback.add(fallback, priority);
        }
    };
    SubHandler.prototype.parse = function (input) {
        var e_2, _a;
        try {
            for (var _b = __values(this._configuration), _c = _b.next(); !_c.done; _c = _b.next()) {
                var map = _c.value.item;
                var result = map.parse(input);
                if (result) {
                    return result;
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
        var _d = __read(input, 2), env = _d[0], symbol = _d[1];
        Array.from(this._fallback)[0].item(env, symbol);
    };
    SubHandler.prototype.lookup = function (symbol) {
        var map = this.applicable(symbol);
        return map ? map.lookup(symbol) : null;
    };
    SubHandler.prototype.contains = function (symbol) {
        return this.applicable(symbol) ? true : false;
    };
    SubHandler.prototype.toString = function () {
        var e_3, _a;
        var names = [];
        try {
            for (var _b = __values(this._configuration), _c = _b.next(); !_c.done; _c = _b.next()) {
                var map = _c.value.item;
                names.push(map.name);
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_3) throw e_3.error; }
        }
        return names.join(', ');
    };
    SubHandler.prototype.applicable = function (symbol) {
        var e_4, _a;
        try {
            for (var _b = __values(this._configuration), _c = _b.next(); !_c.done; _c = _b.next()) {
                var map = _c.value.item;
                if (map.contains(symbol)) {
                    return map;
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
        return null;
    };
    SubHandler.prototype.retrieve = function (name) {
        var e_5, _a;
        try {
            for (var _b = __values(this._configuration), _c = _b.next(); !_c.done; _c = _b.next()) {
                var map = _c.value.item;
                if (map.name === name) {
                    return map;
                }
            }
        }
        catch (e_5_1) { e_5 = { error: e_5_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_5) throw e_5.error; }
        }
        return null;
    };
    SubHandler.prototype.warn = function (message) {
        console.log('TexParser Warning: ' + message);
    };
    return SubHandler;
}());
exports.SubHandler = SubHandler;
var SubHandlers = (function () {
    function SubHandlers() {
        this.map = new Map();
    }
    SubHandlers.prototype.add = function (handlers, fallbacks, priority) {
        var e_6, _a;
        if (priority === void 0) { priority = PrioritizedList_js_1.PrioritizedList.DEFAULTPRIORITY; }
        try {
            for (var _b = __values(Object.keys(handlers)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var key = _c.value;
                var name_2 = key;
                var subHandler = this.get(name_2);
                if (!subHandler) {
                    subHandler = new SubHandler();
                    this.set(name_2, subHandler);
                }
                subHandler.add(handlers[name_2], fallbacks[name_2], priority);
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
    SubHandlers.prototype.set = function (name, subHandler) {
        this.map.set(name, subHandler);
    };
    SubHandlers.prototype.get = function (name) {
        return this.map.get(name);
    };
    SubHandlers.prototype.retrieve = function (name) {
        var e_7, _a;
        try {
            for (var _b = __values(this.map.values()), _c = _b.next(); !_c.done; _c = _b.next()) {
                var handler = _c.value;
                var map = handler.retrieve(name);
                if (map) {
                    return map;
                }
            }
        }
        catch (e_7_1) { e_7 = { error: e_7_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_7) throw e_7.error; }
        }
        return null;
    };
    SubHandlers.prototype.keys = function () {
        return this.map.keys();
    };
    return SubHandlers;
}());
exports.SubHandlers = SubHandlers;
//# sourceMappingURL=MapHandler.js.map

/***/ }),

/***/ 644:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.NodeFactory = void 0;
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var NodeFactory = (function () {
    function NodeFactory() {
        this.mmlFactory = null;
        this.factory = { 'node': NodeFactory.createNode,
            'token': NodeFactory.createToken,
            'text': NodeFactory.createText,
            'error': NodeFactory.createError
        };
    }
    NodeFactory.createNode = function (factory, kind, children, def, text) {
        if (children === void 0) { children = []; }
        if (def === void 0) { def = {}; }
        var node = factory.mmlFactory.create(kind);
        node.setChildren(children);
        if (text) {
            node.appendChild(text);
        }
        NodeUtil_js_1.default.setProperties(node, def);
        return node;
    };
    NodeFactory.createToken = function (factory, kind, def, text) {
        if (def === void 0) { def = {}; }
        if (text === void 0) { text = ''; }
        var textNode = factory.create('text', text);
        return factory.create('node', kind, [], def, textNode);
    };
    NodeFactory.createText = function (factory, text) {
        if (text == null) {
            return null;
        }
        return factory.mmlFactory.create('text').setText(text);
    };
    NodeFactory.createError = function (factory, message) {
        var text = factory.create('text', message);
        var mtext = factory.create('node', 'mtext', [], {}, text);
        var error = factory.create('node', 'merror', [mtext], { 'data-mjx-error': message });
        return error;
    };
    NodeFactory.prototype.setMmlFactory = function (mmlFactory) {
        this.mmlFactory = mmlFactory;
    };
    NodeFactory.prototype.set = function (kind, func) {
        this.factory[kind] = func;
    };
    NodeFactory.prototype.setCreators = function (maps) {
        for (var kind in maps) {
            this.set(kind, maps[kind]);
        }
    };
    NodeFactory.prototype.create = function (kind) {
        var rest = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            rest[_i - 1] = arguments[_i];
        }
        var func = this.factory[kind] || this.factory['node'];
        var node = func.apply(void 0, __spreadArray([this, rest[0]], __read(rest.slice(1)), false));
        if (kind === 'node') {
            this.configuration.addNode(rest[0], node);
        }
        return node;
    };
    NodeFactory.prototype.get = function (kind) {
        return this.factory[kind];
    };
    return NodeFactory;
}());
exports.NodeFactory = NodeFactory;
//# sourceMappingURL=NodeFactory.js.map

/***/ }),

/***/ 321:
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
var MmlNode_js_1 = __webpack_require__(921);
var mo_js_1 = __webpack_require__(946);
var NodeUtil;
(function (NodeUtil) {
    var attrs = new Map([
        ['autoOP', true],
        ['fnOP', true],
        ['movesupsub', true],
        ['subsupOK', true],
        ['texprimestyle', true],
        ['useHeight', true],
        ['variantForm', true],
        ['withDelims', true],
        ['mathaccent', true],
        ['open', true],
        ['close', true]
    ]);
    function createEntity(code) {
        return String.fromCodePoint(parseInt(code, 16));
    }
    NodeUtil.createEntity = createEntity;
    function getChildren(node) {
        return node.childNodes;
    }
    NodeUtil.getChildren = getChildren;
    function getText(node) {
        return node.getText();
    }
    NodeUtil.getText = getText;
    function appendChildren(node, children) {
        var e_1, _a;
        try {
            for (var children_1 = __values(children), children_1_1 = children_1.next(); !children_1_1.done; children_1_1 = children_1.next()) {
                var child = children_1_1.value;
                node.appendChild(child);
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (children_1_1 && !children_1_1.done && (_a = children_1.return)) _a.call(children_1);
            }
            finally { if (e_1) throw e_1.error; }
        }
    }
    NodeUtil.appendChildren = appendChildren;
    function setAttribute(node, attribute, value) {
        node.attributes.set(attribute, value);
    }
    NodeUtil.setAttribute = setAttribute;
    function setProperty(node, property, value) {
        node.setProperty(property, value);
    }
    NodeUtil.setProperty = setProperty;
    function setProperties(node, properties) {
        var e_2, _a;
        try {
            for (var _b = __values(Object.keys(properties)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var name_1 = _c.value;
                var value = properties[name_1];
                if (name_1 === 'texClass') {
                    node.texClass = value;
                    node.setProperty(name_1, value);
                }
                else if (name_1 === 'movablelimits') {
                    node.setProperty('movablelimits', value);
                    if (node.isKind('mo') || node.isKind('mstyle')) {
                        node.attributes.set('movablelimits', value);
                    }
                }
                else if (name_1 === 'inferred') {
                }
                else if (attrs.has(name_1)) {
                    node.setProperty(name_1, value);
                }
                else {
                    node.attributes.set(name_1, value);
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
    }
    NodeUtil.setProperties = setProperties;
    function getProperty(node, property) {
        return node.getProperty(property);
    }
    NodeUtil.getProperty = getProperty;
    function getAttribute(node, attr) {
        return node.attributes.get(attr);
    }
    NodeUtil.getAttribute = getAttribute;
    function removeProperties(node) {
        var properties = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            properties[_i - 1] = arguments[_i];
        }
        node.removeProperty.apply(node, __spreadArray([], __read(properties), false));
    }
    NodeUtil.removeProperties = removeProperties;
    function getChildAt(node, position) {
        return node.childNodes[position];
    }
    NodeUtil.getChildAt = getChildAt;
    function setChild(node, position, child) {
        var children = node.childNodes;
        children[position] = child;
        if (child) {
            child.parent = node;
        }
    }
    NodeUtil.setChild = setChild;
    function copyChildren(oldNode, newNode) {
        var children = oldNode.childNodes;
        for (var i = 0; i < children.length; i++) {
            setChild(newNode, i, children[i]);
        }
    }
    NodeUtil.copyChildren = copyChildren;
    function copyAttributes(oldNode, newNode) {
        newNode.attributes = oldNode.attributes;
        setProperties(newNode, oldNode.getAllProperties());
    }
    NodeUtil.copyAttributes = copyAttributes;
    function isType(node, kind) {
        return node.isKind(kind);
    }
    NodeUtil.isType = isType;
    function isEmbellished(node) {
        return node.isEmbellished;
    }
    NodeUtil.isEmbellished = isEmbellished;
    function getTexClass(node) {
        return node.texClass;
    }
    NodeUtil.getTexClass = getTexClass;
    function getCoreMO(node) {
        return node.coreMO();
    }
    NodeUtil.getCoreMO = getCoreMO;
    function isNode(item) {
        return item instanceof MmlNode_js_1.AbstractMmlNode || item instanceof MmlNode_js_1.AbstractMmlEmptyNode;
    }
    NodeUtil.isNode = isNode;
    function isInferred(node) {
        return node.isInferred;
    }
    NodeUtil.isInferred = isInferred;
    function getForm(node) {
        var e_3, _a;
        if (!isType(node, 'mo')) {
            return null;
        }
        var mo = node;
        var forms = mo.getForms();
        try {
            for (var forms_1 = __values(forms), forms_1_1 = forms_1.next(); !forms_1_1.done; forms_1_1 = forms_1.next()) {
                var form = forms_1_1.value;
                var symbol = mo_js_1.MmlMo.OPTABLE[form][mo.getText()];
                if (symbol) {
                    return symbol;
                }
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (forms_1_1 && !forms_1_1.done && (_a = forms_1.return)) _a.call(forms_1);
            }
            finally { if (e_3) throw e_3.error; }
        }
        return null;
    }
    NodeUtil.getForm = getForm;
})(NodeUtil || (NodeUtil = {}));
exports["default"] = NodeUtil;
//# sourceMappingURL=NodeUtil.js.map

/***/ }),

/***/ 708:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var TexConstants_js_1 = __webpack_require__(7);
var ParseUtil_js_1 = __importDefault(__webpack_require__(702));
var ParseMethods;
(function (ParseMethods) {
    function variable(parser, c) {
        var def = ParseUtil_js_1.default.getFontDef(parser);
        var env = parser.stack.env;
        if (env.multiLetterIdentifiers && env.font !== '') {
            c = parser.string.substr(parser.i - 1).match(env.multiLetterIdentifiers)[0];
            parser.i += c.length - 1;
            if (def.mathvariant === TexConstants_js_1.TexConstant.Variant.NORMAL && env.noAutoOP && c.length > 1) {
                def.autoOP = false;
            }
        }
        var node = parser.create('token', 'mi', def, c);
        parser.Push(node);
    }
    ParseMethods.variable = variable;
    function digit(parser, c) {
        var mml;
        var pattern = parser.configuration.options['digits'];
        var n = parser.string.slice(parser.i - 1).match(pattern);
        var def = ParseUtil_js_1.default.getFontDef(parser);
        if (n) {
            mml = parser.create('token', 'mn', def, n[0].replace(/[{}]/g, ''));
            parser.i += n[0].length - 1;
        }
        else {
            mml = parser.create('token', 'mo', def, c);
        }
        parser.Push(mml);
    }
    ParseMethods.digit = digit;
    function controlSequence(parser, _c) {
        var name = parser.GetCS();
        parser.parse('macro', [parser, name]);
    }
    ParseMethods.controlSequence = controlSequence;
    function mathchar0mi(parser, mchar) {
        var def = mchar.attributes || { mathvariant: TexConstants_js_1.TexConstant.Variant.ITALIC };
        var node = parser.create('token', 'mi', def, mchar.char);
        parser.Push(node);
    }
    ParseMethods.mathchar0mi = mathchar0mi;
    function mathchar0mo(parser, mchar) {
        var def = mchar.attributes || {};
        def['stretchy'] = false;
        var node = parser.create('token', 'mo', def, mchar.char);
        NodeUtil_js_1.default.setProperty(node, 'fixStretchy', true);
        parser.configuration.addNode('fixStretchy', node);
        parser.Push(node);
    }
    ParseMethods.mathchar0mo = mathchar0mo;
    function mathchar7(parser, mchar) {
        var def = mchar.attributes || { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL };
        if (parser.stack.env['font']) {
            def['mathvariant'] = parser.stack.env['font'];
        }
        var node = parser.create('token', 'mi', def, mchar.char);
        parser.Push(node);
    }
    ParseMethods.mathchar7 = mathchar7;
    function delimiter(parser, delim) {
        var def = delim.attributes || {};
        def = Object.assign({ fence: false, stretchy: false }, def);
        var node = parser.create('token', 'mo', def, delim.char);
        parser.Push(node);
    }
    ParseMethods.delimiter = delimiter;
    function environment(parser, env, func, args) {
        var end = args[0];
        var mml = parser.itemFactory.create('begin').setProperties({ name: env, end: end });
        mml = func.apply(void 0, __spreadArray([parser, mml], __read(args.slice(1)), false));
        parser.Push(mml);
    }
    ParseMethods.environment = environment;
})(ParseMethods || (ParseMethods = {}));
exports["default"] = ParseMethods;
//# sourceMappingURL=ParseMethods.js.map

/***/ }),

/***/ 394:
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
var StackItemFactory_js_1 = __importDefault(__webpack_require__(239));
var NodeFactory_js_1 = __webpack_require__(644);
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var Options_js_1 = __webpack_require__(77);
var ParseOptions = (function () {
    function ParseOptions(configuration, options) {
        if (options === void 0) { options = []; }
        this.options = {};
        this.packageData = new Map();
        this.parsers = [];
        this.root = null;
        this.nodeLists = {};
        this.error = false;
        this.handlers = configuration.handlers;
        this.nodeFactory = new NodeFactory_js_1.NodeFactory();
        this.nodeFactory.configuration = this;
        this.nodeFactory.setCreators(configuration.nodes);
        this.itemFactory = new StackItemFactory_js_1.default(configuration.items);
        this.itemFactory.configuration = this;
        Options_js_1.defaultOptions.apply(void 0, __spreadArray([this.options], __read(options), false));
        (0, Options_js_1.defaultOptions)(this.options, configuration.options);
    }
    ParseOptions.prototype.pushParser = function (parser) {
        this.parsers.unshift(parser);
    };
    ParseOptions.prototype.popParser = function () {
        this.parsers.shift();
    };
    Object.defineProperty(ParseOptions.prototype, "parser", {
        get: function () {
            return this.parsers[0];
        },
        enumerable: false,
        configurable: true
    });
    ParseOptions.prototype.clear = function () {
        this.parsers = [];
        this.root = null;
        this.nodeLists = {};
        this.error = false;
        this.tags.resetTag();
    };
    ParseOptions.prototype.addNode = function (property, node) {
        var list = this.nodeLists[property];
        if (!list) {
            list = this.nodeLists[property] = [];
        }
        list.push(node);
        if (node.kind !== property) {
            var inlists = (NodeUtil_js_1.default.getProperty(node, 'in-lists') || '');
            var lists = (inlists ? inlists.split(/,/) : []).concat(property).join(',');
            NodeUtil_js_1.default.setProperty(node, 'in-lists', lists);
        }
    };
    ParseOptions.prototype.getList = function (property) {
        var e_1, _a;
        var list = this.nodeLists[property] || [];
        var result = [];
        try {
            for (var list_1 = __values(list), list_1_1 = list_1.next(); !list_1_1.done; list_1_1 = list_1.next()) {
                var node = list_1_1.value;
                if (this.inTree(node)) {
                    result.push(node);
                }
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (list_1_1 && !list_1_1.done && (_a = list_1.return)) _a.call(list_1);
            }
            finally { if (e_1) throw e_1.error; }
        }
        this.nodeLists[property] = result;
        return result;
    };
    ParseOptions.prototype.removeFromList = function (property, nodes) {
        var e_2, _a;
        var list = this.nodeLists[property] || [];
        try {
            for (var nodes_1 = __values(nodes), nodes_1_1 = nodes_1.next(); !nodes_1_1.done; nodes_1_1 = nodes_1.next()) {
                var node = nodes_1_1.value;
                var i = list.indexOf(node);
                if (i >= 0) {
                    list.splice(i, 1);
                }
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (nodes_1_1 && !nodes_1_1.done && (_a = nodes_1.return)) _a.call(nodes_1);
            }
            finally { if (e_2) throw e_2.error; }
        }
    };
    ParseOptions.prototype.inTree = function (node) {
        while (node && node !== this.root) {
            node = node.parent;
        }
        return !!node;
    };
    return ParseOptions;
}());
exports["default"] = ParseOptions;
//# sourceMappingURL=ParseOptions.js.map

/***/ }),

/***/ 702:
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
var MmlNode_js_1 = __webpack_require__(921);
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var TexParser_js_1 = __importDefault(__webpack_require__(810));
var TexError_js_1 = __importDefault(__webpack_require__(466));
var Entities_js_1 = __webpack_require__(29);
var ParseUtil;
(function (ParseUtil) {
    var emPerInch = 7.2;
    var pxPerInch = 72;
    var UNIT_CASES = {
        'em': function (m) { return m; },
        'ex': function (m) { return m * .43; },
        'pt': function (m) { return m / 10; },
        'pc': function (m) { return m * 1.2; },
        'px': function (m) { return m * emPerInch / pxPerInch; },
        'in': function (m) { return m * emPerInch; },
        'cm': function (m) { return m * emPerInch / 2.54; },
        'mm': function (m) { return m * emPerInch / 25.4; },
        'mu': function (m) { return m / 18; },
    };
    var num = '([-+]?([.,]\\d+|\\d+([.,]\\d*)?))';
    var unit = '(pt|em|ex|mu|px|mm|cm|in|pc)';
    var dimenEnd = RegExp('^\\s*' + num + '\\s*' + unit + '\\s*$');
    var dimenRest = RegExp('^\\s*' + num + '\\s*' + unit + ' ?');
    function matchDimen(dim, rest) {
        if (rest === void 0) { rest = false; }
        var match = dim.match(rest ? dimenRest : dimenEnd);
        return match ?
            muReplace([match[1].replace(/,/, '.'), match[4], match[0].length]) :
            [null, null, 0];
    }
    ParseUtil.matchDimen = matchDimen;
    function muReplace(_a) {
        var _b = __read(_a, 3), value = _b[0], unit = _b[1], length = _b[2];
        if (unit !== 'mu') {
            return [value, unit, length];
        }
        var em = Em(UNIT_CASES[unit](parseFloat(value || '1')));
        return [em.slice(0, -2), 'em', length];
    }
    function dimen2em(dim) {
        var _a = __read(matchDimen(dim), 2), value = _a[0], unit = _a[1];
        var m = parseFloat(value || '1');
        var func = UNIT_CASES[unit];
        return func ? func(m) : 0;
    }
    ParseUtil.dimen2em = dimen2em;
    function Em(m) {
        if (Math.abs(m) < .0006) {
            return '0em';
        }
        return m.toFixed(3).replace(/\.?0+$/, '') + 'em';
    }
    ParseUtil.Em = Em;
    function cols() {
        var W = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            W[_i] = arguments[_i];
        }
        return W.map(function (n) { return Em(n); }).join(' ');
    }
    ParseUtil.cols = cols;
    function fenced(configuration, open, mml, close, big, color) {
        if (big === void 0) { big = ''; }
        if (color === void 0) { color = ''; }
        var nf = configuration.nodeFactory;
        var mrow = nf.create('node', 'mrow', [], { open: open, close: close, texClass: MmlNode_js_1.TEXCLASS.INNER });
        var mo;
        if (big) {
            mo = new TexParser_js_1.default('\\' + big + 'l' + open, configuration.parser.stack.env, configuration).mml();
        }
        else {
            var openNode = nf.create('text', open);
            mo = nf.create('node', 'mo', [], { fence: true, stretchy: true, symmetric: true, texClass: MmlNode_js_1.TEXCLASS.OPEN }, openNode);
        }
        NodeUtil_js_1.default.appendChildren(mrow, [mo, mml]);
        if (big) {
            mo = new TexParser_js_1.default('\\' + big + 'r' + close, configuration.parser.stack.env, configuration).mml();
        }
        else {
            var closeNode = nf.create('text', close);
            mo = nf.create('node', 'mo', [], { fence: true, stretchy: true, symmetric: true, texClass: MmlNode_js_1.TEXCLASS.CLOSE }, closeNode);
        }
        color && mo.attributes.set('mathcolor', color);
        NodeUtil_js_1.default.appendChildren(mrow, [mo]);
        return mrow;
    }
    ParseUtil.fenced = fenced;
    function fixedFence(configuration, open, mml, close) {
        var mrow = configuration.nodeFactory.create('node', 'mrow', [], { open: open, close: close, texClass: MmlNode_js_1.TEXCLASS.ORD });
        if (open) {
            NodeUtil_js_1.default.appendChildren(mrow, [mathPalette(configuration, open, 'l')]);
        }
        if (NodeUtil_js_1.default.isType(mml, 'mrow')) {
            NodeUtil_js_1.default.appendChildren(mrow, NodeUtil_js_1.default.getChildren(mml));
        }
        else {
            NodeUtil_js_1.default.appendChildren(mrow, [mml]);
        }
        if (close) {
            NodeUtil_js_1.default.appendChildren(mrow, [mathPalette(configuration, close, 'r')]);
        }
        return mrow;
    }
    ParseUtil.fixedFence = fixedFence;
    function mathPalette(configuration, fence, side) {
        if (fence === '{' || fence === '}') {
            fence = '\\' + fence;
        }
        var D = '{\\bigg' + side + ' ' + fence + '}';
        var T = '{\\big' + side + ' ' + fence + '}';
        return new TexParser_js_1.default('\\mathchoice' + D + T + T + T, {}, configuration).mml();
    }
    ParseUtil.mathPalette = mathPalette;
    function fixInitialMO(configuration, nodes) {
        for (var i = 0, m = nodes.length; i < m; i++) {
            var child = nodes[i];
            if (child && (!NodeUtil_js_1.default.isType(child, 'mspace') &&
                (!NodeUtil_js_1.default.isType(child, 'TeXAtom') ||
                    (NodeUtil_js_1.default.getChildren(child)[0] &&
                        NodeUtil_js_1.default.getChildren(NodeUtil_js_1.default.getChildren(child)[0]).length)))) {
                if (NodeUtil_js_1.default.isEmbellished(child) ||
                    (NodeUtil_js_1.default.isType(child, 'TeXAtom') && NodeUtil_js_1.default.getTexClass(child) === MmlNode_js_1.TEXCLASS.REL)) {
                    var mi = configuration.nodeFactory.create('node', 'mi');
                    nodes.unshift(mi);
                }
                break;
            }
        }
    }
    ParseUtil.fixInitialMO = fixInitialMO;
    function internalMath(parser, text, level, font) {
        if (parser.configuration.options.internalMath) {
            return parser.configuration.options.internalMath(parser, text, level, font);
        }
        var mathvariant = font || parser.stack.env.font;
        var def = (mathvariant ? { mathvariant: mathvariant } : {});
        var mml = [], i = 0, k = 0, c, node, match = '', braces = 0;
        if (text.match(/\\?[${}\\]|\\\(|\\(eq)?ref\s*\{/)) {
            while (i < text.length) {
                c = text.charAt(i++);
                if (c === '$') {
                    if (match === '$' && braces === 0) {
                        node = parser.create('node', 'TeXAtom', [(new TexParser_js_1.default(text.slice(k, i - 1), {}, parser.configuration)).mml()]);
                        mml.push(node);
                        match = '';
                        k = i;
                    }
                    else if (match === '') {
                        if (k < i - 1) {
                            mml.push(internalText(parser, text.slice(k, i - 1), def));
                        }
                        match = '$';
                        k = i;
                    }
                }
                else if (c === '{' && match !== '') {
                    braces++;
                }
                else if (c === '}') {
                    if (match === '}' && braces === 0) {
                        var atom = (new TexParser_js_1.default(text.slice(k, i), {}, parser.configuration)).mml();
                        node = parser.create('node', 'TeXAtom', [atom], def);
                        mml.push(node);
                        match = '';
                        k = i;
                    }
                    else if (match !== '') {
                        if (braces) {
                            braces--;
                        }
                    }
                }
                else if (c === '\\') {
                    if (match === '' && text.substr(i).match(/^(eq)?ref\s*\{/)) {
                        var len = RegExp['$&'].length;
                        if (k < i - 1) {
                            mml.push(internalText(parser, text.slice(k, i - 1), def));
                        }
                        match = '}';
                        k = i - 1;
                        i += len;
                    }
                    else {
                        c = text.charAt(i++);
                        if (c === '(' && match === '') {
                            if (k < i - 2) {
                                mml.push(internalText(parser, text.slice(k, i - 2), def));
                            }
                            match = ')';
                            k = i;
                        }
                        else if (c === ')' && match === ')' && braces === 0) {
                            node = parser.create('node', 'TeXAtom', [(new TexParser_js_1.default(text.slice(k, i - 2), {}, parser.configuration)).mml()]);
                            mml.push(node);
                            match = '';
                            k = i;
                        }
                        else if (c.match(/[${}\\]/) && match === '') {
                            i--;
                            text = text.substr(0, i - 1) + text.substr(i);
                        }
                    }
                }
            }
            if (match !== '') {
                throw new TexError_js_1.default('MathNotTerminated', 'Math not terminated in text box');
            }
        }
        if (k < text.length) {
            mml.push(internalText(parser, text.slice(k), def));
        }
        if (level != null) {
            mml = [parser.create('node', 'mstyle', mml, { displaystyle: false, scriptlevel: level })];
        }
        else if (mml.length > 1) {
            mml = [parser.create('node', 'mrow', mml)];
        }
        return mml;
    }
    ParseUtil.internalMath = internalMath;
    function internalText(parser, text, def) {
        text = text.replace(/^\s+/, Entities_js_1.entities.nbsp).replace(/\s+$/, Entities_js_1.entities.nbsp);
        var textNode = parser.create('text', text);
        return parser.create('node', 'mtext', [], def, textNode);
    }
    ParseUtil.internalText = internalText;
    function underOver(parser, base, script, pos, stack) {
        ParseUtil.checkMovableLimits(base);
        if (NodeUtil_js_1.default.isType(base, 'munderover') && NodeUtil_js_1.default.isEmbellished(base)) {
            NodeUtil_js_1.default.setProperties(NodeUtil_js_1.default.getCoreMO(base), { lspace: 0, rspace: 0 });
            var mo = parser.create('node', 'mo', [], { rspace: 0 });
            base = parser.create('node', 'mrow', [mo, base]);
        }
        var mml = parser.create('node', 'munderover', [base]);
        NodeUtil_js_1.default.setChild(mml, pos === 'over' ? mml.over : mml.under, script);
        var node = mml;
        if (stack) {
            node = parser.create('node', 'TeXAtom', [mml], { texClass: MmlNode_js_1.TEXCLASS.OP, movesupsub: true });
        }
        NodeUtil_js_1.default.setProperty(node, 'subsupOK', true);
        return node;
    }
    ParseUtil.underOver = underOver;
    function checkMovableLimits(base) {
        var symbol = (NodeUtil_js_1.default.isType(base, 'mo') ? NodeUtil_js_1.default.getForm(base) : null);
        if (NodeUtil_js_1.default.getProperty(base, 'movablelimits') || (symbol && symbol[3] && symbol[3].movablelimits)) {
            NodeUtil_js_1.default.setProperties(base, { movablelimits: false });
        }
    }
    ParseUtil.checkMovableLimits = checkMovableLimits;
    function trimSpaces(text) {
        if (typeof (text) !== 'string') {
            return text;
        }
        var TEXT = text.trim();
        if (TEXT.match(/\\$/) && text.match(/ $/)) {
            TEXT += ' ';
        }
        return TEXT;
    }
    ParseUtil.trimSpaces = trimSpaces;
    function setArrayAlign(array, align) {
        align = ParseUtil.trimSpaces(align || '');
        if (align === 't') {
            array.arraydef.align = 'baseline 1';
        }
        else if (align === 'b') {
            array.arraydef.align = 'baseline -1';
        }
        else if (align === 'c') {
            array.arraydef.align = 'axis';
        }
        else if (align) {
            array.arraydef.align = align;
        }
        return array;
    }
    ParseUtil.setArrayAlign = setArrayAlign;
    function substituteArgs(parser, args, str) {
        var text = '';
        var newstring = '';
        var i = 0;
        while (i < str.length) {
            var c = str.charAt(i++);
            if (c === '\\') {
                text += c + str.charAt(i++);
            }
            else if (c === '#') {
                c = str.charAt(i++);
                if (c === '#') {
                    text += c;
                }
                else {
                    if (!c.match(/[1-9]/) || parseInt(c, 10) > args.length) {
                        throw new TexError_js_1.default('IllegalMacroParam', 'Illegal macro parameter reference');
                    }
                    newstring = addArgs(parser, addArgs(parser, newstring, text), args[parseInt(c, 10) - 1]);
                    text = '';
                }
            }
            else {
                text += c;
            }
        }
        return addArgs(parser, newstring, text);
    }
    ParseUtil.substituteArgs = substituteArgs;
    function addArgs(parser, s1, s2) {
        if (s2.match(/^[a-z]/i) && s1.match(/(^|[^\\])(\\\\)*\\[a-z]+$/i)) {
            s1 += ' ';
        }
        if (s1.length + s2.length > parser.configuration.options['maxBuffer']) {
            throw new TexError_js_1.default('MaxBufferSize', 'MathJax internal buffer size exceeded; is there a' +
                ' recursive macro call?');
        }
        return s1 + s2;
    }
    ParseUtil.addArgs = addArgs;
    function checkMaxMacros(parser, isMacro) {
        if (isMacro === void 0) { isMacro = true; }
        if (++parser.macroCount <= parser.configuration.options['maxMacros']) {
            return;
        }
        if (isMacro) {
            throw new TexError_js_1.default('MaxMacroSub1', 'MathJax maximum macro substitution count exceeded; ' +
                'is here a recursive macro call?');
        }
        else {
            throw new TexError_js_1.default('MaxMacroSub2', 'MathJax maximum substitution count exceeded; ' +
                'is there a recursive latex environment?');
        }
    }
    ParseUtil.checkMaxMacros = checkMaxMacros;
    function checkEqnEnv(parser) {
        if (parser.stack.global.eqnenv) {
            throw new TexError_js_1.default('ErroneousNestingEq', 'Erroneous nesting of equation structures');
        }
        parser.stack.global.eqnenv = true;
    }
    ParseUtil.checkEqnEnv = checkEqnEnv;
    function copyNode(node, parser) {
        var tree = node.copy();
        var options = parser.configuration;
        tree.walkTree(function (n) {
            var e_1, _a;
            options.addNode(n.kind, n);
            var lists = (n.getProperty('in-lists') || '').split(/,/);
            try {
                for (var lists_1 = __values(lists), lists_1_1 = lists_1.next(); !lists_1_1.done; lists_1_1 = lists_1.next()) {
                    var list = lists_1_1.value;
                    list && options.addNode(list, n);
                }
            }
            catch (e_1_1) { e_1 = { error: e_1_1 }; }
            finally {
                try {
                    if (lists_1_1 && !lists_1_1.done && (_a = lists_1.return)) _a.call(lists_1);
                }
                finally { if (e_1) throw e_1.error; }
            }
        });
        return tree;
    }
    ParseUtil.copyNode = copyNode;
    function MmlFilterAttribute(_parser, _name, value) {
        return value;
    }
    ParseUtil.MmlFilterAttribute = MmlFilterAttribute;
    function getFontDef(parser) {
        var font = parser.stack.env['font'];
        return (font ? { mathvariant: font } : {});
    }
    ParseUtil.getFontDef = getFontDef;
    function keyvalOptions(attrib, allowed, error) {
        var e_2, _a;
        if (allowed === void 0) { allowed = null; }
        if (error === void 0) { error = false; }
        var def = readKeyval(attrib);
        if (allowed) {
            try {
                for (var _b = __values(Object.keys(def)), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var key = _c.value;
                    if (!allowed.hasOwnProperty(key)) {
                        if (error) {
                            throw new TexError_js_1.default('InvalidOption', 'Invalid option: %1', key);
                        }
                        delete def[key];
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
        }
        return def;
    }
    ParseUtil.keyvalOptions = keyvalOptions;
    function readKeyval(text) {
        var _a, _b;
        var options = {};
        var rest = text;
        var end, key, val;
        while (rest) {
            _a = __read(readValue(rest, ['=', ',']), 3), key = _a[0], end = _a[1], rest = _a[2];
            if (end === '=') {
                _b = __read(readValue(rest, [',']), 3), val = _b[0], end = _b[1], rest = _b[2];
                val = (val === 'false' || val === 'true') ?
                    JSON.parse(val) : val;
                options[key] = val;
            }
            else if (key) {
                options[key] = true;
            }
        }
        return options;
    }
    function removeBraces(text, count) {
        while (count > 0) {
            text = text.trim().slice(1, -1);
            count--;
        }
        return text.trim();
    }
    function readValue(text, end) {
        var length = text.length;
        var braces = 0;
        var value = '';
        var index = 0;
        var start = 0;
        var startCount = true;
        var stopCount = false;
        while (index < length) {
            var c = text[index++];
            switch (c) {
                case ' ':
                    break;
                case '{':
                    if (startCount) {
                        start++;
                    }
                    else {
                        stopCount = false;
                        if (start > braces) {
                            start = braces;
                        }
                    }
                    braces++;
                    break;
                case '}':
                    if (braces) {
                        braces--;
                    }
                    if (startCount || stopCount) {
                        start--;
                        stopCount = true;
                    }
                    startCount = false;
                    break;
                default:
                    if (!braces && end.indexOf(c) !== -1) {
                        return [stopCount ? 'true' :
                                removeBraces(value, start), c, text.slice(index)];
                    }
                    startCount = false;
                    stopCount = false;
            }
            value += c;
        }
        if (braces) {
            throw new TexError_js_1.default('ExtraOpenMissingClose', 'Extra open brace or missing close brace');
        }
        return [stopCount ? 'true' : removeBraces(value, start), '', text.slice(index)];
    }
})(ParseUtil || (ParseUtil = {}));
exports["default"] = ParseUtil;
//# sourceMappingURL=ParseUtil.js.map

/***/ }),

/***/ 874:
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
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var Stack = (function () {
    function Stack(_factory, _env, inner) {
        this._factory = _factory;
        this._env = _env;
        this.global = {};
        this.stack = [];
        this.global = { isInner: inner };
        this.stack = [this._factory.create('start', this.global)];
        if (_env) {
            this.stack[0].env = _env;
        }
        this.env = this.stack[0].env;
    }
    Object.defineProperty(Stack.prototype, "env", {
        get: function () {
            return this._env;
        },
        set: function (env) {
            this._env = env;
        },
        enumerable: false,
        configurable: true
    });
    Stack.prototype.Push = function () {
        var e_1, _a;
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        try {
            for (var args_1 = __values(args), args_1_1 = args_1.next(); !args_1_1.done; args_1_1 = args_1.next()) {
                var node = args_1_1.value;
                if (!node) {
                    continue;
                }
                var item = NodeUtil_js_1.default.isNode(node) ?
                    this._factory.create('mml', node) : node;
                item.global = this.global;
                var _b = __read(this.stack.length ? this.Top().checkItem(item) : [null, true], 2), top_1 = _b[0], success = _b[1];
                if (!success) {
                    continue;
                }
                if (top_1) {
                    this.Pop();
                    this.Push.apply(this, __spreadArray([], __read(top_1), false));
                    continue;
                }
                this.stack.push(item);
                if (item.env) {
                    if (item.copyEnv) {
                        Object.assign(item.env, this.env);
                    }
                    this.env = item.env;
                }
                else {
                    item.env = this.env;
                }
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (args_1_1 && !args_1_1.done && (_a = args_1.return)) _a.call(args_1);
            }
            finally { if (e_1) throw e_1.error; }
        }
    };
    Stack.prototype.Pop = function () {
        var item = this.stack.pop();
        if (!item.isOpen) {
            delete item.env;
        }
        this.env = (this.stack.length ? this.Top().env : {});
        return item;
    };
    Stack.prototype.Top = function (n) {
        if (n === void 0) { n = 1; }
        return this.stack.length < n ? null : this.stack[this.stack.length - n];
    };
    Stack.prototype.Prev = function (noPop) {
        var top = this.Top();
        return noPop ? top.First : top.Pop();
    };
    Stack.prototype.toString = function () {
        return 'stack[\n  ' + this.stack.join('\n  ') + '\n]';
    };
    return Stack;
}());
exports["default"] = Stack;
//# sourceMappingURL=Stack.js.map

/***/ }),

/***/ 44:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BaseItem = exports.MmlStack = void 0;
var TexError_js_1 = __importDefault(__webpack_require__(466));
var MmlStack = (function () {
    function MmlStack(_nodes) {
        this._nodes = _nodes;
    }
    Object.defineProperty(MmlStack.prototype, "nodes", {
        get: function () {
            return this._nodes;
        },
        enumerable: false,
        configurable: true
    });
    MmlStack.prototype.Push = function () {
        var _a;
        var nodes = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            nodes[_i] = arguments[_i];
        }
        (_a = this._nodes).push.apply(_a, __spreadArray([], __read(nodes), false));
    };
    MmlStack.prototype.Pop = function () {
        return this._nodes.pop();
    };
    Object.defineProperty(MmlStack.prototype, "First", {
        get: function () {
            return this._nodes[this.Size() - 1];
        },
        set: function (node) {
            this._nodes[this.Size() - 1] = node;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(MmlStack.prototype, "Last", {
        get: function () {
            return this._nodes[0];
        },
        set: function (node) {
            this._nodes[0] = node;
        },
        enumerable: false,
        configurable: true
    });
    MmlStack.prototype.Peek = function (n) {
        if (n == null) {
            n = 1;
        }
        return this._nodes.slice(this.Size() - n);
    };
    MmlStack.prototype.Size = function () {
        return this._nodes.length;
    };
    MmlStack.prototype.Clear = function () {
        this._nodes = [];
    };
    MmlStack.prototype.toMml = function (inferred, forceRow) {
        if (inferred === void 0) { inferred = true; }
        if (this._nodes.length === 1 && !forceRow) {
            return this.First;
        }
        return this.create('node', inferred ? 'inferredMrow' : 'mrow', this._nodes, {});
    };
    MmlStack.prototype.create = function (kind) {
        var _a;
        var rest = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            rest[_i - 1] = arguments[_i];
        }
        return (_a = this.factory.configuration.nodeFactory).create.apply(_a, __spreadArray([kind], __read(rest), false));
    };
    return MmlStack;
}());
exports.MmlStack = MmlStack;
var BaseItem = (function (_super) {
    __extends(BaseItem, _super);
    function BaseItem(factory) {
        var nodes = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            nodes[_i - 1] = arguments[_i];
        }
        var _this = _super.call(this, nodes) || this;
        _this.factory = factory;
        _this.global = {};
        _this._properties = {};
        if (_this.isOpen) {
            _this._env = {};
        }
        return _this;
    }
    Object.defineProperty(BaseItem.prototype, "kind", {
        get: function () {
            return 'base';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(BaseItem.prototype, "env", {
        get: function () {
            return this._env;
        },
        set: function (value) {
            this._env = value;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(BaseItem.prototype, "copyEnv", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    BaseItem.prototype.getProperty = function (key) {
        return this._properties[key];
    };
    BaseItem.prototype.setProperty = function (key, value) {
        this._properties[key] = value;
        return this;
    };
    Object.defineProperty(BaseItem.prototype, "isOpen", {
        get: function () {
            return false;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(BaseItem.prototype, "isClose", {
        get: function () {
            return false;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(BaseItem.prototype, "isFinal", {
        get: function () {
            return false;
        },
        enumerable: false,
        configurable: true
    });
    BaseItem.prototype.isKind = function (kind) {
        return kind === this.kind;
    };
    BaseItem.prototype.checkItem = function (item) {
        if (item.isKind('over') && this.isOpen) {
            item.setProperty('num', this.toMml(false));
            this.Clear();
        }
        if (item.isKind('cell') && this.isOpen) {
            if (item.getProperty('linebreak')) {
                return BaseItem.fail;
            }
            throw new TexError_js_1.default('Misplaced', 'Misplaced %1', item.getName());
        }
        if (item.isClose && this.getErrors(item.kind)) {
            var _a = __read(this.getErrors(item.kind), 2), id = _a[0], message = _a[1];
            throw new TexError_js_1.default(id, message, item.getName());
        }
        if (!item.isFinal) {
            return BaseItem.success;
        }
        this.Push(item.First);
        return BaseItem.fail;
    };
    BaseItem.prototype.clearEnv = function () {
        var e_1, _a;
        try {
            for (var _b = __values(Object.keys(this.env)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var id = _c.value;
                delete this.env[id];
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
    BaseItem.prototype.setProperties = function (def) {
        Object.assign(this._properties, def);
        return this;
    };
    BaseItem.prototype.getName = function () {
        return this.getProperty('name');
    };
    BaseItem.prototype.toString = function () {
        return this.kind + '[' + this.nodes.join('; ') + ']';
    };
    BaseItem.prototype.getErrors = function (kind) {
        var CLASS = this.constructor;
        return (CLASS.errors || {})[kind] || BaseItem.errors[kind];
    };
    BaseItem.fail = [null, false];
    BaseItem.success = [null, true];
    BaseItem.errors = {
        end: ['MissingBeginExtraEnd', 'Missing \\begin{%1} or extra \\end{%1}'],
        close: ['ExtraCloseMissingOpen', 'Extra close brace or missing open brace'],
        right: ['MissingLeftExtraRight', 'Missing \\left or extra \\right'],
        middle: ['ExtraMiddle', 'Extra \\middle']
    };
    return BaseItem;
}(MmlStack));
exports.BaseItem = BaseItem;
//# sourceMappingURL=StackItem.js.map

/***/ }),

/***/ 239:
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
var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
var StackItem_js_1 = __webpack_require__(44);
var Factory_js_1 = __webpack_require__(752);
var DummyItem = (function (_super) {
    __extends(DummyItem, _super);
    function DummyItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return DummyItem;
}(StackItem_js_1.BaseItem));
var StackItemFactory = (function (_super) {
    __extends(StackItemFactory, _super);
    function StackItemFactory() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.defaultKind = 'dummy';
        _this.configuration = null;
        return _this;
    }
    StackItemFactory.DefaultStackItems = (_a = {},
        _a[DummyItem.prototype.kind] = DummyItem,
        _a);
    return StackItemFactory;
}(Factory_js_1.AbstractFactory));
exports["default"] = StackItemFactory;
//# sourceMappingURL=StackItemFactory.js.map

/***/ }),

/***/ 237:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.Macro = exports.Symbol = void 0;
var Symbol = (function () {
    function Symbol(_symbol, _char, _attributes) {
        this._symbol = _symbol;
        this._char = _char;
        this._attributes = _attributes;
    }
    Object.defineProperty(Symbol.prototype, "symbol", {
        get: function () {
            return this._symbol;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Symbol.prototype, "char", {
        get: function () {
            return this._char;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Symbol.prototype, "attributes", {
        get: function () {
            return this._attributes;
        },
        enumerable: false,
        configurable: true
    });
    return Symbol;
}());
exports.Symbol = Symbol;
var Macro = (function () {
    function Macro(_symbol, _func, _args) {
        if (_args === void 0) { _args = []; }
        this._symbol = _symbol;
        this._func = _func;
        this._args = _args;
    }
    Object.defineProperty(Macro.prototype, "symbol", {
        get: function () {
            return this._symbol;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Macro.prototype, "func", {
        get: function () {
            return this._func;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Macro.prototype, "args", {
        get: function () {
            return this._args;
        },
        enumerable: false,
        configurable: true
    });
    return Macro;
}());
exports.Macro = Macro;
//# sourceMappingURL=Symbol.js.map

/***/ }),

/***/ 628:
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
exports.EnvironmentMap = exports.CommandMap = exports.MacroMap = exports.DelimiterMap = exports.CharacterMap = exports.AbstractParseMap = exports.RegExpMap = exports.AbstractSymbolMap = exports.parseResult = void 0;
var Symbol_js_1 = __webpack_require__(237);
var MapHandler_js_1 = __webpack_require__(910);
function parseResult(result) {
    return result === void 0 ? true : result;
}
exports.parseResult = parseResult;
var AbstractSymbolMap = (function () {
    function AbstractSymbolMap(_name, _parser) {
        this._name = _name;
        this._parser = _parser;
        MapHandler_js_1.MapHandler.register(this);
    }
    Object.defineProperty(AbstractSymbolMap.prototype, "name", {
        get: function () {
            return this._name;
        },
        enumerable: false,
        configurable: true
    });
    AbstractSymbolMap.prototype.parserFor = function (symbol) {
        return this.contains(symbol) ? this.parser : null;
    };
    AbstractSymbolMap.prototype.parse = function (_a) {
        var _b = __read(_a, 2), env = _b[0], symbol = _b[1];
        var parser = this.parserFor(symbol);
        var mapped = this.lookup(symbol);
        return (parser && mapped) ? parseResult(parser(env, mapped)) : null;
    };
    Object.defineProperty(AbstractSymbolMap.prototype, "parser", {
        get: function () {
            return this._parser;
        },
        set: function (parser) {
            this._parser = parser;
        },
        enumerable: false,
        configurable: true
    });
    return AbstractSymbolMap;
}());
exports.AbstractSymbolMap = AbstractSymbolMap;
var RegExpMap = (function (_super) {
    __extends(RegExpMap, _super);
    function RegExpMap(name, parser, _regExp) {
        var _this = _super.call(this, name, parser) || this;
        _this._regExp = _regExp;
        return _this;
    }
    RegExpMap.prototype.contains = function (symbol) {
        return this._regExp.test(symbol);
    };
    RegExpMap.prototype.lookup = function (symbol) {
        return this.contains(symbol) ? symbol : null;
    };
    return RegExpMap;
}(AbstractSymbolMap));
exports.RegExpMap = RegExpMap;
var AbstractParseMap = (function (_super) {
    __extends(AbstractParseMap, _super);
    function AbstractParseMap() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.map = new Map();
        return _this;
    }
    AbstractParseMap.prototype.lookup = function (symbol) {
        return this.map.get(symbol);
    };
    AbstractParseMap.prototype.contains = function (symbol) {
        return this.map.has(symbol);
    };
    AbstractParseMap.prototype.add = function (symbol, object) {
        this.map.set(symbol, object);
    };
    AbstractParseMap.prototype.remove = function (symbol) {
        this.map.delete(symbol);
    };
    return AbstractParseMap;
}(AbstractSymbolMap));
exports.AbstractParseMap = AbstractParseMap;
var CharacterMap = (function (_super) {
    __extends(CharacterMap, _super);
    function CharacterMap(name, parser, json) {
        var e_1, _a;
        var _this = _super.call(this, name, parser) || this;
        try {
            for (var _b = __values(Object.keys(json)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var key = _c.value;
                var value = json[key];
                var _d = __read((typeof (value) === 'string') ? [value, null] : value, 2), char = _d[0], attrs = _d[1];
                var character = new Symbol_js_1.Symbol(key, char, attrs);
                _this.add(key, character);
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
    return CharacterMap;
}(AbstractParseMap));
exports.CharacterMap = CharacterMap;
var DelimiterMap = (function (_super) {
    __extends(DelimiterMap, _super);
    function DelimiterMap() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    DelimiterMap.prototype.parse = function (_a) {
        var _b = __read(_a, 2), env = _b[0], symbol = _b[1];
        return _super.prototype.parse.call(this, [env, '\\' + symbol]);
    };
    return DelimiterMap;
}(CharacterMap));
exports.DelimiterMap = DelimiterMap;
var MacroMap = (function (_super) {
    __extends(MacroMap, _super);
    function MacroMap(name, json, functionMap) {
        var e_2, _a;
        var _this = _super.call(this, name, null) || this;
        try {
            for (var _b = __values(Object.keys(json)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var key = _c.value;
                var value = json[key];
                var _d = __read((typeof (value) === 'string') ? [value] : value), func = _d[0], attrs = _d.slice(1);
                var character = new Symbol_js_1.Macro(key, functionMap[func], attrs);
                _this.add(key, character);
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_2) throw e_2.error; }
        }
        return _this;
    }
    MacroMap.prototype.parserFor = function (symbol) {
        var macro = this.lookup(symbol);
        return macro ? macro.func : null;
    };
    MacroMap.prototype.parse = function (_a) {
        var _b = __read(_a, 2), env = _b[0], symbol = _b[1];
        var macro = this.lookup(symbol);
        var parser = this.parserFor(symbol);
        if (!macro || !parser) {
            return null;
        }
        return parseResult(parser.apply(void 0, __spreadArray([env, macro.symbol], __read(macro.args), false)));
    };
    return MacroMap;
}(AbstractParseMap));
exports.MacroMap = MacroMap;
var CommandMap = (function (_super) {
    __extends(CommandMap, _super);
    function CommandMap() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    CommandMap.prototype.parse = function (_a) {
        var _b = __read(_a, 2), env = _b[0], symbol = _b[1];
        var macro = this.lookup(symbol);
        var parser = this.parserFor(symbol);
        if (!macro || !parser) {
            return null;
        }
        var saveCommand = env.currentCS;
        env.currentCS = '\\' + symbol;
        var result = parser.apply(void 0, __spreadArray([env, '\\' + macro.symbol], __read(macro.args), false));
        env.currentCS = saveCommand;
        return parseResult(result);
    };
    return CommandMap;
}(MacroMap));
exports.CommandMap = CommandMap;
var EnvironmentMap = (function (_super) {
    __extends(EnvironmentMap, _super);
    function EnvironmentMap(name, parser, json, functionMap) {
        var _this = _super.call(this, name, json, functionMap) || this;
        _this.parser = parser;
        return _this;
    }
    EnvironmentMap.prototype.parse = function (_a) {
        var _b = __read(_a, 2), env = _b[0], symbol = _b[1];
        var macro = this.lookup(symbol);
        var envParser = this.parserFor(symbol);
        if (!macro || !envParser) {
            return null;
        }
        return parseResult(this.parser(env, macro.symbol, envParser, macro.args));
    };
    return EnvironmentMap;
}(MacroMap));
exports.EnvironmentMap = EnvironmentMap;
//# sourceMappingURL=SymbolMap.js.map

/***/ }),

/***/ 251:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TagsFactory = exports.AllTags = exports.NoTags = exports.AbstractTags = exports.TagInfo = exports.Label = void 0;
var TexParser_js_1 = __importDefault(__webpack_require__(810));
var Label = (function () {
    function Label(tag, id) {
        if (tag === void 0) { tag = '???'; }
        if (id === void 0) { id = ''; }
        this.tag = tag;
        this.id = id;
    }
    return Label;
}());
exports.Label = Label;
var TagInfo = (function () {
    function TagInfo(env, taggable, defaultTags, tag, tagId, tagFormat, noTag, labelId) {
        if (env === void 0) { env = ''; }
        if (taggable === void 0) { taggable = false; }
        if (defaultTags === void 0) { defaultTags = false; }
        if (tag === void 0) { tag = null; }
        if (tagId === void 0) { tagId = ''; }
        if (tagFormat === void 0) { tagFormat = ''; }
        if (noTag === void 0) { noTag = false; }
        if (labelId === void 0) { labelId = ''; }
        this.env = env;
        this.taggable = taggable;
        this.defaultTags = defaultTags;
        this.tag = tag;
        this.tagId = tagId;
        this.tagFormat = tagFormat;
        this.noTag = noTag;
        this.labelId = labelId;
    }
    return TagInfo;
}());
exports.TagInfo = TagInfo;
var AbstractTags = (function () {
    function AbstractTags() {
        this.counter = 0;
        this.allCounter = 0;
        this.configuration = null;
        this.ids = {};
        this.allIds = {};
        this.labels = {};
        this.allLabels = {};
        this.redo = false;
        this.refUpdate = false;
        this.currentTag = new TagInfo();
        this.history = [];
        this.stack = [];
        this.enTag = function (node, tag) {
            var nf = this.configuration.nodeFactory;
            var cell = nf.create('node', 'mtd', [node]);
            var row = nf.create('node', 'mlabeledtr', [tag, cell]);
            var table = nf.create('node', 'mtable', [row], {
                side: this.configuration.options['tagSide'],
                minlabelspacing: this.configuration.options['tagIndent'],
                displaystyle: true
            });
            return table;
        };
    }
    AbstractTags.prototype.start = function (env, taggable, defaultTags) {
        if (this.currentTag) {
            this.stack.push(this.currentTag);
        }
        this.currentTag = new TagInfo(env, taggable, defaultTags);
    };
    Object.defineProperty(AbstractTags.prototype, "env", {
        get: function () {
            return this.currentTag.env;
        },
        enumerable: false,
        configurable: true
    });
    AbstractTags.prototype.end = function () {
        this.history.push(this.currentTag);
        this.currentTag = this.stack.pop();
    };
    AbstractTags.prototype.tag = function (tag, noFormat) {
        this.currentTag.tag = tag;
        this.currentTag.tagFormat = noFormat ? tag : this.formatTag(tag);
        this.currentTag.noTag = false;
    };
    AbstractTags.prototype.notag = function () {
        this.tag('', true);
        this.currentTag.noTag = true;
    };
    Object.defineProperty(AbstractTags.prototype, "noTag", {
        get: function () {
            return this.currentTag.noTag;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(AbstractTags.prototype, "label", {
        get: function () {
            return this.currentTag.labelId;
        },
        set: function (label) {
            this.currentTag.labelId = label;
        },
        enumerable: false,
        configurable: true
    });
    AbstractTags.prototype.formatUrl = function (id, base) {
        return base + '#' + encodeURIComponent(id);
    };
    AbstractTags.prototype.formatTag = function (tag) {
        return '(' + tag + ')';
    };
    AbstractTags.prototype.formatId = function (id) {
        return 'mjx-eqn:' + id.replace(/\s/g, '_');
    };
    AbstractTags.prototype.formatNumber = function (n) {
        return n.toString();
    };
    AbstractTags.prototype.autoTag = function () {
        if (this.currentTag.tag == null) {
            this.counter++;
            this.tag(this.formatNumber(this.counter), false);
        }
    };
    AbstractTags.prototype.clearTag = function () {
        this.label = '';
        this.tag(null, true);
        this.currentTag.tagId = '';
    };
    AbstractTags.prototype.getTag = function (force) {
        if (force === void 0) { force = false; }
        if (force) {
            this.autoTag();
            return this.makeTag();
        }
        var ct = this.currentTag;
        if (ct.taggable && !ct.noTag) {
            if (ct.defaultTags) {
                this.autoTag();
            }
            if (ct.tag) {
                return this.makeTag();
            }
        }
        return null;
    };
    AbstractTags.prototype.resetTag = function () {
        this.history = [];
        this.redo = false;
        this.refUpdate = false;
        this.clearTag();
    };
    AbstractTags.prototype.reset = function (offset) {
        if (offset === void 0) { offset = 0; }
        this.resetTag();
        this.counter = this.allCounter = offset;
        this.allLabels = {};
        this.allIds = {};
    };
    AbstractTags.prototype.startEquation = function (math) {
        this.history = [];
        this.stack = [];
        this.clearTag();
        this.currentTag = new TagInfo('', undefined, undefined);
        this.labels = {};
        this.ids = {};
        this.counter = this.allCounter;
        this.redo = false;
        var recompile = math.inputData.recompile;
        if (recompile) {
            this.refUpdate = true;
            this.counter = recompile.counter;
        }
    };
    AbstractTags.prototype.finishEquation = function (math) {
        if (this.redo) {
            math.inputData.recompile = {
                state: math.state(),
                counter: this.allCounter
            };
        }
        if (!this.refUpdate) {
            this.allCounter = this.counter;
        }
        Object.assign(this.allIds, this.ids);
        Object.assign(this.allLabels, this.labels);
    };
    AbstractTags.prototype.finalize = function (node, env) {
        if (!env.display || this.currentTag.env ||
            this.currentTag.tag == null) {
            return node;
        }
        var tag = this.makeTag();
        var table = this.enTag(node, tag);
        return table;
    };
    AbstractTags.prototype.makeId = function () {
        this.currentTag.tagId = this.formatId(this.configuration.options['useLabelIds'] ?
            (this.label || this.currentTag.tag) : this.currentTag.tag);
    };
    AbstractTags.prototype.makeTag = function () {
        this.makeId();
        if (this.label) {
            this.labels[this.label] = new Label(this.currentTag.tag, this.currentTag.tagId);
        }
        var mml = new TexParser_js_1.default('\\text{' + this.currentTag.tagFormat + '}', {}, this.configuration).mml();
        return this.configuration.nodeFactory.create('node', 'mtd', [mml], { id: this.currentTag.tagId });
    };
    return AbstractTags;
}());
exports.AbstractTags = AbstractTags;
var NoTags = (function (_super) {
    __extends(NoTags, _super);
    function NoTags() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    NoTags.prototype.autoTag = function () { };
    NoTags.prototype.getTag = function () {
        return !this.currentTag.tag ? null : _super.prototype.getTag.call(this);
    };
    return NoTags;
}(AbstractTags));
exports.NoTags = NoTags;
var AllTags = (function (_super) {
    __extends(AllTags, _super);
    function AllTags() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    AllTags.prototype.finalize = function (node, env) {
        if (!env.display || this.history.find(function (x) { return x.taggable; })) {
            return node;
        }
        var tag = this.getTag(true);
        return this.enTag(node, tag);
    };
    return AllTags;
}(AbstractTags));
exports.AllTags = AllTags;
var TagsFactory;
(function (TagsFactory) {
    var tagsMapping = new Map([
        ['none', NoTags],
        ['all', AllTags]
    ]);
    var defaultTags = 'none';
    TagsFactory.OPTIONS = {
        tags: defaultTags,
        tagSide: 'right',
        tagIndent: '0.8em',
        useLabelIds: true,
        ignoreDuplicateLabels: false
    };
    TagsFactory.add = function (name, constr) {
        tagsMapping.set(name, constr);
    };
    TagsFactory.addTags = function (tags) {
        var e_1, _a;
        try {
            for (var _b = __values(Object.keys(tags)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var key = _c.value;
                TagsFactory.add(key, tags[key]);
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
    TagsFactory.create = function (name) {
        var constr = tagsMapping.get(name) || tagsMapping.get(defaultTags);
        if (!constr) {
            throw Error('Unknown tags class');
        }
        return new constr();
    };
    TagsFactory.setDefault = function (name) {
        defaultTags = name;
    };
    TagsFactory.getDefault = function () {
        return TagsFactory.create(defaultTags);
    };
})(TagsFactory = exports.TagsFactory || (exports.TagsFactory = {}));
//# sourceMappingURL=Tags.js.map

/***/ }),

/***/ 7:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TexConstant = void 0;
var TexConstant;
(function (TexConstant) {
    TexConstant.Variant = {
        NORMAL: 'normal',
        BOLD: 'bold',
        ITALIC: 'italic',
        BOLDITALIC: 'bold-italic',
        DOUBLESTRUCK: 'double-struck',
        FRAKTUR: 'fraktur',
        BOLDFRAKTUR: 'bold-fraktur',
        SCRIPT: 'script',
        BOLDSCRIPT: 'bold-script',
        SANSSERIF: 'sans-serif',
        BOLDSANSSERIF: 'bold-sans-serif',
        SANSSERIFITALIC: 'sans-serif-italic',
        SANSSERIFBOLDITALIC: 'sans-serif-bold-italic',
        MONOSPACE: 'monospace',
        INITIAL: 'inital',
        TAILED: 'tailed',
        LOOPED: 'looped',
        STRETCHED: 'stretched',
        CALLIGRAPHIC: '-tex-calligraphic',
        BOLDCALLIGRAPHIC: '-tex-bold-calligraphic',
        OLDSTYLE: '-tex-oldstyle',
        BOLDOLDSTYLE: '-tex-bold-oldstyle',
        MATHITALIC: '-tex-mathit'
    };
    TexConstant.Form = {
        PREFIX: 'prefix',
        INFIX: 'infix',
        POSTFIX: 'postfix'
    };
    TexConstant.LineBreak = {
        AUTO: 'auto',
        NEWLINE: 'newline',
        NOBREAK: 'nobreak',
        GOODBREAK: 'goodbreak',
        BADBREAK: 'badbreak'
    };
    TexConstant.LineBreakStyle = {
        BEFORE: 'before',
        AFTER: 'after',
        DUPLICATE: 'duplicate',
        INFIXLINBREAKSTYLE: 'infixlinebreakstyle'
    };
    TexConstant.IndentAlign = {
        LEFT: 'left',
        CENTER: 'center',
        RIGHT: 'right',
        AUTO: 'auto',
        ID: 'id',
        INDENTALIGN: 'indentalign'
    };
    TexConstant.IndentShift = {
        INDENTSHIFT: 'indentshift'
    };
    TexConstant.LineThickness = {
        THIN: 'thin',
        MEDIUM: 'medium',
        THICK: 'thick'
    };
    TexConstant.Notation = {
        LONGDIV: 'longdiv',
        ACTUARIAL: 'actuarial',
        PHASORANGLE: 'phasorangle',
        RADICAL: 'radical',
        BOX: 'box',
        ROUNDEDBOX: 'roundedbox',
        CIRCLE: 'circle',
        LEFT: 'left',
        RIGHT: 'right',
        TOP: 'top',
        BOTTOM: 'bottom',
        UPDIAGONALSTRIKE: 'updiagonalstrike',
        DOWNDIAGONALSTRIKE: 'downdiagonalstrike',
        VERTICALSTRIKE: 'verticalstrike',
        HORIZONTALSTRIKE: 'horizontalstrike',
        NORTHEASTARROW: 'northeastarrow',
        MADRUWB: 'madruwb',
        UPDIAGONALARROW: 'updiagonalarrow'
    };
    TexConstant.Align = {
        TOP: 'top',
        BOTTOM: 'bottom',
        CENTER: 'center',
        BASELINE: 'baseline',
        AXIS: 'axis',
        LEFT: 'left',
        RIGHT: 'right'
    };
    TexConstant.Lines = {
        NONE: 'none',
        SOLID: 'solid',
        DASHED: 'dashed'
    };
    TexConstant.Side = {
        LEFT: 'left',
        RIGHT: 'right',
        LEFTOVERLAP: 'leftoverlap',
        RIGHTOVERLAP: 'rightoverlap'
    };
    TexConstant.Width = {
        AUTO: 'auto',
        FIT: 'fit'
    };
    TexConstant.Actiontype = {
        TOGGLE: 'toggle',
        STATUSLINE: 'statusline',
        TOOLTIP: 'tooltip',
        INPUT: 'input'
    };
    TexConstant.Overflow = {
        LINBREAK: 'linebreak',
        SCROLL: 'scroll',
        ELIDE: 'elide',
        TRUNCATE: 'truncate',
        SCALE: 'scale'
    };
    TexConstant.Unit = {
        EM: 'em',
        EX: 'ex',
        PX: 'px',
        IN: 'in',
        CM: 'cm',
        MM: 'mm',
        PT: 'pt',
        PC: 'pc'
    };
})(TexConstant = exports.TexConstant || (exports.TexConstant = {}));
//# sourceMappingURL=TexConstants.js.map

/***/ }),

/***/ 466:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
var TexError = (function () {
    function TexError(id, message) {
        var rest = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            rest[_i - 2] = arguments[_i];
        }
        this.id = id;
        this.message = TexError.processString(message, rest);
    }
    TexError.processString = function (str, args) {
        var parts = str.split(TexError.pattern);
        for (var i = 1, m = parts.length; i < m; i += 2) {
            var c = parts[i].charAt(0);
            if (c >= '0' && c <= '9') {
                parts[i] = args[parseInt(parts[i], 10) - 1];
                if (typeof parts[i] === 'number') {
                    parts[i] = parts[i].toString();
                }
            }
            else if (c === '{') {
                c = parts[i].substr(1);
                if (c >= '0' && c <= '9') {
                    parts[i] = args[parseInt(parts[i].substr(1, parts[i].length - 2), 10) - 1];
                    if (typeof parts[i] === 'number') {
                        parts[i] = parts[i].toString();
                    }
                }
                else {
                    var match = parts[i].match(/^\{([a-z]+):%(\d+)\|(.*)\}$/);
                    if (match) {
                        parts[i] = '%' + parts[i];
                    }
                }
            }
            if (parts[i] == null) {
                parts[i] = '???';
            }
        }
        return parts.join('');
    };
    TexError.pattern = /%(\d+|\{\d+\}|\{[a-z]+:\%\d+(?:\|(?:%\{\d+\}|%.|[^\}])*)+\}|.)/g;
    return TexError;
}());
exports["default"] = TexError;
//# sourceMappingURL=TexError.js.map

/***/ }),

/***/ 810:
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
var ParseUtil_js_1 = __importDefault(__webpack_require__(702));
var Stack_js_1 = __importDefault(__webpack_require__(874));
var TexError_js_1 = __importDefault(__webpack_require__(466));
var MmlNode_js_1 = __webpack_require__(921);
var TexParser = (function () {
    function TexParser(_string, env, configuration) {
        var e_1, _a;
        this._string = _string;
        this.configuration = configuration;
        this.macroCount = 0;
        this.i = 0;
        this.currentCS = '';
        var inner = env.hasOwnProperty('isInner');
        var isInner = env['isInner'];
        delete env['isInner'];
        var ENV;
        if (env) {
            ENV = {};
            try {
                for (var _b = __values(Object.keys(env)), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var id = _c.value;
                    ENV[id] = env[id];
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
        this.configuration.pushParser(this);
        this.stack = new Stack_js_1.default(this.itemFactory, ENV, inner ? isInner : true);
        this.Parse();
        this.Push(this.itemFactory.create('stop'));
    }
    Object.defineProperty(TexParser.prototype, "options", {
        get: function () {
            return this.configuration.options;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TexParser.prototype, "itemFactory", {
        get: function () {
            return this.configuration.itemFactory;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TexParser.prototype, "tags", {
        get: function () {
            return this.configuration.tags;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(TexParser.prototype, "string", {
        get: function () {
            return this._string;
        },
        set: function (str) {
            this._string = str;
        },
        enumerable: false,
        configurable: true
    });
    TexParser.prototype.parse = function (kind, input) {
        return this.configuration.handlers.get(kind).parse(input);
    };
    TexParser.prototype.lookup = function (kind, symbol) {
        return this.configuration.handlers.get(kind).lookup(symbol);
    };
    TexParser.prototype.contains = function (kind, symbol) {
        return this.configuration.handlers.get(kind).contains(symbol);
    };
    TexParser.prototype.toString = function () {
        var e_2, _a;
        var str = '';
        try {
            for (var _b = __values(Array.from(this.configuration.handlers.keys())), _c = _b.next(); !_c.done; _c = _b.next()) {
                var config = _c.value;
                str += config + ': ' +
                    this.configuration.handlers.get(config) + '\n';
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b.return)) _a.call(_b);
            }
            finally { if (e_2) throw e_2.error; }
        }
        return str;
    };
    TexParser.prototype.Parse = function () {
        var c;
        while (this.i < this.string.length) {
            c = this.getCodePoint();
            this.i += c.length;
            this.parse('character', [this, c]);
        }
    };
    TexParser.prototype.Push = function (arg) {
        if (arg instanceof MmlNode_js_1.AbstractMmlNode && arg.isInferred) {
            this.PushAll(arg.childNodes);
        }
        else {
            this.stack.Push(arg);
        }
    };
    TexParser.prototype.PushAll = function (args) {
        var e_3, _a;
        try {
            for (var args_1 = __values(args), args_1_1 = args_1.next(); !args_1_1.done; args_1_1 = args_1.next()) {
                var arg = args_1_1.value;
                this.stack.Push(arg);
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (args_1_1 && !args_1_1.done && (_a = args_1.return)) _a.call(args_1);
            }
            finally { if (e_3) throw e_3.error; }
        }
    };
    TexParser.prototype.mml = function () {
        if (!this.stack.Top().isKind('mml')) {
            return null;
        }
        var node = this.stack.Top().First;
        this.configuration.popParser();
        return node;
    };
    TexParser.prototype.convertDelimiter = function (c) {
        var symbol = this.lookup('delimiter', c);
        return symbol ? symbol.char : null;
    };
    TexParser.prototype.getCodePoint = function () {
        var code = this.string.codePointAt(this.i);
        return code === undefined ? '' : String.fromCodePoint(code);
    };
    TexParser.prototype.nextIsSpace = function () {
        return !!this.string.charAt(this.i).match(/\s/);
    };
    TexParser.prototype.GetNext = function () {
        while (this.nextIsSpace()) {
            this.i++;
        }
        return this.getCodePoint();
    };
    TexParser.prototype.GetCS = function () {
        var CS = this.string.slice(this.i).match(/^(([a-z]+) ?|[\uD800-\uDBFF].|.)/i);
        if (CS) {
            this.i += CS[0].length;
            return CS[2] || CS[1];
        }
        else {
            this.i++;
            return ' ';
        }
    };
    TexParser.prototype.GetArgument = function (_name, noneOK) {
        switch (this.GetNext()) {
            case '':
                if (!noneOK) {
                    throw new TexError_js_1.default('MissingArgFor', 'Missing argument for %1', this.currentCS);
                }
                return null;
            case '}':
                if (!noneOK) {
                    throw new TexError_js_1.default('ExtraCloseMissingOpen', 'Extra close brace or missing open brace');
                }
                return null;
            case '\\':
                this.i++;
                return '\\' + this.GetCS();
            case '{':
                var j = ++this.i, parens = 1;
                while (this.i < this.string.length) {
                    switch (this.string.charAt(this.i++)) {
                        case '\\':
                            this.i++;
                            break;
                        case '{':
                            parens++;
                            break;
                        case '}':
                            if (--parens === 0) {
                                return this.string.slice(j, this.i - 1);
                            }
                            break;
                    }
                }
                throw new TexError_js_1.default('MissingCloseBrace', 'Missing close brace');
        }
        var c = this.getCodePoint();
        this.i += c.length;
        return c;
    };
    TexParser.prototype.GetBrackets = function (_name, def) {
        if (this.GetNext() !== '[') {
            return def;
        }
        var j = ++this.i, parens = 0;
        while (this.i < this.string.length) {
            switch (this.string.charAt(this.i++)) {
                case '{':
                    parens++;
                    break;
                case '\\':
                    this.i++;
                    break;
                case '}':
                    if (parens-- <= 0) {
                        throw new TexError_js_1.default('ExtraCloseLooking', 'Extra close brace while looking for %1', '\']\'');
                    }
                    break;
                case ']':
                    if (parens === 0) {
                        return this.string.slice(j, this.i - 1);
                    }
                    break;
            }
        }
        throw new TexError_js_1.default('MissingCloseBracket', 'Could not find closing \']\' for argument to %1', this.currentCS);
    };
    TexParser.prototype.GetDelimiter = function (name, braceOK) {
        var c = this.GetNext();
        this.i += c.length;
        if (this.i <= this.string.length) {
            if (c === '\\') {
                c += this.GetCS();
            }
            else if (c === '{' && braceOK) {
                this.i--;
                c = this.GetArgument(name).trim();
            }
            if (this.contains('delimiter', c)) {
                return this.convertDelimiter(c);
            }
        }
        throw new TexError_js_1.default('MissingOrUnrecognizedDelim', 'Missing or unrecognized delimiter for %1', this.currentCS);
    };
    TexParser.prototype.GetDimen = function (name) {
        if (this.GetNext() === '{') {
            var dimen = this.GetArgument(name);
            var _a = __read(ParseUtil_js_1.default.matchDimen(dimen), 2), value = _a[0], unit = _a[1];
            if (value) {
                return value + unit;
            }
        }
        else {
            var dimen = this.string.slice(this.i);
            var _b = __read(ParseUtil_js_1.default.matchDimen(dimen, true), 3), value = _b[0], unit = _b[1], length_1 = _b[2];
            if (value) {
                this.i += length_1;
                return value + unit;
            }
        }
        throw new TexError_js_1.default('MissingDimOrUnits', 'Missing dimension or its units for %1', this.currentCS);
    };
    TexParser.prototype.GetUpTo = function (_name, token) {
        while (this.nextIsSpace()) {
            this.i++;
        }
        var j = this.i;
        var parens = 0;
        while (this.i < this.string.length) {
            var k = this.i;
            var c = this.GetNext();
            this.i += c.length;
            switch (c) {
                case '\\':
                    c += this.GetCS();
                    break;
                case '{':
                    parens++;
                    break;
                case '}':
                    if (parens === 0) {
                        throw new TexError_js_1.default('ExtraCloseLooking', 'Extra close brace while looking for %1', token);
                    }
                    parens--;
                    break;
            }
            if (parens === 0 && c === token) {
                return this.string.slice(j, k);
            }
        }
        throw new TexError_js_1.default('TokenNotFoundForCommand', 'Could not find %1 for %2', token, this.currentCS);
    };
    TexParser.prototype.ParseArg = function (name) {
        return new TexParser(this.GetArgument(name), this.stack.env, this.configuration).mml();
    };
    TexParser.prototype.ParseUpTo = function (name, token) {
        return new TexParser(this.GetUpTo(name, token), this.stack.env, this.configuration).mml();
    };
    TexParser.prototype.GetDelimiterArg = function (name) {
        var c = ParseUtil_js_1.default.trimSpaces(this.GetArgument(name));
        if (c === '') {
            return null;
        }
        if (this.contains('delimiter', c)) {
            return c;
        }
        throw new TexError_js_1.default('MissingOrUnrecognizedDelim', 'Missing or unrecognized delimiter for %1', this.currentCS);
    };
    TexParser.prototype.GetStar = function () {
        var star = (this.GetNext() === '*');
        if (star) {
            this.i++;
        }
        return star;
    };
    TexParser.prototype.create = function (kind) {
        var _a;
        var rest = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            rest[_i - 1] = arguments[_i];
        }
        return (_a = this.configuration.nodeFactory).create.apply(_a, __spreadArray([kind], __read(rest), false));
    };
    return TexParser;
}());
exports["default"] = TexParser;
//# sourceMappingURL=TexParser.js.map

/***/ }),

/***/ 606:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BaseConfiguration = exports.BaseTags = exports.Other = void 0;
var Configuration_js_1 = __webpack_require__(552);
var MapHandler_js_1 = __webpack_require__(910);
var TexError_js_1 = __importDefault(__webpack_require__(466));
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var SymbolMap_js_1 = __webpack_require__(628);
var bitem = __importStar(__webpack_require__(389));
var Tags_js_1 = __webpack_require__(251);
__webpack_require__(962);
var OperatorDictionary_js_1 = __webpack_require__(857);
new SymbolMap_js_1.CharacterMap('remap', null, {
    '-': '\u2212',
    '*': '\u2217',
    '`': '\u2018'
});
function Other(parser, char) {
    var font = parser.stack.env['font'];
    var def = font ?
        { mathvariant: parser.stack.env['font'] } : {};
    var remap = MapHandler_js_1.MapHandler.getMap('remap').lookup(char);
    var range = (0, OperatorDictionary_js_1.getRange)(char);
    var type = (range ? range[3] : 'mo');
    var mo = parser.create('token', type, def, (remap ? remap.char : char));
    range[4] && mo.attributes.set('mathvariant', range[4]);
    if (type === 'mo') {
        NodeUtil_js_1.default.setProperty(mo, 'fixStretchy', true);
        parser.configuration.addNode('fixStretchy', mo);
    }
    parser.Push(mo);
}
exports.Other = Other;
function csUndefined(_parser, name) {
    throw new TexError_js_1.default('UndefinedControlSequence', 'Undefined control sequence %1', '\\' + name);
}
function envUndefined(_parser, env) {
    throw new TexError_js_1.default('UnknownEnv', 'Unknown environment \'%1\'', env);
}
function filterNonscript(_a) {
    var e_1, _b;
    var data = _a.data;
    try {
        for (var _c = __values(data.getList('nonscript')), _d = _c.next(); !_d.done; _d = _c.next()) {
            var mml = _d.value;
            if (mml.attributes.get('scriptlevel') > 0) {
                var parent_1 = mml.parent;
                parent_1.childNodes.splice(parent_1.childIndex(mml), 1);
                data.removeFromList(mml.kind, [mml]);
                if (mml.isKind('mrow')) {
                    var mstyle = mml.childNodes[0];
                    data.removeFromList('mstyle', [mstyle]);
                    data.removeFromList('mspace', mstyle.childNodes[0].childNodes);
                }
            }
            else if (mml.isKind('mrow')) {
                mml.parent.replaceChild(mml.childNodes[0], mml);
                data.removeFromList('mrow', [mml]);
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
}
var BaseTags = (function (_super) {
    __extends(BaseTags, _super);
    function BaseTags() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return BaseTags;
}(Tags_js_1.AbstractTags));
exports.BaseTags = BaseTags;
exports.BaseConfiguration = Configuration_js_1.Configuration.create('base', {
    handler: {
        character: ['command', 'special', 'letter', 'digit'],
        delimiter: ['delimiter'],
        macro: ['delimiter', 'macros', 'mathchar0mi', 'mathchar0mo', 'mathchar7'],
        environment: ['environment']
    },
    fallback: {
        character: Other,
        macro: csUndefined,
        environment: envUndefined
    },
    items: (_a = {},
        _a[bitem.StartItem.prototype.kind] = bitem.StartItem,
        _a[bitem.StopItem.prototype.kind] = bitem.StopItem,
        _a[bitem.OpenItem.prototype.kind] = bitem.OpenItem,
        _a[bitem.CloseItem.prototype.kind] = bitem.CloseItem,
        _a[bitem.PrimeItem.prototype.kind] = bitem.PrimeItem,
        _a[bitem.SubsupItem.prototype.kind] = bitem.SubsupItem,
        _a[bitem.OverItem.prototype.kind] = bitem.OverItem,
        _a[bitem.LeftItem.prototype.kind] = bitem.LeftItem,
        _a[bitem.Middle.prototype.kind] = bitem.Middle,
        _a[bitem.RightItem.prototype.kind] = bitem.RightItem,
        _a[bitem.BeginItem.prototype.kind] = bitem.BeginItem,
        _a[bitem.EndItem.prototype.kind] = bitem.EndItem,
        _a[bitem.StyleItem.prototype.kind] = bitem.StyleItem,
        _a[bitem.PositionItem.prototype.kind] = bitem.PositionItem,
        _a[bitem.CellItem.prototype.kind] = bitem.CellItem,
        _a[bitem.MmlItem.prototype.kind] = bitem.MmlItem,
        _a[bitem.FnItem.prototype.kind] = bitem.FnItem,
        _a[bitem.NotItem.prototype.kind] = bitem.NotItem,
        _a[bitem.NonscriptItem.prototype.kind] = bitem.NonscriptItem,
        _a[bitem.DotsItem.prototype.kind] = bitem.DotsItem,
        _a[bitem.ArrayItem.prototype.kind] = bitem.ArrayItem,
        _a[bitem.EqnArrayItem.prototype.kind] = bitem.EqnArrayItem,
        _a[bitem.EquationItem.prototype.kind] = bitem.EquationItem,
        _a),
    options: {
        maxMacros: 1000,
        baseURL: (typeof (document) === 'undefined' ||
            document.getElementsByTagName('base').length === 0) ?
            '' : String(document.location).replace(/#.*$/, '')
    },
    tags: {
        base: BaseTags
    },
    postprocessors: [[filterNonscript, -4]]
});
//# sourceMappingURL=BaseConfiguration.js.map

/***/ }),

/***/ 389:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.EquationItem = exports.EqnArrayItem = exports.ArrayItem = exports.DotsItem = exports.NonscriptItem = exports.NotItem = exports.FnItem = exports.MmlItem = exports.CellItem = exports.PositionItem = exports.StyleItem = exports.EndItem = exports.BeginItem = exports.RightItem = exports.Middle = exports.LeftItem = exports.OverItem = exports.SubsupItem = exports.PrimeItem = exports.CloseItem = exports.OpenItem = exports.StopItem = exports.StartItem = void 0;
var MapHandler_js_1 = __webpack_require__(910);
var Entities_js_1 = __webpack_require__(29);
var MmlNode_js_1 = __webpack_require__(921);
var TexError_js_1 = __importDefault(__webpack_require__(466));
var ParseUtil_js_1 = __importDefault(__webpack_require__(702));
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var StackItem_js_1 = __webpack_require__(44);
var StartItem = (function (_super) {
    __extends(StartItem, _super);
    function StartItem(factory, global) {
        var _this = _super.call(this, factory) || this;
        _this.global = global;
        return _this;
    }
    Object.defineProperty(StartItem.prototype, "kind", {
        get: function () {
            return 'start';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(StartItem.prototype, "isOpen", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    StartItem.prototype.checkItem = function (item) {
        if (item.isKind('stop')) {
            var node = this.toMml();
            if (!this.global.isInner) {
                node = this.factory.configuration.tags.finalize(node, this.env);
            }
            return [[this.factory.create('mml', node)], true];
        }
        return _super.prototype.checkItem.call(this, item);
    };
    return StartItem;
}(StackItem_js_1.BaseItem));
exports.StartItem = StartItem;
var StopItem = (function (_super) {
    __extends(StopItem, _super);
    function StopItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(StopItem.prototype, "kind", {
        get: function () {
            return 'stop';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(StopItem.prototype, "isClose", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    return StopItem;
}(StackItem_js_1.BaseItem));
exports.StopItem = StopItem;
var OpenItem = (function (_super) {
    __extends(OpenItem, _super);
    function OpenItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(OpenItem.prototype, "kind", {
        get: function () {
            return 'open';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(OpenItem.prototype, "isOpen", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    OpenItem.prototype.checkItem = function (item) {
        if (item.isKind('close')) {
            var mml = this.toMml();
            var node = this.create('node', 'TeXAtom', [mml]);
            return [[this.factory.create('mml', node)], true];
        }
        return _super.prototype.checkItem.call(this, item);
    };
    OpenItem.errors = Object.assign(Object.create(StackItem_js_1.BaseItem.errors), {
        'stop': ['ExtraOpenMissingClose',
            'Extra open brace or missing close brace']
    });
    return OpenItem;
}(StackItem_js_1.BaseItem));
exports.OpenItem = OpenItem;
var CloseItem = (function (_super) {
    __extends(CloseItem, _super);
    function CloseItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(CloseItem.prototype, "kind", {
        get: function () {
            return 'close';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(CloseItem.prototype, "isClose", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    return CloseItem;
}(StackItem_js_1.BaseItem));
exports.CloseItem = CloseItem;
var PrimeItem = (function (_super) {
    __extends(PrimeItem, _super);
    function PrimeItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(PrimeItem.prototype, "kind", {
        get: function () {
            return 'prime';
        },
        enumerable: false,
        configurable: true
    });
    PrimeItem.prototype.checkItem = function (item) {
        var _a = __read(this.Peek(2), 2), top0 = _a[0], top1 = _a[1];
        if (!NodeUtil_js_1.default.isType(top0, 'msubsup') || NodeUtil_js_1.default.isType(top0, 'msup')) {
            var node = this.create('node', 'msup', [top0, top1]);
            return [[node, item], true];
        }
        NodeUtil_js_1.default.setChild(top0, top0.sup, top1);
        return [[top0, item], true];
    };
    return PrimeItem;
}(StackItem_js_1.BaseItem));
exports.PrimeItem = PrimeItem;
var SubsupItem = (function (_super) {
    __extends(SubsupItem, _super);
    function SubsupItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(SubsupItem.prototype, "kind", {
        get: function () {
            return 'subsup';
        },
        enumerable: false,
        configurable: true
    });
    SubsupItem.prototype.checkItem = function (item) {
        if (item.isKind('open') || item.isKind('left')) {
            return StackItem_js_1.BaseItem.success;
        }
        var top = this.First;
        var position = this.getProperty('position');
        if (item.isKind('mml')) {
            if (this.getProperty('primes')) {
                if (position !== 2) {
                    NodeUtil_js_1.default.setChild(top, 2, this.getProperty('primes'));
                }
                else {
                    NodeUtil_js_1.default.setProperty(this.getProperty('primes'), 'variantForm', true);
                    var node = this.create('node', 'mrow', [this.getProperty('primes'), item.First]);
                    item.First = node;
                }
            }
            NodeUtil_js_1.default.setChild(top, position, item.First);
            if (this.getProperty('movesupsub') != null) {
                NodeUtil_js_1.default.setProperty(top, 'movesupsub', this.getProperty('movesupsub'));
            }
            var result = this.factory.create('mml', top);
            return [[result], true];
        }
        if (_super.prototype.checkItem.call(this, item)[1]) {
            var error = this.getErrors(['', 'sub', 'sup'][position]);
            throw new (TexError_js_1.default.bind.apply(TexError_js_1.default, __spreadArray([void 0, error[0], error[1]], __read(error.splice(2)), false)))();
        }
        return null;
    };
    SubsupItem.errors = Object.assign(Object.create(StackItem_js_1.BaseItem.errors), {
        'stop': ['MissingScript',
            'Missing superscript or subscript argument'],
        'sup': ['MissingOpenForSup',
            'Missing open brace for superscript'],
        'sub': ['MissingOpenForSub',
            'Missing open brace for subscript']
    });
    return SubsupItem;
}(StackItem_js_1.BaseItem));
exports.SubsupItem = SubsupItem;
var OverItem = (function (_super) {
    __extends(OverItem, _super);
    function OverItem(factory) {
        var _this = _super.call(this, factory) || this;
        _this.setProperty('name', '\\over');
        return _this;
    }
    Object.defineProperty(OverItem.prototype, "kind", {
        get: function () {
            return 'over';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(OverItem.prototype, "isClose", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    OverItem.prototype.checkItem = function (item) {
        if (item.isKind('over')) {
            throw new TexError_js_1.default('AmbiguousUseOf', 'Ambiguous use of %1', item.getName());
        }
        if (item.isClose) {
            var mml = this.create('node', 'mfrac', [this.getProperty('num'), this.toMml(false)]);
            if (this.getProperty('thickness') != null) {
                NodeUtil_js_1.default.setAttribute(mml, 'linethickness', this.getProperty('thickness'));
            }
            if (this.getProperty('open') || this.getProperty('close')) {
                NodeUtil_js_1.default.setProperty(mml, 'withDelims', true);
                mml = ParseUtil_js_1.default.fixedFence(this.factory.configuration, this.getProperty('open'), mml, this.getProperty('close'));
            }
            return [[this.factory.create('mml', mml), item], true];
        }
        return _super.prototype.checkItem.call(this, item);
    };
    OverItem.prototype.toString = function () {
        return 'over[' + this.getProperty('num') +
            ' / ' + this.nodes.join('; ') + ']';
    };
    return OverItem;
}(StackItem_js_1.BaseItem));
exports.OverItem = OverItem;
var LeftItem = (function (_super) {
    __extends(LeftItem, _super);
    function LeftItem(factory, delim) {
        var _this = _super.call(this, factory) || this;
        _this.setProperty('delim', delim);
        return _this;
    }
    Object.defineProperty(LeftItem.prototype, "kind", {
        get: function () {
            return 'left';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(LeftItem.prototype, "isOpen", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    LeftItem.prototype.checkItem = function (item) {
        if (item.isKind('right')) {
            return [[this.factory.create('mml', ParseUtil_js_1.default.fenced(this.factory.configuration, this.getProperty('delim'), this.toMml(), item.getProperty('delim'), '', item.getProperty('color')))], true];
        }
        if (item.isKind('middle')) {
            var def = { stretchy: true };
            if (item.getProperty('color')) {
                def.mathcolor = item.getProperty('color');
            }
            this.Push(this.create('node', 'TeXAtom', [], { texClass: MmlNode_js_1.TEXCLASS.CLOSE }), this.create('token', 'mo', def, item.getProperty('delim')), this.create('node', 'TeXAtom', [], { texClass: MmlNode_js_1.TEXCLASS.OPEN }));
            this.env = {};
            return [[this], true];
        }
        return _super.prototype.checkItem.call(this, item);
    };
    LeftItem.errors = Object.assign(Object.create(StackItem_js_1.BaseItem.errors), {
        'stop': ['ExtraLeftMissingRight',
            'Extra \\left or missing \\right']
    });
    return LeftItem;
}(StackItem_js_1.BaseItem));
exports.LeftItem = LeftItem;
var Middle = (function (_super) {
    __extends(Middle, _super);
    function Middle(factory, delim, color) {
        var _this = _super.call(this, factory) || this;
        _this.setProperty('delim', delim);
        color && _this.setProperty('color', color);
        return _this;
    }
    Object.defineProperty(Middle.prototype, "kind", {
        get: function () {
            return 'middle';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Middle.prototype, "isClose", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    return Middle;
}(StackItem_js_1.BaseItem));
exports.Middle = Middle;
var RightItem = (function (_super) {
    __extends(RightItem, _super);
    function RightItem(factory, delim, color) {
        var _this = _super.call(this, factory) || this;
        _this.setProperty('delim', delim);
        color && _this.setProperty('color', color);
        return _this;
    }
    Object.defineProperty(RightItem.prototype, "kind", {
        get: function () {
            return 'right';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(RightItem.prototype, "isClose", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    return RightItem;
}(StackItem_js_1.BaseItem));
exports.RightItem = RightItem;
var BeginItem = (function (_super) {
    __extends(BeginItem, _super);
    function BeginItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(BeginItem.prototype, "kind", {
        get: function () {
            return 'begin';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(BeginItem.prototype, "isOpen", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    BeginItem.prototype.checkItem = function (item) {
        if (item.isKind('end')) {
            if (item.getName() !== this.getName()) {
                throw new TexError_js_1.default('EnvBadEnd', '\\begin{%1} ended with \\end{%2}', this.getName(), item.getName());
            }
            if (!this.getProperty('end')) {
                return [[this.factory.create('mml', this.toMml())], true];
            }
            return StackItem_js_1.BaseItem.fail;
        }
        if (item.isKind('stop')) {
            throw new TexError_js_1.default('EnvMissingEnd', 'Missing \\end{%1}', this.getName());
        }
        return _super.prototype.checkItem.call(this, item);
    };
    return BeginItem;
}(StackItem_js_1.BaseItem));
exports.BeginItem = BeginItem;
var EndItem = (function (_super) {
    __extends(EndItem, _super);
    function EndItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(EndItem.prototype, "kind", {
        get: function () {
            return 'end';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(EndItem.prototype, "isClose", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    return EndItem;
}(StackItem_js_1.BaseItem));
exports.EndItem = EndItem;
var StyleItem = (function (_super) {
    __extends(StyleItem, _super);
    function StyleItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(StyleItem.prototype, "kind", {
        get: function () {
            return 'style';
        },
        enumerable: false,
        configurable: true
    });
    StyleItem.prototype.checkItem = function (item) {
        if (!item.isClose) {
            return _super.prototype.checkItem.call(this, item);
        }
        var mml = this.create('node', 'mstyle', this.nodes, this.getProperty('styles'));
        return [[this.factory.create('mml', mml), item], true];
    };
    return StyleItem;
}(StackItem_js_1.BaseItem));
exports.StyleItem = StyleItem;
var PositionItem = (function (_super) {
    __extends(PositionItem, _super);
    function PositionItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(PositionItem.prototype, "kind", {
        get: function () {
            return 'position';
        },
        enumerable: false,
        configurable: true
    });
    PositionItem.prototype.checkItem = function (item) {
        if (item.isClose) {
            throw new TexError_js_1.default('MissingBoxFor', 'Missing box for %1', this.getName());
        }
        if (item.isFinal) {
            var mml = item.toMml();
            switch (this.getProperty('move')) {
                case 'vertical':
                    mml = this.create('node', 'mpadded', [mml], { height: this.getProperty('dh'),
                        depth: this.getProperty('dd'),
                        voffset: this.getProperty('dh') });
                    return [[this.factory.create('mml', mml)], true];
                case 'horizontal':
                    return [[this.factory.create('mml', this.getProperty('left')), item,
                            this.factory.create('mml', this.getProperty('right'))], true];
            }
        }
        return _super.prototype.checkItem.call(this, item);
    };
    return PositionItem;
}(StackItem_js_1.BaseItem));
exports.PositionItem = PositionItem;
var CellItem = (function (_super) {
    __extends(CellItem, _super);
    function CellItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(CellItem.prototype, "kind", {
        get: function () {
            return 'cell';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(CellItem.prototype, "isClose", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    return CellItem;
}(StackItem_js_1.BaseItem));
exports.CellItem = CellItem;
var MmlItem = (function (_super) {
    __extends(MmlItem, _super);
    function MmlItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(MmlItem.prototype, "isFinal", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(MmlItem.prototype, "kind", {
        get: function () {
            return 'mml';
        },
        enumerable: false,
        configurable: true
    });
    return MmlItem;
}(StackItem_js_1.BaseItem));
exports.MmlItem = MmlItem;
var FnItem = (function (_super) {
    __extends(FnItem, _super);
    function FnItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(FnItem.prototype, "kind", {
        get: function () {
            return 'fn';
        },
        enumerable: false,
        configurable: true
    });
    FnItem.prototype.checkItem = function (item) {
        var top = this.First;
        if (top) {
            if (item.isOpen) {
                return StackItem_js_1.BaseItem.success;
            }
            if (!item.isKind('fn')) {
                var mml = item.First;
                if (!item.isKind('mml') || !mml) {
                    return [[top, item], true];
                }
                if ((NodeUtil_js_1.default.isType(mml, 'mstyle') && mml.childNodes.length &&
                    NodeUtil_js_1.default.isType(mml.childNodes[0].childNodes[0], 'mspace')) ||
                    NodeUtil_js_1.default.isType(mml, 'mspace')) {
                    return [[top, item], true];
                }
                if (NodeUtil_js_1.default.isEmbellished(mml)) {
                    mml = NodeUtil_js_1.default.getCoreMO(mml);
                }
                var form = NodeUtil_js_1.default.getForm(mml);
                if (form != null && [0, 0, 1, 1, 0, 1, 1, 0, 0, 0][form[2]]) {
                    return [[top, item], true];
                }
            }
            var node = this.create('token', 'mo', { texClass: MmlNode_js_1.TEXCLASS.NONE }, Entities_js_1.entities.ApplyFunction);
            return [[top, node, item], true];
        }
        return _super.prototype.checkItem.apply(this, arguments);
    };
    return FnItem;
}(StackItem_js_1.BaseItem));
exports.FnItem = FnItem;
var NotItem = (function (_super) {
    __extends(NotItem, _super);
    function NotItem() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.remap = MapHandler_js_1.MapHandler.getMap('not_remap');
        return _this;
    }
    Object.defineProperty(NotItem.prototype, "kind", {
        get: function () {
            return 'not';
        },
        enumerable: false,
        configurable: true
    });
    NotItem.prototype.checkItem = function (item) {
        var mml;
        var c;
        var textNode;
        if (item.isKind('open') || item.isKind('left')) {
            return StackItem_js_1.BaseItem.success;
        }
        if (item.isKind('mml') &&
            (NodeUtil_js_1.default.isType(item.First, 'mo') || NodeUtil_js_1.default.isType(item.First, 'mi') ||
                NodeUtil_js_1.default.isType(item.First, 'mtext'))) {
            mml = item.First;
            c = NodeUtil_js_1.default.getText(mml);
            if (c.length === 1 && !NodeUtil_js_1.default.getProperty(mml, 'movesupsub') &&
                NodeUtil_js_1.default.getChildren(mml).length === 1) {
                if (this.remap.contains(c)) {
                    textNode = this.create('text', this.remap.lookup(c).char);
                    NodeUtil_js_1.default.setChild(mml, 0, textNode);
                }
                else {
                    textNode = this.create('text', '\u0338');
                    NodeUtil_js_1.default.appendChildren(mml, [textNode]);
                }
                return [[item], true];
            }
        }
        textNode = this.create('text', '\u29F8');
        var mtextNode = this.create('node', 'mtext', [], {}, textNode);
        var paddedNode = this.create('node', 'mpadded', [mtextNode], { width: 0 });
        mml = this.create('node', 'TeXAtom', [paddedNode], { texClass: MmlNode_js_1.TEXCLASS.REL });
        return [[mml, item], true];
    };
    return NotItem;
}(StackItem_js_1.BaseItem));
exports.NotItem = NotItem;
var NonscriptItem = (function (_super) {
    __extends(NonscriptItem, _super);
    function NonscriptItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(NonscriptItem.prototype, "kind", {
        get: function () {
            return 'nonscript';
        },
        enumerable: false,
        configurable: true
    });
    NonscriptItem.prototype.checkItem = function (item) {
        if (item.isKind('mml') && item.Size() === 1) {
            var mml = item.First;
            if (mml.isKind('mstyle') && mml.notParent) {
                mml = NodeUtil_js_1.default.getChildren(NodeUtil_js_1.default.getChildren(mml)[0])[0];
            }
            if (mml.isKind('mspace')) {
                if (mml !== item.First) {
                    var mrow = this.create('node', 'mrow', [item.Pop()]);
                    item.Push(mrow);
                }
                this.factory.configuration.addNode('nonscript', item.First);
            }
        }
        return [[item], true];
    };
    return NonscriptItem;
}(StackItem_js_1.BaseItem));
exports.NonscriptItem = NonscriptItem;
var DotsItem = (function (_super) {
    __extends(DotsItem, _super);
    function DotsItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(DotsItem.prototype, "kind", {
        get: function () {
            return 'dots';
        },
        enumerable: false,
        configurable: true
    });
    DotsItem.prototype.checkItem = function (item) {
        if (item.isKind('open') || item.isKind('left')) {
            return StackItem_js_1.BaseItem.success;
        }
        var dots = this.getProperty('ldots');
        var top = item.First;
        if (item.isKind('mml') && NodeUtil_js_1.default.isEmbellished(top)) {
            var tclass = NodeUtil_js_1.default.getTexClass(NodeUtil_js_1.default.getCoreMO(top));
            if (tclass === MmlNode_js_1.TEXCLASS.BIN || tclass === MmlNode_js_1.TEXCLASS.REL) {
                dots = this.getProperty('cdots');
            }
        }
        return [[dots, item], true];
    };
    return DotsItem;
}(StackItem_js_1.BaseItem));
exports.DotsItem = DotsItem;
var ArrayItem = (function (_super) {
    __extends(ArrayItem, _super);
    function ArrayItem() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.table = [];
        _this.row = [];
        _this.frame = [];
        _this.hfill = [];
        _this.arraydef = {};
        _this.dashed = false;
        return _this;
    }
    Object.defineProperty(ArrayItem.prototype, "kind", {
        get: function () {
            return 'array';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(ArrayItem.prototype, "isOpen", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(ArrayItem.prototype, "copyEnv", {
        get: function () {
            return false;
        },
        enumerable: false,
        configurable: true
    });
    ArrayItem.prototype.checkItem = function (item) {
        if (item.isClose && !item.isKind('over')) {
            if (item.getProperty('isEntry')) {
                this.EndEntry();
                this.clearEnv();
                return StackItem_js_1.BaseItem.fail;
            }
            if (item.getProperty('isCR')) {
                this.EndEntry();
                this.EndRow();
                this.clearEnv();
                return StackItem_js_1.BaseItem.fail;
            }
            this.EndTable();
            this.clearEnv();
            var newItem = this.factory.create('mml', this.createMml());
            if (this.getProperty('requireClose')) {
                if (item.isKind('close')) {
                    return [[newItem], true];
                }
                throw new TexError_js_1.default('MissingCloseBrace', 'Missing close brace');
            }
            return [[newItem, item], true];
        }
        return _super.prototype.checkItem.call(this, item);
    };
    ArrayItem.prototype.createMml = function () {
        var scriptlevel = this.arraydef['scriptlevel'];
        delete this.arraydef['scriptlevel'];
        var mml = this.create('node', 'mtable', this.table, this.arraydef);
        if (scriptlevel) {
            mml.setProperty('scriptlevel', scriptlevel);
        }
        if (this.frame.length === 4) {
            NodeUtil_js_1.default.setAttribute(mml, 'frame', this.dashed ? 'dashed' : 'solid');
        }
        else if (this.frame.length) {
            if (this.arraydef['rowlines']) {
                this.arraydef['rowlines'] =
                    this.arraydef['rowlines'].replace(/none( none)+$/, 'none');
            }
            NodeUtil_js_1.default.setAttribute(mml, 'frame', '');
            mml = this.create('node', 'menclose', [mml], { notation: this.frame.join(' ') });
            if ((this.arraydef['columnlines'] || 'none') !== 'none' ||
                (this.arraydef['rowlines'] || 'none') !== 'none') {
                NodeUtil_js_1.default.setAttribute(mml, 'data-padding', 0);
            }
        }
        if (this.getProperty('open') || this.getProperty('close')) {
            mml = ParseUtil_js_1.default.fenced(this.factory.configuration, this.getProperty('open'), mml, this.getProperty('close'));
        }
        return mml;
    };
    ArrayItem.prototype.EndEntry = function () {
        var mtd = this.create('node', 'mtd', this.nodes);
        if (this.hfill.length) {
            if (this.hfill[0] === 0) {
                NodeUtil_js_1.default.setAttribute(mtd, 'columnalign', 'right');
            }
            if (this.hfill[this.hfill.length - 1] === this.Size()) {
                NodeUtil_js_1.default.setAttribute(mtd, 'columnalign', NodeUtil_js_1.default.getAttribute(mtd, 'columnalign') ? 'center' : 'left');
            }
        }
        this.row.push(mtd);
        this.Clear();
        this.hfill = [];
    };
    ArrayItem.prototype.EndRow = function () {
        var node;
        if (this.getProperty('isNumbered') && this.row.length === 3) {
            this.row.unshift(this.row.pop());
            node = this.create('node', 'mlabeledtr', this.row);
        }
        else {
            node = this.create('node', 'mtr', this.row);
        }
        this.table.push(node);
        this.row = [];
    };
    ArrayItem.prototype.EndTable = function () {
        if (this.Size() || this.row.length) {
            this.EndEntry();
            this.EndRow();
        }
        this.checkLines();
    };
    ArrayItem.prototype.checkLines = function () {
        if (this.arraydef['rowlines']) {
            var lines = this.arraydef['rowlines'].split(/ /);
            if (lines.length === this.table.length) {
                this.frame.push('bottom');
                lines.pop();
                this.arraydef['rowlines'] = lines.join(' ');
            }
            else if (lines.length < this.table.length - 1) {
                this.arraydef['rowlines'] += ' none';
            }
        }
        if (this.getProperty('rowspacing')) {
            var rows = this.arraydef['rowspacing'].split(/ /);
            while (rows.length < this.table.length) {
                rows.push(this.getProperty('rowspacing') + 'em');
            }
            this.arraydef['rowspacing'] = rows.join(' ');
        }
    };
    ArrayItem.prototype.addRowSpacing = function (spacing) {
        if (this.arraydef['rowspacing']) {
            var rows = this.arraydef['rowspacing'].split(/ /);
            if (!this.getProperty('rowspacing')) {
                var dimem = ParseUtil_js_1.default.dimen2em(rows[0]);
                this.setProperty('rowspacing', dimem);
            }
            var rowspacing = this.getProperty('rowspacing');
            while (rows.length < this.table.length) {
                rows.push(ParseUtil_js_1.default.Em(rowspacing));
            }
            rows[this.table.length - 1] = ParseUtil_js_1.default.Em(Math.max(0, rowspacing + ParseUtil_js_1.default.dimen2em(spacing)));
            this.arraydef['rowspacing'] = rows.join(' ');
        }
    };
    return ArrayItem;
}(StackItem_js_1.BaseItem));
exports.ArrayItem = ArrayItem;
var EqnArrayItem = (function (_super) {
    __extends(EqnArrayItem, _super);
    function EqnArrayItem(factory) {
        var args = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            args[_i - 1] = arguments[_i];
        }
        var _this = _super.call(this, factory) || this;
        _this.maxrow = 0;
        _this.factory.configuration.tags.start(args[0], args[2], args[1]);
        return _this;
    }
    Object.defineProperty(EqnArrayItem.prototype, "kind", {
        get: function () {
            return 'eqnarray';
        },
        enumerable: false,
        configurable: true
    });
    EqnArrayItem.prototype.EndEntry = function () {
        if (this.row.length) {
            ParseUtil_js_1.default.fixInitialMO(this.factory.configuration, this.nodes);
        }
        var node = this.create('node', 'mtd', this.nodes);
        this.row.push(node);
        this.Clear();
    };
    EqnArrayItem.prototype.EndRow = function () {
        if (this.row.length > this.maxrow) {
            this.maxrow = this.row.length;
        }
        var mtr = 'mtr';
        var tag = this.factory.configuration.tags.getTag();
        if (tag) {
            this.row = [tag].concat(this.row);
            mtr = 'mlabeledtr';
        }
        this.factory.configuration.tags.clearTag();
        var node = this.create('node', mtr, this.row);
        this.table.push(node);
        this.row = [];
    };
    EqnArrayItem.prototype.EndTable = function () {
        _super.prototype.EndTable.call(this);
        this.factory.configuration.tags.end();
        this.extendArray('columnalign', this.maxrow);
        this.extendArray('columnwidth', this.maxrow);
        this.extendArray('columnspacing', this.maxrow - 1);
    };
    EqnArrayItem.prototype.extendArray = function (name, max) {
        if (!this.arraydef[name])
            return;
        var repeat = this.arraydef[name].split(/ /);
        var columns = __spreadArray([], __read(repeat), false);
        if (columns.length > 1) {
            while (columns.length < max) {
                columns.push.apply(columns, __spreadArray([], __read(repeat), false));
            }
            this.arraydef[name] = columns.slice(0, max).join(' ');
        }
    };
    return EqnArrayItem;
}(ArrayItem));
exports.EqnArrayItem = EqnArrayItem;
var EquationItem = (function (_super) {
    __extends(EquationItem, _super);
    function EquationItem(factory) {
        var args = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            args[_i - 1] = arguments[_i];
        }
        var _this = _super.call(this, factory) || this;
        _this.factory.configuration.tags.start('equation', true, args[0]);
        return _this;
    }
    Object.defineProperty(EquationItem.prototype, "kind", {
        get: function () {
            return 'equation';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(EquationItem.prototype, "isOpen", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    EquationItem.prototype.checkItem = function (item) {
        if (item.isKind('end')) {
            var mml = this.toMml();
            var tag = this.factory.configuration.tags.getTag();
            this.factory.configuration.tags.end();
            return [[tag ? this.factory.configuration.tags.enTag(mml, tag) : mml, item], true];
        }
        if (item.isKind('stop')) {
            throw new TexError_js_1.default('EnvMissingEnd', 'Missing \\end{%1}', this.getName());
        }
        return _super.prototype.checkItem.call(this, item);
    };
    return EquationItem;
}(StackItem_js_1.BaseItem));
exports.EquationItem = EquationItem;
//# sourceMappingURL=BaseItems.js.map

/***/ }),

/***/ 962:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var sm = __importStar(__webpack_require__(628));
var TexConstants_js_1 = __webpack_require__(7);
var BaseMethods_js_1 = __importDefault(__webpack_require__(724));
var ParseMethods_js_1 = __importDefault(__webpack_require__(708));
var ParseUtil_js_1 = __importDefault(__webpack_require__(702));
var MmlNode_js_1 = __webpack_require__(921);
var lengths_js_1 = __webpack_require__(914);
new sm.RegExpMap('letter', ParseMethods_js_1.default.variable, /[a-z]/i);
new sm.RegExpMap('digit', ParseMethods_js_1.default.digit, /[0-9.,]/);
new sm.RegExpMap('command', ParseMethods_js_1.default.controlSequence, /^\\/);
new sm.MacroMap('special', {
    '{': 'Open',
    '}': 'Close',
    '~': 'Tilde',
    '^': 'Superscript',
    '_': 'Subscript',
    ' ': 'Space',
    '\t': 'Space',
    '\r': 'Space',
    '\n': 'Space',
    '\'': 'Prime',
    '%': 'Comment',
    '&': 'Entry',
    '#': 'Hash',
    '\u00A0': 'Space',
    '\u2019': 'Prime'
}, BaseMethods_js_1.default);
new sm.CharacterMap('mathchar0mi', ParseMethods_js_1.default.mathchar0mi, {
    alpha: '\u03B1',
    beta: '\u03B2',
    gamma: '\u03B3',
    delta: '\u03B4',
    epsilon: '\u03F5',
    zeta: '\u03B6',
    eta: '\u03B7',
    theta: '\u03B8',
    iota: '\u03B9',
    kappa: '\u03BA',
    lambda: '\u03BB',
    mu: '\u03BC',
    nu: '\u03BD',
    xi: '\u03BE',
    omicron: '\u03BF',
    pi: '\u03C0',
    rho: '\u03C1',
    sigma: '\u03C3',
    tau: '\u03C4',
    upsilon: '\u03C5',
    phi: '\u03D5',
    chi: '\u03C7',
    psi: '\u03C8',
    omega: '\u03C9',
    varepsilon: '\u03B5',
    vartheta: '\u03D1',
    varpi: '\u03D6',
    varrho: '\u03F1',
    varsigma: '\u03C2',
    varphi: '\u03C6',
    S: ['\u00A7', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    aleph: ['\u2135', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    hbar: ['\u210F', { variantForm: true }],
    imath: '\u0131',
    jmath: '\u0237',
    ell: '\u2113',
    wp: ['\u2118', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    Re: ['\u211C', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    Im: ['\u2111', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    partial: ['\u2202', { mathvariant: TexConstants_js_1.TexConstant.Variant.ITALIC }],
    infty: ['\u221E', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    prime: ['\u2032', { variantForm: true }],
    emptyset: ['\u2205', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    nabla: ['\u2207', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    top: ['\u22A4', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    bot: ['\u22A5', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    angle: ['\u2220', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    triangle: ['\u25B3', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    backslash: ['\u2216', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    forall: ['\u2200', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    exists: ['\u2203', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    neg: ['\u00AC', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    lnot: ['\u00AC', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    flat: ['\u266D', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    natural: ['\u266E', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    sharp: ['\u266F', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    clubsuit: ['\u2663', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    diamondsuit: ['\u2662', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    heartsuit: ['\u2661', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }],
    spadesuit: ['\u2660', { mathvariant: TexConstants_js_1.TexConstant.Variant.NORMAL }]
});
new sm.CharacterMap('mathchar0mo', ParseMethods_js_1.default.mathchar0mo, {
    surd: '\u221A',
    coprod: ['\u2210', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    bigvee: ['\u22C1', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    bigwedge: ['\u22C0', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    biguplus: ['\u2A04', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    bigcap: ['\u22C2', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    bigcup: ['\u22C3', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    'int': ['\u222B', { texClass: MmlNode_js_1.TEXCLASS.OP }],
    intop: ['\u222B', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true, movablelimits: true }],
    iint: ['\u222C', { texClass: MmlNode_js_1.TEXCLASS.OP }],
    iiint: ['\u222D', { texClass: MmlNode_js_1.TEXCLASS.OP }],
    prod: ['\u220F', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    sum: ['\u2211', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    bigotimes: ['\u2A02', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    bigoplus: ['\u2A01', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    bigodot: ['\u2A00', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    oint: ['\u222E', { texClass: MmlNode_js_1.TEXCLASS.OP }],
    bigsqcup: ['\u2A06', { texClass: MmlNode_js_1.TEXCLASS.OP,
            movesupsub: true }],
    smallint: ['\u222B', { largeop: false }],
    triangleleft: '\u25C3',
    triangleright: '\u25B9',
    bigtriangleup: '\u25B3',
    bigtriangledown: '\u25BD',
    wedge: '\u2227',
    land: '\u2227',
    vee: '\u2228',
    lor: '\u2228',
    cap: '\u2229',
    cup: '\u222A',
    ddagger: '\u2021',
    dagger: '\u2020',
    sqcap: '\u2293',
    sqcup: '\u2294',
    uplus: '\u228E',
    amalg: '\u2A3F',
    diamond: '\u22C4',
    bullet: '\u2219',
    wr: '\u2240',
    div: '\u00F7',
    divsymbol: '\u00F7',
    odot: ['\u2299', { largeop: false }],
    oslash: ['\u2298', { largeop: false }],
    otimes: ['\u2297', { largeop: false }],
    ominus: ['\u2296', { largeop: false }],
    oplus: ['\u2295', { largeop: false }],
    mp: '\u2213',
    pm: '\u00B1',
    circ: '\u2218',
    bigcirc: '\u25EF',
    setminus: '\u2216',
    cdot: '\u22C5',
    ast: '\u2217',
    times: '\u00D7',
    star: '\u22C6',
    propto: '\u221D',
    sqsubseteq: '\u2291',
    sqsupseteq: '\u2292',
    parallel: '\u2225',
    mid: '\u2223',
    dashv: '\u22A3',
    vdash: '\u22A2',
    leq: '\u2264',
    le: '\u2264',
    geq: '\u2265',
    ge: '\u2265',
    lt: '\u003C',
    gt: '\u003E',
    succ: '\u227B',
    prec: '\u227A',
    approx: '\u2248',
    succeq: '\u2AB0',
    preceq: '\u2AAF',
    supset: '\u2283',
    subset: '\u2282',
    supseteq: '\u2287',
    subseteq: '\u2286',
    'in': '\u2208',
    ni: '\u220B',
    notin: '\u2209',
    owns: '\u220B',
    gg: '\u226B',
    ll: '\u226A',
    sim: '\u223C',
    simeq: '\u2243',
    perp: '\u22A5',
    equiv: '\u2261',
    asymp: '\u224D',
    smile: '\u2323',
    frown: '\u2322',
    ne: '\u2260',
    neq: '\u2260',
    cong: '\u2245',
    doteq: '\u2250',
    bowtie: '\u22C8',
    models: '\u22A8',
    notChar: '\u29F8',
    Leftrightarrow: '\u21D4',
    Leftarrow: '\u21D0',
    Rightarrow: '\u21D2',
    leftrightarrow: '\u2194',
    leftarrow: '\u2190',
    gets: '\u2190',
    rightarrow: '\u2192',
    to: ['\u2192', { accent: false }],
    mapsto: '\u21A6',
    leftharpoonup: '\u21BC',
    leftharpoondown: '\u21BD',
    rightharpoonup: '\u21C0',
    rightharpoondown: '\u21C1',
    nearrow: '\u2197',
    searrow: '\u2198',
    nwarrow: '\u2196',
    swarrow: '\u2199',
    rightleftharpoons: '\u21CC',
    hookrightarrow: '\u21AA',
    hookleftarrow: '\u21A9',
    longleftarrow: '\u27F5',
    Longleftarrow: '\u27F8',
    longrightarrow: '\u27F6',
    Longrightarrow: '\u27F9',
    Longleftrightarrow: '\u27FA',
    longleftrightarrow: '\u27F7',
    longmapsto: '\u27FC',
    ldots: '\u2026',
    cdots: '\u22EF',
    vdots: '\u22EE',
    ddots: '\u22F1',
    dotsc: '\u2026',
    dotsb: '\u22EF',
    dotsm: '\u22EF',
    dotsi: '\u22EF',
    dotso: '\u2026',
    ldotp: ['\u002E', { texClass: MmlNode_js_1.TEXCLASS.PUNCT }],
    cdotp: ['\u22C5', { texClass: MmlNode_js_1.TEXCLASS.PUNCT }],
    colon: ['\u003A', { texClass: MmlNode_js_1.TEXCLASS.PUNCT }]
});
new sm.CharacterMap('mathchar7', ParseMethods_js_1.default.mathchar7, {
    Gamma: '\u0393',
    Delta: '\u0394',
    Theta: '\u0398',
    Lambda: '\u039B',
    Xi: '\u039E',
    Pi: '\u03A0',
    Sigma: '\u03A3',
    Upsilon: '\u03A5',
    Phi: '\u03A6',
    Psi: '\u03A8',
    Omega: '\u03A9',
    '_': '\u005F',
    '#': '\u0023',
    '$': '\u0024',
    '%': '\u0025',
    '&': '\u0026',
    And: '\u0026'
});
new sm.DelimiterMap('delimiter', ParseMethods_js_1.default.delimiter, {
    '(': '(',
    ')': ')',
    '[': '[',
    ']': ']',
    '<': '\u27E8',
    '>': '\u27E9',
    '\\lt': '\u27E8',
    '\\gt': '\u27E9',
    '/': '/',
    '|': ['|', { texClass: MmlNode_js_1.TEXCLASS.ORD }],
    '.': '',
    '\\\\': '\\',
    '\\lmoustache': '\u23B0',
    '\\rmoustache': '\u23B1',
    '\\lgroup': '\u27EE',
    '\\rgroup': '\u27EF',
    '\\arrowvert': '\u23D0',
    '\\Arrowvert': '\u2016',
    '\\bracevert': '\u23AA',
    '\\Vert': ['\u2016', { texClass: MmlNode_js_1.TEXCLASS.ORD }],
    '\\|': ['\u2016', { texClass: MmlNode_js_1.TEXCLASS.ORD }],
    '\\vert': ['|', { texClass: MmlNode_js_1.TEXCLASS.ORD }],
    '\\uparrow': '\u2191',
    '\\downarrow': '\u2193',
    '\\updownarrow': '\u2195',
    '\\Uparrow': '\u21D1',
    '\\Downarrow': '\u21D3',
    '\\Updownarrow': '\u21D5',
    '\\backslash': '\\',
    '\\rangle': '\u27E9',
    '\\langle': '\u27E8',
    '\\rbrace': '}',
    '\\lbrace': '{',
    '\\}': '}',
    '\\{': '{',
    '\\rceil': '\u2309',
    '\\lceil': '\u2308',
    '\\rfloor': '\u230B',
    '\\lfloor': '\u230A',
    '\\lbrack': '[',
    '\\rbrack': ']'
});
new sm.CommandMap('macros', {
    displaystyle: ['SetStyle', 'D', true, 0],
    textstyle: ['SetStyle', 'T', false, 0],
    scriptstyle: ['SetStyle', 'S', false, 1],
    scriptscriptstyle: ['SetStyle', 'SS', false, 2],
    rm: ['SetFont', TexConstants_js_1.TexConstant.Variant.NORMAL],
    mit: ['SetFont', TexConstants_js_1.TexConstant.Variant.ITALIC],
    oldstyle: ['SetFont', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    cal: ['SetFont', TexConstants_js_1.TexConstant.Variant.CALLIGRAPHIC],
    it: ['SetFont', TexConstants_js_1.TexConstant.Variant.MATHITALIC],
    bf: ['SetFont', TexConstants_js_1.TexConstant.Variant.BOLD],
    bbFont: ['SetFont', TexConstants_js_1.TexConstant.Variant.DOUBLESTRUCK],
    scr: ['SetFont', TexConstants_js_1.TexConstant.Variant.SCRIPT],
    frak: ['SetFont', TexConstants_js_1.TexConstant.Variant.FRAKTUR],
    sf: ['SetFont', TexConstants_js_1.TexConstant.Variant.SANSSERIF],
    tt: ['SetFont', TexConstants_js_1.TexConstant.Variant.MONOSPACE],
    mathrm: ['MathFont', TexConstants_js_1.TexConstant.Variant.NORMAL],
    mathup: ['MathFont', TexConstants_js_1.TexConstant.Variant.NORMAL],
    mathnormal: ['MathFont', ''],
    mathbf: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLD],
    mathbfup: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLD],
    mathit: ['MathFont', TexConstants_js_1.TexConstant.Variant.MATHITALIC],
    mathbfit: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDITALIC],
    mathbb: ['MathFont', TexConstants_js_1.TexConstant.Variant.DOUBLESTRUCK],
    Bbb: ['MathFont', TexConstants_js_1.TexConstant.Variant.DOUBLESTRUCK],
    mathfrak: ['MathFont', TexConstants_js_1.TexConstant.Variant.FRAKTUR],
    mathbffrak: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDFRAKTUR],
    mathscr: ['MathFont', TexConstants_js_1.TexConstant.Variant.SCRIPT],
    mathbfscr: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDSCRIPT],
    mathsf: ['MathFont', TexConstants_js_1.TexConstant.Variant.SANSSERIF],
    mathsfup: ['MathFont', TexConstants_js_1.TexConstant.Variant.SANSSERIF],
    mathbfsf: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDSANSSERIF],
    mathbfsfup: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDSANSSERIF],
    mathsfit: ['MathFont', TexConstants_js_1.TexConstant.Variant.SANSSERIFITALIC],
    mathbfsfit: ['MathFont', TexConstants_js_1.TexConstant.Variant.SANSSERIFBOLDITALIC],
    mathtt: ['MathFont', TexConstants_js_1.TexConstant.Variant.MONOSPACE],
    mathcal: ['MathFont', TexConstants_js_1.TexConstant.Variant.CALLIGRAPHIC],
    mathbfcal: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDCALLIGRAPHIC],
    symrm: ['MathFont', TexConstants_js_1.TexConstant.Variant.NORMAL],
    symup: ['MathFont', TexConstants_js_1.TexConstant.Variant.NORMAL],
    symnormal: ['MathFont', ''],
    symbf: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLD],
    symbfup: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLD],
    symit: ['MathFont', TexConstants_js_1.TexConstant.Variant.ITALIC],
    symbfit: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDITALIC],
    symbb: ['MathFont', TexConstants_js_1.TexConstant.Variant.DOUBLESTRUCK],
    symfrak: ['MathFont', TexConstants_js_1.TexConstant.Variant.FRAKTUR],
    symbffrak: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDFRAKTUR],
    symscr: ['MathFont', TexConstants_js_1.TexConstant.Variant.SCRIPT],
    symbfscr: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDSCRIPT],
    symsf: ['MathFont', TexConstants_js_1.TexConstant.Variant.SANSSERIF],
    symsfup: ['MathFont', TexConstants_js_1.TexConstant.Variant.SANSSERIF],
    symbfsf: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDSANSSERIF],
    symbfsfup: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDSANSSERIF],
    symsfit: ['MathFont', TexConstants_js_1.TexConstant.Variant.SANSSERIFITALIC],
    symbfsfit: ['MathFont', TexConstants_js_1.TexConstant.Variant.SANSSERIFBOLDITALIC],
    symtt: ['MathFont', TexConstants_js_1.TexConstant.Variant.MONOSPACE],
    symcal: ['MathFont', TexConstants_js_1.TexConstant.Variant.CALLIGRAPHIC],
    symbfcal: ['MathFont', TexConstants_js_1.TexConstant.Variant.BOLDCALLIGRAPHIC],
    textrm: ['HBox', null, TexConstants_js_1.TexConstant.Variant.NORMAL],
    textup: ['HBox', null, TexConstants_js_1.TexConstant.Variant.NORMAL],
    textnormal: ['HBox'],
    textit: ['HBox', null, TexConstants_js_1.TexConstant.Variant.ITALIC],
    textbf: ['HBox', null, TexConstants_js_1.TexConstant.Variant.BOLD],
    textsf: ['HBox', null, TexConstants_js_1.TexConstant.Variant.SANSSERIF],
    texttt: ['HBox', null, TexConstants_js_1.TexConstant.Variant.MONOSPACE],
    tiny: ['SetSize', 0.5],
    Tiny: ['SetSize', 0.6],
    scriptsize: ['SetSize', 0.7],
    small: ['SetSize', 0.85],
    normalsize: ['SetSize', 1.0],
    large: ['SetSize', 1.2],
    Large: ['SetSize', 1.44],
    LARGE: ['SetSize', 1.73],
    huge: ['SetSize', 2.07],
    Huge: ['SetSize', 2.49],
    arcsin: 'NamedFn',
    arccos: 'NamedFn',
    arctan: 'NamedFn',
    arg: 'NamedFn',
    cos: 'NamedFn',
    cosh: 'NamedFn',
    cot: 'NamedFn',
    coth: 'NamedFn',
    csc: 'NamedFn',
    deg: 'NamedFn',
    det: 'NamedOp',
    dim: 'NamedFn',
    exp: 'NamedFn',
    gcd: 'NamedOp',
    hom: 'NamedFn',
    inf: 'NamedOp',
    ker: 'NamedFn',
    lg: 'NamedFn',
    lim: 'NamedOp',
    liminf: ['NamedOp', 'lim&thinsp;inf'],
    limsup: ['NamedOp', 'lim&thinsp;sup'],
    ln: 'NamedFn',
    log: 'NamedFn',
    max: 'NamedOp',
    min: 'NamedOp',
    Pr: 'NamedOp',
    sec: 'NamedFn',
    sin: 'NamedFn',
    sinh: 'NamedFn',
    sup: 'NamedOp',
    tan: 'NamedFn',
    tanh: 'NamedFn',
    limits: ['Limits', 1],
    nolimits: ['Limits', 0],
    overline: ['UnderOver', '2015'],
    underline: ['UnderOver', '2015'],
    overbrace: ['UnderOver', '23DE', 1],
    underbrace: ['UnderOver', '23DF', 1],
    overparen: ['UnderOver', '23DC'],
    underparen: ['UnderOver', '23DD'],
    overrightarrow: ['UnderOver', '2192'],
    underrightarrow: ['UnderOver', '2192'],
    overleftarrow: ['UnderOver', '2190'],
    underleftarrow: ['UnderOver', '2190'],
    overleftrightarrow: ['UnderOver', '2194'],
    underleftrightarrow: ['UnderOver', '2194'],
    overset: 'Overset',
    underset: 'Underset',
    overunderset: 'Overunderset',
    stackrel: ['Macro', '\\mathrel{\\mathop{#2}\\limits^{#1}}', 2],
    stackbin: ['Macro', '\\mathbin{\\mathop{#2}\\limits^{#1}}', 2],
    over: 'Over',
    overwithdelims: 'Over',
    atop: 'Over',
    atopwithdelims: 'Over',
    above: 'Over',
    abovewithdelims: 'Over',
    brace: ['Over', '{', '}'],
    brack: ['Over', '[', ']'],
    choose: ['Over', '(', ')'],
    frac: 'Frac',
    sqrt: 'Sqrt',
    root: 'Root',
    uproot: ['MoveRoot', 'upRoot'],
    leftroot: ['MoveRoot', 'leftRoot'],
    left: 'LeftRight',
    right: 'LeftRight',
    middle: 'LeftRight',
    llap: 'Lap',
    rlap: 'Lap',
    raise: 'RaiseLower',
    lower: 'RaiseLower',
    moveleft: 'MoveLeftRight',
    moveright: 'MoveLeftRight',
    ',': ['Spacer', lengths_js_1.MATHSPACE.thinmathspace],
    ':': ['Spacer', lengths_js_1.MATHSPACE.mediummathspace],
    '>': ['Spacer', lengths_js_1.MATHSPACE.mediummathspace],
    ';': ['Spacer', lengths_js_1.MATHSPACE.thickmathspace],
    '!': ['Spacer', lengths_js_1.MATHSPACE.negativethinmathspace],
    enspace: ['Spacer', .5],
    quad: ['Spacer', 1],
    qquad: ['Spacer', 2],
    thinspace: ['Spacer', lengths_js_1.MATHSPACE.thinmathspace],
    negthinspace: ['Spacer', lengths_js_1.MATHSPACE.negativethinmathspace],
    hskip: 'Hskip',
    hspace: 'Hskip',
    kern: 'Hskip',
    mskip: 'Hskip',
    mspace: 'Hskip',
    mkern: 'Hskip',
    rule: 'rule',
    Rule: ['Rule'],
    Space: ['Rule', 'blank'],
    nonscript: 'Nonscript',
    big: ['MakeBig', MmlNode_js_1.TEXCLASS.ORD, 0.85],
    Big: ['MakeBig', MmlNode_js_1.TEXCLASS.ORD, 1.15],
    bigg: ['MakeBig', MmlNode_js_1.TEXCLASS.ORD, 1.45],
    Bigg: ['MakeBig', MmlNode_js_1.TEXCLASS.ORD, 1.75],
    bigl: ['MakeBig', MmlNode_js_1.TEXCLASS.OPEN, 0.85],
    Bigl: ['MakeBig', MmlNode_js_1.TEXCLASS.OPEN, 1.15],
    biggl: ['MakeBig', MmlNode_js_1.TEXCLASS.OPEN, 1.45],
    Biggl: ['MakeBig', MmlNode_js_1.TEXCLASS.OPEN, 1.75],
    bigr: ['MakeBig', MmlNode_js_1.TEXCLASS.CLOSE, 0.85],
    Bigr: ['MakeBig', MmlNode_js_1.TEXCLASS.CLOSE, 1.15],
    biggr: ['MakeBig', MmlNode_js_1.TEXCLASS.CLOSE, 1.45],
    Biggr: ['MakeBig', MmlNode_js_1.TEXCLASS.CLOSE, 1.75],
    bigm: ['MakeBig', MmlNode_js_1.TEXCLASS.REL, 0.85],
    Bigm: ['MakeBig', MmlNode_js_1.TEXCLASS.REL, 1.15],
    biggm: ['MakeBig', MmlNode_js_1.TEXCLASS.REL, 1.45],
    Biggm: ['MakeBig', MmlNode_js_1.TEXCLASS.REL, 1.75],
    mathord: ['TeXAtom', MmlNode_js_1.TEXCLASS.ORD],
    mathop: ['TeXAtom', MmlNode_js_1.TEXCLASS.OP],
    mathopen: ['TeXAtom', MmlNode_js_1.TEXCLASS.OPEN],
    mathclose: ['TeXAtom', MmlNode_js_1.TEXCLASS.CLOSE],
    mathbin: ['TeXAtom', MmlNode_js_1.TEXCLASS.BIN],
    mathrel: ['TeXAtom', MmlNode_js_1.TEXCLASS.REL],
    mathpunct: ['TeXAtom', MmlNode_js_1.TEXCLASS.PUNCT],
    mathinner: ['TeXAtom', MmlNode_js_1.TEXCLASS.INNER],
    vcenter: ['TeXAtom', MmlNode_js_1.TEXCLASS.VCENTER],
    buildrel: 'BuildRel',
    hbox: ['HBox', 0],
    text: 'HBox',
    mbox: ['HBox', 0],
    fbox: 'FBox',
    boxed: ['Macro', '\\fbox{$\\displaystyle{#1}$}', 1],
    framebox: 'FrameBox',
    strut: 'Strut',
    mathstrut: ['Macro', '\\vphantom{(}'],
    phantom: 'Phantom',
    vphantom: ['Phantom', 1, 0],
    hphantom: ['Phantom', 0, 1],
    smash: 'Smash',
    acute: ['Accent', '00B4'],
    grave: ['Accent', '0060'],
    ddot: ['Accent', '00A8'],
    tilde: ['Accent', '007E'],
    bar: ['Accent', '00AF'],
    breve: ['Accent', '02D8'],
    check: ['Accent', '02C7'],
    hat: ['Accent', '005E'],
    vec: ['Accent', '2192'],
    dot: ['Accent', '02D9'],
    widetilde: ['Accent', '007E', 1],
    widehat: ['Accent', '005E', 1],
    matrix: 'Matrix',
    array: 'Matrix',
    pmatrix: ['Matrix', '(', ')'],
    cases: ['Matrix', '{', '', 'left left', null, '.1em', null,
        true],
    eqalign: ['Matrix', null, null, 'right left',
        (0, lengths_js_1.em)(lengths_js_1.MATHSPACE.thickmathspace), '.5em', 'D'],
    displaylines: ['Matrix', null, null, 'center', null, '.5em', 'D'],
    cr: 'Cr',
    '\\': 'CrLaTeX',
    newline: ['CrLaTeX', true],
    hline: ['HLine', 'solid'],
    hdashline: ['HLine', 'dashed'],
    eqalignno: ['Matrix', null, null, 'right left',
        (0, lengths_js_1.em)(lengths_js_1.MATHSPACE.thickmathspace), '.5em', 'D', null,
        'right'],
    leqalignno: ['Matrix', null, null, 'right left',
        (0, lengths_js_1.em)(lengths_js_1.MATHSPACE.thickmathspace), '.5em', 'D', null,
        'left'],
    hfill: 'HFill',
    hfil: 'HFill',
    hfilll: 'HFill',
    bmod: ['Macro', '\\mmlToken{mo}[lspace="thickmathspace"' +
            ' rspace="thickmathspace"]{mod}'],
    pmod: ['Macro', '\\pod{\\mmlToken{mi}{mod}\\kern 6mu #1}', 1],
    mod: ['Macro', '\\mathchoice{\\kern18mu}{\\kern12mu}' +
            '{\\kern12mu}{\\kern12mu}\\mmlToken{mi}{mod}\\,\\,#1',
        1],
    pod: ['Macro', '\\mathchoice{\\kern18mu}{\\kern8mu}' +
            '{\\kern8mu}{\\kern8mu}(#1)', 1],
    iff: ['Macro', '\\;\\Longleftrightarrow\\;'],
    skew: ['Macro', '{{#2{#3\\mkern#1mu}\\mkern-#1mu}{}}', 3],
    pmb: ['Macro', '\\rlap{#1}\\kern1px{#1}', 1],
    TeX: ['Macro', 'T\\kern-.14em\\lower.5ex{E}\\kern-.115em X'],
    LaTeX: ['Macro', 'L\\kern-.325em\\raise.21em' +
            '{\\scriptstyle{A}}\\kern-.17em\\TeX'],
    ' ': ['Macro', '\\text{ }'],
    not: 'Not',
    dots: 'Dots',
    space: 'Tilde',
    '\u00A0': 'Tilde',
    begin: 'BeginEnd',
    end: 'BeginEnd',
    label: 'HandleLabel',
    ref: 'HandleRef',
    nonumber: 'HandleNoTag',
    mathchoice: 'MathChoice',
    mmlToken: 'MmlToken'
}, BaseMethods_js_1.default);
new sm.EnvironmentMap('environment', ParseMethods_js_1.default.environment, {
    array: ['AlignedArray'],
    equation: ['Equation', null, true],
    eqnarray: ['EqnArray', null, true, true, 'rcl',
        ParseUtil_js_1.default.cols(0, lengths_js_1.MATHSPACE.thickmathspace), '.5em']
}, BaseMethods_js_1.default);
new sm.CharacterMap('not_remap', null, {
    '\u2190': '\u219A',
    '\u2192': '\u219B',
    '\u2194': '\u21AE',
    '\u21D0': '\u21CD',
    '\u21D2': '\u21CF',
    '\u21D4': '\u21CE',
    '\u2208': '\u2209',
    '\u220B': '\u220C',
    '\u2223': '\u2224',
    '\u2225': '\u2226',
    '\u223C': '\u2241',
    '\u007E': '\u2241',
    '\u2243': '\u2244',
    '\u2245': '\u2247',
    '\u2248': '\u2249',
    '\u224D': '\u226D',
    '\u003D': '\u2260',
    '\u2261': '\u2262',
    '\u003C': '\u226E',
    '\u003E': '\u226F',
    '\u2264': '\u2270',
    '\u2265': '\u2271',
    '\u2272': '\u2274',
    '\u2273': '\u2275',
    '\u2276': '\u2278',
    '\u2277': '\u2279',
    '\u227A': '\u2280',
    '\u227B': '\u2281',
    '\u2282': '\u2284',
    '\u2283': '\u2285',
    '\u2286': '\u2288',
    '\u2287': '\u2289',
    '\u22A2': '\u22AC',
    '\u22A8': '\u22AD',
    '\u22A9': '\u22AE',
    '\u22AB': '\u22AF',
    '\u227C': '\u22E0',
    '\u227D': '\u22E1',
    '\u2291': '\u22E2',
    '\u2292': '\u22E3',
    '\u22B2': '\u22EA',
    '\u22B3': '\u22EB',
    '\u22B4': '\u22EC',
    '\u22B5': '\u22ED',
    '\u2203': '\u2204'
});
//# sourceMappingURL=BaseMappings.js.map

/***/ }),

/***/ 724:
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
var sitem = __importStar(__webpack_require__(389));
var NodeUtil_js_1 = __importDefault(__webpack_require__(321));
var TexError_js_1 = __importDefault(__webpack_require__(466));
var TexParser_js_1 = __importDefault(__webpack_require__(810));
var TexConstants_js_1 = __webpack_require__(7);
var ParseUtil_js_1 = __importDefault(__webpack_require__(702));
var MmlNode_js_1 = __webpack_require__(921);
var Tags_js_1 = __webpack_require__(251);
var lengths_js_1 = __webpack_require__(914);
var Entities_js_1 = __webpack_require__(29);
var Options_js_1 = __webpack_require__(77);
var BaseMethods = {};
var P_HEIGHT = 1.2 / .85;
var MmlTokenAllow = {
    fontfamily: 1, fontsize: 1, fontweight: 1, fontstyle: 1,
    color: 1, background: 1,
    id: 1, 'class': 1, href: 1, style: 1
};
BaseMethods.Open = function (parser, _c) {
    parser.Push(parser.itemFactory.create('open'));
};
BaseMethods.Close = function (parser, _c) {
    parser.Push(parser.itemFactory.create('close'));
};
BaseMethods.Tilde = function (parser, _c) {
    parser.Push(parser.create('token', 'mtext', {}, Entities_js_1.entities.nbsp));
};
BaseMethods.Space = function (_parser, _c) { };
BaseMethods.Superscript = function (parser, _c) {
    var _a;
    if (parser.GetNext().match(/\d/)) {
        parser.string = parser.string.substr(0, parser.i + 1) +
            ' ' + parser.string.substr(parser.i + 1);
    }
    var primes;
    var base;
    var top = parser.stack.Top();
    if (top.isKind('prime')) {
        _a = __read(top.Peek(2), 2), base = _a[0], primes = _a[1];
        parser.stack.Pop();
    }
    else {
        base = parser.stack.Prev();
        if (!base) {
            base = parser.create('token', 'mi', {}, '');
        }
    }
    var movesupsub = NodeUtil_js_1.default.getProperty(base, 'movesupsub');
    var position = NodeUtil_js_1.default.isType(base, 'msubsup') ? base.sup :
        base.over;
    if ((NodeUtil_js_1.default.isType(base, 'msubsup') && !NodeUtil_js_1.default.isType(base, 'msup') &&
        NodeUtil_js_1.default.getChildAt(base, base.sup)) ||
        (NodeUtil_js_1.default.isType(base, 'munderover') && !NodeUtil_js_1.default.isType(base, 'mover') &&
            NodeUtil_js_1.default.getChildAt(base, base.over) &&
            !NodeUtil_js_1.default.getProperty(base, 'subsupOK'))) {
        throw new TexError_js_1.default('DoubleExponent', 'Double exponent: use braces to clarify');
    }
    if (!NodeUtil_js_1.default.isType(base, 'msubsup') || NodeUtil_js_1.default.isType(base, 'msup')) {
        if (movesupsub) {
            if (!NodeUtil_js_1.default.isType(base, 'munderover') || NodeUtil_js_1.default.isType(base, 'mover') ||
                NodeUtil_js_1.default.getChildAt(base, base.over)) {
                base = parser.create('node', 'munderover', [base], { movesupsub: true });
            }
            position = base.over;
        }
        else {
            base = parser.create('node', 'msubsup', [base]);
            position = base.sup;
        }
    }
    parser.Push(parser.itemFactory.create('subsup', base).setProperties({
        position: position, primes: primes, movesupsub: movesupsub
    }));
};
BaseMethods.Subscript = function (parser, _c) {
    var _a;
    if (parser.GetNext().match(/\d/)) {
        parser.string =
            parser.string.substr(0, parser.i + 1) + ' ' +
                parser.string.substr(parser.i + 1);
    }
    var primes, base;
    var top = parser.stack.Top();
    if (top.isKind('prime')) {
        _a = __read(top.Peek(2), 2), base = _a[0], primes = _a[1];
        parser.stack.Pop();
    }
    else {
        base = parser.stack.Prev();
        if (!base) {
            base = parser.create('token', 'mi', {}, '');
        }
    }
    var movesupsub = NodeUtil_js_1.default.getProperty(base, 'movesupsub');
    var position = NodeUtil_js_1.default.isType(base, 'msubsup') ?
        base.sub : base.under;
    if ((NodeUtil_js_1.default.isType(base, 'msubsup') && !NodeUtil_js_1.default.isType(base, 'msup') &&
        NodeUtil_js_1.default.getChildAt(base, base.sub)) ||
        (NodeUtil_js_1.default.isType(base, 'munderover') && !NodeUtil_js_1.default.isType(base, 'mover') &&
            NodeUtil_js_1.default.getChildAt(base, base.under) &&
            !NodeUtil_js_1.default.getProperty(base, 'subsupOK'))) {
        throw new TexError_js_1.default('DoubleSubscripts', 'Double subscripts: use braces to clarify');
    }
    if (!NodeUtil_js_1.default.isType(base, 'msubsup') || NodeUtil_js_1.default.isType(base, 'msup')) {
        if (movesupsub) {
            if (!NodeUtil_js_1.default.isType(base, 'munderover') || NodeUtil_js_1.default.isType(base, 'mover') ||
                NodeUtil_js_1.default.getChildAt(base, base.under)) {
                base = parser.create('node', 'munderover', [base], { movesupsub: true });
            }
            position = base.under;
        }
        else {
            base = parser.create('node', 'msubsup', [base]);
            position = base.sub;
        }
    }
    parser.Push(parser.itemFactory.create('subsup', base).setProperties({
        position: position, primes: primes, movesupsub: movesupsub
    }));
};
BaseMethods.Prime = function (parser, c) {
    var base = parser.stack.Prev();
    if (!base) {
        base = parser.create('node', 'mi');
    }
    if (NodeUtil_js_1.default.isType(base, 'msubsup') && !NodeUtil_js_1.default.isType(base, 'msup') &&
        NodeUtil_js_1.default.getChildAt(base, base.sup)) {
        throw new TexError_js_1.default('DoubleExponentPrime', 'Prime causes double exponent: use braces to clarify');
    }
    var sup = '';
    parser.i--;
    do {
        sup += Entities_js_1.entities.prime;
        parser.i++, c = parser.GetNext();
    } while (c === '\'' || c === Entities_js_1.entities.rsquo);
    sup = ['', '\u2032', '\u2033', '\u2034', '\u2057'][sup.length] || sup;
    var node = parser.create('token', 'mo', { variantForm: true }, sup);
    parser.Push(parser.itemFactory.create('prime', base, node));
};
BaseMethods.Comment = function (parser, _c) {
    while (parser.i < parser.string.length && parser.string.charAt(parser.i) !== '\n') {
        parser.i++;
    }
};
BaseMethods.Hash = function (_parser, _c) {
    throw new TexError_js_1.default('CantUseHash1', 'You can\'t use \'macro parameter character #\' in math mode');
};
BaseMethods.MathFont = function (parser, name, variant) {
    var text = parser.GetArgument(name);
    var mml = new TexParser_js_1.default(text, __assign(__assign({}, parser.stack.env), { font: variant, multiLetterIdentifiers: /^[a-zA-Z]+/, noAutoOP: true }), parser.configuration).mml();
    parser.Push(parser.create('node', 'TeXAtom', [mml]));
};
BaseMethods.SetFont = function (parser, _name, font) {
    parser.stack.env['font'] = font;
};
BaseMethods.SetStyle = function (parser, _name, texStyle, style, level) {
    parser.stack.env['style'] = texStyle;
    parser.stack.env['level'] = level;
    parser.Push(parser.itemFactory.create('style').setProperty('styles', { displaystyle: style, scriptlevel: level }));
};
BaseMethods.SetSize = function (parser, _name, size) {
    parser.stack.env['size'] = size;
    parser.Push(parser.itemFactory.create('style').setProperty('styles', { mathsize: (0, lengths_js_1.em)(size) }));
};
BaseMethods.Spacer = function (parser, _name, space) {
    var node = parser.create('node', 'mspace', [], { width: (0, lengths_js_1.em)(space) });
    var style = parser.create('node', 'mstyle', [node], { scriptlevel: 0 });
    parser.Push(style);
};
BaseMethods.LeftRight = function (parser, name) {
    var first = name.substr(1);
    parser.Push(parser.itemFactory.create(first, parser.GetDelimiter(name), parser.stack.env.color));
};
BaseMethods.NamedFn = function (parser, name, id) {
    if (!id) {
        id = name.substr(1);
    }
    var mml = parser.create('token', 'mi', { texClass: MmlNode_js_1.TEXCLASS.OP }, id);
    parser.Push(parser.itemFactory.create('fn', mml));
};
BaseMethods.NamedOp = function (parser, name, id) {
    if (!id) {
        id = name.substr(1);
    }
    id = id.replace(/&thinsp;/, '\u2006');
    var mml = parser.create('token', 'mo', {
        movablelimits: true,
        movesupsub: true,
        form: TexConstants_js_1.TexConstant.Form.PREFIX,
        texClass: MmlNode_js_1.TEXCLASS.OP
    }, id);
    parser.Push(mml);
};
BaseMethods.Limits = function (parser, _name, limits) {
    var op = parser.stack.Prev(true);
    if (!op || (NodeUtil_js_1.default.getTexClass(NodeUtil_js_1.default.getCoreMO(op)) !== MmlNode_js_1.TEXCLASS.OP &&
        NodeUtil_js_1.default.getProperty(op, 'movesupsub') == null)) {
        throw new TexError_js_1.default('MisplacedLimits', '%1 is allowed only on operators', parser.currentCS);
    }
    var top = parser.stack.Top();
    var node;
    if (NodeUtil_js_1.default.isType(op, 'munderover') && !limits) {
        node = parser.create('node', 'msubsup');
        NodeUtil_js_1.default.copyChildren(op, node);
        op = top.Last = node;
    }
    else if (NodeUtil_js_1.default.isType(op, 'msubsup') && limits) {
        node = parser.create('node', 'munderover');
        NodeUtil_js_1.default.copyChildren(op, node);
        op = top.Last = node;
    }
    NodeUtil_js_1.default.setProperty(op, 'movesupsub', limits ? true : false);
    NodeUtil_js_1.default.setProperties(NodeUtil_js_1.default.getCoreMO(op), { 'movablelimits': false });
    if (NodeUtil_js_1.default.getAttribute(op, 'movablelimits') ||
        NodeUtil_js_1.default.getProperty(op, 'movablelimits')) {
        NodeUtil_js_1.default.setProperties(op, { 'movablelimits': false });
    }
};
BaseMethods.Over = function (parser, name, open, close) {
    var mml = parser.itemFactory.create('over').setProperty('name', parser.currentCS);
    if (open || close) {
        mml.setProperty('open', open);
        mml.setProperty('close', close);
    }
    else if (name.match(/withdelims$/)) {
        mml.setProperty('open', parser.GetDelimiter(name));
        mml.setProperty('close', parser.GetDelimiter(name));
    }
    if (name.match(/^\\above/)) {
        mml.setProperty('thickness', parser.GetDimen(name));
    }
    else if (name.match(/^\\atop/) || open || close) {
        mml.setProperty('thickness', 0);
    }
    parser.Push(mml);
};
BaseMethods.Frac = function (parser, name) {
    var num = parser.ParseArg(name);
    var den = parser.ParseArg(name);
    var node = parser.create('node', 'mfrac', [num, den]);
    parser.Push(node);
};
BaseMethods.Sqrt = function (parser, name) {
    var n = parser.GetBrackets(name);
    var arg = parser.GetArgument(name);
    if (arg === '\\frac') {
        arg += '{' + parser.GetArgument(arg) + '}{' + parser.GetArgument(arg) + '}';
    }
    var mml = new TexParser_js_1.default(arg, parser.stack.env, parser.configuration).mml();
    if (!n) {
        mml = parser.create('node', 'msqrt', [mml]);
    }
    else {
        mml = parser.create('node', 'mroot', [mml, parseRoot(parser, n)]);
    }
    parser.Push(mml);
};
function parseRoot(parser, n) {
    var env = parser.stack.env;
    var inRoot = env['inRoot'];
    env['inRoot'] = true;
    var newParser = new TexParser_js_1.default(n, env, parser.configuration);
    var node = newParser.mml();
    var global = newParser.stack.global;
    if (global['leftRoot'] || global['upRoot']) {
        var def = {};
        if (global['leftRoot']) {
            def['width'] = global['leftRoot'];
        }
        if (global['upRoot']) {
            def['voffset'] = global['upRoot'];
            def['height'] = global['upRoot'];
        }
        node = parser.create('node', 'mpadded', [node], def);
    }
    env['inRoot'] = inRoot;
    return node;
}
BaseMethods.Root = function (parser, name) {
    var n = parser.GetUpTo(name, '\\of');
    var arg = parser.ParseArg(name);
    var node = parser.create('node', 'mroot', [arg, parseRoot(parser, n)]);
    parser.Push(node);
};
BaseMethods.MoveRoot = function (parser, name, id) {
    if (!parser.stack.env['inRoot']) {
        throw new TexError_js_1.default('MisplacedMoveRoot', '%1 can appear only within a root', parser.currentCS);
    }
    if (parser.stack.global[id]) {
        throw new TexError_js_1.default('MultipleMoveRoot', 'Multiple use of %1', parser.currentCS);
    }
    var n = parser.GetArgument(name);
    if (!n.match(/-?[0-9]+/)) {
        throw new TexError_js_1.default('IntegerArg', 'The argument to %1 must be an integer', parser.currentCS);
    }
    n = (parseInt(n, 10) / 15) + 'em';
    if (n.substr(0, 1) !== '-') {
        n = '+' + n;
    }
    parser.stack.global[id] = n;
};
BaseMethods.Accent = function (parser, name, accent, stretchy) {
    var c = parser.ParseArg(name);
    var def = __assign(__assign({}, ParseUtil_js_1.default.getFontDef(parser)), { accent: true, mathaccent: true });
    var entity = NodeUtil_js_1.default.createEntity(accent);
    var moNode = parser.create('token', 'mo', def, entity);
    var mml = moNode;
    NodeUtil_js_1.default.setAttribute(mml, 'stretchy', stretchy ? true : false);
    var mo = (NodeUtil_js_1.default.isEmbellished(c) ? NodeUtil_js_1.default.getCoreMO(c) : c);
    if (NodeUtil_js_1.default.isType(mo, 'mo') || NodeUtil_js_1.default.getProperty(mo, 'movablelimits')) {
        NodeUtil_js_1.default.setProperties(mo, { 'movablelimits': false });
    }
    var muoNode = parser.create('node', 'munderover');
    NodeUtil_js_1.default.setChild(muoNode, 0, c);
    NodeUtil_js_1.default.setChild(muoNode, 1, null);
    NodeUtil_js_1.default.setChild(muoNode, 2, mml);
    var texAtom = parser.create('node', 'TeXAtom', [muoNode]);
    parser.Push(texAtom);
};
BaseMethods.UnderOver = function (parser, name, c, stack) {
    var entity = NodeUtil_js_1.default.createEntity(c);
    var mo = parser.create('token', 'mo', { stretchy: true, accent: true }, entity);
    var pos = (name.charAt(1) === 'o' ? 'over' : 'under');
    var base = parser.ParseArg(name);
    parser.Push(ParseUtil_js_1.default.underOver(parser, base, mo, pos, stack));
};
BaseMethods.Overset = function (parser, name) {
    var top = parser.ParseArg(name);
    var base = parser.ParseArg(name);
    ParseUtil_js_1.default.checkMovableLimits(base);
    if (top.isKind('mo')) {
        NodeUtil_js_1.default.setAttribute(top, 'accent', false);
    }
    var node = parser.create('node', 'mover', [base, top]);
    parser.Push(node);
};
BaseMethods.Underset = function (parser, name) {
    var bot = parser.ParseArg(name);
    var base = parser.ParseArg(name);
    ParseUtil_js_1.default.checkMovableLimits(base);
    if (bot.isKind('mo')) {
        NodeUtil_js_1.default.setAttribute(bot, 'accent', false);
    }
    var node = parser.create('node', 'munder', [base, bot], { accentunder: false });
    parser.Push(node);
};
BaseMethods.Overunderset = function (parser, name) {
    var top = parser.ParseArg(name);
    var bot = parser.ParseArg(name);
    var base = parser.ParseArg(name);
    ParseUtil_js_1.default.checkMovableLimits(base);
    if (top.isKind('mo')) {
        NodeUtil_js_1.default.setAttribute(top, 'accent', false);
    }
    if (bot.isKind('mo')) {
        NodeUtil_js_1.default.setAttribute(bot, 'accent', false);
    }
    var node = parser.create('node', 'munderover', [base, bot, top], { accent: false, accentunder: false });
    parser.Push(node);
};
BaseMethods.TeXAtom = function (parser, name, mclass) {
    var def = { texClass: mclass };
    var mml;
    var node;
    var parsed;
    if (mclass === MmlNode_js_1.TEXCLASS.OP) {
        def['movesupsub'] = def['movablelimits'] = true;
        var arg = parser.GetArgument(name);
        var match = arg.match(/^\s*\\rm\s+([a-zA-Z0-9 ]+)$/);
        if (match) {
            def['mathvariant'] = TexConstants_js_1.TexConstant.Variant.NORMAL;
            node = parser.create('token', 'mi', def, match[1]);
        }
        else {
            parsed = new TexParser_js_1.default(arg, parser.stack.env, parser.configuration).mml();
            node = parser.create('node', 'TeXAtom', [parsed], def);
        }
        mml = parser.itemFactory.create('fn', node);
    }
    else {
        parsed = parser.ParseArg(name);
        mml = parser.create('node', 'TeXAtom', [parsed], def);
    }
    parser.Push(mml);
};
BaseMethods.MmlToken = function (parser, name) {
    var kind = parser.GetArgument(name);
    var attr = parser.GetBrackets(name, '').replace(/^\s+/, '');
    var text = parser.GetArgument(name);
    var def = {};
    var keep = [];
    var node;
    try {
        node = parser.create('node', kind);
    }
    catch (e) {
        node = null;
    }
    if (!node || !node.isToken) {
        throw new TexError_js_1.default('NotMathMLToken', '%1 is not a token element', kind);
    }
    while (attr !== '') {
        var match = attr.match(/^([a-z]+)\s*=\s*('[^']*'|"[^"]*"|[^ ,]*)\s*,?\s*/i);
        if (!match) {
            throw new TexError_js_1.default('InvalidMathMLAttr', 'Invalid MathML attribute: %1', attr);
        }
        if (!node.attributes.hasDefault(match[1]) && !MmlTokenAllow[match[1]]) {
            throw new TexError_js_1.default('UnknownAttrForElement', '%1 is not a recognized attribute for %2', match[1], kind);
        }
        var value = ParseUtil_js_1.default.MmlFilterAttribute(parser, match[1], match[2].replace(/^(['"])(.*)\1$/, '$2'));
        if (value) {
            if (value.toLowerCase() === 'true') {
                value = true;
            }
            else if (value.toLowerCase() === 'false') {
                value = false;
            }
            def[match[1]] = value;
            keep.push(match[1]);
        }
        attr = attr.substr(match[0].length);
    }
    if (keep.length) {
        def['mjx-keep-attrs'] = keep.join(' ');
    }
    var textNode = parser.create('text', text);
    node.appendChild(textNode);
    NodeUtil_js_1.default.setProperties(node, def);
    parser.Push(node);
};
BaseMethods.Strut = function (parser, _name) {
    var row = parser.create('node', 'mrow');
    var padded = parser.create('node', 'mpadded', [row], { height: '8.6pt', depth: '3pt', width: 0 });
    parser.Push(padded);
};
BaseMethods.Phantom = function (parser, name, v, h) {
    var box = parser.create('node', 'mphantom', [parser.ParseArg(name)]);
    if (v || h) {
        box = parser.create('node', 'mpadded', [box]);
        if (h) {
            NodeUtil_js_1.default.setAttribute(box, 'height', 0);
            NodeUtil_js_1.default.setAttribute(box, 'depth', 0);
        }
        if (v) {
            NodeUtil_js_1.default.setAttribute(box, 'width', 0);
        }
    }
    var atom = parser.create('node', 'TeXAtom', [box]);
    parser.Push(atom);
};
BaseMethods.Smash = function (parser, name) {
    var bt = ParseUtil_js_1.default.trimSpaces(parser.GetBrackets(name, ''));
    var smash = parser.create('node', 'mpadded', [parser.ParseArg(name)]);
    switch (bt) {
        case 'b':
            NodeUtil_js_1.default.setAttribute(smash, 'depth', 0);
            break;
        case 't':
            NodeUtil_js_1.default.setAttribute(smash, 'height', 0);
            break;
        default:
            NodeUtil_js_1.default.setAttribute(smash, 'height', 0);
            NodeUtil_js_1.default.setAttribute(smash, 'depth', 0);
    }
    var atom = parser.create('node', 'TeXAtom', [smash]);
    parser.Push(atom);
};
BaseMethods.Lap = function (parser, name) {
    var mml = parser.create('node', 'mpadded', [parser.ParseArg(name)], { width: 0 });
    if (name === '\\llap') {
        NodeUtil_js_1.default.setAttribute(mml, 'lspace', '-1width');
    }
    var atom = parser.create('node', 'TeXAtom', [mml]);
    parser.Push(atom);
};
BaseMethods.RaiseLower = function (parser, name) {
    var h = parser.GetDimen(name);
    var item = parser.itemFactory.create('position').setProperties({ name: parser.currentCS, move: 'vertical' });
    if (h.charAt(0) === '-') {
        h = h.slice(1);
        name = name.substr(1) === 'raise' ? '\\lower' : '\\raise';
    }
    if (name === '\\lower') {
        item.setProperty('dh', '-' + h);
        item.setProperty('dd', '+' + h);
    }
    else {
        item.setProperty('dh', '+' + h);
        item.setProperty('dd', '-' + h);
    }
    parser.Push(item);
};
BaseMethods.MoveLeftRight = function (parser, name) {
    var h = parser.GetDimen(name);
    var nh = (h.charAt(0) === '-' ? h.slice(1) : '-' + h);
    if (name === '\\moveleft') {
        var tmp = h;
        h = nh;
        nh = tmp;
    }
    parser.Push(parser.itemFactory.create('position').setProperties({
        name: parser.currentCS, move: 'horizontal',
        left: parser.create('node', 'mspace', [], { width: h }),
        right: parser.create('node', 'mspace', [], { width: nh })
    }));
};
BaseMethods.Hskip = function (parser, name) {
    var node = parser.create('node', 'mspace', [], { width: parser.GetDimen(name) });
    parser.Push(node);
};
BaseMethods.Nonscript = function (parser, _name) {
    parser.Push(parser.itemFactory.create('nonscript'));
};
BaseMethods.Rule = function (parser, name, style) {
    var w = parser.GetDimen(name), h = parser.GetDimen(name), d = parser.GetDimen(name);
    var def = { width: w, height: h, depth: d };
    if (style !== 'blank') {
        def['mathbackground'] = (parser.stack.env['color'] || 'black');
    }
    var node = parser.create('node', 'mspace', [], def);
    parser.Push(node);
};
BaseMethods.rule = function (parser, name) {
    var v = parser.GetBrackets(name), w = parser.GetDimen(name), h = parser.GetDimen(name);
    var mml = parser.create('node', 'mspace', [], {
        width: w, height: h,
        mathbackground: (parser.stack.env['color'] || 'black')
    });
    if (v) {
        mml = parser.create('node', 'mpadded', [mml], { voffset: v });
        if (v.match(/^\-/)) {
            NodeUtil_js_1.default.setAttribute(mml, 'height', v);
            NodeUtil_js_1.default.setAttribute(mml, 'depth', '+' + v.substr(1));
        }
        else {
            NodeUtil_js_1.default.setAttribute(mml, 'height', '+' + v);
        }
    }
    parser.Push(mml);
};
BaseMethods.MakeBig = function (parser, name, mclass, size) {
    size *= P_HEIGHT;
    var sizeStr = String(size).replace(/(\.\d\d\d).+/, '$1') + 'em';
    var delim = parser.GetDelimiter(name, true);
    var mo = parser.create('token', 'mo', {
        minsize: sizeStr, maxsize: sizeStr,
        fence: true, stretchy: true, symmetric: true
    }, delim);
    var node = parser.create('node', 'TeXAtom', [mo], { texClass: mclass });
    parser.Push(node);
};
BaseMethods.BuildRel = function (parser, name) {
    var top = parser.ParseUpTo(name, '\\over');
    var bot = parser.ParseArg(name);
    var node = parser.create('node', 'munderover');
    NodeUtil_js_1.default.setChild(node, 0, bot);
    NodeUtil_js_1.default.setChild(node, 1, null);
    NodeUtil_js_1.default.setChild(node, 2, top);
    var atom = parser.create('node', 'TeXAtom', [node], { texClass: MmlNode_js_1.TEXCLASS.REL });
    parser.Push(atom);
};
BaseMethods.HBox = function (parser, name, style, font) {
    parser.PushAll(ParseUtil_js_1.default.internalMath(parser, parser.GetArgument(name), style, font));
};
BaseMethods.FBox = function (parser, name) {
    var internal = ParseUtil_js_1.default.internalMath(parser, parser.GetArgument(name));
    var node = parser.create('node', 'menclose', internal, { notation: 'box' });
    parser.Push(node);
};
BaseMethods.FrameBox = function (parser, name) {
    var width = parser.GetBrackets(name);
    var pos = parser.GetBrackets(name) || 'c';
    var mml = ParseUtil_js_1.default.internalMath(parser, parser.GetArgument(name));
    if (width) {
        mml = [parser.create('node', 'mpadded', mml, {
                width: width,
                'data-align': (0, Options_js_1.lookup)(pos, { l: 'left', r: 'right' }, 'center')
            })];
    }
    var node = parser.create('node', 'TeXAtom', [parser.create('node', 'menclose', mml, { notation: 'box' })], { texClass: MmlNode_js_1.TEXCLASS.ORD });
    parser.Push(node);
};
BaseMethods.Not = function (parser, _name) {
    parser.Push(parser.itemFactory.create('not'));
};
BaseMethods.Dots = function (parser, _name) {
    var ldotsEntity = NodeUtil_js_1.default.createEntity('2026');
    var cdotsEntity = NodeUtil_js_1.default.createEntity('22EF');
    var ldots = parser.create('token', 'mo', { stretchy: false }, ldotsEntity);
    var cdots = parser.create('token', 'mo', { stretchy: false }, cdotsEntity);
    parser.Push(parser.itemFactory.create('dots').setProperties({
        ldots: ldots,
        cdots: cdots
    }));
};
BaseMethods.Matrix = function (parser, _name, open, close, align, spacing, vspacing, style, cases, numbered) {
    var c = parser.GetNext();
    if (c === '') {
        throw new TexError_js_1.default('MissingArgFor', 'Missing argument for %1', parser.currentCS);
    }
    if (c === '{') {
        parser.i++;
    }
    else {
        parser.string = c + '}' + parser.string.slice(parser.i + 1);
        parser.i = 0;
    }
    var array = parser.itemFactory.create('array').setProperty('requireClose', true);
    array.arraydef = {
        rowspacing: (vspacing || '4pt'),
        columnspacing: (spacing || '1em')
    };
    if (cases) {
        array.setProperty('isCases', true);
    }
    if (numbered) {
        array.setProperty('isNumbered', true);
        array.arraydef.side = numbered;
    }
    if (open || close) {
        array.setProperty('open', open);
        array.setProperty('close', close);
    }
    if (style === 'D') {
        array.arraydef.displaystyle = true;
    }
    if (align != null) {
        array.arraydef.columnalign = align;
    }
    parser.Push(array);
};
BaseMethods.Entry = function (parser, name) {
    parser.Push(parser.itemFactory.create('cell').setProperties({ isEntry: true, name: name }));
    var top = parser.stack.Top();
    var env = top.getProperty('casesEnv');
    var cases = top.getProperty('isCases');
    if (!cases && !env)
        return;
    var str = parser.string;
    var braces = 0, close = -1, i = parser.i, m = str.length;
    var end = (env ? new RegExp("^\\\\end\\s*\\{".concat(env.replace(/\*/, '\\*'), "\\}")) : null);
    while (i < m) {
        var c = str.charAt(i);
        if (c === '{') {
            braces++;
            i++;
        }
        else if (c === '}') {
            if (braces === 0) {
                m = 0;
            }
            else {
                braces--;
                if (braces === 0 && close < 0) {
                    close = i - parser.i;
                }
                i++;
            }
        }
        else if (c === '&' && braces === 0) {
            throw new TexError_js_1.default('ExtraAlignTab', 'Extra alignment tab in \\cases text');
        }
        else if (c === '\\') {
            var rest = str.substr(i);
            if (rest.match(/^((\\cr)[^a-zA-Z]|\\\\)/) || (end && rest.match(end))) {
                m = 0;
            }
            else {
                i += 2;
            }
        }
        else {
            i++;
        }
    }
    var text = str.substr(parser.i, i - parser.i);
    if (!text.match(/^\s*\\text[^a-zA-Z]/) || close !== text.replace(/\s+$/, '').length - 1) {
        var internal = ParseUtil_js_1.default.internalMath(parser, ParseUtil_js_1.default.trimSpaces(text), 0);
        parser.PushAll(internal);
        parser.i = i;
    }
};
BaseMethods.Cr = function (parser, name) {
    parser.Push(parser.itemFactory.create('cell').setProperties({ isCR: true, name: name }));
};
BaseMethods.CrLaTeX = function (parser, name, nobrackets) {
    if (nobrackets === void 0) { nobrackets = false; }
    var n;
    if (!nobrackets) {
        if (parser.string.charAt(parser.i) === '*') {
            parser.i++;
        }
        if (parser.string.charAt(parser.i) === '[') {
            var dim = parser.GetBrackets(name, '');
            var _a = __read(ParseUtil_js_1.default.matchDimen(dim), 2), value = _a[0], unit = _a[1];
            if (dim && !value) {
                throw new TexError_js_1.default('BracketMustBeDimension', 'Bracket argument to %1 must be a dimension', parser.currentCS);
            }
            n = value + unit;
        }
    }
    parser.Push(parser.itemFactory.create('cell').setProperties({ isCR: true, name: name, linebreak: true }));
    var top = parser.stack.Top();
    var node;
    if (top instanceof sitem.ArrayItem) {
        if (n) {
            top.addRowSpacing(n);
        }
    }
    else {
        if (n) {
            node = parser.create('node', 'mspace', [], { depth: n });
            parser.Push(node);
        }
        node = parser.create('node', 'mspace', [], { linebreak: TexConstants_js_1.TexConstant.LineBreak.NEWLINE });
        parser.Push(node);
    }
};
BaseMethods.HLine = function (parser, _name, style) {
    if (style == null) {
        style = 'solid';
    }
    var top = parser.stack.Top();
    if (!(top instanceof sitem.ArrayItem) || top.Size()) {
        throw new TexError_js_1.default('Misplaced', 'Misplaced %1', parser.currentCS);
    }
    if (!top.table.length) {
        top.frame.push('top');
    }
    else {
        var lines = (top.arraydef['rowlines'] ? top.arraydef['rowlines'].split(/ /) : []);
        while (lines.length < top.table.length) {
            lines.push('none');
        }
        lines[top.table.length - 1] = style;
        top.arraydef['rowlines'] = lines.join(' ');
    }
};
BaseMethods.HFill = function (parser, _name) {
    var top = parser.stack.Top();
    if (top instanceof sitem.ArrayItem) {
        top.hfill.push(top.Size());
    }
    else {
        throw new TexError_js_1.default('UnsupportedHFill', 'Unsupported use of %1', parser.currentCS);
    }
};
BaseMethods.BeginEnd = function (parser, name) {
    var env = parser.GetArgument(name);
    if (env.match(/\\/i)) {
        throw new TexError_js_1.default('InvalidEnv', 'Invalid environment name \'%1\'', env);
    }
    var macro = parser.configuration.handlers.get('environment').lookup(env);
    if (macro && name === '\\end') {
        if (!macro.args[0]) {
            var mml = parser.itemFactory.create('end').setProperty('name', env);
            parser.Push(mml);
            return;
        }
        parser.stack.env['closing'] = env;
    }
    ParseUtil_js_1.default.checkMaxMacros(parser, false);
    parser.parse('environment', [parser, env]);
};
BaseMethods.Array = function (parser, begin, open, close, align, spacing, vspacing, style, raggedHeight) {
    if (!align) {
        align = parser.GetArgument('\\begin{' + begin.getName() + '}');
    }
    var lines = ('c' + align).replace(/[^clr|:]/g, '').replace(/[^|:]([|:])+/g, '$1');
    align = align.replace(/[^clr]/g, '').split('').join(' ');
    align = align.replace(/l/g, 'left').replace(/r/g, 'right').replace(/c/g, 'center');
    var array = parser.itemFactory.create('array');
    array.arraydef = {
        columnalign: align,
        columnspacing: (spacing || '1em'),
        rowspacing: (vspacing || '4pt')
    };
    if (lines.match(/[|:]/)) {
        if (lines.charAt(0).match(/[|:]/)) {
            array.frame.push('left');
            array.dashed = lines.charAt(0) === ':';
        }
        if (lines.charAt(lines.length - 1).match(/[|:]/)) {
            array.frame.push('right');
        }
        lines = lines.substr(1, lines.length - 2);
        array.arraydef.columnlines =
            lines.split('').join(' ').replace(/[^|: ]/g, 'none').replace(/\|/g, 'solid').replace(/:/g, 'dashed');
    }
    if (open) {
        array.setProperty('open', parser.convertDelimiter(open));
    }
    if (close) {
        array.setProperty('close', parser.convertDelimiter(close));
    }
    if ((style || '').charAt(1) === '\'') {
        array.arraydef['data-cramped'] = true;
        style = style.charAt(0);
    }
    if (style === 'D') {
        array.arraydef['displaystyle'] = true;
    }
    else if (style) {
        array.arraydef['displaystyle'] = false;
    }
    if (style === 'S') {
        array.arraydef['scriptlevel'] = 1;
    }
    if (raggedHeight) {
        array.arraydef['useHeight'] = false;
    }
    parser.Push(begin);
    return array;
};
BaseMethods.AlignedArray = function (parser, begin) {
    var align = parser.GetBrackets('\\begin{' + begin.getName() + '}');
    var item = BaseMethods.Array(parser, begin);
    return ParseUtil_js_1.default.setArrayAlign(item, align);
};
BaseMethods.Equation = function (parser, begin, numbered) {
    parser.Push(begin);
    ParseUtil_js_1.default.checkEqnEnv(parser);
    return parser.itemFactory.create('equation', numbered).
        setProperty('name', begin.getName());
};
BaseMethods.EqnArray = function (parser, begin, numbered, taggable, align, spacing) {
    parser.Push(begin);
    if (taggable) {
        ParseUtil_js_1.default.checkEqnEnv(parser);
    }
    align = align.replace(/[^clr]/g, '').split('').join(' ');
    align = align.replace(/l/g, 'left').replace(/r/g, 'right').replace(/c/g, 'center');
    var newItem = parser.itemFactory.create('eqnarray', begin.getName(), numbered, taggable, parser.stack.global);
    newItem.arraydef = {
        displaystyle: true,
        columnalign: align,
        columnspacing: (spacing || '1em'),
        rowspacing: '3pt',
        side: parser.options['tagSide'],
        minlabelspacing: parser.options['tagIndent']
    };
    return newItem;
};
BaseMethods.HandleNoTag = function (parser, _name) {
    parser.tags.notag();
};
BaseMethods.HandleLabel = function (parser, name) {
    var label = parser.GetArgument(name);
    if (label === '') {
        return;
    }
    if (!parser.tags.refUpdate) {
        if (parser.tags.label) {
            throw new TexError_js_1.default('MultipleCommand', 'Multiple %1', parser.currentCS);
        }
        parser.tags.label = label;
        if ((parser.tags.allLabels[label] || parser.tags.labels[label]) && !parser.options['ignoreDuplicateLabels']) {
            throw new TexError_js_1.default('MultipleLabel', 'Label \'%1\' multiply defined', label);
        }
        parser.tags.labels[label] = new Tags_js_1.Label();
    }
};
BaseMethods.HandleRef = function (parser, name, eqref) {
    var label = parser.GetArgument(name);
    var ref = parser.tags.allLabels[label] || parser.tags.labels[label];
    if (!ref) {
        if (!parser.tags.refUpdate) {
            parser.tags.redo = true;
        }
        ref = new Tags_js_1.Label();
    }
    var tag = ref.tag;
    if (eqref) {
        tag = parser.tags.formatTag(tag);
    }
    var node = parser.create('node', 'mrow', ParseUtil_js_1.default.internalMath(parser, tag), {
        href: parser.tags.formatUrl(ref.id, parser.options.baseURL), 'class': 'MathJax_ref'
    });
    parser.Push(node);
};
BaseMethods.Macro = function (parser, name, macro, argcount, def) {
    if (argcount) {
        var args = [];
        if (def != null) {
            var optional = parser.GetBrackets(name);
            args.push(optional == null ? def : optional);
        }
        for (var i = args.length; i < argcount; i++) {
            args.push(parser.GetArgument(name));
        }
        macro = ParseUtil_js_1.default.substituteArgs(parser, args, macro);
    }
    parser.string = ParseUtil_js_1.default.addArgs(parser, macro, parser.string.slice(parser.i));
    parser.i = 0;
    ParseUtil_js_1.default.checkMaxMacros(parser);
};
BaseMethods.MathChoice = function (parser, name) {
    var D = parser.ParseArg(name);
    var T = parser.ParseArg(name);
    var S = parser.ParseArg(name);
    var SS = parser.ParseArg(name);
    parser.Push(parser.create('node', 'MathChoice', [D, T, S, SS]));
};
exports["default"] = BaseMethods;
//# sourceMappingURL=BaseMethods.js.map

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

/***/ 946:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlMo = MathJax._.core.MmlTree.MmlNodes.mo.MmlMo;

/***/ }),

/***/ 857:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.OPDEF = MathJax._.core.MmlTree.OperatorDictionary.OPDEF;
exports.MO = MathJax._.core.MmlTree.OperatorDictionary.MO;
exports.RANGES = MathJax._.core.MmlTree.OperatorDictionary.RANGES;
exports.getRange = MathJax._.core.MmlTree.OperatorDictionary.getRange;
exports.MMLSPACING = MathJax._.core.MmlTree.OperatorDictionary.MMLSPACING;
exports.OPTABLE = MathJax._.core.MmlTree.OperatorDictionary.OPTABLE;

/***/ }),

/***/ 752:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.AbstractFactory = MathJax._.core.Tree.Factory.AbstractFactory;

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

/***/ }),

/***/ 297:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.PrioritizedList = MathJax._.util.PrioritizedList.PrioritizedList;

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

/***/ }),

/***/ 720:
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
// EXTERNAL MODULE: ../../../../js/input/tex.js
var tex = __webpack_require__(205);
// EXTERNAL MODULE: ../../../../js/input/tex/Configuration.js
var Configuration = __webpack_require__(552);
// EXTERNAL MODULE: ../../../../js/input/tex/FilterUtil.js
var FilterUtil = __webpack_require__(199);
// EXTERNAL MODULE: ../../../../js/input/tex/FindTeX.js
var FindTeX = __webpack_require__(982);
// EXTERNAL MODULE: ../../../../js/input/tex/MapHandler.js
var MapHandler = __webpack_require__(910);
// EXTERNAL MODULE: ../../../../js/input/tex/NodeFactory.js
var NodeFactory = __webpack_require__(644);
// EXTERNAL MODULE: ../../../../js/input/tex/NodeUtil.js
var NodeUtil = __webpack_require__(321);
// EXTERNAL MODULE: ../../../../js/input/tex/ParseMethods.js
var ParseMethods = __webpack_require__(708);
// EXTERNAL MODULE: ../../../../js/input/tex/ParseOptions.js
var ParseOptions = __webpack_require__(394);
// EXTERNAL MODULE: ../../../../js/input/tex/ParseUtil.js
var ParseUtil = __webpack_require__(702);
// EXTERNAL MODULE: ../../../../js/input/tex/Stack.js
var Stack = __webpack_require__(874);
// EXTERNAL MODULE: ../../../../js/input/tex/StackItem.js
var StackItem = __webpack_require__(44);
// EXTERNAL MODULE: ../../../../js/input/tex/StackItemFactory.js
var StackItemFactory = __webpack_require__(239);
// EXTERNAL MODULE: ../../../../js/input/tex/Symbol.js
var Symbol = __webpack_require__(237);
// EXTERNAL MODULE: ../../../../js/input/tex/SymbolMap.js
var SymbolMap = __webpack_require__(628);
// EXTERNAL MODULE: ../../../../js/input/tex/Tags.js
var Tags = __webpack_require__(251);
// EXTERNAL MODULE: ../../../../js/input/tex/TexConstants.js
var TexConstants = __webpack_require__(7);
// EXTERNAL MODULE: ../../../../js/input/tex/TexError.js
var TexError = __webpack_require__(466);
// EXTERNAL MODULE: ../../../../js/input/tex/TexParser.js
var TexParser = __webpack_require__(810);
// EXTERNAL MODULE: ../../../../js/input/tex/base/BaseConfiguration.js
var BaseConfiguration = __webpack_require__(606);
// EXTERNAL MODULE: ../../../../js/input/tex/base/BaseItems.js
var BaseItems = __webpack_require__(389);
// EXTERNAL MODULE: ../../../../js/input/tex/base/BaseMethods.js
var BaseMethods = __webpack_require__(724);
;// CONCATENATED MODULE: ./lib/tex-base.js

























if (MathJax.loader) {
  MathJax.loader.checkVersion('input/tex-base', version/* VERSION */.q, 'input');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex_ts: tex,
      tex: {
        Configuration: Configuration,
        FilterUtil: FilterUtil,
        FindTeX: FindTeX,
        MapHandler: MapHandler,
        NodeFactory: NodeFactory,
        NodeUtil: NodeUtil,
        ParseMethods: ParseMethods,
        ParseOptions: ParseOptions,
        ParseUtil: ParseUtil,
        Stack: Stack,
        StackItem: StackItem,
        StackItemFactory: StackItemFactory,
        Symbol: Symbol,
        SymbolMap: SymbolMap,
        Tags: Tags,
        TexConstants: TexConstants,
        TexError: TexError,
        TexParser: TexParser,
        base: {
          BaseConfiguration: BaseConfiguration,
          BaseItems: BaseItems,
          BaseMethods: BaseMethods
        }
      }
    }
  }
});
// EXTERNAL MODULE: ../../core/lib/util/Options.js
var Options = __webpack_require__(77);
;// CONCATENATED MODULE: ../tex/register.js

function registerTeX() {
  var packageList = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : [];
  var tex = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : true;

  if (MathJax.startup) {
    if (tex) {
      MathJax.startup.registerConstructor('tex', MathJax._.input.tex_ts.TeX);
      MathJax.startup.useInput('tex');
    }

    if (!MathJax.config.tex) {
      MathJax.config.tex = {};
    }

    var packages = MathJax.config.tex.packages;
    MathJax.config.tex.packages = packageList;

    if (packages) {
      (0,Options.insert)(MathJax.config.tex, {
        packages: packages
      });
    }
  }
}
;// CONCATENATED MODULE: ./tex-base.js


registerTeX(['base']);
}();
/******/ })()
;