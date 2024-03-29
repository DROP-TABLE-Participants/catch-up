<template>
    <div class="product-card">
        <div class="title-container">
            <h2 class="title">{{ title }}</h2>
            <img class="arrow" src="arrow.png" alt="Arrow" />
        </div>
        <div class="round-div">
            <p class="round-text">{{ roundText }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProductCardComponent',
    props: {
        title: {
            type: String,
            required: true
        },
        roundText: {
            type: String,
            required: true
        }
    }
}
</script>

<style scoped>
.product-card {
    
}

.title-container {
    /* Add your styles for the title container here */
}

.title {
    /* Add your styles for the title here */
}

.arrow {
    /* Add your styles for the arrow image here */
}

.round-div {
    /* Add your styles for the round div here */
}

.round-text {
    /* Add your styles for the round text here */
}
</style>