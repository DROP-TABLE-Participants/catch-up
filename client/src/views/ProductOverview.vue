<template>
    <div class="product-page">
        <header>
            <button @click="navigateToItems" class="back-button">
                <BackArrowIcon />
            </button>
            <h1 v-if="product">{{product.name}}</h1>
        </header>
        
        <section class="trend-section">
            <!-- <canvas ref="chartRef" id="trendChart"></canvas> -->
        </section>

        <section class="interest-section">
        </section>
        <OverviewCard/>
        <h2>The interest is highly positive</h2>
        <img src="../assets/CatchUp.png" alt="chart" class="chart"/>
    </div>

    <Navbar :active="'products'"/>
</template>

<script lang="ts" setup>
import { onMounted, ref, type Ref } from 'vue';
import Chart from 'chart.js/auto';
import { useRoute, useRouter } from 'vue-router';
import BackArrowIcon from '../components/icons/BackArrowIcon.vue';
import OverviewCard from '../components/OverviewCard.vue';
import GaugeChart from '../components/GaugeChart.vue';
import productService from '../services/product-service';
import Navbar from '../components/Navbar.vue';

const route = useRoute();
const router = useRouter();

const navigateToItems = () => {
  router.push('/items');
};

const chartRef = ref<HTMLCanvasElement | null>(null);

const product: Ref<any> = ref();
const history: Ref<Array<any>> = ref([]);

let chartLabels: Array<string> = [];
let chartValues: Array<string> = [];

let show: Ref<boolean> = ref(false);


onMounted(async ()=>{
  product.value = (await productService.getProductById(+route.params.id)).data;

  history.value = (await productService.getProductTrendHistory(+route.params.id)).data;

  history.value.forEach((record: any)=>{
    chartLabels.push(record.date.replaceAll('-', '.'));
    chartValues.push(record.value)
  })
  
  setUpChart();
})

function setUpChart(){
  Chart.defaults.borderColor = 'rgba(164, 195, 255, 0.50)';
    Chart.defaults.color = '#000';
    let ctx = document.getElementById('trendChart');

    new Chart(ctx as HTMLCanvasElement, {
      type: 'line',
      data: {
        labels: chartLabels,
        datasets: [{
          label: 'G102',
          data: chartValues,
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
};




</script>


<style scoped lang="scss">

h2{
        color: #000;
        font-family: Inter;
        font-size: 1.1875rem;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }

.product-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;

  header {
    display: flex;
    align-items: center;
    margin-bottom: 2rem;

    h1 {
      color: #000;
      font-family: "Hanken Grotesk";
      font-size: 2.58888rem;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
      margin-left: 1rem;
    }
}
}

.back-button {
   cursor: pointer;
   border: none;
   background: transparent;
}

.chart {
  margin-top: 2rem;
  width: 250px;
  height: 140px;
}
</style>

