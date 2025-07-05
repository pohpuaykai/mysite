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

/***/ 941:
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
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.TagFormatConfiguration = exports.tagformatConfig = void 0;
var Configuration_js_1 = __webpack_require__(251);
var Tags_js_1 = __webpack_require__(680);
var tagID = 0;
function tagformatConfig(config, jax) {
    var tags = jax.parseOptions.options.tags;
    if (tags !== 'base' && config.tags.hasOwnProperty(tags)) {
        Tags_js_1.TagsFactory.add(tags, config.tags[tags]);
    }
    var TagClass = Tags_js_1.TagsFactory.create(jax.parseOptions.options.tags).constructor;
    var TagFormat = (function (_super) {
        __extends(TagFormat, _super);
        function TagFormat() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        TagFormat.prototype.formatNumber = function (n) {
            return jax.parseOptions.options.tagformat.number(n);
        };
        TagFormat.prototype.formatTag = function (tag) {
            return jax.parseOptions.options.tagformat.tag(tag);
        };
        TagFormat.prototype.formatId = function (id) {
            return jax.parseOptions.options.tagformat.id(id);
        };
        TagFormat.prototype.formatUrl = function (id, base) {
            return jax.parseOptions.options.tagformat.url(id, base);
        };
        return TagFormat;
    }(TagClass));
    tagID++;
    var tagName = 'configTags-' + tagID;
    Tags_js_1.TagsFactory.add(tagName, TagFormat);
    jax.parseOptions.options.tags = tagName;
}
exports.tagformatConfig = tagformatConfig;
exports.TagFormatConfiguration = Configuration_js_1.Configuration.create('tagformat', {
    config: [tagformatConfig, 10],
    options: {
        tagformat: {
            number: function (n) { return n.toString(); },
            tag: function (tag) { return '(' + tag + ')'; },
            id: function (id) { return 'mjx-eqn:' + id.replace(/\s/g, '_'); },
            url: function (id, base) { return base + '#' + encodeURIComponent(id); },
        }
    }
});
//# sourceMappingURL=TagFormatConfiguration.js.map

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

/***/ 680:
/***/ (function(__unused_webpack_module, exports) {



Object.defineProperty(exports, "__esModule", ({
  value: true
}));
exports.Label = MathJax._.input.tex.Tags.Label;
exports.TagInfo = MathJax._.input.tex.Tags.TagInfo;
exports.AbstractTags = MathJax._.input.tex.Tags.AbstractTags;
exports.NoTags = MathJax._.input.tex.Tags.NoTags;
exports.AllTags = MathJax._.input.tex.Tags.AllTags;
exports.TagsFactory = MathJax._.input.tex.Tags.TagsFactory;

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
// EXTERNAL MODULE: ../../../../../../js/input/tex/tagformat/TagFormatConfiguration.js
var TagFormatConfiguration = __webpack_require__(941);
;// CONCATENATED MODULE: ./lib/tagformat.js




if (MathJax.loader) {
  MathJax.loader.checkVersion('[tex]/tagformat', version/* VERSION */.q, 'tex-extension');
}

(0,global/* combineWithMathJax */.r8)({
  _: {
    input: {
      tex: {
        tagformat: {
          TagFormatConfiguration: TagFormatConfiguration
        }
      }
    }
  }
});
;// CONCATENATED MODULE: ./tagformat.js

}();
/******/ })()
;