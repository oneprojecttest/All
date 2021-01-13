// var express = require('express');
var express = require('express');
// var path = require('path');
var router = express.Router();
var app = express();

// var exphbs = require('express-handlebars');
//静态资源托管中间件
app.use(express.static('../public'));
router.get('/', function (req, res) {
    console.log('client');
    res.render('client');
});

router.get('/beinang', function (req, res) {
    console.log('beinang');
    res.render('beinang');
});
router.get('/beizi', function (req, res) {
    console.log('beizi');
    // res.send()
    res.render('beizi');
});
router.get('/cart', function (req, res) {
    console.log('cart');
    res.render('cart');
});
router.get('/maojin', function (req, res) {
    console.log('maojin');
    res.render('maojin');
});
router.get('/micaidayi', function (req, res) {
    console.log('micaidayi');
    res.render('micaidayi');
});
router.get('/micaifu', function (req, res) {
    console.log('micaifu');
    res.render('micaifu');
});
router.get('/paoxie', function (req, res) {
    console.log('paoxie');
    res.render('paoxie');
});
router.get('/tinengfu', function (req, res) {
    console.log('tinengfu');
    res.render('tinengfu');
});
router.get('/waiyaodai', function (req, res) {
    console.log('waiyaodai');
    res.render('waiyaodai');
});
router.get('/yuyi', function (req, res) {
    console.log('yuyi');
    res.render('yuyi');
});
router.get('/zhentou', function (req, res) {
    console.log('zhentou');
    res.render('zhentou');
});
router.get('/zuozhanxue', function (req, res) {
    console.log('zuozhanxue');
    res.render('zuozhanxue');
});

module.exports = router;
