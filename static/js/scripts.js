
document.addEventListener('DOMContentLoaded', function() {
    // Use the embedded data
    var length = lengthData;
    var shear = shearData;
    var moment = momentData;

    // Calculate max and min shear values
    var maxShear = Math.max(...shear);
    var minShear = Math.min(...shear);

    // Create a Chart.js chart
    var ctx = document.getElementById('shearMomentChart').getContext('2d');
    var shearMomentChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: length,
            datasets: [
                {
                    label: 'Shear',
                    yAxisID: 'shearYAxis',
                    data: shear,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2,
                    fill: false
                },
                {
                    label: 'Moment',
                    yAxisID: 'momentYAxis',
                    data: moment,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 2,
                    fill: false
                },
                {
                    label: 'Beam',
                    yAxisID: 'shearYAxis',
                    data: Array(length.length).fill(0),
                    borderColor: 'rgba(0, 0, 255)',
                    borderWidth: 2
                }
            ]
        },
        options: {
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    title: {
                        display: true,
                        text: 'Length (m)'
                    }
                },
                shearYAxis: {
                    type: 'linear',
                    position: 'left',
                    title: {
                        display: true,
                        text: 'Shear (kN)'
                    },
                    grid: {
                        display: true
                    },
//                    max: maxShear,
//                    min: minShear
                },
                momentYAxis: {
                    type: 'linear',
                    position: 'right',
                    title: {
                        display: true,
                        text: 'Moment (kN-m)'
                    },
                    suggestedMin: 0,
                    grid: {
                        display: false
                    }
                }

            },
            plugins: {
                legend: {
                    position: 'top'
                }
            },
            elements: {
                line: {
                    tension: 0.5
                },
                point: {
                    radius: 0
                }
            }
        }
    });
});
