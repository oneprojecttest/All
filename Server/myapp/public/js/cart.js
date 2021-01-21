$(function () {
    /**************数量加减***************/
    $('.num .sub').click(function () {
        var num = parseInt($(this).siblings('span').text());
        if (num <= 1) {
            $(this).attr('disabled', 'disabled');
        } else {
            num--;
            $(this).siblings('span').text(num);
            //获取除了货币符号以外的数字

            var price = $(this).parents('.number').prev().text().substring(1);
            //单价和数量相乘并保留两位小数
            $(this)
                .parents('.th')
                .find('.sAll')
                .text('￥' + (num * price).toFixed(2));
            jisuan();
            zg();
        }
        var aid = $(this).parents('.number').parents('.th').attr('id');
        // alert(aid);
        var num = parseInt(-1);
        $.post(
            '../shop/changeitem',
            {
                item: aid,
                num: num,
            },
            function (data, status) {
                // location.href = '../shop/cart';
                console.log('Data: ' + data + '\nStatus: ' + status);
            }
        );
    });
    $('.num .add').click(function () {
        var num = parseInt($(this).siblings('span').text());
        if (num >= 5) {
            confirm('限购5件');
        } else {
            num++;
            $(this).siblings('span').text(num);
            var price = $(this).parents('.number').prev().text().substring(1);
            $(this)
                .parents('.th')
                .find('.sAll')
                .text('￥' + (num * price).toFixed(2));
            jisuan();
            zg();
        }
        var aid = $(this).parents('.number').parents('.th').attr('id');
        // alert(aid);
        var num = parseInt(1);
        $.post(
            '../shop/changeitem',
            {
                item: aid,
                num: num,
            },
            function (data, status) {
                // location.href = '../shop/cart';
                console.log('Data: ' + data + '\nStatus: ' + status);
            }
        );
        // var item = $('#item').html();
        // var num_t = parseInt(-1);
        // $.post(
        //     '/shop/changeitem',
        //     {
        //         item: item,
        //         num: num_t,
        //     },
        //     function (data, status) {

        //         // alert('Data: ' + data + '\nStatus: ' + status);
        //     }
        // );
    });
    //计算总价
    function jisuan() {
        var all = 0;
        var len = $(".th input[type='checkbox']:checked").length;
        if (len == 0) {
            $('#all').text('￥' + parseFloat(0).toFixed(2));
        } else {
            $(".th input[type='checkbox']:checked").each(function () {
                //获取小计里的数值
                var sAll = $(this).parents('.pro').siblings('.sAll').text().substring(1);
                //累加
                all += parseFloat(sAll);
                //赋值
                $('#all').text('￥' + all.toFixed(2));
            });
        }
    }
    //计算总共几件商品
    function zg() {
        var zsl = 0;
        var index = $(".th input[type='checkbox']:checked").parents('.th').find('.num span');
        var len = index.length;
        if (len == 0) {
            $('#sl').text(0);
        } else {
            index.each(function () {
                zsl += parseInt($(this).text());
                $('#sl').text(zsl);
            });
        }
        if ($('#sl').text() > 0) {
            $('.count').css('background', '#c10000');
        } else {
            $('.count').css('background', '#8e8e8e');
        }
    }
    /*****************商品全选***********************/
    $("input[type='checkbox']").on('click', function () {
        var sf = $(this).is(':checked');
        var sc = $(this).hasClass('checkAll');
        if (sf) {
            if (sc) {
                $("input[type='checkbox']").each(function () {
                    this.checked = true;
                });
                zg();
                jisuan();
            } else {
                $(this).checked = true;
                var len = $("input[type='checkbox']:checked").length;
                var len1 = $('input').length - 1;
                if (len == len1) {
                    $("input[type='checkbox']").each(function () {
                        this.checked = true;
                    });
                }
                zg();
                jisuan();
            }
        } else {
            if (sc) {
                $("input[type='checkbox']").each(function () {
                    this.checked = false;
                });
                zg();
                jisuan();
            } else {
                $(this).checked = false;
                var len = $(".th input[type='checkbox']:checked").length;
                var len1 = $('input').length - 1;
                if (len < len1) {
                    $('.checkAll').attr('checked', false);
                }
                zg();
                jisuan();
            }
        }
    });

    //删除购物车商品
    $('.del').click(function () {
        //单个删除
        var aid = $(this).parents('.th').attr('id');
        $('.mask').show();
        $('.tipDel').show();
        index = $(this).parents('.th').index() - 1;
        $('.cer').click(function () {
            $('.mask').hide();
            $('.tipDel').hide();
            $('.th').eq(index).remove();
            $('.cer').off('click');
            if ($('.th').length == 0) {
                $('.table .goOn').show();
            }
            // var num = parseInt(1);
            $.post(
                '../shop/zeroitem',
                {
                    item: aid,
                    // num: num,
                },
                function (data, status) {
                    // location.href = '../shop/cart';
                    console.log('Data: ' + data + '\nStatus: ' + status);
                }
            );
        });
    });
    $('.cancel').click(function () {
        // alert('取消');
        $('.mask').hide();
        $('.tipDel').hide();
    });
    $('.count').click(function () {
        // alert("Finish")
        var index = $(".th input[type='checkbox']:checked").parents('.th').find('.num span');
        var arrayObj = [];
        var arrayNum = [];
        var num = 0;
        var d = {};
        // var arr = [];
        // if (len == 0) {
        //     $('#sl').text(0);
        // } else {
        index.each(function () {
            // zsl += parseInt($(this).text());
            var tempNum = parseInt($(this).text());
            var aid = $(this).parents('.num').parents('.number').parents('.th').attr('id');
            var temp = { id: aid, num: tempNum};
            arrayObj[num] = temp;
            // arrayNum[num] = tempNum;
            num = num + 1;
            //         $('#sl').text(zsl);
        });
        d.getItem = arrayObj;
        // d.getNum = arrayNum;
        if(num == 0) {
            console.log("buneg ")
        }else{
            $.post(
                '../shop/finish',
                {
                    item: JSON.stringify(d),
                    // num: num,
                },
                function (data, status) {
                    // location.href = '../shop/cart';
                    console.log('Data: ' + data + '\nStatus: ' + status);
                    location.href = '../shop/finish';
                    
                }
            );
        }
        
        // }
    });
});
