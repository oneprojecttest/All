var express = require('express');
var router = express.Router();
// var path = require('path');
// var app = express();
// var exphbs = require('express-handlebars');
// app.engine('html', exphbs({
//         layoutsDir: './views',
//         defaultLayout: 'layout',
//         extname: '.html'
//     }));
// app.set('view engine', 'html');
// app.set('views', path.join(__dirname, 'views'));
router.get('/', function(req, res) {
    // res.send("nih");
    res.render('index');
    
});
 
router.get('/login', function(req, res) {
    res.render('login');
});
//get main paper
router.get('/main', function(req, res) {
    console.log("mian");    
    res.render('ws');
});
 
module.exports = router;