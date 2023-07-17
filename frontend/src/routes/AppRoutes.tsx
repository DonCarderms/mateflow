/* eslint-disable react/react-in-jsx-scope */
import { Home } from "../pages/Home";
import Cadastro from "../pages/cadastro/Cadastro";

import { createBrowserRouter } from "react-router-dom";
import Login from "../pages/login";
import App from "../App";
import { T } from "../pages/materiais";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <>pagina não encontrada</>,
    children: [
      {
        path: "/",
        element: <Home />,
        children: [{ path: "op", element: <T /> }],
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/cadastro",
        element: <Cadastro />,
        children: [
          {
            path: "tr",
            element: <Cadastro />,
          },
        ],
      },
    ],
  },
]);
