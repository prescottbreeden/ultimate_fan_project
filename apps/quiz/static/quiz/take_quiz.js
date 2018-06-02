console.log('Power Overwhelming...')

$(document).ready(function(){

    timer = setTimeout(function() {
        $("button[value='0']").trigger('click')
            console.log('timer ran out');
        }, 15000);

    $('button').on('click', function(){
        clearTimeout(timer);
        if ($(this).val() == '1'){
            $('.question__result').html(
                '<h1 class="question__result--correct">CORRECT!!</h1>'
                );
            $('#quiz').addClass('slide_off');
        }
        else {
            $('.question__result').html(
                '<h1 class="question__result--incorrect">Incorrect...</h1>'
                );
            $('#quiz').addClass('slide_off');
            
            // flash correct answer
            $(".div_value1").parent().addClass('right_answer');
            setTimeout(function() {
                $(".div_value1").parent().removeClass('right_answer')
                }, 250);
            setTimeout(function() {
                $(".div_value1").parent().addClass('right_answer')
                }, 500);
            setTimeout(function() {
                $(".div_value1").parent().removeClass('right_answer')
                }, 750);
        };
    });

    $("#logout").on('click', function() {
        clearTimeout(timer);
        $.ajax({
            url: "/logout",
          });
    })

});