<template>
    <div class="navbar">
        <div class="navbar__logo">
            <img src="../assets/logo.png" alt="logo" />
        </div>
        <div class="navbar__links">
            <router-link to="/pricing">Pricing</router-link>
            <router-link to="/dashboard">Dashboard</router-link>
            <router-link to="/test">Try it out</router-link>
        </div>
        <div class="navbar__button">
            <router-link to="/register">Sing Up</router-link>
        </div>
    </div>
    <div class="content">
        <div class="content__text">
            <p class="heading">Lookup a product and see it’s current market trend</p>
            <p class="description">Enter the name and a short description of your product. Note that the product should be a physical and preferably a gaming orientated for the demo.</p>
        </div>
        <div class="content__input">
            <input v-model="productName" type="text" placeholder="Enter your input" />            
        </div>
        <div class="content__buttons">
            <p>
                <router-link :to="{ name: 'results', params: { productName: productName } }">Test Product</router-link>
            </p>
        </div>
    </div>
</template>


<script setup lang="ts">
  import { ref } from 'vue';
  
  const productName = ref('');
</script>

<style scoped lang="scss">
    * {
      font-family: 'Hanken Grotesk', sans-serif;
    }

    .navbar {
      display: flex;
      justify-content: space-around;
      align-items: center;
      position: relative;
      width: 100vw;
      margin-top: 40px;
  
      &__logo {
        img {
          width: 130px;
        }
      }
  
      &__links {
        display: flex;
        gap: 2rem;
  
        a {
          text-decoration: none;
          color: #000;
          font-weight: 500;
  
          &:hover {
            text-decoration: underline;
          }
        }
      }
  
      &__button {
        a {
          padding: 0.5rem 1rem;
          background-color: #000;
          color: #fff;
          border-radius: 5px;
          text-decoration: none;
          transition: background-color 0.3s;
  
          &:hover {
            background-color: #333;
          }
        }
      }
    }

    .content {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      position:relative;
  
      &__text {
        text-align: center;
        margin-bottom: 2rem;
  
        .heading {
          font-size: 2rem;
          font-weight: 700;
          margin-bottom: 1rem;
        }
  
        .description {
          font-size: 1.2rem;
          font-weight: 500;
        }
      }

      &__input{
        display: flex;
        margin-bottom: 2rem;
        
        input {
          width: 100%;
          box-sizing: border-box;
          padding: 10px;
          margin: 5px 0;
          border: 1px solid #C8C0C0;
          border-radius: 65px;
        }
      }
  
      &__buttons {
        display: flex;
  
        a {
          padding: 0.5rem 1rem;
          background-color: #000;
          color: #fff;
          border-radius: 5px;
          text-decoration: none;
          transition: background-color 0.3s;
  
          &:hover {
            background-color: #333;
          }
        }
      }
    }
</style>
