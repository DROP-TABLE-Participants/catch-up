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
            padding: 1.2rem 2rem;
            margin: 5px 0;
            border-radius: 1.5rem;
            border: 2px solid #3741F2;
            background: #FFF;
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
        color: #FFF;
        font-family: "Hanken Grotesk";
        font-size: 1.23069rem;
        font-style: normal;
        font-weight: 500;
        line-height: normal;

        width: 100%;
        margin-top: 2rem;
        padding: 1.2rem 2rem;
        border: none;
        border-radius: 3.4375rem;
        background: #3741F2;
        color: white;
        cursor: pointer;

        display: flex;
        align-items: center;
        justify-content: space-between;
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
