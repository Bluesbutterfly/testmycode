import './assets/main.css'

import { createApp } from 'vue'
import TDesign from 'tdesign-vue-next';
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// 引入组件库的少量全局样式变量
import 'tdesign-vue-next/es/style/index.css';

// pinia持久化
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
const app = createApp(App)

app.use(TDesign);
app.use(createPinia())
app.use(router)

app.mount('#app')
