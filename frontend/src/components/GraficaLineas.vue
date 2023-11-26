<template>
  <div class="grafica-container">
    <canvas id="myChart"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js/auto";
export default {
  name: "GraficaLineas",
  props: {
    labels: Array,
    temperaturas: Array,
    humedades: Array,
  },
  data() {
    return {
      datacollection: {
        labels: this.labels,
        datasets: [
          {
            label: "Temperatura",
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            data: this.temperaturas,
          },
          {
            label: "Humedad",
            backgroundColor: "rgba(54, 162, 235, 0.2)",
            data: this.humedades,
          },
        ],
      },
      options: {},
    };
  },
  mounted() {
    let myChart = new Chart(document.getElementById("myChart"), {
      type: "line",
      data: this.datacollection,
      options: this.options,
    });
    myChart.update();
  },
};
</script>

<style scoped>
.grafica-container {
  width: 100%;
  height: 100%;
}

#myChart {
  width: 100%;
  height: 100%;
}
</style>
