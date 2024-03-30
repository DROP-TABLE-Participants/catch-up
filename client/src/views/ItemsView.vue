<template>
    <div class="inventory-page">
        <header>
            <h1>Your inventory</h1>
            <button class="add-button">+</button>
        </header>
        <section class="inventory-grid">
            <ProductItem  :item="{name:'pes' , image: 'dadada'}"/>
            <ProductItem  :item="{name:'pes' , image: 'dadada'}"/>
            <ProductItem  :item="{name:'pes' , image: 'dadada'}"/>
            <ProductItem  :item="{name:'pes' , image: 'dadada'}"/>
            
        </section>
    </div>
</template>

<script lang="ts" setup>
import ProductItem from '../components/ProductItem.vue';


</script>

<style scoped lang="scss">
.inventory-page {
  display: flex;
  flex-direction: column;
  padding: 1rem;

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;

    h1 {
      font-size: 1.5rem;
    }

    .add-button {
      border: 1px solid #CFCFCF;
      font-size: 1.5rem;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 1rem;
      width: 2.5rem;
      height: 2.5rem;
      border-radius: 50%;
    }
  }

  .inventory-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); 
    grid-gap: 1rem;
    align-items: start;

    @media (max-width: 768px) {
      grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    }
  }
}

</style>
