import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: '/',  // ← CRUCIAL pour Render/GitHub Pages
  build: {
    outDir: 'dist',  // ← Génère dist/
    emptyOutDir: true
  }
})
