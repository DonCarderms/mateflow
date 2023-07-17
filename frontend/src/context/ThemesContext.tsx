import { createContext, useEffect, useState } from "react";

export type ThemeContextType = {
  theme?: "ligth" | "dark";
  setChangeTheme?: () => void;
};

export const ThemeContext = createContext<ThemeContextType>({});

export type ThemeContextProviderType = {
  children: React.ReactNode;
};

export const ThemeContextProvider = ({
  children,
}: ThemeContextProviderType) => {
  const [theme, setTheme] = useState<"ligth" | "dark">("ligth");

  const setChangeTheme = (): void => {
    if (theme === "ligth") {
      setTheme("dark");
      return;
    }
    setTheme("ligth");
  };

  useEffect(() => {
    localStorage.setItem("theme", JSON.stringify({ theme }));
  }, [theme]);

  return (
    // eslint-disable-next-line react/react-in-jsx-scope
    <ThemeContext.Provider value={{ theme, setChangeTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
