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

/***/ 333:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.BussproofsConfiguration = void 0;
var Configuration_js_1 = __webpack_require__(251);
var BussproofsItems_js_1 = __webpack_require__(854);
var BussproofsUtil_js_1 = __webpack_require__(378);
__webpack_require__(116);
exports.BussproofsConfiguration = Configuration_js_1.Configuration.create('bussproofs', {
    handler: {
        macro: ['Bussproofs-macros'],
        environment: ['Bussproofs-environments']
    },
    items: (_a = {},
        _a[BussproofsItems_js_1.ProofTreeItem.prototype.kind] = BussproofsItems_js_1.ProofTreeItem,
        _a),
    preprocessors: [
        [BussproofsUtil_js_1.saveDocument, 1]
    ],
    postprocessors: [
        [BussproofsUtil_js_1.clearDocument, 3],
        [BussproofsUtil_js_1.makeBsprAttributes, 2],
        [BussproofsUtil_js_1.balanceRules, 1]
    ]
});
//# sourceMappingURL=BussproofsConfiguration.js.map

/***/ }),

/***/ 854:
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ProofTreeItem = void 0;
var TexError_js_1 = __importDefault(__webpack_require__(402));
var StackItem_js_1 = __webpack_require__(76);
var Stack_js_1 = __importDefault(__webpack_require__(935));
var BussproofsUtil = __importStar(__webpack_require__(378));
var ProofTreeItem = (function (_super) {
    __extends(ProofTreeItem, _super);
    function ProofTreeItem() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.leftLabel = null;
        _this.rigthLabel = null;
        _this.innerStack = new Stack_js_1.default(_this.factory, {}, true);
        return _this;
    }
    Object.defineProperty(ProofTreeItem.prototype, "kind", {
        get: function () {
            return 'proofTree';
        },
        enumerable: false,
        configurable: true
    });
    ProofTreeItem.prototype.checkItem = function (item) {
        if (item.isKind('end') && item.getName() === 'prooftree') {
            var node = this.toMml();
            BussproofsUtil.setProperty(node, 'proof', true);
            return [[this.factory.create('mml', node), item], true];
        }
        if (item.isKind('stop')) {
            throw new TexError_js_1.default('EnvMissingEnd', 'Missing \\end{%1}', this.getName());
        }
        this.innerStack.Push(item);
        return StackItem_js_1.BaseItem.fail;
    };
    ProofTreeItem.prototype.toMml = function () {
        var tree = _super.prototype.toMml.call(this);
        var start = this.innerStack.Top();
        if (start.isKind('start') && !start.Size()) {
            return tree;
        }
        this.innerStack.Push(this.factory.create('stop'));
        var prefix = this.innerStack.Top().toMml();
        return this.create('node', 'mrow', [prefix, tree], {});
    };
    return ProofTreeItem;
}(StackItem_js_1.BaseItem));
exports.ProofTreeItem = ProofTreeItem;
//# sourceMappingURL=BussproofsItems.js.map

/***/ }),

