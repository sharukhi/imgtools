import type { Config } from "tailwindcss";

export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  themes: [
    {
      theme: {},
    },
  ],
  daisyui: {
    themes: ["theme"],
  },
  plugins: [require("daisyui")],
} as Config;
