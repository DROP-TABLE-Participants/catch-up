<script setup>
import { computed } from 'vue';

const props = defineProps({
  percentage: {
    type: Number,
    required: true
  }
})


const cssTransformRotateValue = computed(() => {
  const percentageAsFraction = props.percentage / 100
  const halfPercentage = percentageAsFraction / 2

  return `${halfPercentage}turn`
})

</script>

<template>
    <div class="gauge__outer">
      <div class="gauge__inner">
        <div class="gauge__segment gauge__very-negative"></div>
        <div class="gauge__segment gauge__negative"></div>
        <div class="gauge__segment gauge__positive"></div>
        <div class="gauge__segment gauge__very-positive"></div>
        <div class="" :style="{ transform: `rotate(${cssTransformRotateValue})` }"></div>
        <div class="gauge__arrow" :style="{ transform: `rotate(${cssTransformRotateValue})` }"></div>
        <div class="gauge__cover">
          0%
        </div>
      </div>
    </div>
    <div class="info">
      <p>Negative</p>
      <p>Positive</p>
    </div>
    <p class="percentage">
      {{ percentage.toFixed(0) }}%
    </p>
  </template>
  
  

<style scoped>

.gauge__arrow {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform-origin: 50% 100%;
  width: 4px; /* Adjust size as needed */
  height: 106px; /* Adjust size as needed */
  background: #1e1e1e; /* Color of the arrow */
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
  transition: transform 0.2s ease-out;
  z-index: 1 ;
}

.gauge__outer {
  width: 100%;
  max-width: 250px;
}

.gauge__inner {
  width: 100%;
  height: 0;
  padding-bottom: 50%;
  background: linear-gradient(45deg, #1a889e 0%, #10f175 100%);
  position: relative;
  border-top-left-radius: 100% 200%;
  border-top-right-radius: 100% 200%;
  overflow: hidden;
}

.gauge__fill {
  position: absolute;
  top: 100%;
  left: 0;
  width: inherit;
  height: 100%;
  background: #3741F2;
  transform-origin: center top;
  transform: rotate(0turn);
  transition: transform 0.2s ease-out;
}

.gauge__cover {
  width: 75%;
  height: 150%;
  background: #ffffff;
  position: absolute;
  top: 25%;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 50%;

  /* Text */
  display: flex;
  align-items: center;
  justify-content: center;
  padding-bottom: 65%;
  box-sizing: border-box;
  font-family: 'Hanken Grotesk', sans-serif;
  font-weight: bold;
  font-size: 14px;
}

 .info {
  display: flex;
  justify-content: space-between;
  gap: 150px;
  margin: 0 1rem;
}

.percentage {
  font-size: 1.7rem;
  text-align: center;
  font-weight: 500;
}

</style>
