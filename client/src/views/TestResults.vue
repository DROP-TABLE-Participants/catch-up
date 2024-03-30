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
            <p class="heading">{{ heading }}</p>
        </div>
        
    </div>
</template>


<script setup lang="ts">
import { useRoute } from 'vue-router';

const route = useRoute();
var heading = route.params.productName;

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
</style>
