module.exports = {
    content: [
        '../../templates/*.html',
        '../../templates/**/*.html', 
        '../../main/src/index-main.js',
        '../../**/templates/*.html',  
        '!../../**/node_modules',
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',
        // '../../**/*.py'
    ],
    plugins: [
        require('daisyui'),
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
    daisyui: {
        themes: [
          {
            mytheme: {
              "primary": "#FF4444",
              "secondary": "#334263",
              "accent": "#fa0000",
              "neutral": "#3d4451",
              "base-100": "#fffff8",
            },
          },
          "dark",
        ],
      },
      theme: {
        extend: {
          fontFamily: {
            'sans': ['nunito', 'sans-serif'],
          },
        },
      },
}
