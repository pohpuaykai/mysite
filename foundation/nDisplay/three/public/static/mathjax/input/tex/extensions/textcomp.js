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

/***/ 845:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TextcompConfiguration = void 0;
var Configuration_js_1 = __webpack_require__(251);
__webpack_require__(832);
exports.TextcompConfiguration = Configuration_js_1.Configuration.create('textcomp', {
    handler: { macro: ['textcomp-macros'] }
});
//# sourceMappingURL=TextcompConfiguration.js.map

/***/ }),

/***/ 832:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var SymbolMap_js_1 = __webpack_require__(871);
var TexConstants_js_1 = __webpack_require__(108);
var TextMacrosMethods_js_1 = __webpack_require__(245);
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var TextParser_js_1 = __webpack_require__(988);
new SymbolMap_js_1.CommandMap('textcomp-macros', {
    'textasciicircum': ['Insert', '\u005E'],
    'textasciitilde': ['Insert', '\u007E'],
    'textasteriskcentered': ['Insert', '\u002A'],
    'textbackslash': ['Insert', '\u005C'],
    'textbar': ['Insert', '\u007C'],
    'textbraceleft': ['Insert', '\u007B'],
    'textbraceright': ['Insert', '\u007D'],
    'textbullet': ['Insert', '\u2022'],
    'textdagger': ['Insert', '\u2020'],
    'textdaggerdbl': ['Insert', '\u2021'],
    'textellipsis': ['Insert', '\u2026'],
    'textemdash': ['Insert', '\u2014'],
    'textendash': ['Insert', '\u2013'],
    'textexclamdown': ['Insert', '\u00A1'],
    'textgreater': ['Insert', '\u003E'],
    'textless': ['Insert', '\u003C'],
    'textordfeminine': ['Insert', '\u00AA'],
    'textordmasculine': ['Insert', '\u00BA'],
    'textparagraph': ['Insert', '\u00B6'],
    'textperiodcentered': ['Insert', '\u00B7'],
    'textquestiondown': ['Insert', '\u00BF'],
    'textquotedblleft': ['Insert', '\u201C'],
    'textquotedblright': ['Insert', '\u201D'],
    'textquoteleft': ['Insert', '\u2018'],
    'textquoteright': ['Insert', '\u2019'],
    'textsection': ['Insert', '\u00A7'],
    'textunderscore': ['Insert', '\u005F'],
    'textvisiblespace': ['Insert', '\u2423'],
    'textacutedbl': ['Insert', '\u02DD'],
    'textasciiacute': ['Insert', '\u00B4'],
    'textasciibreve': ['Insert', '\u02D8'],
    'textasciicaron': ['Insert', '\u02C7'],
    'textasciidieresis': ['Insert', '\u00A8'],
    'textasciimacron': ['Insert', '\u00AF'],
    'textgravedbl': ['Insert', '\u02F5'],
    'texttildelow': ['Insert', '\u02F7'],
    'textbaht': ['Insert', '\u0E3F'],
    'textcent': ['Insert', '\u00A2'],
    'textcolonmonetary': ['Insert', '\u20A1'],
    'textcurrency': ['Insert', '\u00A4'],
    'textdollar': ['Insert', '\u0024'],
    'textdong': ['Insert', '\u20AB'],
    'texteuro': ['Insert', '\u20AC'],
    'textflorin': ['Insert', '\u0192'],
    'textguarani': ['Insert', '\u20B2'],
    'textlira': ['Insert', '\u20A4'],
    'textnaira': ['Insert', '\u20A6'],
    'textpeso': ['Insert', '\u20B1'],
    'textsterling': ['Insert', '\u00A3'],
    'textwon': ['Insert', '\u20A9'],
    'textyen': ['Insert', '\u00A5'],
    'textcircledP': ['Insert', '\u2117'],
    'textcompwordmark': ['Insert', '\u200C'],
    'textcopyleft': ['Insert', "\uD83C\uDD2F"],
    'textcopyright': ['Insert', '\u00A9'],
    'textregistered': ['Insert', '\u00AE'],
    'textservicemark': ['Insert', '\u2120'],
    'texttrademark': ['Insert', '\u2122'],
    'textbardbl': ['Insert', '\u2016'],
    'textbigcircle': ['Insert', '\u25EF'],
    'textblank': ['Insert', '\u2422'],
    'textbrokenbar': ['Insert', '\u00A6'],
    'textdiscount': ['Insert', '\u2052'],
    'textestimated': ['Insert', '\u212E'],
    'textinterrobang': ['Insert', '\u203D'],
    'textinterrobangdown': ['Insert', '\u2E18'],
    'textmusicalnote': ['Insert', '\u266A'],
    'textnumero': ['Insert', '\u2116'],
    'textopenbullet': ['Insert', '\u25E6'],
    'textpertenthousand': ['Insert', '\u2031'],
    'textperthousand': ['Insert', '\u2030'],
    'textrecipe': ['Insert', '\u211E'],
    'textreferencemark': ['Insert', '\u203B'],
    'textlangle': ['Insert', '\u2329'],
    'textrangle': ['Insert', '\u232A'],
    'textlbrackdbl': ['Insert', '\u27E6'],
    'textrbrackdbl': ['Insert', '\u27E7'],
    'textlquill': ['Insert', '\u2045'],
    'textrquill': ['Insert', '\u2046'],
    'textcelsius': ['Insert', '\u2103'],
    'textdegree': ['Insert', '\u00B0'],
    'textdiv': ['Insert', '\u00F7'],
    'textdownarrow': ['Insert', '\u2193'],
    'textfractionsolidus': ['Insert', '\u2044'],
    'textleftarrow': ['Insert', '\u2190'],
    'textlnot': ['Insert', '\u00AC'],
    'textmho': ['Insert', '\u2127'],
    'textminus': ['Insert', '\u2212'],
    'textmu': ['Insert', '\u00B5'],
    'textohm': ['Insert', '\u2126'],
    'textonehalf': ['Insert', '\u00BD'],
    'textonequarter': ['Insert', '\u00BC'],
    'textonesuperior': ['Insert', '\u00B9'],
    'textpm': ['Insert', '\u00B1'],
    'textrightarrow': ['Insert', '\u2192'],
    'textsurd': ['Insert', '\u221A'],
    'textthreequarters': ['Insert', '\u00BE'],
    'textthreesuperior': ['Insert', '\u00B3'],
    'texttimes': ['Insert', '\u00D7'],
    'texttwosuperior': ['Insert', '\u00B2'],
    'textuparrow': ['Insert', '\u2191'],
    'textborn': ['Insert', '\u002A'],
    'textdied': ['Insert', '\u2020'],
    'textdivorced': ['Insert', '\u26AE'],
    'textmarried': ['Insert', '\u26AD'],
    'textcentoldstyle': ['Insert', '\u00A2', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'textdollaroldstyle': ['Insert', '\u0024', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'textzerooldstyle': ['Insert', '0', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'textoneoldstyle': ['Insert', '1', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'texttwooldstyle': ['Insert', '2', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'textthreeoldstyle': ['Insert', '3', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'textfouroldstyle': ['Insert', '4', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'textfiveoldstyle': ['Insert', '5', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'textsixoldstyle': ['Insert', '6', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'textsevenoldstyle': ['Insert', '7', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'texteightoldstyle': ['Insert', '8', TexConstants_js_1.TexConstant.Variant.OLDSTYLE],
    'textnineoldstyle': ['Insert', '9', TexConstants_js_1.TexConstant.Variant.OLDSTYLE]
}, {
    Insert: function (parser, name, c, font) {
        if (parser instanceof TextParser_js_1.TextParser) {
            if (!font) {
                TextMacrosMethods_js_1.TextMacrosMethods.Insert(parser, name, c);
                return;
            }
            parser.saveText();
        }
        parser.Push(ParseUtil_js_1.default.internalText(parser, c, font ? { mathvariant: font } : {}));
    }
});
//# sourceMappingURL=TextcompMappings.js.map

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

/***/ 108:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.TexConstant = MathJax._.input.tex.TexConstants.TexConstant;

/***/ }),

/***/ 245:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.TextMacrosMethods = MathJax._.input.tex.textmacros.TextMacrosMethods.TextMacrosMethods;

/***/ }),

/***/ 988:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.TextParser = MathJax._.input.tex.textmacros.TextParser.TextParser;

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/textcomp/TextcompConfiguration.js
var TextcompConfiguration = __webpack_require__(845);
;// CONCATENATED MODULE: ./lib/textcomp.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/textcomp', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        textcomp: {
          TextcompConfiguration: TextcompConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./textcomp.js

}();
/******/ })()
;