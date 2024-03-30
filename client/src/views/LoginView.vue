<template>
    <div class="login-container">
        <div class="login-container__logo">
            <img src="../assets/logo.svg" alt="Logo">
        </div>
        <h2 class="login-container__title">Login to continue</h2>
        <form @submit.prevent="submitForm" class="login-container__form">
            <div class="login-container__input-group">
                <input type="email" v-model="user.email" placeholder="Email" required>
            </div>
            <div class="login-container__input-group">
                <input type="password" v-model="user.password" placeholder="Password" required>
            </div>
            <a href="#" class="login-container__forgot-password">Forgot password?</a>
            <button type="submit" class="login-container__button">Login</button>
        </form>
        <div class="login-container__signup-container">
            Don’t have an account?
            <a href="#" class="login-container__signup-container--signup-link">Sign Up</a>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                email: '',
                password: ''
            }
        };
    },
    methods: {
        submitForm() {
            // Handle form submission
            console.log(this.user);
            // TODO: Implement your login logic here
        }
    }
};
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
