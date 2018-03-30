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
            options: {
                legend: {
                    labels: {
                        fontColor: 'white'
                        }
                },
                tooltips: {
                    mode: 'label'
                },
                responsive: true,
                scales: {
                    xAxes: [{

                        ticks:{
                            // stepSize : 1,

                         },
                        stacked: true,
                        gridLines: {
                            lineWidth: 0,
                            // color: "rgba(255,255,255,1)"
                        }
                    }],
                    yAxes: [{
                        stacked: true,
                        gridLines: {
                            // color: "rgba(255,255,255,1)"
                        },
                        ticks: {
                            min: 0,
                            // stepSize: 1,
                        }

                    }]
                }
            }
        });
    });
});
