webpackJsonp([0],{XTEM:function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=s("P9l9"),a={data:function(){return{tableData:{data:[],expands:[]}}},methods:{firstGet:function(){var e=this;this.$http.get(r.a).then(function(e){return e.json()}).then(function(t){console.log(t.data),e.$set(e.tableData,"data",t.data)})},Get:function(){var e=this;this.$http.get(r.a).then(function(e){return e.json()}).then(function(t){console.log(t.data),e.tableData.data.push(t.data[0])})},getRowKeys:function(e){return e.id}},created:function(){this.firstGet()},mounted:function(){var e=this;window.setInterval(function(){e.firstGet()},5e3)}},n={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tableData.data,"row-key":e.getRowKeys,"expand-row-keys":e.tableData.expands}},[s("el-table-column",{attrs:{type:"expand"},scopedSlots:e._u([{key:"default",fn:function(t){return[s("el-form",{staticClass:"demo-table-expand",attrs:{"label-position":"left",inline:""}},[s("el-form-item",{attrs:{label:"request_http_version"}},[s("span",[e._v(e._s(t.row.request_http_version))])]),e._v(" "),s("el-form-item",{attrs:{label:"request_method"}},[s("span",[e._v(e._s(t.row.request_method))])]),e._v(" "),s("el-form-item",{attrs:{label:"request_scheme"}},[s("span",[e._v(e._s(t.row.request_scheme))])]),e._v(" "),s("el-form-item",{attrs:{label:"request_port"}},[s("span",[e._v(e._s(t.row.request_port))])]),e._v(" "),s("el-form-item",{attrs:{label:"request_headers"}},[s("span",[e._v(e._s(t.row.request_headers))])]),e._v(" "),s("el-form-item",{attrs:{label:"request_headers"}},[s("span",[e._v(e._s(t.row.request_headers))])]),e._v(" "),s("el-form-item",{attrs:{label:"request_content"}},[s("span",[e._v(e._s(t.row.request_content))])]),e._v(" "),s("el-form-item",{attrs:{label:"response_http_version"}},[s("span",[e._v(e._s(t.row.response_http_version))])]),e._v(" "),s("el-form-item",{attrs:{label:"response_reason"}},[s("span",[e._v(e._s(t.row.response_reason))])]),e._v(" "),s("el-form-item",{attrs:{label:"response_text"}},[s("span",[e._v(e._s(t.row.request_headers))])]),e._v(" "),s("el-form-item",{attrs:{label:"response_headers"}},[s("span",[e._v(e._s(t.row.response_headers))])]),e._v(" "),s("el-form-item",{attrs:{label:"response_text"}},[s("span",[e._v(e._s(t.row.response_text))])]),e._v(" "),s("el-form-item",{attrs:{label:"response_content"}},[s("span",[e._v(e._s(t.row.response_content))])])],1)]}}])}),e._v(" "),s("el-table-column",{attrs:{label:"url",prop:"url"}})],1)},staticRenderFns:[]};var o=s("VU/8")(a,n,!1,function(e){s("sWTH")},null,null);t.default=o.exports},sWTH:function(e,t){}});
//# sourceMappingURL=0.327758e05023c7262619.js.map