import { Outlet, RouterProvider } from "react-router-dom";
import { router } from "./routes/AppRoutes";
import Header from "./components/headers";

/* eslint-disable @typescript-eslint/no-unused-vars */
interface Users {
  id: number;
  username: string;
  login?: string;
  password: string;
  email: string;
  active: boolean;
}

/* eslint-disable react/react-in-jsx-scope */
const App = () => {
  return (
    <div>
      <Header />
      <RouterProvider router={router} />
      <Outlet />
    </div>
  );
};

export default App;
