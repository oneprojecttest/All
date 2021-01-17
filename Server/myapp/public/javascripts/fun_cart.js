$(document).ready(function () {
    $('#cartclick').click(function () {
        // alert('123');
        var item = $('#item').html();
        var num = $('#buy-num').val();
        $.post(
            '/shop/item',
            {
                item: item,
                num: num,
            },
            function (data, status) {
                location.href = '../shop/cart';
                // alert('Data: ' + data + '\nStatus: ' + status);
            }
        );
    });
    $('#finish').click(function () {
        // alert('123');
        var item = $('#item').html();
        var num = $('#buy-num').val();
        $.post(
            '/shop/finish',
            {
                item: item,
                num: num,
            },
            function (data, status) {
                location.href = '../shop/cart';
                // alert('Data: ' + data + '\nStatus: ' + status);
            }
        );
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
