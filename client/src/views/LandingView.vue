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
      <router-link to="/login">Login</router-link>
    </div>
  </div>
  <section class="centered">
    <div class="content">
      <div class="content__text">
        <p class="heading">Adapt your business to the market trends</p>
        <p class="description">Stay updated on the current market trends of your products and adapt with ease</p>
      </div>
      <div class="content__buttons">
        <router-link to="/test">Test Product</router-link>
        <router-link to="/register">Create Account</router-link>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
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
    margin-bottom: 4rem;
    gap: 4rem;

    .heading {
      font-size: 2rem;
      font-weight: 700;
      margin-bottom: 1rem;
      font-size: 71px;
      font-style: normal;
      font-weight: 700;
      color: #1B1B1B;
      width: 725px;
    }

    .description {
      font-size: 1.2rem;
      font-weight: 500;
      color: #1B1B1B;
      width: 725px;
      text-align: center;
      font-size: 25px;
      font-style: normal;
      font-weight: 500;
      line-height: normal;
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
    }

    :last-child {
      display: flex;
      font-size: 1.1rem;
      justify-content: center;
      align-items: center;
      padding: 0.5rem 1rem;
      border: 2px solid #40F99B;
      border-radius: 17px;
      width: 150px;
      height: 40px;
      color: #252525;
      text-decoration: none;
      transition: background-color 0.3s;

      &:hover {
        background-color: #40F99B;
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
        font-size: 2.2rem;
        width: 80%;
        margin-left: 10%;
      }

      .description {
        font-size: 1rem;
        width: 100%;
      }
    }

    &__buttons {
      flex-direction: column;

      :first-child,
      :last-child {
        width: 100%;
        height: auto;
        font-size: 1.3rem;
      }
    }
  }
}
</style>
