<template>
    <div class="product-card" :class="props.isAccent ? 'main' : ''">
        <div class="title-container">
            <h2 class="title">{{ props.title }}</h2>
            <ArrowLinkIcon :class="props.isAccent ? 'light' : ''"/>
        </div>
        <ProductGrowthElement :percentage="growth" :isGrowthUp="isGrowthUp"/>
    </div>
</template>

<script lang="ts" setup>
import { defineProps } from 'vue';
import ArrowLinkIcon from './icons/ArrowLinkIcon.vue';
import ProductGrowthElement from './misc/ProductGrowthElement.vue';

  const props = defineProps<{
    title: string,
    roundText: string,
    growth: number,
    isAccent?: boolean,
    isGrowthUp: boolean,
}>();
</script>

<style lang="scss" scoped>
.product-card { 
    border-radius: 32px;
    border: 0.5px solid #B8B8B8;
    background: #FFF;

    box-sizing: border-box;
    padding: 1rem;
    cursor: pointer;

    .title-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        margin-bottom: 1rem;

        .title {
            color: #06348D;
            font-family: "Hanken Grotesk";
            font-size: 22.588px;
            font-style: normal;
            font-weight: 400;
            line-height: normal;
        }
    }
}

.main {
    color: white;
    border: 0.5px solid #72A2FF;
    background: #0038FF;

    .title-container {
        .title {
            color: white;
        }
    }
}
</style>