<template>
    <div class="add-items-container">
        <header>
            <button class="add-items-container__back-button">&lt;</button>
            <h1 class="add-items-container__title">Add items</h1>
        </header>

        <section class="add-items-container__import-csv-section">
            <button @click="importCSV" class="add-items-container__import-csv-button">Import CSV</button>
            <p class="add-items-container__drop-file-text">Or drop a file</p>
        </section>

        <div class="middle-text">
            <p>or add manually</p>
        </div>

        <form @submit.prevent="submitForm" class="add-items-container__form">
            <section class="add-items-container__manual-add-section">
                <div class="add-items-container__form-group">
                    <label for="itemName" class="add-items-container__label">Item Name</label>
                    <input type="text" id="itemName" v-model="itemName" placeholder="name" class="add-items-container__input">
                </div>

                <div class="add-items-container__form-group">
                    <label for="imageUpload" class="add-items-container__label">Image</label>
                    <input type="file" id="imageUpload" @change="handleFileUpload" class="add-items-container__file-input">
                </div>

                <button type="submit" class="add-items-container__submit-button">Add Item</button>
            </section>
        </form>
    </div>
</template>

<script>

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

        h1 {
            padding-left: 1rem;
            font-family: "Hanken Grotesk", sans-serif;
            font-size: 1.5rem;
        }

        .add-items-container__back-button {
            border: 1px solid #CFCFCF;
            font-size: 1.5rem;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1rem;
            width: 2.5rem;
            height: 2.5rem;
            border-radius: 50%;
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
            padding: .5rem;
            border-radius: 25px;
            
        }

        .add-items-container__drop-file-text {
            font-size: 10px;
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
                }

                .add-items-container__input {
                    padding: 0.5rem;
                    font-size: 1rem;
                    border: 1px solid #CFCFCF;
                    border-radius: 5px;
                    width: 100%;
                }

                .add-items-container__file-input {
                    
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

.middle-text{
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 1rem;
    font-size: 10px;
    color: #000;
}
</style>
