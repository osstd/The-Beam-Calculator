document.addEventListener("DOMContentLoaded", function () {
  var length = lengthData;
  var shear = shearData;
  var moment = momentData;

  // Calculate max and min shear and moment values
  var maxShear = Math.max(...shear);
  var minShear = Math.min(...shear);

  if (maxShear === minShear) {
    maxShear = maxShear;
    minShear = 0.0;
  }

  var maxMoment = Math.max(...moment);
  var minMoment = Math.min(...moment);

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
          borderColor: "rgb(171, 195, 124)",
          borderWidth: 1,
          order: 1,
          fill: {
            target: true,
            above: "rgb(171, 195, 124)",
            below: "rgb(171, 195, 124)",
          },
        },
        {
          label: "Beam",
          yAxisID: "shearYAxis",
          data: Array(length.length).fill(0),
          borderColor: "rgb(0, 0, 0)",
          borderWidth: 2,
          order: 0,
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
          //          max: maxShear,
          //          min: minShear,
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
          borderColor: "rgb(197, 113, 114)",
          borderWidth: 1,
          order: 1,
          fill: {
            target: true,
            above: "rgb(197, 113, 114)",
            below: "rgb(197, 113, 114)",
          },
        },
        {
          label: "Beam",
          yAxisID: "momentYAxis",
          data: Array(length.length).fill(0),
          borderColor: "rgb(0, 0, 0)",
          borderWidth: 2,
          order: 0,
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
          //          max: maxMoment,
          //          min: minMoment,
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
