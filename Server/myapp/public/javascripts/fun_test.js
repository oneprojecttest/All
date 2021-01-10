var xyy = 99;
$(document).ready(function () {
    $('#rer').click(function () {
        // $.post('/websocket', function (data, status) {
        console.log('web');
        location.href = '/login';
        alert('te');
        // })
        // if (websocketnum == 0) {
        //     // web();
        //     setInterval(() => {
        //         web();
        //     }, 5000);
        // }
    });
    $('#jump').click(function () {
        // $.post('/websocket', function (data, status) {
        // $('#jump').on('click', function() {
        // alert("te");     q
        location.href = '/main';
        // })
        // })
        // if (websocketnum == 0) {
        //     // web();
        //     setInterval(() => {
        //         web();
        //     }, 5000);
        // }
    });
    $('#deluser').click(function () {
        $.post('/deluser', function (data, status) {
            console.log('sss');
            // alert(data);
        });
    });
    $('#update').click(function () {
        $.post('/update', function (data, status) {
            console.log('sss');
            // alert(data);
        });
    });
    $('#xin').click(function () {
        $.post('/xin', function (data, status) {
            console.log('sss');
            // alert(data);
        });
    });

    // $("#check").click(function(){
    //     $.post(
    //         '/check',
    //         function (data, status) {

    //             alert(data)

    //         }
    //     )
    // })
});