/***/ 116:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
var BussproofsMethods_js_1 = __importDefault(__webpack_require__(827));
var ParseMethods_js_1 = __importDefault(__webpack_require__(945));
var SymbolMap_js_1 = __webpack_require__(871);
new SymbolMap_js_1.CommandMap('Bussproofs-macros', {
    AxiomC: 'Axiom',
    UnaryInfC: ['Inference', 1],
    BinaryInfC: ['Inference', 2],
    TrinaryInfC: ['Inference', 3],
    QuaternaryInfC: ['Inference', 4],
    QuinaryInfC: ['Inference', 5],
    RightLabel: ['Label', 'right'],
    LeftLabel: ['Label', 'left'],
    AXC: 'Axiom',
    UIC: ['Inference', 1],
    BIC: ['Inference', 2],
    TIC: ['Inference', 3],
    RL: ['Label', 'right'],
    LL: ['Label', 'left'],
    noLine: ['SetLine', 'none', false],
    singleLine: ['SetLine', 'solid', false],
    solidLine: ['SetLine', 'solid', false],
    dashedLine: ['SetLine', 'dashed', false],
    alwaysNoLine: ['SetLine', 'none', true],
    alwaysSingleLine: ['SetLine', 'solid', true],
    alwaysSolidLine: ['SetLine', 'solid', true],
    alwaysDashedLine: ['SetLine', 'dashed', true],
    rootAtTop: ['RootAtTop', true],
    alwaysRootAtTop: ['RootAtTop', true],
    rootAtBottom: ['RootAtTop', false],
    alwaysRootAtBottom: ['RootAtTop', false],
    fCenter: 'FCenter',
    Axiom: 'AxiomF',
    UnaryInf: ['InferenceF', 1],
    BinaryInf: ['InferenceF', 2],
    TrinaryInf: ['InferenceF', 3],
    QuaternaryInf: ['InferenceF', 4],
    QuinaryInf: ['InferenceF', 5]
}, BussproofsMethods_js_1.default);
new SymbolMap_js_1.EnvironmentMap('Bussproofs-environments', ParseMethods_js_1.default.environment, {
    prooftree: ['Prooftree', null, false]
}, BussproofsMethods_js_1.default);
//# sourceMappingURL=BussproofsMappings.js.map

/***/ }),

