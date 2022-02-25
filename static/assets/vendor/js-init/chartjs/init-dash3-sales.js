// chartjs initialization

$(function () {
    "use strict";

    var ctx = document.getElementById('dash3_sales_chart').getContext('2d');

    var myBarChart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
            datasets: [{
                label: "My First dataset",
                data: [40, 90, 210, 160, 230],
                backgroundColor: '#18b9d4',
                borderColor: '#18b9d4',
                pointBorderColor: '#ffffff',
                pointBackgroundColor: '#18b9d4',
                pointBorderWidth: 2,
                pointRadius: 4

            }, {
                label: "My Second dataset",
                data: [160, 140, 20, 270, 110],
                backgroundColor: '#3d74f1',
                borderColor: '#3d74f1',
                pointBorderColor: '#ffffff',
                pointBackgroundColor: '#3d74f1',
                pointBorderWidth: 2,
                pointRadius: 4
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

});
