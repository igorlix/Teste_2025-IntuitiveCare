import './assets/css/main.css'
import axios from 'axios';

axios.defaults.baseURL = 'http://192.168.0.14:8000';
axios.defaults.headers.common['Accept'] = 'application/json';
axios.defaults.headers.common['Content-Type'] = 'application/json';

import { createApp } from 'vue'
import App from './App.vue'
import { Icon } from '@iconify/vue';


const app = createApp(App)
app.component('IconifyIcon', Icon);
app.mount('#app')
