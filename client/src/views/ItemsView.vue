<template>
    <div class="inventory-page">
        <header>
            <h1>Your inventory</h1>
            <button @click="navigateToAddItem" class="add-button">+</button>
        </header>
        <section class="inventory-grid">
          <ProductItem
        v-for="item in products"
        :key="item.id" 
        :item="item"
        @click="navigateToProductOverview(item.id)"
      />
      <!--

        <ProductItem
        v-for="item in products"
        :key="item.id" 
        :item="item"
        @click="navigateToProductOverview(item.id)"
        />
      -->
            
        </section>
    </div>

    <Navbar :active="'products'"/>
</template>

<script lang="ts" setup>
import { onMounted, type Ref, ref } from 'vue';
import ProductItem from '../components/ProductItem.vue';
import { useRouter } from 'vue-router';
import productService from '../services/product-service';
import Navbar from '../components/Navbar.vue';

let products: Ref<any> = ref();

onMounted(async ()=>{
    products.value = (await productService.getAllProducts()).data;
    console.log(products.value)
})

const router = useRouter();

const navigateToAddItem = () => {
  router.push('/addItem'); 
};


const navigateToProductOverview = (id: any) => {
  router.push({name: 'productView', params: {id: id}});
};


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
      color: #000;
      font-family: "Hanken Grotesk";
      font-size: 2.58888rem;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
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
    grid-template-columns: repeat(2, 1fr); 
    row-gap: 1rem;
    column-gap: 1rem;
    align-items: start;
    overflow-y: scroll;

  }
}
</style>

