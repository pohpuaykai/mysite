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

/***/ 224:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ColorConfiguration = void 0;
var SymbolMap_js_1 = __webpack_require__(871);
var Configuration_js_1 = __webpack_require__(251);
var ColorMethods_js_1 = __webpack_require__(162);
var ColorUtil_js_1 = __webpack_require__(358);
new SymbolMap_js_1.CommandMap('color', {
    color: 'Color',
    textcolor: 'TextColor',
    definecolor: 'DefineColor',
    colorbox: 'ColorBox',
    fcolorbox: 'FColorBox'
}, ColorMethods_js_1.ColorMethods);
var config = function (_config, jax) {
    jax.parseOptions.packageData.set('color', { model: new ColorUtil_js_1.ColorModel() });
};
exports.ColorConfiguration = Configuration_js_1.Configuration.create('color', {
    handler: {
        macro: ['color'],
    },
    options: {
        color: {
            padding: '5px',
            borderWidth: '2px'
        }
    },
    config: config
});
//# sourceMappingURL=ColorConfiguration.js.map

/***/ }),

/***/ 59:
/***/ (function(__unused_webpack_module, exports) {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.COLORS = void 0;
exports.COLORS = new Map([
    ['Apricot', '#FBB982'],
    ['Aquamarine', '#00B5BE'],
    ['Bittersweet', '#C04F17'],
    ['Black', '#221E1F'],
    ['Blue', '#2D2F92'],
    ['BlueGreen', '#00B3B8'],
    ['BlueViolet', '#473992'],
    ['BrickRed', '#B6321C'],
    ['Brown', '#792500'],
    ['BurntOrange', '#F7921D'],
    ['CadetBlue', '#74729A'],
    ['CarnationPink', '#F282B4'],
    ['Cerulean', '#00A2E3'],
    ['CornflowerBlue', '#41B0E4'],
    ['Cyan', '#00AEEF'],
    ['Dandelion', '#FDBC42'],
    ['DarkOrchid', '#A4538A'],
    ['Emerald', '#00A99D'],
    ['ForestGreen', '#009B55'],
    ['Fuchsia', '#8C368C'],
    ['Goldenrod', '#FFDF42'],
    ['Gray', '#949698'],
    ['Green', '#00A64F'],
    ['GreenYellow', '#DFE674'],
    ['JungleGreen', '#00A99A'],
    ['Lavender', '#F49EC4'],
    ['LimeGreen', '#8DC73E'],
    ['Magenta', '#EC008C'],
    ['Mahogany', '#A9341F'],
    ['Maroon', '#AF3235'],
    ['Melon', '#F89E7B'],
    ['MidnightBlue', '#006795'],
    ['Mulberry', '#A93C93'],
    ['NavyBlue', '#006EB8'],
    ['OliveGreen', '#3C8031'],
    ['Orange', '#F58137'],
    ['OrangeRed', '#ED135A'],
    ['Orchid', '#AF72B0'],
    ['Peach', '#F7965A'],
    ['Periwinkle', '#7977B8'],
    ['PineGreen', '#008B72'],
    ['Plum', '#92268F'],
    ['ProcessBlue', '#00B0F0'],
    ['Purple', '#99479B'],
    ['RawSienna', '#974006'],
    ['Red', '#ED1B23'],
    ['RedOrange', '#F26035'],
    ['RedViolet', '#A1246B'],
    ['Rhodamine', '#EF559F'],
    ['RoyalBlue', '#0071BC'],
    ['RoyalPurple', '#613F99'],
    ['RubineRed', '#ED017D'],
    ['Salmon', '#F69289'],
    ['SeaGreen', '#3FBC9D'],
    ['Sepia', '#671800'],
    ['SkyBlue', '#46C5DD'],
    ['SpringGreen', '#C6DC67'],
    ['Tan', '#DA9D76'],
    ['TealBlue', '#00AEB3'],
    ['Thistle', '#D883B7'],
    ['Turquoise', '#00B4CE'],
    ['Violet', '#58429B'],
    ['VioletRed', '#EF58A0'],
    ['White', '#FFFFFF'],
    ['WildStrawberry', '#EE2967'],
    ['Yellow', '#FFF200'],
    ['YellowGreen', '#98CC70'],
    ['YellowOrange', '#FAA21A'],
]);
//# sourceMappingURL=ColorConstants.js.map

/***/ }),

