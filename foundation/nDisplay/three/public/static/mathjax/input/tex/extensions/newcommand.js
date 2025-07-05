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

/***/ 48:
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
var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.NewcommandConfiguration = void 0;
var Configuration_js_1 = __webpack_require__(251);
var NewcommandItems_js_1 = __webpack_require__(205);
var NewcommandUtil_js_1 = __importDefault(__webpack_require__(406));
__webpack_require__(297);
var ParseMethods_js_1 = __importDefault(__webpack_require__(945));
var sm = __importStar(__webpack_require__(871));
var init = function (config) {
    new sm.DelimiterMap(NewcommandUtil_js_1.default.NEW_DELIMITER, ParseMethods_js_1.default.delimiter, {});
    new sm.CommandMap(NewcommandUtil_js_1.default.NEW_COMMAND, {}, {});
    new sm.EnvironmentMap(NewcommandUtil_js_1.default.NEW_ENVIRONMENT, ParseMethods_js_1.default.environment, {}, {});
    config.append(Configuration_js_1.Configuration.local({ handler: { character: [],
            delimiter: [NewcommandUtil_js_1.default.NEW_DELIMITER],
            macro: [NewcommandUtil_js_1.default.NEW_DELIMITER,
                NewcommandUtil_js_1.default.NEW_COMMAND],
            environment: [NewcommandUtil_js_1.default.NEW_ENVIRONMENT]
        },
        priority: -1 }));
};
exports.NewcommandConfiguration = Configuration_js_1.Configuration.create('newcommand', {
    handler: {
        macro: ['Newcommand-macros']
    },
    items: (_a = {},
        _a[NewcommandItems_js_1.BeginEnvItem.prototype.kind] = NewcommandItems_js_1.BeginEnvItem,
        _a),
    options: { maxMacros: 1000 },
    init: init
});
//# sourceMappingURL=NewcommandConfiguration.js.map

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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BeginEnvItem = void 0;
var TexError_js_1 = __importDefault(__webpack_require__(402));
var StackItem_js_1 = __webpack_require__(76);
var BeginEnvItem = (function (_super) {
    __extends(BeginEnvItem, _super);
    function BeginEnvItem() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Object.defineProperty(BeginEnvItem.prototype, "kind", {
        get: function () {
            return 'beginEnv';
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(BeginEnvItem.prototype, "isOpen", {
        get: function () {
            return true;
        },
        enumerable: false,
        configurable: true
    });
    BeginEnvItem.prototype.checkItem = function (item) {
        if (item.isKind('end')) {
            if (item.getName() !== this.getName()) {
                throw new TexError_js_1.default('EnvBadEnd', '\\begin{%1} ended with \\end{%2}', this.getName(), item.getName());
            }
            return [[this.factory.create('mml', this.toMml())], true];
        }
        if (item.isKind('stop')) {
            throw new TexError_js_1.default('EnvMissingEnd', 'Missing \\end{%1}', this.getName());
        }
        return _super.prototype.checkItem.call(this, item);
    };
    return BeginEnvItem;
}(StackItem_js_1.BaseItem));
exports.BeginEnvItem = BeginEnvItem;
//# sourceMappingURL=NewcommandItems.js.map

/***/ }),

/***/ 297:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var NewcommandMethods_js_1 = __importDefault(__webpack_require__(107));
var SymbolMap_js_1 = __webpack_require__(871);
new SymbolMap_js_1.CommandMap('Newcommand-macros', {
    newcommand: 'NewCommand',
    renewcommand: 'NewCommand',
    newenvironment: 'NewEnvironment',
    renewenvironment: 'NewEnvironment',
    def: 'MacroDef',
    'let': 'Let'
}, NewcommandMethods_js_1.default);
//# sourceMappingURL=NewcommandMappings.js.map

/***/ }),