/***/ 827:
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
var TexError_js_1 = __importDefault(__webpack_require__(402));
var TexParser_js_1 = __importDefault(__webpack_require__(193));
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var BussproofsUtil = __importStar(__webpack_require__(378));
var BussproofsMethods = {};
BussproofsMethods.Prooftree = function (parser, begin) {
    parser.Push(begin);
    var newItem = parser.itemFactory.create('proofTree').
        setProperties({ name: begin.getName(),
        line: 'solid', currentLine: 'solid', rootAtTop: false });
    return newItem;
};
BussproofsMethods.Axiom = function (parser, name) {
    var top = parser.stack.Top();
    if (top.kind !== 'proofTree') {
        throw new TexError_js_1.default('IllegalProofCommand', 'Proof commands only allowed in prooftree environment.');
    }
    var content = paddedContent(parser, parser.GetArgument(name));
    BussproofsUtil.setProperty(content, 'axiom', true);
    top.Push(content);
};
var paddedContent = function (parser, content) {
    var nodes = ParseUtil_js_1.default.internalMath(parser, ParseUtil_js_1.default.trimSpaces(content), 0);
    if (!nodes[0].childNodes[0].childNodes.length) {
        return parser.create('node', 'mrow', []);
    }
    var lpad = parser.create('node', 'mspace', [], { width: '.5ex' });
    var rpad = parser.create('node', 'mspace', [], { width: '.5ex' });
    return parser.create('node', 'mrow', __spreadArray(__spreadArray([lpad], __read(nodes), false), [rpad], false));
};
BussproofsMethods.Inference = function (parser, name, n) {
    var top = parser.stack.Top();
    if (top.kind !== 'proofTree') {
        throw new TexError_js_1.default('IllegalProofCommand', 'Proof commands only allowed in prooftree environment.');
    }
    if (top.Size() < n) {
        throw new TexError_js_1.default('BadProofTree', 'Proof tree badly specified.');
    }
    var rootAtTop = top.getProperty('rootAtTop');
    var childCount = (n === 1 && !top.Peek()[0].childNodes.length) ? 0 : n;
    var children = [];
    do {
        if (children.length) {
            children.unshift(parser.create('node', 'mtd', [], {}));
        }
        children.unshift(parser.create('node', 'mtd', [top.Pop()], { 'rowalign': (rootAtTop ? 'top' : 'bottom') }));
        n--;
    } while (n > 0);
    var row = parser.create('node', 'mtr', children, {});
    var table = parser.create('node', 'mtable', [row], { framespacing: '0 0' });
    var conclusion = paddedContent(parser, parser.GetArgument(name));
    var style = top.getProperty('currentLine');
    if (style !== top.getProperty('line')) {
        top.setProperty('currentLine', top.getProperty('line'));
    }
    var rule = createRule(parser, table, [conclusion], top.getProperty('left'), top.getProperty('right'), style, rootAtTop);
    top.setProperty('left', null);
    top.setProperty('right', null);
    BussproofsUtil.setProperty(rule, 'inference', childCount);
    parser.configuration.addNode('inference', rule);
    top.Push(rule);
};
function createRule(parser, premise, conclusions, left, right, style, rootAtTop) {
    var upper = parser.create('node', 'mtr', [parser.create('node', 'mtd', [premise], {})], {});
    var lower = parser.create('node', 'mtr', [parser.create('node', 'mtd', conclusions, {})], {});
    var rule = parser.create('node', 'mtable', rootAtTop ? [lower, upper] : [upper, lower], { align: 'top 2', rowlines: style, framespacing: '0 0' });
    BussproofsUtil.setProperty(rule, 'inferenceRule', rootAtTop ? 'up' : 'down');
    var leftLabel, rightLabel;
    if (left) {
        leftLabel = parser.create('node', 'mpadded', [left], { height: '+.5em', width: '+.5em', voffset: '-.15em' });
        BussproofsUtil.setProperty(leftLabel, 'prooflabel', 'left');
    }
    if (right) {
        rightLabel = parser.create('node', 'mpadded', [right], { height: '+.5em', width: '+.5em', voffset: '-.15em' });
        BussproofsUtil.setProperty(rightLabel, 'prooflabel', 'right');
    }
    var children, label;
    if (left && right) {
        children = [leftLabel, rule, rightLabel];
        label = 'both';
    }
    else if (left) {
        children = [leftLabel, rule];
        label = 'left';
    }
    else if (right) {
        children = [rule, rightLabel];
        label = 'right';
    }
    else {
        return rule;
    }
    rule = parser.create('node', 'mrow', children);
    BussproofsUtil.setProperty(rule, 'labelledRule', label);
    return rule;
}
BussproofsMethods.Label = function (parser, name, side) {
    var top = parser.stack.Top();
    if (top.kind !== 'proofTree') {
        throw new TexError_js_1.default('IllegalProofCommand', 'Proof commands only allowed in prooftree environment.');
    }
    var content = ParseUtil_js_1.default.internalMath(parser, parser.GetArgument(name), 0);
    var label = (content.length > 1) ?
        parser.create('node', 'mrow', content, {}) : content[0];
    top.setProperty(side, label);
};
BussproofsMethods.SetLine = function (parser, _name, style, always) {
    var top = parser.stack.Top();
    if (top.kind !== 'proofTree') {
        throw new TexError_js_1.default('IllegalProofCommand', 'Proof commands only allowed in prooftree environment.');
    }
    top.setProperty('currentLine', style);
    if (always) {
        top.setProperty('line', style);
    }
};
BussproofsMethods.RootAtTop = function (parser, _name, where) {
    var top = parser.stack.Top();
    if (top.kind !== 'proofTree') {
        throw new TexError_js_1.default('IllegalProofCommand', 'Proof commands only allowed in prooftree environment.');
    }
    top.setProperty('rootAtTop', where);
};
BussproofsMethods.AxiomF = function (parser, name) {
    var top = parser.stack.Top();
    if (top.kind !== 'proofTree') {
        throw new TexError_js_1.default('IllegalProofCommand', 'Proof commands only allowed in prooftree environment.');
    }
    var line = parseFCenterLine(parser, name);
    BussproofsUtil.setProperty(line, 'axiom', true);
    top.Push(line);
};
function parseFCenterLine(parser, name) {
    var dollar = parser.GetNext();
    if (dollar !== '$') {
        throw new TexError_js_1.default('IllegalUseOfCommand', 'Use of %1 does not match it\'s definition.', name);
    }
    parser.i++;
    var axiom = parser.GetUpTo(name, '$');
    if (axiom.indexOf('\\fCenter') === -1) {
        throw new TexError_js_1.default('IllegalUseOfCommand', 'Missing \\fCenter in %1.', name);
    }
    var _a = __read(axiom.split('\\fCenter'), 2), prem = _a[0], conc = _a[1];
    var premise = (new TexParser_js_1.default(prem, parser.stack.env, parser.configuration)).mml();
    var conclusion = (new TexParser_js_1.default(conc, parser.stack.env, parser.configuration)).mml();
    var fcenter = (new TexParser_js_1.default('\\fCenter', parser.stack.env, parser.configuration)).mml();
    var left = parser.create('node', 'mtd', [premise], {});
    var middle = parser.create('node', 'mtd', [fcenter], {});
    var right = parser.create('node', 'mtd', [conclusion], {});
    var row = parser.create('node', 'mtr', [left, middle, right], {});
    var table = parser.create('node', 'mtable', [row], { columnspacing: '.5ex', columnalign: 'center 2' });
    BussproofsUtil.setProperty(table, 'sequent', true);
    parser.configuration.addNode('sequent', row);
    return table;
}
BussproofsMethods.FCenter = function (_parser, _name) { };
BussproofsMethods.InferenceF = function (parser, name, n) {
    var top = parser.stack.Top();
    if (top.kind !== 'proofTree') {
        throw new TexError_js_1.default('IllegalProofCommand', 'Proof commands only allowed in prooftree environment.');
    }
    if (top.Size() < n) {
        throw new TexError_js_1.default('BadProofTree', 'Proof tree badly specified.');
    }
    var rootAtTop = top.getProperty('rootAtTop');
    var childCount = (n === 1 && !top.Peek()[0].childNodes.length) ? 0 : n;
    var children = [];
    do {
        if (children.length) {
            children.unshift(parser.create('node', 'mtd', [], {}));
        }
        children.unshift(parser.create('node', 'mtd', [top.Pop()], { 'rowalign': (rootAtTop ? 'top' : 'bottom') }));
        n--;
    } while (n > 0);
    var row = parser.create('node', 'mtr', children, {});
    var table = parser.create('node', 'mtable', [row], { framespacing: '0 0' });
    var conclusion = parseFCenterLine(parser, name);
    var style = top.getProperty('currentLine');
    if (style !== top.getProperty('line')) {
        top.setProperty('currentLine', top.getProperty('line'));
    }
    var rule = createRule(parser, table, [conclusion], top.getProperty('left'), top.getProperty('right'), style, rootAtTop);
    top.setProperty('left', null);
    top.setProperty('right', null);
    BussproofsUtil.setProperty(rule, 'inference', childCount);
    parser.configuration.addNode('inference', rule);
    top.Push(rule);
};
exports["default"] = BussproofsMethods;
//# sourceMappingURL=BussproofsMethods.js.map

