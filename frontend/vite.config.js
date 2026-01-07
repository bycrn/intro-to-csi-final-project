import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  base: '/',  // Changed from '/intro-to-csi-final-project/'
  build: {
    outDir: 'dist'  // Changed from '../dist'
  },
  server: {
    port: 5173,
    host: true
  }
})