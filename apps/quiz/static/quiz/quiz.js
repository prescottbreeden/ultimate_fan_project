$(document).ready(function() {
    
    $(document).on('click', '#ready_btn', function() {
        $('#welcome_hero').stop().animate({left: -3000}, 'slow');
        setTimeout(function() {
            $('.btn__form').addClass('u-shadow');
        },500)
    })

    $('#sign_in_box').click(function() {
        $.ajax({
            type: "GET",
            url: "/logout",
            success: function(res){
                location.reload();
            }
        })
    })

    $(document).on('click', '#close_forms', function() {
        $('.btn__form').removeClass('u-shadow');
        $('#welcome_hero').stop().animate({left: +0 }, 'slow');
    })

    $("#logout").on('click', function() {
        console.log('clicked');
        $.ajax({
            url: "/logout",
          });
    })

})