<template>
<svg xmlns="http://www.w3.org/2000/svg" width="41" height="41" viewBox="0 0 41 41" fill="none">
  <path d="M27.1689 2H14.0811C7.40888 2 2 7.40888 2 14.0811V27.1689C2 33.8411 7.40888 39.25 14.0811 39.25H27.1689C33.8411 39.25 39.25 33.8411 39.25 27.1689V14.0811C39.25 7.40888 33.8411 2 27.1689 2Z" :stroke=" isActive ? '#216DFF' : '#929292'" stroke-width="3.02027"/>
  <path d="M10.5574 26.6656L15.4905 20.1015C15.7926 19.6973 16.2355 19.4212 16.7314 19.328C17.2274 19.2348 17.7403 19.3312 18.1685 19.5981L22.9808 22.6385C23.4255 22.9217 23.9636 23.0192 24.4793 22.91C24.9951 22.8008 25.4475 22.4937 25.7393 22.0546L30.6926 14.5845" :stroke=" isActive ? '#216DFF' : '#929292'" stroke-width="3.02027" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
</template>

<script lang="ts" setup>
import { defineProps, defineEmits, type Ref, ref} from 'vue';
const emits = defineEmits(["on:click"]);

const props = defineProps<{
    isActive: boolean
}>()
</script>

<style lang="scss" scoped>
</style>