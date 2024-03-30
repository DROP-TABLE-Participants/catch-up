<template>
    <div class="product-card" :class="isAccent ? 'main' : ''">
        <div class="title-container">
            <h2 class="title">{{ title }}</h2>
            <ArrowLinkIcon :class="isAccent ? 'light' : ''"/>
        </div>
        <ProductGrowthElement :percentage="1.24123" :isGrowthUp="true"/>
    </div>
</template>

<script lang="ts" setup>
import { defineProps } from 'vue';
import ArrowLinkIcon from './icons/ArrowLinkIcon.vue';
import ProductGrowthElement from './misc/ProductGrowthElement.vue';

  defineProps<{
    title: string,
    roundText, string,
    isAccent?: boolean,
}>();
</script>

<style lang="scss" scoped>
.product-card { 
    border-radius: 32px;
    border: 0.5px solid #B8B8B8;
    background: #FFF;

    box-sizing: border-box;
    padding: 1rem;

    .title-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        width: 100%;

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
    background: #216DFF;

    .title-container {
        .title {
            color: white;
        }
    }
}
</style>