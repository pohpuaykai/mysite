/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 515:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MathJax = exports.combineWithMathJax = exports.combineDefaults = exports.combineConfig = exports.isObject = void 0;
var version_js_1 = __webpack_require__(282);
function isObject(x) {
    return typeof x === 'object' && x !== null;
}
exports.isObject = isObject;
function combineConfig(dst, src) {
    var e_1, _a;
    try {
        for (var _b = __values(Object.keys(src)), _c = _b.next(); !_c.done; _c = _b.next()) {
            var id = _c.value;
            if (id === '__esModule')
                continue;
            if (isObject(dst[id]) && isObject(src[id]) &&
                !(src[id] instanceof Promise)) {
                combineConfig(dst[id], src[id]);
            }
            else if (src[id] !== null && src[id] !== undefined) {
                dst[id] = src[id];
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
    return dst;
}
exports.combineConfig = combineConfig;
function combineDefaults(dst, name, src) {
    var e_2, _a;
    if (!dst[name]) {
        dst[name] = {};
    }
    dst = dst[name];
    try {
        for (var _b = __values(Object.keys(src)), _c = _b.next(); !_c.done; _c = _b.next()) {
            var id = _c.value;
            if (isObject(dst[id]) && isObject(src[id])) {
                combineDefaults(dst, id, src[id]);
            }
            else if (dst[id] == null && src[id] != null) {
                dst[id] = src[id];
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
    return dst;
}
exports.combineDefaults = combineDefaults;
function combineWithMathJax(config) {
    return combineConfig(exports.MathJax, config);
}
exports.combineWithMathJax = combineWithMathJax;
if (typeof __webpack_require__.g.MathJax === 'undefined') {
    __webpack_require__.g.MathJax = {};
}
if (!__webpack_require__.g.MathJax.version) {
    __webpack_require__.g.MathJax = {
        version: version_js_1.VERSION,
        _: {},
        config: __webpack_require__.g.MathJax
    };
}
exports.MathJax = __webpack_require__.g.MathJax;
//# sourceMappingURL=global.js.map

/***/ }),

/***/ 235:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

var __dirname = "/";

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
var e_1, _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CONFIG = exports.MathJax = exports.Loader = exports.PathFilters = exports.PackageError = exports.Package = void 0;
var global_js_1 = __webpack_require__(515);
var package_js_1 = __webpack_require__(265);
var package_js_2 = __webpack_require__(265);
Object.defineProperty(exports, "Package", ({ enumerable: true, get: function () { return package_js_2.Package; } }));
Object.defineProperty(exports, "PackageError", ({ enumerable: true, get: function () { return package_js_2.PackageError; } }));
var FunctionList_js_1 = __webpack_require__(525);
exports.PathFilters = {
    source: function (data) {
        if (exports.CONFIG.source.hasOwnProperty(data.name)) {
            data.name = exports.CONFIG.source[data.name];
        }
        return true;
    },
    normalize: function (data) {
        var name = data.name;
        if (!name.match(/^(?:[a-z]+:\/)?\/|[a-z]:\\|\[/i)) {
            data.name = '[mathjax]/' + name.replace(/^\.\//, '');
        }
        if (data.addExtension && !name.match(/\.[^\/]+$/)) {
            data.name += '.js';
        }
        return true;
    },
    prefix: function (data) {
        var match;
        while ((match = data.name.match(/^\[([^\]]*)\]/))) {
            if (!exports.CONFIG.paths.hasOwnProperty(match[1]))
                break;
            data.name = exports.CONFIG.paths[match[1]] + data.name.substr(match[0].length);
        }
        return true;
    }
};
var Loader;
(function (Loader) {
    var VERSION = global_js_1.MathJax.version;
    Loader.versions = new Map();
    function ready() {
        var e_2, _a;
        var names = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            names[_i] = arguments[_i];
        }
        if (names.length === 0) {
            names = Array.from(package_js_1.Package.packages.keys());
        }
        var promises = [];
        try {
            for (var names_1 = __values(names), names_1_1 = names_1.next(); !names_1_1.done; names_1_1 = names_1.next()) {
                var name_1 = names_1_1.value;
                var extension = package_js_1.Package.packages.get(name_1) || new package_js_1.Package(name_1, true);
                promises.push(extension.promise);
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (names_1_1 && !names_1_1.done && (_a = names_1.return)) _a.call(names_1);
            }
            finally { if (e_2) throw e_2.error; }
        }
        return Promise.all(promises);
    }
    Loader.ready = ready;
    function load() {
        var e_3, _a;
        var names = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            names[_i] = arguments[_i];
        }
        if (names.length === 0) {
            return Promise.resolve();
        }
        var promises = [];
        var _loop_1 = function (name_2) {
            var extension = package_js_1.Package.packages.get(name_2);
            if (!extension) {
                extension = new package_js_1.Package(name_2);
                extension.provides(exports.CONFIG.provides[name_2]);
            }
            extension.checkNoLoad();
            promises.push(extension.promise.then(function () {
                if (!exports.CONFIG.versionWarnings)
                    return;
                if (extension.isLoaded && !Loader.versions.has(package_js_1.Package.resolvePath(name_2))) {
                    console.warn("No version information available for component ".concat(name_2));
                }
            }));
        };
        try {
            for (var names_2 = __values(names), names_2_1 = names_2.next(); !names_2_1.done; names_2_1 = names_2.next()) {
                var name_2 = names_2_1.value;
                _loop_1(name_2);
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (names_2_1 && !names_2_1.done && (_a = names_2.return)) _a.call(names_2);
            }
            finally { if (e_3) throw e_3.error; }
        }
        package_js_1.Package.loadAll();
        return Promise.all(promises);
    }
    Loader.load = load;
    function preLoad() {
        var e_4, _a;
        var names = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            names[_i] = arguments[_i];
        }
        try {
            for (var names_3 = __values(names), names_3_1 = names_3.next(); !names_3_1.done; names_3_1 = names_3.next()) {
                var name_3 = names_3_1.value;
                var extension = package_js_1.Package.packages.get(name_3);
                if (!extension) {
                    extension = new package_js_1.Package(name_3, true);
                    extension.provides(exports.CONFIG.provides[name_3]);
                }
                extension.loaded();
            }
        }
        catch (e_4_1) { e_4 = { error: e_4_1 }; }
        finally {
            try {
                if (names_3_1 && !names_3_1.done && (_a = names_3.return)) _a.call(names_3);
            }
            finally { if (e_4) throw e_4.error; }
        }
    }
    Loader.preLoad = preLoad;
    function defaultReady() {
        if (typeof exports.MathJax.startup !== 'undefined') {
            exports.MathJax.config.startup.ready();
        }
    }
    Loader.defaultReady = defaultReady;
    function getRoot() {
        var root = __dirname + '/../../es5';
        if (typeof document !== 'undefined') {
            var script = document.currentScript || document.getElementById('MathJax-script');
            if (script) {
                root = script.src.replace(/\/[^\/]*$/, '');
            }
        }
        return root;
    }
    Loader.getRoot = getRoot;
    function checkVersion(name, version, _type) {
        Loader.versions.set(package_js_1.Package.resolvePath(name), VERSION);
        if (exports.CONFIG.versionWarnings && version !== VERSION) {
            console.warn("Component ".concat(name, " uses ").concat(version, " of MathJax; version in use is ").concat(VERSION));
            return true;
        }
        return false;
    }
    Loader.checkVersion = checkVersion;
    Loader.pathFilters = new FunctionList_js_1.FunctionList();
    Loader.pathFilters.add(exports.PathFilters.source, 0);
    Loader.pathFilters.add(exports.PathFilters.normalize, 10);
    Loader.pathFilters.add(exports.PathFilters.prefix, 20);
})(Loader = exports.Loader || (exports.Loader = {}));
exports.MathJax = global_js_1.MathJax;
if (typeof exports.MathJax.loader === 'undefined') {
    (0, global_js_1.combineDefaults)(exports.MathJax.config, 'loader', {
        paths: {
            mathjax: Loader.getRoot()
        },
        source: {},
        dependencies: {},
        provides: {},
        load: [],
        ready: Loader.defaultReady.bind(Loader),
        failed: function (error) { return console.log("MathJax(".concat(error.package || '?', "): ").concat(error.message)); },
        require: null,
        pathFilters: [],
        versionWarnings: true
    });
    (0, global_js_1.combineWithMathJax)({
        loader: Loader
    });
    try {
        for (var _b = __values(exports.MathJax.config.loader.pathFilters), _c = _b.next(); !_c.done; _c = _b.next()) {
            var filter = _c.value;
            if (Array.isArray(filter)) {
                Loader.pathFilters.add(filter[0], filter[1]);
            }
            else {
                Loader.pathFilters.add(filter);
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
}
exports.CONFIG = exports.MathJax.config.loader;
//# sourceMappingURL=loader.js.map

/***/ }),

/***/ 265:
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
exports.Package = exports.PackageError = void 0;
var loader_js_1 = __webpack_require__(235);
var PackageError = (function (_super) {
    __extends(PackageError, _super);
    function PackageError(message, name) {
        var _this = _super.call(this, message) || this;
        _this.package = name;
        return _this;
    }
    return PackageError;
}(Error));
exports.PackageError = PackageError;
var Package = (function () {
    function Package(name, noLoad) {
        if (noLoad === void 0) { noLoad = false; }
        this.isLoaded = false;
        this.isLoading = false;
        this.hasFailed = false;
        this.dependents = [];
        this.dependencies = [];
        this.dependencyCount = 0;
        this.provided = [];
        this.name = name;
        this.noLoad = noLoad;
        Package.packages.set(name, this);
        this.promise = this.makePromise(this.makeDependencies());
    }
    Object.defineProperty(Package.prototype, "canLoad", {
        get: function () {
            return this.dependencyCount === 0 && !this.noLoad && !this.isLoading && !this.hasFailed;
        },
        enumerable: false,
        configurable: true
    });
    Package.resolvePath = function (name, addExtension) {
        if (addExtension === void 0) { addExtension = true; }
        var data = { name: name, original: name, addExtension: addExtension };
        loader_js_1.Loader.pathFilters.execute(data);
        return data.name;
    };
    Package.loadAll = function () {
        var e_1, _a;
        try {
            for (var _b = __values(this.packages.values()), _c = _b.next(); !_c.done; _c = _b.next()) {
                var extension = _c.value;
                if (extension.canLoad) {
                    extension.load();
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
    Package.prototype.makeDependencies = function () {
        var e_2, _a;
        var promises = [];
        var map = Package.packages;
        var noLoad = this.noLoad;
        var name = this.name;
        var dependencies = [];
        if (loader_js_1.CONFIG.dependencies.hasOwnProperty(name)) {
            dependencies.push.apply(dependencies, __spreadArray([], __read(loader_js_1.CONFIG.dependencies[name]), false));
        }
        else if (name !== 'core') {
            dependencies.push('core');
        }
        try {
            for (var dependencies_1 = __values(dependencies), dependencies_1_1 = dependencies_1.next(); !dependencies_1_1.done; dependencies_1_1 = dependencies_1.next()) {
                var dependent = dependencies_1_1.value;
                var extension = map.get(dependent) || new Package(dependent, noLoad);
                if (this.dependencies.indexOf(extension) < 0) {
                    extension.addDependent(this, noLoad);
                    this.dependencies.push(extension);
                    if (!extension.isLoaded) {
                        this.dependencyCount++;
                        promises.push(extension.promise);
                    }
                }
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (dependencies_1_1 && !dependencies_1_1.done && (_a = dependencies_1.return)) _a.call(dependencies_1);
            }
            finally { if (e_2) throw e_2.error; }
        }
        return promises;
    };
    Package.prototype.makePromise = function (promises) {
        var _this = this;
        var promise = new Promise((function (resolve, reject) {
            _this.resolve = resolve;
            _this.reject = reject;
        }));
        var config = (loader_js_1.CONFIG[this.name] || {});
        if (config.ready) {
            promise = promise.then(function (_name) { return config.ready(_this.name); });
        }
        if (promises.length) {
            promises.push(promise);
            promise = Promise.all(promises).then(function (names) { return names.join(', '); });
        }
        if (config.failed) {
            promise.catch(function (message) { return config.failed(new PackageError(message, _this.name)); });
        }
        return promise;
    };
    Package.prototype.load = function () {
        if (!this.isLoaded && !this.isLoading && !this.noLoad) {
            this.isLoading = true;
            var url = Package.resolvePath(this.name);
            if (loader_js_1.CONFIG.require) {
                this.loadCustom(url);
            }
            else {
                this.loadScript(url);
            }
        }
    };
    Package.prototype.loadCustom = function (url) {
        var _this = this;
        try {
            var result = loader_js_1.CONFIG.require(url);
            if (result instanceof Promise) {
                result.then(function () { return _this.checkLoad(); })
                    .catch(function (err) { return _this.failed('Can\'t load "' + url + '"\n' + err.message.trim()); });
            }
            else {
                this.checkLoad();
            }
        }
        catch (err) {
            this.failed(err.message);
        }
    };
    Package.prototype.loadScript = function (url) {
        var _this = this;
        var script = document.createElement('script');
        script.src = url;
        script.charset = 'UTF-8';
        script.onload = function (_event) { return _this.checkLoad(); };
        script.onerror = function (_event) { return _this.failed('Can\'t load "' + url + '"'); };
        document.head.appendChild(script);
    };
    Package.prototype.loaded = function () {
        var e_3, _a, e_4, _b;
        this.isLoaded = true;
        this.isLoading = false;
        try {
            for (var _c = __values(this.dependents), _d = _c.next(); !_d.done; _d = _c.next()) {
                var dependent = _d.value;
                dependent.requirementSatisfied();
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (_d && !_d.done && (_a = _c.return)) _a.call(_c);
            }
            finally { if (e_3) throw e_3.error; }
        }
        try {
            for (var _e = __values(this.provided), _f = _e.next(); !_f.done; _f = _e.next()) {
                var provided = _f.value;
                provided.loaded();
            }
        }
        catch (e_4_1) { e_4 = { error: e_4_1 }; }
        finally {
            try {
                if (_f && !_f.done && (_b = _e.return)) _b.call(_e);
            }
            finally { if (e_4) throw e_4.error; }
        }
        this.resolve(this.name);
    };
    Package.prototype.failed = function (message) {
        this.hasFailed = true;
        this.isLoading = false;
        this.reject(new PackageError(message, this.name));
    };
    Package.prototype.checkLoad = function () {
        var _this = this;
        var config = (loader_js_1.CONFIG[this.name] || {});
        var checkReady = config.checkReady || (function () { return Promise.resolve(); });
        checkReady().then(function () { return _this.loaded(); })
            .catch(function (message) { return _this.failed(message); });
    };
    Package.prototype.requirementSatisfied = function () {
        if (this.dependencyCount) {
            this.dependencyCount--;
            if (this.canLoad) {
                this.load();
            }
        }
    };
    Package.prototype.provides = function (names) {
        var e_5, _a;
        if (names === void 0) { names = []; }
        try {
            for (var names_1 = __values(names), names_1_1 = names_1.next(); !names_1_1.done; names_1_1 = names_1.next()) {
                var name_1 = names_1_1.value;
                var provided = Package.packages.get(name_1);
                if (!provided) {
                    if (!loader_js_1.CONFIG.dependencies[name_1]) {
                        loader_js_1.CONFIG.dependencies[name_1] = [];
                    }
                    loader_js_1.CONFIG.dependencies[name_1].push(name_1);
                    provided = new Package(name_1, true);
                    provided.isLoading = true;
                }
                this.provided.push(provided);
            }
        }
        catch (e_5_1) { e_5 = { error: e_5_1 }; }
        finally {
            try {
                if (names_1_1 && !names_1_1.done && (_a = names_1.return)) _a.call(names_1);
            }
            finally { if (e_5) throw e_5.error; }
        }
    };
    Package.prototype.addDependent = function (extension, noLoad) {
        this.dependents.push(extension);
        if (!noLoad) {
            this.checkNoLoad();
        }
    };
    Package.prototype.checkNoLoad = function () {
        var e_6, _a;
        if (this.noLoad) {
            this.noLoad = false;
            try {
                for (var _b = __values(this.dependencies), _c = _b.next(); !_c.done; _c = _b.next()) {
                    var dependency = _c.value;
                    dependency.checkNoLoad();
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
    };
    Package.packages = new Map();
    return Package;
}());
exports.Package = Package;
//# sourceMappingURL=package.js.map

/***/ }),

/***/ 282:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.VERSION = void 0;
exports.VERSION = '3.2.2';
//# sourceMappingURL=version.js.map

/***/ }),

/***/ 525:
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
exports.FunctionList = void 0;
var PrioritizedList_js_1 = __webpack_require__(666);
var FunctionList = (function (_super) {
    __extends(FunctionList, _super);
    function FunctionList() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    FunctionList.prototype.execute = function () {
        var e_1, _a;
        var data = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            data[_i] = arguments[_i];
        }
        try {
            for (var _b = __values(this), _c = _b.next(); !_c.done; _c = _b.next()) {
                var item = _c.value;
                var result = item.item.apply(item, __spreadArray([], __read(data), false));
                if (result === false) {
                    return false;
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
        return true;
    };
    FunctionList.prototype.asyncExecute = function () {
        var data = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            data[_i] = arguments[_i];
        }
        var i = -1;
        var items = this.items;
        return new Promise(function (ok, fail) {
            (function execute() {
                var _a;
                while (++i < items.length) {
                    var result = (_a = items[i]).item.apply(_a, __spreadArray([], __read(data), false));
                    if (result instanceof Promise) {
                        result.then(execute).catch(function (err) { return fail(err); });
                        return;
                    }
                    if (result === false) {
                        ok(false);
                        return;
                    }
                }
                ok(true);
            })();
        });
    };
    return FunctionList;
}(PrioritizedList_js_1.PrioritizedList));
exports.FunctionList = FunctionList;
//# sourceMappingURL=FunctionList.js.map

/***/ }),

/***/ 666:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.PrioritizedList = void 0;
var PrioritizedList = (function () {
    function PrioritizedList() {
        this.items = [];
        this.items = [];
    }
    PrioritizedList.prototype[Symbol.iterator] = function () {
        var i = 0;
        var items = this.items;
        return {
            next: function () {
                return { value: items[i++], done: (i > items.length) };
            }
        };
    };
    PrioritizedList.prototype.add = function (item, priority) {
        if (priority === void 0) { priority = PrioritizedList.DEFAULTPRIORITY; }
        var i = this.items.length;
        do {
            i--;
        } while (i >= 0 && priority < this.items[i].priority);
        this.items.splice(i + 1, 0, { item: item, priority: priority });
        return item;
    };
    PrioritizedList.prototype.remove = function (item) {
        var i = this.items.length;
        do {
            i--;
        } while (i >= 0 && this.items[i].item !== item);
        if (i >= 0) {
            this.items.splice(i, 1);
        }
    };
    PrioritizedList.DEFAULTPRIORITY = 5;
    return PrioritizedList;
}());
exports.PrioritizedList = PrioritizedList;
//# sourceMappingURL=PrioritizedList.js.map

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
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
!function() {

// EXTERNAL MODULE: ../../../js/components/global.js
var global = __webpack_require__(515);
// EXTERNAL MODULE: ../../../js/components/version.js
var version = __webpack_require__(282);
// EXTERNAL MODULE: ../../../js/components/loader.js
var loader = __webpack_require__(235);
// EXTERNAL MODULE: ../../../js/components/package.js
var components_package = __webpack_require__(265);
;// CONCATENATED MODULE: ./lib/loader.js





if (MathJax.loader) {
  MathJax.loader.checkVersion('loader', version.VERSION, 'loader');
}

(0,global.combineWithMathJax)({
  _: {
    components: {
      loader: loader,
      "package": components_package
    }
  }
});
;// CONCATENATED MODULE: ../dependencies.js
function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }

function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _iterableToArray(iter) { if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter); }

function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

/*************************************************************
 *
 *  Copyright (c) 2019-2021 The MathJax Consortium
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
var dependencies = {
  'a11y/semantic-enrich': ['input/mml', 'a11y/sre'],
  'a11y/complexity': ['a11y/semantic-enrich'],
  'a11y/explorer': ['a11y/semantic-enrich', 'ui/menu'],
  '[mml]/mml3': ['input/mml'],
  '[tex]/all-packages': ['input/tex-base'],
  '[tex]/action': ['input/tex-base', '[tex]/newcommand'],
  '[tex]/autoload': ['input/tex-base', '[tex]/require'],
  '[tex]/ams': ['input/tex-base'],
  '[tex]/amscd': ['input/tex-base'],
  '[tex]/bbox': ['input/tex-base', '[tex]/ams', '[tex]/newcommand'],
  '[tex]/boldsymbol': ['input/tex-base'],
  '[tex]/braket': ['input/tex-base'],
  '[tex]/bussproofs': ['input/tex-base'],
  '[tex]/cancel': ['input/tex-base', '[tex]/enclose'],
  '[tex]/centernot': ['input/tex-base'],
  '[tex]/color': ['input/tex-base'],
  '[tex]/colorv2': ['input/tex-base'],
  '[tex]/colortbl': ['input/tex-base', '[tex]/color'],
  '[tex]/configmacros': ['input/tex-base', '[tex]/newcommand'],
  '[tex]/enclose': ['input/tex-base'],
  '[tex]/extpfeil': ['input/tex-base', '[tex]/newcommand', '[tex]/ams'],
  '[tex]/html': ['input/tex-base'],
  '[tex]/mathtools': ['input/tex-base', '[tex]/newcommand', '[tex]/ams'],
  '[tex]/mhchem': ['input/tex-base', '[tex]/ams'],
  '[tex]/newcommand': ['input/tex-base'],
  '[tex]/noerrors': ['input/tex-base'],
  '[tex]/noundefined': ['input/tex-base'],
  '[tex]/physics': ['input/tex-base'],
  '[tex]/require': ['input/tex-base'],
  '[tex]/setoptions': ['input/tex-base'],
  '[tex]/tagformat': ['input/tex-base'],
  '[tex]/textcomp': ['input/tex-base', '[tex]/textmacros'],
  '[tex]/textmacros': ['input/tex-base'],
  '[tex]/unicode': ['input/tex-base'],
  '[tex]/verb': ['input/tex-base'],
  '[tex]/cases': ['[tex]/empheq'],
  '[tex]/empheq': ['input/tex-base', '[tex]/ams']
};
var paths = {
  tex: '[mathjax]/input/tex/extensions',
  mml: '[mathjax]/input/mml/extensions',
  sre: '[mathjax]/sre/mathmaps'
};
var allPackages = Array.from(Object.keys(dependencies)).filter(function (name) {
  return name.substr(0, 5) === '[tex]' && name !== '[tex]/autoload' && name !== '[tex]/colorv2' && name !== '[tex]/all-packages';
});
var provides = {
  'startup': ['loader'],
  'input/tex': ['input/tex-base', '[tex]/ams', '[tex]/newcommand', '[tex]/noundefined', '[tex]/require', '[tex]/autoload', '[tex]/configmacros'],
  'input/tex-full': ['input/tex-base', '[tex]/all-packages'].concat(_toConsumableArray(allPackages)),
  '[tex]/all-packages': allPackages
}; //
//  Compatibility with v3.0 names for TeX extensions
//

var compatibility = {
  '[tex]/amsCd': '[tex]/amscd',
  '[tex]/colorV2': '[tex]/colorv2',
  '[tex]/configMacros': '[tex]/configmacros',
  '[tex]/tagFormat': '[tex]/tagformat'
};
;// CONCATENATED MODULE: ./loader.js
function loader_toConsumableArray(arr) { return loader_arrayWithoutHoles(arr) || loader_iterableToArray(arr) || loader_unsupportedIterableToArray(arr) || loader_nonIterableSpread(); }

function loader_nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function loader_unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return loader_arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return loader_arrayLikeToArray(o, minLen); }

function loader_iterableToArray(iter) { if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter); }

function loader_arrayWithoutHoles(arr) { if (Array.isArray(arr)) return loader_arrayLikeToArray(arr); }

function loader_arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }





(0,global.combineDefaults)(MathJax.config.loader, 'dependencies', dependencies);
(0,global.combineDefaults)(MathJax.config.loader, 'paths', paths);
(0,global.combineDefaults)(MathJax.config.loader, 'provides', provides);
loader.Loader.load.apply(loader.Loader, loader_toConsumableArray(loader.CONFIG.load)).then(function () {
  return loader.CONFIG.ready();
})["catch"](function (message, name) {
  return loader.CONFIG.failed(message, name);
});
}();
/******/ })()
;