/***/ 107:
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
var TexError_js_1 = __importDefault(__webpack_require__(402));
var sm = __importStar(__webpack_require__(871));
var BaseMethods_js_1 = __importDefault(__webpack_require__(360));
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var NewcommandUtil_js_1 = __importDefault(__webpack_require__(406));
var NewcommandMethods = {};
NewcommandMethods.NewCommand = function (parser, name) {
    var cs = NewcommandUtil_js_1.default.GetCsNameArgument(parser, name);
    var n = NewcommandUtil_js_1.default.GetArgCount(parser, name);
    var opt = parser.GetBrackets(name);
    var def = parser.GetArgument(name);
    NewcommandUtil_js_1.default.addMacro(parser, cs, NewcommandMethods.Macro, [def, n, opt]);
};
NewcommandMethods.NewEnvironment = function (parser, name) {
    var env = ParseUtil_js_1.default.trimSpaces(parser.GetArgument(name));
    var n = NewcommandUtil_js_1.default.GetArgCount(parser, name);
    var opt = parser.GetBrackets(name);
    var bdef = parser.GetArgument(name);
    var edef = parser.GetArgument(name);
    NewcommandUtil_js_1.default.addEnvironment(parser, env, NewcommandMethods.BeginEnv, [true, bdef, edef, n, opt]);
};
NewcommandMethods.MacroDef = function (parser, name) {
    var cs = NewcommandUtil_js_1.default.GetCSname(parser, name);
    var params = NewcommandUtil_js_1.default.GetTemplate(parser, name, '\\' + cs);
    var def = parser.GetArgument(name);
    !(params instanceof Array) ?
        NewcommandUtil_js_1.default.addMacro(parser, cs, NewcommandMethods.Macro, [def, params]) :
        NewcommandUtil_js_1.default.addMacro(parser, cs, NewcommandMethods.MacroWithTemplate, [def].concat(params));
};
NewcommandMethods.Let = function (parser, name) {
    var cs = NewcommandUtil_js_1.default.GetCSname(parser, name);
    var c = parser.GetNext();
    if (c === '=') {
        parser.i++;
        c = parser.GetNext();
    }
    var handlers = parser.configuration.handlers;
    if (c === '\\') {
        name = NewcommandUtil_js_1.default.GetCSname(parser, name);
        var macro_1 = handlers.get('delimiter').lookup('\\' + name);
        if (macro_1) {
            NewcommandUtil_js_1.default.addDelimiter(parser, '\\' + cs, macro_1.char, macro_1.attributes);
            return;
        }
        var map_1 = handlers.get('macro').applicable(name);
        if (!map_1) {
            return;
        }
        if (map_1 instanceof sm.MacroMap) {
            var macro_2 = map_1.lookup(name);
            NewcommandUtil_js_1.default.addMacro(parser, cs, macro_2.func, macro_2.args, macro_2.symbol);
            return;
        }
        macro_1 = map_1.lookup(name);
        var newArgs = NewcommandUtil_js_1.default.disassembleSymbol(cs, macro_1);
        var method = function (p, _cs) {
            var rest = [];
            for (var _i = 2; _i < arguments.length; _i++) {
                rest[_i - 2] = arguments[_i];
            }
            var symb = NewcommandUtil_js_1.default.assembleSymbol(rest);
            return map_1.parser(p, symb);
        };
        NewcommandUtil_js_1.default.addMacro(parser, cs, method, newArgs);
        return;
    }
    parser.i++;
    var macro = handlers.get('delimiter').lookup(c);
    if (macro) {
        NewcommandUtil_js_1.default.addDelimiter(parser, '\\' + cs, macro.char, macro.attributes);
        return;
    }
    NewcommandUtil_js_1.default.addMacro(parser, cs, NewcommandMethods.Macro, [c]);
};
NewcommandMethods.MacroWithTemplate = function (parser, name, text, n) {
    var params = [];
    for (var _i = 4; _i < arguments.length; _i++) {
        params[_i - 4] = arguments[_i];
    }
    var argCount = parseInt(n, 10);
    if (argCount) {
        var args = [];
        parser.GetNext();
        if (params[0] && !NewcommandUtil_js_1.default.MatchParam(parser, params[0])) {
            throw new TexError_js_1.default('MismatchUseDef', 'Use of %1 doesn\'t match its definition', name);
        }
        for (var i = 0; i < argCount; i++) {
            args.push(NewcommandUtil_js_1.default.GetParameter(parser, name, params[i + 1]));
        }
        text = ParseUtil_js_1.default.substituteArgs(parser, args, text);
    }
    parser.string = ParseUtil_js_1.default.addArgs(parser, text, parser.string.slice(parser.i));
    parser.i = 0;
    ParseUtil_js_1.default.checkMaxMacros(parser);
};
NewcommandMethods.BeginEnv = function (parser, begin, bdef, edef, n, def) {
    if (begin.getProperty('end') && parser.stack.env['closing'] === begin.getName()) {
        delete parser.stack.env['closing'];
        var rest = parser.string.slice(parser.i);
        parser.string = edef;
        parser.i = 0;
        parser.Parse();
        parser.string = rest;
        parser.i = 0;
        return parser.itemFactory.create('end').setProperty('name', begin.getName());
    }
    if (n) {
        var args = [];
        if (def != null) {
            var optional = parser.GetBrackets('\\begin{' + begin.getName() + '}');
            args.push(optional == null ? def : optional);
        }
        for (var i = args.length; i < n; i++) {
            args.push(parser.GetArgument('\\begin{' + begin.getName() + '}'));
        }
        bdef = ParseUtil_js_1.default.substituteArgs(parser, args, bdef);
        edef = ParseUtil_js_1.default.substituteArgs(parser, [], edef);
    }
    parser.string = ParseUtil_js_1.default.addArgs(parser, bdef, parser.string.slice(parser.i));
    parser.i = 0;
    return parser.itemFactory.create('beginEnv').setProperty('name', begin.getName());
};
NewcommandMethods.Macro = BaseMethods_js_1.default.Macro;
exports["default"] = NewcommandMethods;
//# sourceMappingURL=NewcommandMethods.js.map

