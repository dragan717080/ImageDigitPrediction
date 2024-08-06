/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#006DAD',
          foreground: '#0073B7'
        },
        secondary: {
          DEFAULT: '#ECECEC',
        }
      },
      fontFamily: {
        sans: ['Inter', 'Roboto', 'Helvetica Neue', 'Arial', 'Noto Sans', 'sans-serif'],
      },
      spacing: {
        '1/5': '20%',
      }
    },
  },
  plugins: [],
}
