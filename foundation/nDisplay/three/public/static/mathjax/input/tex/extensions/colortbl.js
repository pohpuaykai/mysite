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

/***/ 558:
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
exports.ColortblConfiguration = exports.ColorArrayItem = void 0;
var BaseItems_js_1 = __webpack_require__(935);
var Configuration_js_1 = __webpack_require__(251);
var SymbolMap_js_1 = __webpack_require__(871);
var TexError_js_1 = __importDefault(__webpack_require__(402));
var ColorArrayItem = (function (_super) {
    __extends(ColorArrayItem, _super);
    function ColorArrayItem() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.color = {
            cell: '',
            row: '',
            col: []
        };
        _this.hasColor = false;
        return _this;
    }
    ColorArrayItem.prototype.EndEntry = function () {
        _super.prototype.EndEntry.call(this);
        var cell = this.row[this.row.length - 1];
        var color = this.color.cell || this.color.row || this.color.col[this.row.length - 1];
        if (color) {
            cell.attributes.set('mathbackground', color);
            this.color.cell = '';
            this.hasColor = true;
        }
    };
    ColorArrayItem.prototype.EndRow = function () {
        _super.prototype.EndRow.call(this);
        this.color.row = '';
    };
    ColorArrayItem.prototype.createMml = function () {
        var mml = _super.prototype.createMml.call(this);
        var table = (mml.isKind('mrow') ? mml.childNodes[1] : mml);
        if (table.isKind('menclose')) {
            table = table.childNodes[0].childNodes[0];
        }
        if (this.hasColor && table.attributes.get('frame') === 'none') {
            table.attributes.set('frame', '');
        }
        return mml;
    };
    return ColorArrayItem;
}(BaseItems_js_1.ArrayItem));
exports.ColorArrayItem = ColorArrayItem;
new SymbolMap_js_1.CommandMap('colortbl', {
    cellcolor: ['TableColor', 'cell'],
    rowcolor: ['TableColor', 'row'],
    columncolor: ['TableColor', 'col']
}, {
    TableColor: function (parser, name, type) {
        var lookup = parser.configuration.packageData.get('color').model;
        var model = parser.GetBrackets(name, '');
        var color = lookup.getColor(model, parser.GetArgument(name));
        var top = parser.stack.Top();
        if (!(top instanceof ColorArrayItem)) {
            throw new TexError_js_1.default('UnsupportedTableColor', 'Unsupported use of %1', parser.currentCS);
        }
        if (type === 'col') {
            if (top.table.length) {
                throw new TexError_js_1.default('ColumnColorNotTop', '%1 must be in the top row', name);
            }
            top.color.col[top.row.length] = color;
            if (parser.GetBrackets(name, '')) {
                parser.GetBrackets(name, '');
            }
        }
        else {
            top.color[type] = color;
            if (type === 'row' && (top.Size() || top.row.length)) {
                throw new TexError_js_1.default('RowColorNotFirst', '%1 must be at the beginning of a row', name);
            }
        }
    }
});
var config = function (config, jax) {
    if (!jax.parseOptions.packageData.has('color')) {
        Configuration_js_1.ConfigurationHandler.get('color').config(config, jax);
    }
};
exports.ColortblConfiguration = Configuration_js_1.Configuration.create('colortbl', {
    handler: { macro: ['colortbl'] },
    items: { 'array': ColorArrayItem },
    priority: 10,
    config: [config, 10]
});
//# sourceMappingURL=ColortblConfiguration.js.map

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

/***/ 935:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.StartItem = MathJax._.input.tex.base.BaseItems.StartItem;
exports.StopItem = MathJax._.input.tex.base.BaseItems.StopItem;
exports.OpenItem = MathJax._.input.tex.base.BaseItems.OpenItem;
exports.CloseItem = MathJax._.input.tex.base.BaseItems.CloseItem;
exports.PrimeItem = MathJax._.input.tex.base.BaseItems.PrimeItem;
exports.SubsupItem = MathJax._.input.tex.base.BaseItems.SubsupItem;
exports.OverItem = MathJax._.input.tex.base.BaseItems.OverItem;
exports.LeftItem = MathJax._.input.tex.base.BaseItems.LeftItem;
exports.Middle = MathJax._.input.tex.base.BaseItems.Middle;
exports.RightItem = MathJax._.input.tex.base.BaseItems.RightItem;
exports.BeginItem = MathJax._.input.tex.base.BaseItems.BeginItem;
exports.EndItem = MathJax._.input.tex.base.BaseItems.EndItem;
exports.StyleItem = MathJax._.input.tex.base.BaseItems.StyleItem;
exports.PositionItem = MathJax._.input.tex.base.BaseItems.PositionItem;
exports.CellItem = MathJax._.input.tex.base.BaseItems.CellItem;
exports.MmlItem = MathJax._.input.tex.base.BaseItems.MmlItem;
exports.FnItem = MathJax._.input.tex.base.BaseItems.FnItem;
exports.NotItem = MathJax._.input.tex.base.BaseItems.NotItem;
exports.NonscriptItem = MathJax._.input.tex.base.BaseItems.NonscriptItem;
exports.DotsItem = MathJax._.input.tex.base.BaseItems.DotsItem;
exports.ArrayItem = MathJax._.input.tex.base.BaseItems.ArrayItem;
exports.EqnArrayItem = MathJax._.input.tex.base.BaseItems.EqnArrayItem;
exports.EquationItem = MathJax._.input.tex.base.BaseItems.EquationItem;

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/colortbl/ColortblConfiguration.js
var ColortblConfiguration = __webpack_require__(558);
;// CONCATENATED MODULE: ./lib/colortbl.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/colortbl', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        colortbl: {
          ColortblConfiguration: ColortblConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./colortbl.js

}();
/******/ })()
;