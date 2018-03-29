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
        };
    });

});