<template>
  <div id="app">
    <header class="app-header">
      <div class="container">
        <h1 class="logo">♻️ 桃園垃圾分類</h1>
        <nav>
          <router-link to="/" class="nav-link">分類助手</router-link>
          <router-link to="/rules" class="nav-link">分類規則</router-link>
        </nav>
      </div>
    </header>
    
    <main class="app-main">
      <router-view></router-view>
    </main>
    
    <footer class="app-footer">
      <p>桃園市垃圾分類助手 | Taoyuan Waste Sorting Helper</p>
      <p class="small">幫助外國人了解台灣桃園的垃圾分類規則</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.app-header {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 1rem 0;
}

.app-header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: #333;
}

nav {
  display: flex;
  gap: 1.5rem;
}

.nav-link {
  color: #555;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.nav-link:hover,
.nav-link.router-link-active {
  color: #667eea;
}

.app-main {
  flex: 1;
  padding: 2rem 0;
}

.app-footer {
  background: rgba(0, 0, 0, 0.2);
  color: white;
  text-align: center;
  padding: 1.5rem;
}

.app-footer .small {
  font-size: 0.875rem;
  opacity: 0.8;
  margin-top: 0.5rem;
}

@media (max-width: 768px) {
  .app-header .container {
    flex-direction: column;
    gap: 1rem;
  }
  
  .logo {
    font-size: 1.25rem;
  }
  
  nav {
    gap: 1rem;
  }
}
</style>
