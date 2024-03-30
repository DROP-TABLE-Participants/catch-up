<template>
<div class="dashboard-container">
    <OverviewCard/>
    
    <TrendFluctuationSection/>
</div>
</template>

<script lang="ts" setup>
import OverviewCard from '../components/OverviewCard.vue';
import TrendFluctuationSection from '../components/sections/TrendFluctuationSection.vue';
</script>

<style lang="scss" scoped>
.dashboard-container {
    width: 100%;
    box-sizing: border-box;
    padding: 2rem 1rem 0rem 1rem;
}
</style>