webpackJsonp([1],{"1JWS":function(e,t){},rNYc:function(e,t,o){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=o("2hMI"),l={data:function(){return{formLabelWidth:"120px",tableData:{data:[],expands:[]},addRedirect:!1,selectRedirectForm:{id:""},deleteRedirect:!1,deleteRedirectForm:{id:""},redirectUrl:!1,redirectUrlForm:{function_name:"RedirectUrl",Url:"",newUrl:""},redirectHost:!1,redirectHostForm:{function_name:"RedirectHost",Host:"",newHost:""},redirectPath:!1,redirectPathForm:{function_name:"RedirectPath",Host:"",newHost:"",Path:"",newPath:""},clearRedirect:!1,deleteAllRedirect:!1,redirectResponse:!1,redirectResponseForm:{function_name:"RedirectResponseText",Url:"",Response:""},redirectResponseStatusCode:!1,redirectResponseStatusCodeForm:{function_name:"RedirectResponseStatusCode",Url:"",NewStatusCode:""}}},created:function(){this.getAllRedirect()},mounted:function(){var e=this;window.setInterval(function(){e.getAllRedirect()},1e3)},methods:{getRowKeys:function(e){return e.id},getAllRedirect:function(){var e=this;this.$http.get(r.e).then(function(e){return e.json()}).then(function(t){e.tableData.data=t.data})},toggleSelection:function(e){var t=this;e?e.forEach(function(e){t.$refs.multipleTable.toggleRowSelection(e)}):this.$refs.multipleTable.clearSelection()},addRequestRedirectUrl:function(){var e=this;this.$http.post(r.b,this.redirectUrlForm).then(function(e){return e.json()}).then(function(t){"error"==t.code?e.$message({showClose:!0,message:"接口有错误，上传失败！"}):e.redirectUrl=!1})},addRequestRedirectHost:function(){var e=this;this.$http.post(r.a,this.redirectHostForm).then(function(e){return e.json()}).then(function(t){"error"==t.code?e.$message({showClose:!0,message:"接口有错误，添加失败！"}):e.redirectHost=!1})},addResponseRedirect:function(){var e=this;this.$http.post(r.c,this.redirectResponseForm).then(function(e){return e.json()}).then(function(t){"error"==t.code?e.$message({showClose:!0,message:"接口有错误，添加失败！\n"+t.message}):e.redirectResponse=!1})},addResponseStatusCodeRedirect:function(){var e=this;this.$http.post(r.d,this.redirectResponseStatusCodeForm).then(function(e){return e.json()}).then(function(t){"error"==t.code?e.$message({showClose:!0,message:"接口有错误，添加失败！\n"+t.message}):e.redirectResponseStatusCode=!1})},deleteAllRequestRedirect:function(){var e=this;this.$http.get(r.j).then(function(e){return e.json()}).then(function(t){"error"==t.code?e.$message({showClose:!0,message:"接口有错误，清理失败！"}):e.deleteAllRedirect=!1})},deleteIdRequestRedirect:function(){var e=this;this.$http.post(r.l,this.deleteRedirectForm).then(function(e){return e.json()}).then(function(t){"error"==t.code?e.$message({showClose:!0,message:"接口有错误，添加失败！"}):e.deleteRedirect=!1})},selecetRequestRedirect:function(){var e=this;new FormData;this.$http.post(r.v,this.selectRedirectForm).then(function(e){return e.json()}).then(function(t){if("error"==t.code){var o=t.message;e.$message({showClose:!0,message:"接口有错误，添加失败！"+o})}else e.addRedirect=!1})},clearSelectedRequestRedirect:function(){var e=this;this.$http.get(r.k).then(function(e){return e.json()}).then(function(t){console.log(t.code),"error"==t.code?e.$message({showClose:!0,message:"接口有错误，清理失败！"}):e.clearRedirect=!1})}}},s={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",[o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.redirectUrl=!0}}},[e._v("新增url替换")]),e._v(" "),o("el-dialog",{attrs:{title:"新增url替换",visible:e.redirectUrl},on:{"update:visible":function(t){e.redirectUrl=t}}},[o("el-form",{attrs:{model:e.redirectUrlForm}},[o("el-form-item",{attrs:{label:"要替换的url","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off",type:"text"},model:{value:e.redirectUrlForm.Url,callback:function(t){e.$set(e.redirectUrlForm,"Url",t)},expression:"redirectUrlForm.Url"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"新的url","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off"},model:{value:e.redirectUrlForm.newUrl,callback:function(t){e.$set(e.redirectUrlForm,"newUrl",t)},expression:"redirectUrlForm.newUrl"}})],1)],1),e._v(" "),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.redirectUrl=!1}}},[e._v("取 消")]),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.addRequestRedirectUrl()}}},[e._v("确 定\n      ")])],1)],1),e._v(" "),o("el-dialog",{attrs:{title:"新增host替换",visible:e.redirectHost},on:{"update:visible":function(t){e.redirectHost=t}}},[o("el-form",{attrs:{model:e.redirectHostForm}},[o("el-form-item",{attrs:{label:"要替换的host","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off",type:"text"},model:{value:e.redirectHostForm.Host,callback:function(t){e.$set(e.redirectHostForm,"Host",t)},expression:"redirectHostForm.Host"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"新的host","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off"},model:{value:e.redirectHostForm.newHost,callback:function(t){e.$set(e.redirectHostForm,"newHost",t)},expression:"redirectHostForm.newHost"}})],1)],1),e._v(" "),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.redirectHost=!1}}},[e._v("取 消")]),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.addRequestRedirectHost()}}},[e._v("确 定")])],1)],1),e._v(" "),o("el-dialog",{attrs:{title:"新增path替换",visible:e.redirectPath},on:{"update:visible":function(t){e.redirectPath=t}}},[o("el-form",{attrs:{model:e.redirectPathForm}},[o("el-form-item",{attrs:{label:"要替换的host","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off",type:"text"},model:{value:e.redirectPathForm.Host,callback:function(t){e.$set(e.redirectPathForm,"Host",t)},expression:"redirectPathForm.Host"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"新的host","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off"},model:{value:e.redirectPathForm.newHost,callback:function(t){e.$set(e.redirectPathForm,"newHost",t)},expression:"redirectPathForm.newHost"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"要替换的path","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off"},model:{value:e.redirectPathForm.Path,callback:function(t){e.$set(e.redirectPathForm,"Path",t)},expression:"redirectPathForm.Path"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"新的path","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off"},model:{value:e.redirectPathForm.newPath,callback:function(t){e.$set(e.redirectPathForm,"newPath",t)},expression:"redirectPathForm.newPath"}})],1)],1),e._v(" "),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.redirectPath=!1}}},[e._v("取 消")]),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(e){}}},[e._v("确 定")])],1)],1),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.redirectResponse=!0}}},[e._v("新增Response替换")]),e._v(" "),o("el-dialog",{attrs:{title:"新增Response替换",visible:e.redirectResponse},on:{"update:visible":function(t){e.redirectResponse=t}}},[o("el-form",{attrs:{model:e.redirectResponseForm}},[o("el-form-item",{attrs:{label:"要替换的url","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off",type:"text"},model:{value:e.redirectResponseForm.Url,callback:function(t){e.$set(e.redirectResponseForm,"Url",t)},expression:"redirectResponseForm.Url"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"替换Response","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off"},model:{value:e.redirectResponseForm.Response,callback:function(t){e.$set(e.redirectResponseForm,"Response",t)},expression:"redirectResponseForm.Response"}})],1)],1),e._v(" "),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.redirectResponse=!1}}},[e._v("取 消")]),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.addResponseRedirect()}}},[e._v("确 定\n      ")])],1)],1),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.redirectResponseStatusCode=!0}}},[e._v("新增StatusCode替换")]),e._v(" "),o("el-dialog",{attrs:{title:"新增StatusCode替换",visible:e.redirectResponseStatusCode},on:{"update:visible":function(t){e.redirectResponseStatusCode=t}}},[o("el-form",{attrs:{model:e.redirectResponseStatusCodeForm}},[o("el-form-item",{attrs:{label:"要替换的url","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off",type:"text"},model:{value:e.redirectResponseStatusCodeForm.Url,callback:function(t){e.$set(e.redirectResponseStatusCodeForm,"Url",t)},expression:"redirectResponseStatusCodeForm.Url"}})],1),e._v(" "),o("el-form-item",{attrs:{label:"替换StatusCode","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off"},model:{value:e.redirectResponseStatusCodeForm.NewStatusCode,callback:function(t){e.$set(e.redirectResponseStatusCodeForm,"NewStatusCode",t)},expression:"redirectResponseStatusCodeForm.NewStatusCode"}})],1)],1),e._v(" "),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.redirectResponseStatusCode=!1}}},[e._v("取 消")]),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.addResponseStatusCodeRedirect()}}},[e._v("确 定\n      ")])],1)],1),e._v(" "),o("el-button",{attrs:{type:"success"},on:{click:function(t){e.addRedirect=!0}}},[e._v("添加一种替换策略")]),e._v(" "),o("el-dialog",{attrs:{title:"添加一种替换策略",visible:e.addRedirect},on:{"update:visible":function(t){e.addRedirect=t}}},[o("el-form",{attrs:{model:e.selectRedirectForm}},[o("el-form-item",{attrs:{label:"要添加的策略id","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off",type:"text"},model:{value:e.selectRedirectForm.id,callback:function(t){e.$set(e.selectRedirectForm,"id",t)},expression:"selectRedirectForm.id"}})],1)],1),e._v(" "),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.addRedirect=!1}}},[e._v("取 消")]),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.selecetRequestRedirect()}}},[e._v("确 定")])],1)],1),e._v(" "),o("el-button",{attrs:{type:"success"},on:{click:function(t){e.clearRedirect=!0}}},[e._v("清空正在使用的替换策略")]),e._v(" "),o("el-dialog",{attrs:{title:"取消正在使用的替换策略",visible:e.clearRedirect},on:{"update:visible":function(t){e.clearRedirect=t}}},[o("p",[e._v("点击确定清空所有正在使用的替换策略")]),e._v(" "),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.clearRedirect=!1}}},[e._v("取 消")]),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.clearSelectedRequestRedirect()}}},[e._v("确 定")])],1)]),e._v(" "),o("el-button",{attrs:{type:"danger"},on:{click:function(t){e.deleteRedirect=!0}}},[e._v("删除一个策略")]),e._v(" "),o("el-dialog",{attrs:{title:"删除一个策略",visible:e.deleteRedirect},on:{"update:visible":function(t){e.deleteRedirect=t}}},[o("el-form",{attrs:{model:e.deleteRedirectForm}},[o("el-form-item",{attrs:{label:"要删除的策略id","label-width":e.formLabelWidth}},[o("el-input",{attrs:{"auto-complete":"off",type:"text"},model:{value:e.deleteRedirectForm.id,callback:function(t){e.$set(e.deleteRedirectForm,"id",t)},expression:"deleteRedirectForm.id"}})],1)],1),e._v(" "),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.deleteRedirect=!1}}},[e._v("取 消")]),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.deleteIdRequestRedirect()}}},[e._v("确 定")])],1)],1),e._v(" "),o("el-button",{attrs:{type:"danger"},on:{click:function(t){e.deleteAllRedirect=!0}}},[e._v("删除所有替换策略")]),e._v(" "),o("el-dialog",{attrs:{title:"删除所有替换",visible:e.deleteAllRedirect},on:{"update:visible":function(t){e.deleteAllRedirect=t}}},[o("p",[e._v("点击确定清空说有的替换策略")]),e._v(" "),o("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[o("el-button",{on:{click:function(t){e.deleteAllRedirect=!1}}},[e._v("取 消")]),e._v(" "),o("el-button",{attrs:{type:"primary"},on:{click:function(t){e.deleteAllRequestRedirect()}}},[e._v("确 定")])],1)]),e._v(" "),o("el-table",{ref:"multipleTable",staticStyle:{width:"100%"},attrs:{data:e.tableData.data,"row-key":e.getRowKeys,"expand-row-keys":e.tableData.expands}},[o("el-table-column",{attrs:{type:"expand"},scopedSlots:e._u([{key:"default",fn:function(t){return[o("el-form",{staticClass:"demo-table-expand",attrs:{"label-position":"left",inline:""}},[o("el-form-item",{attrs:{label:"Parameter"}},[o("span",[e._v(e._s(t.row.parameter))])])],1)]}}])}),e._v(" "),o("el-table-column",{attrs:{label:"Id",prop:"id"}}),e._v(" "),o("el-table-column",{attrs:{label:"Function",prop:"function"}}),e._v(" "),o("el-table-column",{attrs:{label:"Describe",prop:"describe"}})],1)],1)},staticRenderFns:[]};var i=o("VU/8")(l,s,!1,function(e){o("1JWS")},null,null);t.default=i.exports}});
//# sourceMappingURL=1.167dcab58864b7363f9b.js.map