// ws.js
var express = require('express');
var expressWs = require('express-ws');

var router = express.Router();
expressWs(router);

router
  .ws('/ifc', function (ws, req){
      ws.on('message', function (msg) {
          // 业务代码
          send("nih");
      })
   })
  .get('/ifc', function(req, resp) {
  })
  .post('/ifc', function(req, resp) {
  })
  

module.exports = router;