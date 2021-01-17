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
    if (req.session.username == undefined) {
        console.log('未登录');
        res.render('login');
    } else {
        // console.log(req.body);
        var sql = 'SELECT * FROM churuku.cart where username=?';
        var arrayObj = new Array();
        var name = req.session.username;
        arrayObj[0] = name;
        var tag = sql_q.Sql_op.select;
        sql_q
            .sqlQuery(sql, arrayObj, tag)
            .then(function onFulfilled(data) {
                console.log('qwe', data);
                var cartnum = 0;
                if (data != 'NULL') {
                    var num_i = 0;
                    for (var p in data) {
                        for (var key in data[p]) {
                            if (num_i == 0) {
                                console.log(0);
                            } else {
                                cartnum = cartnum + data[p][key];
                            }
                            num_i++;
                        }
                    }
                    console.log('client');
                    // res.render('main');
                    console.log('cartnum', cartnum);
                    res.render('client', {
                        data: 1,
                        username: req.session.username,
                        allnum: cartnum,
                    });
                } else {
                    console.log('背囊查询失败');
                    // console.log('dddddd', data);
                }
            })
            .catch(function onRejected(error) {
                console.error(error);
            });
    }
});
router.post('/login', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log('client');
    // res.render('main');
    res.render('client', { data: 1, username: req.session.username });
    // }
});
function getNum(username) {
    return new Promise((resolve, reject) => {
        var sql = 'SELECT * FROM churuku.cart where username =?';
        var arrayObj = new Array();
        // console.log(id);
        var tag = sql_q.Sql_op.select;
        var arr = [];
        console.log('sdd', username);
        // for (var i = 0; i < 12; i++) {
        arrayObj[0] = username;
        sql_q
            .sqlQuery(sql, arrayObj, tag)
            .then(function onFulfilled(data) {
                console.log('qwe');
                if (data != 'NULL') {
                    // console.log('getnum', data);
                    // arr.push(data[0])
                    // if(i==11)
                    resolve(data);
                } else {
                    console.log('/cart num查询失败');
                    // console.log('dddddd', data);
                }
            })
            .catch(function onRejected(error) {
                console.error(error);
            });
        // console.log(res);
        // }
    });
}
function getPagetid(name) {
    var id = 0;
    switch (name) {
        case 'beinang':
            id = 1;
            break;
        case 'beizi':
            id = 4;
            break;
        case 'maojin':
            id = 5;
            break;
        case 'yuyi':
            id = 12;
            break;
        case 'waiyaodai':
            id = 9;
            break;
        case 'zuozhanxue':
            id = 11;
            break;
        case 'zhentou':
            id = 10;
            break;
        case 'tinengfu':
            id = 8;
            break;
        case 'paoxie':
            id = 3;
            break;
        case 'micaidayi':
            id = 6;
            break;
        case 'micaifu':
            id = 2;
            break;
        case 'shoutao':
            id = 7;
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
                console.log(data[0].shuliang);
                var return_num = data[0].shuliang;
                // console.log(' 用户已经存在');
                // res.render('repeat_username');
                console.log('jump');
                var item = req.route.path.substr(1);
                console.log('dsd', item);
                res.render(returnPage, {
                    data: return_num,
                    username: req.session.username,
                    item: item,
                });
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
    console.log(req.route.path.substr(1));
    arrayObj[0] = getPagetid(req.route.path.substr(1));
    var tag = sql_q.Sql_op.select;
    var sql = 'SELECT * FROM churuku.kucun where cailiao_id=?';
    // var a   = 'mes';
    // var id = getPagetid(req.route.path.substr(1));
    // console.log('dsd ', id);

    // console.log('qwe');
    // consolelog(req.route.path);
    // returnPage = req.route.path.substr(1);
    // console.log(returnPage)
    sqlNumItems(req, res, arrayObj, tag, sql, req.route.path.substr(1));
}
router.post('/item', function (req, res) {
    console.log("weewr");
    var sql = 'SELECT * FROM churuku.cart where username=?';
    var arrayObj = new Array();
    var name = req.session.username;
    // if (name == undefined) {
    //     name = '123';
    //     console.log(sdsdsd);
    // }
    arrayObj[0] = name;
    var tag = sql_q.Sql_op.select;
    sql_q
        .sqlQuery(sql, arrayObj, tag)
        .then(function onFulfilled(data) {
            // console.log('qwe');
            var arrayItem = new Array();
            if (data != 'NULL') {
                var num_i = 0;
                var t = req.body.item;
                var num = req.body.num;
                for (var p in data) {
                    console.log('ss', data[p]);
                    for (var key in data[p]) {
                        if (num_i == 0) {
                            console.log(0);
                        }
                        if (key == t) {
                            arrayItem[num_i - 1] = data[p][key] + parseInt(num);
                            num_i++;
                        } else {
                            arrayItem[num_i - 1] = data[p][key];
                            num_i++;
                        }
                    }
                }
                arrayItem[num_i - 1] = name;
                for (var i = 0; i < arrayItem.length; i++) {
                    console.log(i, arrayItem[i]);
                }

                tag = sql_q.Sql_op.update;
                var esql =
                    'update churuku.cart  set beinang = ?, micaifu = ?, paoxie = ?, beizi = ?,maojin = ?,micaidayi = ? ,shoutao = ?,tinengfu = ?,waiyaodai = ?,zhentou = ?,zuozhanxue = ?,yuyi = ? where  username = ?';
                sql_q
                    .sqlQuery(esql, arrayItem, tag)
                    .then(function onFulfilled(data) {
                        // console.log('qwe');
                        res.send("ok");
                        if (data != 'NULL') {
                            console.log(data);
                        } else {
                            console.log('背囊查询失败');
                            // console.log('dddddd', data);
                        }
                    })
                    .catch(function onRejected(error) {
                        console.error(error);
                    });
            } else {
                console.log('背囊查询失败');
                // console.log('dddddd', data);
            }
        })
        .catch(function onRejected(error) {
            console.error(error);
        });
    console.log('qwe');
    console.log('qwe');
    
});
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
    //             console.log(data[0].shuliang);
    //             var return_num = data[0].shuliang;
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
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
router.get('/beizi', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
// router.get('/cart', function (req, res) {
//     // if (req.session.username == undefined) {
//     //     console.log('未登录');
//     //     res.render('login');
//     // } else {
//         console.log(req.route.path.substr(1));
//         getReturnPage(req, res);
//     // }
// });
router.get('/maojin', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
router.get('/micaidayi', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
router.get('/micaifu', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
router.get('/paoxie', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
router.get('/tinengfu', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
router.get('/waiyaodai', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
router.get('/yuyi', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
router.get('/zhentou', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});
router.get('/zuozhanxue', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});

router.get('/shoutao', function (req, res) {
    // if (req.session.username == undefined) {
    //     console.log('未登录');
    //     res.render('login');
    // } else {
    console.log(req.route.path.substr(1));
    getReturnPage(req, res);
    // }
});

router.get('/cart', function (req, res) {
    // if (req.session.username == undefined) {
    // console.log('cart');

    // console.log('cart');
    // console.log('cart');

    var d = {};
    var arr = [];

    // for (var i = 0; i < 12; i++) {
    // nums[i]=getNum(i+1);
    // var arr
    if (req.session.username == undefined) {
        console.log('cart未登录');
        res.render('login');
    } else {
        // res.render('admin', { data: 1, username: 'qwre' });

        getNum(req.session.username)
            .then(function onFulfilled(data) {
                console.log('ddddd', data[0].beinang);
                var size = data.length;
                for (var i = 0; i < 12; i++) {
                    var temp = { id: i + 1, name: 'NULL', num: 0 };
                    arr[i] = temp;
                }
                var id_num = 0;
                var temp = {
                    id: id_num + 1,
                    name: 'beinang',
                    num: data[0].beinang,
                    price: parseFloat(data[0].beinang * 17.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'micaifu',
                    num: data[0].micaifu,
                    price: parseFloat(data[0].micaifu * 25.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'paoxie',
                    num: data[0].paoxie,
                    price: parseFloat(data[0].paoxie * 22.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'beizi',
                    num: data[0].beizi,
                    price: parseFloat(data[0].beizi * 18.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'maojin',
                    num: data[0].maojin,
                    price: parseFloat(data[0].maojin * 9.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'micaidayi',
                    num: data[0].micaidayi,
                    price: parseFloat(data[0].micaidayi * 30.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'shoutao',
                    num: data[0].shoutao,
                    price: parseFloat(data[0].shoutao * 17.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;
                temp = {
                    id: id_num + 1,
                    name: 'tinengfu',
                    num: data[0].tinengfu,
                    price: parseFloat(data[0].tinengfu * 17.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'waiyaodai',
                    num: data[0].waiyaodai,
                    price: parseFloat(data[0].waiyaodai * 15.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'zhentou',
                    num: data[0].zhentou,
                    price: parseFloat(data[0].zhentou * 23.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'zuozhanxue',
                    num: data[0].zuozhanxue,
                    price: parseFloat(data[0].zuozhanxue * 22.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                temp = {
                    id: id_num + 1,
                    name: 'yuyi',
                    num: data[0].yuyi,
                    price: parseFloat(data[0].yuyi * 20.9).toFixed(2),
                };
                arr[id_num] = temp;
                id_num = id_num + 1;

                d.result = arr;
                console.log('arr', arr);
                var numAll = 0;
                var PriceAll = 0.0;
                for (var i = 0; i < 12; i++) {
                    // var temp = { id: 1, name: 2, num: 3 };
                    //
                    // console.log(data.length);
                    for (var j = 0; j < size; j++) {
                        numAll += d.result[i].num;
                        PriceAll += parseFloat(d.result[i].price);
                        console.log('ds', PriceAll);
                    }
                }

                d.numAll = numAll;
                d.priceAll = PriceAll.toFixed(2);
                d.username = req.session.username;
                console.log(d.result);
                // var nums = new Array(12);
                res.render('cart', { data: d });
            })
            .catch(function onRejected(error) {
                console.error(error);
            });
        // }
    }

    // }
});



router.post('/changeitem', function (req, res) {
    console.log('change', req.body);
    var sql = 'SELECT * FROM churuku.cart where username=?';
    var arrayObj = new Array();
    var name = req.session.username;
    // if (name == undefined) {
    //     name = '123';
    //     console.log(sdsdsd);
    // }
    arrayObj[0] = name;
    var tag = sql_q.Sql_op.select;
    sql_q
        .sqlQuery(sql, arrayObj, tag)
        .then(function onFulfilled(data) {
            // console.log('qwe');
            var arrayItem = new Array();
            if (data != 'NULL') {
                var num_i = 0;
                var t = req.body.item;

                var num = req.body.num;
                for (var p in data) {
                    console.log('ss', data[p]);
                    for (var key in data[p]) {
                        if (num_i == 0) {
                            console.log(0);
                        }
                        if (num_i == t) {
                            arrayItem[num_i - 1] = data[p][key] + parseInt(num);
                            num_i++;
                        } else {
                            arrayItem[num_i - 1] = data[p][key];
                            num_i++;
                        }
                    }
                }
                arrayItem[num_i - 1] = name;
                for (var i = 0; i < arrayItem.length; i++) {
                    console.log(i, arrayItem[i]);
                }

                tag = sql_q.Sql_op.update;
                var esql =
                    'update churuku.cart  set beinang = ?, micaifu = ?, paoxie = ?, beizi = ?,maojin = ?,micaidayi = ? ,shoutao = ?,tinengfu = ?,waiyaodai = ?,zhentou = ?,zuozhanxue = ?,yuyi = ? where  username = ?';
                sql_q
                    .sqlQuery(esql, arrayItem, tag)
                    .then(function onFulfilled(data) {
                        // console.log('qwe');
                        if (data != 'NULL') {
                            console.log(data);
                        } else {
                            console.log('背囊查询失败');
                            // console.log('dddddd', data);
                        }
                    })
                    .catch(function onRejected(error) {
                        console.error(error);
                    });
            } else {
                console.log('背囊查询失败');
                // console.log('dddddd', data);
            }
        })
        .catch(function onRejected(error) {
            console.error(error);
        });
    console.log('qwe');
    console.log('qwe');
    res.send('dsds');
});
router.post('/zeroitem', function (req, res) {
    console.log('change', req.body);
    var sql = 'SELECT * FROM churuku.cart where username=?';
    var arrayObj = new Array();
    var name = req.session.username;
    // if (name == undefined) {
    //     name = '123';
    //     console.log(sdsdsd);
    // }
    arrayObj[0] = name;
    var tag = sql_q.Sql_op.select;
    sql_q
        .sqlQuery(sql, arrayObj, tag)
        .then(function onFulfilled(data) {
            // console.log('qwe');
            var arrayItem = new Array();
            if (data != 'NULL') {
                var num_i = 0;
                var t = req.body.item;

                var num = req.body.num;
                for (var p in data) {
                    console.log('ss', data[p]);
                    for (var key in data[p]) {
                        if (num_i == 0) {
                            console.log(0);
                        }
                        if (num_i == t) {
                            arrayItem[num_i - 1] = parseInt(0);
                            num_i++;
                        } else {
                            arrayItem[num_i - 1] = data[p][key];
                            num_i++;
                        }
                    }
                }
                arrayItem[num_i - 1] = name;
                for (var i = 0; i < arrayItem.length; i++) {
                    console.log(i, arrayItem[i]);
                }

                tag = sql_q.Sql_op.update;
                var esql =
                    'update churuku.cart  set beinang = ?, micaifu = ?, paoxie = ?, beizi = ?,maojin = ?,micaidayi = ? ,shoutao = ?,tinengfu = ?,waiyaodai = ?,zhentou = ?,zuozhanxue = ?,yuyi = ? where  username = ?';
                sql_q
                    .sqlQuery(esql, arrayItem, tag)
                    .then(function onFulfilled(data) {
                        // console.log('qwe');
                        if (data != 'NULL') {
                            console.log(data);
                        } else {
                            console.log('背囊查询失败');
                            // console.log('dddddd', data);
                        }
                    })
                    .catch(function onRejected(error) {
                        console.error(error);
                    });
            } else {
                console.log('背囊查询失败');
                // console.log('dddddd', data);
            }
        })
        .catch(function onRejected(error) {
            console.error(error);
        });
    console.log('qwe');
    console.log('qwe');
    res.send('dsds');
});
router.post('/finish', function (req, res) {
    console.log('finish');
    // var t = req.body;
    var getItem = JSON.parse(req.body.item).getItem;
    // var getNum = JSON.parse(req.body.item).getItem;
    //
    for (var i in getItem) {
        console.log('sdd', getItem[i].num);
        var arrayItem = new Array();
        arrayItem[0] = getItem[i].num;
        arrayItem[1] = getItem[i].id;
        console.log('sdd', getItem[i].num);
        console.log('qwe');
        var sql = 'update kucun set shuliang = shuliang - ? where cailiao_id = ?';
        var tag = sql_q.Sql_op.update;
        console.log('qwe');
        sql_q
            .sqlQuery(sql, arrayItem, tag)
            .then(function onFulfilled(data) {
                if (data != 'NULL') {
                    console.log(data);
                } else {
                    console.log('背囊查询失败');
                    // console.log('dddddd', data);
                }
            })
            .catch(function onRejected(error) {
                console.error(error);
            });
        var arrayCart = new Array();

        for (var j = 0; j < 12; j++) {
            if (j + 1 == getItem[i].id) {
                arrayCart[j] = getItem[i].num;
            } else {
                arrayCart[j] = 0;
            }
        }
        arrayCart[12] = req.session.username;
        var sqlCart =
            'update cart set beinang = beinang - ? , micaifu = micaifu - ? , paoxie = paoxie - ? , beizi = beizi - ? , maojin = maojin - ? , micaidayi = micaidayi - ? , shoutao = shoutao - ? , tinengfu = tinengfu - ? , waiyaodai = waiyaodai - ? , zhentou = zhentou - ? , zuozhanxue = zuozhanxue - ? , yuyi = yuyi - ? where username = ?';
        var tag = sql_q.Sql_op.update;
        sql_q
            .sqlQuery(sqlCart, arrayCart, tag)
            .then(function onFulfilled(data) {
                // console.log('qwe');
                if (data != 'NULL') {
                    console.log(data);
                } else {
                    console.log('背囊查询失败');
                    // console.log('dddddd', data);
                }
            })
            .catch(function onRejected(error) {
                console.error(error);
            });
    }
    res.send("ok")
});
router.get('/finish', function (req, res) {
    console.log('get finish');
    res.render('finish');
});
module.exports = router;
