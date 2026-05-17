import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  // Relative asset paths make the build work both at https://user.github.io/repo/
  // and when opened locally from the dist folder.
  base: './',
  plugins: [react()],
})
