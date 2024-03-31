<template>
    <div class="navbar">
        <div class="navbar__logo">
            <router-link to="/" class="navbar__logo">
                <img src="../assets/logo.png" alt="logo"/>
            </router-link>
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
    <div v-if="loading" class="loading-bar">
        <div class="loading-spinner"></div>
    </div>
    <section class="centered" v-if="!loading">
        <div class="content">
            <div class="content__text">
                <p class="heading">{{ heading }}</p>
                <p class="description">Based on the below statistics you could look into increasing the supply of the product or decreasing</p>
            </div>
            <GaugeChart :percentage="fetchedData"/>
        </div>
    </section>
</template>


<script setup lang="ts">
import { useRoute } from 'vue-router';
import GaugeChart from '../components/GaugeChart.vue';
import { onMounted, ref } from 'vue';

const route = useRoute();
const apiUrl = 'http://localhost:8000/api/test/';
const loading = ref(true);
const fetchedData = ref([]);
var heading = route.params.productName;

async function fetchData() {
  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
      body: JSON.stringify({
        title: `${route.params.productName}`
        },
    )});

    const data = await response.json();
    fetchedData.value = data;
  } catch (error) {
    console.error('Error fetching data:', error);
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchData();
});
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
  max-width: 850px;

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
      font-size: 3.5rem;
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
    align-items: center;
    margin-top: 20px;
    gap: 10px;

    &__links {
      margin-top: 10px;
    }

    &__button {
      display: none;
      margin-top: 20px;
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

.loading-bar {
    width: 100%;
    height: 100vh;
    background-color: transparent;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
}

.loading-spinner {
    width: 40px;
    height: 40px;
    border-radius: 50%; /* Make it circular */
    border: 4px solid #ccc;
    border-top-color: #007bff; /* Loading bar color */
    animation: loading-rotate 1s linear infinite; /* Rotate animation */
}

@keyframes loading-rotate {
    to {
        transform: rotate(360deg); /* Rotate a full circle */
    }
}
</style>
