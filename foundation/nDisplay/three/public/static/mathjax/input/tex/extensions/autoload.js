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

/***/ 275:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.AutoloadConfiguration = void 0;
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var Symbol_js_1 = __webpack_require__(924);
var RequireConfiguration_js_1 = __webpack_require__(96);
var package_js_1 = __webpack_require__(629);
var Options_js_1 = __webpack_require__(74);
function Autoload(parser, name, extension, isMacro) {
    var e_1, _a, e_2, _b;
    if (package_js_1.Package.packages.has(parser.options.require.prefix + extension)) {
        var def = parser.options.autoload[extension];
        var _c = __read((def.length === 2 && Array.isArray(def[0]) ? def : [def, []]), 2), macros = _c[0], envs = _c[1];
        try {
            for (var macros_1 = __values(macros), macros_1_1 = macros_1.next(); !macros_1_1.done; macros_1_1 = macros_1.next()) {
                var macro = macros_1_1.value;
                AutoloadMacros.remove(macro);
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (macros_1_1 && !macros_1_1.done && (_a = macros_1.return)) _a.call(macros_1);
            }
            finally { if (e_1) throw e_1.error; }
        }
        try {
            for (var envs_1 = __values(envs), envs_1_1 = envs_1.next(); !envs_1_1.done; envs_1_1 = envs_1.next()) {
                var env = envs_1_1.value;
                AutoloadEnvironments.remove(env);
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (envs_1_1 && !envs_1_1.done && (_b = envs_1.return)) _b.call(envs_1);
            }
            finally { if (e_2) throw e_2.error; }
        }
        parser.string = (isMacro ? name + ' ' : '\\begin{' + name.slice(1) + '}') + parser.string.slice(parser.i);
        parser.i = 0;
    }
    (0, RequireConfiguration_js_1.RequireLoad)(parser, extension);
}
function initAutoload(config) {
    if (!config.options.require) {
        (0, Options_js_1.defaultOptions)(config.options, RequireConfiguration_js_1.RequireConfiguration.options);
    }
}
function configAutoload(config, jax) {
    var e_3, _a, e_4, _b, e_5, _c;
    var parser = jax.parseOptions;
    var macros = parser.handlers.get('macro');
    var environments = parser.handlers.get('environment');
    var autoload = parser.options.autoload;
    parser.packageData.set('autoload', { Autoload: Autoload });
    try {
        for (var _d = __values(Object.keys(autoload)), _e = _d.next(); !_e.done; _e = _d.next()) {
            var extension = _e.value;
            var def = autoload[extension];
            var _f = __read((def.length === 2 && Array.isArray(def[0]) ? def : [def, []]), 2), macs = _f[0], envs = _f[1];
            try {
                for (var macs_1 = (e_4 = void 0, __values(macs)), macs_1_1 = macs_1.next(); !macs_1_1.done; macs_1_1 = macs_1.next()) {
                    var name_1 = macs_1_1.value;
                    if (!macros.lookup(name_1) || name_1 === 'color') {
                        AutoloadMacros.add(name_1, new Symbol_js_1.Macro(name_1, Autoload, [extension, true]));
                    }
                }
            }
            catch (e_4_1) { e_4 = { error: e_4_1 }; }
            finally {
                try {
                    if (macs_1_1 && !macs_1_1.done && (_b = macs_1.return)) _b.call(macs_1);
                }
                finally { if (e_4) throw e_4.error; }
            }
            try {
                for (var envs_2 = (e_5 = void 0, __values(envs)), envs_2_1 = envs_2.next(); !envs_2_1.done; envs_2_1 = envs_2.next()) {
                    var name_2 = envs_2_1.value;
                    if (!environments.lookup(name_2)) {
                        AutoloadEnvironments.add(name_2, new Symbol_js_1.Macro(name_2, Autoload, [extension, false]));
                    }
                }
            }
            catch (e_5_1) { e_5 = { error: e_5_1 }; }
            finally {
                try {
                    if (envs_2_1 && !envs_2_1.done && (_c = envs_2.return)) _c.call(envs_2);
                }
                finally { if (e_5) throw e_5.error; }
            }
        }
    }
    catch (e_3_1) { e_3 = { error: e_3_1 }; }
    finally {
        try {
            if (_e && !_e.done && (_a = _d.return)) _a.call(_d);
        }
        finally { if (e_3) throw e_3.error; }
    }
    if (!parser.packageData.get('require')) {
        RequireConfiguration_js_1.RequireConfiguration.config(config, jax);
    }
}
var AutoloadMacros = new SymbolMap_js_1.CommandMap('autoload-macros', {}, {});
var AutoloadEnvironments = new SymbolMap_js_1.CommandMap('autoload-environments', {}, {});
exports.AutoloadConfiguration = Configuration_js_1.Configuration.create('autoload', {
    handler: {
        macro: ['autoload-macros'],
        environment: ['autoload-environments']
    },
    options: {
        autoload: (0, Options_js_1.expandable)({
            action: ['toggle', 'mathtip', 'texttip'],
            amscd: [[], ['CD']],
            bbox: ['bbox'],
            boldsymbol: ['boldsymbol'],
            braket: ['bra', 'ket', 'braket', 'set', 'Bra', 'Ket', 'Braket', 'Set', 'ketbra', 'Ketbra'],
            bussproofs: [[], ['prooftree']],
            cancel: ['cancel', 'bcancel', 'xcancel', 'cancelto'],
            color: ['color', 'definecolor', 'textcolor', 'colorbox', 'fcolorbox'],
            enclose: ['enclose'],
            extpfeil: ['xtwoheadrightarrow', 'xtwoheadleftarrow', 'xmapsto', 'xlongequal', 'xtofrom', 'Newextarrow'],
            html: ['href', 'class', 'style', 'cssId'],
            mhchem: ['ce', 'pu'],
            newcommand: ['newcommand', 'renewcommand', 'newenvironment', 'renewenvironment', 'def', 'let'],
            unicode: ['unicode'],
            verb: ['verb']
        })
    },
    config: configAutoload,
    init: initAutoload,
    priority: 10
});
//# sourceMappingURL=AutoloadConfiguration.js.map

/***/ }),

/***/ 955:
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

/***/ 924:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Symbol = MathJax._.input.tex.Symbol.Symbol;
exports.Macro = MathJax._.input.tex.Symbol.Macro;

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

/***/ 96:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.RequireLoad = MathJax._.input.tex.require.RequireConfiguration.RequireLoad;
exports.RequireMethods = MathJax._.input.tex.require.RequireConfiguration.RequireMethods;
exports.options = MathJax._.input.tex.require.RequireConfiguration.options;
exports.RequireConfiguration = MathJax._.input.tex.require.RequireConfiguration.RequireConfiguration;

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/autoload/AutoloadConfiguration.js
var AutoloadConfiguration = __webpack_require__(275);
;// CONCATENATED MODULE: ./lib/autoload.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/autoload', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        autoload: {
          AutoloadConfiguration: AutoloadConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./autoload.js

}();
/******/ })()
;