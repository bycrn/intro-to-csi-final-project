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
:root {
  /* Couleurs  */
  --dry-sage: #bdbd9b;      
  --ash-brown: #6C584C;      
  --black-forest: #283618;           /* Vert très foncé (texte) */
  --vanilla: rgb(240,234,210); 
  
  /* Couleurs système */
  --color-shadow: #283618; /* black forest en ombre */
  --faded-copper: #A98467;  
  --burnt-peach: #E07A5F;
  
  /* Espacements */
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--dry-sage);
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
  background: var(--vanilla);
  box-shadow: 0 2px 10px var(--color-shadow);
  padding: var(--spacing-md) 0;
}

.app-header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--black-forest);
}

nav {
  display: flex;
  gap: var(--spacing-lg);
}

.nav-link {
  color: var(--black-forest);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.nav-link:hover,
.nav-link.router-link-active {
  color: var(--ash-brown);
}

.app-main {
  flex: 1;
  padding: var(--spacing-xl) 0;
}

.app-footer {
  background: var(--ash-brown);
  color: var(--vanilla);
  text-align: center;
  padding: var(--spacing-lg);
}

.app-footer .small {
  font-size: 0.875rem;
  opacity: 0.8;
  margin-top: var(--spacing-sm);
}

@media (max-width: 768px) {
  .app-header .container {
    flex-direction: column;
    gap: var(--spacing-md);
  }
  
  .logo {
    font-size: 1.25rem;
  }
  
  nav {
    gap: var(--spacing-md);
  }
}
</style>
