import React from "react";
import { Redirect } from "react-router-dom";

// Layout Types
import { DefaultLayout } from "./layouts";

// Route Views
import Login from "./views/auth/Login";
import Register from "./views/auth/Register";
import Home from "./views/home/Home";

export default [
  {
    path: "/",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Home
  },
  {
    path: "/login",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Login
  },
  {
    path: "/register",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Register
  },
];
