$(document).ready(function(){
    $.get( '/bar_data', function(data){
        console.log(data)
        var myData= data
        var ctx = document.getElementById('bar_data').getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'horizontalBar',
            // The data for our dataset
            data: myData,
            // Configuration options go here
            options: {}
        });
    });
})