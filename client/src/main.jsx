import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import DailyPage from "./pages/DailyPage.jsx";
import Home from "./pages/Home.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    // loader: () =>
    //   fetch("")
    //     .then((res) => res.json())
    //     .then((data) => data)
    //     .catch((error) => console.error(error)),
    id: "app",
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/:id",
        element: <DailyPage />,
        // loader: ({ params }) =>
        //   fetch(`http://localhost:3310/api/cupcakes/${params.id}`)
        //     .then((res) => res.json())
        //     .then((data) => data)
        //     .catch((err) => console.error(err)),
      },
    ],
  },
]);

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
