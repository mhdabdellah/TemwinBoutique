
// chartjs initialization

$(function () {
    "use strict";

    // sales_overview_chart

    var ctx = document.getElementById('sales_overview_chart').getContext('2d');

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: ['A', 'B', 'C', 'D', 'E', 'F'],
            datasets: [{
                label: "Sales Overview 1",
                type: 'line',
                data: [8, 15, 4, 30, 8, 5, 18],
                fill: true,
                backgroundColor: 'rgba(50,141,255,.2)',
                borderColor: '#328dff',
                pointBorderColor: '#328dff',
                pointBackgroundColor: '#fff',
                pointBorderWidth: 2,

                borderWidth: 1,
                borderJoinStyle: 'miter',
                //pointHoverRadius: 2,
                pointHoverBackgroundColor: '#328dff',
                pointHoverBorderColor: '#328dff',
                pointHoverBorderWidth: 1,
                pointRadius: 3

            }, {
                label: "Sales Overview 2",
                type: 'line',
                data: [1, 7, 21, 4, 12, 5, 10],
                fill: false,
                borderDash: [5, 5],
                backgroundColor: 'rgba(87,115,238,.3)',
                borderColor: '#5773ee',
                pointBorderColor: '#5773ee',
                pointBackgroundColor: '#5773ee',
                pointBorderWidth: 2,

                borderWidth: 1,
                borderJoinStyle: 'miter',
                pointHoverBackgroundColor: '#5773ee',
                pointHoverBorderColor: '#fff',
                pointHoverBorderWidth: 1,
                pointRadius: 3
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
                    display: true
                }],
                yAxes: [{
                    display: true,
                    gridLines: {
                        zeroLineColor: '#f1f3f5',
                        color: '#f1f3f5',
                        //drawBorder: false
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


