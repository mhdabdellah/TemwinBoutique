
// chartjs initialization

$(function () {
    "use strict";

// state_order_chart

    var ctx = document.getElementById('state_order_chart').getContext('2d');

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
            datasets: [{
                label: "My First dataset",
                backgroundColor: 'rgba(251,146,140,.15)',
                borderColor: '#fb928c',
                pointBackgroundColor: "#ffffff",
                data: [100, 90, 250, 180, 300]
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
                    display: false,
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
              //tension: 0.4,
                    borderWidth: 1
                },
                point: {
                    radius: 2,
                    hitRadius: 10,
                    hoverRadius: 6,
                    borderWidth: 2
                }
            }
        }
    });



// state_sale_chart

    var ctx = document.getElementById('state_sale_chart').getContext('2d');

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"],
            datasets: [{
                label: "My First dataset",
                backgroundColor: 'rgba(236,209,164,.15)',
                borderColor: '#ecd1a4',
                pointBackgroundColor: "#ffffff",
                data: [120, 200, 170, 220, 150, 170]
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
                    display: false,
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
                    //tension: 0.4,
                    borderWidth: 1
                },
                point: {
                    radius: 2,
                    hitRadius: 10,
                    hoverRadius: 6,
                    borderWidth: 2
                }
            }
        }
    });



// state_profit_chart

    var ctx = document.getElementById('state_profit_chart').getContext('2d');

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
            datasets: [{
                label: "My First dataset",
                backgroundColor: 'rgba(147,159,255,.15)',
                borderColor: '#939fff',
                pointBackgroundColor: "#ffffff",
                data: [300, 190, 250, 80, 300]
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
                    display: false,
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
                    //tension: 0.4,
                    borderWidth: 1
                },
                point: {
                    radius: 2,
                    hitRadius: 10,
                    hoverRadius: 6,
                    borderWidth: 2
                }
            }
        }
    });

});


