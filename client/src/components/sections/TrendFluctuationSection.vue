<template>
<div class="trend-fluctuation-section">
    <div class="heading-container">
        <h2>Trend Fluctuation</h2>
    </div>

    <div class="product-trend-cards-container">
        <ProductTrendCard :title="'G102 Mouse'" :roundText="'test'" :isAccent="true" :isGrowthUp="true"/>
        <ProductTrendCard :title="'G102 Mouse'" :roundText="'test'" :isGrowthUp="false"/>
        <ProductTrendCard :title="'G102 Mouse'" :roundText="'test'" :isGrowthUp="false"/>
    </div>
</div>
</template>

<script lang="ts" setup>
import ProductTrendCard from '../ProductTrendCard.vue';
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