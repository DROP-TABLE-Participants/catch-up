<script setup lang="ts">
import LoginView from './views/LoginView.vue';
import Navbar from './components/Navbar.vue';
</script>

<template>
    <RouterView />

  <Navbar/>
</template>

<style scoped lang="scss">
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