/***/ }),

/***/ 378:
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
var _a;
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.clearDocument = exports.saveDocument = exports.makeBsprAttributes = exports.removeProperty = exports.getProperty = exports.setProperty = exports.balanceRules = void 0;
var NodeUtil_js_1 = __importDefault(__webpack_require__(748));
var ParseUtil_js_1 = __importDefault(__webpack_require__(398));
var doc = null;
var item = null;
var getBBox = function (node) {
    item.root = node;
    var width = doc.outputJax.getBBox(item, doc).w;
    return width;
};
var getRule = function (node) {
    var i = 0;
    while (node && !NodeUtil_js_1.default.isType(node, 'mtable')) {
        if (NodeUtil_js_1.default.isType(node, 'text')) {
            return null;
        }
        if (NodeUtil_js_1.default.isType(node, 'mrow')) {
            node = node.childNodes[0];
            i = 0;
            continue;
        }
        node = node.parent.childNodes[i];
        i++;
    }
    return node;
};
var getPremises = function (rule, direction) {
    return rule.childNodes[direction === 'up' ? 1 : 0].childNodes[0].
        childNodes[0].childNodes[0].childNodes[0];
};
var getPremise = function (premises, n) {
    return premises.childNodes[n].childNodes[0].childNodes[0];
};
var firstPremise = function (premises) {
    return getPremise(premises, 0);
};
var lastPremise = function (premises) {
    return getPremise(premises, premises.childNodes.length - 1);
};
var getConclusion = function (rule, direction) {
    return rule.childNodes[direction === 'up' ? 0 : 1].childNodes[0].childNodes[0].childNodes[0];
};
var getColumn = function (inf) {
    while (inf && !NodeUtil_js_1.default.isType(inf, 'mtd')) {
        inf = inf.parent;
    }
    return inf;
};
var nextSibling = function (inf) {
    return inf.parent.childNodes[inf.parent.childNodes.indexOf(inf) + 1];
};
var previousSibling = function (inf) {
    return inf.parent.childNodes[inf.parent.childNodes.indexOf(inf) - 1];
};
var getParentInf = function (inf) {
    while (inf && (0, exports.getProperty)(inf, 'inference') == null) {
        inf = inf.parent;
    }
    return inf;
};
var getSpaces = function (inf, rule, right) {
    if (right === void 0) { right = false; }
    var result = 0;
    if (inf === rule) {
        return result;
    }
    if (inf !== rule.parent) {
        var children_1 = inf.childNodes;
        var index_1 = right ? children_1.length - 1 : 0;
        if (NodeUtil_js_1.default.isType(children_1[index_1], 'mspace')) {
            result += getBBox(children_1[index_1]);
        }
        inf = rule.parent;
    }
    if (inf === rule) {
        return result;
    }
    var children = inf.childNodes;
    var index = right ? children.length - 1 : 0;
    if (children[index] !== rule) {
        result += getBBox(children[index]);
    }
    return result;
};
var adjustValue = function (inf, right) {
    if (right === void 0) { right = false; }
    var rule = getRule(inf);
    var conc = getConclusion(rule, (0, exports.getProperty)(rule, 'inferenceRule'));
    var w = getSpaces(inf, rule, right);
    var x = getBBox(rule);
    var y = getBBox(conc);
    return w + ((x - y) / 2);
};
var addSpace = function (config, inf, space, right) {
    if (right === void 0) { right = false; }
    if ((0, exports.getProperty)(inf, 'inferenceRule') ||
        (0, exports.getProperty)(inf, 'labelledRule')) {
        var mrow = config.nodeFactory.create('node', 'mrow');
        inf.parent.replaceChild(mrow, inf);
        mrow.setChildren([inf]);
        moveProperties(inf, mrow);
        inf = mrow;
    }
    var index = right ? inf.childNodes.length - 1 : 0;
    var mspace = inf.childNodes[index];
    if (NodeUtil_js_1.default.isType(mspace, 'mspace')) {
        NodeUtil_js_1.default.setAttribute(mspace, 'width', ParseUtil_js_1.default.Em(ParseUtil_js_1.default.dimen2em(NodeUtil_js_1.default.getAttribute(mspace, 'width')) + space));
        return;
    }
    mspace = config.nodeFactory.create('node', 'mspace', [], { width: ParseUtil_js_1.default.Em(space) });
    if (right) {
        inf.appendChild(mspace);
        return;
    }
    mspace.parent = inf;
    inf.childNodes.unshift(mspace);
};
var moveProperties = function (src, dest) {
    var props = ['inference', 'proof', 'maxAdjust', 'labelledRule'];
    props.forEach(function (x) {
        var value = (0, exports.getProperty)(src, x);
        if (value != null) {
            (0, exports.setProperty)(dest, x, value);
            (0, exports.removeProperty)(src, x);
        }
    });
};
var adjustSequents = function (config) {
    var sequents = config.nodeLists['sequent'];
    if (!sequents) {
        return;
    }
    for (var i = sequents.length - 1, seq = void 0; seq = sequents[i]; i--) {
        if ((0, exports.getProperty)(seq, 'sequentProcessed')) {
            (0, exports.removeProperty)(seq, 'sequentProcessed');
            continue;
        }
        var collect = [];
        var inf = getParentInf(seq);
        if ((0, exports.getProperty)(inf, 'inference') !== 1) {
            continue;
        }
        collect.push(seq);
        while ((0, exports.getProperty)(inf, 'inference') === 1) {
            inf = getRule(inf);
            var premise = firstPremise(getPremises(inf, (0, exports.getProperty)(inf, 'inferenceRule')));
            var sequent = ((0, exports.getProperty)(premise, 'inferenceRule')) ?
                getConclusion(premise, (0, exports.getProperty)(premise, 'inferenceRule')) :
                premise;
            if ((0, exports.getProperty)(sequent, 'sequent')) {
                seq = sequent.childNodes[0];
                collect.push(seq);
                (0, exports.setProperty)(seq, 'sequentProcessed', true);
            }
            inf = premise;
        }
        adjustSequentPairwise(config, collect);
    }
};
var addSequentSpace = function (config, sequent, position, direction, width) {
    var mspace = config.nodeFactory.create('node', 'mspace', [], { width: ParseUtil_js_1.default.Em(width) });
    if (direction === 'left') {
        var row = sequent.childNodes[position].childNodes[0];
        mspace.parent = row;
        row.childNodes.unshift(mspace);
    }
    else {
        sequent.childNodes[position].appendChild(mspace);
    }
    (0, exports.setProperty)(sequent.parent, 'sequentAdjust_' + direction, width);
};
var adjustSequentPairwise = function (config, sequents) {
    var top = sequents.pop();
    while (sequents.length) {
        var bottom = sequents.pop();
        var _a = __read(compareSequents(top, bottom), 2), left = _a[0], right = _a[1];
        if ((0, exports.getProperty)(top.parent, 'axiom')) {
            addSequentSpace(config, left < 0 ? top : bottom, 0, 'left', Math.abs(left));
            addSequentSpace(config, right < 0 ? top : bottom, 2, 'right', Math.abs(right));
        }
        top = bottom;
    }
};
var compareSequents = function (top, bottom) {
    var tr = getBBox(top.childNodes[2]);
    var br = getBBox(bottom.childNodes[2]);
    var tl = getBBox(top.childNodes[0]);
    var bl = getBBox(bottom.childNodes[0]);
    var dl = tl - bl;
    var dr = tr - br;
    return [dl, dr];
};
var balanceRules = function (arg) {
    var e_1, _a;
    item = new arg.document.options.MathItem('', null, arg.math.display);
    var config = arg.data;
    adjustSequents(config);
    var inferences = config.nodeLists['inference'] || [];
    try {
        for (var inferences_1 = __values(inferences), inferences_1_1 = inferences_1.next(); !inferences_1_1.done; inferences_1_1 = inferences_1.next()) {
            var inf = inferences_1_1.value;
            var isProof = (0, exports.getProperty)(inf, 'proof');
            var rule = getRule(inf);
            var premises = getPremises(rule, (0, exports.getProperty)(rule, 'inferenceRule'));
            var premiseF = firstPremise(premises);
            if ((0, exports.getProperty)(premiseF, 'inference')) {
                var adjust_1 = adjustValue(premiseF);
                if (adjust_1) {
                    addSpace(config, premiseF, -adjust_1);
                    var w_1 = getSpaces(inf, rule, false);
                    addSpace(config, inf, adjust_1 - w_1);
                }
            }
            var premiseL = lastPremise(premises);
            if ((0, exports.getProperty)(premiseL, 'inference') == null) {
                continue;
            }
            var adjust = adjustValue(premiseL, true);
            addSpace(config, premiseL, -adjust, true);
            var w = getSpaces(inf, rule, true);
            var maxAdjust = (0, exports.getProperty)(inf, 'maxAdjust');
            if (maxAdjust != null) {
                adjust = Math.max(adjust, maxAdjust);
            }
            var column = void 0;
            if (isProof || !(column = getColumn(inf))) {
                addSpace(config, (0, exports.getProperty)(inf, 'proof') ? inf : inf.parent, adjust - w, true);
                continue;
            }
            var sibling = nextSibling(column);
            if (sibling) {
                var pos = config.nodeFactory.create('node', 'mspace', [], { width: adjust - w + 'em' });
                sibling.appendChild(pos);
                inf.removeProperty('maxAdjust');
                continue;
            }
            var parentRule = getParentInf(column);
            if (!parentRule) {
                continue;
            }
            adjust = (0, exports.getProperty)(parentRule, 'maxAdjust') ?
                Math.max((0, exports.getProperty)(parentRule, 'maxAdjust'), adjust) : adjust;
            (0, exports.setProperty)(parentRule, 'maxAdjust', adjust);
        }
    }
    catch (e_1_1) { e_1 = { error: e_1_1 }; }
    finally {
        try {
            if (inferences_1_1 && !inferences_1_1.done && (_a = inferences_1.return)) _a.call(inferences_1);
        }
        finally { if (e_1) throw e_1.error; }
    }
};
exports.balanceRules = balanceRules;
var property_prefix = 'bspr_';
var blacklistedProperties = (_a = {},
    _a[property_prefix + 'maxAdjust'] = true,
    _a);
