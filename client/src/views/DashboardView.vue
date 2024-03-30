<template>
<div class="dashboard-container">
    <h1>Dashboard</h1>
    
    <ProductTrendCard :title="'G102 Mouse'" :roundText="'test'"/>
    
    <TrendFluctuationSection/>
</div>
</template>

<script lang="ts" setup>
import ProductTrendCard from '../components/ProductTrendCard.vue';
import TrendFluctuationSection from '../components/sections/TrendFluctuationSection.vue';
</script>

<style lang="scss" scoped>
.dashboard-container {
    width: 100%;
    box-sizing: border-box;
    padding: 2rem 1rem 0rem 1rem;
}
</style>