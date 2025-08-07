/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */

const barConfig = {
  type: 'bar',
  data: {
    labels: [ 'Junio', 'Julio', 'Agosto'],
    datasets: [
      {
        label: 'Producto 1',
        backgroundColor: '#0694a2',
        // borderColor: window.chartColors.red,
        borderWidth: 1,
        data: [2, 1, 0],
      },
      {
        label: 'Producto 2',
        backgroundColor: '#7e3af2',
        // borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: [1, 0, 0],
      },
      {
        label: 'Producto 3',
        backgroundColor: 'rgba(88, 228, 118, 1)',
        // borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: [3, 0, 2],
      },
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },
  },
}

const barsCtx = document.getElementById('bars')
window.myBar = new Chart(barsCtx, barConfig)
