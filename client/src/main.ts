import { createApp } from 'vue'
import './styles/style.scss'
import App from './App.vue'
import router from './router'
import storageService from './services/storage-service';
import { REFRESH_TOKEN_CHEKING_INTERVAL } from './shared/constants';
import authenticationService from './services/authentication-service';

const app = createApp(App);

const tokenCheck = async () => {
    if (!storageService.retrieveAccessToken()) {
      return;
    }
    
    const expiration = new Date(Number(storageService.retrieveTokenExpiresDate()));
    const now = new Date( Date.now() + REFRESH_TOKEN_CHEKING_INTERVAL);
    
    if (expiration! < now) {
      await authenticationService.renewToken(storageService.retrieveAccessToken()!, storageService.retrieveRefreshToken()!).then((response) => {
        storageService.saveAccessToken(response.data.access);
        storageService.saveRefreshToken(response.data.refresh);
        storageService.saveTokenExpiresDate((Date.now() + 29 * 60000).toString());
        return response;
      }, (error) => {
        storageService.deleteUserData();
        // Should redirect to login page
        console.log(error);
      });
    }
  }
  
  await tokenCheck();
  setInterval(tokenCheck, REFRESH_TOKEN_CHEKING_INTERVAL);
  
app.use(router);
app.mount('#app')