/***/ 162:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ColorMethods = void 0;
var NodeUtil_js_1 = __importDefault(__webpack_require__(748));
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
function padding(colorPadding) {
    var pad = "+".concat(colorPadding);
    var unit = colorPadding.replace(/^.*?([a-z]*)$/, '$1');
    var pad2 = 2 * parseFloat(pad);
    return {
        width: "+".concat(pad2).concat(unit),
        height: pad,
        depth: pad,
        lspace: colorPadding,
    };
}
exports.ColorMethods = {};
exports.ColorMethods.Color = function (parser, name) {
    var model = parser.GetBrackets(name, '');
    var colorDef = parser.GetArgument(name);
    var colorModel = parser.configuration.packageData.get('color').model;
    var color = colorModel.getColor(model, colorDef);
    var style = parser.itemFactory.create('style')
        .setProperties({ styles: { mathcolor: color } });
    parser.stack.env['color'] = color;
    parser.Push(style);
};
exports.ColorMethods.TextColor = function (parser, name) {
    var model = parser.GetBrackets(name, '');
    var colorDef = parser.GetArgument(name);
    var colorModel = parser.configuration.packageData.get('color').model;
    var color = colorModel.getColor(model, colorDef);
    var old = parser.stack.env['color'];
    parser.stack.env['color'] = color;
    var math = parser.ParseArg(name);
    if (old) {
        parser.stack.env['color'] = old;
    }
    else {
        delete parser.stack.env['color'];
    }
    var node = parser.create('node', 'mstyle', [math], { mathcolor: color });
    parser.Push(node);
};
exports.ColorMethods.DefineColor = function (parser, name) {
    var cname = parser.GetArgument(name);
    var model = parser.GetArgument(name);
    var def = parser.GetArgument(name);
    var colorModel = parser.configuration.packageData.get('color').model;
    colorModel.defineColor(model, cname, def);
};
exports.ColorMethods.ColorBox = function (parser, name) {
    var cname = parser.GetArgument(name);
    var math = ParseUtil_js_1.default.internalMath(parser, parser.GetArgument(name));
    var colorModel = parser.configuration.packageData.get('color').model;
    var node = parser.create('node', 'mpadded', math, {
        mathbackground: colorModel.getColor('named', cname)
    });
    NodeUtil_js_1.default.setProperties(node, padding(parser.options.color.padding));
    parser.Push(node);
};
exports.ColorMethods.FColorBox = function (parser, name) {
    var fname = parser.GetArgument(name);
    var cname = parser.GetArgument(name);
    var math = ParseUtil_js_1.default.internalMath(parser, parser.GetArgument(name));
    var options = parser.options.color;
    var colorModel = parser.configuration.packageData.get('color').model;
    var node = parser.create('node', 'mpadded', math, {
        mathbackground: colorModel.getColor('named', cname),
        style: "border: ".concat(options.borderWidth, " solid ").concat(colorModel.getColor('named', fname))
    });
    NodeUtil_js_1.default.setProperties(node, padding(options.padding));
    parser.Push(node);
};
//# sourceMappingURL=ColorMethods.js.map

/***/ }),

