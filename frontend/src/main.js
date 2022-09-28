import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://127.0.0.1:8000'
axios.interceptors.response.use(
  (response) => response,
  async (error) => {
    const status = error?.response?.status;
    if (status === 401) {
      await refreshToken(store);
      error.config.headers[
        "Authorization"
      ] = `Bearer ${store.state.auth.token}`;
      error.config.baseURL = undefined;
      return axios.request(error.config);
    }
    return Promise.reject(error);
  }
);

createApp(App).config.productionTip = false


createApp(App).use(store).use(router).mount('#app')
