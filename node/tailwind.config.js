/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../sheldon_site/templates/**/*.html',
    '../sheldon_site/node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

