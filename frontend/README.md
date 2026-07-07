# ⚡ Modern React + TypeScript + Vite Starter

A streamlined starter template for building modern web applications with **React**, **TypeScript**, and **Vite**. It offers a fast development workflow, clean project structure, and a solid foundation for scalable applications.

---

## ✨ Highlights

- ⚛️ React with TypeScript
- ⚡ Vite for lightning-fast builds and development
- 🔥 Hot Module Replacement (HMR)
- ✅ ESLint preconfigured for better code quality
- 📦 Easy to extend and customize
- 🚀 Optimized development experience

---

## 🛠 Available React Plugins

You can choose either of the official React plugins depending on your workflow:

- **@vitejs/plugin-react** — Powered by the Oxc compiler for fast development.
- **@vitejs/plugin-react-swc** — Uses SWC for high-performance compilation.

---

## ⚙ React Compiler

This template keeps the React Compiler disabled by default to ensure fast development and build times. If your project requires it, you can enable it later by following the official React documentation.

---

## 🧹 Improving ESLint

For production applications, it's recommended to enable type-aware linting for stronger TypeScript checks.

```js
export default defineConfig([
  globalIgnores(["dist"]),
  {
    files: ["**/*.{ts,tsx}"],
    extends: [
      tseslint.configs.recommendedTypeChecked,
      tseslint.configs.strictTypeChecked,
      tseslint.configs.stylisticTypeChecked,
    ],
    languageOptions: {
      parserOptions: {
        project: ["./tsconfig.node.json", "./tsconfig.app.json"],
        tsconfigRootDir: import.meta.dirname,
      },
    },
  },
]);
```

---

## ⚛ Additional React Lint Rules

For even better React development, consider installing:

- eslint-plugin-react-x
- eslint-plugin-react-dom

Example configuration:

```js
import reactX from "eslint-plugin-react-x";
import reactDom from "eslint-plugin-react-dom";

export default defineConfig([
  globalIgnores(["dist"]),
  {
    files: ["**/*.{ts,tsx}"],
    extends: [
      reactX.configs["recommended-typescript"],
      reactDom.configs.recommended,
    ],
  },
]);
```

---

## 📂 Suggested Project Structure

```
src/
├── assets/
├── components/
├── hooks/
├── layouts/
├── pages/
├── services/
├── store/
├── styles/
├── utils/
├── App.tsx
└── main.tsx
```

---

## 🚀 Getting Started

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Build for production:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

---

## 📖 Resources

- React Documentation
- TypeScript Documentation
- Vite Documentation
- ESLint Documentation


