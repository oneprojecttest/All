var mysql = require('mysql');
var pool = mysql.createPool({
    host: '127.0.0.1',
    user: 'root',
    password: '12345',
    database: 'test',
});
function test(){
    console.log("sssssss");
}
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
        if (tag == Sql_op.insert) {
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
        if (tag == Sql_op.select) {
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



module.exports ={ test , sqlQuery, Sql_op }