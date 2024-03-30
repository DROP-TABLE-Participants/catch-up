<template>
<div class="overview-card-container">
    <h1>Overview</h1>
    <canvas id="chart"></canvas>
</div>
</template>

<script lang="ts" setup>
import Chart from 'chart.js/auto';
import { onMounted } from 'vue';

onMounted(()=>{
    Chart.defaults.borderColor = 'rgba(164, 195, 255, 0.50)';
    Chart.defaults.color = '#FFF';
    let ctx = document.getElementById('chart');

    new Chart(ctx as HTMLCanvasElement, {
      type: 'line',
      data: {
        labels: ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar'],
        datasets: [{
          label: '# of Votes',
          data: [7, 12, 10, 5, 12, 19, 3, 5, 2, 3, 10, 12],
          borderWidth: 1,
          tension: 0.4,
          fill: true, 
          backgroundColor: (context)=>{
            if(!context.chart.chartArea) return;
            const {ctx, data, chartArea: {top, bottom} } = context.chart;
            const gradientBg = ctx.createLinearGradient(0, top, 0, bottom);


            gradientBg.addColorStop(0, '#40F99B');
            gradientBg.addColorStop(1, 'rgba(177, 185, 248, 0.00)');

            return gradientBg;
          },
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        },
        responsive: true,
      }
    });

})


</script>

<style lang="scss" scoped>
.overview-card-container {
    border-radius: 2rem;
    border: 1px solid #72A2FF;
    background: #0038FF;

    box-sizing: border-box;
    padding: 1rem;

    width: 100%;
    height: fit-content;

    h1 {
        color: #FFF;
        font-family: 'Montserrat';
        font-size: 2.03306rem;
        font-style: normal;
        font-weight: 600;
        line-height: normal;
    }

    #chart {
        width: 100% !important;
    }
}
</style>
