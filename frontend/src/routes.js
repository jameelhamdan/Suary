import React from "react";

// Layout Types
import { DefaultLayout } from "layouts";

// Route Views
import Login from "views/auth/Login";
import Logout from "views/auth/Logout";
import Register from "views/auth/Register";
import Home from "views/home/Home";

//Users
import UserDetail from "views/user/Detail"


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
  {
    path: "/logout",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Logout
  },
  {
    path: "/profile/:username",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: UserDetail
  },
];
