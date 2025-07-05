/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 667:
/***/ (function(__unused_webpack_module, exports) {

var __webpack_unused_export__;

__webpack_unused_export__ = ({ value: true });
exports.q = void 0;
exports.q = '3.2.2';
//# sourceMappingURL=version.js.map

/***/ }),

/***/ 778:
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
exports.RequireConfiguration = exports.options = exports.RequireMethods = exports.RequireLoad = void 0;
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var TexError_js_1 = __importDefault(__webpack_require__(402));
var global_js_1 = __webpack_require__(955);
var package_js_1 = __webpack_require__(629);
var loader_js_1 = __webpack_require__(282);
var mathjax_js_1 = __webpack_require__(149);
var Options_js_1 = __webpack_require__(74);
var MJCONFIG = global_js_1.MathJax.config;
function RegisterExtension(jax, name) {
    var _a;
    var require = jax.parseOptions.options.require;
    var required = jax.parseOptions.packageData.get('require').required;
    var extension = name.substr(require.prefix.length);
    if (required.indexOf(extension) < 0) {
        required.push(extension);
        RegisterDependencies(jax, loader_js_1.CONFIG.dependencies[name]);
        var handler = Configuration_js_1.ConfigurationHandler.get(extension);
        if (handler) {
            var options_1 = MJCONFIG[name] || {};
            if (handler.options && Object.keys(handler.options).length === 1 && handler.options[extension]) {
                options_1 = (_a = {}, _a[extension] = options_1, _a);
            }
            jax.configuration.add(extension, jax, options_1);
            var configured = jax.parseOptions.packageData.get('require').configured;
            if (handler.preprocessors.length && !configured.has(extension)) {
                configured.set(extension, true);
                mathjax_js_1.mathjax.retryAfter(Promise.resolve());
            }
        }
    }
}
function RegisterDependencies(jax, names) {
    var e_1, _a;
    if (names === void 0) { names = []; }
    var prefix = jax.parseOptions.options.require.prefix;
    try {
        for (var names_1 = __values(names), names_1_1 = names_1.next(); !names_1_1.done; names_1_1 = names_1.next()) {
            var name_1 = names_1_1.value;
            if (name_1.substr(0, prefix.length) === prefix) {
                RegisterExtension(jax, name_1);
            }
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (names_1_1 && !names_1_1.done && (_a = names_1.return)) _a.call(names_1);
        }
        finally { if (e_1) throw e_1.error; }
    }
}
function RequireLoad(parser, name) {
    var options = parser.options.require;
    var allow = options.allow;
    var extension = (name.substr(0, 1) === '[' ? '' : options.prefix) + name;
    var allowed = (allow.hasOwnProperty(extension) ? allow[extension] :
        allow.hasOwnProperty(name) ? allow[name] : options.defaultAllow);
    if (!allowed) {
        throw new TexError_js_1.default('BadRequire', 'Extension "%1" is not allowed to be loaded', extension);
    }
    if (package_js_1.Package.packages.has(extension)) {
        RegisterExtension(parser.configuration.packageData.get('require').jax, extension);
    }
    else {
        mathjax_js_1.mathjax.retryAfter(loader_js_1.Loader.load(extension));
    }
}
exports.RequireLoad = RequireLoad;
function config(_config, jax) {
    jax.parseOptions.packageData.set('require', {
        jax: jax,
        required: __spreadArray([], __read(jax.options.packages), false),
        configured: new Map()
    });
    var options = jax.parseOptions.options.require;
    var prefix = options.prefix;
    if (prefix.match(/[^_a-zA-Z0-9]/)) {
        throw Error('Illegal characters used in \\require prefix');
    }
    if (!loader_js_1.CONFIG.paths[prefix]) {
        loader_js_1.CONFIG.paths[prefix] = '[mathjax]/input/tex/extensions';
    }
    options.prefix = '[' + prefix + ']/';
}
exports.RequireMethods = {
    Require: function (parser, name) {
        var required = parser.GetArgument(name);
        if (required.match(/[^_a-zA-Z0-9]/) || required === '') {
            throw new TexError_js_1.default('BadPackageName', 'Argument for %1 is not a valid package name', name);
        }
        RequireLoad(parser, required);
    }
};
exports.options = {
    require: {
        allow: (0, Options_js_1.expandable)({
            base: false,
            'all-packages': false,
            autoload: false,
            configmacros: false,
            tagformat: false,
            setoptions: false
        }),
        defaultAllow: true,
        prefix: 'tex'
    }
};
new SymbolMap_js_1.CommandMap('require', { require: 'Require' }, exports.RequireMethods);
exports.RequireConfiguration = Configuration_js_1.Configuration.create('require', { handler: { macro: ['require'] }, config: config, options: exports.options });
//# sourceMappingURL=RequireConfiguration.js.map

/***/ }),

/***/ 955:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.isObject = MathJax._.components.global.isObject;
exports.combineConfig = MathJax._.components.global.combineConfig;
exports.combineDefaults = MathJax._.components.global.combineDefaults;
exports.combineWithMathJax = MathJax._.components.global.combineWithMathJax;
exports.MathJax = MathJax._.components.global.MathJax;

/***/ }),

/***/ 149:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.mathjax = MathJax._.mathjax.mathjax;

/***/ }),

/***/ 74:
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

/***/ 251:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Configuration = MathJax._.input.tex.Configuration.Configuration;
exports.ConfigurationHandler = MathJax._.input.tex.Configuration.ConfigurationHandler;
exports.ParserConfiguration = MathJax._.input.tex.Configuration.ParserConfiguration;

/***/ }),

/***/ 871:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.parseResult = MathJax._.input.tex.SymbolMap.parseResult;
exports.AbstractSymbolMap = MathJax._.input.tex.SymbolMap.AbstractSymbolMap;
exports.RegExpMap = MathJax._.input.tex.SymbolMap.RegExpMap;
exports.AbstractParseMap = MathJax._.input.tex.SymbolMap.AbstractParseMap;
exports.CharacterMap = MathJax._.input.tex.SymbolMap.CharacterMap;
exports.DelimiterMap = MathJax._.input.tex.SymbolMap.DelimiterMap;
exports.MacroMap = MathJax._.input.tex.SymbolMap.MacroMap;
exports.CommandMap = MathJax._.input.tex.SymbolMap.CommandMap;
exports.EnvironmentMap = MathJax._.input.tex.SymbolMap.EnvironmentMap;

/***/ }),

/***/ 402:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.TexError["default"];

/***/ }),

/***/ 282:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.PathFilters = MathJax._.components.loader.PathFilters;
exports.Loader = MathJax._.components.loader.Loader;
exports.MathJax = MathJax._.components.loader.MathJax;
exports.CONFIG = MathJax._.components.loader.CONFIG;

/***/ }),

/***/ 629:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.PackageError = MathJax._.components["package"].PackageError;
exports.Package = MathJax._.components["package"].Package;

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

// EXTERNAL MODULE: ../../../../core/lib/components/global.js
var global = __webpack_require__(955);
// EXTERNAL MODULE: ../../../../../../js/components/version.js
var version = __webpack_require__(667);
// EXTERNAL MODULE: ../../../../../../js/input/tex/require/RequireConfiguration.js
var RequireConfiguration = __webpack_require__(778);
;// CONCATENATED MODULE: ./lib/require.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/require', version/* VERSION */.q, 'tex-extension');
}

(0,global.combineWithMathJax)({
  _: {
    input: {
      tex: {
        require: {
          RequireConfiguration: RequireConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./require.js

}();
/******/ })()
;