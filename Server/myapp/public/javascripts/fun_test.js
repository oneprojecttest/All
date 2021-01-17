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
    $('#shop').click(function () {
        // $.post('/websocket', function (data, status) {
        // $('#jump').on('click', function() {
        // alert("te");     q

        location.href = '/shop';
        // })
        // })
        // if (websocketnum == 0) {
        //     // web();
        //     setInterval(() => {
        //         web();
        //     }, 5000);
        // }
    });
    $('#shp').click(function () {
        // $.post('/websocket', function (data, status) {
        // $('#jump').on('click', function() {
        alert("te");  

        location.href = '/shp';
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

    $('.sen1').click(function () {
        var data = 'sss';
        $.post(
            '/send',
            {
                // name:$(".sen").val(),
                city: 'Duckburg',
            },
            function (data, status) {
                // alert(data)
            }
        );
    });
    $('#gett').click(function () {
        $.ajax({
            url: '/gett',
            type: 'GET',
            async: true,
            dataType: 'json',
            data: {
                name: '前台数据',
                age: 12,
            },
            success: function (result) {
                alert(123);
                $('#mydiv').html(result.name);
            },
            error: function (xhr) {
                alert('错误提示： ' + xhr.status + ' ' + xhr.statusText);
            },
        });
    });
});
