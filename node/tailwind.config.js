/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../project_container/templates/**/*.html',
    '../project_container/static/**/*.js',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      fontFamily: {
        'body': [
      'Inter', 
      'ui-sans-serif', 
      'system-ui', 
      '-apple-system', 
      'system-ui', 
      'Segoe UI', 
      'Roboto', 
      'Helvetica Neue', 
      'Arial', 
      'Noto Sans', 
      'sans-serif', 
      'Apple Color Emoji', 
      'Segoe UI Emoji', 
      'Segoe UI Symbol', 
      'Noto Color Emoji'
    ],
        'sans': [
      'Inter', 
      'ui-sans-serif', 
      'system-ui', 
      '-apple-system', 
      'system-ui', 
      'Segoe UI', 
      'Roboto', 
      'Helvetica Neue', 
      'Arial', 
      'Noto Sans', 
      'sans-serif', 
      'Apple Color Emoji', 
      'Segoe UI Emoji', 
      'Segoe UI Symbol', 
      'Noto Color Emoji'
    ]
      },
      screens: {
        'nav-limit': '1050px',
        'footer-limit': '767px',
        // => @media (min-width: 1024px) { ... }
      },
      colors: {
        // Define your custom colors here
        'uci-blue-dk': '#1C3D6E',
        'uci-blue-lt': '#0369a1',
        'uci-white': '#fafafa',
        'uci-yellow': '#facc15',
        primary: {"50":"#eff6ff","100":"#dbeafe","200":"#bfdbfe","300":"#93c5fd","400":"#60a5fa","500":"#3b82f6","600":"#2563eb","700":"#1d4ed8","800":"#1e40af","900":"#1e3a8a","950":"#172554"}
        // Add more custom colors as needed
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
