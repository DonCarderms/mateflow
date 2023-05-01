/* eslint-disable react/react-in-jsx-scope */

import { Home } from "../pages/Home";
import Cadastro from "../pages/cadastro/Cadastro";
import Login from "../pages/login";

import { createBrowserRouter } from "react-router-dom";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },

  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/cadastro",
    element: <Cadastro />,
    // children: [
    //   {
    //     path: "/",
    //     element: <App />,
    //   },
    // ],
  },
]);