var setProperty = function (node, property, value) {
    NodeUtil_js_1.default.setProperty(node, property_prefix + property, value);
};
exports.setProperty = setProperty;
var getProperty = function (node, property) {
    return NodeUtil_js_1.default.getProperty(node, property_prefix + property);
};
exports.getProperty = getProperty;
var removeProperty = function (node, property) {
    node.removeProperty(property_prefix + property);
};
exports.removeProperty = removeProperty;
var makeBsprAttributes = function (arg) {
    arg.data.root.walkTree(function (mml, _data) {
        var attr = [];
        mml.getPropertyNames().forEach(function (x) {
            if (!blacklistedProperties[x] && x.match(RegExp('^' + property_prefix))) {
                attr.push(x + ':' + mml.getProperty(x));
            }
        });
        if (attr.length) {
            NodeUtil_js_1.default.setAttribute(mml, 'semantics', attr.join(';'));
        }
    });
};
exports.makeBsprAttributes = makeBsprAttributes;
var saveDocument = function (arg) {
    doc = arg.document;
    if (!('getBBox' in doc.outputJax)) {
        throw Error('The bussproofs extension requires an output jax with a getBBox() method');
    }
};
exports.saveDocument = saveDocument;
var clearDocument = function (_arg) {
    doc = null;
};
exports.clearDocument = clearDocument;
//# sourceMappingURL=BussproofsUtil.js.map

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

