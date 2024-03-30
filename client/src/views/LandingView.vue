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
  </template>
  
  <script setup lang="ts">
  </script>
  
  <style scoped lang="scss">
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
  
      &__buttons {
        display: flex;
        gap: 2rem;
  
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
  