import { useContext } from "react";
import { Outlet } from "react-router-dom";
import { ThemeProvider } from "styled-components";
import { QueryClient, QueryClientProvider } from "react-query";

import Header from "./components/headers";
import GlobalStyle from "./styles/GolbalStyle";
import { darkTheme, lightTheme } from "./styles/themes/theme";
import { ThemeContext } from "./context/ThemesContext";

/* eslint-disable @typescript-eslint/no-unused-vars */
interface Users {
  id: number;
  username: string;
  login?: string;
  password: string;
  email: string;
  active: boolean;
}
const queryClient = new QueryClient();

/* eslint-disable react/react-in-jsx-scope */
const App = () => {
  const { theme } = useContext(ThemeContext);
  const themeMode = theme === "dark" ? darkTheme : lightTheme;
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={themeMode}>
        <Header />
        <Outlet />
        <GlobalStyle />
      </ThemeProvider>
    </QueryClientProvider>
  );
};

export default App;
