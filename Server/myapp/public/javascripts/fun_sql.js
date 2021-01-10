// var app = require('../app');
// document.write("<script type='text/javascript' src='javascripts/fun_test.js'></script>");
// alert(xyy);
// const express = require('express')
const cors = require('cors');
const db = require('../../db/db');
// 跨域
const bodyParser = require('body-parser'); //解析参数

// const app = express();

// app.use(cors()) //解决跨域
// app.use(bodyParser.json());
// app.use(bodyParser.urlencoded({extended: true}));//允许表单请求

// app.listen(9000,()=>console.log('服务启动'))

//查询
// app.get('/search',async (req,res,next)=>{
//     try{
//         db.query('SELECT * FROM user', [], function(result, fields) {
//             res.json({result})
//         });
//     }catch(error){
//         next(error)//抛错,将错误携带致回调函数,往下传递
//     }

// })
function chart(num) {
    var sqldata, data;
    var sql = 'SELECT * FROM churuku ';
    //查
    //查
    console.log(xyy);

    alert('te');

    db.query(sql, function (err, result) {
        if (err) {
            console.log('[SELECT ERROR] - ', err.message);
            return;
        }
        data = result;
        sqldata = result;
        console.log(data);
    });
}

$(document).ready(function () {
    $('#sql_query').click(function () {
        // $.post('/websocket', function (data, status) {

        console.log('sql');
        chart(1);
        // })
        // if (websocketnum == 0) {
        //     // web();
        //     setInterval(() => {
        //         web();
        //     }, 5000);
        // }
    });
});
