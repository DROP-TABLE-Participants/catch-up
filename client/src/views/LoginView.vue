<template>
    <div class="login-container">
        <div class="login-container__logo">
            <img src="../assets/logo.svg" alt="Logo">
        </div>
        <h2 class="login-container__title">Login to continue</h2>
        <form @submit.prevent="submitForm" class="login-container__form">
            <div class="login-container__input-group">
                <input type="username" v-model="form.username" placeholder="Username" required>
            </div>
            <div class="login-container__input-group">
                <input type="password" v-model="form.password" placeholder="Password" required>
            </div>
            <button type="submit" class="login-container__button">Login</button>
        </form>
        <div class="login-container__signup-container">
            Don’t have an account?
            <a href="#" class="login-container__signup-container--signup-link">Sign Up</a>
        </div>
    </div>
</template>


<script setup lang="ts">
import storageService from "../services/storage-service";
import authenticationService from "../services/authentication-service";
import { ref } from "vue";
import { useRouter } from "vue-router";


const form = ref({
  username: '',
  password: '',
});

const router = useRouter();

async function submitForm() {
  authenticationService.makeLoginRequest(form.value.username, form.value.password).then((response) => {
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
    align-items: center;
    flex-direction: column;
    width: 100%;

    &__form {
        width: 100%;
        box-sizing: border-box;
        padding: 0 2rem;
    }

    &__logo {
        img {
            max-width: 300px;
            margin-bottom: 20px;
        }
    }

    &__title {
        margin-bottom: 15px;
    }

    &__input-group {
        width: 100%;
       

        input {
            width: 100%;
            box-sizing: border-box;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #C8C0C0;
            border-radius: 65px;
        }
    }

    &__forgot-password {
        display: flex;
        justify-content: right;
        margin-top: 10px;
        color: #202020;
        text-decoration: none;
    }

    &__button {
        width: 100%;
        margin-top: 2rem;
        padding: 10px;
        border: none;
        border-radius: 10px;
        background: linear-gradient(90deg, #363FF2 0%, #3CA6C2 55.5%, #40F99B 100%);
        color: white;
        cursor: pointer;
    }

    &__signup-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-top: 20px;

        &--signup-link {
            font-size: 12px;
            color: #00BAB9;
            text-decoration: none;
            text-align: center;
        }
    }
}
</style>
