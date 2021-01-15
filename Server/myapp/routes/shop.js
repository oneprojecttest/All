// var express = require('express');
var express = require('express');
// var path = require('path');
var router = express.Router();
var app = express();
const path = require('path');
// const app = express()

router.use(express.static(path.join(__dirname, '../public')));
// app.use(express.static('public'));
// import './public/javascripts/sql_t.js'
var sql_q = require('../public/javascripts/sql_t.js');
// var exphbs = require('express-handlebars');
//静态资源托管中间件
// app.use(express.static('../public'));
router.get('/', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
        console.log('client');
        // res.render('main');
        res.render('client',{ data:1, username: req.session.username });
    // }
});
function getPagetid(name) {
    var id = 0;
    switch (name) {
        case 'beinang':
            id = 1;
            break;
        case 'beizi':
            id = 2;
            break;
        case 'maojin':
            id = 3;
            break;
        case 'yuyi':
            id = 4;
            break;
        case 'waiyaodai':
            id = 5;
            break;
        case 'zuozhanxue':
            id = 6;
            break;
        case 'zhentou':
            id = 7;
            break;
        case 'tinengfu':
            id = 8;
            break;
        case 'paoxie':
            id = 9;
            break;
        case 'micaidayi':
            id = 10;
            break;
        case 'micaifu':
            id = 11;
            break;

        default:
            break;
    }
    return id;
}

function sqlNumItems(req, res, arrayObj, tag, sql, returnPage) {
    sql_q
        .sqlQuery(sql, arrayObj, tag)
        .then(function onFulfilled(data) {
            console.log('qwe');
            if (data != 'NULL') {
                console.log('dddddd', data);
                console.log(data[0].guige);
                var return_num = data[0].guige;
                // console.log(' 用户已经存在');
                // res.render('repeat_username');
                console.log('jump');
                res.render(returnPage, { data: return_num, username: req.session.username });
            } else {
                console.log('背囊查询失败');
                // console.log('dddddd', data);
            }
        })
        .catch(function onRejected(error) {
            console.error(error);
        });
}

function getReturnPage(req, res) {
    console.log(path);
    console.log(__dirname);
    var arrayObj = new Array();
    arrayObj[0] = getPagetid(req.route.path.substr(1));
    var tag = sql_q.Sql_op.select;
    var sql = 'SELECT * FROM test.cailiao where id=?';
    // var a   = 'mes';
    // var id = getPagetid(req.route.path.substr(1));
    // console.log('dsd ', id);

    // console.log('qwe');
    // consolelog(req.route.path);
    // returnPage = req.route.path.substr(1);
    // console.log(returnPage)
    sqlNumItems(req, res, arrayObj, tag, sql, req.route.path.substr(1));
}

router.get('/beinang', function (req, res) {
    // console.log('beinang');
    // var t = sql_q.test();
    // t;
    // var sql = 'SELECT * FROM test.cailiao where id=?';
    // var arrayObj = new Array();
    // arrayObj[0] = 1;
    // // var a   = 'mes';
    // var tag = sql_q.Sql_op.select;
    // console.log('qwe');

    // sql_q
    //     .sqlQuery(sql, arrayObj, tag)
    //     .then(function onFulfilled(data) {
    //         console.log('qwe');
    //         if (data != 'NULL') {
    //             console.log('dddddd', data);
    //             console.log(data[0].guige);
    //             var return_num = data[0].guige;
    //             // console.log(' 用户已经存在');
    //             // res.render('repeat_username');
    //             console.log('jump');
    //             res.render('beinang', { data: return_num });
    //         } else {
    //             console.log('背囊查询失败');
    //             // console.log('dddddd', data);
    //         }
    //     })
    //     .catch(function onRejected(error) {
    //         console.error(error);
    //     });
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/beizi', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/cart', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/maojin', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/micaidayi', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/micaifu', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/paoxie', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/tinengfu', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/waiyaodai', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/yuyi', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/zhentou', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});
router.get('/zuozhanxue', function (req, res) {
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        console.log(req.route.path.substr(1));
        getReturnPage(req, res);
    }
});

module.exports = router;
