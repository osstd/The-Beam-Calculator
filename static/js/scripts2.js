document.addEventListener("DOMContentLoaded", function () {
  var length = lengthData;
  var shear = shearData;
  var moment = momentData;

  // Calculate max and min shear values
  var maxShear = Math.max(...shear);
  var minShear = Math.min(...shear);

  if (maxShear === minShear) {
    maxShear = maxShear;
    minShear = 0;
  }

  // Create a Shear Chart.js chart
  var ctx = document.getElementById("ShearChart").getContext("2d");
  var ShearChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: length,
      datasets: [
        {
          label: "Shear",
          yAxisID: "shearYAxis",
          data: shear,
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 2,
          fill: true,
        },
        {
          label: "Beam",
          yAxisID: "shearYAxis",
          data: Array(length.length).fill(0),
          borderColor: "rgba(0, 0, 255)",
          borderWidth: 2,
        },
      ],
    },
    options: {
      scales: {
        x: {
          type: "linear",
          position: "bottom",
          title: {
            display: true,
            text: "Length (m)",
          },
          grid: {
            display: false,
          },
        },
        shearYAxis: {
          type: "linear",
          position: "left",
          title: {
            display: true,
            text: "Shear (kN)",
          },
          grid: {
            display: false,
          },
          max: maxShear,
          min: minShear,
        },
      },
      plugins: {
        legend: {
          position: "top",
        },
      },
      elements: {
        line: {
          tension: 0.5,
        },
        point: {
          radius: 0,
        },
      },
    },
  });

  // Create a Moment Chart.js chart
  var ctx = document.getElementById("MomentChart").getContext("2d");
  var MomentChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: length,
      datasets: [
        {
          label: "Moment",
          yAxisID: "momentYAxis",
          data: moment,
          borderColor: "rgba(255, 99, 132, 1)",
          borderWidth: 2,
          fill: true,
        },
        {
          label: "Beam",
          yAxisID: "momentYAxis",
          data: Array(length.length).fill(0),
          borderColor: "rgba(0, 0, 255)",
          borderWidth: 2,
        },
      ],
    },
    options: {
      scales: {
        x: {
          type: "linear",
          position: "bottom",
          title: {
            display: true,
            text: "Length (m)",
          },
          grid: {
            display: false,
          },
        },
        momentYAxis: {
          type: "linear",
          position: "left",
          title: {
            display: true,
            text: "Moment (kN-m)",
          },
          grid: {
            display: false,
          },
        },
      },
      plugins: {
        legend: {
          position: "top",
        },
      },
      elements: {
        line: {
          tension: 0.5,
        },
        point: {
          radius: 0,
        },
      },
    },
  });
});
