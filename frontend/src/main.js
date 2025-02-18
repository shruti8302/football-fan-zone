import { createApp } from 'vue';
import { Quasar } from 'quasar';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';

import 'quasar/dist/quasar.css';

const app = createApp(App);
app.use(Quasar);
app.use(router);
app.use(createPinia());
app.mount('#app');
