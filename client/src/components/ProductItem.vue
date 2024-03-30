<template>
    <div class="product-item">
      <img :src="item.image" :alt="item.name" class="product-image" />
      <div class="product-details">
        <h3 class="product-name">{{ item.name }}</h3>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { defineProps } from 'vue';
  
  const props = defineProps< {
    item: {
      image: string,
      name: string
    }
}>();
  </script>
  
  <style scoped lang="scss">
  .product-item {
    display: flex;
    flex-direction: column;
    // min-width: 11rem;
    // min-height: 12rem;
    align-items: center;
    margin: 0.5rem;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 10px;
    background: #000;
  }
  
  .product-image {
    max-width: 100%;
    margin-bottom: 1rem;
  }
  
  .product-details {
    text-align: center;
  }
  
  .product-name {
    font-size: 1rem;
    color: white;
    margin: 0;
  }
  </style>
  