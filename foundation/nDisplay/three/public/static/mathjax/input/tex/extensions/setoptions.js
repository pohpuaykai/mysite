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

/***/ 596:
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
exports.SetOptionsConfiguration = exports.SetOptionsUtil = void 0;
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var TexError_js_1 = __importDefault(__webpack_require__(402));
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var Symbol_js_1 = __webpack_require__(924);
var BaseMethods_js_1 = __importDefault(__webpack_require__(360));
var Options_js_1 = __webpack_require__(74);
exports.SetOptionsUtil = {
    filterPackage: function (parser, extension) {
        if (extension !== 'tex' && !Configuration_js_1.ConfigurationHandler.get(extension)) {
            throw new TexError_js_1.default('NotAPackage', 'Not a defined package: %1', extension);
        }
        var config = parser.options.setoptions;
        var options = config.allowOptions[extension];
        if ((options === undefined && !config.allowPackageDefault) || options === false) {
            throw new TexError_js_1.default('PackageNotSettable', 'Options can\'t be set for package "%1"', extension);
        }
        return true;
    },
    filterOption: function (parser, extension, option) {
        var _a;
        var config = parser.options.setoptions;
        var options = config.allowOptions[extension] || {};
        var allow = (options.hasOwnProperty(option) && !(0, Options_js_1.isObject)(options[option]) ? options[option] : null);
        if (allow === false || (allow === null && !config.allowOptionsDefault)) {
            throw new TexError_js_1.default('OptionNotSettable', 'Option "%1" is not allowed to be set', option);
        }
        if (!((_a = (extension === 'tex' ? parser.options : parser.options[extension])) === null || _a === void 0 ? void 0 : _a.hasOwnProperty(option))) {
            if (extension === 'tex') {
                throw new TexError_js_1.default('InvalidTexOption', 'Invalid TeX option "%1"', option);
            }
            else {
                throw new TexError_js_1.default('InvalidOptionKey', 'Invalid option "%1" for package "%2"', option, extension);
            }
        }
        return true;
    },
    filterValue: function (_parser, _extension, _option, value) {
        return value;
    }
};
var setOptionsMap = new SymbolMap_js_1.CommandMap('setoptions', {
    setOptions: 'SetOptions'
}, {
    SetOptions: function (parser, name) {
        var e_1, _a;
        var extension = parser.GetBrackets(name) || 'tex';
        var options = ParseUtil_js_1.default.keyvalOptions(parser.GetArgument(name));
        var config = parser.options.setoptions;
        if (!config.filterPackage(parser, extension))
            return;
        try {
            for (var _b = __values(Object.keys(options)), _c = _b.next(); !_c.done; _c = _b.next()) {
                var key = _c.value;
                if (config.filterOption(parser, extension, key)) {
                    (extension === 'tex' ? parser.options : parser.options[extension])[key] =
                        config.filterValue(parser, extension, key, options[key]);
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
});
function setoptionsConfig(_config, jax) {
    var require = jax.parseOptions.handlers.get('macro').lookup('require');
    if (require) {
        setOptionsMap.add('Require', new Symbol_js_1.Macro('Require', require._func));
        setOptionsMap.add('require', new Symbol_js_1.Macro('require', BaseMethods_js_1.default.Macro, ['\\Require{#2}\\setOptions[#2]{#1}', 2, '']));
    }
}
exports.SetOptionsConfiguration = Configuration_js_1.Configuration.create('setoptions', {
    handler: { macro: ['setoptions'] },
    config: setoptionsConfig,
    priority: 3,
    options: {
        setoptions: {
            filterPackage: exports.SetOptionsUtil.filterPackage,
            filterOption: exports.SetOptionsUtil.filterOption,
            filterValue: exports.SetOptionsUtil.filterValue,
            allowPackageDefault: true,
            allowOptionsDefault: true,
            allowOptions: (0, Options_js_1.expandable)({
                tex: {
                    FindTeX: false,
                    formatError: false,
                    package: false,
                    baseURL: false,
                    tags: false,
                    maxBuffer: false,
                    maxMaxros: false,
                    macros: false,
                    environments: false
                },
                setoptions: false,
                autoload: false,
                require: false,
                configmacros: false,
                tagformat: false
            })
        }
    }
});
//# sourceMappingURL=SetOptionsConfiguration.js.map

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

/***/ 398:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.ParseUtil["default"];

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

/***/ 402:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.TexError["default"];

/***/ }),

/***/ 360:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.base.BaseMethods["default"];

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/setoptions/SetOptionsConfiguration.js
var SetOptionsConfiguration = __webpack_require__(596);
;// CONCATENATED MODULE: ./lib/setoptions.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/setoptions', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        setoptions: {
          SetOptionsConfiguration: SetOptionsConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./setoptions.js

}();
/******/ })()
;