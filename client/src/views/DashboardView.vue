<template>
<div class="dashboard-container">
    <OverviewCard/>
    
    <TrendFluctuationSection v-if="products" :products="products"/>
</div>
</template>

<script lang="ts" setup>
import { onMounted, type Ref, ref } from 'vue';
import OverviewCard from '../components/OverviewCard.vue';
import TrendFluctuationSection from '../components/sections/TrendFluctuationSection.vue';
import productService from '../services/product-service';

let products: Ref<any> = ref();
let productsHistory: Ref<any> = ref([]);

onMounted(async ()=>{
    products.value = (await productService.getAllProducts()).data;
    console.log(products.value)
})

</script>

<style lang="scss" scoped>
.dashboard-container {
    width: 100%;
    height: fit-content;
    box-sizing: border-box;
    padding: 2rem 1rem 8rem 1rem;
}
</style>