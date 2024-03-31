<template>
    <div class="login-container">
      <div class="login-container__logo">
        <img src="../assets/logo.png" alt="Logo">
      </div>
      <h2 class="login-container__title">Register an account</h2>
      <form @submit.prevent="submitForm" class="login-container__form">
        <div class="login-container__input-group">
          <input type="username" v-model="form.username" placeholder="Username" required>
        </div>
        <div class="login-container__input-group">
          <input type="email" v-model="form.email" placeholder="Email" required>
        </div>
        <div class="login-container__input-group">
          <input type="password" v-model="form.password" placeholder="Password" required>
        </div>
        <div class="login-container__input-group">
          <input type="password" v-model="form.repeat" placeholder="Repeat Password" required>
        </div>
        <button type="submit" class="login-container__button"><span>Sign Up</span> <ArrowLinkIcon class="light"/></button>
      </form>
      <div class="login-container__signup-container">
        Have an account?
        <a href="#" class="login-container__signup-container--signup-link">Sign in</a>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import storageService from "../services/storage-service";
  import authenticationService from "../services/authentication-service";
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import ArrowLinkIcon from "../components/icons/ArrowLinkIcon.vue";
  
  
  const form = ref({
    username: '',
    email: '',
    password: '',
    repeat: '',
  });
  
  const router = useRouter();
  
  async function submitForm() {
    authenticationService.makeRegisterRequest(form.value.username, form.value.email, form.value.password, form.value.repeat).then((response) => {
      storageService.saveAccessToken(response.data.access);
      storageService.saveRefreshToken(response.data.refresh);
      storageService.saveTokenExpiresDate((Date.now() + 29 * 60000).toString());
      router.push("/dashboard");
    }).catch((error) => {
      console.log(error);
    });
  }
  </script>
  
  <style scoped lang="scss">
  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }
  
  .login-container__form {
    width: 100%;
    max-width: 400px; /* Adjust max-width as needed */
    box-sizing: border-box;
    padding: 0 2rem;
  }
  
  .login-container__logo img {
    max-width: 300px;
    margin-bottom: 20px;
  }
  
  .login-container__title {
    margin-bottom: 15px;
    font-family: "Hanken Grotesk", sans-serif;
  }
  
  .login-container__input-group {
    width: 100%;
  }
  
  .login-container__input-group input {
    width: 100%;
    box-sizing: border-box;
    padding: 1.2rem 2rem;
    margin: 5px 0;
    border-radius: 1.5rem;
    border: 2px solid #3741f2;
    background: #fff;
    font-family: "Hanken Grotesk", sans-serif;
  }
  
  .login-container__button {
    width: 100%;
    margin-top: 2rem;
    padding: 1.2rem 2rem;
    border: none;
    border-radius: 3.4375rem;
    background: #3741f2;
    color: white;
    height: 50px;
    cursor: pointer;
    font-family: "Hanken Grotesk", sans-serif;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .login-container__signup-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-top: 20px;
  }
  
  .login-container__signup-container--signup-link {
    font-size: 12px;
    color: #00bab9;
    text-decoration: none;
    text-align: center;
    font-family: "Hanken Grotesk", sans-serif;
  }
  </style>
  