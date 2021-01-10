// 配置链接数据库参数
module.exports = {
    host:'localhost',//数据库地址
    user:'root',//账户名
    password:'12345',//密码
    port:'3306',//端口
    database:'churuku',//数据库名
    connectTimeout:5000, // 连接超时
    multipleStatements:false // 是否允许一个query中包含多条sql语句
};