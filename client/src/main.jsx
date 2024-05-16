import { RouterProvider, createBrowserRouter } from "react-router-dom";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import DailyPage from "./pages/DailyPage.jsx";
import Home from "./pages/Home.jsx";

const router = createBrowserRouter([
  {
    element: <App />,
    children: [
      {
        path: "/",
        element: <Home />,
        loader: () =>
          fetch("http://localhost:8000/")
            .then((res) => res.json())
            .then((postures) => postures.postures)
            .catch((error) => console.error(error)),
      },
      {
        path: "/:id",
        element: <DailyPage />,
        loader: ({ params }) =>
          fetch(`http://localhost:8000/`)
            .then((res) => res.json())
            .then((data) => data.postures[params.id-1])
            .catch((err) => console.error(err)),
      },
    ],
  },
]);

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<RouterProvider router={router} />);
