
// chartjs initialization

$(function () {
    "use strict";

// area_chart

    var ctx = document.getElementById('area_chart').getContext('2d');

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
            datasets: [{
                label: "My First dataset",
                backgroundColor: 'rgba(42,192,33,.05)',
                borderColor: '#2ac021',
                pointBackgroundColor: "#ffffff",
                data: [120, 90, 220, 180, 300]
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
                    display: false
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
                    radius: 4,
                    hitRadius: 10,
                    hoverRadius: 6,
                    borderWidth: 4
                }
            }
        }
    });

});


