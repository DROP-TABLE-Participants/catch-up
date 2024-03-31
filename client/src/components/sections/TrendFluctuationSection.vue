<template>
<div class="trend-fluctuation-section">
    <div class="heading-container">
        <h2>Trend Fluctuation</h2>
    </div>

    <div class="product-trend-cards-container" v-if="products.at(0).name">
        <ProductTrendCard v-for="product in productsHistory" :title="product.product.name" :growth="product.fluctuation" :isGrowthUp="product.fluctuation > 0"  @click="router.push({name:'productView', params:{id:product.product.id}})"/>
    </div>
</div>
</template>

<script lang="ts" setup>
import { defineProps, onMounted, type Ref, ref } from 'vue';
import ProductTrendCard from '../ProductTrendCard.vue';
import productService from '../../services/product-service';
import router from '../../router';

const props = defineProps<{
    products: any,
}>();

let productsHistory: Ref<any> = ref([]);

onMounted(()=>{
    props.products.forEach(async (product)=>{
        productService.getProductTrendHistory(product.id).then((res)=>{
            let record = res.data;
            let fluctuation = record[record.length-2].value / record[record.length-1].value * 100 - 100;
            productsHistory.value.push({product:product, fluctuation:fluctuation.toFixed(2)});
            console.log(record)
        });
    })

   
})


</script>

<style lang="scss" scoped>
.trend-fluctuation-section {
    width: 100%;
    .heading-container {
        color: #333;
        font-family: "Hanken Grotesk";
        font-size: 1rem;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin-bottom: 1rem;
    }

    .product-trend-cards-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
    }
}
</style>