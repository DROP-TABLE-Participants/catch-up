<template>
    <div class="tag-container">
        <p>{{percentage}}</p>
        <!-- <IconUp v-if="isGrowthUp"/>
        <IconDown v-else/> -->
    </div>
</template>

<script lang="ts" setup>
import { defineProps } from 'vue';

const props = defineProps<{
    percentage: number,
    isGrowthUp: boolean,
}>();

</script>

<style lang="scss" scoped>
</style>