<template>
    <div class="product-item">
      <img :src="BASE_PATH + props.item.image_url" :alt="props.item.name" class="product-image" />
      <div class="product-details">
        <h3 class="product-name">{{ props.item.name }}</h3>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { defineProps } from 'vue';
  import { BASE_PATH } from '../api/base';

  const props = defineProps< {
    item: any,
}>();
  </script>
  
  <style scoped lang="scss">
  .product-item {
    display: flex;
    flex-direction: column;
    // min-width: 11rem;
    // min-height: 12rem;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    border-radius: 1.125rem;
    border: 1px solid #E3E3E3;
    background: #FFF;

    .product-image {
      max-width: 100%;
      margin-bottom: 1rem;
      height: 80%;
      object-fit: cover;
    }
  }
  
  
  .product-details {
    height: 20%;
    text-align: center;
  }
  
  .product-name {
    color: #000;
    font-family: "Hanken Grotesk";
    font-size: 1.41175rem;
    font-style: normal;
    font-weight: 400;
    line-height: normal;
  }
  </style>
  