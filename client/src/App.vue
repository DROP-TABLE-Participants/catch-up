<script setup lang="ts">
import LoginView from './views/LoginView.vue';
import Navbar from './components/Navbar.vue';
</script>

<template>
  <div class="site-wrapper">
    <div class="content-container">
      <RouterView />
    </div>
  </div>
</template>

<style scoped lang="scss">
.site-wrapper {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;

  justify-content: center;
  overflow: hidden;
  .content-container {
    width: 100%;
    height: 100vh;
    max-width: 850px;
    overflow: auto;

  }

}
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
