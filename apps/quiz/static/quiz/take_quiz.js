console.log('Power Overwhelming...')

$(document).ready(function(){

$('button').on('click', function(){
    if ($(this).val() == '1'){
        $('.response_answer').html(
            '<h1 class="correct">CORRECT!!</h1>'
            )
    }
    else {
        $('.response_answer').html(
            '<h1 class="incorrect">Incorrect...</h1>'
            )
    }

    console.log('next question').delay(1000)
})
})