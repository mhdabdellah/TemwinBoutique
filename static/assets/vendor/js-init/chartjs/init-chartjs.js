
// chartjs initialization

$(function () {
    "use strict";

    var ctx = document.getElementById('bar-chart-js').getContext('2d');

    var myBarChart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
            datasets: [{
                label: "My First dataset",
                data: [40, 90, 210, 160, 230],
                backgroundColor: '#3dba6f',
                borderColor: '#3dba6f',
                pointBorderColor: '#ffffff',
                pointBackgroundColor: '#3dba6f',
                pointBorderWidth: 2,
                pointRadius: 4

            }, {
                label: "My Second dataset",
                data: [160, 140, 20, 270, 110],
                backgroundColor: '#57b9d8',
                borderColor: '#57b9d8',
                pointBorderColor: '#ffffff',
                pointBackgroundColor: '#57b9d8',
                pointBorderWidth: 2,
                pointRadius: 4
            }]
        },

        // Configuration options go here
        options: {
            maintainAspectRatio: false,
            legend: {
                display: true
            },

            scales: {
                xAxes: [{
                    display: true,
                    gridLines: {
                        zeroLineColor: '#e7ecf0',
                        color: '#e7ecf0',
                        borderDash: [5,5,5],
                        zeroLineBorderDash: [5,5,5],
                        drawBorder: false
                    }
                }],
                yAxes: [{
                    display: true,
                    gridLines: {
                        zeroLineColor: '#e7ecf0',
                        color: '#e7ecf0',
                        borderDash: [5,5,5],
                        zeroLineBorderDash: [5,5,5],
                        drawBorder: false
                    }
                }]

            },
            elements: {
                line: {
                    tension: 0.00001,
//              tension: 0.4,
                    borderWidth: 1
                },
                point: {
                    radius: 2,
                    hitRadius: 10,
                    hoverRadius: 6,
                    borderWidth: 4
                }
            }
        }
    });


    // doughnut_chart

    var ctx = document.getElementById("doughnut-chart-example");
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
                display: true
            }
        }
    });

});


