<template>
<div class="dashboard-container">
    <OverviewCard/>
    
    <TrendFluctuationSection :products="products"/>
</div>
</template>

<script lang="ts" setup>
import { onMounted, type Ref, ref } from 'vue';
import OverviewCard from '../components/OverviewCard.vue';
import TrendFluctuationSection from '../components/sections/TrendFluctuationSection.vue';
import productService from '../services/product-service';
import TestProduct from './TestProduct.vue';

let products: any = [];
let productsHistory: any = [];
let productsHistorySorted: Ref<any> = ref([]);

onMounted( ()=>{
    productService.getAllProducts().then((res)=>{
        products = res.data;

        res.data.forEach( (product: any)=>{
            productService.getProductTrendHistory(product.id).then((res)=>{
                productsHistory.push(res.data);
            });
        })

        console.log(productsHistory)

        Test();
    });

    //for each record check second to last and last value difference
    //sort by that


    
    // productsHistory.value = productsHistory.value.sort((recordA: any, recordB: any) =>{((recordA[recordA.length - 2] - recordA[recordA.length-1]) / recordA[recordA.length-1]) * 100 > ((recordB[recordB.length - 2] - recordB[recordB.length-1]) / recordB[recordB.length-1]) * 100 ? 1 : -1 });

    // console.log(productsHistory.value)



    
})

function Test() {
    productsHistory.forEach(()=>{
        console.log('hello')
    })
}
</script>

<style lang="scss" scoped>
.dashboard-container {
    width: 100%;
    box-sizing: border-box;
    padding: 2rem 1rem 0rem 1rem;
}
</style>