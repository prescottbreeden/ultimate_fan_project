$(document).ready(function() {
    console.log('testing-link');
    var c = 0;
    $(document).on('click', '#ready_btn', function() {
        console.log('clicked ready');
        
        $('#welcome_hero').stop().animate({left: -3000}, 'slow');

        setTimeout(function() {
            $('.btn__form').addClass('shadow');
        },500)
    })

    $(document).on('click', '#close_forms', function() {
        console.log('clicked close');
        $('.btn__form').removeClass('shadow');
        $('#welcome_hero').stop().animate({left: +0 }, 'slow');

    })
})