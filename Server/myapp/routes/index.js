var express = require('express');
var crypto = require('crypto');
var createError = require('http-errors');
var shopRouter = require('./shop');
var express = require('express');
var path = require('path');
var router = express.Router();
var mysql = require('mysql');
var app = express();
// router.use(express.static(path.join(__dirname, '../public')))
var pool = mysql.createPool({
    host: '127.0.0.1',
    user: 'root',
    password: '12345',
    database: 'test',
});
var Sql_op = {
    insert: 1,

    select: 2,

    delete: 3,

    other_op: 4,
};
// conntoDB.connect();
function sqlQuery(sqlstring, para, tag) {
    return new Promise((resolve, reject) => {
        console.log(tag);
        if (tag == 1) {
            pool.getConnection(function (err, connection) {
                connection.query(sqlstring, para, function (err, result) {
                    console.log('insert');
                    connection.release();
                    if (err) {
                        console.log('[INSERT ERROR] - ', err.message);
                        reject(err);
                    }
                    // if (result.length) {
                    //如果查到了数据
                    console.log('INSERT ID:', result);
                    data = result;
                    // data = result;
                    // console.log('------------start----------------');
                    // var string = JSON.stringify(result);
                    // var json = JSON.parse(string)[0];
                    // console.log(json.username);
                    // // if (json.UserPass == password) {
                    // //     console.log('密码校验正确');
                    // // } else {
                    // //                     console.log('密码校验错误');
                    // // }
                    // console.log('--------------end-----------------');
                    // } else {
                    //     data = 'NULL';
                    //     console.log('账号不存在');
                    // }
                    resolve(data);
                });
            });
        }
        if (tag == 2) {
            pool.getConnection(function (err, connection) {
                connection.query(sqlstring, para, function (err, result) {
                    console.log('selcet');
                    connection.release();
                    if (err) {
                        console.log('[SELECT ERROR] - ', err.message);
                        reject(err);
                    }
                    if (result.length) {
                        //如果查到了数据
                        data = result;
                        console.log('------------start----------------');
                        var string = JSON.stringify(result);
                        var json = JSON.parse(string)[0];
                        console.log(json.username);
                        // if (json.UserPass == password) {
                        //     console.log('密码校验正确');
                        // } else {
                        //                     console.log('密码校验错误');
                        // }
                        console.log('--------------end-----------------');
                    } else {
                        data = 'NULL';
                        console.log('账号不存在');
                    }
                    resolve(data);
                });
            });
        }
    });
    // }
}

router.get('/', function (req, res) {
    // // res.send("nih");
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
        res.render('index');
    // }
});
// router.get('/admin', function (req, res) {
//     // // res.send("nih");
//     // if (req.session.username == undefined) {
//         console.log('admin未登录');
//     //     res.render('login');
//     // } else {
//         res.render('admin',{ data: 1, username: "qwre" });
//     // }
// });

router.get('/login', function (req, res) {
    console.log(__dirname)
    res.render('login');
});
//get main paper
router.get('/main', function (req, res) {
    console.log('mian');
    res.render('ws');
});
router.get('/one', function (req, res) {
    console.log('one');
    res.render('page1');
});
router.get('/two', function (req, res) {
    console.log('two');
    res.render('page2');
});
router.post('/main', function (req, res) {
    console.log('mian');
    res.render('ws');
});
//  register post

async function deal_post_register(req, res) {}

router.post('/register', function (req, res) {
    // console.log(data);
    // deal_post_register(req,res);
    console.log('xyyq');

    var username = req.body.username;
    var pwd = req.body.password;
    var pwd2 = req.body.password2;
    var sql = 'SELECT * FROM test.username_tab where username=? and password=?';
    console.log(sql);
    var arrayObj = new Array();
    arrayObj[0] = username;
    arrayObj[1] = crypto.createHash('md5').update(pwd).digest('hex');
    // console.log(sql);
    console.log(username);
    var data;
    var tag = Sql_op.select;
    sqlQuery(sql, arrayObj, tag)
        .then(function onFulfilled(data) {
            if (data != 'NULL') {
                console.log(' 用户已经存在');
                res.render('repeat_username');
            } else if (pwd != pwd2) {
                //两次密码输入不一样
                console.log('error');
                res.render('register_error');
            } else {
                console.log('注册信息');
                sql = 'insert into test.username_tab (username,password) values (?,?)';
                tag = Sql_op.insert;
                sqlQuery(sql, arrayObj, tag)
                    .then(function onFulfilled(data) {
                        console.log(data);
                    })
                    .catch(function onRejected(error) {
                        console.error(error);
                    });

                res.render('login');
            }
            console.log('dddddd', data);
        })
        .catch(function onRejected(error) {
            console.error(error);
        });

    // db.close();
});

//表单提交，注册信息
router.post('/login', function (req, res) {
    console.log(__dirname)
    var username = req.body.username;
    var pwd = req.body.password;
    var sql = 'SELECT * FROM test.username_tab where username=?';
    // console.log(sql);
    var arrayObj = new Array();
    arrayObj[0] = username;
    // arrayObj[1] = pwd;
    var tag = Sql_op.select;
    sqlQuery(sql, arrayObj, tag)
        .then(function onFulfilled(data) {
            if (data == 'NULL') {
                //用户不存在
                res.render('/no_username');
            } else {
                //判断密码
                sql = 'SELECT * FROM test.username_tab where username=? and password=?';
                // console.log(sql);
                // var arrayObj = new Array();
                arrayObj[0] = username;
                arrayObj[1] = crypto.createHash('md5').update(pwd).digest('hex');
                tag = Sql_op.select;
                sqlQuery(sql, arrayObj, tag)
                    .then(function onFulfilled(data) {
                        if (data != 'NULL') {
                            console.log('to main');
                            req.session.username = username;
                            // req.session.usergrade = result[0].usergrade;
                            res.render('main');
                        } else {
                            res.render('password_error');
                            console.log('password error!  登录');
                        }
                    })
                    .catch(function onRejected(error) {
                        console.error(error);
                    });
            }
        })
        .catch(function onRejected(error) {
            console.error(error);
        });
});

//跳转到购物界面
router.use('/shop', shopRouter);

router.get('/shp', function (req, res) {
    console.log('shp');
    res.render('main');
});
//get main paper
router.get('/register2', function (req, res) {
    console.log('register2');
    res.render('register2');
});
router.post('/send', function (req, res) {
    console.log(req.body.name);
    console.log(req.body.city);
    console.log(req.body);
    // res.send("dsds")
});
router.get('/gett', function (req, res) {
    // console.log(req.body.name);
    console.log('qwe');
    console.log(req.getParameter('name'));
    console.log('qwe');
    res.send('dsds');
});
// conntoDB.connect();
module.exports = router;
