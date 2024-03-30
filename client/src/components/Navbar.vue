<template>
<div class="nav-container"> 
    <DashboardIcon @click="navigate('/dashboard')"/>
    <ItemsIcon @click="navigate('/items')"/>
    <AccountIcon @click="navigate('/account')"/>
</div>
</template>

<script lang="ts" setup>
import DashboardIcon from './icons/DashboardIcon.vue';
import ItemsIcon from './icons/ItemsIcon.vue';
import AccountIcon from './icons/AccountIcon.vue';
import { useRouter } from 'vue-router';


const router = useRouter();

const navigate = (path: string) => {
  router.push(path);
};

</script>

<style lang="scss" setup>
.nav-container {
    background: rgba(255, 255, 255, 0.64);
    border: 0.5px solid rgba(0, 0, 0, 0.12);
    border-radius: 50rem;
    backdrop-filter: blur(21.350000381469727px);
    
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translate(-50%, -50%);
    
    width: 90%;
    height: 3.5rem;

    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box;
    padding: 2rem 3rem;
}

</style>