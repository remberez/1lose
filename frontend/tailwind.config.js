export default {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,html}",
  ],
  theme: {
    extend: {
      container: {
        center: true
      },
      colors: {
        oneWinBlue: {
          DEFAULT: '#1e283f',
          50: '#e6e8ed',
          100: '#c2c6d3',
          200: '#9da3b8',
          300: '#79809e',
          400: '#545e83',
          500: '#1e283f',
          600: '#181f32',
          700: '#121725',
          800: '#0c0e18',
          900: '#06060c',
        },        
        oneWinBrandBlue: {
          DEFAULT: '#00A3FF',
          100: '#e0f6ff',
          200: '#b8e7ff',
          300: '#8fd8ff',
          400: '#66c9ff',
          500: '#00A3FF',
          600: '#0084cc',
          700: '#006699',
          800: '#004766',
          900: '#002933',
        },
      },
      fontFamily: {
        inter: ["Inter", "sans-serif"]
      }
    },
  },
  plugins: [],
}

