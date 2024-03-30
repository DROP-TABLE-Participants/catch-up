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
    <section class="centered">
      <div class="content">
        <div class="content__text">
            <p class="heading">Lookup a product and see it’s current market trend</p>
            <p class="description">Enter the name and a short description of your product. Note that the product should be a physical and preferably a gaming orientated for the demo.</p>
        </div>
        <div class="content__input">
          <input v-model="productName" type="text" placeholder="Product Name and Description" />
          <br>
          <span v-if="!productNameValid" class="error">Product name is required</span>
        </div>
        <div class="content__buttons">
            <p @click="submitForm">
              <button :disabled="!isFormValid" @click="submitForm">
                Test Product
              </button>
            </p>
        </div>
    </div>
    </section>
</template>


<script setup lang="ts">
  import { ref } from 'vue';
import router from '../router';
  
  const productName = ref('');
  const productNameValid = ref(true);

  function submitForm() {
    if (!productName.value.trim()) {
      productNameValid.value = false;
      return;
    }
    router.push({ name: 'results', params: { productName: productName.value } });
    }

  const isFormValid = ref(true);
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
      background-color: #00E99E;
      color: #262626;
      border-radius: 5px;
      width: 40px;
      text-decoration: none;
      transition: background-color 0.3s;

      &:hover {
        background-color: #3bf0b7;
      }
    }
  }
}

  .centered {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70vh;
}

.content {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  position: relative;

  &__text {
    text-align: center;
    margin-bottom: 3rem;
    gap: 4rem;

    .heading {
      font-size: 3.2rem;
      font-weight: 700;
      margin-bottom: 1rem;
      font-style: normal;
      color: #1B1B1B;
      width: 725px;
    }

    .description {
      font-size: 1.2rem;
      font-weight: 400;
      color: #1B1B1B;
      width: 725px;
      text-align: center;
      font-style: normal;
      line-height: normal;
    }
  }

  &__input {
    margin-bottom: 2rem;
    input {
      padding: 0.5rem 1rem;
      border-radius: 16px;
      border: 1px solid #000;
      width: 500px;
      height: 30px;
      font-size: 1rem;
      text-align: center;
    }
  }

  &__buttons {
    display: flex;
    gap: 2rem;

    :first-child {
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 1.1rem;
      padding: 0.5rem 1rem;
      border-radius: 17px;
      width: 150px;
      height: 40px;
      background: #3741F2;
      color: #fff;
      text-decoration: none;
      transition: background-color 0.3s;

      &:hover {
        background-color: #1d27e6;
      }

      button {
          background: none;
          color: inherit;
          border: none;
          padding: 0;
          font: inherit;
          cursor: pointer;
          outline: inherit;
        }
    }
  }
}

@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
    align-items: flex-start;
    margin-top: 20px;

    &__links {
      margin-top: 10px;
    }

    &__button {
      margin-top: 10px;
    }
  }

  .content {
    &__text {
      .heading {
        font-size: 1.5rem;
        width: 100%;
      }

      .description {
        font-size: 1rem;
        width: 100%;
      }
    }

    &__buttons {
      flex-direction: column;
      cursor: pointer;


      :first-child {
        width: 100%;
        height: auto;
        font-size: 1rem;

        button {
          background: none;
          color: inherit;
          border: none;
          padding: 0;
          font: inherit;
          cursor: pointer;
          outline: inherit;
        }
      }
    }
  }
}

.error {
  color: red;
  font-size: 0.8rem;
}
</style>
