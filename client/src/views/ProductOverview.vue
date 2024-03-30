<template>
    <div class="product-page">
        <header>
            <button @click="navigateToItems" class="back-button">
                <BackArrowIcon />
            </button>
            <h1 v-if="product">{{product.name}}</h1>
        </header>
        
        <section class="trend-section">
            <h2>This item is getting trendy</h2>
            <canvas ref="chartRef" id="trendChart"></canvas>
        </section>

        <section class="interest-section">
            <h2>Item interest is prop</h2>
            <GaugeChart :percentage="25.23"/>
        </section>



    </div>
</template>

<script lang="ts" setup>
import { onMounted, ref, type Ref } from 'vue';
import Chart from 'chart.js/auto';
import { useRoute, useRouter } from 'vue-router';
import BackArrowIcon from '../components/icons/BackArrowIcon.vue';
import GaugeChart from '../components/GaugeChart.vue';
import productService from '../services/product-service';

const route = useRoute();
const router = useRouter();

const navigateToItems = () => {
  router.push('/items');
};

const chartRef = ref<HTMLCanvasElement | null>(null);

const product: Ref<any> = ref();

onMounted(async ()=>{
  product.value = (await productService.getProductById(+route.params.id)).data;

  console.log((await productService.getProductTrendHistory(+route.params.id)).data);
})

onMounted(() => {
  if (!chartRef.value) return;
  
  const ctx = chartRef.value.getContext('2d');
  if (!ctx) return;

  const gradientBg = ctx.createLinearGradient(0, 0, 0, ctx.canvas.clientHeight);
  gradientBg.addColorStop(0, '#40F99B');
  gradientBg.addColorStop(1, 'rgba(177, 185, 248, 0)');

  const trendChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: 'Today\'s Activity',
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: gradientBg, // Use the gradient for the fill color
        borderColor: 'rgba(135, 206, 250, 1)',
        borderWidth: 1,
        fill: true,
        tension: 0.4, // Added to smooth the line
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
});




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

</style>

