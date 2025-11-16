import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'
import {defineConfig, globalIgnores} from 'eslint/config'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      js.configs.recommended,
      tseslint.configs.recommended,
      reactHooks.configs['recommended-latest'],
      reactRefresh.configs.vite,
    ],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    rules: {
      '@typescript-eslint/ban-types': 'off', // Отключаем запрет базовых типов
      '@typescript-eslint/explicit-module-boundary-types': 'off', // Отключаем требование экспорта типов
      '@typescript-eslint/prefer-readonly-parameter-types': 'off', // Отключаем предупреждение о readonly параметрах
      '@typescript-eslint/restrict-template-expressions': 'off', // Отключаем ограничения на шаблоны строк
      '@typescript-eslint/unbound-method': 'off', // Отключаем предупреждения о необъявленных методах
      // '@typescript-eslint/no-extraneous-class': 'off',

    }
  },
])






