/* eslint-disable quotes */
/* eslint-disable indent */
/* eslint-disable react/react-in-jsx-scope */
/* eslint-disable @typescript-eslint/no-unused-vars */
import React from "react";
import { Children, createContext } from "react";

interface User {
  nome: string;
  senha: string;
}

interface UserContextType {
  user: User;
}

interface UserContextProviderProps {
  children: React.ReactNode;
}
const UserContext = createContext<UserContextType | undefined>(undefined);

const UserContextProvider = ({ children }: UserContextProviderProps) => {
  const user: User = {
    nome: "oi",
    senha: "kkkk",
  };
  return (
    <UserContext.Provider value={{ user }}>{children}</UserContext.Provider>
  );
};
