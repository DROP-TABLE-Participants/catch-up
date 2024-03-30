<template>
    <div class="product-page">
        <header>
            <button @click="navigateToItems">
                <BackArrowIcon />
            </button>
            <h1>Name prop</h1>
        </header>
        
    </div>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router';
import BackArrowIcon from '../components/icons/BackArrowIcon.vue';


const router = useRouter();

const navigateToItems = () => {
  router.push('/items'); 
};


</script>

<style scoped lang="scss">
.product-page {
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
}
}

</style>

