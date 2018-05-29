$(document).ready(function() {
    
    $(document).on('click', '#ready_btn', function() {
        $('#welcome_hero').stop().animate({left: -3000}, 'slow');
        setTimeout(function() {
            $('.btn__form').addClass('u-shadow');
        },500)
    })

    $(document).on('click', '#close_forms', function() {
        $('.btn__form').removeClass('u-shadow');
        $('#welcome_hero').stop().animate({left: +0 }, 'slow');
    })



})