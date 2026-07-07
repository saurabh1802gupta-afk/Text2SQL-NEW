import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    sourcemap: false, // Disables source maps in production for smaller file sizes
    rollupOptions: {
      output: {
        // Manually separates large libraries into their own files
        manualChunks(id) {
          if (id.includes('node_modules')) {
            if (id.includes('react')) return 'vendor-react';
            if (id.includes('axios')) return 'vendor-axios';
            return 'vendor'; // All other dependencies
          }
        }
      }
    }
  }
});
