import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import Home from './views/Home.vue'
import Rules from './views/Rules.vue'

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

const app = createApp(App)
app.use(router)
app.mount('#app')
