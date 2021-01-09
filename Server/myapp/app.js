var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var loginRouter = require('./routes/login');
// var mainRouter = require('./routes/main');
var session = require('express-session');
var app = express();

var exphbs = require('express-handlebars');
//静态资源托管中间件
app.use(express.static('public'));
app.use(express.static('node_modules'));

//数据库连接
var mysql = require('mysql');
var conntoDB = mysql.createConnection({
  host: '127.0.0.1',
  user: 'root',
  password: '12345',
  database: 'test'
});
conntoDB.connect();

// ejs渲染
var ejs = require('ejs');
app.engine('html', ejs.__express)
app.set('view engine', 'html');




// app.engine('html', exphbs({
//   layoutsDir: 'views',
//   // defaultLayout: 'layout',
//   extname: '.html'
// }));
// app.set('view engine', 'html');

// session
app.use(cookieParser())
app.use(session({
  secret: 'dev',
  resave: false,
  saveUninitialized: true,
  cookie: {
    maxAge: 2000 * 1000
  } //30 天免登陆
}));
// view engine setup
app.set('views', path.join(__dirname, 'views'));

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// sql查询
function sqlQuery(sqlstring, db) {
  var sqldata,data;
  var sql = sqlstring;
  sql = "SELECT * FROM test.username_tab";
  //查
  //查
  console.log(xyy);

  // alert("te");
  
  db.query(sql, function (err, result) {
    if (err) {
      console.log('[SELECT ERROR] - ', err.message);
      return;
    }
    data = result;
    sqldata = result;
    console.log(data);
  });
  return data;
}





//ws模块
var ws = require('ws'); // 加载ws模块;
var ip_addr = "127.0.0.1";
var wsServer = new ws.Server({
  host: ip_addr,
  port: 8082,
});
console.log('WebSocket sever is listening at port localhost:8181');
wsServer.on("connection", on_server_client_comming);

function on_server_client_comming(wsObj) {
  console.log("request comming");
  
  websocket_add_listener(wsObj);
  // wsObj.send("test_s/end");
}
//ws发送数据给client
function sendtoc(wsObj) {
  console.log("sss");
  var nowDate = new Date().getTime();
  // chart(num);
  console.log("发送")
  // ws.send("sdsd")
  // wsServer.on("connection", function on_server_client_comming(wsObj) {
  //   console.log("sdss", sqldata)
  var send_data = sqlQuery("sq",conntoDB);
  console.log((send_data))
  // var decc = new TextEncoder()
  wsObj.send((String(send_data)));
  // });
  // websocket_add_listener(wsObj);

}
// ws接收各事件处理逻辑
function websocket_add_listener(wsObj) {
  console.log("receive");
  //通信
  wsObj.on("message", function (data) {
    if (data == 'chart') {
      sendtoc(wsObj);
      console.log("chart");
    }
    if (data == 'one') {
      // sendtoc(1);
      console.log("woshicuowu")
      // wsObj.send(JSON.stringify(sqldata));
    }
    if (data == "two") {
      sendtoc(2);
      // wsObj.send(JSON.stringify(sqldata));
    } else {
      // wsObj.send(JSON.stringify(sqldata));
    }
    console.log("request data:" + data);
  });
  // wsObj.send("sss")
  //关闭连接
  wsObj.on("close", function () {
    console.log("request close");
  });
  //错误
  wsObj.on("error", function (err) {
    console.log("request error", err);
  });
}



// 路由
// app.get('/', function(req, res) {
//   // res.send("nih");
//   res.render('index.html');
  
// });
app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/login', loginRouter);
// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});
var xyy = 0;
// var server = app.listen(3000, "127.0.0.1");
module.exports = app;
