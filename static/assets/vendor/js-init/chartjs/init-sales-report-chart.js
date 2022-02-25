
// chartjs initialization

$(function () {
    "use strict";

    // sales_report_chart

    var ctx = document.getElementById('sales_report_chart').getContext('2d');

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
            datasets: [{
                label: "Sales Overview 1",
                type: 'line',
                data: [50, 20, 55, 10, 70, 10, 40, 10],
                fill: true,
                backgroundColor: 'rgba(122,134,255,.1)',
                borderColor: '#7a86ff',
                pointBorderColor: '#7a86ff',
                pointBackgroundColor: '#7a86ff',
                pointBorderWidth: 2,
                borderWidth: 1,
                borderJoinStyle: 'miter',
                pointHoverBackgroundColor: '#7a86ff',
                pointHoverBorderColor: '#fff',
                pointHoverBorderWidth: 1,
                pointRadius: 2

            }, {
                label: "Sales Overview 2",
                type: 'line',
                data: [15, 28, 140, 40, 0, 40, 0, 40],
                fill: true,
                //borderDash: [5, 5],
                backgroundColor: 'rgba(96,197,146,.1)',
                borderColor: '#60c592',
                pointBorderColor: '#60c592',
                pointBackgroundColor: '#60c592',
                pointBorderWidth: 2,
                borderWidth: 1,
                borderJoinStyle: 'miter',
                pointHoverBackgroundColor: '#60c592',
                pointHoverBorderColor: '#fff',
                pointHoverBorderWidth: 1,
                pointRadius: 2
            }]
        },

        // Configuration options go here
        options: {
            maintainAspectRatio: false,
            legend: {
                display: false
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
                    //tension: 0.00001,
                    tension: 0.4,
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


});


