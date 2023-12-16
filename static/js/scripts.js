
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
                    borderWidth: 2, // Increase line width for better visibility
                    fill: false
                },
                {
                    label: 'Moment',
                    yAxisID: 'momentYAxis',
                    data: moment,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 2, // Increase line width for better visibility
                    fill: false
                },
                {
                    label: 'Beam',
                    yAxisID: 'shearYAxis',
                    data: Array(length.length).fill(0), // Array of zeros for the origin
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
                        display: true // Turn off grid for shear
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
                        display: false // Turn off grid for moment
                    }
                }

            },
            plugins: {
                legend: {
                    position: 'top' // Position legend at the bottom
                }
            },
            elements: {
                line: {
                    tension: 0.5 // Adjust tension for smooth lines
                },
                point: {
                    radius: 0 // Set point radius to 0 to disable points
                }
            }
        }
    });
});
