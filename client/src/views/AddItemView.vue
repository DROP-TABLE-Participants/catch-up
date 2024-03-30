<template>
    <div class="add-items-container">
        <header>
            <button class="add-items-container__back-button">
                <BackArrowIcon />
            </button>
            <h1 class="add-items-container__title">Add items</h1>
        </header>

        <section class="add-items-container__import-csv-section">
            <button @click="importCSV" class="add-items-container__import-csv-button">Import CSV</button>
            <p class="add-items-container__drop-file-text">Or drop a file</p>
        </section>

        <div class="middle__text">
            <p class="middle__text-text">or add manually</p>
        </div>

        <form @submit.prevent="submitForm" class="add-items-container__form">
            <section class="add-items-container__manual-add-section">
                <div class="add-items-container__form-group">
                    <label for="itemName" class="add-items-container__label">Item Name</label>
                    <input type="text" id="itemName" v-model="itemName" placeholder="Name" class="add-items-container__input">
                </div>

                <div class="add-items-container__form-group">
                    <label for="itemName" class="add-items-container__label">Image</label>
                    <input type="file" id="imageUpload" @change="handleFileUpload" class="add-items-container__file-input" placeholder="Upload a file">
                    <label for="imageUpload" class="add-items-container__label--upload">Upload a file</label>
                </div>


                <button type="submit" class="add-items-container__submit-button">Add Item</button>
            </section>
        </form>
    </div>
</template>

<script lang="ts" setup>
import BackArrowIcon from "../components/icons/BackArrowIcon.vue";
</script>

<style scoped lang="scss">
.add-items-container {
    display: flex;
    flex-direction: column;
    padding: 1rem;

    header {
        display: flex;
        align-items: center;
        margin-bottom: 2rem;

     

        .add-items-container__back-button {
            cursor: pointer;
           border: none;
           background: transparent;
        }

        .add-items-container__title {
            padding-left: 1rem;
            font-size: 2rem;
            font-family: "Hanken Grotesk";
        }


    }

    .add-items-container__import-csv-section {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        justify-content: center;
        align-items: center;
        margin-bottom: 2rem;
        border-radius: 17px;
        border: 1px solid #C8C0C0;
        padding: 1rem 0rem;

        .add-items-container__import-csv-button {
            border: 1px solid #216DFF;
            background-color: #216DFF;
            color: white;
            font-size: 10px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: .5rem 1rem; 
            border-radius: 1.5rem;
            
        }

        .add-items-container__drop-file-text {
            color: #585858;
            font-family: Inter;
            font-size: 0.62rem;
        }
    }



    .add-items-container__form {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;

        .add-items-container__manual-add-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;

            .add-items-container__form-group {
                width: 90%;
                display: flex;
                flex-direction: column;
                margin-bottom: 1rem;

                .add-items-container__label {
                    font-size: 1rem;
                    margin-bottom: 0.5rem;
                    margin-left: 0.5rem;

                    &--upload {
                        font-size: 1rem;
                        margin-bottom: 0.5rem;
                        padding: 1rem;
                        display: inline-block;
                        border: 1px solid #CFCFCF;
                        border-radius: 0.7rem;
                        width: 100%; 
                        text-align: center;
                        cursor: pointer;
                        background-color: #fff; 
                        color: #9C8888; 
                        box-sizing: border-box;
                        
                        
                }
            }

                .add-items-container__input {
                    box-sizing: border-box;
                    padding: 1rem;
                    font-size: 1rem;
                    border: 1px solid #CFCFCF;
                    border-radius: 0.7rem;
                    width: 100%;

                    &::placeholder {
                        color: #9C8888;
                    }
                }

                .add-items-container__file-input {
                    width: 0.1px;
                    height: 0.1px;
                    opacity: 0;
                    overflow: hidden;
                    position: absolute;
                    z-index: -1;
                    
                }
            }

            .add-items-container__submit-button {
                border: none;
                border-radius: 25px;
                background: #216DFF;
                color: white;
                cursor: pointer;    
                padding: 1rem 2.5rem;
                font-size: 17px;
                
            }
        }
    }
}

.middle__text{
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 1rem;
    font-size: 10px;
    color: #000;

    &-text{
        font-size: .8rem;
        font-family: Inter;
        color: #000;
        
    }
}
</style>
