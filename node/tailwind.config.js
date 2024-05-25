/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../sheldon_site/templates/**/*.html',
    '../sheldon_site/static/**/*.js',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      screens: {
        'nav-limit': '1050px',
        // => @media (min-width: 1024px) { ... }
      },
      colors: {
        // Define your custom colors here
        'uci-blue-dk': '#1C3D6E',
        'uci-blue-lt': '#0369a1',
        'uci-white': '#fafafa',
        'uci-yellow': '#facc15',
        // Add more custom colors as needed
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
