module.exports = {
  content: [
    "./application/templates/**/*.html", // Include all template files
    "./application/static/**/*.css", // Include your CSS files
    "./application/static/**/*.js", // Include JS files if using Tailwind classes in JS
  ],
  theme: {
    extend: {
      animation: {
        marquee: "marquee 30s linear infinite",
        marqueeFade: "marqueeFade 30s linear infinite",
      },
      keyframes: {
        marquee: {
          "0%": { transform: "translateX(100%)" },
          "100%": { transform: "translateX(-100%)" },
        },
        marqueeFade: {
          "0%": { transform: "translateX(100%)", opacity: "0" },
          "10%": { opacity: "1" },
          "90%": { opacity: "1" },
          "100%": { transform: "translateX(-100%)", opacity: "0" },
        },
      },
    },
  },
  plugins: [],
};
