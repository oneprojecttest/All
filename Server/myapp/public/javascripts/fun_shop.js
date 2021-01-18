$(document).ready(function () {
    $('#rer').click(function () {
        // $.post('/websocket', function (data, status) {
        console.log('web');
        location.href = '/login';
        alert('te');
        
    });
    

    $("#check").click(function(){
        $.post(
            '/check',
            function (data, status) {

                alert(data)

            }
        )
    })
});
