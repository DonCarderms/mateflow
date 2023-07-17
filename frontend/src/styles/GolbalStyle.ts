import { createGlobalStyle } from "styled-components";
import { ThemeProps } from "./themes/theme";


export type GlobalThemeProps = {
  theme: ThemeProps;
};

const GlobalStyle = createGlobalStyle`

:root {
  //dark-mode
  --dark-background: #1a1a1a;
  --dark-text: #F5F5F7;

  //light-mode
  --light-background: #f2f2f2;
  --light-text: #2E0509;
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;
    
  outline: none;
  list-style: none;
  text-decoration: none;

  color-scheme: light dark;
  color:  ${({ theme }: GlobalThemeProps) => theme.text};
  background-color:  ${({ theme }: GlobalThemeProps) => theme.background};

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}
a {
  font-weight: 500;
  color: #646cff;
  text-decoration: inherit;
}
a:hover {
  color: #535bf2;
}

body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
}
h1 {
  font-size: 3.375rem;
  color: ${({ theme }: GlobalThemeProps) => theme.text};
  line-height: 1.1;
}

button {
  border-radius: 8px;
  border: 1px solid transparent;
  padding: 0.6em 1.2em;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  /* background-color: #1a1a1a; */
  cursor: pointer;
  transition: border-color 0.25s;
}
button:hover {
  border-color: #646cff;
}
button:focus,
button:focus-visible {
  outline: 4px auto -webkit-focus-ring-color;
}

@media (prefers-color-scheme: light) {
  :root {
    color: #213547;
    background-color: #ffffff;
  }
  a:hover {
    color: #747bff;
  }
  button, input {
    cursor: pointer;
    border: none;
  }
}

`
export default GlobalStyle;