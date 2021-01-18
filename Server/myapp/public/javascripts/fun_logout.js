var xyy = 99;


$(document).ready(function () {
   
    
    $('.logout').click(function () {
        // $('#cartclick').click(function () {
            // alert('123');
            $.post(
                '/shop/logout',
               
                function (data, status) {
                    location.href = 'login';
                    // alert('Data: ' + data + '\nStatus: ' + status);
                }
            );
        });
    // });
   
});
