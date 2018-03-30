console.log('Power Overwhelming...')

$(document).ready(function(){

    setTimeout(function() {
        $("button[value='0']").trigger('click')
        }, 15000);

    $('button').on('click', function(){
        if ($(this).val() == '1'){
            $('.response_answer').html(
                '<h1 class="correct">CORRECT!!</h1>'
                );
            $('#quiz').addClass('slide_off');
        }
        else {
            $('.response_answer').html(
                '<h1 class="incorrect">Incorrect...</h1>'
                );
            $('#quiz').addClass('slide_off');

            // flash correct answer
            $("p.div_value1").addClass('right_answer');
            setTimeout(function() {
                $("p.div_value1").removeClass('right_answer')
                }, 250);
            setTimeout(function() {
                $("p.div_value1").addClass('right_answer')
                }, 500);
            setTimeout(function() {
                $("p.div_value1").removeClass('right_answer')
                }, 750);
        };
    });

});