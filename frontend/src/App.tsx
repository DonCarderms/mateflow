import { Outlet, RouterProvider } from "react-router-dom";
import { router } from "./routes/AppRoutes";
import Header from "./components/headers";
import { QueryClient, QueryClientProvider } from "react-query";

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
  return (
    <QueryClientProvider client={queryClient}>
      <Header />
      <RouterProvider router={router} />
      <Outlet />
    </QueryClientProvider>
  );
};

export default App;