/***/ 358:
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
exports.ColorModel = void 0;
var TexError_js_1 = __importDefault(__webpack_require__(402));
var ColorConstants_js_1 = __webpack_require__(59);
var ColorModelProcessors = new Map();
var ColorModel = (function () {
    function ColorModel() {
        this.userColors = new Map();
    }
    ColorModel.prototype.normalizeColor = function (model, def) {
        if (!model || model === 'named') {
            return def;
        }
        if (ColorModelProcessors.has(model)) {
            var modelProcessor = ColorModelProcessors.get(model);
            return modelProcessor(def);
        }
        throw new TexError_js_1.default('UndefinedColorModel', 'Color model \'%1\' not defined', model);
    };
    ColorModel.prototype.getColor = function (model, def) {
        if (!model || model === 'named') {
            return this.getColorByName(def);
        }
        return this.normalizeColor(model, def);
    };
    ColorModel.prototype.getColorByName = function (name) {
        if (this.userColors.has(name)) {
            return this.userColors.get(name);
        }
        if (ColorConstants_js_1.COLORS.has(name)) {
            return ColorConstants_js_1.COLORS.get(name);
        }
        return name;
    };
    ColorModel.prototype.defineColor = function (model, name, def) {
        var normalized = this.normalizeColor(model, def);
        this.userColors.set(name, normalized);
    };
    return ColorModel;
}());
exports.ColorModel = ColorModel;
ColorModelProcessors.set('rgb', function (rgb) {
    var e_1, _a;
    var rgbParts = rgb.trim().split(/\s*,\s*/);
    var RGB = '#';
    if (rgbParts.length !== 3) {
        throw new TexError_js_1.default('ModelArg1', 'Color values for the %1 model require 3 numbers', 'rgb');
    }
    try {
        for (var rgbParts_1 = __values(rgbParts), rgbParts_1_1 = rgbParts_1.next(); !rgbParts_1_1.done; rgbParts_1_1 = rgbParts_1.next()) {
            var rgbPart = rgbParts_1_1.value;
            if (!rgbPart.match(/^(\d+(\.\d*)?|\.\d+)$/)) {
                throw new TexError_js_1.default('InvalidDecimalNumber', 'Invalid decimal number');
            }
            var n = parseFloat(rgbPart);
            if (n < 0 || n > 1) {
                throw new TexError_js_1.default('ModelArg2', 'Color values for the %1 model must be between %2 and %3', 'rgb', '0', '1');
            }
            var pn = Math.floor(n * 255).toString(16);
            if (pn.length < 2) {
                pn = '0' + pn;
            }
            RGB += pn;
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (rgbParts_1_1 && !rgbParts_1_1.done && (_a = rgbParts_1.return)) _a.call(rgbParts_1);
        }
        finally { if (e_1) throw e_1.error; }
    }
    return RGB;
});
ColorModelProcessors.set('RGB', function (rgb) {
    var e_2, _a;
    var rgbParts = rgb.trim().split(/\s*,\s*/);
    var RGB = '#';
    if (rgbParts.length !== 3) {
        throw new TexError_js_1.default('ModelArg1', 'Color values for the %1 model require 3 numbers', 'RGB');
    }
    try {
        for (var rgbParts_2 = __values(rgbParts), rgbParts_2_1 = rgbParts_2.next(); !rgbParts_2_1.done; rgbParts_2_1 = rgbParts_2.next()) {
            var rgbPart = rgbParts_2_1.value;
            if (!rgbPart.match(/^\d+$/)) {
                throw new TexError_js_1.default('InvalidNumber', 'Invalid number');
            }
            var n = parseInt(rgbPart);
            if (n > 255) {
                throw new TexError_js_1.default('ModelArg2', 'Color values for the %1 model must be between %2 and %3', 'RGB', '0', '255');
            }
            var pn = n.toString(16);
            if (pn.length < 2) {
                pn = '0' + pn;
            }
            RGB += pn;
        }
    }
    catch (e_2_1) { e_2 = { error: e_2_1 }; }
    finally {
        try {
            if (rgbParts_2_1 && !rgbParts_2_1.done && (_a = rgbParts_2.return)) _a.call(rgbParts_2);
        }
        finally { if (e_2) throw e_2.error; }
    }
    return RGB;
});
ColorModelProcessors.set('gray', function (gray) {
    if (!gray.match(/^\s*(\d+(\.\d*)?|\.\d+)\s*$/)) {
        throw new TexError_js_1.default('InvalidDecimalNumber', 'Invalid decimal number');
    }
    var n = parseFloat(gray);
    if (n < 0 || n > 1) {
        throw new TexError_js_1.default('ModelArg2', 'Color values for the %1 model must be between %2 and %3', 'gray', '0', '1');
    }
    var pn = Math.floor(n * 255).toString(16);
    if (pn.length < 2) {
        pn = '0' + pn;
    }
    return "#".concat(pn).concat(pn).concat(pn);
});
//# sourceMappingURL=ColorUtil.js.map

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

/***/ 748:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.NodeUtil["default"];

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

/***/ 402:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.TexError["default"];

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/color/ColorConfiguration.js
var ColorConfiguration = __webpack_require__(224);
// EXTERNAL MODULE: ../../../../../../js/input/tex/color/ColorConstants.js
var ColorConstants = __webpack_require__(59);
// EXTERNAL MODULE: ../../../../../../js/input/tex/color/ColorMethods.js
var ColorMethods = __webpack_require__(162);
// EXTERNAL MODULE: ../../../../../../js/input/tex/color/ColorUtil.js
var ColorUtil = __webpack_require__(358);
;// CONCATENATED MODULE: ./lib/color.js







if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/color', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        color: {
          ColorConfiguration: ColorConfiguration,
          ColorConstants: ColorConstants,
          ColorMethods: ColorMethods,
          ColorUtil: ColorUtil
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./color.js

}();
/******/ })()
;