/***/ 935:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.Stack["default"];

/***/ }),

/***/ 76:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.MmlStack = MathJax._.input.tex.StackItem.MmlStack;
exports.BaseItem = MathJax._.input.tex.StackItem.BaseItem;

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

/***/ 193:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports["default"] = MathJax._.input.tex.TexParser["default"];

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/bussproofs/BussproofsConfiguration.js
var BussproofsConfiguration = __webpack_require__(333);
// EXTERNAL MODULE: ../../../../../../js/input/tex/bussproofs/BussproofsItems.js
var BussproofsItems = __webpack_require__(854);
// EXTERNAL MODULE: ../../../../../../js/input/tex/bussproofs/BussproofsMethods.js
var BussproofsMethods = __webpack_require__(827);
// EXTERNAL MODULE: ../../../../../../js/input/tex/bussproofs/BussproofsUtil.js
var BussproofsUtil = __webpack_require__(378);
;// CONCATENATED MODULE: ./lib/bussproofs.js







if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/bussproofs', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        bussproofs: {
          BussproofsConfiguration: BussproofsConfiguration,
          BussproofsItems: BussproofsItems,
          BussproofsMethods: BussproofsMethods,
          BussproofsUtil: BussproofsUtil
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./bussproofs.js

}();
/******/ })()
;