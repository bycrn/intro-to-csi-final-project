import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import Home from './views/Home.vue'
import Rules from './views/Rules.vue'

import './firebase/config.js' 

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/rules',
      name: 'Rules',
      component: Rules
    }
  ]
})

const vueApp = createApp(App)  // Renommé pour éviter conflit
vueApp.use(router)
vueApp.mount('#app')
