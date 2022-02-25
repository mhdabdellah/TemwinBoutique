
// chartjs initialization

$(function () {
    "use strict";


// doughnut_chart

    var ctx = document.getElementById("doughnut_chart");
    var data = {
        labels: [
            "Reopen", "Declain", "Pending", "Solved "
        ],
        datasets: [{
            data: [40, 10, 10, 40],
            backgroundColor: [
                "#acf5fe",
                "#f79490",
                "#fcdd82",
                "#cae59b"
            ],
            borderWidth: [
                "0px",
                "0px",
                "0px",
                "0px"
            ],
            borderColor: [
                "#acf5fe",
                "#f79490",
                "#fcdd82",
                "#cae59b"
            ]
        }]
    };

    var myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: {
            legend: {
                display: false
            }
        }
    });


});