/***/ }),

/***/ 406:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var TexError_js_1 = __importDefault(__webpack_require__(402));
var Symbol_js_1 = __webpack_require__(924);
var NewcommandUtil;
(function (NewcommandUtil) {
    function disassembleSymbol(name, symbol) {
        var newArgs = [name, symbol.char];
        if (symbol.attributes) {
            for (var key in symbol.attributes) {
                newArgs.push(key);
                newArgs.push(symbol.attributes[key]);
            }
        }
        return newArgs;
    }
    NewcommandUtil.disassembleSymbol = disassembleSymbol;
    function assembleSymbol(args) {
        var name = args[0];
        var char = args[1];
        var attrs = {};
        for (var i = 2; i < args.length; i = i + 2) {
            attrs[args[i]] = args[i + 1];
        }
        return new Symbol_js_1.Symbol(name, char, attrs);
    }
    NewcommandUtil.assembleSymbol = assembleSymbol;
    function GetCSname(parser, cmd) {
        var c = parser.GetNext();
        if (c !== '\\') {
            throw new TexError_js_1.default('MissingCS', '%1 must be followed by a control sequence', cmd);
        }
        var cs = ParseUtil_js_1.default.trimSpaces(parser.GetArgument(cmd));
        return cs.substr(1);
    }
    NewcommandUtil.GetCSname = GetCSname;
    function GetCsNameArgument(parser, name) {
        var cs = ParseUtil_js_1.default.trimSpaces(parser.GetArgument(name));
        if (cs.charAt(0) === '\\') {
            cs = cs.substr(1);
        }
        if (!cs.match(/^(.|[a-z]+)$/i)) {
            throw new TexError_js_1.default('IllegalControlSequenceName', 'Illegal control sequence name for %1', name);
        }
        return cs;
    }
    NewcommandUtil.GetCsNameArgument = GetCsNameArgument;
    function GetArgCount(parser, name) {
        var n = parser.GetBrackets(name);
        if (n) {
            n = ParseUtil_js_1.default.trimSpaces(n);
            if (!n.match(/^[0-9]+$/)) {
                throw new TexError_js_1.default('IllegalParamNumber', 'Illegal number of parameters specified in %1', name);
            }
        }
        return n;
    }
    NewcommandUtil.GetArgCount = GetArgCount;
    function GetTemplate(parser, cmd, cs) {
        var c = parser.GetNext();
        var params = [];
        var n = 0;
        var i = parser.i;
        while (parser.i < parser.string.length) {
            c = parser.GetNext();
            if (c === '#') {
                if (i !== parser.i) {
                    params[n] = parser.string.substr(i, parser.i - i);
                }
                c = parser.string.charAt(++parser.i);
                if (!c.match(/^[1-9]$/)) {
                    throw new TexError_js_1.default('CantUseHash2', 'Illegal use of # in template for %1', cs);
                }
                if (parseInt(c) !== ++n) {
                    throw new TexError_js_1.default('SequentialParam', 'Parameters for %1 must be numbered sequentially', cs);
                }
                i = parser.i + 1;
            }
            else if (c === '{') {
                if (i !== parser.i) {
                    params[n] = parser.string.substr(i, parser.i - i);
                }
                if (params.length > 0) {
                    return [n.toString()].concat(params);
                }
                else {
                    return n;
                }
            }
            parser.i++;
        }
        throw new TexError_js_1.default('MissingReplacementString', 'Missing replacement string for definition of %1', cmd);
    }
    NewcommandUtil.GetTemplate = GetTemplate;
    function GetParameter(parser, name, param) {
        if (param == null) {
            return parser.GetArgument(name);
        }
        var i = parser.i;
        var j = 0;
        var hasBraces = 0;
        while (parser.i < parser.string.length) {
            var c = parser.string.charAt(parser.i);
            if (c === '{') {
                if (parser.i === i) {
                    hasBraces = 1;
                }
                parser.GetArgument(name);
                j = parser.i - i;
            }
            else if (MatchParam(parser, param)) {
                if (hasBraces) {
                    i++;
                    j -= 2;
                }
                return parser.string.substr(i, j);
            }
            else if (c === '\\') {
                parser.i++;
                j++;
                hasBraces = 0;
                var match = parser.string.substr(parser.i).match(/[a-z]+|./i);
                if (match) {
                    parser.i += match[0].length;
                    j = parser.i - i;
                }
            }
            else {
                parser.i++;
                j++;
                hasBraces = 0;
            }
        }
        throw new TexError_js_1.default('RunawayArgument', 'Runaway argument for %1?', name);
    }
    NewcommandUtil.GetParameter = GetParameter;
    function MatchParam(parser, param) {
        if (parser.string.substr(parser.i, param.length) !== param) {
            return 0;
        }
        if (param.match(/\\[a-z]+$/i) &&
            parser.string.charAt(parser.i + param.length).match(/[a-z]/i)) {
            return 0;
        }
        parser.i += param.length;
        return 1;
    }
    NewcommandUtil.MatchParam = MatchParam;
    function addDelimiter(parser, cs, char, attr) {
        var handlers = parser.configuration.handlers;
        var handler = handlers.retrieve(NewcommandUtil.NEW_DELIMITER);
        handler.add(cs, new Symbol_js_1.Symbol(cs, char, attr));
    }
    NewcommandUtil.addDelimiter = addDelimiter;
    function addMacro(parser, cs, func, attr, symbol) {
        if (symbol === void 0) { symbol = ''; }
        var handlers = parser.configuration.handlers;
        var handler = handlers.retrieve(NewcommandUtil.NEW_COMMAND);
        handler.add(cs, new Symbol_js_1.Macro(symbol ? symbol : cs, func, attr));
    }
    NewcommandUtil.addMacro = addMacro;
    function addEnvironment(parser, env, func, attr) {
        var handlers = parser.configuration.handlers;
        var handler = handlers.retrieve(NewcommandUtil.NEW_ENVIRONMENT);
        handler.add(env, new Symbol_js_1.Macro(env, func, attr));
    }
    NewcommandUtil.addEnvironment = addEnvironment;
    NewcommandUtil.NEW_DELIMITER = 'new-Delimiter';
    NewcommandUtil.NEW_COMMAND = 'new-Command';
    NewcommandUtil.NEW_ENVIRONMENT = 'new-Environment';
})(NewcommandUtil || (NewcommandUtil = {}));
exports["default"] = NewcommandUtil;
//# sourceMappingURL=NewcommandUtil.js.map

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

/***/ 945:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.ParseMethods["default"];

/***/ }),

/***/ 398:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.ParseUtil["default"];

/***/ }),

/***/ 76:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlStack = MathJax._.input.tex.StackItem.MmlStack;
exports.BaseItem = MathJax._.input.tex.StackItem.BaseItem;

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/newcommand/NewcommandConfiguration.js
var NewcommandConfiguration = __webpack_require__(48);
// EXTERNAL MODULE: ../../../../../../js/input/tex/newcommand/NewcommandItems.js
var NewcommandItems = __webpack_require__(205);
// EXTERNAL MODULE: ../../../../../../js/input/tex/newcommand/NewcommandMethods.js
var NewcommandMethods = __webpack_require__(107);
// EXTERNAL MODULE: ../../../../../../js/input/tex/newcommand/NewcommandUtil.js
var NewcommandUtil = __webpack_require__(406);
;// CONCATENATED MODULE: ./lib/newcommand.js







if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/newcommand', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        newcommand: {
          NewcommandConfiguration: NewcommandConfiguration,
          NewcommandItems: NewcommandItems,
          NewcommandMethods: NewcommandMethods,
          NewcommandUtil: NewcommandUtil
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./newcommand.js

}();
/******/ })()
;