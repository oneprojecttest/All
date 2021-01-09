if ("WebSocket" in window) {
    // alert("您的浏览器支持 WebSocket!");
}
var wsObj = new WebSocket("ws://127.0.0.1:8082");
var cpu ;
var mem;
wsObj.onmessage = function (ev) { //获取后端响应
    console.log("sssssssssssssssssss");
    // sdata = JSON.parse(ev.data)
    console.log(ev);
    // clearcontent();
    // show(sdata);
    var decc = new TextDecoder("utf-8");
    console.log((JSON.parse(ev.data)));

    // var jslength = 0;
    // for (var js2 in sdata) {
    //     // console.log(sdata)
    //     jslength++;
    // }
    // // console.log("sdsdsd", sdata);

    // //  console.log("sdd",sdata[0])
    // for (var i = 0; i < jslength; i++) {
    //     // console.log(sdata[i])
    //     if (sdata[i].Funname == 'cpu') {
    //         cpu= sdata[i].Val+10;
            
    //     }
    //     if (sdata[i].Funname == 'mempercent') {
    //         mem = sdata[i].Val;
            
    //     }
    // }
    
};

// function getdata() {
//     console.log("ssssssssssssssssssss")
//     wsObj.onopen = function () { //发送请求
//         // alert("open");
//         wsObj.send('chart');
//     };
    
 
//     // };
//     wsObj.onerror = function (ev) {
//         //alert("error");
//     };
// }


// var ctx = document.getElementById('chart').getContext('2d');
// var chart = new Chart(ctx, config);

// setInterval(function() {
//     if (config.data.datasets.length > 0) {
//         wsObj.send("one");
//         var last = parseInt(dataLabels[dataLabels.length - 1]);
//         var label = last + 1;
//         if (last >= 23) {
//             label = 0;
//         }
//         label = label + 's';

//         dataLabels.push(label);
//         dataPV.push(cpu);
//         dataUV.push(mem);

//         dataLabels.shift();
//         dataPV.shift();
//         dataUV.shift();

//         chart.update();
//     }
// }, 300);

// function getRandomNum(min, max) {
//     var range = max - min;
//     var rand = Math.random();
//     return(min + Math.round(rand * range));
// }
function connect(){
    console.log("connect");
    wsObj.onopen = function () { //发送请求
        // alert("open");
        wsObj.send("chart");
    };
}
function connect(){
    console.log("connect");
    // wsObj.onopen = function () { //发送请求
    //     // alert("open");
        wsObj.send("chart");
    // };
}
function close(){
    console.log("close");
    wsObj.onclose = function (ev) { //发送请求
        // alert("open");
        // wsObj.send('chart');
    };
}
$(document).ready(function () {
    $("#open").click(function () {
        // $.post('/websocket', function (data, status) {

            console.log("sql");
            connect();
            // chart(1)
        // })
        // if (websocketnum == 0) {
        //     // web();
        //     setInterval(() => {
        //         web();
        //     }, 5000);
        // }
    })
    $("#close").click(function () {
        // $.post('/websocket', function (data, status) {

            console.log("sql");
            close();
            // chart(1)
        // })
        // if (websocketnum == 0) {
        //     // web();
        //     setInterval(() => {
        //         web();
        //     }, 5000);
        // }
    })
   
})