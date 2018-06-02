
$(document).ready(function(){

	$("#logout").on('click', function() {
        $.ajax({
            url: "/logout",
		  });
		location.reload();
	})

	$.get('/quiz/make_chart', function(data){
	      var myData= data[0]

		var ctx = document.getElementById('myChart').getContext('2d');
		var chart = new Chart(ctx, {
		    // The type of chart we want to create
		    type: 'pie',
		    // The data for our dataset
		    data: myData,
		        // Configuration options go here
	        options: {
		        legend: {
		            labels: {
		                fontColor: "white",
		                fontSize: 14
		            }
		        },
	        }
	    });
	});

	$.get('/quiz/last_quiz', function(data){
	    var myData= data[0]
	    var ctx = document.getElementById('lastTest').getContext('2d');
	    var chart = new Chart(ctx, {
	        // The type of chart we want to create
	        type: 'pie',
	        // The data for our dataset
	        data: myData,
	        // Configuration options go here
	        options: {
		        legend: {
		            labels: {
		                fontColor: "white",
		                fontSize: 14,
		            }
		        }
	        }
	    });
	});


})
